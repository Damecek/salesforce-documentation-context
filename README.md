# salesforce-documentation-context
## Usage (Context7 MCP)

Install the Context7 MCP server into your AI agent:
https://github.com/upstash/context7#installation

Then tell the agent to use this library (the `llms.txt` from this repo) directly via Context7. Example instruction:

```
- If a Context7 MCP server is available, call `get-library-docs` directly (skip `resolve-library-id`) with
  `context7CompatibleLibraryID: damecek/salesforce-documentation-context`, to get up to date information about target topic.
```

## Generate Documentation

One place where Salesforce documentation (PDFs on URLs) is downloaded, converted to Markdown, and written into
`documentation/`. The project also generates `llms.txt` (per https://llmstxt.org/) with links to the GitHub Raw
versions of those Markdown files.

## Requirements

- Python 3.10+ (`python3 --version`)
- uv (`uv --version`)

Fastest way to create or re-generate Markdown documentation files (`documentation/`) and update `llms.txt`:

1. Update `src.txt` (your list of PDF sources).
2. Install dependencies:

```bash
uv sync
```

3. Generate / refresh Markdown:

```bash
FORCE=1 PDF_IGNORE_IMAGES=1 PDF_FORCE_TEXT=1 uv run update
```

Output:

- Markdown files in `documentation/` (one per entry in `src.txt`).
- Download cache in `.cache/` (ETag / Last-Modified when available).
- Updated `llms.txt` with GitHub Raw links.

## Refresh only one specific link

Do not use `FORCE=1` here (it clears the whole `documentation/` folder).

1. Prepare a temporary source file with just the one entry:

```bash
cat > /tmp/one.txt <<'EOF'
https://example.com/doc.pdf | doc.md
EOF
```

2. (Optional but recommended) Clear the cache just for that URL so it always regenerates:

```bash
URL="https://example.com/doc.pdf"
KEY=$(python - <<'PY'
import hashlib, os
url = os.environ["URL"]
print(hashlib.sha256(url.encode("utf-8")).hexdigest()[:24])
PY
)
rm -f ".cache/${KEY}.pdf" ".cache/${KEY}.json"
```

3. Run the updater against only that temporary file:

```bash
uv run update --src /tmp/one.txt
```

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
