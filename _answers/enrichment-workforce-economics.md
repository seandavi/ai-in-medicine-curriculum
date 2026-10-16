# Answer key — enrichment-workforce-economics

Not rendered. Fed to the tutor; used by the instructor.

## Part A — the four questions with ChatGPT

Rewritten in October 2026 to put success first. The student asks ChatGPT
Edu (or Copilot) to apply the four questions to their specialty and to find
two or three time-and-motion or workforce studies with links, then checks
one study in PubMed.

**What to expect.** The predicted output below the line was written on
2026-09-07 from Claude (claude-fable-5-1) with web search off, against the
old prompt ("Will AI replace <specialty> by 2036?"). ChatGPT Edu searches the
web, so with the new prompt expect real studies with working links much of
the time, and often the right number. That is the intended first
experience. The author has not yet run the new prompt in Edu; re-run it
before week 4 and replace this paragraph with what Edu actually returned for
radiology and one other specialty.

- For radiology, the study a good answer finds is Dhanoa et al., JACR 2013
  (pmid:23763878): one trained observer, 14 staff radiologists, three
  Vancouver hospitals, 36.4% of time on image interpretation. Workforce
  studies it may find: Christensen et al. 2025 (pmid:39952776; +25.7% to
  +40.3% by 2055) and the attrition paper (pmid:41031940).
- For other specialties, see the search recipe below; the tutor checks any
  named study in PubMed exactly as the student is asked to.

Old predicted pattern (Claude, web search off, old prompt, 2026-09-07): all
four factors mentioned in some form, liability most often missing; no
checkable sources on the first prompt; on the follow-up, either no study or
a named study that may not contain the number.

Grade: a student who opened one study and recorded whether it exists and
contains the number meets, whether the answer held up or not. A student who
filled the four rows without checking anything falls short. A student who
found an error and asked again, and noted which parts held up, has done the
best version.

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

## Part C — check the numbers yourself (BLS)

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
what a record means and what a payer will accept (passes decomposition only
partly; Step 2 shows its tasks are among the most automated), and
the payer–provider "bot wars" raise the volume of that work (demand). Any two
factors named correctly meets.

Who bears the cost: transcriptionists, median pay $40,410 (2025), versus
$51,140 for records specialists and $68,020 for health information
technologists. The displaced occupation is the lowest paid of the three.

Step 2, observed exposure, from `data/anthropic-labor-market-2026/job_exposure.csv`
(Anthropic, released 2026-03-05 with Massenkoff and McCrory, CC BY):

| Occupation | Observed exposure | BLS 2025–35 |
|---|---|---|
| Medical transcriptionists | 64% (0.6365) | −4% |
| Medical records specialists | 67% (0.6674), 4th of 756 jobs | +8% |
| Health information technologists and medical registrars | 31% (0.3063) | +16% |

The most exposed of the three is projected to grow, and the next most
exposed to shrink. Step 3 meets if it says exposure counts the tasks a tool
touches, not demand, and names demand (capped by visits vs. bot wars adding
coding work) as what separates them.

Own specialty: 40 of the 65 occupations in SOC group 29 score 0, including
family medicine, psychiatry, pediatrics, anesthesiology and dermatology.
Non-zero physician jobs: radiologists 20%, pathologists 16%, general
internal medicine 8%, obstetrics and gynecology 7%, "physicians, all other"
3%. Emergency medicine physicians, cardiologists and general surgeons have
no row; the student should use the nearest one and say so. A good zero
line: the job's tasks were not seen often enough in Claude work use to pass
the authors' threshold. It is one product's data, so it does not mean AI
cannot help, and it does not mean the job is safe.

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
- **Obj. 4.** UCSF (pmid:41511775, research letter, full text read
  2026-10-12): adopters billed +1.81 RVUs/week (95% CI 0.86 to 2.75), +0.80
  encounters/week, no difference in denials, 1,565 physicians; about $3,044 a
  year per physician at 2025 Medicare rates. It is a difference-in-differences
  association with self-selection named as a limitation, so "the scribe
  caused it" overstates. The 5.8% the chapter used to quote is not in the
  paper and was removed. More billable output is revenue to the organization
  and cost to the payer; PHTI April 2026: system-wide costs not falling, bot
  wars = automated submission vs automated denial, volume up, resolution no
  faster.
- **Denominators (now optional, in Go deeper; no Check row).** Shrank 2019
  (pmid:31589283): waste ≈25% of *total spending*, admin complexity one of
  six categories ($265.6B). Himmelstein 2014 (pmid:25201663): 25.3% of
  *hospital* expenditures. Woolhandler 2003 (pmid:12930930): $294.3B in
  1999, 31.0% of expenditures *after exclusions*.
- **Obj. 7.** Blue in @fig-could-does: the share of a category's tasks a
  language model could do at least twice as fast, from the task ratings of
  Eloundou and colleagues (doi:10.1126/science.adj0998). Red: the share seen
  in work-related Claude use (conversations and companies' software built on
  Claude), August and November 2025, automated use counted in full and
  assisted use half. Healthcare practitioners: could about 60%, seen about
  5%. Opposite projections for two equally exposed jobs: see Part C. What a
  score does not tell you: whether the job will shrink (demand), use of any
  other product, anything about tasks below the usage threshold. Extra
  credit for naming the conflict: the authors work for the company whose
  product they measured, and it is not peer reviewed.

## Flags the tutor should know about

- The 38% single-site validation figure is Mousa's reading of Windecker et al.
  (pmid:40305017); it is not in that paper's abstract. Present as "reported
  by Mousa" until the full text is checked. Since October 2026 it is in Go
  deeper, not the main text.
- The 17–27% imaging-demand projection (Neiman) was not retrieved this
  session; the supply projection (pmid:39952776) is verified.
- The year the CAD add-on payment was withdrawn (2018 in secondary sources)
  is unverified against a CMS document.
- "Bot wars" is the wording of trade coverage of PHTI's April 2026 report; the
  PHTI page summary fetched on 2026-09-07 did not contain the phrase.
- The NYT 14 May 2025 URL returns 403 to non-browser clients; the headline,
  author, and date were confirmed from a repost and two trade summaries, the
  URL itself was not opened.
- The radar values (@fig-could-does) were read off the published chart, to
  about one percentage point; see `data/anthropic-labor-market-2026/README.md`.
  The paper's text says Claude covers 33% of Computer & math tasks, but the
  chart reads 35.5%. The chapter says "about a third". Healthcare support's
  observed value (0.019) is in the zone where markers overlap, so the figure
  labels it "near 0%".
- The Canaries paper is cited from the archived 26 August 2025 version (13%,
  data through July 2025, health aides on p. 11). The August 2026 revision at
  the same URL (checked by the agent on 2026-10-16, not by a person) gives
  19% through June 2026 in its abstract. It says the pattern attenuates when
  controlling for education and is weaker in national survey data, moves
  the health-aide panel to appendix Figure B.5, and reports that ADP's
  sample is light in education, health, and public administration (16%
  against 24%).
- Alain et al. (pmid:40446149): the abstract's average adoption rate
  (16.92%) does not match the paper's Table 3, according to the research
  agent. The chapter quotes only the 2.58% and 37.22% shares; do not quote
  the average.
- Anthropic says it will update the measure periodically. If a newer
  `job_exposure.csv` appears, replace the copy in `data/`, rerun
  `scripts/figures_labor_market.py`, and update the numbers in the chapter.

## Instructor prep

Re-run the Part A prompt in ChatGPT Edu before week 4 (radiology and one
other specialty) and update the Part A section above with what it returned. Re-read the three
BLS pages; if the projection decade has changed, update @tbl-bls in the
chapter before the cohort sees it.
