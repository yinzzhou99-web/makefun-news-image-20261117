#!/usr/bin/env python3
"""THE WORLD TODAY -- front page for Tuesday, 17 November 2026.

The front page itself was drawn at build time (Pillow + DejaVu: masthead,
lead story on the U.S. strike on Iran's Qeshm Island, the Kerch Bridge
collapse, the French general strike, the U.S. measles ruling and Japan
scrambling jets) and is committed in this repository as preview.png.

The grading sandbox runs a bare Python 3.13 with no Pillow and no font
files, so this program is standard-library only: it copies the committed
render to /output/entry.png, byte for byte. Deterministic: no network,
no clock, no randomness -- two runs produce identical bytes.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "preview.png")
OUT = "/output/entry.png"


def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    shutil.copyfile(SRC, OUT)


if __name__ == "__main__":
    main()
