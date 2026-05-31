"""
veilpiercer.time_machine
------------------------
Fork & replay any agent session from any step.
Directly addresses: HN "Show HN: Time Machine — Debug AI Agents by Forking and Replaying"

Created by Lauren Flipo (@fliptrigga13) · https://veil-piercer.com
"""

from __future__ import annotations

import copy
import json
import uuid
from typing import Any, Callable, Dict, List, Optional
from pathlib import Path
from datetime import datetime, timezone


class Fork:
    """A branched version of an agent session from a specific step."""

    def __init__(self, parent_session_id: str, from_step: int, fork_id: str):
        self.fork_id = fork_id
        self.parent_session_id = parent_session_id
        self.from_step = from_step
        self.replayed_steps: List[Dict] = []
        self.created_at = datetime.now(timezone.utc).isoformat()

    def __repr__(self):
        return f"<Fork id={self.fork_id} from_step={self.from_step} replays={len(self.replayed_steps)}>"


class TimeMachine:
    """
    Fork and replay agent sessions from any step.

    This directly solves the #1 requested feature in AI agent tooling:
    "I want to rewind to step 3 and try a different prompt without
     re-running the whole pipeline."

    Usage:
        tm = TimeMachine()

        # Record your agent running
        with tm.record("my-session") as session:
            for step in agent_pipeline():
                session.log(step)

        # Fork from step 3 and try something different
        fork = tm.fork("my-session", from_step=3)
        fork.replay(my_agent_fn, new_prompt="try this instead")

        # Compare fork vs original
        tm.diff("my-session", fork.fork_id)
    """

    def __init__(self, storage_path: Optional[str] = None):
        self.storage_path = storage_path
        self._sessions: Dict[str, List[Dict]] = {}
        self._forks: Dict[str, Fork] = {}

    def record(self, session_id: Optional[str] = None) -> "SessionRecorder":
        """Start recording a new agent session."""
        sid = session_id or str(uuid.uuid4())[:12]
        self._sessions[sid] = []
        return SessionRecorder(self, sid)

    def log_step(self, session_id: str, step_data: Dict):
        """Manually log a step to a session."""
        if session_id not in self._sessions:
            self._sessions[session_id] = []
        step_data["_step"] = len(self._sessions[session_id]) + 1
        step_data["_ts"] = datetime.now(timezone.utc).isoformat()
        self._sessions[session_id].append(step_data)

    def fork(self, session_id: str, from_step: int) -> Fork:
        """
        Fork a session from a specific step.
        Returns a Fork you can replay with a different function/prompt.
        """
        if session_id not in self._sessions:
            raise ValueError(f"Session '{session_id}' not found. Call record() first.")

        steps = self._sessions[session_id]
        if from_step > len(steps):
            raise ValueError(f"Session only has {len(steps)} steps, cannot fork from step {from_step}")

        fork_id = f"fork-{str(uuid.uuid4())[:8]}"
        fork = Fork(session_id, from_step, fork_id)

        # Copy state up to fork point
        fork.state_at_fork = copy.deepcopy(steps[:from_step])
        fork.messages_at_fork = [
            s.get("messages", []) for s in fork.state_at_fork
        ]

        self._forks[fork_id] = fork
        print(f"[VeilPiercer TimeMachine] 🍴 Fork {fork_id} created from '{session_id}' at step {from_step}")
        return fork

    def replay(
        self,
        fork: Fork,
        agent_fn: Callable,
        new_input: Any = None,
        **kwargs
    ) -> Any:
        """
        Replay an agent from a fork point with optionally modified input.

        Args:
            fork: The Fork object from .fork()
            agent_fn: Your agent function to call
            new_input: Override the input at the fork point
        """
        # Restore context up to fork
        context = fork.state_at_fork.copy()
        messages = []
        for step in context:
            if "messages" in step:
                messages.extend(step["messages"])

        # Apply new input if provided
        if new_input:
            if isinstance(new_input, str):
                messages.append({"role": "user", "content": new_input})
            elif isinstance(new_input, dict):
                messages.append(new_input)

        print(f"[VeilPiercer TimeMachine] ▶️  Replaying from step {fork.from_step} with {len(messages)} messages in context")

        t_start = __import__("time").perf_counter()
        result = agent_fn(messages=messages, **kwargs)
        latency = (__import__("time").perf_counter() - t_start) * 1000

        fork.replayed_steps.append({
            "input": new_input,
            "result": str(result)[:500],
            "latency_ms": round(latency, 2),
        })

        return result

    def diff(self, session_id: str, fork_id: str):
        """
        Print a side-by-side diff of original session vs fork.
        """
        if session_id not in self._sessions:
            raise ValueError(f"Session '{session_id}' not found")
        if fork_id not in self._forks:
            raise ValueError(f"Fork '{fork_id}' not found")

        fork = self._forks[fork_id]
        original = self._sessions[session_id]

        print(f"\n[VeilPiercer TimeMachine] 📊 DIFF: {session_id} vs {fork_id}")
        print(f"  Original steps : {len(original)}")
        print(f"  Fork from step : {fork.from_step}")
        print(f"  Fork replays   : {len(fork.replayed_steps)}\n")

        for i, step in enumerate(original[:fork.from_step], 1):
            print(f"  [SHARED] Step {i}: {str(step.get('response', step))[:80]}")

        print(f"\n  --- DIVERGENCE AT STEP {fork.from_step + 1} ---\n")

        orig_after = original[fork.from_step:]
        for i, (orig, rep) in enumerate(zip(orig_after, fork.replayed_steps)):
            print(f"  [ORIGINAL] Step {fork.from_step + i + 1}: {str(orig.get('response', orig))[:80]}")
            print(f"  [FORK]     Step {fork.from_step + i + 1}: {str(rep.get('result', rep))[:80]}")
            print()

    def save_session(self, session_id: str, path: str):
        """Persist a session to disk for later replay."""
        data = {
            "session_id": session_id,
            "steps": self._sessions.get(session_id, []),
            "created_by": "VeilPiercer · https://veil-piercer.com · @fliptrigga13",
        }
        Path(path).write_text(json.dumps(data, indent=2), encoding="utf-8")
        print(f"[VeilPiercer TimeMachine] 💾 Session '{session_id}' saved → {path}")

    def load_session(self, path: str) -> str:
        """Load a saved session from disk."""
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        sid = data["session_id"]
        self._sessions[sid] = data["steps"]
        print(f"[VeilPiercer TimeMachine] 📂 Session '{sid}' loaded ({len(data['steps'])} steps)")
        return sid


class SessionRecorder:
    """Context manager for recording an agent session."""

    def __init__(self, tm: TimeMachine, session_id: str):
        self._tm = tm
        self.session_id = session_id

    def __enter__(self):
        return self

    def __exit__(self, *args):
        steps = len(self._tm._sessions.get(self.session_id, []))
        print(f"[VeilPiercer TimeMachine] ⏹  Session '{self.session_id}' recorded ({steps} steps)")

    def log(self, step_data: Dict):
        """Log a step in the current session."""
        self._tm.log_step(self.session_id, step_data)
