"""
VeilPiercer callback — captures every LangChain step into local SQLite.
Covers LLM calls, tool calls, chain events, and agent actions.
"""
import json
import sqlite3
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional


_SCHEMA = """
CREATE TABLE IF NOT EXISTS sessions (
    session_id TEXT PRIMARY KEY,
    start_time TEXT,
    metadata   TEXT
);
CREATE TABLE IF NOT EXISTS steps (
    step_id    TEXT PRIMARY KEY,
    session_id TEXT,
    step_num   INTEGER,
    step_type  TEXT,
    input_data TEXT,
    output_data TEXT,
    latency_ms  REAL,
    timestamp   TEXT,
    metadata    TEXT
);
"""


def _get_default_db() -> Path:
    p = Path.home() / ".veilpiercer"; p.mkdir(exist_ok=True)
    return p / "sessions.db"


class VeilPiercerCallback:
    """
    Drop-in LangChain/LCEL callback. Zero hard deps when langchain not installed.

    Usage:
        from veilpiercer import VeilPiercerCallback
        chain = LLMChain(llm=llm, callbacks=[VeilPiercerCallback()])
        # or with API key for future hosted streaming:
        VeilPiercerCallback(api_key="vp_xxx")
    """

    raise_error = False  # required by BaseCallbackHandler duck-typing

    def __init__(self, api_key: str = None, session_id: str = None,
                 db_path: Path = None, local_only: bool = True):
        self.api_key = api_key
        self.session_id = session_id or f"lc_{uuid.uuid4().hex[:12]}"
        self.local_only = local_only
        self._step = 0
        self._t0: float = 0.0
        self._last_input = ""

        db = Path(db_path) if db_path else _get_default_db()
        self._conn = sqlite3.connect(str(db))
        self._conn.executescript(_SCHEMA)
        self._conn.commit()
        self._conn.execute(
            "INSERT OR IGNORE INTO sessions VALUES (?,?,?)",
            (self.session_id, datetime.now(timezone.utc).isoformat(),
             json.dumps({"version": "0.2.0"}))
        )
        self._conn.commit()
        print(f"🔍 VeilPiercer — session {self.session_id[:8]}... tracing started")

    # ── LLM ──────────────────────────────────────────────────────────────────
    def on_llm_start(self, serialized: Dict, prompts: List[str], **kw) -> None:
        self._t0 = time.time()
        self._step += 1
        self._last_input = prompts[0] if prompts else ""
        self._log("llm_start", json.dumps({"prompts": prompts[:1]}), None,
                  meta={"model": serialized.get("kwargs", {}).get("model_name")})

    def on_llm_end(self, response: Any, **kw) -> None:
        lat = (time.time() - self._t0) * 1000
        try: text = response.generations[0][0].text
        except Exception: text = str(response)
        self._log("llm_end", None, json.dumps({"output": text[:2000]}), latency=lat)

    def on_llm_error(self, error: Exception, **kw) -> None:
        self._log("llm_error", None, json.dumps({"error": str(error)}))

    # ── Tools ─────────────────────────────────────────────────────────────────
    def on_tool_start(self, serialized: Dict, input_str: str, **kw) -> None:
        self._step += 1
        self._log("tool_start",
                  json.dumps({"tool": serialized.get("name"), "input": input_str}), None)

    def on_tool_end(self, output: str, **kw) -> None:
        self._log("tool_end", None, json.dumps({"output": str(output)[:1000]}))

    def on_tool_error(self, error: Exception, **kw) -> None:
        self._log("tool_error", None, json.dumps({"error": str(error)}))

    # ── Chains ────────────────────────────────────────────────────────────────
    def on_chain_start(self, serialized: Dict, inputs: Dict, **kw) -> None:
        self._step += 1
        self._log("chain_start", json.dumps(inputs)[:1000], None)

    def on_chain_end(self, outputs: Dict, **kw) -> None:
        self._log("chain_end", None, json.dumps(outputs)[:1000])

    # ── Internal ──────────────────────────────────────────────────────────────
    def _log(self, step_type: str, inp: Optional[str], out: Optional[str],
             latency: float = 0.0, meta: dict = None):
        self._conn.execute(
            "INSERT INTO steps VALUES (?,?,?,?,?,?,?,?,?)",
            (str(uuid.uuid4()), self.session_id, self._step, step_type,
             inp, out, latency, datetime.now(timezone.utc).isoformat(),
             json.dumps(meta or {}))
        )
        self._conn.commit()

    def close(self):
        self._conn.close()

    def __enter__(self): return self
    def __exit__(self, *_): self.close()
    def __del__(self):
        try: self._conn.close()
        except Exception: pass


# Alias
VeilPiercer = VeilPiercerCallback
