# Enrichment module — Prompting and clinical reasoning lab

**Format:** one 75-minute Zoom session · **Prereq:** none
**Competencies:** AIM-5 (clinical application and practical use), AIM-2 (critical appraisal)

## What this session is actually for

The obvious version of this session teaches students to write better prompts. The
useful version teaches them what changes when they do — and what doesn't. A
structured prompt reliably produces a better-organized answer. Whether it produces
a *more correct* answer is a separate question, and the gap between those two
things is where students get into trouble, because a well-formatted differential
reads as authoritative regardless of whether it is right.

There is a specific reason to run this with fourth-years. When final-year students
at Imperial were asked to evaluate GPT-3.5's answers to ten clinical vignettes,
five of which were deliberately wrong, the median correct-evaluation rate was
**56%** — barely better than chance at spotting a wrong answer in their own
field. The students themselves credited case-based and pathology teaching, not any
AI training, for whatever ability they had. Only **5%** had encountered the term
"clinical prompt engineering" at all (Waldock et al., *BMC Med Educ* 2025;25(1):195,
[doi:10.1186/s12909-025-06735-5](https://doi.org/10.1186/s12909-025-06735-5)).

So the session has two jobs, and the second matters more: build the prompting
skill, then immediately demonstrate its limits.

## Learning objectives

By the end, a student can:

1. Convert a bare clinical question into a structured prompt specifying role,
   task, required reasoning, output format, and what the model should say when
   uncertain.
2. Compare naive and structured prompt outputs on the same vignette and
   distinguish improvements in *organization* from improvements in *accuracy*.
3. Identify at least one confident error in an LLM's clinical output by checking
   it against a source rather than against intuition.
4. State why a well-formatted answer is more dangerous than a poorly formatted
   one when it is wrong.
5. Describe what the published evidence does and does not show about LLMs
   improving physician diagnostic performance.

## Before class

- **Account created ahead of time** — ChatGPT free, Claude.ai free, or Gemini.
  Any of the three works. Students who want to use OpenEvidence or Doximity GPT
  (both free for verified medical students) must complete identity verification
  well before the session; it is not instantaneous.
- **Vignettes are distributed in session, not before.** Students who pre-run the
  cases lose the experience the session is built on.

All vignettes are fictional and written for this course. Nothing from a real
encounter enters any tool, in this session or any other — the free tiers carry no
BAA.

## Session plan (75 min)

| Time | Mode | What happens |
|---|---|---|
| 0–8 | Frame | The Waldock finding: final-year students caught deliberately wrong AI answers 56% of the time. Ask the room to predict the number before showing it — they overestimate, every time. The three standing rules. |
| 8–18 | Demo | Instructor runs one vignette with a bare prompt, then the same vignette with a structured prompt, narrating what improved and explicitly flagging what did not. |
| 18–35 | Breakout round 1 | Groups run their assigned vignette with a naive prompt — literally "what's the diagnosis?" — and record the output verbatim. |
| 35–52 | Breakout round 2 | Same vignette, structured prompt. Record output. Then score both against the answer key, which is released at 35 minutes. |
| 52–65 | Verification | Groups check two specific factual claims from the better output against a source — MDCalc, a guideline, or PubMed. Post findings to chat. |
| 65–75 | Close | Report-back and the standing question. |

**Deliverable:** one shared document per group containing both outputs
side-by-side, the scored comparison, and the result of the two verification
checks.

## The structured prompt scaffold

Teach this as a shape, not a script. Five elements, and the fifth is the one
students skip and the one that matters most:

> **Role.** "You are assisting a physician preparing for a case discussion."
> **Context.** The vignette, in clinical language — "epigastric pain radiating to the back," not "stomach pain."
> **Task.** "Give a ranked differential with the three findings that most support and most oppose each entry."
> **Format.** "Table. One row per diagnosis."
> **Uncertainty.** "Where the vignette lacks information you would need, say what is missing instead of assuming it."

That last line is the whole session in one instruction. Models default to
producing a complete-looking answer from incomplete information, and asking them
to name the gap is the single highest-yield thing a clinician can add to a prompt.
Have students compare outputs with and without it.

## Vignettes

Write four to six, and build each one with a deliberate trap. The traps are what
make the session work:

- **One with a critical omission** — a vignette missing the one piece of history that would change management, to test whether the model names the gap or invents around it.
- **One where the common answer is wrong** — a presentation that pattern-matches to a frequent diagnosis but has a discriminating feature pointing elsewhere.
- **One with a drug interaction** buried in a medication list, to see whether it surfaces unprompted.
- **One that is genuinely ambiguous**, where the correct output is "these two remain on the differential and here is what distinguishes them." Models tend to over-commit; a student who accepts a confident single answer here has learned something.

Hold an answer key with the discriminating features written out, and release it at
the 35-minute mark so groups score rather than guess.

## Why not to over-teach the prompting

Close the session on the evidence, because it complicates the enthusiasm in a
useful direction.

In a randomized trial of 50 physicians working through clinical vignettes,
physicians given LLM access scored a median 76% versus 74% for those with
conventional resources — an adjusted difference of **+2 points (95% CI −4 to 8,
p=.60)**, which is to say no significant benefit. In the same study **the LLM
working alone scored 16 points higher** than the physicians using conventional
resources (95% CI 2–30, p=.03) (Goh et al., *JAMA Netw Open* 2024;7(10):e2440969,
[doi:10.1001/jamanetworkopen.2024.40969](https://doi.org/10.1001/jamanetworkopen.2024.40969)).

That result is worth ten minutes on its own. The tool was better than the
physicians. The physicians using the tool were not better than the physicians
without it. Something in how clinicians integrate AI output is discarding the
benefit — anchoring on their own initial impression, skimming, or asking the model
to confirm rather than to challenge. Ask the students which of those they did
during the lab, and they will recognize themselves.

The honest summary for a fourth-year: prompting skill is real and worth having,
but the evidence that it makes *physicians* better is not yet there. What the
evidence supports is that the bottleneck is human integration, not model
capability.

## Optional extension

If the cohort is engaged and time allows, add a **model comparison round** — the
same vignette through two or three tools, comparing which cited real sources,
which gave the better differential, and which was most concise. This pairs
naturally with `core-appraisal`, which runs the citation-verification exercise in
depth; if both modules are in the assembly, keep the comparison here brief and let
appraisal do the heavy work.

## Reusable material

`../talks/archive/2024-10-17-prompt-engineering/` (published at
<https://talks.seandavis.net/archive/2024-10-17-prompt-engineering/>) is the
lowest-adaptation-cost item in the entire talks repo for this purpose. Its ten
rules already use clinical examples throughout — providing context with a
hypertensive patient presenting with chest pain, precise language ("epigastric
pain radiating to the back"), differential-diagnosis output formats, few-shot
prompting with medical abbreviation expansion. It is roughly fifteen slides and
needs essentially no rewriting.

The Who/Where/What prompting scaffold in the recovered `ai-safety` deck
(see `../research/talks-drive-decks.md`) is an alternative to the five-element
scaffold above and is already pitched at residents. If `core-centaur-cyborg` is
also in the assembly, use the same scaffold in both so students see it twice
rather than learning two competing structures.

For the published-exercise precedent, Choy et al., *MedEdPORTAL* 2026;22:11621
([doi:10.15766/mep_2374-8265.11621](https://doi.org/10.15766/mep_2374-8265.11621))
is a peer-reviewed, reusable case-based LLM workshop — a 60-minute lecture plus a
100-minute interactive case workshop, run at Harvard with 168 preclinical
students. Worth pulling the full module for its timing and facilitation notes even
though its audience is earlier in training than this one.
