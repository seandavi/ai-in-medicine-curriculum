# Review: core-bias-equity chapter, 2026-09-07

Six-persona self-review of `chapters/core-bias-equity.qmd` per
`curriculum/personas.md`, Elena first, Lindqvist last. Each finding lists the
fix applied in the same pass; open items are marked. Reviewed by the AI
assistant that drafted the chapter; author to confirm.

## Elena (avoider, surgery, free tier, ESL) — reads first

Passes, with five fixes applied.

1. **The opening does not need a chatbot.** Pulse oximeter, blood gas, a man
   who looks unwell. She recognizes it from a sub-I. No fix needed; noted
   because the pattern requires it.
2. **Undefined terms on first use.** Found: *hazard* ("29 percent lower
   hazard"), *counterfactual*, *prediction target*, *photoplethysmography*.
   **Fixed:** each now carries a clause on first use. *Proxy*, *occult
   hypoxemia*, *heat map*, *allocation/representation*, *statistical/social
   bias* were already defined.
3. **Is there a ten-minute way in on a free account?** Part A needs no
   account at all; the chatbot step is optional and says so twice.
   **No fix needed.**
4. **Is skepticism ever the right answer?** Yes, structurally: the standing
   question's correct answer for the risk score is "nothing could be caught",
   and the rubric rewards "could not determine". Her instinct to distrust the
   number on the monitor is the correct clinical move in the opening.
5. **Do the pictures make sense cold?** Photo of an oximeter on a finger:
   yes. Two bar charts: yes, each labeled in words and numbers, no
   abbreviations except SpO2 which is defined in the monitor block.
   **Fixed:** the alt text on both charts states every number.
6. **Prompt fluency.** The optional chatbot step's result does not depend on
   phrasing; the prompt is given verbatim. **No fix needed.**

## Marcus (early adopter, radiology)

Passes.

1. **A failure in a tool he trusts.** The LLM case (Omiye, Zack) and the
   optional step where the model launders a proxy into a fact. Also the
   chest radiograph case, in his specialty, with "who wrote the ground truth"
   as the question. Good.
2. **Something he could not get by asking the model.** The optional step is
   designed so the model's answer is the specimen, not the source. Good.
3. **Treated as an evaluator.** Part B produces a table row he could bring
   to a departmental AI committee. Good.
4. **Cites something about his specialty's future?** Seyyed-Kalantari is
   cited; the FDA-clearance link back to the appraisal chapter names the
   130-summary analysis. **Fixed:** added "so were the chest radiograph
   tools" to the FDA callout so he reads it twice.

## Priya (clinician-in-waiting, emergency medicine)

Passes on scenario, one fix applied.

1. **Skip the mechanism, still know what to do?** The oximeter section
   originally had no single practical rule. **Fixed:** added the co-intern
   sentence: "when the number and the patient disagree, believe the patient
   and get the direct measurement."
2. **A scenario she recognizes.** Night cross-cover, a nurse call, a number
   that says go back to bed. Yes.
3. **Who is accountable, what to document.** The standing question asks what
   to tell the patient; the answer key gives a form of words. Accountability
   for the deployed risk score is answered structurally (an auditor with
   authority), and the ethics chapter is named for the disclosure rule.
   Adequate for AIM-3; the ethics chapter owns the rest.

## Jordan (instructional designer)

1. **Objective map.** 1 → worksheet line 1 and the "one sentence" Check row.
   2 → Part A. 3 → Part B and Check line 4. 4 → lines 6 and 7. 5 → line 5
   and the "counterweight" Check row. All five objectives assessed.
2. **Time.** 25 + 25 + 35 + 5 = 90, stated in the Time note and the
   subtitle. Reading is ~4,100 words of prose plus a seven-row table; 25
   minutes is honest for a median reader, tight for Elena. Acceptable.
3. **Standalone.** The appraisal chapter is referenced twice and neither
   reference is load-bearing; a student who skipped it loses one callout.
4. **Accessibility.** Podcast is on four platforms; the fallback is a
   written deck. Every image has `fig-alt` with the numbers spelled out.
5. **Visuals earn their place.** Photo: shows the device and a reading, on
   a dark-skinned hand, which is the whole scenario. Chart 1: four cohorts,
   one direction, which prose cannot do in one glance. Chart 2: the 17.7 to
   46.5 jump. Two `.vendor-slide` blocks: the monitor is the thing the
   student is asked to disbelieve; the dashboard tile is the artifact under
   appraisal in Part A. Nothing decorative.
6. **Check is self-applicable.** Yes; the answer key is only needed for
   Part B specifics.
7. **Scenario returns.** Bed 14 is in the standing question and the summary.

## Dr. Okafor (borrowing educator)

1. **Run the Do alone?** Part A is entirely in the chapter with the answer
   key. Part B's pre-vetted set has one verified paper per specialty cluster.
   Yes.
2. **Restate the mechanism?** The four-step Obermeyer walk (job, measurement
   problem, failure, correction) is written to be read aloud. The oximeter
   mechanism is two sentences. Yes.
3. **What will students ask that the chapter does not answer?** "So which
   equation should the lab use for spirometry?" The chapter deliberately
   says contested and points to Diao et al.; an adopter should know that is
   the intended answer, and the answer key says so.
4. **Institution-specific parts.** ChatGPT Edu / Copilot named once, in the
   optional step, with "your institutional" as the marker.
5. **Stale in twelve months?** The status column is dated "as of September
   2026", the FDA draft status carries a dated `[VERIFY]`, and the summary
   says the LLM answers move. Yes, marked.
6. **Image licences for reuse.** Photo is CC BY-SA 4.0. **Fixed:** caption
   now says "reuse requires the same licence" per the pattern. The two SVG
   charts are redrawn data with citations; no restriction. The two styled
   blocks are CSS and labeled illustrative.

## Dr. Lindqvist (clinical ethicist) — reads last

1. **PHI.** No step touches a patient. The warning callout is at the top of
   Do and repeated in the optional step. Passes.
2. **Does the patient know?** The opening says explicitly that nobody in the
   room, including the patient, knew the device's calibration population,
   and the standing question makes "should he be told, and what" a required
   written answer. Passes.
3. **Who bears the cost, named?** Every row of the proxy table names the
   population and the decision; the Fawzy pathway (451 never recognized,
   most Black) is the worked example. The spirometry row names that the
   correction has costs for White veterans too, so the harm is not
   described as one-directional where the evidence says it is not. Passes.
4. **Contested presented as settled?** Spirometry is labeled contested with
   the modeling that shows why; the FDA guidance is labeled draft with a
   dated flag; eGFR adoption is flagged unconfirmed rather than asserted.
   The chest radiograph and LLM rows say "no correction adopted" rather than
   implying one. Passes.
5. **Register.** The module asks that the session be framed as a post-mortem
   rather than a debate. **Fixed:** added the "A note on register" callout
   before the catalog. Kept to five sentences so it does not become the
   paragraph-on-ethics failure mode.
6. **Illustrative artifacts mistakable for real material?** The monitor and
   dashboard tile carry the "illustrative; not a real device / vendor" line
   in the block. Passes.
7. **AI disclosure.** The ledger row records that the model drafted the
   chapter, retrieved and read every PMID, and built the SVGs from published
   numbers; the Obermeyer figure numbers came from secondary summaries of a
   paywalled paper, and the answer key says so.

## Citations and flags

Twenty PMIDs retrieved and read this session; every `@pmid:` key in the
chapter is one of them. Three `[VERIFY]` flags remain, all on claims that are
stated conditionally in prose: FDA draft status (dated check), eGFR adoption
figure (not asserted), Crawford keynote URL. One module claim was dropped
rather than flagged: the "22.7% of Black and 3.3% of Southeast Asian
individuals reclassified" spirometry figure could not be located in PubMed
and is replaced by the verified Diao et al. 2024 numbers.

## Action list, applied

1. Define hazard, counterfactual, prediction target, photoplethysmography.
2. Add the co-intern sentence to the oximeter section.
3. Add the register note before the catalog.
4. Note the share-alike condition in the photo caption.
5. Name the chest radiograph tools in the FDA callout.
