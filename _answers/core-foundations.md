# Answer key: core-foundations

Not rendered. Instructor notes for the course director (Wednesday's talk,
office hours). Revised 2026-10-12: a new objective 1 (the nested circles), so
the other objectives moved up by one; Part B is now "Ask, then check"; the
eGFR history, COVID X-rays, and MYCIN/Watson are in one optional box.

## Check rows

**Objective 1, the nested circles.** MYCIN: AI only (rules written by hand,
nothing learned from data). The eGFR equation: machine learning (learned from
data; a statistician would call it a regression, and the chapter accepts
that). A model that reads chest X-rays: deep learning (a neural network).
A chatbot: generative AI, inside deep learning. Meets: the student says what
makes each one a kind of the one around it (learned from data; many layers;
writes new text or images). A student who says "the eGFR is just
statistics" is right too, if they can say why the chapter counts it.

**Objective 2, eGFR.** Predictors: standardized serum creatinine, age, sex.
Response: measured GFR (iothalamate or other exogenous marker clearance).
Training population: 8,254 participants in 10 studies, 31.5% Black, all 18 or
older, from research studies and clinical populations; the studies included
only ambulatory adults without serious coexisting conditions (pmid:34554658,
abstract and PMC full text). Test set: 4,050 in 12 studies.
Why it matters for the patient: she is 45 kg and sarcopenic after a year of
illness; creatinine is a muscle product, so the same creatinine reflects a
lower true GFR than the equation returns. She is an extrapolation on the
muscle-mass axis, which the equation does not see, and she is not like the
ambulatory, otherwise well adults it was fit to. Good answers for "what
instead": cystatin C (not muscle-derived; the creatinine–cystatin equation is
more accurate per the same paper), or a measured GFR if the decision is high
stakes, or simply telling the attending that 57 is probably an overestimate.

**Objective 3, four models.**

| Model | Truth in training data? | Output | Answer |
|---|---|---|---|
| eGFR | Yes, measured GFR | Number | Supervised regression |
| EHR sepsis alert | Yes, sepsis yes/no per hospitalization | Category (alert / no alert, from a score and threshold) | Supervised classification (a student who says "regression to a score, then thresholded" is right and more precise) |
| Tumor expression clustering, no diagnoses | No | Groups | Unsupervised |
| Chatbot next-token prediction | Yes, the next token is in the text | Category (one of ~100k tokens) | Supervised classification; no human labeler because the label is the text itself. "Self-supervised" is the term of art and is a bonus, not required |

**Objective 4, Part A.** The slider fits a polynomial to 12 made-up training
points and scores it on 60 held-back test points (seeded, so every student sees
the same numbers). Read from the chapter's widget code on 2026-10-12, training
and test error (root-mean-square) by setting, approximately: 0, 0.76 and 0.80
(a flat line, wrong on both sets: too simple); 1, 0.31 and 0.58; 3, 0.26 and
0.42 (the lowest test error; 4 is close at 0.44); 6, 0.23 and 2.1 (the readout
says "above 1.5" from here on); 11, 0.00 and far off the chart (the curve
passes through every training dot: too flexible). Third sentence: on training
error alone the student would have picked 11, because training error only
ever falls and reaches zero there; the test error shows 11 is the worst
setting and the best one is in the middle, around 3. A student who answers
"too simple: 0 or 1; too flexible: 6 and above" is right. The transfer: a
vendor number with no test set is that training error.

**Fitting by hand (the eGFR sliders in "A formula learned from data").** Not a
Check row, but students may ask. Starting setting a = 50, b = 0.3, average
miss about 19.3 mL/min/1.73 m². The best setting the sliders allow is a = 75,
b = 1.05, average miss about 6.1. The data were generated from
80 × creatinine^(−1.1) with scatter, so a student near a = 80, b = 1.1 is
close. The curve and data are illustrative, not CKD-EPI.

**Objective 5, Part B ("Ask, then check").** Part B is success first: the
student asks a question they would ask on the wards, checks the numbers on
MDCalc, the original publication in PubMed against @tbl-scores, and one link
if the chatbot searched. Meets: the record says which parts were right and
how each was checked, and the sentence is of the form "the model produced the
most plausible next tokens after `the original publication was`, and a real
citation and a made-up one are both plausible, so nothing in the output
signals which it is." Must not use "hallucinate". The sentence is still
required when everything was right; that is the point of the routine. Bonus
if the student notes that RLHF tuning rewards complete, confident answers, so
the tone does not change on a wrong one.

What to expect. ChatGPT Edu usually searches the web, so most students will
get the point values right and often the original publication too. That is a
good result, not a failed exercise. The earlier runs below used other tools,
with search off, and are a guide to the errors that do occur, not a forecast
for Edu.

- A 2026-09 run (no search): on well-known scores the point values were
  usually right; the most common errors were (a) naming a later validation
  paper as the original (HEART: Backus 2013 Int J Cardiol instead of Six 2008
  Neth Heart J; Wells: the 1998 Ann Intern Med paper or a 2001 paper instead
  of Thromb Haemost 2000), (b) wrong volume or pages with the correct author
  and year, (c) outcome percentages from a different cohort attached to the
  original. All three are "partly matches".
- A 2026-10-03 run through the APIs, one run per prompt, search off (research
  note `research/foundations-chatbot-test-2026-10-03.md`): GPT-5.4 and Claude
  named the correct original for all six scores tried. On the five-PMID
  question, correct PMIDs were 9 of 10 for GPT-5.4, 5 of 10 for Claude Sonnet
  5, 0 of 10 for Gemini 2.5 Flash, and 0 of 5 for GPT-4o-mini. Every wrong
  PMID was a real record for an unrelated paper, so the student must read the
  title, not just confirm the link opens.

Neither run used ChatGPT Edu. Run Part B in Edu before relying on these
patterns (see Instructor prep).

**Objective 6, Part C.** No course test run of the check prompt yet; judge
the record, not the model. Meets: the student says what the check corrected
(often a PMID, volume, or page; sometimes nothing), what it marked as not found,
and whether each of two opened links supports the claim it was attached to.
The "could not catch" line should name at least one of: a real link whose
source does not say what the answer says, if nobody opens it (the Wu 2025
finding, about 3 in 10 statements unsupported for GPT-4o with web search,
pmid:40240349); a source that the search itself got wrong; any fact about a
patient, because ChatGPT Edu cannot see the chart (the dose against the
patient's weight, the history against the notes). Some tools built into the
electronic health record can see the chart; the course does not use them. A
student who writes "it checked everything" or who opened no link falls short.

## The optional box: when a good result did not carry over

The eGFR history table, the COVID-19 X-ray example, and MYCIN and Watson are
now one collapsed "If you have more time" callout after "The one sentence".
No Check row depends on them.

The eGFR table, checked 2026-10-12 against the PubMed abstracts: MDRD 1,628
patients, 1,070 training, 558 validation (pmid:10075613); CKD-EPI 2009, 8,254
in 10 studies, 3,896 in 16 for validation (pmid:19414839); Inker 2021
(pmid:34554658): the 2009 equation **with** the race term overestimated
measured GFR in Black participants by a median of 3.7 mL/min/1.73 m²; with
the race coefficient simply removed, it underestimated by 7.1; the new
equation without race underestimated by 3.6 in Black participants and
overestimated by 3.9 in non-Black participants. A student who says "the race
term made it underestimate" has the direction backwards.

COVID-19 X-rays. Framing: a test set that shared the training set's flaw
(shortcut learning, confounding by source), not classic overfitting. The split
into training and test was done; both came from the same pooled sources. Facts
the chapter uses, and only these: Roberts et al. 2021
(doi:10.1038/s42256-021-00307-0), 62 papers in full review, 16 used a
pediatric pneumonia set (ages one to five) as non-COVID controls, quoted as
"merely detecting children versus adults". DeGrave et al. (journal version
doi:10.1038/s42256-021-00338-7; preprint doi:10.1101/2020.09.13.20193565, CC
BY 4.0, source of the two figures): Dataset I paired GitHub-COVID images,
many cropped from publication figures, with NIH ChestX-ray14 non-COVID images
from one US hospital; internal test good, "half of the model's predictive
performance is lost" on a new hospital system (the PMC text of the preprint
has a gap at that sentence, so the exact wording was not re-confirmed on
2026-10-12); saliency maps highlighted laterality markers, arrows and
annotations, image edges, the diaphragm, and the cardiac silhouette; swapping
laterality markers shifted the output (confirmed in the preprint full text).
Do not add AUC figures or claims that no COVID model was clinically useful;
neither was verified for the chapter.

MYCIN (pmid:480542): eight experts, ten meningitis cases, acceptability 65%
against 42.5% to 62.5% for the five faculty specialists. "Never used in
routine patient care" is not in that paper and carries a VERIFY flag. Watson
(pmid:30053147) is a 2017 JNCI news piece with no abstract in PubMed.

## Verified originals in @tbl-scores

All confirmed by PubMed metadata on 2026-09-07 (first author, journal, year,
first page): 18665203 (Six, Neth Heart J 2008;16:191), 12728155 (Lim, Thorax
2003;58:377), 3963537 (Alvarado, Ann Emerg Med 1986;15:557), 11556941
(Kroenke, J Gen Intern Med 2001;16:606), 11073021 (Blatchford, Lancet
2000;356:1318), 7165009 (Oken, Am J Clin Oncol 1982;5:649), 13083014 (Apgar,
Curr Res Anesth Analg 1953;32:260), 10744147 (Wells, Thromb Haemost
2000;83:416). Note: Wells's score has several "original" papers;
the 2000 Thromb Haemost paper is the one that gives the seven-item point
values used by MDCalc. A student who cites Wells 1998 Ann Intern Med has found
the earlier clinical model, which is defensible; grade as "partly, and
explain".

## The illustrative chat block

Constructed. The point values and cutoffs are correct for HEART (0–2 each,
0–3 low, 4–6 intermediate, 7–10 high). The reference given (Backus et al.,
Int J Cardiol 2013) is a real *validation* paper, not the original
description; that substitution is the most common real-world error and is why
it was chosen. The percentages are of the kind reported in the validation
literature and are not to be quoted from the chapter.

## Instructor prep

Run Part B in ChatGPT Edu, with a CU login, on two scores before students
do it: the question, the three checks, and the five-PMID question. Note what
Edu got right, whether it searched, and how many of the five PMIDs matched,
and replace the "What to expect" notes above with that run. To demonstrate
it, show the routine working: a mostly right answer, checked part by part.
If something is wrong, show how the check found it. Then send the Part C
check prompt in the same conversation and open two of the links it gives on
screen. The two sliders run in the page with no outside site, so there is
nothing to confirm in advance beyond the page loading.
