"""
veilpiercer.audit
-----------------
RepoAuditor — scan any public GitHub repo for security gaps, missing files,
exposed secrets, logic issues, and engineering quality problems.

Usage:
    # As a module
    from veilpiercer.audit import RepoAuditor
    audit = RepoAuditor("https://github.com/louz514/Claudecraft")
    report = audit.run()
    report.print()
    report.open_github_issue()   # posts findings directly to their repo

    # As a CLI
    python -m veilpiercer.audit https://github.com/louz514/Claudecraft
    python -m veilpiercer.audit https://github.com/louz514/Claudecraft --issue

Created by Lauren Flipo (@fliptrigga13) · https://veil-piercer.com
"""

from __future__ import annotations

import re
import json
import base64
import urllib.request
import urllib.error
from datetime import datetime, timezone
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field


# ─── Data classes ────────────────────────────────────────────────────────────

@dataclass
class Finding:
    severity: str          # CRITICAL | HIGH | MEDIUM | LOW | INFO
    category: str          # Security | Testing | CI | Documentation | Logic
    title: str
    detail: str
    file: Optional[str] = None
    line: Optional[int] = None

    def emoji(self) -> str:
        return {"CRITICAL": "🔴", "HIGH": "🟠", "MEDIUM": "🟡", "LOW": "🔵", "INFO": "ℹ️"}.get(self.severity, "⚪")

    def __str__(self):
        loc = f" in `{self.file}`" if self.file else ""
        return f"{self.emoji()} **[{self.severity}] {self.title}**{loc}\n   {self.detail}"


@dataclass
class AuditReport:
    repo: str
    owner: str
    name: str
    findings: List[Finding] = field(default_factory=list)
    files_scanned: int = 0
    scanned_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    metadata: Dict = field(default_factory=dict)

    # ── Score ────────────────────────────────────────────────────────────────
    def score(self) -> int:
        """0–100 health score. 100 = perfect. Deduct per finding severity."""
        deductions = {"CRITICAL": 20, "HIGH": 12, "MEDIUM": 6, "LOW": 2, "INFO": 0}
        total = sum(deductions.get(f.severity, 0) for f in self.findings)
        return max(0, 100 - total)

    def grade(self) -> str:
        s = self.score()
        if s >= 90: return "A"
        if s >= 75: return "B"
        if s >= 60: return "C"
        if s >= 40: return "D"
        return "F"

    # ── Console output ───────────────────────────────────────────────────────
    def print(self):
        print(f"\n{'='*64}")
        print(f"  VeilPiercer Audit Report")
        print(f"  Repo   : {self.repo}")
        print(f"  Score  : {self.score()}/100  (Grade: {self.grade()})")
        print(f"  Files  : {self.files_scanned} scanned")
        print(f"  Issues : {len(self.findings)} found")
        print(f"  Time   : {self.scanned_at}")
        print(f"{'='*64}")

        by_severity = {}
        for f in self.findings:
            by_severity.setdefault(f.severity, []).append(f)

        for sev in ["CRITICAL", "HIGH", "MEDIUM", "LOW", "INFO"]:
            bucket = by_severity.get(sev, [])
            if not bucket:
                continue
            print(f"\n── {sev} ({len(bucket)}) {'─'*40}")
            for finding in bucket:
                loc = f"  [{finding.file}]" if finding.file else ""
                print(f"\n  {finding.emoji()} {finding.title}{loc}")
                print(f"     {finding.detail}")

        print(f"\n{'─'*64}")
        print(f"  Audited by VeilPiercer · https://veil-piercer.com · @fliptrigga13")
        print(f"  github.com/fliptrigga13/VEILPIERCER")
        print(f"{'='*64}\n")

    # ── Markdown for GitHub Issues ───────────────────────────────────────────
    def to_markdown(self, max_per_severity: int = 5) -> str:
        lines = [
            f"## 🔍 VeilPiercer Audit — `{self.name}`",
            f"",
            f"> Automated security & quality audit by [VeilPiercer](https://veil-piercer.com)",
            f"> Created by [Lauren Flipo](https://github.com/fliptrigga13) · [@fliptrigga13](https://github.com/fliptrigga13)",
            f"",
            f"**Score: {self.score()}/100 (Grade {self.grade()})** · {self.files_scanned} files scanned · {len(self.findings)} total issues",
            f"",
        ]

        by_severity = {}
        for f in self.findings:
            by_severity.setdefault(f.severity, []).append(f)

        for sev in ["CRITICAL", "HIGH", "MEDIUM", "LOW"]:
            bucket = by_severity.get(sev, [])
            if not bucket:
                continue

            # Deduplicate by title (collapse repeated same-title findings)
            seen_titles = {}
            deduped = []
            for finding in bucket:
                key = finding.title
                if key not in seen_titles:
                    seen_titles[key] = 0
                    deduped.append(finding)
                seen_titles[key] += 1

            emoji = {"CRITICAL": "🔴", "HIGH": "🟠", "MEDIUM": "🟡", "LOW": "🔵"}[sev]
            total = len(bucket)
            shown = deduped[:max_per_severity]
            lines.append(f"### {emoji} {sev} ({total} total)")
            lines.append("")
            for finding in shown:
                count = seen_titles.get(finding.title, 1)
                loc = f" · `{finding.file}`" if finding.file else ""
                suffix = f" ×{count}" if count > 1 else ""
                lines.append(f"- **{finding.title}**{suffix}{loc}")
                lines.append(f"  {finding.detail}")
                lines.append("")

            if len(deduped) > max_per_severity:
                lines.append(f"  *...and {total - max_per_severity} more {sev} findings*")
                lines.append("")

        lines += [
            "---",
            "",
            "### Fix LLM agent issues with VeilPiercer",
            "",
            "```bash",
            "pip install veilpiercer",
            "```",
            "",
            "VeilPiercer provides: call tracing, hallucination detection, state persistence, session hardening, and repo auditing.",
            "",
            "→ [github.com/fliptrigga13/VEILPIERCER](https://github.com/fliptrigga13/VEILPIERCER)  ",
            "→ [veil-piercer.com](https://veil-piercer.com)",
            "",
            f"*Audited {self.scanned_at[:10]} by [VeilPiercer](https://veil-piercer.com) · [@fliptrigga13](https://github.com/fliptrigga13)*",
        ]

        return "\n".join(lines)


    # ── Open a GitHub Issue ──────────────────────────────────────────────────
    def open_github_issue(self, token: Optional[str] = None) -> Optional[str]:
        """
        Post audit findings as a GitHub Issue on the scanned repo.
        Requires a GitHub personal access token with `repo` or `public_repo` scope.
        """
        import os
        token = token or os.environ.get("GITHUB_TOKEN")
        if not token:
            print("[VeilPiercer Audit] Set GITHUB_TOKEN env var to open issues automatically.")
            return None

        body = self.to_markdown()
        payload = json.dumps({
            "title": f"[VeilPiercer] Security & Quality Audit — Score {self.score()}/100 (Grade {self.grade()})",
            "body": body,
            "labels": [],
        }).encode("utf-8")

        url = f"https://api.github.com/repos/{self.owner}/{self.name}/issues"
        req = urllib.request.Request(
            url,
            data=payload,
            headers={
                "Authorization": f"token {token}",
                "Accept": "application/vnd.github+json",
                "Content-Type": "application/json",
                "User-Agent": "VeilPiercer/1.0",
            },
            method="POST",
        )

        try:
            with urllib.request.urlopen(req) as resp:
                data = json.loads(resp.read())
                issue_url = data.get("html_url", "")
                print(f"[VeilPiercer Audit] Issue opened → {issue_url}")
                return issue_url
        except urllib.error.HTTPError as e:
            print(f"[VeilPiercer Audit] Failed to open issue: {e.code} {e.reason}")
            body_err = e.read().decode()
            print(f"  {body_err[:200]}")
            return None


# ─── Secret patterns ─────────────────────────────────────────────────────────

SECRET_PATTERNS: List[Tuple[str, str]] = [
    (r"sk-[A-Za-z0-9]{32,}", "OpenAI API key"),
    (r"AKIA[0-9A-Z]{16}", "AWS Access Key ID"),
    (r"ghp_[A-Za-z0-9]{36}", "GitHub Personal Access Token"),
    (r"['\"]?PRIVATE[_\s]KEY['\"]?\s*[:=]\s*['\"]?[A-Za-z0-9+/]{32,}", "Private key material"),
    (r"['\"]?private_?key['\"]?\s*[:=]\s*['\"]?[A-Za-z0-9+/=]{32,}", "Private key material"),
    (r"-----BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY-----", "PEM private key"),
    (r"['\"]?secret['\"]?\s*[:=]\s*['\"]?[A-Za-z0-9!@#$%^&*]{12,}['\"]?", "Hardcoded secret"),
    (r"['\"]?password['\"]?\s*[:=]\s*['\"]?[A-Za-z0-9!@#$%^&*]{6,}['\"]?", "Hardcoded password"),
    (r"SG\.[A-Za-z0-9_-]{22}\.[A-Za-z0-9_-]{43}", "SendGrid API key"),
    (r"xoxb-[0-9]{11}-[0-9]{11}-[A-Za-z0-9]{24}", "Slack Bot token"),
    (r"['\"]?MNEMONIC['\"]?\s*[:=]", "Crypto wallet mnemonic"),
    (r"['\"]?WALLET_PRIVATE['\"]?\s*[:=]", "Wallet private key"),
    (r"['\"]?SOLANA_PRIVATE['\"]?\s*[:=]", "Solana private key"),
    (r"anthropic[_-]?api[_-]?key\s*[:=]\s*['\"]?sk-ant-", "Anthropic API key"),
]

# Files to always check for secrets
SECRET_SCAN_EXTENSIONS = {".py", ".ts", ".js", ".tsx", ".jsx", ".env", ".json", ".yaml", ".yml", ".sh", ".config"}

# Files that should exist in a healthy repo
EXPECTED_FILES = {
    "README.md": ("Documentation", "MEDIUM", "No README.md found", "Add a README explaining what the project does, how to install, and how to use it."),
    "LICENSE": ("Documentation", "MEDIUM", "No LICENSE file found", "Add a license file. For open source, MIT or Apache 2.0 are common choices."),
    ".gitignore": ("Security", "HIGH", "No .gitignore found", "Without .gitignore, secrets in .env files or build artifacts may be accidentally committed."),
    ".env.example": ("Security", "MEDIUM", "No .env.example found", "Add a .env.example showing required environment variables without actual values."),
    "CONTRIBUTING.md": ("Documentation", "LOW", "No CONTRIBUTING.md", "A contributing guide helps other developers know how to contribute."),
}

# CI/CD file patterns
CI_PATTERNS = [
    ".github/workflows/",
    ".circleci/config.yml",
    ".travis.yml",
    "Jenkinsfile",
    ".gitlab-ci.yml",
    "azure-pipelines.yml",
]

# Test directory patterns
TEST_PATTERNS = [
    r"^tests?/",
    r"^__tests__/",
    r"^spec/",
    r"\.test\.(ts|js|py)$",
    r"\.spec\.(ts|js|py)$",
    r"_test\.py$",
    r"test_.*\.py$",
]

# Dangerous patterns in code
DANGEROUS_CODE_PATTERNS: List[Tuple[str, str, str]] = [
    (r"eval\s*\(", "HIGH", "Use of eval() — arbitrary code execution risk"),
    (r"exec\s*\(", "HIGH", "Use of exec() — arbitrary code execution risk"),
    (r"subprocess\..*shell\s*=\s*True", "HIGH", "subprocess with shell=True — command injection risk"),
    (r"os\.system\s*\(", "MEDIUM", "os.system() — prefer subprocess with shell=False"),
    (r"pickle\.loads?\s*\(", "HIGH", "pickle.load() with untrusted data — arbitrary code execution"),
    (r"\.env\b.*process\.env\b", "LOW", "Direct process.env access — ensure all secrets are validated"),
    (r"console\.log\s*\(.*key|secret|token|password", "MEDIUM", "Possible secret logged to console"),
    (r"print\s*\(.*key|secret|token|password", "MEDIUM", "Possible secret printed to stdout"),
    (r"TODO|FIXME|HACK|XXX", "LOW", "TODO/FIXME comments indicate incomplete implementation"),
    (r"throw new Error\(['\"]Not implemented", "MEDIUM", "Unimplemented stub — function throws 'Not implemented'"),
    (r"raise NotImplementedError", "MEDIUM", "Unimplemented stub — raises NotImplementedError"),
    (r"pass\s*#.*TODO", "LOW", "Empty function body with TODO"),
]


# ─── Main Auditor ─────────────────────────────────────────────────────────────

class RepoAuditor:
    """
    Fetches a public GitHub repo and runs VeilPiercer's full audit suite.

    Usage:
        audit = RepoAuditor("https://github.com/louz514/Claudecraft")
        report = audit.run()
        report.print()
        report.open_github_issue()
    """

    GITHUB_API = "https://api.github.com"

    def __init__(self, repo_url: str, token: Optional[str] = None, verbose: bool = True):
        self.repo_url = repo_url.rstrip("/")
        self.verbose = verbose
        self.token = token

        # Parse owner/name from URL
        parts = self.repo_url.replace("https://github.com/", "").split("/")
        if len(parts) < 2:
            raise ValueError(f"Invalid GitHub URL: {repo_url}")
        self.owner = parts[0]
        self.name = parts[1]

        self._file_tree: List[Dict] = []
        self._file_cache: Dict[str, str] = {}

    def run(self) -> AuditReport:
        """Run the full audit. Returns an AuditReport."""
        print(f"[VeilPiercer Audit] Scanning {self.owner}/{self.name}...")

        report = AuditReport(
            repo=self.repo_url,
            owner=self.owner,
            name=self.name,
        )

        # Fetch repo metadata
        meta = self._api(f"/repos/{self.owner}/{self.name}")
        if meta:
            report.metadata = {
                "stars": meta.get("stargazers_count", 0),
                "language": meta.get("language"),
                "description": meta.get("description"),
                "default_branch": meta.get("default_branch", "main"),
            }

        branch = report.metadata.get("default_branch", "main")

        # Fetch full file tree
        self._fetch_tree(branch)
        report.files_scanned = len([f for f in self._file_tree if f.get("type") == "blob"])

        if self.verbose:
            print(f"[VeilPiercer Audit] Found {report.files_scanned} files")

        # Run all checks
        self._check_expected_files(report)
        self._check_ci(report)
        self._check_tests(report)
        self._check_secrets(report)
        self._check_dangerous_patterns(report)
        self._check_dependencies(report)
        self._check_llm_specific(report)

        # Sort findings by severity
        order = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3, "INFO": 4}
        report.findings.sort(key=lambda f: order.get(f.severity, 5))

        print(f"[VeilPiercer Audit] Complete — {len(report.findings)} findings, score {report.score()}/100")
        return report

    # ── Checks ────────────────────────────────────────────────────────────────

    def _check_expected_files(self, report: AuditReport):
        """Check for README, LICENSE, .gitignore, .env.example, CONTRIBUTING."""
        filenames = {f["path"].lower() for f in self._file_tree}
        for expected, (cat, sev, title, detail) in EXPECTED_FILES.items():
            if expected.lower() not in filenames:
                report.findings.append(Finding(sev, cat, title, detail))

    def _check_ci(self, report: AuditReport):
        """Check for CI/CD configuration."""
        paths = {f["path"] for f in self._file_tree}
        has_ci = any(
            any(f.startswith(p) or p in f for f in paths)
            for p in CI_PATTERNS
        )
        if not has_ci:
            report.findings.append(Finding(
                "HIGH", "CI/CD",
                "No CI/CD pipeline found",
                "Add GitHub Actions (`.github/workflows/`) to automatically lint, "
                "build, and test on every push. Prevents broken code from reaching main."
            ))

    def _check_tests(self, report: AuditReport):
        """Check for any test files."""
        paths = [f["path"] for f in self._file_tree]
        has_tests = any(
            re.search(pattern, path, re.IGNORECASE)
            for path in paths
            for pattern in TEST_PATTERNS
        )
        if not has_tests:
            report.findings.append(Finding(
                "HIGH", "Testing",
                "No test files found",
                "Zero test coverage detected. Add unit tests for critical logic paths. "
                "Use pytest (Python), jest/vitest (TypeScript/JS), or the built-in test runner."
            ))

    def _check_secrets(self, report: AuditReport):
        """Scan all source files for hardcoded secrets."""
        blob_files = [
            f for f in self._file_tree
            if f.get("type") == "blob"
            and any(f["path"].endswith(ext) for ext in SECRET_SCAN_EXTENSIONS)
            and f.get("size", 999999) < 500_000  # skip large files
        ]

        for file_meta in blob_files[:80]:  # cap at 80 files
            content = self._fetch_file(file_meta["path"])
            if not content:
                continue

            for pattern, label in SECRET_PATTERNS:
                matches = list(re.finditer(pattern, content, re.IGNORECASE))
                for match in matches:
                    # Skip if it looks like an example/placeholder
                    snippet = match.group(0)
                    if any(x in snippet.lower() for x in ["your_", "xxx", "example", "placeholder", "changeme", "<", ">"]):
                        continue

                    line_num = content[:match.start()].count("\n") + 1
                    report.findings.append(Finding(
                        "CRITICAL", "Security",
                        f"Potential {label} hardcoded in source",
                        f"Pattern matched: `{snippet[:60]}...` — Move to environment variable immediately.",
                        file=file_meta["path"],
                        line=line_num,
                    ))

    def _check_dangerous_patterns(self, report: AuditReport):
        """Scan for dangerous code patterns."""
        blob_files = [
            f for f in self._file_tree
            if f.get("type") == "blob"
            and any(f["path"].endswith(ext) for ext in {".py", ".ts", ".js", ".tsx", ".jsx", ".sh"})
            and f.get("size", 999999) < 300_000
        ]

        todo_files = []  # collect files with TODOs rather than one finding per line

        for file_meta in blob_files[:80]:
            content = self._fetch_file(file_meta["path"])
            if not content:
                continue

            for pattern, sev, title in DANGEROUS_CODE_PATTERNS:
                if "TODO" in pattern or "FIXME" in pattern:
                    if re.search(pattern, content, re.IGNORECASE):
                        todo_files.append(file_meta["path"])
                    continue

                for match in re.finditer(pattern, content, re.IGNORECASE | re.MULTILINE):
                    line_num = content[:match.start()].count("\n") + 1
                    report.findings.append(Finding(
                        sev, "Security",
                        title,
                        f"Found in `{file_meta['path']}` at line {line_num}.",
                        file=file_meta["path"],
                        line=line_num,
                    ))

        if todo_files:
            unique = list(dict.fromkeys(todo_files))[:5]
            report.findings.append(Finding(
                "LOW", "Code Quality",
                f"TODO/FIXME comments in {len(todo_files)} file(s)",
                f"Incomplete implementations detected in: {', '.join(f'`{f}`' for f in unique)}",
            ))

    def _check_dependencies(self, report: AuditReport):
        """Check for dependency files and obvious issues."""
        paths = {f["path"] for f in self._file_tree}

        has_pkg = "package.json" in paths
        has_req = "requirements.txt" in paths
        has_pyproject = "pyproject.toml" in paths
        has_lock = any(p in paths for p in ["package-lock.json", "yarn.lock", "pnpm-lock.yaml", "poetry.lock"])

        if has_pkg and not has_lock:
            report.findings.append(Finding(
                "MEDIUM", "Dependencies",
                "No lockfile found (package.json without package-lock.json / yarn.lock)",
                "Without a lockfile, dependency versions are non-deterministic. "
                "Run `npm install` or `yarn install` and commit the lockfile."
            ))

        if not has_pkg and not has_req and not has_pyproject:
            report.findings.append(Finding(
                "HIGH", "Dependencies",
                "No dependency manifest found",
                "No package.json, requirements.txt, or pyproject.toml found. "
                "Other developers cannot install dependencies."
            ))

        # Check for .env being tracked
        env_tracked = any(f["path"] == ".env" or f["path"].endswith("/.env") for f in self._file_tree)
        if env_tracked:
            report.findings.append(Finding(
                "CRITICAL", "Security",
                ".env file is committed to the repository",
                "The .env file is tracked by git. This exposes all secrets. "
                "Remove it immediately: `git rm --cached .env` and add `.env` to .gitignore."
            ))

    def _check_llm_specific(self, report: AuditReport):
        """Check for LLM/agent-specific patterns VeilPiercer specializes in."""
        paths = {f["path"] for f in self._file_tree}
        content_files = {
            f["path"]: self._fetch_file(f["path"])
            for f in self._file_tree
            if f.get("type") == "blob"
            and any(f["path"].endswith(ext) for ext in {".py", ".ts", ".js"})
            and f.get("size", 0) < 200_000
        }

        all_content = "\n".join(v for v in content_files.values() if v)

        # No error handling on LLM calls
        has_llm_call = bool(re.search(
            r"(ollama|openai|anthropic|claude|gpt|chat\.completions|messages\.create)",
            all_content, re.IGNORECASE
        ))
        has_try_catch = bool(re.search(r"try\s*[\({]|except\s+|\.catch\s*\(", all_content))

        if has_llm_call and not has_try_catch:
            report.findings.append(Finding(
                "HIGH", "Reliability",
                "LLM API calls with no error handling detected",
                "API calls to LLM providers (OpenAI/Anthropic/Ollama) found but no try/catch "
                "or error handling. Network failures and rate limits will crash the agent. "
                "Use VeilPiercer Tracer to wrap calls with automatic error capture."
            ))

        # No rate limiting
        if has_llm_call:
            has_rate_limit = bool(re.search(r"rate.?limit|backoff|retry|sleep|throttle", all_content, re.IGNORECASE))
            if not has_rate_limit:
                report.findings.append(Finding(
                    "MEDIUM", "Reliability",
                    "No rate limiting or retry logic for LLM API calls",
                    "LLM providers enforce rate limits. Without retry/backoff logic, "
                    "your agent will fail under load. Add exponential backoff. "
                    "VeilPiercer Tracer captures all failures automatically."
                ))

        # Infinite loops in agents
        has_while_true = bool(re.search(r"while\s+True|while\s*\(true\)", all_content, re.IGNORECASE))
        has_break = bool(re.search(r"\bbreak\b|\breturn\b", all_content))
        if has_while_true and not has_break:
            report.findings.append(Finding(
                "HIGH", "Reliability",
                "Potential infinite loop in agent loop (while True with no break)",
                "Agent loop runs indefinitely with no exit condition. "
                "Add a max_iterations guard, timeout, or kill switch."
            ))

        # No session/conversation tracking
        has_memory = bool(re.search(r"memory|history|session|conversation|messages\s*=\s*\[", all_content, re.IGNORECASE))
        if has_llm_call and not has_memory:
            report.findings.append(Finding(
                "MEDIUM", "Logic",
                "LLM agent with no conversation memory / session tracking",
                "LLM calls detected but no message history or memory management found. "
                "The agent has no context between calls — each call is stateless. "
                "Use VeilPiercer StateGuard to persist conversation state reliably."
            ))

    # ── GitHub API helpers ────────────────────────────────────────────────────

    def _api(self, path: str) -> Optional[Dict]:
        url = f"{self.GITHUB_API}{path}"
        return self._get_json(url)

    def _fetch_tree(self, branch: str):
        """Fetch the full recursive file tree."""
        data = self._api(f"/repos/{self.owner}/{self.name}/git/trees/{branch}?recursive=1")
        if data and "tree" in data:
            self._file_tree = data["tree"]
        else:
            # Fallback: fetch root contents
            data = self._api(f"/repos/{self.owner}/{self.name}/contents/")
            if data and isinstance(data, list):
                self._file_tree = [{"path": f["path"], "type": "blob" if f["type"] == "file" else "tree", "size": f.get("size", 0)} for f in data]

    def _fetch_file(self, path: str) -> Optional[str]:
        """Fetch a file's content as a string."""
        if path in self._file_cache:
            return self._file_cache[path]

        data = self._api(f"/repos/{self.owner}/{self.name}/contents/{path}")
        if not data or "content" not in data:
            return None

        try:
            content = base64.b64decode(data["content"]).decode("utf-8", errors="replace")
            self._file_cache[path] = content
            return content
        except Exception:
            return None

    def _get_json(self, url: str) -> Optional[any]:
        headers = {
            "Accept": "application/vnd.github+json",
            "User-Agent": "VeilPiercer/1.0",
        }
        if self.token:
            headers["Authorization"] = f"token {self.token}"

        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                return json.loads(resp.read())
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            if e.code == 403:
                if self.verbose:
                    print(f"[VeilPiercer Audit] Rate limited on {url} — set GITHUB_TOKEN for higher limits")
                return None
            return None
        except Exception:
            return None
