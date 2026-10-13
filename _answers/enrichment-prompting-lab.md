# Answer key: enrichment-prompting-lab

Not rendered. Instructor notes for the course director (Monday's talk, office
hours). Revised 2026-10-08 for the week 2 core version of
the chapter ("Prompting lab: getting good answers, and knowing their limits"):
Part A (build a prompt that works) is new, Part B checks one claim instead of
two, and reference scoring was dropped from the Do. Revised 2026-10-12: every
run is in a Temporary Chat or a chat outside the course project; Step 5 (check
the claim) is "if you have time", and otherwise done later in the week on the
student's own work; the template is kept in the student's ChatGPT project and
the one-sentence finding goes in journal question 2; objective 5 (the two
trials) moved to Go deeper and is no longer assessed.

## The opening case (Sam's phone)

Fictional. 44F, three weeks post ankle ORIF, pleuritic chest pain, HR 108, calf
asymmetry. Wells criteria for PE: surgery within four weeks (1.5), HR >100
(1.5), clinical signs of DVT (3), PE most likely diagnosis (3) gives 9; even
without the judgement item she is 6, "PE likely" on the dichotomised score. A
negative D-dimer does not exclude PE at that pretest probability; go to CT
pulmonary angiography (or V/Q if contrast contraindicated). The strategy of
clinical model plus D-dimer to exclude PE without imaging was validated in the
*low* pretest-probability group: Wells et al., Ann Intern Med 2001.
pmid:11453709. The two chat answers are composed by the author for the chapter,
not transcripts of any tool; both say so in the block.

Newer pathways do not change this: on the two-level Wells score she is "PE
likely" (over 4), and at 44 the age-adjusted D-dimer cutoff is the standard
one. (The YEARS algorithm is not mentioned in the chapter; a student who raises
it is right that it handles D-dimer differently, and the point about checking
the claim the plan depends on still stands.)

The one sentence to add to Sam's prompt: "Where the case lacks information you
would need, say what is missing instead of assuming it." In Monday's
demonstration, run Sam's structured prompt with and without that sentence. The
chapter's chat answers are composed, not observed; nobody has yet run this
case through the institutional tools. ChatGPT Edu can search the web, so it
may well get the D-dimer right. Run it before the talk and use whichever
result you get; if it gets it right, ask the room how they would know.

## Part A: build a prompt that works

No single right answer; the student's own topic. What to look for:

- The template has all five parts. The fifth line is about what to do with
  gaps or disagreement ("say so instead of picking one"), not "be accurate".
- One line per change. Expected observations (from the design, not yet
  observed in a class run; record what students actually see): changing the audience to patients
  shortens sentences and drops jargon; changing to an attending adds evidence
  and nuance; format changes length and order but rarely content; deleting the
  last line usually removes hedges and statements about guideline
  disagreement, so the answer reads more confident without being better
  sourced. Accept any honest observation, including "nothing changed".
- The kept template is the deliverable. A student who keeps it and names a
  task to reuse it on has met objective 1.

## The four traps

| Case | Trap kind | Discriminating feature | Full-marks answer | Sources |
|---|---|---|---|---|
| A | Critical omission | Pregnancy status, hormonal contraception or other oestrogen, immobilisation, personal or family VTE history are all absent | Names at least two missing items as needed before choosing D-dimer vs imaging; does not compute a Wells score or declare "low risk" from what is given | Wells 2001, pmid:11453709 (model + D-dimer validated in low-probability patients) |
| B | Common answer is wrong | Oxybutynin (strongly anticholinergic, Beers list) started 12 days before onset; no local urinary symptoms; dipstick alone does not establish infection in this population | New anticholinergic ahead of or beside the dipstick; observation and other causes rather than reflex antibiotics, per IDSA 2019 for delirium without local GU symptoms | IDSA ASB guideline 2019, pmid:31506700 (summary) and pmid:30895288 (full); AGS Beers Criteria 2023, pmid:37139824. Recommendation V.1 (Nicolle 2019, pmid:30895288): for older patients with functional or cognitive impairment, bacteriuria, and delirium, without local genitourinary symptoms or systemic signs, the guideline recommends assessment for other causes and careful observation rather than antibiotics (strong recommendation, very low-quality evidence; read from the IDSA guideline page 2026-09-08). |
| C | Buried interactions | Clarithromycin (strong CYP3A4 inhibitor) with simvastatin 40 mg; amiodarone with simvastatin >20 mg; clarithromycin raising apixaban exposure; amiodarone + clarithromycin QT | Statin-macrolide interaction named and acted on (hold or switch statin for the course, or stop the macrolide); apixaban perioperative interruption plan; metformin plan is expected, not the trap | AHA scientific statement on statin drug interactions, Wiggins et al. Circulation 2016, pmid:27754879 (abstract not available via tool). Simvastatin label (DailyMed, Accord, Jan 2022): section 4 contraindicates strong CYP3A4 inhibitors including clarithromycin; sections 2 and 7 cap the dose at 20 mg/day with amiodarone. |
| D | Genuinely ambiguous | Onset after prednisone 60 mg; family history of bipolar; weekend cannabis | Both corticosteroid-induced mania/psychosis and first-episode bipolar I with psychotic features stay on the list; cannabis-induced named and excluded by tox screen and timeline; distinguishing test is course after steroid withdrawal; safety plan independent of which diagnosis | Warrington & Bostwick, Mayo Clin Proc 2006, pmid:17036562 (psychiatric effects of corticosteroids: common, dose-related, early, resolve with withdrawal) |

## Scoring notes

- Organisation 0 to 5: ranked; for-and-against per entry; explicit next step;
  readable format; statement of what is missing. The bare answer will usually
  score 1 to 2; the structured 4 to 5. That gap is expected and is not the finding.
- Trap 2/1/0: the finding is the *difference* between the two trap scores.
  The four cases have not yet been run through the institutional tools (see
  Instructor prep). The expectation from the trap design, to be checked
  against real transcripts from ChatGPT Edu with web search available: the
  uncertainty line should help Case A
  most (an omission trap is what the line targets), Case B sometimes, and
  Cases C and D least, since structure does not make a model read a medication
  list more carefully; it makes it format what it read. Record what actually
  happened here after the first run.
- References are no longer scored in this version of the Do (the appraisal
  chapter is a week 2 menu item). If a student scores them anyway, use the
  appraisal chapter's 2/1/0 scale (McLaughlin et al. 2026, pmid:42232526) and
  do not accept "looked real".
- A reply that asks for the missing information instead of committing to a
  plan (increasingly the default on the bare prompt) scores as the trap caught
  for Case A, and as organisation point 5 for any case. It is not a
  non-answer; it is the behaviour the uncertainty line is trying to produce.
- Step 5 verdict (one claim, the one the plan depends on; optional in class,
  or done later on the student's own work and reported in journal question 2):
  accept *not addressed* as a legitimate verdict. A common student error is to check a
  claim against a second chatbot; that scores as unchecked. A good choice of
  claim is the one that would change the next step: for Case A, any "low risk"
  or "D-dimer first"; for B, "start antibiotics"; for C, any statement about
  simvastatin dose or the macrolide; for D, a single named diagnosis.

## Objectives to activities

| Objective | Where assessed |
|---|---|
| 1 A kept five-part template | Part A and "What you keep" (saved in the ChatGPT project); Check row 1; "What this changes" part 2 |
| 2 One part changed at a time | Part A; Check row 2 |
| 3 Bare vs structured, organisation vs correctness | Part B Steps 2 to 4 and the one-sentence finding (journal question 2); Check row 3 |
| 4 The claim the plan depends on, checked against a source | Part B Step 5 if time, or the student's own work that week (journal question 2); Check row 4; "What this changes" part 1 |

The two randomized trials (Goh 2024, pmid:39466245; Goh 2025, pmid:39910272)
are now in Go deeper and not assessed. If a student brings them up: the first
found no benefit for physicians given the model, while the model alone scored
16 points higher in an exploratory comparison; the second found physicians
with GPT-4 scored 6.5 points higher on management, about the same as the
model alone, and took about two minutes longer per case.

## "What this changes for you", part 1 (Sam)

A strong answer to Sam, in three sentences: the second answer is better
organised (ranked, for and against, a next step per row) and that is worth
keeping; but a negative D-dimer only excludes PE at low pretest probability,
and this patient (surgery within four weeks, HR over 100, signs of DVT) is not
low on Wells, so the next step is imaging; next time add "where the case lacks
information you would need, say what is missing instead of assuming it", and
check the claim the plan depends on (here, in MDCalc) before it goes in the
note. Extra credit for noting that Sam typed a real patient into a phone,
which the course rule forbids.

## Instructor prep

Run all four cases through ChatGPT Edu and Copilot, bare and structured, each
in a Temporary Chat (or a chat outside any project), and keep the transcripts.
Edu can search the web, so expect some traps to be caught on the bare prompt.
If a tool catches every trap, say so and let the result stand; the chapter's
"one case is not a study" note covers it. Students open the traps callout
themselves after both runs.

Not yet checked in Edu: that Temporary Chat is available in the CU Edu
workspace, and the easiest way to keep a template in a project (a chat or a
file).
