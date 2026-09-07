# Answer key — enrichment-workforce-economics

Not rendered. Fed to the tutor; used by the instructor in the live session.

## Part A — grading the model

There is no fixed answer; the expected pattern (checked 2026-09-07 with
Claude, claude-fable-5-1, and to be re-run before each cohort) is:

- All four factors *mentioned* in some form; liability is the one most often
  missing.
- Zero checkable sources on the first prompt. A fraction, if given, is
  unsourced.
- On the follow-up, the model either declines to name a study or names one.
  For radiology the correct answer is Dhanoa et al., JACR 2013 (pmid:23763878),
  36.4%. For other specialties, see the search recipe below; the tutor should
  check any named study in PubMed exactly as the student is asked to.

Grade: a student who searched PubMed for the cited study and recorded the
result meets; a student who ticked "Y" on "mentioned" for all four rows
without a note per row falls short.

## Part B — the forecast

No right answer on the task or the fraction. What the tutor checks:

1. Line 1 is a *task* (protocolling, drafting the discharge summary, reading
   the ECG, triage note, pre-op risk stratification), not a job or a
   specialty.
2. Line 2 has a fraction *and* a named source or an explicit "my own estimate."
   A student who claims a study should be able to give the PMID.
3. Line 3 names one of the four factors with a reason specific to the task.

Search recipe verified 2026-09-07 in PubMed:
`"time and motion studies"[MeSH] AND emergency physicians AND documentation`
returned 20 results; `"time and motion studies"[MeSH] AND surgeons AND (workday
OR "work day" OR tasks)` returned 24. Both are enough for a student to pick
two.

Benchmark for the debrief: radiology 36.4% image interpretation
(pmid:23763878). Most first estimates for other specialties are higher than a
time-and-motion study supports.

## Part C — BLS

As read from the *Occupational Outlook Handbook* on 2026-09-07 (2025–2035
projections; BLS revises every two years, so accept the live page over these):

| Occupation | Change | Reason (BLS wording, paraphrased) |
|---|---|---|
| Medical transcriptionists | −4% (42,000 jobs, 2025) | Speech recognition and NLP let physicians document in real time |
| Medical records specialists | +8% (200,700 jobs) | Aging population, chronic disease, coding for reimbursement; AI coding "may affect" demand |
| Health information technologists and medical registrars | +16% (42,000 jobs) | Growing volume of electronic health information; registries |

Expected explanation: transcription is one benchmarkable task (decomposition),
generalizes well (speech is speech), carries no signature, and demand is
capped by encounters. Coding and health-information work are judgment about
what a record means and what a payer will accept (fails decomposition), and
the payer–provider "bot wars" raise the volume of that work (demand). Any two
factors named correctly meets.

Who bears the cost: transcriptionists, median pay $40,410 (2025), versus
$51,140 for records specialists and $68,020 for health information
technologists. The displaced occupation is the lowest paid of the three.

## Check rows — reference answers

- **Obj. 1.** 2016: "stop training radiologists now; within five years deep
  learning will do better." 2026 primary numbers: 1,083 diagnostic radiology
  PGY-2 positions offered, 1,066 filled (98.4%), 1,741 applicants (NRMP
  Results and Data 2026, Tables 1A, 3, 7A); Neiman projection +25.7% to
  +40.3% radiologists by 2055 (pmid:39952776). Why not "early": Hinton's own
  2025 correction says he forecast a task (image analysis) as a job; the
  failure is mechanism, not timing.
- **Obj. 3.** Fenton 2007 (pmid:17409321): 429,345 mammograms, biopsy rate
  +19.7%, cancer detection unchanged, specificity 90.2→87.2%. Lehman 2015
  (pmid:26414882): no improvement on any metric; sensitivity lower with CAD
  among radiologists reading both ways.
- **Obj. 4.** UCSF (pmid:41511775): +1.81 RVUs/week (5.8%), +0.80 encounters,
  no rise in denials, 1,565 physicians. More billable output is revenue to
  the organization and cost to the payer; PHTI April 2026: system-wide costs
  not falling, bot wars = automated submission vs automated denial, volume up,
  resolution no faster.
- **Denominators.** Shrank 2019 (pmid:31589283): waste ≈25% of *total
  spending*, admin complexity one of six categories ($265.6B). Himmelstein
  2014 (pmid:25201663): 25.3% of *hospital* expenditures. Woolhandler 2003
  (pmid:12930930): $294.3B in 1999, 31.0% of expenditures *after exclusions*.

## Flags the tutor should know about

- The 38% single-site validation figure is Mousa's reading of Windecker et al.
  (pmid:40305017); it is not in that paper's abstract. Present as "reported
  by Mousa" until the full text is checked.
- The 17–27% imaging-demand projection (Neiman) was not retrieved this
  session; the supply projection (pmid:39952776) is verified.
- The year the CAD add-on payment was withdrawn (2018 in secondary sources)
  is unverified against a CMS document.
- "Bot wars" is the wording of trade coverage of PHTI's April 2026 report; the
  PHTI page summary fetched on 2026-09-07 did not contain the phrase.
- The NYT 14 May 2025 URL returns 403 to non-browser clients; the headline,
  author, and date were confirmed from a repost and two trade summaries, the
  URL itself was not opened.

## Instructor prep

Re-run the Part A prompts the morning of the session with the institutional
tool and note whether the follow-up produces a real study. Re-read the three
BLS pages; if the projection decade has changed, update @tbl-bls in the
chapter before the cohort sees it.
