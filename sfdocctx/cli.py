from __future__ import annotations

import argparse
import os
import sys

from .update import run_update


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="update",
        description=(
            "Download PDFs listed in src.txt, convert them to Markdown under documentation/, "
            "and regenerate llms.txt."
        ),
    )
    parser.add_argument(
        "--src",
        default=os.environ.get("SRC_FILE", "src.txt"),
        help="Source list file (default: src.txt; env: SRC_FILE).",
    )
    parser.add_argument(
        "--docs-dir",
        default=os.environ.get("DOCS_DIR", "documentation"),
        help="Output documentation directory (default: documentation; env: DOCS_DIR).",
    )
    parser.add_argument(
        "--cache-dir",
        default=os.environ.get("CACHE_DIR", ".cache"),
        help="Cache directory (default: .cache; env: CACHE_DIR).",
    )
    parser.add_argument(
        "--concurrency",
        type=int,
        default=int(os.environ.get("CONCURRENCY", "4")),
        help="Parallel download/conversion concurrency (default: 4; env: CONCURRENCY).",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        default=_env_flag("FORCE"),
        help="Regenerate Markdown even if the PDF is unchanged (env: FORCE).",
    )
    parser.add_argument(
        "--github-raw-base",
        default=os.environ.get("GITHUB_RAW_BASE"),
        help="Override GitHub raw base URL (env: GITHUB_RAW_BASE).",
    )
    parser.add_argument(
        "--github-raw-branch",
        default=os.environ.get("GITHUB_RAW_BRANCH"),
        help="Override branch used for raw links (env: GITHUB_RAW_BRANCH).",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=float(os.environ.get("HTTP_TIMEOUT", "60")),
        help="HTTP timeout in seconds (default: 60; env: HTTP_TIMEOUT).",
    )

    args = parser.parse_args(argv)
    return run_update(
        src_file=args.src,
        docs_dir=args.docs_dir,
        cache_dir=args.cache_dir,
        concurrency=args.concurrency,
        force=args.force,
        github_raw_base=args.github_raw_base,
        github_raw_branch=args.github_raw_branch,
        http_timeout_s=args.timeout,
    )


def _env_flag(name: str) -> bool:
    value = os.environ.get(name, "").strip().lower()
    return value in {"1", "true", "yes", "y", "on"}


if __name__ == "__main__":
    raise SystemExit(main())

