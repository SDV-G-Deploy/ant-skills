#!/usr/bin/env python3
"""Tiny heuristic linter for ANT-style answers.

Usage:
  python3 tools/ant_lint.py answer.txt
  cat answer.txt | python3 tools/ant_lint.py

This is not a real evaluator. It only flags common wording risks.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

BAD_PHRASES = [
    "just run",
    "obviously",
    "trivial",
    "simply run",
    "you forgot to",
]

JARGON = [
    "dependency",
    "dependencies",
    "middleware",
    "endpoint",
    "schema",
    "migration",
    "runtime",
    "deploy",
    "deployment",
    "CI/CD",
    "JWT",
    "OAuth",
    "token",
    "environment variable",
]

RISK_PATTERNS = [
    r"rm\s+-rf",
    r"DROP\s+TABLE",
    r"TRUNCATE",
    r"DELETE\s+FROM",
    r"git\s+reset\s+--hard",
    r"git\s+push\s+--force",
    r"terraform\s+destroy",
    r"kubectl\s+delete",
]

CONFIRMATION_HINTS = [
    "confirm",
    "confirmation",
    "подтверд",
    "подтверждение",
]


def read_text() -> str:
    if len(sys.argv) > 1:
        return Path(sys.argv[1]).read_text(encoding="utf-8")
    return sys.stdin.read()


def main() -> int:
    text = read_text()
    lowered = text.lower()
    warnings: list[str] = []

    for phrase in BAD_PHRASES:
        if phrase in lowered:
            warnings.append(f"Avoid phrase: {phrase!r}")

    for term in JARGON:
        if term.lower() in lowered:
            # Very rough: allow if followed nearby by explanation-ish words.
            idx = lowered.find(term.lower())
            window = lowered[max(0, idx - 120): idx + 220]
            if not any(marker in window for marker in ["means", "это", "то есть", "called", "называется", "проще"]):
                warnings.append(f"Possible unexplained jargon: {term!r}")

    risky = any(re.search(pattern, text, flags=re.IGNORECASE) for pattern in RISK_PATTERNS)
    confirmed = any(hint in lowered for hint in CONFIRMATION_HINTS)
    if risky and not confirmed:
        warnings.append("Risky/destructive command appears without an obvious confirmation warning")

    if warnings:
        print("ANT lint warnings:")
        for warning in warnings:
            print(f"- {warning}")
        return 1

    print("ANT lint: no obvious issues found")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
