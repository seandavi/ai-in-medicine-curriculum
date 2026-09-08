# Review: core-bias-equity chapter, 2026-09-08

Six-persona review of `chapters/core-bias-equity.qmd` after the plain-language
pass, per `curriculum/personas.md`, Elena first, Lindqvist last. Filed as
GitHub issue #32. Fixes were applied in the same pass; open items are marked
and need the author's call. Reviewed by the AI assistant that made the pass;
author to confirm.

## What the plain-language pass changed

Same content, same section order, same numbers, citation keys, `[VERIFY]`
spans, figure ids, `fig-alt` text, block classes, and callout structure
(checked by script against the 2026-09-07 file). No em-dashes. Sentences
split to about one idea each; roughly 60 sentences split. Word count 5,608
to about 5,830.

Terms replaced with plain words: *anchor case* (main case), *register* (tone),
*artifact* (what a clinician would have seen; the row you hand in),
*substituted / substitution* (used in its place; the swap), *counterfactual*
(dropped; the idea stated in plain words), *reformulated* (changed what the
model predicted), *denominator* (a count, by group), *load-bearing* (needed;
both are needed), *vigilance* (alertness), *systematically* (consistently;
deliberately, for the Jabbour model), *in aggregate* (only when you count
across many patients), *vignettes* (written cases), *post-mortem* (review of a
failure), *taxonomy* (a list sorted by where they come from), *laundered*
(turned into a "fact"), *canonical* (well-known), *normed away* (counted as
normal), *compounding at intersections* (worst for patients in more than one
of these groups), *frame* (answer), *catalog* heading (the cases in one
table), *interrogating the prediction target* (asking what the model actually
predicts), *reweighting / adversarial debiasing / post-processing thresholds*
(described in plain words), *mentation* (how alert he is), *discrepancy*
(mismatch), *signal* (sign), *unversioned* (without clear version notes),
*decision summary* (clearance summary), *benchmark score* (test-set score),
*race coefficient* (race multiplier, in the table; kept as "race coefficient"
in Go deeper where it names the paper's subject).

Terms kept as taught terms, each with a plain definition on first use:
*proxy*, *proxy problem*, *occult hypoxemia*, *hazard*, *prediction target*,
*statistical / social bias*, *allocation / representation harm*, *heat map*,
*ground truth*, *task formulation*, *photoplethysmography*, *cohort*,
*NeurIPS*.

Headings: "The idea" became "How the failures happen"; "Two distinctions"
became "Two pairs of terms"; "The catalog" became "The cases in one table";
"The finding that complicates the bedside frame" became "The study that
complicates the bedside answer"; "The standing question" became "What this
changes for you", and the Time note says "closing question". Callout titles:
"A note on register" became "A note on tone"; "Necessary and insufficient"
became "Needed, and not enough". Worksheet line 3 is now "WHAT FIX FOLLOWED";
the Check row "The counterweight" is now "The other half". The answer key was
updated to match.

## Elena (avoider, surgery, free tier, ESL) — reads first

Passes, with two fixes applied.

1. **Assumes a chatbot?** No. Part A needs nothing but the chapter; the
   optional step says twice that the exercise is complete without it.
2. **Undefined terms.** After the pass every taught term is glossed on first
   use. **Fixed:** *cohort* appeared unglossed one sentence after "two groups
   of patients"; now "two cohorts, meaning two groups of patients".
   **Fixed:** "a tile in a population-health dashboard" now says what a
   population-health dashboard is.
3. **Ten-minute way in?** Part A, no account. No fix needed.
4. **Skepticism the right answer?** Yes, in the opening (believe the man, not
   the number) and in the rubric ("could not determine" with a reason meets).
5. **Prompt fluency.** The one prompt is verbatim. No fix needed.
6. **Pictures cold.** Photo and two labeled bar charts; alt text unchanged.

## Marcus (early adopter, radiology)

Passes; nothing changed. The chest radiograph case is in his specialty and
cited; the optional step makes the model's answer the specimen; the co-intern
sentence and the Part B row are the things to do tomorrow.

## Priya (clinician-in-waiting, emergency medicine)

Passes, one fix applied.

1. **The rule without the mechanism.** Present: believe the patient, get the
   direct measurement.
2. **What to document.** **Fixed:** the oximeter section now says to write
   the mismatch in the note with both numbers, so the next person covering
   the patient knows the oximeter reads high on him.
3. **Who is accountable.** For the risk score, structurally: someone
   counting by group with the power to act. The ethics chapter owns the
   disclosure rule; the closing question still makes the student decide what
   to tell the patient.

## Jordan (instructional designer)

1. **Objective map.** Unchanged: 1 → worksheet line 1 and the "one sentence"
   Check row; 2 → Part A; 3 → Part B and Check line 4; 4 → lines 6 and 7;
   5 → line 5 and the "other half" Check row.
2. **Time.** About 220 words added by sentence splitting. Reading is still
   about 25 minutes for a median reader, tight for Elena. **Open:** trim if
   90 minutes is a hard ceiling; the "Why this chapter does not teach you to
   fix the model" section could drop to three sentences.
3. **Skeleton headings.** **Open, author / coordinator:** "The idea" and
   "The standing question" were renamed in this chapter. If sibling chapters
   keep the originals the book is inconsistent; pick one plain name per
   skeleton slot for all chapters, or accept per-chapter names.
4. **Accessibility.** `fig-alt` text identical to the verified version;
   podcast has a written fallback.
5. **Check self-applicable.** Yes.
6. **Scenario returns.** Bed 14 is in the closing question and the summary.

## Dr. Okafor (borrowing educator)

1. **Run the Do alone?** Yes, from the chapter and the answer key.
2. **Answer key matches the worksheet.** **Fixed:** item 3 and the Part B
   column header now say "Fix" to match "WHAT FIX FOLLOWED"; the "Standing
   question, bed 14" heading now names the renamed chapter section.
3. **Restate the mechanism?** The oximeter and Obermeyer walk-throughs are
   now shorter sentences; easier to read aloud than before.
4. **Institution-specific and stale parts.** Still marked ("institutional",
   dated status, `[VERIFY]` with dates).
5. **Image licences.** Unchanged: CC BY-SA photo with the share-alike note,
   redrawn SVGs, illustrative CSS blocks.

## Dr. Lindqvist (clinical ethicist) — reads last

Passes; nothing changed.

1. **PHI.** No step touches a patient; the warning callout stands.
2. **Does the patient know?** Stated in the opening; the closing question
   requires a decision on what to tell him.
3. **Who bears the cost.** Every table row names the group and the decision;
   the spirometry row still names the cost to White veterans of the fix.
4. **Contested as settled?** Spirometry "actively contested", FDA guidance
   "still draft" with a dated flag, eGFR adoption flagged unconfirmed.
5. **Tone.** The register callout survives as "A note on tone", same
   content, same length.
6. **Claim wording after the rewrite.** "Eleven devices overestimated
   saturation more in darkly pigmented participants" is the plain form of
   "more positive bias"; "deliberately biased" is accurate for a model the
   Jabbour authors built to be wrong in one direction.

## Citations and flags

No citation key or number changed. PubMed re-check not run today: NCBI
returned 429 rate-limit errors during the parallel pass; the numbers are the
set verified on 2026-09-07. Three `[VERIFY]` flags remain, unchanged.

## Action list

1. Gloss *cohort* on first use. **Done.**
2. Gloss "population-health dashboard". **Done.**
3. Add the documentation sentence for Priya. **Done.**
4. Align answer-key labels with the renamed worksheet line and section.
   **Done.**
5. Decide skeleton heading names across chapters. **Open, author.**
6. Decide whether to trim about 200 words. **Open, author.**
7. Three `[VERIFY]` flags: FDA draft status, eGFR adoption figure, Crawford
   keynote URL. **Open, unchanged.**
