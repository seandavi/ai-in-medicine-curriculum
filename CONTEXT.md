# Course context

The design in `curriculum/` and `modules/` is deliberately free of names, dates and
institutional mechanics so it can be reassembled for any cohort. This file holds the
part that is specific to the CU Anschutz offering, because it exists nowhere else in
the repo and is the first thing you will want when you come back to this cold.

**Last updated: 2026-10-12.** Everything below is operational state and goes stale
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
trying.* Each week has one core chapter plus a menu (week 1 foundations, with no
menu; week 2 prompting lab; week 3 patient communication; week 4 ethics). "Students aim for
5 to 10 hours a week of AI-related learning, 2 to 4 with the book" was the
first budget; with two talks a week it is restated as about 8 to 10 hours
(see the syllabus table). The main hands-on activity is "Learn it with AI" (`course/learn-with-ai.qmd`). The resource log is
replaced by a learning journal of five open questions (decided 2026-10-12:
what I chose to learn; how AI helped or got in the way, with one check; what
surprised me; what changed for me; what I used and whether it was worth it).
Question 5 absorbs the resource log's surviving piece: about three resources
a week, at least one found by the student, with links and a recommend-or-not
line, meant to be low-key (2026-10-09 meeting; three a week decided
2026-10-10). Its answers double as weekly course feedback. Friday groups are open,
student-led discussion (`course/friday-groups.qmd`; scenario cards removed
2026-10-12, ideas kept in issue #95). The Monday hour includes "How
I used AI this week" (the director's own work, shown live). Bias is not core
this offering (menu chapter and possibly a week 3 talk). Why: 2025 students were afraid to use
chatbots and felt lost; see `curriculum/design-constraints.md` constraint 5.
**Next:** revisit each chapter before the week it is used, to cut it to its
framework core and move hands-on work toward success first.

**Week 1 chapter (decided 2026-10-12):** the centaur-or-cyborg chapter is kept
in the repo (`chapters/core-centaur-cyborg.qmd` and its answer key) but no
longer published. Week 1 has one chapter, How these systems work
(`core-foundations`).

- **Week 1 (Oct 12 to 16):** the course director teaches live, Monday to
  Thursday at 10 a.m. Mountain time (decided 2026-10-09): Monday welcome and
  adult learning (from the 2024 Google Slides intro deck); Tuesday history of
  AI; Wednesday what AI is, AI to ML to DL to LLMs (the foundations deck, PR
  #60, trimmed; keep a few slides on overfitting); Thursday a hands-on session,
  "set up your learning with ChatGPT" (decided 2026-10-11, replacing
  "centaur or cyborg, live"): everyone in ChatGPT Edu, working through
  `chapters/plan-your-learning.qmd` (decided 2026-10-12, replacing
  `course/first-session.qmd`): set up a project, have ChatGPT research what
  the field expects, then build a personal four-week plan and journal
  template, structured on OpenAI's "Plan something from start to finish"
  practice. The session schedule moved to the director's talk slides, so the
  session ends with students working. First contact is something useful, not
  a hunt for AI errors, because students arrive wary of chatbots; also
  catches account problems early. Then office hours.
  Friday small groups, from that week's signup. Students read `core-foundations`.
  Weeks 2 to 4 Monday and Wednesday talks are also at 10 a.m.
- **Weeks 2 to 4, each week (decided 2026-10-08):** the course director's
  talks are the main event and each core chapter is their companion ("read it
  after the talk, or instead of it if you missed the talk").
  - Monday, 60 min, live and recorded: "How I used AI this week", then a talk
    on the week's core chapter topic with live demos.
  - Wednesday, 60 min, live and recorded: a talk on a menu chapter or a topic
    beyond the book, sometimes a guest. No class vote (dropped 2026-10-09). The
    open labs stay as self-paced activities.
  - Thursday, 11 to 11:45 a.m., live, not recorded: office hours, drop in
    (no signup; decided 2026-10-09). Learning journal due
    Thursday night.
  - Friday, 60 min: small group, best effort (decided 2026-10-10), one of four slots (10 a.m., 11 a.m., 1 p.m.,
    2 p.m.; up to 15 students each for 49 enrolled; decided 2026-10-09). Whether to use
    breakout rooms is undecided; the book does not mention them.
    Friday October 30 is "bring your clinical stories" (2026-10-09 meeting):
    students bring situations where AI helped or hurt and lead the talk;
    Christina Olson joins two slots, Matt Zuckerman one afternoon slot.
    Which slots is not yet decided.
  - Guest talks: attend or watch one a week (was two, cut so the week still
    adds up; see the syllabus table).
  - Attendance (decided 2026-10-10): aim for about 3 hours a week of sessions,
    live or recorded, chosen by interest, in every week including week 1; Friday
    groups best effort and not counted; register absences per SOM protocols.
    Matt agreed in the 2026-10-09 meeting that 6 to 7 lecture hours a week is too
    much; neither co-director commented on the 3-hour figure.
  - Watch and do (decided 2026-10-10): optional hands-on session, Wednesdays
    2 to 3:30 p.m., October 21 and 28 and November 4; content to be announced;
    marked recorded; Sean is responsible for it each week, whoever runs it.
  - Recording (decided 2026-10-09): week 1 lectures, Monday and Wednesday
    talks, guest talks, and Christina Olson's sessions are recorded; office
    hours and Friday small groups are not. Recordings are for catching up;
    they no longer count as attending.
  Starting topic grid (the director's starting point, subject to change):
  week 2, Monday "getting good answers" (prompting lab), Wednesday October 21
  "Professional work with AI: writing and beyond", given by Christina Olson
  (decided 2026-10-09); week 3, Monday talking with patients about AI,
  Wednesday to be announced, bias and equity or building a small tool live;
  week 4, Monday who answers for the note (ethics), Wednesday where this is
  going (workforce, environment) and what you will keep. Open question: bias
  is meant to carry AIM-3 this offering, but as one of two options it may not run;
  since the Friday cards were removed (2026-10-12), nothing guarantees it.
- **Why lectures now (2026-10-08):** the director lectures well (evaluations
  in every course he teaches say he is the best part), and writing a talk
  forces him to make the material good. The earlier rule was "no live
  teaching of chapter content unless week 2 shows students are not doing the
  chapters", on the grounds that October to November is residency interview
  season and recordings plus self-contained chapters keep away students on
  track. Recordings still do that job, so interview season no longer argues
  against talks.
- **Known cost:** the director is live about 6.75 hours a week in weeks 2 to 4
  (Monday 1, Wednesday 1, Thursday 0.75, four Friday slots 4) and writes two
  new talks a week. Watch for this in week 2. A suggestion, not decided: if it
  is too much, the Wednesday talk is the first thing to hand to a guest.
- **Submissions:** Canvas text-entry assignments, one per week, complete or
  incomplete (decided 2026-10-09; replaces the planned Microsoft Form),
  reviewed on Fridays.
- **Canvas (built 2026-10-09):** modules Start here and Weeks 1 to 4, each
  linking the Zoom meeting and the week's chapters on aim.seandavis.net plus
  the journal assignment; calendar events for every live session; drop-in
  office hours every Thursday 11 to 11:45 a.m., titled with the instructor's
  name ("Office hours: Sean Davis") so other instructors can add their own;
  a Canvas signup (appointment group) for every Friday (10 a.m., 11 a.m.,
  1 p.m., 2 p.m., up to 15 each, one time per student); students sign up again
  each week, so groups change from week to week (decided 2026-10-10, replacing
  one choice on October 16 plus plain events for later Fridays). The signups
  open when the course starts (Canvas course start date, October 11).
  Guest talks (from the lecturer signup sheet, 2026-10-09), on the Canvas
  calendar and in the week 3 and 4 modules: Matt DeCamp, ethics (Tue Oct 27,
  1 p.m.); Mike Rosenberg, cardiology (Thu Oct 29, 1 p.m.); Elizabeth Kudron,
  pediatrics (Mon Nov 2, 11 a.m.); Sorabh Singhal, psychiatry (Mon Nov 2,
  1 p.m.). Added later the same day: Dan Denman, AI in neuroscience (Wed
  Oct 21, 1 p.m.); Matt Zuckerman, AI in medical education (Thu Oct 22,
  1 p.m.). All agreed to recording. Christina Olson's workshop: moved
  2026-10-12 to Mon Oct 26, 10 a.m. to noon (about 90 minutes, breakout rooms;
  title to come), replacing the course director's week 3 Monday talk. CT Lin
  took Tue Oct 27, 11 a.m. (signup sheet, 2026-10-12): "I'm Sorry Dave, I'm
  Afraid I Can't Do That (AI, Sepsis, Inbasket Replies)", recording OK.
  Home page rewritten 2026-10-09 (Canvas keeps the old version in the page's
  history): points to the book and the modules, states the schedule, the
  attendance rule (expected, flexible; register absences with the SOM), drop-in office
  hours, and the made-up-cases rule; links this year's three standing
  discussions (created the same day) instead of last year's course; the
  syllabus link was the book. School resource sections unchanged.
  **Published to students 2026-10-09, with the book hidden** (the author wants
  the calendar out first; the book still needs work). Hidden, to turn back on
  later: every module item linking aim.seandavis.net and the "The course
  book", "Core chapter", and "Menu (optional)" headers (unpublished items;
  modules stay published); book links removed from calendar events, the
  Friday signup, the home page (syllabus section says "posted soon"), and
  the ChatGPT Edu page. Journal instructions are written into each journal
  assignment instead of linking the book. Last year's four published pages
  were unpublished. Book branches are not pushed. Last year's
  assignments are unpublished, not deleted. The course is still unpublished. A custom submission and chatbot app is a
  post-course project; start CU's data-use review early.
- **Chat channel:** Discord (decided 2026-10-09 in the meeting with Christina
  Olson and Matt Zuckerman: every class already has its own student Discord,
  and students do not use Teams much). Server "Frontier of AI in Medicine
  2026" (reused from Sean's September server, renamed; teal heartbeat-to-
  network icon): #welcome (welcome post: unofficial, Canvas is official,
  made-up cases only), #general, #resources, #show-and-tell, General voice.
  Framed as an unofficial experiment; some phases discourage course
  directors from contacting students outside Canvas. Students not yet
  invited. The Teams team created earlier the same day (Sean, Maritza,
  Christina, Matt) is superseded.
  Canvas stays the official record (announcements, calendar, journals).
  Canvas: Announcements is the one-way channel (now shown in the menu; it had
  been hidden) plus one discussion, "General Questions", linked from the home
  page. Students cannot start new topics, only reply there.
  Each week's module lists the Friday small group (published placeholder
  linking that Friday on the calendar; week 1 says to sign up first). Random and Social
  discussions unpublished (2026-10-09).

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
