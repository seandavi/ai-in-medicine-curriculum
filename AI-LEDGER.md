Where AI was used to build this course, what it did, and who checked it. The
course teaches students to disclose and verify AI use; this file is the course
doing the same. It answers the ethicist's last question in
`curriculum/personas.md`, and is rendered as an appendix of the book.

**Rule.** Any commit where an AI tool drafted, rewrote, or verified content that
students or adopters will read adds a row. Tooling that only formats or builds
(Quarto, wrangler, CI) does not. "Human review" says what a person actually did,
not that review happened.

**Standing uses.** Not logged per commit because they run every time:

| What | Tool | Human review |
|---|---|---|
| Drafting and editing of design files, modules, and chapters in this repo | Claude Code (Claude Fable 5.1 and predecessors), pair-programming style: the author directs, the model drafts, the author edits and commits | Every file is read and edited by the author before commit. Citations are verified separately, below. |
| Resolving `@pmid:` / `@doi:` citation keys into `references.resolved.bib` at render time | quartobot (`_quarto.yml` pre-render) | Resolution is a lookup against PubMed and Crossref, not generation. A key that does not resolve fails the render. |
| Chat tutor over the rendered chapters (planned; see `curriculum/chapter-pattern.md`) | Not yet built | Answer keys in `_answers/` are held for the tutor and never rendered. Disclosure to students goes in the preface when it ships. |

**Per-commit log.** Newest first.

| Date | Artifact | What AI did | Human review |
|---|---|---|---|
| 2026-09-07 | `chapters/enrichment-rag-notebooklm.qmd`, `_answers/enrichment-rag-notebooklm.md`, `reviews/enrichment-rag-notebooklm-2026-09-07.md`, `images/retrieval-hallucination-vollmer-2026.svg`, additions to `styles.css` | Drafted the chapter from `modules/enrichment-rag-notebooklm.md` and the archive article; searched PubMed and read the abstracts of 12 papers cited by PMID and one by DOI (Crossref); produced the score-1 specimen by a real run of a source-grounded summarizer (the unnamed model behind Claude Code's WebFetch tool) on the PMC full text of Vollmer et al. 2026 and checked its numbers against the paper's Table 6; confirmed the IBM video's date and length from the YouTube page; confirmed NotebookLM education-account access from Google's help and admin pages; drew the bar chart by hand as SVG from the paper's reported figures; reviewed as all six personas and applied the fixes | Author to read the chapter. NotebookLM itself was not run (no Google sign-in available to the assistant); the answer key says to run the pre-vetted set before the cohort. Tier limits are from third-party guides and flagged VERIFY. Claims resting on a specific number were checked against abstracts, not full texts, except the specimen |
| 2026-09-07 | `images/`, `styles.css`, visual additions to `chapters/core-appraisal.qmd` | Found and licence-checked one CC BY-SA photo (Wikimedia Commons) and two xkcd strips (CC BY-NC 2.5); verified three real headlines about the five-system scribe study via web search and built them as text clippings rather than screenshots; drew an illustrative vendor slide in CSS | Author asked for visual appeal, humour, and lay-press material; author to confirm the NC licence on xkcd is acceptable for a free public course page |
| 2026-09-07 | `reviews/core-appraisal-2026-09-07.md`, GitHub issue #1, revisions to `chapters/core-appraisal.qmd`, `_answers/core-appraisal.md`, `styles.css` | Reviewed the chapter as all six personas; verified FUTURE-AI, TRIPOD-LLM, NAM AICC, Goodman 2023, Chen 2023 in PubMed; ran the Part A prompt itself and checked its five references in PubMed for the specimen panel; drafted the three new sections and all nine action items | Author asked for the review and named the three gaps (concrete examples, information correctness, what makes a good tool); author to read the new sections. The score-1 and score-0 specimens are constructed, and say so in the chapter |
| 2026-09-07 | `curriculum/personas.md`, `AI-LEDGER.md`, `appendix/` (about, personas, ledger), opening-scenario rule in `chapter-pattern.md`, new opening of `chapters/core-appraisal.qmd` | Drafted all of it from the author's brief; proposed the ethicist persona and the four persona revisions; modeled the appendix on the author's RBiocBook about page | Author specified the personas and the scenario requirement, reviewed the draft, asked for and approved the revisions |
| 2026-09-06 | `chapters/core-appraisal.qmd`, `_answers/core-appraisal.md` | Drafted chapter prose, figures, the Do activities, and the answer key from `modules/core-appraisal.md`; looked up every reference with the PubMed tool and inserted resolved keys | Author read the chapter in full. References were checked against PubMed by tool, not by the author reading each paper; claims in prose that rest on a specific number should still be spot-checked against the source |
| 2026-09-06 | `curriculum/chapter-pattern.md`, `curriculum/delivery-modes.md`, `exercises/`, `research/comparable-courses.md` | Drafted from the author's design decisions; reviewed the HMS ExecEd program from its public page | Author directed and edited |
| 2026-09-01 | `CONTEXT.md` | Drafted from author-supplied facts about people, roster, and registration | Author supplied every fact; none were generated |
| 2026-08-05 | `curriculum/`, `modules/`, `research/` (initial framework, modules, and research notes) | Drafted competency framework, module catalog, and research notes with web search; flagged unverified claims `[VERIFY]` inline | Author reviewed structure. `[VERIFY]` flags remain in `research/` until the author checks each claim; they travel into chapters unchanged |
| 2026-08-05 | `research/talks-inventory.md`, recovered Drive deck contents | Read and summarized the author's prior lecture decks | Author's own material; summaries checked against the decks |

**What is not AI.** The competency IDs, the four-week structure, the design
constraints, the guest roster, the choice of personas, and the requirement that
every chapter open with a clinical scenario are the author's decisions. The
model drafted the prose that records them.
