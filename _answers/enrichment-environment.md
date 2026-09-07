# Answer key — enrichment-environment

Not rendered. Fed to the tutor; used by the instructor in the live session.

## Part A — the traced chain

| Row | Date | Model | Unit | Water counted | Number |
|---|---|---|---|---|---|
| Preprint (Li, Yang, Islam, Ren; arXiv 2304.03271 v1) | 6 Apr 2023 | GPT-3 (175B) | one Q&A in a "simple conversation" of 20–50 | on-site (scope 1) + off-site power-plant water (scope 2) | 500 mL per 20–50 → 10–25 mL per question; the current version says 10–50 medium-length responses → 10–50 mL |
| *Washington Post* with UC Riverside (Verma and Tan, 18 Sep 2024) | Sep 2024 | GPT-4 | one 100-word email | on-site + off-site | 519 mL; 0.14 kWh. [VERIFY: the Post's location assumptions and lower bound; secondary reporting gives a range down to about 235 mL by data-center location] |
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

**What the chatbot typically says (run 2026-09-07, Claude, no retrieval).**
Expect either the bottle-per-email or "about 0.3 mL" with a vague source.
Both are attribution failures of the kind the chapter teaches if given
without model, date, and scope. Re-run before each cohort.

## Part B — denominators

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
  (per dialysis session), ophthalmology (per cataract case). [VERIFY: pick
  and PubMed-check one per specialty before the live session if the
  pre-vetted-set route is needed.]

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
- Memphis: turbine count and permit status change; check Earthjustice case
  page before the session.

## Instructor prep

Run the Part A step-1 prompt the morning of the session and note what
source, if any, the tool gives. If it cites Google's five drops with the
on-site caveat, the tools have moved and the chapter's "wearing off" point
needs restating with a fresh specimen.
