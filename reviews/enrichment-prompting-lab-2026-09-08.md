# Review: enrichment-prompting-lab chapter, 2026-09-08

Six-persona review of `chapters/enrichment-prompting-lab.qmd` after the
plain-language pass of the same day, per `curriculum/personas.md`, Elena first,
Lindqvist last. Filed as issue #49. Each finding is followed by the fix applied
on branch `pass/enrichment-prompting-lab`, or marked *open* with whose call it
is. Reviewed by the AI assistant; author to confirm.

## What the plain-language pass changed first

Headings: "The idea" became "What a prompt can and cannot do"; "The standing
question" became "The question you keep"; "The scaffold" became "The five-part
prompt" (table id `tbl-scaffold` unchanged). Replaced: artifact, surfaced,
mechanism, thesis, specimen, verbatim, bounded, over-committed, discriminating
feature, vignette, integration, bottleneck, recruits, iterate/decompose/
delimit/few-shot, hedged, deliberately coarse, clinical register, modular
prompt framework, extraction accuracy, compressed cousin, counter-case,
conventional resources. Defined on first use and kept: register, pretest
probability, confidence interval, anchoring, automation bias. About 25
sentences split. No em-dashes were present. Numbers, citation keys, `[VERIFY]`
spans, figure ids, alt text, block classes, callout structure, objectives, and
section order are unchanged.

## Elena (avoider, surgery, ESL, free tier) — reads first

1. **Way in.** Steps 1 to 3 on the institutional account, nothing to sign up
   for, no phone number. Passes.
2. **Fluency.** The register callout tells her which row of the prompt she
   controls and calls it a lever, not a handicap. Passes.
3. **Tool availability.** The chapter named only "your institutional ChatGPT
   Edu or Copilot account", so a reader whose school has neither had no
   instruction. *Fix:* the Time note now marks that line as this school's
   setup and says to use whatever the institution provides.
4. **Vocabulary met cold.** Pretest probability, confidence interval, and
   register are defined on first use after the pass. The clinical shorthand
   in the first chat pane ("44F, ORIF, sats") is left as written: it is the
   bare prompt, and an MS4 reads it.
5. **Skepticism as the right answer.** Twice: Sam's better answer is wrong, and
   the record's third outcome (bare catches the trap, structured misses) is
   named "the best result of all". Kept.

Passes.

## Marcus (early adopter, radiology)

1. **Not obtainable from the model.** The three "structure did not buy
   accuracy" studies with numbers and both Goh trials with intervals. Passes.
2. **Concrete failure of his habit.** The opening chat pair: structured
   prompt, table, into the note, wrong next step. Passes.
3. **Model-alone result overstated.** The chapter presented "the model on its
   own scored 16 points higher" as if it were a trial arm. The abstract calls
   it a secondary exploratory analysis. *Fix:* the chapter now says so in the
   sentence that reports it. He would have found this in the paper and
   discounted the chapter for it.
4. **Tomorrow.** The optional rerun without the uncertainty line. Kept.

## Priya (clinician-in-waiting, emergency medicine)

1. **Ward rule without mechanism.** "The one sentence" callout, Step 5's three
   named sources, Check row 4. Passes.
2. **Bare prompt gets questions back.** Current tools often answer the bare
   prompt with clarifying questions rather than a plan, and the chapter did
   not say what to do. *Fix:* Step 2 now says do not answer them; the
   questions are the reply, copy and score them. The answer key has a
   matching scoring note (questions on Case A count as the trap caught, and as
   organisation point 5 on any case).
3. **Documentation.** Still pointed to the ethics chapter rather than taught
   here. Unchanged; consistent with the 2026-09-07 decision.

Her one sentence for a co-intern is unchanged: a structured prompt improves how
an answer is organised, not whether it is right.

## Jordan (instructional designer)

1. **Objectives to activities.** Each of the five maps to a Do step or Check
   row; the key has the table. Passes.
2. **Time.** 20 + 20 + 30 + 5 with the podcast stop point stated; Do steps sum
   to 30 plus the bonus 5. Honest.
3. **Mermaid figure had no alt text.** Quarto renders mermaid client-side and
   drops `fig-alt` on diagram cells (tested: the attribute never reaches the
   HTML; the figure is described only through `aria-describedby` on the
   caption). *Fix:* the diagram now carries mermaid `accTitle` and `accDescr`
   directives, which land in the rendered SVG as `<title>` and `<desc>`. No
   stylesheet change needed. Other chapters with mermaid figures could use the
   same pattern; noted for the coordinator.
4. **Heading names.** The plain-language pass renamed "The idea" and "The
   standing question". *Open, coordinator's call:* sibling chapters may keep
   the pattern's names; harmonise across the book one way or the other.
5. **Scenario returns.** In "The question you keep" and the last summary
   bullet. Passes.

## Dr. Okafor (borrowing educator)

1. **Run the Do alone.** Prompts verbatim, traps in the chapter, two scoring
   tables, instructor prep in the key. Passes.
2. **Institution-specific parts marked.** Now yes (Elena 3).
3. **Stale in a year.** The chapter says outputs change month to month; the
   key says rerun the cases the morning of. Passes.
4. **Causes stated as fact.** The reasons the physicians-plus-model group did
   not beat the physicians ("anchoring, skimming, confirming") were given as
   what happened. *Fix:* now given as the likely candidates the trial could
   not test.
5. **Images.** Redrawn figure is the course's own; chat pair and diagram are
   code. Nothing stops at this course.

## Dr. Lindqvist (clinical ethicist) — reads last

1. **PHI.** Four fictional cases, substitution forbidden, Sam's phone named
   as the forbidden act, institutional accounts do not change the rule.
   Passes.
2. **Contested reading presented as settled.** "Two trials, one direction: the
   bottleneck is integration, not capability" was stated flat. *Fix:* now "the
   reading the authors favour, and the one this chapter takes", plus one
   sentence that both trials used written cases, not real patients, as the
   authors themselves say.
3. **Uncitable trial in prose.** The *NEJM AI* automation-bias trial is
   mentioned with a `[VERIFY]` flag and still cannot be found in PubMed
   (searched again today: journal-restricted and free-text queries, 2025 on,
   zero hits). *Open, author's call:* locate and cite it, or cut the
   sentence. A trial nobody can find should not outlive this pass.
4. **Patient awareness in the scenario.** Carried over from 2026-09-07, still
   *open, author's call:* one sentence in the opening scenario on whether
   Sam's patient knows her case went into a phone. The PHI callout covers it;
   the scenario itself does not.
5. **Illustrative artifact.** The chat panes now say "Made-up answer, written
   for this chapter. Not a transcript of any real tool." No product name or
   logo. Passes.

No activity would fail an IRB sniff test.

## Verification status

- Re-read today: pmid:39466245 and pmid:39910272 (both Goh trials); numbers in
  the chapter match the abstracts. The 2024 model-alone comparison is a
  secondary exploratory analysis; the 2025 trial reports no significant
  difference between physicians-with-model and model alone (-0.9, 95% CI -9.0
  to 7.2) and 119 s longer per case.
- `[VERIFY]` flags unchanged: the NEJM AI automation-bias trial (open item 3
  above); the Rodman episode duration; the simvastatin label claims. One in
  the answer key on the IDSA delirium wording.
- Rendered clean; no unresolved citations in the output.

## Action list, by priority

1. Mark the model-alone result as a secondary exploratory analysis. **Done.**
2. Hedge the causal reading of the two trials and the list of reasons.
   **Done.**
3. Mark the institutional-tool line as swappable. **Done.**
4. Tell the student what to do when the bare prompt gets questions back;
   matching key note. **Done.**
5. Accessible title and description on the mermaid figure. **Done.**
6. *Open, author:* NEJM AI trial, find or cut.
7. *Open, author:* scenario sentence on patient awareness.
8. *Open, coordinator:* heading names across chapters; `accDescr` pattern for
   other chapters' mermaid figures.
