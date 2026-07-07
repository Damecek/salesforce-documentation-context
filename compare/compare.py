#!/usr/bin/env python3
"""Compare three documentation-retrieval approaches for one question.

Approaches
----------
A) salesforce-docs-mcp     -> Salesforce official Docs MCP (`salesforce_docs_search`)
B) context7 + our library  -> Context7 `query-docs` pinned to /damecek/salesforce-documentation-context
C) context7 without library-> Context7 `resolve-library-id` (auto-pick top lib) then `query-docs`

Both targets are remote streamable-HTTP MCP servers; this script speaks raw
JSON-RPC / MCP over HTTP using only the Python standard library. No API keys
are required for either server at the time of writing.

Usage
-----
    python compare.py "your question"      # one question, all 3 approaches
    python compare.py --all                # run the 5 built-in benchmark questions

Raw answers are written to compare/out/*.md; a short summary is printed.
"""
from __future__ import annotations

import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

SF_URL = "https://salesforce-docs-76258744c9d7.herokuapp.com/api/mcp"
C7_URL = "https://mcp.context7.com/mcp"
OUR_LIB = "/damecek/salesforce-documentation-context"

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")

# Optional: Context7 raises rate limits with a key. Works without one too.
C7_KEY = os.environ.get("CONTEXT7_API_KEY")

QUESTIONS = [
    "How do I write a SOQL query with a LIMIT clause in Apex, and what is the maximum LIMIT value?",
    "How do I configure an OAuth 2.0 JWT bearer token flow for a connected app in Salesforce?",
    "What is the maximum number of SOQL queries allowed in a single synchronous Apex transaction?",
    "How do I create a record-triggered flow that runs after a record is saved?",
    "How do I use the @future annotation for asynchronous Apex, and what are its restrictions?",
    "How do I write a multiline string literal in Apex, and can I use the null coalescing operator?",
    "How do I display a toast message in a Salesforce screen flow?",
    "What is the difference between LWC, LWR and LWS in Salesforce, and from which API version are they available and enforced?",
    "How do I get the list of picklist values for a given record type in Apex?",
    "How do I use the Flow Transform element, and what advantages does it have over a Flow Loop?",
    "How do I create a headless quick action with LWC (like Aura headless actions), and since which API version is it supported?",
]


class MCPClient:
    """Minimal streamable-HTTP MCP client (stdlib only)."""

    def __init__(self, url: str, headers: dict | None = None):
        self.url = url
        self.extra = headers or {}
        self.session = None
        self._id = 0
        self._init()

    def _post(self, payload: dict) -> tuple[int, str | None, str]:
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json, text/event-stream",
        }
        headers.update(self.extra)
        if self.session:
            headers["Mcp-Session-Id"] = self.session
        req = urllib.request.Request(
            self.url, data=json.dumps(payload).encode(), headers=headers, method="POST"
        )
        try:
            r = urllib.request.urlopen(req, timeout=120)
            return r.status, r.headers.get("Mcp-Session-Id"), r.read().decode()
        except urllib.error.HTTPError as e:
            return e.code, e.headers.get("Mcp-Session-Id"), e.read().decode()

    @staticmethod
    def _parse(raw: str) -> dict:
        # streamable-HTTP may answer as SSE (event/data lines) or plain JSON
        if "data:" in raw[:40]:
            data = "".join(
                ln[5:].strip() for ln in raw.splitlines() if ln.startswith("data:")
            )
            return json.loads(data) if data else {}
        return json.loads(raw)

    def _init(self):
        self._id += 1
        st, sid, raw = self._post(
            {
                "jsonrpc": "2.0",
                "id": self._id,
                "method": "initialize",
                "params": {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {},
                    "clientInfo": {"name": "doc-compare", "version": "1.0"},
                },
            }
        )
        if sid:
            self.session = sid
        # required handshake completion
        self._post({"jsonrpc": "2.0", "method": "notifications/initialized"})

    def call(self, tool: str, arguments: dict) -> dict:
        self._id += 1
        st, _, raw = self._post(
            {
                "jsonrpc": "2.0",
                "id": self._id,
                "method": "tools/call",
                "params": {"name": tool, "arguments": arguments},
            }
        )
        return self._parse(raw)


def _text(result: dict) -> str:
    """Flatten an MCP tool result's content[] into plain text."""
    if "error" in result:
        return f"[MCP ERROR] {json.dumps(result['error'])}"
    content = result.get("result", {}).get("content", [])
    parts = [c.get("text", "") for c in content if c.get("type") == "text"]
    return "\n".join(parts) if parts else json.dumps(result.get("result", result))[:4000]


# ---------------------------------------------------------------- approaches
def approach_sf(q: str) -> dict:
    t0 = time.time()
    c = MCPClient(SF_URL)
    res = c.call("salesforce_docs_search", {"query": q, "limit": 5})
    txt = _text(res)
    return {"name": "A_salesforce-docs-mcp", "text": txt, "ms": int((time.time() - t0) * 1000), "meta": {}}


def approach_c7_lib(q: str) -> dict:
    t0 = time.time()
    hdr = {"Authorization": f"Bearer {C7_KEY}"} if C7_KEY else None
    c = MCPClient(C7_URL, hdr)
    res = c.call("query-docs", {"libraryId": OUR_LIB, "query": q})
    txt = _text(res)
    return {"name": "B_context7-our-library", "text": txt, "ms": int((time.time() - t0) * 1000),
            "meta": {"libraryId": OUR_LIB}}


def approach_c7_nolib(q: str) -> dict:
    t0 = time.time()
    hdr = {"Authorization": f"Bearer {C7_KEY}"} if C7_KEY else None
    c = MCPClient(C7_URL, hdr)
    resolve = c.call("resolve-library-id", {"query": q, "libraryName": q[:60]})
    resolve_txt = _text(resolve)
    m = re.search(r"Context7-compatible library ID:\s*(\S+)", resolve_txt)
    chosen = m.group(1) if m else None
    title = None
    tm = re.search(r"Title:\s*(.+)", resolve_txt)
    if tm:
        title = tm.group(1).strip()
    docs_txt = "[no library resolved]"
    if chosen:
        docs = c.call("query-docs", {"libraryId": chosen, "query": q})
        docs_txt = _text(docs)
    full = (
        f"### resolve-library-id picked: {chosen} ({title})\n\n"
        f"--- resolve-library-id ranking (top of list) ---\n{resolve_txt[:1200]}\n\n"
        f"--- query-docs against {chosen} ---\n{docs_txt}"
    )
    return {"name": "C_context7-no-library", "text": full, "ms": int((time.time() - t0) * 1000),
            "meta": {"chosenLibrary": chosen, "chosenTitle": title}}


def run_question(idx: int, q: str):
    print(f"\n{'='*78}\nQ{idx}: {q}\n{'='*78}")
    for fn in (approach_sf, approach_c7_lib, approach_c7_nolib):
        try:
            r = fn(q)
        except Exception as e:  # noqa: BLE001 - report, never crash the batch
            r = {"name": fn.__name__, "text": f"[EXCEPTION] {e}", "ms": 0, "meta": {}}
        fname = os.path.join(OUT_DIR, f"q{idx}_{r['name']}.md")
        with open(fname, "w") as fh:
            fh.write(f"# Q{idx}: {q}\n\n## Approach: {r['name']}\n")
            fh.write(f"- latency: {r['ms']} ms\n")
            for k, v in r["meta"].items():
                fh.write(f"- {k}: {v}\n")
            fh.write(f"\n---\n\n{r['text']}\n")
        snippet = re.sub(r"\s+", " ", r["text"])[:160]
        extra = ""
        if r["meta"].get("chosenLibrary"):
            extra = f"  -> picked {r['meta']['chosenLibrary']}"
        print(f"  [{r['name']:<26}] {r['ms']:>6} ms | {len(r['text']):>6} chars{extra}")
        print(f"      {snippet}")


def main(argv: list[str]):
    os.makedirs(OUT_DIR, exist_ok=True)
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return
    if argv[0] == "--all":
        for i, q in enumerate(QUESTIONS, 1):
            run_question(i, q)
    else:
        run_question(1, " ".join(argv))
    print(f"\nRaw answers written to: {OUT_DIR}")


if __name__ == "__main__":
    main(sys.argv[1:])
