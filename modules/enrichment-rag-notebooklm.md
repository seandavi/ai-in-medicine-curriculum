# Enrichment module — Grounding AI in real sources

**Format:** one 60-minute Zoom session · **Prereq:** none
**Competencies:** AIM-1 (foundations of AI and data), AIM-9 (research, innovation, and scholarship)

## The idea this module makes concrete

Students already know that chatbots make up citations. What almost none of them
know is *why*, or why some AI tools do it far less than others. The difference
between a general-purpose chatbot and a retrieval-grounded tool like NotebookLM
or OpenEvidence is not that one is more careful or better trained. It is
structural: one generates an answer from everything it absorbed during training,
where a citation is just more plausible text; the other assembles an answer out
of passages it actually retrieved from a specific set of documents, where a
citation is a pointer back into that set.

Once a student sees that difference by clicking a citation and landing on the
sentence it came from, the whole category of "which AI tool should I trust for
this question" reorganizes itself. That is the payoff, and it is worth an hour
even in a four-week course, because it generalizes to tools that do not exist
yet.

This session is built on an existing IDPT 8079 asset that is already written as
an article rather than a slide deck, which makes the prep unusually cheap — see
*Reusable material* below.

## Learning objectives

By the end, a student can:

1. Explain what the context window is and why an LLM's apparent memory of a
   conversation is just text being re-sent every turn.
2. State plainly that an LLM does not learn from its users — that nothing a
   student types changes the model — and explain what does change between turns.
3. Describe the RAG pipeline in order: chunking, embedding, indexing, retrieval,
   augmentation, generation.
4. Explain why retrieval-grounded tools fabricate citations at dramatically lower
   rates than general-purpose chatbots, and identify this as a structural
   property rather than a quality difference.
5. Name the failure mode grounding does *not* fix: a real, correctly-linked
   source that has been misread or over-generalized in the summary.
6. Build a working grounded notebook from sources they chose, and state when
   this is and is not an appropriate way to do a literature search.

## Tool choice

**Use NotebookLM.** Free with any Google account, entirely browser-based, no
install, and it enforces exactly the property the session is about: it answers
only from the sources you gave it, with inline citations that link back to the
passage. The free tier allows up to 100 notebooks, 50 sources per notebook, and
50 queries per day — comfortably more than a 60-minute session needs, though the
query cap is worth mentioning so nobody burns it in the first ten minutes.

Students also need a **general-purpose chatbot open in a second tab** — whichever
free one they already have — because half the exercise is asking the same
question in both places and watching what differs. Claude.ai's free tier works;
so does anything else. This is deliberately not a comparison of vendors.

**Do before class, not during it:** confirm you can sign in to NotebookLM with a
Google account and open the shared notebook. Institutional Google accounts
sometimes have NotebookLM disabled by administrative policy, and a student who
discovers that at minute three is stranded for the whole session. Anyone blocked
should use a personal Google account.

**Assigned pre-reading:** the RAG handout (see *Reusable material*). It is
already written as an article, so it carries the context-window and pipeline
material without help. Assigning it lets the didactic block shrink to eight
minutes and gives the session back to the hands-on work, which is where the
learning is.

## Session plan (60 min)

| Time | Mode | What happens |
|---|---|---|
| 0–8 | Frame | The context window from first principles: the model has no memory, the conversation is re-sent every turn, nothing you type teaches it anything. Poll: *has a chatbot ever given you a citation that did not exist?* Nearly every hand goes up, and that is the session's premise established for free. |
| 8–18 | Didactic + demo | The pipeline — chunking, embedding, indexing, retrieval, augmentation, generation — narrated over a live query in the shared notebook, clicking through to the source passage each time. |
| 18–35 | Breakout, Part A | The shared notebook: ask questions, audit the citations, then try to make it answer something its sources cannot support. |
| 35–48 | Solo or pairs, Part B | Build your own notebook from three to five sources you chose, and run the same-question-in-both-tabs comparison. |
| 48–56 | Report-back | What did the grounded tool refuse to do? Who got a citation that pointed at a real passage that did not actually say what the summary claimed? |
| 56–60 | Close | The standing question, and the honest limit: grounding fixes provenance, not comprehension. |

**Deliverable:** one shareable notebook per student, plus one posted example of a
question the grounded tool declined to answer or answered thinly — which is the
artifact that proves they understood the mechanism.

## Part A — the shared notebook (17 min, breakouts of 4–5)

The existing IDPT 8079 exercise supplies the notebook: a collection of physician
and patient perspectives on AI in healthcare. It is well suited to this because
the sources genuinely disagree with each other, which means the interesting
questions do not have one retrievable answer.

Three tasks, in order, and the third is the one that matters:

**Ask three questions and click every citation.** Not a sample — every one. For
each, decide whether the linked passage actually supports the sentence it was
attached to. Students almost always find at least one case where the link is real
and the claim built on it is stretched. That discovery is the whole point of the
task and it should not be given away in advance.

**Ask a question the sources genuinely disagree about.** Something like what
patients fear about AI in their care versus what physicians think patients fear.
Watch what the tool does with disagreement: whether it presents both positions or
smooths them into a consensus that no source actually holds. Smoothing is the
more common behavior and it is a real limitation, not a bug in the exercise.

**Try to make it fabricate.** Ask something the source set cannot support — a
specific statistic that is not in there, a named study, a claim about a
population none of the sources discuss. A grounded tool should decline, hedge, or
answer thinly. Then ask the identical question in the general chatbot tab. The
contrast between "I cannot find that in your sources" and a fluent, confident,
unsupported paragraph is the single most durable thing in this session, and
students should produce it themselves rather than watch the instructor produce
it.

Each room reports one line: the question they could not get NotebookLM to answer,
and what the chatbot said instead.

## Part B — build your own (13 min)

Each student makes a notebook from three to five sources they choose and care
about — papers from a rotation, a specialty society guideline, whatever they were
already going to read. Then two things:

Ask a question they already know the answer to, so they can judge the answer
rather than just accept it. Students consistently over-trust output on topics
they cannot check, and the fix is to make them check one they can.

Ask the same question in the general chatbot tab and compare. Not to declare a
winner — the chatbot will often give a better-written, broader, more useful
answer, and pretending otherwise makes the session propaganda. Compare on one
axis only: can you verify where each sentence came from?

Thirteen minutes is enough to load a few PDFs and ask three questions. It is not
enough to build something anyone would keep, and it should not pretend to be.
The point is that they have now done it once and can do it again on their own
time with a rotation's reading list.

## What to teach about the mechanism

Keep the explanation concrete and resist the urge to go deeper than this.

The reason a general-purpose chatbot invents citations is that generating a
citation is the same operation as generating any other text: producing plausible
next words. A citation that looks right — real journal, plausible authors, a
volume and page that fit the pattern — is a successful output by the only
criterion the mechanism has. Nothing in the process ever checks whether the paper
exists, because nothing in the process is capable of checking anything.

A retrieval-grounded tool inverts the order of operations. It first finds
passages in a fixed set of documents, then writes an answer conditioned on those
passages, then attaches pointers back to them. A fabricated citation would have
to point at a passage that is not in the source set, which the architecture makes
awkward rather than natural. That is the structural difference, and it is why
this generalizes: any tool built this way inherits the property, and any tool not
built this way does not, regardless of how carefully it was trained.

**Then teach the limit, in the same breath.** Grounding constrains *where* the
text came from. It does not constrain whether the summary read the source
correctly, whether the source set is any good, or whether what is missing from
the source set matters. A confident summary of five bad papers is still a
confident summary of five bad papers, and it will have perfect citations. This is
the AIM-9 content of the session and it belongs in the close, not as a footnote.

## Guardrails

**No PHI, no patient documents, no institutional data.** Consumer Google accounts
carry no BAA. Sources for Part B are published literature, guidelines, or
material the student wrote themselves. A de-identified case someone typed up is
still not appropriate here — the rule is a bright line on purpose, because the
edge cases are exactly where students get it wrong.

**NotebookLM is not a citable source.** If a student uses a grounded tool to find
or summarize literature, the citation is the underlying paper, which they have
read. The tool is a way of navigating sources, not a source. This is standard
attribution practice and worth saying explicitly, because grounded tools *feel*
citable in a way that chatbots do not.

**A grounded search is not a systematic search.** The tool answers from what you
gave it, which means the quality of the answer is bounded entirely by the quality
and completeness of the source set you assembled. That is a strength for reading
a defined body of work and a serious weakness for answering "what does the
literature say," where the sources you failed to include are the ones that would
have changed your mind.

## Reusable material

Nearly all of the didactic content already exists as
`../talks/archive/2025-10-07-rag-notebooklm-idpt-8079/`, published at
`https://talks.seandavis.net/archive/2025-10-07-rag-notebooklm-idpt-8079/`. It is
a written article rather than a slide deck, which is why it can be assigned as
pre-reading and reused as the session handout with no adaptation. It builds the
context window from first principles using the 2020 World Series example and then
shows the same conversation as raw JSON — which is the single clearest way to
make "the model has no memory" land — states plainly that LLMs do not learn from
users except through context, walks the full RAG pipeline, and ends with the
shared-notebook exercise this session's Part A is built on. Archive items are
imported verbatim and slugs are immutable, so the URL is safe to hard-code in a
syllabus.

For the context-window block, `../talks/talks/agentic-coding/slides/tokens.qmd`
and `../talks/talks/agentic-coding/slides/context-window.qmd` frame the context
window as a budget and cover "lost in the middle" (Liu et al. 2023) and context
rot. Both are domain-neutral fragments with substantive speaker notes; they need
clinical examples swapped in but nothing else.

`../talks/archive/2024-11-12-word-embeddings-basis-for-llms/` covers the
machinery under the retrieval step — bag-of-words and TF-IDF limitations,
embeddings, the king-queen analogy, word2vec — and has a "Why Word Embeddings Are
Powerful for Medical Text" section plus a hands-on TensorFlow Embedding Projector
exercise. That is the natural extension if a cohort wants to know what
"semantically similar" actually means, and it is enough material to become its
own session if the four-week assembly ever grows.

`../talks/archive/2024-10-17-prompt-engineering/` supplies clinically-worded
prompt examples for students who write vague queries in Part B; its ten rules are
short and the examples are already medical, so adaptation cost is near zero.
