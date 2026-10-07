# Competency coverage map

Date: 2026-10-07. Repository state: `main` at commit `9021d25`.

This file maps every piece of student-facing material in the book to our own
competency framework (`curriculum/competencies.md`, AIM-1 to AIM-9 and AIM-X)
and to the published medical-student AI competency frameworks. It is meant as
the basis for the coverage table and the assessment table in a curriculum
paper. No chapter was edited.

Short version:

- The default four-week course meets the coverage rules. AIM-1 to AIM-6 are
  each taught and checked at least once. AIM-4 recurs five times and AIM-5
  twice.
- The rule is met narrowly in two places. AIM-6 (talking to patients) rests on
  one chapter. AIM-3 (bias and equity) gets a second chapter only if the cohort
  picks the environment chapter in week 4.
- AIM-8 (health data science) is not the main subject of anything. No chapter
  teaches sensitivity, specificity, or calibration as a skill. The only hands-on
  data activity is an unwritten open-lab idea.
- Subtitle tags under-report what several chapters teach. The biggest misses:
  critical appraisal is a main subject of the environment, workforce, and
  retrieval chapters, and none of them is tagged AIM-2.
- Every Check in the book is self-scored, and the course is ungraded. A paper
  should say "self-assessed against a rubric", not "assessed".
- The AAMC has not yet published its national AI competencies. On 2026-10-07
  its project page still says "Target release of the final report is fall
  2026" and links no report or draft.

---

## 1. Method

### What was read

- Design files: `CLAUDE.md`, `CONTEXT.md`, `curriculum/competencies.md`,
  `curriculum/chapter-plan.md`, `research/competency-frameworks.md`,
  `_quarto.yml`, `index.qmd` (its coverage table), `course/syllabus.qmd`, and
  `appendix/instructors.qmd` (its module tables and variants).
- All eleven chapters in `chapters/`. For each one I read the subtitle tags,
  the "What you'll learn" objectives, the whole Do, the Check rubric, and the
  standing question ("What this changes for you"). I searched the reading
  sections for specific topics (for example AUC, calibration, dataset shift,
  IRB, reporting guidelines, alert fatigue, data scientists) rather than
  reading every line of them.
- `course/patient-information.qmd` and `course/resource-log.qmd` in full.
- `appendix/open-labs.qmd` in full. `appendix/resources.qmd` by section.

### How each cell was judged

Each cell says how strongly one piece of material serves one competency.

| Code | Meaning | Test used |
|---|---|---|
| **P** (primary) | Taught and checked | A numbered objective targets it, *and* the Do or a row of the Check asks the student to produce something that shows it |
| **S** (secondary) | Taught but not checked | Real teaching in the reading or the Do, but no objective or no Check row targets it; or it is checked only as a step toward another competency |
| **M** (mention) | Named in passing | A sentence, a link to another chapter, a safety callout, or a reading suggestion |
| blank | Not there | |

Three rules of thumb kept the grading consistent:

1. When one objective serves two competencies, the competency whose
   definition in `competencies.md` names the skill most directly gets P and
   the other gets S. Example: the train-versus-test exercise in the
   foundations chapter is P for AIM-1 and AIM-2, and S for AIM-8.
2. The "No patient information, ever" callout appears in every Do. On its own
   it counts as M for AIM-4. It counts as S or P only where the page teaches
   the rule (business associate agreements, Safe Harbor) and checks it.
3. Every chapter closes with the standing question, *what does this change
   about how you'll practice?* That written reflection counts as S for AIM-X
   everywhere. AIM-X is P only where an objective and a Check row ask for a
   personal position (for example "the part of clinical judgment I will not
   hand over").

### What "assessed" means here

The course is ungraded (`course/syllabus.qmd`). Each chapter's Check is a
rubric the student scores alone. Answer keys exist in `_answers/` for a
planned tutor, which has not shipped. The only piece of work anyone else marks
is the resource log, marked complete or incomplete. So in this file, "checked"
means "self-assessed against a written rubric with stated meets and falls-short
levels". That is weaker than graded assessment, and a paper should say so.

### Limits of the method

One reader (an AI model, see section 7) made every judgment. Boundary cases
are noted in the tables. A second rater on a sample of cells would make the
matrix publishable.

---

## 2. Matrix A: our materials against AIM-1 to AIM-9 and AIM-X

Rows follow the book order in `_quarto.yml` for chapters, then the course
pages and appendices. "Tags" is what the subtitle claims.

| # | Material | Tags | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | X |
|---|---|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| | **Week 1** | | | | | | | | | | | |
| 1 | How these systems work (`core-foundations`) | 1, 2 | **P** | **P** | M | M | S | M | | S | M | S |
| 2 | Centaur or cyborg (`core-centaur-cyborg`) | 5, X, 4 | | S | | **P** | **P** | S | S | | M | **P** |
| | **Week 2** | | | | | | | | | | | |
| 3 | Critical appraisal (`core-appraisal`) | 2, 9 | **P** | **P** | M | **P** | S | M | S | M | **P** | S |
| 4 | Bias and equity (`core-bias-equity`) | 3 | M | S | **P** | M | M | M | | S | S | S |
| | **Week 3** | | | | | | | | | | | |
| 5 | Agentic coding (`enrichment-agentic-coding`) | 5, 2, 4 | S | **P** | | **P** | **P** | | S | | M | S |
| 6 | Talking to patients (`core-patient-communication`) | 6, 4 | M | S | | **P** | S | **P** | M | | | S |
| | **Week 4** (cohort picks 7 *or* 8) | | | | | | | | | | | |
| 7 | Will AI take your job? (`enrichment-workforce-economics`) | 3, 7 | | **P** | S | S | | | **P** | M | S | **P** |
| 8 | What AI costs the planet (`enrichment-environment`) | 3, X | M | **P** | **P** | | | M | **P** | M | S | S |
| 9 | Ethics, liability, device line (`core-ethics-regulation`) | 4, 7, X | M | S | S | **P** | S | S | S | | S | **P** |
| | **Spare** | | | | | | | | | | | |
| 10 | Prompting lab (`enrichment-prompting-lab`) | 5, 2 | M | **P** | | S | **P** | | | | S | S |
| 11 | Grounding AI in real sources (`enrichment-rag-notebooklm`) | 1, 9 | **P** | **P** | | S | S | | | M | **P** | S |
| | **Course pages** | | | | | | | | | | | |
| 12 | Patient information and AI tools | none | | | | **P** | M | M | | | | |
| 13 | Weekly resource log | none | M | S | M | S | M | M | M | | **P**\* | S |
| | **Appendices** | | | | | | | | | | | |
| 14a | Open lab: "Hear it, draft it, check it" (scribe, written out) | none | S | S | | S | S | | M | | | S |
| 14b | Open labs: the eight "Idea" labs | none | M | M | M | | M | M | | M | M | |
| 15 | Starter resources | none | M | M | M | M | M | M | M | | M | M |

\* The resource log has no objectives callout. It is marked P for AIM-9
because it is the one marked assignment and its whole task is to find, read,
verify, and synthesize literature, with an AI-use disclosure each week. Its
other cells depend on the themes each student picks; the M cells come from its
optional theme list.

The three "Ready" open labs other than the scribe lab point to chapters 10,
11, and 5, so they are covered by those rows.

### Notes on boundary cells

- **Ch 1, AIM-5 = S.** Objective 5 (two rules for the context window) is about
  prompting, and the Check asks what the student will do differently at the
  keyboard. It is graded S because the objective is framed as a limit of the
  mechanism. A stricter reader would give P.
- **Ch 1, AIM-8 = S.** Training versus test data, the training population of
  the eGFR equation, an AUC, and dataset shift are all taught. They are
  checked as AIM-1 and AIM-2 skills, not as data science.
- **Ch 2, AIM-4 = P.** Objective 2 (deskilling, never-skilling, mis-skilling)
  is "automation bias and deliberate skill preservation" from the AIM-4
  definition. Objective 5 (what to document, whom to tell) is checked too.
- **Ch 3, AIM-1 = P.** Objective 2 (why made-up references follow from how the
  text is produced) has its own Check row ("the mechanism"). It repeats
  foundations on purpose.
- **Ch 3, AIM-4 = P.** Objective 5 ("FDA clearance is not evidence of clinical
  performance") has a Check row ("cleared is not validated").
- **Ch 4, AIM-2 = S.** Objective 5 (what a clinician can catch at the bedside,
  and the evidence that explanations do not help) is graded under AIM-3,
  whose definition names black-box models.
- **Ch 7, AIM-3 = S.** The economic material (system cost, "bot wars") and one
  sentence on who bears the job losses are taught and partly checked. No
  objective is about equity.
- **Ch 8, AIM-7 = P.** Objective 5 (a vendor question with a checkable answer,
  for a contract review) is procurement, and it has a Check row.
- **Ch 9, AIM-7 = S.** Predetermined Change Control Plans, contracts, and the
  institutional-policy question are taught. They are checked as regulation
  (AIM-4). Monitoring, human factors, and team roles are not checked.
- **Ch 9, AIM-3 = S.** The Jabbour study of clinicians using a biased model is
  objective 3. It is graded under AIM-4 (automation bias), S for AIM-3.

---

## 3. Matrix B: our materials against the published frameworks

### Which frameworks, and a correction to the brief

`research/competency-frameworks.md` names, at domain level: Russell et al.
[@pmid:36731054], Hunt et al. [@pmid:42120544], Lee et al. [@pmid:38207056],
Singla et al. [@pmid:39557985], DECODE [@pmid:39888625], CAIP
[@pmid:41767172], AI-PACE [@pmid:42141085], the CGEA educator framework, and
the AAMC's stated goals.

**Liaw et al. and Çalışkan et al. are not in that file.** The brief named them
as examples, so they are added here after lookup in PubMed:

- Liaw et al. is *Annals of Family Medicine* **2022**;20(6):559-563
  [@pmid:36443071], not 2023. It proposes six domains for primary care
  clinicians, not specifically for medical students.
- Çalışkan et al. is *PLoS One* 2022;17(7):e0271872 [@pmid:35862401]. PMID
  confirmed. It is an e-Delphi with 60 panellists in round 3 that produced
  **27 competency items with no domains** (23 strong consensus, 4 weak). To map
  it at domain level I grouped the items into seven clusters myself; the
  grouping is mine, not the authors'.

CGEA is a framework for faculty, so it is left out. CAIP is a list of 21
items rather than domains, and AI-PACE is a structure (psychomotor, affective,
cognitive, embedded) rather than content domains, so neither is mapped here.
CAIP's assessment model is used in section 6.

### How to read the tables

Each row is one domain of a published framework. "P in" and "S in" list our
materials by the row numbers of Matrix A. The rating is for the **default
four-week course** (rows 1 to 9, with 7 or 8):

- **Strong**: P in two or more default sessions.
- **Adequate**: P in one default session, or P only through the cohort's week-4
  choice, with S elsewhere.
- **Thin**: S only, or P only in spare chapters, open labs, or the resource log.
- **Gap**: M or nothing.

### B1. Russell et al. 2023, six domains [@pmid:36731054]

| Domain | Our AIM | P in | S in | Rating |
|---|---|---|---|---|
| 1. Basic knowledge of AI | 1 | 1, 3, 11 | 5, 14a | Strong |
| 2. Social and ethical implications | 3, 4 | 2, 3, 4, 5, 6, 8, 9, 12 | 7 | Strong |
| 3. AI-enhanced clinical encounters | 5, 6 | 2, 5, 6, 10 | 1, 3, 9, 14a | Adequate. The skills are taught on made-up cases; using AI inside a real or simulated encounter (scribe, decision support) is only in optional open lab 14a and the live session of chapter 6 |
| 4. Evidence-based evaluation of AI tools | 2, 9 | 1, 3, 5, 7, 8, 10, 11 | 2, 4, 6, 9 | Strong |
| 5. Workflow analysis | 7 | 7 or 8 | 2, 3, 5, 9 | Adequate, by the week-4 choice only |
| 6. Practice-based learning and improvement | X, 9 | 2, 9, 13 | all chapters (standing question) | Adequate for learning; Gap for practice *improvement* (no quality-improvement activity) |

### B2. Hunt et al. 2026, seven domains [@pmid:42120544]

| Domain | Our AIM | P in | S in | Rating |
|---|---|---|---|---|
| AI ethics | 3, 4 | 2, 4, 6, 8, 9 | 7 | Strong |
| AI law and regulation | 4 | 3, 5, 9, 12 | 7 | Strong |
| AI professionalism in healthcare | 4, X | 2, 6, 9 | all | Strong |
| Clinical applications of AI | 5 | 2, 5, 10 | 1, 3, 6, 9, 11, 14a | Adequate (two default sessions, both on made-up cases) |
| Critical appraisal of AI output | 2 | 1, 3, 5, 7, 8, 10, 11 | 4, 6, 9 | Strong |
| Research and innovation in AI | 9 | 3, 11, 13 | 4, 7, 8, 9, 10 | Adequate for using and appraising research; Thin for innovation (chapter 5 builds a tool but does not teach development or validation studies) |
| Theory and foundations of AI | 1 | 1, 3, 11 | 5, 14a | Strong |

### B3. Lee et al. 2024, six domains [@pmid:38207056]

| Domain | Our AIM | P in | S in | Rating |
|---|---|---|---|---|
| 1. Understanding digital health and changes driven by AI | 7, X | 7 | 2, 8, 9 | Adequate if the cohort picks chapter 7; Thin if it picks chapter 8 |
| 2. Fundamental knowledge and skills in medical AI | 1, 5 | 1, 2, 3, 5 | 11 | Strong |
| 3. Ethics and legal aspects | 4 | 2, 3, 5, 6, 9, 12 | 7 | Strong |
| 4. Medical AI application in clinical practice | 5 | 2, 5, 10 | 6, 9, 14a | Adequate |
| 5. Processing, analysing, and evaluating medical data | 8 | none | 1, 4 | Thin. Lee's panel rated this domain optional more often |
| 6. Research and development of medical AI | 9 | 3, 11 | 5 | Thin for development. Also rated optional more often by Lee's panel |

### B4. Liaw et al. 2022, six domains [@pmid:36443071]

| Domain (with the authors' question) | Our AIM | P in | S in | Rating |
|---|---|---|---|---|
| 1. Foundational knowledge ("what is this tool?") | 1 | 1, 3, 11 | 5 | Strong |
| 2. Critical appraisal ("should I use this tool?") | 2 | 1, 3, 5, 7, 8, 10, 11 | 4, 6, 9 | Strong |
| 3. Medical decision making ("when should I use this tool?") | 5, X | 2 | 9, 10 | Adequate. Chapter 2's task sort is the one place this is checked |
| 4. Technical use ("how do I use this tool?") | 5 | 2, 5, 10 | 1, 11, 14a | Adequate |
| 5. Patient communication | 6 | 6 | 2, 9 | Adequate (one session) |
| 6. Awareness of unintended consequences | 3, 4, 7 | 2, 4, 7, 8, 9 | 1 | Strong |

### B5. Çalışkan et al. 2022, 27 items in seven clusters [@pmid:35862401]

Cluster names and item groupings are mine.

| Cluster (item numbers) | Our AIM | P in | S in | Rating |
|---|---|---|---|---|
| AI concepts, how systems are trained, limits, strengths and weaknesses (17, 19, 24, 25, 26) | 1, 2 | 1, 3, 11 | 5 | Strong |
| Data science and statistics basics; data collection, analysis, safety; keeping records AI can process (4, 10, 15, 18, 20) | 8 | none | 1, 4 | Gap for items 4, 10, 18, 20; Thin for 15 |
| Ethics and law (1, 2, 14) | 4 | 2, 3, 5, 6, 9, 12 | | Strong |
| Choosing and using AI for a clinical problem (3, 5, 7, 9, 21, 23) | 5, 2 | 2, 5, 10 | 6 | Adequate |
| Workflow and teamwork with AI developers (8, 12, 22) | 7 | 7 or 8 (item 8 only) | 2, 9 | Gap for items 12 and 22 (working with developers; how physician knowledge feeds development) |
| Keeping up, information literacy, opportunities and threats (6, 11, 13, 16) | 9, X | 3, 7, 13 | all | Strong |
| Explaining AI applications to the patient (27) | 6 | 6 | 2, 9 | Adequate. Note that item 27 reached only *weak* consensus in that panel, while our framework treats it as the course's signature |

### B6. Singla et al. 2024, seven competency areas [@pmid:39557985]

The areas are listed in the abstract. The 107 individual competencies were not
read for this map (see section 7).

| Area | Our AIM | P in | S in | Rating |
|---|---|---|---|---|
| Ethics | 3, 4 | 2, 4, 6, 9 | 7, 8 | Strong |
| Law | 4 | 3, 5, 9, 12 | | Strong |
| Theory | 1 | 1, 3, 11 | | Strong |
| Application | 5 | 2, 5, 10 | 6, 9 | Adequate |
| Communication | 6 | 6 | 2, 9 | Adequate (one session) |
| Collaboration | 7 | none | 2, 5 | Gap. Nothing teaches working with data scientists, informaticists, or other professions |
| Quality improvement | 7 | none | 3, 9 | Gap |

### B7. DECODE 2025, four domains [@pmid:39888625]

DECODE covers digital health as a whole, so some of its content is outside a
course on AI by design.

| Domain | Our AIM | P in | S in | Rating |
|---|---|---|---|---|
| Professionalism in digital health | 4, X | 2, 9, 12 | all | Strong |
| Patient and population digital health | 3, 6 | 4, 6, 8 | 7 | Strong |
| Health information systems | 7 | none | 9, 12 (BAAs, tools inside the EHR) | Thin |
| Health data science | 8 | none | 1, 4 | Thin |

### B8. AAMC

**Status checked 2026-10-07: not published.** Both AAMC project pages
(<https://www.aamc.org/about-us/medical-education/ai-competencies> and
<https://www.aamc.org/about-us/medical-education/cbme/ai-competencies>) say
"Target release of the final report is fall 2026". They describe the project
as in its draft-and-revise and feedback-gathering phases, and link no report
or draft. A web search the same day found no release announcement. So there
is nothing to map yet.

As a placeholder, here are the three stated goals on the project page. They
are goals, not competencies.

| AAMC stated goal | Our AIM | Rating |
|---|---|---|
| A shared foundation in core AI concepts | 1 | Strong |
| Understand the ethical, legal, and professional implications of AI-enabled care | 3, 4, X | Strong |
| Effectively use, evaluate, and collaborate around AI technologies alongside interprofessional teams, data scientists, and health system leaders | 2, 5, 7 | Strong for *use* and *evaluate*; Gap for *collaborate* (same gap as Singla's collaboration area) |

---

## 4. Tag accuracy

A tag is "missing" when the chapter is P for a competency it does not tag. A
tag is "overstated" when the chapter tags a competency it serves only at S.

| Chapter | Tags | Missing tags (P but untagged) | Overstated tags | Comment |
|---|---|---|---|---|
| Foundations | 1, 2 | none | none | Accurate. AIM-8 at S is honestly described in `index.qmd` |
| Centaur or cyborg | 5, X, 4 | none | none | Accurate |
| Critical appraisal | 2, 9 | **AIM-4** (FDA clearance, objective 5), AIM-1 (objective 2) | none | AIM-4 is the one that matters: it changes the recurrence count |
| Bias and equity | 3 | none | none | Accurate. AIM-8 and AIM-9 at S |
| Agentic coding | 5, 2, 4 | none | none | Accurate |
| Talking to patients | 6, 4 | none | none | Accurate |
| Workforce | 3, 7 | **AIM-2** (objectives 2 and 3), **AIM-X** (objective 6) | **AIM-3** (S: economics, not equity) | Mostly an appraisal-of-forecasts chapter |
| Environment | 3, X | **AIM-2** (objectives 1 and 2, most of the Do), **AIM-7** (objective 5) | **AIM-X** (S: no objective names it) | The largest mismatch. Its main skill is tracing a quoted number to its source |
| Ethics and regulation | 4, 7, X | none | **AIM-7** (S: checked only as regulation) | AIM-7 is defensible as a tag if the Check gained one governance row |
| Prompting lab | 5, 2 | none | none | Accurate |
| Grounding in real sources | 1, 9 | **AIM-2** (objective 5, the citation scoring) | none | Its central exercise is appraisal |
| Patient information page | none | **AIM-4** | | It has objectives and a self-check, so it could carry a tag |
| Resource log | none | **AIM-9** | | The one marked assignment carries no tag |

Related inconsistencies found while checking:

- `index.qmd` says its coverage table is "from each chapter's own subtitle and
  objectives". It matches the subtitles exactly, so it reflects the tags, not
  the objectives.
- `index.qmd` says AIM-4 appears four times in the default order;
  `appendix/instructors.qmd` says three. By the tags, four is right
  (centaur, agentic coding, patient communication, ethics). By content it is
  five, adding appraisal.
- `curriculum/competencies.md` says AIM-7 to AIM-9 "belong to enrichment
  modules". In practice two core chapters carry them as tags (appraisal:
  AIM-9; ethics: AIM-7). That is fine, but the rule text and the book
  disagree.
- `_quarto.yml` puts both chapter 7 and chapter 8 in the "Week 4" part, while
  the syllabus runs only one of them. A reader of the table of contents will
  count three week-4 sessions.

---

## 5. Gaps and thin spots

### 5.1 Does the default course meet the coverage rules?

Yes. Counting P cells in the eight default sessions (rows 1 to 6 and 9, plus
row 7 or row 8):

| Competency | Rule | P count (with 7 / with 8) | Met? |
|---|---|---|---|
| AIM-1 | at least once | 2 / 2 (foundations, appraisal) | Yes |
| AIM-2 | at least once | 4 / 4 | Yes |
| AIM-3 | at least once | 1 / 2 (bias; plus environment) | Yes, but with chapter 7 it rests on one session |
| AIM-4 | should recur | 5 / 5 (centaur, appraisal, agentic, patients, ethics) plus the patient information page | Yes |
| AIM-5 | should recur | 2 / 2 (centaur, agentic) | Yes, at the minimum |
| AIM-6 | at least once | 1 / 1 (patients) | Yes, at the minimum |
| AIM-7 | optional | 1 / 1 (by week-4 choice) | n/a |
| AIM-8 | optional | 0 / 0 | n/a |
| AIM-9 | optional | 1 / 1 (appraisal) plus the resource log | n/a |
| AIM-X | closing question | 2 / 3 | Yes |

The rule is met by tags alone as well, so the result does not depend on my
grading.

### 5.2 The course variants in `appendix/instructors.qmd`

- **One session a week** (centaur, appraisal, patients, ethics; foundations as
  pre-work; "cover bias inside appraisal"). AIM-3 then depends on content that
  does not exist: the appraisal chapter mentions bias but does not teach it.
  As written, this variant **fails** the AIM-3 rule unless the bias chapter is
  also assigned as pre-work. AIM-1 still passes through appraisal's objective 2.
- **Hands-on cohort** (prompting and retrieval labs replace foundations and
  ethics). Passes. AIM-1 moves to the retrieval chapter. AIM-4 still recurs.
  It loses the course's closing session, though centaur or cyborg keeps an
  AIM-X position.
- **Policy cohort** (both week-4 chapters, foundations as pre-work). Passes.
  AIM-1 is met only through appraisal.

### 5.3 Single points of failure

- **AIM-6** is the course's stated signature and lives in one session.
  `curriculum/competencies.md` calls it the largest gap between consensus and
  practice, and the chapter is the strongest in the book on it. But a student
  who misses session 6 loses it, apart from S-level moments in centaur or
  cyborg (row 8, "answer for the patient") and ethics ("whom to tell").
- **AIM-3** has one dedicated chapter. Whether it gets a second depends on the
  week-4 vote.
- **AIM-7** is reached at P only through the week-4 vote. Either choice gives
  P, so this is safe, but the two chapters reach it in different ways
  (workforce: roles and system cost; environment: procurement).

### 5.4 AIM-8, health data science

No chapter tags AIM-8, and none teaches it as a skill. What exists:

- Foundations teaches training versus test data, the training population, an
  AUC, and dataset shift, in service of AIM-1 and AIM-2.
- Bias asks "who wrote the ground truth" for one case.
- "Sensitivity" appears only in the workforce chapter's mammography history.
  "Calibration" appears only in the pulse-oximeter sense (a device calibrated
  on light skin), not as a property of a risk model.
- Nothing on EHR data, data quality, governance of data, or working with data
  scientists.
- The only hands-on data activity is "Ask questions of a dataset", an open lab
  still at the idea stage.

This is allowed by the coverage rules (AIM-8 is optional), and Lee's Delphi
panel rated the matching domain optional more often. But Çalışkan's panel
reached strong consensus on four data-science items, and DECODE makes data
science one of four domains. A reviewer will notice.

### 5.5 Other thin spots, compared with the published frameworks

- **Collaboration** (Singla; AAMC's "collaborate around AI technologies";
  Çalışkan items 12 and 22). Nothing.
- **Quality improvement and monitoring deployed tools** (Singla; Russell
  domain 6; AIM-7). The Predetermined Change Control Plan in ethics is the only
  monitoring content, and it is checked as regulation. "Alert fatigue" does not
  appear anywhere.
- **Research ethics** (AIM-9 names IRB considerations). Nothing. Reporting
  guidelines appear once, as TRIPOD-LLM in appraisal's Go deeper.
- **Clinical application in a realistic encounter** (AIM-5 names decision
  support, ambient documentation, and diagnostic imaging AI). These are
  discussed in several chapters, but the hands-on versions are the optional
  scribe open lab and the patient-communication live session. The default Do
  activities use made-up cases on general chatbots. The proposed LCME element
  asks for experiential learning; the course has it, but not inside a clinical
  workflow.

### 5.6 Competencies reached only through optional material

| Competency or topic | Only in |
|---|---|
| AIM-8 hands-on (analysing a dataset; training a classifier) | Open-lab ideas 14b |
| AIM-5 with an ambient scribe, start to finish | Open lab 14a |
| AIM-9 at P outside appraisal (retrieval tools, literature synthesis) | Spare chapter 11; resource log |
| AIM-6 practice with other hard conversations, and plain-language handouts | Open-lab ideas 14b |
| AIM-3 in generated images | Open-lab idea "Draw me a doctor" |

---

## 6. Suggestions for publication

### What a reader of a curriculum paper will want

1. **A coverage table like Matrix A**, with P / S / M rather than dots, and a
   sentence saying how the levels were judged. The current dot table in
   `index.qmd` shows tags only.
2. **An assessment alignment table**: for each core competency, the objective,
   the activity, the evidence the student produces, and who judges it. Today
   the answer to "who judges it" is the student, for every Check. Say so
   plainly, and name the planned tutor as future work.
3. **A crosswalk to at least Russell et al. and Hunt et al.**, since the
   research file recommends both, with the published frameworks' own domain
   names. Matrix B gives this.
4. **A named learning theory.** Tolentino et al. found that no paper in their
   review described a theory or pedagogy behind its program [@pmid:39023999].
   The course already has the shape of experiential learning (scenario, do,
   check, reflect). Naming it costs a paragraph.
5. **An honest treatment of AIM-8** as out of scope, with the reason (Lee's
   optional rating; four weeks), so a reviewer reads it as a choice.
6. **The AAMC crosswalk as planned work**, dated, since the national set is
   not out yet.

### The smallest changes that would close the gaps

None of these were made. Each is small.

1. **Fix the tags** (subtitle only). Add AIM-4 to appraisal; AIM-2 to
   workforce, environment, and retrieval; AIM-7 to environment. Consider
   whether workforce really serves AIM-3. Then regenerate the `index.qmd` table
   and fix the AIM-4 count in `appendix/instructors.qmd`.
2. **Tag the two course pages.** Patient information: AIM-4. Resource log:
   AIM-9 and AIM-X.
3. **Repair the one-session-a-week variant** in `appendix/instructors.qmd`:
   either make the bias chapter required pre-work, or say that the variant
   does not meet the AIM-3 rule.
4. **Add one AIM-8 Check row to foundations.** For example: given a model's
   sensitivity, specificity, and the prevalence in your clinic, say what
   share of its positive alerts will be true. This uses material the chapter
   nearly has and would turn AIM-8 from S into P without a new chapter.
5. **Add an AIM-6 thread outside chapter 6.** One Check row in ethics ("the
   sentence you say to Mr. Alvarez about the scribe") would make AIM-6 recur
   at P. The scenario is already there.
6. **Add one governance row to the ethics Check** (for example, "who at your
   institution decides whether a scribe is turned on, and what they monitor
   after"). That makes the AIM-7 tag accurate.
7. **Write out the "Ask questions of a dataset" open lab** if a hands-on AIM-8
   activity is wanted. It already fits the browser-only, free-tier rules.
8. **For a stronger assessment claim**, use the live patient-communication
   session's observer checklist as an observed assessment for AIM-6. It is the
   closest thing in the course to the situational and OSCE-style assessment
   that CAIP recommends for skills and attitudes [@pmid:41767172].

---

## 7. Could not verify

- **Singla et al.'s 107 individual competencies** and their mapping to EPAs
  and CanMEDS roles. Only the abstract's seven areas were used.
- **Hunt et al.'s 37 competencies and 170 learning objectives.** Only the
  seven domains were used.
- **Liaw et al.'s sub-items** beyond the six domains in the abstract.
- **The grouping of Çalışkan et al.'s 27 items** into clusters is my own. The
  item wording was read from the full text on PubMed Central (PMC9302857).
- **That the AAMC report has not appeared somewhere other than its project
  pages.** Checked: the two project pages and one web search, 2026-10-07. The
  pages show no "last updated" date.
- **The live sessions.** Several chapters say the live session adds practice
  the chapter cannot (most of all chapter 6). Live sessions were not observed,
  so they are not in Matrix A.
- **Reading sections were searched, not read line by line.** A competency
  taught only in a chapter's reading, with no objective, Do step, or keyword I
  searched for, could be missing from an S or M cell. P cells do not have this
  problem, because they come from the objectives and the Check.
- **Single rater.** Every cell was graded by one AI model (Claude, in Claude
  Code). A person should check a sample before the matrix goes into a paper,
  and an `AI-LEDGER.md` row should record it if this file feeds
  student-facing content.

## Citations used, all checked in PubMed on 2026-10-07

Russell 2023 [@pmid:36731054]; Hunt 2026 [@pmid:42120544]; Lee 2024
[@pmid:38207056]; Singla 2024 [@pmid:39557985]; DECODE, Car 2025
[@pmid:39888625]; CAIP, Gong 2026 [@pmid:41767172]; AI-PACE, McGrath 2026
[@pmid:42141085]; Liaw 2022 [@pmid:36443071]; Çalışkan 2022 [@pmid:35862401];
Tolentino 2024 [@pmid:39023999].
