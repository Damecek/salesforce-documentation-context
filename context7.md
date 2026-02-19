# Context7

This Context7 library represents the Salesforce documentation corpus stored in `documentation/`.
The corpus is generated from official Salesforce PDFs and published as Markdown files for AI retrieval.

## What The Documentation Contains

- Salesforce platform guides and references converted to Markdown.
- Source and fetch metadata in each document header (source URL and fetch timestamp).
- Split parts for large guides (for example `*-part-01.md`, `*-part-02.md`).

The authoritative content lives in `documentation/`, and `llms.txt` indexes those files for retrieval.

## Context7 Access

Use the fixed library identity for this documentation set:

- Library page: `https://context7.com/damecek/salesforce-documentation-context`
- Library ID: `/damecek/salesforce-documentation-context`

```json
{
  "libraryId": "/damecek/salesforce-documentation-context",
  "query": "Answer using the Salesforce docs corpus in documentation/. Include exact command/limit/syntax details and a minimal example."
}
```

Query this library when you need answers grounded in the generated Salesforce documentation corpus, not in general framework docs.

## Sources

- https://github.com/damecek/salesforce-documentation-context/blob/main/README.md
- https://raw.githubusercontent.com/Damecek/salesforce-documentation-context/main/llms.txt
