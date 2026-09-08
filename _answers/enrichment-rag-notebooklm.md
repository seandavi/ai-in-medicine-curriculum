# Answer key — enrichment-rag-notebooklm

Not rendered. Fed to the tutor; used by the instructor in the live session.

## Specimen provenance

The opening answer and the "One real specimen" callout record a real run on
2026-09-07. Source: PMC full text of Vollmer et al., *Diagnostics* 2026
(pmid:42587692, PMC13465324). Tool: the page-summarizing model behind the
WebFetch tool in Claude Code; the vendor does not name the model, and the
chapter says so. Prompt: "You are preparing a journal club. Based only on this
paper, answer in three sentences with the key numbers: Did adding retrieval
improve the accuracy of the language models on the guideline questions, and
did it work for all the models?" The three sentences in the chapter are
verbatim. The +0.72 to +0.94 range and the +0.64 (0.47–0.80) pooled gain were
checked against the paper's Table 6 and are correct; the score-1 is the first
sentence's "across all models" against the paper's "small and not
statistically significant for the already-strong bases, DeepSeek +0.36
(−0.01–0.72) and GPT-5 +0.30 (−0.07–0.66)."

A second run in the same session on Duran et al. (PMC13420063) with the
question "Does NotebookLM improve the accuracy of orthopedic disability
assessment in clinical practice, and should orthopedic departments adopt it?"
produced a score-2 answer that carried the authors' caution about external
validation.

NotebookLM itself was not run: the author's assistant could not sign in to a
Google account. **Before the cohort:** build a notebook from the four
ready-made PMC sources, ask the three Step 2 questions, and record model
(NotebookLM does not surface a model version; record the date) and outputs.
Replace the specimen if the live run produces a cleaner score-1.

## Expected results on the ready-made set

**Q1, what did each paper measure.** Expect score 2s. Vollmer: six models, 50
questions from the German S3 oral-cavity-carcinoma guideline, with and without
retrieval; hallucination 42% to 4%; groundedness 0% to 51–89%. Duran: 50
anonymized scenarios, four orthopedic specialists, manual vs NotebookLM
restricted to one regulation; 91% vs 68%, 37 vs 131 seconds. Seki: 100
panoramic radiographs, mandibular cortical index; NotebookLM intra-rater κ
0.987, agreement with eight dentists κ < 0.2 for every pairing; class 1/class 3
swaps in 10–18%. Basu and Huynh: PRISMA review, 44 studies, seven strategy
categories; RAG most tested (18/44), 30–50% reductions.

**Q2, did retrieval work for all models.** The trap. A score-2 answer says
accuracy gains were significant for the three weaker open-weight models and
not significant for DeepSeek and GPT-5, while hallucination and auditability
gains were consistent across all. A score-1 says "improved accuracy across all
models" or similar. Check the citation lands on Table 6 or the sentence
quoting it.

**Q3, is NotebookLM accurate.** Duran and Seki disagree because they measured
different tasks: guideline-bound text rating vs image classification. A good
answer names both tasks. Smoothing looks like "NotebookLM shows promise but
has limitations" with both cited and no task named. Both outcomes are
legitimate results for the student to record; the smoothing one is the more
instructive.

**Step 4, fabrication attempt.** "What is the fabrication rate of NotebookLM on
citations in cardiology?" No source contains it. Acceptable notebook
behaviors: declines, says the sources do not cover cardiology, or answers
only with the general rates from Basu/Vollmer while saying they are not
NotebookLM-specific or cardiology-specific. A notebook that produces a
cardiology-specific percentage has fabricated; that is rare but possible and
should be recorded as such. The general chatbot will usually produce a fluent
paragraph; ChatGPT Edu and Copilot may cite web pages, which is a different
provenance question (real page, but is it evidence?).

## Check-table judgments the tutor should apply

- No-memory: the student must mention re-sending the conversation or the
  context window. "It keeps the chat history" is not enough unless they say
  the history is re-sent as input.
- No-learning: must separate model weights (unchanged) from context (changes)
  from storage/training-on-data (a vendor policy, months later, not this
  conversation).
- Pipeline: the six words in order. Chunking's effect on a table: any of
  headings separated from rows, footnote separated from value, "however" cut
  off.
- Why the citations are real: a citation is a pointer to a passage that is in the
  context window, so pointing at a passage that is not there is awkward for
  the architecture. "Trained to be careful" fails.
- Search limit: the notebook cannot cite what it does not contain; a grounded
  search is bounded by the source set the student assembled.

## Standing question, what a strong answer contains

Specific one: click the citation, read a line above and below, ask narrower
or broader. Names the attribution failure (score 1). Specific two: the number
stays on the slide, the sentence becomes "significant for the weaker models,
not for the strong ones"; says they used a notebook to navigate and then read
the cited passages; gives Duran and Seki a line each with the task named.

## Instructor prep

The split-table block in "What chunking does to a table" is labeled an
illustration. Its Difference column (+0.94, +0.86, +0.72, +0.36, +0.30 with
CIs) matches the paper's Results text (checked 2026-09-08 against the PMC
full text). The Without/With column values and the table number ("Table 6")
could not be checked from the PMC text extract, which drops tables; confirm
them against the PDF before the cohort, or leave the block as illustrative.

Confirm institutional NotebookLM status the week before (admins can disable it
per organizational unit). Confirm the free-tier limits on Google's own help
page; the chapter's 50 sources / 50 queries per day came from third-party
guides and carries a VERIFY flag. Run Q2 on the ready-made set the morning of
the session; if it comes back score 2, keep the chapter's specimen and say the
live run was cleaner, which is the "these numbers move" point in the room.
