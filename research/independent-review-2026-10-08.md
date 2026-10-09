# Independent review: is the AI in Medicine book too much and too heavy?

Reviewer: an AI agent (Claude), asked to review independently, 8 October 2026.
Scope: the student-facing book as a student meets it (`index.qmd`, `course/`,
the 11 chapters, `appendix/open-labs.qmd`, `appendix/resources.qmd`). I did not
read the answer keys, the research or review folders, the ledger, the design
documents, or the git history.

## 1. Verdict

The concern is right about load and tone, and wrong about difficulty. The prose
is plain (Flesch-Kincaid grade 7 to 9, about 14 words a sentence), and the
stated reading times are honest. But the required path comes to about 38 to 42
hours over four weeks, the Do activities take about half again as long as
stated, and a student meets about 120 cited papers and 400 distinct numbers.
Only about 2 hours of the whole course is spent typing into a chatbot, and more
than half of that time is spent hunting for the tool's failures, so goal 3
(judgment and safety) is over-served while goal 1 (confident use) is
under-served. The two chapters that serve goal 1 best, the prompting lab and the
retrieval chapter, are marked "spare".

## 2. The numbers

### How I measured

- **Words.** A script stripped YAML, fenced code blocks (worksheets, mermaid,
  raw HTML figures), HTML comments, citation keys, URLs and markup, then counted
  words. Text inside illustrative mock-ups (chat transcripts, vendor slides) was
  kept, because students read it. "Go deeper" is excluded from the totals.
- **Reading minutes.** Prose outside the Do, Check and Go deeper sections,
  divided by 200 words a minute; the figure in brackets is 150 words a minute,
  closer to a second-language reader with technical text.
- **Stated minutes.** The chapter subtitle and its "Time." line.
- **Estimated real minutes.** Reading at 200 wpm, plus the listening the chapter
  budgets (not the full episode), plus my estimate of the Do for a first-time
  student working steadily, plus 10 minutes for the Check and the standing
  question. The Do estimates are judgment; the reasons are in section 4.
- **Hands-on AI minutes.** The stated minutes of required Do steps in which the
  student types into, or works directly with, an AI tool (chatbot, NotebookLM,
  TensorFlow Playground, the calculator they built).
- **Caution:capability.** A crude word count: caution terms (do not, never,
  wrong, error, fail, harm, risk, fabricated, hallucination, bias, worse,
  liability and similar) against capability terms (useful, helps, works, better,
  improves, benefit, saves, worth, accurate, good, well and similar), in prose
  outside Go deeper. It over-counts caution slightly, because "made up for this
  chapter" labels count as caution. Treat it as a direction, not a measure. My
  reading of tone is in section 3.
- **Flesch-Kincaid grade.** Computed with the `textstat` package on every prose
  paragraph of 30 words or more in each chapter's "How it works" section
  (11 to 31 paragraphs per chapter, 1,300 to 2,600 words). Spot checks on every
  fourth paragraph ranged from grade 3 to 17, with most between 6 and 9.
- **Citations per 1,000 words.** `@pmid:` and `@doi:` keys outside Go deeper.
  The environment and ethics chapters also cite many sources as plain links,
  which this count misses.
- **Distinct numbers.** Distinct numerals in the prose, excluding years and the
  integers 1 to 10. A rough count of how many figures a student meets.

### Chapters

| Chapter (week) | Words | Reading min @200 (@150) | Stated min | Est. real min | Hands-on AI min | Share of real time | Caution:capability | FK grade | Cites per 1,000 | Distinct numbers |
|---|---|---|---|---|---|---|---|---|---|---|
| How these systems work (1) | 5,598 | 21 (28) | 75 | 88 | 18 | 20% | 2.8 | 6.9 | 3.7 | 50 |
| Centaur or cyborg (1) | 4,854 | 20 (27) | 90 | 100 | 10 (skippable) | 10% | 2.5 | 6.6 | 2.3 | 31 |
| Critical appraisal (2) | 5,548 | 18 (24) | ~120 | 123 | 25 (about 5 typing, 20 checking in PubMed) | 20% | 1.6 | 7.5 | 3.2 | 76 |
| Bias and equity (2) | 5,077 | 21 (28) | 90 | 106 | 0 (5 optional) | 0% | 3.0 | 8.1 | 8.2 | 59 |
| Agentic coding (3) | 5,333 | 18 (24) | 75 | 98 | 35 | 36% | 2.9 | 7.7 | 3.5 | 44 |
| Talking to patients (3) | 5,507 | 22 (29) | 90 | 97 | 20 | 21% | 2.0 | 6.9 | 2.5 | 29 |
| Will AI take your job? (4, choice) | 4,833 | 20 (26) | 90 | 100 | 10 | 10% | 1.1 | 8.1 | 4.1 | 87 |
| What AI costs the planet (4, choice) | 5,131 | 21 (27) | ~60 | 87 | 5 | 6% | 1.7 | 8.8 | 2.3 | 66 |
| Ethics, liability, device line (4) | 5,777 | 25 (33) | 75 | 105 | 0 | 0% | 5.2 | 8.0 | 2.6 | 46 |
| Prompting lab (spare) | 5,204 | 16 (21) | 75 | 91 | 30 | 33% | 1.2 | 8.1 | 3.4 | 55 |
| Grounding in real sources (spare) | 5,045 | 19 (25) | ~60 | 81 | 30 | 37% | 1.7 | 6.9 | 3.7 | 52 |

Do time, stated against my estimate: foundations 20 vs 30; centaur 30 vs 45;
appraisal 45 vs 65; bias 35 vs 50; agentic 35 vs 55 (the open-labs page itself
gives 60 for the same activity); patients 35 vs 45; workforce 35 vs 50;
environment 25 vs 45; ethics 25 vs 50 (its own parts add to 30); prompting 30
vs 45; grounding 30 vs 45. On average the Do is understated by about half, and
the chapter total by about 20 percent (16 minutes). The listening budgets
assume students stop where told; the episodes run 40 to 78 minutes, and a
student who listens to the end adds 20 to 45 minutes per chapter.

### Course pages

| Page | Words | Reading min @200 | Stated | Caution:capability | FK grade |
|---|---|---|---|---|---|
| Preface (`index.qmd`) | 1,195 | 6 | none | 2.2 | 8.0 |
| Syllabus | 594 | 3 | none | 1.5 | 7.6 |
| Resource log | 712 | 4 | none | 1.6 | 5.8 |
| Patient information | 1,517 | 8 | 15 (with quiz) | 10.0 | 8.0 |
| Open labs | 1,848 | 9 | 30 to 60 per lab | 7.8 | 5.1 |
| Starter resources | 1,463 | 7 | none | 0.6 | 6.1 |

### Across the required path

- About 120 distinct cited papers in the eight required chapters (with the
  workforce chapter as the week-4 choice). Several are cited in three to five
  chapters: the Goh trial, the 130 FDA decision summaries, the five-system
  scribe study, the Price, Gerke, and Cohen framework.
- About 400 distinct numbers across the same chapters.
- The business associate agreement is explained in full in at least seven
  places, and a "No patient information, ever" callout opens every Do.
- The required path has seven chatbot sessions. Four are designed to show the
  tool failing (foundations Part B, "produce a hallucination on purpose";
  appraisal Part A, "the fabrication hunt"; workforce Part A, where "the model
  failing is the expected result"; environment Part A step 1). Two build skill
  (centaur Part B, hint-seeking and quiz; patients Part B, role-play). One does
  both (agentic coding: build it, then break it).

### Weekly totals

Assumptions: week-1 live sessions are one hour each (the syllabus does not say);
the resource log takes 2 to 3 hours for three to five resources (reading a
paper or watching a talk, then writing three sentences on each), against the
syllabus's 1 to 2; guest talks 2 hours; the optional open lab is excluded.

| Week | Chapters (est. real) | Live, required | Guest talks | Resource log or synthesis | Total, required | Syllabus says |
|---|---|---|---|---|---|---|
| 1 | 3.1 h | 4 h (Mon, Tue, Wed, Fri) | none | 2 to 3 h, due day 4 | 9 to 10 h | not stated |
| 2 | 3.8 h | 2 h (Mon, Fri) | 2 h | 2 to 3 h | 10 to 11 h | 7 to 10 h |
| 3 | 3.3 h | 2 h | 2 h | 2 to 3 h | 9 to 10 h | 7 to 10 h |
| 4 | 3.4 h | 2 h | 2 h | 2 to 3 h (synthesis and talk) | 9.5 to 10.5 h | 7 to 10 h |
| **Course** | **13.6 h** | **10 h** | **6 h** | **8 to 12 h** | **38 to 42 h** | |

What an MS4 on interview season can do: my assumption is 6 to 8 hours in a
typical week and 3 to 4 in a week with two or three interview days, with
attention fragmented across travel, pre-interview dinners, and other
coursework. If this elective is credited as a full-time block, 10 hours a week
is not much in absolute terms. But it is ungraded, Zoom-only, and running
against interviews, so in practice students will triage. The real risk is not
that they do too little; it is that they spend the time they do give on
reading rather than on using the tools.

## 3. Goal by goal

### Goal 1: confidence and real experience using chatbots well

Served weakly on the required path.

- **Volume.** About 120 minutes of required hands-on AI time in about 40 hours,
  roughly 5 percent of the course and 15 percent of chapter time. Week 1 has 4
  hours of live talks (welcome, history, AI to LLMs) and no scheduled hands-on
  time; the Wednesday talk covers the same ground as the foundations chapter.
- **Kind of reps.** Of about 120 minutes, roughly 40 build confidence:
  centaur Part B (a hint-seeking prompt and a three-question quiz, 10 min),
  agentic coding Part A (a working calculator in about ten minutes, 12 min),
  and the patient role-play (20 min). The rest is designed to make the tool fail
  in front of the student. A student whose first three chatbot exercises are
  "produce a hallucination", "the fabrication hunt", and "the model failing is
  the expected result" learns to distrust the tool before learning to use it.
- **What is missing.** Everyday productive uses that build a habit: explaining a
  concept at your level, making practice questions, summarising a document you
  supply, drafting and revising a letter or handout, plain-language rewriting,
  comparing two tools, iterating on an answer you do not like. The open-labs
  page lists several of these ("Write your own board question", "A handout your
  patient can read", "Build the tool you wish existed") but as "Idea", not
  written. Nothing uses the most timely task an MS4 has this month: preparing
  for residency interviews.
- **Where it is strong.** The centaur chapter's six techniques and Who / Where /
  What pattern; the prompting lab's five-part prompt and "say what is missing"
  line; the retrieval chapter's notebook workflow; the agentic build; and the
  resource log's reading companion, which gives the bot less to do each week.
  That last is the best confidence-building design in the book, and it is
  optional and placed at the bottom of a page.
- **Placement.** The prompting lab is the only chapter whose subject is how to
  get good answers, and it is spare. Its title, "the same wrong answer, better
  organised", leads with the limitation.

### Goal 2: confidence discussing AI with colleagues and patients

Served well for patients, and in writing only for colleagues.

- **Patients.** The patient-communication chapter is the strongest in the book
  for this goal: the three-sentence spine (what it did, what a person did, who
  is responsible), "say what is right first", the table of what a patient can
  refuse, permission to say "I don't know how that system works", and a
  20-minute role-play with a hidden detail and an observer rubric. A student who
  does it can hold the conversation.
- **Colleagues.** Nearly every chapter ends by sending the student back to a
  colleague with a sentence to say: the attending about the eGFR (foundations),
  the senior resident about drafting notes (centaur), the chief resident about
  the vendor slide (appraisal), the attending on rounds about the oximeter
  (bias), the coordinator and the resident who built the calculator (agentic),
  the uncle at dinner (workforce), the resident and medical director at huddle
  (environment), Sam at 2:40 a.m. (prompting). That is about nine colleague
  conversations, all written alone, none spoken. The Friday small groups could
  be the place to practise, but the syllabus does not say what happens there
  beyond "the week's questions".
- **Balance.** A student finishes with many more talking points about failure
  than about benefit. The book contains real successes (the model alone scored
  16 points above physicians; the management trial's 6.5-point gain; inbox
  drafts reducing burden; retrieval cutting hallucination from 42 to 4 percent;
  the tethered-cord podcast; NotebookLM raising accuracy from 68 to 91 percent;
  radiology's growing workforce), but almost every one is qualified in the next
  sentence. An attending who asks "so what is it actually good for?" would get a
  thinner answer than one who asks "what can go wrong?".
- **A scheduling gap.** The patient chapter describes a live session with three
  rounds of role-play and six scenario cards. The syllabus has no such session.

### Goal 3: judging AI claims and knowing the safety rules

Served thoroughly, arguably more than the goals need.

- The three rules (no patient information, verify before it counts, you sign the
  note) are stated in the preface, the syllabus, and every chapter, and the
  patient-information page explains them clearly with a good six-question
  self-check. A student will not miss them.
- Appraisal, bias, ethics, and both week-4 choices are mainly goal-3 chapters,
  and the cautions appear in every other chapter too. The tone is explanatory
  rather than scolding: the book usually says why (the mechanism of a made-up
  citation, the proxy, the business associate agreement). That is to its credit.
- The ethics chapter carries the most legal and regulatory detail (FDA's four
  criteria, PCCP, HTI-1 and HTI-5, the EU AI Act timetable, malpractice
  elements, insurers, the Elsa episode) and has no AI tool use. Its caution
  ratio (5.2) is the highest in the book.

### Tone, overall

On balance a student comes away more careful than confident. Six of the nine
required opening scenarios are harms or near-harms (a misleading eGFR, an
unread AI draft sent to a patient, an AI-sourced reference, occult hypoxemia,
a patient left unlisted by a resident's calculator, a stroke after a scribe
error). The workforce and environment chapters are the exceptions: both end in
reassurance with numbers (radiology is growing; one person's chatbot use is
negligible). The centaur chapter is the best balanced, quoting one faculty
member who asks whether avoiding AI is really an option and another who says
"we should be scared".

## 4. Too heavy?

Yes, moderately, and not in the way the director may fear.

**Not too hard.** Reading level is grade 7 to 9, sentences average 13 to 16
words, terms are defined on first use, and the stated reading times match 200
words a minute almost exactly. A second-language reader at 150 words a minute
adds 5 to 8 minutes per chapter. That is fine.

**Too long, by about a third.**

- Each chapter is 4,800 to 5,800 words before Go deeper, and the "How it works"
  sections alone run 1,600 to 3,500 words (8 to 18 minutes).
- The Do is understated by about half. The largest gaps: ethics (two
  primary-source hunts plus a four-part legal analysis in "25 minutes"),
  environment (three sources, unit conversions, a PubMed search and a
  denominator in "25"), agentic coding (build, three cases checked against two
  sources each, a comprehension test and a device paragraph in "35"), and
  appraisal (ten references each searched in PubMed three ways in "25").
- Every chapter asks for several written products: a worksheet, a record, a
  Check against a rubric of six to nine rows, and a written standing question.
  In an ungraded course, students will skip these first.
- The weekly load is about 9 to 11 hours against my estimate of 6 to 8
  available in a typical interview-season week. Cutting about a third of the
  chapter time and 1 hour from the resource log would bring it to 7 to 8 hours.

**Too weighted toward caution.** Roughly two-thirds of hands-on time is spent
finding failures. The fix is not to remove the cautions but to change the order:
success first, then verification as part of a working routine.

**Where the weight sits, heaviest first.**

1. Ethics, liability, and the device line: most words, most legal detail, no
   tool use, and a closing question that repeats the centaur chapter's.
2. Critical appraisal: the Do (ten references) and 76 distinct numbers.
3. Bias and equity: highest citation density (8.2 per 1,000 words), entirely
   about harm, no required tool use. Important, and not a chatbot chapter.
4. Workforce: 87 distinct numbers, the most in the book; most could go to Go
   deeper without losing the argument.

## 5. Recommendations

Ranked by impact per hour of effort within each group.

### Before Monday, October 12 (small, safe changes)

1. **Add a "short path" table to the syllabus (about 1 hour; highest impact).**
   One row per chapter naming what to read when time is short (about 45 to 60
   minutes), with the rest marked "if you have time". Suggested short paths:
   - *How these systems work*: the scenario; "A formula learned from data";
     "Why performance on data it has seen tells you nothing"; "From tables to
     words" through "What this does and does not mean"; Do Part B. Skip the
     eGFR history table, the context-window section, Part A, and the
     MYCIN/Watson callout.
   - *Centaur or cyborg*: "Two ways to work with a machine"; "The learners'
     study, and six techniques"; "Who, where, what"; Do Part B; the closing
     question. Part A Step 1 only, four of the eight tasks including rows 1 and 2.
   - *Critical appraisal*: "Three things that can be wrong"; "Cleared is not
     validated"; Do Part A with three references per prompt instead of five.
     Part B optional.
   - *Bias and equity*: the scenario; "Case two: cost standing in for need";
     "The study that complicates the bedside answer"; Do Part A only.
   - *Agentic coding*: the scenario; "Three ways the tool you just built is
     wrong"; Do Parts A and B.
   - *Talking to patients*: all of it. It is the chapter that most serves goal 2.
   - *Workforce* or *environment*: the scenario, the first "How it works"
     subsection, and Part A.
   - *Ethics*: the scenario; "How a scribe turns a conversation into a note";
     "Four boxes"; "The note, the patient, and the contract"; the closing
     question. Mark "Where a tool becomes a medical device", "A model that
     changes", "Rules elsewhere", the insurer callout and the HTI-5 callout as
     optional. Part A: one question, not two.
2. **Make part of week 1 live time hands-on (1 to 2 hours to prepare).** The
   Wednesday talk (AI to ML to deep learning to LLMs) covers the foundations
   chapter's material. Give 30 minutes of it, or of Monday, to everyone signing
   in to ChatGPT Edu and doing three things that work: "explain [a concept you
   are studying] to me at my level, then quiz me", the centaur chapter's
   hint-seeking prompt, and "rewrite this public handout at a sixth-grade
   reading level". Then one verification step. Students leave week 1 having
   succeeded with the tool before they are asked to break it.
3. **Lighten the resource log (15 minutes).** Change "three to five resources"
   to "two or three" for weeks 1 to 3, and allow one or two in week 1, which is
   due on day 4 of the course. Move the reading companion prompts from the
   bottom of the page to a short "try this" box near the top.
4. **Let students take the prompting lab in place of one chapter (30 minutes).**
   Add a syllabus line: a student new to chatbots may swap the prompting lab for
   the week-2 or week-3 chapter of their choice (not the patient chapter).
   Retitle it "Prompting lab: getting better answers, and knowing their limits".
   The content does not need to change.
5. **Give the Friday small groups a spoken-practice slot (30 minutes).** Add one
   sentence to the syllabus and four scenario cards: a skeptical attending asks
   whether you used ChatGPT for your presentation; a co-intern pasted a real
   patient into a personal account; a patient asks whether the scribe is safe;
   an interviewer asks "what do you think about AI in medicine?". Ten minutes in
   pairs, using the patient chapter's spine. This also answers the scheduling
   gap for the patient chapter's role-play.
6. **Fix the open-labs table (10 minutes).** Mark "The patient who talks back"
   as Ready and link it to the patient chapter's Part B, which is the full lab.
   Correct "Same question, three tools": the prompting lab runs one case twice
   in one tool. Put the patient lab on the first vote.
7. **Fill student-facing placeholders (15 minutes).** The submission link on the
   syllabus, "due [day/time]" on the resource log, and the vote link on the
   open-labs page. The canvas and NotebookLM checks flagged `[VERIFY]` in the
   agentic and grounding chapters need a person to run them before weeks 3 and
   2 respectively.
8. **Correct the stated Do times where the gap is largest (30 minutes).** Either
   say 45 to 50 minutes for ethics, environment, agentic coding and appraisal,
   or cut the steps as in recommendation 1. Students trust a book whose times
   are right.

### After this offering

1. **Write a required "Using it well" chapter for week 1 (high impact, about a
   week of work).** Built on success: six everyday tasks done well (explain and
   quiz, summarise a document you supply, draft and revise, plain-language
   rewrite and back-translation, compare two tools on one question, mock
   residency interview with feedback), each ending in something the student
   keeps, and each with one verification habit built in. Fold in the centaur
   chapter's techniques and the prompting lab's five-part prompt. End with a
   one-page personal workflow card.
2. **Reorder the hands-on sequence so success comes first.** Keep the failure
   demonstrations but move them after a working routine exists. Concretely:
   foundations Part B becomes "ask, then check one fact" rather than "produce a
   hallucination on purpose"; appraisal Part A starts with a search-first tool
   producing references that check out, then a short fabrication contrast.
   Target: at least half of required tool time ends in a usable product.
3. **Merge or cut duplication.** The centaur chapter's closing question ("which
   part of clinical judgment will you not hand over") and the ethics chapter's
   are nearly the same; the Polish deskilling study, the Goh trials, Jabbour,
   the 130 FDA summaries, the register finding and the five-system scribe study
   each appear in two to five chapters. Keep the chapters stand-alone, but make
   each repeat one sentence and a link. Replace the eleven patient-information
   callouts (about 120 words each) with one line and the link to the page.
4. **Set a length budget.** About 3,000 to 3,500 words of reading prose per
   chapter, and no more than about 25 distinct numbers in the main text. Move
   the rest of the numbers to Go deeper. The workforce, appraisal, environment
   and bias chapters would shrink most.
5. **Promote two spare chapters into the core sequence.** For example: week 1
   foundations (shortened) and "Using it well"; week 2 appraisal and grounding
   (they share the 2/1/0 scale and the register finding); week 3 patients and
   agentic coding; week 4 a merged centaur-and-ethics chapter, with bias as a
   required week-2 or week-4 option so AIM-3 stays a main subject.
6. **Write up the "Idea" open labs that build confidence.** "Write your own board
   question", "A handout your patient can read", and "Build the tool you wish
   existed" are all success-shaped and need no new evidence base.
7. **Measure the goals.** A two-minute survey on day 1 and day 20: "How
   confident are you using a chatbot for X?" and "How confident are you
   answering a colleague who asks Y?" on a five-point scale. Without it, the
   next review is guessing too.

## 6. Keep

- **The patient-communication chapter**, especially the three-sentence spine,
  "say what is right first", the refusal table, and the role-play prompt with
  the hidden detail and the observer score. It is the best thing in the book.
- **The centaur chapter's practical core**: centaur and cyborg as two ways of
  working, the six techniques, Who / Where / What, the hint-seeking prompt with
  the quiz, and the draft-versus-write pair in the task grid.
- **Agentic coding's build-then-break**, including the starter prompt that puts
  the "educational prototype" banner in before the tool exists.
- **The resource log's reading companion** that fades from "the bot leads" to
  "no help". Excellent design; just move it up the page.
- **The patient-information page** and its self-check. Clear, specific, and
  stricter than the law for stated reasons.
- **The three rules**, stated the same way everywhere.
- **The writing standard**: plain sentences, terms defined on first use,
  scenario first and returning at the end, illustrative mock-ups labelled as
  illustrative, and honest `[VERIFY]` flags instead of guessed citations.
- **The "What this does and does not mean" callout** in the foundations
  chapter. It is the most balanced paragraph in the book and could be the model
  for the rest.
- **The scribe open lab** ("Hear it, draft it, check it"). Concrete, timely,
  and directly tied to what interns will meet.
- **The workforce and environment chapters' proportion**: both reach a
  reassuring, evidence-based conclusion for the individual student.

## 7. Limits of this review

- One reviewer, an AI model, reading source files, not the rendered site.
  Collapsed callouts, figures, and layout may read differently on screen.
- I did not run any exercise in ChatGPT Edu, Copilot, NotebookLM, or the
  Playground. My "realistic" Do times are judgment, not observation; real times
  will vary widely with a student's experience.
- The caution:capability ratio is a word count with a hand-made list; it is a
  direction, not a measure. Flesch-Kincaid uses syllables and sentence length
  and does not capture density of new concepts or numbers, which is where the
  load really is.
- The weekly capacity of an MS4 in interview season is an assumption. If the
  elective is credited as full-time and students are expected to give it 20 or
  more hours a week, the load conclusion weakens, though the composition
  conclusion (little hands-on time, most of it failure-hunting) does not.
- I did not check citations, links, or statistics against their sources.
- I did not read the design documents, the answer keys, the instructor
  appendix, or what the live sessions and guest talks contain. Live sessions may
  already supply hands-on practice and spoken conversation practice that the
  book does not show.
- No student data. The best test of this review is to ask the 49 students in
  week 2 what they skipped and why.
