# Delivery modes — an untested idea

**Status: idea, not decision.** Nothing here has been run with students, costed, or
agreed with the co-directors. It exists because two questions kept recurring — *which
sessions actually need everyone in the Zoom at the same time?* and *could a chat
interface guide a student through an exercise alone?* — and the answers are worth
writing down before they get lost. Read it as a proposal to argue with. The default
assembly in `schedule.md` remains the plan of record: eleven modules, eleven live
sessions.

Two things would have to be true before any of this is worth building, and neither
has been checked: that students who miss a session would actually use an async path
rather than skipping it, and that the CQI reviewers count async participation as
participation. If either is false, this file is a dead end and should be deleted.

## Part 1 — Which sessions need to be live

Every module is written as one live Zoom session. But the sessions differ in *what*
the live time buys, and only some of them break when you take the synchronous group
out. Three tiers, arguable at the boundaries:

### Tier 1 — The interaction is the content

| Module | Why it cannot go async |
|---|---|
| `core-patient-communication` | Rotating triads. Someone has to be the frightened patient, and the whole point of the session is that the words land differently than the student meant them. |
| `core-ethics-regulation` | The moot court needs live opposition, and the class vote is what makes the four verdicts mean anything. |
| `enrichment-workforce-economics` | Same shape — opposed positions built from a packet, rebuttal, class poll. |
| `core-centaur-cyborg` | The value is cross-group disagreement on the eight-task sort, plus the loop where Breakout A's posted concerns seed the talk at minute 18. Borderline: the sort itself could be prepped alone. |

### Tier 2 — Needs a cohort, but not synchrony

The deliverable is a class-wide aggregate. An aggregate can fill up over 48 hours as
well as over 20 minutes.

| Module | The cohort-dependent part |
|---|---|
| `core-appraisal` | The class-wide fabrication rate, pooled from per-pair citation sheets. |
| `core-bias-equity` | The proxy table, one row per case, assembled from the group worksheets. |
| `enrichment-environment` | "No numbers from the instructor until every group has committed to one" is a *gate*, not a meeting. |
| `core-foundations` | Group screen-share on Playground is convenience; the deliverable is one slide per group. |

### Tier 3 — Solo work currently wrapped in a Zoom

| Module | The only live elements |
|---|---|
| `enrichment-prompting-lab` | Answer-key release at minute 35; report-back. |
| `enrichment-rag-notebooklm` | Part B is explicitly solo already. |
| `enrichment-agentic-coding` | The showcase, and it is five volunteers. |

**Count: three hard, four if `core-centaur-cyborg` is counted.** In the default
eight-session assembly that is three of eight — `core-patient-communication`,
`core-ethics-regulation`, `enrichment-workforce-economics` — plus
`core-centaur-cyborg` on the boundary.

The obvious consequence, if the tiering holds: Tier 2 and Tier 3 could run as async
work with a shorter live report-back. That is also a partial answer to the problem
the modular design already anticipates — a third of the class misses week two — since
a missed async module can be completed late, and a missed Zoom cannot.

The obvious risk: an ungraded elective with async components is an elective that
students skip entirely. The live session is a weak commitment device, but it is the
only one this course has.

## Part 2 — A chat interface as the async path

The idea is deliberately small: **the module files are already the tutor's script.**
Each one contains the session plan in blocks, the worksheet, the rubric, the answer
key, and facilitation notes naming the failure modes to watch for — which is what a
guide needs and is otherwise the expensive part of building one.

So the proposal is a configuration, not a build. On the Open WebUI instance described
as option B in `CONTEXT.md`, one saved model per module, whose system prompt is the
module `.md` verbatim plus stage direction:

```
You are running <module> with one MS4, working alone, at their pace.
Follow the session plan's blocks in order. One block at a time.
Do not advance until they have produced that block's artifact.
Do not reveal the answer key (or the sourced figures) until they commit to an answer.
Close with the module's standing question. Do not accept a one-word answer to it.
End by emitting their artifact as a markdown block they can paste into the shared board.
```

No content authoring, and the module files stay the single source of truth — editing
a module edits the tutor. Three consequences that come free:

**Reflection is already written.** Every module ends on the standing question — *what
does this change about how you'll practice?* — and several carry an `AIM-X` written
close. In a Zoom, 35 of 40 students answer that silently or not at all. A tutor that
will not end the session without an answer gets more reflection than the live version,
not less.

**Deeper learning is the RAG layer already under consideration.** Same instance,
corpus = `research/` plus the readings. "Why does Obermeyer matter here" gets answered
from the cited sources rather than from model memory — which also makes the tool an
instance of the thing `enrichment-rag-notebooklm` teaches.

**A standardized-patient bot for the one session that can never go async.** The six
scenario cards in `core-patient-communication` are already written as patient roles
with a stated position, a motivation, and one detail the patient will not volunteer.
That is a system prompt. Students could rehearse a disclosure conversation privately
before having it in front of peers. This does not replace the live triads — it lowers
the cost of the first attempt. `enrichment-agentic-coding` already lists an OSCE bot
as an alternate build, so the pattern is not new to this repo.

### The week-2 sentence

`CONTEXT.md` sets the test: *before building anything, write the sentence that says
what a student does with it in week 2.* For this idea the sentence is —

> A student who missed the appraisal session opens the appraisal tutor, runs the
> fabrication hunt alone, and posts their scored citation sheet into the class-wide
> rate.

That sentence was easy to write, which by the stated rule is the argument for
building it. It is not evidence that a student would actually do it.

### What this would not have

No auth, no per-student state, no grading, no LMS integration. The transcript is the
artifact and the student keeps it, consistent with the ungraded design.

The answer key sits in an extractable system prompt. In a graded course that would be
disqualifying; here there is nothing to win by extracting it. If a student does it
anyway, the fix is two saved models per gated module rather than an access-control
layer.

## Open questions

- Does an async completion count as participation for the CQI? Unknown, and it
  determines whether this is a real alternative or just a make-up mechanism.
- Does the Open WebUI instance actually deliver the one-URL-no-accounts property that
  option B in `CONTEXT.md` claims? The constraint is hard — anything with a login
  re-creates the LMS problem.
- Is the report-back worth keeping as a separate short live session, or does it
  collapse into the next module's opening block?
- Would a single tutor over the whole course beat eleven per-module tutors? Fewer
  things to maintain, but the per-module system prompt is what makes the tutor follow
  a script rather than chat.
