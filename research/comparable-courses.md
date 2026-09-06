# Comparable courses

External courses reviewed for what to borrow and what to deliberately not be.
Add one section per course. Keep the "steal" list concrete enough to act on.

## HMS Executive Education — *AI in Health Care: From Strategies to Implementation*

- **URL:** https://execonline.hms.harvard.edu/artificial-intelligence-in-health-care-from-strategies-to-implementation
- **Reviewed:** 2026-09-06 (page fetch; not enrolled)
- **Provider:** Harvard Medical School Executive Education, delivered by Emeritus
- **Format:** 8 weeks, 4–6 h/week, async video + live sessions + weekly office hours; ~32–48 h total
- **Audience:** executives, leaders, consultants, regulators, researchers; "no coding required"
- **Price:** not on page — [VERIFY]; Emeritus/HMS certificates typically run in the low thousands USD
- **Lead faculty:** Andrew Beam. Guests: Lily Peng, Sunny Virmani, Karandeep Singh, Marzyeh Ghassemi, Molly Gibson, Luca Foschini
- **Explicit disclaimer:** "not intended for direct clinical decision-making training"

### Modules

1. History and foundations of AI (supervised vs self-supervised)
2. The AI development pipeline — train / validate / deploy; capstone concept
3. Lab to real world — product success factors
4. Transparency, reproducibility, generalizability — risk prediction, evaluation measures
5. Bias and harm across the pipeline
6. AI for startups — investor pitch
7. Wearable / person-generated data
8. Live capstone presentations, community vote

Assignments: *Algorithmic Trust* (decide with a predictive model), *Model Cards*,
*ML for Wearables*, *AI Viability*. Capstone: pitch a novel AI-first health care
solution. Cases: EchoNet-Dynamic, Evidation, Flagship Pioneering, Generate:
Biomedicines, Google Health, Sage Bionetworks. Ships an "AI Tutor" over course content.

### Read against this course

It is a **builder's/leader's course** — the through-line is "conceive a product and
pitch it." Ours is a **user's/appraiser's course** for people who will be handed
deployed tools in residency in a few months. Design constraint 5 (appraisal over
tool training) is the right call and this course is evidence for it: even HMS
declines to claim it prepares anyone for clinical decision-making.

It is also **predictive-ML-shaped, not LLM-shaped.** Risk prediction, echo
models, wearables. No module on generative AI, prompting, ambient documentation,
or hallucination. That is the gap our course fills, and it means the content
overlap with us is mostly modules 4–5 → `core-appraisal`, `core-bias-equity`.

**Absent from HMS, present here:** patient communication (AIM-6), regulation /
liability / device boundary (AIM-4), workforce and deskilling, environmental cost,
hands-on use of actual LLM tools, AIM-X.

### Worth stealing

- **Model card exercise** → `core-appraisal`. Read a real model card, then write the
  section the vendor left out. We already hold the CHAI Applied Model Card template
  (`research/enrichment-activities.md`, CHAI entry). Fits the 20–60 breakout block.
- **EchoNet-Dynamic as an appraisal case.** Open model, published validation, and a
  clean "benchmark number vs deployed performance" story — throughline 3.
- **"Algorithmic trust" scenario** — act on a risk score you can't inspect. Overlaps
  the centaur/cyborg stance; a usable 10-minute opener for `core-centaur-cyborg`.
- **AI Tutor over course content.** HMS/Emeritus ship exactly option B in
  `CONTEXT.md` (chat over the course corpus). External validation that it is a
  normal thing to give students, not an experiment.
- **Community vote.** Zero-cost engagement for an ungraded course. Apply to the
  AIM-9 source collection (option C): cohort votes the most defensible sources.
- **Weekly office hour** — cheap add to the async path in `curriculum/delivery-modes.md`.

### Deliberately not importing

Startup/investor pitch, wearables module, history module, product-pipeline
sequencing, 8-week runtime, six guest speakers (breaks the one-per-session cap;
their economics are recorded video, ours are live Zoom).

### Where to cite it

Closing session (AIM-X personal learning plan): "if you want to *build* rather
than *use*, this is the next course." Also the honest answer if a student asks
whether to take it instead of ours: different course, different job.
