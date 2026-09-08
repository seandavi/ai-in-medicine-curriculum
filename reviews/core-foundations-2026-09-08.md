# Review: core-foundations chapter, 2026-09-08

Six-persona review of `chapters/core-foundations.qmd` per
`curriculum/personas.md`, done by the AI assistant after the plain-language
pass on the same branch (`pass/core-foundations`), and filed as GitHub
issue #36. Each finding is followed by what was changed in the
same pass. Items marked *open* were not fixed and are for the author.

## What the plain-language pass changed first

Same content, same section order, same numbers, citations, figure ids,
`fig-alt` text, and block classes. Terms replaced or defined:

- Replaced: "emits" (gives, gives out); "fabricated" (made-up); "mechanism"
  (how it works, the process); "structural" (built-in); "attended to less
  reliably" (gets less reliable attention); "deployment" (in real use, on the
  ward); "artifact" (the three sentences you keep); "deliverable" (the line
  that matters); "specimen" (example); "reference class" (history);
  "the non-negotiable minimum" (the least you should accept); "sample a token
  from the distribution" (pick one at random, weighted by the probabilities);
  "retrieval-grounded" (built from search results); "regenerate the data"
  (press the regenerate button); "capacity" (make the model more flexible);
  "contort" (bend); "transfers" (carries over); "coefficient" (multiplier, a
  term that adjusted the result); "systematically underestimated" (gave values
  that were too low); "investigators pooled" (researchers combined);
  "immutable" (permanent); "model zoo" (the other algorithms); "fluent"
  (smooth) where it was doing no work.
- Defined on first use and kept: extrapolation, external validation, training
  loss and test loss, plausible ("the one most likely to follow"), model card,
  prompt injection, epoch, hidden layer and neuron (see Elena below).
- Headings: "The idea" is now "How it works"; "The standing question" is now
  "What this changes for you"; the title dropped "actually".
- Roughly 45 sentences split; no em-dashes were present.
- `_answers/core-foundations.md`: "the mechanism sentence" is now "the
  one-sentence explanation", matching the Check row.

## Elena (avoider, surgery, free tier, ESL) — reads first

Passes, with three fixes.

1. **The xkcd caption read as praise.** "The one on the bottom right fits it
   best" is sarcasm, and an ESL reader taking it literally would learn the
   opposite of the lesson. *Fixed:* the caption now says the curve passes
   through every point and is the worst model of the twelve.
2. **"Hidden layer" and "neurons" undefined** in Part A step 1; they are the
   site's own words, so they have to appear. *Fixed:* one clause naming them
   as the site's terms for the middle stage of the network and the units in
   it.
3. **"Toy dataset that ships with the tool"** is idiom on idiom. *Fixed:* "a
   small practice dataset built into the site".
4. Way in: Part A needs no account; Part B uses the institutional login
   named in the Time note. Justified versus outdated fear is separated in
   "What this does and does not mean"; Part B is the moment where skepticism
   is the right answer; the end of Part B says the result depends on wording.
   No change.

## Marcus (early adopter, radiology)

Passes.

1. A failure he did not expect in a tool he trusts: the eGFR history table,
   the sepsis-model external validation, and Part B against a verified
   target. No change.
2. Something to do tomorrow: `@tbl-two-questions` and the two window rules.
   No change.
3. No radiology hook; the chapter is specialty-neutral by design and the deep
   learning deck in Go deeper is the imaging pointer. No change.

## Priya (clinician-in-waiting, emergency medicine)

Passes.

1. Skipping the mechanism still leaves the wards-facing content: "The one
   sentence", "Nothing in this process checks whether a claim is true", the
   no-PHI callout with "you sign it", and the two window rules. No change.
2. Scenario she recognizes: the sepsis alert, with the miss rate and alert
   rate. No change.
3. Documentation is handed to the ethics and regulation chapter with a
   pointer. No change.
4. Her co-intern sentence: "if the training set and the test set are the
   same, you have no number yet." Present.

## Jordan (instructional designer)

1. **Objective mapping.** Objectives 1–5 still map to Check rows 1–5 and to
   Do Parts A, B, and C; the plain-language pass changed wording only. No
   change.
2. **Time estimate.** Word count rose about 2 percent (splitting sentences
   adds words). 22 minutes of reading is still about right. No change.
3. **Heading names.** Two block headings were renamed in the plain-language
   pass ("How it works", "What this changes for you"). Sibling chapters may
   land on different names. *Open, author:* settle the book-wide heading
   names in the cross-reference pass (#13); this chapter will follow.
4. **Accessibility.** Quarto still does not carry mermaid `fig-alt` into the
   HTML output; captions do that job. *Open,* book-wide, unchanged from
   09-07.
5. **Visuals.** Each teaches something the prose does not; the caption fix
   under Elena makes the comic land on its own. No change.

## Dr. Okafor (borrowing educator)

1. The Do can be run alone: panel names, buttons, and a verified target
   table. No change.
2. **Swap point not marked.** The Time note named "ChatGPT Edu or Microsoft
   Copilot" as if fixed. *Fixed:* "or whatever assistant your school
   provides".
3. Stale-in-a-year content: window figures deliberately withheld; Part B
   drift covered by the answer key's re-run instruction; `@tbl-scores` carries
   its verification date. No change.
4. Image reuse: xkcd is CC BY-NC 2.5 and the caption says so; the rest is the
   course's own. No change.

## Dr. Lindqvist (clinical ethicist) — reads last

1. **PHI.** Part A uses a practice dataset; Part B asks about a published
   score. No activity touches a patient, classmate, or real note. Passes.
2. **Certainty exceeding evidence.** The context-window paragraph asserted,
   with no citation, that output-token cost is *why* the tools are "quietly
   tuned to answer briefly" and that the advertised window "is rarely the
   usable one". *Fixed:* stated as "one reason" and "often smaller than", a
   tendency rather than a mechanism.
3. **Uncited claim.** "Later studies across newer models have found quality
   dropping as the input grows long" has no citation. *Open, author:* add a
   2025 long-context evaluation or cut the sentence; the Liu et al. finding
   stands on its own.
4. Who bears the cost is named at every point: Black adults in the eGFR
   history, the 67 percent of septic patients missed, the 45 kg patient in
   clinic. No change.
5. The lab panel and the chat exchange are labeled as made up inside the
   block. No change.

No veto.

## Action list

1. Done: xkcd caption says the best-fitting curve is the worst model (Elena).
2. Done: hedge the output-token-cost causal claim (Lindqvist).
3. Done: gloss "hidden layer" and "neurons" in Part A (Elena).
4. Done: replace "toy dataset that ships with the tool" (Elena).
5. Done: mark the institutional account as the swap point (Okafor).
6. Open, author: cite or cut "later studies across newer models" (Lindqvist).
7. Open, author: book-wide heading names after the plain-language pass,
   under #13 (Jordan).
8. Open, book-wide: mermaid `fig-alt` not rendered by Quarto (Jordan).

## Verification record

- No number, citation key, or figure changed in either pass, so the 09-07
  verification record stands. Citation keys re-resolved through quartobot at
  render.
- The PubMed API was rate-limited during this pass (eleven sibling agents on
  one address); resolution was retried until the cache was complete.

## Open `[VERIFY]` flags

- 3Blue1Brown *But what is a neural network?* length and date (Go deeper),
  unchanged.
