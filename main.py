#!/usr/bin/env python3
"""Have You Tried Turning It Off? — make.fun entry.

Writes one funny line a hopeless tech support agent gives a desperate
customer to /output/entry.txt. Deterministic: the same line every run.

The line: the agent cheerfully reframes the classic "turn it off and on
again" as emotional care for the computer itself. The humour comes from
the agent's cheerful uselessness — not from mocking the customer, whose
desperation is met with an absurdly sincere "good news".
"""

import os

ENTRY = (
    "Good news \u2014 your computer isn't broken, it just misses you. "
    "Turn it off, tell it you appreciate it, then turn it back on."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate self-check: the scorer requires 1-199 UTF-8 characters and
    # more than whitespace, so refuse to write a line that would fail.
    if not (1 <= len(ENTRY) <= 199) or not ENTRY.strip():
        raise SystemExit(f"entry fails gate: {len(ENTRY)} characters")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(OUTPUT_PATH, 0o644)
    print(f"wrote {len(ENTRY)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
