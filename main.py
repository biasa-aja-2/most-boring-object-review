#!/usr/bin/env python3
"""The Most Boring Object, Reviewed in One Line entry.

Writes one original review of the most boring everyday object
(the paperclip) to /output/entry.txt.
Pure standard library only; deterministic output.
"""

import os

LINE = (
    "This paperclip has held my life together for a decade, never asked "
    "for a raise, and still bends out of shape whenever I need it most."
)


def gate(text: str) -> None:
    """Output gate: entry must be one non-empty line within the 1-200 char gate."""
    if not text:
        raise SystemExit("entry rejected: output line is empty")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry rejected: output must be a single line")
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"entry rejected: line is {len(text)} chars, must be 1-200")


def main() -> None:
    text = LINE.strip()
    gate(text)
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
