# Course context

The design in `curriculum/` and `modules/` is deliberately free of names, dates and
institutional mechanics so it can be reassembled for any cohort. This file holds the
part that is specific to the CU Anschutz offering, because it exists nowhere else in
the repo and is the first thing you will want when you come back to this cold.

**Last updated: 2026-09-01.** Everything below is operational state and goes stale
fast — check it before acting on it.

## The offering

**IDPT 8079 — The Frontier of AI & Medicine.** A fourth-year selective at the
University of Colorado Anschutz School of Medicine. ~40 MS4s, Zoom-only, ungraded.
This repo is the redesign; the course has run in prior years, and the AY 25-26
evaluation data exists (see *Evaluation* below).

**Dates for the next offering are not yet fixed.** Nothing downstream — guest
invitations, pre-work account lists, the CQI cycle — can move until they are. Treat
this as the first blocking question, not a detail.

## People

| Role | Who |
|---|---|
| Course director | Sean Davis |
| Co-directors | Christina Olson (pediatric hospitalist; Telehealth Medical Director, Children's Colorado) · Matt Zuckerman (emergency medicine) |
| Dean-level champion | Shanta Zimmer |
| Course coordinator / CQI | Maritza Casillas |
| Evaluation data | Erin Broening |
| CQI faculty partner | Dr. Stickrath |

Christina Olson is also the driver of a related effort: using an LLM to map PBL
session descriptions against AI/digital-health competencies, for curriculum gap
analysis. That work shares this repo's competency framework and is the natural
consumer of `curriculum/competencies.md`.

## Guest lecturers

The design constraints cap guests deliberately — **one per session, two across the
whole course.** Every session is built to pair an idea with an activity, and a
guest-heavy course reverts to lectures without anyone deciding to.

The strongest local source is the **UCHealth Oncology AI Steer Group**, which as of
Aug 2026 was preparing a patient-facing AI tipsheet for system-wide release. Its
members can speak to tools actually deployed in this health system in the last
quarter, which is what an MS4 audience wants and what a survey lecture cannot give.

Candidate matches by module:

| Module | The ask | Candidates |
|---|---|---|
| `core-centaur-cyborg` | Ambient documentation and AI in oncology workflow, as deployed | Wells Messersmith; UCHealth clinical informatics leads |
| `core-patient-communication` | Disclosure conversations; the tipsheet's "why" | UCHealth patient-experience + the tipsheet authors |
| `core-appraisal` | How a tool actually gets approved here — governance and procurement | UCHealth AI governance leads |
| `core-ethics-regulation` | Device boundary, liability, local policy | CU Genomic Governance Committee; SOM compliance |
| `core-bias-equity` | Proxy failure in a model that was really deployed | DBMI faculty |
| `enrichment-workforce-economics` | What AI is doing to a specific specialty's job market | Medical oncology; radiology |
| Platform / infrastructure | The UCHealth AI platform and Snowflake environment | UCHealth AI platform co-director |

**Invitation should specify:** date and time, a 20-minute slot inside a 90-minute
session (never a 50-minute lecture), the competency the session serves, Zoom-only,
~40 MS4s, ungraded — and the actual ask: *bring one thing you deployed and one thing
that went wrong.* Sending them as one batch with the Dean's co-signature converts
maybes to yeses; sending them ad hoc does not.

## Evaluation and CQI

The school runs a Continuous Quality Improvement review on each selective. It covers
course evaluations, syllabus updates, learning objectives and assessments — i.e. it
consumes exactly what this repo produces, so the redesign makes the CQI cheaper
rather than competing with it.

AY 25-26 course evaluation comments and numeric data live in the CU Tableau instance
(`viz-public.cu.edu`, Electives Evaluation Summary Dashboard → set *Select View* to
*By Program* → Selectives), plus a comments spreadsheet from the evaluation office.
**Read that before rebuilding sessions** — it is the only direct evidence of what
landed and what did not.

*Status 2026-09-01: the CQI was postponed on the grounds that reviewing the course
immediately before it is rebuilt reviews a version about to be replaced.*

## Registration

Enrollment runs through OASIS. There is a **recurring defect where students who were
enrolled later show as waitlisted** — observed at least three times in 2026. If
students report enrollment confusion, treat it as the known registrar issue and
escalate once for all affected students rather than replying individually.

## Open design decision — the student-facing tool

Unresolved as of 2026-09-01. The question is not "NotebookLM or custom" but *what
artifact should exist at the end of four weeks that does not exist now.*

**A — Stay on NotebookLM.** Zero build. But no persistence you can see, no shared
collection, and the tool being taught and the tool being used are the same thing.
Fine for `enrichment-rag-notebooklm`; thin as a course spine.

**B — Chat over a course corpus.** A self-hosted Open WebUI instance over the modules,
the readings, the competency framework and the talks archive. Students get one URL:
no accounts, no cost, no install — which satisfies design constraint 4 (free tools,
no installs) better than asking 40 students to register for anything. This pattern is
already proven on adjacent work.

**C — A resource dashboard.** Students *collect* sources into a shared, cited,
browsable board rather than posting into a dead LMS thread. Better pedagogy, because
the artifact is cumulative and visible to the cohort, and because "curate a defensible
source set" is literally AIM-9.

B and C are complementary — C is the collection layer, B the query layer over what
gets collected — but building both before the course runs means neither gets
rehearsed. **Before building anything, write the sentence that says what a student
does with it in week 2.** If that sentence is hard to write, ship B and stop.

A fourth use worth considering: point the agent at the *course* rather than the
content — "which session covers X?", "what did the cohort conclude in week 2?" That
is the PBL curriculum-mapping idea aimed at this curriculum, and it produces
accreditation evidence as a byproduct.

**Hard constraints on anything built here:** no PHI, no accounts, no cost, no install.
Anything requiring a login re-creates the problem the LMS already has.

## Watch items

- **AAMC national AI competencies are expected fall 2026.** The `AIM-*` IDs exist so
  this is a crosswalk rather than a rewrite. Do the mapping when they land.
- **LCME revised Standard 7, Element 7.2** — approved in principle Feb 2025, not yet
  in force, and it requires *experiential* learning for the clinical-application
  domain. That is the accreditation argument for the hands-on modules.
- The 57 verification flags across `research/` and `modules/` — see the README.
