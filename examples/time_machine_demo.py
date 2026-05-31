"""
Example: Fork & Replay Agent Sessions with TimeMachine

Directly solves: Show HN: "Time Machine — Debug AI Agents by Forking and
Replaying from Any Step" (top HN post — this is the open-source implementation)

Created by Lauren Flipo (@fliptrigga13) · https://veil-piercer.com
"""

from veilpiercer import TimeMachine

def fake_agent(messages, **kwargs):
    """Simulates an LLM agent response."""
    last = messages[-1]["content"] if messages else "?"
    return {"role": "assistant", "content": f"Agent response to: '{last}'"}

def main():
    print("=" * 60)
    print("VeilPiercer · Time Machine Demo")
    print("Fork & replay agent sessions from any step")
    print("github.com/fliptrigga13/veilpiercer")
    print("=" * 60)

    tm = TimeMachine(storage_path="./tm_sessions")

    # --- Record a full agent session ---
    print("\n🔴 Recording agent session...")
    with tm.record("session-alpha") as session:
        session.log({
            "messages": [{"role": "user", "content": "Plan a trip to Paris"}],
            "response": "I'll plan a 5-day Paris trip for you.",
            "step_name": "plan"
        })
        session.log({
            "messages": [{"role": "user", "content": "Book flights"}],
            "response": "Searching for flights to Paris CDG...",
            "step_name": "search_flights"
        })
        session.log({
            "messages": [{"role": "user", "content": "What hotels are available?"}],
            "response": "I found 3 hotels near the Eiffel Tower.",
            "step_name": "search_hotels"
        })
        session.log({
            "messages": [{"role": "user", "content": "Book the Ritz"}],
            "response": "ERROR: Booking service unavailable.",
            "step_name": "book_hotel"  # ← Something went wrong here
        })

    # --- Fork from step 3 (before the error) ---
    print("\n🍴 Forking from step 3 to try different hotel booking...")
    fork = tm.fork("session-alpha", from_step=3)

    # Replay with a different input
    result = tm.replay(
        fork,
        agent_fn=fake_agent,
        new_input="Book the Hotel de Ville instead of the Ritz"
    )
    print(f"   Fork result: {result['content']}")

    # --- Show the diff ---
    tm.diff("session-alpha", fork.fork_id)

    # --- Save and reload ---
    print("\n💾 Saving session to disk...")
    tm.save_session("session-alpha", "session_alpha.json")

    print("\n📂 Reloading session from disk (simulates restart)...")
    tm2 = TimeMachine()
    sid = tm2.load_session("session_alpha.json")
    print(f"   Loaded session '{sid}' — can fork and replay again!")

    print("\n✅ Time Machine complete.")
    print("   → Any agent step can be forked and replayed without re-running the pipeline.")

if __name__ == "__main__":
    main()
