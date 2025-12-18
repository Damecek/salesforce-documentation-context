from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class MarkdownDoc:
    rel_path: str
    title: str


_H1_RE = re.compile(r"^#\s+(.+?)\s*$")


def list_markdown_docs(docs_dir: str | Path) -> list[MarkdownDoc]:
    root = Path(docs_dir)
    if not root.exists():
        return []

    docs: list[MarkdownDoc] = []
    for path in sorted(root.rglob("*.md")):
        if not path.is_file():
            continue
        rel = path.relative_to(root).as_posix()
        title = _title_from_markdown(path)
        docs.append(MarkdownDoc(rel_path=rel, title=title))
    return docs


def _title_from_markdown(path: Path) -> str:
    try:
        with path.open("r", encoding="utf-8") as f:
            for line in f:
                m = _H1_RE.match(line.rstrip("\n"))
                if m:
                    return m.group(1).strip()
    except Exception:
        pass

    base = path.stem.replace("-", " ").replace("_", " ").strip()
    return base[:1].upper() + base[1:] if base else "Document"

