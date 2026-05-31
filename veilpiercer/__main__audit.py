"""
veilpiercer.audit CLI entry point

Usage:
    python -m veilpiercer.audit https://github.com/louz514/Claudecraft
    python -m veilpiercer.audit https://github.com/louz514/Claudecraft --issue
    python -m veilpiercer.audit https://github.com/louz514/Claudecraft --json
    python -m veilpiercer.audit https://github.com/louz514/Claudecraft --issue --token ghp_xxx
"""

import sys
import os
import json as _json

def main():
    args = sys.argv[1:]

    if not args or args[0] in ("--help", "-h"):
        print(__doc__)
        sys.exit(0)

    repo_url = args[0]
    open_issue = "--issue" in args
    output_json = "--json" in args

    # Token from flag or env
    token = None
    if "--token" in args:
        idx = args.index("--token")
        if idx + 1 < len(args):
            token = args[idx + 1]
    token = token or os.environ.get("GITHUB_TOKEN")

    from veilpiercer.audit import RepoAuditor

    auditor = RepoAuditor(repo_url, token=token)
    report = auditor.run()

    if output_json:
        data = {
            "repo": report.repo,
            "score": report.score(),
            "grade": report.grade(),
            "files_scanned": report.files_scanned,
            "findings": [
                {
                    "severity": f.severity,
                    "category": f.category,
                    "title": f.title,
                    "detail": f.detail,
                    "file": f.file,
                    "line": f.line,
                }
                for f in report.findings
            ],
            "scanned_at": report.scanned_at,
            "audited_by": "VeilPiercer · https://veil-piercer.com · @fliptrigga13",
        }
        print(_json.dumps(data, indent=2))
    else:
        report.print()

    if open_issue:
        url = report.open_github_issue(token=token)
        if url:
            print(f"\nIssue opened: {url}")
        else:
            print("\nCould not open issue. Set GITHUB_TOKEN env var with repo scope.")
            print("Markdown report:")
            print(report.to_markdown())

if __name__ == "__main__":
    main()
