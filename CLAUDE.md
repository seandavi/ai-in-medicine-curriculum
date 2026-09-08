# AI in Medicine curriculum

A Quarto book (`chapters/*.qmd`) for a four-week elective for fourth-year medical
students, plus the design files that generated it (`curriculum/`, `modules/`,
`research/`). Rendered to `_book/` and deployed to Cloudflare on every push to
`main`. Start with `curriculum/chapter-plan.md` and `CONTEXT.md`.

## Standards every chapter is held to

Full versions: `curriculum/chapter-pattern.md` (structure, budget, visuals,
specialty choice) and `curriculum/personas.md` (the six reviewers). In short:

- **Plain language.** Written for a fourth-year student who has never heard the
  term, possibly reading in a second language. Design-doc vocabulary (anchor,
  register, throughline, artifact, proxy, framing, grounded, surface, mode) is
  replaced with plain words or defined in plain words on first use. Sentences
  about 20 words, one idea each. No em-dashes anywhere.
- **Say what you mean.** No metaphor or set phrase where a literal phrase exists:
  "a parameter worth varying", not "a dial worth turning"; "still matters", not
  "earns its keep". A metaphor stays only when it is the chapter's own explained
  teaching device (the keyboard-suggestion analogy, centaur and cyborg) or
  clinical idiom a student uses at work.
- **Scenario first.** A clinical situation before any term of art; it returns at
  the standing question.
- **Blocks and budget.** Objectives callout; why it matters; the idea; watch or
  listen (one real, dated episode with length); do (one student, browser only,
  free tier, no PHI); check; standing question; go deeper. Minutes stated
  honestly.
- **Citations.** Every citation is a `[@pmid:NNNNNNNN]` or `[@doi:...]` key that
  was looked up before it went in. A claim that cannot be verified stays
  `[VERIFY: ...]{.verify}` in prose, never as a citation key. A fabricated
  citation is disqualifying. Verbs no stronger than the evidence.
- **Visuals.** Illustrative artifacts drawn in CSS and labelled illustrative;
  data redrawn from the paper's numbers; open-licence images only, with
  `fig-alt` and the credit in the caption. Nothing decorative.
- **Stand-alone.** Terms defined on first use in every chapter; cross-chapter
  mentions are links.
- **Answer keys** live in `_answers/` and are never rendered.
- **Ledger.** Any change to student-facing content drafted or verified by an AI
  tool adds a row to `AI-LEDGER.md` saying what the tool did and what a person
  checked.

## Reviewing a pull request

Read the diff as the six personas in `curriculum/personas.md`, Elena (the avoider,
ESL, free tier) first and Lindqvist (the ethicist) last. Comment inline on:
jargon, metaphor and set phrases, and long sentences; em-dashes; any citation key the PR adds (say whether
the PMID's metadata supports the sentence, if you can check; flag it if you
cannot); numbers with no source; a Do that needs an install, a payment, or
patient data; an image without `fig-alt` or a licence; a missing ledger row when
content changed; a chapter that no longer stands alone. Say what is good in one
line, then the findings, most serious first. Do not rewrite the chapter; propose
the smallest edit.

## Working in this repo

- Render: `quartobot resolve --from-scan . --id-mode citation-key && quarto render`.
  A key that does not resolve fails the render; that is the citation test.
- One branch per chapter or pass, PR to `main`; merging deploys.
- Do not edit `_answers/` casually; the tutor reads them.
