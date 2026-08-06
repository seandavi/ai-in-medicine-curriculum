# Drive-Only Decks — Recovered Content

Content recovered from the Google Drive PowerPoints that the `talks` repo tracks only as `.yml` stubs. All five files read cleanly via the Drive MCP tools; text extraction was complete (speaker notes are *not* included — this is on-slide text only, so the structure is reliable but the narrative connective tissue is missing).

**Two descriptors are wrong.** `talks/llm-in-medicine` and `agentic-coding/venues/2025-10-17-idpt-vibe-coding.yml` carry titles and abstracts that do not match the actual decks — details in each section below. Fix those before citing them.

---

## 1. `talks/ai-safety` — the most curriculum-ready deck of the four

**Descriptor says:** "Constructive and Safe AI in the Clinic," CU Anschutz IDPT 8079, 2025-10-21, 50 min.
**Deck actually says:** "Constructive Use of AI in the Life of a Medical Resident," Sean Davis MD PhD, October 21, 2025, IDPT-8079. Close enough — the descriptor is a fair paraphrase.

Audience is residents and 4th-year medical students. Discussion-driven, built around **two breakout exercises**, and structured as pitfalls → approaches → perils → a framework. This is the closest thing in the whole portfolio to a ready-made med-student AI-safety session.

**Opening — an anonymous student quote** that frames the whole talk: comparing one's own thought process against an AI response to evaluate *both* the medical knowledge and the AI, "as if the program is a mentor or learner" — followed by the admission that the student does not yet trust their ability to prompt well, and feels "the temptation to quickly use AI to save time despite the limitations."

**Breakout 1** (~8 minutes): discuss with colleagues your concerns about using AI for your own work.

**A set of attributed faculty provocations** used to open the discussion — these are quoted with named attribution on the slides:
- "There is one right approach or answer" — flagged as not reality except in the simplest cases; "medicine is not about the black and white" (Christina Olson, MD)
- "We should be scared. Because what we do is scary!" (Christina Olson, MD)
- From the ChangeMedEd conference: 5–10 years away from *not* using AI being malpractice; "You CAN choose to avoid AI use, but is that really an option?" (Chad Stickrath, MD)
- Lectures only get you so far — competence comes from doing, whether that's taking a history, using a stethoscope, talking about death, or using AI (Matthew Zuckerman, MD)
- "AI is new and powerful, but new is the rule, not the exception" — the internet, the EHR, and patient chat messages were all new once (Sean Davis)

**Scope statement:** focus on LLMs in everyday life as busy residents, teachers, and care-team members; recognize AI is being integrated into systems you do not control; you will use it with increasing regularity, less supervision, and more autonomy.

**Anchor citation:** Abdulnour RE, Gin B, Boscardin CK. *Educational Strategies for Clinical Supervision of Artificial Intelligence Use.* N Engl J Med. 2025 Aug 21;393(8):786-797. <https://www.nejm.org/doi/10.1056/NEJMra2503232> — much of the framework content below comes from this paper.

**Pitfalls:** overtrust in plausible answers · poor prompts · ignoring reasoning · uncritical acceptance · using AI for graded or sensitive work.

**Approaches (one slide each):**
- *Verify-then-trust* — address overtrust by cross-checking against guidelines, mentors, or additional resources
- *Prompting and context* — a **Who / Where / What** scaffold with worked medical examples ("I am a fourth-year medical student…", "I am on a rotation in X in a hospital setting…", "I want to understand why my patient is being treated using…", "I want to teach my medical students about disease X")
- *Ask the AI to explain* — explain your reasoning; explain MY reasoning; tell me like I'm five; ask many follow-ups; **ask the AI to quiz YOU on your understanding**
- *Keep transparency intact* — cite AI use; use for preparation of work, do not substitute FOR work

**Critical thinking and adaptive practice:** clinicians need *adaptive expertise* — shifting between efficient routine practice and innovative problem-solving. Critical thinking is the foundation and must be taught, modeled, and assessed during AI use. Notes that **supervisors often have less AI expertise than learners**, so shared learning and team-based inquiry are recommended.

**The perils** — a sharp three-way distinction worth lifting verbatim:
- **Deskilling** — losing reasoning skills you had
- **Never-skilling** — never learning particular reasoning skills at all
- **Mis-skilling** — learning incorrect reasoning patterns

**Centaur vs. Cyborg** (the deck's central framework): a *centaur* divides tasks and verifies outputs; a *cyborg* co-creates with AI. Adaptive use = knowing when to shift. The deck's own gloss: engagement should vary moment to moment by task type and risk. Centaur strategies suit high-stakes tasks or tools not validated for the intended use — the clinician delegates carefully and always evaluates output. Cyborg strategies may enhance efficiency for low-risk, creative, or well-validated tasks.

**Breakout 2 — centaur vs. cyborg**, sorting eight concrete clinical tasks: drafting a progress note · writing a progress note · literature search · differential diagnosis creation · patient education handout · slide presentation for journal club · summarizing an academic paper · answering a patient message. (The draft-vs-write pairing is deliberate.) The supporting steps listed: specify the task · ask for reasoning · find supporting evidence · evaluate output · apply judgment · integrate reflectively.

**SAFE-AI** and **DEFT-AI** frameworks. Only DEFT-AI is expanded on the slides:
- **D**iagnosis/Discussion — what was your reasoning? how did AI assist?
- **E**vidence — how did you verify?
- **F**eedback — what could improve?
- **T**eaching — what did you learn about AI and reasoning?
- **AI** Recommendation — next steps for safe use.

(SAFE-AI appears as a titled slide with no expansion in the extracted text — likely a figure. Would need the original to recover.)

**Closing:** environment matters · assignments from Christina, "Promptathon" · use AI regularly · "You are the leaders (not even the future ones!)" · physicians must be adaptive in practice and learning · AI is here to stay.

---

## 2. `talks/ml-intro` part 1 — A Gentle Introduction to Machine Learning

October 1, 2025, IDPT-8079, 50 min. **Built entirely on a clinical worked example**, which makes it far more curriculum-ready than the domain-neutral archive `ml-intro` lineage.

**Stated learning objectives:** understand the AI/ML relationship · know data is essential · know ML applications are often about prediction · understand that supervised ML needs paired predictors and truth · recognize linear regression as a type of ML model.

**Definitional ladder** — AI (simulation of human intelligence: learning, reasoning, self-correction) → ML (algorithms that improve through experience, learning without explicitly programmed rules) → Deep Learning (brain-inspired, learns from unstructured data — text, images) → Generative AI (creates new content; relies on deep learning). Notes plainly that AI is an umbrella term now used almost interchangeably with ML.

**The GFR example — the spine of the lecture.** GFR cannot be directly measured in routine practice (gold standard requires infusing inulin or iohexol and collecting urine); instead it is *estimated* from serum creatinine, age, and sex. The slide then asks: **but where does this formula come from? It is learned from data.** From there: dataset (measured creatinine, age, sex, and GFR on many patients) → training → model `GFR = f(creatinine)` → prediction for a new patient with creatinine 0.9 and unknown GFR.

**The generalized loop**, repeated as a recurring visual: translate data into machine-readable predictors → collect associated "truth" → learn to predict truth from predictors → `Response = f(predictors)`.

**A synthetic aside** — "blepticorn" creatures (credited to kimi.ai and ChatGPT) with R/ggplot2 code generating a weight-vs-price scatter, used to ask "what are the predictors? what is the response? what model might work here?" and to introduce parameter fitting ("turn down parameter 1, turn down parameter 2") with worked arithmetic against an actual value.

**Second worked example — predicting medical costs** using an insurance dataset (<https://seandavi.github.io/RBiocBook/ggplot2/intro.html>), asking how many predictors, what kind of variables, what is the response. Then a fully expanded interaction model (age × smoker × obese, all two- and three-way interactions) worked through arithmetically to predict expenses for a 50-year-old obese smoker: **$44,615.73**.

**Summary and the flexibility/interpretability tradeoff:** linear regression (interpretable, small/noisy data, many predictors, understanding relationships is the goal) vs. neural network ("black box", large dataset, complex non-linear `Y=f(X)`, accurate prediction is the goal). Ends by pointing forward to train/test separation, classification vs. regression, and example models.

## 3. `talks/ml-intro` part 2 — Machine Learning, Part 2

October 2, 2025, IDPT-8079, 50 min. Picks up directly from part 1's GFR example.

- **Classification vs. regression** — class/category vs. numerical value; framed as "predict insurance cost" vs. "approve or deny"
- **Errors, split by type** — classification: how often correct, and *what types* of errors (missing a positive, calling a negative true); regression: how far off, and the magnitude and direction of errors
- **Training vs. testing** — "building models that generalize"; the full-dataset → training-set + test-set split, with an explicit slide making the point that the fit shown comes from **only** the training data
- **Bias and variance** — bias as error from an overly simplistic model that cannot capture true relationships (too simple); variance as error from over-sensitivity to small fluctuations in training data (too complex). Includes a **Socratic sequence**: what is your estimate of error in the training data? in the test data? is training error larger or smaller than test error? Then `Total Error = Bias² + Variance + Irreducible Error`
- **Model zoo** — K-nearest neighbor (developed 1951, works for both classification and regression, "only parameter of the model?") · penalized regression (for high-dimensional data, correlated predictors, overfitting) · decision trees · random forest (with the three-step build and the per-tree voting explained) · neural networks (three slides)
- **Resources** — <https://seandavi.github.io/RBiocBook/machine_learning/models.html>, mlr3verse, and the 3blue1brown neural-network video (<https://youtu.be/aircAruvnKk>)
- **Take-homes** — ML is computers learning from data · supervised ML reduces to regression or classification · data quality over quantity, garbage in garbage out · **"the two (or three) set rule is non-negotiable"** · models come with tradeoffs

---

## 4. `talks/llm-in-medicine` — DESCRIPTOR IS WRONG

**Descriptor says:** "How Large Language Models Learn" — "a BigCare session on how large language models are trained and how they learn."

**The deck is actually:** *"The Augmented Analyst: Integrating LLMs into your R journey without Sacrificing Critical Thinking,"* July 8, 2025, BigCare 2025, Irvine CA.

It contains **nothing about how LLMs are trained.** The title in the repo appears to be a placeholder that was never corrected, and the abstract is a guess derived from it. It is also **R-focused, not medicine-focused** — every worked example is dplyr/tidyverse/purrr. The `llm-in-medicine` topic name is a misnomer.

That said, the actual content is genuinely useful for a curriculum, just under a different heading — **how to use an LLM to learn without letting it do your thinking**:

- **Anchor study:** a randomized experimental study comparing learners across AI, human-expert, and checklist-tool conditions (<https://doi.org/10.1111/bjet.13544>). Its finding is the deck's thesis: ChatGPT **significantly improves short-term task performance but may not boost intrinsic motivation, knowledge gain, or transfer**, and can promote dependence and trigger **metacognitive "laziness."**
- Implications drawn for learners (engage in evaluation, monitoring, orientation rather than blindly following feedback to finish tasks efficiently), for teachers (choose which tasks are suitable for AI assistance, stimulate intrinsic motivation, build scaffolding), and for researchers.
- Answer to "should we use LLMs to help us learn?" — **"Probably, yes!"**
- **Five concrete anti-laziness techniques**, each with a worked prompt:
  1. **Start on your own** — always attempt the problem first; grappling is part of learning; consult only when genuinely stuck
  2. **Ask for hints, not answers** — contrasts "Write R code to calculate average monthly sales" against "I think I need dplyr. What functions should I look into? Can you give me a hint on how to start?" Also: have the LLM help build a plan, and give it context about your background
  3. **Teach back to the LLM** — articulate the solution in your own words and ask "is my understanding correct?"
  4. **Focus on the why** — "channel your inner toddler self"; understanding the reasoning is what produces learning
  5. **Four use patterns** — code explanation, error debugging, conceptual clarification, and learning better approaches after you've already solved it
- Framing throughout: *hybrid intelligence* — augment human capability rather than replace it. "Stay in the driver's seat at all times."

**For a med-student curriculum**, the pedagogy transfers directly (it is about learning with an LLM, not about R), but every example would need to be swapped from dplyr to clinical content. It also pairs naturally with the deskilling/never-skilling/mis-skilling material in the `ai-safety` deck — same concern, different vocabulary.

---

## 5. `agentic-coding/venues/2025-10-17-idpt-vibe-coding.yml` — DESCRIPTOR IS THIN

**Descriptor says:** "Vibe Coding: A Live Session" — "IDPT 8079 hands-on session working with AI coding agents live."

**The deck is actually:** *"AI-Powered Medicine: Building the Tools You Wish Existed,"* October 17, 2025, IDPT-8079. The descriptor isn't wrong about format, but the real title is much better and the deck has a clear clinical framing the stub hides.

Short deck (roughly a dozen content slides) — it is mostly a launcher for live building.

- **Framing:** programming has traditionally taken years to master, needs significant time investment, benefits from teamwork, and often requires complex environment setup. But computers are programmed in *languages*, and **LLMs are powerful calculators over language** — they grasp not just syntax but intent, and can translate English to Python. The payoff line: vibe coding lets us **"think computationally without coding."**
- **How to think about it** — "In the past, if you had a good idea, you had to find a programmer. Now you can prototype it yourself." · "This lets you think *with* data, not just *about* it." · exploration prompts: what if I could model patient flow? visualize where errors happen in medication ordering? ask questions of my data?
- **What it's for** — contract out boilerplate · build small proofs-of-principle in plain language · prototype something to hand off to a real programmer · do analysis or build ML models in code rather than a GUI · create websites, documents, datasets · have a programming partner available 24/7
- **Five clinical project examples** — and these are the most directly reusable assignment prompts in any of the four decks:
  1. A patient-satisfaction collection tool linked to your clinic EHR, sent to a random patient sample, with results feeding QI interventions
  2. A "formula portal" — tabbed portal of the formulas you use regularly
  3. A depression-screening collector that feeds into your clinic's medical record system
  4. A website for a local conference you are hosting
  5. An app producing integrated discharge instructions matched to patient and caregiver reading level
- **Tools used:** <https://bolt.new>, Claude Code, and two prepared Google Colab notebooks:
  - <https://colab.research.google.com/drive/14wr7Jyr3lIajsDZMwtjLQp0r0_mAHdmC?usp=sharing>
  - <https://colab.research.google.com/drive/1noXWgOo8__kx2OjC-Ua1I3zLgsWMWFe0?usp=sharing>

  The Colab notebooks are live hands-on assets and were not visible anywhere in the talks repo. Their contents have not been checked — worth opening before relying on them.

---

## What this changes about the earlier inventory

The gap flagged in `talks-inventory.md` section 5 is now closed, and it closed favorably. Three of the four decks are more curriculum-relevant than their stubs suggested:

- **`ai-safety` is the single best fit for a med-student curriculum in the entire portfolio** — better than anything in `archive/`. It is already pitched at residents and 4th-years, already discussion-structured with two breakouts, and carries a 2025 NEJM framework. It was invisible because the stub says nothing.
- **`ml-intro` parts 1 and 2 are clinically grounded** (GFR/creatinine, insurance cost) in a way the archive `ml-intro` lineage is not. Prefer these over the archive versions.
- **The vibe-coding deck's five clinical project prompts** are ready-to-use assignment seeds.
- **`llm-in-medicine` is mislabeled** and is an R talk, though its metacognitive-laziness content is worth keeping under a different heading.

Recovered content is on-slide text only. Speaker notes were not extracted, so where the `ai-safety` deck leans on a framework figure (SAFE-AI) or a diagram, the reasoning behind it is not recoverable from this pass — open the original if that section matters.
