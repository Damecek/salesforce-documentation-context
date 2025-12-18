from __future__ import annotations

import asyncio
import json
import os
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import httpx

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
) -> int:
    concurrency = concurrency if concurrency and concurrency > 0 else 4

    src_path = Path(src_file)
    contents = src_path.read_text(encoding="utf-8") if src_path.exists() else ""
    try:
        entries = parse_src_txt(contents) if contents.strip() else []
    except Exception as e:
        sys.stderr.write(f"Invalid {src_file}: {e}\n")
        return 2

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
) -> int:
    failures: list[tuple[str, str]] = []

    timeout = httpx.Timeout(http_timeout_s)
    limits = httpx.Limits(max_connections=concurrency, max_keepalive_connections=concurrency)
    async with httpx.AsyncClient(timeout=timeout, follow_redirects=True, limits=limits) as client:
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
) -> None:
    out_abs = safe_join_under(docs_dir, entry.out_file)
    out_file_url = entry.out_file.replace("\\", "/")
    out_rel = f"{_path_for_urls(docs_dir).rstrip('/')}/{out_file_url}"

    fetched_at_iso = _iso_now()
    pdf_bytes, changed = await _fetch_pdf_with_cache(client=client, url=entry.url, cache_dir=cache_dir)

    if not force and not changed and out_abs.exists():
        sys.stdout.write(f"= {title_from_entry(entry)} (unchanged) -> {out_rel}\n")
        return

    md = pdf_to_markdown(
        pdf_bytes=pdf_bytes,
        title=title_from_entry(entry),
        source_url=entry.url,
        fetched_at_iso=fetched_at_iso,
    )
    write_text_atomic(out_abs, md)
    sys.stdout.write(f"✓ {title_from_entry(entry)} -> {out_rel}\n")


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
