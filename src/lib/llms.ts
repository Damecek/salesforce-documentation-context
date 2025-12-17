export type LlmsDocLink = {
  title: string;
  rawUrl: string;
};

export function buildLlmsTxt(docs: LlmsDocLink[]): string {
  const lines: string[] = [];

  lines.push("# Salesforce documentation context");
  lines.push("");
  lines.push("> Salesforce PDF docs converted to Markdown for LLM context.");
  lines.push("");
  lines.push(
    "Update `src.txt`, then run `bun run update` to regenerate Markdown files in `documentation/` and refresh this list.",
  );
  lines.push("");
  lines.push("## Documentation");

  if (docs.length === 0) {
    lines.push("- (none yet) Add entries to `src.txt` and run `bun run update`.");
  } else {
    for (const doc of docs) {
      lines.push(`- [${doc.title}](${doc.rawUrl})`);
    }
  }

  lines.push("");
  return lines.join("\n");
}

