from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class LlmsDocLink:
    title: str
    raw_url: str


def build_llms_txt(docs: list[LlmsDocLink]) -> str:
    lines: list[str] = []
    lines.append("# Salesforce documentation context")
    lines.append("")
    lines.append("> Salesforce PDF docs converted to Markdown for LLM context.")
    lines.append("")
    lines.append(
        "Update `src.txt`, then run `uv run update` to regenerate Markdown files in `documentation/` and refresh this list."
    )
    lines.append("")
    lines.append("## Documentation")

    if not docs:
        lines.append("- (none yet) Add entries to `src.txt` and run `uv run update`.")
    else:
        for doc in docs:
            lines.append(f"- [{doc.title}]({doc.raw_url})")

    lines.append("")
    return "\n".join(lines)

