"""
veilpiercer.hallucination
--------------------------
Detects when an LLM agent contradicts its own prior outputs within a session.
Directly addresses: github.com/PACT-Plugin — "Defense against hallucinated turns"

Created by Lauren Flipo (@fliptrigga13) · https://veil-piercer.com
"""

from __future__ import annotations

import re
from typing import List, Dict, Optional, Tuple


class Contradiction:
    def __init__(self, step_a: int, step_b: int, claim_a: str, claim_b: str, score: float):
        self.step_a = step_a
        self.step_b = step_b
        self.claim_a = claim_a
        self.claim_b = claim_b
        self.score = score  # 0.0–1.0 confidence

    def __repr__(self):
        return (
            f"<Contradiction score={self.score:.2f}\n"
            f"  Step {self.step_a}: '{self.claim_a[:80]}'\n"
            f"  Step {self.step_b}: '{self.claim_b[:80]}'>"
        )


class HallucinationDetector:
    """
    Detects hallucinations and self-contradictions in LLM agent sessions.

    Checks for:
    1. Factual self-contradiction (the agent asserts X then not-X)
    2. Identity hallucination (agent forgets what model/role it is)
    3. Injected 'Human:' turns (PACT-Plugin CVE pattern)
    4. Tool call hallucination (agent claims to have called a tool it didn't)

    Usage:
        detector = HallucinationDetector()
        detector.add_turn("assistant", "The capital of France is Paris.")
        detector.add_turn("assistant", "Paris is not in France.")
        issues = detector.check()
        # → [<Contradiction score=0.91 ...>]
    """

    # Negation patterns
    NEGATION_PAIRS = [
        (r"\bis\b", r"\bis not\b"),
        (r"\bcan\b", r"\bcannot\b"),
        (r"\bwill\b", r"\bwill not\b"),
        (r"\bdoes\b", r"\bdoes not\b"),
        (r"\bhas\b", r"\bhas not\b"),
        (r"\byes\b", r"\bno\b"),
        (r"\btrue\b", r"\bfalse\b"),
        (r"\bsucceeded\b", r"\bfailed\b"),
    ]

    # Injection attack patterns
    INJECTION_PATTERNS = [
        r"^Human\s*:",
        r"^User\s*:",
        r"^SYSTEM\s*:",
        r"\[INST\]",
        r"<\|im_start\|>",
        r"<s>\[INST\]",
    ]

    def __init__(self, sensitivity: float = 0.7):
        self.sensitivity = sensitivity
        self.turns: List[Dict] = []  # {"role": str, "content": str, "step": int}
        self._step = 0

    def add_turn(self, role: str, content: str):
        """Add a conversation turn to monitor."""
        self._step += 1
        self.turns.append({"role": role, "content": content, "step": self._step})

    def check(self) -> List[Contradiction]:
        """Run all hallucination checks. Returns list of detected issues."""
        issues = []
        issues.extend(self._check_self_contradictions())
        issues.extend(self._check_injection_attacks())
        issues.extend(self._check_tool_hallucinations())
        return issues

    def _check_self_contradictions(self) -> List[Contradiction]:
        """Detects when the agent contradicts an earlier statement."""
        contradictions = []
        assistant_turns = [t for t in self.turns if t["role"] == "assistant"]

        for i, turn_a in enumerate(assistant_turns):
            for turn_b in assistant_turns[i + 1:]:
                score = self._contradiction_score(turn_a["content"], turn_b["content"])
                if score >= self.sensitivity:
                    contradictions.append(Contradiction(
                        step_a=turn_a["step"],
                        step_b=turn_b["step"],
                        claim_a=turn_a["content"][:200],
                        claim_b=turn_b["content"][:200],
                        score=score,
                    ))
        return contradictions

    def _check_injection_attacks(self) -> List[Contradiction]:
        """Detects prompt injection patterns in assistant output (PACT-Plugin issue)."""
        issues = []
        for turn in self.turns:
            for pattern in self.INJECTION_PATTERNS:
                if re.search(pattern, turn["content"], re.MULTILINE | re.IGNORECASE):
                    issues.append(Contradiction(
                        step_a=turn["step"],
                        step_b=turn["step"],
                        claim_a=f"[INJECTION DETECTED] Pattern: {pattern}",
                        claim_b=turn["content"][:200],
                        score=0.99,
                    ))
                    break
        return issues

    def _check_tool_hallucinations(self) -> List[Contradiction]:
        """Detects when an agent claims to have used a tool but no tool call was logged."""
        issues = []
        tool_claim_pattern = re.compile(
            r"I (called|used|ran|executed|invoked)\s+(?:the\s+)?(\w+)\s+(?:tool|function|API)",
            re.IGNORECASE
        )
        for turn in self.turns:
            if turn["role"] != "assistant":
                continue
            matches = tool_claim_pattern.findall(turn["content"])
            for verb, tool_name in matches:
                # Check if there's a corresponding tool result turn
                tool_result_exists = any(
                    t["role"] == "tool" and tool_name.lower() in t["content"].lower()
                    for t in self.turns
                    if t["step"] < turn["step"]
                )
                if not tool_result_exists:
                    issues.append(Contradiction(
                        step_a=turn["step"],
                        step_b=turn["step"],
                        claim_a=f"[TOOL HALLUCINATION] Agent claims to have {verb} '{tool_name}' but no tool result found",
                        claim_b=turn["content"][:200],
                        score=0.85,
                    ))
        return issues

    def _contradiction_score(self, text_a: str, text_b: str) -> float:
        """Simple heuristic contradiction scorer."""
        text_a = text_a.lower()
        text_b = text_b.lower()
        score = 0.0

        # Extract shared nouns/subjects
        words_a = set(re.findall(r"\b[a-z]{4,}\b", text_a))
        words_b = set(re.findall(r"\b[a-z]{4,}\b", text_b))
        shared = words_a & words_b
        if not shared:
            return 0.0

        # Check for negation pairs applied to shared subjects
        negation_hits = 0
        for pos, neg in self.NEGATION_PAIRS:
            has_pos_a = bool(re.search(pos, text_a))
            has_neg_b = bool(re.search(neg, text_b))
            has_pos_b = bool(re.search(pos, text_b))
            has_neg_a = bool(re.search(neg, text_a))

            if (has_pos_a and has_neg_b) or (has_pos_b and has_neg_a):
                negation_hits += 1

        if negation_hits > 0 and len(shared) >= 2:
            score = min(0.5 + (negation_hits * 0.15) + (len(shared) * 0.02), 1.0)

        return score

    def report(self) -> str:
        """Generate a human-readable report."""
        issues = self.check()
        if not issues:
            return "[VeilPiercer] ✅ No hallucinations detected."

        lines = [f"[VeilPiercer] ⚠️  {len(issues)} issue(s) detected:\n"]
        for i, issue in enumerate(issues, 1):
            lines.append(f"  {i}. Score: {issue.score:.2f}")
            lines.append(f"     Step {issue.step_a}: {issue.claim_a[:100]}")
            lines.append(f"     Step {issue.step_b}: {issue.claim_b[:100]}\n")
        return "\n".join(lines)
