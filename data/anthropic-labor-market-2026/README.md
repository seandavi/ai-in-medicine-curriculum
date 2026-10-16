# Anthropic labor-market data, March 2026

Data behind two figures and the occupation lookup in
`chapters/enrichment-workforce-economics.qmd`. Source paper: Maxim Massenkoff
and Peter McCrory, *Labor market impacts of AI: A new measure and early
evidence*, Anthropic, 5 March 2026 (corrected 8 March 2026),
<https://www.anthropic.com/research/labor-market-impacts>. Not peer reviewed.
The authors work for the company whose product the data measure.

## Files

| File | What one row is | Source | Licence |
|---|---|---|---|
| `job_exposure.csv` | One US occupation (O*NET-SOC code, title) and its *observed exposure*, 0 to 1. 756 rows. | Verbatim copy of `labor_market_impacts/job_exposure.csv` from the Anthropic Economic Index dataset, <https://huggingface.co/datasets/Anthropic/EconomicIndex>. Created there 2026-03-05, unchanged since (checked 2026-10-16). SHA-256 `4f0a3adf5feeb2ec5f5d02ab18cc5e851a2a4b8470bde84c0c9335017be12d68`. | CC BY, as stated on the dataset page ("Data released under CC-BY") |
| `figure2-radar-digitized.csv` | One of the 22 job categories in the paper's Figure 2: the *theoretical* share of tasks a language model could do (blue in the original) and the *observed* share (red). | Read off the published 4096 px PNG of Figure 2 by `scripts/digitize_anthropic_radar.py`. | Facts read from a chart; the course's reading |

## What observed exposure means

For each O*NET task the authors ask whether a language model could do it at
least twice as fast (the rating from Eloundou and colleagues, 2023) and
whether it appeared in enough work-related Claude conversations or business
(API) use, sampled in August and November 2025. Automated use counts in full,
assisted use counts half. Task scores are averaged to the job, weighted by
the share of working time each task takes. The authors' appendix says the
score "can be loosely interpreted as the share of a job being performed or
accelerated by an LLM", but is not a pure percentage. A zero means the job's
tasks were not seen often enough in Claude traffic to pass the threshold, not
that AI cannot help with them.

## How good the digitized values are

The geometry was measured from the image once: centre (2043, 2098) px, outer
ring 1.0 at 1360 px, rings every 0.2, linear from zero. Checks:

- The paper's text gives 94% (Computer & math) and 90% (Office & admin) for
  the theoretical series. The script reads 0.943 and 0.898.
- Crops of the image with the readings drawn over them put each marker
  inside its circle (checked for Computer & math, Food & serving, Grounds
  maintenance and Personal care).
- One disagreement: the text says Claude "covers just 33% of all tasks in the
  Computer & Math category", but the red marker on the chart sits at 0.355.
  The CSV keeps the chart reading. The chapter says "about a third".
- Observed values below 0.03 are flagged in the `note` column. There, the
  markers of neighbouring categories overlap at the centre, and the reading
  means only "close to zero".

Precision is about ±0.01 elsewhere.

## Regenerating

```sh
uv run scripts/digitize_anthropic_radar.py > data/anthropic-labor-market-2026/figure2-radar-digitized.csv
python3 scripts/figures_labor_market.py   # writes images/anthropic-2026-*.svg
```
