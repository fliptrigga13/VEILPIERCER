# VeilPiercer

> **Per-step tracing for local LLM pipelines. Zero cloud. Zero config.**

[![PyPI version](https://img.shields.io/pypi/v/veilpiercer.svg)](https://pypi.org/project/veilpiercer/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![CI](https://github.com/fliptrigga13/VEILPIERCER/actions/workflows/ci.yml/badge.svg)](https://github.com/fliptrigga13/VEILPIERCER/actions/workflows/ci.yml)

When your AI agent breaks, the failure didn't happen at the error. It happened 3–5 steps earlier when agents silently diverged. VeilPiercer tells you **exactly which step went wrong, what it read, and what it produced.**

Works with **Ollama, LangChain, LangGraph, CrewAI** — 100% offline, no API key needed.

---

## Install

```bash
pip install veilpiercer
```

---

## Quickstart — 60 seconds

### LangChain / LangGraph

```python
from veilpiercer import VeilPiercerCallback

cb = VeilPiercerCallback(session_id="my-run-1")

# Pass to any LangChain chain, agent, or LLM
result = chain.invoke({"input": "..."}, config={"callbacks": [cb]})
```

### Ollama (monkey-patch, 1 line)

```python
from veilpiercer import enable_ollama_tracing
enable_ollama_tracing()  # all subsequent ollama.chat() calls are traced
```

### Manual logging

```python
from veilpiercer.logger import SessionLogger

with SessionLogger.new("my-session") as s:
    s.log_step("prompt", "What is the capital of France?", model="llama3")
    s.log_step("response", "Paris.", model="llama3")
```

---

## CLI

```bash
# List all captured sessions
veilpiercer sessions

# Open the visual diff UI in your browser
veilpiercer dashboard

# Compare two sessions side-by-side
veilpiercer diff <session_a> <session_b>

# Run a demo (no agent needed)
veilpiercer demo

# Check version
veilpiercer --version
```

---

## What It Captures

Every session records:

| Event | What's stored |
|-------|--------------|
| LLM calls | prompt, output, model, token count, latency |
| Tool calls | tool name, input, output |
| Chain start/end | session metadata, duration |
| Agent steps | thought, action, observation |
| Retrievals | query, documents returned |
| Errors | exception type, traceback step |

All stored locally in **SQLite**: `vp_sessions.db` in your working directory, or wherever `VEILPIERCER_DB` points. Nothing leaves your machine.

---

## Visual Diff UI

```bash
veilpiercer demo      # generates two sample sessions
veilpiercer dashboard # opens the diff UI in your browser
```

Select any two sessions and see exactly **where they diverged** — which step produced different output, what each version of the agent saw.

---

## How It Works

```
Your Agent
    ↓ (2 lines of code)
VeilPiercerCallback
    ↓ captures every step
vp_sessions.db (local SQLite)
    ↓
veilpiercer dashboard (visual diff)
```

No backend. No cloud. Sessions are stored in `vp_sessions.db` in your working directory (override with `VEILPIERCER_DB=/path/to/file.db`). `veilpiercer dashboard` serves the diff UI from that file on `127.0.0.1:8765`.

---

## Privacy

- **100% local** — SQLite only, nothing is sent anywhere
- **No telemetry by default.** An anonymous first-run ping (Python version + OS) exists but only fires if you set `VEILPIERCER_TELEMETRY=1`
- Works fully offline — no API key, no account required
- Compatible with air-gapped environments

---

## Compatibility

| Framework | Support |
|-----------|---------|
| LangChain / LCEL | ✅ Full (LLMs, tools, chains, agents, retrievers) |
| Ollama | ✅ 1-line hook |
| LangGraph | ✅ Via LangChain callbacks |
| CrewAI | ✅ Via LangChain callbacks |
| AutoGPT | ✅ Via LangChain callbacks |
| Raw Python | ✅ `SessionLogger` directly |

---

## Feedback wanted

`pip install veilpiercer` is free and MIT-licensed. If you run local agents (Ollama, LangGraph, CrewAI) and it helps, or doesn't, open an [issue](https://github.com/fliptrigga13/VEILPIERCER/issues) with what you traced. That shapes what gets built next.

---

## License

MIT © VeilPiercer
