"""
VeilPiercer — LLM Agent Observability SDK
Created by Lauren Flipo (@fliptrigga13)
https://veil-piercer.com
"""

from .tracer import Tracer, trace
from .hallucination import HallucinationDetector
from .time_machine import TimeMachine
from .state_guard import StateGuard
from .session_integrity import SessionIntegrity
from .audit import RepoAuditor, AuditReport


__version__ = "1.0.0"
__author__ = "Lauren Flipo"
__url__ = "https://veil-piercer.com"

import sys

def _banner():
    print(f"\033[90mVeilPiercer v{__version__} · {__url__} · github.com/fliptrigga13\033[0m", file=sys.stderr)

_banner()

__all__ = [
    "Tracer",
    "trace",
    "HallucinationDetector",
    "TimeMachine",
    "StateGuard",
    "SessionIntegrity",
]
