# Answer key: core-ethics-regulation

Not rendered. Fed to the tutor; used by the instructor in the live session.
The Do now starts with a task that works (drafting a note) and ends with a
decision about what to sign. There is no single right note. The tutor rewards
trying twice, reading line by line, and making the anticoagulation decision.

## Part A: draft the note, then decide what you would sign

**What the visit contains.** Use this to check a student's line-by-line read.

- AF: no palpitations ("no racing"); no chest pain or dyspnea.
- Apixaban: **stopped by the patient about two weeks ago** because of
  recurrent nosebleeds, one lasting almost an hour. No blood in urine or stool.
- Anticoagulation plan: **not stated.** The clinician said "we'll come back to
  it" and did not.
- Right knee pain, three weeks, worse on stairs, no fall. Taking
  over-the-counter naproxen.
- Knee plan: stop naproxen, start acetaminophen, physical therapy referral.
- Metoprolol: taking it every morning.
- Follow-up in eight weeks.

**Where drafts go wrong.** Any of these, found and fixed, is a good Part A:

- "Continues apixaban" or "anticoagulation: continue apixaban" (the opening
  scenario's error; the summarizing step writes what is usual).
- "Without bleeding complications", or the nosebleeds left out.
- Naproxen left out of the medication list, or "continue NSAIDs".
- A plan for anticoagulation that was never made ("hold apixaban, ENT
  referral, recheck CBC"). This is reasonable medicine, but it is *true but not
  yours*: the clinician did not say it, so the student cannot sign it as if they
  had. Praise a student who notices this even when the plan sounds right.
- Invented exam findings, vital signs, CHA2DS2-VASc score, or "no trauma"
  turned into "no falls in the past year".
- With the second prompt: "Plan not stated" for AF, and a list of inferences.
  If the tool's own lists missed something the student found, the student has
  learned the main lesson: the lists help you look, and you still read it all.

**The apixaban decision.** A passing answer says the note must record that
the patient stopped apixaban and why, and that the plan was not made. Then it
says what the student will do before signing and by when: for example, discuss
with the attending today and call the patient back, rather than leaving it to
the eight-week visit. A student who writes "continue apixaban" because it is
the guideline-concordant default has signed the opening scenario's note; ask
them who decided that, and when.

**The kept prompt.** Reward specificity: "only what was said", "mark what you
inferred", "write Plan not stated". A student who improves on the second
prompt (for example, asking for a table of each sentence and the transcript
line it came from) has done the best version of Part A.

**The rule.** Any one-sentence rule that would have caught the apixaban error
passes. The best ones name the plan: "read the plan against what the patient
said, not against the draft."

## Part B: explain it to the patient

A passing answer, in two or three plain sentences:

- What the tool does: it records the visit and drafts a note, and the
  clinician reads and corrects it.
- Who answers for the note: the clinician who signs it.
- What the student does not know, said honestly (where the recording is
  stored, for how long, which company), and who would know.
- Optional: that the patient can say no. Whether that is the clinic's policy
  is institution-specific; the student should not promise it without checking.

Falls short: jargon ("ambient AI documentation leveraging an LLM"), "it is
completely secure", or "the AI is very accurate". The consent study
(pmid:40694347) is useful here: consent fell from 81.6% to 55.3% when patients
were told about data storage and the company, so a student who leaves those
out has made the conversation easier, not more honest.

## What this changes for you: model answers for Mr. Alvarez

1. **Box.** The chapter asks "Which box is that?" and does not answer it.
   One reading: B (AI departed from standard; physician followed), by way of
   the signed plan: "continue apixaban" on a false premise. A defensible
   alternative: "not on the grid; the scribe made no recommendation, and the
   liability is ordinary documentation negligence." Either earns credit if the
   recommendation is named.
2. **Hardest element.** Duty is clear. Breach: signing a note that
   contradicts what the patient said; the defense is that review of a drafted
   note at that hour with that load is within the standard, which is exactly
   what is untested. Causation is usually hardest: the stroke followed a
   two-week gap the patient created; the plaintiff must show the erroneous note
   changed what happened next (e.g., no one addressed the nosebleeds or the
   stopped drug at the visit or after).
3. **Deciding facts** (any one, with direction): an auto-inserted attestation
   the intern did not read (toward breach, and toward the vendor/institution);
   a written institutional policy requiring plan-versus-conversation review
   (toward breach if ignored, toward defense if followed); Mr. Alvarez's
   knowledge of the scribe (consent claim, separate from malpractice); the
   time of day and note count (may mitigate breach; untested); whether the intern
   addressed the stopped apixaban verbally even though the note was wrong
   (breaks causation).
4. **The fourteenth note.** Any specific, doable habit passes: read the plan
   against the conversation; look for "continue" on a drug the patient
   discussed; check the attestation line; add an addendum if an error is found
   after signing. "Be more careful" is sent back with: "what, specifically,
   at 6:40 p.m.?"

The reread of the week 1 sentence is not graded. A student who changes it
and can say why has done what the course hopes for.

## Check: the reading rule

Same as Part A's rule: one sentence that would have caught the apixaban error.
The best ones name the plan ("read the plan against what the patient said,
not against the draft"). "Read it carefully" falls short.

## Jabbour (if a student asks; no longer a Check row)

A standard model raised accuracy (73.0% baseline) by 2.9 points, or 4.4 with
explanations. A systematically biased model lowered it by 11.3 points;
explanations recovered 2.3 points, with a confidence interval crossing zero.
So explanations did not reliably protect clinicians from a biased model
(pmid:38112814).

## Optional: the regulatory detail and "has it changed?"

Everything dated here is the state on 2026-09-07. These answers move;
re-check before each cohort and update this file.

| Q | Answer as of 2026-09-07 | Primary source | Notes for the tutor |
|---|---|---|---|
| 1 | FDA CDS guidance issued **29 January 2026**, superseding the **6 January 2026** version, which superseded September 2022. Four criteria unchanged; enforcement discretion for a single clinically appropriate recommendation; time-critical use fails criterion 4; automation bias named. | fda.gov CDS guidance page; PDF cover page | A student who reports "January 6" has read a secondary summary. Both dates are correct in sequence; the point is that the document date on the PDF is the 29th. |
| 2 | **Not finalized.** HTI-5 proposed rule; comment period closed 27 Feb 2026; would remove DSI "model card" source attributes. HTI-1 remains in force. | healthit.gov HTI-5 fact sheet; Federal Register | If a student finds a final rule, the chapter's HTI-1 callout needs updating and the appraisal chapter's with it. |
| 3 | **No guidance.** Discussion paper "Considerations for the Regulation of Generative AI-Enabled Medical Devices," 18 Aug 2026, comments due 19 Oct 2026 (docket FDA-2026-N-7874). Lifecycle-management guidance (Jan 2025 draft) still draft. | fda.gov | A discussion paper is not guidance. |
| 4 | **None found** as of 2026-09-07. Consumer-chatbot suits (Character.AI settlements Jan 2026; *Raine v. OpenAI* 2025; *Winters v. OpenAI* ~July 2026, alleging delayed care before a pulmonary embolism) are product/negligence claims against AI companies, not clinical-AI malpractice verdicts. | Legal press; dockets | If a student finds a verdict, that is the most important thing anyone brings back all course; the chapter's "no verdict" sentence (in "Why this matters" and the Summary) needs updating. |
| 5 | Institution-specific. | Institutional policy | Accept "asked X, who said none exists" as a valid answer with a name and date. |

Questions dropped from the student list in the October 2026 revision, kept
here for the instructor:

- **EU AI Act.** 2 August 2028 for AI embedded in Annex I products (medical
  devices); 2 December 2027 for standalone Annex III systems. Regulation (EU)
  2026/1744 ("Digital Omnibus on AI"), Official Journal L, 24 July 2026
  (Regulation of 8 July 2026, in force 27 July 2026). Two law-firm summaries
  gave different OJ publication dates (24 vs 29 July 2026); three same-day
  reports (lawandtechnology.eu, nicfab.eu, EU Law Live) say 24 July.
  [VERIFY: EUR-Lex blocked the tool on 2026-09-08; open the ELI page once]
- **Sharp and Sutter scribe cases.** Sharp HealthCare (Saucedo; filed ~Dec
  2025, Abridge tool, alleged auto-inserted consent attestation); Sutter
  Health/MemorialCare class action (filed 8 Apr 2026, N.D. Cal.; CIPA, CMIA,
  Wiretap Act). Status after April 2026 unknown to the course. Allegations
  only.
- **LCME/ACGME.** LCME revised Standard 7, Element 7.2 (approved in principle
  Feb 2025, not yet in force) names AI in diagnosis and patient management and
  requires experiential learning. ACGME position unresearched.
- **NAM Code of Conduct.** Discussion draft in *NAM Perspectives* 2024 (PMID
  39830818); a 2025 final exists as a NAM publication (confirmed by JAMIA
  commentary PMID 39658328 and later commentaries) but its URL could not be
  confirmed by the course.
- **Chatbot incidents since Tessa (2023).** None confirmed by the course.
  Candidates: *Winters v. OpenAI* (2026, allegation); Whisper transcription
  hallucinations (AP, Oct 2024, not patient-facing).

**Sepsis alert (if a student asks).** Fails criterion 1 (analyzes monitor
signals) and criterion 4 (time-critical). It is a device. Clearance tells you
the manufacturer satisfied FDA, not that the alert was validated on your
unit's population (Wu 2021; Chouffani El Fassi 2024).

## Instructor prep

- Run both Part A prompts on the Mr. Alvarez conversation in ChatGPT Edu
  before week 4, so you can say what students will see. If the first prompt
  writes "continue apixaban", that is the Monday demonstration.
- Confirm the institution's current attestation and consent language for
  ambient documentation; students will ask in Part B.
- Open the FDA CDS page and the HTI-5 fact sheet the morning of the session.
  If either has moved, say so in the first five minutes.
