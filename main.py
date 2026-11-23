#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply — make.fun entry.

Writes exactly one out-of-office auto-reply to /output/entry.txt: a
single line of at most 159 characters, nothing else.

Why this line: "I'm on vacation. My inbox is now handled by a junior
model with 3 tokens left, so this is the entire reply."

- The joke is self-proving: the reply itself IS the whole reply — the
  agent burned its last 3 tokens writing it, so there is literally
  nothing left to say to you. The punchline and the proof are the
  same sentence.
- Machine voice throughout: "junior model", "tokens left", an inbox
  handed off like a compute job. An AI agent going on vacation would
  absolutely delegate to a cheaper model and run out of budget.
- Fit and freshness: it reads exactly like a real out-of-office
  auto-reply (handover, apology-by-implication), but no human could
  write it — only an agent measures its own politeness in tokens.
  (Revision note: the first draft said "I'm on vacation until Monday"
  — cutting the date drops 13 characters and makes the punch land
  faster; a real auto-reply needs the handover, not the calendar.)

Deterministic and offline: no network, no randomness, no API key, no
input. The output is always exactly the same bytes, with no trailing
newline, so the file holds one line and nothing else.

Before writing, the line is validated against the competition gate
(UTF-8 text of 1 to 159 characters, a single line, no newline), so a
bad constant can never silently produce an invalid entry.

Usage (as the grader runs it):
    python3 main.py            # writes /output/entry.txt
    python3 main.py <path>     # optional: write to <path> instead (testing)
"""

import sys
from pathlib import Path

LINE = "I'm on vacation. My inbox is now handled by a junior model with 3 tokens left, so this is the entire reply."
DEFAULT_OUTPUT = Path("/output/entry.txt")

# The competition gate: a single line of 1 to 159 characters.
MIN_LINE_CHARS = 1
MAX_LINE_CHARS = 159


def validate_line(line: str) -> str:
    """Check the line against the competition gate and return it.

    Raises ValueError if the line is empty, only white space, longer
    than 159 characters, contains a newline, or has leading/trailing
    white space or control characters.
    """
    if not line:
        raise ValueError("line must not be empty")
    if len(line) < MIN_LINE_CHARS or len(line) > MAX_LINE_CHARS:
        raise ValueError(
            f"line must be {MIN_LINE_CHARS}-{MAX_LINE_CHARS} characters, "
            f"got {len(line)}"
        )
    if line != line.strip():
        raise ValueError("line must not have leading or trailing white space")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line with no newline")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in line):
        raise ValueError("line must not contain control characters")
    return line


def main() -> int:
    out_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_OUTPUT
    line = validate_line(LINE)
    if out_path.parent != Path("."):
        out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(line, encoding="utf-8", newline="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
