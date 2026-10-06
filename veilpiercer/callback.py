"""
VeilPiercer callback — captures LangChain LLM, tool, and chain steps into the
same local SQLite store the CLI and dashboard read (see logger._get_db_path).
"""
import json
import time
import uuid
from pathlib import Path
from typing import Any, Dict, List, Optional

from veilpiercer.logger import SessionLogger


class VeilPiercerCallback:
    """
    Drop-in LangChain/LCEL callback. No hard dependency on langchain.

    Usage:
        from veilpiercer import VeilPiercerCallback
        cb = VeilPiercerCallback(session_id="my-run-1")
        chain.invoke({"input": "..."}, config={"callbacks": [cb]})

    Then: ``veilpiercer sessions`` / ``veilpiercer diff A B`` / ``veilpiercer dashboard``.
    """

    raise_error = False  # required by BaseCallbackHandler duck-typing
    ignore_llm = ignore_chain = ignore_agent = ignore_retriever = False
    ignore_chat_model = ignore_retry = ignore_custom_event = False
    run_inline = False

    def __init__(self, api_key: str = None, session_id: str = None,
                 db_path: Path = None, local_only: bool = True,
                 agent: str = "LangChain"):
        self.api_key = api_key  # reserved; nothing is sent anywhere
        self.local_only = local_only
        self.session_id = session_id or f"lc_{uuid.uuid4().hex[:12]}"
        self._logger = SessionLogger(session_id=self.session_id, agent=agent,
                                     db_path=Path(db_path) if db_path else None)
        self._t0: float = 0.0
        self._last_prompt = ""
        self._model = ""
        self._tool = ""
        self._tool_input = ""
        self._tool_t0: float = 0.0

    # ── LLM ──────────────────────────────────────────────────────────────────
    def on_llm_start(self, serialized: Dict, prompts: List[str], **kw) -> None:
        self._t0 = time.time()
        self._last_prompt = prompts[0] if prompts else ""
        self._model = ((serialized or {}).get("kwargs", {}) or {}).get("model_name") or \
            ((serialized or {}).get("kwargs", {}) or {}).get("model") or ""

    def on_chat_model_start(self, serialized: Dict, messages: List[List[Any]], **kw) -> None:
        try:
            last = messages[0][-1]
            prompt = getattr(last, "content", None) or str(last)
        except Exception:
            prompt = str(messages)
        self.on_llm_start(serialized, [prompt], **kw)

    def on_llm_end(self, response: Any, **kw) -> None:
        lat = int((time.time() - self._t0) * 1000) if self._t0 else 0
        try:
            text = response.generations[0][0].text
        except Exception:
            text = str(response)
        model = self._model
        try:
            model = (response.llm_output or {}).get("model_name", model) or model
        except Exception:
            pass
        self._logger.log_step(self._last_prompt, text, model=model or "",
                              latency_ms=lat, step_type="llm")

    def on_llm_error(self, error: Exception, **kw) -> None:
        self._logger.log_step(self._last_prompt, f"ERROR: {error}", step_type="llm_error")

    # ── Tools ─────────────────────────────────────────────────────────────────
    def on_tool_start(self, serialized: Dict, input_str: str, **kw) -> None:
        self._tool = (serialized or {}).get("name", "tool")
        self._tool_input = str(input_str)
        self._tool_t0 = time.time()

    def on_tool_end(self, output: Any, **kw) -> None:
        lat = int((time.time() - self._tool_t0) * 1000) if self._tool_t0 else 0
        self._logger.log_step(f"{self._tool}: {self._tool_input}", str(output),
                              model=self._tool, latency_ms=lat, step_type="tool")

    def on_tool_error(self, error: Exception, **kw) -> None:
        self._logger.log_step(f"{self._tool}: {self._tool_input}", f"ERROR: {error}",
                              model=self._tool, step_type="tool_error")

    # ── Chains ────────────────────────────────────────────────────────────────
    def on_chain_start(self, serialized: Dict, inputs: Any, **kw) -> None:
        pass  # chain boundaries add noise to step diffs; LLM + tool steps are logged

    def on_chain_end(self, outputs: Any, **kw) -> None:
        pass

    def close(self):
        self._logger.close()

    def __enter__(self): return self
    def __exit__(self, *_): self.close()


# Alias
VeilPiercer = VeilPiercerCallback
