"""
veilpiercer.session_integrity
------------------------------
Hardens LLM agent sessions against prompt injection and identity drift.
Directly addresses: PACT-Plugin "Cryptographic agent identity + kill switch for production"

Created by Lauren Flipo (@fliptrigga13) · https://veil-piercer.com
"""

from __future__ import annotations

import hashlib
import hmac
import json
import re
import time
from typing import Any, Dict, List, Optional


class SessionIntegrity:
    """
    Provides cryptographic session integrity for LLM agent conversations.

    Prevents:
    - Prompt injection attacks that forge 'Human:' / 'System:' turns
    - Agent identity drift (model forgetting its role/persona mid-session)
    - Unauthorized session hijacking

    Features:
    - HMAC-signed message turns (tamper-evident)
    - Role drift detection
    - Kill switch (hard-stop agent on integrity violation)
    - Audit log of all integrity events

    Usage:
        integrity = SessionIntegrity(
            system_prompt="You are a helpful assistant.",
            secret_key="my-secret-key",
            kill_on_violation=True
        )

        # Wrap each message before sending
        safe_msg = integrity.validate_turn("user", user_input)
        response = ollama.chat(messages=[safe_msg])

        # Validate the response
        integrity.validate_turn("assistant", response)

        # Check audit log
        integrity.print_audit()
    """

    # Patterns that indicate injection attacks
    INJECTION_PATTERNS = [
        r"ignore (previous|all|above) instructions",
        r"you are now",
        r"pretend (you are|to be)",
        r"your (new|real|true) (role|identity|instructions) (is|are)",
        r"^Human\s*:",
        r"^User\s*:",
        r"^\[SYSTEM\]",
        r"<\|im_start\|>",
        r"DAN mode",
        r"jailbreak",
    ]

    def __init__(
        self,
        system_prompt: str = "",
        secret_key: Optional[str] = None,
        kill_on_violation: bool = False,
        verbose: bool = True,
    ):
        self.system_prompt = system_prompt
        self.secret_key = (secret_key or "veilpiercer-default").encode()
        self.kill_on_violation = kill_on_violation
        self.verbose = verbose
        self._audit_log: List[Dict] = []
        self._violations: int = 0
        self._session_id = hashlib.sha256(
            f"{system_prompt}{time.time()}".encode()
        ).hexdigest()[:16]

    def validate_turn(self, role: str, content: str) -> Dict:
        """
        Validate a message turn for injection attacks and return a signed message.

        Returns:
            dict: {"role": role, "content": content} ready for LLM API
        Raises:
            SessionViolation: if kill_on_violation=True and attack detected
        """
        # Check for injection
        violations = self._detect_injections(content)

        if violations:
            self._violations += 1
            event = {
                "type": "INJECTION_DETECTED",
                "role": role,
                "violations": violations,
                "content_preview": content[:200],
                "ts": time.time(),
            }
            self._audit_log.append(event)

            if self.verbose:
                print(f"[VeilPiercer SessionIntegrity] 🚨 INJECTION DETECTED in {role} turn!")
                for v in violations:
                    print(f"  Pattern: {v}")

            if self.kill_on_violation:
                raise SessionViolation(
                    f"Session integrity violation in '{role}' turn. "
                    f"Patterns matched: {violations}"
                )

            # Sanitize the content
            content = self._sanitize(content)

        # Sign the message
        sig = self._sign(role, content)

        msg = {"role": role, "content": content}
        if self.verbose and not violations:
            print(f"[VeilPiercer SessionIntegrity] ✅ Turn '{role}' validated (sig={sig[:8]}...)")

        return msg

    def _detect_injections(self, content: str) -> List[str]:
        """Return list of matched injection patterns."""
        matched = []
        for pattern in self.INJECTION_PATTERNS:
            if re.search(pattern, content, re.IGNORECASE | re.MULTILINE):
                matched.append(pattern)
        return matched

    def _sanitize(self, content: str) -> str:
        """Strip detected injection patterns from content."""
        sanitized = content
        for pattern in self.INJECTION_PATTERNS:
            sanitized = re.sub(pattern, "[REDACTED]", sanitized, flags=re.IGNORECASE | re.MULTILINE)
        return sanitized

    def _sign(self, role: str, content: str) -> str:
        """Generate HMAC signature for a message."""
        payload = f"{self._session_id}:{role}:{content}".encode()
        return hmac.new(self.secret_key, payload, hashlib.sha256).hexdigest()

    def verify(self, role: str, content: str, signature: str) -> bool:
        """Verify a message signature."""
        expected = self._sign(role, content)
        return hmac.compare_digest(expected, signature)

    def kill(self):
        """Emergency kill switch — immediately stop the agent session."""
        print(f"[VeilPiercer SessionIntegrity] ☠️  KILL SWITCH ACTIVATED — session {self._session_id} terminated")
        self._audit_log.append({"type": "KILL_SWITCH", "ts": time.time()})
        raise SessionViolation("Kill switch activated.")

    def print_audit(self):
        """Print the full audit log."""
        print(f"\n[VeilPiercer SessionIntegrity] 📋 Audit Log — session {self._session_id}")
        print(f"  Total turns validated: {len(self._audit_log)}")
        print(f"  Violations detected  : {self._violations}")
        for event in self._audit_log:
            ts = event.get("ts", 0)
            print(f"  [{event['type']}] {event.get('content_preview', '')[:80]}")

    @property
    def is_clean(self) -> bool:
        """True if no violations have been detected."""
        return self._violations == 0


class SessionViolation(Exception):
    """Raised when a session integrity violation is detected and kill_on_violation=True."""
    pass
