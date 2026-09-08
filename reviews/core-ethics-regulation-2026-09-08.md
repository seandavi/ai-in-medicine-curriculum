# Review: core-ethics-regulation chapter, 2026-09-08

Six-persona review of `chapters/core-ethics-regulation.qmd` after the
plain-language pass, per `curriculum/personas.md`, Elena first, Lindqvist
last. Filed as GitHub issue #37 (part of #12). Each finding is followed by
the fix applied before commit, or by the reason it was left. Reviewed by the
AI assistant that did the plain-language pass; author to confirm.

## The plain-language pass, briefly

Terms replaced or defined on first use: plaintiff, elements (of negligence),
standard of care, learned intermediary doctrine, exposure (as legal risk),
cell (now "box" of the 2×2), doctrine (now "current law"), litigated (now
"argued in court"), indemnify (now "pay the claim"), underwriting (now
"decide case by case"), criteria (now "four tests, which the law calls
criteria"), in vitro diagnostic (glossed as a lab test), signal-acquisition
system (now "a monitor"), non-device CDS, clearance, substantially equivalent
(now "about as safe and effective as something already on the market"),
Predetermined Change Control Plan, attestation, covered entity, business
associate agreement, adjudicated (now "decided by a court"), high-risk,
deregulatory (now "loosening the rules"), preempt (now "override"), adenoma
detection rate, deskilling, vignettes (now "written cases"), falsifiable
condition (now "a condition that could prove you wrong"), artifact (now
"what you hand in" / "the real product of the exercise"), delegate (now
"hand over"), "The idea" (now "What you need to know"), "The standing
question" (now "The question you keep"). About 70 long sentences were split.
No number, citation key, `[VERIFY]` span, figure id, `fig-alt`, block class,
callout structure, objective mapping, or section order changed. The answer
key was updated for "cell" to "box" and for the rubric's last row.

## Elena (avoider, surgery, free tier, ESL) — reads first

Gets in the door. No chatbot is needed anywhere; Part A is a browser and
public documents; the images (a note, a bar chart, a flowchart, three
headlines) land cold.

1. **"Hallucination" used without a definition in this chapter.** Earlier
   chapters define it, but each chapter stands alone. *Fixed:* a short gloss
   at first use in the device section.
2. **"Court docket."** *Fixed:* glossed in Part A as the court's own record
   of the case.
3. **"The month-one boundary case from the appraisal chapter"** is a pointer
   she cannot follow if she skipped that chapter. *Fixed:* the sentence now
   says what the case was (a tool your hospital licenses inside the EHR).

## Marcus (early adopter, radiology)

Jabbour is still the failure he did not expect. The "on your own in either
direction" line stops him reading the juror studies as permission. He can
ask about a BAA and a PCCP tomorrow.

4. **Radiology.** Criterion 1 puts every imaging tool on the device side,
   which is why most of FDA's list is radiology, and the chapter said so only
   in a Go-deeper bookmark. *Fixed:* one clause in the worked-example
   paragraph of the device section.

## Priya (clinician-in-waiting, emergency medicine)

Her chapter. The Documentation, Disclosure, Contract section stands alone if
she skips the mechanism; the sepsis alert is the worked example and Part B
q4; the co-intern sentence is in the summary.

5. **The error found after signing.** The two habits cover catching it
   before signing; the realistic case is finding it later. *Fixed:* one
   sentence in the Documentation paragraph: add an addendum, do not quietly
   edit the signed note.

## Jordan (instructional designer)

1. **Objectives map.** 1 → Part B q2 and Check "four elements"; 2 → Part B
   q1 and Check "box for the note"; 3 → Check "Jabbour sentence"; 4 → Part B
   q4 and Check "device question"; 5 → Check "PCCP sentence"; 6 → Part A and
   its two Check rows; 7 → the closing question and Check "your position".
   Unchanged by the pass.
2. **Scenario returns.** In "Four boxes", Documentation, Watch or listen,
   Part B, the closing question, and the last summary bullet. *Yes.*
3. **Accessibility.** The mermaid flowchart had a caption but no `fig-alt`.
   *Fixed:* added. The bar chart and the note block were already fine. The
   podcast has a full transcript.
4. **Time.** About 4,500 words of prose. 25 minutes reading is tight for a
   median reader; the pass added sentences but not length. *Left,* with the
   two-question cap on Part A protecting the budget. **Open for the author:**
   whether to trim the EU/US paragraph.
5. **Block headings.** "The idea" and "The standing question" were renamed
   per the pass brief. If sibling chapters chose different plain names, the
   coordinator should pick one set. **Open for the author.**

## Dr. Okafor (borrowing educator)

Can run Part A and Part B alone; the answer key is dated and says what
"moved" looks like; mechanism is restatable in one sentence each; no
third-party images.

6. **"Can I be sued for not using a tool?"** Open from the 09-07 review.
   *Fixed:* three sentences after the juror studies, citing Price, Gerke,
   and Cohen's expectation that the standard of care shifts toward AI use as
   it becomes routine.

## Dr. Lindqvist (clinical ethicist) — reads last

No PHI. The patient's knowledge of the scribe is in the scenario and has its
own paragraph. Mr. Alvarez bears the cost, and the equity finding names who
is misdocumented most. Lawsuits are labelled allegations. "No verdict" is
dated and is itself a scavenger question. No veto.

7. **"The only comprehensive AI statute in force."** Contested: South Korea's
   AI Basic Act took effect in January 2026, and China has binding
   generative-AI measures. *Fixed:* "the most comprehensive".
8. **"Your scribe is not a device at all under any of this."** Presented as
   settled; FDA has not ruled on ambient tools that summarize clinical
   content, and the August 2026 discussion paper is about that class.
   *Fixed:* "probably not a device, as FDA reads the criteria today".

## Action list

Fixed in this pass: Elena 1–3, Marcus 4, Priya 5, Jordan 3, Okafor 6,
Lindqvist 7–8.

## Open

- Reading time (Jordan 4): author's call whether to trim.
- Plain names for the pattern's block headings across chapters (Jordan 5):
  coordinator's call.
- Back-port the HTI-1 resolution to `chapters/core-appraisal.qmd` (from the
  09-07 review). Not done; other chapters are off limits in this pass.
- The Korea and China statutes are named here, not in the chapter, so that
  the chapter does not carry two more claims that go stale; the hedge is
  enough for the lesson.
