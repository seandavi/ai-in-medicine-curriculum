# Answer key — enrichment-agentic-coding

Not rendered. Fed to the tutor; used by the course director, including for
the week 3 Wednesday talk if it is "building a small tool live". Revised
2026-10-12: MELD values corrected, Goodell 2025 restated, Part C optional,
the four VIBE-HI questions restated from the paper, no live-session steps.

## Opening scenario arithmetic

Illustrative patient: bilirubin 3.4, INR 1.9, creatinine 1.6, sodium 134,
dialysis twice in the past week. MELD (Kamath 2001 coefficients, UNOS
constant 6.43, values <1 set to 1, creatinine capped at 4.0 and set to 4.0
with dialysis) and MELD-Na in the OPTN version used for US allocation from
2016 to 2023 (MELD(i) + 1.32 × (137 − Na) − 0.033 × MELD(i) × (137 − Na);
sodium bounded 125–137; sodium term applied only when MELD > 11; these rules
are set out in Kim et al. 2021, pmid:34481845, PMC full text):

- Without the dialysis rule (creatinine 1.6): MELD 22.7 → MELD-Na 24.
- With the dialysis rule (creatinine 4.0): MELD 31.5 → MELD-Na 32.

Recomputed in Python 2026-10-12: MELD 22.74 and 31.51; MELD-Na 24.41 and
32.34, rounding to 24 and 32. The 2026-09-07 version of this key gave MELD
24.4 and 32.0, which were wrong. Kim 2008's own formula (MELD − Na − 0.025 ×
MELD × (140 − Na) + 140, sodium 125–140) would give 25 and 33 for the same
patient: a live example of the version failure, if a student asks why their
tool and MDCalc differ by one point.

An earlier draft used sodium
118 and creatinine 2.1 with both rules missing; the two omissions cancelled to
the same score, which is itself a good tutor example of why one test case is
not enough. The 118 sodium is kept in the prose as the *next* patient's
problem.

The scenario's threshold is the team's own referral threshold and is
deliberately not stated. If a student asks, MELD 3.0 (Kim et al.,
Gastroenterology 2021, pmid:34481845) replaced MELD-Na for US allocation in
July 2023, which is the "version" failure in the chapter's table. MELD 3.0
adds sex and albumin and lowers the creatinine cap to 3.0.

## Part B — the edges, by score, with the expected direction

| Score | Edge the model tends to miss | What the paper / MDCalc does |
|---|---|---|
| CHA₂DS₂-VASc | Both age bands checkable at once | Mutually exclusive; 65–74 = 1, ≥75 = 2, never 3 |
| CHA₂DS₂-VASc | "Female sex" point | Lip 2010 scores female sex as 1. The 2023 ACC/AHA/ACCP/HRS guideline (pmid:38033089) keeps the point but sets the treatment threshold one higher for women: anticoagulation recommended at ≥2 in men and ≥3 in women (Class 1), reasonable at 1 in men and 2 in women (Class 2a); it calls female sex a risk modifier. ESC 2024 (pmid:39210723) dropped the point (CHA₂DS₂-VA): anticoagulation recommended at ≥2 (Class I), should be considered at 1 (Class IIa). A tool must say which it implements. `[VERIFY: ESC 2024 rows read from secondary summaries, not the guideline text, 2026-09-08]` |
| CHA₂DS₂-VASc | Annual stroke risk % | The percentages most tools print are from Friberg 2012 (Swedish cohort), not Lip 2010 (Euro Heart Survey); the two tables differ. Source must be named. |
| Wells PE | Rounding of 1.5-point items; version | Three-tier (<2 / 2–6 / >6) and two-tier ("PE likely" >4) both published; the tool must name one |
| MELD-Na | Floors and caps | Bili, INR, creatinine <1 → 1; creatinine >4 → 4; dialysis ≥2/week → 4; Na bounded 125–137 in the OPTN version (Kim 2008 used 125–140); MELD-Na only when MELD > 11; final score capped at 40 |
| qSOFA | GCS cutoff | Any GCS <15 scores; SBP ≤100 (not <100); RR ≥22 |
| PHQ-9 | Item 9 | Any non-zero response on self-harm needs a direct prompt to the user, not a colour band; bands 5/10/15/20 |
| Fleischner 2017 | Exclusions | Not for patients <35, immunocompromised, or with known cancer; solid vs subsolid, single vs multiple, size bands at 6 and 8 mm, risk category |

## Goodell 2025, what it does and does not show

For the tutor, if a student asks why the chapter says writing code does not
make a model reliable (pmid:40097720, PMC11914283, read 2026-10-12):

- Exploratory phase: web ChatGPT (GPT-4, November 2023), which already had a
  code interpreter and web search, on 48 MDCalc calculators; 140 of 212
  scorable answers correct (66%). Of 82 errors, 31 were assignment errors
  (wrong points for a criterion) and 13 incorrect criteria (missed or
  invented), so more than half were rule errors.
- Focused phase: the ten hardest calculators, 1,000 new templated vignettes,
  GPT-4o and LLaMa 3.1 70B by API. GPT-4o base 36% correct (64% wrong); code
  interpreter added 9.9 points (about 54% wrong); RAG with MDCalc's
  instructions added 41 points; RAG plus code interpreter 82%; OpenMedCalc
  (task-specific calculators the authors wrote and a physician validated) 95%
  (4.8% wrong, the abstract's 13-fold drop).
- So the 13-fold drop is not from the model writing code, and the
  one-in-three figure and the 64 percent figure come from different test sets
  and different models.

## Part C (optional) — where it sits

Expected elements:

- **A study aid now** because it is used by its builder, on invented inputs,
  with a banner saying so; nobody's care depends on it.
- **The four VIBE-HI questions** (pmid:42564266, PMC full text, Table 3), in
  the paper's terms: data sensitivity (is PHI involved?); clinical-decision
  proximity (does the output inform a treatment decision?); user autonomy (can
  the clinician independently verify the output?); scale of impact
  (individual or institution). The tier is set by the worst answer. A student
  tool is Green on all four; the resident's bookmarked tool is not.
- **What would have to change**: any of real patient data, a treatment
  decision, users who cannot check the output, or reach beyond the builder.
- **Background, no longer asked in the chapter**: the non-device CDS
  criterion that the clinician can independently review the basis for the
  recommendation. A
  page showing inputs, rule, and citation can be reviewed; a bare number
  cannot. FDA CDS guidance, issued 29 January 2026, Criterion 4: software
  "intended for the purpose of enabling an HCP to independently review the
  basis for the recommendations that such software presents so that it is not
  the intent that the HCP rely primarily on any of such recommendations". The
  guidance adds that a time-critical function does not meet Criterion 4, and
  that inputs, rule, and validation should be shown in plain language.

## The one sentence

Must contain a verb meaning *compare against an outside source*: "check it
against MDCalc", "run three cases through it and the paper", "validate it
before anyone else uses it". "Be careful" fails.

## Standing question — what a strong answer contains

- To the coordinator: her number stands; the team's tool omits the dialysis
  rule; the patient's score, and the referral that depends on it, are
  recalculated from a checked source today.
- To the resident: the tool is good work and it needs three things before it
  goes back on the workroom machines: the missing rules, a named version with
  a citation on screen, and a written comparison against MDCalc on a fixed
  set of cases including dialysis and low sodium.
- The bookmark comes down until that is done. Saying so to a senior is the
  uncomfortable part, and is the point.
- Documentation: the score in the note comes from MDCalc or the paper, with
  the source named.

## Worked-example provenance

**The chapter's worked examples are expected behaviour, not a recorded run.** Two
live runs of the starter prompt (CHA₂DS₂-VASc and MELD-Na, Claude, no tools,
2026-09-07) were started for this chapter and did not return in time to be
read, so the callout was written from the known edge failures in the table
above and labelled as constructed. Author to do: run both prompts in the CU
ChatGPT Edu workspace with a university login (the starter prompt now ends
"Open it in canvas so I can preview it"), confirm the canvas preview, read
the code, and replace the two "expected" paragraphs with what actually came
back, model and date recorded, keeping whichever expected failures did *not*
occur as a note (the "numbers move" point). Then the footnoted VERIFY flag in
the Do's "Which tool" box can be removed.

## Instructor prep

- If the week 3 Wednesday talk is "building a small tool live", run the
  CHA₂DS₂-VASc and MELD-Na prompts in ChatGPT Edu that morning and confirm
  the canvas preview button appears. If it does not, canvas code execution
  is off in the workspace; show the save-as-`calc.html` fallback instead.
- Have MDCalc open for all six scores.
- A good closing question for volunteers: "here's my tool, here's the one
  thing I'd fix before trusting it."
