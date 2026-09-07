# Review: core-ethics-regulation chapter, 2026-09-07

Six-persona self-review of `chapters/core-ethics-regulation.qmd` per
`curriculum/personas.md`, Elena first, Lindqvist last. Each finding is followed
by the fix applied before commit, or by the reason it was left. Reviewed by the
AI assistant that drafted the chapter; author to confirm.

## Elena (avoider, surgery, free tier, ESL) — reads first

Passes, with three fixes.

1. **Terms.** First draft used "standard of care," "learned intermediary,"
   "automation bias," "business associate agreement," "high-risk," "PCCP,"
   and "non-device CDS" before defining them. *Fixed:* each now carries a
   defining clause at first use; "standard of care" is defined inside the
   four-elements paragraph, "learned intermediary" in the same paragraph,
   "automation bias" at the end of the Jabbour section, "BAA" in the contract
   paragraph.
2. **No account needed.** Her question is whether she can do the Do on a free
   account without a phone number. *Fixed:* the Time note and the Do warning
   say that no chatbot is required at all, and that if one is used it is for
   finding documents, not answering.
3. **Skepticism is the right answer here.** The whole chapter is a case where
   her instinct (do not trust the draft) is the standard of care. *Left as
   is,* because the scenario makes it without saying so; the Check row "The
   device question" rewards "cleared is not enough."

Reads slowly but has no demo she cannot follow; the images (a note, a bar
chart, a flowchart) land cold.

## Marcus (early adopter, radiology)

1. **A failure he did not expect.** The Jabbour finding that explanations did
   not help is the one. He believes in explainability. *Present in the chapter
   and in the figure.*
2. **"So the tool is safest when it agrees with me."** That is the jury-study
   takeaway, and the first draft let him stop there. *Fixed:* the sentence
   after the juror studies now says that the moment the tool disagrees, he is
   on his own in either direction, and the deskilling section says the tool
   can change him even when it is right.
3. **His specialty.** Radiology is where most cleared devices are, and
   criterion 1 puts every imaging tool on the device side. *Fixed:* the
   criterion-1 example in the device section names imaging; the device-list
   bookmark says most are radiology, with the count flagged.
4. **The thing he can do tomorrow.** Ask whether there is a BAA and a PCCP.
   *Present.*

## Priya (clinician-in-waiting, emergency medicine)

Passes on scenario; this is her chapter.

1. **What do I document?** *Fixed:* the "Documentation" paragraph gives two
   concrete habits (read the plan against the conversation; know what the
   auto-inserted attestation says) rather than "be careful."
2. **The sepsis alert she silenced.** *Fixed:* Part B question 4 is that alert,
   and the device section uses it as the worked criterion-1/criterion-4
   example.
3. **The co-intern sentence.** "You sign it, you own it; the patient has to
   know; and there is a contract, or there is not." *In the summary.*
4. **Who is accountable.** Named: the physician under current doctrine, the
   hospital and the developer as additional defendants per Mello and Guha,
   and the patients in the consent study who already assign it to the
   physician.

## Jordan (instructional designer)

1. **Time.** Subtitle says 75 minutes; the Time note says 25 + 20 + 25 + 5 =
   75. Reading is ~4,400 words of prose plus a table and three figures; 25
   minutes is tight for a median reader but honest for an MS4 skimming the
   regulatory subsections. *Left; the scavenger hunt is capped at two
   questions to protect the budget.*
2. **Objectives map.** 1 → Part B q2 and Check "four elements"; 2 → Part B q1;
   3 → Check "Jabbour sentence"; 4 → Part B q4 and Check "device question";
   5 → Check "PCCP sentence"; 6 → Part A and the Check rows for it; 7 → the
   standing question and the Check "your position" row. Objective 6 is a
   compound objective; *fixed* by splitting its Check coverage across two
   rows. No read-only objectives.
3. **Scenario returns.** In "Four cells" (cell B by a side door), in the
   documentation paragraph, in Watch or listen, in Part B, in the standing
   question, and in the last summary bullet. *Yes.*
4. **Accessibility.** The Jabbour SVG has `fig-alt` and the numbers in the
   alt text; the mermaid figure has a caption; the note block is HTML text,
   not an image. The podcast has a full transcript on the episode page.
   *Yes.*
5. **`[VERIFY]` flags render.** Two, both styled. One on the insurer quote,
   one on the device count. *Accepted; they are the pattern.*
6. **Does every visual teach?** The note block is the artifact under
   appraisal; the bar chart carries the "explanations did not help" finding
   with its confidence intervals, which the prose cannot; the flowchart makes
   criterion 4 a question about the clinician rather than the model; the
   clippings show the disclosure question is live. *No decoration.*

## Dr. Okafor (borrowing educator)

1. **Can I run the Do alone?** Part A needs only the question list and a
   browser; the answer key gives current answers with sources and tells the
   tutor what "moved" looks like. Part B needs the 2×2, which is in the
   chapter. *Yes.*
2. **Can I restate the mechanism?** The four elements of negligence, the four
   criteria, and the PCCP are each restated in one plain sentence. The
   Jabbour finding is one sentence plus a figure. *Yes.*
3. **What will a student ask that the chapter does not answer?** "Is my
   institutional ChatGPT covered by a BAA?" *Answered:* not unless the
   institution says so in writing. "What about the EU if I train abroad?"
   *Pointed at:* the EU section and question 4. "Can I be sued for *not*
   using a tool?" *Not answered;* it is cell C's mirror and belongs in a
   future revision. Noted here rather than added, to hold the budget.
4. **Institution-specific parts, marked?** Scavenger-hunt question 10 and the
   insurer callout are the only ones and both say so.
5. **Stale in twelve months?** Almost certainly, and the chapter says so four
   times, with a callout titled for it. The answer key is dated and the prep
   note says to re-check two pages the morning of the session.
6. **Image licences.** No third-party images. The note block and the bar
   chart are original; the SVG is data redrawn from a cited paper; the
   mermaid diagram is generated. All reusable by an adopter.

## Dr. Lindqvist (clinical ethicist) — reads last

1. **PHI.** Mr. Alvarez is labeled synthetic in the note block and in the Do
   warning. Part A uses public documents only. Question 10 asks about the
   student's own institution's policy, which is not patient data. *Passes.*
2. **Does the patient know?** *Fixed in the scenario:* the waiting-room sign
   and the medical assistant's mention are there, and the chapter says
   whether that is consent is being litigated. Disclosure has its own
   paragraph with the consent study's numbers.
3. **Who bears the cost?** Mr. Alvarez, named. The equity finding (higher
   speech-recognition error rates for Black speakers) was in the first draft
   only in Go deeper. *Left there but made explicit:* "the patient most
   likely to be misdocumented is not random."
4. **Contested presented as settled?** The lawsuits are labeled allegations
   twice. "No verdict" is stated as of the chapter's date and is itself a
   scavenger-hunt question. The juror studies are experiments about
   reasonableness, not law, and the chapter says jurors "reward" rather than
   "courts hold." The Doctors Company statement carries a `[VERIFY]`. *Passes.*
5. **Course's own AI use.** The ledger row is added; this review says who
   wrote what.
6. **Could the illustrative artifact be mistaken for real material?** The
   note block's footer says illustrative, synthetic, not any vendor's or
   institution's. No vendor is named in it. *Passes.*

No veto. The one tone note: the scenario ends with a stroke, which is heavy
for an opening. Kept, because the module's seed is "a scribe error in a note
you signed; who answers for it," and a trivial harm would make the question
trivial.

## Action list applied before commit

1. Defining clauses for the seven terms (Elena 1).
2. "No chatbot required" in Time and in the Do warning (Elena 2).
3. "On your own in either direction" after the juror studies (Marcus 2).
4. Radiology named at criterion 1 (Marcus 3).
5. Two documentation habits, not a warning (Priya 1).
6. Sepsis alert as the worked example and Part B q4 (Priya 2).
7. Objective 6 split across two Check rows (Jordan 2).
8. Sign and MA mention in the scenario; "allegations" stated twice
   (Lindqvist 2, 4).
9. Equity sentence made explicit in Go deeper (Lindqvist 3).

## Open

- "Can I be sued for not using a tool?" (Okafor 3) — a paragraph for the next
  revision.
- Back-port to `chapters/core-appraisal.qmd`: replace its HTI-1 `[VERIFY]`
  with "in force as of September 2026; HTI-5 proposes to remove the
  source-attribute requirement; see the ethics and regulation chapter." Not
  done here because this branch does not edit other chapters.
