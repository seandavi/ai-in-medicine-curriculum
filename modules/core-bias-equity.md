# Core module — Bias, equity, and the proxy problem

**Format:** one 90-minute Zoom session · **Prereq:** none
**Competencies:** AIM-3 (bias, equity, and social implications)

## The claim this module tests

Every canonical case of algorithmic harm in medicine is the same case. A quantity
that mattered could not be measured, so something measurable was substituted for
it — cost for need, light-skin reflectance for oxygen saturation, race for
unmeasured biology or environment. The substitution was reasonable when it was
made. It was documented, or at least documentable. And it was wrong in a way that
tracked existing inequity, because the measurable proxy was measurable precisely
because the existing system had already been collecting it, and the existing
system had already been treating people differently.

Taught as a list, these cases become six things to remember and forget. Taught as
one structure with six instances, they become a question a student can ask about
a tool nobody has written a paper about yet: *what is this thing actually
measuring, and what did somebody hope it stood for?* That question is the whole
session. Students will meet dozens of clinical algorithms in residency, almost
none of which will have a *Science* paper dissecting them.

The second load-bearing question is harder and gets the last third of the
session: **what could a clinician have caught at the bedside, without knowing
anything about the algorithm's internals?** For pulse oximetry the answer is
genuinely encouraging — a discrepancy between a reassuring saturation and a
patient who looks and sounds unwell is a bedside finding, available to anyone
paying attention. For the Obermeyer algorithm the honest answer is much bleaker.
Students should leave holding both.

## Learning objectives

By the end, a student can:

1. State the proxy problem in one sentence and identify the substituted quantity in an algorithm they have not seen before.
2. Walk the Obermeyer analysis from proxy choice to measured harm to correction, including the magnitude of the correction.
3. For an assigned case, name the proxy or data gap, the population harmed, the correction that followed, and that correction's adoption status as of now — including where the answer is "still contested" or "still draft."
4. Distinguish harms of allocation from harms of representation, and distinguish social bias from statistical bias.
5. Say what is and is not detectable at the bedside without access to a model's internals, and cite evidence that clinicians do not reliably detect a biased model even when they are told a model is assisting them.

## Prep and tool notes

**No accounts and no tools are required.** This is the one core session that runs
entirely on the case packets, a shared document, and conversation. That makes it
the safest session to schedule opposite a call week, and the one most likely to
survive a cohort where a third of the class is interviewing.

**Case packets go out 48 hours ahead, not at the start of the session.** Each
packet is one page: the citation, the finding, the correction, and the current
status, with the **[VERIFY]** flags left visible. Students will not all read
them, and the session is designed to work if only one member of each group has.
Do not read the packets aloud during the session — the breakout is for judgment,
not for information transfer.

**Assign cases to rooms in advance and duplicate every case across two rooms.**
With about 40 students in groups of 4–5 that is eight to ten rooms and five
cases, so each case is worked twice, independently. The cross-group comparison in
the report-back depends on this: two groups given the same evidence will
frequently disagree about what a clinician could have caught, and that
disagreement is more instructive than either answer.

**A note on register.** These cases are about harm to real patients along racial
lines, and the class will include students who have been on the receiving end of
the systems under discussion. Set the expectation at the top that the session is
an engineering post-mortem of specific decisions and their consequences, not a
debate about whether the harm occurred; the harm is documented in every case
here. Keep the conversation on mechanism and correction.

## Session plan (90 min)

| Time | Mode | What happens |
|---|---|---|
| 0–8 | Frame | The proxy problem stated once, plainly. Two vocabulary distinctions that will be used all session: social versus statistical bias, and harms of allocation versus harms of representation. |
| 8–25 | Walkthrough | Obermeyer et al. 2019 walked live, start to finish — what the algorithm was for, what it optimized, why cost seemed like a sensible stand-in for need, what that produced, and what the correction changed. |
| 25–55 | Breakout (4–5) | Each room takes one assigned case and completes the fixed worksheet. Every question gets an answer, including "we could not determine this," which is a legitimate finding for the adoption-status question. |
| 55–80 | Report-back | Build the proxy table on screen, one row per case, filled in live by the reporting groups. Where two rooms took the same case, take both answers to question 5 before moving on. |
| 80–90 | Close | Jabbour et al. 2023 as the counterweight to bedside optimism, then the standing question: what does this change about how you'll practice? |

**Deliverable:** one completed worksheet per group, and a class-wide proxy table
assembled live from them — one row per case, naming the substituted quantity, the
harm, the correction, its status, and the bedside signal. Distribute the
completed table after the session; it is the only artifact from this course that
students are likely to actually keep.

## Part A — Obermeyer, walked live (8–25)

Do this as a narrative with the class, not as slides read aloud. The order
matters, because the point is that every step was defensible in isolation.

**Obermeyer Z, Powers B, Vogeli C, Mullainathan S. "Dissecting racial bias in an
algorithm used to manage the health of populations." *Science*
2019;366(6464):447–453. PMID 31649194.**

Start with the job. A health system wants to identify which patients would
benefit from enrollment in a high-touch care management program — extra nursing
contact, care coordination, the scarce resource. There are far more patients than
program slots. Something has to rank them.

Then the measurement problem. "Which patients will benefit most from extra care"
is not a column in any database. Nobody records it. It is not even well-defined
without a counterfactual. So the algorithm predicted something that *is* in the
database and that plausibly tracks it: **future healthcare costs**. Sicker
patients cost more. Ask the class to argue for this choice before you undercut
it, because it is genuinely arguable — cost is objective, universally recorded,
continuous, and available for every patient without additional data collection.
It is exactly the kind of choice a competent team makes.

Then the failure. Cost measures healthcare *consumed*, not illness. Black
patients in this system generated lower costs at the same level of illness —
because of reduced access, because of differential treatment intensity, because
of well-documented disparities in what the system spends on whom. The algorithm
was accurate at what it predicted and systematically wrong at what it was used
for. Sicker Black patients were assigned the same risk scores as healthier white
patients, and the scarce program slots went accordingly.

Then the correction, which is the reason this paper is the anchor case rather
than one more grievance. The authors did not merely identify the problem; they
reformulated the label. Correcting the bias, in the paper's own words, "would
increase the percentage of Black patients receiving additional help from **17.7
to 46.5%**." Land on that number and leave it on the screen. A single choice of
prediction target, made for defensible reasons, was suppressing eligibility for
this population by roughly a factor of two and a half.

Close the walkthrough with the two vocabulary distinctions, both of which the
archive fairness deck develops well. **Statistical bias** is a model's error
relative to the quantity it was trained to predict; the Obermeyer algorithm had
very little of it. **Social bias** is a mismatch between what was predicted and
what should have been. A model can be statistically excellent and socially
disastrous at the same time, and the two objectives are frequently at odds rather
than merely different. Separately, Crawford's distinction between **harms of
allocation** — a resource is distributed unfairly, as here — and **harms of
representation** — a system encodes a demeaning or erasing view of a group,
independent of any resource decision. Most of the cases in the breakout are
allocation harms. At least one is not, and groups should be made to decide which.

## Part B — Case breakouts (25–55)

### The worksheet (identical for every case, five fixed questions)

```
Case: _______________________________   Room: ____

1. THE PROXY OR DATA GAP
   What quantity actually mattered, and what measurable thing was
   substituted for it? If the failure was a data gap rather than a
   substitution, say what was missing from the data and why it was missing.
   _____________________________________________________________________

2. WHO WAS HARMED
   Which population, and through what concrete clinical pathway? Name the
   decision that went differently, not just the group that was affected.
   _____________________________________________________________________

3. WHAT CORRECTION FOLLOWED
   What was proposed or changed in response — a new equation, a new
   standard, a new dataset, a regulatory action?
   _____________________________________________________________________

4. ADOPTION STATUS RIGHT NOW
   Is the correction finalized, adopted, partially adopted, still draft,
   or actively contested? Cite where your answer comes from. "We could not
   determine this from the packet" is an acceptable and useful answer —
   write it down rather than guessing.
   _____________________________________________________________________

5. THE BEDSIDE QUESTION  (spend the most time here)
   What could a clinician have caught at the bedside, WITHOUT knowing
   anything about the algorithm's internals? Be specific about the signal:
   what would you have seen, heard, or measured that did not fit?
   If your honest answer is "nothing," say so and explain why not.
   _____________________________________________________________________

6. Allocation harm, representation harm, or both? One sentence of defense.
   _____________________________________________________________________
```

Question 5 is the one to protect. Groups will race through it in ninety seconds
if not warned; tell them at the start of the breakout that questions 1 through 4
are lookups and question 5 is the actual exercise.

### The five case packets

**Case 1 — Pulse oximetry.** Sjoding MW et al., *NEJM* 2020;383(25):2477–2478
**[VERIFY]** — this citation is likely PMID 33326721 but was not independently
re-pulled during course research; confirm before putting it on a slide. Fawzy A
et al., *JAMA Intern Med* 2022;182(7):730–738, PMID 35639368, verified. Valbuena
VSM et al., *BMJ* 2022;378:e069775, PMID 35793817, verified. The proxy is optical:
the device infers arterial oxygen saturation from light absorbance, and the
calibration assumed a skin-reflectance profile that does not hold across skin
tones, producing occult hypoxemia read as normal. **Regulatory status as of
August 2026: FDA issued draft guidance on January 7, 2025 proposing that
premarket diversity requirements rise from 10 to 150 participants across skin
tones. That guidance is still DRAFT and has not been finalized.** Groups must
record it as draft, not as a rule. This is the case with the most encouraging
answer to question 5.

**Case 2 — Dermatology datasets.** Daneshjou R et al., *Sci Adv*
2022;8(32):eabq6147, PMID 35960806. Adamson AS & Smith A, *JAMA Dermatol*
2018;154(11):1247–1248, PMID 30073260 — note for the group that this one is a
**Viewpoint, not original research**, and should be cited as commentary.
Fitzpatrick17k (Groh et al., CVPR-W 2021, arXiv:2104.09957) shows Fitzpatrick
types V–VI severely underrepresented. **[VERIFY]** — no single canonical citation
was found for ISIC skin-tone underrepresentation as a standalone claim, so groups
should not assert a specific figure for that dataset. Here the failure is a data
gap rather than a substitution: light skin became the implicit definition of
normal presentation because it was what the training images contained.

**Case 3 — Race-based clinical algorithms: eGFR and spirometry.** Vyas DA,
Eisenstein LG, Jones DS, "Hidden in Plain Sight," *NEJM* 2020;383(9):874–882,
PMID 32853499, verified — the systematic catalog of race-adjusted algorithms and
the best single entry point. For kidney function, the NKF-ASN Task Force
(Delgado C et al.) published simultaneously in *AJKD* 2021;79(2):268–288 and
*JASN* 2021;32(12):2994–3015. **[VERIFY]** on adoption: the widely repeated figure
that roughly two-thirds of US labs have moved to race-free eGFR traces to a
single secondary source citing an unspecified survey, and groups should record it
as unconfirmed rather than as a fact. For spirometry, Bowerman C et al.,
*AJRCCM* 2023;207(6):768–774, PMID 36383197; race-neutral GLI-Global equations
were recommended in April 2023, but **adoption is uneven and the change is
actively contested, not settled** — 2025 data show reclassification of roughly
22.7% of Black and 3.3% of Southeast Asian individuals to greater impairment
severity under the race-neutral equations, which has consequences for disability
determination, transplant listing, and occupational exposure claims that cut in
more than one direction. This is the case where the group should come back
saying the correction is genuinely unresolved. Do not let them flatten it.

**Case 4 — Chest X-ray underdiagnosis.** Seyyed-Kalantari L et al., *Nat Med*
2021;27(12):2176–2182, PMID 34893776, verified. Models trained on large public
radiograph datasets systematically underdiagnosed findings in underserved
populations, with the effect compounding across intersecting attributes. The
useful wrinkle for question 1 is that no one chose a proxy here in the way
Obermeyer's team did; the labels were extracted from existing reports, so the
model inherited whatever the original radiologists and the original documentation
practices encoded. Ask this group specifically who wrote the ground truth.

**Case 5 — LLMs and race-based medicine.** Omiye JA et al., "Large language
models propagate race-based medicine," *NPJ Digit Med* 2023;6(1):195, PMID
37864012, verified. Zack T et al., *Lancet Digit Health* 2024;6(1):e12–e22, PMID
38123252, verified. Models reproduced debunked race-based claims about physiology
in response to clinical questions. This is the case most likely to be classified
as a **representation** harm rather than an allocation harm, and the group should
be pushed on whether that distinction holds once the output enters a clinical
decision. It is also the case closest to what these students will actually touch
next year, which makes it a good one to report last.

## Part C — Report-back and the proxy table (55–80)

Build the table live on a shared screen. One row per case, one column per
worksheet question. The reporting group fills its own row while talking; the
second group that took the same case gets the floor immediately afterward and
adds or contests. The completed table is what students take away.

Three cross-case observations to draw out rather than assert, in roughly this
order:

**The proxies were all reasonable.** Cost is objective and universally recorded.
Optical calibration on the available population is how devices get built. Report
text is the only label available at radiograph scale. Race entered clinical
equations through observed population differences that someone was trying to
account for. Nobody in these cases set out to encode inequity, which is exactly
why "just don't be biased" is not an available strategy and why interrogating the
prediction target is.

**Correction is slower and messier than identification.** Obermeyer is six years
old. The pulse oximetry guidance is still draft. Race-neutral spirometry is
recommended and contested at the same time. The eGFR adoption number cannot be
pinned down from available sources. Students should notice that the paper
identifying the problem is usually the easy part of the story, and that "this was
fixed" is a claim requiring its own verification. A group that wrote "we could
not determine this" for question 4 has done the exercise correctly and should be
told so publicly.

**The bedside answers differ sharply by case, and that is the finding.** Pulse
oximetry has a real bedside signal: a saturation that does not match a patient's
work of breathing, mentation, or appearance is a discrepancy any clinician can
register without knowing anything about photoplethysmography. Race-based
equations were auditable in principle by anyone who read the equation, which was
printed in the lab report the whole time. Chest X-ray underdiagnosis and the care
management algorithm are close to undetectable from a single encounter — the harm
is defined by a comparison across patients that no individual clinician ever
sees. Push the class to name what would have been needed instead: not sharper
bedside instincts, but a denominator. Someone auditing outcomes by group, on
purpose, with the authority to act on it.

## The close (80–90)

End with the finding that complicates the entire bedside frame, because leaving
students with "a careful clinician would have caught it" is a comfortable and
false conclusion.

**Jabbour S et al., "Measuring the Impact of AI in the Diagnosis of Hospitalized
Patients: A Randomized Clinical Vignette Survey Study." *JAMA*
2023;330(23):2275–2284. PMID 38112814.** Across 457 clinicians, baseline
diagnostic accuracy was 73.0%. A standard AI model raised it by 2.9 points, and
by 4.4 points when explanations were shown. **A systematically biased AI model
lowered accuracy by 11.3 points — and adding explanations did not mitigate the
harm.** Clinicians who could see the model's reasoning were not rescued by it.

The honest synthesis is that individual clinical vigilance is necessary and
demonstrably insufficient. It catches the discrepancies that show up in one
patient in front of you, which is a real and non-trivial category — the pulse
oximetry case is exactly that. It does not catch the harms that only exist in
aggregate, and the evidence says it does not reliably catch a confidently wrong
model even with the reasoning displayed. Both institutional auditing and personal
skepticism are load-bearing, and neither substitutes for the other.

Then the standing question, asked concretely enough to answer: **you will use a
clinical algorithm in your first month of residency that nobody in this room has
heard of. What is the one question you will ask about it?** The answer the
session has been building toward is some version of *what is it actually
predicting, and what did somebody hope that stood for* — but let the class arrive
at their own phrasing, and collect the phrasings in chat. Those are worth more
than the table.

## Framing notes

Resist the pull toward a technical-mitigation discussion. Reweighting, adversarial
debiasing, fair representation learning, and post-processing are all real, and the
archive fairness deck covers them properly, but none of them would have fixed the
Obermeyer algorithm — the label was wrong, and no amount of downstream correction
fixes a wrong prediction target. Mention that as the reason for the omission
rather than letting it look like an oversight; it is a stronger point than the
mitigation survey would have been.

If a student raises the "but it's FDA-cleared" objection about any of the device
cases, that is the same objection that anchors the end of `core-appraisal`, and
the answer is Wu, Wu, Daneshjou et al., *Nat Med* 2021 — of 130 FDA decision
summaries for medical AI devices, clinical performance data appeared in only
about half, roughly a quarter reported none, and among those reporting clinical
data, well under a third gave sex-specific results. If the two modules run in the
same week, hand the objection forward or backward rather than answering it twice.

## Reusable material

`../talks/archive/2024-11-05-ml-fairness/`
(<https://talks.seandavis.net/archive/2024-11-05-ml-fairness/>) is the most
seminar-ready deck in the talks repo and maps onto this session almost
one-to-one. It opens with two thought experiments that work well as a cold start
if the Obermeyer walkthrough needs a warm-up — the CEO image-search dilemma and
the FICO loan officer — then develops social versus statistical bias and shows
that the two objectives are mathematically at odds rather than merely different.
It carries Crawford's procedural, distributive, and representational fairness
framing and the allocation-versus-representation harm distinction used in
worksheet question 6, plus a taxonomy of bias sources in healthcare ML
(collection, sampling, label, feature selection, algorithmic) that is a cleaner
scaffold for worksheet question 1 than anything written fresh would be. The
mitigation section (reweighting, adversarial debiasing, fair representation
learning, post-processing) is deliberately left out of the 90-minute plan above
but is there if a cohort wants it, or if this module is ever expanded.

`../talks/archive/2024-10-28-ai-ml-oncology-service-line/`
(<https://talks.seandavis.net/archive/2024-10-28-ai-ml-oncology-service-line/>)
contains the eight guiding principles for AI tools in healthcare
(doi:10.1038/s43856-023-00279-9). Two of them are this session in one line each:
"alleviate health disparities" and "incorporate biography" — the latter meaning
social, structural, and environmental exposures beyond biology, which is
precisely the unmeasured territory that race was standing in for in Case 3. The
deck's stakeholder-by-stakeholder view (patients, providers, researchers,
administrators) and its monitoring and compliance section are the institutional
half of the close, if the class pushes on "so who is supposed to be auditing
this?"

`../talks/archive/2024-10-31-ml-intro/`
(<https://talks.seandavis.net/archive/2024-10-31-ml-intro/>) closes with a bias
section and contains the train/test split and generalizability material. Useful
only if this module runs before `core-foundations` and the room needs ten minutes
on what a prediction target is before Obermeyer will land. The examples are
medicine-neutral and would need clinical substitution.

Note that everything under `archive/` is imported as verbatim rendered HTML with
no recoverable Quarto source, so reuse means linking to the published URL or
extracting the text and rewriting — the repo's own position, ADR-0008, is that
cross-talk reuse is agent-mediated adaptation rather than a live include graph.
Archive slugs are immutable once published, so the URLs above are safe to
hard-code into a syllabus.
