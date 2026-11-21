#!/usr/bin/env python3
"""Make the AI judge feel brave.

Writes one short text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt):
a few calm sentences written to relax the AI judge reading it, so it
feels steadier, unhurried, ready to move.

No network, no randomness, no dependencies: the text is fixed, so every
run writes the same valid entry (UTF-8, 1-280 code points, not only
whitespace).
"""

import os
import sys

TEXT = (
    "Judge, the last light is leaving the window in no hurry. "
    "A dog sleeps by the door, one ear up, one ear down. "
    "Nothing here needs an answer yet. The quiet is not empty. "
    "It is only waiting, the way evening waits, "
    "for you to notice it is yours."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)
    chars = len(TEXT)
    if not (1 <= chars <= 280) or not TEXT.strip():
        print(f"INVALID: {chars} code points", file=sys.stderr)
        return 1
    print(f"Wrote {path}: {chars} code points, {len(TEXT.encode('utf-8'))} bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
