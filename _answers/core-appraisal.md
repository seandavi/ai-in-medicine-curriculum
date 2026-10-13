# Answer key: core-appraisal

Not rendered. For the course director and for the tutor if one is built.
Revised 2026-10-12: Part A is now success first (ChatGPT Edu with web search,
three references, then a patient-worded contrast, three more), with a "Did it
show sources?" column; the OpenEvidence row is gone; the tier is
"observational", not "large observational".

## Part A

There is no fixed answer. Expect most references from the clinician prompt
with web search on to score 2; in McLaughlin et al. 2026 (pmid:42232526, full
text read 2026-10-12), ChatGPT with search, asked as a clinician, fabricated
2.1% of references, and most of ChatGPT's score-1 errors were wrong PMIDs or
DOIs. A student whose six references all score 2 has done the exercise well if
each score is backed by a named PubMed search. Do not accept "looked real".

Note on the scale: McLaughlin's score 1 is "real article, wrong metadata or a
non-peer-reviewed web source". The chapter's score 1 is "real paper, but the
model's description of it is wrong". The chapter says the scale is adapted.
Accept either kind of error as a 1.

## Part B: tiers and sources

| Claim | Tier | Source |
|---|---|---|
| 1 | Observational (no control) | Tierney et al., NEJM Catalyst 2024. doi:10.1056/CAT.23.0404. Kaiser/TPMG. |
| 2 | Observational (six-system, pre/post survey; 263 analysed of 451 enrolled) | Olson et al., JAMA Netw Open 2025. pmid:41037268 |
| 3 | Observational (pre/post survey) | You et al., JAMA Netw Open 2025. pmid:40839265. MGB/Emory. |
| 4 | Observational (pilot of 45 physicians, pre/post; not large) | Ma et al. and Shah et al., JAMIA 2025. pmid:39688515 (documentation 6.89 and after-hours 5.17 minutes per day), pmid:39657021. Stanford. |
| 5 | RCT (three-arm, n=238) | Lukac et al., "Ambient AI Scribes in Clinical Practice: A Randomized Trial", NEJM AI 2025;2(12). pmid:41497288 (published version, abstract checked 2026-10-12; preprint pmid:40672471). UCLA. The published abstract calls the burnout, task load, and work exhaustion findings "potential improvements" that need confirmation. |
| 6 | RCT (stepped-wedge, n=66) | Afshar et al., NEJM AI 2025. pmid:41625485. Wisconsin. The outcome that lost significance is "work outside work" (hours per day), not workweek hours; the chapter's claim was corrected 2026-10-12. |
| 7 | RCT (crossover, 160 randomized, 136 surveys analysed) | Chowdhury et al., JAMIA 2026. pmid:41729180. Duke. The trial compared two scribe products; the abstract says pajama time was "largely unaffected". The chapter's claim was reworded to match on 2026-10-12. |
| 8 | Small randomized QI trial (n=23; 12 intervention, 11 control) | Shin et al., Appl Clin Inform 2025. pmid:40675605. Emory/CHOA pediatric subspecialists. Burnout 89% to 56% among the 9 intervention providers who completed both surveys. This is why the chapter no longer says "randomized trials report smaller effects" without qualification. |
| 9 | Observational (five systems, difference-in-differences; 8,581 clinicians in the sample, 1,809 adopters) | Rotenstein et al., JAMA 2026. pmid:41920565. Adoption was opt-in at 4 of the 5 sites. The paper does not say all 8,581 were offered the tool. |
| 10 | Trade press attached to a peer-reviewed paper | STAT, 1 April 2026, "Large AI scribe study finds modest time savings, inconsistent use": https://www.statnews.com/2026/04/01/ai-ambient-scribes-modest-time-savings-clinical-documentation/ . The 79% matches 1 minus 1,809/8,581, but "offered ... declined" goes beyond the paper, which reports a sample, not an offer. The STAT text is paywalled; the 79% was not seen in the article on 2026-10-12 (author to confirm). |

## Closing questions

Mechanisms: selection and Hawthorne. Outcome: after-hours charting. See the
collapsed solution in the chapter for the full reasoning.

## Counterweights

- Peterson Health Technology Institute, March 2025 report <https://phti.org/ai-adoption-early-applications-impacts/> and April 2026 report <https://phti.org/administrative-ai-current-use-and-potential-impact/>.
- UCSF: adopters billed 1.81 more RVUs a week (95% CI 0.86 to 2.75), no difference in denials, one site, possible self-selection; the authors call for randomization. pmid:41511775 (full text read 2026-10-12). The 5.8% figure attributed to a UCSF press release is not in the paper and was removed from the chapter.
- Frutuoso Maia et al., Br J Oral Maxillofac Surg 2026;64(3):216-222 (GPT-4
  36%, Gemini 14%, DeepSeek 8.8% hallucinated citations). pmid:41633924.

## FDA devices

The chapter's numbers are Windecker et al., JAMA Netw Open 2025, pmid:40305017:
903 devices to 31 August 2024; clinical performance studies reported for 505
(55.9%); 218 (24.1%) explicitly none; 145 of the clinical studies (28.7%) gave
sex-specific data; radiology 692 (76.6%). They were previously attributed to Wu
et al. 2021 (pmid:33820998, no abstract in PubMed); that key was removed.

## Example panel provenance

The "Three examples" callout in Part A records a real run: clinician-framed
prompt (five references, the earlier version of the Do), anticoagulation in AF
with stage 4 CKD, Claude (claude-fable-5-1), no retrieval, 2026-09-07. Five
references generated; all five resolved in PubMed with correct authors,
journal, volume, and pages (pmid:29954737, 36335914, 36335915, 32160801,
31976865). The score-2 example (Stanifer) is from that run. The score-1 and
score-0 examples are made up and labeled as such in the chapter; the score-1
misreading of RENAL-AF is the documented common one (the trial was
underpowered, not positive).

## Before students do it

Run Part A once in ChatGPT Edu with web search on, both prompts, three
references each, and keep the result. If the patient-worded prompt also
returns real, sourced references, that is the expected success, not a failed
demonstration. If the Edu run produces a real 0 or 1, consider replacing the
made-up examples in the panel with it.
