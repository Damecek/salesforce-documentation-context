import { spawnSync } from "node:child_process";

export type GithubRawConfig = {
  rawBaseUrl: string | null;
  branch: string | null;
  ownerRepo: string | null;
};

function runGit(args: string[]): string | null {
  const res = spawnSync("git", args, { encoding: "utf8" });
  if (res.status !== 0) return null;
  return (res.stdout ?? "").trim() || null;
}

function parseGithubOwnerRepo(remote: string): string | null {
  // git@github.com:OWNER/REPO.git
  const ssh = remote.match(/^git@github\.com:([^/]+\/[^/]+?)(?:\.git)?$/);
  if (ssh?.[1]) return ssh[1];

  // https://github.com/OWNER/REPO(.git)
  const https = remote.match(/^https?:\/\/github\.com\/([^/]+\/[^/]+?)(?:\.git)?$/);
  if (https?.[1]) return https[1];

  return null;
}

export function detectGithubRawConfig(): GithubRawConfig {
  const branch = runGit(["rev-parse", "--abbrev-ref", "HEAD"]);
  const remote = runGit(["config", "--get", "remote.origin.url"]);
  const ownerRepo = remote ? parseGithubOwnerRepo(remote) : null;
  const rawBaseUrl =
    ownerRepo && branch ? `https://raw.githubusercontent.com/${ownerRepo}/${branch}` : null;

  return { rawBaseUrl, branch, ownerRepo };
}

