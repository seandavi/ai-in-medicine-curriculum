# Review: enrichment-environment chapter, 2026-09-08

Six-persona review of `chapters/enrichment-environment.qmd` after the
plain-language pass of the same day, per `curriculum/personas.md`, Elena
first, Lindqvist last. Filed as issue #41. Each finding is followed by the
fix applied in the same pass, or by why it was left. Reviewed by the AI
assistant that ran the pass; author to confirm.

## What the plain-language pass changed (context for this review)

Headings "The idea" and "The standing question" became "How the numbers were
made" and "What this changes for you". Design-doc and insider words were
replaced or glossed on first use: carbon-accounting, attribute, orders of
magnitude, infrastructure, tiers, inclusive, amortized, benchmark,
superseded, converged, module, baseline, methodology, diffuse, competency,
training cluster, aquifer, legitimate conventions, model card, denominator,
lever, fine-tuned, perspective, deployment, encounter, predates, procurement,
aggregate, water scope; and reference / attribution / claim each got a plain
gloss. About sixty clause-stacked sentences were split. No number, citation,
`[VERIFY]` span, figure id, alt text, block class, callout, objective, or
section order changed.

## Elena (avoider, surgery, free tier, ESL) — reads first

Passes, with three fixes.

1. **"Prompt" and "per-query" before definition.** The scenario used
   "prompt" and objective 2 used "per-query" before either was explained.
   *Fixed:* "a prompt, one message to a chatbot"; "per-query figures (the
   cost of one question to a chatbot)".
2. **Bare energy units.** Wh, kWh, and TWh appeared without a hook. *Fixed:*
   a watt-hour is what a one-watt LED uses in an hour, a kilowatt-hour is a
   thousand of them, a terawatt-hour is a billion kilowatt-hours.
3. **Three more unexplained words.** "Open models," "parameter," and "the
   local grid." *Fixed:* one-clause glosses each.
4. **First activity.** Guess, one chatbot question, three free tabs. Ten
   minutes, institutional account, no phone number. Passes.
5. **Skepticism as the right answer.** The resident and the director are
   both wrong, differently, in one paragraph. Passes.
6. **Prompt wording.** Step 1 says the answer changes with wording, day, and
   tool. Passes.
7. **Pictures.** Infographic, SVG (log scale explained in caption), press
   clips, cooling-tower photo. All read cold. Passes.

## Marcus (early adopter, radiology)

Passes on content; no change.

1. **A failure in a tool he trusts.** Step 1 collects the chatbot's
   unsourced number and checks it against three primary sources.
2. **Tomorrow.** Electricity Maps, the AI Energy Score leaderboard, and a
   vendor question with a checkable answer.
3. **His specialty.** Doo et al., *Radiology* 2024, is cited with numbers.
   Abstract re-checked in PubMed this session: the 7B fine-tuned Vicuna
   matched the 70B general-purpose Llama 2 on accuracy, and the 70B used
   4.16 kWh against 0.59 kWh for the 7B, more than seven times. The chapter's
   wording matches.
4. **Cites or vibes on the future.** LBNL, IEA, and Google's totals all
   carry a source and date.

## Priya (clinician-in-waiting, emergency medicine)

Passes; no change.

1. **Skip the mechanism, still know what to do.** Part C's rule, the summary
   bullets, and the co-intern sentence: "a figure without a model and a date
   is not a figure."
2. **Scenario she recognizes.** Huddle, scribe rollout, a colleague opting
   out, a director who signed the contract.
3. **Accountability and documentation.** Footprint accountability sits with
   purchasing and the vendor. Patient disclosure is explicitly pointed at the
   patient-communication chapter.

## Jordan (instructional designer)

1. **Objectives map to Do or Check.** 1 → Part A; 2 → Check "Three choices";
   3 → Part B; 4 → Check "Jevons sentence"; 5 → Part C and Check "The vendor
   question". Passes.
2. **Time estimate.** About 4,500 words of prose (20 min), 11 min video, 25
   min Do, 5 min Check. About one hour, as the subtitle says. Passes.
3. **Stand-alone.** The appraisal chapter's reference / attribution / claim
   triad is now glossed inline, so a student who skipped that chapter can
   follow. Improved by the pass.
4. **Accessibility.** Every image has alt text; TED has a transcript; the
   paywalled *Post* has a free alternative. Passes.
5. **Headings.** The pass renamed the two pattern headings ("The idea", "The
   standing question"). *Left open:* sibling chapters may have chosen
   different plain names; the book should settle on one set. Author's call.
6. **Scenario returns.** In "What this changes for you" and the summary's
   first bullet. Passes.

## Dr. Okafor (borrowing educator)

1. **The question a student will ask.** "So what does *our* scribe cost?"
   was answered only in the answer key. *Fixed:* Part C now opens with
   "Nobody has published a measured figure for an ambient scribe. The way to
   get one is to ask."
2. **Could I run the Do alone?** Three URLs, a worksheet, a PubMed recipe,
   an answer key with model sentences and the arithmetic. Passes.
3. **Restatable mechanism.** Three choices, one paragraph and one number
   each; Jevons with the 1865 coal example; location- versus market-based
   with the Llama model card. Passes.
4. **Institution-specific parts.** None.
5. **Staleness.** Every number dated; the "These numbers move" callout; the
   answer key's dated-numbers section. Passes.
6. **Image licences.** CC0 photo, CC BY 4.0 course SVG, CSS blocks. Reusable
   without conditions. Passes.

## Dr. Lindqvist (clinical ethicist) — reads last

1. **PHI.** The Do asks a chatbot about itself and reads public documents;
   the warning callout names and forbids the temptation. Passes.
2. **Accuracy of the Memphis paragraph.** The linked Earthjustice case page
   (fetched 2026-09-08, created April 2026) describes NAACP v. xAI, filed in
   the Northern District of Mississippi, over 27 unpermitted turbines in
   Southaven, Mississippi, powering the Colossus 2 data center in South
   Memphis, "half a mile from homes and just a mile from an elementary
   school". The chapter had said "in South Memphis ... sued by the NAACP and
   the Southern Environmental Law Center", merging the 2025 Memphis site
   (notice of intent, later county permits) with the 2026 Mississippi suit.
   *Fixed:* the paragraph now names both sites, puts the lawsuit and the 27
   turbines in Southaven, keeps the American Lung Association F grade with
   the Memphis site, and keeps the existing `[VERIFY]` span. The answer key's
   Memphis line now carries the two-site history with its own `[VERIFY]` on
   the site-1 turbine and permit counts, which come from press memory and
   were not re-checked this session.
3. **Who bears the cost, named.** Newton County residents; the neighborhoods
   around the South Memphis and Southaven sites. Passes.
4. **Contested presented as settled.** Nothing new. The Register headline is
   loaded ("games numbers"), but the chapter's own prose states only what
   each party counted and lets the reader weigh it. No change.
5. **Course disclosure.** Ledger rows are added by the coordinator for the
   whole pass. Nothing chapter-side.
6. **Illustrative artifact.** The infographic is labeled illustrative and
   attributed generically. Passes.

## Action list

1. Gloss prompt, per-query, Wh/kWh, TWh, open models, parameter, grid. *Done.*
2. "Nobody has measured the scribe" sentence at the top of Part C. *Done.*
3. Rewrite the Memphis paragraph to match the linked case page; update the
   answer key. *Done.*
4. Settle the book-wide plain names for "The idea" and "The standing
   question". *Open, author's call.*
5. Re-check the Memphis site-1 turbine count and July 2025 permit numbers in
   the answer key against a press source before the live session. *Open,
   flagged `[VERIFY]` in the answer key.*

## Notes for the coordinator

- No stylesheet change needed.
- `quartobot resolve` was rate-limited by PubMed (429) during this pass
  because eleven agents ran it at once. No citation keys were added, so the
  render was done with the resolver shimmed out and the main checkout's
  `references.resolved.bib`, per the coordinator's instruction. The rendered
  chapter has no unresolved (`???`) citations.
