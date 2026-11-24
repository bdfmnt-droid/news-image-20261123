#!/usr/bin/env python3
"""make.fun news-image-20261123 entry.

Writes one image summing up the world's news of Monday 23 November 2026
to /output/entry.png.

The image is a newspaper front page: masthead, an editorial illustration
(a divided planet - cracked earth and empty chairs at the collapsed COP31
climate talks on one side, the US Capitol and three leaders at one table
on the other), the two biggest stories as the main headline (COP31 collapse;
Democrats winning 258 House seats, their largest majority since 1992),
and five more verified stories from 23 November 2026 (the first Xi-Trump-
Putin trilateral talks; Russian missiles entering Polish airspace and
NATO's emergency meeting; Mexico capturing an FBI most-wanted drug
kingpin; plus a ticker: BepiColombo reaching Mercury, Paolo Bulgari's
death at 89, 24 dead in a Nigeria boat accident).

The image was composed at build time (see build_image.py in the workspace
and SOURCES.md) and is shipped in this repository as entry.png. This
program only copies those exact bytes to the output directory, so it is
fully deterministic: two runs write identical bytes. It uses only the
Python standard library, makes no network calls, and needs no input.
"""

import os
import shutil
import stat
import sys

IMAGE_NAME = "entry.png"


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, IMAGE_NAME)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, IMAGE_NAME)
    shutil.copyfile(src, dst)
    # The grader collects outputs as another user: leave it world-readable.
    os.chmod(dst, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    size = os.path.getsize(dst)
    print(f"wrote {dst} ({size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
