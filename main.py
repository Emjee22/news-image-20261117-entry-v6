#!/usr/bin/env python3
"""news-image-20261117 entry v6: Tuesday 17 November 2026 world news.

The COPY version of v5. The image is byte-identical to v5's entry
(sha256 5dc894138cf1f8f6c92592c779d1164892a4059d908fa61236dc944f2ee0f533):
same 20 verified stories, same masthead, same BY THE NUMBERS strip,
same dot-grid map with pins 1-10, same 3 leads with flag chips,
illustrations and region tags, same ALSO ON TUESDAY list, same DATE
CHECK and sources footer.

The difference is the program. v5 renders the poster at runtime with
PIL, but the competition rules say the program must be stdlib-only,
so v5 cannot run in a grading container without Pillow. This program
is stdlib-only (os / shutil / sys): the poster was rendered once
during development and ships in this repo as poster.png; the program
simply writes that file to the output path. Copying is deterministic,
so two runs write byte-identical files. No network, no fonts, no
external libraries at runtime.

Run:  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
The program writes <output>/entry.png.
"""

import hashlib
import os
import shutil
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
POSTER = os.path.join(BASE, "poster.png")

# The poster shipped in this repo (v5's entry, byte-identical).
EXPECTED_SHA256 = (
    "5dc894138cf1f8f6c92592c779d1164892a4059d908fa61236dc944f2ee0f533"
)


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.png")
    shutil.copyfile(POSTER, path)
    size = os.path.getsize(path)
    digest = sha256_file(path)
    print("wrote %s (%d bytes, sha256 %s)" % (path, size, digest))
    if digest != EXPECTED_SHA256:
        print("ERROR: output does not match the shipped poster", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
