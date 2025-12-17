import path from "node:path";

export type SrcEntry = {
  title: string | null;
  url: string;
  outFile: string | null;
};

function isHttpUrl(value: string): boolean {
  try {
    const u = new URL(value);
    return u.protocol === "http:" || u.protocol === "https:";
  } catch {
    return false;
  }
}

function slugify(value: string): string {
  return value
    .trim()
    .toLowerCase()
    .replace(/['"]/g, "")
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "")
    .slice(0, 80);
}

function defaultOutFile(title: string | null, url: string): string {
  const urlPath = (() => {
    try {
      return new URL(url).pathname;
    } catch {
      return "";
    }
  })();
  const base = path.posix.basename(urlPath || "document.pdf").replace(/\.pdf$/i, "");
  const slug = slugify(title ?? base) || slugify(base) || "document";
  return `${slug}.md`;
}

export function parseSrcTxt(contents: string): SrcEntry[] {
  const entries: SrcEntry[] = [];

  const lines = contents.split(/\r?\n/);
  for (const rawLine of lines) {
    const line = rawLine.trim();
    if (!line) continue;
    if (line.startsWith("#")) continue;

    if (line.includes("|")) {
      const parts = line
        .split("|")
        .map((p) => p.trim())
        .filter(Boolean);

      if (parts.length < 2 || parts.length > 3) {
        throw new Error(`Invalid src.txt line (expected 2-3 parts separated by "|"): ${rawLine}`);
      }

      const [a, b, c] = parts;

      if (isHttpUrl(a) && b) {
        entries.push({ title: null, url: a, outFile: c ?? b });
        continue;
      }

      if (isHttpUrl(b) && a) {
        entries.push({ title: a, url: b, outFile: c ?? null });
        continue;
      }

      throw new Error(`Invalid src.txt line (could not detect URL): ${rawLine}`);
    }

    const tokens = line.split(/\s+/);
    const url = tokens[0] ?? "";
    if (!isHttpUrl(url)) throw new Error(`Invalid URL in src.txt: ${rawLine}`);

    const outFile = tokens.length > 1 ? tokens.slice(1).join(" ") : null;
    entries.push({ title: null, url, outFile });
  }

  // Fill defaults.
  return entries.map((e) => ({
    ...e,
    outFile: e.outFile ? e.outFile : defaultOutFile(e.title, e.url),
  }));
}

