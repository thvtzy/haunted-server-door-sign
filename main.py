#!/usr/bin/env python3
"""Print the sign that hangs on the haunted server room door."""

from pathlib import Path

SIGN_FILE = Path(__file__).with_name("sign.txt")


def read_sign() -> str:
    return SIGN_FILE.read_text(encoding="utf-8").strip()


def framed(text: str) -> str:
    """Render the line the way it hangs on the door: boxed, like a real sign."""
    bar = "+" + "-" * (len(text) + 2) + "+"
    return f"{bar}\n| {text} |\n{bar}"


def main() -> None:
    print(framed(read_sign()))


if __name__ == "__main__":
    main()
