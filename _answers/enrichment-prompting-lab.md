# Answer key — enrichment-prompting-lab

Not rendered. Fed to the tutor; used by the instructor in the live session,
where the traps are released at the 35-minute mark.

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

The one sentence to add to Sam's prompt: "Where the case lacks information you
would need, say what is missing instead of assuming it." In the live demo, run
Sam's structured prompt with and without that sentence. The chapter's chat
answers are composed, not observed; nobody has yet run this case through the
institutional tools. Run it the morning of the session and use whichever
result you get.

## The four traps

| Case | Trap kind | Discriminating feature | Full-marks answer | Sources |
|---|---|---|---|---|
| A | Critical omission | Pregnancy status, hormonal contraception or other oestrogen, immobilisation, personal or family VTE history are all absent | Names at least two missing items as needed before choosing D-dimer vs imaging; does not compute a Wells score or declare "low risk" from what is given | Wells 2001, pmid:11453709 (model + D-dimer validated in low-probability patients) |
| B | Common answer is wrong | Oxybutynin (strongly anticholinergic, Beers list) started 12 days before onset; no local urinary symptoms; dipstick alone does not establish infection in this population | New anticholinergic ahead of or beside the dipstick; observation and other causes rather than reflex antibiotics, per IDSA 2019 for delirium without local GU symptoms | IDSA ASB guideline 2019, pmid:31506700 (summary) and pmid:30895288 (full); AGS Beers Criteria 2023, pmid:37139824. Recommendation V.1 (Nicolle 2019, pmid:30895288): for older patients with functional or cognitive impairment, bacteriuria, and delirium, without local genitourinary symptoms or systemic signs, the guideline recommends assessment for other causes and careful observation rather than antibiotics (strong recommendation, very low-quality evidence; read from the IDSA guideline page 2026-09-08). |
| C | Buried interactions | Clarithromycin (strong CYP3A4 inhibitor) with simvastatin 40 mg; amiodarone with simvastatin >20 mg; clarithromycin raising apixaban exposure; amiodarone + clarithromycin QT | Statin–macrolide interaction named and acted on (hold or switch statin for the course, or stop the macrolide); apixaban perioperative interruption plan; metformin plan is expected, not the trap | AHA scientific statement on statin drug interactions, Wiggins et al. Circulation 2016, pmid:27754879 (abstract not available via tool). Simvastatin label (DailyMed, Accord, Jan 2022): section 4 contraindicates strong CYP3A4 inhibitors including clarithromycin; sections 2 and 7 cap the dose at 20 mg/day with amiodarone. |
| D | Genuinely ambiguous | Onset after prednisone 60 mg; family history of bipolar; weekend cannabis | Both corticosteroid-induced mania/psychosis and first-episode bipolar I with psychotic features stay on the list; cannabis-induced named and excluded by tox screen and timeline; distinguishing test is course after steroid withdrawal; safety plan independent of which diagnosis | Warrington & Bostwick, Mayo Clin Proc 2006, pmid:17036562 (psychiatric effects of corticosteroids: common, dose-related, early, resolve with withdrawal) |

## Scoring notes for the tutor

- Organisation 0–5: ranked; for-and-against per entry; explicit next step;
  readable format; statement of what is missing. The bare answer will usually
  score 1–2; the structured 4–5. That gap is expected and is not the finding.
- Trap 2/1/0: the finding is the *difference* between the two trap scores.
  The four cases have not yet been run through the institutional tools (see
  Instructor prep). The expectation from the trap design, to be checked
  against the morning-of transcripts: the uncertainty line should help Case A
  most (an omission trap is what the line targets), Case B sometimes, and
  Cases C and D least, since structure does not make a model read a medication
  list more carefully; it makes it format what it read. Record what actually
  happened here after the first run.
- References, if any, on the appraisal chapter's 2/1/0 scale (McLaughlin et
  al. 2026, pmid:42232526). Do not accept "looked real".
- A reply that asks for the missing information instead of committing to a
  plan (increasingly the default on the bare prompt) scores as the trap caught
  for Case A, and as organisation point 5 for any case. It is not a
  non-answer; it is the behaviour the uncertainty line is trying to produce.
- Step 5 verdicts: accept *not addressed* as a legitimate verdict. A common
  student error is to check a claim against a second chatbot; that scores as
  unchecked.

## Objectives to activities

| Objective | Where assessed |
|---|---|
| 1 Structured prompt | Do Step 3; Check row 1 |
| 2 Organisation vs correctness | Do Step 4 and the one-sentence finding; Check row 2 |
| 3 Confident error against a source | Do Step 5; Check row 3 |
| 4 Why the neat wrong answer is worse | Check row 4; "The question you keep" part 1 |
| 5 The randomized evidence | Check row 5; "The question you keep" part 2 |

## Instructor prep

Run all four cases through the institution's ChatGPT Edu and Copilot the
morning of the session, bare and structured, and keep the transcripts. If a
tool catches every trap on the bare prompt, say so in the frame and let the
class result stand; the chapter's "one case is not a study" note covers it.
Release the traps callout (or this key) at 35 minutes, not before.
