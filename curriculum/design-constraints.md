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
   *(Amended 2026-10-08: in weeks 2 to 4 of fall 2026 the course director's
   Monday and Wednesday talks are lectures with live demonstrations, by
   choice. See constraint 5. The rule still holds for Friday groups and for
   guests.)*
4. **Free tools only, no installs.** Institutional accounts where available;
   otherwise browser-based free tiers. Cost is an equity problem, not a
   footnote — see the `pricing` fragment in the talks repo.
5. **Skill and confidence first; appraisal inside the use.** *(Revised
   2026-10-07; this replaces "critical appraisal over tool training".)* The
   course's aim is that students leave confident and practised at using AI in
   their own work, and able to talk about it with colleagues and patients.
   "It is your job to learn where AI helps your work; you learn that by
   trying." Checking is taught as part of using a tool well, not as a reason
   to avoid it. The chapters are a framework (one core chapter a week plus a
   menu), not a curriculum that teaches everything; less is better.
   **Why it changed:** students in the 2025 offering said they were afraid to
   use chatbots and felt the course lacked structure. An independent review
   of this book (`research/independent-review-2026-10-08.md`) found about two
   hours of hands-on chatbot use across the whole course, most of it designed
   to make the tool fail. Surveys show students are already told AI makes
   mistakes; what they lack is confidence (`research/student-interests-survey-2026-10-07.md`).
   The original reasoning still holds in part: products change, so teach the
   habit of finding where a tool helps, not a product.

   **Amended 2026-10-08: lectures are the weekly main event; chapters are
   the companion.** In weeks 2 to 4 the course director gives two talks a
   week (Monday on the core chapter's topic, Wednesday on a menu chapter or
   a topic beyond the book), live and recorded, with demonstrations on
   screen. Each core chapter goes with its talk: read it after the talk, or
   instead of it if you missed the talk. Recordings count as attending.
   "Learn it with AI" stays the main hands-on activity.
   **Why:** the director lectures well (evaluations in every course he
   teaches say he is the best part), and writing a talk forces him to make
   the material good. Until then the plan (`CONTEXT.md`, 2026-10-07) was
   that the chapters carry the teaching, with no live teaching of chapter
   content, because October to November is residency interview season. Recordings
   answer that concern, so it no longer rules out talks.
   **Cost:** about 5.75 live hours a week for the director, plus two new
   talks a week. Constraint 3's "no 50-minute lecture blocks" is set aside
   for these talks.
