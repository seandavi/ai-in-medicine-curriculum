"""Post-render: tidy llms.txt and write llms-full.txt, the whole book as one file.

Quarto's llms-txt option writes llms.txt (an index) and a .llms.md copy of
every page. This script runs after a full render and

1. strips Quarto's span markup from the page titles in llms.txt, and
2. joins the pages, in book order, into _book/llms-full.txt: one plain
   markdown file to upload to a chatbot (for example a ChatGPT agent's
   files). Inline figures become their alt text, links between pages become
   full URLs on the site, and in-page anchors become plain text.

The file is rebuilt on every deploy, so the current copy is always at
SITE_URL/llms-full.txt. Replacing it in a chatbot means downloading that
file and uploading it again.
"""

from __future__ import annotations

import datetime as dt
import os
import posixpath
import re
import subprocess
import sys
from pathlib import Path

SITE_URL = "https://aim.seandavis.net"

# Process records, not teaching content: they add length and nothing a
# student asks about.
EXCLUDE = {"appendix/ai-ledger.llms.md", "appendix/personas.llms.md"}

TITLE_SPANS = re.compile(
    r"\[\[(?P<num>[^\]]+)\]\{\.chapter-number\}\s+\[(?P<title>.*?)\]\{\.chapter-title\}\]"
)
INDEX_LINK = re.compile(r"^- \[(?P<title>.*)\]\((?P<path>[^)]+\.llms\.md)\)\s*$", re.M)
IMAGE = re.compile(r"!\[(?P<alt>[^\]]*)\]\((?P<src>[^)]*)\)(\{[^}]*\})?")
LINK = re.compile(r"(?<!!)\[(?P<text>[^\]]+)\]\((?P<href>[^)\s]+)\)")


def clean_title(title: str) -> str:
    """'[[4]{.chapter-number}  [Centaur]{.chapter-title}]' -> '[4. Centaur]'.

    Also turns Quarto's 'Appendix C <em-dash> Name' label into 'Appendix C: Name',
    because the book does not use em-dashes.
    """
    title = TITLE_SPANS.sub(lambda m: f"[{m['num']}. {m['title']}]", title)
    return re.sub("(Appendix [A-Z]) \u2014 ", r"\1: ", title)


def page_url(rel_md: str) -> str:
    """Site URL of the HTML page a .llms.md file was made from."""
    return f"{SITE_URL}/{rel_md.removesuffix('.llms.md')}.html"


def rewrite(text: str, rel_md: str) -> str:
    """Make one page's markdown stand alone inside the combined file."""

    def image(m: re.Match[str]) -> str:
        alt = m["alt"].strip()
        return f"[Figure: {alt}]" if alt else "[Figure]"

    def link(m: re.Match[str]) -> str:
        text, href = m["text"], m["href"]
        if href.startswith("#"):
            return text  # anchors (references, figures) do not survive joining
        if re.match(r"^[a-z]+:", href):
            return m[0]  # already absolute: http, https, mailto
        path, _, frag = href.partition("#")
        target = posixpath.normpath(posixpath.join(posixpath.dirname(rel_md), path))
        if target.endswith(".llms.md"):
            url = page_url(target)
        else:
            url = f"{SITE_URL}/{target}"
        return f"[{text}]({url}{'#' + frag if frag else ''})"

    text = re.sub("^(#+ Appendix [A-Z]) \u2014 ", r"\1: ", text, flags=re.M)
    text = IMAGE.sub(image, text)
    return LINK.sub(link, text)


def commit() -> str:
    sha = os.environ.get("GITHUB_SHA")
    if sha:
        return sha[:7]
    try:
        out = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            capture_output=True, text=True, check=True,
        )
        return out.stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return "unknown"


def main() -> int:
    if not os.environ.get("QUARTO_PROJECT_RENDER_ALL"):
        return 0  # a single-page render has no complete llms.txt to work from
    out_dir = Path(os.environ.get("QUARTO_PROJECT_OUTPUT_DIR", "_book"))
    index = out_dir / "llms.txt"
    if not index.exists():
        print("llms_full: no llms.txt; is llms-txt on?", file=sys.stderr)
        return 0

    index_text = clean_title(index.read_text(encoding="utf-8"))
    # With site-url set, Quarto writes full URLs into llms.txt; work in
    # paths relative to the output directory.
    pages = [
        (m["title"], m["path"].removeprefix(SITE_URL + "/"))
        for m in INDEX_LINK.finditer(index_text)
    ]

    built = dt.date.today().isoformat()
    parts = [
        "# AI in Medicine: the full book",
        "",
        f"A four-week elective for fourth-year medical students. Website: {SITE_URL}",
        f"Built {built} from commit {commit()}. This file is regenerated on every"
        f" deploy; the current copy is at {SITE_URL}/llms-full.txt.",
        "",
        "Each page below starts with a 'Source:' line giving its web address."
        " Link students to that address rather than quoting long passages.",
        "",
        "When you combine ideas from several pages, say that the summary is"
        " yours, not the book's. Quote the book only where the words are on a"
        " page below.",
        "",
        "## Contents",
        "",
        *[f"- {title}" for title, path in pages if path not in EXCLUDE],
    ]
    for title, rel in pages:
        if rel in EXCLUDE:
            continue
        body = (out_dir / rel).read_text(encoding="utf-8").strip()
        parts += ["", "---", "", f"Source: {page_url(rel)}", "", rewrite(body, rel)]

    full = out_dir / "llms-full.txt"
    full.write_text("\n".join(parts) + "\n", encoding="utf-8")

    if "llms-full.txt" not in index_text:
        index_text = index_text.rstrip("\n") + (
            "\n\n## Optional\n\n- [The whole book in one file](llms-full.txt)\n"
        )
    index.write_text(index_text, encoding="utf-8")
    words = len(full.read_text(encoding="utf-8").split())
    print(f"llms_full: wrote {full} ({len(pages) - len(EXCLUDE)} pages, {words} words)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
