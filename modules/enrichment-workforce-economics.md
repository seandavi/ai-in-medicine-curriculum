# Enrichment module — Will AI take your job? Workforce and economics

**Format:** one 90-minute Zoom session · **Prereq:** none
**Competencies:** `AIM-3` (bias, equity, and social implications), `AIM-7`
(workflow, systems, and implementation)

## The claim this module tests

In 2016 Geoffrey Hinton said physicians should **stop training radiologists
now** — that within five years, deep learning would obviously do the job better.
He is a Nobel laureate and one of the people most responsible for the technology
in question. He was wrong, and not merely early: he was wrong about the
mechanism.

Ten years later, radiology offered a record number of residency positions, filled
essentially all of them, has a documented workforce shortage, and posts salary
growth roughly double the average specialty. In a May 2026 NYT interview Hinton
acknowledged he "spoke too broadly," said he had meant only narrow image
analysis, and now predicts a radiologist-plus-AI combination. **[VERIFY]** — that
interview was accessed through secondary reporting because the original is
paywalled; confirm before quoting it.

This session is not a reassurance exercise. The transferable lesson is not "AI
never disrupts labor." It is that the most confident, most credentialed
job-elimination prediction in modern medicine failed for four identifiable
structural reasons, and that those four reasons are a tool students can apply to
their own specialty choice — a decision most of them are making right now.

## Learning objectives

By the end, a student can:

1. State the Hinton prediction, what actually happened in radiology through 2026,
   and why "he was just early" is an inadequate reading.
2. Apply a four-factor framework — task decomposition, real-world
   generalization, liability and regulatory structure, demand elasticity — to a
   specialty other than radiology and reach a defensible conclusion.
3. Use the mammography CAD precedent to explain why adoption of a tool and
   improvement in outcomes are separate questions.
4. Explain why AI can reduce administrative burden inside an organization while
   raising system-wide cost, and describe the "bot wars" dynamic.
5. Read the BLS occupational projections for health-information work and explain
   why two adjacent occupations move in opposite directions.
6. Name the most automatable *task* in their own intended specialty, estimate
   what fraction of the job it is, and state what would change their estimate.

## Prep and tools

**No accounts, no installs.** Breakout rooms, a shared document, and an
evidence packet.

**Build the packet before class.** Both activities run on the rule that every
claim needs a citation from the packet — students may not argue from vibes about
what AI will do, which is the entire failure mode the session is about. The
packet is one page per specialty plus a shared page of the numbers below.
Assemble it from `research/enrichment-activities.md` section 4 and carry the
verification flags into the packet itself, not just into the instructor's notes.
Students should see the flags. A packet where some numbers are marked "confirm
this" models the reading posture the session is trying to teach.

**Substitute the specialties.** The four specialties in the debate should be
four specialties this cohort is actually entering. Poll the class a week ahead
and swap. The session lands proportionally harder when a student is arguing
about the job they matched into.

## Session plan (90 min)

| Time | Mode | What happens |
|---|---|---|
| 0–8 | Frame | The 2016 quote, cold, with no context. Zoom poll: has it happened? Then the 2026 numbers. |
| 8–22 | Talk (5 slides max) | What actually happened, the four-factor framework, and the mammography CAD precedent. |
| 22–40 | Breakouts of 4–5 | **Specialty debate prep.** Eight groups, four specialties, two opposed positions each. Build a case from the packet. |
| 40–60 | Plenary | Four rounds of five minutes: 90 seconds per side, one rebuttal each, then a class poll. |
| 60–70 | Talk | The economics the debate does not surface: PHTI on system-wide cost, the BLS contradiction, RVUs. |
| 70–85 | Individual, then pairs | **Specialty-choice forecasting.** Each student names the most automatable task in their intended specialty and estimates its share of the job; pairs pressure-test with the four factors. |
| 85–90 | Close | The standing question, with the Hinton caveat attached. |

**Deliverables:** four debate verdicts with the class's vote on each, and one
written forecast per student — task, estimated fraction of the job, and the
factor most likely to make the estimate wrong.

## What actually happened in radiology

| Year | Positions offered | Fill rate | Applicants |
|---|---|---|---|
| 2025 | 1,451 (+5.2%) | 97.4% | 1,759 (−6.4%) |
| 2026 | 1,478 (record high) | ~98.4% diagnostic | 1,741 (−14% from the 2023 peak) |

**[VERIFY]** — these figures come from secondary reporting. Confirm against the
[NRMP 2026 primary PDF](https://www.nrmp.org/wp-content/uploads/2026/05/Main_Match_Results_and_Data-2026.pdf)
before they go on a slide.

Alongside that: more than 1,400 openings listed on the ACR Career Center;
attrition roughly doubled between 2014 and 2022; and ACR/Neiman projects the
workforce growing 20.9% by 2055 against 17–27% growth in imaging demand.
Doximity's 2025 report puts average diagnostic radiologist compensation at
**$571,749, up 7.5%** — roughly double the average specialty raise. A competing
figure of $520,000 exists from a different methodology; **present one or the
other with its source, and do not merge or average them.**

The nuance that keeps this from becoming blanket reassurance: **pediatric
radiology shrank**, from 2,190 to 2,032 radiologists between 2016 and 2023. Sub-
specialty labor markets can contract while the parent specialty grows, and a
student choosing a subspecialty is making a finer-grained bet than the headline
numbers describe.

## The four-factor framework

This is the analytic spine of the session, and every subsequent activity uses it.

**1. Task decomposition.** Radiologists spend only about **36% of their time on
image interpretation.** Even a tool that performed interpretation perfectly would
leave roughly two-thirds of the job untouched — protocoling, consultation,
procedures, communicating results, teaching, and bearing responsibility for the
read. A job is automatable to the extent that it decomposes into benchmarkable
tasks, and most physician jobs decompose badly.

**2. Real-world generalization.** More than 700 FDA-cleared radiology AI models
exist, roughly 75% of all cleared medical AI, and none has meaningfully displaced
labor. Models degrade off their training hospital — drops of up to 20 points —
and **38% of 2024 clearances were validated on a single hospital's data.**
Clearances also cluster on conditions that make good demos rather than conditions
that make up the case volume: stroke and breast or lung cancer account for
roughly 60%. (These figures are compiled in Deena Mousa's
["AI isn't replacing radiologists"](https://www.understandingai.org/p/ai-isnt-replacing-radiologists),
which is the best single reading to assign.)

**3. Liability and regulatory structure.** Someone has to sign the read. Current
tort doctrine measures the physician, not the model, and the regulatory framework
keeps a human in the loop by design — which is the connection point to
`core-ethics-regulation` if both sessions run. The multi-society position of the
ACR, CAR, ESR, RANZCR, and RSNA states that "for almost all AI models with
current regulatory approval, the model inference serves to augment, not replace."

**4. Demand elasticity, or the Jevons problem.** Making a diagnostic task cheaper
and faster does not obviously reduce the number of people doing it; it can
increase how much of it gets ordered. Imaging demand is growing 17–27% against a
workforce projected to grow 20.9%. This is the same paradox that runs through
`enrichment-environment`, and naming the shared structure is worth thirty seconds
if the cohort took both sessions.

## The mammography CAD precedent

Computer-aided detection for mammography is the closest historical rehearsal, and
it went further than most students expect: **74% adoption by 2010.** Then a study
of roughly 430,000 mammograms found it increased biopsies by about 20% with no
gain in cancer detection, and **Medicare withdrew the supplemental reimbursement
in 2018.** A technology was adopted at scale, generated additional procedures for
patients, and was eventually paid out of existence.

The automation-bias finding attached to it is the one to sit with: clinicians
using computer prompts identified only **50% of malignancies versus 68%
unprompted**, and were **26% more likely to follow a wrong call.** The
technology did not replace the radiologists. It made some of them worse. That is
a different and more troubling failure than the one everyone was worried about,
and it is the same shape as the Jabbour result in `core-ethics-regulation` — a
model that is wrong in a systematic way degrades the human rather than being
caught by them.

## Activity detail — the structured specialty debate (22–60)

Eight groups of five. Four specialties, two groups each, arguing opposite
positions:

- **"This specialty follows the radiology pattern"** — the perceptual core is
  narrower than it looks, the rest of the job is judgment, liability, and
  communication, and demand will absorb the efficiency.
- **"This specialty is genuinely different"** — the task decomposition is more
  favorable to automation, or the generalization problem is easier, or the
  liability structure is weaker, or demand is capped.

Default specialties if the cohort poll gives you nothing: **pathology** (the
strongest perceptual analogue), **dermatology** (image-based with an access
argument attached), **emergency medicine** (undifferentiated presentations, high
ambiguity, documentation-heavy), and **primary care** (where the automatable
share is administrative rather than diagnostic).

Every claim needs a packet citation. A group that runs out of citations has to
say so out loud — "we believe this but we cannot source it" — which is a more
useful contribution than a confident number nobody can check.

In the plenary, take a class poll after each round *before* commenting. Then
debrief each round against the four factors: which factor did the winning side
actually rely on? Groups usually converge on task decomposition without being
told to, and noticing that convergence is worth naming.

## The economics beat (60–70)

The debate produces optimism about physician employment. This block complicates
it, because "your job survives" and "the system gets better or cheaper" are
different claims.

**The independent finding, and the one to anchor on.** The Peterson Health
Technology Institute (non-vendor-funded) reported in March 2025 that ambient
scribes likely reduce burnout but show **little to no evidence of financial
ROI**. Its April 2026 "Administrative AI" report goes further: AI reduces burden
*within* organizations but is **not lowering system-wide costs and may be raising
them**, through a **"bot wars"** dynamic — providers auto-generating appeals,
payers auto-adjudicating denials, more volume of back-and-forth without resolving
the clinical question any faster. PHTI states there is "no existing evidence"
that AI-accelerated prior authorization lowers cost per claim once the AI's own
cost is counted. UCSF found that scribe adopters billed **5.8% more RVUs with no
rise in denials** — more billable output, which is not the same thing as cost
reduction.

**The BLS contradiction — the most useful single fact in this section.** Medical
transcriptionists are projected to decline about **5% from 2024 to 2034**,
attributed to speech recognition **[VERIFY]** — the direct BLS fetch was blocked
during research and this was corroborated only through secondary sources. Over
the same period, **medical records specialists are projected +7% and health
information technologists +15%.** Same industry, same technology, adjacent
occupations, opposite directions.

Put that on one slide and ask what distinguishes them. The answer is the four-
factor framework applied to non-physician work: transcription decomposes into a
single benchmarkable task, and the other two do not. This matters for these
students in a second way — the people whose jobs change first are their
colleagues, and a physician who understands why will be more useful in that
conversation than one who is only relieved about their own position.

**One number to refuse to simplify.** The widely quoted "25% of healthcare
spending is administrative" conflates three studies with three different
denominators: Shrank et al., *JAMA* 2019 (waste overall, of which administrative
complexity is one of six categories); Himmelstein et al., *Health Affairs*
(administrative costs as 25.3% of *hospital* expenditures); and Woolhandler et
al., *NEJM* 2003 (~24% of total spending, on 1999 data). Teach them as three
denominators, not one number. The habit of asking "percent of what?" is more
durable than any of the three figures.

## Activity detail — specialty-choice forecasting (70–85)

Individually, in four minutes, every student writes three lines:

1. The most automatable **task** in the specialty they are entering — a task, not
   the specialty.
2. What fraction of the job that task is. The benchmark on screen is radiology's
   ~36% image interpretation, which is the number most students will anchor
   against and usually overestimate for their own field.
3. Which of the four factors is most likely to make their estimate wrong.

Then pairs, eight minutes, swapping and pressure-testing: the partner's job is to
attack the fraction and to name a factor the writer ignored. Then a chat
waterfall — everyone pastes their task and fraction at once. Reading forty
estimates at once produces the useful observation directly: the distribution is
wide, and it is wide because students are estimating different things about the
same jobs.

Close the activity, not the session, on the caveat that makes it honest. Every
student in the room just made a confident forecast about the future of a medical
specialty. So did a Nobel laureate, using better information than any of them
have, and he got it wrong in both magnitude and direction. The point of writing
it down is to have something to be wrong against later.

## Closing question

The standing close applies with an extra clause:

> **What does this change about how you'll practice — and what would you have to
> see in the next five years to conclude you got this wrong?**

Ask them to keep their forecast. Reread at the end of residency.

## Reusable material

`../talks/archive/2025-09-30-ai-history/` (and the near-identical `2024-10-30-`
and `2024-09-19-` versions) contains the **IBM Watson thread** — Watson winning
Jeopardy! and MD Anderson setting it aside in 2017–18 — which is the best
available warm-up for the Hinton narrative. It gives students a second instance
of the same shape before they hear the first one, and makes the session about a
pattern rather than about one man's bad call. The same decks carry MYCIN and the
AI winters, which extend the pattern back forty years. Published at
`https://talks.seandavis.net/archive/2025-09-30-ai-history/`.

`../talks/archive/2024-10-28-ai-ml-oncology-service-line/` provides the
institutional and stakeholder framing — patients, providers, researchers,
administrators — that the economics block needs, plus the eight guiding
principles for AI tools in healthcare (doi:10.1038/s43856-023-00279-9). Two of
those principles, "have high healthcare value" and "reduce overdiagnosis and
overtreatment," map directly onto the mammography CAD story.

`../talks/archive/2024-11-05-ml-fairness/` supplies the equity framing for
`AIM-3`, particularly harms of allocation versus representation, which is the
vocabulary for discussing displaced non-physician health-information workers as
something other than a footnote.

Nothing in the talks repo covers the workforce or health-economics material
directly — the Hinton narrative, the four-factor framework, the PHTI findings,
and the BLS contradiction all need writing fresh from
`research/enrichment-activities.md` section 4.
