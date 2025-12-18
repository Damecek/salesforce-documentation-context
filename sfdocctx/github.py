from __future__ import annotations

import re
import subprocess
from dataclasses import dataclass


@dataclass(frozen=True)
class GithubRawConfig:
    raw_base_url: str | None
    branch: str | None


_GITHUB_SSH_RE = re.compile(r"^git@github\.com:(?P<owner>[^/]+)/(?P<repo>[^/]+?)(?:\.git)?$")
_GITHUB_HTTPS_RE = re.compile(
    r"^https://github\.com/(?P<owner>[^/]+)/(?P<repo>[^/]+?)(?:\.git)?/?$"
)


def detect_github_raw_config() -> GithubRawConfig:
    remote = _git("config", "--get", "remote.origin.url")
    branch = _git("rev-parse", "--abbrev-ref", "HEAD")

    remote_url = remote.strip() if remote else ""
    branch_name = branch.strip() if branch else ""
    if branch_name == "HEAD":
        branch_name = ""

    owner_repo = _parse_github_owner_repo(remote_url)
    if not owner_repo:
        return GithubRawConfig(raw_base_url=None, branch=branch_name or None)

    owner, repo = owner_repo
    raw_base = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch_name or 'main'}"
    return GithubRawConfig(raw_base_url=raw_base, branch=branch_name or None)


def _parse_github_owner_repo(remote_url: str) -> tuple[str, str] | None:
    m = _GITHUB_SSH_RE.match(remote_url)
    if m:
        return m.group("owner"), m.group("repo")
    m = _GITHUB_HTTPS_RE.match(remote_url)
    if m:
        return m.group("owner"), m.group("repo")
    return None


def _git(*args: str) -> str:
    try:
        out = subprocess.check_output(["git", *args], stderr=subprocess.DEVNULL, text=True)
        return out
    except Exception:
        return ""

