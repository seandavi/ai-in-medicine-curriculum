# AI in Medicine — Curriculum

A modular, competency-based four-week elective on AI in medicine for fourth-year
medical students. ~40 students, Zoom-only, ungraded. Successor to IDPT 8079.

## Start here

1. **`curriculum/competencies.md`** — nine competency domains (`AIM-1`…`AIM-9`
   plus cross-cutting `AIM-X`), six core and three extension, each with a stable
   ID so the whole thing can be remapped when the AAMC competencies land in fall
   2026.
2. **`curriculum/schedule.md`** — the module catalog and the default four-week
   assembly, plus variants for a one-session-per-week or hands-on-heavy cohort.
3. **`curriculum/design-constraints.md`** — the fixed facts and what each one
   forces. Check any new module against this.
4. **`curriculum/chapter-pattern.md`** — the skeleton every student-facing
   chapter follows: 1–2 h budget, one video or podcast, specialty-choice literature.
5. **`CONTEXT.md`** — who directs and teaches the course, the guest-lecturer
   roster, evaluation and CQI mechanics, registration quirks, and the open
   decision about the student-facing tool. The design files are deliberately
   name-free and date-free so they travel; `CONTEXT.md` is where the CU
   Anschutz specifics live.

## Layout

| Path | What's in it |
|---|---|
| `curriculum/` | Competency framework, module catalog, design constraints, and `delivery-modes.md` — an untested idea about which sessions need live Zoom and what a chat-based async path would look like |
| `modules/` | One self-contained file per module — session plan, activities, rubrics |
| `chapters/`, `index.qmd`, `_quarto.yml` | The student-facing Quarto book; one chapter per module following `curriculum/chapter-pattern.md`. `_answers/` holds answer keys that are never rendered |
| `research/` | The background research the design rests on, with citations; `comparable-courses.md` reviews external courses for what to borrow |

Modules are independent by design. Each tags its competencies, assumes no prior
module, and can be reordered or dropped without breaking the rest — because in a
four-week ungraded elective, students *will* miss sessions.

## Building the book

```
uv tool install git+https://github.com/seandavi/quartobot   # once
quarto render                                                 # → _book/
```

Cite with persistent-identifier keys — `@pmid:40206627`, `@doi:10.1126/science.aax2342` —
and the pre-render hook resolves them into `references.resolved.bib`. To verify every
key against PubMed and Crossref without rendering:

```
quartobot resolve --from-scan . --id-mode citation-key
```

Hand-curated entries (talks, videos, reports without a DOI) go in `references.bib`.

## Deploying

Published at <https://ai-in-medicine.seandavi.workers.dev> as a Cloudflare Workers
static-assets site, the same pattern as the talks repo. Every push to `main` renders
and deploys via `.github/workflows/deploy.yml`. To deploy by hand:

```
export CLOUDFLARE_API_TOKEN="$(gcloud secrets versions access latest --secret cdsci-cloudflare-workers-token --project cdsci-infra)"
export CLOUDFLARE_ACCOUNT_ID="$(gcloud secrets versions access latest --secret cdsci-r2-account-id --project cdsci-infra)"
quarto render && npm run deploy
```

The two GitHub repository secrets the workflow uses are copies of those same two
Google Secret Manager entries.

## Working on another machine

This repo assumes the [`seandavi/talks`](https://github.com/seandavi/talks) repo is
checked out **as a sibling directory** (`../talks`). Roughly 45 references across
`research/` and `modules/` point into it, and `research/talks-inventory.md` still
carries absolute paths from the machine it was written on. Clone both under the same
parent and the relative paths resolve:

```
git clone git@github.com:seandavi/ai-in-medicine-curriculum.git
git clone git@github.com:seandavi/talks.git
```

Where a module cites reusable material, it also gives the published URL under
`https://talks.seandavis.net/` — archive slugs are immutable, so those links are safe
to follow (and safe to hard-code in a syllabus) even without the sibling checkout.

## Source material

Existing talk materials live in the sibling [seandavi/talks](https://github.com/seandavi/talks)
repo (`../talks`), published at <https://talks.seandavis.net>. See
`research/talks-inventory.md` for what's reusable and
`research/talks-drive-decks.md` for content recovered from Drive-only decks —
including the `ai-safety` deck, which turned out to be the best-fitting material
in the whole portfolio and was invisible from its stub description.

## Before you teach from this

The research files flag uncertain claims — `[VERIFY]`, `[CONFLICTING]`, and
`[UNVERIFIED]` in most files, inline ⚠ marks in
`research/enrichment-activities.md`. Those flags are load-bearing and were carried
forward into the modules deliberately. `research/enrichment-activities.md` ends
with a consolidated re-verification list triaged by how badly a mistake would
hurt; **read it before building slides.**

The claims most likely to be stale or wrong by the time you teach:

- **Regulatory status**, which moved twice during this research. The FDA Clinical
  Decision Support guidance students may know from 2022 was replaced in January
  2026, and the EU AI Act's high-risk deadline was deferred via the Digital
  Omnibus. Both need a fresh check.
- **Payer litigation** (Lokken, Kisting-Leung, Humana) — active dockets.
- **NRMP Match and BLS employment figures** — secondary-sourced.
- **The Lancet colonoscopy deskilling numbers** (28.4% → 22.4% adenoma detection)
  — the most quotable statistic in that literature, and the primary abstract was
  paywall-blocked.

Known genuine gaps, still unfilled: ACGME and LCME AI expectations, the status of
the NAM AI Code of Conduct, and any 2024–2026 patient-facing clinical chatbot
safety incident (the 2023 NEDA "Tessa" case remains the canonical example).
