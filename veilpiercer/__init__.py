"""
VeilPiercer — Local-first AI agent observability.
Per-step tracing for Ollama, LangChain, LangGraph, CrewAI.
Zero cloud. Zero config. pip install veilpiercer.
"""
from veilpiercer.callback import VeilPiercerCallback
from veilpiercer.ollama_hook import enable_ollama_tracing
from veilpiercer.logger import SessionLogger

try:
    from veilpiercer.__version__ import __version__
except ImportError:
    __version__ = "0.2.0-dev"

__all__ = [
    "VeilPiercerCallback",    # LangChain/LCEL callback — drop into any chain
    "enable_ollama_tracing",  # 1-line Ollama monkey-patch
    "SessionLogger",          # manual step logging
    "__version__",
]
