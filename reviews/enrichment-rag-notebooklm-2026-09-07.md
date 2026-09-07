# Review: enrichment-rag-notebooklm chapter, 2026-09-07

Six-persona self-review of `chapters/enrichment-rag-notebooklm.qmd` per
`curriculum/personas.md`, Elena first, Lindqvist last. Each section lists
findings and the fix applied in the same pass. Reviewed by the AI assistant;
author to confirm.

## Elena (avoider, surgery, free tier, ESL) — reads first

1. **Does the chapter assume she uses these tools?** The scenario has a
   co-intern suggest NotebookLM and shows the result, so she does not have to
   have used it. But the first draft used "chunk" and "embedding" before
   defining them. *Fix:* objective 3 still names the six pipeline words, since
   they are what the objective is, but every one of them is now bolded and
   defined in the sentence that first uses it in the pipeline section, and
   "context window" and "token" are defined in the first section before
   anything else uses them.
2. **Phone number / signup.** NotebookLM needs a Google account. She will not
   give a phone number. A personal Gmail is the path; institutional accounts
   may be disabled. *Fix:* "Getting in" callout says personal Gmail works and
   gives a no-Google fallback (ChatGPT Edu / Copilot with attached files) with
   an honest note that the guarantee is weaker.
3. **Is her fear separated into justified and outdated?** Yes: the chapter
   says the chatbot's answer "may be better written and more useful" and that
   grounded tools misread real sources. The skeptical moment is the Step 2
   click-through, where skepticism is the method. *No change.*
4. **Prompt fluency.** Step 4 tells her not to prompt carefully, so results
   do not depend on phrasing. Step 2 questions are supplied for the pre-vetted
   set. *No change.*
5. **Do the visuals land cold?** The split-table block needs no prior
   knowledge; the bar chart has two pairs of bars with plain labels. The
   opening grounded-answer block is the thing she is asked to judge and is
   labeled as a real output with its provenance. *No change.*

## Marcus (early adopter, radiology)

1. **Anything he could not get by asking the model?** The split-table
   mechanism and the real specimen. He has used NotebookLM; he has not seen it
   fail on a table. *No change.*
2. **A concrete case where his habit gets the wrong answer.** The opening
   specimen is exactly that, and it was produced by a real run, not
   constructed. *No change.*
3. **Treats him as evaluator?** The Do block asks him to score every citation
   on a published scale and to produce the disagreement result. Seki et al.
   (NotebookLM on radiographs, agreement with dentists near zero) is his
   specialty's hook and is in the pre-vetted set. *Fix:* added the "read them
   as a pair" note in Go deeper so the radiograph paper is framed as
   wrong-tool-for-the-task, not as an anti-AI result.
4. **Thing to do tomorrow.** Build a notebook from a rotation's reading list;
   the one-minute check. *No change.*

## Priya (clinician-in-waiting, emergency medicine)

1. **Skip the mechanism, still know what to do?** The "practical rule"
   callout and the Check table stand alone. *Fix:* moved the practical rule
   into its own callout at the end of The idea so it is findable without
   reading the pipeline.
2. **A scenario she recognizes.** Journal club prep with five PDFs and two
   call shifts. Yes.
3. **Accountability and documentation.** The chapter says the citation in
   the slide is the paper, which she has read that part of, and that the tool
   is not a citable source. The EHR-embedded grounded tool is named in Why
   this matters but its governance is left to the ethics chapter. *Fix:* the
   no-PHI callout now names the business associate agreement and says an
   institutional account does not change the rule unless the institution says
   so in writing.
4. **One sentence for a co-intern.** "Grounding fixes the reference, not the
   reading. Click and read a line above and below." Present in the summary.

## Jordan (instructional designer)

1. **Objectives to activities.** 1 and 2 map to Check rows (no-memory,
   no-learning); 3 to the Check pipeline row; 4 to the Step 4 contrast and
   the structural-argument row; 5 to Step 2 and the score-1 row; 6 to Step 1
   and the search-limit row. Objectives 1 and 2 are read-only plus Check,
   which the pattern allows. *No change.*
2. **Time honesty.** 20 min reading, 7 min video, 30 min doing, plus Check
   and standing question ≈ 60–65 min. The Do steps are budgeted at 10 + 10 +
   5 + 5 = 30 and each is bounded by a supplied question set. Adding sources
   and waiting for processing is the risk; the pre-vetted set is four URLs.
   *Fix:* Step 1 tells students to paste PMC URLs rather than download PDFs
   first, which is faster.
3. **Standalone?** The chapter references the appraisal chapter's figure and
   2/1/0 scale. *Fix:* the scale is restated in Step 2 (2, 1, 0 with
   one-line definitions) so a student who skipped that chapter can score.
   The cross-chapter figure reference is a link plus plain-text description.
4. **Accessibility.** The video has YouTube captions; the reading alternative
   is a text article. Every image has fig-alt; the styled blocks are HTML
   text, readable by screen readers. *No change.*
5. **Scenario returns?** Standing question puts the reader back on Monday
   with the slide. Summary's last bullet names Thursday. *No change.*
6. **VERIFY flags render as text.** Two, both styled with `.verify`, both
   about operational facts (tier limits, institutional access) that must be
   checked the week before. *No change.*

## Dr. Okafor (borrowing educator)

1. **Can they run the Do alone?** Yes: pre-vetted set with URLs, supplied
   questions, expected results in the answer key, and a fallback tool.
2. **Can they restate the mechanism?** "Handed the answer and asked to
   paraphrase it" and "a phonebook sorted by meaning" are restatable. The
   split-table block is the demo. *No change.*
3. **What will students ask that is unanswered?** "Is Gemini/ChatGPT with
   web search a grounded tool?" *Fix:* Step 4 now notes that ChatGPT Edu and
   Copilot may cite web pages, and that this is a different provenance
   question (real page, but is it evidence?). "What about OpenEvidence?" is
   the appraisal chapter's ground.
4. **Institution-specific parts marked?** The Google account access note is
   flagged VERIFY and says what to check. *No change.*
5. **Stale in twelve months?** Tier limits (flagged), the specific tool (the
   chapter says the pipeline is the durable part), and the specimen (the
   answer key says to re-run it). *No change.*
6. **Image reuse.** The bar chart is redrawn data with a CC BY 4.0 source
   named; the styled blocks are CSS; no NC or fair-use material in this
   chapter. Adopters can reuse everything. *No change.*

## Dr. Lindqvist (clinical ethicist) — reads last

1. **PHI nudge?** Step 1 says "papers you were already going to read"; the
   no-PHI callout excludes de-identified cases explicitly. No activity
   touches patient data. *No change.*
2. **Patient in the scenario?** There is no patient; the scenario is journal
   club. The chapter's EHR-embedded example in Why this matters mentions a
   tool answering from protocols, not from a patient's record. *No change.*
3. **Who bears the cost when the tool is wrong?** The misreading specimen is
   about a paper, and its cost is a wrong slide. *Fix:* added to Why this
   matters that the same misreading in an EHR-embedded tool lands on a
   patient, and that the clinician who repeats the sentence owns it. Kept to
   one sentence per the persona file's warning against preachiness.
4. **Contested question presented as settled?** The chapter says the chatbot
   may give the more useful answer, that accuracy gains from retrieval were
   not significant for strong models, and that a notebook can smooth
   disagreement. Nothing is settled in either direction. *No change.*
5. **Course discloses its own AI use?** The specimen names the tool that
   produced it, says the model is unnamed by the vendor, and the answer key
   says NotebookLM itself could not be run by the assistant. The AI-LEDGER
   row records it. *No change.*
6. **Images licensed; artifacts mistakable for real material?** The
   grounded-answer block is a real output and is labeled as such with the
   tool named; it is not styled to look like NotebookLM's interface. The
   chunk block is illustrative and says "chunk 7 of 23" with no product name.
   *No change.*

## Fixes applied in this pass, in order

1. Objectives in plain language; six pipeline words defined at first use.
2. "Getting in" callout: personal Gmail path, admin-disable warning, no-Google
   fallback with weaker-guarantee note.
3. Practical rule as its own callout at the end of The idea.
4. No-PHI callout names the BAA and the institutional-account boundary.
5. Step 1 prefers PMC URLs over PDF download.
6. 2/1/0 scale restated in Step 2.
7. Step 4 note on web-citing chatbots.
8. One sentence in Why this matters on who bears the cost in the EHR case.
9. Go deeper frames the two NotebookLM papers as a pair.

## Open items for the author

- Run the pre-vetted set in NotebookLM before the cohort; replace the
  specimen if the live run is cleaner (answer key has the procedure).
- Confirm tier limits on Google's help page and institutional access.
- The cross-chapter `@fig-citation-paths` reference renders as a link only
  because both chapters are in one book; if the appraisal chapter's figure
  label changes, this breaks at render.
