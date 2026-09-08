# Review: core-patient-communication chapter, 2026-09-08

Six-persona review of `chapters/core-patient-communication.qmd` per
`curriculum/personas.md`, run after the plain-language pass on the same
branch (`pass/core-patient-communication`). Filed as GitHub issue #35.
Findings are ordered by reviewer; each says whether it was fixed in this pass
or left open for the author.

## The plain-language pass (context for the review)

Terms replaced or defined: anchors, competency framework (defined on first
use), scoping review, clinical encounter, blinded raters (defined), replication,
mechanism, spine (named and defined), confounds, hold loosely, task load,
randomized rollout, converging, decline/declinable, deployment,
disclose/disclosure (kept only in the statute sentence), retention terms,
fabricated-reference rate, property of the writing, "the move", observer
rubric (now "observer's checklist", pointed at the Check section), workflow,
canonical, failure mode, lay-press, deskilling (defined), persona, triads and
rotations, taxonomy, frame, mediation, capitulating and condescending, hedging,
informed, empathy paradox (now named in the prose before the Check uses it).
About forty sentences split. No numbers, citation keys, VERIFY spans, figure
ids, alt text, block classes, or section order changed. Answer-key wording
aligned where the rubric's words changed.

## Elena (avoider, surgery, free tier, ESL) — reads first

Passes, with three fixes applied.

1. **"Blinded raters" was never tied to the plain phrase.** The prose said
   "raters who were not told which was which" but the caption and summary use
   the word "blinded" bare. *Fixed*: "so-called blinded raters" on first use.
2. **"Card 5 of the live session"** referred to a card she has not seen.
   *Fixed*: "one of the live session's scenario cards".
3. **"The seventh question the appraisal chapter said no vendor slide
   answers"** needed the other chapter. *Fixed*: one sentence of context so it
   stands alone.
4. Ten-minute way in (Part A, no tool, no account), the prompt-fluency
   sentence, and three places where skepticism is the right answer are all
   present. Both images land cold. No comic.

## Marcus (early adopter, radiology)

Passes. The clinician-versus-patient fabrication jump, the authorship-label
effect, and the Winters complaint are not things he would get by asking the
model. The mammogram CAD script and the image-read table row put him in the
room. The spine is the thing to do tomorrow. Nothing to fix.

## Priya (clinician-in-waiting, emergency medicine)

Passes. The decline table, the scribe callout (write the refusal in the note,
log consent where the institution does), the attending who sent a draft
unread, and Part C for the sepsis alert she silenced. Her co-intern sentence
is the tip callout's title. Nothing to fix.

## Jordan (instructional designer)

Passes, with two notes left open.

1. **Objective 5 has no Do activity**; it is assessed by the Check row only.
   Carried over from the 2026-09-07 review. *Open*: a written task would push
   the time budget; author's call.
2. **The desk photo (`fig-desk`) is decoration** by the chapter-pattern test:
   cover the caption and the image alone teaches nothing. *Open*: keep as
   scene-setting or cut; author's call.
3. Time estimate is still honest (same length, shorter sentences). The
   scenario returns in the standing question. Both images carry `fig-alt`.
   The Check is self-applicable.

## Dr. Okafor (borrowing educator)

Passes, with one fix applied.

1. **The 21 percent figure** (Tolentino et al. 2024, pmid:39023999) was
   carried from `research/` with a "confirm against the table" note.
   Re-checked against the PMC full text (PMC11294785): "communication of AI
   results to patients (4/19, 21%)". The denominator is the 19 papers that
   describe programs, not the 30 programs. *Fixed*: chapter and summary now
   say about one in five of the papers describing them; the answer-key
   source row records the check and closes the note.
2. The mechanism paragraph is restatable, Part B is pasteable, the
   institution-specific parts are marked, and every image can be reused.

## Dr. Lindqvist (clinical ethicist) — reads last

Passes, with one fix applied.

1. **The spine's second sentence could be said without knowing it is true.**
   "Dr. Chen read the whole study herself" is the same comforting-lie pattern
   the scribe section warns against, if the student says it from habit rather
   than from the report. *Fixed*: two sentences after the spine callout: say
   it only when you know it; the signed report tells you who read the study.
2. PHI warning covers the chatbot, the transcript, and the student's own
   notes. The patient knows the AI is in the room from the first line. The
   cost-bearers are named. The disclosure question is stated as unsettled.
   The course discloses its own AI use (the observer score). No veto.

## Action list

Fixed on the branch:

- Tie "blinded raters" to the plain phrase.
- Replace "Card 5" with a self-contained reference.
- Make the "seventh question" reference stand alone.
- Correct the 21% denominator (papers, not programs) in chapter, summary, and
  answer key.
- Add "say the second sentence only when you know it" after the spine.

Open for the author:

- Objective 5 has no Do activity (Check row only). Add a short written task
  or accept.
- `fig-desk` is decoration by the chapter-pattern test. Keep or cut.
- Three `[VERIFY]` flags remain: state-law text and scope; Tradeoffs episode
  length; public URL for the *ai-safety* deck.
- Run the Part B prompt against ChatGPT Edu and Copilot before the first
  cohort and adjust the persona if it caves.

No stylesheet change needed.
