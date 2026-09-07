# Review: core-centaur-cyborg chapter, 2026-09-07

Six-persona self-review of `chapters/core-centaur-cyborg.qmd` per
`curriculum/personas.md`, done by the AI assistant that drafted the chapter,
before the PR. Findings are listed per reviewer with the fix applied in the
same pass; items not fixed are marked *open*. Author to confirm.

## Elena (avoider, surgery, free tier, ESL) — reads first

Passes, after five fixes.

1. **Undefined terms on first use.** "Language model," "ambient scribe,"
   "EHR," and "frontier model" appeared before any definition. *Fixed:* each
   now carries a clause on first use; "frontier model" replaced with "GPT-4."
   "Metacognition" and "business associate agreement" were already defined.
2. **Ten-minute way in.** Part A step 1 needs only a pen, and the callout
   "If you have ten minutes and no appetite for the chatbot" says so
   explicitly. No fix needed.
3. **Prompt fluency.** The Who / Where / What section says the difference
   between a hint and an answer is not obvious if English is not your first
   language. Present; no fix needed.
4. **Skepticism as the right answer.** "Not at all" is a listed verdict, and
   the opening now says "never" is available for any single line (added when
   softening the "that argument is over" sentence; see Lindqvist 3). The
   drafted note is the moment where distrust is correct. No further fix.
5. **Pictures land cold.** The task list, the drafted note, and the bar chart
   need no prior knowledge. The mermaid decision figure uses "validated,"
   which is defined in the paragraph above it. No fix needed.

What works for her: the chapter opens on a list, not a term; the drafted-note
error is visible without knowing anything about AI.

## Marcus (early adopter, radiology)

Passes.

1. **A failure in a tool he trusts.** The Goh trial (model alone strong,
   physicians with it no better) and the drafted note's contradictory plan.
   Present.
2. **The thing to do tomorrow.** The quiz-me prompt in Part B step 3. Present.
3. **Treated as an evaluator, not a user to be restrained.** The decision
   figure has a "Cyborg, iterate freely" quadrant, and the chapter says
   neither mode is the correct one. Present.
4. **His specialty.** The deskilling row of @tbl-perils names reading your own
   images; the measured deskilling study is GI, not radiology, and the chapter
   says so by describing the study. *Open:* no radiology-specific deskilling
   citation exists that I could verify this session; the appraisal chapter
   already notes most cleared devices are radiology.

## Priya (clinician-in-waiting, emergency medicine)

Passes on the practical rules; her scenario is the chapter's.

1. **Skip the mechanism.** "The practical rules, in the order you will need
   them" is written for her and says so in its first sentence. Present.
2. **Scenario she recognizes.** The attending sending an AI-drafted reply
   unread is taken from her persona and returns in the rules section.
   Present.
3. **Accountability and documentation.** "You sign the note" names the
   signer; the documentation rule carries a `[VERIFY]` for the institution's
   attestation language because it genuinely varies. *Open by design:* the
   flag stays until the course institution's policy is confirmed.
4. **One sentence for a co-intern.** "If you could not have written it, do not
   sign it." Present, and in the Check.

## Jordan (instructional designer)

1. **Objectives map.** 1 → Part A step 1; 2 → Part A peril column and the
   Check row "a peril per row"; 3 → Part B; 4 → Check rows "the two findings"
   and "two techniques"; 5 → Part A step 2 and its Check row; 6 → standing
   question. All six map. No fix needed.
2. **Time estimate.** Stated as 30 read + 25 listen + 30 do + 5 = 90. The
   file is ~5,700 words but roughly 1,900 of those are exercise templates,
   tables, and raw HTML; the prose a student reads is about 3,600 words,
   which is 18–25 minutes at a technical reading pace plus three figures.
   The 30-minute reading estimate is honest for a median reader. The podcast
   is 48 minutes and the chapter says to budget 25 and which parts to listen
   for. No fix needed; flag if the author wants the chapter shorter.
3. **Standalone.** The Goh trial is restated in full rather than assumed from
   the appraisal chapter. A student who skipped that chapter can follow.
4. **Accessibility.** The SVG carries `role="img"` and an `aria-label`; the
   mermaid figure has a caption; the two styled blocks are real text, not
   images. The podcast is free and hosted by NEJM. *Open:* I did not confirm
   whether the episode page carries a transcript.
5. **Scenario returns.** The standing question puts the reader back at
   6:10 a.m. with the senior resident waiting. Present.
6. **Visuals earn their place.** Task list: the artifact under sorting. Draft
   note: the mis-skilling specimen the prose cannot show. Bar chart: the
   trial's three numbers at a glance. Decision figure: the rule as a
   procedure. None is decoration.

## Dr. Okafor (borrowing educator)

1. **Run the Do alone.** Part A and B are fully specified; the answer key
   gives defensible verdicts per row with the reasoning to listen for.
   Present.
2. **Mechanism restatable.** Centaur/cyborg and the three perils are each one
   sentence and one example. Present.
3. **Institution-specific parts marked.** The attestation rule carries a
   `[VERIFY]`; the validation column is explicitly "at my institution"; the
   chapter now says the validation column will look different in twelve
   months and the sorting will not (*added*).
4. **Images reusable.** All four visuals are drawn (CSS/HTML), redrawn from
   published numbers (SVG), or generated (mermaid). No NC, SA, or fair-use
   material in this chapter; an adopter can reuse everything.
5. **Question students will ask that the chapter does not answer:** "Which
   tool does my hospital actually have, and is it validated?" The chapter
   tells them to ask in week one and accepts "don't know" in the grid; it
   cannot answer for another institution.

## Dr. Lindqvist (clinical ethicist) — reads last

1. **No PHI.** Stated in the practical rules and again in the Do warning;
   Part A needs no tool; Part B uses a fictional patient supplied by the
   chapter. Institutional logins are explicitly said not to change the rule.
   No activity would fail an IRB sniff test.
2. **Does the patient know?** The portal-reply case names the attending's two
   decisions (not reading, not telling) and sends the disclosure question to
   the patient-communication chapter. The drafted progress note and the
   discharge summary are not disclosed to the patient in the scenario, and
   the chapter does not claim they should or should not be. *Open by design:*
   that is the patient-communication chapter's content; here the student is
   asked to write, per task, to whom they would disclose.
3. **Contested presented as settled.** The draft said "that argument ended
   before you matched." That presents "should you use AI" as closed, which it
   is not for every task. *Fixed:* now reads that the student will meet the
   tools regardless and that "never" is an available verdict per line.
4. **Who bears the cost.** The decision figure's first question is "who is
   harmed"; the drafted-note passage says a wrong plan goes to a patient.
   Named.
5. **Illustrative artifacts.** The task list and the drafted note are both
   labeled as illustrative and not any real product's output; the note
   header imitates generic EHR chrome, not a named vendor's. The faculty
   quotations are attributed to real named faculty of this course and are
   now labeled as quoted from the course's prior session (*added*), so the
   attribution is traceable.
6. **Course's own AI use.** Logged in `AI-LEDGER.md` with this commit.

## Citations

Eight keys, all resolved at render. Six PMIDs retrieved and read this
session: 40834302 (Abdulnour, NEJM 2025; metadata only, no abstract in
PubMed), 39466245 and 39910272 (Goh 2024, 2025), 40560616 (Bastani 2025),
40816301 (Budzyń 2025), 38506805 (Garcia 2024). Two DOIs not in PubMed,
checked against Crossref: 10.1111/bjet.13544 (Fan et al., BJET 2025) and
10.2139/ssrn.4573321 (Dell'Acqua et al., 2023). Every number in the prose
was checked against the retrieved abstract. The Abdulnour claims (three
perils, adaptive expertise, supervisors' lesser expertise, DEFT-AI) rest on
the module's and the deck's summary of the paper, not on the abstract, which
PubMed does not carry; the author has the paper.

## Open `[VERIFY]` flags

1. Institutional attestation and disclosure language for AI-drafted notes and
   portal replies.
2. The Kasparov freestyle-chess anecdote (not a peer-reviewed source).
3. Length of the alternative podcast episode (Rodman, June 2024).
