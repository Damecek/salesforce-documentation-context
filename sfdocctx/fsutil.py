from __future__ import annotations

import os
import tempfile
from pathlib import Path


def ensure_dir(path: str | Path) -> None:
    Path(path).mkdir(parents=True, exist_ok=True)


def read_text_if_exists(path: str | Path) -> str | None:
    p = Path(path)
    if not p.exists():
        return None
    return p.read_text(encoding="utf-8")


def file_exists(path: str | Path) -> bool:
    return Path(path).exists()


def write_text_atomic(path: str | Path, text: str) -> None:
    target = Path(path)
    ensure_dir(target.parent)

    with tempfile.NamedTemporaryFile(
        mode="w", encoding="utf-8", delete=False, dir=str(target.parent), prefix=".tmp.", suffix=".txt"
    ) as f:
        f.write(text)
        tmp_name = f.name

    os.replace(tmp_name, target)


def safe_join_under(root_dir: str | Path, relative_path: str) -> Path:
    root = Path(root_dir).resolve()
    rel = relative_path.replace("\\", "/").lstrip("/")
    resolved = (root / rel).resolve()
    if root != resolved and root not in resolved.parents:
        raise ValueError(f"Refusing to write outside {root}: {relative_path}")
    return resolved

