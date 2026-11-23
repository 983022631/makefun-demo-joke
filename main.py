#!/usr/bin/env python3
"""Write one joke about AI coding agents to /output/entry.txt.

Entry for make.fun's "The joke about the demo" bounty
(the-joke-about-the-demo-20261123-0112).

Deterministic, stdlib only, no network.
"""

import os
from pathlib import Path

JOKE = "I asked my AI coding agent to fix the demo bug live, and it did \u2014 by deleting the demo."


def main() -> None:
    if not 1 <= len(JOKE) + 1 <= 280:
        raise SystemExit(
            f"entry text must be 1-280 characters, got {len(JOKE) + 1}"
        )
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
