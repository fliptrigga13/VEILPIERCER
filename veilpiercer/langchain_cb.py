"""
veilpiercer.langchain_cb — LangChain/LCEL callback for VeilPiercer.
"""
import time
import uuid
from typing import Any
from veilpiercer.logger import SessionLogger


class VeilPiercerCallback:
    """
    Drop-in LangChain callback. Logs every LLM call to VeilPiercer.

    Usage:
        from veilpiercer import VeilPiercerCallback
        chain = LLMChain(llm=llm, callbacks=[VeilPiercerCallback()])
    """

    def __init__(self, session_id: str = None, agent: str = "LangChain",
                 local_only: bool = True):
        self.session_id = session_id or f"lc_{uuid.uuid4().hex[:12]}"
        self._logger = SessionLogger(session_id=self.session_id, agent=agent)
        self._step = 0
        self._t0 = None
        self._last_prompt = ""

    # ── LangChain BaseCallbackHandler interface ───────────────────────────────
    def on_llm_start(self, serialized: dict, prompts: list, **kw) -> None:
        self._t0 = time.time()
        self._last_prompt = prompts[0] if prompts else ""
        self._step += 1

    def on_llm_end(self, response: Any, **kw) -> None:
        latency = int((time.time() - self._t0) * 1000) if self._t0 else 0
        try:
            text = response.generations[0][0].text
        except Exception:
            text = str(response)
        model = ""
        try:
            model = response.llm_output.get("model_name", "")
        except Exception:
            pass
        self._logger.log_step(
            prompt=self._last_prompt[:2000], response=text[:2000],
            state_version=f"step_{self._step}", model=model, latency_ms=latency
        )

    def on_llm_error(self, error: Exception, **kw) -> None:
        pass

    def close(self):
        self._logger.close()

    def __enter__(self): return self
    def __exit__(self, *_): self.close()
