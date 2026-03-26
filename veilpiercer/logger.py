"""
veilpiercer.logger — Core session capture engine.
Stores every agent step locally in SQLite. Zero cloud. Zero deps.
"""

import sqlite3
import uuid
import logging
from datetime import datetime, timezone
from pathlib import Path

log = logging.getLogger("veilpiercer")

# Store DB next to user's project (or in home dir as fallback)
_DEFAULT_DB = Path.home() / ".veilpiercer" / "sessions.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS vp_sessions (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id    TEXT NOT NULL,
    agent         TEXT NOT NULL DEFAULT 'UNKNOWN',
    step_index    INTEGER NOT NULL DEFAULT 0,
    state_version TEXT NOT NULL DEFAULT 'v0',
    prompt        TEXT NOT NULL DEFAULT '',
    response      TEXT NOT NULL DEFAULT '',
    model         TEXT DEFAULT '',
    latency_ms    INTEGER DEFAULT 0,
    step_type     TEXT DEFAULT 'llm',
    divergence_score REAL DEFAULT 0.0,
    hallucination_flag INTEGER DEFAULT 0,
    created_at    TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_sess_id    ON vp_sessions(session_id);
CREATE INDEX IF NOT EXISTS idx_sess_agent ON vp_sessions(agent, created_at);
"""


def _get_db_path() -> Path:
    """Use local db if in a project, otherwise ~/.veilpiercer/sessions.db"""
    local = Path.cwd() / "vp_sessions.db"
    if local.parent.exists():
        return local
    _DEFAULT_DB.parent.mkdir(parents=True, exist_ok=True)
    return _DEFAULT_DB


class SessionLogger:
    def __init__(self, session_id: str = None, agent: str = "agent",
                 db_path: Path = None):
        self.session_id = session_id or f"sess_{uuid.uuid4().hex[:12]}"
        self.agent = agent
        self._db_path = db_path or _get_db_path()
        self._step = 0
        self._conn = sqlite3.connect(str(self._db_path))
        self._conn.executescript(SCHEMA)
        self._conn.commit()

    @classmethod
    def new(cls, agent: str = "agent") -> "SessionLogger":
        return cls(agent=agent)

    def log_step(self, prompt: str, response: str,
                 state_version: str = None,
                 model: str = "",
                 latency_ms: int = 0,
                 step_type: str = "llm"):
        self._step += 1
        sv = state_version or f"step_{self._step}"
        self._conn.execute(
            """INSERT INTO vp_sessions
               (session_id,agent,step_index,state_version,prompt,response,
                model,latency_ms,step_type,created_at)
               VALUES (?,?,?,?,?,?,?,?,?,?)""",
            (self.session_id, self.agent, self._step, sv,
             prompt[:4000], response[:4000],
             model, latency_ms, step_type,
             datetime.now(timezone.utc).isoformat())
        )
        self._conn.commit()

    def close(self):
        self._conn.close()

    def __enter__(self): return self
    def __exit__(self, *_): self.close()


def list_sessions(db_path: Path = None):
    db = db_path or _get_db_path()
    if not db.exists():
        return []
    conn = sqlite3.connect(str(db))
    rows = conn.execute("""
        SELECT session_id, agent, COUNT(*) as steps, MAX(created_at) as last
        FROM vp_sessions GROUP BY session_id ORDER BY last DESC LIMIT 50
    """).fetchall()
    conn.close()
    return [{"session_id": r[0], "agent": r[1], "steps": r[2], "last": r[3]}
            for r in rows]


def find_divergence(session_a: str, session_b: str, db_path: Path = None):
    db = db_path or _get_db_path()
    conn = sqlite3.connect(str(db))

    def _steps(sid):
        return conn.execute(
            "SELECT step_index,state_version,prompt,response,model,latency_ms "
            "FROM vp_sessions WHERE session_id=? ORDER BY step_index",
            (sid,)
        ).fetchall()

    sa, sb = _steps(session_a), _steps(session_b)
    conn.close()

    fork_step, last_shared = 0, None
    for i, (a, b) in enumerate(zip(sa, sb)):
        if a[3] == b[3]:   # same response = shared state
            last_shared = a[1]
        else:
            fork_step = a[0]
            break

    def _fmt(rows):
        return [{"step": r[0], "state_version": r[1], "prompt": r[2],
                 "response": r[3], "model": r[4], "latency_ms": r[5]}
                for r in rows]

    return {
        "steps_a": _fmt(sa), "steps_b": _fmt(sb),
        "fork_step": fork_step, "last_shared": last_shared,
        "diverged": fork_step > 0 or (sa and sb and sa[-1][3] != sb[-1][3])
    }
