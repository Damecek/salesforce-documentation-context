type PdfParseResult = {
  text?: string;
  info?: Record<string, unknown>;
  metadata?: unknown;
};

async function loadPdfParse(): Promise<(data: Buffer | Uint8Array) => Promise<PdfParseResult>> {
  // pdf-parse is CommonJS; Bun generally maps default import, but keep a robust fallback.
  const mod: any = await import("pdf-parse");
  return (mod?.default ?? mod) as (data: Buffer | Uint8Array) => Promise<PdfParseResult>;
}

function normalizePdfText(text: string): string {
  // Preserve line breaks but tame PDF oddities.
  let out = text.replace(/\r\n/g, "\n").replace(/\r/g, "\n");
  out = out.replace(/\f/g, "\n\n---\n\n");
  out = out.replace(/[ \t]+\n/g, "\n");
  out = out.replace(/\n{3,}/g, "\n\n");
  return out.trim();
}

export type PdfToMarkdownInput = {
  pdfBytes: Uint8Array;
  title: string;
  sourceUrl: string;
  fetchedAtIso: string;
};

export async function pdfToMarkdown(input: PdfToMarkdownInput): Promise<string> {
  const pdfParse = await loadPdfParse();
  const parsed = await pdfParse(Buffer.from(input.pdfBytes));
  const body = normalizePdfText(parsed.text ?? "");

  const header = [
    `# ${input.title}`,
    "",
    `> Source: ${input.sourceUrl}`,
    "",
    `Fetched: ${input.fetchedAtIso}`,
    "",
  ].join("\n");

  return `${header}${body}\n`;
}

