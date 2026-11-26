#!/usr/bin/env python3
"""Best advice entry for make.fun.

Writes the one-sentence answer to entry.txt inside $MAKEFUN_OUTPUT_DIR.
"""

import os

ENTRY = (
    "My first boss told me, 'Nobody remembers the extra hour you worked, "
    "but everyone remembers the promise you broke,' "
    "and I have treated every promise like a debt ever since."
)


# Guard: the answer must stay one well-formed sentence, 1-200 chars.
def validate(text):
    if not (1 <= len(text) <= 200):
        raise SystemExit("entry must be 1-200 characters")
    if not text.strip():
        raise SystemExit("entry must not be blank")
    if not any(mark in text for mark in ".!?"):
        raise SystemExit("entry must contain a sentence-ending mark")


def main():
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
