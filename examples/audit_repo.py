"""
Example: Audit @louz514's Claudecraft repo with VeilPiercer

Created by Lauren Flipo (@fliptrigga13) · https://veil-piercer.com
"""

import os
from veilpiercer.audit import RepoAuditor

def main():
    # Audit Claudecraft — the real repo the swarm flagged as having gaps
    auditor = RepoAuditor(
        "https://github.com/louz514/Claudecraft",
        token=os.environ.get("GITHUB_TOKEN"),  # Optional: for higher rate limits
        verbose=True
    )

    report = auditor.run()
    report.print()

    # Save the markdown report to file
    with open("claudecraft_audit.md", "w", encoding="utf-8") as f:
        f.write(report.to_markdown())
    print("Markdown report saved to claudecraft_audit.md")

    # Uncomment to post findings directly as a GitHub Issue on their repo:
    # report.open_github_issue()

    # Or audit goblintown
    print("\n" + "="*64)
    auditor2 = RepoAuditor("https://github.com/louz514/goblintown")
    report2 = auditor2.run()
    report2.print()

if __name__ == "__main__":
    main()
