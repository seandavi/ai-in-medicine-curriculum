# Review: core-appraisal chapter, 2026-09-08

Second six-persona review of `chapters/core-appraisal.qmd`, after the
plain-language pass of the same day (commit "Plain-language pass:
core-appraisal"). Personas per `curriculum/personas.md`, Elena first, Lindqvist
last. Filed as issue #40. Reviewed by the AI assistant; author to confirm.

## What the plain-language pass changed

The author's note on the deployed book was "a lot of jargonish language usage.
Anchors, register of voice, etc." This chapter is the oldest and the origin of
"register". The term is the chapter's central finding (the clinician-versus-
patient prompt effect), so it stays, defined in one plain sentence on first use;
everywhere else the chapter now says "asked as a clinician" and "asked as a
patient", including the record template. Other replacements: retrieval-grounded
(kept as the term of art, "search-first tool" thereafter), throughline, artifact,
surface (verb), workflow, provenance, structurally, substantial equivalence
(defined), guideline-concordant, specimens, constructed, cohort, degrades
gracefully, conflating, counterweights. Two headings changed: "The idea" is now
"How it works", "The standing question" is now "What this changes for you". About
thirty long sentences were split. No numbers, citation keys, VERIFY spans, figure
ids, alt text, block classes, callout structures, objective mapping, or section
order changed. The answer key's "specimen" wording was updated to match.

## Elena (avoider, surgery, free tier, ESL) — reads first

Passes.

1. **Undefined terms remaining after the pass**: PMID, NCCN, benchmark, trade
   press. *Fixed*: one plain clause each on first use.
2. **"Register"** is defined where the finding is stated and not used again as
   a bare label. The ESL sentence in "The practical consequence" is her moment.
   *Works.*
3. **Comics.** Citogenesis lands cold. Machine Learning assumes the reader has
   heard of linear algebra; the caption and alt text carry the point without
   it. *Accepted.*
4. First activity: two prompts and ten PubMed lookups, 25 minutes, institutional
   or free account, no phone number. *Passes the ten-minute test loosely; the
   first prompt and first lookup are under ten.*

## Marcus (early adopter, radiology)

Passes.

1. **The score-1 example is still made up.** The 09-07 review asked for a real
   misread from a search-first tool, because "so just use OpenEvidence" is the
   takeaway an enthusiast draws from zero fabrications. The chapter labels the
   example as constructed, which is honest but does not show the failure.
   *Open, author*: needs a real run against a retrieval tool with model and
   date recorded; a verified account is required.
2. **"What about Perplexity, Consensus, Elicit?"** *Fixed*: one sentence after
   the retrieval-grounded definition points to the retrieval chapter for how to
   tell whether a given product really searches first.
3. Radiology clause on FDA clearances, cited. FUTURE-AI table is the checklist
   for the next tool. Three-example panel is the failure he did not expect.
   *Pass.*

## Priya (clinician-in-waiting, emergency medicine)

Passes. Nothing new since 09-07: PHI callout with the business associate
agreement defined, the EHR-embedded boundary case, the documentation pointer to
the ethics chapter, "cleared is not validated" as the co-intern sentence. Skipping
"How it works" and reading only Do and Check still tells her what to do.

## Jordan (instructional designer)

1. **Objectives to activities.** 1 and 3 to Part A; 2 to the Check row "The
   mechanism"; 4 to Part B; 5 to the Check row "The one sentence"; 6 to the
   Check row on misrepresented references and the closing question; 7 to the
   Check row "The vendor question" and the closing question. *Pass.*
2. **Time.** 35 + 30 + 45 = 110 minutes; subtitle says about two hours. *Pass.*
3. **Diagram alt text.** The citation-paths mermaid figure had no `fig-alt`.
   *Fixed in source* (`%%| fig-alt`, matching the foundations chapter), but
   Quarto's client-side mermaid ignores it: the HTML build emits a
   `<pre class="mermaid">` with no `alt` or `aria-label`. *Open, coordinator*:
   `mermaid-format: svg` (or `png`) under `format: html` in `_quarto.yml`
   would make the alt text render. Not changed here because `_quarto.yml` is
   off limits to this pass.
4. **Podcast accessibility.** Neither NEJM AI Grand Rounds entry says whether a
   transcript exists. *Open, author*: check and note in the Watch block.
5. **The telemedicine photo.** Cover the caption and ask what the image teaches:
   little that the prose does not. The author added it deliberately in commit
   8ac53f6, so this is flagged, not cut. *Open, author.*
6. **Headings.** Two headings changed in the pass. If sibling chapters kept "The
   idea" and "The standing question", the book is inconsistent. *Open,
   coordinator.*

## Dr. Okafor (borrowing educator)

1. **Run the Do alone.** Yes: the answer key carries Part B tiers and sources,
   the example-panel provenance, and instructor prep for the morning of the
   session. *Pass.*
2. **Restate the mechanism.** "Most likely next words, one token at a time",
   plus the phone-keyboard analogy. *Pass.*
3. **Stale in twelve months.** The HTI-1 callout carried a `[VERIFY]`. *Fixed*:
   replaced with the resolution proposed in
   `reviews/core-ethics-regulation-2026-09-07.md` (in force as of September
   2026; HTI-5 proposes to remove the source-attribute requirement; the ethics
   and regulation chapter tracks status). The remaining VERIFY flags (Frutuoso
   Maia, FDA device counts, video duration, OpenEvidence eligibility, Peterson
   URLs, UCSF RVU figure) are unchanged and still needed.
4. **Licences.** CC BY-SA photo, two CC BY-NC comics, credited in captions with
   links; illustrative vendor slide labelled; press clippings are headlines with
   links, not screenshots. *Pass.*

## Dr. Lindqvist (clinical ethicist) — reads last

1. **PHI.** Every Do question is a general management question; the callout
   says why and names the boundary case. *Pass.*
2. **Patient in the room.** The seventh question (does the patient know the
   visit is recorded) is in the FUTURE-AI section and returns in the closing
   question. *Pass.*
3. **Certainty versus evidence.** "Efficiency gains get absorbed by volume" was
   stated as a flat lesson in the tiers section while the collapsed solution
   calls the same idea a hypothesis. *Fixed*: "may also be", "tends to".
4. **Who bears the cost.** The equity paragraph names patients asking in their
   own words. *Pass.*
5. **Course's own AI use.** The example panel names the model and date of the
   run; the tutor is named as the holder of the answer key. *Pass.*

## Action list, by priority

1. HTI-1 callout: replace VERIFY with the September 2026 status. **Fixed.**
2. Define PMID, NCCN, benchmark, trade press. **Fixed.**
3. Soften the "absorbed by volume" lesson to match the solution's hedge. **Fixed.**
4. Pointer to the retrieval chapter for search-first products. **Fixed.**
5. `fig-alt` on the citation-paths diagram. **Fixed in source; inert in HTML.**
6. Real score-1 example from a retrieval-grounded tool. **Open, author.**
7. `mermaid-format` in `_quarto.yml` so diagram alt text renders. **Open, coordinator.**
8. Podcast transcript availability. **Open, author.**
9. Keep or cut the telemedicine photo. **Open, author.**
10. Heading names across chapters. **Open, coordinator.**

## What was fixed in this pass

Items 1 to 5 above, in `chapters/core-appraisal.qmd`. No change to
`_answers/core-appraisal.md` beyond the wording sync from the plain-language
commit.

## What is open

Items 6 to 10. None blocks a cohort; 6 is the most valuable, 7 is the cheapest.
