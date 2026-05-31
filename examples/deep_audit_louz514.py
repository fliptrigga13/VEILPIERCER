"""
Deep audit of all louz514 (Zack) public repos using VeilPiercer.
Fetches actual file content and runs full analysis on each.
"""

import os, sys, json, time
sys.stdout.reconfigure(encoding='utf-8')

from veilpiercer.audit import RepoAuditor

TOKEN = os.environ.get("GITHUB_TOKEN")

REPOS = [
    "https://github.com/louz514/Claudecraft",
    "https://github.com/louz514/goblintown",
    "https://github.com/louz514/automagotchi",
    "https://github.com/louz514/openhermit",
    "https://github.com/louz514/oraclexbt",
    "https://github.com/louz514/NeverBondout",
    "https://github.com/louz514/pump-chat",
    "https://github.com/louz514/AI-Content-Generator",
    "https://github.com/louz514/AI-Stock-Analyzer",
    "https://github.com/louz514/Copywriting-Assistant",
    "https://github.com/louz514/TradingView-SmartSignals",
    "https://github.com/louz514/NetWorth-BHP",
    "https://github.com/louz514/epstein-studio",
    "https://github.com/louz514/wormhole",
]

all_reports = []

for repo_url in REPOS:
    name = repo_url.split("/")[-1]
    print(f"\n{'='*60}")
    print(f"  Auditing: {name}")
    print(f"{'='*60}")
    try:
        auditor = RepoAuditor(repo_url, token=TOKEN, verbose=True)
        report = auditor.run()
        all_reports.append(report)
        print(f"  Score: {report.score()}/100 | Grade: {report.grade()} | Findings: {len(report.findings)}")
        
        # Print top CRITICAL and HIGH only
        top = [f for f in report.findings if f.severity in ("CRITICAL", "HIGH")]
        if top:
            print(f"\n  TOP ISSUES:")
            for f in top[:8]:
                loc = f"  [{f.file}:{f.line}]" if f.file else ""
                print(f"    {f.emoji()} [{f.severity}] {f.title}{loc}")
                print(f"       {f.detail[:120]}")
        time.sleep(1)  # be polite to GitHub API
    except Exception as e:
        print(f"  ERROR: {e}")

# Summary
print(f"\n\n{'='*60}")
print(f"  VEILPIERCER DEEP AUDIT — @louz514 SUMMARY")
print(f"{'='*60}")
print(f"  Repos scanned : {len(all_reports)}")

total_findings = sum(len(r.findings) for r in all_reports)
print(f"  Total findings: {total_findings}")
print()

for r in sorted(all_reports, key=lambda x: x.score()):
    crits = len([f for f in r.findings if f.severity == "CRITICAL"])
    highs = len([f for f in r.findings if f.severity == "HIGH"])
    print(f"  {r.grade()}  {r.score():3d}/100  {r.name:<35} 🔴×{crits} 🟠×{highs}")

print(f"\n  Audited by VeilPiercer · https://veil-piercer.com · @fliptrigga13")
print(f"{'='*60}")

# Save full JSON report
output = {
    "audited_by": "VeilPiercer v1.0.0 · https://veil-piercer.com · @fliptrigga13",
    "target": "@louz514",
    "repos": [
        {
            "repo": r.repo,
            "score": r.score(),
            "grade": r.grade(),
            "files_scanned": r.files_scanned,
            "findings": [
                {"severity": f.severity, "category": f.category,
                 "title": f.title, "detail": f.detail,
                 "file": f.file, "line": f.line}
                for f in r.findings
                if f.severity in ("CRITICAL", "HIGH", "MEDIUM")  # skip noise
            ]
        }
        for r in all_reports
    ]
}

with open("louz514_deep_audit.json", "w", encoding="utf-8") as fp:
    json.dump(output, fp, indent=2)
print("\nFull report saved: louz514_deep_audit.json")
