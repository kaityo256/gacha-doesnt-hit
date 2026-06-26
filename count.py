#!/usr/bin/env python3
from pathlib import Path

def main() -> None:
    total = 0

    # カレントディレクトリ直下の */*.md を対象にする
    for path in Path(".").glob("*/*.md"):
        text = path.read_text(encoding="utf-8")
        total += len(text)

    print(total)

if __name__ == "__main__":
    main()