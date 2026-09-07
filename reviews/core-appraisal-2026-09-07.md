# Review: core-appraisal chapter, 2026-09-07

Six-persona review of `chapters/core-appraisal.qmd` per `curriculum/personas.md`,
plus the author's own notes on concrete examples, information correctness, and
what constitutes a good tool. Findings are ordered by reviewer; the action list at
the end is ordered by priority. Reviewed by the AI assistant; author to confirm.

## Elena (avoider, surgery, free tier, ESL) — reads first

Passes, with four fixes.

1. **The scenario excludes her.** The chief resident asks "because you are the
   one who does the AI stuff." Elena isn't. Change to: because you are the
   intern, and interns get asked.
2. **Account requirement.** "You need a free ChatGPT or Claude.ai account."
   Claude.ai signup asks for a phone number; she won't. Name which free tool
   works without one and give a fallback. `[VERIFY current signup requirements]`
3. **Undefined terms**, in order of appearance: token, retrieval-grounded,
   register, business associate agreement, pre/post, Hawthorne, RVU. Each needs
   a clause on first use. "Register" in particular carries the chapter's central
   finding and is never defined.
4. **Her best moment is unstated.** The clinician-versus-patient framing finding
   is exactly her question about prompt fluency, and the chapter never says:
   if English is not your first language, your prompts may land in the patient
   register even when you are the clinician. One sentence.

What works for her: the "These numbers move" callout separates the justified
fear from the outdated one. Claim 10 and the Goh trial are moments where
skepticism is the right answer. The fabrication hunt is a ten-minute way in.

## Marcus (early adopter, radiology)

Passes on content, fails on "the thing I can do tomorrow."

1. **No worked example of the 2/1/0 scale.** The scale is defined, and the
   student is sent to score ten references cold. Show one of each: a real
   citation that supports the claim, a real citation the model misrepresented,
   and a fabricated one, side by side, with what gave each away. This is the
   single most valuable addition to the chapter.
2. **"So just use OpenEvidence."** That is the takeaway an enthusiast draws from
   zero fabrications. The chapter says a retrieval tool "can still misread a
   paper it found" and never shows one doing so. The misrepresented example
   above should come from a retrieval-grounded tool.
3. **No checklist for the next tool.** He will be shown a new tool every month.
   The chapter teaches him to grade the evidence about scribes and citations,
   not how to interrogate a tool he has never seen. See "What constitutes a
   good tool" below.
4. **Missed hook.** Most FDA-cleared AI devices are radiology. The FDA section
   never says so. One clause would make him read it twice.

## Priya (clinician-in-waiting, emergency medicine)

Passes on scenario, fails on "what do I document."

1. **Correctness of the answer, not just the citation.** Her question is "can I
   act on this," and Part A only scores whether the references exist. Score 2
   requires that the paper "supports the claim," which is the closest the
   chapter gets. She needs the distinction made explicit: the reference can be
   wrong, the claim can be wrong, and the attribution can be wrong, and these
   fail independently. See "Information correctness" below.
2. **Nothing on documentation or disclosure.** If she uses a tool to draft or
   check something that goes in a note, what does she write, and to whom does
   she say so? The chapter says "you sign the note" and stops. Even a pointer
   to the ethics chapter would do.
3. **Boundary case for the PHI rule.** The warning covers consumer tools. Her
   hospital's Epic-embedded model is a different case, and she will meet it in
   month one. Add the boundary: institution-licensed tools inside the EHR are
   governed by a business associate agreement; ask whether one exists.

Her one sentence for a co-intern exists: "cleared is not validated." Good.

## Jordan (instructional designer)

1. **Time estimate is inconsistent.** Subtitle says about 90 minutes; the Time
   note says 25 + 30 + 45 = 100. Pick one. If the additions below go in, reading
   becomes ~35 minutes and the honest total is closer to two hours.
2. **Objectives 2 and 5 have no activity or Check row.** Objective 2 (explain
   why fabrication follows from generation) is read-only; the Check has no row
   for it. Objective 5 (FDA clearance) has a Check row but no activity. Either
   add a one-line Check item for objective 2 or accept two read-only objectives
   and say so.
3. **Part B cannot currently be completed.** The tier for each claim is "in the
   answer key held by the course tutor," and the tutor does not exist yet. Until
   it ships, the collapsed solution should include the tiers, or the student
   cannot close the loop.
4. **Five `[VERIFY]` flags render as raw text.** The pattern says they travel;
   fine. But to a student they read as an unfinished draft. Style them (a
   small callout or a footnote convention) or resolve them before the cohort
   sees the chapter.
5. **Scenario returns in the standing question but not the summary.** Add one
   summary bullet that names the lunch room.

## Dr. Okafor (borrowing educator)

1. **The mechanism paragraph is one paragraph.** "Plausible continuation, one
   token at a time" is correct and not restatable by someone who has never
   heard it. Add the autocomplete analogy and one sentence on what "token"
   means. The worked 2/1/0 example doubles as their demo.
2. **OpenEvidence verified accounts require professional verification.**
   Medical students generally cannot get one. The optional third row is
   therefore unavailable to most of the intended audience, and an adopter at
   another school will not know that. Say so, or drop the row.
   `[VERIFY: current OpenEvidence eligibility for students]`
3. **Questions the chapter does not answer**, which students will ask: "Which
   tool should I use, then?" "What about Perplexity, Consensus, Elicit?" "Can I
   use this for my note?" The first two are answered by the good-tool section
   below; the third by Priya's documentation point.

Staleness is handled well: the chapter dates its numbers and says they move.

## Dr. Lindqvist (clinical ethicist) — reads last

1. **The patient in the opening scenario is never mentioned.** An ambient
   scribe records the visit. Whether the patient is told, and consents, is the
   ethical question of that product category, and the chapter opens on the
   product without it. The fix fits the existing structure: the standing
   question asks for "one question to ask the vendor." Make consent the
   worked example of what such a question could be.
2. **The equity finding is not named as one.** The tenfold higher fabrication
   rate on patient-framed prompts means the people least able to verify get
   the worst answers. The chapter says "your patient" and leaves it there. One
   sentence naming who bears the cost.
3. **Free-tier inputs may be used for training.** Not PHI, so not a violation,
   but a student running the exercise should know where their prompts go.
   One clause in the PubMed-is-the-verification-tool callout.
4. **No contested claim is presented as settled.** Selection and Hawthorne are
   offered as mechanisms, not conclusions; the Goh trial is reported with its
   confidence intervals; the "optimistic number" is labeled a heuristic. Good.

No activity would fail an IRB sniff test. The PHI guard is the strongest in
any chapter draft to date.

## Author's notes, assessed

### Concrete examples

Agreed, and the gap is specific: the chapter has statistics and no specimens.
Three additions cover it:

- A **worked 2/1/0 panel**: one real, one misrepresented, one fabricated
  citation, with the tell for each. Best built from an actual run of the
  Part A prompts, with the model and date recorded, so the example is itself
  verifiable.
- A **wrong-answer specimen**: a management question where the tool's answer
  is fluent, cited, and clinically wrong. See the next section for sources.
- A **provenance specimen**: what a retrieval-grounded citation looks like on
  screen (inline source, link to the abstract) versus a generated one, so a
  student can recognize the difference before scoring.

### Information correctness, transparency, provenance

Agreed that the chapter conflates three failures. Proposed framing, as a new
subsection after "Where a citation comes from":

**Three things that can be wrong.** The *reference* (does it exist), the
*claim* (is it true), and the *attribution* (does the source say that). They
fail independently. A retrieval tool nearly eliminates the first, reduces the
third, and does nothing for the second.

Two verified sources for the claim-level failure, both suitable for a
specialty-agnostic example:

- Goodman et al., *JAMA Netw Open* 2023 (PMID 37782499). Thirty-three
  physicians across 17 specialties wrote 284 questions and graded the answers.
  Median accuracy 5.5 of 6, but 36 of 284 answers scored 1 to 2, meaning
  mostly or completely wrong, in fluent prose. Accuracy improved on requery
  weeks later and on the newer model version, which is the "numbers move"
  point restated for answers rather than references.
- Chen et al., *JAMA Oncol* 2023 (PMID 37615976). Cancer treatment
  recommendations checked against NCCN guidelines; a substantial fraction of
  outputs contained at least one non-concordant recommendation, and some
  recommendations were not part of any guideline. `[VERIFY exact figures;
  abstract not available via tool; letter format]`

For transparency and provenance, the US regulatory hook is the ONC HTI-1 rule
(2024), which requires certified EHR decision-support tools to expose "source
attributes," including training data, validation, and fairness testing, to the
clinician. That is the closest thing to a legal right to know what a tool is.
Not in PubMed; cite the Federal Register. `[VERIFY current status after the
2025–2026 deregulatory changes]`

### What constitutes a good tool

The best single reference is **FUTURE-AI** (Lekadir et al., *BMJ* 2025,
PMID 39909534, open access): a consensus of 117 experts from 50 countries,
six principles, 30 best practices across the lifecycle. The principles map
directly onto the author's list:

| FUTURE-AI principle | Author's term | The question to ask the vendor at lunch |
|---|---|---|
| Fairness | bias | Was it tested on patients like mine, and did performance differ by group? |
| Universality | (generalizability) | Does it work outside the site that built it? |
| Traceability | transparency, provenance | Can I see what it was trained on, and can I trace an output to its source? |
| Usability | trust | Did the people who will use it help design it, and did they keep using it? |
| Robustness | correctness | What happens when the input is unusual, noisy, or from a different EHR? |
| Explainability | transparency | Can it tell me *why*, in a form I could defend in a chart review? |

That table is the "checklist for the next tool" Marcus wants, the "one
question for the vendor" the standing question asks for, and the bridge to
the bias-equity and ethics-regulation chapters. It also converts the scenario
into an activity: give the student the vendor's slide and have them ask six
questions.

Supporting references, all verified in PubMed:

- NAM AI Code of Conduct. Discussion draft: Adams et al., *NAM Perspectives*
  2024 (PMID 39830818). The 2025 final is a NAM publication, not indexed;
  a JAMIA commentary (PMID 39658328) and a 2026 nursing-perspective
  commentary (PMID 41739499) confirm its release. Use for "principles," not
  for an operational checklist.
- TRIPOD-LLM, Gallifant et al., *Nat Med* 2025 (PMID 39779929). What a
  *study* of an LLM should report. Belongs in Part B as the standard the
  tiered claims fail to meet, and in Go deeper.
- CHAI Applied Model Card. Web only, not indexed. `[VERIFY URL and version]`
  Optional; FUTURE-AI covers the ground.

Recommendation: FUTURE-AI as the anchor citation and the table above as the
didactic device. It is one open-access paper, it has a name a student will
remember, and its six words are the outline the author asked for.

## Action list, by priority

1. Add the worked 2/1/0 panel, built from a real run, model and date recorded.
2. Add "Three things that can be wrong" with the Goodman and Chen examples.
3. Add "What a trustworthy tool looks like" with the FUTURE-AI table, and
   rewrite the standing question so the vendor question draws on it.
4. Put the patient's consent into the scenario's resolution (Lindqvist 1).
5. Fix the scenario line that excludes Elena; define the seven terms; add the
   ESL sentence; name the equity cost.
6. Add the EHR-embedded boundary case and a documentation pointer for Priya.
7. Fix the time estimate; add a Check row for objective 2; put Part B tiers in
   the collapsed solution until the tutor exists.
8. Note OpenEvidence student eligibility; note free-tier training; note
   radiology's share of FDA clearances.
9. Style or resolve the five rendered `[VERIFY]` flags.
