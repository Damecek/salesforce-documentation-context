# salesforce-documentation-context
## Usage (Context7 MCP)

Install the Context7 MCP server into your AI agent:
https://github.com/upstash/context7#installation

Then tell the agent to use this library (the `llms.txt` from this repo) directly via Context7. Example instruction:

```
- If a Context7 MCP server is available, call `query-docs` directly (skip `resolve-library-id`) with
  `context7CompatibleLibraryID: damecek/salesforce-documentation-context`, to get up to date information about target topic.
```

> The live Context7 server (v3.2.2) renamed `get-library-docs` → `query-docs`. Always pin the library
> explicitly — see the [Benchmark](#benchmark) below for why unpinned resolution is unsafe for Salesforce.

## Benchmark

We benchmarked this Context7 library against the official [Salesforce Docs MCP](https://labs.agentforce.com/docs/salesforce-docs-mcp)
across 11 real Salesforce questions (SOQL, Apex, Flow, LWC). Full report, methodology and raw answers:
[`compare/REPORT.md`](./compare/REPORT.md) (reproduce with `python3 compare/compare.py --all`).

Average score (relevance + correctness, 0–5):

| Approach | Avg | Notes |
|---|:--:|---|
| **A** · Salesforce Docs MCP (official) | **4.3** | Broadest, freshest, best on procedures; raw JSON chunks, largest payloads |
| **B** · Context7 + **this** library (pinned) | **3.0** | Compact, deterministic, code-first, low token cost; limited to our corpus |
| **C** · Context7 **without** pinning the library | **0.95** | Resolver drifts to the wrong ecosystem (Go, Ruby, Flutter, WebVR…) — unusable |

**Conclusion — stay with Context7, don't migrate.** The official Docs MCP wins overall, but it doesn't make
this library obsolete: our pinned corpus is the low-token, deterministic, code-first option that stays 100%
Salesforce-relevant and cites stable GitHub source links. The two are **complements**, not substitutes:

- Use the **official Salesforce Docs MCP** for broad platform / admin / how-to / procedural questions.
- Use **Context7 pinned to `/damecek/salesforce-documentation-context`** for compact, code-grounded answers from our curated corpus.
- **Never** use Context7 unpinned for Salesforce — approach C proves the resolver ignores platform context and picks the wrong library most of the time.

Migrating away from Context7 would trade a cheap, deterministic complement for nothing. The bigger win is
closing corpus gaps the benchmark surfaced (LWC Developer Guide, LWR/LWS) by feeding them into `src.txt`.

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

- Markdown files in `documentation/` (one or more per entry in `src.txt`; large outputs are split).
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
- `MAX_MD_BYTES` (default `899999`; split markdown outputs so each file stays under this size)
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
