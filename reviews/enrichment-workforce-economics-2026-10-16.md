# Review: enrichment-workforce-economics, labor-market additions, 2026-10-16

Six-persona review of PR #111 per `curriculum/personas.md`, Elena first,
Lindqvist last. It covers the new section "Could versus does", the
emergency medicine paragraph under question 1, Part C step 2, objective 7,
and the Go deeper additions. A fresh subagent did the review. It had not
written the material, and it read the diff, the sources, and the rendered
page, including the lookup table at 390 px. The agent that wrote the
material applied the fixes. Author to confirm.

**Good.** This is the book's clearest lesson in "which measure, made by
whom?". Nearly every number checked out against the Anthropic paper and
appendix, the released CSV (same SHA-256 as Hugging Face), PubMed, Crossref,
the Microsoft and OpenAI data files, and the Stanford PDFs.

## Elena (avoider, surgery, free tier, ESL), reads first

**Findings.** The question 1 paragraph used O\*NET before the definition,
which came later in the new section. "Language model" was never defined.
The In short box said "how exposed" before the chapter defines exposure.
Typing "surgeon" in the lookup gives orthopedic and pediatric surgeons at
0%, with no warning that general surgery has no row. On a phone, the figure
labels render at about 6 px.

**Fixes applied.** O\*NET is defined at its first use, in the question 1
paragraph. "Language model" is defined in the first bullet of the new
section. The In short says "how much of each health job people were seen
doing with one AI company's chatbot". Part C step 2 now names the
specialties with no row (emergency medicine, general surgery, cardiology)
and says to use the nearest job and name it. **Not fixed:** label size on
phones. The lightbox enlarges both figures, and a radar chart with 22
labels cannot be read at 336 px at any type size.

Her moment of justified skepticism: the "trial run by the company that
sells the drug" list. Kept.

## Marcus (early adopter, radiology)

**Findings.** The existing line "Coding and health-information work fail
the first test" contradicted the new data, in which medical records
specialists are the 4th most exposed of 756 jobs. The answer key graded the
old line. He would also want the 2026 Stanford number.

**Fixes applied.** The line now reads "pass the first test only in part.
Much of the job is judgment…", and the answer key matches. The Stanford
update is added: 19% through June 2026, attenuated by education, weaker in
national survey data. The paragraph also notes that Stanford ranks jobs by
the "could" ratings, not observed use.

## Priya (emergency medicine)

**Findings.** The emergency medicine paper was attributed to "two emergency
physicians". It has six authors, including a statistician and an
informatician. The two physicians did the classifying. The lookup sends
her to Emergency Medical Technicians.

**Fixes applied.** The paragraph now says "A team led by Stanford emergency
physicians" combined the sources and "two emergency physicians on the team"
judged each category. "Expert judgment" replaces "two physicians'
judgment". The missing-row note in Part C covers her specialty. Her
sentence for a co-intern: "Exposure counts the tasks a tool touches. It
does not tell you whether the job will shrink."

## Jordan (instructional designer)

**Findings.** The prose before the Do grew by about half, and "about 60
minutes" was no longer honest. Objective 7 maps to Part C step 2 and a
Check row. The alt text is accurate and neither figure is decoration. Part
C's 11 minutes is tight but plausible.

**Fixes applied.** The young-workers material moved into the chapter's one
collapsed "If you have more time" callout. Required reading is now about
22 minutes (3,103 prose words, against 2,117 before). The subtitle says
about 70 minutes, as does the row in `appendix/instructors.qmd`. Four
other chapters already state 70 to 85.

## Dr. Okafor (borrowing educator)

**Findings.** The Do runs from the chapter alone. There was no fallback if
the table fails to load, and nothing said the scores will change. Both
figures are the course's own drawings, CC BY 4.0, and can be reused.

**Fixes applied.** After the table, the chapter links the CSV and says
the table shows the March 2026 release, which Anthropic says it will
update.

## Dr. Lindqvist (clinical ethicist), reads last

**Findings.** The conflict of interest is named, and the section is
balanced against Stanford, University of Washington, Microsoft and Ohio
State. Places where the text was more certain than its source:

- the refill task described as one "a language model alone could do", when
  the rating means "make at least twice as fast";
- "so anyone can check the numbers", when the conversations are not public;
- "The four questions do that";
- the University of Washington conclusion quoted without its warning that
  this could change;
- "Three of its four authors worked at OpenAI", which is true of the 2023
  version only; the *Science* version lists Manning at GovAI.

The book's own disclosure read as an afterthought, and the list did not
say which way the company's interest could cut. "OpenEvidence" was
undefined, and the item was inaccurate: tools built on Claude do count.

**Fixes applied.** Each overclaim was narrowed to its source, and the
University of Washington warning was added. The disclosure is now item 5 of
the list, and item 1 says that both of the paper's main findings are ones
the company would welcome. Item 2 now reads "ChatGPT, or a scribe built on
another company's model". No activity involves patients or classmates.

## Also changed

- The health-jobs caption now says "records and office jobs".
- The radar labels healthcare support "seen near 0%", the zone where its
  markers overlap.
- Step 3 is split into two sentences.
- "Routine paper tasks" now reads "routine record and office tasks".

## Open

- The ledger row's human-review cell needs the author's entry before merge.
- The Alain et al. (pmid:40446149) average-adoption inconsistency is still
  the research agent's reading. The chapter does not quote that figure.
