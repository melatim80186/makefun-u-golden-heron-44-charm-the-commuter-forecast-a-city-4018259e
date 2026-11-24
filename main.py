#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather forecast (at most 140 characters) for the
invented city of Snuzzleford to /output/entry.txt.

Deterministic: no network, no randomness, no time dependence. The line
was chosen after three review rounds over ten candidates (see REVIEW.md).
"""

import os

ENTRY = (
    # Snuzzleford: the snow spells the train times in the sky, and the
    # 8:15 is delayed by a very polite blizzard. Forecast register kept
    # (times, delay, named city); the joke is the politeness, not the snow.
    "In Snuzzleford, light snow spells out the train times in the sky "
    "\u2014 7:42 on time, 8:15 delayed by a very polite blizzard."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars, must be 1-140"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
