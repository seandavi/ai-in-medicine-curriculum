"""Copy the rendered decks, and their narration scripts, into the book's output.

Runs as the slides project's post-render step. Quarto renders the decks inside
this project (slides/_output/); the deployed site serves them from
_book/slides/, next to the book, so the decks' ../images/ and ../chapters/
links resolve. Each *-narration.md is copied as .txt, so a browser shows it
as plain text: students can read along or translate it.
"""

import os
import shutil
from pathlib import Path

here = Path(__file__).resolve().parent
src = here / os.environ.get("QUARTO_PROJECT_OUTPUT_DIR", "_output")
dst = here.parent / "_book" / "slides"
shutil.copytree(src, dst, dirs_exist_ok=True)
print(f"copied {src.relative_to(here.parent)}/ to {dst.relative_to(here.parent)}/")
for script in here.glob("*-narration.md"):
    shutil.copyfile(script, dst / f"{script.stem}.txt")
    print(f"copied {script.name} to {dst.relative_to(here.parent)}/{script.stem}.txt")
