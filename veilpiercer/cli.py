"""
veilpiercer CLI entry point.
Commands: sessions, diff, dashboard, demo, quickstart
"""
import argparse, json, sys, webbrowser

README_URL = "https://github.com/fliptrigga13/VEILPIERCER#readme"


def _serve_dashboard(port: int, open_browser: bool = True):
    """Serve the diff UI plus /vp/sessions and /vp/diff from the local store."""
    from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
    from importlib.resources import files
    from urllib.parse import urlparse, parse_qs
    from veilpiercer.logger import list_sessions, find_divergence, _get_db_path

    html = (files("veilpiercer.static") / "session_diff.html").read_bytes()

    class H(BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def _send(self, code, body, ctype):
            self.send_response(code)
            self.send_header("Content-Type", ctype)
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def do_GET(self):
            u = urlparse(self.path)
            if u.path in ("/", "/index.html"):
                return self._send(200, html, "text/html; charset=utf-8")
            if u.path == "/vp/sessions":
                rows = [{**r, "started_at": r.get("last")} for r in list_sessions()]
                return self._send(200, json.dumps(rows).encode(), "application/json")
            if u.path == "/vp/diff":
                q = parse_qs(u.query)
                r = find_divergence(q.get("a", [""])[0], q.get("b", [""])[0])
                return self._send(200, json.dumps(r).encode(), "application/json")
            return self._send(404, b"not found", "text/plain")

    srv = ThreadingHTTPServer(("127.0.0.1", port), H)
    url = f"http://127.0.0.1:{srv.server_address[1]}/"
    print(f"✅ Dashboard: {url}  (store: {_get_db_path()})  Ctrl+C to stop")
    if open_browser:
        webbrowser.open(url)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        srv.server_close()


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
    db = sub.add_parser("dashboard", help="Serve the diff UI on 127.0.0.1 and open it")
    db.add_argument("--port", type=int, default=8765)
    db.add_argument("--no-browser", action="store_true")

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
        with SessionLogger.new("demo-A", agent="demo") as s:
            # re-running the demo replaces the old demo sessions
            s._conn.execute("DELETE FROM vp_sessions WHERE session_id IN ('demo-A','demo-B')")
            s._conn.commit()
            s.log_step("What broke?", "Timeout at step 3.", "v1")
            s.log_step("Fix?",        "Retry with lower temp.", "v2")
            s.log_step("Result?",     "FAILED — same timeout.", "v3a")
        with SessionLogger.new("demo-B", agent="demo") as s:
            s.log_step("What broke?", "Timeout at step 3.", "v1")
            s.log_step("Fix?",        "Retry with lower temp.", "v2")
            s.log_step("Result?",     "SUCCESS — pipeline resumed.", "v3b")
        r = find_divergence("demo-A", "demo-B")
        print(f"✅ Demo complete — Divergence: {r['diverged']} at step {r.get('fork_step')}")
        print("   Run: veilpiercer dashboard  to see the visual diff")

    elif args.cmd == "quickstart":
        webbrowser.open(README_URL)
        print("✅ Opened quickstart in browser")

    elif args.cmd == "dashboard":
        _serve_dashboard(args.port, open_browser=not args.no_browser)

    else:
        p.print_help()


if __name__ == "__main__":
    main()
