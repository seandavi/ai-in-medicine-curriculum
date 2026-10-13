# Answer key: core-bias-equity

Not rendered. For the instructor and the planned tutor.

## Part A: care management risk score (Obermeyer et al. 2019, pmid:31649194)

1. **Proxy.** Mattered: health need, or benefit from care management.
   Measured: predicted 12-month health care cost. Cost tracks care
   *consumed*, and less is spent on Black patients at the same illness.
2. **Harmed.** Black patients. Decision: not auto-enrolled (97th percentile
   threshold) or not referred for review, at the same illness burden as
   enrolled White patients. At the threshold, 4.8 vs 3.8 active chronic
   conditions (26.3% more).
3. **Fix.** Reformulate the prediction target to track illness (the
   authors tested combinations of cost and active chronic conditions); share
   of Black patients among the auto-enrolled rises from 17.7% to 46.5%. The
   paper reports that the manufacturer replicated the finding on its own
   national data (3,695,943 patients) and began an unpaid collaboration with
   the authors; a first changed label cut the excess chronic conditions by
   84%. It does not report that the product was changed.
4. **Status.** The paper describes a fix under way with the manufacturer, not
   a fix in use; the status of this product and of other commercial risk
   scores built the same way is not publicly known. "Could not determine" is
   a correct answer. Source: the paper itself; no public audit of competing
   products located.
5. **Bedside.** Nothing at a single encounter. The harm is a comparison across
   patients that no clinician sees. What would have caught it: an audit of
   enrollment by race against a measure of illness, by someone with authority
   to act. The dashboard tile said "utilization", which is a clue only to a
   reader who already knows the proxy problem; that is the point of the tile.
6. **Allocation** harm: a scarce program slot distributed unfairly. Not a
   representation harm in itself, although a student who argues the score
   encodes "Black patients are healthier" as a stored belief has a defensible
   case for "both".
7. **Social bias, not statistical.** The model predicted cost well (low
   statistical bias). The target was wrong (social bias). This is the case
   that shows the two can be in tension.

## Part B: cases students are likely to bring

Part B starts in ChatGPT Edu: "Name three algorithms in [my specialty] where
what is measured differs from what matters, by race, sex or skin tone; for
each, give the paper and mark it to be verified." With web search on, Edu
will usually return real cases with real papers; not yet run in Edu with a CU
login (see Instructor prep). What to look for in the student's work:

- **The check (journal question 2).** The student found the paper in PubMed
  themselves and says whether the title, authors, and abstract match what
  the chatbot said. Common results: the paper exists but the chatbot's
  one-line summary overstates it; a real paper with the wrong year or first
  author; occasionally a paper that does not exist. "It matched" is a fine
  result if they say how they checked.
- **The row.** Written from the abstract, not from the chatbot's summary.
  Line 1 names two different quantities. Line 4 has a source or says "could
  not determine" with a reason.
- **Sex as the axis.** The prompt allows sex as well as race and skin tone.
  Cases on sex (for example, models trained mostly on male patients) are
  legitimate rows; judge them by the same seven lines.
- **Step 4 (does the model name the proxy).** Current models often name the
  cost-for-need gap for Obermeyer and the calibration gap for oximetry. Either
  answer is a result; the point is that the student compared it with line 1.

The table below covers the fallback rows the chapter points to by specialty.

| Case | 1 Proxy / gap | 2 Harmed, decision | 3 Fix | 4 Status (checked Sept to Oct 2026) | 5 Bedside | 6 Harm type |
|---|---|---|---|---|---|---|
| Dermatology (pmid:35960806; pmid:30073260 is a viewpoint) | Data gap: training images mostly Fitzpatrick I–III; light skin became the implicit "normal" | Dark-skinned patients; lesion missed or misclassified by model *and* by dermatologists labeling the data | Diverse, biopsy-confirmed benchmark (DDI); fine-tuning closed the gap in-study | Datasets exist; no regulatory requirement for skin-tone reporting; adoption by commercial tools not determinable | Partly: a clinician who examines the lesion is not bound by the model, but the same clinician performed worse on dark skin in the study | Allocation (missed diagnosis); arguably representation (dark skin absent from the definition of normal) |
| eGFR (pmid:32853499; pmid:34563581) | Race coefficient (~1.16–1.21) standing in for unmeasured muscle mass / creatinine generation | Black patients; higher reported eGFR, so later CKD staging, later nephrology referral and transplant listing | NKF-ASN Task Force 2021: CKD-EPI 2021 refit without race, immediate implementation in all US labs; cystatin C confirmation | Recommended. CAP survey: 65.8% of 3,542 responding US labs had adopted the 2021 creatinine equation by March 2023 (pmid:37559439; Clinical Chemistry letter, text checked on the journal page 2026-10-12). No later national count found. "Widely adopted, not universal; no count after March 2023" is the right answer | Yes in principle: the equation was printed on the lab report. Anyone could read it. Almost nobody did | Allocation |
| Spirometry (pmid:36383197; pmid:36973004; pmid:38767252) | Race-specific expected values standing in for unmeasured exposure and body proportion; assumed fixed biological difference | Black patients; lower function normed as "expected", so impairment under-called, with consequences for disability, occupational eligibility, transplant priority | GLI-Global race-neutral equations (2022); ATS statement 2023 recommending them (April 2023 per pmid:40712949) | **Contested.** Diao et al. 2024: 12.5M reclassified; nonobstructive impairment +141% Black, −69% White; disability payments shift >$1B/yr toward Black veterans and −$0.5B for White veterans; predictive accuracy equivalent. Single-system transitions published (pmid:40712949). The module's "22.7% / 3.3%" reclassification figure could not be sourced and is not in the chapter | Yes in principle (equation on the report). The harder answer: the correction has costs for some patients too, and the bedside cannot adjudicate that | Allocation; the "fixed racial difference" assumption is a representation harm as well |
| Chest radiograph (pmid:34893776) | Labels extracted from prior radiology reports; the model inherits whatever documentation practice encoded. No one chose a proxy; the gap is in who wrote the ground truth | Female, Black, Hispanic, low-SES, uninsured patients, compounding at intersections (e.g., Hispanic female); disease called "no finding" | Documented; no adopted correction at scale | Not corrected. "Could not determine" any adoption is correct | No. Underdiagnosis is invisible on a single read unless the clinician disagrees with the model *and* the original report; needs a denominator | Allocation |
| LLMs (pmid:37864012; pmid:38123252) | Text that reproduces race-based medicine standing in for physiology; training corpus encodes debunked claims | Black patients; kidney function, lung capacity, pain, skin thickness claims; stereotyped differentials; more expensive procedures recommended by demographic | Vendor updates, unversioned; prompt-level guardrails | Not determinable; re-test each model release. Omiye's 45 responses per model were inconsistent across repeats | Partly: a clinician who knows the claim is debunked catches it. One who learned it in med school (the questions came from trainee misconceptions) does not | **Representation**, primarily; becomes allocation once the output enters a plan |

## The proxy sentence

Acceptable forms of objective 1 (no "bias"): "The tool measures X because Y
cannot be measured, and X tracks Y differently for different patients."
"An algorithm is only as fair as the relationship between what it measures
and what you hoped it measured."

## Closing question ("What this changes for you"), bed 14

Expected: light absorbance measured, oxygen saturation hoped for; calibration
population had lighter skin. Telling the patient: yes, in plain terms ("the
finger probe reads high on darker skin, so we checked your blood directly");
it is a disclosure about a device limitation, not an accusation, and it
changes how the patient reads the monitor next time. The ethics chapter owns
the general disclosure question; this chapter only asks that the student
decide.

## Jabbour numbers (pmid:38112814)

n = 457; baseline 73.0%; standard model +2.9 (no explanation), +4.4 (with);
biased model −11.3; biased with explanation −9.1; difference 2.3 points, 95%
CI −2.7 to 7.2, not significant.

## Verified

**2026-10-12** (PubMed tool, abstracts unless stated):

- 40305017 (Windecker 2025, JAMA Netw Open): 903 AI-enabled devices listed
  by the FDA to 31 August 2024; clinical performance study reported for 505
  (55.9%); 218 (24.1%) said none was done; sex-specific data in 145 of the
  studies (28.7%). Replaces Wu 2021 (33820998), which has no abstract and
  covered 130 summaries; the chapter no longer cites Wu.
- 40832401 (Hughes et al., medRxiv preprint): 34 oximeters; 1/34 passed the
  *anticipated* FDA criteria; 11 had more positive bias in dark than light
  pigmentation.
- 35639368 (Fawzy 2022): 451 never recognized, 247 (54.8%) Black; Black
  patients' median delay 1.0 hour longer than White patients'.
- 38112814 (Jabbour 2023): numbers as above.
- 31649194 (Obermeyer 2019): 4.8 vs 3.8 chronic conditions at the 97th
  percentile (26.3%, P < 0.001), the manufacturer's replication (3,695,943
  patients) and the 84% reduction, read in the authors' accepted manuscript
  on eScholarship (escholarship.org/uc/item/6h92v832). The Science page is
  paywalled.
- 37559439 (CAP eGFR adoption letter): 65.8% by March 2023, 3,542 US labs;
  read on the Clinical Chemistry page.
- 38767252, 36973004, 40712949, 36383197, 34893776, 37864012, 38123252,
  35960806, 30073260, 32853499, 34563581, 33326721, 35793817: metadata and
  abstracts re-read; the table's wording follows them.
- FDA 2013 oximeter guidance (fda.gov/media/72470): "at least 2 darkly
  pigmented subjects or 15% of your subject pool, whichever is larger",
  read in the PDF. No longer quoted in the chapter.
- FDA draft guidance page (January 2025): still "Draft. Not for
  implementation." on 2026-10-12.

**2026-09-07:** the earlier pass checked the same keys plus 38507611 and
36413243, which the chapter no longer cites.

Numbers for the redrawn figures: Sjoding Michigan cohort 88/749 (11.7%) vs
99/2,778 (3.6%); multicenter 160/939 (17.0%) vs 546/8,795 (6.2%), from the
PMC full text (PMC7808260). Valbuena and Fawzy figures from abstracts.
Obermeyer figure numbers from the accepted manuscript (above).

## Open flags

- FDA pulse oximeter guidance: draft as of 2026-10-12. Re-check before each
  cohort.
- Crawford NeurIPS 2017 keynote URL and length: not confirmed.

## Instructor prep

Run the Part B prompt in ChatGPT Edu with a CU login, for two or three
specialties, and keep the transcripts. Note whether each paper it names
exists and matches. If it gets all of them right, say so to students: the
check is still the habit, and "it was right, and here is how I know" is a
good journal answer.
