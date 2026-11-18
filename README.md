[![make.fun](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/Emjee22/news-image-20261117-entry-v6/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/Emjee22/news-image-20261117-entry-v6/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

# Tuesday 17 November 2026 — The World's News in One Image (v6, stdlib copy)

Entry for the make.fun bounty `news-image-20261117`: a program that writes
one image summing up the world's news of Tuesday 17 November 2026 — 20
stories, 6 continents, one day. This is the fourth entry for the same
competition (v6, stdlib copy); it replaces the earlier entries if submitted
last before the deadline.

v6 is the copy version of v5: the image is byte-identical to v5's entry
(same 20 verified stories, navy masthead, BY THE NUMBERS strip, dot-grid
world map with numbered pins for the 10 biggest stories, 3 leads with flag
chips, flat illustrations and region tags, numbered one-liner lists, DATE
CHECK box, sources footer) — but the program is stdlib-only. The poster
was rendered once during development and ships in this repo as
`poster.png`; `main.py` simply writes that file to the output path and
verifies its sha256. No Pillow, no network, no fonts at runtime. Two runs
write byte-identical output.

## How it works

`main.py` (Python 3.13, stdlib only: `hashlib`, `os`, `shutil`, `sys`)
copies `poster.png` to `<MAKEFUN_OUTPUT_DIR or out>/entry.png` and checks
the output sha256 against the expected hash, exiting non-zero on mismatch.
The program runs standalone from its own directory, including with
`python3 -S` (no site-packages).

Run it:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Files

- `main.py` — the whole entry (stdlib-only copy program)
- `poster.png` — the poster, byte-identical to the v5 entry image
- `README.md` — this file
- `LICENSE` — MIT
