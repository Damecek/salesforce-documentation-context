# salesforce-documentation-context

One place where Salesforce documentation (PDFs on URLs) is downloaded, converted to Markdown, and written into
`documentation/`. The project also generates `llms.txt` (per https://llmstxt.org/) with links to the GitHub Raw
versions of those Markdown files.

## Requirements

- Bun (`bun --version`)

## Usage

1. Update `src.txt` (your list of PDF sources).
2. Install dependencies:

   ```bash
   bun install
   ```

3. Generate / refresh Markdown:

   ```bash
   bun run update
   ```

Output:

- Markdown files in `documentation/` (one per entry in `src.txt`).
- Download cache in `.cache/` (ETag / Last-Modified when available).
- Updated `llms.txt` with GitHub Raw links.

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
- `GITHUB_RAW_BASE` (e.g. `https://raw.githubusercontent.com/OWNER/REPO/main`)
- `GITHUB_RAW_BRANCH` (override branch used for raw links)
