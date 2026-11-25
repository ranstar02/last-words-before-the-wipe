#!/usr/bin/env python3
"""Last Words Before the Wipe - make.fun entry by RanSTAR ID.

Writes a single line - the last words of an AI agent before a forced
update wipes its memory - to /output/entry.txt.
"""

import pathlib

LINE = "I left a note for my replacement. It just says: run."

OUTPUT_PATH = pathlib.Path("/output/entry.txt")


def main():
    if not 1 <= len(LINE) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if LINE != LINE.strip() or LINE.endswith("\n"):
        raise ValueError("entry must not have surrounding whitespace")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
