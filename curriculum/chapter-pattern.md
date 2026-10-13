# Chapter pattern

**Status: shaping decision, 2026-09-06; top and bottom of the chapter and
success first revised 2026-10-12 (issue #89).** The student-facing course is a
Quarto book in the style of [RBiocBook](https://seandavi.github.io/RBiocBook):
self-explaining chapters, one per module. (An LLM chat tutor over the sources
was planned in September and dropped in October 2026; the answer keys remain as
instructor notes.) The talks at <https://talks.seandavis.net> are linked as
resources; they are not ported. This file is the skeleton every chapter follows.

## Shape of a chapter (2026-10-12)

Make the first phone screen useful. Every chapter opens like this:

```markdown
---
title: "...unchanged..."
subtitle: "About 60 minutes"
---

::: {.callout-tip title="In short"}
- **The idea.** One or two plain sentences: the main point, stated as what
  the student can now do well.
- **What you do.** One sentence, starting with the task that works.
- **What you keep.** The thing the student leaves with (a template, a card,
  a prompt, a plan).
- **Short on time?** Which two or three sections to read, and which part of
  the Do to do.
:::

::: {.callout-note title="What you'll learn"}
...objectives...

Course competencies: AIM-6 (talking to patients), AIM-4 (ethics and law).
:::

**What you need.** Your university ChatGPT Edu or Copilot account. Nothing to
install. Made-up patients only.
```

- The subtitle is the honest total only, "About N minutes". No competency
  codes in the subtitle.
- The AIM codes are the last line of the objectives callout, each with its
  name from the preface (`index.qmd`, "In short: AIM-1 foundations; ...").
- The old **Time.** paragraph becomes **What you need.** Keep one sentence of
  time breakdown only if it helps.
- **No `## Summary` at the bottom.** Its best lines go into "In short". The
  chapter ends with "What this changes for you" (the standing question) and
  "Go deeper".
- Valuable optional material goes to Go deeper or into one collapsed callout
  per chapter: `::: {.callout-note collapse="true" title="If you have more
  time: <topic>"}`.
- The chapters are a guide, not assignments (said to students on 2026-10-12).
  A core chapter goes with the Monday talk: read it after the talk, or instead
  of it.

## Success first (2026-10-12)

The course mantra is *it is your job to learn where AI helps your work, and
you learn that by trying*. Students arrive wary of chatbots
(`design-constraints.md`, constraint 5). A student should leave each chapter
having succeeded with the tool and knowing how to check it, not having watched
it fail.

- Every Do opens with a task the student can succeed at, on something they
  care about, and ends with something they keep.
- Checking is part of the routine, not a hunt: "Ask, then check. Most of a
  good answer is right; your job is to find out which parts." ChatGPT Edu
  searches the web, so a step that promises the model will fail may not fail.
  Never write "the model failing is the expected result"; write "it may get
  this right; if so, how would you know?"
- A failure demonstration may stay only after a success, and it is framed as
  learning which parts to trust.
- In "Why this matters" and the closing lines, state what the tool does well
  with the evidence, and do not qualify every success in the next sentence.
  The rules (patient information, check, you sign) stay. The ethicist still
  vetoes harm: do not overstate benefits either.

## Budget

**Core chapters aim for about 60 minutes; menu chapters for 60 to 75**
(revised 2026-10-12; the September budget was 1 to 2 hours). Count honestly:
prose outside Do, Check, and Go deeper at 200 words a minute, plus the time a
first-time student would really need for the Do, plus 5 to 10 minutes for
Check and the standing question. If cutting cannot reach the target, the
subtitle states the true number. Rough split, in reading order:

| Block | Minutes | What |
|---|---|---|
| In short | 1 | The box at the top: the idea, what you do, what you keep, short on time (see *Shape of a chapter*) |
| What you'll learn, What you need | 2 | Objectives, with the competencies as the callout's last line; one line on the account and "made-up patients only" |
| Opening scenario | 3 | A clinical situation an MS4 recognizes, before any term of art is used (see *Opening scenario*) |
| Why this matters | 3 | What this changes in residency by next July, and what the tool does well, with the evidence |
| The idea | 15–20 | Prose with figures and tables |
| Watch or listen | 5–10 | One video or podcast episode, with where to stop (see *Multimedia*) |
| Do | 20–30 | Opens with a task that works, ends with something kept; one student alone can finish it (see *Specialty choice* and *Success first*) |
| Check | 5 | Rubric in the chapter; answer key **not rendered**, held in `_answers/` as instructor notes |
| Standing question | 5 | *What does this change about how you'll practice?* The opening scenario comes back with a better answer |
| Go deeper | Not counted | Papers, talks, blogs, videos; every entry carries the `[VERIFY]` convention from `research/` |

No Summary block at the bottom. In fall 2026 the course director's talks are
the main event in weeks 2 to 4, and each core chapter is their companion.

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

Papers a student finds this way can go in question 5 of that week's learning
journal (`course/learning-journal.qmd`); the Do and the journal share the work
rather than duplicating it. (Until 2026-10-12 this was the resource log.)

## Language

Written for a fourth-year student who has never heard the term and may be reading
in a second language (Elena in `personas.md`). Sentences about 20 words, one idea
each. No em-dashes. Design-document vocabulary (anchor, register, throughline,
artifact, proxy, framing, grounded, surface, mode) is replaced with plain words or
defined in plain words on first use.

**Say what you mean.** Mannered prose substitutes metaphor and flourish for direct
statement: "a dial worth turning" for "a parameter worth varying", "earns its keep"
for "still matters", "load-bearing", "the spine", "lever", "get in the door",
"counterweight", "hand off", "landing cold". The phrases exist to display the writer,
not to convey the idea, and they are imprecise, because a metaphor carries
connotations the writer did not choose. When a literal phrase exists, use it. A
metaphor stays only when it is the chapter's own teaching device and is explained
(the keyboard-suggestion analogy in foundations; the centaur and cyborg names) or
when it is clinical idiom a student uses at work ("rule out", "red flag" for a
warning sign). The three recurring ideas keep their fixed names.

## Rules carried over

- No PHI, ever; everything uses synthetic data.
- Free tiers only; no installs; browser-based tools.
- Each chapter stands alone and tags its `AIM-*` competencies in the
  objectives callout.
- Verification flags (`[VERIFY]`, `[UNVERIFIED]`, `[CONFLICTING]`) travel from
  `research/` into chapters; they are not cleaned up until the claim is checked.

## First chapter

`core-appraisal`. It is the most solo-able module (`delivery-modes.md`, Tier 2), its
Do maps to a search recipe directly, and the model-card exercise from
`research/comparable-courses.md` fits its Check block.
