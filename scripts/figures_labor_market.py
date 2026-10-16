"""Draw the two labor-market figures in the workforce chapter from committed data.

Reads data/anthropic-labor-market-2026/ and writes two SVGs to images/:

- anthropic-2026-could-vs-does.svg: Figure 2 of Massenkoff and McCrory
  (2026) redrawn as a radar chart. What a language model could speed up in
  each of 22 job categories, against what people were seen using Claude for
  at work. Values come from figure2-radar-digitized.csv, which
  scripts/digitize_anthropic_radar.py reads off the published image.
- anthropic-2026-health-jobs.svg: observed exposure for selected health
  occupations, from job_exposure.csv, the occupation-level data Anthropic
  released with the paper (CC BY).

Standard library only, so the slide decks can reuse it. Run from the
repository root:

    python3 scripts/figures_labor_market.py
"""

from __future__ import annotations

import csv
import math
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "anthropic-labor-market-2026"
IMAGES = ROOT / "images"

FONT = "Segoe UI, Helvetica, Arial, sans-serif"
INK, MUTED, GRID, SURFACE = "#1f2933", "#5f6b7a", "#dfe3e8", "#ffffff"
COULD, SEEN = "#1f5fa8", "#b3261e"  # passes the dataviz CVD and contrast checks

HEALTH = {"Healthcare practitioners", "Healthcare support"}


def pct(v: float) -> str:
    return f"{round(v * 100)}%"


def radar() -> str:
    rows = list(csv.DictReader((DATA / "figure2-radar-digitized.csv").open()))
    n = len(rows)
    W, H, cx, cy, R = 820, 760, 410, 410, 230
    step = 2 * math.pi / n

    def xy(i: int, v: float) -> tuple[float, float]:
        a = math.pi / 2 - i * step  # clockwise from the top, as in the original
        return cx + v * R * math.cos(a), cy - v * R * math.sin(a)

    out: list[str] = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
        f'font-family="{FONT}" font-size="15">',
        "<title>Could do versus does: share of tasks a language model could speed up, and share "
        "seen in Claude work use, for 22 job categories</title>",
        "<!-- Redrawn from Massenkoff and McCrory, 'Labor market impacts of AI', Anthropic, "
        "March 2026, Figure 2. Values read from the published chart by "
        "scripts/digitize_anthropic_radar.py. Data are not copyrightable; drawing by the course. -->",
        f'<rect width="{W}" height="{H}" fill="{SURFACE}"/>',
        f'<text x="24" y="32" font-size="20" font-weight="600" fill="{INK}">'
        "Could do versus does, by job category</text>",
    ]
    # legend: line-key plus marker shape, so identity is never colour alone
    ly = 62
    out += [
        f'<line x1="24" y1="{ly}" x2="52" y2="{ly}" stroke="{COULD}" stroke-width="2"/>',
        f'<circle cx="38" cy="{ly}" r="4.5" fill="{COULD}" stroke="{SURFACE}" stroke-width="2"/>',
        f'<text x="60" y="{ly + 5}" fill="{INK}"><tspan font-weight="600">Could:</tspan> '
        "share of tasks a language model could do at least twice as fast</text>",
        f'<line x1="24" y1="{ly + 26}" x2="52" y2="{ly + 26}" stroke="{SEEN}" stroke-width="2"/>',
        f'<rect x="33.5" y="{ly + 21.5}" width="9" height="9" fill="{SEEN}" stroke="{SURFACE}" stroke-width="1.5"/>',
        f'<text x="60" y="{ly + 31}" fill="{INK}"><tspan font-weight="600">Seen:</tspan> '
        "share seen in work use of Claude, August and November 2025</text>",
    ]
    # rings and spokes: hairline, recessive
    for k in range(1, 6):
        out.append(
            f'<circle cx="{cx}" cy="{cy}" r="{R * k / 5:.1f}" fill="none" stroke="{GRID}" stroke-width="1"/>'
        )
    for i, r in enumerate(rows):
        x, y = xy(i, 1.0)
        spoke = "#9aa5b1" if r["category"] in HEALTH else GRID  # the two health spokes a step darker
        out.append(f'<line x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}" stroke="{spoke}" stroke-width="1"/>')
    # ring labels on the gap between the last spoke and the first
    a = math.pi / 2 + step / 2
    for k in range(1, 6):
        x, y = cx + R * k / 5 * math.cos(a), cy - R * k / 5 * math.sin(a)
        out.append(
            f'<text x="{x - 3:.1f}" y="{y - 3:.1f}" font-size="13" fill="{MUTED}" text-anchor="end">{k * 20}%</text>'
        )

    def poly(key: str, colour: str, fill_opacity: float) -> str:
        pts = " ".join(f"{x:.1f},{y:.1f}" for x, y in (xy(i, float(r[key])) for i, r in enumerate(rows)))
        return (
            f'<polygon points="{pts}" fill="{colour}" fill-opacity="{fill_opacity}" '
            f'stroke="{colour}" stroke-width="2" stroke-linejoin="round"/>'
        )

    out += [poly("theoretical", COULD, 0.10), poly("observed", SEEN, 0.20)]
    for i, r in enumerate(rows):
        x, y = xy(i, float(r["theoretical"]))
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.5" fill="{COULD}" stroke="{SURFACE}" stroke-width="2"/>')
    for i, r in enumerate(rows):
        x, y = xy(i, float(r["observed"]))
        out.append(
            f'<rect x="{x - 4.5:.1f}" y="{y - 4.5:.1f}" width="9" height="9" fill="{SEEN}" '
            f'stroke="{SURFACE}" stroke-width="1.5"/>'
        )
    # category labels; the two health categories carry their values
    for i, r in enumerate(rows):
        a = math.pi / 2 - i * step
        c, s = math.cos(a), math.sin(a)
        x, y = cx + (R + 14) * c, cy - (R + 14) * s
        anchor = "start" if c > 0.2 else "end" if c < -0.2 else "middle"
        y += 4 if abs(s) < 0.9 else (-6 if s > 0 else 14)
        name = escape(r["category"])
        if r["category"] in HEALTH:
            out.append(
                f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-weight="600" fill="{INK}">{name}'
                f'<tspan x="{x:.1f}" dy="18" font-weight="400" fill="{INK}">could {pct(float(r["theoretical"]))}'
                f" · seen {pct(float(r['observed']))}</tspan></text>"
            )
        else:
            out.append(f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" fill="{MUTED}">{name}</text>')
    out.append(
        f'<text x="24" y="{H - 16}" font-size="13" fill="{MUTED}">Redrawn from Massenkoff and McCrory '
        "(Anthropic, March 2026), Figure 2.</text>"
    )
    out.append("</svg>")
    return "\n".join(out) + "\n"


# (SOC code, label shown, group); values come from job_exposure.csv
HEALTH_ROWS: list[tuple[str, str, str]] = [
    ("15-1251", "Computer programmers, the highest of all 756 jobs", "Comparison"),
    ("29-2072", "Medical records specialists", "Records and office work"),
    ("31-9094", "Medical transcriptionists", "Records and office work"),
    ("43-6013", "Medical secretaries and administrative assistants", "Records and office work"),
    ("29-9021", "Health information technologists and registrars", "Records and office work"),
    ("29-1224", "Radiologists", "Clinicians"),
    ("29-1222", "Pathologists", "Clinicians"),
    ("29-1171", "Nurse practitioners", "Clinicians"),
    ("29-1051", "Pharmacists", "Clinicians"),
    ("29-1216", "General internal medicine physicians", "Clinicians"),
    ("29-1141", "Registered nurses", "Clinicians"),
    ("29-1215", "Family medicine physicians", "Clinicians"),
    ("29-1223", "Psychiatrists", "Clinicians"),
]


def bar(x0: float, y: float, w: float, h: float, colour: str) -> str:
    """Horizontal bar: square at the baseline, 4 px rounded data end."""
    if w < 1:
        return ""
    rr = min(4.0, w / 2)
    return (
        f'<path d="M{x0:.1f},{y:.1f} h{w - rr:.1f} a{rr},{rr} 0 0 1 {rr},{rr} v{h - 2 * rr:.1f} '
        f'a{rr},{rr} 0 0 1 -{rr},{rr} h-{w - rr:.1f} z" fill="{colour}"/>'
    )


def health_jobs() -> str:
    exposure = {
        r["occ_code"]: float(r["observed_exposure"])
        for r in csv.DictReader((DATA / "job_exposure.csv").open())
    }
    W, x0, scale, row_h, bar_h = 810, 410, 450, 26, 16  # scale: px for 100%
    top = 100
    body: list[str] = []
    y, group = top, ""
    for soc, label, g in HEALTH_ROWS:
        if g != group:
            group = g
            y += 8
            body.append(f'<text x="24" y="{y + 14}" font-weight="600" fill="{INK}">{escape(g)}</text>')
            y += row_h
        v = exposure[soc]
        colour = MUTED if g == "Comparison" else SEEN
        w = v * scale
        body.append(f'<text x="{x0 - 10}" y="{y + 14}" text-anchor="end" fill="{INK}">{escape(label)}</text>')
        body.append(bar(x0, y + 1, w, bar_h, colour))
        body.append(f'<text x="{x0 + w + 6:.1f}" y="{y + 14}" fill="{INK}" font-weight="600">{pct(v)}</text>')
        y += row_h
    axis_y = y + 6
    H = axis_y + 58
    grid = []
    for t in range(0, 81, 20):
        gx = x0 + t / 100 * scale
        grid.append(f'<line x1="{gx:.1f}" y1="{top}" x2="{gx:.1f}" y2="{axis_y}" stroke="{GRID}" stroke-width="1"/>')
        grid.append(
            f'<text x="{gx:.1f}" y="{axis_y + 16}" font-size="13" text-anchor="middle" fill="{MUTED}">{t}%</text>'
        )
    head = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
        f'font-family="{FONT}" font-size="15">',
        "<title>Observed exposure for selected health occupations, Anthropic data released "
        "March 2026</title>",
        "<!-- Data: Anthropic Economic Index, labor_market_impacts/job_exposure.csv "
        "(Massenkoff and McCrory 2026), CC BY. Drawing by the course. -->",
        f'<rect width="{W}" height="{H}" fill="{SURFACE}"/>',
        f'<text x="24" y="32" font-size="20" font-weight="600" fill="{INK}">'
        "How much of each job people were seen doing with Claude at work</text>",
        f'<text x="24" y="58" font-size="14" fill="{MUTED}">Observed exposure: share of the job\'s working time spent on '
        "tasks seen in Claude work use.</text>",
        f'<text x="24" y="78" font-size="14" fill="{MUTED}">Automated use counts in full, assisted use half. '
        "0% means too little use was seen to count.</text>",
    ]
    foot = [
        f'<text x="24" y="{H - 14}" font-size="13" fill="{MUTED}">Data: Anthropic Economic Index, '
        "job_exposure.csv (March 2026), CC BY.</text>",
        "</svg>",
    ]
    return "\n".join(head + grid + body + foot) + "\n"


def main() -> None:
    (IMAGES / "anthropic-2026-could-vs-does.svg").write_text(radar())
    (IMAGES / "anthropic-2026-health-jobs.svg").write_text(health_jobs())


if __name__ == "__main__":
    main()
