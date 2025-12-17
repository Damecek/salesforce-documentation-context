import { readdir, readFile } from "node:fs/promises";
import path from "node:path";

export type DocFile = {
  title: string;
  relPath: string; // posix relative to docs root, e.g. "foo/bar.md"
};

async function listFilesRecursive(rootAbs: string, relDirPosix = ""): Promise<string[]> {
  const dirAbs = path.join(rootAbs, relDirPosix);
  const dirents = await readdir(dirAbs, { withFileTypes: true });

  const out: string[] = [];
  for (const dirent of dirents) {
    const relPosix = relDirPosix
      ? path.posix.join(relDirPosix, dirent.name)
      : dirent.name;
    if (dirent.isDirectory()) {
      out.push(...(await listFilesRecursive(rootAbs, relPosix)));
    } else {
      out.push(relPosix);
    }
  }
  return out;
}

function titleFromMarkdown(contents: string, fallback: string): string {
  const firstHeading = contents.match(/^#\s+(.+)\s*$/m);
  const title = firstHeading?.[1]?.trim();
  return title && title.length > 0 ? title : fallback;
}

export async function listMarkdownDocs(docsDir: string): Promise<DocFile[]> {
  const rootAbs = path.resolve(docsDir);
  const all = await listFilesRecursive(rootAbs);
  const md = all.filter((p) => p.toLowerCase().endsWith(".md"));

  const docs: DocFile[] = [];
  for (const relPath of md) {
    const abs = path.join(rootAbs, relPath);
    const contents = await readFile(abs, "utf8").catch(() => "");
    const fallback = path.posix.basename(relPath).replace(/\.md$/i, "").replace(/[-_]+/g, " ");
    docs.push({ relPath, title: titleFromMarkdown(contents, fallback) });
  }

  docs.sort((a, b) => a.title.localeCompare(b.title));
  return docs;
}

