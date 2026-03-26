"""
veilpiercer CLI entry point.
Commands: sessions, diff, dashboard, demo, quickstart
"""
import argparse, sys, webbrowser


def main():
    p = argparse.ArgumentParser(prog="veilpiercer",
        description="VeilPiercer — Local-first AI agent observability")
    p.add_argument("--version", action="store_true")
    sub = p.add_subparsers(dest="cmd")
    sub.add_parser("sessions", help="List captured sessions")
    dp = sub.add_parser("diff", help="Compare two sessions")
    dp.add_argument("session_a"); dp.add_argument("session_b")
    sub.add_parser("demo", help="Run a quick demo (no agent needed)")
    sub.add_parser("quickstart", help="Open quickstart docs in browser")
    sub.add_parser("dashboard", help="Open diff UI in browser")

    args = p.parse_args()

    if args.version:
        from veilpiercer import __version__; print(f"veilpiercer v{__version__}"); return

    if args.cmd == "sessions":
        from veilpiercer.logger import list_sessions
        rows = list_sessions()
        if not rows: print("No sessions yet. Add VeilPiercerCallback() to your agent."); return
        for r in rows: print(f"  {r['session_id']:30s} | {r['agent']:12s} | {r['steps']} steps")

    elif args.cmd == "diff":
        from veilpiercer.logger import find_divergence
        r = find_divergence(args.session_a, args.session_b)
        print(f"Divergence: {r['diverged']}  |  Fork at step: {r.get('fork_step', 0)}")

    elif args.cmd == "demo":
        from veilpiercer.logger import SessionLogger, find_divergence
        with SessionLogger.new("demo-A") as s:
            s.log_step("What broke?", "Timeout at step 3.", "v1")
            s.log_step("Fix?",        "Retry with lower temp.", "v2")
            s.log_step("Result?",     "FAILED — same timeout.", "v3a")
        with SessionLogger.new("demo-B") as s:
            s.log_step("What broke?", "Timeout at step 3.", "v1")
            s.log_step("Fix?",        "Retry with lower temp.", "v2")
            s.log_step("Result?",     "SUCCESS — pipeline resumed.", "v3b")
        r = find_divergence("demo-A", "demo-B")
        print(f"✅ Demo complete — Divergence: {r['diverged']} at step {r.get('fork_step')}")
        print("   Run: veilpiercer dashboard  to see the visual diff")

    elif args.cmd == "quickstart":
        webbrowser.open("https://veil-piercer.com/docs/quickstart")
        print("✅ Opened quickstart in browser")

    elif args.cmd == "dashboard":
        import pathlib
        # Auto-detect DB in common locations
        db_candidates = [
            pathlib.Path.cwd() / "nexus_mind.db",
            pathlib.Path.home() / "nexus_mind.db",
        ]
        db_found = next((p for p in db_candidates if p.exists()), None)
        if db_found:
            try:
                from veilpiercer.logger import list_sessions
                sessions = list_sessions()
                print(f"✅ Found DB: {db_found}")
                print(f"   {len(sessions)} session(s) ready to view")
            except Exception:
                print(f"✅ Found DB: {db_found}")
        else:
            print("ℹ️  No nexus_mind.db yet — run your agent first to capture sessions.")
            print("   Opening dashboard with demo data.")
        try:
            from importlib.resources import files
            html = files("veilpiercer.static") / "session_diff.html"
            html_path = pathlib.Path(str(html))
            webbrowser.open(f"file:///{html_path.as_posix()}")
            print("✅ Dashboard opened — select two sessions to diff.")
        except Exception as e:
            print(f"Could not open dashboard: {e}")

    else:
        p.print_help()


if __name__ == "__main__":
    main()
