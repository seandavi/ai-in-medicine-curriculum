# Review: core-foundations slide deck, 2026-10-03

Six-persona review of `slides/core-foundations.qmd` per `curriculum/personas.md`,
run by AI agents, one per persona, in three rounds. Each agent read the deck
source, the narration script, and a screenshot of every slide; several also ran
the widgets and the TensorFlow Playground presets in a headless browser. Elena
read first and Dr. Lindqvist last. Items marked *open* were not fixed and are
for the author.

## Verdicts

| Reader | Round 1 | Round 2 | Round 3 |
|---|---|---|---|
| Elena | put down (1 blocker) | put down | keep |
| Marcus | put down (1 blocker) | put down | keep |
| Priya | put down (1 blocker) | keep | not needed |
| Jordan | put down (2 blockers) | put down | keep |
| Dr. Okafor | put down (2 blockers) | keep | not needed |
| Dr. Lindqvist | put down (6 majors) | keep | not needed |

## Round 1: what the readers found, and what changed

- **Elena.** No route into the chatbot exercise without a phone number; key
  terms defined only in the speaker notes; an unreadable xkcd comic; small
  text. *Changed:* a "What you will be able to do" slide with what you need
  and a no-phone-number route; proxy, function, fit, token, temperature,
  context window, external validation, bias, variance, overfitting and epoch
  defined on the slides; the comic cut; all small text raised.
- **Marcus.** "The model does not look anything up" ignored tools with web
  search; the HEART quiz could be solved by reading the years; the exercise may
  not fail on a paid tool. *Changed:* "the model itself" plus a line on search
  tools; a search off/on comparison; prompt B (five references with PubMed
  IDs); a radiology row (Fleischner); years removed from the quiz.
- **Priya.** The closing clinic question had no answer for a self-paced
  student; nothing told her what to do on the wards. *Changed:* a model answer
  to "what do you say to the attending"; a new "On the wards" slide with one
  sentence for a co-intern; "no alert does not mean no sepsis".
- **Jordan.** Objective 5 had no activity; live timing overran; the Check
  rubric was missing; every widget failed if a CDN was blocked. *Changed:*
  students write their own two keyboard rules; a run sheet with minutes per
  block and a skip list; a "Check yourself" slide; widgets rewritten as plain
  HTML and SVG with no library download, tested with every outside domain
  blocked.
- **Dr. Okafor.** The original Playground presets did not show overfitting (the
  flexible network had the lowest test loss); the breakouts could not be run
  from the deck alone. *Changed:* new presets (same noisy spiral, 20% training
  data) where step 3 has the worst test loss at about 500 epochs, checked by
  three reviewers independently; LIVE cues for what to paste before each
  breakout, the shared page, and "if asked" answers.
- **Dr. Lindqvist.** The business associate agreement sentence contradicted
  rule 1 and named products; no-PHI reminders were missing where students type;
  the sepsis slide asserted a cause the study did not test; no AI disclosure.
  *Changed:* the privacy-office wording on slides 2, 39 and 46; "made-up
  sentence, never about a patient" wherever students type; the sepsis slide
  says what the study shows and not why; an on-slide disclosure and a ledger
  row.

## Rounds 2 and 3

Round 2 found a wrong time map (68 minutes, not 75), the quiz answer printed
under the question, the personal-paid-account point only in the notes, an
exercise that had grown without more time, and a Playground criterion that
stops holding if a group runs past about 1,500 epochs. All were fixed: the time
map adds to 75, the source line is a fragment shown after the guess, prompt A
is marked required and the rest is optional, and students pause at about 500
epochs. Round 3 found no blocker or major.

## Open, for the author

- *Open.* The repository has no licence, so a borrowing educator cannot reuse
  the deck or its figures. Choosing one is the author's decision.
- *Open.* Live timing is about 3 to 4 minutes over 75 by Jordan's estimate,
  with the module's 20- and 14-minute breakouts. Not timed with a presenter.
- *Tested after round 3.* The chatbot prompts were run once each on four
  models with search off (`research/foundations-chatbot-test-2026-10-03.md`).
  Large current models got prompt A right on the famous scores; prompt B
  produced wrong PMIDs from all four models, from 1 in 10 (GPT-5.4) to all of
  them (Gemini 2.5 Flash). The deck now sends students who get A right on to
  B, and tells them to read the title of each PMID.
- *Open.* The chapter's Part B uses prompt A only. By this test, a student
  using a large current model will often get it right and have no error to
  explain. The chapter already covers that case; adding prompt B would make an
  error more likely. The chapter was not changed here.
- *Open.* The chapter's own Playground exercise (Part A) uses noise 0 and the
  default 50% training split. The reviewers found that setup shows little
  overfitting; the deck's presets do. The chapter was not changed here.
