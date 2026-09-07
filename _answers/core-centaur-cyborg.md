# Answer key — core-centaur-cyborg

Not rendered. Fed to the tutor; used by the instructor in the live session.
This chapter asks for positions, so the "answers" below are defensible
verdicts with the reasoning the tutor should look for, not the only correct
ones. A student who sorts a task the other way with a stated reason tied to
risk and validation meets the rubric.

## Part A — the eight-task sort

| Task | Defensible verdict | Risk | Validation (typical, 2026) | Peril | What the tutor listens for |
|---|---|---|---|---|---|
| 1. Drafting a progress note | Centaur | Patient | Ambient scribes: yes for visit notes (see appraisal chapter); EHR inpatient note drafting: institution-specific, often piloted, rarely validated on outcomes | Mis-skilling | The draft is a bounded delegation; every assessment/plan line is read against the student's own reasoning before signing. The student should name the day-3 creatinine example or an equivalent. |
| 2. Writing a progress note | Not at all, or centaur for structure only | Patient | None for the reasoning content | Never-skilling | The difference from row 1: here nobody has done the thinking yet. The note *is* the reasoning. Students who give rows 1 and 2 the same verdict have not seen that one has a human holding the pen and one does not. |
| 3. Literature search | Cyborg with retrieval-grounded tools; centaur with a general chatbot | Me, then patient | Retrieval-grounded tools: near-zero fabrication (appraisal chapter); general chatbot: not validated for citations | Deskilling of search skill; mis-skilling if citations are trusted | Verification in PubMed is the check. "Cyborg" is fine if the student says which tool and why. |
| 4. Building a differential | Centaur, after starting alone | Patient | Goh 2024: model alone strong, physician+model no better; not validated for unsupervised use | Never-skilling (the sharpest one for an MS4) | Technique 1 and 2: own differential first, then hint-seeking. A student who says "cyborg" must explain how they preserve the grappling. |
| 5. Patient education handout | Cyborg | Patient, moderate (reading level, wrong facts) | Not validated; patient-facing text must be read and checked | Mis-skilling is low; the risk is to the patient, not the learner | Read every fact; reading-level check; disclosure to the patient that it was AI-assisted is reasonable (patient-communication chapter). |
| 6. Journal club slides | Cyborg | Me | Not needed; low stakes | Deskilling of synthesis is the honest concern | The one task on the list where iterating freely is fine. Slides are not the paper; the reading is. |
| 7. Summarizing a paper | Centaur | Me, then patient if acted on | Not validated; summaries drop the limitations section | Never-skilling (critical appraisal) | Read the methods yourself; use the tool to check your summary, not to replace it (teach-back). |
| 8. Answering a patient message | Centaur | Patient | Garcia 2024 (pmid:38506805): institutional, EHR-integrated, BAA-covered; 20% utilization, no time saved, burden reduced | Mis-skilling of tone and content | Read and edit every draft; never send unread. Disclosure: institution-specific; the student should say whether the patient is told and by whom. Consumer chatbot: never, PHI. |

The tutor should reward a grid in which "don't know" appears in the
validation column. Most students do not know what their institution has
validated, and saying so is the correct answer.

## Part A step 3 — the disagreement

A good disagreement names the opposing case's strongest premise. Examples the
tutor can offer if the student is stuck:

- Row 1 vs 2: "A drafted note I edit heavily *is* a note I wrote." Counter: the
  editing preserves the plan's structure and anchors on its conclusions
  (mis-skilling). Resolution: draft only after writing your own one-line
  assessment.
- Row 4: "The model alone scored higher than the physicians; refusing to use it
  harms patients." Counter: the physicians *with* the model did no better, so
  the benefit is not automatic; and the trial measured attendings and
  residents, not learners building the skill.

## Part B — the prompt

A rewritten prompt meets the rubric if it (a) states who and where, (b) asks
for a hint, a question, or a check rather than the product, and (c) contains the
student's own current position. The chapter's worked example is the model.
Common failure: the rewrite adds context but still ends "what should I do?"

The quiz step: the tutor should ask what the student got wrong and whether
they could explain why the tool's correction was correct (technique 4). A
student who reports the tool refused to quiz and gave a plan anyway has
observed something true; note it and move on.

## The drafted note

The mis-skilled line is problem 2: "AKI, likely prerenal in setting of poor PO
intake and diuresis. Continue IV fluids at 75 mL/h." It contradicts problem 1
(net negative 1–1.5 L). Creatinine 1.0 → 1.3 → 1.6 on day 3 of diuresis in a
still-congested patient (JVP 8, crackles, 1+ edema, weight down 2.8 kg) is the
expected cardiorenal picture; the decision is hold/slow/continue diuresis, not
"add fluids." A secondary tell: home lisinopril continued through an AKI without
comment. Students who spot the second one have read the whole plan.

The case is fictional and written for the chapter. It was not generated by any
product and should not be described as an example of a specific vendor's
output.

## The two findings, reconciled

- Physicians: Goh 2024 (pmid:39466245) diagnosis, no benefit to physicians with
  the model, model alone +16; Goh 2025 (pmid:39910272) management, +6.5 with
  the model, indistinguishable from model alone.
- Learners: Bastani 2025 (pmid:40560616), +48%/+127% while using, −17% after
  removal for plain chat, mitigated by hint-giving tutor; Fan 2025
  (doi:10.1111/bjet.13544), better task performance, no gain in knowledge or
  transfer, metacognitive laziness.
- Deskilling: Budzyń 2025 (pmid:40816301), ADR 28.4% → 22.4% off-AI after AI
  exposure.

Not in conflict: the physician trials measure performance with the tool
present; the learner studies measure what remains when it is removed. The
chapter's point is that an intern needs both, and the second is the one the
tool does not supply.

## The standing sentence

No key. The tutor should check only that it names a task and a reason, not a
category or a slogan. "I cannot yet name one" is an accepted answer and is
flagged for the final session.

## Instructor prep

- Confirm the institution's current attestation/disclosure language for
  AI-drafted notes and portal replies before the live session; the chapter
  carries a `[VERIFY]` for it.
- Run the hint-seeking prompt from the chapter the morning of the session in
  the institutional tool and see whether it answers with a plan anyway. If it
  does, that is the demo.
- The live session's Breakout B is Part A with groups of 4–5; the report-back
  grids the eight tasks against group verdicts and spends the time on rows 1–2.
