"""
veilpiercer.tracer
------------------
Wraps any LLM call (Ollama, OpenAI, LangChain) and captures:
  - full prompt / response
  - latency
  - token counts (if available)
  - model name
  - session ID

Created by Lauren Flipo (@fliptrigga13) · https://veil-piercer.com
"""

from __future__ import annotations

import time
import uuid
import json
import functools
from datetime import datetime, timezone
from typing import Any, Callable, Dict, List, Optional
from pathlib import Path


class Span:
    """A single traced LLM call."""

    def __init__(
        self,
        session_id: str,
        step: int,
        model: str,
        prompt: Any,
        response: Any,
        latency_ms: float,
        metadata: Optional[Dict] = None,
    ):
        self.id = str(uuid.uuid4())[:8]
        self.session_id = session_id
        self.step = step
        self.model = model
        self.prompt = prompt
        self.response = response
        self.latency_ms = latency_ms
        self.metadata = metadata or {}
        self.timestamp = datetime.now(timezone.utc).isoformat()

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "session_id": self.session_id,
            "step": self.step,
            "model": self.model,
            "prompt": self.prompt,
            "response": self.response,
            "latency_ms": round(self.latency_ms, 2),
            "metadata": self.metadata,
            "timestamp": self.timestamp,
        }

    def __repr__(self):
        preview = str(self.response)[:80].replace("\n", " ")
        return f"<Span step={self.step} model={self.model} latency={self.latency_ms:.0f}ms response='{preview}...'>"


class Tracer:
    """
    Core VeilPiercer tracer. Wraps any callable that talks to an LLM.

    Usage:
        tracer = Tracer(session_id="my-agent-run")

        # Wrap an ollama call
        response = tracer.call(ollama.chat, model="deepseek-r1:8b", messages=[...])

        # View full trace
        tracer.print_trace()

        # Export to JSON
        tracer.save("trace.json")
    """

    def __init__(
        self,
        session_id: Optional[str] = None,
        model: str = "unknown",
        log_file: Optional[str] = None,
        verbose: bool = True,
    ):
        self.session_id = session_id or str(uuid.uuid4())[:12]
        self.model = model
        self.log_file = log_file
        self.verbose = verbose
        self.spans: List[Span] = []
        self._step = 0

    def call(self, fn: Callable, *args, model: Optional[str] = None, **kwargs) -> Any:
        """Call any LLM function and trace it."""
        self._step += 1
        step = self._step
        used_model = model or self.model

        # Extract prompt for common APIs
        prompt = self._extract_prompt(args, kwargs)

        t0 = time.perf_counter()
        try:
            result = fn(*args, **kwargs)
        except Exception as e:
            latency_ms = (time.perf_counter() - t0) * 1000
            span = Span(self.session_id, step, used_model, prompt, f"ERROR: {e}", latency_ms)
            self.spans.append(span)
            self._log(span)
            raise
        latency_ms = (time.perf_counter() - t0) * 1000

        response = self._extract_response(result)
        span = Span(self.session_id, step, used_model, prompt, response, latency_ms)
        self.spans.append(span)
        self._log(span)

        if self.log_file:
            self._append_to_file(span)

        return result

    def _extract_prompt(self, args, kwargs) -> Any:
        """Best-effort prompt extraction for Ollama / OpenAI / raw strings."""
        if "messages" in kwargs:
            msgs = kwargs["messages"]
            if msgs:
                return msgs[-1].get("content", str(msgs[-1]))
        if "prompt" in kwargs:
            return kwargs["prompt"]
        if args:
            return str(args[0])[:500]
        return "(unknown)"

    def _extract_response(self, result: Any) -> str:
        """Best-effort response extraction."""
        if isinstance(result, str):
            return result
        if isinstance(result, dict):
            # Ollama format
            if "message" in result:
                return result["message"].get("content", str(result))
            # OpenAI format
            if "choices" in result:
                return result["choices"][0].get("message", {}).get("content", str(result))
        if hasattr(result, "content"):
            return result.content
        if hasattr(result, "text"):
            return result.text
        return str(result)[:1000]

    def _log(self, span: Span):
        if self.verbose:
            color = "\033[36m"
            reset = "\033[0m"
            print(f"{color}[VeilPiercer] Step {span.step} | {span.model} | {span.latency_ms:.0f}ms{reset}")
            print(f"  Prompt : {str(span.prompt)[:120]}")
            print(f"  Response: {str(span.response)[:120]}")

    def _append_to_file(self, span: Span):
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(json.dumps(span.to_dict()) + "\n")

    def print_trace(self):
        """Pretty-print the full session trace."""
        print(f"\n\033[1m[VeilPiercer] Session: {self.session_id} — {len(self.spans)} calls\033[0m")
        for span in self.spans:
            print(f"\n  Step {span.step} | {span.model} | {span.latency_ms:.0f}ms | {span.timestamp}")
            print(f"    Prompt  : {str(span.prompt)[:200]}")
            print(f"    Response: {str(span.response)[:200]}")

    def save(self, path: str):
        """Export full trace as JSON."""
        data = {
            "session_id": self.session_id,
            "spans": [s.to_dict() for s in self.spans],
            "created_by": "VeilPiercer · https://veil-piercer.com · @fliptrigga13",
        }
        Path(path).write_text(json.dumps(data, indent=2), encoding="utf-8")
        print(f"[VeilPiercer] Trace saved → {path}")

    def get_span(self, step: int) -> Optional[Span]:
        """Get a specific span by step number."""
        for s in self.spans:
            if s.step == step:
                return s
        return None

    @property
    def total_latency_ms(self) -> float:
        return sum(s.latency_ms for s in self.spans)


def trace(model: str = "unknown", session_id: Optional[str] = None, verbose: bool = True):
    """
    Decorator to auto-trace any function that calls an LLM.

    Usage:
        @trace(model="deepseek-r1:8b")
        def my_agent_call(prompt):
            return ollama.chat(...)
    """
    def decorator(fn: Callable):
        tracer = Tracer(session_id=session_id, model=model, verbose=verbose)

        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            return tracer.call(fn, *args, **kwargs)

        wrapper.tracer = tracer
        return wrapper

    return decorator
