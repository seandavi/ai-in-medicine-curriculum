# Design constraints

The fixed facts about this offering, and what each one forces. Everything in
`modules/` should be checkable against this page.

## The situation

| | |
|---|---|
| Learners | ~40 fourth-year medical students |
| Duration | 4 weeks |
| Delivery | Zoom only, no in-person component |
| Assessment | Ungraded |
| Predecessor | IDPT 8079 (CU Anschutz) — prior lectures inventoried in `research/talks-inventory.md` |

## What each constraint forces

**Fourth-year students, ungraded.** MS4s are post-Step 2, matched or matching,
and pulled in many directions. Attendance is voluntary in practice even when
nominally required, so every session has to justify itself on the day. This
argues for sessions that are useful immediately — things they can use in
residency in a few months — rather than foundational-then-applied sequencing
that only pays off at the end. It also means no exams, no graded assignments,
and no busywork: participation is the only currency, and it is earned, not
compelled.

**~40 students on Zoom.** Too many for one conversation, fine for breakouts of
4–6. Plenary discussion will be silence unless it is seeded — polls, chat
waterfalls, or a named cold-call convention agreed to up front. Any hands-on
activity has to survive 40 people on 40 different machines with no one able to
look over a shoulder, which rules out anything requiring local installs and
argues for browser-based tools.

**Zoom, not in-person.** Attention decays faster than in a room. Plan in
15–20 minute blocks with a change of mode at each boundary — talk, then do,
then discuss. Breakout rooms are the only way to get real participation at this
size. Screen-share demos work; silent independent work does not.

**4 weeks.** Short enough that a linear survey would cover a little of
everything and stick to nothing. Better to pick a small number of competencies
and hit each more than once, in different modes.

## Design commitments that follow

1. **Modular, not sequential.** Each module stands alone with its own
   competency mapping, so sessions can be reordered, swapped, or dropped
   without breaking what follows. Some students will miss weeks; missing week 2
   must not make week 3 incomprehensible.
2. **Core plus enrichment.** A core spine that maps to the consensus
   competencies, plus enrichment modules (agentic coding, environmental impact,
   social and economic impact, ethics) that can be swapped in as interest and
   time allow.
3. **Every session does something.** No 50-minute lecture blocks. Each session
   pairs an idea with an activity that produces an artifact or a judgment.
4. **Free tools only, no installs.** Institutional accounts where available;
   otherwise browser-based free tiers. Cost is an equity problem, not a
   footnote — see the `pricing` fragment in the talks repo.
5. **Critical appraisal over tool training.** Specific products will be
   obsolete before these students finish residency. The durable skill is
   judging whether an AI claim or tool deserves trust.
