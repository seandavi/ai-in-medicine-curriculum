# Chapter pattern

**Status: shaping decision, 2026-09-06.** The student-facing course is a Quarto book
in the style of [RBiocBook](https://seandavi.github.io/RBiocBook): self-explaining
chapters, one per module, with an LLM chat over the sources as tutor and async path.
The talks at <https://talks.seandavis.net> are linked as resources and used in the
live demo block; they are not ported. This file is the skeleton every chapter follows.

## Budget

**1–2 hours per chapter**, self-paced. Rough split:

| Block | Minutes | What |
|---|---|---|
| Why this matters | 5 | Two paragraphs: what this changes in residency in three months |
| The idea | 20–30 | Prose with figures and tables; replaces the didactic block of the live session |
| Watch or listen | 15–30 | One video or podcast episode — see *Multimedia* |
| Do | 30–45 | The module's activity, written so one student alone can finish it — see *Specialty choice* |
| Check | 5–10 | Rubric in the chapter; answer key **not rendered**, held in `_answers/` for the tutor only |
| Standing question | 5 | *What does this change about how you'll practice?* Written, not optional |
| Go deeper | — | Papers, talks, blogs, videos; every entry carries the `[VERIFY]` convention from `research/` |

The live session then runs the same Do with breakouts and the cross-group comparison;
the chapter is the pre-work and the make-up path. Six chapters at the low end of the
budget is ~8 h of self-study across four weeks, on top of the weekly resource log.

## Multimedia

Every chapter includes at least one video or podcast, chosen to the same verification
standard as a citation: real episode, stable URL, length stated, and a one-line note
on what to listen for. Prefer sources that will still exist in three years.

Candidate feeds to draw from — each entry must be confirmed before it goes in a chapter:

- *NEJM AI Grand Rounds* (podcast; Manrai and Beam) — appraisal, deployment, regulation
- *JAMA Clinical Reviews* and *JAMA Network* video interviews — clinical-evidence chapters
- 3Blue1Brown, *But what is a GPT?* — foundations chapter, the one visual explanation worth the time
- Karpathy, *Intro to Large Language Models* (2023, ~1 h) — foundations, for the students who want more
- Your own decks at `talks.seandavis.net/<slug>/` — link the archive slug; they are immutable

If no good episode exists for a chapter, say so in the chapter rather than padding.

## Specialty choice

Wherever the Do engages with literature, students pick their own specialty. Two
mechanisms, in order of preference:

1. **A search recipe.** A PubMed query pattern with the specialty as the variable —
   e.g. `("large language model" OR "artificial intelligence") AND <specialty> AND
   (validation OR "external validation")` with a date filter — plus two sentences on
   how to pick one paper from the results. Scales to any specialty and never goes stale.
2. **A pre-vetted set.** One verified paper each across roughly six specialties
   (radiology, oncology, emergency medicine, primary care, psychiatry, surgery is a
   reasonable default spread) for chapters whose Do needs a *specific* property — a
   known-flawed validation, a retracted claim, a proxy failure. Verify with the PubMed
   tooling before listing; a fabricated citation in an appraisal chapter is
   disqualifying.

Papers a student finds this way count toward that week's resource log — the two
assignments share the work rather than duplicating it.

## Rules carried over

- No PHI, ever; everything uses synthetic data.
- Free tiers only; no installs; browser-based tools.
- Each chapter stands alone and tags its `AIM-*` competencies.
- Verification flags (`[VERIFY]`, `[UNVERIFIED]`, `[CONFLICTING]`) travel from
  `research/` into chapters; they are not cleaned up until the claim is checked.

## First chapter

`core-appraisal`. It is the most solo-able module (`delivery-modes.md`, Tier 2), its
Do maps to a search recipe directly, and the model-card exercise from
`research/comparable-courses.md` fits its Check block.
