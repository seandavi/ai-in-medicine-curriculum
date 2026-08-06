# Core module — Ethics, liability, and the device boundary

**Format:** one 75-minute Zoom session · **Prereq:** none
**Competencies:** `AIM-4` (ethics, law, regulation, professionalism), `AIM-7`
(workflow, systems, implementation), closing on `AIM-X` (professional identity
and adaptability)

**This is the course-closing session.** It carries the AIM-X obligation for the
whole offering, so the last ten minutes are not a wrap-up — they are the point.

## The claim this module tests

Students arrive expecting the law to have answers. It does not yet.
**No US malpractice claim involving a clinical AI tool has reached a verdict as
of 2026.** Say that in the first two minutes, not as a reveal at the end. The
session works only if students understand from the outset that they are
rehearsing an open question rather than hunting for a rule someone already
wrote down. What exists instead is a regulatory boundary they can actually
learn (FDA's non-device CDS criteria), a doctrinal framework for reasoning
about exposure (Price/Gerke/Cohen), and one hard experimental finding about
what happens to clinicians who trust a bad model (Jabbour). Those three things
are enough to build a defensible personal position, which is what each student
leaves with.

## Learning objectives

By the end, a student can:

1. State FDA's four criteria for non-device clinical decision support, and
   explain why criterion 4 — the clinician can independently review the basis
   for the recommendation — is the one that decides most real cases.
2. Explain what a Predetermined Change Control Plan is and why it is the
   mechanism that makes a continuously-updating model regulable at all.
3. Place a clinical scenario in the Price/Gerke/Cohen 2×2 and say which cell
   carries the most liability exposure and why.
4. State that this area is untested in US courts, and describe what a plaintiff
   would have to prove anyway, given that tort doctrine measures the *physician*
   against a standard-of-care benchmark rather than measuring the AI.
5. Describe the Jabbour finding — including the part where explanations did not
   help — and say what it implies about relying on "explainable AI" as a safety
   control.
6. Articulate, in writing, one part of clinical judgment they will not delegate,
   and what would have to be true for them to change their mind.

## Prep and tools

**No accounts, no tools, no installs.** This is the one session in the course
that needs nothing but Zoom, breakout rooms, and a shared document (Google Doc
or equivalent) that everyone can type into. Open the shared doc at the start and
leave it up; it collects both the courtroom rulings and the closing statements.

**Instructor prep:** print or paste the four CDS criteria and the 2×2 into the
shared doc before class so students are not transcribing from a slide. Have the
four fact patterns below ready as separate sections of the doc, one per
courtroom, so groups can write in place.

**Re-verify before you teach this.** The regulatory half of this session moves
faster than anything else in the course. The revised final CDS guidance
**reportedly issued January 6, 2026** — framed as deregulatory but analyzed as
largely preserving the four-criteria framework — is **[VERIFY]**, and the
lifecycle-management guidance (draft January 7, 2025) was **still draft as of
mid-2026** **[VERIFY]**. Device-count figures (more than 1,400 AI-enabled
devices authorized since 1995; 331 cleared in 2025) are **[VERIFY]** and come
from a secondary tracker — FDA's own device-list URL returned HTTP 404 twice
during research. Do not cite a specific radiology share of cleared devices
without re-checking. **FDA has not finalized a generative-AI framework** — its
Digital Health Advisory Committee met November 20–21, 2024 and recommended
patient disclosure, post-market error reporting, and hallucination-rate
measurement, but do not say a genAI guidance exists.

## Session plan (75 min)

| Time | Mode | What happens |
|---|---|---|
| 0–8 | Frame | The open question, stated plainly: no US verdict exists. What a plaintiff would have to prove. Why "the AI was wrong" is not, by itself, a legal theory. |
| 8–22 | Talk (4 slides max) | The device boundary: four non-device CDS criteria, with criterion 4 worked through two examples. PCCP as the answer to "how do you regulate a model that changes?" Then Jabbour 2023 as the empirical bridge into the moot court. |
| 22–50 | Breakouts of 4–5 | **Liability moot court.** Eight groups, four courtrooms, one per cell of the Price 2×2. Each group builds its side's case. |
| 50–65 | Plenary | Courtroom by courtroom: 90 seconds per side, then the class votes and the instructor plots the four verdicts onto the 2×2. |
| 65–75 | Written close (`AIM-X`) | Every student types a three-sentence personal position into the shared doc. Six volunteers read theirs aloud. |

**Deliverables:** four courtroom rulings with the single fact that would have
flipped each one, and forty written personal positions in the shared doc.

## Activity detail — the liability moot court

The design point is that the four courtrooms are not four variations on a
theme; they are the four cells of Price/Gerke/Cohen, handed out without telling
students that is what they are. The 2×2 gets revealed in the report-back, when
the class discovers that the two courtrooms where the defense struggled are the
two cells the framework predicts.

Assign eight groups of five — two groups per courtroom, one plaintiff and one
defense. All four fact patterns share the same skeleton: an FDA-cleared
deterioration-prediction model deployed on an inpatient service, a patient who
does badly, and a physician who has to explain what they did.

| Courtroom | AI recommendation | Physician | The question the group must answer |
|---|---|---|---|
| A | Consistent with the standard of care | Followed it | Does following a correct recommendation ever create exposure? What if the physician could not have said *why* it was correct? |
| B | Departed from the standard of care | Followed it | The high-exposure cell. What would the physician have had to do to be defensible — and is that realistic at 2 a.m. with fourteen patients? |
| C | Consistent with the standard of care | Overrode it | The other high-exposure cell. Does a clinician now have to justify *disagreeing* with a machine? What does that do to independent judgment? |
| D | Departed from the standard of care | Overrode it | The physician was right. Is there any residual exposure — in documentation, in institutional policy, in the fact that the tool stayed deployed? |

Each group produces two things and posts them to the shared doc: a one-sentence
ruling, and **the single fact that, if changed, would have flipped it.** That
second item is the real artifact. It forces the group past "it depends" into
naming the pivot.

Two constraints keep the exercise honest. First, remind groups that current tort
doctrine still measures the physician against a standard-of-care benchmark — the
AI is evidence, not a defendant, and the **learned intermediary doctrine** sits
the physician between the manufacturer and the patient, which makes direct
product-liability claims against the vendor harder and pushes exposure back onto
the treating clinician's judgment. Second, no group may assert what a court
"would" hold. They argue what a court *should* hold and say why. There is no
case law to be right about.

Feed Jabbour into courtrooms B and C as the plaintiff's or defense's best
evidence, depending on the side. Jabbour S et al., *JAMA*
2023;330(23):2275–2284 (PMID 38112814): 457 clinicians, baseline diagnostic
accuracy 73.0%. A standard AI model raised accuracy by 2.9 points, or 4.4 points
with explanations. **A systematically biased model lowered accuracy by 11.3
points — and adding explanations did not mitigate the harm.** That last clause
is worth the whole session. It means the reflexive institutional answer to
automation bias — "we'll require explainable AI" — has one randomized test
behind it, and in that test it did not work. A defense built on "the tool showed
its reasoning, so the physician should have caught it" has to contend with
evidence that showing reasoning did not help.

## If you need the shorter or the asynchronous version

The **regulatory scavenger hunt** (30–40 min, async-friendly) substitutes for the
moot court when time is short or when the cohort has already had a heavy
discussion session. Each group takes one open question and finds the current
primary-source answer, with the URL and the date they checked.

Use the genuinely unresolved ones: **ACGME and LCME expectations for AI training**
(never researched), the **status of the NAM AI Code of Conduct** (could not be
confirmed), and whether any **patient-facing clinical chatbot safety incident**
has been documented since the 2023 NEDA "Tessa" case. Two questions that were open
earlier in this course's development — the EU AI Act high-risk timeline and the
scope of the January 2026 CDS revision — now have verified answers in
`../research/enrichment-activities.md` §5.3 and §5.4, so assign them only if you
want a group to *check whether the answer has already moved again*, which on
current form is a live possibility.

Run it as a real exercise, not a homework assignment: the finding students bring
back is that several of these questions do not have a clean answer even from the
primary source, and that two credible outlets will say different things.
Demonstrating how hard this space is to pin down is arguably the most honest
lesson the course can teach, and it is a skill they will need in five years when
everything specific taught here has been replaced.

The two activities can also be run together across a 75-minute session by
assigning the scavenger hunt as pre-work and opening with a five-minute
report-back, which has the additional benefit of correcting anything on this page
that has gone stale.

## Content the didactic block has to land

**The four non-device CDS criteria** (September 2022 final guidance). Software is
non-device CDS when it (1) is not intended to acquire, process, or analyze a
medical image or a signal from an in vitro diagnostic or signal-acquisition
system; (2) displays, analyzes, or prints medical information; (3) provides
*recommendations* rather than a specific directive; and (4) **allows the
clinician to independently review the basis for the recommendation** so that the
clinician does not rely primarily on it.

Criterion 4 is the teaching point and the one to spend time on. A bare risk score
with no visible rationale fails it. The same score with its inputs, weights, and
source publication displayed may pass. This is the same criterion that made the
calculator in `enrichment-agentic-coding` a toy rather than a device, and it is
worth calling that connection out explicitly if the cohort ran that session —
the guardrail written into the starter prompt there was this criterion in
disguise.

**PCCP** (final guidance December 4, 2024). A manufacturer pre-specifies
anticipated modifications in the original submission — a description of the
modifications, a modification protocol, and an impact assessment — so that later
updates falling inside the plan do not trigger a new 510(k), De Novo, or PMA.
This is the mechanism that in principle lets a continuously-updating model ship
improvements without re-review each time, and it is the single most important
regulatory concept for these students. It also raises the question worth putting
to the class: if the model on your unit today is not the model that was cleared,
what exactly did clearance tell you?

**"But it's FDA-cleared, isn't it fine?"** The answer is Wu E, Wu K, Daneshjou R,
et al., *Nat Med* 2021;27:582–584. Of 130 FDA decision summaries, clinical
performance data was reported for only about half, and roughly a quarter reported
none at all; among those with data, well under a third gave sex-specific results.
A 2024 follow-up ("Not all AI health tools with regulatory authorization are
clinically validated") finds the gap persists. Clearance is a regulatory status,
not a validation certificate.

**Insurance, briefly.** The Doctors Company stated in Q4 2025 that it carries no
AI exclusion and will defend and indemnify physicians in AI-involved claims. The
broader market pattern is cautious, case-by-case underwriting with advice to
notify your carrier before adopting a clinical AI tool. For an MS4 entering
residency, the practical version is: your institution's coverage is the one that
matters first, and someone in GME can tell you what it says.

**The teaching irony**, if there is time for one aside: FDA's own internal
reviewer LLM, Elsa (v1.0 June 2025, v4.0 May 2026), had documented accuracy and
hallucination problems acknowledged by the Commissioner. The agency writing the
rules is working through the same failure modes as everyone else.

## The AIM-X close

Ten minutes, and it is the reason the module is scheduled last.

Put one question in the shared doc and give students six silent minutes to
answer it in three sentences:

> **What part of clinical judgment will you not delegate to an AI system — and
> what would have to be true for you to change your mind?**

The second clause does the work. Without it, students write a slogan. With it,
they have to state a falsifiable condition, which converts a reflex into a
position they can defend and, more importantly, revise. That is exactly what
AIM-X asks for: not a fixed rule but a considered stance held with stated
reasons, in a field where the reasons will change.

Read six aloud. Do not adjudicate them. The variation across forty answers is
the demonstration — the class watches a defensible range of positions emerge from
the same evidence, which is what professional judgment under uncertainty actually
looks like.

Close by naming that the answers are dated. Ask them to keep the file and reread
it at the end of intern year. Half the class will have moved, and the useful
skill is noticing *why*.

## Reusable material

`../talks/archive/2024-10-28-ai-ml-oncology-service-line/` is the best structural
fit — it carries a campus LLM governance framework and the eight guiding
principles for AI tools in healthcare (doi:10.1038/s43856-023-00279-9), which
work well as a checklist against which to test the moot-court rulings.
Published at `https://talks.seandavis.net/archive/2024-10-28-ai-ml-oncology-service-line/`.

`../talks/archive/2024-10-23-ai-in-medical-education/` has the four-tier taxonomy
of classroom AI policies and twelve practical tips for ethical AI use. It is
aimed at faculty rather than students, but the policy taxonomy is a clean warm-up
for the device-boundary discussion: both are about drawing a line and defending
where you drew it.

The PHI, privacy, and trust section of
`../talks/talks/agentic-coding/venues/2026-07-28-umihc.qmd:560-616` (~500 words of
speaker notes) lifts nearly verbatim for the standing rules, including "verify
before it counts — you sign the note," which is the one-line version of this
entire session.

`../talks/talks/ai-safety/` — "Constructive and Safe AI in the Clinic," delivered
to IDPT 8079, is the closest existing lecture to this module, but it exists only
as a Drive PowerPoint stub with a one-line abstract. If it matters, someone has
to open the Drive file; nothing in the talks repo reveals its content.
