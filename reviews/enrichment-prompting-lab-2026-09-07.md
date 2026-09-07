# Review: enrichment-prompting-lab chapter, 2026-09-07

Six-persona self-review of `chapters/enrichment-prompting-lab.qmd` per
`curriculum/personas.md`, Elena first, Lindqvist last. Findings are what the
first draft got wrong; each is followed by the fix applied in the committed
version. Reviewed by the AI assistant; author to confirm.

## Elena (avoider, surgery, free tier, ESL) — reads first

1. **Opening assumed the reader knew what "prompting" was.** First draft used
   "prompt" in the scenario's second sentence. *Fix:* the scenario now
   describes Sam typing the question "the way you would say it out loud" and
   then "properly", and the terms prompting and language model are defined in
   the paragraph after the chat block, once the reader already has the case.
2. **Her fluency question was answered only by cross-reference.** *Fix:* a
   callout in The idea ("If English is not your first language") restates the
   register finding from the appraisal chapter, defines register, and tells
   her which row of the scaffold controls it. It is framed as a lever she
   holds, not a handicap.
3. **Case C reads as a pharmacology exam.** Surgery is her match, and the
   surgical case is the one with the most drug names. *Fix:* the case now
   states the question for the model ("what needs attention before this
   operation?") so she is not expected to know what to ask, and the trap
   callout names the interaction in plain words before the enzyme.
4. **Her skepticism is the right answer twice**: the scenario (Sam's better
   answer is wrong) and the record's third outcome (bare answer catches the
   trap, structured misses it), which the chapter calls "the best result of
   all". Kept.

Passes. Ten-minute way in: Steps 1–3 on an institutional account with nothing
to sign up for.

## Marcus (early adopter, radiology)

1. **"I could get this from the model itself."** The scaffold, yes. *Fix:* the
   three studies in which structure did not buy accuracy (Yang, Wang, Luo) and
   the model-alone results of both Goh trials are the content he cannot get by
   asking the model, and are now in The idea with numbers rather than
   summarised.
2. **No concrete failure of his current habit.** *Fix:* the opening chat pair
   is exactly his habit (structured prompt, table, into the note) producing a
   wrong next step, with the mechanism named. The D-dimer error was chosen
   because it is subtle enough that he might not have caught it either.
3. **Nothing to do tomorrow.** *Fix:* the optional last block of the record
   (delete the uncertainty line and rerun) is a two-minute experiment he will
   actually run, and the standing question asks for a named move, not a
   caution.
4. **Radiology hook.** Not added; the chapter has no imaging content and
   forcing one would be decoration. He gets Case A's imaging-versus-D-dimer
   decision instead.

## Priya (clinician-in-waiting, emergency medicine)

1. **Skip the mechanism, what do I do?** *Fix:* the "One sentence" callout
   and the Check row 4 are the ward-level rule; Step 5 is the concrete
   verification habit with three named free sources (MDCalc, PubMed guideline
   recipe, DailyMed).
2. **Who is accountable and what do I document?** *Fix:* the standing
   question now asks what she will check "before any chatbot-drafted plan goes
   into a note with your name on it". Documentation policy itself is pointed
   to the ethics and regulation chapter in the PHI callout rather than
   re-taught here.
3. **Scenario she recognises:** night float, co-intern, phone. Case A is her
   specialty. Kept.

Her one sentence for a co-intern: "A structured prompt improves how an answer
is organised, not whether it is right."

## Jordan (instructional designer)

1. **Time estimate.** First draft said 75 minutes and assigned a 48-minute
   podcast plus a deck. *Fix:* the Time note now states 20 + 20 + 30 + 5 and
   says explicitly that 75 holds only if the listener stops at twenty minutes,
   and that finishing the episode makes it closer to 100. The Watch block
   repeats "the first twenty minutes are enough".
2. **Objective 5 had no activity.** *Fix:* Check row 5 assesses it directly,
   and the standing question's second part requires the student to use the
   trial result. Objectives-to-activities table added to the answer key.
3. **Objective 4 was assessed only by the standing question.** *Fix:* Check
   row 4 added, requiring the mechanism to be named.
4. **Alt text and captions.** The redrawn figure has `fig-alt` and a credit
   naming the source paper; the mermaid figure has a caption; the chat pair is
   HTML text, so it is screen-reader legible as written.
5. **Can the Check be self-applied?** The traps callout gives the
   discriminating features in the chapter; sources stay in the key. Yes.
6. **Scenario returns:** in the standing question and in the last summary
   bullet. Yes.
7. **Cognitive load.** Four vignettes in a row is heavy. Each is in its own
   callout so the student can read one and skip three; the pick-by-specialty
   instruction comes first.

## Dr. Okafor (borrowing educator)

1. **Can I run the Do alone?** Yes: the prompts are verbatim, the traps are in
   the chapter, the scoring is two tables, and the answer key has an instructor
   prep note (run all four cases the morning of; release traps at 35 minutes).
2. **Can I restate the mechanism?** *Fix:* the "Two different things a prompt
   can change" section now separates organisation from correctness in two
   plain paragraphs before any study is cited, and the mermaid figure is the
   one-slide version.
3. **What will students ask that the chapter does not answer?** "Which prompt
   *does* improve accuracy, then?" The chapter's honest answer is "the
   uncertainty line, sometimes, and it depends on the model"; the Go deeper
   list includes the counter-case (clickBrick) so the adopter is not caught
   out by a student who has read it.
4. **Staleness.** Every number is dated by its citation, the "one case is not
   a study" note says outputs move, and the answer key tells the instructor to
   rerun the cases the morning of the session.
5. **Image licences.** The only raster image is redrawn from published
   estimates and is the course's own; the chat pair and the diagram are code.
   Nothing here stops at this course.
6. **Tools named with a fallback.** ChatGPT Edu or Copilot; either works; the
   verification sources are all free and public.

## Dr. Lindqvist (clinical ethicist) — reads last

1. **PHI.** The Do uses four fictional cases, says so, forbids substitution,
   and states that institutional accounts do not change the rule. The opening
   scenario's patient is fictional and the chapter says the chat answers are
   composed. Passes.
2. **Does the patient in the scenario know an AI is in the room?** Sam asked a
   chatbot about her case on a personal phone at 2:40 a.m. The first draft
   passed over this. *Fix:* not added as a paragraph, per the persona's own
   warning about preachiness; but the PHI callout now says explicitly that
   what Sam did with a real patient's details is the thing the callout
   forbids, and the ethics chapter pointer is there for the disclosure
   question. The vignette-only rule keeps the student on the right side of it.
   *Author to decide whether one more sentence in the scenario is wanted.*
3. **When the tool is wrong, who bears the cost?** Named: the student who
   would have signed (Why this matters), the patient with the delayed CT
   (scenario), and, via the register callout, the patient or ESL clinician
   whose phrasing gets the worse answer.
4. **Contested question presented as settled?** The chapter's thesis
   ("structure does not reliably improve correctness") is stated with three
   supporting studies and one counter-case in Go deeper, and the Goh trials
   are reported with confidence intervals in both directions. The NEJM AI
   automation-bias trial is flagged `[VERIFY]` rather than cited.
5. **Could the illustrative artifact be mistaken for a real company's
   material?** The chat panes carry no product name or logo and say
   "composed for this chapter; not a transcript" in each pane.
6. **Course's own AI use disclosed?** AI-LEDGER row added, stating that the
   chat answers were written by the model and that citations were checked by
   tool against abstracts, not by the author reading each paper.

No activity would fail an IRB sniff test.

## Verification status

- 13 `@pmid:` keys in the chapter, every one retrieved and abstract-read this
  session; 6 further PMIDs in the answer key, same standard.
- `[VERIFY]` flags left in the chapter: the NEJM AI automation-bias RCT (not in
  PubMed); the Rodman episode duration; the simvastatin label claims (AHA
  statement abstract unavailable via tool). One more in the answer key on the
  exact wording of the IDSA delirium recommendation.
- Podcast episode date and length confirmed from the NEJM AI Grand Rounds RSS
  feed (15 Oct 2025; 2,897 s).

## Action list, by priority (all applied unless marked)

1. Define prompting and language model after the scenario, not before.
2. Register callout for Elena; scaffold row named as the lever.
3. Three "structure did not buy accuracy" studies with numbers; both Goh
   trials with intervals; redrawn figure.
4. Honest time statement with the podcast stop point.
5. Check rows for objectives 4 and 5; objectives table in the key.
6. Named verification sources and a PubMed guideline recipe in Step 5.
7. Optional uncertainty-line ablation on the record.
8. *Open, author's call:* one sentence in the scenario on whether Sam's
   patient knows her case went into a phone.
