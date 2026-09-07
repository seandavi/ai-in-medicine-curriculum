# Review: enrichment-environment chapter, 2026-09-07

Six-persona self-review of `chapters/enrichment-environment.qmd` per
`curriculum/personas.md`, Elena first, Lindqvist last. Each finding is
followed by the fix applied in the same pass, or by why it was left. Reviewed
by the AI assistant that drafted the chapter; author to confirm.

## Elena (avoider, surgery, free tier, ESL) — reads first

Passes, with five fixes.

1. **Undefined terms on first use.** "Preprint," "CO2e," "amortized,"
   "inference," and "PUE" appeared before they were explained. *Fixed:* a
   clause on first use for each ("a paper shared before peer review"; "the
   unit that folds every greenhouse gas into one number"; "spread across
   every query it will ever answer"; "the running of a trained model to
   answer requests"; PUE was already expanded).
2. **Does the result depend on how she phrases the prompt?** Step 1 of the
   Do asks a chatbot a question and did not say the answer varies. *Fixed:*
   a sentence that the answer changes with wording, day, and tool, and that
   comparing two classmates' answers is itself part of the exercise.
3. **Her first activity.** Guess, ask a chatbot once, open three free
   tabs. Ten minutes, institutional account, no phone number. Passes.
4. **Is skepticism ever the right answer?** Yes, twice: the resident's
   bottle is wrong by attribution, and the director's five drops is wrong
   by omission. The chapter says both in the same paragraph, which is the
   moment she needs. No change.
5. **Pictures without in-jokes.** The infographic block reads cold; the
   cooling-tower photo needs its caption to say what "on-site water" means,
   which it does. The SVG figure's log scale is explained in the caption.
   *Fixed:* the infographic's third stat said "1 in 3" where the text says
   two-thirds; corrected to "2 in 3."

The 60-minute budget is the right length for her: one hour, one guess, one
ratio.

## Marcus (early adopter, radiology)

Passes on content.

1. **A failure in a tool he trusts.** Step 1 makes the chatbot answer a
   question about itself and then has him check it against three primary
   sources. On the run recorded in the answer key, the tool gives a number
   without model, date, or scope. That is the concrete case. No change.
2. **Something to do tomorrow.** The Hugging Face leaderboard and
   Electricity Maps, both free, and a vendor question with a checkable
   answer. No change.
3. **His specialty.** The Doo et al. *Radiology* 2024 study (metered
   energy across model sizes on chest radiograph reports) is in "The
   denominator" and in Go deeper, cited. No change.
4. **Cites or vibes on the future.** The chapter's forward-looking numbers
   (LBNL, IEA, Google's totals) all carry a source and date. No change.

## Priya (clinician-in-waiting, emergency medicine)

Passes on scenario; one fix.

1. **A scenario she recognizes.** A huddle, a scribe rollout, a colleague
   opting out, and a director who signed the contract. Yes.
2. **Skip the mechanism and still know what to do.** The practical rule is
   in the Part C seeding and the summary: the lever is procurement and model
   choice, not the keyboard; ask which accounting basis and where inference
   is hosted. Her one sentence for a co-intern: "A figure without a model and
   a date is not a figure." Present in the text and the summary.
3. **Who is accountable, and what to document.** Accountability for the
   footprint is placed with the vendor and the committee, not with her. No
   documentation question arises here; the scribe's consent and
   documentation questions are pointed at the patient-communication and
   ethics chapters. *Fixed:* the standing question now says explicitly that
   whether the patient is told belongs to the patient-communication chapter.

## Jordan (instructional designer)

1. **Objectives map to Do or Check.** 1 → Part A; 2 → Check row "Three
   choices"; 3 → Part B; 4 → Check row "The Jevons sentence"; 5 → Part C and
   Check row "The vendor question." All five map. No change.
2. **Time estimate.** Stated as 20 min reading, 11 watching, 25 doing; the
   Check and standing question add about five. The chapter says "about one
   hour" and the subtitle agrees. The qmd is 589 lines against the
   exemplar's ~700 for two hours; reading time is honest for a median
   student. No change.
3. **Stand-alone.** The chapter references the appraisal chapter's
   three-failures table but restates the three failures in its own words
   before using them. A student who skipped that chapter can follow. No
   change.
4. **Accessibility.** TED page has transcript and subtitles; the podcast
   version is an alternative. Every image has `fig-alt`. The *Washington
   Post* link may be paywalled; the Do gives a free secondary source. No
   change.
5. **Does each visual teach something the prose does not?** The infographic
   is the artifact under appraisal. The SVG shows the spread on one axis,
   which the prose can only assert. The press clips show the three tiers.
   The photo shows what evaporative cooling physically is, in a desert. All
   four pass the cover-the-caption test.
6. **Self-applicable Check.** Every row has a "meets" that a student can
   judge without an instructor. No change.
7. **Scenario returns.** In the standing question, and the summary's first
   bullet names the bottle and the five drops. No change.

## Dr. Okafor (borrowing educator)

1. **Could I run the Do alone?** Yes: three URLs, a worksheet, a PubMed
   recipe, and an answer key with model sentences and the arithmetic. No
   change.
2. **Can I restate the mechanism?** The three choices (what you count,
   which query, which model and when) are each one paragraph with one
   number. Jevons is defined with the 1865 coal example. Location- versus
   market-based accounting is defined with the Llama model card. Restatable.
3. **What will a student ask that the chapter does not answer?** "So what
   does *our* scribe cost?" The chapter's honest answer is that nobody has
   measured it and that the vendor question is how to find out. Stated in
   the answer key's model sentences. "What about Microsoft's numbers?" Left
   to the answer key, which carries the three conflicting figures with
   scopes, to keep the chapter within an hour.
4. **Institution-specific parts.** The scenario's "county under watering
   restrictions" and the scribe rollout are generic. Nothing needs swapping.
5. **Staleness.** Every number carries a date, the "These numbers move"
   callout says they move fastest here, and the Google 48/51/81 percent
   sequence shows it happening. The answer key has a dated numbers section
   for the instructor.
6. **Image licences for reuse.** Photo CC0; SVG made by the course, CC BY
   4.0; infographic and press clips are CSS with no third-party material.
   All reusable without conditions. No NC or SA licences in this chapter.

## Dr. Lindqvist (clinical ethicist) — reads last

1. **PHI.** The Do asks a chatbot about itself and reads public documents.
   The warning callout names the temptation (paste a note to "see what it
   costs") and forbids it. Passes.
2. **Does the patient know an AI is in the room?** The scenario's scribe
   records visits. *Fixed:* the standing question now says the disclosure
   question exists and belongs to the patient-communication chapter, rather
   than leaving the scribe's recording unmentioned.
3. **Who bears the cost, named?** Newton County residents; the residents of
   South Memphis presenting with asthma; the population is named and the
   mechanism (siting, local water and air) is stated. Passes.
4. **Contested presented as settled?** Two risks, both handled. The
   Memphis turbine count and permit status change with litigation; the
   chapter gives the case page and a `[VERIFY]`. A draft sentence said the
   volume of prompts "is the reason a new gas plant is being built," which
   overstates causation; *fixed* to "is the demand the turbines in the next
   section were installed to meet." The *Post*'s numbers were paywalled to
   the tool and come from secondary reporting; flagged `[VERIFY]` in the
   chapter and the ledger. The "80 percent" claim is presented as a real
   finding about one use case, with the paper cited, not as false.
5. **Course disclosure.** The ledger row states what was verified by tool
   and what was not, including that one PubMed item had no abstract and one
   author attribution in the module did not match Crossref.
6. **Could the illustrative artifact be mistaken for a real organization's
   material?** The infographic is labeled illustrative in its fine print
   and attributes to "researchers at a major university," which is
   deliberately generic. Passes.

## Corrections to the source module, for the author

- `modules/enrichment-environment.md` attributes the *NEJM Catalyst* piece
  (doi:10.1056/CAT.24.0501) to "Sherman JD et al." Crossref lists Osmanlliu,
  Senkaiahliyan, Eisen-Cuadra, Kalla, Kalema, Rangel Teixeira, and Celi,
  published 16 July 2025. The chapter cites it by DOI without naming
  authors. The module was not edited (out of scope for this branch).
- The module's Google figure "up 48% since 2019" is the 2024 report. The
  2025 report says 51% and the 2026 report 81%; the chapter carries all
  three with dates.

## Action list, applied

1. Defined preprint, CO2e, amortized, inference on first use.
2. Prompt-variability sentence in Do step 1.
3. Infographic "1 in 3" → "2 in 3."
4. Patient-disclosure clause in the standing question.
5. Softened the gas-turbine causation sentence.
6. Jegham label: "short query, as reported" rather than attributing 0.42 Wh
   to the most intensive model, which the abstract does not say.
7. Redrew the SVG labels after an overlap check found four off-canvas and
   two overlapping labels.
