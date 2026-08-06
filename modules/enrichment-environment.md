# Enrichment module — What AI costs the planet

**Format:** one 60-minute Zoom session · **Prereq:** none
**Competencies:** `AIM-3` (bias, equity, and social implications), `AIM-X`
(professional identity and adaptability)

## The claim this module tests

Ask a room of medical students what a ChatGPT query costs the environment and
you will get numbers spanning two orders of magnitude, all of them stated with
confidence, most of them traceable to a headline nobody checked. That is not a
knowledge gap this session fixes by supplying the right number, because **there
is no single right number.** Published per-query energy figures from credible
sources differ by more than 100-fold, and the reasons they differ — model size,
output length, batching, hardware generation, datacenter efficiency, and whether
you count idle capacity, cooling, and amortized training — are the actual
content.

So the session is built backwards. Students estimate first, commit to a number
in front of their group, and only then see that the published range brackets
almost anything they could have guessed. The disorientation is the teaching
move. What they take away is not a figure to quote but a reflex: when someone
tells you what AI costs, ask what they counted.

The second half supplies proportion. Healthcare's own environmental footprint is
large, well-measured, and directly attributable to the profession these students
are entering. Presenting AI's cost without that denominator produces guilt,
which is not useful. Presenting it with the denominator produces judgment, which
is.

## Learning objectives

By the end, a student can:

1. Explain why per-query AI energy figures vary by more than 100x across
   credible sources, and name at least three specific methodological choices
   that drive the variation.
2. State the Jevons dynamic in this context: per-unit efficiency improving
   dramatically while total emissions rise.
3. Place AI's healthcare-associated footprint against US healthcare's own
   measured emissions and articulate honest proportion without dismissing the
   question.
4. Explain why water use and datacenter siting make this an equity issue and not
   only a carbon-accounting one.
5. Read a corporate emissions disclosure critically enough to ask which scope and
   which accounting basis produced the number.
6. State one personal or institutional practice they would actually change, and
   one they concluded is not worth changing.

## Prep and tools

**No accounts, no installs.** Breakout rooms, a shared document with one section
per group, and a calculator — students will need arithmetic, not tooling.

Two optional live resources, both browser-based and free, worth having open in a
tab if the discussion goes there: the
[Hugging Face AI Energy Score leaderboard](https://huggingface.co/spaces/AIEnergyScore/Leaderboard),
which rates about 166 models 1–5 stars on standardized benchmarks, and
[Electricity Maps](https://app.electricitymaps.com), which shows live grid carbon
intensity by region and makes the point that *where* a model runs matters as much
as how efficiently it runs.

**Do not pre-announce the numbers.** The estimation block only works if students
have not seen the reveal. If you circulate a reading beforehand, circulate the
MIT Technology Review explainer *after* the session, not before.

## Session plan (60 min)

| Time | Mode | What happens |
|---|---|---|
| 0–6 | Frame | The question, and the rule: no numbers from the instructor until every group has committed to one. |
| 6–17 | Breakouts of 4–5 | **The estimation exercise.** Each group computes the class's total query energy for the elective and posts the number *with its assumptions*. |
| 17–28 | Reveal | Three sourced figures. The spread. Why they differ. |
| 28–38 | Talk | Proportion and Jevons: healthcare's own footprint, Google's 33x, the conflicting Microsoft figures. |
| 38–45 | Talk | Water, siting, and where the cost physically lands. Newton County and xAI Memphis. |
| 45–55 | Breakouts | Three questions a CMIO should ask a vendor, plus one personal rule each student would actually keep. |
| 55–60 | Close (`AIM-X`) | The standing question, and the one claim not to repeat. |

**Deliverables:** one estimate per group with its stated assumptions, three
procurement questions per group, and one written personal rule per student.

## Activity detail — estimate, then reveal

**The setup.** Give every group the same countable quantity: this class, this
elective. Forty students, roughly fifteen queries per student per week, four
weeks. **2,400 queries.** Groups must produce a total energy figure in kilowatt-
hours and — this is the part that matters — write down every assumption they
used to get there. What did they assume one query costs? Did they count the
training of the model? Cooling? The idle server?

Post the numbers to the shared doc without comment. There will be a wide spread
across eight groups, and the spread among the students' own estimates is a
preview of the spread in the literature.

**The reveal.** Three figures, each from a real source, each applied to the same
2,400 queries:

| Per-query source | Figure | Class total (2,400 queries) |
|---|---|---|
| Google, August 2025 — median Gemini text prompt | 0.24 Wh | **0.58 kWh** |
| Sam Altman blog, June 2025 — ChatGPT "average" | 0.34 Wh | **0.82 kWh** |
| Jegham et al., arXiv:2505.09598 — most intensive proprietary models, long prompt | 29 Wh | **69.6 kWh** |

**The ~120x spread is the lesson.** Not any single row. Ask which number a
student would have used if they had read one article, and which article they
would have read.

Then the water parallel, using Google's disclosed 0.26 mL per prompt: about
**624 mL** for the whole class over four weeks — roughly 2.6 cups. Individually
trivial, which is exactly what sets up the scale question in the next block.

**Why the figures differ**, in the order worth teaching:

- **Source quality is not equal.** Google's figure comes from a technical paper
  ([arXiv:2508.15734](https://arxiv.org/abs/2508.15734)) with a disclosed
  full-stack methodology. Altman's is a blog post with **no methodology
  disclosed** and an ambiguous definition of "average." Epoch AI's independent
  analysis converges near **0.3 Wh** with a transparent method. Three numbers,
  three very different epistemic standings, and only one of them is a
  measurement you could audit.
- **Model size dominates.** MIT Technology Review measured Llama 3.1 8B at about
  114 J per response including cooling, and the 405B model at about 6,706 J —
  roughly a microwave running for eight seconds. About a 60x spread from model
  size alone. Jegham et al. benchmarked 30 models and found the most intensive
  proprietary models exceeding 65x the most efficient.
- **What you count.** Idle capacity, cooling overhead, datacenter PUE, and
  amortized training cost can each be in or out. Nobody is lying; they are
  answering different questions.

**The number that outran its evidence.** The famous claim that an AI query uses
"10x a Google search" traces to de Vries, *Joule* 2023
([doi:10.1016/j.joule.2023.09.004](https://www.sciencedirect.com/science/article/pii/S2542435123003653)).
The comparison is against a **2009 Google blog figure** for search energy,
assumes 100% chip utilization, and ignores every subsequent efficiency gain. It
is a real citation, in a real journal, repeated everywhere, and it does not
support the weight now placed on it. Worth five minutes on its own as a case
study in citation drift — and a natural callback if the cohort ran
`core-appraisal`.

## Proportion and Jevons (28–38)

**The denominator that makes this honest.** Eckelman MJ, Huang K, Lagasse R,
Senay E, Dubrow R, Sherman JD, "Health Care Pollution and Public Health Damage in
the United States: An Update," *Health Aff* 2020;39(12):2071–2079
([doi:10.1377/hlthaff.2020.01247](https://doi.org/10.1377/hlthaff.2020.01247)):
US healthcare emissions were **1,692 kg CO2e per capita in 2018**, the highest
among industrialized nations, with **388,000 DALYs lost** to the associated
pollution. That is the profession these students are joining, and it is measured
in disability-adjusted life years — the same currency they use for everything
else.

Do the arithmetic on screen, and do it carefully. Google's disclosed 0.03 gCO2e
per prompt across 2,400 queries is about **72 g CO2e** — against 1,692 kg per
person per year, the class's entire four weeks of AI use is a rounding error, on
the order of a few thousandths of one percent of one person's annual healthcare
footprint. **State the limit of that calculation out loud:** the only per-query
carbon figure available is Google's, which is also the most favorable of the
three energy figures, and no comparable carbon disclosure exists for the
high-intensity end. The honest statement is that at the best-documented rate the
individual footprint is negligible, and that the aggregate question is a
different question.

**Which is where Jevons comes in.** Google reports a **33x reduction in energy
per prompt and 44x in carbon over twelve months** — a genuinely large engineering
achievement. Google's **total** greenhouse gas emissions are **up 48% since
2019.** Per-unit efficiency is improving fast and being outrun by volume growth.
The individual-action framing collapses here, and it should: the student who
decides to send fewer prompts is not the mechanism by which any of this changes.

**Microsoft is the [CONFLICTING] case, and present all three figures.** The
reported increase in Microsoft's emissions since 2020 is **29.1%** (2024
sustainability report), **23.4%** (2025 report), or **80%** (Stand.earth, using a
different scope that includes gas buildout). **Do not collapse these into one
number and do not pick the one that suits the argument.** Put all three on the
slide with their scopes attached and ask the class which one they would cite in a
policy memo, and what they would have to say about the other two. The discrepancy
is the teachable object: three defensible numbers about one company's emissions,
differing because of what each counted, is the corporate-disclosure version of
the per-query problem from the first half of the session.

**The infrastructure numbers**, briefly, and as a range rather than a point.
LBNL's 2024 report puts US data centers at **176 TWh in 2023, 4.4% of US
electricity**, with growth accelerating from about 7%/yr (2014–18) to about
18%/yr (2018–23) and a 2028 projection of **325–580 TWh, or 6.7–12%**. EPRI
projects **9–17% of US electricity by 2030 (380–790 TWh)** — **[CONFLICTING]**
with LBNL on both methodology and AI-adoption assumptions. Present the range with
the caveat; do not average them. Globally, the IEA's April 2025 "Energy and AI"
projects data center demand more than doubling to about **945 TWh by 2030**, just
under 3% of global electricity.

**The disclosure gap worth naming.** Training footprints were published for GPT-3
(1,287 MWh, 552 tCO2e), BLOOM 176B (433,195 kWh; 24.7 tCO2e dynamic, 50.5 tCO2e
including embodied carbon), and Llama 3.1 (27.51 GWh, 11,390 tCO2e location-based
— **but 0 tCO2e market-based** via renewable power purchase agreements, which is
a clean illustration of why "which accounting basis?" is a real question).
**[DATA GAP]** — no comparable disclosed training figures exist for GPT-4,
Gemini, or Claude-generation models. The labs largely stopped publishing them.
That silence is itself the finding.

## Water, siting, and where the cost lands (38–45)

Carbon is diffuse; water and land are not. This block is where `AIM-3` actually
attaches.

Training a GPT-3-scale model can directly evaporate about **700,000 L** of
freshwater (Li et al., [arXiv:2304.03271](https://arxiv.org/abs/2304.03271)),
with global AI water withdrawal projected at 4.2–6.6 billion m³ by 2027. Google's
data-center water consumption rose from **4.3 billion gallons in 2021 to 6.1
billion in 2024.** US data centers consumed **17.4 billion gallons in 2023**,
projected at 38–73 billion by 2028, plus roughly 800 billion liters indirectly
through power-plant cooling.

The equity structure is the point: **two-thirds of data centers built or planned
since 2022 sit in water-stressed regions.** A single facility in Newton County,
Georgia uses about **500,000 gallons per day — roughly 10% of the county's water
use** (Ceres, ["Drained by Data"](https://www.ceres.org/resources/reports/drained-by-data-the-cumulative-impact-of-data-centers-on-regional-water-stress)).

**xAI Memphis is the sharpest case**, and the one to spend the most time on:
roughly 59 gas turbines operating without Clean Air Act permits in a South
Memphis area already rated "F" for ozone and carrying about 4x the national
cancer risk, followed by NAACP and SELC litigation
([Earthjustice](https://earthjustice.org/case/xai-illegal-gas-power-plant-data-center-colossus)).

Put the clinical question directly to the class: the residents of that part of
Memphis will present to an emergency department with asthma exacerbations, and
the physician seeing them will have no way to attribute the visit. This is
environmental exposure as a social determinant, in the specific form these
students are trained to recognize and usually cannot act on. Ask what, if
anything, that changes about how they think about the tool on their own
workstation.

## Activity detail — what would you actually ask (45–55)

Breakouts of 4–5 produce two things and post both.

**Three questions a CMIO could put to an AI vendor during procurement.** Not
aspirations — questions with answers a vendor either has or conspicuously does
not. The three worth converging on, if groups need seeding, are: publish an AI
Energy Score or equivalent standardized benchmark for the deployed model; state
which accounting basis the reported emissions use, location-based or market-
based; and disclose where inference is physically hosted, since grid carbon
intensity and local water stress both vary by region. Groups usually generate at
least one better question than these — a good one seen often is asking whether
the vendor's figure includes amortized training or only inference.

**One personal rule each, and one deliberate non-change.** Each student writes a
practice they would actually keep, plus one thing they considered changing and
concluded was not worth it. The second half prevents the exercise from becoming
a performance. A student who writes "I will not stop using AI for literature
search, because the footprint is negligible against the clinical benefit and the
lever that matters is procurement, not my keyboard" has done the reasoning this
session is asking for.

## The claim not to repeat

State this explicitly before the close, because students will encounter it and
some will find it reassuring.

**[UNVERIFIED — do not circulate]** The claim that "autonomous AI could reduce
healthcare greenhouse gas emissions by ~80%" traces to a narrow study of
autonomous diabetic-retinopathy screening replacing in-person visits. It is a
single-use-case estimate that has been generalized into a claim about healthcare
as a whole, which it does not support. **This figure must not be repeated in this
course or carried out of it**, and naming it here is deliberate — students should
recognize it when they see it and know why it does not hold.

The legitimate literature on the question exists and should be pointed at
instead: Sherman JD et al., "The Urgency of Environmentally Sustainable and
Socially Just Deployment of Artificial Intelligence in Health Care," *NEJM
Catalyst* ([doi:10.1056/CAT.24.0501](https://catalyst.nejm.org/doi/full/10.1056/CAT.24.0501));
"Sustainability of large-scale artificial intelligence models in health care,"
*Lancet Digit Health* 2026; and "Sustainable AI in medicine: balancing benefits
and environmental costs," *Nat Rev Nephrol* 2026.

## Closing question (`AIM-X`)

Five minutes, and it should not be a summary.

> **You now know the honest answer is a range spanning two orders of magnitude,
> that your individual use is negligible, and that the aggregate is not. What do
> you do with that?**

The temptation is to resolve it. Resist that, and say why: holding a real
uncertainty without collapsing it into either "it's fine" or "it's a
catastrophe" is the specific professional skill this session is for, and it is
the same skill required by every other unresolved question in the course. A
physician who can say "the per-query cost is small, the systemic cost is
growing, I know which numbers I trust and why, and here is where the leverage
actually sits" is doing something more useful than either reassurance or alarm.

## Reusable material

**Nothing in the talks repo covers environmental impact.** This module is written
from scratch against `research/enrichment-activities.md` section 3, and that
should be stated plainly rather than discovered by someone hunting for slides.

The nearest adjacent asset is the `pricing` fragment in
`../talks/talks/agentic-coding/slides/`, which frames the cost of AI access
explicitly as an equity question and warns against a free tier that quietly fails
students. It is about dollars rather than kilowatt-hours, but it is the same
argumentative move — a per-user cost that looks trivial individually and
structures access at scale — and the transition into the Newton County and
Memphis material is short.

`../talks/archive/2024-11-05-ml-fairness/` supplies the `AIM-3` vocabulary the
siting discussion needs: procedural, distributive, and representational fairness
(Crawford), and harms of allocation versus representation. Published at
`https://talks.seandavis.net/archive/2024-11-05-ml-fairness/`. Its two opening
thought experiments are also a usable structural model for the estimate-then-
reveal design, since both work by getting the room to commit before showing them
the data.

For outside reading, MIT Technology Review's "We did the math on AI's energy
footprint" (May 2025) is the flagship explainer and the right thing to circulate
**after** the session.
