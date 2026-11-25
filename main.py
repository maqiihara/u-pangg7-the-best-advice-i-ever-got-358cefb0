#!/usr/bin/env python3
"""The Best Advice I Ever Got -- one sentence, up to 200 characters.

Writes the entry to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Standard library only; no network, no randomness.
"""
import os

LINE = (
    "My first boss told me, 'Nobody remembers the extra hour you worked, "
    "but everyone remembers the promise you broke,' and I have treated "
    "every promise like a debt ever since."
)


def validate(text):
    """The gate: one sentence, 1-200 chars, non-whitespace UTF-8 text."""
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"entry is {len(text)} chars, gate needs 1-200")
    if text.strip() != text or not text.strip():
        raise SystemExit("entry must be non-whitespace text")
    if text.count(".") + text.count("!") + text.count("?") < 1:
        raise SystemExit("entry must be a sentence")


def main():
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
