# Chapter plan

**Status: 2026-09-07.** One chapter exists (`core-appraisal`). Ten modules remain.
This is the order, the per-chapter contract, and the two passes that follow. Each
item is a GitHub issue labelled `chapter` or `pass`; tracking issue #14 links them.

## Order

Default-assembly order first, so the eight-session course is complete before the
two spare enrichment chapters.

| # | Chapter | Min | AIM | Scenario seed (from the module) |
|---|---|---|---|---|
| 1 | `core-foundations` | 75 | 1, 2 | The eGFR on this morning's BMP is a model; you already trust one |
| 2 | `core-centaur-cyborg` | 90 | 5, X, 4 | Your first intern task list; which lines go to the machine |
| 3 | `core-bias-equity` | 90 | 3 | A pulse-ox reading on a patient with dark skin that does not match the gas |
| 4 | `enrichment-agentic-coding` | 75 | 5, 2, 4 | The resident who built a spreadsheet tool the whole team now uses |
| 5 | `core-patient-communication` | 90 | 6, 4 | A patient brings a chatbot diagnosis to clinic, or asks if AI wrote the note |
| 6 | `enrichment-workforce-economics` | 90 | 3, 7 | Matching into radiology the year everyone says radiology is over |
| 7 | `enrichment-environment` | 60 | 3, X | The water-per-query number everyone quotes and nobody has checked |
| 8 | `core-ethics-regulation` | 75 | 4, 7, X | A scribe error in a note you signed; who answers for it |
| 9 | `enrichment-prompting-lab` | 75 | 5, 2 | Same question, two prompts, one better-organised wrong answer |
| 10 | `enrichment-rag-notebooklm` | 60 | 1, 9 | Journal-club prep with a source-grounded tool |

## Per-chapter contract

Every chapter issue carries the same checklist. In short:

- Read `chapter-pattern.md`, `personas.md`, `design-constraints.md`, the module
  file, and `chapters/core-appraisal.qmd` as the exemplar, before writing.
- Follow the block structure and budget. Opening scenario before any jargon.
- Every citation is a `@pmid:` or `@doi:` key, verified with the PubMed tooling
  before it goes in. Unverifiable claims stay flagged `[VERIFY: …]{.verify}`.
- Visuals per the pattern's Visuals section; at least the artifact under
  appraisal, drawn, and one redrawn or CC BY figure where the module has data.
- Answer key in `_answers/<chapter>.md`; never rendered.
- Self-review as all six personas before the PR; record it in `reviews/`.
- Add a row to `AI-LEDGER.md`. Add the chapter to `_quarto.yml`.
- One branch per chapter, PR to `main`. Merge deploys.

## Passes

**Review pass** (after all ten merge). Six-persona review of every chapter,
Elena first, Lindqvist last, findings filed as one issue per chapter, fixed, and
recorded in `reviews/`. Also re-runs the appraisal chapter, which will have
drifted relative to its siblings.

**Cross-reference pass** (after the review pass). Chapters are written
independently and will overlap and contradict. This pass makes them a book: every
"the X chapter" mention becomes a link; throughlines named consistently; shared
terms defined the same way; duplicated material (retrieval mechanism in appraisal
and RAG; regulation in appraisal and ethics; register in appraisal and prompting)
resolved by cross-reference rather than repetition; multimedia not repeated; Go
deeper deduplicated; AIM coverage table checked against `competencies.md`; the
preface updated; all `[VERIFY]` flags inventoried into one issue.

## After the passes

Update `appendix/about.qmd` for whatever the process turned out to be, and the
ledger for all of it.
