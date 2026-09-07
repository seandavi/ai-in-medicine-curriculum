# Review: core-foundations chapter, 2026-09-07

Six-persona self-review of `chapters/core-foundations.qmd` per
`curriculum/personas.md`, done by the AI assistant that drafted the chapter,
before the PR. Each finding is followed by what was changed in the same pass.
Items marked *open* were not fixed and are for the author.

## Elena (avoider, surgery, free tier, ESL) — reads first

Passes, with five fixes.

1. **"By regression" in the first paragraph of The idea** used the word two
   paragraphs before the chapter defined it. *Fixed:* dropped the phrase and
   added a plain-language clause for "fit".
2. **"Area under the curve" undefined** in the sepsis-model sentence.
   *Fixed:* one clause, "0.5 is a coin flip and 1.0 is perfect".
3. **"Epoch" undefined** in Part A step 1. *Fixed:* defined inline as one pass
   through the data, and pointed at the on-screen counter.
4. **Prompt fluency not addressed.** Her standing question, "does the result
   depend on how I phrase it", was unanswered. *Fixed:* one sentence at the
   end of Part B inviting a plainer-worded re-ask and pointing at the appraisal
   chapter for the measured effect.
5. **Does the comic land cold?** xkcd 2048 assumes the reader can see that
   every curve fits the same dots. The caption says that in one line, and
   the alt text describes the "house of cards" panel. Judged acceptable;
   *open* for the author to confirm.

What works for her: the scenario is a surgery pre-op clinic; the account
requirement is her institutional one with no phone number; "What this does
and does not mean" separates the justified fear from the outdated one in her
own terms; and the Do has a moment (Part B) where skepticism is the correct
result.

## Marcus (early adopter, radiology)

Passes.

1. **A failure he did not expect in a tool he trusts:** the eGFR history
   table and the sepsis-model external validation both qualify; Part B is the
   one he does with his own hands. No change.
2. **Something to do tomorrow:** the two questions in `@tbl-two-questions` and
   the two window rules. No change.
3. **Radiology hook:** none in this chapter; the mechanism chapter is
   specialty-neutral by design, and the raw-material box in the loop figure
   names images. *Open, minor:* the deep learning deck in Go deeper opens on
   medical imaging and is the pointer.

## Priya (clinician-in-waiting, emergency medicine)

Passes on scenario and on the practical rule.

1. **If she skips the mechanism**, the two callouts ("The one sentence",
   "Nothing in this mechanism checks whether a claim is true") plus the
   no-PHI warning and the window rules are the wards-facing content. No change.
2. **Who signs and what to document** were absent. *Fixed:* one sentence in
   the no-PHI callout, "whatever drafts a note, you sign it", with a pointer to
   the ethics and regulation chapter for documentation.
3. **Scenario she recognizes:** the sepsis alert she silenced on her sub-I is
   now in the chapter as the external validation with the numbers. No change.
4. Her one sentence for a co-intern: "if the training set and the test set
   are the same, you have no number yet." Present.

## Jordan (instructional designer)

1. **Time estimate.** First draft said 20 + 27 + 20 + 8 = 75 with a reading
   block that is closer to 22 minutes for the prose length. *Fixed:* 22 + 27 +
   20 + 6 = 75; subtitle unchanged.
2. **Objective mapping.** 1 → Check row 1 and the standing question; 2 → Check
   row 2; 3 → Do Part A and Check row 3; 4 → Do Part B and Check row 4; 5 → Do
   Part C and Check row 5. All five map. No change.
3. **Accessibility.** The two mermaid figures had captions but no alt text.
   *Fixed:* `fig-alt` added to both in the source. *Open:* Quarto's HTML
   mermaid renderer does not carry `fig-alt` into the output (grep of the
   rendered page finds neither), so the captions are doing that job for now;
   same limitation applies to the appraisal chapter's mermaid figure. The
   xkcd image has `fig-alt`. Captions and a transcript for the video are noted
   in Watch.
4. **Broken-link survival.** playground.tensorflow.org has no mirror.
   *Fixed:* a fallback (screenshots in the archived deck) added to Part A, and
   an instructor note in the answer key.
5. **Scenario returns:** standing question and the last summary bullet. No
   change.

## Dr. Okafor (borrowing educator)

1. **Could they run the Do alone?** Yes: the Playground steps name the panel,
   the dataset position, and the buttons; Part B has a verified target table
   so the instructor does not need to know the scores.
2. **Mechanism restatable by a non-specialist?** The keyboard analogy, the
   "predict, pick one, repeat" sentence, and the "no truth step" callout are
   written to be read aloud. No change.
3. **Questions students will ask.** "Which equation does my lab use?" is
   answered by the lab-report footnote convention (the illustrative panel
   names CKD-EPI 2021). "What is attention?" is delegated to the video with
   permission to let it go. "So is it usually wrong?" is answered in the
   "What this does and does not mean" callout.
4. **Stale in twelve months:** context-window figures and token prices are
   deliberately not quoted, and the chapter says why. Model behaviour in Part
   B will drift; the answer key says to re-run it the morning of the session.
5. **Image reuse:** xkcd is CC BY-NC 2.5, noted in the caption as
   non-commercial; the lab report, chat block, and both mermaid figures are the
   course's own. Table 1 is redrawn from the papers' numbers.

## Dr. Lindqvist (clinical ethicist) — reads last

1. **PHI.** Part A uses a toy dataset; Part B asks about a published scoring
   system. The callout names the business associate agreement and says the
   institutional account does not change the rule. No activity touches a
   patient, classmate, or real note. Passes.
2. **Does the patient know a model is in the room?** The scenario's model is
   the eGFR, and no one tells patients where that number comes from. *Fixed:*
   one sentence in the standing question noting that and handing the question
   to the patient communication chapter, without adding an ethics paragraph.
3. **Who bears the cost.** Named at each point: Black adults in the eGFR
   history (with the medians), the 67 percent of septic patients the vendor
   model missed, and the 45 kg patient in the clinic. No change.
4. **Contested claims presented as settled.** The RLHF paragraph asserted
   that preference tuning "rewards confidence". *Fixed:* softened to "in
   practice tends to reward", stated as a tendency. Context-rot thresholds are
   explicitly withheld. The MYCIN sentence was tightened to match the abstract
   ("never failed to cover a treatable pathogen").
5. **Illustrative artifacts.** The lab panel and the chat exchange are both
   labeled illustrative in the block itself; the chat block adds "do not use
   as a source". Neither carries a real company's or person's branding. The
   chat block does name real authors of a real validation paper as the
   "original"; that is the intended specimen and the prose says so
   immediately after.
6. **Course's own AI use.** Ledger row added; the appendix carries the
   standing disclosure.

No veto.

## Verification record

- 18 `@pmid:` keys, every one retrieved and its metadata read this session:
  34554658, 19414839, 10075613, 34260843, 480542, 34152373, 34563581,
  37460753, 30053147, 18665203, 12728155, 3963537, 11556941, 11073021,
  7165009, 10744147; plus 13083014 (Apgar 1953), which PubMed returns but
  quartobot cannot resolve (no DOI), so it is linked in the table as plain
  text rather than cited.
- 1 `@doi:` key (10.1162/tacl_a_00638, Liu et al., TACL 2024) confirmed via
  Crossref.
- Numbers checked against abstracts: CKD-EPI 2021 development and validation
  counts and race medians; CKD-EPI 2009 counts; MDRD counts and the
  higher-GFR underestimation; Epic sepsis model AUC, miss rate, and alert
  rate; MYCIN 65 percent versus 42.5–62.5 percent.
- Video: 3Blue1Brown *But what is a GPT?*, YouTube `yMQPQuz5WpA`, published
  1 April 2024, 27 minutes (length from search results; the lesson page
  confirms the date). Karpathy *Intro to Large Language Models*, November
  2023, about one hour, confirmed via the video page and a dated contemporary
  post.
- Image: xkcd 2048 *Curve-Fitting*, downloaded from imgs.xkcd.com, licence
  line on xkcd.com confirmed CC BY-NC 2.5.
- playground.tensorflow.org confirmed reachable on 2026-09-07; three
  talks.seandavis.net archive URLs return 200.

## Open `[VERIFY]` flags

- 3Blue1Brown *But what is a neural network?* length and date (Go deeper).
