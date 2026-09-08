# Review: enrichment-rag-notebooklm chapter, 2026-09-08

Six-persona review of `chapters/enrichment-rag-notebooklm.qmd` after the
plain-language pass of the same day, per `curriculum/personas.md`, Elena first,
Lindqvist last. Filed as issue #34. Each section lists findings and the fix
applied in the same pass. Reviewed by the AI assistant; author to confirm.

The plain-language pass preceded this review and is summarised at the end.

## Elena (avoider, surgery, free tier, ESL) — reads first

1. **Does the chapter assume she uses these tools?** No. The co-intern
   suggests NotebookLM and the result is shown. "Grounded" and "retrieval"
   are now defined in plain words before "Why this matters," and every
   pipeline word is defined in the sentence that first uses it. *Confirmed.*
2. **Assumed background.** "Who won the 2020 World Series" assumes she knows
   it is baseball. *Fix:* "the baseball championship" added.
3. **Phone number / signup.** The "Getting in" callout said a personal Gmail
   asks for nothing more. True for an existing account; making a *new* Google
   account often asks for a phone number, which she will not give. *Fix:* one
   sentence sends her to the no-Google path (ChatGPT Edu or Copilot with
   attached files) in that case.
4. **Is the one-minute check followable?** "Two of the five confidence
   intervals cross zero" was the whole check, with its meaning implicit.
   *Fix:* "which means the gain for those two models may be nothing."
5. **Vendor vocabulary in the opening block.** "Pooled gain," "automated
   judge," "base models" appear in the grounded-answer block. It is verbatim
   tool output and the chapter asks her to judge only the first sentence, so
   it stays. *No change.*
6. **Skeptical moment; prompt fluency.** Step 2 supplies the questions; Step 4
   says not to prompt carefully; the click-through is the method. *No change.*

## Marcus (early adopter, radiology)

1. **Claim stronger than the evidence.** "Nothing in the pipeline knows that a
   table is a table." Better tools add layout-aware parsing and Marcus will
   know that. *Fix:* hedged to "the basic pipeline," plus a sentence that
   better tools try to keep tables whole and you cannot tell from outside
   whether yours does, or how well.
2. **"Grounding does not make a model smarter."** Rests on the strong models'
   non-significant accuracy gain in Vollmer et al. The PMC full text was
   re-checked (according to PubMed, [DOI](https://doi.org/10.3390/diagnostics16152456)):
   the authors attribute that pattern "partly to ceiling compression that we
   do not interpret mechanistically." *Fix:* the caveat is now in the chapter
   and the sentence reads "does not reliably make a model smarter."
3. **Anything he could not get from the model; a concrete failure; evaluator
   role.** The split-table mechanism, the real score-1 specimen, the scored
   citation set, and Seki et al. on radiographs. *No change.*

## Priya (clinician-in-waiting, emergency medicine)

1. **Skip the mechanism, still know what to do?** The practical-rule callout,
   the Check table, and the summary stand alone. *Confirmed.*
2. **Scenario she recognizes.** Journal club with five PDFs and two call
   shifts. *Confirmed.*
3. **Accountability and documentation.** "The clinician who repeated the
   sentence owns it"; "what do you say when the chief asks how you prepared"
   covers disclosure; the citation on the slide is the paper. *No change.*
4. **One sentence for a co-intern.** "Grounding does not fix reading. Click,
   read a line above and below, ask narrower or broader." In the summary.
   *No change.*

## Jordan (instructional designer)

1. **Standalone reading order.** The 2/1/0 scale was used in "Why grounded
   tools fabricate less," and "score 1" in "The failure grounding does not
   fix," before Step 2 defined them. A student who skipped the appraisal
   chapter would be lost. *Fix:* one-line gloss of 2/1/0 at first use;
   "score 1" now refers to "the 2/1/0 scale."
2. **Alt text.** The mermaid pipeline figure had no `fig-alt`; the foundations
   chapter's mermaid figures do. *Fix:* added. Note: Quarto renders mermaid
   as inline SVG in this project, so the `fig-alt` may not surface as an
   `alt` attribute; see the open item below.
3. **Objectives to activities.** 1 and 2 map to the no-memory and no-learning
   Check rows; 3 to the pipeline row; 4 to Step 4 and the "Why the citations
   are real" row; 5 to Step 2 and the scored-citations row; 6 to Step 1 and
   the search-limit row. *Confirmed.*
4. **Time.** About 5,600 words. 20 minutes of reading is honest for a median
   reader; Elena will take nearer 30. The subtitle's "about one hour" holds.
   *No change.*
5. **Scenario returns.** "Write it down" puts the reader back on Monday with
   the slide; the summary's last bullet names Thursday. *Confirmed.*

## Dr. Okafor (borrowing educator)

1. **What will a student ask that the chapter does not answer?** "How big is a
   context window?" and "Does NotebookLM really work like this?" *Fix:* one
   clause on size (a long book to a small shelf, no number, so it does not go
   stale) and one sentence that Google does not publish NotebookLM's
   internals and the six steps are the general design every such tool
   follows.
2. **Run the Do alone.** Ready-made set with URLs, supplied questions,
   expected results in the answer key, fallback tool. *Confirmed.*
3. **Restatable mechanism.** "Handed the answer and asked to paraphrase it";
   "a phonebook sorted by meaning." *Confirmed.*
4. **Stale in twelve months.** Tier limits and institutional access carry
   VERIFY flags; the specimen has a re-run procedure; the pipeline is named
   as the durable part. *No change.*
5. **Image reuse.** Redrawn CC BY data, CSS blocks, mermaid code. *Confirmed.*

## Dr. Lindqvist (clinical ethicist) — reads last

1. **PHI nudge.** None. Sources are published papers or the student's own
   writing; the callout excludes de-identified cases and classmates' data.
   *Confirmed.*
2. **Could an illustrative artifact be mistaken for real material?** The
   split-table block was not labeled illustrative and could be read as a real
   stored chunk from a named tool. *Fix:* the lead-in says it is an
   illustration built from the paper's reported differences and not a
   screenshot of any tool.
3. **Certainty exceeding evidence.** "The common result is a smoothed-over
   consensus" had no citation. *Fix:* "a frequent result," with "nobody has
   measured how often," and the Do block as the test.
4. **Numbers in the illustration.** The Difference column of the chunk block
   (+0.94, +0.86, +0.72, +0.36, +0.30 with CIs) matches the Results text of
   the PMC full text. The Without/With column values and the "Table 6" label
   could not be checked because the text extract drops tables. *Open;*
   recorded in the answer key's instructor prep.
5. **Who bears the cost; disclosure of the course's own AI use.** Patient and
   the repeating clinician are named; the specimen callout names the tool and
   says the vendor does not name the model. *Confirmed.*

## Fixes applied in this pass, in order

1. Chunk block labeled an illustration; "nothing in the pipeline knows" hedged
   to the basic pipeline, with a sentence on layout-aware tools.
2. Vollmer et al.'s ceiling-compression caveat added; "does not reliably make
   a model smarter."
3. 2/1/0 scale glossed at first use; "score 1" tied to the scale, not the
   other chapter.
4. Phone-number sentence in "Getting in."
5. `fig-alt` on the mermaid pipeline figure.
6. Context-window size clause; NotebookLM-internals sentence.
7. Confidence-interval gloss; World Series gloss; disagreement-smoothing
   hedge.
8. Answer key: instructor-prep note on the chunk block's unverified column
   values.

## Open items for the author

- Confirm the chunk block's Without/With values and the "Table 6" number
  against the Vollmer PDF, or leave the block labeled illustrative (it now
  is).
- Carried from 2026-09-07: run the ready-made set in NotebookLM before the
  cohort and replace the specimen if the live run is cleaner; confirm tier
  limits on Google's help page and institutional NotebookLM access.
- Stylesheet (not changed here): the citation links in `.grounded-answer`
  have link text "1", which a screen reader announces as "link, 1". An
  `aria-label` such as "source 1" on `.grounded-answer .cite`, set in
  `styles.css` or the block's HTML, would help. Also check whether the
  mermaid `fig-alt` reaches the rendered SVG; if not, this is a Quarto
  mermaid-rendering setting, not a chapter fix.
- Heading rename: "The standing question" became "Write it down" and "The
  idea" became "How it works" in this chapter, per the plain-language brief.
  If sibling chapters kept the pattern's headings, the coordinator should pick
  one and align.

## Plain-language pass (same day, committed first)

Replaced with plain words: retrieval-grounded, source-grounded summarizer,
provenance, mechanically, load-bearing, attention, structural / by
construction, diligence, characterization, corpus, attribution, navigating,
artifact, axis, hedge, external validation, guideline-bound, organizational
unit, mitigation, seminal, prerequisites, pre-vetted, generalizes,
training-data problem. Kept and defined at first use: grounded, retrieval,
retrieval pipeline, context window, token, weights, embedding, index,
hallucination. Roughly 60 sentences split. No em-dashes. Numbers, citation
keys, VERIFY spans, figure ids and alt text, callouts, objectives mapping,
and section order unchanged. Check row "The structural argument" renamed
"Why the citations are real"; answer key updated to match.
