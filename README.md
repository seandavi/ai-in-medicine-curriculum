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

The research files flag uncertain claims with **`[VERIFY]`**, **`[CONFLICTING]`**,
or **`[UNVERIFIED]`**. Those flags are load-bearing and were carried forward into
the modules deliberately. Re-check flagged figures against primary sources before
they go on a slide — the fast-moving ones are payer litigation status, FDA
guidance status, NRMP and BLS figures, and the Lancet colonoscopy deskilling
numbers.

Two topics in `research/enrichment-activities.md` are marked **NOT RESEARCHED**
rather than filled in from memory: patient consent/transparency requirements, and
the EU AI Act. Fill those before running `core-ethics-regulation`.
