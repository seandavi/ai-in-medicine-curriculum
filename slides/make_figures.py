"""Generate the SVG figures used by the slide decks.

Standard library only. Run from the repository root:

    python3 slides/make_figures.py

Writes into images/, next to the book's other figures, so a chapter can use
the same file. Every figure draws its own white card, so it reads the same on
the dark slide theme and the light book theme. Data figures are redrawn from
the numbers in the cited paper; the illustrative figure says so in its legend.
"""

from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "images"

INK = "#1f2933"
MUTED = "#5f6b7a"
BLUE = "#1f5fa8"
ORANGE = "#c45a00"
RED = "#b3261e"
GREEN = "#2e7d4f"
GRID = "#d9dee5"
FONT = "Helvetica, Arial, sans-serif"

ARROW_DEFS = (
    "<defs>"
    f'<marker id="head" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" orient="auto-start-reverse">'
    f'<path d="M0,0 L10,5 L0,10 z" fill="{INK}"/></marker>'
    f'<marker id="head-muted" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" orient="auto-start-reverse">'
    f'<path d="M0,0 L10,5 L0,10 z" fill="{MUTED}"/></marker>'
    "</defs>"
)


def svg(width: int, height: int, body: list[str], title: str, desc: str) -> str:
    return "\n".join(
        [
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
            f'width="{width}" height="{height}" role="img" font-family="{FONT}">',
            f"<title>{escape(title)}</title>",
            f"<desc>{escape(desc)}</desc>",
            ARROW_DEFS,
            f'<rect x="0" y="0" width="{width}" height="{height}" rx="14" fill="#ffffff"/>',
            *body,
            "</svg>",
            "",
        ]
    )


def text(x, y, s, size=22, fill=INK, anchor="start", weight="normal") -> str:
    return (
        f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" '
        f'text-anchor="{anchor}" font-weight="{weight}">{escape(s)}</text>'
    )


def box(x, y, w, h, lines, fill="#eef3fb", stroke=BLUE, size=22, ink=INK, bold_first=False) -> list[str]:
    """A rounded box with centred lines of text."""
    out = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" stroke="{stroke}" stroke-width="2.5"/>']
    step = size * 1.3
    y0 = y + h / 2 - step * (len(lines) - 1) / 2 + size * 0.35
    for i, line in enumerate(lines):
        weight = "bold" if bold_first and i == 0 else "normal"
        out.append(text(x + w / 2, y0 + i * step, line, size, ink, "middle", weight))
    return out


def arrow(x1, y1, x2, y2, dashed=False, muted=False) -> str:
    color = MUTED if muted else INK
    dash = ' stroke-dasharray="9 7"' if dashed else ""
    head = "head-muted" if muted else "head"
    return (
        f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="2.5"{dash} '
        f'marker-end="url(#{head})"/>'
    )


def legend_line(x, y, label, dashed=False) -> list[str]:
    dash = ' stroke-dasharray="9 7"' if dashed else ""
    return [
        f'<line x1="{x}" y1="{y - 7}" x2="{x + 50}" y2="{y - 7}" stroke="{INK}" stroke-width="2.5"{dash} marker-end="url(#head)"/>',
        text(x + 62, y, label, 20, MUTED),
    ]


def egfr_bridge() -> str:
    """What the eGFR equation takes in and what it stands for (Inker et al. 2021)."""
    w, h = 1200, 560
    body = []
    # What the lab has.
    body.append(f'<rect x="40" y="40" width="300" height="330" rx="12" fill="#f7f9fb" stroke="{GRID}" stroke-width="2"/>')
    body.append(text(190, 76, "What the lab has", 22, MUTED, "middle", "bold"))
    body += box(80, 100, 220, 64, ["Age"])
    body += box(80, 190, 220, 64, ["Sex"])
    body += box(80, 280, 220, 64, ["Creatinine"])
    # The equation.
    body += box(395, 140, 370, 150, ["eGFR = f(creatinine, age, sex)", "learned from 8,254 people", "whose GFR was measured"],
                fill="#fff7e6", stroke=ORANGE, size=21, bold_first=True)
    body.append(arrow(300, 132, 393, 190))
    body.append(arrow(300, 222, 393, 215))
    body.append(arrow(300, 312, 393, 240))
    # Output and the truth it stands for.
    body += box(830, 150, 330, 110, ["eGFR", "the number on your panel"], bold_first=True)
    body.append(arrow(765, 212, 828, 205))
    body += box(830, 340, 330, 110, ["Measured GFR", "rarely done in routine care"], fill="#eef7f1", stroke=GREEN, bold_first=True)
    body.append(arrow(995, 260, 995, 338, dashed=True))
    body.append(text(1010, 306, "stands in for", 20, MUTED))
    # What moves creatinine without moving GFR.
    body += box(40, 420, 330, 80, ["Muscle mass · diet ·", "drugs that block secretion"], fill="#f1f3f5", stroke="#9aa0a6", ink=MUTED, size=21)
    body.append(arrow(190, 420, 190, 346, dashed=True, muted=True))
    body.append(text(205, 395, "changes creatinine, not GFR", 19, MUTED))
    # Legend.
    ly = h - 22
    body += legend_line(430, ly, "goes into")
    body += legend_line(640, ly, "stands in for, or changes without changing GFR", dashed=True)
    return svg(
        w, h, body,
        "What the eGFR equation takes in and what it stands for",
        "Diagram. Age, sex, and creatinine, the three things the lab has, feed an equation learned from 8,254 people "
        "whose GFR was measured. The equation outputs the eGFR on your panel, which stands in for measured GFR, rarely "
        "done in routine care. A grey box, muscle mass, diet, and drugs that block secretion, changes creatinine "
        "without changing GFR.",
    )


def model_loop() -> str:
    """The loop every learned model comes from."""
    w, h = 1200, 500
    body = []
    y, bh = 60, 130
    body += box(30, y, 200, bh, ["Raw material", "labs, images,", "notes, text"], bold_first=True, size=21)
    body += box(280, y, 190, bh, ["Predictors"], bold_first=True)
    body += box(520, y, 260, bh, ["Learn", "find f so that", "truth ≈ f(predictors)"], fill="#fff7e6", stroke=ORANGE, bold_first=True, size=21)
    body += box(830, y, 340, bh, ["Model", "response = f(predictors)"], bold_first=True)
    body.append(arrow(230, y + bh / 2, 278, y + bh / 2))
    body.append(arrow(470, y + bh / 2, 518, y + bh / 2))
    body.append(arrow(780, y + bh / 2, 828, y + bh / 2))
    # Truth feeds learning.
    body += box(440, 280, 360, 130, ["Truth for each case", "measured GFR, sepsis yes/no,", "the next word"], fill="#eef7f1", stroke=GREEN, bold_first=True, size=21)
    body.append(arrow(620, 280, 620, y + bh + 2))
    # A new case goes up into the model; the prediction comes down out of it.
    body += box(830, 290, 210, 80, ["New case,", "truth unknown"], fill="#f1f3f5", stroke="#9aa0a6", size=21)
    body += box(1060, 290, 120, 80, ["Prediction"], fill="#f1f3f5", stroke="#9aa0a6", size=21, bold_first=True)
    body.append(arrow(935, 290, 935, y + bh + 2))
    body.append(arrow(1120, y + bh, 1120, 288))
    ly = h - 20
    body.append(f'<rect x="30" y="{ly - 20}" width="26" height="22" rx="5" fill="#fff7e6" stroke="{ORANGE}" stroke-width="2"/>')
    body.append(text(66, ly, "the learning step", 20, MUTED))
    body.append(f'<rect x="280" y="{ly - 20}" width="26" height="22" rx="5" fill="#eef7f1" stroke="{GREEN}" stroke-width="2"/>')
    body.append(text(316, ly, "the truth, known only for training cases", 20, MUTED))
    body.append(f'<rect x="760" y="{ly - 20}" width="26" height="22" rx="5" fill="#f1f3f5" stroke="#9aa0a6" stroke-width="2"/>')
    body.append(text(796, ly, "use on a new patient", 20, MUTED))
    return svg(
        w, h, body,
        "The loop every learned model comes from",
        "Diagram. Raw material such as labs, images, notes, or text becomes predictors. The truth for each case, such as "
        "measured GFR, sepsis yes or no, or the next word, joins them in a learning step that finds f so that truth is "
        "approximately f of predictors. The result is a model. A new case with unknown truth goes through the model "
        "to give a prediction.",
    )


def lost_in_the_middle() -> str:
    """Liu et al. 2024 (TACL), 20-document multi-document QA, GPT-3.5-Turbo.

    Accuracy by position of the one document that holds the answer, from the
    paper's appendix table for 20 total retrieved documents (arXiv v3 HTML,
    checked 2026-10-03). Closed-book accuracy (no documents at all) is from
    the paper's Table 1.
    """
    positions = [1, 5, 10, 15, 20]
    accuracy = [75.8, 57.2, 53.8, 55.4, 63.2]
    closed_book = 56.1

    w, h = 1100, 600
    left, right, top, bottom = 110, 1040, 80, 460
    ymin, ymax = 50, 80

    def px(p):
        return left + (p - 1) / 19 * (right - left)

    def py(a):
        return bottom - (a - ymin) / (ymax - ymin) * (bottom - top)

    body = [text(40, 44, "Accuracy depends on where the answer sits among 20 documents", 25, weight="bold")]
    for a in range(50, 81, 10):
        body.append(f'<line x1="{left}" y1="{py(a):.1f}" x2="{right}" y2="{py(a):.1f}" stroke="{GRID}" stroke-width="1.5"/>')
        body.append(text(left - 14, py(a) + 8, f"{a}%", 22, MUTED, "end"))
    for p in positions:
        body.append(text(px(p), bottom + 32, f"{p}", 22, MUTED, "middle"))
    body.append(text((left + right) / 2, bottom + 66, "Position of the document that holds the answer (1 = first, 20 = last)", 21, MUTED, "middle"))

    body.append(
        f'<line x1="{left}" y1="{py(closed_book):.1f}" x2="{right}" y2="{py(closed_book):.1f}" '
        f'stroke="{ORANGE}" stroke-width="3" stroke-dasharray="10 8"/>'
    )
    pts = " ".join(f"{px(p):.1f},{py(a):.1f}" for p, a in zip(positions, accuracy))
    body.append(f'<polyline points="{pts}" fill="none" stroke="{BLUE}" stroke-width="5"/>')
    for p, a in zip(positions, accuracy):
        body.append(f'<circle cx="{px(p):.1f}" cy="{py(a):.1f}" r="9" fill="{BLUE}"/>')
        dy = -20 if a > closed_book + 2 else 36
        body.append(text(px(p), py(a) + dy, f"{a:.1f}%", 22, BLUE, "middle", "bold"))

    ly = h - 22
    body.append(f'<line x1="40" y1="{ly - 7}" x2="90" y2="{ly - 7}" stroke="{BLUE}" stroke-width="5"/>')
    body.append(text(102, ly, "GPT-3.5-Turbo, given 20 documents", 20))
    body.append(f'<line x1="480" y1="{ly - 7}" x2="530" y2="{ly - 7}" stroke="{ORANGE}" stroke-width="3" stroke-dasharray="10 8"/>')
    body.append(text(542, ly, "same model, given no documents (56.1%)", 20))

    return svg(
        w, h, body,
        "Lost in the middle: accuracy by position of the answer",
        "Line chart. GPT-3.5-Turbo answered questions from 20 documents, one of which held the answer. "
        "Accuracy was 75.8% with the answer first, 57.2% at position 5, 53.8% at position 10, "
        "55.4% at position 15, and 63.2% last. A dashed line at 56.1% shows the same model with no documents. "
        "In the middle positions the model did about as well as, or worse than, having no documents.",
    )


def sepsis_icon_array() -> str:
    """Wong et al. 2021, JAMA Intern Med: external validation of a vendor sepsis model.

    Uses only the two proportions the chapter quotes: the model missed 67% of
    patients with sepsis, and it alerted on 18% of all hospitalizations.
    """
    w, h = 1100, 560
    cell, gap = 34, 6
    body = []

    def grid(x0, y0, filled, fill_color, empty_color, empty_stroke):
        out = []
        for i in range(100):
            r, c = divmod(i, 10)
            x = x0 + c * (cell + gap)
            y = y0 + r * (cell + gap)
            if i < filled:
                out.append(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="6" fill="{fill_color}"/>')
            else:
                out.append(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="6" fill="{empty_color}" stroke="{empty_stroke}" stroke-width="2"/>')
        return out

    gx1, gx2, gy = 70, 600, 110
    body.append(text(gx1, 50, "100 patients who had sepsis", 26, weight="bold"))
    body.append(text(gx1, 84, "33 alerted, 67 missed", 22, MUTED))
    body += grid(gx1, gy, 33, BLUE, "#fbe9e7", RED)
    body.append(text(gx2, 50, "100 admissions of any kind", 26, weight="bold"))
    body.append(text(gx2, 84, "18 set off an alert", 22, MUTED))
    body += grid(gx2, gy, 18, ORANGE, "#f1f3f5", "#c3cad3")

    ly = h - 24
    body.append(f'<rect x="{gx1}" y="{ly - 20}" width="24" height="24" rx="5" fill="{BLUE}"/>')
    body.append(text(gx1 + 34, ly, "alert fired", 21))
    body.append(f'<rect x="{gx1 + 180}" y="{ly - 20}" width="24" height="24" rx="5" fill="#fbe9e7" stroke="{RED}" stroke-width="2"/>')
    body.append(text(gx1 + 214, ly, "sepsis, no alert", 21))
    body.append(f'<rect x="{gx2}" y="{ly - 20}" width="24" height="24" rx="5" fill="{ORANGE}"/>')
    body.append(text(gx2 + 34, ly, "alert fired", 21))
    body.append(f'<rect x="{gx2 + 180}" y="{ly - 20}" width="24" height="24" rx="5" fill="#f1f3f5" stroke="#c3cad3" stroke-width="2"/>')
    body.append(text(gx2 + 214, ly, "no alert", 21))

    return svg(
        w, h, body,
        "A vendor sepsis model tested on 38,455 hospitalizations at one academic center",
        "Two grids of 100 squares. Left: of 100 patients who had sepsis, 33 squares are blue for an alert "
        "and 67 are outlined in red for no alert. Right: of 100 admissions of any kind, 18 squares are orange "
        "for an alert and 82 are grey.",
    )


def embeddings_illustrative() -> str:
    """Hand-placed points showing the idea of an embedding. Not computed."""
    w, h = 1100, 540
    groups = [
        ("Antibiotics", BLUE, [("vancomycin", 250, 170), ("linezolid", 330, 230), ("daptomycin", 205, 260), ("cefazolin", 320, 125)]),
        ("Loop diuretics", ORANGE, [("furosemide", 740, 150), ("bumetanide", 820, 210), ("torsemide", 715, 250)]),
        ("Days of the week", GREEN, [("Tuesday", 560, 370), ("Monday", 460, 405), ("Friday", 640, 420)]),
    ]
    body = [
        f'<rect x="40" y="40" width="1020" height="420" rx="10" fill="#f7f9fb" stroke="{GRID}" stroke-width="2"/>',
        text(1040, 78, "Illustrative: placed by hand, not computed", 20, MUTED, "end"),
    ]
    for _name, color, pts in groups:
        for word, x, y in pts:
            body.append(f'<circle cx="{x}" cy="{y}" r="11" fill="{color}"/>')
            body.append(text(x + 18, y + 8, word, 24, color, weight="bold"))
    lx, ly = 60, h - 30
    for name, color, _pts in groups:
        body.append(f'<circle cx="{lx + 10}" cy="{ly - 8}" r="10" fill="{color}"/>')
        body.append(text(lx + 28, ly, name, 21))
        lx += 90 + 12 * len(name)
    return svg(
        w, h, body,
        "Words used in similar sentences get similar numbers",
        "Illustrative scatter of words placed by hand. Four antibiotics, vancomycin, linezolid, daptomycin and "
        "cefazolin, sit together at upper left. Three loop diuretics sit together at upper right. "
        "Three days of the week sit together at the bottom, far from both drug groups.",
    )


def main() -> None:
    figures = {
        "egfr-bridge.svg": egfr_bridge(),
        "model-loop.svg": model_loop(),
        "lost-in-the-middle-liu-2024.svg": lost_in_the_middle(),
        "sepsis-alert-external-validation.svg": sepsis_icon_array(),
        "embeddings-illustrative.svg": embeddings_illustrative(),
    }
    for name, content in figures.items():
        (OUT / name).write_text(content, encoding="utf-8")
        print(f"wrote images/{name}")


if __name__ == "__main__":
    main()
