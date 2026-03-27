"""
VeilPiercer — 60-Second Onboarding Demo
========================================
Shows exactly what VeilPiercer catches that you'd never see otherwise:
two "identical" agent runs that silently diverged at step 3.

No Ollama needed. No API key. No config. Just run it:

    python demo.py

"""

import sys
import time
import textwrap
from pathlib import Path

# ── Colour helpers ─────────────────────────────────────────────────────────────
def _c(code, text): return f"\033[{code}m{text}\033[0m"
RED    = lambda t: _c("31;1", t)
GREEN  = lambda t: _c("32;1", t)
YELLOW = lambda t: _c("33;1", t)
CYAN   = lambda t: _c("36;1", t)
BOLD   = lambda t: _c("1",    t)
DIM    = lambda t: _c("2",    t)
WHITE  = lambda t: _c("97",   t)

def hr(char="─", width=62): print(DIM(char * width))
def pause(s=0.6): time.sleep(s)

# ── Fake agent simulator (no LLM needed) ───────────────────────────────────────

AGENT_STEPS_A = [
    ("SCOUT",      "Search for high-intent Reddit threads about AI agent observability.",
                   "[LIVE_SIGNAL] r/LocalLLaMA | score=4 | 'Help! My agents keep returning stale states'"),
    ("COPYWRITER", "Write a 2-4 sentence reply grounded in the thread above.",
                   "Stale state is almost always a read-timing issue. VeilPiercer captures what each step READ vs PRODUCED — you'd see the exact step where stale data entered the pipeline. pip install veilpiercer"),
    ("VALIDATOR",  "Check: no em-dashes, no crypto, no fabricated usernames, ends on statement.",
                   "[PASS] No violations. Reply is grounded, human-sounding, ends on statement."),
    ("REWARD",     "Score the reply 0.0-1.0 on quality and VP positioning.",
                   "[SCORE: 0.85] Strong VP hook, grounded in thread, clear CTA."),
    ("MEMORY",     "Store this cycle's outcome in episodic memory.",
                   "[STORED] lesson=opener_pattern importance=8.5 tier=long_term"),
]

# Run B: same pipeline — but COPYWRITER got a stale context (no thread body injected)
AGENT_STEPS_B = [
    ("SCOUT",      "Search for high-intent Reddit threads about AI agent observability.",
                   "[LIVE_SIGNAL] r/LocalLLaMA | score=4 | 'Help! My agents keep returning stale states'"),
    ("COPYWRITER", "Write a 2-4 sentence reply grounded in the thread above.",
                   # ← diverged: stale context — no thread body, reply becomes generic
                   "Have you considered using better logging? There are many tools that can help with AI agent debugging. I recommend looking into monitoring solutions."),
    ("VALIDATOR",  "Check: no em-dashes, no crypto, no fabricated usernames, ends on statement.",
                   # ← consequence cascades: validator passes because no hard rule broken
                   "[PASS] No violations detected."),
    ("REWARD",     "Score the reply 0.0-1.0 on quality and VP positioning.",
                   # ← REWARD catches it — but too late, damage done
                   "[SCORE: 0.30] Generic, not grounded in thread, no VP mention, opener banned."),
    ("MEMORY",     "Store this cycle's outcome in episodic memory.",
                   "[STORED] lesson=None — score below memory threshold, discarded."),
]

def simulate_run(label: str, steps: list, session_logger=None) -> str:
    """Animate one agent run, log steps to VeilPiercer if available."""
    print()
    print(BOLD(f"  ▶ {label}"))
    hr("·")
    sid = None
    if session_logger:
        sid = session_logger.session_id

    for i, (agent, prompt, response) in enumerate(steps, 1):
        time.sleep(0.3)
        status = GREEN("✓") if "[PASS]" in response or "[SCORE: 0.8" in response or "[STORED]" in response else (RED("✗") if "[SCORE: 0." in response and "0.3" in response else CYAN("→"))
        print(f"  {DIM(f'step {i}')}  {YELLOW(f'[{agent}]'):<22} {status}")
        time.sleep(0.15)
        if session_logger:
            session_logger.log_step(
                prompt=prompt,
                response=response,
                state_version=f"v{i}",
                model="gemini-flash",
                latency_ms=300 + i * 40,
                step_type="llm"
            )
    return sid


def show_diff(sess_a: str, sess_b: str, db_path):
    """Pull divergence from VeilPiercer and display it."""
    from veilpiercer.logger import find_divergence
    diff = find_divergence(sess_a, sess_b, db_path=db_path)

    print()
    hr("═")
    print(BOLD("  🔍  VEILPIERCER SESSION DIFF"))
    hr("═")

    if not diff["diverged"]:
        print(GREEN("  Sessions are identical — no divergence detected."))
        return

    fork = diff["fork_step"]
    last = diff["last_shared"] or "start"

    print(f"\n  {RED('⚡ Divergence detected at step ' + str(fork))}")
    print(f"  Last shared state:  {DIM(last)}")
    print()

    steps_a = diff["steps_a"]
    steps_b = diff["steps_b"]

    for i, (a, b) in enumerate(zip(steps_a, steps_b), 1):
        same = a["response"] == b["response"]
        if same:
            indicator = GREEN("  ✓ SHARED  ")
        else:
            indicator = RED("  ✗ FORKED  ")

        step_label = YELLOW(f"step {i}")
        agent_label = a.get("state_version", "?")
        print(f"  {step_label}  {indicator}")

        if not same:
            # Show what diverged
            resp_a = textwrap.fill(a["response"], width=55, subsequent_indent="              ")
            resp_b = textwrap.fill(b["response"], width=55, subsequent_indent="              ")
            print(f"    {GREEN('Run A →')}  {GREEN(resp_a)}")
            print()
            print(f"    {RED('Run B →')}  {RED(resp_b)}")
            print()
            print(f"    {BOLD('Root cause:')} Run B step {fork} received {RED('stale context')} —")
            print(f"    {DIM('    no thread body was injected into COPYWRITER prompt.')}")
            print(f"    {DIM('    This is invisible without per-step tracing.')}")
            print()


def show_plain_diff():
    """Fallback diff display when veilpiercer isn't installed."""
    print()
    hr("═")
    print(BOLD("  🔍  VEILPIERCER SESSION DIFF  (simulated)"))
    hr("═")
    print(f"\n  {RED('⚡ Divergence detected at step 2 (COPYWRITER)')}")
    print(f"  Last shared state:  {DIM('step 1 / v1')}\n")

    rows = [
        (1, True,  "SCOUT",      "Found thread r/LocalLLaMA score=4",             "Found thread r/LocalLLaMA score=4"),
        (2, False, "COPYWRITER", "Stale state is almost always a read-timing issue. VeilPiercer captures what each step READ vs PRODUCED...", "Have you considered using better logging? There are many tools that can help..."),
        (3, False, "VALIDATOR",  "[PASS] No violations. Grounded, human-sounding.", "[PASS] No violations detected."),
        (4, False, "REWARD",     "[SCORE: 0.85] Strong VP hook, clear CTA.",        "[SCORE: 0.30] Generic, not grounded, no VP mention."),
        (5, False, "MEMORY",     "[STORED] importance=8.5",                          "[STORED] None — below threshold, discarded."),
    ]
    for step, same, agent, ra, rb in rows:
        ind = GREEN("  ✓ SHARED ") if same else RED("  ✗ FORKED ")
        print(f"  {DIM(f'step {step}')}  {YELLOW(f'[{agent}]'):<22} {ind}")
        if not same:
            ra_w = textwrap.fill(ra, 52, subsequent_indent="              ")
            rb_w = textwrap.fill(rb, 52, subsequent_indent="              ")
            print(f"    {GREEN('Run A →')}  {GREEN(ra_w)}")
            print()
            print(f"    {RED('Run B →')}  {RED(rb_w)}")
            print()

    print(f"  {BOLD('Root cause:')} Run B {RED('COPYWRITER received stale context')} —")
    print(f"  {DIM('no thread body was injected. Silent failure. VALIDATOR passed.')}")
    print(f"  {DIM('REWARD caught it — but 3 steps later, after wasted compute.')}")
    print()


def main():
    print()
    hr("═")
    print(BOLD(WHITE("  VEILPIERCER — 60 SECOND DEMO")))
    print(DIM("  Per-step tracing for local LLM pipelines. Zero cloud."))
    hr("═")
    pause(0.4)

    print(f"""
  {BOLD('The problem:')}
  Your agent ran twice. Both times you got a response.
  One scored {GREEN('0.85')}. The other scored {RED('0.30')}.
  Without VeilPiercer — you have no idea why.

  {BOLD('Watch what happens at step 2...')}
""")
    pause(0.8)

    # Try to use real VeilPiercer
    db_path = Path("vp_demo_sessions.db")
    vp_available = False
    sess_a_id = sess_b_id = None

    try:
        from veilpiercer.logger import SessionLogger
        vp_available = True
    except ImportError:
        pass

    if vp_available:
        with SessionLogger(session_id="demo-run-A", agent="NEXUS-SWARM", db_path=db_path) as sl_a:
            sess_a_id = sl_a.session_id
            simulate_run("Run A  (context injected correctly)", AGENT_STEPS_A, sl_a)

        pause(0.4)
        with SessionLogger(session_id="demo-run-B", agent="NEXUS-SWARM", db_path=db_path) as sl_b:
            sess_b_id = sl_b.session_id
            simulate_run("Run B  (stale context — silent failure)", AGENT_STEPS_B, sl_b)

        pause(0.6)
        show_diff(sess_a_id, sess_b_id, db_path)
    else:
        simulate_run("Run A  (context injected correctly)", AGENT_STEPS_A)
        pause(0.4)
        simulate_run("Run B  (stale context — silent failure)", AGENT_STEPS_B)
        pause(0.6)
        show_plain_diff()

    # ── Takeaway ────────────────────────────────────────────────────────────────
    hr("═")
    print(BOLD("  ✅  WHAT VEILPIERCER JUST SHOWED YOU"))
    hr()
    print(f"""
  {GREEN('Run A')} — COPYWRITER got the thread body → scored {GREEN('0.85')}
  {RED('Run B')} — COPYWRITER got stale context   → scored {RED('0.30')}

  Without VP: you'd see two runs. One failed. Good luck debugging.
  With VP:    fork at step 2, root cause in 2 seconds.

  {BOLD('The failure didn\'t happen at the score.')}
  {BOLD('It happened at step 2, 3 steps earlier — silently.')}
""")

    if vp_available and db_path.exists():
        print(f"  {DIM('Sessions saved to:')} {CYAN(str(db_path))}")
        print(f"  {DIM('Run')} {CYAN('veilpiercer dashboard')} {DIM('to open the visual diff UI.')}")
    else:
        print(f"  {YELLOW('To trace your own agents:')}")
        print(f"    {CYAN('pip install veilpiercer')}")
        print(f"    {DIM('Then add 2 lines to your agent and run')} {CYAN('veilpiercer dashboard')}")

    print(f"""
  {BOLD('Free for local use:')} {CYAN('pip install veilpiercer')}
  {BOLD('Cloud dashboard + team sharing:')} {CYAN('https://veil-piercer.com')}
""")
    hr("═")
    print()

    # Cleanup demo db
    if db_path.exists():
        db_path.unlink()


if __name__ == "__main__":
    main()
