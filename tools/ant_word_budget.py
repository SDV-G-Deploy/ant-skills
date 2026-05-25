#!/usr/bin/env python3
"""Check whether a sample ANT response fits a target word budget.

Usage:
  python3 tools/ant_word_budget.py --max 80 sample.txt
  echo "Смысл: ..." | python3 tools/ant_word_budget.py --max 80
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


def count_words(text: str) -> int:
    # Counts words/numbers across Latin and Cyrillic text. Keeps commands as word-like chunks.
    return len(re.findall(r"[\wА-Яа-яЁё-]+", text, flags=re.UNICODE))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("file", nargs="?", help="Optional text file. Reads stdin when omitted.")
    parser.add_argument("--max", type=int, default=160, help="Maximum word budget")
    args = parser.parse_args()

    if args.file:
        text = Path(args.file).read_text(encoding="utf-8")
    else:
        text = sys.stdin.read()

    words = count_words(text)
    status = "PASS" if words <= args.max else "FAIL"
    print(f"{status}: {words}/{args.max} words")
    return 0 if words <= args.max else 1


if __name__ == "__main__":
    raise SystemExit(main())
