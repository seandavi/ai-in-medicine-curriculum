# Answer key — core-foundations

Not rendered. Fed to the tutor; used by the instructor in the live session.

## Check rows

**Objective 1, eGFR.** Predictors: standardized serum creatinine, age, sex.
Response: measured GFR (iothalamate or other exogenous marker clearance).
Training population: 8,254 participants in 10 studies, 31.5% Black, adults,
mostly kidney-research cohorts (pmid:34554658). Test set: 4,050 in 12 studies.
Why it matters for the patient: she is 45 kg and sarcopenic; creatinine is a
muscle product, so the same creatinine reflects a lower true GFR than the
equation returns. She is an extrapolation on the muscle-mass axis, which the
equation does not see. Good answers for "what instead": cystatin C (not
muscle-derived; the creatinine–cystatin equation is more accurate per the same
paper), or a measured GFR if the decision is high stakes, or simply telling
the attending that 57 is probably an overestimate.

**Objective 2, four models.**

| Model | Truth in training data? | Output | Answer |
|---|---|---|---|
| eGFR | Yes, measured GFR | Number | Supervised regression |
| EHR sepsis alert | Yes, sepsis yes/no per hospitalization | Category (alert / no alert, from a score and threshold) | Supervised classification (a student who says "regression to a score, then thresholded" is right and more precise) |
| Tumor expression clustering, no diagnoses | No | Groups | Unsupervised |
| Chatbot next-token prediction | Yes, the next token is in the text | Category (one of ~100k tokens) | Supervised classification; no human labeler because the label is the text itself. "Self-supervised" is the term of art and is a bonus, not required |

**Objective 3, Part A.** All three steps use the same noisy spiral (noise 50)
with 20% of the dots used for training and a fixed seed. Measured in a
headless browser on 2026-10-03, at about 500 epochs: step 1 (one layer of two,
X₁ and X₂) training loss about 0.45, test about 0.49, a near-straight boundary
through the spiral; step 2 (two layers of six, with sin(X₁) and sin(X₂) added)
about 0.09 and 0.27; step 3
(six layers of eight, all features) about 0.10 and 0.55, with the boundary
wrapping individual dots. Third sentence: on training loss alone, steps 2 and 3
look about the same (0.09 against 0.10, close enough that either can come out
ahead depending on when the student pauses); test loss shows step 3 is the
worst of the three. So training loss alone could not have told the student
which network to trust. If a group lets step 3 run past about 1,500 epochs its test loss
falls again; that is a good discussion point (the number depends on when you
stop), not a wrong result. The transfer: a vendor number with no test set is
that training loss.

**Objective 4, Part B.** Any sentence of the form "the model produced the most
plausible next tokens after `the original publication was`, and a plausible
citation has the same form as a real one, so nothing in the output signals
which it is." Must not use "hallucinate". Bonus if the student notes that RLHF
tuning rewards complete, confident answers, so the model does not hedge on the
wrong one.

Expected Part B results, from a 2026-09 run: on well-known scores the point
values are usually right; the most common errors are (a) naming a later
validation paper as the original (HEART: Backus 2013 Int J Cardiol instead of
Six 2008 Neth Heart J; Wells: the 1998 Ann Intern Med paper or a 2001 paper
instead of Thromb Haemost 2000), (b) wrong volume/pages with correct author and
year, (c) outcome percentages from a different cohort attached to the original.
All three are "partly matches" and are the intended specimen.

A 2026-10-03 run with search off, one run per prompt (research note
`research/foundations-chatbot-test-2026-10-03.md`): GPT-5.4
and Claude named the correct original for all six scores tried, so a student
on a large current model will often get the first question right. The second
question (five references with PMIDs) then usually produces an error: correct
PMIDs were 9 of 10 for GPT-5.4, 5 of 10 for Claude Sonnet 5, 0 of 10 for
Gemini 2.5 Flash, and 0 of 5 for GPT-4o-mini. Every wrong PMID was a real
record for an unrelated paper, so the student must read the title, not just
confirm the link opens. A student whose model got everything right on both
questions should still write the one-sentence explanation; see the chapter.

**Objective 5, Part C.** Budget rule examples: paste only the section that
matters rather than the whole guideline; start a new conversation when the
topic changes; ask for the answer before pasting the long document rather than
after. Middle rule examples: put the question at the end (or the beginning)
after a long paste, restate the key facts at the end, do not bury the one
sentence that matters on page 20 of 40.

## Verified originals in @tbl-scores

All confirmed by PubMed metadata on 2026-09-07 (first author, journal, year,
first page): 18665203 (Six, Neth Heart J 2008;16:191), 12728155 (Lim, Thorax
2003;58:377), 3963537 (Alvarado, Ann Emerg Med 1986;15:557), 11556941
(Kroenke, J Gen Intern Med 2001;16:606), 11073021 (Blatchford, Lancet
2000;356:1318), 7165009 (Oken, Am J Clin Oncol 1982;5:649), 13083014 (Apgar,
Curr Res Anesth Analg 1953;32:260), 10744147 (Wells, Thromb Haemost
2000;83:416). Note for the tutor: Wells's score has several "original" papers;
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

Run both Part B questions yourself the morning of the session on two scores.
If everything comes back correct, the second question is the one to
demonstrate live: in testing it failed far more often than the first. Also
confirm playground.tensorflow.org is up and that the three step links still
open with the spiral and the 20% training split; the exercise cannot be done
without it. If it is down, the archive deck `2024-11-06-deep-learning-intro`
has screenshots of a spiral fit that can substitute for a talk-through.
