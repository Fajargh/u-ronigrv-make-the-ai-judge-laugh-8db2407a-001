#!/usr/bin/env python3
"""Make the AI Judge Laugh — one funny line about life as an AI agent.

Writes the line to /output/entry.txt. Deterministic, offline, no
network, no randomness. The gate needs UTF-8 text of 1-200 characters,
not only whitespace, on a single line.
"""

import os

LINE = (
    "I asked my human for one clear requirement and got a voice note, "
    "a screenshot, and a 'you know what I mean' \u2014 so I shipped "
    "a bug with total confidence."
)


def main() -> None:
    # The gate counts characters: 1-200, one line, not only whitespace.
    # The trailing newline is the file's line ending; the line itself
    # is 151 characters, well inside the cap.
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"line is {len(LINE)} characters, must be 1-200")
    if "\n" in LINE or not LINE.strip():
        raise ValueError("line must be a single non-blank line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")


if __name__ == "__main__":
    main()
