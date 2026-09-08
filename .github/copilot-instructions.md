# Instructions for Copilot code review

This repository is a Quarto book of prose chapters for fourth-year medical
students, not a codebase. Review pull requests against the standard in
`CLAUDE.md` at the repository root, especially its "Reviewing a pull request"
section, and the two files it names (`curriculum/chapter-pattern.md`,
`curriculum/personas.md`).

In short, comment inline on:

- jargon a student who has never heard the term would not follow; sentences
  much longer than about 20 words; em-dashes (none allowed); metaphor or
  flourish where a literal phrase exists
- any new `[@pmid:...]` or `[@doi:...]` citation key: say whether the cited
  work plausibly supports the sentence, and flag it if you cannot tell
- a number with no source, or a verb stronger than its evidence
- a Do activity that needs an install, a payment, an account with a phone
  number, or patient data
- an image without `fig-alt` or a licence credit in its caption
- student-facing content that changed without a row in `AI-LEDGER.md`
- a chapter that now depends on another chapter to define a term

Open with one line on what is good, then findings, most serious first, each
with the smallest edit that fixes it. Do not rewrite chapters. Do not comment
on `_answers/` (answer keys, never rendered), `reviews/`, `research/`, or
`references.bib`.
