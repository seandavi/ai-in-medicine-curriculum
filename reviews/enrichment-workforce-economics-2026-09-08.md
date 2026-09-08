# Review: enrichment-workforce-economics chapter, 2026-09-08

Second six-persona review of `chapters/enrichment-workforce-economics.qmd`,
done after the plain-language pass of the same day, per
`curriculum/personas.md`, Elena first, Lindqvist last. Tracked as GitHub issue
#29. Reviewed by the AI assistant that did the plain-language pass; author to
confirm the open items.

## What the plain-language pass changed first

The author's note on the deployed book was that the content is good but the
language is "jargonish": anchors, register of voice, design-doc vocabulary.
Before the personas read it, the chapter got one pass for that. In this
chapter the main offenders were the framework vocabulary ("four-factor
framework", "task decomposition", "real-world generalization", "dynamic",
"structural", "decompose", "perceptual core", "surface" as a verb, "register",
"refutation", "stakeholder framing", "evidence tiers") and undefined clinical
and billing shorthand (specificity, sensitivity, RVU, prior authorization,
downcode, Level 5, benchmark, protocolling, denominator). The four factors are
now introduced as four plain questions, one per heading, and the worksheets
say they call them "factors". About 45 long sentences were split. No number,
citation, flag, figure id, caption, block class, or section moved. The
persona name "Elena" had leaked into student-facing text in Part A and was
removed. Details are in the commit message.

## Elena (avoider, surgery, free tier, ESL) — reads first

**Findings.**

1. The pie chart's slice "Noninterpretive clinical work" was the paper's
   term, and the prose around it now says "reading images". A reader who
   looks at the chart before the paragraph has to guess.
2. "Hundreds of cleared tools" says cleared without saying by whom.
3. Every term she would meet cold is now defined where it first appears.
   Part A says the model failing is the expected result and needs no skill
   with prompts. The Do uses an institutional account and no phone number.
4. The press clippings and the slide land cold. The flowchart is four plain
   questions.

**Fixes applied.** Slice relabelled "Clinical work other than reading images"
(the caption keeps the paper's wording so the number can be traced).
"FDA-cleared". Nothing else needed.

Her moment where skepticism is right: Part A step 3 and the CAD section. Both
kept.

## Marcus (early adopter, radiology)

**Findings.**

1. The things a chatbot will not hand him are still here: NRMP Tables 3 and
   7A redrawn, the BLS pages, the Dhanoa PMID, the Neiman projections with
   their two scenarios.
2. The "concrete case" callout is his habit failing on the tool he trusts,
   and Part A step 3 makes him watch it fail.
3. Specialty future is cited throughout; the pediatric radiology
   counterexample keeps it from being cheerleading.

**Fixes applied.** None requested.

## Priya (clinician-in-waiting, emergency medicine)

**Findings.**

1. The CAD section ends by naming the sepsis alert she will silence, but
   stopped at "a tool that is wrong in a systematic way drags the human
   down." It named the shape and not the move.
2. Her co-intern sentence, "adoption and outcomes are separate questions," is
   stated as such and is a Check row.
3. Accountability: "Someone signs the read. Malpractice law judges the
   physician, not the model." Present.

**Fixes applied.** One sentence added after the sepsis alert: "The defence is
the same in both places: find out how often the tool is wrong before you
decide how much to trust it." Accepted, as in the first review, that this
chapter's practical rule is about reading forecasts and labor rather than a
patient in front of her.

## Jordan (instructional designer)

**Findings.**

1. The four mermaid figures had captions but no `fig-alt`. The other
   chapters carry `%%| fig-alt:` on mermaid blocks; the pattern says every
   image has one.
2. Reading load: about 5,600 words including code blocks and footnotes. That
   is 25 to 30 minutes for a fluent reader and longer for Elena. The stated
   25 minutes is at the low edge.
3. Objective mapping unchanged from 2026-09-07: obj. 2, 5, 6 map to Parts A
   to C; obj. 1, 3, 4 have Check rows and are read-only in the Do.
4. Scenario returns in the standing question and the last summary bullet.
5. Visuals: each still does a job the prose does not; none is decoration.
6. Check is self-applicable.

**Fixes applied.** `fig-alt` added to all four figures. Time statement left
as is; see open items.

## Dr. Okafor (borrowing educator)

**Findings.**

1. "Your institutional ChatGPT Edu or Microsoft Copilot account" is
   institution-specific and was not marked as swappable.
2. The Do can be run from the chapter alone; the answer key carries the
   expected chatbot behaviour and the BLS values with the read date, and the
   instructor-prep note says to re-run Part A with the local tool.
3. Staleness is dated everywhere (NRMP May 2026, BLS 2026-09-07, Doximity
   2026, PHTI April 2026, KFF July 2026).
4. No downloaded images; nothing to license.
5. "Is pathology different?" still not answered in the chapter.

**Fixes applied.** "Swap in whatever your own school licenses" added to the
time paragraph. Pathology left for the live session.

## Dr. Lindqvist (clinical ethicist) — reads last

**Findings.**

1. "Students are hearing the prediction and acting on it" asserted a cause the
   Radiology Business headline does not establish. The headline reports an
   applicant decline; it does not say why.
2. "The prediction failed for four reasons" presented the chapter's framework
   as the settled explanation. It is the most useful explanation, drawn from
   Mousa; it is not the only one.
3. "No measured loss of jobs" was unhedged in time.
4. No PHI, no patient in the scenario, no classmate data. The harmed
   populations are named: women biopsied without more cancers found, readers
   made worse by CAD, transcriptionists, students who acted on the forecast.
5. The illustrative Hinton slide names a real person. Labelled as a rendering
   in fine print and in body text, with the real clip linked. Unchanged.

**Fixes applied.** Hedged: "The headline does not prove why the pool shrank.
But if students are hearing the prediction and acting on it ... that is a
harm the prediction did." "The most useful explanation of the failure has
four parts." "So far no measured loss of radiologist jobs."

No activity would fail an IRB sniff test.

## Verification record

No new claims were introduced in this pass, so no new PubMed lookups were
made; the 2026-09-07 verification record stands. PubMed's E-utilities were
rate-limited during the render (ten sibling passes running at once), so
`quartobot resolve` was shimmed out and the render used the existing
`references.resolved.bib` from the main checkout. All citation keys in the
chapter resolved; the rendered page has no unresolved keys.

## Action list

1. [done] Remove the persona name from student-facing text.
2. [done] `fig-alt` on all four mermaid figures.
3. [done] Hedge the applicant-pool causal claim and the four-reasons framing;
   "so far" on the jobs claim.
4. [done] One-line practical rule after the sepsis-alert sentence.
5. [done] Mark the institutional chatbot as swappable; relabel the pie slice;
   "FDA-cleared".
6. [open] Hinton slide: keep as a styled block or reduce to a blockquote.
7. [open] Reading time: leave at 25 minutes or say 25 to 30.
8. [open] The four `[VERIFY]` flags: 38% single-site (Mousa), Neiman demand
   projection, CAD add-on withdrawal year, "bot wars" wording in the PHTI PDF.
9. [open] Objective 4 has no Do activity; pathology deferred to the live
   session.

## Open items for the author

Items 6 to 9 above. None blocks publication; 6 and 7 are taste, 8 is one CMS
document and one Neiman paper away, 9 is a design choice carried from the
first review. No stylesheet change is needed.
