import path from "node:path";
import { readFile } from "node:fs/promises";

import { ensureDir, fileExists, readTextIfExists, writeFileAtomic } from "./lib/fs.js";
import { detectGithubRawConfig } from "./lib/github.js";
import { sha256Hex } from "./lib/hash.js";
import { buildLlmsTxt } from "./lib/llms.js";
import { runWithConcurrency } from "./lib/limit.js";
import { pdfToMarkdown } from "./lib/pdf.js";
import { parseSrcTxt, type SrcEntry } from "./lib/srcList.js";
import { listMarkdownDocs } from "./lib/docs.js";

type CacheMeta = {
  etag?: string;
  lastModified?: string;
  sha256?: string;
};

const SRC_FILE = process.env.SRC_FILE ?? "src.txt";
const DOCS_DIR = process.env.DOCS_DIR ?? "documentation";
const CACHE_DIR = process.env.CACHE_DIR ?? ".cache";
const CONCURRENCY = (() => {
  const value = Number(process.env.CONCURRENCY ?? "4");
  return Number.isFinite(value) && value > 0 ? value : 4;
})();
const FORCE = (() => {
  const v = (process.env.FORCE ?? "").toLowerCase().trim();
  return v === "1" || v === "true" || v === "yes";
})();

function safeJoinDocs(outFile: string): string {
  const normalized = outFile.replace(/\\/g, "/").replace(/^\/+/, "");
  const resolved = path.resolve(DOCS_DIR, normalized);
  const docsRoot = path.resolve(DOCS_DIR) + path.sep;
  if (!resolved.startsWith(docsRoot)) {
    throw new Error(`Refusing to write outside ${DOCS_DIR}/: ${outFile}`);
  }
  return resolved;
}

function normalizeOutFile(outFile: string): string {
  const trimmed = outFile.trim();
  return trimmed.toLowerCase().endsWith(".md") ? trimmed : `${trimmed}.md`;
}

async function fetchPdfWithCache(url: string): Promise<{ bytes: Uint8Array; changed: boolean }> {
  await ensureDir(CACHE_DIR);
  const key = sha256Hex(url).slice(0, 24);
  const pdfPath = path.join(CACHE_DIR, `${key}.pdf`);
  const metaPath = path.join(CACHE_DIR, `${key}.json`);

  const prevMetaText = await readTextIfExists(metaPath);
  const prevMeta: CacheMeta | null = (() => {
    if (!prevMetaText) return null;
    try {
      return JSON.parse(prevMetaText) as CacheMeta;
    } catch {
      return null;
    }
  })();

  const headers = new Headers();
  if (prevMeta?.etag) headers.set("If-None-Match", prevMeta.etag);
  if (prevMeta?.lastModified) headers.set("If-Modified-Since", prevMeta.lastModified);

  let res = await fetch(url, { headers });
  if (res.status === 304) {
    if (await fileExists(pdfPath)) {
      const bytes = new Uint8Array(await Bun.file(pdfPath).arrayBuffer());
      return { bytes, changed: false };
    }
    // Cache got wiped; retry without validators.
    res = await fetch(url);
  }

  if (!res.ok) {
    throw new Error(`Failed to download PDF (${res.status} ${res.statusText}): ${url}`);
  }

  const arrayBuffer = await res.arrayBuffer();
  const bytes = new Uint8Array(arrayBuffer);
  const sha256 = sha256Hex(bytes);
  const changed = prevMeta?.sha256 ? prevMeta.sha256 !== sha256 : true;
  await Bun.write(pdfPath, bytes);

  const nextMeta: CacheMeta = {};
  const etag = res.headers.get("etag");
  const lastModified = res.headers.get("last-modified");
  if (etag) nextMeta.etag = etag;
  if (lastModified) nextMeta.lastModified = lastModified;
  nextMeta.sha256 = sha256;
  await writeFileAtomic(metaPath, JSON.stringify(nextMeta, null, 2));

  return { bytes, changed };
}

function titleFromEntry(entry: SrcEntry, outFile: string): string {
  if (entry.title) return entry.title;
  const base = path.posix.basename(outFile.replace(/\\/g, "/")).replace(/\.md$/i, "");
  const title = base.replace(/[-_]+/g, " ").trim();
  return title ? title[0]!.toUpperCase() + title.slice(1) : "Document";
}

async function main(): Promise<void> {
  const srcContents = await readFile(SRC_FILE, "utf8").catch(() => "");
  const entries = srcContents ? parseSrcTxt(srcContents) : [];

  await ensureDir(DOCS_DIR);
  await ensureDir(CACHE_DIR);

  const results: { title: string; outRel: string }[] = [];
  const failures: { url: string; error: unknown }[] = [];

  await runWithConcurrency(entries, CONCURRENCY, async (entry) => {
    const outFile = normalizeOutFile(entry.outFile ?? "document.md");
    const outAbs = safeJoinDocs(outFile);
    const outRel = path.posix.join(DOCS_DIR.replace(/\\/g, "/"), outFile.replace(/\\/g, "/"));
    const title = titleFromEntry(entry, outFile);

    try {
      const fetchedAtIso = new Date().toISOString();
      const { bytes, changed } = await fetchPdfWithCache(entry.url);
      const outExists = await fileExists(outAbs);

      if (!FORCE && !changed && outExists) {
        results.push({ title, outRel });
        process.stdout.write(`= ${title} (unchanged) -> ${outRel}\n`);
        return;
      }
      const md = await pdfToMarkdown({ pdfBytes: bytes, title, sourceUrl: entry.url, fetchedAtIso });
      await writeFileAtomic(outAbs, md);
      results.push({ title, outRel });
      process.stdout.write(`✓ ${title} -> ${outRel}\n`);
    } catch (error) {
      failures.push({ url: entry.url, error });
      process.stderr.write(`✗ ${entry.url}\n`);
      process.stderr.write(`  ${String(error)}\n`);
    }
  });

  const rawBaseOverride = process.env.GITHUB_RAW_BASE ?? null;
  const branchOverride = process.env.GITHUB_RAW_BRANCH ?? null;
  const detected = detectGithubRawConfig();
  const rawBase =
    rawBaseOverride ??
    (detected.rawBaseUrl && branchOverride
      ? detected.rawBaseUrl.replace(/\/[^/]+$/, `/${branchOverride}`)
      : detected.rawBaseUrl);

  const docsOnDisk = await listMarkdownDocs(DOCS_DIR);
  const docsForLlms = docsOnDisk.map((doc) => {
    const outRel = path.posix.join(DOCS_DIR.replace(/\\/g, "/"), doc.relPath);
    return {
      title: doc.title,
      rawUrl: rawBase ? `${rawBase}/${outRel}` : outRel,
    };
  });

  await writeFileAtomic("llms.txt", buildLlmsTxt(docsForLlms));

  if (failures.length > 0) {
    process.exitCode = 1;
  }
}

await main();
