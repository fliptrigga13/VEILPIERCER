"""
Example: Fix LangGraph State Persistence with VeilPiercer StateGuard

Directly solves GitHub Issue:
  langchain-ai/langgraph — "`langgraph dev` Ignores Checkpointer Config,
  Forcing In-Memory Storage and Preventing State Persistence"

Created by Lauren Flipo (@fliptrigga13) · https://veil-piercer.com
"""

from veilpiercer import StateGuard

def main():
    print("=" * 60)
    print("VeilPiercer · LangGraph StateGuard Demo")
    print("Fixes: silent in-memory state loss on restart")
    print("github.com/fliptrigga13/veilpiercer")
    print("=" * 60)

    # --- PROBLEM: Standard LangGraph MemorySaver loses state on restart ---
    print("\n❌ WITHOUT VeilPiercer:")
    print("   graph = builder.compile(checkpointer=MemorySaver())")
    print("   → State is lost every time the process restarts")
    print("   → No warning, no error — just silent data loss")

    # --- SOLUTION: StateGuard wraps checkpointer with disk persistence ---
    print("\n✅ WITH VeilPiercer StateGuard:")

    guard = StateGuard(
        persist_path="./demo_state.json",
        verbose=True
    )

    # Simulate agent saving state across "runs"
    thread_id = "user-thread-42"

    print(f"\n--- Run 1: Agent processes messages ---")
    state_run1 = {
        "messages": [
            {"role": "user", "content": "What's the weather?"},
            {"role": "assistant", "content": "It's sunny in New York today."}
        ],
        "step": 1,
        "metadata": {"user_id": "u123"}
    }
    guard.save(thread_id, state_run1)

    print(f"\n--- Simulating process restart... ---")
    # Create a fresh guard (simulates new process)
    guard2 = StateGuard(persist_path="./demo_state.json", verbose=True)

    print(f"\n--- Run 2: Agent resumes from saved state ---")
    restored = guard2.load(thread_id)
    print(f"\n📂 Restored state: {len(restored['messages'])} messages, step={restored['step']}")
    print(f"   Last message: '{restored['messages'][-1]['content']}'")

    # Continue the conversation
    restored["messages"].append({"role": "user", "content": "What about tomorrow?"})
    restored["step"] = 2
    guard2.save(thread_id, restored)

    # Show history
    print(f"\n📊 Full state history for thread '{thread_id}':")
    for i, snapshot in enumerate(guard2.history(thread_id), 1):
        print(f"   Snapshot {i}: {snapshot['ts']} — {len(snapshot['snapshot']['messages'])} messages")

    guard2.print_summary()

    # --- Show how to wrap a real LangGraph checkpointer ---
    print("\n--- Using with real LangGraph ---")
    print("""
    from langgraph.checkpoint.memory import MemorySaver
    from veilpiercer import StateGuard

    guard = StateGuard(persist_path="./agent_state.json")
    
    # Detects silent in-memory fallback and mirrors state to disk
    checkpointer = guard.wrap(MemorySaver())
    graph = builder.compile(checkpointer=checkpointer)
    
    # Now your state survives restarts ✅
    """)

if __name__ == "__main__":
    main()
