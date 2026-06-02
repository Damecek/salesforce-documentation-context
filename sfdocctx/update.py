from __future__ import annotations

import asyncio
import json
import os
import shutil
import ssl
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import httpx


def _build_ssl_context() -> ssl.SSLContext:
    """Verify TLS using the OS trust store when possible.

    Some Salesforce hosts (e.g. resources.docs.salesforce.com) serve an
    incomplete certificate chain (leaf only, missing the DigiCert
    intermediate). certifi has only roots and Python does not chase AIA, so
    verification fails. The native macOS/Windows verifier fetches the missing
    intermediate, so prefer truststore and fall back to the default context.
    """
    try:
        import truststore

        return truststore.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    except Exception:
        return ssl.create_default_context()

from .docs import list_markdown_docs
from .fsutil import ensure_dir, safe_join_under, write_text_atomic
from .github import detect_github_raw_config
from .hashing import sha256_hex, sha256_hex_text
from .llms import LlmsDocLink, build_llms_txt
from .pdf import pdf_to_markdown
from .src_list import SrcEntry, parse_src_txt


@dataclass
class _CacheMeta:
    etag: str | None = None
    last_modified: str | None = None
    sha256: str | None = None


def run_update(
    *,
    src_file: str,
    docs_dir: str,
    cache_dir: str,
    concurrency: int,
    force: bool,
    github_raw_base: str | None,
    github_raw_branch: str | None,
    http_timeout_s: float,
    max_md_bytes: int,
) -> int:
    concurrency = concurrency if concurrency and concurrency > 0 else 4
    max_md_bytes = max(max_md_bytes, 1)

    src_path = Path(src_file)
    contents = src_path.read_text(encoding="utf-8") if src_path.exists() else ""
    try:
        entries = parse_src_txt(contents) if contents.strip() else []
    except Exception as e:
        sys.stderr.write(f"Invalid {src_file}: {e}\n")
        return 2

    if force:
        _clear_docs_dir(docs_dir)
    ensure_dir(docs_dir)
    ensure_dir(cache_dir)

    exit_code = asyncio.run(
        _run_update_async(
            entries=entries,
            docs_dir=docs_dir,
            cache_dir=cache_dir,
            concurrency=concurrency,
            force=force,
            github_raw_base=github_raw_base,
            github_raw_branch=github_raw_branch,
            http_timeout_s=http_timeout_s,
            max_md_bytes=max_md_bytes,
        )
    )
    return exit_code


async def _run_update_async(
    *,
    entries: list[SrcEntry],
    docs_dir: str,
    cache_dir: str,
    concurrency: int,
    force: bool,
    github_raw_base: str | None,
    github_raw_branch: str | None,
    http_timeout_s: float,
    max_md_bytes: int,
) -> int:
    failures: list[tuple[str, str]] = []

    timeout = httpx.Timeout(http_timeout_s)
    limits = httpx.Limits(max_connections=concurrency, max_keepalive_connections=concurrency)
    ssl_context = _build_ssl_context()
    async with httpx.AsyncClient(
        timeout=timeout, follow_redirects=True, limits=limits, verify=ssl_context
    ) as client:
        sem = asyncio.Semaphore(concurrency)

        async def worker(entry: SrcEntry) -> None:
            async with sem:
                try:
                    await _process_entry(
                        client=client,
                        entry=entry,
                        docs_dir=docs_dir,
                        cache_dir=cache_dir,
                        force=force,
                        max_md_bytes=max_md_bytes,
                    )
                except Exception as e:
                    failures.append((entry.url, str(e)))
                    sys.stderr.write(f"✗ {entry.url}\n  {e}\n")

        await asyncio.gather(*(worker(e) for e in entries))

    await _write_llms_txt(
        docs_dir=docs_dir,
        github_raw_base=github_raw_base,
        github_raw_branch=github_raw_branch,
    )

    return 1 if failures else 0


async def _process_entry(
    *,
    client: httpx.AsyncClient,
    entry: SrcEntry,
    docs_dir: str,
    cache_dir: str,
    force: bool,
    max_md_bytes: int,
) -> None:
    out_abs = safe_join_under(docs_dir, entry.out_file)
    out_file_url = entry.out_file.replace("\\", "/")
    out_rel = f"{_path_for_urls(docs_dir).rstrip('/')}/{out_file_url}"

    fetched_at_iso = _iso_now()
    pdf_bytes, changed = await _fetch_pdf_with_cache(client=client, url=entry.url, cache_dir=cache_dir)

    if not force and not changed and _output_exists(out_abs):
        sys.stdout.write(f"= {title_from_entry(entry)} (unchanged) -> {out_rel}\n")
        return

    md = pdf_to_markdown(
        pdf_bytes=pdf_bytes,
        title=title_from_entry(entry),
        source_url=entry.url,
        fetched_at_iso=fetched_at_iso,
    )
    written_paths = _write_markdown_outputs(base_abs=out_abs, markdown=md, max_md_bytes=max_md_bytes)
    if len(written_paths) == 1:
        sys.stdout.write(f"✓ {title_from_entry(entry)} -> {out_rel}\n")
    else:
        sys.stdout.write(f"✓ {title_from_entry(entry)} -> {out_rel} (split into {len(written_paths)} parts)\n")


def title_from_entry(entry: SrcEntry) -> str:
    if entry.title:
        return entry.title
    base = Path(entry.out_file).name
    base = base[:-3] if base.lower().endswith(".md") else base
    title = base.replace("-", " ").replace("_", " ").strip()
    return title[:1].upper() + title[1:] if title else "Document"


async def _fetch_pdf_with_cache(
    *, client: httpx.AsyncClient, url: str, cache_dir: str
) -> tuple[bytes, bool]:
    ensure_dir(cache_dir)
    key = sha256_hex_text(url)[:24]
    pdf_path = Path(cache_dir) / f"{key}.pdf"
    meta_path = Path(cache_dir) / f"{key}.json"

    prev_meta = _read_cache_meta(meta_path)

    headers: dict[str, str] = {}
    if prev_meta.etag:
        headers["If-None-Match"] = prev_meta.etag
    if prev_meta.last_modified:
        headers["If-Modified-Since"] = prev_meta.last_modified

    res = await client.get(url, headers=headers)
    if res.status_code == 304:
        if pdf_path.exists():
            return pdf_path.read_bytes(), False
        res = await client.get(url)

    if res.status_code < 200 or res.status_code >= 300:
        raise RuntimeError(f"Failed to download PDF ({res.status_code} {res.reason_phrase}): {url}")

    pdf_bytes = res.content
    sha = sha256_hex(pdf_bytes)
    changed = sha != (prev_meta.sha256 or "")

    pdf_path.write_bytes(pdf_bytes)
    next_meta = _CacheMeta(
        etag=res.headers.get("etag"),
        last_modified=res.headers.get("last-modified"),
        sha256=sha,
    )
    meta_path.write_text(json.dumps(next_meta.__dict__, indent=2, sort_keys=True), encoding="utf-8")
    return pdf_bytes, changed


def _read_cache_meta(meta_path: Path) -> _CacheMeta:
    if not meta_path.exists():
        return _CacheMeta()
    try:
        data: Any = json.loads(meta_path.read_text(encoding="utf-8"))
        return _CacheMeta(
            etag=data.get("etag"),
            last_modified=data.get("last_modified") or data.get("lastModified"),
            sha256=data.get("sha256"),
        )
    except Exception:
        return _CacheMeta()


async def _write_llms_txt(
    *, docs_dir: str, github_raw_base: str | None, github_raw_branch: str | None
) -> None:
    detected = detect_github_raw_config()
    raw_base = github_raw_base or detected.raw_base_url
    if raw_base and github_raw_branch:
        raw_base = "/".join(raw_base.rstrip("/").split("/")[:-1] + [github_raw_branch])

    docs_on_disk = list_markdown_docs(docs_dir)
    links: list[LlmsDocLink] = []
    for doc in docs_on_disk:
        out_rel = f"{_path_for_urls(docs_dir).rstrip('/')}/{doc.rel_path}"
        raw_url = f"{raw_base.rstrip('/')}/{out_rel}" if raw_base else out_rel
        links.append(LlmsDocLink(title=doc.title, raw_url=raw_url))

    write_text_atomic("llms.txt", build_llms_txt(links))


def _iso_now() -> str:
    import datetime as dt

    return dt.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"


def _path_for_urls(path: str) -> str:
    p = Path(path)
    try:
        rel = p.resolve().relative_to(Path.cwd().resolve())
        return rel.as_posix()
    except Exception:
        return p.as_posix()


def _clear_docs_dir(docs_dir: str) -> None:
    root = Path(docs_dir)
    if not root.exists():
        return
    for child in root.iterdir():
        if child.is_dir():
            shutil.rmtree(child)
        else:
            child.unlink()


def _output_exists(base_abs: Path) -> bool:
    if base_abs.exists():
        return True
    return any(_iter_part_paths(base_abs))


def _iter_part_paths(base_abs: Path):
    stem, suffix = base_abs.stem, base_abs.suffix
    yield from base_abs.parent.glob(f"{stem}-part-*{suffix}")


def _remove_output_variants(base_abs: Path) -> None:
    if base_abs.exists():
        base_abs.unlink()
    for part in _iter_part_paths(base_abs):
        if part.exists():
            part.unlink()


def _write_markdown_outputs(*, base_abs: Path, markdown: str, max_md_bytes: int) -> list[str]:
    chunks = _split_markdown_by_size(markdown, max_md_bytes=max_md_bytes)
    _remove_output_variants(base_abs)

    if len(chunks) == 1:
        write_text_atomic(base_abs, chunks[0])
        return [base_abs.name]

    written: list[str] = []
    width = max(2, len(str(len(chunks))))
    for i, chunk in enumerate(chunks, start=1):
        part_name = f"{base_abs.stem}-part-{str(i).zfill(width)}{base_abs.suffix}"
        part_path = base_abs.with_name(part_name)
        write_text_atomic(part_path, chunk)
        written.append(part_path.name)
    return written


def _split_markdown_by_size(text: str, *, max_md_bytes: int) -> list[str]:
    if len(text.encode("utf-8")) <= max_md_bytes:
        return [text]

    chunks: list[str] = []
    current: list[str] = []
    current_bytes = 0

    def flush() -> None:
        nonlocal current, current_bytes
        if current:
            chunks.append("".join(current))
            current = []
            current_bytes = 0

    for line in text.splitlines(keepends=True):
        line_bytes = len(line.encode("utf-8"))
        if line_bytes > max_md_bytes:
            flush()
            for line_part in _split_oversized_text(line, max_md_bytes=max_md_bytes):
                chunks.append(line_part)
            continue

        if current and current_bytes + line_bytes > max_md_bytes:
            flush()
        current.append(line)
        current_bytes += line_bytes

    flush()
    return chunks if chunks else [text]


def _split_oversized_text(text: str, *, max_md_bytes: int) -> list[str]:
    parts: list[str] = []
    current: list[str] = []
    current_bytes = 0

    for ch in text:
        ch_bytes = len(ch.encode("utf-8"))
        if current and current_bytes + ch_bytes > max_md_bytes:
            parts.append("".join(current))
            current = []
            current_bytes = 0
        current.append(ch)
        current_bytes += ch_bytes

    if current:
        parts.append("".join(current))
    return parts if parts else [text]
