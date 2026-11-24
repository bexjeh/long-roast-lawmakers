#!/usr/bin/env python3
"""Write one satirical sentence to $MAKEFUN_OUTPUT_DIR/entry.txt."""

import os

SENTENCE = (
    "The congressman writing the law to govern artificial intelligence "
    "cannot convert his own bill to PDF, but he converted a lobbyist's "
    "lunch into law."
)


def main():
    # Gate check: the entry must be one sentence of 1-320 characters.
    text = SENTENCE.strip()
    assert 1 <= len(text) <= 320, "sentence must be 1-320 characters"
    assert text.count(".") == 1 and text.endswith("."), "must be exactly one sentence"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
