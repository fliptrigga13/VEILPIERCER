import json
import threading
import urllib.request

import pytest

from veilpiercer import VeilPiercerCallback, SessionLogger, __version__
from veilpiercer import logger as vlog


@pytest.fixture(autouse=True)
def isolated_store(tmp_path, monkeypatch):
    monkeypatch.setenv("VEILPIERCER_DB", str(tmp_path / "vp.db"))
    monkeypatch.delenv("VEILPIERCER_TELEMETRY", raising=False)
    return tmp_path / "vp.db"


def test_session_logger_new_uses_session_id():
    with SessionLogger.new("run-1") as s:
        s.log_step("q", "a")
    assert [r["session_id"] for r in vlog.list_sessions()] == ["run-1"]


def test_divergence_found_at_forking_step():
    for sid, last in (("A", "FAILED"), ("B", "SUCCESS")):
        with SessionLogger.new(sid) as s:
            s.log_step("p1", "same")
            s.log_step("p2", "same")
            s.log_step("p3", last)
    r = vlog.find_divergence("A", "B")
    assert r["diverged"] is True and r["fork_step"] == 3


class _Gen:
    def __init__(self, text):
        self.text = text


class _Resp:
    def __init__(self, text):
        self.generations = [[_Gen(text)]]
        self.llm_output = {"model_name": "llama3"}


def test_langchain_callback_writes_to_same_store_cli_reads():
    cb = VeilPiercerCallback(session_id="lc-1")
    cb.on_llm_start({}, ["hello"])
    cb.on_llm_end(_Resp("world"))
    cb.on_tool_start({"name": "search"}, "x")
    cb.on_tool_end("result")
    cb.close()
    rows = vlog.list_sessions()
    assert rows and rows[0]["session_id"] == "lc-1" and rows[0]["steps"] == 2


def test_telemetry_off_by_default(monkeypatch):
    called = []
    monkeypatch.setattr(urllib.request, "urlopen", lambda *a, **k: called.append(a))
    vlog._activation_ping()
    assert called == []


def test_dashboard_api_serves_real_sessions():
    from http.server import ThreadingHTTPServer
    from veilpiercer import cli

    with SessionLogger.new("dash-1") as s:
        s.log_step("q", "a")

    started = {}
    orig_init = ThreadingHTTPServer.__init__

    def capture(self, *a, **k):
        orig_init(self, *a, **k)
        started["srv"] = self

    ThreadingHTTPServer.__init__ = capture
    try:
        t = threading.Thread(target=cli._serve_dashboard, args=(0, False), daemon=True)
        t.start()
        for _ in range(100):
            if "srv" in started:
                break
            threading.Event().wait(0.02)
        port = started["srv"].server_address[1]
        data = json.loads(urllib.request.urlopen(f"http://127.0.0.1:{port}/vp/sessions").read())
        assert data[0]["session_id"] == "dash-1"
        started["srv"].shutdown()
    finally:
        ThreadingHTTPServer.__init__ = orig_init


def test_version():
    assert __version__ == "0.2.3"
