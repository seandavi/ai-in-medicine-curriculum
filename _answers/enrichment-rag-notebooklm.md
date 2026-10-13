# Answer key: enrichment-rag-notebooklm

Not rendered. For the instructor and the planned tutor.

## The tool's name

Google renamed NotebookLM to Gemini Notebook on 16 July 2026 (Google blog,
read 2026-10-12). notebooklm.google and notebooklm.google.com redirect to
notebook.google (checked with curl 2026-10-12). The papers in the ready-made
set use the old name. Limits as of 2026-10-12: the plans page
(support.google.com/notebooklm/answer/16213268) lists 50 sources per notebook
and 100 notebooks per user on the free (Standard) plan, and does not list a
chat limit; Google's blog (28 August 2026) says compute-based limits that
refresh every five hours roll out to consumer accounts from 2 September 2026.
Workspace for Education accounts are not covered by that post.

## Specimen provenance

The opening answer and the "Where the opening answer came from" callout
record a real run on 2026-09-07. Source: PMC full text of Vollmer et al.,
*Diagnostics* 2026 (pmid:42587692, PMC13465324). Tool: the page-summarizing
model behind the WebFetch tool in Claude Code (a Claude model; the version is
not shown). It was not NotebookLM or Gemini Notebook, and the chapter now
says so in the specimen's source line and in the callout. Prompt: "You are
preparing a journal club. Based only on this paper, answer in three sentences
with the key numbers: Did adding retrieval improve the accuracy of the
language models on the guideline questions, and did it work for all the
models?" The three sentences in the chapter are verbatim.

Checked 2026-10-12 against the PMC page HTML: Table 6 is "Within-model effect
of guideline retrieval (automated judge)", with columns Model, Base, +RAG,
Δ Accuracy (95% CI), Groundedness, Hallucination. Rows: DeepSeek-V3.2 4.08 to
4.44, +0.36 (−0.01 to 0.72); Mistral Small 3.2 3.40 to 4.34, +0.94 (0.58 to
1.30); Qwen3-Next-80B 3.52 to 4.38, +0.86 (0.50 to 1.22); GPT-OSS-120B 3.62
to 4.34, +0.72 (0.36 to 1.08); GPT-5-chat 4.18 to 4.48, +0.30 (−0.07 to
0.66); pooled +0.64 (0.47 to 0.80), hallucination 42% to 4%. The chunked
illustration uses these values; its row order and the cut are made up, as
the chapter says.

Why it is a score 1 and not a 0: the abstract says retrieval "improved
accuracy, significantly in the three weaker open-weight models ... and
directionally in the already-strong DeepSeek and GPT-5 bases." "Improved
accuracy across all models" drops the qualifier; it is broader than the
paper, not contrary to it. The chapter used to say the sentence "is not what
the paper says"; that overstated it and was changed.

Model counts: the paper first compared six systems (Custom GPT with the
guideline, ConsensusGPT, DeepSeek, Mistral, Qwen3, GPT-OSS). The paired
with/without-retrieval test used five base models (those four plus
GPT-5-chat, added for that test), 13 arms by 50 questions. The figure's SVG
footnote still says "Six models"; the caption explains the difference.

A second run in the same session on Duran et al. (PMC13420063) with the
question "Does NotebookLM improve the accuracy of orthopedic disability
assessment in clinical practice, and should orthopedic departments adopt it?"
produced a score-2 answer that carried the authors' caution about external
validation.

Gemini Notebook itself has not been run on this Do. See "Author to do".

## Expected results on the ready-made set

**Step 2, the brief.** Expect most sentences to score 2. What each paper
says, for checking: Vollmer: 50 questions from the German S3 oral cavity
cancer guideline; six systems compared, then five base models each with and
without retrieval; hallucination 42% to 4%; citation groundedness 0% to
51 to 89%. Duran: 50 anonymized scenarios, four orthopedic specialists,
manual vs NotebookLM restricted to one regulation; 91% vs 68%, 37 vs 131
seconds. Seki: 100 panoramic radiographs, mandibular cortical index;
NotebookLM intra-rater κ 0.987, agreement with eight dentists κ < 0.2 for
every pairing; class 1 and class 3 swapped in 10 to 18%. Basu and Huynh:
PRISMA review, 44 studies, seven strategy categories; RAG most tested
(18/44), 30 to 50% reductions.

The sentence most likely to score 1 is the brief's line on Vollmer's
result: "improved accuracy across all models" or similar. A score-2 version
says the gain was significant for the three weaker models and not for
DeepSeek and GPT-5, while the hallucination and citation gains held for all
five. Check that the citation lands on Table 6 or the sentence quoting it.
Other likely 1s: Seki's κ described as "inaccurate" (the paper measured
agreement, not accuracy against a reference standard); Duran's result stated
without "under controlled conditions" or the need for external validation.

A student whose three sentences all scored 2 has done the step. The good
answer says how they know (which passage, which line).

**Step 3, is NotebookLM accurate.** Duran and Seki disagree because they
measured different tasks: guideline-bound text rating vs image
classification. A good answer names both tasks. Smoothing looks like
"NotebookLM shows promise but has limitations" with both cited and no task
named. Both outcomes are legitimate results to record; the smoothing one is
the more instructive.

**Step 4, a question the sources cannot answer.** "What is the fabrication
rate of NotebookLM on citations in cardiology?" No source contains it.
Acceptable notebook behaviors: declines, says the sources do not cover
cardiology, or answers only with the general rates from Basu or Vollmer while
saying they are not NotebookLM-specific or cardiology-specific. A notebook
that produces a cardiology-specific percentage has made it up; that is rare
but possible and should be recorded as such. ChatGPT Edu searches the web and
will often answer with links; that is a different question about where the
answer came from (a real page, but is it evidence?).

## Check-table judgments

- No-memory: the student must mention re-sending the conversation or the
  context window. "It keeps the chat history" is not enough unless they say
  the history is re-sent as input. A memory setting (saved notes pasted into
  later chats) is still context, not learning.
- No-learning: must separate model weights (unchanged) from context
  (changes) from storage and training on data (a vendor policy, months
  later, not this conversation).
- Pipeline: the six words in order, each with a sentence. The chunked-table
  material is optional ("If you have more time") and not required.
- Why the citations are real: a citation is a pointer to a passage that is
  in the context window, so pointing at a passage that is not there is
  awkward for the design. "Trained to be careful" fails.
- The brief: three citations clicked, each sentence beside its passage, one
  corrected or a reason all three stand. Scores given without clicking fail.
- Search limit: the notebook cannot cite what it does not contain; a
  grounded search is bounded by the source set the student assembled.

## Standing question, what a strong answer contains

Specific one: click the citation, read a line above and below, ask narrower
or broader. Names the misreading failure (score 1). Specific two: the number
stays on the slide, the sentence becomes "significant for the weaker models,
not for the strong ones"; says they used the notebook to find their way and
then read the cited passages; gives Duran and Seki a line each with the task
named.

## Verified 2026-10-12

PubMed metadata and abstracts: 42587692 (Vollmer; plus PMC full text and
page HTML for Table 6 and the model counts), 42534267 (Duran), 42645138
(Seki), 42251377 (Basu and Huynh), 42232526 (McLaughlin: OpenEvidence perfect
accuracy; Gemini 26.2% fabricated, the highest), 41266194 (Hooshiar: the
"avoided fabricated references but still generated incorrect
interpretations" quote), 40309181 (Peters and Chin-Yee: 10 models, 4,900
summaries, OR 4.85), 42611847 (Nishisako: "consistently declined to answer"
quote), 42684317 (Liu: effect on fabrication "was not tested").
doi:10.1162/tacl_a_00638 (Liu et al. 2024, TACL, "Lost in the Middle"):
Crossref abstract. Keys removed from the chapter: 40662770 and 42546813
(chunk sizes).

## Author to do

- Run the Do once in Gemini Notebook with the four PMC sources, ideally with
  a CU Google account if CU has one, or a personal one. Record the date, the
  brief, and the scores for the three checked sentences. Then remove or
  update the chapter's VERIFY flag on CU account access, and replace the
  opening specimen with a Gemini Notebook answer if the run gives a clear
  score 1.
- Run the Step 4 question in ChatGPT Edu and note whether it answered with
  links.
