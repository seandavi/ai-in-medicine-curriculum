# Book review and improvement plan, 12 October 2026

**Status: applied the same day.** The author made the decisions below on
12 October, and the fixes landed as PRs #104 (front door), #105 (week 2 core
and appraisal), #106 (week 1), #107 (week 3), #108 (bias and grounding),
#109 (week 4) and a cleanup PR. Line numbers below refer to `main` at 370d1cf,
before the fixes. What is still open is at the end.

Reviewer: Claude (Opus 5.5) in Claude Code, with seven read-only subagents (one per
week's chapters, one for the course pages and appendices, one for the 12 October
session transcript, read locally for what students were told; nothing from
it is stored in the repo). The review itself changed nothing in the repo.

**Verified by me:** prose word counts, em-dashes (none), `fig-alt` (all images),
relative links (none broken), `[VERIFY]` count (12 in chapters), the phone-width
render of the foundations chapter, repo visibility (private), the AI-LEDGER row
publishing the plan chapter to students, and five citation findings against
PubMed (Goodell, Windecker vs Wu, Waldock) and the web (NotebookLM rename).
**Reported by subagents, not re-checked by me:** everything else below. Line
numbers are from `main` at 370d1cf and will drift.

## Where the book stands

The 8 October independent review (`research/independent-review-2026-10-08.md`)
drove the refocus. Since then the four core chapters were reworked (prompting
lab promoted, patient communication and ethics trimmed, centaur dropped,
plan-your-learning added). The menu chapters were not touched: no short path,
no honest Do times, no success-first order in appraisal, bias, RAG, workforce,
environment.

What is strong and must survive edits: the writing standard (no em-dashes,
plain words, scenario first and returned to), the patient chapter's three
sentences and Part B role-play, foundations' eGFR scenario and sliders and the
"Nothing checks" and "does and does not mean" callouts, the prompting lab's
Sam case and five-part template, agentic coding's build-then-break, ethics'
"write your plan before you read the draft", the workforce four-questions
figure, the environment bottle trace, the patient-information page.

## Cross-cutting findings

1. **The book is already partly visible.** The plan chapter was published in
   Canvas on 12 October (AI-LEDGER row 30). Its sidebar reaches the syllabus,
   journal, open labs and instructors pages. "Before the book is re-shown"
   means before Thursday for the front door.
2. **The repo link 404s.** `_quarto.yml:79` `repo-url` puts a GitHub link on
   every page; the repo is private.
3. **Citations that do not say what the chapter says** (section B). The render
   test proves a key resolves, not that it supports the sentence. Several errors
   trace upstream to `modules/` and `research/`, so fixing the chapter alone
   lets them come back.
4. **Time.** The syllabus promises about 1 hour per core chapter. Core
   subtitles say 70 to 90 minutes; realistic totals are 75 to 110. Menu
   chapters understate by 20 to 40 minutes.
5. **Rules stated four ways.** The syllabus's four rules; plan-your-learning
   L325 ("unless your hospital has approved that tool"); "any free chatbot also
   works" in ethics L25, patient-communication L24, prompting lab L21;
   appraisal L413-416 grounding the rule in "consumer tools have no BAA" when
   students use Edu, which has one. About 1,000 words of patient-information
   callouts across six chapters and two open labs.
6. **Never run in the course's tool.** Plan chapter (Projects, account label,
   downloads), prompting lab cases (memory and Projects may contaminate the
   bare-vs-structured comparison), agentic canvas preview, NotebookLM (now
   Gemini Notebook; the specimen answer came from Claude), and the answer keys'
   predicted failures (from Claude with web search off; Edu searches the web,
   so several "the model will fail" Do steps may not fail).
7. **Failure-first Do steps remain** in foundations Part B ("produce a
   hallucination on purpose"), appraisal Part A, RAG Step 2 ("You are looking
   for a 1"), workforce Part A ("the model failing is the expected result").
8. **Small slips repeated across pages:** "in three months" (index:19,
   foundations:80, agentic:110, prompting:84; residency is about nine months
   away), "live session" (bias:567, foundations:35), a tutor that "will grade
   your reasons" (appraisal:663, index:132-140; that direction was dropped),
   authoring notes visible to students (rag:339-342, workforce:124-126,
   147-148, 407, 540-544), "AIM-n" codes in student-facing subtitles and prose.
9. **The first phone screen** of every chapter is the title, competency codes,
   a minutes figure that disagrees with the syllabus, and dense objectives. The
   summary is at the bottom (issue #89).
10. **Content duplicated by copy, so it drifts.** The five journal questions
    live in five places (journal page, three Canvas assignments, plan chapter
    template and extra questions, instructors page). The rules live in three
    wordings.
11. **The clickable self-check** (`theme/self-check.html`) is used only on the
    patient-information page. Chapter Checks are written rubrics.

## A. Before Thursday 15 October

Front door (students can reach these now):

- [ ] `_quarto.yml:79` remove `repo-url` while the repo is private.
- [ ] `syllabus.qmd`: a "This week" box first (talks Mon to Wed 10 a.m.;
      Thursday hands-on, bring ChatGPT Edu; read How these systems work;
      journal due Thursday night in Canvas; Friday signup in Canvas). Say the
      chapters are a guide, not a requirement (#89; matches "suggestions, not
      assignments" said on 12 October). Week 1 section before the weeks 2 to 4
      table.
- [ ] `syllabus.qmd:31-32` one hours sentence (the next sentence's arithmetic
      gives 7.5 to 9.5, not 8 to 10). `:38` an honest core-chapter time.
- [ ] `syllabus.qmd:107` plan chapter out of the week 1 Menu column; label it
      "Thursday session".
- [ ] `index.qmd:30` delete "not optional"; `:19` "three months".
- [ ] `open-labs.qmd:20-21` and `about.qmd:56` remove the class vote.
- [ ] `patient-information.qmd:221` quiz answer says only Edu is covered; L95
      says Copilot is too.
- [ ] Syllabus matches what was said on 12 October (needs decisions, see D):
      guest-talk expectation, 30 October group, pass/fail vs ungraded, late
      work is fine, journals are private unless shared.

Plan your four weeks (the only chapter students can open):

- [ ] L325-327 replace rule 1 with the syllabus's four rules, word for word
      (Lindqvist fails the chapter until this is fixed).
- [ ] Add Learn it with AI (2 to 4 h a week) to the course list (L176-198) and
      the plan prompt (L229-233); link it at L90. Journal Q1 asks how the week
      connects to the week 1 goals, so the plan must include it.
- [ ] Mark steps 1, 3 and 4 as in-session; template and sharing "after, before
      tonight's journal". Add "use a laptop" and "no Projects? start a chat
      named AI in Medicine".
- [ ] L319-321 delete the two extra journal questions, or make them the
      answers to journal Q1 and Q3.
- [ ] L273 Discord #show-and-tell only if invites go out by Wednesday.
- [ ] Author dry run in Edu: account label, Projects, search links, file
      download (ledger row 32 already asks for this).

How these systems work (students read it this week):

- [ ] Watch: swap the 27-minute video for the deck's 8-minute 3Blue1Brown
      (LPZh9BOjkQs); the long one to Go deeper. Saves 19 minutes, more than
      all word cuts together.
- [ ] L3, L28-32 honest time; L35 "Wednesday's talk" not "the live session".
- [ ] Facts: L294 the 2009 equation *with* the race term overestimated by 3.7
      (without it, underestimated by 7.1; Inker 2021 abstract); L546 Pastucha's
      best version "scored 51 percent on reference accuracy", not "about half
      of its references fully right"; L558-559 "ChatGPT Edu cannot see the
      chart; some EHR-built tools can"; L368 past tense ("in 2021"); L80.
- [ ] L735 retitle Part B "Ask, then check", one sentence saying most first
      answers are right and the job is to find which parts.
- [ ] Add the nested-circles figure (`images/ai-nested-circles.svg`, in the
      deck) and about 80 words, so the chapter covers the syllabus's "AI to ML
      to DL to LLMs" and L949's "named the neural network" becomes true.
- [ ] Collapse history table (L289-305), COVID X-rays (L378-431) and
      MYCIN/Watson (L564-580) into one "If you have more time" callout.
- [ ] Author reads the COVID, sliders and Ask-it-to-check sections (ledger row
      34 says they are unread).

## B. Citation fixes (one PR, all chapters, plus upstream)

- [ ] **FDA device numbers under the wrong paper.** "About half reported
      clinical performance data, a quarter none, under a third sex-specific"
      are Windecker et al. 2025, 903 devices to August 2024 (55.9%, 24.1%,
      28.7%; pmid:40305017, verified). The chapters cite Wu et al. 2021 (130
      summaries; pmid:33820998, no abstract in PubMed). appraisal:298-301,
      ethics:641-645, bias:117-121 and :377. Upstream:
      `modules/core-appraisal.md:300`, `research/enrichment-activities.md:1374`.
- [ ] **Waldock 2025** (pmid:39915801, verified): the five wrong answers were
      GPT-3.5's own errors, not "deliberately wrong"; 56% is the median share
      of students who judged each answer correctly. prompting:85-89,
      appraisal:372.
- [ ] **Goodell 2025** (pmid:40097720, verified on the abstract): the 13-fold
      drop (64% to 4.8%) came from purpose-built calculator tools
      (OpenMedCalc), not from the model writing code; the subagent reports the
      code-interpreter arm cut GPT errors only from 63.9% to 54.0% (full text,
      Table 3). "One in three" (48 tasks) and "64%" are different test sets.
      agentic:197-206 and Summary :581-583. The real finding supports "check
      against MDCalc" better.
- [ ] **Agentic MELD:** L33-34, 41-42 call MELD-Na the ranking score; the
      chapter says MELD 3.0 replaced it in 2023. L410 credits OPTN bounds
      (125-137, MELD>11) to Kim 2008, whose abstract gives 125-140. Answer key
      L13-14 MELD values (22.7 and 31.5, not 24.4 and 32.0).
- [ ] **RAG, Vollmer** (doi 10.3390/diagnostics16152456): the specimen drops
      the abstract's own qualifier ("directionally" in strong models), so
      "is not what the paper says" (L51-52) overstates; "six models with and
      without retrieval" (L247, 258) is wrong (the six included a Custom GPT
      and ConsensusGPT). "Table 6" stated as fact, never checked.
- [ ] **Bias:** Obermeyer 4.8 vs 3.8 drawn in a figure but from press
      coverage, not the abstract; the 34-device preprint says 1 passed the
      "anticipated" criteria, the chapter says "passed the draft FDA
      standard" (L179-180); "every well-documented case" (L98, L573) vs the
      chapter's own dermatology data-gap row; "rule" for 2013 guidance (L183).
- [ ] **Appraisal:** Summary L697-698 "a quarter to two-thirds" vs the
      chapter's own 2.1%, 8.8%, 94%; claim 4 (n=45) labelled "large
      observational"; L626-628 "8,581 clinicians offered" and "every earlier
      pre/post study" overstate pmid:41920565; answer key Lukac now published
      (pmid:41497288).
- [ ] **Prompting lab:** L123-131 second-language advice goes further than
      pmid:42232526 (persona and wording changed together; second-language
      writers not tested). Same at appraisal:225-232.
- [ ] **Workforce:** L174 "observers" was one trained observer
      (pmid:23763878); L336-337 "time saved became visits" states cause for an
      association; the 5.8% not found in pmid:41511775 full text.
- [ ] **Environment:** L298-302 the Ceres page has neither "two-thirds" nor
      Newton County (likely Bloomberg May 2025, NYT July 2025); L362-366 the
      80% paper's authors include the device maker's staff, unstated; L338
      "not correlated" vs "not highly correlated"; L354 "further trained" for
      a general chat model.
- [ ] **Ethics:** L207 "automation bias is a property of tired people" has no
      source; L51-55 leaves out the 94.7% of notes with no significant error
      (pmid:41996389).
- [ ] **Process fix:** a claim check per chapter. For every key, the sentence
      and the abstract side by side; an agent flags mismatches; a person
      decides. Record it in the ledger. The render stays the existence test.

## C. Week 2, before Monday 19 October

Prompting lab (core):

- [ ] L253, 265, 321 "use a Temporary Chat, or a chat outside your course
      project" so memory and the week 1 project do not leak into the bare run;
      test in Edu.
- [ ] L20-21 drop "any free chatbot also works"; L84 "By next July".
- [ ] L3, L19 "about an hour" plus a one-line short path; say it goes with
      Monday's talk (after it or instead of it); link Learn it with AI.
- [ ] L436-462 keep the template in the project; the one-sentence finding
      goes in journal Q2.
- [ ] Move "What the trials show", objective 5 and its Check row to Go deeper;
      trim L112-121; drop the Mermaid figure that repeats the callout.
- [ ] Step 5 "if you have time".

Appraisal (menu):

- [ ] L663-664 delete the tutor sentence; L413-416 "Course rule: made-up
      questions only" plus the link; L29-31 signup and personal-account lines;
      L3 honest time.
- [ ] Part A success first: one Edu run with search on (most references will
      check out), then the contrast; three references, not five; a "showed
      sources?" column; drop the OpenEvidence row (it requires health
      professional verification).
- [ ] Cuts (about 670 words, 35 numbers): L369-383, L196-202, HTI-1 callout
      to ethics, L317-322, Kohane to Go deeper, the decorative photo L76-80.

Bias (menu):

- [ ] Stale: L524 "what you hand in", L567-568 "live session collects these
      in chat", L379 "assigned in the same week", L116 assumes appraisal.
- [ ] L531-533 "check whether yours names the proxy" (current models
      often do).
- [ ] Part B as a Learn-it-with-AI step: Edu proposes three proxy cases in
      the student's specialty, flags each paper to verify; the student
      confirms one in PubMed (journal Q2) and writes the row (journal Q5).
- [ ] Cuts (about 1,050 words, 30 numbers): the proxy table that repeats
      Part B's list, FDA detail L169-183, L148-151, L362-381, L400-405.

Grounding in real sources (menu):

- [ ] Delete the author note L339-342 (visible to students).
- [ ] L108-109, L126, L609, L622 point to foundations sections that were cut
      (context window, lost in the middle); L431 "your write-up"; L84 "AIM-1".
- [ ] One line on the rename to Gemini Notebook (16 July 2026) and the
      compute-based free limits (from 2 September 2026); L28-29 "50 chat
      questions a day" is stale.
- [ ] Run the Do once in Gemini Notebook with the four PMC sources; close the
      L425 flag; replace the Claude-made specimen or say plainly it is not
      NotebookLM output (Lindqvist).
- [ ] Step 2 success first: "make me a one-page journal-club brief", check
      three citations, correct one; the corrected brief is what they keep.

## D. Week 3, before Monday 26 October

Talking to patients (core; no Monday talk this week):

- [ ] L82-83, L390-394, L429 Friday role-play lines that no longer match;
      answer key L4-7, L133-142 (cards, votes).
- [ ] Send Christina Olson the Part B persona and observer list (L333-360) as
      a three-person breakout script for her 26 October workshop.
- [ ] "The spine" to "the three sentences" (L226-229, 301, 308, 403).
- [ ] L390 "paste these into journal question 4".
- [ ] Issue #92: an optional Part A item ("She read that AI broke out of a
      test. Is the phone safe?"), answered with the three sentences and the
      refusal table. The alignment debate goes to the week 4 talk.
- [ ] Trim about 600 words (L87-122 to the figure plus three sentences,
      L195-204, L265-270 prose, L72-78, Summary); say about 60 minutes.

Agentic coding (menu):

- [ ] Fix the Goodell claim (section B).
- [ ] Author runs the starter prompt in Edu; add "Open it in canvas so I can
      preview it" to the prompt; remove the L380 flag; replace the worked
      example L469-503 with the real run.
- [ ] Remove "live session" lines (L389-390, 505-506); Do 60, total about 90;
      Part C optional; Copilot student line L628 ("most need a paid plan").
- [ ] Cuts (about 1,400 words): "Two names" L163-182 (closes a flag), L91-108,
      L242-272, device section to the rule plus a link, L308-337 to one line.
- [ ] "Build first" link near the top so Elena does not read 36 minutes
      before building.

Scribe open lab: drop the vote line (L19-21); define the two error types in
the lab; use Mrs. Park, not Mr. Alvarez, in the self-check.

## E. Week 4, before Monday 2 November

Ethics (core):

- [ ] L24-26 require the university account; L554 point to the week 4 "what
      you will keep" piece.
- [ ] Cuts (about 730 words, 25 numbers): "Who the tool fails" L255-278 to Go
      deeper, Jabbour L189-208 to Go deeper, trials L282-302 to two sentences,
      L390-393, L119-126 to one sentence. Subtitle "about 60 minutes".
- [ ] Re-check on 2 November: FDA CDS (29 January 2026 agrees with agentic
      coding), HTI-5, EU dates, device count, malpractice verdict; update the
      "as of" dates (L366, 675, 763, 832-834). Add one state-law sentence
      (Colorado's AI Act status is unconfirmed) marked `[VERIFY]`.
- [ ] Move the attestation advice into the main text after L146; Check rows
      for objectives 4 and 6; define "proxies fail" at L315.

Workforce (menu):

- [ ] Delete L265-266 ("Groups working through this"), authoring notes
      (L124-126, 147-148, 407, 542-544), L319 second sentence; rename Part C.
- [ ] Part A success first (Edu applies the four questions to your specialty
      and finds time-and-motion studies; you check one); re-run in Edu and
      update the answer key.
- [ ] Move about 750 words and 50 numbers to Go deeper; "about 60 minutes,
      video optional"; L594 point to the week 4 piece.

Environment (menu):

- [ ] L481-482 "question 2" of a journal that week 4 does not have; L60 and
      L172 assume the appraisal chapter; L241 "Forty students" (49).
- [ ] xAI L303-313: drop the turbine count and permit claim, give the filing
      and "no ruling as of [date]".
- [ ] Part A success first; cuts (about 450 words); split L342-349 (73
      words), L260-265, L115-119.

## F. After the course (next offering)

- Issue #89 in full: a short "In short" box at the top of every chapter (the
  summary moved up), AIM codes out of student-facing subtitles.
- Single-source the rules and journal questions with Quarto includes
  (`{{< include >}}`), and institution facts with `_variables.yml` (#66).
- One line plus a link in place of each patient-information callout.
- Preface to about 400 words; coverage table to the competency-frameworks
  appendix; tutor section out.
- Instructors and about appendices brought in line with fall 2026.
- Answer keys: re-run predicted failures in Edu with search on; remove
  live-session, card and vote references.
- One clickable self-check per chapter Check, for the phone reader.
- Write up the success-shaped Idea labs (board question, handout, build a
  tool), which can also fill "Watch and do".
- Day 1 and day 20 confidence survey (independent review, after-course #7);
  journal Q4 and Q5 answers are the free version of this.

## Decisions (the author, 12 October)

1. **Patient information rule unchanged:** made-up patients only in course
   activities, in any account, including ChatGPT Edu.
2. **Attendance:** about 3 hours a week of sessions plus the Friday group; no
   separate guest-talk quota.
3. **Friday 30 October** stays "bring your clinical stories", without
   scenario cards.
4. **Grading:** pass/fail.
5. **Week 4 piece:** missing the Friday 6 November group is fine; submitting
   the piece is enough.
6. **Unhiding:** week by week in Canvas; the book stays online meanwhile.
7. **Direction:** positive outcomes are the primary lesson (success first in
   every Do), and cutting is welcome: longer is not better.

## Still open after the fixes

Things only the author can do, collected from the PRs' "Author to do" lists.

Before Thursday 15 October:

- Dry-run the plan chapter in ChatGPT Edu: the account label, Projects,
  search links, file download.
- Read the syllabus expectations and hours, and the foundations sections the
  ledger marks unread (COVID X-rays, sliders, Ask it to check, new Part B).
- Update the three Canvas journal assignments to match the journal page
  (question 2 wording, privacy and late lines, week 4 fallback).
- Confirm handout notes are posted at talks.seandavis.net; confirm whether
  Discord invites go out (the plan chapter mentions it conditionally).
- Decide whether Watch and do counts toward the 3 hours (the syllabus says
  optional).

Before Monday 19 October (week 2):

- Prompting lab: confirm Temporary Chat exists in Edu and that a chat outside
  a project does not pick up memory; run Sam's case.
- Appraisal: find the web-search option in Edu; run Part A and one Part B
  case; confirm STAT's 79 percent (claim 10) or reword it.
- Grounding: run the Do in Gemini Notebook with the four PMC sources (ideally
  a CU account), close the remaining `[VERIFY]`, replace the specimen if the
  run gives a clear example.
- Bias: run the Part B prompt in Edu for two or three specialties.
- Foundations: run Parts B and C in Edu; update the answer key.

Before Monday 26 October (week 3):

- Agentic coding: run the starter prompt in Edu with a CU login; if canvas
  preview appears, remove the footnoted `[VERIFY]` and replace the worked
  example with the real run.
- Patient chapter: run Part A and the Part B persona in Edu. Forward the
  three-person breakout script (in PR #107's body) to Christina Olson if
  wanted.

Before Monday 2 November (week 4):

- Re-check the dated facts in ethics: FDA CDS guidance date, HTI-5 (still a
  proposal), EU AI Act dates, the FDA device count, malpractice verdicts, the
  state-law sentence (AB 3030; Colorado's AI Act status), and the xAI docket in
  environment.
- Run the Part A prompts (and ethics Part B) in Edu; update the answer keys.

After the course (section F above): single-source the rules and journal
questions with `{{< include >}}`, `_variables.yml` for institution facts (#66),
the preface coverage table to the competency-frameworks appendix, answer keys
re-run in Edu, one clickable self-check per chapter, the Idea labs written up,
and a day-1 and day-20 confidence survey.
