# Answer key — enrichment-agentic-coding

Not rendered. Fed to the tutor; used by the instructor in the live session.

## Opening scenario arithmetic

Illustrative patient: bilirubin 3.4, INR 1.9, creatinine 1.6, sodium 134,
dialysis twice in the past week. MELD (Kamath 2001 coefficients, UNOS
constant 6.43, values <1 set to 1, creatinine capped at 4.0 and set to 4.0
with dialysis) and MELD-Na (Kim 2008; sodium bounded 125–137; sodium term
applied when MELD > 11):

- Without the dialysis rule (creatinine 1.6): MELD 24.4 → MELD-Na 24.
- With the dialysis rule (creatinine 4.0): MELD 32.0 → MELD-Na 32.

Checked in Python for this chapter (2026-09-07). An earlier draft used sodium
118 and creatinine 2.1 with both rules missing; the two omissions cancelled to
the same score, which is itself a good tutor example of why one test case is
not enough. The 118 sodium is kept in the prose as the *next* patient's
problem.

Listing thresholds vary by region and era and the scenario deliberately does
not state one; if a student asks, MELD 3.0 (Kim et al., Gastroenterology 2021)
replaced MELD-Na for US allocation in July 2023, which is the "version" failure
in the chapter's table.

## Part B — the edges, by score, with the expected direction

| Score | Edge the model tends to miss | What the paper / MDCalc does |
|---|---|---|
| CHA₂DS₂-VASc | Both age bands checkable at once | Mutually exclusive; 65–74 = 1, ≥75 = 2, never 3 |
| CHA₂DS₂-VASc | "Female sex" point | Lip 2010 scores female sex as 1. The 2023 ACC/AHA/ACCP/HRS guideline (pmid:38033089) keeps the point but sets the treatment threshold one higher for women: anticoagulation recommended at ≥2 in men and ≥3 in women (Class 1), reasonable at 1 in men and 2 in women (Class 2a); it calls female sex a risk modifier. ESC 2024 (pmid:39210723) dropped the point (CHA₂DS₂-VA): anticoagulation recommended at ≥2 (Class I), should be considered at 1 (Class IIa). A tool must say which it implements. `[VERIFY: ESC 2024 rows read from secondary summaries, not the guideline text, 2026-09-08]` |
| CHA₂DS₂-VASc | Annual stroke risk % | The percentages most tools print are from Friberg 2012 (Swedish cohort), not Lip 2010 (Euro Heart Survey); the two tables differ. Source must be named. |
| Wells PE | Rounding of 1.5-point items; version | Three-tier (<2 / 2–6 / >6) and two-tier ("PE likely" >4) both published; the tool must name one |
| MELD-Na | Floors and caps | Bili, INR, creatinine <1 → 1; creatinine >4 → 4; dialysis ≥2/week → 4; Na bounded 125–137; MELD-Na only when MELD > 11; final score capped at 40 |
| qSOFA | GCS cutoff | Any GCS <15 scores; SBP ≤100 (not <100); RR ≥22 |
| PHQ-9 | Item 9 | Any non-zero response on self-harm needs a direct prompt to the user, not a colour band; bands 5/10/15/20 |
| Fleischner 2017 | Exclusions | Not for patients <35, immunocompromised, or with known cancer; solid vs subsolid, single vs multiple, size bands at 6 and 8 mm, risk category |

## Part C — the device paragraph

Expected elements:

- **Not a device now** because it is a personal study aid, used by its builder,
  on invented inputs, with a banner saying so; nobody's care depends on it.
- **What changes the answer** (any two of the four VIBE-HI questions): real
  patient data entering it; its output changing what is done to a patient;
  users other than the builder; scale (a team, a service).
- **The criterion a bare score fails**: the non-device CDS criterion that the
  clinician can independently review the basis for the recommendation. A
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
  rule; the patient's listing status is recalculated from a checked source
  today.
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
above and labelled as constructed. Before the first cohort, run both prompts
in the institutional ChatGPT Edu workspace, read the code, and replace the
two "expected" paragraphs with what actually came back, model and date
recorded, keeping whichever expected failures did *not* occur as a note (the
"numbers move" point).

## Instructor prep

- Run the CHA₂DS₂-VASc and MELD-Na prompts in the institutional ChatGPT Edu
  workspace the morning of the session and confirm the canvas preview button
  appears. If it does not, the workspace admin has disabled canvas code
  execution; use the save-as-`calc.html` fallback for the whole class.
- Have MDCalc open for all six scores.
- The showcase question for volunteers is fixed: "here's my tool, here's the
  one thing I'd fix before trusting it."
