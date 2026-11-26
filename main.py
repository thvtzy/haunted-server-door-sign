#!/usr/bin/env python3
"""Print the sign that hangs on the haunted server room door."""

from pathlib import Path

SIGN_FILE = Path(__file__).with_name("sign.txt")


def read_sign() -> str:
    return SIGN_FILE.read_text(encoding="utf-8").strip()


def main() -> None:
    print(read_sign())


if __name__ == "__main__":
    main()
