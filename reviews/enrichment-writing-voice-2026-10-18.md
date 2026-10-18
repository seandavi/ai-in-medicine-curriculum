# Review: enrichment-writing-voice chapter, 2026-10-18

Six-persona self-review of the new chapter
`chapters/enrichment-writing-voice.qmd`, per `curriculum/personas.md`, Elena
first, Lindqvist last. Reviewed by the AI agent that drafted it; author and
Christina Olson (whose Wednesday talk it goes with) to confirm. Each finding is
followed by the fix applied on branch `chapter/writing-with-ai`, or marked
*open*.

## Elena (avoider, surgery, ESL, free tier), reads first

1. **Way in.** The first AI step is being interviewed by the chatbot, which
   needs no skill and usually works. ChatGPT Edu, no signup. Passes.
2. **Jargon.** "Pre-registered" was undefined. *Fix:* "planned and
   registered before any data were collected". TOEFL, voice, ownership, AI
   detector, and humanizer are defined on first use.
3. **"Can I still use it to fix my English?"** The chapter implied it but did
   not say it. *Fix:* one sentence in "What the rules say": correcting your
   English is editing, which the rules allow; check it did not remove your
   details. The detector and Agarwal paragraphs say plainly that plain and
   non-native writing is what detectors flag unfairly.
4. **Skepticism as the right answer.** The chapter's stance is that the
   chatbot should not write the core. Her caution is treated as correct for
   drafting and outdated for criticism and proofreading. Passes.

## Marcus (early adopter, radiology)

1. **Not obtainable from the model.** The three reader studies with numbers,
   the Traylor word counts, the ownership experiments, the detector
   false-positive and paraphrase numbers. Passes.
2. **His habit shown failing.** The opening draft drops his details and adds
   a view he did not state. Passes.
3. **Honesty about the trade.** Gero et al. found more AI help made essays
   better; the chapter says so instead of hiding it. Passes.

## Priya (emergency medicine)

1. **The rule and the sentence for a co-intern.** The one-sentence callout
   and the five-habit table. Passes.
2. **Accountability and what to document.** The disclosure line in Step 6.
   Passes.

## Jordan (instructional designer)

1. **Objectives to activities.** Five objectives, five Check rows, each with
   a Do step or section. Passes.
2. **Time.** Reading about 12 minutes (about 2,350 words before the Do at
   200 a minute), listening 18 (optional), Do 32 to 37 by the step times,
   Check and last question 5 to 10. Subtitle says 75. Short-on-time path 25
   minutes by the step times. Passes.
3. **Scenario returned to.** The standing question goes back to the free
   clinic entry and the interviewer. Passes.
4. **Accessibility.** The figure is HTML with `role="img"` and an
   `aria-label` giving every value. The video has automatic captions on
   YouTube only; *open*: no human-made transcript was confirmed.

## Dr. Okafor (borrowing educator)

1. **Runnable from the chapter alone.** Every prompt is given in full.
   Passes.
2. **Institution-specific parts.** The AAMC quote is US-only and dated; the
   module file says to swap it. ChatGPT Edu is this school's tool, as in
   every chapter. Passes.
3. **Stale in twelve months.** The AAMC wording; the chapter says rules
   change and to read the current version. Passes.

## Dr. Lindqvist (ethicist), reads last

1. **Patient information.** Personal statements often tell patient stories.
   The Do says to replace any such passage with `[patient story]` before
   pasting. The opening notes contain no patient detail. Passes.
2. **Claims stronger than the evidence.** Three found and fixed:
   - "Readers do notice when every statement sounds the same": no study
     shows this. *Fix:* "Chatbot drafts make statements more alike", which
     Traylor, Padmakumar and Doshi support.
   - "You remember less of it": only the Kosmyna preprint supports this.
     *Fix:* removed from the main text and the heading; the preprint stays in
     Go deeper, labelled.
   - "What readers remember is the part only you could have written":
     unsupported. *Fix:* the callout now gives the chapter's own reason
     (the details and views are yours).
   - "A high detector score is not evidence": too strong given ZeroGPT's 91
     percent in Vaccaro. *Fix:* "not proof".
3. **Who bears the cost.** Writers whose first language is not English,
   named, with Liang and Subillaga. Passes.
4. **The voice check.** A chatbot judging "same author?" is untested. The Do
   labels it a rough check with no study behind it, and the answer key says
   not to credit "the AI said it sounds like me". Passes.
5. **Course disclosure.** The rules section links the AI ledger. Passes.

## Open

- The Do has not been run in ChatGPT Edu with a university login.
- The KevinMD episode summary comes from its web page; the audio was not
  listened to in full.
- Christina Olson to review against her Wednesday talk, so the two do not
  overlap or contradict.
