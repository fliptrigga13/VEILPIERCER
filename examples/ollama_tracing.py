"""
Example: Tracing Ollama / DeepSeek-R1 calls with VeilPiercer

Solves: "How to use DeepSeek-R1 with function calls on Ollama" 
        (github.com/vllm-project/vllm, multiple open issues)

Created by Lauren Flipo (@fliptrigga13) · https://veil-piercer.com
"""

from veilpiercer import Tracer

# --- Simulate an Ollama call (works with real ollama too) ---
def fake_ollama_chat(**kwargs):
    """Replace this with: import ollama; ollama.chat(...)"""
    import time, random
    time.sleep(0.05)
    return {
        "message": {
            "role": "assistant",
            "content": f"I am DeepSeek-R1. You asked: {kwargs['messages'][-1]['content']}"
        },
        "model": kwargs.get("model", "unknown"),
        "done": True
    }

def main():
    print("=" * 60)
    print("VeilPiercer · Ollama Tracing Demo")
    print("github.com/fliptrigga13/veilpiercer")
    print("=" * 60)

    tracer = Tracer(
        model="deepseek-r1:8b",
        session_id="ollama-demo",
        log_file="ollama_trace.jsonl",
        verbose=True
    )

    questions = [
        "What is 2 + 2?",
        "Explain gradient descent in one sentence.",
        "What did I just ask you before this?",  # Tests context
    ]

    history = []
    for q in questions:
        history.append({"role": "user", "content": q})

        response = tracer.call(
            fake_ollama_chat,
            model="deepseek-r1:8b",
            messages=history,
        )

        assistant_msg = response["message"]["content"]
        history.append({"role": "assistant", "content": assistant_msg})

    # Full trace
    tracer.print_trace()
    tracer.save("ollama_trace.json")

    print(f"\n✅ Total latency: {tracer.total_latency_ms:.0f}ms across {len(tracer.spans)} calls")
    print("📁 Trace exported to ollama_trace.json")

if __name__ == "__main__":
    main()
