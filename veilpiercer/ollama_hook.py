"""veilpiercer.ollama_hook — auto-trace all ollama.chat() calls"""
import uuid
from veilpiercer.logger import SessionLogger

_session = None

def enable_ollama_tracing(session_id: str = None, agent: str = "Ollama"):
    global _session
    _session = SessionLogger(session_id=session_id or f"ollama_{uuid.uuid4().hex[:8]}", agent=agent)
    try:
        import ollama as _ol
        _orig = _ol.chat
        def _hook(model="", messages=None, **kw):
            import time; t = time.time()
            r = _orig(model=model, messages=messages, **kw)
            if _session:
                p = (messages[-1].get("content","") if messages else "")
                _session.log_step(p[:2000], r.get("message",{}).get("content","")[:2000], model=model, latency_ms=int((time.time()-t)*1000))
            return r
        _ol.chat = _hook
    except ImportError:
        pass
    return _session
