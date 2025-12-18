from __future__ import annotations

import re
from dataclasses import dataclass
from urllib.parse import urlparse


@dataclass(frozen=True)
class SrcEntry:
    url: str
    title: str | None
    out_file: str


_SLUG_RE = re.compile(r"[^a-z0-9]+")


def parse_src_txt(contents: str) -> list[SrcEntry]:
    entries: list[SrcEntry] = []

    for raw_line in contents.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue

        if "|" in line:
            parts = [p.strip() for p in line.split("|")]
            parts = [p for p in parts if p]
            if len(parts) < 2 or len(parts) > 3:
                raise ValueError(
                    f"Invalid src.txt line (expected 2-3 parts separated by '|'): {raw_line}"
                )

            a, b = parts[0], parts[1]
            c = parts[2] if len(parts) == 3 else None

            if _is_http_url(a):
                url = a
                out_file = c or b
                title = None
            elif _is_http_url(b):
                title = a
                url = b
                out_file = c
            else:
                raise ValueError(f"Invalid src.txt line (could not detect URL): {raw_line}")

            out_file = _normalize_out_file(out_file or _default_out_file(title, url))
            entries.append(SrcEntry(url=url, title=title, out_file=out_file))
            continue

        tokens = line.split()
        url = tokens[0] if tokens else ""
        if not _is_http_url(url):
            raise ValueError(f"Invalid URL in src.txt: {raw_line}")
        out_file = " ".join(tokens[1:]).strip() if len(tokens) > 1 else ""
        out_file = _normalize_out_file(out_file or _default_out_file(None, url))
        entries.append(SrcEntry(url=url, title=None, out_file=out_file))

    return entries


def _is_http_url(value: str) -> bool:
    try:
        parsed = urlparse(value)
        return parsed.scheme in {"http", "https"} and bool(parsed.netloc)
    except Exception:
        return False


def _slugify(value: str) -> str:
    v = value.strip().lower()
    v = v.replace("'", "").replace('"', "")
    v = _SLUG_RE.sub("-", v).strip("-")
    return v[:80]


def _default_out_file(title: str | None, url: str) -> str:
    base = "document"
    try:
        path = urlparse(url).path or ""
        m = re.search(r"([^/]+)$", path)
        if m:
            base = re.sub(r"\.pdf$", "", m.group(1), flags=re.IGNORECASE) or base
    except Exception:
        base = "document"

    slug = _slugify(title or base) or _slugify(base) or "document"
    return f"{slug}.md"


def _normalize_out_file(out_file: str) -> str:
    trimmed = out_file.strip()
    if not trimmed:
        return "document.md"
    return trimmed if trimmed.lower().endswith(".md") else f"{trimmed}.md"

