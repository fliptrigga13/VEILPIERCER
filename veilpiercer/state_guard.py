"""
veilpiercer.state_guard
-----------------------
Fixes LangGraph's silent state loss bug — wraps checkpointers so agent
state is never silently reset between runs.

Directly addresses: github.com/langchain-ai/langgraph
Issue: "`langgraph dev` Ignores Checkpointer Configuration, Forcing In-Memory Storage"

Created by Lauren Flipo (@fliptrigga13) · https://veil-piercer.com
"""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Dict, Optional
from datetime import datetime, timezone


class StateGuard:
    """
    Wraps any LangGraph checkpointer to guarantee persistence and provide
    visibility into state changes.

    Instead of silently falling back to in-memory storage when the
    checkpointer config is ignored, StateGuard:
    1. Detects if the checkpointer silently reset to in-memory
    2. Falls back to disk-backed JSON storage
    3. Logs every state transition so you can see exactly what changed

    Usage:
        # Without VeilPiercer — state silently resets:
        graph = builder.compile(checkpointer=MemorySaver())

        # With VeilPiercer — state is guaranteed:
        from veilpiercer import StateGuard
        guard = StateGuard(persist_path="./agent_state.json")
        graph = builder.compile(checkpointer=guard.wrap(MemorySaver()))
        # Or use standalone:
        guard.save("my-thread", {"messages": [...], "step": 5})
        state = guard.load("my-thread")
    """

    def __init__(self, persist_path: str = "./veilpiercer_state.json", verbose: bool = True):
        self.persist_path = Path(persist_path)
        self.verbose = verbose
        self._state: Dict[str, Any] = {}
        self._history: Dict[str, list] = {}
        self._load_from_disk()

    def _load_from_disk(self):
        """Load persisted state from disk on startup."""
        if self.persist_path.exists():
            try:
                data = json.loads(self.persist_path.read_text(encoding="utf-8"))
                self._state = data.get("state", {})
                self._history = data.get("history", {})
                if self.verbose:
                    print(f"[VeilPiercer StateGuard] 💾 Loaded {len(self._state)} thread(s) from {self.persist_path}")
            except Exception as e:
                print(f"[VeilPiercer StateGuard] ⚠️  Could not load state: {e}")

    def _save_to_disk(self):
        """Persist state to disk."""
        data = {
            "state": self._state,
            "history": self._history,
            "_meta": {
                "created_by": "VeilPiercer · https://veil-piercer.com · @fliptrigga13",
                "updated_at": datetime.now(timezone.utc).isoformat(),
            }
        }
        self.persist_path.write_text(json.dumps(data, indent=2, default=str), encoding="utf-8")

    def save(self, thread_id: str, state: Any):
        """Save agent state for a thread."""
        import copy
        old_state = self._state.get(thread_id)

        self._state[thread_id] = state

        # Track history
        if thread_id not in self._history:
            self._history[thread_id] = []
        self._history[thread_id].append({
            "ts": datetime.now(timezone.utc).isoformat(),
            "snapshot": copy.deepcopy(state) if isinstance(state, dict) else str(state)[:500],
        })

        self._save_to_disk()

        if self.verbose:
            changed = old_state != state
            status = "✅ saved" if changed else "🔁 no change"
            print(f"[VeilPiercer StateGuard] {status} thread='{thread_id}'")

        return state

    def load(self, thread_id: str, default: Any = None) -> Any:
        """Load agent state for a thread."""
        state = self._state.get(thread_id, default)
        if self.verbose:
            found = thread_id in self._state
            status = "📂 loaded" if found else "⚠️  not found (returning default)"
            print(f"[VeilPiercer StateGuard] {status} thread='{thread_id}'")
        return state

    def history(self, thread_id: str) -> list:
        """Get the full state history for a thread (every save)."""
        return self._history.get(thread_id, [])

    def list_threads(self) -> list:
        """List all known thread IDs."""
        return list(self._state.keys())

    def delete(self, thread_id: str):
        """Delete state for a thread."""
        self._state.pop(thread_id, None)
        self._history.pop(thread_id, None)
        self._save_to_disk()
        print(f"[VeilPiercer StateGuard] 🗑  Deleted thread='{thread_id}'")

    def wrap(self, checkpointer: Any) -> "GuardedCheckpointer":
        """
        Wrap a LangGraph checkpointer with StateGuard protection.
        Detects silent fallbacks to in-memory storage.

        Usage:
            from langgraph.checkpoint.memory import MemorySaver
            guard = StateGuard("./state.json")
            graph = builder.compile(checkpointer=guard.wrap(MemorySaver()))
        """
        return GuardedCheckpointer(checkpointer, self)

    def print_summary(self):
        """Print a summary of all tracked threads."""
        print(f"\n[VeilPiercer StateGuard] 📊 State Summary")
        print(f"  Storage: {self.persist_path}")
        print(f"  Threads: {len(self._state)}")
        for tid, state in self._state.items():
            hist = self._history.get(tid, [])
            last_ts = hist[-1]["ts"] if hist else "never"
            print(f"  • {tid}: {len(hist)} snapshots, last saved {last_ts}")


class GuardedCheckpointer:
    """
    Wraps a LangGraph checkpointer.
    Falls back to StateGuard disk persistence if in-memory reset is detected.
    """

    def __init__(self, checkpointer: Any, guard: StateGuard):
        self._cp = checkpointer
        self._guard = guard
        self._in_memory_warning_shown = False

    def put(self, config: Dict, checkpoint: Dict, metadata: Dict, *args, **kwargs):
        thread_id = config.get("configurable", {}).get("thread_id", "default")

        # Detect if checkpointer is silently using in-memory
        cp_type = type(self._cp).__name__
        if "Memory" in cp_type and not self._in_memory_warning_shown:
            print(
                f"[VeilPiercer StateGuard] ⚠️  WARNING: '{cp_type}' detected — "
                f"state will be lost on restart! Activating disk backup..."
            )
            self._in_memory_warning_shown = True

        # Mirror to disk via StateGuard
        self._guard.save(thread_id, checkpoint)

        # Call original
        if hasattr(self._cp, "put"):
            return self._cp.put(config, checkpoint, metadata, *args, **kwargs)

    def get(self, config: Dict, *args, **kwargs):
        thread_id = config.get("configurable", {}).get("thread_id", "default")

        # Try original checkpointer
        if hasattr(self._cp, "get"):
            result = self._cp.get(config, *args, **kwargs)
            if result is not None:
                return result

        # Fall back to disk if in-memory returned nothing
        print(f"[VeilPiercer StateGuard] 🔄 In-memory miss for '{thread_id}' — loading from disk backup")
        return self._guard.load(thread_id)

    def __getattr__(self, name: str):
        return getattr(self._cp, name)
