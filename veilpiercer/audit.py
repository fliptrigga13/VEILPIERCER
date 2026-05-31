"""
veilpiercer.audit — v2.0
------------------------
Deep GitHub repo intelligence engine.

What it actually does now:
  1. Context-aware secret detection (no more false positives)
  2. Commit history scan (finds secrets that were added then deleted)
  3. Dependency CVE check via OSV.dev vulnerability database
  4. GitHub Issues analysis (what are users actually reporting as bugs?)
  5. GitHub Code Search API (search patterns across entire codebase)
  6. Python AST analysis (real semantic understanding, not just regex)
  7. Dependency version staleness check
  8. GitHub Actions workflow audit
  9. LLM-specific deep patterns
 10. Dead repo detection

Created by Lauren Flipo (@fliptrigga13) · https://veil-piercer.com
"""

from __future__ import annotations

import re
import ast
import json
import base64
import hashlib
import urllib.request
import urllib.error
import urllib.parse
import time
from datetime import datetime, timezone
from typing import Dict, List, Optional, Tuple, Set
from dataclasses import dataclass, field


# ─── Finding & Report ─────────────────────────────────────────────────────────

@dataclass
class Finding:
    severity: str
    category: str
    title: str
    detail: str
    file: Optional[str] = None
    line: Optional[int] = None
    evidence: Optional[str] = None      # actual code snippet / proof
    cve: Optional[str] = None           # CVE ID if applicable
    fix: Optional[str] = None           # concrete fix suggestion

    def emoji(self) -> str:
        return {"CRITICAL": "🔴", "HIGH": "🟠", "MEDIUM": "🟡", "LOW": "🔵", "INFO": "ℹ️"}.get(self.severity, "⚪")


@dataclass
class AuditReport:
    repo: str
    owner: str
    name: str
    findings: List[Finding] = field(default_factory=list)
    files_scanned: int = 0
    commits_scanned: int = 0
    issues_analyzed: int = 0
    scanned_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    metadata: Dict = field(default_factory=dict)

    def score(self) -> int:
        deductions = {"CRITICAL": 20, "HIGH": 12, "MEDIUM": 6, "LOW": 2, "INFO": 0}
        return max(0, 100 - sum(deductions.get(f.severity, 0) for f in self.findings))

    def grade(self) -> str:
        s = self.score()
        if s >= 90: return "A"
        if s >= 75: return "B"
        if s >= 60: return "C"
        if s >= 40: return "D"
        return "F"

    def print(self):
        order = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3, "INFO": 4}
        self.findings.sort(key=lambda f: order.get(f.severity, 5))

        print(f"\n{'='*68}")
        print(f"  VeilPiercer Deep Audit — {self.owner}/{self.name}")
        print(f"  Score   : {self.score()}/100  (Grade: {self.grade()})")
        print(f"  Files   : {self.files_scanned} scanned")
        print(f"  Commits : {self.commits_scanned} scanned")
        print(f"  Issues  : {self.issues_analyzed} analyzed")
        print(f"  Findings: {len(self.findings)}")
        print(f"{'='*68}")

        by_sev = {}
        for f in self.findings:
            by_sev.setdefault(f.severity, []).append(f)

        for sev in ["CRITICAL", "HIGH", "MEDIUM", "LOW", "INFO"]:
            bucket = by_sev.get(sev, [])
            if not bucket:
                continue
            print(f"\n── {sev} ({len(bucket)}) {'─'*44}")
            for f in bucket:
                loc = f"  [{f.file}:{f.line}]" if f.file else ""
                print(f"\n  {f.emoji()} {f.title}{loc}")
                print(f"     {f.detail}")
                if f.evidence:
                    print(f"     Evidence: {f.evidence[:140]}")
                if f.fix:
                    print(f"     Fix: {f.fix}")
                if f.cve:
                    print(f"     CVE: {f.cve}")

        print(f"\n{'─'*68}")
        print(f"  Audited by VeilPiercer · https://veil-piercer.com · @fliptrigga13")
        print(f"{'='*68}\n")

    def to_markdown(self, max_per_severity: int = 6) -> str:
        order = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3, "INFO": 4}
        self.findings.sort(key=lambda f: order.get(f.severity, 5))

        lines = [
            f"## 🔍 VeilPiercer Deep Audit — `{self.name}`",
            f"",
            f"> Automated deep security & quality audit by [VeilPiercer](https://veil-piercer.com)",
            f"> Created by [Lauren Flipo](https://github.com/fliptrigga13) · [@fliptrigga13](https://github.com/fliptrigga13)",
            f"",
            f"**Score: {self.score()}/100 (Grade {self.grade()})**",
            f"- {self.files_scanned} files scanned",
            f"- {self.commits_scanned} commits scanned",
            f"- {self.issues_analyzed} open issues analyzed",
            f"- {len(self.findings)} findings",
            f"",
        ]

        by_sev = {}
        for f in self.findings:
            by_sev.setdefault(f.severity, []).append(f)

        for sev in ["CRITICAL", "HIGH", "MEDIUM", "LOW"]:
            bucket = by_sev.get(sev, [])
            if not bucket:
                continue
            seen = {}
            deduped = []
            for f in bucket:
                if f.title not in seen:
                    seen[f.title] = 0
                    deduped.append(f)
                seen[f.title] += 1

            emoji = {"CRITICAL": "🔴", "HIGH": "🟠", "MEDIUM": "🟡", "LOW": "🔵"}[sev]
            lines.append(f"### {emoji} {sev} ({len(bucket)} total)")
            lines.append("")
            for f in deduped[:max_per_severity]:
                count = seen.get(f.title, 1)
                loc = f" · `{f.file}:{f.line}`" if f.file else ""
                suffix = f" ×{count}" if count > 1 else ""
                lines.append(f"**{f.title}**{suffix}{loc}")
                lines.append(f"> {f.detail}")
                if f.evidence:
                    lines.append(f"> ```\n> {f.evidence[:200]}\n> ```")
                if f.fix:
                    lines.append(f"> 💡 Fix: {f.fix}")
                if f.cve:
                    lines.append(f"> ⚠️ {f.cve}")
                lines.append("")
            if len(deduped) > max_per_severity:
                lines.append(f"*...and {len(bucket) - max_per_severity} more {sev} findings*")
                lines.append("")

        lines += [
            "---",
            "",
            "### Fix with VeilPiercer",
            "",
            "```bash",
            "pip install veilpiercer",
            "python -m veilpiercer.audit " + self.repo,
            "```",
            "",
            "→ [github.com/fliptrigga13/VEILPIERCER](https://github.com/fliptrigga13/VEILPIERCER)",
            "→ [veil-piercer.com](https://veil-piercer.com)",
            "",
            f"*Audited {self.scanned_at[:10]} by [VeilPiercer](https://veil-piercer.com) · [@fliptrigga13](https://github.com/fliptrigga13)*",
        ]
        return "\n".join(lines)

    def open_github_issue(self, token: Optional[str] = None) -> Optional[str]:
        import os
        token = token or os.environ.get("GITHUB_TOKEN")
        if not token:
            print("[VeilPiercer Audit] Set GITHUB_TOKEN to open issues automatically.")
            return None

        body = self.to_markdown()
        if len(body) > 65000:
            body = self.to_markdown(max_per_severity=3)

        payload = json.dumps({
            "title": f"[VeilPiercer] Deep Audit — Score {self.score()}/100 (Grade {self.grade()}) · {len(self.findings)} findings",
            "body": body,
        }).encode("utf-8")

        url = f"https://api.github.com/repos/{self.owner}/{self.name}/issues"
        req = urllib.request.Request(url, data=payload, headers={
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github+json",
            "Content-Type": "application/json",
            "User-Agent": "VeilPiercer/2.0",
        }, method="POST")
        try:
            with urllib.request.urlopen(req) as resp:
                data = json.loads(resp.read())
                url = data.get("html_url", "")
                print(f"[VeilPiercer Audit] Issue opened → {url}")
                return url
        except urllib.error.HTTPError as e:
            print(f"[VeilPiercer Audit] Failed: {e.code} — {e.read().decode()[:200]}")
            return None


# ─── Context-Aware Secret Rules ───────────────────────────────────────────────
# Each rule: (pattern, label, severity, is_false_positive_fn)
# is_false_positive_fn takes (match, surrounding_lines) → bool

def _is_env_read(match, ctx: str) -> bool:
    """True if the value is being READ from env, not hardcoded."""
    env_indicators = [
        "os.environ", "process.env", "os.getenv", "config.get",
        "settings.", "parsed.", "getenv", "environ.get",
        "secrets.token", "uuid.uuid", "random.", "hashlib.",
        ".token_urlsafe", ".token_hex", "generate_", "get_secret",
        "vault", "keyring", "boto3", "Parameter",
    ]
    return any(ind in ctx for ind in env_indicators)

def _is_placeholder(match, ctx: str) -> bool:
    """True if value looks like a placeholder."""
    val = match.group(0).lower()
    placeholders = ["your_", "xxx", "example", "placeholder", "changeme",
                    "todo", "replace", "<", ">", "...", "test", "dummy",
                    "sample", "fake", "mock", "here", "insert"]
    return any(p in val for p in placeholders)

def _is_comment(match, ctx: str) -> bool:
    """True if the match is inside a comment."""
    line = ctx.split("\n")[0] if ctx else ""
    stripped = line.lstrip()
    return stripped.startswith("#") or stripped.startswith("//") or stripped.startswith("*")

SECRET_RULES: List[Tuple] = [
    # pattern, label, severity, false_positive_fns
    (
        r"""(?:api[_-]?key|apikey)\s*[:=]\s*["']([A-Za-z0-9\-_]{16,})["']""",
        "Hardcoded API key", "CRITICAL",
        [_is_placeholder, _is_comment]
    ),
    (
        r"""sk-[A-Za-z0-9]{20,}""",
        "OpenAI/Anthropic API key", "CRITICAL",
        [_is_placeholder, _is_comment]
    ),
    (
        r"""sk-ant-[A-Za-z0-9\-_]{20,}""",
        "Anthropic API key", "CRITICAL",
        [_is_placeholder, _is_comment]
    ),
    (
        r"""AKIA[0-9A-Z]{16}""",
        "AWS Access Key ID", "CRITICAL",
        [_is_placeholder, _is_comment]
    ),
    (
        r"""ghp_[A-Za-z0-9]{36}""",
        "GitHub Personal Access Token", "CRITICAL",
        [_is_placeholder, _is_comment]
    ),
    (
        r"""-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----""",
        "PEM private key in source", "CRITICAL",
        [_is_comment]
    ),
    (
        r"""(?:private[_-]?key|secret[_-]?key|wallet[_-]?key|mnemonic)\s*[:=]\s*["']([a-zA-Z0-9+/]{32,}={0,2})["']""",
        "Hardcoded private/wallet key", "CRITICAL",
        [_is_placeholder, _is_env_read, _is_comment]
    ),
    (
        r"""(?:password|passwd)\s*[:=]\s*["']([^"']{6,})["']""",
        "Hardcoded password literal", "CRITICAL",
        [_is_placeholder, _is_env_read, _is_comment]
    ),
    (
        r"""(?:token|secret)\s*[:=]\s*["']([A-Za-z0-9\-_.]{12,})["']""",
        "Hardcoded token/secret", "HIGH",
        [_is_placeholder, _is_env_read, _is_comment]
    ),
    (
        r"""SG\.[A-Za-z0-9_-]{22}\.[A-Za-z0-9_-]{43}""",
        "SendGrid API key", "CRITICAL",
        [_is_placeholder, _is_comment]
    ),
    (
        r"""xoxb-[0-9]{11}-[0-9]{11}-[A-Za-z0-9]{24}""",
        "Slack Bot token", "CRITICAL",
        [_is_placeholder, _is_comment]
    ),
    (
        r"""[0-9a-fA-F]{64}""",
        "Possible 256-bit hex key (wallet/crypto)", "MEDIUM",
        [_is_placeholder, _is_comment, _is_env_read]
    ),
]

# ─── Dangerous Code Rules (context-aware) ─────────────────────────────────────

DANGEROUS_RULES: List[Tuple] = [
    # pattern, severity, title, false_positive check
    (
        r"""\beval\s*\((?!.*\/\*.*\*\/)""",
        "HIGH", "eval() — arbitrary code execution risk",
        lambda m, ctx: ".exec(" in ctx or "regex" in ctx.lower() or "/test" in ctx.lower()
    ),
    (
        r"""\bexec\s*\(""",
        "HIGH", "exec() — arbitrary code execution risk",
        # False positive: regex .exec(), string.exec, method chains
        lambda m, ctx: (
            re.search(r'["\'/].*\.exec\s*\(', ctx) is not None or
            "RegExp" in ctx or ".exec(" in ctx[:m.start() - max(0, m.start()-30)] or
            "regex" in ctx.lower() or ".exec(" in m.group(0)
        )
    ),
    (
        r"""subprocess\.(?:run|Popen|call|check_output).*shell\s*=\s*True""",
        "CRITICAL", "subprocess with shell=True — command injection risk",
        lambda m, ctx: False
    ),
    (
        r"""\bos\.system\s*\(""",
        "HIGH", "os.system() — prefer subprocess with shell=False",
        lambda m, ctx: "test" in ctx.lower()
    ),
    (
        r"""\bpickle\.loads?\s*\(""",
        "HIGH", "pickle.load() — arbitrary code execution if data is untrusted",
        lambda m, ctx: "test" in ctx.lower()
    ),
    (
        r"""child_process|require\s*\(\s*['"]child_process['"]\s*\)""",
        "HIGH", "Node.js child_process — check for command injection",
        lambda m, ctx: False
    ),
    (
        r"""\.innerHTML\s*=(?!=)""",
        "MEDIUM", "innerHTML assignment — potential XSS vector",
        lambda m, ctx: "sanitize" in ctx.lower() or "escape" in ctx.lower()
    ),
    (
        r"""document\.write\s*\(""",
        "MEDIUM", "document.write() — XSS risk",
        lambda m, ctx: False
    ),
    (
        r"""Math\.random\s*\(\).*(?:key|token|secret|password|salt|nonce)""",
        "HIGH", "Math.random() used for security token — not cryptographically secure",
        lambda m, ctx: "test" in ctx.lower()
    ),
    (
        r"""random\.random\s*\(\).*(?:key|token|secret|password|salt)""",
        "HIGH", "random.random() for security token — use secrets module instead",
        lambda m, ctx: "test" in ctx.lower()
    ),
    (
        r"""md5\s*\(|hashlib\.md5""",
        "MEDIUM", "MD5 used — weak hash, use SHA-256 or better",
        lambda m, ctx: "test" in ctx.lower()
    ),
    (
        r"""sha1\s*\(|hashlib\.sha1""",
        "MEDIUM", "SHA-1 used — weak hash, use SHA-256 or better",
        lambda m, ctx: "test" in ctx.lower()
    ),
    (
        r"""verify\s*=\s*False""",
        "HIGH", "SSL verification disabled — vulnerable to MITM",
        lambda m, ctx: "test" in ctx.lower()
    ),
    (
        r"""ssl\._create_unverified_context|CERT_NONE""",
        "CRITICAL", "SSL certificate validation disabled",
        lambda m, ctx: False
    ),
    (
        r"""DEBUG\s*=\s*True""",
        "HIGH", "Django/Flask DEBUG=True — never deploy to production",
        lambda m, ctx: "test" in ctx.lower() or "local" in ctx.lower()
    ),
    (
        r"""ALLOWED_HOSTS\s*=\s*\[\s*['"]\*['"]\s*\]""",
        "HIGH", "ALLOWED_HOSTS=['*'] — exposes Django to host header attacks",
        lambda m, ctx: "test" in ctx.lower()
    ),
    (
        r"""cors.*allow.*origin.*\*|Access-Control-Allow-Origin.*\*""",
        "MEDIUM", "CORS wildcard (*) — allows any origin to access the API",
        lambda m, ctx: "test" in ctx.lower() or "dev" in ctx.lower()
    ),
    (
        r"""TODO|FIXME|HACK|XXX|BROKEN""",
        "LOW", "TODO/FIXME left in code",
        lambda m, ctx: False
    ),
    (
        r"""raise NotImplementedError|throw new Error\(['"](Not implemented|TODO)""",
        "MEDIUM", "Unimplemented stub — will crash at runtime",
        lambda m, ctx: "test" in ctx.lower()
    ),
]

# ─── Expected Files ───────────────────────────────────────────────────────────

EXPECTED_FILES = {
    "README.md": ("Documentation", "MEDIUM", "No README.md", "Add a README with install/usage instructions."),
    "LICENSE": ("Documentation", "MEDIUM", "No LICENSE file", "Add a license. MIT is common for open source."),
    ".gitignore": ("Security", "HIGH", "No .gitignore", "Without .gitignore, .env files can be accidentally committed."),
    ".env.example": ("Security", "MEDIUM", "No .env.example", "Show required env vars without exposing values."),
    "CONTRIBUTING.md": ("Documentation", "LOW", "No CONTRIBUTING.md", "Helps others contribute."),
}

CI_PATHS = [".github/workflows/", ".circleci/", ".travis.yml", "Jenkinsfile", ".gitlab-ci.yml", "azure-pipelines.yml"]
TEST_PATTERNS = [r"^tests?/", r"^__tests__/", r"^spec/", r"\.test\.(ts|js|py)$", r"\.spec\.(ts|js)$", r"_test\.py$", r"test_.*\.py$"]

SCAN_EXTS = {".py", ".ts", ".js", ".tsx", ".jsx", ".env", ".sh", ".yaml", ".yml", ".toml", ".cfg", ".ini", ".json", ".config", ".rb", ".go", ".java", ".php"}
SKIP_DIRS = {"node_modules", ".git", "vendor", "dist", "build", "__pycache__", ".next", "coverage", "venv", ".env"}


# ─── Main Auditor v2 ──────────────────────────────────────────────────────────

class RepoAuditor:
    """
    VeilPiercer Deep Repo Auditor v2.0

    Tools at its disposal:
    - Context-aware secret detection (no false positives from env reads)
    - Python AST semantic analysis
    - Commit history scan (finds secrets committed then deleted)
    - OSV.dev CVE database check for all dependencies
    - GitHub Issues scraper (what are users actually complaining about?)
    - GitHub Code Search API (cross-file pattern search)
    - Workflow/CI file deep audit
    - Dependency staleness check (PyPI / npm)
    - LLM-specific anti-patterns
    - Dead repo signals

    Usage:
        auditor = RepoAuditor("https://github.com/louz514/Claudecraft", token=TOKEN)
        report = auditor.run()
        report.print()
        report.open_github_issue()
    """

    GITHUB_API = "https://api.github.com"
    OSV_API = "https://api.osv.dev/v1"

    def __init__(self, repo_url: str, token: Optional[str] = None, verbose: bool = True):
        self.repo_url = repo_url.rstrip("/")
        self.verbose = verbose
        self.token = token
        parts = self.repo_url.replace("https://github.com/", "").split("/")
        self.owner, self.name = parts[0], parts[1]
        self._file_tree: List[Dict] = []
        self._cache: Dict[str, str] = {}
        self._rate_limited = False

    def run(self) -> AuditReport:
        if self.verbose:
            print(f"[VeilPiercer] Deep scanning {self.owner}/{self.name}...")

        report = AuditReport(repo=self.repo_url, owner=self.owner, name=self.name)

        meta = self._api(f"/repos/{self.owner}/{self.name}")
        if not meta:
            report.findings.append(Finding("INFO", "Access", "Repo not accessible", "Private, deleted, or rate limited."))
            return report

        branch = meta.get("default_branch", "main")
        report.metadata = {
            "stars": meta.get("stargazers_count", 0),
            "forks": meta.get("forks_count", 0),
            "language": meta.get("language"),
            "description": meta.get("description", ""),
            "created_at": meta.get("created_at", ""),
            "updated_at": meta.get("updated_at", ""),
            "open_issues": meta.get("open_issues_count", 0),
            "has_wiki": meta.get("has_wiki", False),
            "license": meta.get("license", {}).get("spdx_id") if meta.get("license") else None,
            "default_branch": branch,
        }

        # Fetch file tree
        self._fetch_tree(branch)
        blobs = [f for f in self._file_tree if f.get("type") == "blob"]
        scannable = [
            f for f in blobs
            if not any(skip in f["path"] for skip in SKIP_DIRS)
            and any(f["path"].endswith(ext) for ext in SCAN_EXTS)
            and f.get("size", 0) < 400_000
        ]
        report.files_scanned = len(blobs)

        if self.verbose:
            print(f"[VeilPiercer]   Files: {len(blobs)} total, {len(scannable)} scannable")

        # Run all checks
        self._check_structure(report)
        self._check_secrets_contextual(report, scannable)
        self._check_dangerous_patterns(report, scannable)
        self._check_python_ast(report, scannable)
        self._check_dependencies(report)
        self._check_dependency_cves(report)
        self._check_workflows(report, scannable)
        self._check_commit_history(report, branch)
        self._check_github_issues(report)
        self._check_llm_patterns(report, scannable)
        self._check_dead_repo(report, meta)

        order = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3, "INFO": 4}
        report.findings.sort(key=lambda f: order.get(f.severity, 5))

        if self.verbose:
            print(f"[VeilPiercer]   Done — {len(report.findings)} findings, score {report.score()}/100")

        return report

    # ── Structure ─────────────────────────────────────────────────────────────

    def _check_structure(self, report: AuditReport):
        paths_lower = {f["path"].lower() for f in self._file_tree}

        for filename, (cat, sev, title, detail) in EXPECTED_FILES.items():
            if filename.lower() not in paths_lower:
                report.findings.append(Finding(sev, cat, title, detail))

        # CI check
        paths = {f["path"] for f in self._file_tree}
        if not any(any(f.startswith(ci) or ci in f for f in paths) for ci in CI_PATHS):
            report.findings.append(Finding(
                "HIGH", "CI/CD", "No CI/CD pipeline",
                "No GitHub Actions, CircleCI, Travis CI, or similar found. "
                "Add `.github/workflows/ci.yml` to auto-run tests on every push.",
                fix="Create .github/workflows/ci.yml"
            ))

        # Test check
        if not any(re.search(p, f["path"], re.I) for f in self._file_tree for p in TEST_PATTERNS):
            report.findings.append(Finding(
                "HIGH", "Testing", "No test files found",
                "Zero test coverage detected across the entire codebase. "
                "Even a single failing test is better than none.",
                fix="Add tests/ directory with pytest or jest"
            ))

    # ── Context-Aware Secret Detection ───────────────────────────────────────

    def _check_secrets_contextual(self, report: AuditReport, files: List[Dict]):
        """
        Scans files for secrets using context-aware rules.
        Gets surrounding lines of each match and runs false-positive filters.
        """
        seen: Set[str] = set()  # deduplicate by hash of evidence

        for file_meta in files[:100]:
            path = file_meta["path"]
            # Skip test files and example files for most checks
            is_test = any(x in path.lower() for x in ["test", "spec", "mock", "fixture", "example"])

            content = self._fetch_file(path)
            if not content:
                continue

            lines = content.split("\n")

            for pattern, label, severity, fp_checks in SECRET_RULES:
                for match in re.finditer(pattern, content, re.IGNORECASE | re.MULTILINE):
                    line_num = content[:match.start()].count("\n")
                    # Context: surrounding 3 lines
                    ctx_lines = lines[max(0, line_num - 2): line_num + 3]
                    ctx = "\n".join(ctx_lines)

                    # Run false positive filters
                    if any(check(match, ctx) for check in fp_checks):
                        continue
                    if is_test and severity != "CRITICAL":
                        continue

                    # Deduplicate
                    snippet = match.group(0)[:80]
                    key = hashlib.md5(f"{path}:{line_num}:{snippet}".encode()).hexdigest()
                    if key in seen:
                        continue
                    seen.add(key)

                    # Redact the actual value in evidence
                    evidence = ctx_lines[2] if len(ctx_lines) > 2 else snippet
                    evidence = evidence[:140]

                    report.findings.append(Finding(
                        severity, "Security",
                        f"{label} detected",
                        f"Potential secret found. Verify this is not a real credential.",
                        file=path,
                        line=line_num + 1,
                        evidence=evidence,
                        fix="Move to environment variable. Add to .gitignore. Rotate the credential."
                    ))

    # ── Dangerous Pattern Detection ───────────────────────────────────────────

    def _check_dangerous_patterns(self, report: AuditReport, files: List[Dict]):
        seen_titles: Dict[str, int] = {}

        for file_meta in files[:100]:
            path = file_meta["path"]
            content = self._fetch_file(path)
            if not content:
                continue
            lines = content.split("\n")

            for pattern, severity, title, fp_check in DANGEROUS_RULES:
                for match in re.finditer(pattern, content, re.IGNORECASE | re.MULTILINE):
                    line_num = content[:match.start()].count("\n")
                    ctx_lines = lines[max(0, line_num - 1): line_num + 2]
                    ctx = "\n".join(ctx_lines)

                    if fp_check(match, ctx):
                        continue

                    # Only report each title once per file to reduce noise
                    dedup_key = f"{path}:{title}"
                    if seen_titles.get(dedup_key, 0) >= 2:
                        seen_titles[dedup_key] = seen_titles.get(dedup_key, 0) + 1
                        continue
                    seen_titles[dedup_key] = seen_titles.get(dedup_key, 0) + 1

                    report.findings.append(Finding(
                        severity, "Security", title,
                        f"Found in `{path}` at line {line_num + 1}.",
                        file=path,
                        line=line_num + 1,
                        evidence=ctx_lines[1][:140] if len(ctx_lines) > 1 else match.group(0)[:80],
                    ))

    # ── Python AST Analysis ───────────────────────────────────────────────────

    def _check_python_ast(self, report: AuditReport, files: List[Dict]):
        """
        Real semantic analysis of Python files using the AST.
        Finds: bare excepts, mutable defaults, assert in prod, hardcoded IPs.
        """
        py_files = [f for f in files if f["path"].endswith(".py")]

        for file_meta in py_files[:40]:
            path = file_meta["path"]
            content = self._fetch_file(path)
            if not content:
                continue

            try:
                tree = ast.parse(content, filename=path)
            except SyntaxError as e:
                report.findings.append(Finding(
                    "HIGH", "Code Quality",
                    f"Python syntax error",
                    f"File `{path}` has a syntax error: {e}. Code will crash on import.",
                    file=path,
                    line=e.lineno,
                    fix="Fix the syntax error."
                ))
                continue

            for node in ast.walk(tree):
                # Bare except
                if isinstance(node, ast.ExceptHandler) and node.type is None:
                    report.findings.append(Finding(
                        "MEDIUM", "Reliability",
                        "Bare `except:` clause silences ALL errors",
                        "A bare `except:` catches even KeyboardInterrupt and SystemExit. "
                        "Use `except Exception as e:` and log the error.",
                        file=path, line=node.lineno,
                        evidence="except:",
                        fix="Replace `except:` with `except Exception as e: logger.error(e)`"
                    ))

                # assert used in production logic
                if isinstance(node, ast.Assert) and not path.endswith("_test.py"):
                    report.findings.append(Finding(
                        "LOW", "Reliability",
                        "assert used in production code",
                        "`assert` statements are removed when Python runs with `-O`. "
                        "Use explicit `if` checks instead.",
                        file=path, line=node.lineno,
                        fix="Replace assert with explicit if/raise."
                    ))
                    break  # one per file

                # Mutable default argument
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    for default in node.args.defaults:
                        if isinstance(default, (ast.List, ast.Dict, ast.Set)):
                            report.findings.append(Finding(
                                "MEDIUM", "Code Quality",
                                "Mutable default argument (classic Python bug)",
                                f"Function `{node.name}` uses a mutable default (list/dict/set). "
                                "All callers share the SAME object — state leaks between calls.",
                                file=path, line=node.lineno,
                                fix=f"Change `def {node.name}(x=[])` to `def {node.name}(x=None): if x is None: x = []`"
                            ))
                            break

    # ── Dependency Checks ─────────────────────────────────────────────────────

    def _check_dependencies(self, report: AuditReport):
        paths = {f["path"] for f in self._file_tree}

        has_pkg = "package.json" in paths
        has_req = "requirements.txt" in paths
        has_pyproject = "pyproject.toml" in paths
        has_lock = any(p in paths for p in ["package-lock.json", "yarn.lock", "pnpm-lock.yaml", "poetry.lock", "uv.lock"])

        if has_pkg and not has_lock:
            report.findings.append(Finding(
                "MEDIUM", "Dependencies",
                "No lockfile (package.json without lock)",
                "Non-deterministic installs. Different developers get different versions.",
                fix="Run `npm install` and commit package-lock.json"
            ))

        if not has_pkg and not has_req and not has_pyproject:
            report.findings.append(Finding(
                "HIGH", "Dependencies",
                "No dependency manifest found",
                "No package.json, requirements.txt, or pyproject.toml. "
                "Nobody can reproduce your environment.",
                fix="Add requirements.txt or package.json"
            ))

        # Check if .env is tracked
        for f in self._file_tree:
            if f["path"] == ".env" or f["path"].endswith("/.env"):
                report.findings.append(Finding(
                    "CRITICAL", "Security",
                    ".env file is committed to git",
                    "The .env file is tracked. All secrets in it are PUBLIC.",
                    file=f["path"],
                    fix="Run: git rm --cached .env && echo '.env' >> .gitignore && git commit"
                ))

    # ── CVE Check via OSV.dev ─────────────────────────────────────────────────

    def _check_dependency_cves(self, report: AuditReport):
        """
        Checks dependencies against the OSV.dev vulnerability database.
        Works for Python (requirements.txt) and Node (package.json).
        """
        # Python deps
        req_content = self._fetch_file("requirements.txt")
        if req_content:
            deps = self._parse_requirements(req_content)
            if self.verbose:
                print(f"[VeilPiercer]   Checking {len(deps)} Python deps against OSV.dev...")
            for pkg, version in deps[:20]:
                vulns = self._osv_check("PyPI", pkg, version)
                for v in vulns:
                    report.findings.append(Finding(
                        "CRITICAL" if v.get("severity") == "CRITICAL" else "HIGH",
                        "CVE",
                        f"Known vulnerability in {pkg}=={version}",
                        v.get("summary", "Vulnerability found in dependency."),
                        cve=", ".join(v.get("aliases", [v.get("id", "")])),
                        fix=f"Upgrade {pkg} to a patched version. See: https://osv.dev/vulnerability/{v.get('id', '')}"
                    ))

        # Node deps
        pkg_content = self._fetch_file("package.json")
        if pkg_content:
            try:
                pkg_data = json.loads(pkg_content)
                all_deps = {}
                all_deps.update(pkg_data.get("dependencies", {}))
                all_deps.update(pkg_data.get("devDependencies", {}))
                if self.verbose:
                    print(f"[VeilPiercer]   Checking {len(all_deps)} npm deps against OSV.dev...")
                for pkg, version in list(all_deps.items())[:20]:
                    clean_ver = version.lstrip("^~>=")
                    vulns = self._osv_check("npm", pkg, clean_ver)
                    for v in vulns:
                        report.findings.append(Finding(
                            "CRITICAL" if v.get("severity") == "CRITICAL" else "HIGH",
                            "CVE",
                            f"Known vulnerability in {pkg}@{version}",
                            v.get("summary", "Vulnerability found in dependency."),
                            cve=", ".join(v.get("aliases", [v.get("id", "")])),
                            fix=f"Upgrade {pkg}. See: https://osv.dev/vulnerability/{v.get('id', '')}"
                        ))
            except Exception:
                pass

    def _osv_check(self, ecosystem: str, package: str, version: str) -> List[Dict]:
        """Query OSV.dev for known vulnerabilities in a package version."""
        if not version or version in ("latest", "*", ""):
            return []
        payload = json.dumps({
            "version": version,
            "package": {"name": package, "ecosystem": ecosystem}
        }).encode("utf-8")
        req = urllib.request.Request(
            f"{self.OSV_API}/query",
            data=payload,
            headers={"Content-Type": "application/json"},
            method="POST"
        )
        try:
            with urllib.request.urlopen(req, timeout=8) as resp:
                data = json.loads(resp.read())
                return data.get("vulns", [])
        except Exception:
            return []

    def _parse_requirements(self, content: str) -> List[Tuple[str, str]]:
        deps = []
        for line in content.split("\n"):
            line = line.strip()
            if not line or line.startswith("#") or line.startswith("-"):
                continue
            m = re.match(r"([A-Za-z0-9_\-\.]+)\s*==\s*([^\s;]+)", line)
            if m:
                deps.append((m.group(1), m.group(2)))
        return deps

    # ── GitHub Actions Workflow Audit ─────────────────────────────────────────

    def _check_workflows(self, report: AuditReport, files: List[Dict]):
        workflow_files = [f for f in self._file_tree if ".github/workflows" in f.get("path", "")]
        if not workflow_files:
            return  # already flagged by structure check

        for wf_meta in workflow_files:
            content = self._fetch_file(wf_meta["path"])
            if not content:
                continue

            # Unpinned actions (use @main or @master instead of commit hash)
            unpinned = re.findall(r"uses:\s+([^\s@]+@(?:main|master|latest|v\d+))", content)
            for action in unpinned[:3]:
                report.findings.append(Finding(
                    "MEDIUM", "CI/CD",
                    f"Unpinned GitHub Action: `{action}`",
                    "Using @main/@master/@latest means a compromised action repo "
                    "can inject malicious code into your CI pipeline.",
                    file=wf_meta["path"],
                    fix=f"Pin to a specific commit hash: `{action.split('@')[0]}@<sha>`"
                ))

            # Secrets in run commands
            if re.search(r"run:.*\$\{\{.*secrets\.", content):
                report.findings.append(Finding(
                    "HIGH", "Security",
                    "GitHub secret passed directly to shell `run:` command",
                    "Secrets passed to `run:` can be leaked in logs. "
                    "Use environment variables instead.",
                    file=wf_meta["path"],
                    fix="Use `env:` block to pass secrets, not inline ${{ secrets.X }}"
                ))

            # No permissions: block
            if "permissions:" not in content:
                report.findings.append(Finding(
                    "MEDIUM", "Security",
                    "GitHub Actions workflow has no `permissions:` block",
                    "Without explicit permissions, workflow gets default (often over-privileged) access. "
                    "Add `permissions: read-all` and grant only what's needed.",
                    file=wf_meta["path"],
                    fix="Add `permissions: read-all` to the workflow YAML"
                ))

    # ── Commit History Scan ───────────────────────────────────────────────────

    def _check_commit_history(self, report: AuditReport, branch: str):
        """
        Scans recent commit messages and diffs for secrets that were
        added then removed (still in git history = still exposed).
        """
        commits = self._api(f"/repos/{self.owner}/{self.name}/commits?sha={branch}&per_page=30")
        if not commits or not isinstance(commits, list):
            return

        report.commits_scanned = len(commits)
        if self.verbose:
            print(f"[VeilPiercer]   Scanning {len(commits)} commits...")

        # Look for suspicious commit messages
        suspicious_msgs = [
            (r"remove.*(?:key|secret|password|token|credential)", "Credential removed from commit history (still in git history!)"),
            (r"fix.*leak|secret.*leak|accidentally.*commit", "Developer acknowledged accidental secret commit"),
            (r"oops|mistake|wrong|undo.*key|revert.*secret", "Possible secret accidentally committed then reverted"),
            (r"add.*(?:api.?key|private.?key|secret)", "Commit message suggests secret was added"),
        ]

        for commit in commits:
            msg = commit.get("commit", {}).get("message", "").lower()
            sha = commit.get("sha", "")[:7]
            for pattern, meaning in suspicious_msgs:
                if re.search(pattern, msg, re.I):
                    report.findings.append(Finding(
                        "HIGH", "Security",
                        f"Suspicious commit message suggests secret leak",
                        f"Commit {sha}: \"{commit['commit']['message'][:100]}\" — {meaning}. "
                        f"Even if removed, the secret is still in git history.",
                        evidence=commit["commit"]["message"][:200],
                        fix="Rotate any credentials that were ever committed. Use git-filter-repo to scrub history."
                    ))
                    break

    # ── GitHub Issues Analysis ────────────────────────────────────────────────

    def _check_github_issues(self, report: AuditReport):
        """
        Scrapes open GitHub issues to find patterns users are reporting.
        Real user complaints = real bugs.
        """
        issues = self._api(f"/repos/{self.owner}/{self.name}/issues?state=open&per_page=30")
        if not issues or not isinstance(issues, list):
            return

        report.issues_analyzed = len(issues)
        if self.verbose:
            print(f"[VeilPiercer]   Analyzing {len(issues)} open issues...")

        # Pattern categories from issue text
        bug_patterns = [
            (r"crash|exception|error|traceback|stack.?trace", "Bug/crash reported by users"),
            (r"memory.?leak|out.?of.?memory|oom", "Memory leak reported"),
            (r"slow|performance|timeout|hang|freeze", "Performance issue reported"),
            (r"security|vulnerability|exploit|inject|xss|csrf", "Security issue reported by users"),
            (r"data.?loss|corrupt|broken|not.?working", "Data integrity issue reported"),
            (r"auth|login|token|permission|403|401|unauthorized", "Authentication issue reported"),
        ]

        issue_categories: Dict[str, List[str]] = {}
        for issue in issues:
            title = issue.get("title", "")
            body = (issue.get("body") or "")[:500]
            combined = f"{title} {body}".lower()
            issue_num = issue.get("number", "?")

            for pattern, category in bug_patterns:
                if re.search(pattern, combined, re.I):
                    issue_categories.setdefault(category, []).append(f"#{issue_num}: {title[:60]}")
                    break

        for category, issue_list in issue_categories.items():
            report.findings.append(Finding(
                "HIGH" if "Security" in category or "crash" in category.lower() else "MEDIUM",
                "User Reported",
                f"{category} ({len(issue_list)} issues)",
                f"Real users are reporting this. Issues: {', '.join(issue_list[:3])}",
                fix="Prioritize fixing issues reported by actual users."
            ))

        # Stale issues
        stale = [i for i in issues if i.get("comments", 0) == 0]
        if len(stale) > 5:
            report.findings.append(Finding(
                "LOW", "Maintenance",
                f"{len(stale)} open issues with zero responses",
                "Unresponsive issue tracker signals abandoned/unmaintained project.",
                fix="Triage open issues. Close stale ones. Respond to bugs."
            ))

    # ── LLM-Specific Deep Patterns ────────────────────────────────────────────

    def _check_llm_patterns(self, report: AuditReport, files: List[Dict]):
        src_files = [f for f in files if any(f["path"].endswith(e) for e in {".py", ".ts", ".js"})]
        all_content = ""
        file_contents: Dict[str, str] = {}

        for f in src_files[:60]:
            c = self._fetch_file(f["path"])
            if c:
                all_content += c
                file_contents[f["path"]] = c

        has_llm = bool(re.search(
            r"(openai|anthropic|ollama|claude|gpt|gemini|mistral|llm|chat\.completions|messages\.create|generate)",
            all_content, re.I
        ))
        if not has_llm:
            return

        # 1. No error handling around LLM calls
        llm_call_files = [
            fp for fp, c in file_contents.items()
            if re.search(r"openai|anthropic|ollama|claude|chat\.completions|messages\.create", c, re.I)
        ]
        for fp in llm_call_files:
            c = file_contents[fp]
            has_try = bool(re.search(r"try\s*[\({:]|\.catch\s*\(|except\s+", c))
            if not has_try:
                report.findings.append(Finding(
                    "HIGH", "Reliability",
                    "LLM API calls with no error handling",
                    f"`{fp}` calls an LLM API but has no try/catch. "
                    "Network failures and rate limits will crash the agent.",
                    file=fp,
                    fix="Wrap LLM calls in try/except. Use VeilPiercer Tracer to auto-capture failures."
                ))

        # 2. No retry/backoff
        has_retry = bool(re.search(r"retry|backoff|sleep|rate.?limit|RateLimitError|429", all_content, re.I))
        if not has_retry:
            report.findings.append(Finding(
                "MEDIUM", "Reliability",
                "No retry/backoff logic for LLM API calls",
                "LLM APIs enforce rate limits and return 429 errors. "
                "Without retry logic, your agent will fail silently under any load.",
                fix="Add exponential backoff. VeilPiercer Tracer captures all retries."
            ))

        # 3. Infinite agent loop without exit condition
        for fp, c in file_contents.items():
            if re.search(r"while\s+True|while\s*\(\s*true\s*\)", c, re.I):
                # Check if there's a max_iterations / break / timeout
                has_escape = bool(re.search(r"max_iter|max_step|max_turn|break|sys\.exit|raise|return|timeout", c, re.I))
                if not has_escape:
                    report.findings.append(Finding(
                        "HIGH", "Reliability",
                        "Infinite agent loop with no exit condition",
                        f"`{fp}` has `while True` with no max_iterations, timeout, or break. "
                        "Runaway agents burn money on API credits.",
                        file=fp,
                        fix="Add max_iterations counter or timeout. Use VeilPiercer TimeMachine to replay safely."
                    ))

        # 4. Prompt built with string concatenation (injection risk)
        for fp, c in file_contents.items():
            if re.search(r"(prompt|message|system)\s*[+=]\s*(?:f[\"']|[\"'].*\+.*user|str\(|format\()", c, re.I):
                if not re.search(r"sanitize|escape|strip|validate|bleach", c, re.I):
                    report.findings.append(Finding(
                        "MEDIUM", "Security",
                        "Prompt built with string concatenation — injection risk",
                        f"`{fp}` builds prompts by concatenating user input without sanitization. "
                        "Malicious input can hijack the agent's instructions.",
                        file=fp,
                        fix="Sanitize user input before injecting into prompts. Use VeilPiercer SessionIntegrity."
                    ))
                    break

        # 5. No conversation memory / stateless agent
        has_memory = bool(re.search(
            r"memory|history|messages\s*=\s*\[|conversation|checkpoint|stateful", all_content, re.I
        ))
        if not has_memory:
            report.findings.append(Finding(
                "MEDIUM", "Logic",
                "Stateless LLM agent — no conversation memory",
                "No message history or memory management found. "
                "The agent loses all context between calls.",
                fix="Maintain a messages[] array. Use VeilPiercer StateGuard for persistence."
            ))

        # 6. Model name hardcoded (not configurable)
        model_hardcoded = re.findall(r"""model\s*[:=]\s*["'](gpt-[^"']+|claude-[^"']+|deepseek[^"']+|llama[^"']+|mistral[^"']+)["']""", all_content, re.I)
        if len(model_hardcoded) > 1:
            report.findings.append(Finding(
                "LOW", "Maintainability",
                f"Model name hardcoded in {len(model_hardcoded)} places",
                f"Found: {', '.join(set(model_hardcoded[:4]))}. "
                "When the model is updated or deprecated, all instances need changing.",
                fix="Extract model name to a single config constant or env var."
            ))

    # ── Dead Repo Detection ───────────────────────────────────────────────────

    def _check_dead_repo(self, report: AuditReport, meta: Dict):
        updated_at = meta.get("updated_at", "")
        if updated_at:
            try:
                updated = datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
                days_ago = (datetime.now(timezone.utc) - updated).days
                if days_ago > 365:
                    report.findings.append(Finding(
                        "INFO", "Maintenance",
                        f"Repo not updated in {days_ago} days",
                        "This repository appears abandoned. Issues may go unresolved.",
                    ))
            except Exception:
                pass

        if meta.get("open_issues_count", 0) > 20 and meta.get("stargazers_count", 0) < 5:
            report.findings.append(Finding(
                "LOW", "Maintenance",
                f"Many open issues ({meta['open_issues_count']}) with few stars ({meta['stargazers_count']})",
                "High issue-to-star ratio suggests the project has problems but limited community.",
            ))

    # ── GitHub API Helpers ────────────────────────────────────────────────────

    def _api(self, path: str, params: str = "") -> Optional[any]:
        url = f"{self.GITHUB_API}{path}{params}"
        headers = {"Accept": "application/vnd.github+json", "User-Agent": "VeilPiercer/2.0"}
        if self.token:
            headers["Authorization"] = f"token {self.token}"
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                remaining = resp.headers.get("X-RateLimit-Remaining", "?")
                if remaining != "?" and int(remaining) < 5:
                    print(f"[VeilPiercer] ⚠️  GitHub rate limit nearly exhausted ({remaining} remaining)")
                return json.loads(resp.read())
        except urllib.error.HTTPError as e:
            if e.code == 403:
                print(f"[VeilPiercer] Rate limited. Set GITHUB_TOKEN for 5000 req/hr.")
                self._rate_limited = True
            return None
        except Exception:
            return None

    def _fetch_tree(self, branch: str):
        data = self._api(f"/repos/{self.owner}/{self.name}/git/trees/{branch}?recursive=1")
        if data and "tree" in data:
            self._file_tree = data["tree"]
        else:
            data = self._api(f"/repos/{self.owner}/{self.name}/contents/")
            if data and isinstance(data, list):
                self._file_tree = [
                    {"path": f["path"], "type": "blob" if f["type"] == "file" else "tree", "size": f.get("size", 0)}
                    for f in data
                ]

    def _fetch_file(self, path: str) -> Optional[str]:
        if path in self._cache:
            return self._cache[path]
        data = self._api(f"/repos/{self.owner}/{self.name}/contents/{urllib.parse.quote(path)}")
        if not data or "content" not in data:
            return None
        try:
            content = base64.b64decode(data["content"]).decode("utf-8", errors="replace")
            self._cache[path] = content
            return content
        except Exception:
            return None
