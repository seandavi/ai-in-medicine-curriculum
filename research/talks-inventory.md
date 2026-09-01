# Talks Repo Inventory for a 4-Week AI-in-Medicine Curriculum

**Repo:** `../talks` · published at `https://talks.seandavis.net`

The short version: the two richest reusable assets are the **`agentic-coding` venue decks** (fully sourced Quarto, 1,000–1,750 lines each, with speaker notes that read as prose) and the **`archive/` legacy decks from the IDPT 8079 medical-student course** (rendered HTML only, but exactly the right audience and altitude). Everything under `talks/` other than `agentic-coding` and `microbiome` is a stub pointing at a Google Drive PowerPoint — title and abstract only, no extractable content.

---

## 1. How the repo is structured (build/publish)

Each talk is a self-contained Quarto reveal.js deck rendered to a single `embed-resources: true` HTML file, built by a Python CLI (`uv run talks build`) and published at a **flat URL, `/<slug>/`** — topic directories are an authoring convenience and never appear in URLs; organization is by `tags:` front matter. Three talk kinds coexist: a **project talk** (`talks/<slug>/_quarto.yml` + `index.qmd`, the default), a **fragment topic** (`talks/<topic>/slides/*.qmd` include-only fragments composed by thin `venues/<slug>.qmd` decks — `agentic-coding` is the only example), and an **external deck** (`venues/<slug>.yml` descriptor pointing at a Drive-hosted PowerPoint, from which the Astro site generates a landing page). Legacy talks live in `archive/<slug>/` as verbatim rendered HTML, copied to `_site/archive/<slug>/` without re-rendering, so they are readable and linkable but **not editable as source**.

The repo's own stance on reuse (ADR-0008) is that **reuse across talks is agent-mediated** — read a past deck's rendered `index.md` and adapt it — *not* a live include graph. So new curriculum materials should either link to published URLs (`https://talks.seandavis.net/<slug>/`, archive at `https://talks.seandavis.net/archive/<slug>/`) or copy-and-adapt content, rather than trying to `include` fragments across repos. Every deck also gets an auto-generated per-deck `index.md` markdown rendition and a PDF (plus a `-handout.pdf` with speaker notes for decks with `handout: true`), which is the most convenient form for lifting content.

---

## 2. Talks under `talks/` (current)

### `agentic-coding` — the flagship reusable asset

A fragment topic: nine shared fragments in `../talks/talks/agentic-coding/slides/`, composed by five full Quarto venue decks plus one external stub. Fragments (all with substantive speaker notes): `opener`, `chatbot-vs-agent`, `mental-model`, `tokens`, `context-window`, `working-well`, `good-session`, `pricing`, `takeaways`.

| Venue deck | Title | Length | Audience |
|---|---|---|---|
| `2026-06-18-cshl.qmd` | From Chatbots to Coding Agents | ~90 lines (thin, all includes) | CSHL course, genomics |
| `2026-07-22-bigcare.qmd` | AI Agents for Knowledge Workers | ~1,250 lines | General knowledge workers |
| `2026-07-28-umihc.qmd` | AI Agents for Biomedical Knowledge Work | ~890 lines | Biomedical researchers |
| `2026-07-31-harvard-agents.qmd` | AI Agents for Bioconductor and R | ~1,190 lines | R/Bioconductor developers |
| `2026-07-31-harvard-skills-mcp.qmd` | Skills, MCP, and Sub-agents | ~1,750 lines | Advanced/technical |
| `2025-10-17-idpt-vibe-coding.yml` | Vibe Coding: A Live Session | 50 min, PowerPoint stub | CU Anschutz IDPT 8079 |

Key topics across the family:

- **Chatbot vs. agent** — same model, different scaffolding; the plan/act/observe loop running inside real files with permissions
- **Mental model** — "a capable but junior colleague, not an oracle"; your job shifts from writing to directing and reviewing; model vs. framework distinction
- **Tokens and the context window as a budget** — input vs. output cost asymmetry (output 4–8× input), "lost in the middle" (Liu et al. 2023), context rot
- **Working well** — Markdown as persistent memory (`CLAUDE.md`/`AGENTS.md`), one objective per conversation, clear/compact between tasks, skills vs. one giant instructions file, MCP as "USB-C for AI"
- **Privacy, PHI, and trust** (bigcare, umihc, harvard-agents) — consumer chat accounts are not for PHI; BAA-covered institutional deployments differ; IRB and DUAs outrank the slides; local open-weight models when data can't leave; "verify before it counts — you sign the note." ~500 words of notes; **directly liftable into a medical-student ethics/safety session**. Source: `../talks/talks/agentic-coding/venues/2026-07-28-umihc.qmd:560-616`
- **AI safety / misuse** (bigcare, umihc, harvard-agents) — agentic capability pointed at security, autonomous multi-step attacks, an agent escaping its sandbox, "when capability meets policy," and an honest "what it does and doesn't mean"
- **Cost and access** (`pricing.qmd`) — free tiers are demo-grade; the $20/mo on-ramp framed explicitly as an equity question, with notes warning against the free path quietly failing students
- **Where this is going** (bigcare) — agents built for biomedical research, multi-agent systems that propose and test, agents in cancer research, and the honest evaluation

**Hands-on/demo:** yes, and it's the best one in the repo. `../talks/talks/agentic-coding/demo/` drives a live two-act demo — the agent reads `papers.csv`, downloads 10 open-access single-cell/immunotherapy PDFs, then extracts a structured `extraction.csv` and writes a synthesis. The paper set is deliberately constructed around a **real scientific disagreement** (what predicts checkpoint-blockade response), plus a review with no sample size, so the teachable failure is the agent either smoothing over the disagreement or inventing a missing field. There's a `fetch_papers.py` fallback script and a pre-talk rehearsal checklist. `harvard-skills-mcp` additionally has hands-on "write a skill right now" and a workshop `.mcp.json` with live biomedical MCP servers (`biocontext`, `pdbe`, `gget`, biomcp.org).

**Medicine relevance:** high for the umihc/bigcare variants; the Harvard pair is bioinformatics-only.

### `microbiome` — Microbiome and Metagenomics in Cancer

Full Quarto project (`../talks/talks/microbiome/index.qmd`, ~1,560 lines, 60 min, BigCare audience). Four parts: establishing causation (Koch's postulates from the molecular to the sequencing age), measuring the microbiome (16S vs. shotgun, MetaPhlAn 4, reference databases, the count matrix), the microbiome in cancer (single microbes that cause cancer, indirect effects, microbiome-based diagnostics, therapy), and analysis/data resources (differential abundance, alpha/beta diversity, MicroBioMap, curatedMetagenomicData, BugSigDB). Includes a well-built **cautionary tale** section — a high-profile pan-cancer microbiome result that "was wrong," with a slide explicitly marked "Do not quote the last three rows" and a distinction between what's real and what collapsed. That retraction narrative is genuinely reusable in a curriculum unit on evaluating AI/ML claims in medicine, but the rest is **bioinformatics-only** and too deep for 4th-year med students. No hands-on component; ships a handout build (`make-handout.sh`).

### Stub-only topics (Drive PowerPoints, no extractable content)

- **`ai-safety`** — "Constructive and Safe AI in the Clinic," IDPT 8079, 50 min. **Medicine-relevant title, zero source.** The closest thing to a ready-made clinical-safety lecture, but you'd be rebuilding it from the Drive deck.
- **`llm-in-medicine`** — "How Large Language Models Learn," BigCare, 60 min.
- **`ml-intro`** — two 50-min IDPT 8079 lectures (Intro to ML, parts 1 and 2).
- **`bioconductor`** — ITCR/Bioconductor, 45 min. Bioinformatics-only.
- **`scrnaseq`** — CSHL, 90 min. Bioinformatics-only.

---

## 3. Archive (rendered HTML, verbatim, still linkable)

Ordered by usefulness to this curriculum. All under `../talks/archive/`.

**`2024-10-23-ai-in-medical-education` — the single most on-target deck.** Opens with the Bernard Chang (HMS dean) quote about a once-in-decades revolution in medical education. Covers: an academic-medical-center governance framework (campus-llm-kb); a discussion prompt about ChatGPT drafting residency LoRs; what LLMs know about medicine (Med-PaLM 2 / MedQA); adult-learning principles; a scoping review of AI in medical education; then domain-by-domain — admissions and selection, AI-augmented instruction, teaching clinical reasoning with simulated patients, assessment, AI-generated MCQs, procedural-skills tracking; student attitudes; ethics. Second half is a **ready-made faculty/policy module**: a four-tier taxonomy of classroom AI policies (prohibited / allowed with attribution / limited instances / broadly encouraged), academic-integrity appeals (logical, moral, personal), twelve practical tips for ethical AI in medical education, and the FACETS reporting framework. Discussion-driven; no technical hands-on.

**`2024-11-05-ml-fairness` — Fairness in Machine Learning for Healthcare.** Two strong opening thought experiments (the CEO image-search dilemma; the FICO loan officer). Distinguishes social vs. statistical bias and shows they're mathematically at odds; procedural, distributive, and representational fairness (Crawford); harms of allocation vs. representation; sources of bias in healthcare ML (collection, sampling, label, feature selection, algorithmic); mitigation strategies (reweighting, adversarial debiasing, fair representation learning, post-processing); implementation and ethics. Discussion-heavy, **highly medicine-relevant**, and the most seminar-ready item in the archive.

**`2024-10-28-ai-ml-oncology-service-line` — AI in the Oncology Service Line.** Institutional/implementation view: AI vs. ML vs. deep learning ontology, a campus LLM governance framework and vision statement, then stakeholder-by-stakeholder considerations (patients, providers, researchers, administrators) and monitoring/compliance. The core is the **eight guiding principles for AI tools in healthcare** (doi:10.1038/s43856-023-00279-9): alleviate health disparities, report clinically meaningful outcomes, reduce overdiagnosis/overtreatment, have high healthcare value, incorporate biography (social/structural/environmental exposures beyond biology), be tailorable to local populations, promote a learning healthcare system, facilitate shared decision-making. An excellent spine for a "how do you evaluate a clinical AI tool" session.

**`2025-09-30-ai-history` / `2024-10-30-ai-history` / `2024-09-19-ai-history` (three near-identical versions) — History of AI and ML.** Turing 1936/1950, McCulloch-Pitts, Dartmouth 1956, perceptron, ELIZA; a full **expert-systems section built around MYCIN** (features, impact, legacy); AI winters; the 2000s technology triggers including **health information exchanges**; then AlexNet, **IBM Watson winning Jeopardy! and MD Anderson setting Watson aside (2017-18)**, GANs, AlphaGo, transformers, AlphaFold, GPT-4. The Watson and MYCIN threads make this the medicine-flavored version of an AI history lecture. `2025-09-29-brief-history-ai-idpt-8079` is a landing page only (7 lines) — the actual IDPT 8079 delivery is externally hosted.

**`2025-10-07-rag-notebooklm-idpt-8079` — LLMs with Retrieval Augmented Generation.** Not a slide deck but a **written article/handout**, which makes it the easiest thing here to fold into a reading assignment. Builds the context window from first principles (the 2020 World Series ChatGPT example, then the same conversation shown as JSON), states plainly that LLMs don't learn from users except through context, walks the RAG pipeline (chunking, embedding, indexing, semantic retrieval, augmentation, generation), lists benefits, and ends with a **hands-on NotebookLM exercise** — a shared notebook of physician and patient perspectives on AI in healthcare, plus instructions to build your own. Directly usable as a week-2 or week-3 lab.

**`2024-10-17-prompt-engineering` — ten rules, medical examples throughout.** Clear objective, provide context ("A 55-year-old male with a history of hypertension presents with chest pain…"), precise language ("epigastric pain radiating to the back" not "stomach pain"), specify output format (differential diagnosis lists), iterate, few-shot (medical abbreviation expansion), decompose complex tasks, delimiters, bias awareness, stay current. Short, ~15 slides, and the examples are already clinical — **near-zero adaptation cost**.

**`2024-10-17-ai-agents-and-llms` — AI Agents (2024 vintage).** Tool use, APIs, JSON structured output, the task-identification → tool-selection → API-call → response-integration loop, planning/memory/tools decomposition, and a healthcare tool-use slide. Superseded in every respect by the 2026 `agentic-coding` decks; useful only if you want the simpler, pre-agentic-coding framing.

**`2024-10-31-ml-intro` (also `2024-09-20-ml-intro`, `2023-11-03-monroe-ai-ml`, `2023-07-11-cshldata-ai-ml-intro`, `2022-09-06-cu-som-ai-ml-intro` — same lineage).** ~55 slides: supervised vs. unsupervised, classification vs. regression, a data-types side trip (structured vs. unstructured, tabular), the scikit-learn algorithm map, worked classification and regression examples with data exploration, train/test splits and generalizability, algorithm survey, and bias. The most complete ML-fundamentals deck available as readable source-ish HTML. Medicine-neutral — examples would need clinical substitution.

**`2024-11-06-deep-learning-intro` — From Simple Models to Deep Networks.** Opens with deep learning in healthcare and medical imaging plus opportunities/obstacles, then builds a neuron from linear regression and works up to image classification. Ends with a **hands-on TensorFlow Playground tutorial**. Short (~28 slides), good week-1 or week-2 material.

**`2024-11-12-word-embeddings-basis-for-llms` — Language for computers.** Bag-of-words and TF-IDF limitations, embeddings, the king-queen analogy, word2vec skip-gram training, then **"Concepts applied in Healthcare" and "Why Word Embeddings Are Powerful for Medical Text."** Closes with hands-on exercises: TensorFlow Embedding Projector, a word-embedding visualization, and an optional Python notebook. The natural bridge lecture between ML fundamentals and LLMs.

**Not relevant:** `2023-03-08-univ-colorado-bmsc-7812-r-intro` (R/reproducibility, has a `hands-on.html`), `2023-11-27-cuny-json-data`, `2024-11-13-big-data-storage-formats`, `2023-05-19-uccc-sd-retreat`.

---

## 4. Medicine-relevant vs. bioinformatics-only

**Medicine-relevant:** `archive/2024-10-23-ai-in-medical-education`, `archive/2024-11-05-ml-fairness`, `archive/2024-10-28-ai-ml-oncology-service-line`, `archive/2025-10-07-rag-notebooklm-idpt-8079`, `archive/2024-10-17-prompt-engineering`, the AI-history decks (MYCIN + Watson threads), `archive/2024-11-06-deep-learning-intro` (imaging framing), `archive/2024-11-12-word-embeddings-basis-for-llms` (medical-text section), `talks/ai-safety` (stub), `talks/ml-intro` (stub, IDPT 8079), and the PHI/privacy + safety sections of the `agentic-coding` bigcare/umihc decks.

**Bioinformatics-only:** `talks/microbiome` (except the retraction case study), `talks/scrnaseq`, `talks/bioconductor`, `agentic-coding/venues/2026-07-31-harvard-*` and `2026-06-18-cshl`.

**Domain-neutral, needs clinical examples swapped in:** the `ml-intro` lineage and the core `agentic-coding` fragments (`tokens`, `context-window`, `mental-model`, `good-session`).

---

## 5. Practical notes for building on this

The `agentic-coding` shared fragments are the only content in the repo designed for recomposition, and a sixth venue deck for a med-student audience would be cheap: `opener` + `chatbot-vs-agent` + `mental-model` + `tokens` + `context-window` + `working-well` + `good-session` + `takeaways` already exist, and you'd write only the clinical framing and the PHI section (liftable nearly verbatim from `venues/2026-07-28-umihc.qmd:560-616`).

Everything in `archive/` is rendered HTML with no recoverable `.qmd`, so reuse there means either linking to the published URL or extracting text and rewriting. Note the archive rule: those decks are imported verbatim and never re-rendered, and slugs are immutable once published — so links are safe to hard-code.

The gap worth flagging: the two most curriculum-shaped items — `talks/ai-safety` ("Constructive and Safe AI in the Clinic," IDPT 8079) and `talks/ml-intro` — exist only as Drive PowerPoint stubs. If those decks matter to the curriculum, someone needs to open the Drive files; nothing in this repo reveals their content beyond a one-line abstract.
