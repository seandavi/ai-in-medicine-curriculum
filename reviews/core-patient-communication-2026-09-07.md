# Review: core-patient-communication chapter, 2026-09-07

Six-persona self-review of `chapters/core-patient-communication.qmd` per
`curriculum/personas.md`, written by the drafting agent before the first commit.
Findings are ordered by reviewer; each finding says whether it was fixed in the
same pass or left open. Author to confirm.

## Elena (avoider, surgery, free tier, ESL) — reads first

Passes, with five fixes applied.

1. **Undefined terms on first use.** "Computer-aided detection" appeared bare in
   Part A; "portal message" and "tethered cord" appeared bare in The idea and
   Watch or listen. *Fixed*: a clause on each.
2. **Her ESL point was missing.** The patient-framed-prompt finding is her
   question about fluency, and the draft left it to the appraisal chapter.
   *Fixed*: one sentence in the printout section pointing at her own prompts.
3. **Part B depends on how she phrases the prompt.** A chatbot playing a patient
   is more agreeable than a patient and may cave. *Fixed*: the chapter says so
   and gives the "be harder to persuade" fallback.
4. **Ten-minute way in exists.** Part A needs no tool and no account. Good.
5. **Skepticism as the right answer** appears three times: the empathy trap,
   the Thomae caveats, and the warning that the chatbot's observer score is
   itself a language model's opinion. Good.

What works for her: the scenario needs no vocabulary; both images land cold;
no comic, so no in-joke risk.

## Marcus (early adopter, radiology)

Passes.

1. **A failure in a tool he trusts.** The printout, the 2.1 → 20.0 percent
   finding, and the Winters complaint. Good.
2. **Radiology hook.** The mammogram CAD script and the "AI-assisted image
   read" row of the decline table put him in the room. Good.
3. **Thing to do tomorrow.** The three-sentence spine and the "say what is
   right first" order. Good.
4. **Vibes check.** The chapter cites for every number and dates every
   percentage. The one unsourced structural claim ("almost nobody arrives with
   a printout because they trust a chatbot more") is presented as the
   scenario's design, not as a finding. Acceptable; left open as a judgment.

## Priya (clinician-in-waiting, emergency medicine)

Passes, with one fix applied.

1. **What to document.** The draft said whose note it is and stopped. *Fixed*:
   the scribe callout now says to document a declined scribe in the note and
   log consent where the institution does.
2. **Scenario she recognizes.** The attending who sent an AI draft unread is
   named in the portal section and given its consequence. Good.
3. **Who is accountable.** Every table row and the spine's third sentence. Good.
4. **Her one sentence for a co-intern**: "What it did, what a person did, who is
   responsible, in that order." Present.

## Jordan (instructional designer)

Passes, with one note left open.

1. **Objectives map.** 1, 2, 3 → Part A and Check rows; 4 → Part B and Check
   row; 6 → Part C and Check row; 5 → Check row only (read-only objective,
   assessed by explanation). Acceptable for a communication chapter; the
   Check row names the two studies' limits so it is not a recall item.
2. **Time.** 25 + 20 + 35 + 10 = 90, and the subtitle says ninety. The podcast
   is 40 minutes; the chapter says the first twenty carry the story, which is
   honest. A median student reading ~430 lines of prose at this density will
   take 20–25 minutes.
3. **Scenario returns** in the standing question and in the summary's
   sixth and seventh bullets. Good.
4. **Accessibility.** Both images have `fig-alt`; the SVG has a `<title>`;
   the podcast page carries a transcript link on the NEJM site
   [VERIFY: transcript availability]. No paywall on any linked source.
5. **Check is self-applicable.** Yes; it is the observer rubric turned on the
   student's own artifacts.
6. **Open:** Part B produces a transcript the student must read back through
   to fill in the record block; that is the cognitive-load peak of the
   chapter. Left as is; the record block is short.

## Dr. Okafor (borrowing educator)

Passes, with one fix applied.

1. **Mechanism restatable.** The draft deferred "why the printout is
   unreliable" entirely to the appraisal chapter. *Fixed*: one paragraph in
   the printout section gives the plausible-next-words mechanism in a form an
   adopter can restate.
2. **Could they run the Do alone?** Part B's prompt is complete and pasteable;
   Part A needs nothing; the answer key has model answers and failure
   patterns. Yes.
3. **Institution-specific parts.** Tool names (ChatGPT Edu, Copilot), state
   law, and the local scribe policy. The first two are named and the law is
   flagged VERIFY with "check your own state"; the scribe table's middle
   column says "common case, not a rule." Marked.
4. **Stale in twelve months.** Percentages are dated; the laws are flagged;
   the Winters case is described as undecided. Marked.
5. **Image reuse.** One public-domain photo and one course-drawn SVG. Nothing
   NC, nothing fair-use. An adopter can reuse everything.

## Dr. Lindqvist (clinical ethicist) — reads last

Passes, with one fix applied.

1. **Does the patient know an AI is in the room?** It is the scenario's first
   line. Good.
2. **PHI.** The warning covers the chatbot persona, the transcript, and the
   student's own notes ("every detail you or the chatbot invent stays
   invented"). Part B's persona is fictional and specified in the prompt.
   Nothing nudges toward a real patient.
3. **Contested presented as settled.** The draft's portal section said the
   patient's expectation and the statute "are converging," which could read as
   the disclosure question being closed. *Fixed*: a paragraph before the
   decline table says which AI involvement requires disclosure is not settled,
   and names the narrower thing that is.
4. **Who bears the cost.** Named in the incidents section (a person with an
   eating disorder, a man with a clot, a patient who asked in her own words)
   and in the scribe section (patients in non-English visits).
5. **The Winters complaint.** The chapter names no person, says "allegations,
   not findings," and says the case has not been decided. The linked clipping
   names the plaintiff, who filed a public lawsuit and spoke to the press. No
   veto.
6. **Illustrative artifacts.** Both styled blocks are labeled illustrative and
   written for this chapter; the portal message uses invented names; no
   company is named. No confusion with real material.
7. **Course's own AI use.** Ledger row added; the chapter's Part B tells the
   student the observer score is a model's opinion, which is the course
   practicing its own disclosure.

## Action list

All fixes above were applied before commit. Open items:

- Confirm the 21% figure against the table in Tolentino et al. 2024
  (pmid:39023999); it is carried from `research/competency-frameworks.md`.
- Run the Part B prompt against ChatGPT Edu and Copilot before the first cohort
  and adjust the persona if it caves.
- Resolve the three `[VERIFY]` flags: state-law text and scope; Tradeoffs
  episode length; public URL for the *ai-safety* deck.
