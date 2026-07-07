# Salesforce Docs MCP vs. Context7 — Comparison Report

**Date:** 2026-06-30 · **Mode:** local only, nothing committed
**Script:** [`compare.py`](./compare.py) · **Questions:** [`questions.md`](./questions.md) · **Raw answers:** [`out/`](./out)

## What was compared

| # | Approach | Endpoint / target | Tool(s) used |
|---|----------|-------------------|--------------|
| A | **salesforce-docs-mcp** | `https://salesforce-docs-76258744c9d7.herokuapp.com/api/mcp` | `salesforce_docs_search` |
| B | **Context7 + our library** | `https://mcp.context7.com/mcp`, lib `/damecek/salesforce-documentation-context` | `query-docs` |
| C | **Context7 without library** | same server, library auto-picked | `resolve-library-id` → `query-docs` |

Both targets are remote **streamable-HTTP MCP servers**. The script speaks raw
JSON-RPC/MCP over HTTP (stdlib only) and needs **no API key** for either server.

### Capability validation (the docs page vs. reality)

The [Docs MCP page](https://labs.agentforce.com/docs/salesforce-docs-mcp) advertises two tools and they exist as documented:

- `salesforce_docs_search(query, collection?, limit?)` — semantic search, ranked excerpts with **source URLs + relevance scores**.
- `salesforce_docs_fetch(id)` — fetch a full page by `documentPath` from a search hit.

Context7 (server v3.2.2) exposes `resolve-library-id(query, libraryName)` and
`query-docs(libraryId, query)`. Note: the repo README still references the old
`get-library-docs` name — the live server now uses **`query-docs`**.

## Results

### Per-question scoring (relevance + correctness, 0–5)

| # | A · salesforce-docs-mcp | B · Context7 + our lib | C · Context7 no lib | Library C auto-picked |
|---|:--:|:--:|:--:|---|
| 1 SOQL LIMIT | **4.5** | 3.0 | 1.0 | `/forcedotcom/go-soql` (a **Go** lib!) |
| 2 JWT bearer flow | **5.0** | 4.0 | 1.0 | `/websites/oauth_net` (generic OAuth) |
| 3 max SOQL/txn | 3.5 | 3.0 | 1.0 | `/beyond-the-cloud-dev/soql-lib` |
| 4 record-triggered flow | **5.0** | 2.5 | 0.0 | `/aframevr/aframe` (**VR framework!**) |
| 5 @future annotation | **4.5** | 4.0 | 3.0 | `/trailheadapps/apex-recipes` |
| 6 multiline string + `??` | 3.5 | 3.5 | 0.5 | `/websites/literal_fun` (a **Ruby** gem!) |
| 7 toast in screen flow | **4.0** | 2.5 | 0.5 | `/calintamas/react-native-toast-message` |
| 8 LWC vs LWR vs LWS | 3.5 | 1.0 | 2.5 | `/salesforce/lwc` (right ecosystem!) |
| 9 picklist by record type | **5.0** | 4.5 | 0.0 | `/llfbandit/record` (**Flutter audio**!) |
| 10 Transform vs Loop | **4.0** | 4.0 | 0.0 | `/crossplane-contrib/...` (Crossplane) |
| 11 LWC headless quick action | **4.5** | 1.5 | 1.0 | `/salesforce/lwc` (right lib, wrong content) |
| **Average** | **4.3** | **3.0** | **0.95** | |

> Questions 1–5 are the original batch; 6–11 were added in later runs and skew
> toward newer / more specific Salesforce features.

### Operational characteristics

| Metric | A · sf-docs | B · C7 our lib | C · C7 no lib |
|--------|:--:|:--:|:--:|
| Latency (typical) | **~1.7–2.0 s** (fastest) | ~2.8–9.4 s | ~4.0–5.3 s (2 round-trips) |
| Payload size | 6k–10k chars (largest) | 2.5k–6.6k chars (compact) | 2.2k–4.8k chars |
| Output format | JSON chunks `{content, score, url, documentPath}` — **needs formatting** | pre-rendered Markdown + code blocks + GitHub source links | same as B |
| Citations | official `help/developer.salesforce.com` URLs + relevance score | GitHub raw links into our corpus (`v1.3.0` tag) | links into whatever lib was picked |
| Coverage | full official Salesforce docs (help, dev guides, release notes) | only what we generated into `documentation/` | all of Context7 (mostly **non-Salesforce**) |

## Findings

**A · salesforce-docs-mcp — best overall (4.3/5).** Every question hit relevant,
**official, current** Salesforce content with real source URLs and relevance
scores. It nailed the procedural questions where the others struggled — Q4
returned the exact official tutorial *"Create a Simple After-Save
Record-Triggered Flow"*, Q2 returned the step-by-step external-client-app + JWT
procedure. Downsides: it returns raw JSON chunks (the agent must format them),
payloads are the largest (most tokens), and semantic search occasionally ranks a
tangential page first — Q3's top chunk was a *Net Zero Cloud* report page that
merely quotes the 50,000-record recommendation, with the precise per-transaction
numbers (100/200) appearing in later chunks rather than up top.

**B · Context7 + our library — solid, code-first, deterministic (3.0/5).**
Pinned to our corpus it is always Salesforce-relevant, compact, pre-formatted as
Markdown with runnable code blocks and stable GitHub source links. It shines on
code-pattern questions (Q2 `Auth.JWT` example, Q5 `@future` example). Its ceiling
is our corpus coverage: Q4 returned a *definitional* `FlowRecordVersion`
description instead of a build procedure, and Q1 returned a near-trivial
`LIMIT 1` example. It answers "show me the code/definition", less so "walk me
through the procedure". This is the right tool when you specifically want answers
grounded in *this* curated corpus.

**C · Context7 without a pinned library — unreliable to misleading (0.95/5).**
`resolve-library-id` ranks by library-name match + benchmark score and **ignores
the Salesforce platform context**. Across 10 questions it landed in the wrong
ecosystem most of the time, sometimes absurdly so: a **Go** SOQL marshaller (Q1),
generic OAuth.net (Q2), **A-Frame / WebVR** for "record-triggered flow" (Q4), a
**Ruby** gem for the Apex string question (Q6), **react-native-toast-message**
for a screen-flow toast (Q7), and a **Flutter audio-recording** plugin for the
Apex picklist question (Q9). It picked a sane Salesforce library only twice:
`apex-recipes` (Q5) and `/salesforce/lwc` (Q8) — and Q8 is the *one* case where
C actually beat B, because our corpus has thin LWR/LWS coverage while the
official LWC repo is on Context7. Takeaway: for Salesforce questions Context7 is
only safe **when you pin the library** — exactly this repo's README instruction.

### Two genuine gaps surfaced (none of the three nailed these)

- **Q6 null coalescing operator (`??`)** — A and B both answered the *multiline
  string* half well (triple-quote `'''…'''` literal, escape sequences) but
  neither surfaced the `??` operator. The compound question wasn't fully covered.
- **Q8 LWR / LWS + enforcement version** — A returned the authoritative LWC
  *release→API-version* table (Spring '25 = 63.0, …) but didn't cleanly separate
  Lightning Web **Runtime** vs Lightning Web **Security** or state enforcement
  versions; B drifted to an unrelated `FlowVariableView` object. This is a
  coverage gap worth feeding back into `src.txt` for our corpus.
- **Q11 LWC headless quick action** — A nailed it: the official *Create Headless
  Quick Actions* + *migrate from Aura quick actions* pages, including the
  availability notes (record pages in Lightning Experience, LWR sites). B missed
  entirely (returned `lightning__FlowAction` metadata and an Aura
  `getShowQuickActionLcHeader()` method) — the **LWC Developer Guide is not in
  our corpus**, same root cause as Q8. C picked the right library
  (`/salesforce/lwc`) for the second time but the OSS repo docs answered with
  *headless Chrome testing*, not quick actions — platform features simply aren't
  documented in the OSS repo. Neither A's top excerpts nor B/C surfaced the
  explicit minimum API version for the `invoke()` headless target.

Also note Q7's nuance: A correctly surfaced the **Message screen component** (the
native way to show a notice *in a screen flow*), whereas B returned the Aura
`lightning:notificationsLibrary.showToast` pattern — a real toast, but a
*component* technique rather than the in-flow answer the question asked for.

## Verdict & recommendation

1. **For Salesforce platform/admin/security/how-to questions → use
   salesforce-docs-mcp (A).** Broadest, freshest, official, best on procedures.
   Accept the cost: format the JSON yourself and keep `limit` low (3–5) to
   control tokens; use `salesforce_docs_fetch` only when a full page is needed.
2. **For code-grounded answers from our curated corpus → use Context7 pinned to
   `/damecek/salesforce-documentation-context` (B).** Compact, deterministic,
   code-first, cheap on tokens. Best as a *complement* to A.
3. **Never rely on Context7 without pinning the library for Salesforce questions
   (C).** The resolver drifts to the wrong ecosystem. If using Context7, always
   pass `libraryId` explicitly.

**Bottom line:** salesforce-docs-mcp is the stronger general-purpose Salesforce
retriever; our Context7 library is a valuable, low-token, code-oriented
complement for topics our corpus covers. The "no pinned library" path validates
*why* this repo exists — generic Context7 resolution is not a substitute for a
curated, pinned Salesforce corpus.

## Reproduce

```bash
python3 compare/compare.py --all            # 5 benchmark questions, all 3 approaches
python3 compare/compare.py "your question"  # any single question
# optional, raises Context7 rate limits: export CONTEXT7_API_KEY=...
```
