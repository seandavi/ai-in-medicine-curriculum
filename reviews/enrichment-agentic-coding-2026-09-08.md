# Review: enrichment-agentic-coding chapter, 2026-09-08

Second six-persona review of `chapters/enrichment-agentic-coding.qmd`, after
the plain-language pass of the same day, per `curriculum/personas.md`. Elena
first, Lindqvist last. Filed as issue #27. Reviewed by the chapter's AI
author; course author to confirm.

## What the plain-language pass changed (context for this review)

Same content, same section order, same citations, flags, figure ids, alt
text, and styled blocks. Terms replaced or defined on first use: canvas
(defined in the Time note), specimen → worked example, iterate → ask for two
changes, artifact (kept only as Claude's product name, defined; elsewhere →
"your record", "a running tool"), mental model → the most useful way to think
of it, framing → approach, workflow → a whole data analysis, coined → invented
the phrase, passé → out of date, mutually exclusive → cannot both be true,
bounded → limited, re-identified → traced back to a person, syntactically
correct → correctly written, logistic regression (glossed as a statistical
analysis), clinical validation (glossed), non-device clinical decision
support (glossed), comprehension abdication (defined in plain words), risk
tier (glossed as level), guardrails → safety wording, democratises → opens to
everyone, credentials → passwords, appraisal object → a good thing to
appraise. Headings "The idea" → "How it works" and "The standing question" →
"Before you close this chapter". The one em-dash (in the banner text of the
starter prompt) became a period. Roughly forty long sentences were split.

## Elena (avoider, surgery, free tier, ESL) — reads first

Passes, with two fixes applied.

1. **MDCalc was never explained.** The chapter used it as the outside source
   of truth from the Time note onward without saying what it is. *Fixed:*
   "MDCalc, the free calculator website most residents use" on first use.
2. **"Copilot" is two products.** The fallback meant the Microsoft chatbot;
   Go deeper names GitHub Copilot, a paid editor tool. *Fixed:* "Microsoft
   Copilot" in the fallback.
3. After the pass, canvas is defined before it is needed, the starter prompt
   is a paste into an institutional account with no phone number, the chapter
   says the fixed prompt makes the result reflect the model rather than her
   fluency, and the comic's alt text carries the joke. Her skeptical moment
   is still the spine: the coordinator is right and the tool is wrong.

## Marcus (early adopter, radiology)

Passes on content; one item stays open.

1. **The worked example is still expected behaviour, not a recorded run.**
   Its first line says so, and the answer key tells the instructor to
   replace it before the first cohort. The failure he is promised arrives in
   his own Part B. *Open for the author:* run the CHA₂DS₂-VASc and MELD-Na
   prompts in the institutional ChatGPT Edu workspace and replace the two
   "expected" paragraphs with what came back, model and date recorded.
2. The one-in-three figure, the thirteenfold tool effect (64% to 4.8%), the
   registry validation (*r* = 1.000 for TIMI and GRACE, 226 cases), and the
   VIBE-HI four criteria and "comprehension abdication" were re-read against
   PubMed this pass (PMIDs 40097720, 40462782, 42564266) and match the
   chapter's wording. Kept.
3. Fleischner 2017 remains the radiology build and the only decision-table
   item. No claim about radiology's future in either direction.

## Priya (clinician-in-waiting, emergency medicine)

Passes; no change.

1. The team tool everyone uses and nobody checked is her sub-internship;
   Wells and qSOFA are in the menu.
2. "Who signs" names the accountable clinician and what goes in the note.
3. The one sentence is a deliverable and a Check row.
4. Skipping "How it works" loses only objective 1; the Do and Check stand
   alone.

## Jordan (instructional designer)

1. **The mermaid figure had no `fig-alt`.** The previous review said every
   image had one; the diagram carried only a caption. *Partly fixed:* a
   `fig-alt` describing the two shapes is now in the source. Quarto renders
   mermaid in the browser for HTML and does not emit that alt text; the
   rendered figure is described to screen readers only by its caption
   (`aria-describedby`). A full fix needs `mermaid-format: svg` or `png` in
   `_quarto.yml` so the diagram is pre-rendered with the alt text. That is a
   project-config change, left for the coordinator.
2. **Section heading names.** The pass renamed "The idea" and "The standing
   question", both on the brief's jargon list. Sibling chapters may have
   made different choices. *Open for the author:* pick book-wide names for
   those two blocks and align the chapters.
3. Objectives map is unchanged: 1 → Check row 1; 2 → Part A, Check row 2;
   3 → Part B and the comprehension test, Check rows 3–4; 4 → Part C, Check
   row 5; 5 → the Do warning callout, Check row 6.
4. Time is unchanged and adds up: 20 + 15 + 35 + 5 = 75; Part A 12, B 15,
   C 8. The pass added about 100 words, all of them definitions.
5. The scenario returns in "Before you close this chapter" and in the
   summary's last bullet. Every visual still does a job the prose does not.
   The Check is self-applicable.

## Dr. Okafor (borrowing educator)

Passes; no change.

1. The Do runs from the tool callout, the menu, the verbatim prompt, and the
   three cases; the answer key adds the expected edge for each score and the
   instructor prep.
2. The mechanism is restatable in one sentence plus the figure.
3. Institution-specific parts sit in one callout with a `[VERIFY]` flag and
   a fallback that needs no institution.
4. Staleness: tool names, the Copilot student plan, the FDA revision, and the
   two names for the practice are dated or flagged; the security numbers are
   called old.
5. The Collins Dictionary word-of-the-year claim now has a peer-reviewed
   secondary source: the VIBE-HI paper states it in its abstract
   (PMID 42564266). The `[VERIFY]` span was left unchanged, since it also
   covers the two Karpathy posts, which remain secondary-sourced.
6. xkcd is CC BY-NC 2.5 and the caption says the condition travels.

## Dr. Lindqvist (clinical ethicist) — reads last

Passes; no change.

1. No PHI: the Time note, "Patient information, once more", and the Do's
   warning callout, with the same escalation as before.
2. The patient in the scenario does not know the project exists; the chapter
   says so.
3. Cost bearers are named: the patient waiting unlisted; the ~16,000 people
   whose contacts went untraced.
4. Nothing contested is presented as settled: the Karpathy view is
   attributed, the FDA boundary is stated as turning on a criterion and
   flagged, the security figures are dated.
5. The illustrative app says it is drawn in CSS and not a product.
6. The worked example discloses that it is constructed, not recorded.

## Action list

Fixed in this branch:

- Define MDCalc on first use (Elena 1).
- "Microsoft Copilot" in the fallback (Elena 2).
- `fig-alt` on the mermaid figure (Jordan 1), in source; see the config note.

Open for the author:

- Replace the constructed worked example with a recorded ChatGPT Edu run
  (Marcus 1). The answer key's "Worked-example provenance" section says how.
- Book-wide names for the "The idea" and "The standing question" blocks
  (Jordan 2).
- Existing `[VERIFY]` flags, unchanged from the 2026-09-07 review: Karpathy
  posts and Collins WOTY (Collins now corroborated by PMID 42564266); FDA CDS
  guidance revised January 2026; canvas enabled in the Edu workspace; Copilot
  student plan; (answer key) 2023 ACC/AHA and 2024 ESC sex-category wording.

No stylesheet change is needed. One project-config change is suggested
(`mermaid-format: svg`, above) so mermaid alt text reaches the HTML.
