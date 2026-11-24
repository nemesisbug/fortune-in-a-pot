#!/usr/bin/env python3
"""Fortune in a Pot — a kind, funny fortune for the houseplant on the windowsill.

The program writes exactly one line (<=120 characters) to /output/entry.txt:
a prediction spoken to the plant itself, about its own near future in the
window — sunny, warm, and with one small joke that lands.
"""

import os

FORTUNE = (
    "Tomorrow the sun will find your newest leaf first, and your keeper "
    "will smile at you like you planned it that way."
)


def main() -> None:
    text = FORTUNE.strip()
    assert 1 <= len(text) <= 120, f"fortune is {len(text)} chars, must be 1-120"
    assert text == text.strip() and "\n" not in text, "fortune must be one line"
    text.encode("utf-8")  # gate requires UTF-8 text
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {len(text)}-char fortune to /output/entry.txt")
    print(text)


if __name__ == "__main__":
    main()
