# /// script
# requires-python = ">=3.11"
# dependencies = ["pillow", "numpy"]
# ///
"""Read the values off Figure 2 of Massenkoff and McCrory (2026), a radar chart.

The paper ("Labor market impacts of AI: A new measure and early evidence",
Anthropic, 5 March 2026) publishes its occupation-level data but not the
22 job-category values behind Figure 2. This script recovers them from the
published 4096 x 4096 px image, so the workforce chapter can redraw the
figure instead of copying it.

Geometry, measured once from the image: the centre is at (2043, 2098); the
outer ring is 1.0 at a radius of 1360 px; rings fall every 272 px (0.2), so
the scale is linear from zero at the centre. Each marker is found as a solid
blob of its series colour lying on its spoke; a filter that keeps only
pixels inside a solid 9 x 9 block drops the 2 px polygon edges.

Check: the text of the paper gives 0.94 for Computer & math and 0.90 for
Office & admin (theoretical). This script reads 0.943 and 0.898.

Run from the repository root:

    uv run scripts/digitize_anthropic_radar.py > data/anthropic-labor-market-2026/figure2-radar-digitized.csv
"""

from __future__ import annotations

import csv
import io
import math
import sys
import urllib.request

import numpy as np
from PIL import Image

FIGURE_URL = (
    "https://cdn.sanity.io/images/4zrzovbb/website/"
    "c1952c81bca02a7c8cc05ef7801e67ca60831c55-4096x4096.png"
)
CX, CY, R1 = 2043.0, 2098.0, 1360.0

# Clockwise from the top, as in the published figure.
CATEGORIES: list[tuple[str, str]] = [
    ("11", "Management"),
    ("13", "Business & finance"),
    ("15", "Computer & math"),
    ("17", "Architecture & engineering"),
    ("19", "Life & social sciences"),
    ("21", "Social services"),
    ("23", "Legal"),
    ("25", "Education & library"),
    ("27", "Arts & media"),
    ("29", "Healthcare practitioners"),
    ("31", "Healthcare support"),
    ("33", "Protective service"),
    ("35", "Food & serving"),
    ("37", "Grounds maintenance"),
    ("39", "Personal care"),
    ("41", "Sales"),
    ("43", "Office & admin"),
    ("45", "Agriculture"),
    ("47", "Construction"),
    ("49", "Installation & repair"),
    ("51", "Production"),
    ("53", "Transportation"),
]

# Below this, markers from neighbouring spokes overlap at the centre and the
# reading is only good to "close to zero".
NEAR_CENTRE = 0.03


def solid(mask: np.ndarray, k: int = 9) -> np.ndarray:
    """Keep pixels whose k x k neighbourhood is at least 85% mask."""
    c = np.pad(mask.astype(np.int32), ((1, 0), (1, 0))).cumsum(0).cumsum(1)
    s = c[k:, k:] - c[:-k, k:] - c[k:, :-k] + c[:-k, :-k]
    out = np.zeros_like(mask)
    h = k // 2
    out[h : h + s.shape[0], h : h + s.shape[1]] = s >= 0.85 * k * k
    return out


def read_spoke(mask: np.ndarray, dx: np.ndarray, dy: np.ndarray, theta: float) -> float:
    """Radius of the outermost marker blob on one spoke, as a fraction of 1.0."""
    t = math.radians(theta)
    along = dx * math.cos(t) + dy * math.sin(t)
    perp = np.abs(-dx * math.sin(t) + dy * math.cos(t))
    a = np.sort(along[mask & (perp < 6) & (along > 0)])
    if a.size == 0:
        return float("nan")
    gaps = np.nonzero(np.diff(a) > 4)[0]
    run = a[a >= (a[gaps[-1] + 1] if gaps.size else a[0])]
    return float((run.min() + run.max()) / 2 / R1)


def main() -> None:
    with urllib.request.urlopen(FIGURE_URL) as resp:
        im = np.asarray(Image.open(io.BytesIO(resp.read())).convert("RGB")).astype(int)
    r, g, b = im[..., 0], im[..., 1], im[..., 2]
    blue = solid((b > 170) & (r < 110) & (g > 90) & (g < 175))
    red = solid((r > 180) & (g < 110) & (b < 110))
    ys, xs = np.indices(r.shape)
    dx, dy = xs - CX, CY - ys

    out = csv.writer(sys.stdout, lineterminator="\n")
    out.writerow(["soc_major", "category", "theoretical", "observed", "note"])
    step = 360 / len(CATEGORIES)
    for k, (soc, name) in enumerate(CATEGORIES):
        theta = 90 - k * step
        theo = read_spoke(blue, dx, dy, theta)
        obs = read_spoke(red, dx, dy, theta)
        note = "close to zero; markers overlap at the centre" if obs < NEAR_CENTRE else ""
        out.writerow([soc, name, f"{theo:.3f}", f"{obs:.3f}", note])


if __name__ == "__main__":
    main()
