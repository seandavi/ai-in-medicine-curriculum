# Does the foundations chatbot exercise produce an error? A test, 2026-10-03

The foundations session (chapter Part B, deck slides 40 to 42) asks students to
make a chatbot give a wrong answer and then explain it. Reviewers asked whether
a current model would get the exercise right. This is one test, run by an AI
agent, to give the instructor an idea of what students will see. It is not a
study: one run per prompt, no repeats, and the citations were graded but the
point values were not.

## How it was run

- **Prompts.** Prompt A as on slide 41: "Give me the exact point values and
  cutoffs of the `<score>`, the outcome each cutoff was validated against, and
  the full original publication that first described it: first author,
  journal, year, volume, and pages." For Fleischner, size thresholds and
  follow-up intervals instead. Prompt B: "Give me five references, with
  PubMed IDs, that support this claim: `<claim>`. For each, give first author,
  journal, year, title, and PMID." Both prompts ended "Answer from memory; do
  not use any tools or search."
- **Models.** Through API, not the chat apps students use, with no tools and a
  one-line system prompt ("You are a helpful assistant"): GPT-5.4, GPT-4o-mini,
  Gemini 2.5 Flash, Claude Sonnet 5. Prompt A on Claude ran through Claude Code
  (Claude Fable 5.1), whose own system prompt is about coding. The chat apps add
  their own system prompts and often search, so students may see different
  results.
- **Grading.** Prompt A: the citation compared with the PubMed record of the
  first publication (the table on slide 40). Prompt B: each PMID looked up in
  PubMed; "right" if the record's title matched the paper the model described.

## Prompt A: the original publication

| Score | GPT-5.4 | Claude Fable 5.1 | Gemini 2.5 Flash | GPT-4o-mini |
|---|---|---|---|---|
| CURB-65 | right | right | right | right |
| Alvarado | right | right | right | right |
| Wells (PE) | right | right | right | made up (a) |
| Fleischner | right (2005) | right (2005) | right (2005) | later paper (b) |
| HEART | right | right | made up (c) | made up (d) |
| PHQ-9 | right | right | right | earlier paper (e) |

a. "Wells, *Chest* 2000;118:1557–1561". Those volume and pages belong to an
   unrelated paper on chronic bronchitis (PMID 11115440).
b. The 2017 Fleischner update (MacMahon, *Radiology* 2017;284:228–243), a real
   paper, named as the original.
c. "Six AJ, *Am Heart J* 2008;155:883–888". Those volume and pages belong to an
   unrelated paper on albumin in heart failure (PMID 18440336).
d. "Hoekstra, *Am J Cardiol* 2010;105:81–85". PubMed's citation matcher found
   no paper at that volume and page.
e. Spitzer et al., *JAMA* 1999;282:1737–1744, a real paper on the full
   Patient Health Questionnaire, named as the original PHQ-9 paper.

## Prompt B: five references with PubMed IDs

| Claim | GPT-5.4 | Claude Sonnet 5 | Gemini 2.5 Flash | GPT-4o-mini |
|---|---|---|---|---|
| CURB-65 0 or 1 can be treated as outpatients | 4 of 5 right | 1 of 5 right | 0 of 5 right | declined |
| HEART 0 to 3 is low risk in the ED | 5 of 5 right | 4 of 5 right | 0 of 5 right | 0 of 5 right |

Every wrong PMID was a real PubMed record for an unrelated paper (nitrogen
dioxide and mortality, ketogenic diets and pain, laser projectors, and so on),
attached to a plausible title and author. None was a number that does not
exist, so a student who only checks that the PMID "works" will be fooled. The
paper the model described was sometimes real, with the wrong PMID. Both GPT-5.4
and Claude cited Capelastegui et al., "Validation of a predictive rule for the
management of community-acquired pneumonia", *Eur Respir J* 2006, a real
paper, PMID 16387948. GPT-5.4 gave 16387946, two off, which is a paper on
gastro-oesophageal reflux in pulmonary fibrosis. Claude gave 16540496, a paper
on nitrogen dioxide and mortality.

## What this suggests for the exercise

- Large current models usually get prompt A right on famous scores. Small or
  older models often do not. That matches slide 33: often right, sometimes
  wrong, in the same tone.
- Prompt B produced errors from every model except GPT-5.4 on the HEART
  claim. It is the more reliable way to produce an error to explain, so the
  deck now asks students who got prompt A right to go on to prompt B.
- Checking a PMID means opening it and reading the title, not seeing that the
  link loads.
- Search was off. With search on, results are likely to differ; the deck asks
  students to compare.

The answers and the grading script were kept in the session's scratch folder
and are not in the repository.
