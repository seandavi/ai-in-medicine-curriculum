# Course context

The design in `curriculum/` and `modules/` is deliberately free of names, dates and
institutional mechanics so it can be reassembled for any cohort. This file holds the
part that is specific to the CU Anschutz offering, because it exists nowhere else in
the repo and is the first thing you will want when you come back to this cold.

**Last updated: 2026-10-08.** Everything below is operational state and goes stale
fast. Check it before acting on it.

## The offering

**IDPT 8079: The Frontier of AI & Medicine.** A fourth-year selective at the
University of Colorado Anschutz School of Medicine. 49 MS4s enrolled for fall 2026
(Canvas, 2026-10-07), Zoom-only, ungraded.
This repo is the redesign; the course has run in prior years, and the AY 25-26
evaluation data exists (see *Evaluation* below).

**Fall 2026 offering: October 12 to November 6, 2026** (Canvas course IDPT 8079
A39F, unpublished as of 2026-10-07; its modules and assignments are still the 2025
copy). The student-facing week-by-week plan is in `course/syllabus.qmd`.

## Delivery, fall 2026 (decided 2026-10-07)

**Refocus (decided 2026-10-07/08): skill and confidence first.** The course's
mantra: *it is your job to learn where AI helps your work, and you learn that by
trying.* Each week has one core chapter plus a menu (week 1 centaur-cyborg; week
2 prompting lab; week 3 patient communication; week 4 ethics). "Students aim for
5 to 10 hours a week of AI-related learning, 2 to 4 with the book" was the
first budget; with two talks a week it is restated as about 8 to 10 hours
(see the syllabus table). The main hands-on activity is "Learn it with AI" (`course/learn-with-ai.qmd`). The resource log is
replaced by a learning journal. Friday groups practise conversations about AI
from scenario cards (`course/friday-groups.qmd`). The Monday hour includes "How
I used AI this week" (the director's own work, shown live). Bias is not core
this offering (Friday card instead). Why: 2025 students were afraid to use
chatbots and felt lost; see `curriculum/design-constraints.md` constraint 5.
**Next:** revisit each chapter before the week it is used, to cut it to its
framework core and move hands-on work toward success first.

- **Week 1 (Oct 12 to 16):** the course director teaches live: welcome and adult
  learning (from the 2024 Google Slides intro deck), history of AI, then AI to ML
  to DL to LLMs (the foundations deck, PR #60, trimmed; keep a few slides on
  overfitting). Students read `core-foundations` and `core-centaur-cyborg`.
- **Weeks 2 to 4, each week (decided 2026-10-08):** the course director's
  talks are the main event and each core chapter is their companion ("read it
  after the talk, or instead of it if you missed the talk").
  - Monday, 60 min, live and recorded: "How I used AI this week", then a talk
    on the week's core chapter topic with live demos.
  - Wednesday, 60 min, live and recorded: a talk on a menu chapter or a topic
    beyond the book. The class votes on the topic from a short list, the week
    before. This replaces the voted mid-week open lab; the open labs stay as
    self-paced activities and as Wednesday topic candidates.
  - Thursday, 45 min, live, not recorded: office hours. Learning journal due
    Thursday night.
  - Friday, 60 min: small group, required, one of three slots, breakout rooms
    of 4 to 5 with the same members each week.
  - Guest talks: attend or watch one a week (was two, cut so the week still
    adds up; see the syllabus table).
  - Recordings count as attending.
  Starting topic grid (the director's starting point, subject to change):
  week 2, Monday "getting good answers" (prompting lab), Wednesday vote
  between AI for scholarly writing (co-led with a co-director) and answers
  grounded in real sources; week 3, Monday talking with patients about AI,
  Wednesday vote between bias and equity and building a small tool live;
  week 4, Monday who answers for the note (ethics), Wednesday where this is
  going (workforce, environment) and what you will keep. Open question: bias
  is meant to carry AIM-3 this offering, but as a vote option it may not run;
  the week 2 Friday bias card is the only certain coverage.
- **Why lectures now (2026-10-08):** the director lectures well (evaluations
  in every course he teaches say he is the best part), and writing a talk
  forces him to make the material good. The earlier rule was "no live
  teaching of chapter content unless week 2 shows students are not doing the
  chapters", on the grounds that October to November is residency interview
  season and recordings plus self-contained chapters keep away students on
  track. Recordings still do that job, so interview season no longer argues
  against talks.
- **Known cost:** the director is live about 5.75 hours a week in weeks 2 to 4
  (Monday 1, Wednesday 1, Thursday 0.75, three Friday slots 3) and writes two
  new talks a week. Watch for this in week 2. A suggestion, not decided: if it
  is too much, the Wednesday talk is the first thing to hand to a guest.
- **Submissions:** Microsoft Form (university login, data stays in CU Microsoft
  365), reviewed on Fridays. A custom submission and chatbot app is a
  post-course project; start CU's data-use review early.
- **Chat channel:** undecided. Microsoft Teams preferred over Discord (no new
  accounts, stays inside the institution).

## People

| Role | Who |
|---|---|
| Course director | Sean Davis |
| Co-directors | Christina Olson (pediatric hospitalist; Telehealth Medical Director, Children's Colorado): one two-hour session with students in fall 2026 · Matt Zuckerman (emergency medicine): one or two lectures. The course director runs everything else alone. |
| Dean-level champion | Shanta Zimmer |
| Course coordinator / CQI | Maritza Casillas |
| Evaluation data | Erin Broening |
| CQI faculty partner | Dr. Stickrath |

Christina Olson is also the driver of a related effort: using an LLM to map PBL
session descriptions against AI/digital-health competencies, for curriculum gap
analysis. That work shares this repo's competency framework and is the natural
consumer of `curriculum/competencies.md`.

## Guest lecturers

**Fall 2026: the two-guest cap is lifted for weeks 2 to 4** (decided 2026-10-07).
The course director teaches week 1; guests give 45 to 50 minute talks plus
questions in weeks 2 to 4, from a signup sheet (Google Sheet
"ai-in-medicine-lecturer-signup": Monday to Thursday, 9, 10, 11 and 1, Oct 19 to
Nov 6, 48 slots). The cap guarded against the course turning back into lectures.
Since 2026-10-08 the director's own talks are the main event by choice, so the
cap's worry now applies to guests only: students are asked to attend or watch
one guest talk a week, not two. Confirmed as of
2026-10-07: Mike Rosenberg (cardiology, Thu Oct 29, 1 pm), Elizabeth Kudron
(pediatrics, Mon Nov 2, 11 am), Sorabh Singhal (psychiatry, Mon Nov 2, 1 pm).

The original reasoning for the cap, kept for future offerings: every session pairs
an idea with an activity, and a guest-heavy course reverts to lectures without
anyone deciding to.

The strongest local source is the **UCHealth Oncology AI Steer Group**, which as of
Aug 2026 was preparing a patient-facing AI tipsheet for system-wide release. Its
members can speak to tools actually deployed in this health system in the last
quarter, which is what an MS4 audience wants and what a survey lecture cannot give.

Candidate matches by module:

| Module | The ask | Candidates |
|---|---|---|
| `core-centaur-cyborg` | Ambient documentation and AI in oncology workflow, as deployed | Wells Messersmith; UCHealth clinical informatics leads |
| `core-patient-communication` | Disclosure conversations; the tipsheet's "why" | UCHealth patient-experience + the tipsheet authors |
| `core-appraisal` | How a tool actually gets approved here: governance and procurement | UCHealth AI governance leads |
| `core-ethics-regulation` | Device boundary, liability, local policy | CU Genomic Governance Committee; SOM compliance |
| `core-bias-equity` | Proxy failure in a model that was really deployed | DBMI faculty |
| `enrichment-workforce-economics` | What AI is doing to a specific specialty's job market | Medical oncology; radiology |
| Platform / infrastructure | The UCHealth AI platform and Snowflake environment | UCHealth AI platform co-director |

**Invitation should specify:** date and time, a 20-minute slot inside a 90-minute
session (never a 50-minute lecture), the competency the session serves, Zoom-only,
~40 MS4s, ungraded; and the actual ask: *bring one thing you deployed and one thing
that went wrong.* Sending them as one batch with the Dean's co-signature converts
maybes to yeses; sending them ad hoc does not.

## Evaluation and CQI

The school runs a Continuous Quality Improvement review on each selective. It covers
course evaluations, syllabus updates, learning objectives and assessments. That is, it
consumes exactly what this repo produces, so the redesign makes the CQI cheaper
rather than competing with it.

AY 25-26 course evaluation comments and numeric data live in the CU Tableau instance
(`viz-public.cu.edu`, Electives Evaluation Summary Dashboard → set *Select View* to
*By Program* → Selectives), plus a comments spreadsheet from the evaluation office.
**Read that before rebuilding sessions**: it is the only direct evidence of what
landed and what did not.

*Status 2026-09-01: the CQI was postponed on the grounds that reviewing the course
immediately before it is rebuilt reviews a version about to be replaced.*

## Registration

Enrollment runs through OASIS. There is a **recurring defect where students who were
enrolled later show as waitlisted**, observed at least three times in 2026. If
students report enrollment confusion, treat it as the known registrar issue and
escalate once for all affected students rather than replying individually.

## Open design decision: the student-facing tool

Unresolved as of 2026-09-01. The question is not "NotebookLM or custom" but *what
artifact should exist at the end of four weeks that does not exist now.*

**A. Stay on NotebookLM.** Zero build. But no persistence you can see, no shared
collection, and the tool being taught and the tool being used are the same thing.
Fine for `enrichment-rag-notebooklm`; thin as a course spine.

**B. Chat over a course corpus.** A self-hosted Open WebUI instance over the modules,
the readings, the competency framework and the talks archive. Students get one URL:
no accounts, no cost, no install, which satisfies design constraint 4 (free tools,
no installs) better than asking 40 students to register for anything. This pattern is
already proven on adjacent work.

**C. A resource dashboard.** Students *collect* sources into a shared, cited,
browsable board rather than posting into a dead LMS thread. Better pedagogy, because
the artifact is cumulative and visible to the cohort, and because "curate a defensible
source set" is literally AIM-9.

B and C are complementary (C is the collection layer, B the query layer over what
gets collected), but building both before the course runs means neither gets
rehearsed. **Before building anything, write the sentence that says what a student
does with it in week 2.** If that sentence is hard to write, ship B and stop.

A fourth use worth considering: point the agent at the *course* rather than the
content: "which session covers X?", "what did the cohort conclude in week 2?" That
is the PBL curriculum-mapping idea aimed at this curriculum, and it produces
accreditation evidence as a byproduct.

**Hard constraints on anything built here:** no PHI, no accounts, no cost, no install.
Anything requiring a login re-creates the problem the LMS already has.

## Watch items

- **AAMC national AI competencies are expected fall 2026.** The `AIM-*` IDs exist so
  this is a crosswalk rather than a rewrite. Do the mapping when they land.
- **LCME revised Standard 7, Element 7.2**: approved in principle Feb 2025, not yet
  in force, and it requires *experiential* learning for the clinical-application
  domain. That is the accreditation argument for the hands-on modules.
- The 57 verification flags across `research/` and `modules/`; see the README.

## Student tool access

Confirmed 2026-09-07: students have institutional ChatGPT Edu and Microsoft
Copilot accounts. Chapters can assume one general-purpose chatbot without a
signup step. Confirmed by the course director 2026-10-07: ChatGPT Edu and
Copilot are covered by a business associate agreement for clinical use when
signed in with university credentials (not through personal accounts). The
course rule is unchanged: course exercises use made-up patients only.
