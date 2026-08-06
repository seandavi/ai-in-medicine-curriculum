# Core module — How these systems actually work

**Format:** one 75-minute Zoom session · **Prereq:** none (no math or coding background assumed)
**Competencies:** AIM-1 (foundations of AI and data); AIM-2 (critical appraisal)

## The claim this module tests

Students do not need to build a model to use one safely, but they do need a
mechanical picture accurate enough to predict how it fails. The organizing move
is to start from something every fourth-year already trusts and uses daily — the
estimated GFR on every basic metabolic panel — and show that it is a model
learned from data, with all the properties that implies. Once "the formula came
from data" is real, the rest follows: why a model degrades in a population it
was not trained on, why a language model produces fluent citations that do not
exist, and why neither of those is a bug someone forgot to fix.

The session ends with students having produced a hallucination on purpose and
explained it mechanically. That explanation is the deliverable, not the
hallucination.

## Learning objectives

By the end, a student can:

1. Explain, using eGFR as the worked example, what it means for a formula to be *learned from data* rather than derived, and name the predictors, the response, and the training population for that model.
2. Distinguish supervised from unsupervised learning by what the training data contains, and classification from regression by what the model emits.
3. State why a model's performance on data it has already seen tells you nothing useful, and why the train/test separation is the non-negotiable minimum.
4. Describe in plain language what a language model computes at each step, and use that description to explain why fabricated citations and confident wrong answers are properties of the mechanism.
5. Name two structural limits of the context window — that it is a shared budget, and that material buried mid-window is attended to less reliably — and say what each implies for how they will prompt.

## Tool and prep notes

**In session, browser only, no accounts required for the modeling half.**
TensorFlow Playground (`playground.tensorflow.org`) runs in any browser with no
login and no install, which is what makes it survivable across forty machines.

**Pre-work is one account, not a reading.** Students need a free account on
whichever general-purpose assistant the course has standardized on (Claude.ai or
the institutional equivalent) for the second half. Say so a week ahead;
creating accounts live burns ten minutes and strands the students who hit a
verification problem.

**Standing rules, pinned in chat for the whole session:** no PHI in any consumer
tool, ever; verify before it counts; you sign the note. These recur in every
module and are stated here first because this is where the mechanical reason for
them gets established.

## Session plan (75 min)

| Time | Mode | What happens |
|---|---|---|
| 0–8 | Talk + poll | Open on a chemistry panel. Zoom poll: "Where does the eGFR number come from?" Reveal: GFR is not measured in routine practice — the gold standard requires infusing inulin or iohexol and collecting urine. It is estimated from creatinine, age, and sex. Then the question the whole session hangs on: **where did that formula come from?** |
| 8–22 | Talk (slides, tight) | The generalized loop, drawn once and referred back to all session: translate data into machine-readable predictors → collect the associated truth → learn to predict truth from predictors → `Response = f(predictors)`. Supervised vs. unsupervised as a question about whether the truth column exists. Classification vs. regression as a question about what comes out. Train/test separation, and bias vs. variance as too-simple vs. too-sensitive. |
| 22–42 | Breakout (4–5) on TensorFlow Playground | Each group works one shared screen. Fit the spiral dataset; then deliberately break it in both directions. Group records three judgments on a shared slide — see below. |
| 42–54 | Talk (slides, tight) | From tables to language. Words become vectors; a language model is trained to predict the next token from the ones before it. Tokens as the actual unit of processing, the context window as a shared budget, and the two failure modes that follow: everything competes for the same space, and material buried in the middle is attended to less reliably than material at the edges. Then the payoff sentence: nothing in this mechanism contains a step where the model checks whether a claim is true. |
| 54–68 | Breakout (same groups) | Hallucination hunt — see below. Each group posts one verified fabrication with a mechanical explanation. |
| 68–75 | Report-back and close | Two or three groups read their fabrication and their explanation. Close on the standing question: what does this change about how you'll practice? |

**Deliverable:** one shared slide per group carrying the three Playground
judgments and one documented fabrication with its mechanical explanation. Forty
students produce eight slides; the deck is the class's own record of how these
systems fail.

## Activity 1 — Overfitting you can see (20 min)

Groups of 4–5, one member screen-sharing `playground.tensorflow.org`. No
account, no install, and the visual feedback is immediate enough to survive
Zoom.

1. Select the **spiral** dataset. With only the two raw `X₁`, `X₂` features and
   a single small hidden layer, run it. It will not separate the classes. Record
   what the training loss does.
2. Now add capacity — more features, more layers, more neurons — until the
   training loss goes near zero. Look at the **test loss** in the same panel.
3. Set the noise slider high and re-run the large network. Watch the decision
   boundary contort around individual points.

The group writes three sentences on its slide: *which configuration was too
simple and how we could tell*; *which was too complex and how we could tell*;
and *what we would have concluded if we had only ever been shown the training
loss*. That third sentence is the one that transfers — it is the same question
they will ask of every vendor performance claim in `core-appraisal`.

Instructors should resist the temptation to lecture over this. The whole point
is that they see the training curve and the test curve diverge themselves.

## Activity 2 — Hallucination hunt (14 min)

Same groups. Each group asks its assistant for something with a checkable
answer in a domain the group knows, and where the correct answer is specific
rather than general. Assign one prompt per group so the class covers a spread:

- Ask for five references supporting a named clinical claim, with PMIDs.
- Ask for the exact point values and cutoffs of a scoring system the group has
  used on the wards, plus the original publication.
- Ask for the dosing of an uncommon drug in renal impairment, with a source.
- Ask a question whose honest answer is "that is not established."

The group then **verifies** — PubMed, MDCalc, the original publication — and
posts to the shared slide: the prompt, the specific claim that turned out to be
wrong or unverifiable, and one sentence explaining it in terms of the mechanism
described at minute 42. "It predicted plausible next tokens and a plausible
citation looks like a real one" is the answer being fished for. "It made a
mistake" is not.

A group that fails to produce a fabrication has still produced the more useful
result, and should report that too: the failure rate is not 100%, which is
exactly why unverified output is dangerous rather than merely useless.

## Framing notes

Two threads from the history material are worth thirty seconds each if the room
is cold, and both are medicine-flavored. **MYCIN** — an expert system that
performed respectably at antimicrobial selection and was never deployed — makes
the point that clinical performance and clinical adoption are different
problems. **IBM Watson**, from winning Jeopardy! to MD Anderson setting the
oncology project aside in 2017–18, makes the point that a demonstration is not
a deployment. Both give students a reference class for the current wave that is
neither hype nor dismissal.

Resist expanding the model zoo. K-nearest neighbors, random forests, and
penalized regression are available in the source material and are interesting,
but naming five algorithms in a 75-minute session buys vocabulary at the cost of
the mechanism, and the mechanism is the thing that generalizes. If the cohort
wants the zoo, point them at the resources rather than spending session time:
`https://seandavi.github.io/RBiocBook/machine_learning/models.html` and the
3blue1brown neural-network video (`https://youtu.be/aircAruvnKk`).

Be straight about what is uncertain. "Context rot" — quality degrading as input
grows long, sometimes well below the advertised limit — comes from 2025 studies
across frontier models and is a robust finding in shape, but the specific
thresholds move with every model release and should not be quoted as numbers.
The same goes for token pricing: the asymmetry (output costs several times
input) is durable; the figures are not.

## Reusable material

The spine of the didactic half is the **recovered `ml-intro` part 1 and part 2
Drive decks** — `talks/ml-intro/venues/2025-10-01-idpt-ml-intro.yml` and
`2025-10-02-idpt-ml-intro-pt2.yml` in the talks repo, whose content is
summarized in `../research/talks-drive-decks.md` sections 2 and 3. These are the
versions to use: they are built on the GFR/creatinine example and a medical-cost
regression, where the archive `ml-intro` lineage is domain-neutral and would
need clinical examples substituted throughout. Part 1 supplies the definitional
ladder (AI → ML → deep learning → generative AI), the GFR spine, and the
flexibility/interpretability tradeoff. Part 2 supplies classification vs.
regression, error types, the train/test split, and the bias–variance Socratic
sequence.

**Caveat carried forward from the research pass:** those decks were recovered as
on-slide text only. Speaker notes were not extracted, so the narrative
connecting the slides is not in the summary — open the originals in Drive before
delivering, particularly for the bias–variance sequence, which is written as
questions whose intended answers live in the notes.

The neural-network hands-on comes from
`../talks/archive/2024-11-06-deep-learning-intro`, which already ends on a
TensorFlow Playground tutorial and opens with medical imaging framing. The
bridge from tables to language comes from
`../talks/archive/2024-11-12-word-embeddings-basis-for-llms`, which has a
"Why Word Embeddings Are Powerful for Medical Text" section and the Embedding
Projector exercise; only the embeddings-to-next-token-prediction step needs
writing fresh.

Tokens and the context window lift directly from the agentic-coding fragments
`../talks/talks/agentic-coding/slides/tokens.qmd` and
`../talks/talks/agentic-coding/slides/context-window.qmd`, both of which carry
substantive speaker notes and existing figures. They are domain-neutral, but
nothing in them needs a clinical example — the budget metaphor works as written.

The MYCIN and Watson threads are in any of the three near-identical AI-history
decks; `../talks/archive/2025-09-30-ai-history` is the most recent.
