# Enrichment module — Agentic coding for clinicians

**Format:** one 75-minute Zoom session · **Prereq:** none (no coding background assumed)
**Competencies:** practical use; critical appraisal; ethics/regulation (SaMD boundary); privacy/PHI

## The claim this module tests

A fourth-year medical student with no programming background can, in a single
session, build a working clinical tool — and the interesting part is not that
they can, but what they have to understand before the thing is safe to trust.
The build is the hook. The guardrails are the curriculum.

## Learning objectives

By the end, a student can:

1. Describe what a coding agent does differently from a chatbot (plan/act/observe against real files, with permissions).
2. Build and iterate on a single-page clinical tool from a natural-language prompt.
3. Independently verify generated clinical logic against a primary source, and find at least one discrepancy or edge-case failure in their own tool.
4. State why the tool they just built is not a medical device, and what would have to change for it to become one.
5. State the PHI rule for consumer AI tiers and why it is not a formality.

## Tool choice

**Use Claude.ai Artifacts.** Free account, no credit card, browser-only, no
seat or file caps, and it builds and hosts a shareable single-page app with no
deploy step. Google AI Studio / Gemini Canvas is the equivalent fallback if a
student hits account trouble; Bolt.new is a distant third.

Explicitly **excluded from the live session**: Claude Code and GitHub Copilot.
Both require a local install (and Copilot's student verification has its own
problems), and install plus terminal literacy would consume the whole session
for non-coders. Mention them as "if you want to go further after class" only.

**Do before class, not during it:** every student creates a free account and
enables code execution / file creation in settings. Account creation eats ten
minutes if left to the session.

## Session plan (75 min)

| Time | Mode | What happens |
|---|---|---|
| 0–10 | Talk (3 slides max) | Chatbot vs. agent. The three standing rules: no PHI, toy-not-device, verify before trusting. Pin these in Zoom chat for the whole session. |
| 10–15 | Demo | Instructor builds a Wells' Criteria (PE) calculator live from the starter prompt, narrating what to check in the output. |
| 15–55 | Build (solo or breakout) | Students build their own calculator from an assigned menu — Wells, CHA₂DS₂-VASc, MELD, qSOFA — then iterate: add a citation, fix rounding, color-code by risk tier. |
| 55–70 | Verify | Each student cross-checks two test cases against MDCalc or the original publication and posts any discrepancy to chat. **This is the graded-in-spirit part of the session.** |
| 70–75 | Showcase | 5–6 volunteers, one minute each: here's my tool, here's the one thing I'd fix before trusting it. |

**Deliverable:** a shareable artifact link per student, posted to a shared doc
with the verification note attached.

Alternate builds if this cohort skews away from calculators: a
discharge-instruction plain-language translator (pairs well with health
literacy), or a scripted standardized-patient OSCE bot (pairs well with
clinical skills, and the class ends up with a shared practice bank). See
`research/enrichment-activities.md` for full session designs.

## Starter prompt (hand this out verbatim)

> Build a single-page web app that calculates the CHA₂DS₂-VASc score for stroke
> risk in atrial fibrillation. Show each risk factor as a checkbox with its
> point value. Display the running total and a risk-category interpretation
> with approximate annual stroke risk %. Add a prominent red banner:
> "Educational prototype only — not validated for clinical decision-making."
> Cite the score methodology in a footnote so I can independently verify every
> point value against MDCalc before I trust the output.

The guardrail is inside the prompt on purpose. That is the teaching move:
"toy, not device" gets baked in at the point of creation, not bolted on after.

## Guardrails to teach

1. **No PHI in a consumer AI prompt, ever.** Free and consumer tiers carry no
   BAA. Only BAA-covered institutional deployments are compliant. Every
   in-session prompt uses fictional data the student writes themselves.
2. **Toy, not device.** A personal study aid is fine. Deploying the same
   calculator for real clinical use is a different regulatory category — FDA's
   Non-Device CDS criteria turn substantially on whether the clinician can
   independently review the basis for a recommendation, which a bare score with
   no visible rationale does not satisfy.
3. **Never trust generated clinical math.** Every scoring rule, cutoff, and
   unit conversion gets confirmed against a validated primary source. LLMs
   hallucinate clinical arithmetic and citations at rates high enough that this
   is the rule, not a precaution.
4. **Comprehension abdication is the named failure.** Before demoing, a student
   must be able to say in plain language what their tool does for every input,
   including nonsense ones — all boxes unchecked, contradictory combinations.
   If you cannot explain your own generated code, you cannot anticipate how it
   fails.
5. **No credentials, no identifiers, nothing sensitive** in a throwaway
   artifact you are not going to security-review. Roughly half of AI-generated
   code carries a security defect; hardening is out of scope for 90 minutes, so
   the operative rule is to keep anything worth stealing out of it.
6. **Label AI-assisted output.** Every artifact carries an on-screen "prototype,
   not for clinical use, not faculty-reviewed" disclaimer. This is a rehearsal
   for a professional habit, not classroom theater.

## Framing notes

The term "vibe coding" (Karpathy, Feb 2025; Collins Word of the Year 2025) is
worth naming once so students recognize it, then setting aside — the field has
already moved toward "agentic engineering," where the point is directing and
reviewing an agent rather than accepting whatever it emits. That shift *is* the
lesson: technical judgment becomes more valuable, not less.

Two honest data points to keep the session from turning into a sales pitch:
AI-generated code carries security defects at high rates, and the one published
study of a vibe-coded medical-education app (an ECG tutor built with Gemini,
evaluated against control sites) found mixed and inconsistent effects on exam
performance. Building something fast is not the same as building something that
works.

## Reusable material

Fragments in `../talks/talks/agentic-coding/slides/` — `chatbot-vs-agent`,
`mental-model`, `working-well`, `good-session`, `takeaways` — cover the framing
directly. The PHI and trust section of
`../talks/talks/agentic-coding/venues/2026-07-28-umihc.qmd:560-616` lifts nearly
verbatim. A med-student venue deck composed from existing fragments would need
only the clinical framing written fresh.
