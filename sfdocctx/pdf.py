from __future__ import annotations

import os


def pdf_to_markdown(*, pdf_bytes: bytes, title: str, source_url: str, fetched_at_iso: str) -> str:
    header = "\n".join(
        [
            f"# {title}",
            "",
            f"> Source: {source_url}",
            f"> Fetched: {fetched_at_iso}",
            "",
        ]
    )

    body = ""
    try:
        import pymupdf4llm  # type: ignore
    except ModuleNotFoundError as e:
        raise RuntimeError("Missing dependency: pymupdf4llm (run `uv sync`).") from e

    doc = _open_pymupdf_doc(pdf_bytes)
    try:
        hdr_info = _build_header_detector(pymupdf4llm, doc)

        force_text = _env_flag("PDF_FORCE_TEXT")
        ignore_images = _env_flag("PDF_IGNORE_IMAGES")
        ignore_graphics = _env_flag("PDF_IGNORE_GRAPHICS")
        table_strategy = os.environ.get("PDF_TABLE_STRATEGY") or None

        try:
            md = pymupdf4llm.to_markdown(  # type: ignore[attr-defined]
                doc,
                hdr_info=hdr_info,
                use_glyphs=True,
                force_text=force_text,
                ignore_images=ignore_images,
                ignore_graphics=ignore_graphics,
                table_strategy=table_strategy,
            )
        except Exception as e:
            # PyMuPDF4LLM rejects the combination of "ignore images" with also suppressing
            # "text on images" (i.e., force_text=False). If a user asked to ignore images,
            # prefer keeping text extraction working.
            msg = str(e)
            if "Images and text on images cannot both be suppressed" in msg:
                if ignore_images and not force_text:
                    md = pymupdf4llm.to_markdown(  # type: ignore[attr-defined]
                        doc,
                        hdr_info=hdr_info,
                        use_glyphs=True,
                        force_text=True,
                        ignore_images=True,
                        ignore_graphics=ignore_graphics,
                        table_strategy=table_strategy,
                    )
                else:
                    md = pymupdf4llm.to_markdown(  # type: ignore[attr-defined]
                        doc,
                        hdr_info=hdr_info,
                        use_glyphs=True,
                        force_text=force_text,
                        ignore_images=False,
                        ignore_graphics=ignore_graphics,
                        table_strategy=table_strategy,
                    )
            else:
                raise
        body = _strip_leading_h1(_normalize_markdown(md))
    finally:
        try:
            doc.close()
        except Exception:
            pass

    return f"{header}{body}\n" if body else f"{header}\n"


def _open_pymupdf_doc(pdf_bytes: bytes):
    try:
        import pymupdf  # type: ignore

        return pymupdf.open(stream=pdf_bytes, filetype="pdf")
    except Exception:
        import fitz  # type: ignore

        return fitz.open(stream=pdf_bytes, filetype="pdf")


def _normalize_markdown(md: str) -> str:
    out = md.replace("\r\n", "\n").replace("\r", "\n")
    while "\n\n\n" in out:
        out = out.replace("\n\n\n", "\n\n")
    return out.strip()


def _strip_leading_h1(md: str) -> str:
    lines = md.split("\n")
    if not lines:
        return md
    if not lines[0].startswith("# "):
        return md
    rest = lines[1:]
    if rest and rest[0] == "":
        rest = rest[1:]
    return "\n".join(rest).strip()


def _build_header_detector(pymupdf4llm, doc):
    mode = (os.environ.get("PDF_HDR_MODE") or "auto").strip().lower()
    if mode in {"0", "false", "none", "off"}:
        return False

    if mode in {"toc", "auto"}:
        try:
            return pymupdf4llm.TocHeaders(doc)  # type: ignore[attr-defined]
        except Exception:
            if mode == "toc":
                return None

    if mode in {"identify", "auto"}:
        try:
            body_limit = _env_int("PDF_HDR_BODY_LIMIT", 12)
            max_levels = _env_int("PDF_HDR_MAX_LEVELS", 4)
            sample_pages_n = _env_int("PDF_HDR_SAMPLE_PAGES", 10)

            page_count = getattr(doc, "page_count", None) or getattr(doc, "pageCount", None) or 0
            page_count = int(page_count) if page_count else 0
            sample_pages = list(range(min(page_count, max(sample_pages_n, 0)))) if page_count else None

            return pymupdf4llm.IdentifyHeaders(  # type: ignore[attr-defined]
                doc, pages=sample_pages, body_limit=body_limit, max_levels=max_levels
            )
        except Exception:
            return None

    return None


def _env_flag(name: str) -> bool:
    value = os.environ.get(name, "").strip().lower()
    return value in {"1", "true", "yes", "y", "on"}


def _env_int(name: str, default: int) -> int:
    try:
        value = int(os.environ.get(name, "").strip())
        return value
    except Exception:
        return default
