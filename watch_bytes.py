#!/usr/bin/env python3
from pathlib import Path
import time

INTERVAL_SEC = 300
OUTFILE = "bytes.dat"


def total_bytes() -> int:
    return sum(p.stat().st_size for p in Path(".").glob("*/*.md") if p.is_file())


def main():
    minute = 0
    with open(OUTFILE, "w", buffering=1) as f:
        while True:
            print(f"{minute} {total_bytes()}")
            f.write(f"{minute} {total_bytes()}\n")
            minute += INTERVAL_SEC / 60
            time.sleep(INTERVAL_SEC)


if __name__ == "__main__":
    main()
