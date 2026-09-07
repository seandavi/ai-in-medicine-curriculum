# Review: enrichment-workforce-economics chapter, 2026-09-07

Six-persona self-review of `chapters/enrichment-workforce-economics.qmd` per
`curriculum/personas.md`, Elena first, Lindqvist last. Each section records
what the persona found in the first draft and what was changed in response.
Reviewed by the AI assistant that drafted the chapter; author to confirm.

## Elena (avoider, surgery, free tier, ESL) — reads first

**Findings.**

1. First draft opened with "Hinton's prediction" in the first sentence, before
   any scene. Fails the opening-scenario rule and puts a name she does not know
   before a situation she does.
2. Terms used before definition: RVU, Jevons paradox, CAD, attrition,
   automation bias, prior authorization, BLS.
3. The Do began with a chatbot prompt. Her question: is the model failing my
   failure? The draft did not say the failure is the expected result.
4. Radiology-centric: she is going into surgery and the exercise as first
   drafted defaulted to radiology throughout.
5. Press clippings: fine, they land cold. The keynote-slide block needed its
   "illustrative" line to be visible, not fine print only.

**Fixes applied.** Scenario rewritten as the family dinner, with the
prediction arriving via an uncle's phone; the specialty question is put to
"every specialty" in the second paragraph. Every term above is now defined on
first use (RVU in the economics section, Jevons with the steam-engine
sentence, CAD in the precedent section, attrition and automation bias where
they first appear, BLS by its full name). Part A ends with an explicit
sentence that the model failing is the expected result and needs no prompt
skill. Part B's search recipe takes the specialty as the variable and gives a
fallback if no time-and-motion study exists. The slide block carries a fine
line plus a sentence of body text stating it is a rendering.

Her moment where skepticism is right: the CAD section and the Part A
follow-up. Both kept.

## Marcus (early adopter, radiology)

**Findings.**

1. "Is there anything here I could not have found by asking the model?" The
   first draft's four factors could have come from a chatbot. What the model
   will not give him is the primary tables, so the chapter needed to show
   them: NRMP's own Table 3 and 7A numbers, the BLS pages, the time-and-motion
   study with a PMID.
2. Needed a concrete case where his habit gets the wrong answer. The draft
   told him to be careful about forecasts; it did not show a forecast failing.
3. "When the chapter talks about my specialty's future, does it cite anything?"
   The first draft's workforce numbers were the module's secondary-sourced
   figures (20.9% growth by 2055; $571,749). Both were replaced by primary
   sources with different numbers.

**Fixes applied.** Match figure redrawn from the NRMP 2026 PDF, read directly.
Neiman supply projection cited from the JACR paper (25.7% / 40.3%, not the
module's 20.9%). Doximity 2026 figure with its year, and a footnote
explaining why it differs from the module's. Added the "concrete case"
callout: ask the model for the fraction of a radiologist's day spent reading
with a source, then check it, which is also Part A step 3. The pediatric
radiology contraction kept as the counterweight so the chapter is not
cheerleading.

## Priya (clinician-in-waiting, emergency medicine)

**Findings.**

1. If she skips the mechanism, does the chapter still tell her what to do on
   the wards? Mostly not; this is a workforce chapter, and the practical rule
   is about how she reads a forecast, not about a patient.
2. The one scenario she recognizes is the sepsis alert. The CAD automation-bias
   finding is that scenario in a different department, and the draft did not
   say so.
3. Her one sentence for a co-intern was missing.

**Fixes applied.** CAD section now ends by naming the sepsis alert she will
silence in her first month as the same shape. The BLS section names the
colleagues whose jobs move first, which is the ward-level version of this
chapter's content. The co-intern sentence is "adoption and outcomes are
separate questions," stated as such and made a Check row. Accepted that this
chapter's practical guidance is about reading forecasts and labor, not about
a patient in front of her; that is honest for an enrichment module and is
said in "Why this matters."

## Jordan (instructional designer)

**Findings.**

1. Time: reading 25 + watching 20 + doing 35 + check and standing 10 = 90.
   Watching is honest only because the chapter says "first 20 minutes" of a
   60-minute talk; a student who watches all of it is at 130.
2. Objective mapping: obj. 1 and 3 are read-only in the Do; both have Check
   rows. Obj. 2 and 6 map to Part A and Part B; obj. 5 to Part C; obj. 4 has
   a Check row and no activity.
3. Scenario returns in the standing question (the uncle and the phone) and in
   the summary's last bullet.
4. Accessibility: both YouTube videos have auto-captions; the BLS pages are
   plain HTML; the NRMP PDF is a government document; Mousa's essay is free.
   NYT and New Yorker clippings are paywalled but are clippings, not required
   reading. All three mermaid figures have captions; the figures are SVG with
   the data in the caption, so a screen-reader user gets the numbers.
5. Each visual: the match chart shows five years the prose does not narrate;
   the pie shows the two-thirds; the flowchart is the Do's tool; the BLS chart
   is the contradiction; the press clips are the evidence-tier lesson; the
   slide is the artifact under appraisal. None is decoration.
6. Check is self-applicable; no row needs an instructor.

**Fixes applied.** Time statement rewritten to the split above. "Watch the
first 20 minutes" made explicit with the full length stated. Objective
numbers added to the Check rows so the mapping is visible.

## Dr. Okafor (borrowing educator)

**Findings.**

1. Could they run the Do alone? Yes: three parts, each with a script, and the
   answer key has the expected chatbot behaviour and the BLS values with the
   date read.
2. Mechanism at a level they can restate: the four factors are four
   questions; the flowchart is the restatement.
3. What will students ask that the chapter does not answer? "What about my
   specialty?" is answered by the recipe. "Is pathology different?" is not
   answered; the module's debate defaults (pathology, dermatology, EM,
   primary care) are the live session's material and are not in this chapter.
4. Staleness: BLS revises every two years (and revised between the module and
   the chapter); NRMP annually; Doximity annually. All three are dated in the
   text and the Part C instructions tell the student to trust the live page.
5. Images: no downloaded images in this chapter. All visuals are CSS blocks,
   mermaid figures redrawn from data, or text clippings. Nothing to license;
   the whole chapter can be reused.

**Fixes applied.** Table caption for the BLS data records the revision that
happened during writing, so an adopter sees the staleness pattern
demonstrated rather than warned about. Added the instructor-prep note to the
answer key: re-read the BLS pages and re-run Part A before each cohort. The
pathology question is left for the live session and the module; noted here as
the gap an adopter should expect.

## Dr. Lindqvist (clinical ethicist) — reads last

**Findings.**

1. No patient in the opening scenario, so no disclosure question arises. The
   Do uses no patient, note, or classmate data; the only paste is a public
   government page. Passes.
2. Who bears the cost when the tool is wrong: the CAD section names the women
   biopsied (19.7% more biopsies, no more cancers found) and the readers made
   worse. The BLS section names transcriptionists as the displaced group and
   gives their pay relative to the growing occupations. The press-clipping
   paragraph names students who acted on the prediction as a harmed
   population. Passes.
3. Contested question presented as settled? Two risks. First draft implied
   the Neiman demand projection as fact; it was not retrieved and is now
   flagged. First draft used "bot wars" as PHTI's phrase; the PHTI page
   summary did not contain it, so it is attributed to trade coverage and
   flagged. The chapter does not claim AI will never displace physicians; the
   pediatric radiology counterexample and the "forecast with no refutation is
   a mood" line keep the question open.
4. Course disclosure of its own AI use: this chapter was drafted by the model
   and the ledger row says what was checked and how. The answer key records
   the model and date of the Part A test run.
5. The illustrative slide quotes a real person. It is labelled as a rendering
   of a public remark, not the speaker's slide, in both fine print and body
   text; the actual clip is linked so the reader can compare. No real
   company's or person's material is imitated.

**Fixes applied.** Two `[VERIFY]` flags added (demand projection, "bot wars"
wording); the 38% single-site figure attributed to Mousa and flagged; the CAD
reimbursement year flagged. NYT date corrected from the module's May 2026 to
May 2025 with a footnote saying so.

No activity would fail an IRB sniff test.

## Verification record

PMIDs retrieved and read this session, with the claim each supports:
17409321, 26414882, 15354301, 21685142 (CAD and automation bias); 23763878
(36.4%); 30399157 (generalization); 40305017 (FDA device counts and study
reporting); 38276923 (multi-society statement); 33937794 (Langlotz);
39952776, 41031940, 40923948 (Neiman workforce); 41920565, 41511775
(scribes); 31589283, 25201663, 12930930 (administrative cost denominators).
Also read but not cited: 39017689 (commentary on the statement), 41779374
(subspecialty attrition), 37099398 and 31322128 (Mousa's sources for the 60%
cluster and 74% adoption figures; abstracts do not contain those numbers, so
the numbers were dropped rather than cited).

Non-PubMed sources read directly: NRMP 2026 Results and Data PDF (pypdf
text of Tables 1A, 3, 7A); three BLS OOH pages; Doximity 2026 report page;
PHTI report page; HIT Consultant and KFF coverage of PHTI; UCSF DoC-IT news
page for the Holmgren figures (the PubMed record has no abstract); YouTube
page metadata for both videos (length and upload date); AuntMinnie for the
Hinton 2025 quotation; New Republic and Fortune article pages. The New Yorker
and NYT pages could not be fetched; headline, author, and date were confirmed
from search-index metadata and reposts.

## Open items for the author

1. Decide whether the Hinton slide block is acceptable or should become a plain
   blockquote. It is labelled, but it is the one visual that names a real
   person.
2. The four `[VERIFY]` flags above; the CAD reimbursement year and the demand
   projection are one CMS document and one Neiman paper away.
3. The chapter uses no photos or comics. If the book wants one per chapter for
   texture, the Wile E. Coyote image Hinton invoked is not free; a Commons
   photo of a reading room would do.
