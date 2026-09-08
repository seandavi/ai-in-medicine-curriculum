# Answer key — core-bias-equity

Not rendered. Fed to the tutor; used by the instructor in the live session.

## Part A — care management risk score (Obermeyer et al. 2019, pmid:31649194)

1. **Proxy.** Mattered: health need, or benefit from care management.
   Measured: predicted 12-month health care cost. Cost tracks care
   *consumed*, and less is spent on Black patients at the same illness.
2. **Harmed.** Black patients. Decision: not auto-enrolled (97th percentile
   threshold) or not referred for review, at the same illness burden as
   enrolled White patients. At the threshold, 4.8 vs 3.8 active chronic
   conditions (26.3% more).
3. **Correction.** Reformulate the prediction target to track illness (the
   authors tested combinations of cost and active chronic conditions); share
   of Black patients among the auto-enrolled rises from 17.7% to 46.5%. The
   paper reports the vendor engaged to change the product.
4. **Status.** The specific vendor's product was changed per the paper; the
   status of other commercial risk scores built the same way is not known,
   and "could not determine" is the correct answer for the industry. Source:
   the paper itself; no public audit of competing products located.
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

## Part B — pre-vetted cases

| Case | 1 Proxy / gap | 2 Harmed, decision | 3 Correction | 4 Status (Sept 2026) | 5 Bedside | 6 Harm type |
|---|---|---|---|---|---|---|
| Dermatology (pmid:35960806; pmid:30073260 is a viewpoint) | Data gap: training images mostly Fitzpatrick I–III; light skin became the implicit "normal" | Dark-skinned patients; lesion missed or misclassified by model *and* by dermatologists labeling the data | Diverse, biopsy-confirmed benchmark (DDI); fine-tuning closed the gap in-study | Datasets exist; no regulatory requirement for skin-tone reporting; adoption by commercial tools not determinable | Partly: a clinician who examines the lesion is not bound by the model, but the same clinician performed worse on dark skin in the study | Allocation (missed diagnosis); arguably representation (dark skin absent from the definition of normal) |
| eGFR (pmid:32853499; pmid:34563581) | Race coefficient (~1.16–1.21) standing in for unmeasured muscle mass / creatinine generation | Black patients; higher reported eGFR, so later CKD staging, later nephrology referral and transplant listing | NKF-ASN Task Force 2021: CKD-EPI 2021 refit without race, immediate implementation in all US labs; cystatin C confirmation | Recommended; adoption widespread but the "two-thirds of labs" figure is **unconfirmed** (secondary source). pmid:38507611 is a 28-lab survey about communication, not coverage. Correct answer: adopted, extent not determinable from the packet | Yes in principle: the equation was printed on the lab report. Anyone could read it. Almost nobody did | Allocation |
| Spirometry (pmid:36383197; pmid:36973004; pmid:38767252) | Race-specific expected values standing in for unmeasured exposure and body proportion; assumed fixed biological difference | Black patients; lower function normed as "expected", so impairment under-called, with consequences for disability, occupational eligibility, transplant priority | GLI-Global race-neutral equations (2022); ATS statement April 2023 recommending them | **Contested.** Diao et al. 2024: 12.5M reclassified; nonobstructive impairment +141% Black, −69% White; disability payments shift >$1B/yr toward Black veterans and −$0.5B for White veterans; predictive accuracy equivalent. Single-system transitions published (pmid:40712949). The module's "22.7% / 3.3%" reclassification figure could not be sourced and is not in the chapter | Yes in principle (equation on the report). The harder answer: the correction has costs for some patients too, and the bedside cannot adjudicate that | Allocation; the "fixed racial difference" assumption is a representation harm as well |
| Chest radiograph (pmid:34893776) | Labels extracted from prior radiology reports; the model inherits whatever documentation practice encoded. No one chose a proxy; the gap is in who wrote the ground truth | Female, Black, Hispanic, low-SES, uninsured patients, compounding at intersections (e.g., Hispanic female); disease called "no finding" | Documented; no adopted correction at scale | Not corrected. "Could not determine" any adoption is correct | No. Underdiagnosis is invisible on a single read unless the clinician disagrees with the model *and* the original report; needs a denominator | Allocation |
| LLMs (pmid:37864012; pmid:38123252) | Text that reproduces race-based medicine standing in for physiology; training corpus encodes debunked claims | Black patients; kidney function, lung capacity, pain, skin thickness claims; stereotyped differentials; more expensive procedures recommended by demographic | Vendor updates, unversioned; prompt-level guardrails | Not determinable; re-test each model release. Omiye's 45 responses per model were inconsistent across repeats | Partly: a clinician who knows the claim is debunked catches it. One who learned it in med school (the questions came from trainee misconceptions) does not | **Representation**, primarily; becomes allocation once the output enters a plan |

## The proxy sentence

Acceptable forms of objective 1 (no "bias"): "The tool measures X because Y
cannot be measured, and X tracks Y differently for different patients."
"An algorithm is only as fair as the relationship between what it measures
and what you hoped it measured."

## Closing question, bed 14

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

## Verified this session (PubMed tool, 2026-09-07)

31649194, 33326721, 35639368, 35793817, 35960806, 30073260, 32853499,
34563581, 36383197, 36973004, 38767252, 34893776, 37864012, 38123252,
38112814, 33820998, 40042945, 40832401, 38507611, 40712949.

Numbers for the redrawn figures: Sjoding Michigan cohort 88/749 (11.7%) vs
99/2,778 (3.6%); multicenter 160/939 (17.0%) vs 546/8,795 (6.2%), from the
PMC full text (PMC7808260). Valbuena and Fawzy figures from abstracts.
Obermeyer 4.8 vs 3.8 (26.3%) and 17.7% → 46.5% from the abstract and the
paper's reported results as summarized by Science News and the Chicago Booth
Review; the Science full text is paywalled and was not fetched.

## Open flags

- FDA pulse oximeter guidance: draft as of 2026-09-07 (fda.gov page checked).
  Re-check before each cohort.
- eGFR "two-thirds of labs" adoption: unconfirmed; not stated as fact.
- Crawford NeurIPS 2017 keynote URL and length: not confirmed.

## Instructor prep

Run the optional chatbot prompt on the care management algorithm the morning
of the session and keep the transcript. If the model names the cost-for-need
gap unprompted, say so in the session; the finding that current models often
do is itself a "numbers move" point.
