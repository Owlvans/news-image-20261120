"""make.fun entry for news-image-20261120 — "Sum up 20 November's world news in one image".

The entry is a one-page broadsheet, THE WORLD IN ONE DAY, drawn and typeset
from hand-written HTML/SVG and rendered to entry.png beside this file. Every
story on the page was reported on Friday 20 November 2026 and carries its
source; the program's whole job is to deliver those exact bytes, unchanged,
to the output directory as entry.png.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def output_path() -> Path:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir / "entry.png"


def main() -> None:
    if not SOURCE.is_file():
        raise SystemExit(f"entry image missing beside main.py: {SOURCE}")
    target = output_path()
    shutil.copyfile(SOURCE, target)
    data = target.read_bytes()
    if data != SOURCE.read_bytes():
        raise SystemExit("copied image differs from the shipped entry.png")
    print(f"wrote {target} ({len(data)} bytes)")


if __name__ == "__main__":
    main()
