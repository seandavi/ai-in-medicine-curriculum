# Review: enrichment-agentic-coding chapter, 2026-09-07

Six-persona self-review of `chapters/enrichment-agentic-coding.qmd` per
`curriculum/personas.md`, Elena first, Lindqvist last. Each section lists what
the persona found and what was then changed in the chapter. Reviewed by the
chapter's AI author; course author to confirm.

## Elena (avoider, surgery, free tier, ESL) — reads first

Passes, with four fixes applied.

1. **She is in the scenario.** The intern with the bookmark is anyone on the
   team, and "you have used it twice today" makes her complicit without
   making her the AI person. No change.
2. **Account and phone number.** The Do assumed Claude.ai Artifacts in the
   module. Claude.ai signup requires a phone number (web search, 2026-09).
   *Fixed:* the assumed path is the institutional ChatGPT Edu canvas; the
   universal fallback is "save the code as `calc.html` and open it", which
   works with Copilot and any chatbot; Claude.ai and Google AI Studio are
   listed as alternatives with what each asks at signup.
3. **Undefined terms.** Checked on first use: coding agent, permissions,
   canvas, business associate agreement, vibe coding, comprehension
   abdication, non-device clinical decision support. "MRN" appeared in the
   VIBE-HI table. *Fixed:* "medical record numbers".
4. **Prompt fluency.** The starter prompt is verbatim, but the chapter did not
   say why that helps her. *Fixed:* a sentence in Part A step 2 saying the
   fixed text makes the result reflect the model, not her fluency, and that
   the same prompt varies day to day anyway.

Her skeptical moment exists and is the chapter's spine: the coordinator is
right, the tool is wrong, and "none found" needs a reason. The ten-minute way
in is a paste. The comic's alt text carries the joke for a reader who has not
seen it.

## Marcus (early adopter, radiology)

Passes on content once the specimen is real.

1. **A failure in the thing he built.** The module promised it; the chapter
   has to show it. *Partly done:* two live runs of the starter prompt were
   started (CHA₂DS₂-VASc and MELD-Na, Claude, no tools, 2026-09-07) and did
   not return in time to be read. The specimen callout is therefore written
   as expected behaviour from the known edge failures and says so in its
   first line; the answer key tells the instructor to replace it with a real
   run before the first cohort. The failure Marcus is promised still arrives,
   in his own Part B, and the opening scenario shows one in full.
2. **Something he could not get by asking the model.** The Goodell one-in-three
   figure with the thirteenfold tool effect, the VIBE-HI four questions, and
   the Egaimi registry validation are all things a model will paraphrase but
   not source. Kept.
3. **His specialty.** Fleischner 2017 is in the menu as the radiology build,
   and it is the only decision-table item, so his build is harder than the
   others, which he will like. The chapter makes no claim about radiology's
   future in either direction.
4. **Treated as an evaluator.** Part C's device paragraph and the "one
   sentence" ask him to place a tool, not to be restrained from building one.
   The standing question puts him in the room with the resident who built
   the bad one.

## Priya (clinician-in-waiting, emergency medicine)

Passes on scenario; one gap fixed.

1. **Recognisable scenario.** A team tool everyone uses and nobody checked is
   her sub-internship. Wells and qSOFA are in the menu.
2. **Who is accountable, and what to document.** The chapter said "toy, not
   device" and stopped. *Fixed:* a "Who signs" callout in the device section:
   the clinician who acted on the number is accountable, the note records
   the score and a checked source, and the ethics and regulation chapter
   takes documentation further.
3. **The one sentence** is an explicit deliverable in Part C and a Check row,
   and must contain a verb meaning *compare against an outside source*.
4. **Skipping the mechanism.** The Do and Check stand alone without the
   chatbot-versus-agent section; objective 1 is the only thing she loses.

## Jordan (instructional designer)

1. **Objectives map.** 1 → Check row 1 (read-only objective, assessed in
   Check). 2 → Part A and Check row 2. 3 → Part B and the comprehension test,
   Check rows 3–4. 4 → Part C device paragraph, Check row 5. 5 → the Do's
   warning callout and Check row 6 (read-only, assessed in Check). Two
   read-only objectives, both assessed; acceptable for a 75-minute chapter.
2. **Time.** Subtitle and Time note agree: 20 + 15 + 35 + 5 = 75. The chapter
   is about 300 lines of prose plus tables, against the exemplar's 700 for two
   hours; 20 minutes of reading is honest for a median reader. Part A at 12
   minutes assumes the model returns a working page on the first try, which
   the specimen runs did; if a cohort's tool is slow, the live session
   absorbs it.
3. **Scenario returns.** In the standing question (the coordinator on the
   phone, the bookmark) and in the summary's last bullet.
4. **Accessibility.** Every image has `fig-alt`; the video is on YouTube with
   automatic captions (noted) and on a podcast feed; no paywall anywhere;
   the talks links are the author's own archive.
5. **Visuals earn their place.** The app mock is the artifact under
   appraisal, with the missing field visible. The press clippings show three
   framings of one incident. The mermaid figure is the mechanism. The comic
   is the only one that is close to decoration; it stays because its last
   panel *is* "toy, not device" and the caption says so.
6. **Check is self-applicable.** Every row has a concrete pass and fail.

## Dr. Okafor (borrowing educator)

1. **Running the Do alone.** The tool callout, the menu, the verbatim prompt,
   and the three cases are enough; the answer key adds the expected edge
   for each score and the instructor prep.
2. **Mechanism restatable.** "A chatbot writes and stops; an agent plans,
   acts, observes, repeats, inside permissions" plus the figure. The
   junior-colleague model is one sentence.
3. **Institution-specific parts.** The ChatGPT Edu canvas assumption is in
   one callout with a `[VERIFY]` flag and a fallback that needs no
   institution at all.
4. **Stale in twelve months.** Tool names, the Copilot student plan, the FDA
   guidance revision, and the two names for the practice are all dated in
   the text or flagged. The security numbers are explicitly called old.
5. **Image licences.** xkcd is CC BY-NC 2.5 and the caption says the
   non-commercial condition travels with reuse. The app mock and clippings
   have no licence to inherit.

## Dr. Lindqvist (clinical ethicist) — reads last

1. **No PHI.** Stated three times with escalating specificity: the Time note,
   the "Patient information, once more" section, and the Do's warning
   callout ("If a test case needs a sodium of 118, invent a patient with a
   sodium of 118"). The specimen runs used no patient data. Nothing in the
   Do touches a real patient, a classmate, or a real dataset.
2. **The patient in the scenario.** First draft never mentioned her
   knowledge. *Fixed:* "The patient, who would have waited unlisted on the
   strength of a number from a weekend project, does not know the project
   exists."
3. **Who bears the cost.** Named: the patient waiting unlisted; the ~16,000
   people whose contacts went untraced. The security callout names the risk
   to whoever's data would be in the tool.
4. **Contested claims presented as settled?** "Vibe coding is passé" is
   attributed to Karpathy as his view. The FDA device boundary is stated as
   turning on a criterion and left to the ethics chapter, with the January
   2026 revision flagged. The security figures are dated and hedged.
5. **Illustrative artifact.** `teamtools.local/meld`, "drawn in CSS; not a
   real product". Cannot be mistaken for a vendor.
6. **Course disclosure.** The specimen callout says in its first line that it
   is expected behaviour rather than a recorded run; the ledger row records
   the attempted runs and what was and was not verified by a human.

No activity would fail an IRB sniff test.

## Verification notes

- 18 PMIDs retrieved and read by tool this session; 4 DOIs resolved through
  Crossref. The BMJ news item for the Excel incident was located by
  citation lookup (PMID 33023893) after an initial DOI guess, and the
  chapter now cites the PMID and attributes the row-limit mechanism to the
  clippings, since the BMJ title speaks only to the count and the contacts.
- The opening scenario's arithmetic was checked in Python. The first draft's
  patient (sodium 118, creatinine 2.1, dialysis) produced the *same* MELD-Na
  with and without the two omitted rules, because the two omissions
  cancelled. The patient was changed so that a single missing rule explains
  the gap; the answer key records the original as a tutor example.
- Karpathy video: 2,371 seconds from the YouTube page's metadata (39 min);
  Apple Podcasts lists 40 min and a 19 June 2025 release.
- The `.app-mock` block was added to `styles.css` at the end, with a comment
  naming the chapter, because no existing block draws a light application
  window.

## Open flags

- `[VERIFY]` Karpathy posts (2 Feb 2025; Feb 2026) and Collins WOTY 2025:
  secondary sources only in `research/`.
- `[VERIFY]` FDA CDS guidance revised 6 January 2026: current text and what
  changed.
- `[VERIFY]` Canvas code execution enabled in the institutional ChatGPT Edu
  workspace.
- `[VERIFY]` GitHub Copilot student plan signup status.
- `[VERIFY]` (answer key) 2023 ACC/AHA and 2024 ESC wording on the sex
  category in CHA₂DS₂-VASc.
