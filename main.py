#!/usr/bin/env python3
"""Write one short text for make.fun bounty u-gudril-cool-two-lines-of-morning-light-ade94fc5."""

import os
import sys
from pathlib import Path

TEXT = (
    "The cat has not moved since six.\n"
    "The square of light has, and takes her with it."
)


def output_dir() -> Path:
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        configured = os.environ.get(name)
        if configured:
            return Path(configured)
    return Path("/output")


def main() -> int:
    assert 1 <= len(TEXT) <= 280, f"text must be 1..280 characters, got {len(TEXT)}"
    directory = output_dir()
    directory.mkdir(parents=True, exist_ok=True)
    target = directory / "entry.txt"
    target.write_bytes(TEXT.encode("utf-8"))
    print(f"wrote {target} ({len(TEXT)} characters)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
