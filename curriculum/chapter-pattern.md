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
| Opening scenario | 5 | A clinical situation an MS4 recognizes, before any term of art is used — see *Opening scenario* |
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

## Opening scenario

Every chapter starts with a clinical or medically grounded scenario, not with
the chapter's topic. The scenario is the problem; the chapter's vocabulary is
introduced only once the reader already has the problem in hand. A vendor at
lunch selling an ambient scribe is the right kind of opening; "critical
appraisal is the skill of..." is not. Test: a student who has never heard the
chapter's key term should be able to read the first two paragraphs and know
what is at stake.

The scenario returns at the end of the chapter. The Standing question, or the
last paragraph before it, should put the reader back in the same room with a
better answer.

Review every chapter against `personas.md`: the avoider first, then the other
two students, then the faculty readers, the ethicist last.

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

## Visuals

A chapter should look like a book chapter, not a handout. Aim for one visual per
major section, each doing a job the prose cannot. Five kinds have earned a place;
use them in roughly this order of preference.

1. **The artifact under appraisal, drawn.** A vendor slide, a chatbot answer, a
   model card, an EHR alert, built in CSS or as a styled block and labeled
   *illustrative*. It is the thing the student is being asked to judge, it can
   be exactly as misleading as the lesson needs, and nobody owns it.
2. **Redrawn data.** Data are not copyrightable. A figure from a paper, rebuilt
   from the paper's own numbers with a citation, is always clean and usually
   clearer than the original. Prefer this over copying a panel.
3. **Open-access figures.** Where a paper is CC BY (most of *JAMA Network
   Open*, *BMJ Open*, *npj Digital Medicine*, *Nature Medicine* open-access
   articles), reuse the figure with credit. Check the article's license line,
   not the journal's reputation; the same journal publishes under several.
   CC BY-NC and CC BY-SA carry conditions; note them in the caption.
4. **Press clippings.** Quote the headline, name the outlet, link the piece,
   style it as a clipping. Never a screenshot. Three headlines about one paper
   is a better lesson in evidence tiers than any diagram.
5. **Photos and comics.** Wikimedia Commons and Openverse for CC or public
   domain photos; xkcd for humor (CC BY-NC 2.5, so note the non-commercial
   condition). A comic that assumes the reader already knows the field fails
   the avoider; pick ones that land cold.

**Fair use is a defense, not a permission.** Nonprofit teaching with commentary
and attribution is the strongest fact pattern there is, and a publicly hosted
book is weaker than a classroom handout. Reserve it for a figure that cannot be
redrawn and is essential, and say in the caption that it is reproduced under
fair use for commentary.

Mechanics:

- Files live in `images/`, named for what they show, sized for the page
  (about 900 px wide for photos; comics displayed at 420 px via `.comic`).
- Every image has a `fig-alt` for screen readers and a caption that carries the
  credit: creator, license with link, source with link. The caption is the
  attribution; there is no separate credits page.
- Styled components (`.vendor-slide`, `.press-clips`) are in `styles.css`.
  Reuse them rather than styling per chapter.
- A figure that is only decoration is cut. The test: cover the caption and ask
  what a student learns from the image alone. If the answer is "nothing", it
  goes.

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

Papers a student finds this way count toward that week's resource log, and the
Do says so with a link to `course/resource-log.qmd`; the two assignments share
the work rather than duplicating it.

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
