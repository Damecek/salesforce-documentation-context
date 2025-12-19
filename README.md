# salesforce-documentation-context

One place where Salesforce documentation (PDFs on URLs) is downloaded, converted to Markdown, and written into
`documentation/`. The project also generates `llms.txt` (per https://llmstxt.org/) with links to the GitHub Raw
versions of those Markdown files.

## Requirements

- Python 3.10+ (`python3 --version`)
- uv (`uv --version`)

## Usage

1. Update `src.txt` (your list of PDF sources).
2. Install dependencies:

```bash
uv sync
```

3. Generate / refresh Markdown:

```bash
export PDF_IGNORE_IMAGES=1 && export PDF_FORCE_TEXT=1 && uv run update
```

Output:

- Markdown files in `documentation/` (one per entry in `src.txt`).
- Download cache in `.cache/` (ETag / Last-Modified when available).
- Updated `llms.txt` with GitHub Raw links.

Conversion notes:

- Uses `pymupdf4llm.to_markdown()` (PyMuPDF4LLM) for Markdown output.
- Header detection defaults to auto (TOC-based if available, otherwise font-size heuristics).

## `src.txt` format

Supported variants (1 line = 1 document):

- `https://example.com/doc.pdf`
- `https://example.com/doc.pdf | sfdx_dev.md`
- `Document title | https://example.com/doc.pdf`
- `Document title | https://example.com/doc.pdf | sfdx_dev.md`

Lines starting with `#` are comments.

## Configuration (optional)

The updater supports these env vars:

- `SRC_FILE` (default `src.txt`)
- `DOCS_DIR` (default `documentation`)
- `CACHE_DIR` (default `.cache`)
- `CONCURRENCY` (default `4`)
- `FORCE` (set to `1`/`true` to regenerate Markdown even if the PDF content is unchanged)
- `HTTP_TIMEOUT` (default `60`, seconds)
- `GITHUB_RAW_BASE` (e.g. `https://raw.githubusercontent.com/OWNER/REPO/main`)
- `GITHUB_RAW_BRANCH` (override branch used for raw links)

PyMuPDF4LLM conversion tuning:

- `PDF_HDR_MODE` (`auto` | `toc` | `identify` | `none`) (default `auto`)
- `PDF_HDR_BODY_LIMIT` (default `12`)
- `PDF_HDR_MAX_LEVELS` (default `4`)
- `PDF_HDR_SAMPLE_PAGES` (default `10`)
- `PDF_FORCE_TEXT` (`1`/`true` to extract text even over images)
- `PDF_IGNORE_IMAGES` (`1`/`true`)
- `PDF_IGNORE_GRAPHICS` (`1`/`true`)
- `PDF_TABLE_STRATEGY` (e.g. `lines_strict`, `lines`, `text`, `explicit`; empty disables)
