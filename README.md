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

## Layout

| Path | What's in it |
|---|---|
| `curriculum/` | Competency framework, module catalog, design constraints |
| `modules/` | One self-contained file per module — session plan, activities, rubrics |
| `research/` | The background research the design rests on, with citations |

Modules are independent by design. Each tags its competencies, assumes no prior
module, and can be reordered or dropped without breaking the rest — because in a
four-week ungraded elective, students *will* miss sessions.

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
