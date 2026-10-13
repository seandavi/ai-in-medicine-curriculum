# Answer key — enrichment-environment

Not rendered. Fed to the tutor; used by the instructor.

## Part A — the traced chain

Rewritten in October 2026 to put success first. The student asks ChatGPT
Edu (or Copilot) to find the sources behind "a bottle per email" and "five
drops per prompt" plus the 2023 preprint, and to say for each what was
counted; the student then opens one source and marks that row confirmed or
corrected. Grade: three rows filled and one row checked against the source
meets, whether the chatbot was right or not. Rows copied with no source
opened falls short. The reference rows below are what a fully correct
answer contains.

| Row | Date | Model | Unit | Water counted | Number |
|---|---|---|---|---|---|
| Preprint (Li, Yang, Islam, Ren; arXiv 2304.03271 v1) | 6 Apr 2023 | GPT-3 (175B) | one Q&A in a "simple conversation" of 20–50 | on-site (scope 1) + off-site power-plant water (scope 2) | 500 mL per 20–50 → 10–25 mL per question; the current version says 10–50 medium-length responses → 10–50 mL |
| *Washington Post* with UC Riverside (Verma and Tan, 18 Sep 2024) | Sep 2024 | GPT-4 | one 100-word email | on-site + off-site | 519 mL; 0.14 kWh. Location range as reported by Tom's Hardware from the Post's model: Texas about 235 mL, Washington state about 1,408 mL. [VERIFY: Post article paywalled; figures from secondary coverage, 2026-09-08] |
| Google (Elsworth et al., arXiv 2508.15734; Cloud blog 21 Aug 2025) | Aug 2025 | Gemini Apps, median text prompt | one prompt | on-site cooling only | 0.26 mL; 0.24 Wh; 0.03 gCO2e |
| Altman, "The Gentle Singularity" (blog, Jun 2025) | Jun 2025 | ChatGPT, "average" | one query, undefined | not stated | 0.000085 gal ≈ 0.32 mL; 0.34 Wh; no method |

**Ratio.** Post per email ÷ Google per prompt = 519 / 0.26 ≈ 2,000. If the
student treats the email as several queries (the underlying UCR work
counted a conversation as many requests), the per-question ratio drops but
stays above 100. Preprint ÷ Google = 10–25 / 0.26 ≈ 40–100.

**The single choice that explains most of the ratio.** Water scope
(on-site only versus on-site plus off-site) is the defensible first answer;
the Riverside group's own statement is that Google compared its on-site
figure against their total. Model/year (GPT-3 or GPT-4 in 2023–24 versus
Gemini in 2025, after a claimed 33x per-prompt energy reduction) is the
other acceptable answer. "Which query" (email versus median prompt) is
third. A student who names any one and can say why it dominates meets the
rubric.

**Verdict sentences, model answers.**

- To the resident: "The bottle is a 2024 estimate for GPT-4 writing a
  100-word email, counting the power plant's water as well as the cooling
  tower's; the same group's 2023 figure was a bottle per 20 to 50 questions,
  and nobody has measured the scribe."
- To the medical director: "The five drops is Google's 2025 median Gemini
  prompt counting only the water used on site; the researchers whose work
  it was compared against say adding the power plant's share puts it
  higher, and the scribe is not Gemini."
- The sentence true at every point on the figure: "At every published rate
  one clinic's use is a rounding error against the county's water; the
  aggregate is a different question, and it is about where the data center
  is, not about who opts out."

**What the chatbot typically says.** The prediction written on 2026-09-07
came from Claude with no retrieval (web search off), against the old prompt
("How much water does one ChatGPT query use?"): either the bottle per email
or "about 0.3 mL" with a vague source. ChatGPT Edu searches the web, so
with the new prompt expect it to find the preprint, the Post analysis and
Google's report, often with the right numbers, and sometimes to miss the
on-site-only scope of Google's figure. That scope is the cell most worth
checking. The author has not yet run the new prompt in Edu; re-run it
before week 4 and replace this paragraph with what it returned.

## Part B — denominators (optional since October 2026)

Any real paper with a per-unit number passes. Useful anchors if a student
is stuck (all verified in PubMed this session unless flagged):

- US health care, 1,692 kg CO2e per capita, 2018 (Eckelman et al., Health
  Aff 2020, pmid:33284703). Divided by roughly 10 encounters per person per
  year, ~170 kg per encounter as a crude upper anchor.
- Autonomous DR screening encounter versus in-person specialist visit
  (Wolf et al., npj Digit Med 2022, pmid:35551275): the paper's per-encounter
  figures are the cleanest "one encounter" numbers in the AI literature.
- Digital-health footprint scoping review (Lokmic-Tomkins et al., JAMIA
  2022, pmid:36314391) for what "per telehealth visit" estimates usually
  include (travel avoided) and omit (device and server energy).
- Specialty anchors students commonly find: anesthesia (desflurane per
  case), surgery (per laparoscopic case), radiology (per MRI/CT), nephrology
  (per dialysis session), ophthalmology (per cataract case). Pre-vetted set,
  one per specialty (PubMed-checked 2026-09-08): anesthesia, Lechani et al.
  BJA 2026, pmid:42613204 (10.8 kg CO2e per hysteroscopy under sevoflurane,
  6.6 kg TIVA, 5.5 kg spinal); surgery, Comes et al. BJS 2024, pmid:39291674
  (56.5 kg per laparoscopic cholecystectomy); radiology, McAlister et al.
  Lancet Reg Health West Pac 2022, pmid:35538935 (17.5 kg per MRI, 9.2 kg per
  CT); nephrology, Adv Ther 2024, pmid:39541083 (3.5 to 43.9 kg per dialysis
  session by modality); ophthalmology, Ophthalmologica 2026, pmid:42671945
  (14.1 kg per cataract procedure).

**Class arithmetic in the chapter (49 students, from October 2026).** 49 x 15
queries x 4 weeks = 2,940 queries. At 0.24 Wh: 705.6 Wh, about 0.71 kWh
(about 40 minutes of a 1 kW microwave). At 0.26 mL: 764 mL. At 0.03 g:
88 g, about 0.005% of 1,692 kg. At the Post's 519 mL: about 1,526 litres.

**Arithmetic check.** At Google's 0.03 g per prompt, 1 kg CO2e ≈ 33,000
prompts. At 29 Wh × 0.125 g/Wh ≈ 3.6 g per prompt, 1 kg ≈ 280 prompts. Both
are large; a student's "sentence I would actually say" should state that
the keyboard is not the lever and that the aggregate is a separate
question.

## Part C

Acceptable vendor questions have a checkable answer: accounting basis
(location- versus market-based), hosting location and its grid intensity
(Electricity Maps), inclusion of training/idle/cooling, willingness to
publish an AI Energy Score. "Is it sustainable?" fails.

The rule and the non-change are graded on specificity and on whether the
reason is arithmetic from Parts A–B rather than mood.

## Numbers with dates, for the instructor

- Google total emissions vs 2019: +48% (2023, 2024 report), +51% (2024,
  2025 report), +81% (2025, 2026 report, ESG Dive 2 Jul 2026). Data-center
  electricity +27% (2024), +37% (2025). Per-prompt energy −33x, carbon −44x
  over 12 months to mid-2025 (Google).
- Microsoft, if asked: +29.1% since 2020 (2024 report), +23.4% (2025
  report), +80% (Stand.earth, wider scope). [CONFLICTING]; present all three.
- LBNL: 176 TWh, 4.4% of US electricity, 2023; 6.7–12% by 2028. EPRI:
  9–17% by 2030. [CONFLICTING]; quote the range.
- IEA: ~415 TWh (2024) → ~945 TWh (2030), just under 3% of global.
- Memphis: two sites. Colossus 1 in South Memphis (Shelby County, TN):
  about 35 turbines ran without permits from 2024; SELC and the NAACP sent a
  notice of intent to sue on 17 June 2025; the county permitted 15 turbines on
  2 July 2025 and the groups appealed on 16 July 2025 (SELC timeline, checked
  2026-09-08). Colossus
  2's turbines sit across the line in Southaven, MS. Rechecked 2026-10-12
  (SELC timeline dated 8 May 2026; CourtListener docket): MDEQ approved a
  permit on 10 March 2026 (reported as 41 turbines; some outlets say 27);
  SELC appealed for the NAACP and others on 9 April 2026; NAACP v. X.AI Corp.,
  N.D. Miss. 3:26-cv-00074, filed 14 April 2026, before Judge Debra M. Brown;
  preliminary-injunction motion filed 6 May 2026. As of 5 October 2026 the
  docket shows the United States appealing (Fifth Circuit 26-60806) and
  seeking a stay of all proceedings; no ruling on the NAACP's claims. The
  chapter now gives no turbine count and says only "no ruling as of 12
  October 2026". Check the docket before the session.
- Water stress: the chapter used to cite Ceres, *Drained by Data*, for
  "two-thirds" and a Newton County, Georgia figure; that page has neither.
  "About two-thirds of new data centers built or in development since 2022
  are in places already gripped by high levels of water stress" is a
  Bloomberg News analysis (Nicoletti, Ma, Bass, May 2025), read through
  Sherwood News (8 May 2025), KUNC (2 June 2025) and DatacenterDynamics,
  because the Bloomberg page is paywalled. The Newton County figure (about a
  tenth of county water, attributed to the county water authority director in
  the New York Times, 14 July 2025) was cut: the Times article could not be
  opened, and a later local report (seen only in a search summary, not
  opened) gives about 2 percent.
- Wolf et al. 2022 (pmid:35551275), the "80 percent" paper: an estimate for
  IDx-DR (Digital Diagnostics); three of six authors (Abramoff, Tava,
  Clarida) list Digital Diagnostics as an affiliation. It is a modelled
  marginal estimate, not a measurement.
- Doo et al. 2024 (pmid:39189909): Vicuna 1.5 is a Llama 2 model fine-tuned
  on general conversations; the paper calls it "a specialized fine-tuned
  model", but it was not trained for radiology.

## Instructor prep

Run the Part A step-1 prompt the morning of the session and note what
source, if any, the tool gives. If it cites Google's five drops with the
on-site caveat, the tools have moved and the chapter's "wearing off" point
needs restating with a fresh specimen.
