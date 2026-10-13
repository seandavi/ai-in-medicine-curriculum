# AI Enrichment Modules — Research Report

Background research for the "AI enrichment" modules of a 4-week, Zoom-only, ungraded
AI-in-medicine elective for ~40 fourth-year medical students.

**Compiled:** 2026-08-05. **Research window:** current through August 2026.

---

## How to read this document

This report was assembled from five parallel research passes (one per area below), each
of which verified claims against primary sources where possible. **Caveats and
"unverified" flags from the original research are preserved deliberately and have not
been smoothed into confident prose.** Where a number could not be confirmed, it says so.
Treat every flagged item as requiring a fresh check before it goes on a slide.

Three global warnings:

1. **Sections 4 and 5 have fast-moving legal and regulatory status.** Litigation dockets,
   FDA guidance, and EU AI Act deadlines all moved during 2025–2026 and several items are
   mid-flight. Re-verify close to the course date.
2. **Provenance is uneven.** Some claims are PubMed-verified with DOIs; others come from
   trade press, law-firm client alerts, or vendor material. The sourcing is stated
   inline. Where only a secondary source exists, it is labelled.
3. **The ethics/regulation area (Section 5) was assembled from three topic-specific
   research passes that were never merged by a synthesizing pass.** One of those passes
   exhausted its search budget partway through. The resulting gaps are listed explicitly
   at the end of Section 5 — they are real holes, not oversights in the writing.

---

## Area 1 — Hands-on LLM activities for medical students

### 1.1 Published prompt-engineering exercises with clinical vignettes

Evidence here is thinner than for the diagnostic-accuracy literature. Few papers describe
a formal "prompt engineering exercise" as such, but two directly relevant peer-reviewed
pieces exist:

- **Waldock WJ, Lam G, Baptista A, Walls R, Sam AH.** "Which curriculum components do
  medical students find most helpful for evaluating AI outputs?" *BMC Med Educ*
  2025;25(1):195. [DOI](https://doi.org/10.1186/s12909-025-06735-5).
  Final-year Imperial College students (n=148) evaluated GPT-3.5's answers to 10 clinical
  vignettes, 5 of them deliberately wrong. Median correct-evaluation rate was only **56%**.
  Students reported that case-based and pathology teaching — not formal AI training — was
  what let them catch errors. Only **5%** had heard of "clinical prompt engineering."
  Useful as baseline-need justification for the elective.

- **Choy BC, Shanmugam H, Redden HW, et al.** "Artificial Intelligence and Large Language
  Models: A Case-Based, Peer-Teaching Workshop for Preclinical Medical Students."
  *MedEdPORTAL* 2026;22:11621. [DOI](https://doi.org/10.15766/mep_2374-8265.11621).
  A published, reusable MedEdPORTAL module: 60-min lecture plus 100-min interactive-case
  workshop for Harvard preclinical students (n=168 enrolled, some groups peer-led).
  Pre/post Likert surveys (n=124/62) showed statistically significant knowledge and
  self-efficacy gains (p<.01); attitude and behavioral-intent items were mixed. This is
  the closest thing to a ready-made template — worth pulling the full module from
  MedEdPORTAL for structure and timing.

No MedEdPORTAL module specifically titled around "prompt engineering with clinical
vignettes" was found beyond Choy et al. Related but non-peer-reviewed-as-classroom-exercise
material: a general "Prompt Engineering as an Important Emerging Skill for Medical
Professionals" tutorial (PMC10585440), and a case study on ChatGPT-driven interactive
clinical simulations for early clinical education (PMID 37948112, PMC10674152).

### 1.2 LLMs for differential diagnosis — studies students can critique

- **Goh E, Gallo R, Hom J, et al.** "Large Language Model Influence on Diagnostic
  Reasoning: A Randomized Clinical Trial." *JAMA Netw Open* 2024;7(10):e2440969.
  [DOI](https://doi.org/10.1001/jamanetworkopen.2024.40969).
  Single-blind RCT, 50 physicians (26 attendings, 24 residents), up to 6 vignettes, 60 min.
  LLM-plus-conventional-resources vs conventional alone: median score 76% (IQR 66–87) vs
  74% (IQR 63–84); adjusted difference **+2 points** (95% CI −4 to 8, p=.60) — access to an
  LLM did *not* significantly help physicians. Time per case 519s vs 565s (n.s.).
  Critically, the **LLM alone scored 16 points higher** than the conventional-resources
  group (95% CI 2–30, p=.03). The tool outperformed the humans using it. Excellent
  discussion material.

- **Kanjee Z, Crowe B, Rodman A.** "Accuracy of a Generative Artificial Intelligence Model
  in a Complex Diagnostic Challenge." *JAMA* 2023;330(1):78–80.
  [DOI](https://doi.org/10.1001/jama.2023.8288). GPT-4 against NEJM
  clinicopathological-conference-style case records.
  **⚠ The PubMed abstract field was empty for this record.** Widely-reported secondary
  figures — correct diagnosis in the differential in roughly two-thirds of cases, top
  diagnosis in under half — **should be verified against the primary PDF before quoting
  exact percentages to students.**

- **Tu T, Schaekermann M, Palepu A, et al.** "Towards conversational diagnostic artificial
  intelligence." *Nature* 2025;642(8067):442–450.
  [DOI](https://doi.org/10.1038/s41586-025-08866-7).
  Google's AMIE vs 20 primary-care physicians, randomized double-blind crossover,
  text-based OSCE-style consultations with validated patient-actors, 159 case scenarios
  (Canada/UK/India). AMIE showed greater diagnostic accuracy and superior performance on
  **30/32 axes** per specialist raters and **25/26 axes** per patient-actors. Key
  limitation to raise with students: synchronous text chat is not real clinical practice.

- **McDuff D, Schaekermann M, Tu T, et al.** "Towards accurate differential diagnosis with
  large language models." *Nature* 2025;642(8067):451–457.
  [DOI](https://doi.org/10.1038/s41586-025-08869-4).
  20 clinicians, 302 real-world challenging cases from published case reports. AMIE
  standalone top-10 accuracy **59.1% vs 33.6%** unassisted (p=.04). Clinicians assisted by
  AMIE reached **51.7%** top-10 accuracy vs **36.1%** unassisted (p<.01) and vs **44.4%**
  with search engines only (p=.03).

- **Microsoft MAI-DxO** ("Sequential Diagnosis with Language Models"), 2025.
  arXiv:2506.22405 plus Microsoft AI blog. MAI-DxO solved up to **85.5%** of 304 difficult
  cases adapted from NEJM CPC cases, vs a **20%** average for 21 experienced physicians
  under constrained benchmark conditions (sequential test-ordering, cost tracking, no open
  internet).
  **⚠ This is a preprint / industry tech report, not peer-reviewed** as of Aug 2026. Flag
  clearly to students: curated hard cases, benchmark rules that restricted physician
  resources, no clinical validation.

### 1.3 LLMs for patient communication

- **Ayers JW, Poliak A, Dredze M, et al.** "Comparing Physician and Artificial Intelligence
  Chatbot Responses to Patient Questions Posted to a Public Social Media Forum."
  *JAMA Intern Med* 2023;183(6):589–596.
  [DOI](https://doi.org/10.1001/jamainternmed.2023.1838).
  195 Reddit r/AskDocs exchanges; licensed evaluators preferred chatbot responses in
  **78.6%** of 585 evaluations (95% CI 75.0–81.8). Chatbot responses were much longer
  (median 211 vs 52 words, p<.001), rated higher quality (good/very good 78.5% vs 22.1%,
  ~3.6x) and far more empathetic (empathetic/very empathetic 45.1% vs 4.6%, ~9.8x).

- **Garcia P, Ma SP, Shah S, et al.** "Artificial Intelligence-Generated Draft Replies to
  Patient Inbox Messages." *JAMA Netw Open* 2024;7(3):e243201.
  [DOI](https://doi.org/10.1001/jamanetworkopen.2024.3201).
  Stanford Health Care 5-week QI pilot, 162 clinicians. AI-draft utilization averaged
  **20%** of replies; **no significant change in reply, write, or read time**, but
  statistically significant drops in physician task load (61.31→47.26, p<.001) and
  work-exhaustion scores (1.95→1.62, p<.001). A good counter-example to "AI saves time" —
  it reduced *burden*, not clock time.

- **Fereydooni S, Homer R, Chartash D.** "From complexity to clarity: GPT-4 for
  patient-centered prostate cancer pathology reports." *Patient Educ Couns*
  2026;149:109597. [DOI](https://doi.org/10.1016/j.pec.2026.109597).
  GPT-4-turbo rewrote 44 TCGA prostate-cancer pathology reports; iterative prompt
  engineering on 20, tested on 24 unseen. Significantly reduced text complexity (p<.001);
  academic vocabulary score fell 68.47→23.16. Authors report iterative prompting
  "eliminated hallucinations."

- **Monaci M, Viviani E, Sottotetti F, Bigi S, Barello S.** "Beyond readability: Advancing
  patient-centered evaluation of AI-generated clinical reports." *Patient Educ Couns*
  2026;149:109702. [DOI](https://doi.org/10.1016/j.pec.2026.109702).
  Commentary arguing readability scores alone are insufficient; proposes evaluating
  AI-simplified documents on comprehensibility, relevance, usability, emotional impact,
  and empowerment, with patients involved in design. Good basis for a student-facing
  evaluation checklist that goes beyond Flesch-Kincaid.

### 1.4 Hallucination and fabricated-citation detection

Strong, quantified evidence across specialties, several from 2026:

- **Gravel J, D'Amours-Gravel M, Osmanlliu E.** "Learning to Fake It: Limited Responses and
  Fabricated References Provided by ChatGPT for Medical Questions." *Mayo Clin Proc Digit
  Health* 2023;1(3):226–234. [DOI](https://doi.org/10.1016/j.mcpdig.2023.05.004).
  Of 59 references ChatGPT provided across 20 medical questions, **41 (69%) were
  fabricated** despite looking real.

- **McGowan A, Gui Y, Dobbs M, et al.** "ChatGPT and Bard exhibit spontaneous citation
  fabrication during psychiatry literature search." *Psychiatry Res* 2023;326:115334.
  [DOI](https://doi.org/10.1016/j.psychres.2023.115334).
  March 2023: 35 citations generated, only **2 were real**.

- **McLaughlin ND, Srinivas AN, Lowe ZF, et al.** "Large Language Model Hallucinations in
  Spine Surgery: A Comparative Analysis of Clinician vs Patient-Level Prompts."
  *Neurosurg Pract* 2026;7(3):e000244.
  [DOI](https://doi.org/10.1227/neuprac.0000000000000244).
  Five tools (ChatGPT, Gemini, Claude, Copilot, OpenEvidence), citations scored 2/1/0
  (accurate/misrepresented/fabricated). **OpenEvidence had zero fabrications** (it indexes
  PubMed directly); among general-purpose LLMs, Claude was most accurate (78.0% accurate
  citations), Gemini worst (26.2% fabrication rate). Notably, **ChatGPT's fabrication rate
  rose from 2.1% on clinician-framed prompts to 20.0% on patient-framed prompts** — a
  strong demonstration that prompt framing changes hallucination risk.

- **Sakharkar M, Jalihal P, Chang S, et al.** "Large Language Model Responses to Common
  Otolaryngological Questions." *Otolaryngol Head Neck Surg* 2026.
  [DOI](https://doi.org/10.1002/ohn.70309). ChatGPT and Claude "both hallucinated at least
  half of their references" on patient-facing ENT questions.

- **Frutuoso Maia BK, de Morais EF, de Santana Santos T, Pagotto LEC.** "Performance of
  large language models in preoperative and postoperative counselling for aesthetic facial
  procedures." *Br J Oral Maxillofac Surg* 2026;64(3):216–222.
  [DOI](https://doi.org/10.1016/j.bjoms.2026.01.002).
  GPT-4 produced **36%** hallucinated citations vs Gemini 14% and DeepSeek 8.8%
  (p<.00001) — useful for showing hallucination rates vary substantially by model.

- **Shah R, Miranda JL.** "Leveraging generative artificial intelligence errors to teach
  appropriate citation usage." *J Microbiol Biol Educ* 2026;e0019525.
  [DOI](https://doi.org/10.1128/jmbe.00195-25).
  The one published **classroom-exercise framework** built specifically around AI citation
  errors. Not medicine-specific (biology), but directly portable.

### 1.5 Free / accessible tools for a Zoom session (as of Aug 2026)

| Tool | Access model | PHI / HIPAA note |
|---|---|---|
| **ChatGPT (free tier)** | Free account, no institutional verification | Consumer tier not BAA-covered — no PHI |
| **Claude.ai (free tier)** | Free account, defaults to Sonnet | Consumer tiers (Free/Pro/Max/Team) explicitly outside Anthropic's BAA — never use with PHI |
| **Google Gemini / NotebookLM** | Free with any Google account; NotebookLM 100 notebooks, 50 sources/notebook, 50 queries/day | Consumer tier, not PHI-safe |
| **OpenEvidence** | Free for verified US clinicians (NPI) **and medical students** (student ID/transcript upload); NEJM Group and JAMA Network content partnerships; vendor markets it as HIPAA-compliant | Not currently available in UK/Europe; verify institutional policy before treating as PHI-safe |
| **Doximity GPT** | Free for verified US physicians, NPs, PAs, **and medical students** via Doximity verification; vendor states HIPAA/BAA support | Same caveat — verify with your institution |
| **Consensus** | Free tier (limited queries/day); paid ~$8.99+/mo | Not for PHI; literature-search tool |
| **Elicit** | Free tier with query limits; structured literature review/extraction | Not for PHI |
| **Perplexity** | Free tier; "Deep Research" mode more autonomous as of 2026 | Not for PHI |
| **Abridge / Nabla** | Enterprise-focused; **no meaningful free trial for individual students** as of 2026 | Enterprise BAA required; do not live-demo with real patient audio |

**Planning implication:** ChatGPT free, Claude.ai free, and Gemini/NotebookLM are the only
truly frictionless, zero-verification options for a live session — use these with
**synthetic or de-identified vignettes only**. OpenEvidence and Doximity GPT are excellent
to feature and are free, but require pre-session identity verification. Have students set
up those accounts *before* class, not during it.

Related, worth citing but not usable as a student tool: a 2026 *JMIR Med Educ* RCT found an
ambient-scribe workflow improved written narrative feedback quality for medical students
without increasing instructor effort ([e89996](https://mededu.jmir.org/2026/1/e89996)).

### 1.6 Rubrics and checklists for evaluating LLM clinical outputs

- **PDSQI-9 (Provider Documentation Summarization Quality Instrument)** — developed with
  Epic collaboration to evaluate LLM-generated clinical summaries. Nine attributes: Cited,
  Accurate, Thorough, Useful, Organized, Comprehensible, Succinct, Synthesized,
  non-Stigmatizing (arXiv:2501.08977; AMIA presentation).
  **⚠ Preprint / conference-validated instrument, not a peer-reviewed journal publication**
  as far as could be determined. Still a clean, teachable 9-item rubric well suited to a
  40-student breakout.
- **Monaci et al. 2026** (§1.3) — complementary patient-communication rubric
  (comprehensibility, relevance, usability, emotional impact, empowerment).
- **McLaughlin et al. 2026** (§1.4) — the 0/1/2 citation-accuracy scale is trivially
  reusable as a scoring key.

### 1.7 Activities — Area 1

**Activity 1.A — "Naive vs. Engineered Prompt" diagnostic lab (45 min).**
Pre-assign 8–10 breakout rooms of 4–5. Post two synthetic clinical vignettes (faculty hold
an answer key) in chat or a shared doc. Students use their own free ChatGPT or Claude.ai
account, logged in before class.
*Run:* (1) 15 min — enter the vignette with no prompt engineering, just "what's the
diagnosis?", capture the output. (2) 15 min — re-run with a structured prompt: assign a
role, request differential plus supporting and opposing findings plus next diagnostic step,
in a specified format. (3) 10 min — group scores both outputs against the key.
*Produces:* a shared doc per group with both outputs side by side and a self-scored
comparison.
*Debrief (10 min plenary):* Why did prompt structure change the output? Reference Waldock
et al. (only 5% of students knew the term "clinical prompt engineering") and Goh et al.
(the LLM alone beat both the LLM-assisted and unassisted physicians). What does that imply
about *how* clinicians integrate these tools?

**Activity 1.B — Journal club jigsaw: critiquing the diagnostic-AI literature (40 min).**
*Pre-work:* four 1-page summaries distributed to four groups of ~10 (Goh 2024, Kanjee 2023,
the Tu/McDuff AMIE Nature 2025 pair, MAI-DxO).
*Run:* split each group into breakout pairs for 15 min, reconvene as expert groups for 10
min to build a 3-bullet critique.
*Produces:* a shared slide or chat post per group covering study design, population (real
patients vs vignettes vs curated hard cases), and one major limitation.
*Debrief (15 min):* seed with "MAI-DxO reports 85.5% accuracy vs 20% for physicians — why
is that comparison potentially misleading?" (unrealistic case mix, no healthy or mild
presentations, preprint status, benchmark rules restricting physician resources).

**Activity 1.C — Fabrication hunt: citation verification lab (40 min).**
*Setup:* 20 pairs. Each pair asks a free chatbot a clinical question and requests 5
references.
*Run:* demonstrate a PubMed search live first, then have pairs verify each citation and
score it 2 (accurate) / 1 (real but misrepresented) / 0 (fabricated) using the McLaughlin
scale. Compile into a shared spreadsheet.
*Produces:* a class-wide tally of fabrication rates by tool.
*Debrief:* compare the class's empirical rate to published rates — Gravel et al. (69%
fabricated), McGowan et al. (2 of 35 real), McLaughlin et al. (Claude 78% accurate, Gemini
26.2% fabrication, OpenEvidence 0%). Why do retrieval-augmented tools differ *structurally*
from general-purpose chatbots?

**Activity 1.D — Patient message and discharge-instruction rewrite (45 min).**
*Setup:* provide a synthetic patient-portal question and a synthetic discharge summary.
Breakout groups of 4–5.
*Run:* (1) draft an empathetic reply using a free LLM; (2) rewrite the discharge
instructions to a 6th-grade reading level, then check with a free Flesch-Kincaid tool;
(3) edit the AI output as if you were the attending signing off.
*Produces:* before/after text plus readability score, and a marked-up "what I changed and
why" annotation.
*Debrief:* Ayers et al. (chatbot responses rated more empathetic and higher quality but 4x
longer — what needs trimming?), Garcia et al. (drafts reduced burnout, not time — why might
that still be worth it?), Fereydooni and Monaci (readability isn't the whole picture — what
else matters?).

**Activity 1.E — Score it yourself: applying a clinical-AI rubric (40 min).**
*Setup:* introduce the PDSQI-9 attributes. Prepare two pre-written AI outputs, one strong
and one flawed on 2–3 axes (e.g. an AI-drafted discharge summary or inbox reply).
*Run:* breakout groups independently score both outputs on all 9 dimensions via a shared
form, then compare across groups.
*Produces:* completed rubric with a 1–2 sentence justification per low score.
*Debrief:* show the variance across groups on the *same* output. Discuss inter-rater
reliability and how a structured rubric changes decisions versus a gut "this looks fine."

**Activity 1.F — Free-tool bake-off (25 min, optional wrap-up).**
Each group runs the same clinical question through 2–3 tools (ChatGPT free, Claude free,
and — if pre-verified — OpenEvidence and/or Doximity GPT).
*Produces:* a one-slide comparison: which cited real sources, which had the best
differential, which was most concise.
*Debrief:* which tool would you trust for what task? Close with an explicit PHI reminder —
none of the consumer-tier tools are BAA-covered.

---

## Area 2 — Agentic coding / "vibe coding" for non-programmers

### 2.1 Origin, current meaning, failure modes

**Origin.** Coined by Andrej Karpathy in a tweet on **February 2, 2025**: "There's a new
kind of coding I call 'vibe coding', where you fully give in to the vibes, embrace
exponentials, and forget that the code even exists... I just see stuff, say stuff, run
stuff, and copy-paste stuff, and it mostly works."
[Karpathy tweet](https://x.com/karpathy/status/1886192184808149383?lang=en) ·
[1-year retrospective](https://x.com/karpathy/status/2019137879310836075) ·
[CodeRabbit semantic history](https://www.coderabbit.ai/blog/a-semantic-history-how-the-term-vibe-coding-went-from-a-tweet-to-prod)

**Word of the Year — verified.** Collins Dictionary named "vibe coding" its 2025 Word of
the Year, defining it as software development using AI prompted by natural language rather
than hand-written code.
[Collins WOTY](https://www.collinsdictionary.com/woty) ·
[Collins blog](https://blog.collinsdictionary.com/language-lovers/collins-word-of-the-year-2025-ai-meets-authenticity-as-society-shifts/) ·
[CNN](https://www.cnn.com/2025/11/06/tech/vibe-coding-collins-word-year-scli-intl)

**Where the term stands in mid-2026.** In February 2026 Karpathy declared vibe coding
"passé," proposing "agentic engineering" as the successor — orchestrating and overseeing
coding agents rather than blindly accepting output, with technical mastery becoming "even
more of a multiplier than before."
[The New Stack](https://thenewstack.io/vibe-coding-is-passe/) ·
[Forbes](https://www.forbes.com/sites/jodiecook/2026/06/12/is-vibe-coding-already-dead-even-karpathy-is-moving-on/)

**Documented failure modes:**

- **Security.** 40–62% of AI-generated code samples contain security vulnerabilities in
  benchmark testing; Java-specific testing found a 72% failure rate on security checks (the
  "70% problem"). 86% of samples failed to defend against XSS, 88% against log injection.
  Georgia Tech's "Vibe Security Radar" tracked 35 new CVEs traceable to AI-generated code in
  March 2026 alone, up from 6 in January 2026. A scan of 1,400+ vibe-coded production apps
  found 65% had security issues, 58% with at least one critical vulnerability.
  [IBM](https://www.ibm.com/think/insights/vibe-coding-security-risks) ·
  [OX Security](https://www.ox.security/blog/vibe-coding-security/) ·
  [Cloud Security Alliance](https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-generated-code-vulnerability-surge-2026/) ·
  [Forbes](https://www.forbes.com/sites/jodiecook/2026/03/20/vibe-coding-has-a-massive-security-problem/)
- **Non-reproducibility / drift.** The same prompt produces different code structures on
  different days because the model has no persistent memory of prior architectural
  decisions. [The Vibelog](https://thevibelog.dev/blog/vibe-coding-technical-debt-2026/)
- **Technical debt.** Reported 30–41% increase in technical debt after AI tool adoption,
  48% rise in code duplication, 60% drop in refactoring activity where teams don't read the
  diffs.
  [Salesforce Ben](https://www.salesforceben.com/2026-predictions-its-the-year-of-technical-debt-thanks-to-vibe-coding/) ·
  [Pixelmojo](https://www.pixelmojo.io/blogs/vibe-coding-technical-debt-crisis-2026-2027)
- **"Comprehension abdication"** — a term from the health-informatics literature (§2.3) for
  the specific hazard of a clinician-developer who cannot explain, anticipate failure modes
  in, or safely modify the code they've deployed.

This is a useful framing for the elective: what students will do in 60–90 minutes *is* real
vibe coding, with all of the above in play — which is exactly why the guardrails (§2.5)
matter more than the build itself.

> **⚠ Sourcing caveat for this subsection.** The security and technical-debt statistics come
> from vendor blogs, trade press, and security-firm marketing content rather than
> peer-reviewed work. The direction of the finding is well-corroborated; the specific
> percentages should be treated as illustrative, not precise.

### 2.2 Zero-setup tools ranked by friction

| Tool | Account/card | Browser-only | Free tier | Notes for 40 students on Zoom |
|---|---|---|---|---|
| **Claude.ai Artifacts** | Free account, no card | Yes | Artifact creation/editing/publishing included; must enable "Code execution and file creation" in Settings; rate-limited | **Lowest friction.** Single-page HTML/JS/React apps, SVGs, docs; no deploy step, instantly shareable via link. [pricing](https://claude.com/pricing) · [docs](https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them) |
| **Google AI Studio "Build mode" / Gemini Canvas** | Google account, no card | Yes | Interface always free; API use in a shipped product costs later | Full-stack apps, one-click Cloud Run deploy. Good fallback. [guide](https://www.nocode.mba/articles/free-google-app-builder-ai) · [Canvas](https://gemini.google/overview/canvas/) |
| **ChatGPT Canvas** | Free account, no card | Yes | Free on every tier, but free-tier limits tight (~10 msgs/5hr before model downgrade) | Viable, but rate limits could bite mid-session. [guide](https://pecollective.com/tools/chatgpt-free-tier-guide/) |
| **Bolt.new** | Free account, no card | Yes | 1M tokens/month, 300K/day, hosting included | Genuinely functional for one session. [FreeTier.co](https://freetier.co/directory/products/boltnew) |
| **Lovable** | Free account, no card | Yes | 5 credits/day (~30/month), up to 5 hosted projects | Enough for one build, tight if students iterate. [eesel AI](https://www.eesel.ai/blog/lovable-pricing) |
| **v0 by Vercel** | Free account | Yes | $5/month credits, **7-message daily cap** | Cap too tight for live iteration. [costbench](https://costbench.com/software/ai-coding-assistants/v0-vercel/) |
| **Replit Agent** | Free account | Yes | Starter: limited daily credits, older model, 1 published app, all public | Public-by-default is a PHI risk worth flagging. [source](https://www.wearefounders.uk/replit-pricing-what-you-actually-pay-to-build-apps/) |
| **Figma Make** | Figma account | Yes | Free Starter: 500 AI credits/month, capped at 2 editors / 3 files | Seat/file caps awkward for 40 builders. [comparedge](https://comparedge.com/tools/figma/pricing) |
| **Claude Code (CLI/desktop)** | Paid subscription or API credits | **No** — local install | No durable free tier | **Not viable for a zero-install cohort session.** Install plus terminal literacy would eat the whole budget. [pricing](https://www.nxcode.io/resources/news/claude-code-pricing-2026-free-api-costs-max-plan) |
| **GitHub Copilot (student)** | GitHub Education verification | No (needs IDE) | **New Copilot Student Plan sign-ups paused April 20, 2026**, no reopening date; only students verified before the pause keep free Pro access | **Do not plan around this for August 2026.** [GitHub Discussion #198236](https://github.com/orgs/community/discussions/198236) · [roboin.io](https://roboin.io/article/en/2026/04/21/github-copilot-sign-ups-suspended/) |

**Bottom line:** Claude.ai Artifacts and Google AI Studio / Gemini Canvas are the only two
options with no card, a durable free tier, true browser-only operation, no seat or file caps
that break at scale, and generation fast enough for a live 60–90 min build-and-share.
Bolt.new is a solid third. Everything requiring local install should be explicitly excluded
from the live session and offered only as an optional "if you want to go further" pointer.

### 2.3 Documented examples of clinicians building tools without being programmers

- **Moore JH & Tatonetti N.** *BioData Mining* (2025) — editorial on vibe coding
  "democratizing" biomedical informatics; recommends validation pipelines, HIPAA/FDA/EMA-
  aligned audit trails, and sandboxing as guardrails.
  [PMC12217882](https://pmc.ncbi.nlm.nih.gov/articles/PMC12217882/)
- **"How Can Clinicians Leverage Vibe Coding for Machine Learning and Deep Learning
  Research?"** — frames vibe coding as lowering the barrier for clinicians without Python
  skills. [PMC12602019](https://pmc.ncbi.nlm.nih.gov/articles/PMC12602019/)
- **"Vibe coding for clinicians: democratising bespoke software development for digital
  health innovation"** — arXiv preprint 2026, directly on-topic. Full text was not
  extractable (PDF binary); pull directly.
  [arxiv.org/pdf/2604.22604](https://arxiv.org/pdf/2604.22604) **⚠ citation not
  independently verified — confirm the arXiv ID resolves before use.**
- **Alqheedan & Alzughaibi, *Frontiers in AI* (2026), "The VIBE-HI framework"** — a
  governance model for evaluating vibe-coded health-informatics tools. Names "comprehension
  abdication" as the central hazard and proposes four-tier risk stratification
  (Green/Yellow/Orange/Red by PHI involvement, clinical-decision proximity, user autonomy,
  scale of impact) mapping to HIPAA / IEC 62304 / FDA SaMD / EU AI Act obligations.
  **The single most directly reusable framework for teaching guardrails here.**
  [Frontiers frai.2026.1882814](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2026.1882814/full)
  **⚠ verify this DOI resolves before assigning.**
- **JMIR Preprint #95998**, "Clinician-Led Artificial Intelligence Innovation: A Practical
  Guide to Building Custom Healthcare Applications Without Traditional Programming"
  (posted March 26, 2026). [preprints.jmir.org/preprint/95998](https://preprints.jmir.org/preprint/95998)
- **Medical education build-session precedent:** a 2026 study (*AI*, MDPI, 7(6)) describes a
  faculty member using Gemini to vibe-code a custom ECG-interpretation learning app for
  first-year medical students at one WWAMI site, evaluated against five control sites using
  the uMARS scale. Results on exam performance were **mixed and inconsistent across exams** —
  itself a useful teaching point about efficacy claims for hastily-built tools.
  [doi.org/10.3390/ai7060223](https://doi.org/10.3390/ai7060223) **⚠ verify DOI.**
- **Health-system adoption signal:** Children's Nebraska has stated a goal to train all
  clinicians in vibe coding by 2027.
  [DistilINFO](https://distilinfo.com/2026/05/27/clinicians-embrace-vibe-coding-revolution/)
- **Named physician-builder anecdotes** (not peer-reviewed): Dr. Tom Kelly (vascular
  surgeon, CEO of Heidi Health, contributes to production code); Dr. Rashad Usmani's
  "Primary AI" CDS tool; Dr. Josh Barron's "Claire" AI triage assistant.
  [Offcall](https://www.offcall.com/learn/articles/how-physicians-are-building-clinical-ai-tools)
- **Hackathon precedent for the format:** Harvard HSIL Hackathon (500+ teams, 19 global hubs
  in 2025), Georgetown H2AI (student-organized), Medi-Hacks — all demonstrate
  rapid-build-and-demo at student scale, though over days rather than 90 minutes.
  [HSIL 2026](https://hsph.harvard.edu/research/health-systems-innovation-lab/work/hsil-hackathon-2026-building-high-value-health-systems-leveraging-ai/) ·
  [Georgetown H2AI](https://meded.georgetown.edu/news-stories/medical-students-host-healthcare-hackathon-with-ai/)

### 2.4 What is realistically achievable in 60–90 minutes

Achievable for a novice on Claude.ai Artifacts or AI Studio: a **single-file, client-side,
no-login, no-database HTML/JS tool** — a calculator, a generator, a static-data
visualization, or a scripted chat flow. **Not** achievable: anything needing a real backend,
user accounts, persistent storage across sessions, or integration with real patient data.

Good candidate builds: clinical risk calculators (Wells, CHA₂DS₂-VASc, MELD), a
patient-education handout generator, a discharge-instruction reading-level simplifier, a
spaced-repetition flashcard tool, a rounding checklist, a static public-health data
dashboard, an OSCE practice chatbot with a fixed case script.

**Three starter prompts:**

1. **CHA₂DS₂-VASc calculator**
   > "Build a single-page web app that calculates the CHA₂DS₂-VASc score for stroke risk in
   > atrial fibrillation. Show each risk factor as a checkbox with its point value
   > (congestive heart failure=1, hypertension=1, age≥75=2, diabetes=1, prior
   > stroke/TIA/thromboembolism=2, vascular disease=1, age 65–74=1, sex category female=1).
   > Display the running total and a risk-category interpretation with approximate annual
   > stroke risk %. Add a prominent red banner: 'Educational prototype only — not validated
   > for clinical decision-making, contains no PHI storage.' Cite the original score
   > methodology in a footnote so I can independently verify every point value against
   > MDCalc before I trust the output."

2. **Discharge-instruction plain-language translator**
   > "Build a tool with a text box where I can paste a block of generic (de-identified, no
   > real patient data) discharge instructions, and a dropdown for target reading level (6th
   > grade / 8th grade) and language (English/Spanish). On submit, show a simplified version
   > side-by-side with the original, plus a checklist confirming no medication doses were
   > altered from the original text. Add a warning banner that a licensed clinician must
   > review every output before it reaches a real patient."

3. **OSCE practice chatbot**
   > "Build a single-page chat interface simulating a standardized patient with [chief
   > complaint: chest pain, scripted case: musculoskeletal chest pain, not ACS]. The
   > 'patient' should only reveal history when asked relevant questions, refuse to volunteer
   > the diagnosis, and give realistic vague answers to vague questions. Include a hidden
   > 'answer key' panel I can toggle to check my differential and questioning technique
   > afterward. This is a role-play chatbot for practice, not a real patient — do not let it
   > dispense actual medical advice if asked out-of-scope questions."

Each prompt deliberately embeds a guardrail instruction. That doubles as the teaching
moment: **the prompt itself is where "toy, not device" framing gets baked in.**

### 2.5 Guardrails to teach

1. **No PHI, ever, in a consumer AI prompt.** Free and consumer tiers of Claude.ai, ChatGPT,
   and Gemini carry no Business Associate Agreement; entering PHI is a potential HIPAA
   breach regardless of intent. Use only fictional or de-identified data in every session
   prompt. [HIPAA Vault](https://www.hipaavault.com/resources/is-claude-hipaa-compliant/)
2. **These are toys, not medical devices.** FDA's CDS guidance defines criteria for software
   to qualify as non-device CDS — notably that it must not use signals or images, and the
   clinician must be able to independently review the basis for any recommendation. A
   homemade calculator that gives a bare score with no visible rationale, or one intended
   for real patients, risks crossing into regulated SaMD territory. "I vibe-coded a Wells
   score calculator" is fine as a personal study aid; deploying it clinically is a different
   regulatory category. **Note the CDS guidance was revised January 6, 2026 — see §5.1.**
   [FDA CDS FAQ](https://www.fda.gov/medical-devices/software-medical-device-samd/clinical-decision-support-software-frequently-asked-questions-faqs)
3. **Verification — never trust generated clinical logic.** Independently confirm every
   scoring rule, cutoff, and unit conversion against a validated source (e.g. MDCalc) before
   treating output as correct. Research groups have built entire projects around wrapping
   verifiable calculator implementations precisely because LLMs hallucinate clinical math.
   [arXiv 2503.17550](https://arxiv.org/pdf/2503.17550)
4. **"Comprehension abdication" is the named failure mode to avoid.** Per VIBE-HI: if a
   student cannot explain what their own generated code does, they cannot anticipate its
   failure modes. Teaching rule: before demoing, the student must state in plain language
   what happens for each input, including edge cases (all boxes unchecked, nonsensical
   combinations).
5. **Licensing and liability.** A tool built by a medical student carries no institutional
   review, no clinical validation, and no malpractice coverage. Framing every artifact with
   an explicit on-screen disclaimer is both ethical practice and a template for the
   professional habit of labelling AI-assisted output.
6. **Security by default.** Given the vulnerability rates in §2.1, and that these are
   throwaway single-session artifacts, the operative guardrail is not "harden your app"
   (out of scope) but **"never put real credentials, real patient identifiers, or anything
   sensitive into a vibe-coded artifact, because you are not going to security-review it."**

### 2.6 Session designs — Area 2

**Design 2.A — "First Build" (75 min, single calculator, Claude Artifacts).**
- 0–10: frame vibe coding (Karpathy origin, Collins WOTY, "toy not device," PHI rule). 3 slides max.
- 10–15: live demo — instructor builds a Wells' Criteria (PE) calculator on shared screen, narrating what to check in the output.
- 15–55: students build their own calculator from a menu (Wells, CHA₂DS₂-VASc, MELD, qSOFA) using the §2.4 pattern prompt, iterating with follow-ups ("add a reference citation," "fix the rounding," "color-code by risk tier").
- 55–70: **verification exercise** — each student cross-checks their tool against MDCalc or the original publication for 2 test cases; report discrepancies in chat.
- 70–75: rapid showcase — 5–6 volunteers share screen, 1 min each, showing their calculator and one thing they'd fix before trusting it.
- *Deliverable:* a shareable Artifact link per student posted to a shared doc with the verification note attached.

**Design 2.B — "Patient-Facing Content Generator" (90 min).**
- 0–10: framing and guardrails, emphasis on PHI and health-literacy stakes.
- 10–20: instructor demo builds the discharge-instruction simplifier (§2.4 prompt 2) live, showing iterative refinement (add Spanish, add a "flag if dosage changed" checker).
- 20–70: students build a patient-education artifact of their choice using only fictional sample text they write themselves. Encourage 2–3 rounds of "critique your own output like a health-literacy expert would."
- 70–85: peer review in breakout pairs — each student runs their partner's tool with new fictional input and flags anything medically wrong or confusing.
- 85–90: debrief — what would it take to deploy this responsibly (IRB, clinical review, FDA CDS analysis)?

**Design 2.C — "OSCE Practice Bot Sprint" (75 min).**
- 0–10: framing, plus a caution about chatbots emulating patients — flag that the LLM-roleplay pattern is exactly how PHI leaks if someone reuses the same window for real charting.
- 10–20: instructor demo builds a scripted standardized-patient chatbot (§2.4 prompt 3).
- 20–60: students each build a chatbot for a different assigned chief complaint, iterating on the hidden answer key and realism.
- 60–70: students test each other's bots in breakout rooms — one interviews, one watches for realism and scripting failures.
- 70–75: two volunteers do a 90-second live OSCE interview against a classmate's bot for the whole group.
- *Deliverable:* an artifact link per case, aggregated into a class-shared "OSCE practice bank."

**Design 2.D — "Data Story" (60 min, lower-energy slot, good as a Week 1 warm-up).**
- 0–5: abbreviated framing.
- 5–15: instructor demo — paste a small CDC/WHO public dataset snippet, ask for an interactive chart plus a one-paragraph narrative.
- 15–45: students pick from 3–4 **pre-vetted** small CSV/JSON snippets (pre-vetting avoids data-hunting eating the session) and build a visualization plus narrative.
- 45–55: popcorn share — everyone drops their link in chat; instructor spotlights 3–4.
- 55–60: close on "what would you need to verify before citing this chart in a real presentation?"

**Cross-cutting logistics:** confirm in advance that all 40 students have created free
Claude.ai or Google accounts *before* the session — account creation alone can eat 10+
minutes. Pin the guardrail rules (no PHI, toy-not-device, verify before trusting) as a
persistent Zoom chat message throughout the build window.

---

## Area 3 — Environmental impact of AI

### 3.1 Data center electricity demand

**IEA, "Energy and AI" (April 2025)**
- Global data center electricity demand projected to **more than double to ~945 TWh by
  2030** (roughly Japan's current total consumption), about **just under 3% of global
  electricity**.
- AI-optimized data centers specifically **triple** consumption 2025→2030.
- US and China account for **~80% of global data center growth to 2030**: US +~240 TWh
  (+130%), China +~175 TWh (+170%).
- IEA follow-up: data center electricity use **surged 17% in 2025**, more than 5x faster
  than overall global electricity demand growth (3%), amid >$400B in AI infrastructure
  spending.
- [IEA Energy and AI](https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai) ·
  [IEA 2025 surge](https://www.iea.org/news/data-centre-electricity-use-surged-in-2025-even-with-tightening-bottlenecks-driving-a-scramble-for-solutions) ·
  [S&P Global](https://www.spglobal.com/energy/en/news-research/latest-news/electric-power/041025-global-data-center-power-demand-to-double-by-2030-on-ai-surge-iea)

**LBNL, "2024 United States Data Center Energy Usage Report" (Dec 2024)**
- **Confirmed:** US data centers used **176 TWh in 2023 = 4.4% of total US electricity**.
- Growth accelerated from ~7%/yr (2014–2018) to ~18%/yr (2018–2023).
- 2028 projection: **325–580 TWh**, framed by LBNL as **6.7%–12% of total US electricity by
  2028**.
- [LBNL PDF](https://eta-publications.lbl.gov/sites/default/files/2024-12/lbnl-2024-united-states-data-center-energy-usage-report_1.pdf) ·
  [DOE/LBNL release](https://newscenter.lbl.gov/2025/01/15/berkeley-lab-report-evaluates-increase-in-electricity-demand-from-data-centers/)

**EPRI ("Powering Intelligence," 2024–2026)**
- 2024 US consumption estimated at **177–192 TWh** (~4% of 2023 load), consistent with LBNL.
- More aggressive projection: **9–17% of US electricity by 2030**, possibly **380–790 TWh**.
- **⚠ CONFLICTING with LBNL.** Flag for students that estimates vary substantially by
  methodology and AI-adoption assumptions. Present as a range, not a number.
- AI workloads currently ~15–25% of data center electricity, share rising.
- [EPRI 2026](https://powering-intelligence.epri.com/load-growth.html) ·
  [EPRI release](https://www.epri.com/about/media-resources/press-release/q5vU86fr8TKxATfX8IHf1U48Vw4r1DZF)

### 3.2 Per-query inference energy — precision matters

| Source | Figure | Status |
|---|---|---|
| **Google, "Measuring the environmental impact of delivering AI at Google Scale"** (Aug 21, 2025) | Median Gemini Apps text prompt: **0.24 Wh, 0.03 gCO2e, 0.26 mL water** (~5 drops) | Technical paper, [arXiv 2508.15734](https://arxiv.org/abs/2508.15734); full-stack methodology (chip power, host CPU/RAM, idle capacity, PUE). Google reports a **33x energy / 44x carbon reduction per prompt over 12 months** |
| **Sam Altman, "The Gentle Singularity"** (June 2025) | Average ChatGPT query: **0.34 Wh, ~0.32 mL water** | **⚠ Not peer-reviewed, no methodology disclosed**, unclear what "average" excludes (possibly reasoning/deep-research queries). Treat as a claim, not a measurement |
| **Epoch AI (2025)** | Convergent ~**0.3 Wh** per standard text query; per-output-token empirical range **0.0001–0.002 Wh** | Independent, transparent methodology; challenges the older viral "~3 Wh" figure as likely an overestimate |
| **MIT Technology Review, "We did the math"** (May 2025) | Llama 3.1 8B ~57 J (114 J with cooling); Llama 3.1 405B ~3,353 J (6,706 J with cooling) ≈ a microwave for ~8 seconds | Independently measured across open models; shows a ~60x spread by model size |
| **"How Hungry is AI?"** (Jegham et al., [arXiv 2505.09598](https://arxiv.org/abs/2505.09598)) | Most energy-intensive proprietary models exceed **29 Wh per long prompt** — >65x the most efficient | Infrastructure-aware benchmarking across 30 commercial models |

**Why estimates vary:** model size (dense vs MoE, parameter count), output length and
reasoning tokens, batching efficiency, hardware generation, datacenter PUE, whether idle
capacity and cooling overhead are counted, and whether training is amortized into the
per-query figure. **This is the single most useful teaching point — "per query energy" is
not one number.**

**The "10x a Google search" claim — origin and problems.** Traces to **Alex de Vries, "The
growing energy footprint of artificial intelligence," *Joule*, Oct 2023**
([ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2542435123003653)),
which estimated that if all Google searches used an LLM-scale model it would require ~29.2
TWh/yr (≈ Ireland's annual consumption). The "10x" framing widely repeated in media relies
on comparing this to a **2009 Google blog post figure for search energy (~0.3 Wh/search)** —
not a contemporary audited number for either side. It also assumes 100% chip utilization
and ignores subsequent hardware and model efficiency gains. Energy economist Jonathan Koomey
has flagged this style of extrapolation-from-anecdote as prone to overestimation. Good
worked example of a bad statistic.
[technical.ly explainer](https://technical.ly/civics/chatgpt-vs-google-energy-use/)

### 3.3 Training footprint

- **GPT-3** (Patterson et al. 2021, [arXiv 2104.10350](https://arxiv.org/pdf/2104.10350)):
  **confirmed — 1,287 MWh, 552 tCO2e.**
- **BLOOM 176B** (Luccioni et al., JMLR;
  [arXiv 2211.02001](https://arxiv.org/abs/2211.02001)): 433,195 kWh over 1.08M A100
  GPU-hours; **24.7 tCO2e** dynamic power, **50.5 tCO2e** including embodied carbon.
- **Llama 3.1** (verified directly from
  [Meta's model card](https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md)):
  8B — 1.022 GWh, 420 tCO2e; 70B — 4.9 GWh, 2,040 tCO2e; 405B — 21.588 GWh, **8,930 tCO2e**.
  Total **27.51 GWh, 11,390 tCO2e location-based; 0 tCO2e market-based** (100%
  renewable-matched via PPAs). **The location-based vs market-based gap is an excellent
  teaching point on carbon accounting.**
- **Luccioni, Jernite, Strubell — "Power Hungry Processing"** (FAccT 2024,
  [ACM](https://dl.acm.org/doi/10.1145/3630106.3658542) /
  [arXiv](https://arxiv.org/abs/2311.16863)): first systematic inference-cost comparison
  across task types. **Multi-purpose generative models are orders of magnitude more
  energy-costly per task than fine-tuned task-specific models**, even controlling for
  parameter count; at scale, **cumulative inference cost can rival or exceed one-time
  training cost.**
- **⚠ DATA GAP, not merely unverified:** no comparable disclosed training-energy figures
  were found for GPT-4, Gemini, or Claude-generation frontier models. Labs have largely
  stopped publishing Patterson/Luccioni-style training carbon numbers for their largest
  models. This is itself worth teaching as a transparency problem.

### 3.4 Water

- **Li et al., "Making AI Less Thirsty"**
  ([arXiv 2304.03271](https://arxiv.org/abs/2304.03271), updated through Jan 2025; also in
  *Communications of the ACM*): training GPT-3-scale models in Microsoft's US datacenters
  can **directly evaporate ~700,000 liters** of freshwater. Global AI water withdrawal
  projected at **4.2–6.6 billion m³ in 2027** (more than Denmark's total annual withdrawal).
- **Microsoft:** 25% reduction in water-use intensity by 2025, targeting 40% by 2030; claims
  a water-positive milestone in FY2025 (~14.2M m³ replenished). Newest AI datacenters
  reportedly use no water for cooling in normal operation. **⚠ Microsoft changed its
  water-accounting methodology between the FY24 and FY25 reports, limiting year-over-year
  comparability.**
  [2025 Sustainability Report](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/2025-Microsoft-Environmental-Sustainability-Report.pdf)
- **Google (2025 report, covering 2024):** total water consumption ~**8.1 billion gallons**;
  data-center-specific consumption rose from **4.3B gallons (2021) to 6.1B gallons (2024)**;
  72% of freshwater withdrawal from low-risk sources; replenishment covered ~64% of
  freshwater consumption, targeting 120% by 2030.
  [Google Sustainability](https://sustainability.google/operations/)
- **US-wide:** data centers directly consumed **17.4 billion gallons (~66 billion litres) in
  2023**, projected to **38–73 billion gallons by 2028**, plus roughly 800 billion litres
  indirectly via power-plant cooling.
  [MOST Policy Initiative](https://mostpolicyinitiative.org/science-note/data-center-water-use/)
- **Equity / siting angle:** two-thirds of data centers built or planned since 2022 sit in
  water-stressed regions (southern Arizona, Colorado River Basin, Texas, drought-affected
  Southeast). A Newton County, GA facility uses **500,000 gal/day (~10% of the entire
  county's water use)**; unauthorized withdrawals by developers in Arizona and Georgia in
  2026 triggered regulatory action after residents reported dropped water pressure.
  [Fortune](https://fortune.com/2026/05/13/data-center-georgia-arizona-water-wars/) ·
  [Ceres, "Drained by Data"](https://www.ceres.org/resources/reports/drained-by-data-the-cumulative-impact-of-data-centers-on-regional-water-stress)

### 3.5 Efficiency gains vs Jevons paradox

- **Google:** total GHG emissions **up 48% since 2019** (2023: 14.3 million tCO2e), driven
  largely by data center electricity plus Scope 3, jeopardizing its 2030 halve-emissions
  target.
  [Earth.org](https://earth.org/google-emissions-grow-48-in-five-years-owing-to-large-scale-ai-deployment-jeopardizing-companys-net-zero-plans/) ·
  [NPR](https://www.npr.org/2024/07/12/g-s1-9545/ai-brings-soaring-emissions-for-google-and-microsoft-a-major-contributor-to-climate-change)
- **Microsoft — ⚠ CONFLICTING / evolving figure. Report the trend, not one number:**
  - 2024 report (FY2023 vs 2020 baseline): total emissions **up 29.1% since 2020**.
  - 2025 report (FY2024 vs 2020 baseline): **up 23.4%** (Scope 1+2 down ~29.9%; Scope 3 —
    dominated by datacenter construction materials — up ~30.9% and 97% of total footprint).
  - Stand.earth's independent analysis of Microsoft's 2026 report claims an **80% increase
    since 2020**, using a scope that includes gas-plant buildout Microsoft's own report
    excludes. **A methodology dispute — excellent discussion prompt.**
    [Stand.earth](https://stand.earth/press-releases/microsofts-sustainability-report-discloses-80-emissions-increase-since-2020-reveals-energy-demand-rivaling-denmark-leaves-out-massive-new-fossil-gas-buildout-that-will-double-companys-pol/)
- **The Jevons point:** Google's 33x/44x per-prompt reduction in one year is real, yet total
  emissions still rose. Per-unit efficiency gains outpaced by volume growth.
- **xAI Memphis/Colossus:** xAI ran **30+ unpermitted gas turbines** (later ~59 across
  Colossus 1 & 2, ~500 MW) without Clean Air Act permits in South Memphis — an area already
  rated "F" for ozone by the American Lung Association, with cancer risk ~4x the national
  average. NAACP and Earthjustice/SELC sued. Potential emissions **>1,700 tons NOx/yr, ~180
  tons PM/yr, ~500 tons CO/yr, ~19 tons formaldehyde/yr**. A clean environmental-justice case
  that maps onto healthcare siting/equity discussions.
  [CNBC](https://www.cnbc.com/2026/04/14/elon-musk-xai-memphis-data-centers.html) ·
  [Earthjustice](https://earthjustice.org/case/xai-illegal-gas-power-plant-data-center-colossus)
- **Nuclear/PPA response:** by 2026, Microsoft, Google, Amazon, and Meta collectively signed
  **13+ nuclear deals totalling ~10 GW**, including Microsoft's 20-year, $16B deal to restart
  **Three Mile Island** with Constellation (targeting ~2027–28), Google's SMR deal with
  Kairos Power, Amazon's $500M in X-energy, and Meta's 1.1 GW deal with Clinton Clean Energy
  Center.

### 3.6 Healthcare-specific angle

- **US healthcare's own footprint — PubMed-verified.** Eckelman MJ, Huang K, Lagasse R,
  Senay E, Dubrow R, Sherman JD. "Health Care Pollution and Public Health Damage in the
  United States: An Update." *Health Affairs* 2020;39(12):2071–2079.
  [DOI](https://doi.org/10.1377/hlthaff.2020.01247).
  US healthcare GHG emissions rose 6% from 2010–2018, reaching **1,692 kg CO2e per capita in
  2018 (highest among industrialized nations)**; associated pollution caused **388,000 lost
  DALYs** that year. (This is the update to the earlier ~8.5%-of-US-emissions estimate from
  the same group.)
- **Planetary Health Report Card** — student-led, founded 2019, published in *Lancet
  Planetary Health* 2022; evaluates medical schools across curriculum, research, community
  outreach, student support, and campus sustainability.
  [Lancet Planetary Health](https://www.thelancet.com/journals/lanplh/article/PIIS2542-5196(22)00045-6/fulltext)
- **AAMC/AMA:** a 2022 AAMC survey found **55% of US medical schools** included
  climate-health effects in required coursework, more than double the 2019 rate. AMA policy
  calls for climate-health integration; no LCME accreditation mandate yet.
- **AI-specific healthcare environmental papers (peer-reviewed, good assigned reading):**
  - Sherman JD et al., "The Urgency of Environmentally Sustainable and Socially Just
    Deployment of Artificial Intelligence in Health Care," *NEJM Catalyst*,
    [DOI 10.1056/CAT.24.0501](https://catalyst.nejm.org/doi/full/10.1056/CAT.24.0501)
  - "Sustainability of large-scale artificial intelligence models in health care," *Lancet
    Digital Health* (2026) — cites Llama 3.1 405B's 8,930 tCO2e figure (cross-validates the
    Meta model card above) and a Querétaro, Mexico datacenter case using ~15 billion
    litres/year (~13% of metro water use).
    [Lancet Digital Health](https://www.thelancet.com/journals/landig/article/PIIS2589-7500(26)00039-7/fulltext)
  - "Sustainable AI in medicine: balancing benefits and environmental costs," *Nature Reviews
    Nephrology* (2026). [Nature](https://www.nature.com/articles/s41581-026-01047-3)
  - Green radiology: *Japanese Journal of Radiology* (2026),
    [DOI 10.1007/s11604-026-02043-0](https://doi.org/10.1007/s11604-026-02043-0); ASNR-ESNR
    White Paper on Sustainability in Neuroradiology, *AJNR* 47(7):1771–1775,
    [DOI 10.3174/ajnr.A9238](https://doi.org/10.3174/ajnr.A9238). Both directly relevant to
    fourth-years.
  - "Green artificial intelligence in health applications," systematic review, *Artificial
    Intelligence in Medicine* (2026),
    [DOI 10.1016/j.artmed.2026.103442](https://doi.org/10.1016/j.artmed.2026.103442) —
    argues AI can *both* add footprint and reduce it (optimized scheduling, reduced
    low-value imaging, telemedicine).
- **⚠ UNVERIFIED — handle carefully:** a frequently-circulated claim that "autonomous AI
  could reduce healthcare GHG emissions by ~80%" traces to a narrow paper on autonomous
  diabetic retinopathy screening replacing in-person specialist visits. It is a
  **specific-use-case** estimate, not a general claim about AI in healthcare, and should not
  be presented without that caveat.
  [PMC9098499](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9098499/)

### 3.7 Teaching resources

- **MIT Technology Review, "We did the math on AI's energy footprint"** (May 20, 2025,
  O'Donnell & Crownhart) — the flagship explainer package.
  [Main piece](https://www.technologyreview.com/2025/05/20/1116327/ai-energy-usage-climate-footprint-big-tech/) ·
  [Three takeaways](https://www.technologyreview.com/2025/05/22/1117277/ai-energy-three-takeaways/) ·
  [Big-picture follow-up (Nov 2025)](https://www.technologyreview.com/2025/11/06/1127579/ai-footprint/)
- **MIT News**, "Responding to the climate impact of generative AI" (Sept 2025).
  [link](https://news.mit.edu/2025/responding-to-generative-ai-climate-impact-0930)
- **Hugging Face AI Energy Score** — public leaderboard rating ~166 models across 10 tasks
  on a 1–5 star scale using standardized H100 benchmarks.
  [Leaderboard](https://huggingface.co/spaces/AIEnergyScore/Leaderboard)
- **ML CO2 Impact calculator** — estimates training-run footprint from GPU type/hours/region.
  [docs](https://huggingface.co/docs/hub/en/model-cards-co2)
- **Electricity Maps** (app.electricitymaps.com) — live grid carbon intensity by region;
  shows why *where* a model runs matters as much as *how efficiently*.
- **Hannah Ritchie (Our World in Data)** — reader-friendly, frequently updated, good
  pre-reading.
  [AI footprint, Aug 2025](https://hannahritchie.substack.com/p/ai-footprint-august-2025)

### 3.8 Activities — Area 3

**Activity 3.A — "What did this elective cost the planet?" (25 min, estimation then reveal).**
Before revealing any sources, each breakout group (5–6 students) estimates from intuition
how much energy the class itself used querying ChatGPT/Gemini over 4 weeks, assuming
**~40 students × ~15 queries/week × 4 weeks = 2,400 queries**.
Then reveal, using real sourced figures:
- Google's Gemini median (0.24 Wh) → **576 Wh (~0.58 kWh)**
- Altman's ChatGPT figure (0.34 Wh) → **816 Wh (~0.82 kWh)**
- "How Hungry is AI?" long-prompt high end (29 Wh) → **69.6 kWh**

Anchor concretely: 0.58–0.82 kWh ≈ a microwave for a few minutes, or ~10 laptop charges;
69.6 kWh ≈ several days of an average US household's electricity.
Water parallel at Google's 0.26 mL/prompt: 2,400 prompts ≈ **624 mL (~2.6 cups)**.
*The ~120x spread between low and high scenarios is the lesson* — model choice, prompt
length, and reasoning mode change the footprint far more than most students will guess. The
trivially small individual/class scale sets up the scale question in Activity 3.B.

**Activity 3.B — Structured debate: "Should our hospital restrict clinical AI use on
environmental grounds?" (30–35 min).**
Two sides, assigned by breakout room, each given a sourced numbers packet.
*Pro-restriction:* Google's and Microsoft's rising **total** emissions (+48% since 2019 /
+23–29% since 2020) despite efficiency gains (Jevons); the xAI Memphis case as a worst-case
governance failure; data-center siting in water-stressed regions as an environmental-justice
issue directly analogous to healthcare's own siting problems.
*Pro-AI-use:* US healthcare's own baseline (Eckelman/Sherman — 1,692 kg CO2e per capita) —
AI use is a rounding error next to imaging, pharma supply chains, and building energy;
documented efficiency gains (33x/44x in one year); use-case evidence that AI can *cut*
healthcare emissions (the *AI in Medicine* 2026 review, the green radiology papers).
*Debrief:* both sides are using real numbers — the disagreement is about **scale and
counterfactual**, not facts. Good moment to introduce Scope 1/2/3 and location-based vs
market-based accounting, using Llama 3.1's 11,390 tCO2e location-based vs 0 tCO2e
market-based as the clean illustration.

**Activity 3.C — Draft a hospital AI-procurement sustainability memo (30 min).**
Groups draft a one-page bulleted memo a CMIO could actually use when evaluating a clinical
AI vendor. Toolkit to cite: Hugging Face AI Energy Score and the ML CO2 calculator as
vendor-comparison tools; the location-based vs market-based distinction (ask vendors which
they report); water-stress siting questions (where is inference hosted?); and the anchoring
point that since healthcare is already a large emissions sector, AI procurement is one lever
among many, not the dominant one. Each group reports its top 3 policy asks in plenary (5 min).

**Activity 3.D — "Rank the models" (15–20 min, optional).**
Facilitator-driven shared-screen exploration of the
[Hugging Face AI Energy Score Leaderboard](https://huggingface.co/spaces/AIEnergyScore/Leaderboard),
comparing star ratings across familiar models and tasks (text vs image generation),
side-by-side with [Electricity Maps](https://app.electricitymaps.com) showing grid carbon
intensity by region.
*Prompt:* "If your health system's AI vendor could choose *where* to run inference, how much
would that matter versus which model they choose?" — reinforces that model efficiency and
grid carbon intensity are independent levers.

### 3.9 Flagged items — Area 3

- EPRI's 9–17%-by-2030 vs LBNL's 6.7–12%-by-2028 — genuinely conflicting; present as a range
  with a methodology caveat.
- Microsoft's emissions increase: **29.1% (2024 report) vs 23.4% (2025 report) vs 80%
  (Stand.earth, differently scoped)** — present all three with scope, don't collapse.
- Altman's 0.34 Wh figure: not peer-reviewed, no methodology, ambiguous "average query."
- "Autonomous AI could reduce healthcare emissions by ~80%": one narrow use-case study, not
  a general finding.
- No disclosed training energy/carbon for GPT-4, Gemini, or Claude-generation models — a
  genuine transparency gap.

---

## Area 4 — Social and economic impacts

### 4.1 Physician workforce: the Hinton prediction and what happened

**The prediction.** At a 2016 Creative Destruction Lab talk, Geoffrey Hinton said: *"People
should stop training radiologists now. It's just completely obvious within five years deep
learning is going to do better than radiologists… we've got plenty of radiologists already."*
He compared radiologists to "the coyote that's already over the edge of the cliff but hasn't
yet looked down."

**Hinton's 2026 walk-back.** In a **May 14, 2026 NYT feature** (Steve Lohr; accessed via
secondary reporting, original paywalled), Hinton acknowledged he "spoke too broadly," said
he'd meant only narrow image analysis, and now predicts the job becomes "a combination of AI
and a radiologist" making radiologists "a whole lot more efficient" — wrong on mechanism,
not merely on timing.
[Radiology Business](https://radiologybusiness.com/topics/artificial-intelligence/ny-times-revisits-nobel-prize-winners-prediction-ai-will-render-radiologists-obsolete) ·
[AuntMinnie](https://www.auntminnie.com/imaging-informatics/artificial-intelligence/article/15746014/hinton-acknowledges-mistake-in-predicting-ai-replacement-of-radiologists)

**Match data (NRMP):**

| Year | Radiology positions offered | Fill rate | Applicants |
|---|---|---|---|
| 2025 | 1,451 (+5.2% YoY) | 97.4% | 1,759 (−6.4% YoY) |
| 2026 | 1,478 (record high) | ~98.4% diagnostic | 1,741 (−1% YoY; −14% from 2023 peak) |

Positions have hit a record high every cycle while the applicant pool softened for two
straight years post-2023 peak, with fill rates near-full. The opposite of a specialty being
automated into oversupply.
**⚠ Exact 2024 fill-rate and precise 2026 position counts came from secondary reporting, not
a directly-pulled NRMP table — confirm against the primary source for slide-grade precision.**
[NRMP 2026 PDF](https://www.nrmp.org/wp-content/uploads/2026/05/Main_Match_Results_and_Data-2026.pdf) ·
[Match Day 2026 coverage](https://radiologybusiness.com/topics/healthcare-management/healthcare-staffing/match-day-2026-radiology-programs-offer-more-positions-ever-applicant-pool-declines)

**ACR / workforce data.** >1,400 physician openings currently posted on the ACR Career
Center ([ACR Bulletin 2026](https://www.acr.org/Clinical-Resources/Publications-and-Research/ACR-Bulletin/2026/radiologist-shortage-work-force-update)).
Attrition roughly doubled 2014→2022 (1.1%→2.5%/yr), worse for subspecialists, nonacademic,
female, and rural radiologists. ACR/Neiman HPI projects the workforce **20.9% larger by
2055** while imaging demand grows **17–27%** — demand tracking or outpacing supply. Pediatric
radiology is a genuine soft spot: 2,190→2,032 pediatric radiologists (2016–2023),
6.4%→4.6% of the workforce.

**Salary.** Doximity 2025: full-time diagnostic radiologist average **$571,749**, up 7.5%
YoY, roughly double the average specialty raise. Deena Mousa cites a different
figure/methodology ($520,000, "48% higher than 2015") — **directionally consistent but not
numerically reconcilable; do not merge the two.**
[The Imaging Wire](https://theimagingwire.com/2026/04/15/radiologist-salaries-grew-9-in-2025/)

**Official society position.** Multi-society statement (ACR, CAR, ESR, RANZCR, RSNA): "for
almost all AI models with current regulatory approval, the model inference serves to augment,
not replace, the radiologists' interpretations."
[Radiology: AI, RSNA](https://pubs.rsna.org/doi/full/10.1148/ryai.230513).
Langlotz's canonical line: "AI won't replace radiologists, but radiologists who use AI will
replace those who don't."

**Why radiologists weren't replaced — Deena Mousa, "AI isn't replacing radiologists"**
(Works in Progress / Understanding AI, Sept 2025;
[fetched directly](https://www.understandingai.org/p/ai-isnt-replacing-radiologists); the
worksinprogress.co URL 404'd,
[mirror](https://www.worksinprogress.news/p/why-ai-isnt-replacing-radiologists)):

- 700+ FDA-cleared radiology AI models exist (~75% of all FDA-cleared medical AI devices),
  yet none has meaningfully displaced radiologist labor.
- Models generalize poorly outside their training hospital (up to 20-point performance
  drops); **38% of 2024-cleared models were validated on a single hospital's data only.**
- Cleared models cluster on flashy conditions (stroke, breast/lung cancer ≈ 60% of
  clearances) that aren't the bulk of actual case volume.
- Radiologists spend only **~36% of their time on image interpretation** — the rest is
  protocolling, consultation, critical-result communication, procedures, teaching.
- Historical precedent: mammography CAD (FDA-approved 1998, Medicare-reimbursed 2001)
  reached 74% adoption by 2010, but a 430,000-mammogram study found it **increased biopsies
  20% with no gain in cancer detection**; Medicare pulled extra CAD reimbursement in 2018.
- Automation bias: a cited study found clinicians using computer prompts correctly identified
  only 50% of malignancies vs 68% unprompted, and were 26% more likely to follow a wrong AI
  call.
- Malpractice and regulatory structure entrench human-in-the-loop: many malpractice insurers
  exclude autonomous-AI-diagnosis coverage; FDA draws a hard assistive-vs-autonomous line and
  very few autonomous tools exist (IDx-DR for diabetic retinopathy is a rare example).
- **Jevons paradox again:** imaging demand growth (aging population, more sensitive
  protocols, defensive medicine) outpaced whatever productivity gains AI delivered.

Corroborating press: [The New Republic](https://newrepublic.com/article/187203/ai-radiology-geoffrey-hinton-nobel-prediction) ·
[Fortune, May 2026](https://fortune.com/2026/05/04/godfather-of-ai-geoffrey-hinton-radiologists-future-of-work-tech-ai-job-anxiety/)
(Mayo Rochester radiology staff up 55% since 2016) ·
[Forbes, Jan 2026](https://www.forbes.com/sites/jonmarkman/2026/01/26/the-radiologist-effect-why-ai-creates-more-jobs-not-fewer/).
No distinct Economist or STAT piece on this specific theme was located — recorded as **not
found** rather than invented.

**Pathology.**
- FDA clearances: **Paige.AI FullFocus** — first 510(k) clearance (2020) for a
  digital-pathology viewer for primary diagnosis; **Paige Prostate** — De Novo authorization
  (2021) for cancer-focus flagging in prostate biopsies. Roche's high-volume slide scanner
  cleared ~Jan 2025.
- Workforce: pathology residency positions **decreased** by 6 YoY in the 2025 Match
  (contrast with radiology's expansion). Anatomic/clinical pathology ranked #1 anticipated
  physician shortage in Axuall's 2025 report; a CAP-linked study claims the pathologist
  workforce is undercounted by nearly 40%.
  [CAP Newsroom](https://newsroom.cap.org/advocacy/new-study-reveals-pathologists-workforce-undercounted-by-nearly-40-/s/fa95b8fc-267e-44ef-83be-0816f630f2f0)
- **⚠ Gap:** national whole-slide-imaging adoption-rate statistics (% of US labs) were **not
  found as a verified figure**; only workflow-level claims from a single unconfirmed source.
- Framing is identical to radiology: AI arriving into a *shrinking* workforce as
  shortage-mitigation, not replacement.

**Primary care.**
- Ambient scribe adoption rose from **20%→29% of physicians** between two Doximity survey
  waves (latest Jan 2026); PHTI called it "one of the fastest technology adoptions in health
  care history." [Doximity 2026](https://www.doximity.com/reports/state-of-ai-medicine-report/2026)
- Structural backdrop AI doesn't touch: ~6,500 more 2026 medical school graduates than
  residency positions nationally; new-patient wait times up from ~20 days (early 2000s) to
  over a month (2025).
- **No credible workforce-level evidence** was found that AI scribes or triage have reduced
  primary-care physician demand or hiring.

**MS4 takeaway.** The most specific, most confidently stated, most credentialed (later Nobel
laureate) AI-job-elimination prediction in modern medicine was wrong on both magnitude and
direction. Ten years later radiology shows record Match positions, near-full fill rates, a
documented shortage, and top-tier salary growth. The transferable lesson isn't "AI never
disrupts medicine" — it's that **jobs reducible to a narrow, benchmarked perceptual task are
rare**; most physician value is judgment under ambiguity, communication, procedures, and
liability-bearing sign-off, further protected by malpractice and regulatory structures that
keep humans in the loop. Choosing a specialty by "how automatable does this look" would have
steered students away from radiology in 2016, right before it became one of the
best-compensated, most in-demand fields of the following decade. Pediatric radiology's
genuine softening is a useful nuance against blanket reassurance.

### 4.2 Health equity and algorithmic bias — canonical cases

*All PubMed metadata below verified directly except where flagged.*

**Obermeyer et al., cost-as-proxy bias.** Obermeyer Z, Powers B, Vogeli C, Mullainathan S.
"Dissecting racial bias in an algorithm used to manage the health of populations."
*Science* 2019 Oct 25;366(6464):447–453.
[DOI 10.1126/science.aax2342](https://doi.org/10.1126/science.aax2342). PMID 31649194.
**Statistic confirmed verbatim from the PubMed abstract:** correcting the bias "would
increase the percentage of Black patients receiving additional help from 17.7 to 46.5%."

**Pulse oximetry.**
- Sjoding MW et al. "Racial Bias in Pulse Oximetry Measurement." *NEJM* 2020 Dec
  17;383(25):2477–2478. DOI 10.1056/NEJMc2029240. **⚠ Widely-cited but not independently
  re-pulled via PubMed this session — confirm PMID (likely 33326721) before course use.**
- Fawzy A et al. "Racial and Ethnic Discrepancy in Pulse Oximetry and Delayed Identification
  of Treatment Eligibility Among Patients With COVID-19." *JAMA Intern Med*
  2022;182(7):730–738.
  [DOI](https://doi.org/10.1001/jamainternmed.2022.1906). PMID 35639368. Verified.
- Valbuena VSM et al. *BMJ* 2022;378:e069775.
  [DOI](https://doi.org/10.1136/bmj-2021-069775). PMID 35793817. Verified.
- **FDA status as of Aug 2026: still DRAFT, not finalized.** FDA issued draft guidance
  **Jan 7, 2025** (Federal Register 2024-31540) proposing premarket-study diversity
  requirements rise from 10 to **150 participants across skin tones**. It remains
  unfinalized. Companion piece: Lipnick MS et al. *JAMA* 2025;333(16):1393–1395.
  [DOI](https://doi.org/10.1001/jama.2025.1959). PMID 40042945.

**Dermatology datasets.**
- Daneshjou R et al. "Disparities in dermatology AI performance on a diverse, curated
  clinical image set." *Sci Adv* 2022;8(32):eabq6147.
  [DOI](https://doi.org/10.1126/sciadv.abq6147). PMID 35960806. Verified. (A DDI-2 follow-up
  exists in *J Invest Dermatol* 2024;145(5):1205–1208 — different journal, note if citing.)
- Adamson AS, Smith A. "Machine Learning and Health Care Disparities in Dermatology."
  *JAMA Dermatol* 2018;154(11):1247–1248.
  [DOI](https://doi.org/10.1001/jamadermatol.2018.2348). PMID 30073260. Verified — **note
  this is a Viewpoint, not original research.**
- Fitzpatrick17k: Groh M et al., CVPR Workshops 2021:1820–1828, arXiv:2104.09957 — not
  PubMed-indexed. Darker skin tones (Fitzpatrick V–VI) severely underrepresented (~10–20%).
- **⚠ No single canonical peer-reviewed citation** was found for "ISIC archive skin-tone
  underrepresentation" as a standalone claim — treat as synthesized, not single-sourced.

**Race-based clinical algorithms.**
- NKF-ASN Task Force: Delgado C et al., published simultaneously in *Am J Kidney Dis*
  2021;79(2):268–288.e1 ([DOI](https://doi.org/10.1053/j.ajkd.2021.08.003), PMID 34563581)
  and *J Am Soc Nephrol* 2021;32(12):2994–3015
  ([DOI](https://doi.org/10.1681/ASN.2021070988), PMID 34556489).
  **Current adoption (mid-2026):** roughly two-thirds of US labs have switched to race-free
  eGFR reporting; smaller and independent labs lag. **⚠ This adoption figure traces to a
  single secondary source citing an unspecified survey — flag before quoting precisely.**
- Vyas DA, Eisenstein LG, Jones DS. "Hidden in Plain Sight — Reconsidering the Use of Race
  Correction in Clinical Algorithms." *NEJM* 2020;383(9):874–882.
  [DOI](https://doi.org/10.1056/NEJMms2004740). PMID 32853499. Verified.
- Spirometry: Bowerman C et al. *Am J Respir Crit Care Med* 2023;207(6):768–774.
  [DOI](https://doi.org/10.1164/rccm.202205-0963OC). PMID 36383197. ATS/ERS recommended
  race-neutral GLI-Global equations from April 2023; adoption is uneven and **the switch
  remains actively debated** — 2025 data show race-neutral equations reclassify ~22.7% of
  Black and ~3.3% of Southeast Asian individuals to greater impairment severity. An
  unresolved controversy, not a settled correction.

**Chest X-ray underdiagnosis.** Seyyed-Kalantari L et al. "Underdiagnosis bias of artificial
intelligence algorithms applied to chest radiographs in under-served patient populations."
*Nat Med* 2021;27(12):2176–2182.
[DOI](https://doi.org/10.1038/s41591-021-01595-0). PMID 34893776. Verified.

**LLM-specific bias.**
- Omiye JA et al. "Large language models propagate race-based medicine." *NPJ Digit Med*
  2023;6(1):195. [DOI](https://doi.org/10.1038/s41746-023-00939-z). PMID 37864012. Verified.
- Zack T et al. "Assessing the potential of GPT-4 to perpetuate racial and gender biases in
  health care." *Lancet Digit Health* 2024;6(1):e12–e22.
  [DOI](https://doi.org/10.1016/S2589-7500(23)00225-X). PMID 38123252. Verified.
- **⚠** 2025–2026 follow-ups exist (a psychiatric-diagnosis LLM-bias audit in *npj Digital
  Medicine* 2025; "EQUITRIAGE," a 2026 ED-triage gender-bias audit of 9 LLMs) but **were not
  peer-review-confirmed this session** — verify venue before citing as canonical.

### 4.3 AI scribes and documentation burden

**Kaiser Permanente / TPMG.** Tierney AA et al. "Ambient Artificial Intelligence Scribes to
Alleviate the Burden of Clinical Documentation." *NEJM Catalyst* 2024;5(3).
[DOI](https://doi.org/10.1056/CAT.23.0404). 10,000 physicians enabled; 3,442 active users
across 303,266 encounters over 10 weeks; qualitatively higher note quality, reduced EHR and
after-hours time, favourable patient survey (no validated instrument).
**Design: pre-post, no control group.** Follow-up
([DOI 10.1056/CAT.25.0040](https://catalyst.nejm.org/doi/abs/10.1056/CAT.25.0040)): 7,260
physicians, >2.5M encounters over ~14 months, ~15,700–16,000 documentation-hours saved.

**Sutter Health.** No standalone Sutter-only paper found; Sutter co-authored a 6-system
study: Olson KD et al. *JAMA Netw Open* 2025;8(10):e2534976.
[PMID 41037268](https://pubmed.ncbi.nlm.nih.gov/41037268/). Self-reported burnout fell
**51.9%→38.8%** at 30 days (OR 0.26, 95% CI 0.13–0.54). **Pre/post, no control.**

**Mass General Brigham / Stanford.**
- You JG et al. (MGB + Emory), *JAMA Netw Open* 2025;8(8):e2528056.
  [PMID 40839265](https://pubmed.ncbi.nlm.nih.gov/40839265/). MGB: 21.2-point absolute
  burnout reduction at 84 days; Emory: 30.7-point wellbeing increase at 60 days; 60% of MGB
  participants said the tool made them more likely to extend their clinical career.
- Shah SJ et al. (Stanford), *JAMIA* 2025;32(2):375–380.
  [PMID 39657021](https://pubmed.ncbi.nlm.nih.gov/39657021/): task load −24.42 pts, burnout
  −1.94 pts (both p<.001), n=48, 3-month pilot.
- Ma SP et al. (Stanford), *JAMIA* 2025;32(2):381–385.
  [PMID 39688515](https://pubmed.ncbi.nlm.nih.gov/39688515/): median daily documentation time
  −6.89 min, after-hours −5.17 min, total EHR time −19.95 min/day; n=45, 17,428 encounters.

**RCT-level evidence now exists (2025–2026) — genuinely mixed, especially on "pajama time":**
- Lukac PJ et al. (UCLA), 3-arm RCT n=238, medRxiv preprint,
  [PMID 40672471](https://pubmed.ncbi.nlm.nih.gov/40672471/): Mini-Z burnout +2.76, task load
  −35.8/400 (both p≈.01) for either scribe vs control; occasional clinically-significant
  inaccuracies on both tools.
- Afshar M et al. (U Wisconsin), stepped-wedge RCT n=66, *NEJM AI* 2025,
  [PMID 41625485](https://pubmed.ncbi.nlm.nih.gov/41625485/): work exhaustion −0.44 pts
  (p<.001); note quality (PDSQI-9) 3.97–4.99/5; **workweek-hours reduction lost significance
  after outlier removal.**
- Chowdhury A et al. (Duke), randomized crossover n=136, *JAMIA* 2026,
  [PMID 41729180](https://pubmed.ncbi.nlm.nih.gov/41729180/): burnout improved with both
  tools; **no meaningful difference in pajama time.**
- Shin HS et al. (Emory/CHOA peds), randomized QI trial n=23, *Appl Clin Inform* 2025,
  [PMID 40675605](https://pubmed.ncbi.nlm.nih.gov/40675605/): burnout 89%→56% in intervention
  vs stable 38% control, but **no significant change in pajama time or charting time.**
- **Largest, most rigorous non-randomized counterweight:** Rotenstein LS et al. (UCSF, MGB,
  UC Davis, Yale New Haven, Emory), *JAMA* 2026;335(16):1408–1417,
  [PMID 41920565](https://pubmed.ncbi.nlm.nih.gov/41920565/), n=8,581 clinicians (1,809
  adopters): total EHR time −13.4 min/day, documentation time −16.0 min/day, +0.49
  visits/week — **but after-hours EHR time did not change significantly**, and STAT reported
  **79% of clinicians offered the tool declined to use it.**
  [STAT](https://www.statnews.com/2026/04/01/ai-ambient-scribes-modest-time-savings-clinical-documentation/)

**Takeaway on evidence quality.** Most widely publicized health-system statistics (Kaiser's
hours saved, MGB's 21.2-point burnout drop) are **pre/post pilot data from self-selected
early adopters** — susceptible to selection bias and Hawthorne effects. The smaller but
growing RCT literature shows real but smaller and more heterogeneous benefits, and largely
**fails to confirm the "pajama time" reduction that residents care about most.** Time saved
may be redirected into seeing more patients rather than recovered as personal time.

**Market (2025–2026, trade-press sourced — directional, not audited).** Becker's market-share
estimate: Microsoft/Nuance DAX Copilot ~33%, Abridge ~30%, Ambience ~13%, Suki ~10%,
Nabla/Freed ~4% each. Abridge: $300M Series E (a16z-led), June 2025, $5.3B valuation, with
contracts including Sutter, Mayo, UCSF, Yale New Haven, Emory. Ambience: $243M Series C, July
2025, $1.25B valuation. Suki: $70M Series D, Oct 2024, $500M valuation.
[Becker's](https://www.beckershospitalreview.com/healthcare-information-technology/ai/ambient-ai-scribes-by-market-share/)

**Skeptical takes:** *npj Digital Medicine* on AI-scribe hallucination/safety risk categories
([nature.com](https://www.nature.com/articles/s41746-025-01895-6)); malpractice-carrier
commentary that clinicians remain legally responsible for AI-drafted note content
([MICA](https://www.mica-insurance.com/blog/posts/ai-scribes-pose-liability-risks/)).

### 4.4 Payer / utilization-management AI — legal and regulatory status (as of Aug 2026)

> **⚠ This section moves fast. Re-check every item close to the course date.**

**UnitedHealth nH Predict — *Estate of Gene Lokken v. UnitedHealth* (D. Minn.), filed Nov
2023.** March 11, 2025: court denied UnitedHealth's motion to dismiss on breach-of-contract
and good-faith/fair-dealing claims, rejecting the Medicare-exhaustion defense. March 9, 2026:
magistrate ordered discovery largely favouring plaintiffs (6 of 7 requested document
categories, including nH Predict design/training/government-inquiry materials), reportedly
citing the Senate PSI findings. **Status: NOT settled, dismissed, or at trial — active
discovery, moving toward class certification.** Declarations reportedly due Sept 2026 per
Forbes — **not docket-verified.**
[Forbes, June 2026](https://www.forbes.com/sites/daraabasiita/2026/06/09/the-algorithm-that-counted-on-no-one-appealing/)

**Cigna PXDX — *Kisting-Leung v. Cigna* (E.D. Cal.).** ProPublica's March 2023 investigation
reported ~300,000 claims rejected in two months of 2022 at ~1.2 seconds per claim. Filed July
2023. March 31, 2025: mixed ruling — case proceeds on ERISA-adjacent
plan-terms-delegation claims, but three named plaintiffs lost standing.
**⚠ Status beyond March 2025 not confirmed — needs a fresh docket check.**

**Humana nH Predict class action (W.D. Ky.), filed ~Dec 2023.** Court ruled plaintiffs need
not exhaust Medicare administrative appeals first; survived motion to dismiss.
**⚠ Current 2026 procedural phase not confirmed.**

**Senate PSI report — important correction.** The core report, *"Refusal of Recovery: How
Medicare Advantage Insurers Have Denied Patients Access to Post-Acute Care,"* was published
**October 17, 2024** — **not October 2025**, under then-chair Sen. Richard Blumenthal. Key
statistics: UnitedHealthcare post-acute prior-auth denial rate **10.9% (2020) → 16.3% (2021)
→ 22.7% (2022)**; Humana long-term acute-care denial rates up 54% (2020–2022). **October 2025
activity was follow-up oversight letters** to UHC/Humana/CVS-Aetna (Blumenthal now ranking
member), not a new report; a further letter to Humana followed July 14, 2026. If source
material says "Oct 2025 report," it is conflating the two.
[Blumenthal release](https://www.blumenthal.senate.gov/newsroom/press/release/senate-permanent-subcommittee-on-investigations-releases-majority-staff-report-exposing-medicare-advantage-insurers-refusal-of-care-for-vulnerable-seniors) ·
[STAT, Oct 2025](https://www.statnews.com/2025/10/09/blumenthal-letter-on-medicare-insurers-using-ai-unitedhealth-humana-cvs-aetna/)

**CMS regulatory actions.**
- **2024 MA/Part D Final Rule (CMS-4201-F):** AI and algorithms may inform coverage decisions
  but **cannot be the sole basis for a denial** — decisions must be individualized to the
  enrollee's actual medical history, clinical notes, and physician input.
  [CMS fact sheet](https://www.cms.gov/newsroom/fact-sheets/2024-medicare-advantage-and-part-d-final-rule-cms-4201-f)
- **CMS WISeR Model** (Wasteful and Inappropriate Service Reduction): launched **January 1,
  2026**, a 6-year CMMI pilot bringing AI-assisted prior authorization into *traditional*
  fee-for-service Medicare in six states (NJ, OH, OK, TX, AZ, WA). Contractors use AI to flag
  requests against coverage policy; a human clinician must review before a denial is
  finalized. **Central criticism: contractor compensation is tied to "averted expenditures"**
  — a savings-share structure creating a denial incentive. **May 20, 2026:** Democrats
  introduced a Congressional Review Act resolution to repeal WISeR; the Senate rejected it
  **46–50** along party lines, so the pilot stands. A Georgetown CHIR piece flags a possible
  GAO-driven repeal threat that was **not independently substantiated**.
  [DLA Piper](https://www.dlapiper.com/en/insights/publications/2026/01/cms-wiser-model) ·
  [KFF](https://www.kff.org/medicare/examining-the-potential-impact-of-medicares-new-wiser-model/)

**State laws.**

| State | Bill | Provision | Effective |
|---|---|---|---|
| California | SB 1120 (Physicians Make Decisions Act) | AI cannot be the sole basis for denying/delaying/modifying care; final medical-necessity call by a licensed clinician | Signed Sept 2024, effective Jan 1, 2025 |
| Georgia | SB 444 | Adverse determinations require a qualified human clinical-peer reviewer | Jan 1, 2027 |
| Illinois | SB 3114 (Transparency in Downcoding Act) | Targets AI-driven claim downcoding; adverse determinations require a "clinical peer" | ⚠ Effective date unconfirmed |
| Texas | SB 815 | AI cannot be sole basis for adverse coverage determinations | ⚠ Effective date unconfirmed |
| New York | S7896/A11048 | Pending, not enacted | N/A |

**⚠ Secondary sources put the 2026 national count at 14–15 new state AI-healthcare laws
(Transparency Coalition) vs 7 state-specific "AI health insurance" laws (Becker's). These two
lists were not reconciled — pull both directly before finalizing slides.**
[Holland & Knight](https://www.hklaw.com/en/insights/publications/2026/05/states-continue-efforts-to-regulate-ai-in-healthcare) ·
[Transparency Coalition](https://www.transparencycoalition.ai/news/state-lawmakers-have-passed-15-new-laws-regulating-the-use-of-ai-in-health-care)

### 4.5 Economics

**Investment.** Rock Health: digital health venture funding **$14.2B across 482 deals in
2025**, up 35% from 2024's $10.5B; AI-branded firms captured **54% of 2025 dollars** (up from
37% in 2024) with a ~19% deal-size premium.
[Rock Health](https://rockhealth.com/insights/2025-year-end-digital-health-funding-overview-a-tale-of-two-markets/)
CHIME CIO survey: 76% of health-IT leaders plan to increase AI/automation spend in 2026;
AI-clinical solutions jumped from 19% to 57% of C-suite top-5 tech priorities since 2023 —
capturing a growing *share* of budgets that are themselves flat-to-shrinking (41% expect
capital investment to fall over two years).
**⚠ "Market size" dollar figures from vendor research firms ($6B–$18B depending on source)
are inconsistent and unverified — do not present as hard data.**

**ROI evidence — the central independent finding.** Peterson Health Technology Institute
(PHTI), funded by the non-vendor Peterson Center on Healthcare:
- **March 2025 report on ambient scribes:** likely reduces burnout, but PHTI found **little
  to no evidence of financial ROI** — health systems themselves acknowledged gaps in
  productivity and financial-impact data.
  [PHTI PDF](https://phti.org/wp-content/uploads/sites/3/2025/03/PHTI-Adoption-of-AI-in-Healthcare-Delivery-Systems-Early-Applications-Impacts.pdf) ·
  [STAT](https://www.statnews.com/2025/03/27/do-ai-scribes-help-health-systems-save-time-health-tech/)
- **April 2026 report, "Administrative AI: Current Use and Potential Impact":** AI reduces
  burden **within individual organizations** but is **not lowering system-wide costs — and
  may be raising them**, via a "bot wars" dynamic (providers auto-generating appeals, payers
  auto-adjudicating denials, more back-and-forth without resolving clinical questions). PHTI
  states explicitly there is "no existing evidence" that AI-accelerated prior auth lowers
  average cost per claim once the AI solution's own cost is counted.
  [PHTI](https://phti.org/administrative-ai-current-use-and-potential-impact/) ·
  [Fierce Healthcare](https://www.fiercehealthcare.com/ai-and-machine-learning/ai-speeding-prior-authorizations-while-driving-higher-costs-health-systems)
- Corroborating: UCSF found ambient-scribe adopters saw a **5.8% increase in billed RVUs with
  no rise in denials** — early evidence of more billable output, not cost reduction.

**"AI won't cut costs" debate.** Robert Pearl (Forbes, July 2026) argues clinical labor is
only ~one-fifth of total spending, so even a 10% AI-driven labor cut yields only ~2–3% total
savings; he argues generative AI's real leverage is chronic-disease management, not staff
replacement. Penn LDI / Amol Navathe (April 2026): reimbursement policy is built around
human-labor inputs and doesn't account for AI's scalability, risking overuse absent payment
reform. PHTI's "bot wars" finding is the most concrete evidence-based version of this.

**Workforce displacement — the actually-measured cases.**
- **Medical transcriptionists:** BLS projects **~5% employment decline 2024–2034**,
  explicitly attributed to speech recognition and AI. **⚠ Direct BLS.gov fetch returned 403 —
  verify wording directly before quoting.**
- **Medical coders / health-information technicians:** BLS projects **growth, not decline** —
  Medical Records Specialists **+7%**, Health Information Technologists **+15%** (2024–2034),
  driven by aging population and rising documentation volume. This **directly contradicts** a
  naive "AI is displacing coders" narrative — a useful teaching contrast against the
  transcriptionist data.
- **Medical scribes:** not a standalone BLS/SOC category, so no official time series exists.
  Trade press only: Augmedix reportedly pivoted from human-scribe staffing to an AI-only
  product; ScribeAmerica reportedly transitioning to an AI platform model. **Present as
  anecdotal industry evidence, not verified labor statistics.**

**Administrative burden ~25% — three distinct studies commonly conflated:**
1. Shrank WH, Rogstad TL, Parekh N. "Waste in the US Health Care System." *JAMA* 2019.
   [PMID 31589283](https://pubmed.ncbi.nlm.nih.gov/31589283/). Total waste $760B–$935B/yr,
   ~25% of spending — **administrative complexity is one of six sub-categories, not the whole
   25%.**
2. Himmelstein DU et al., *Health Affairs*: US **hospital** administrative costs = **25.3% of
   hospital expenditures** (>$200B); the 2014 8-nation comparison found US hospital admin
   costs far exceed peers (Netherlands 19.8%, England 15.5%).
3. Woolhandler, Campbell, Himmelstein, *NEJM* 2003: total US healthcare administration
   ≈ $294.3B, **~24% of spending** (1999 data) — the broadest definition in the literature.

Teach these as **three different denominators**, not one number from one paper. PHTI's April
2026 report is the strongest current independent test of the "AI will cut this 25%" pitch,
and its answer is a qualified no at the system level so far.

### 4.6 Activities — Area 4

**Activity 4.A — "The Hinton Prediction" structured debate (60 min).**
Split into 4 breakout groups. Each gets a different specialty (radiology, pathology, primary
care, and a wildcard such as anesthesiology or dermatology) and 15 min to build a 2026-data
case for "this specialty follows the radiology pattern" vs "this specialty is genuinely
different." Reconvene for a four-corners rapid-fire debate. **Ground rule: every claim needs
a citation from the packet** (Match data, ACR/CAP reports, salary trends, FDA clearance
counts). Debrief with the Mousa framework (task decomposition, generalization gaps, liability
structure, Jevons paradox) as the analytic tool students then apply to their own specialty
choice.

**Activity 4.B — Algorithm bias audit walkthrough (75 min).**
Walk through Obermeyer et al. live (10–15 min: what the algorithm optimized for — cost — vs
what it should have optimized for — need — and the 17.7%→46.5% correction). Then break into
groups of 4–5, each assigned one other canonical case (pulse oximetry, dermatology datasets,
eGFR, chest X-ray underdiagnosis, or LLM bias). Each group answers a fixed worksheet:
(a) what proxy or training-data gap caused the bias; (b) who was harmed and how; (c) what
corrective action was taken and its **current adoption status** (e.g. ~2/3 of labs on
race-free eGFR; FDA pulse-ox guidance still in draft as of 2026); (d) what a clinician could
have caught at the bedside without knowing the algorithm's internals. Report back in plenary.
Close on the throughline: **every case is a proxy problem** — cost for need, light skin for
"normal" reflectance, race for unmeasured biology and environment.

**Activity 4.C — Payer-denial appeal role-play (60 min, breakout triads).**
Triads: one student is a hospitalist/PCP appealing an AI-flagged post-acute-care denial
(modelled loosely on the nH Predict fact pattern), one is a payer utilization-review nurse
operating under an algorithm's recommendation, one is an observer scoring with a rubric (did
the physician cite specific clinical findings the algorithm couldn't see? did the payer rep
articulate the algorithm's role vs final human authority, per the 2024 CMS rule?). Rotate
roles across two 12-minute rounds. Debrief with the real numbers: UnitedHealthcare post-acute
denial rate climbing 10.9%→22.7% (2020–2022, Senate PSI), the reversal-on-appeal claims in
the Lokken litigation, and California SB 1120 as a regulatory response.

**Activity 4.D — AI scribe evidence-grading exercise (45 min).**
Give pairs 6–8 mixed claims about AI scribes pulled straight from §4.3 (Kaiser's hours saved,
MGB's 21.2-point burnout drop, the UCLA/Wisconsin/Duke/Emory RCT findings on pajama time, the
Rotenstein *JAMA* 2026 finding that after-hours time didn't change and 79% of offered
clinicians declined the tool). Pairs sort each claim into "RCT," "large observational /
pre-post," or "vendor / trade press," then rate confidence. Plenary reveal: **why do the
flagship health-system press releases look so much better than the RCTs?** What does that
mean for how students should read AI vendor claims as attendings?

**Activity 4.E — Specialty-choice forecasting exercise (45 min).**
Each student privately ranks their top 2 specialty choices, then answers: what is the single
most AI-automatable *task* within that specialty (not the whole job), and what fraction of the
actual job does that task represent (using the radiology 36%-image-interpretation figure as a
benchmark)? Pair up and pressure-test each other using the four Mousa factors. Close with the
explicit caveat: **this is a forecasting method, not a guarantee** — a Nobel laureate got the
highest-profile version of this call wrong in both directions.

**Activity 4.F — "Will AI cut costs?" mock policy briefing (60 min).**
Four roles: hospital CFO, independent health-policy economist (PHTI-style evaluator), AI
vendor, and a displaced-worker advocate (coders/transcriptionists/scribes). Each team has 20
min to build a 3-slide-equivalent verbal pitch from assigned evidence (PHTI's two reports,
the Shrank/Himmelstein admin-cost figures, the BLS transcriptionist-decline vs coder-growth
contrast, Rock Health investment data). Each presents 3 min, then open Q&A where teams
challenge each other using competing evidence from the packet. Close on augment-vs-replace as
an **explicitly unresolved policy question**, appropriate given these are the residents who
will live this debate for 30 years.

*Format notes:* cap breakout groups at 4–5 for real participation. Use Zoom auto-assign for
4.A, 4.B, 4.D, 4.F; manual or self-select for 4.E (specialty-specific). Activities 4.B and
4.F work well as the spine of two different weekly sessions; 4.A, 4.C, 4.D, 4.E can each
anchor a single 60–90 min session alongside a short didactic block.

---

## Area 5 — Ethics and regulation

> **Provenance note.** This area was researched in three topic-specific passes that were
> never merged by a synthesizing pass. One pass **exhausted its web-search budget partway
> through**, leaving real holes (listed in §5.7). The activities in §5.6 were written from
> the research findings rather than supplied by the research passes.

### 5.1 FDA regulation of AI/ML medical devices (verified 2026-08-05)

**AI-Enabled Device List.** **⚠ Direct fetch of the FDA AI-device-list page returned 404 —
the URL has likely changed. The figures below are secondary and must be re-checked against
fda.gov before use.**
- **~1,451 AI-enabled devices authorized total** (since 1995) per the FDA database, per the
  [MedTech Dive tracker](https://www.medtechdive.com/news/ai-medtech-track-new-devices-fda/748397/),
  which downloaded FDA's list May 11, 2026 and states FDA last updated the underlying
  database **March 4, 2026**. **331 devices authorized in 2025 alone** (record year).
- Specialty breakdown: **76% radiology**; then cardiovascular, neurology, hematology,
  gastroenterology-urology.
- **As of March 2026, no device has been authorized using generative AI / LLMs**
  ([IntuitionLabs](https://intuitionlabs.ai/articles/fda-ai-medical-device-tracker) —
  secondary, not FDA-verified).

**Predetermined Change Control Plans (PCCP).** Final guidance issued **Dec 4, 2024**. A PCCP
lets manufacturers pre-specify anticipated modifications (description of modifications +
modification protocol + impact assessment) in the original marketing submission, so
subsequent updates within the plan don't require a new submission — the key mechanism for
continuously-learning models. The final guidance broadened scope from ML-only (2023 draft) to
all AI device software functions.
[Ropes & Gray](https://www.ropesgray.com/en/insights/alerts/2024/12/fda-finalizes-guidance-on-predetermined-change-control-plans-for-ai-enabled-device) ·
[Foley & Lardner](https://www.foley.com/insights/publications/2025/01/fda-final-guidance-ai-device-software-predetermined-change-control-plan/)

**Jan 2025 draft lifecycle guidance.** "AI-Enabled Device Software Functions: Lifecycle
Management and Marketing Submission Recommendations," issued **Jan 7, 2025**
([Federal Register](https://www.federalregister.gov/documents/2025/01/07/2024-31543/artificial-intelligence-enabled-device-software-functions-lifecycle-management-and-marketing)),
comment period closed April 7, 2025. **Still in draft as of June 2026** — not finalized. Would
be the first guidance covering the full AI device lifecycle including postmarket performance
monitoring.
[ClinicalMind tracker](https://healthcareaiinsights.com/fda-clearance-tracker/fda-ai-samd-guidance-status-june-2026)

**Clinical Decision Support — IMPORTANT UPDATE.** The **Sept 28, 2022** final CDS guidance was
**superseded by a revised final CDS guidance issued January 6, 2026.** Commissioner Makary
framed it as deregulatory ("cut unnecessary regulation"), but analysts (Covington, DLA Piper)
say it **largely preserves existing policy** rather than fundamentally shifting it.
**Teach both the original 2022 four-criteria framework and this Jan 2026 replacement — it is
a live, moving target.**
[ABA](https://www.americanbar.org/groups/health_law/news/2026/fda-guidance-clinical-decision-support-software/) ·
[Covington](https://www.cov.com/news-and-insights/insights/2026/01/5-key-takeaways-from-fdas-revised-clinical-decision-support-cds-software-guidance) ·
[FDA Law Blog](https://www.thefdalawblog.com/2026/01/a-busy-day-in-the-cdrh-neighborhood-updates-to-the-cds-and-general-wellness-guidance-documents/)
*2022 controversy worth teaching:* the CDS Coalition filed a Feb 2023 Citizen Petition to
rescind the guidance, arguing FDA's reading of "recommendations" (statutory plural)
improperly narrowed the device exemption; the HIMSS EHR Association also objected.
[Sidley](https://www.sidley.com/en/insights/newsupdates/2022/10/one-step-forward-two-steps-back-fdas-final-guidance-on-clinical-decision-software)

**Generative AI / LLM position.** FDA's Digital Health Advisory Committee met **Nov 20–21,
2024** specifically on generative AI. The panel recommended: patients be told when a genAI
device is used and how it influenced care; user-friendly post-market error reporting;
performance evaluation **including hallucination rates**; and acknowledged that genAI's
probabilistic, unpredictable nature requires new regulatory thinking versus deterministic
narrow AI. **⚠ No dedicated final generative-AI guidance was found — a genAI-specific
framework appears not to be finalized as of Aug 2026. Worth one targeted follow-up search.**
[Federal Register notice](https://www.federalregister.gov/documents/2024/09/17/2024-21074/) ·
[MedTech Dive recap](https://www.medtechdive.com/news/fda-digital-health-advisory-committee-gen-ai/735371/) ·
[Jones Day](https://www.jonesday.com/en/insights/2024/12/fda-digital-health-advisory-committee-discusses-genaienabled-devices)

**FDA's "Elsa" tool.** An internal FDA AI for reviewers (not a medical device). Elsa 1.0
launched June 2025; **Elsa 4.0 released May 2026** with agentic features, document
generation, data analysis, OCR, and web search. The early version had **documented
hallucination and accuracy problems, acknowledged by Commissioner Makary** — excellent
teaching irony: the regulator's own tool hallucinates.
[Hogan Lovells](https://www.hoganlovells.com/en/publications/fda-ai-tool-elsa-40-and-halo-unveiled) ·
[FDA press release](https://www.fda.gov/news-events/press-announcements/fda-expands-artificial-intelligence-capabilities-agentic-ai-deployment) ·
[Applied Clinical Trials](https://www.appliedclinicaltrialsonline.com/view/fda-elsa-ai-tool-raises-accuracy-and-oversight-concerns)

**510(k) / De Novo criticism.** Windecker D, Baj G, Shiri I, et al. "Generalizability of
FDA-Approved AI-Enabled Medical Devices for Clinical Use." *JAMA Netw Open*
2025;8(4):e258052. pmid:40305017. Of 903 AI-enabled devices listed by the FDA as of 31 August
2024: clinical performance studies reported for 505 (55.9%); 218 (24.1%) explicitly stated
none was done; among clinical studies, 145 (28.7%) gave sex-specific data and 117 (23.2%)
addressed age subgroups. Corrected 2026-10-12: these figures were earlier attributed here to
Wu E, Wu K, Daneshjou R, et al., *Nature Medicine* 2021;27:582-584 (130 decision summaries;
pmid:33820998; [link](https://www.nature.com/articles/s41591-021-01312-x)), whose PubMed
record has no abstract, so its own figures were not checked. "Not all AI health tools with
regulatory authorization are clinically validated" (*Nat Med* 2024, pmid:39187696,
[link](https://www.nature.com/articles/s41591-024-03203-3)) also has no abstract in PubMed;
cite it for its title's claim only.

### 5.2 Liability

**Price WN 2nd, Gerke S, Cohen IG.** "Potential Liability for Physicians Using Artificial
Intelligence." *JAMA* 2019;322(18):1765–1766, published Oct 4, 2019. DOI
10.1001/jama.2019.15064.
[JAMA](https://jamanetwork.com/journals/jama/article-abstract/2752750) ·
[PubMed](https://pubmed.ncbi.nlm.nih.gov/31584609/).
Proposes a 2×2 framework — (AI recommendation aligns with / conflicts with standard of care)
× (physician follows / departs from AI) — mapping four liability scenarios. **The
uncomfortable implication for students: physicians face the most legal risk when they deviate
from standard of care by following AI.** Current tort law still centers on physician conduct
measured against standard-of-care benchmarks, not on the AI itself — which structurally
discourages AI adoption where it would most change management.

**Product liability / learned intermediary.** Best coverage found in the NCBI Bookshelf
chapter "Liability for use of artificial intelligence in medicine" (*Research Handbook on
Health, AI and the Law*), [link](https://www.ncbi.nlm.nih.gov/books/NBK613216/). **⚠ Not
fully extracted — fetch directly if doctrinal depth is needed.**

**Decided malpractice cases involving clinical AI: NONE confirmed as of 2026.** Multiple
2025–2026 secondary sources (Duquesne Juris Magazine Nov 2025, arXiv legal analyses)
explicitly state no malpractice claim has worked through to verdict involving a clinical AI
tool. **Do not claim otherwise.**

**Malpractice insurers.** The Doctors Company published guidance ("AI on Trial," Q4 2025,
[thedoctors.com](https://www.thedoctors.com/the-doctors-advocate/fourth-quarter-2025/ai-on-trial-the-rising-liability-risks-of-artificial-intelligence-in-healthcare))
stating it currently has **no AI exclusion** and would still defend and indemnify physicians
when AI is involved. General market pattern (CM&F Group, Medical Economics): cautious
case-by-case underwriting, no blanket AI exclusions yet, advice to notify the carrier before
adopting clinical AI. No specific published Coverys position found.

**AI-company lawsuits (consumer/mental-health — not clinical AI, but directly relevant).**
- Character.AI/Google and OpenAI: ~10+ wrongful-death/negligence suits by end of 2025.
  **Jan 2026: Character.AI and Google settled with 5 families** (confidential terms, no
  admission of liability). Aug 2025: *Raine v. OpenAI* — first-of-its-kind wrongful death
  suit. Nov 2025: 7 more OpenAI suits filed in California state court. **June 2, 2026:
  Florida AG Uthmeier filed suit against OpenAI — the first state AG action against an AI
  company**, alleging concealed safety warnings.
- **May 2025:** federal judge Anne C. Conway rejected Character.AI's First Amendment and
  Section 230 defenses, allowing product-liability and negligence claims to proceed. A
  significant doctrinal development.
- **Directly health-relevant:** *Scott Winters v. OpenAI/Altman*, San Francisco Superior
  Court, ~July 2026 — plaintiff alleges ChatGPT-4o minimized his symptoms (dizziness, low
  BP), told him to stay "recliner-bound," and delayed care before a pulmonary embolism. The
  suit also seeks an injunction pausing "ChatGPT Health" pending independent safety review.
  **⚠ The product name "ChatGPT Health" comes from one secondary summary — confirm it exists
  and what it is before citing. Case status: filed, not decided.**
  [Forbes](https://www.forbes.com/sites/jessepines/2026/07/26/a-lawsuit-says-chatgpt-nearly-someone-heres-the-data-on-ai-diagnosis/)

### 5.3 Consent, transparency, disclosure (verified 2026-08-05)

**Patient attitudes.** Pew Research Center, "How Americans View Use of AI in Health Care and
Medicine by Doctors and Other Providers," released **Feb 22, 2023**, fielded Dec 12–18 2022,
n=11,004 US adults. **60% would feel uncomfortable if their provider relied on AI for
diagnosis/treatment recommendations** (39% comfortable); 66% of women vs 54% of men
uncomfortable. Only 38% thought AI would improve outcomes; 33% thought it would worsen them.
Specifics: 65% wanted AI in skin-cancer screening; **79% opposed AI chatbots for mental health
support**; 67% opposed AI-set pain-medication dosing; 59% opposed AI-powered surgical robots.
[Pew](https://www.pewresearch.org/science/2023/02/22/60-of-americans-would-be-uncomfortable-with-provider-relying-on-ai-in-their-own-health-care/)

**⚠ No Pew repeat survey located for 2024–2026.** A 2024–2025 multinational hospital-patient
survey (medRxiv preprint) found 57.6% net-positive attitude toward AI in healthcare with the
same gender-gap pattern, but it is **not directly comparable** to Pew's "comfortable with
provider using AI" framing. PMC review articles (PMC11829222, PMC12012342, PMC12964161) show
trust is highly conditional on FDA approval, clinician-in-the-loop, and disclosed data
provenance. **Treat 2023 as the anchor figure**; attitudes appear to be softening somewhat,
but the data is fragmented across smaller academic surveys with no authoritative tracker.

**AI scribes — the consent-law collision (an active 2026 flashpoint, not settled practice).**
Ambient scribes (Abridge, Nuance DAX Copilot, Ambience, DeepScribe) saw reported ~2.4x revenue
growth in 2025 (~$600M).
- California and ~12 other two-party/all-party consent states require every participant's
  consent before recording. **Florida treats non-consensual recording of oral communication
  as a third-degree felony** (up to 5 years, $5,000) — directly implicating ambient scribes
  absent consent.
- **Washington v. Sutter Health** class action (filed ~April 2026) alleges CIPA, CMIA, and
  federal Wiretap Act violations from ambient scribe recording without adequately informed
  consent — **HIPAA compliance alone was argued to be an insufficient defense.**
- A separate **Sharp HealthCare / Abridge** class action was filed January 2026 alleging a
  patient's physical exam was recorded without knowledge or consent.
- *Practical upshot:* verbal/opt-out consent scripts are now common practice, but the
  plaintiffs' bar is testing whether that consent is "informed" enough given AI processing and
  retention. **Unsettled, active litigation — excellent moot-court material.**
- **⚠ Source quality is mixed** (several law-firm blogs and marketing sites). Present the
  litigation claims to students as **allegations, not adjudicated facts.**

**HTI-1 final rule (ASTP/ONC) — DSI transparency.** Published in the Federal Register **Jan 9,
2024** (effective Feb 8, 2024); creates the "Decision Support Intervention" (DSI)
certification criterion at 45 CFR 170.315(b)(11), replacing the old CDS criterion at (a)(9).
Two sub-categories: **evidence-based DSIs (13 required source attributes)** and **Predictive
DSIs (31 source attributes)** — the "nutrition label," covering development data, validity,
and fairness testing. Developers had to update certified health IT to the DSI criterion by
Dec 31, 2024. **Starting Jan 1, 2026, developers with Predictive DSI offerings must collect a
full calendar year of real-world performance / risk-management / FAVES data for ONC
reporting** — meaning as of Aug 2026 we are **mid-way through the first data-collection year,
with actual public transparency reporting still pending.**
[Federal Register](https://www.federalregister.gov/documents/2024/01/09/2023-28857) ·
[healthit.gov](https://www.healthit.gov/topic/laws-regulation-and-policy/health-data-technology-and-interoperability-certification-program)

**HTI-2 / HTI-4 / HTI-5 — the 2025–2026 deregulatory pivot (important, not widely known).**
ASTP/ONC finalized a pared-down HTI-2 rule in Dec 2024, then **withdrew the remaining
non-finalized HTI-2 provisions effective Dec 29, 2025** (Federal Register 2025-23890),
explicitly citing a deregulatory posture and "emerging AI technologies." HTI-4 (e-prescribing,
prior auth, real-time benefit) was finalized separately. A new **HTI-5 NPRM ("Deregulatory
Actions to Unleash Prosperity")** was released for 60-day comment, removing redundant
certification requirements and reworking AI-enabled interoperability rules.
**Net effect for the course:** the Biden-era HTI-1 AI transparency requirements **remain in
force and are entering their first reporting cycle**, but the broader ONC trajectory turned
sharply deregulatory in 2025–2026.
[Federal Register 2025-23890](https://www.federalregister.gov/documents/2025/12/29/2025-23890)

**CHAI (Coalition for Health AI).** Released a draft "Applied Model Card" template (first
applied to Aidoc, Oct 2024) — open-access schema on GitHub
(coalition-for-health-ai/mc-schema), pitched as a nutrition label for health AI.
**2025 controversy:** HHS leadership under Secretary RFK Jr. and Deputy Secretary Jim O'Neill
publicly criticized CHAI, with HHS asserting it would not let CHAI or any nonprofit "operate
as an implicitly government-backed regulator." **A genuinely live governance fight worth
surfacing: a private consortium trying to fill a regulatory gap, now itself politically
contested.**
[Healthcare IT News](https://www.healthcareitnews.com/news/chai-seeks-communicate-hhs-leaders-over-recent-criticisms)

**Epic AI Trust and Assurance Suite.** Open-source tool (free, on GitHub) that automates data
mapping and provides near-real-time dashboards on AI model performance and bias broken out by
age, sex, and race/ethnicity; enables continuous local monitoring for drift and
clinical-outcome impact, not just accuracy.
[Healthcare IT News](https://www.healthcareitnews.com/news/epics-ai-validation-cookbook)

**Reporting guidelines (verified citations).**
- **TRIPOD+AI**: Collins GS et al., *BMJ* 2024;385:e078378 — prediction model
  development/validation reporting.
- **CONSORT-AI**: Liu X et al., *BMJ* 2020;370:m3164 / *Nature Medicine* 2020 — RCT reporting
  for AI interventions.
- **SPIRIT-AI**: Cruz Rivera S et al., *BMJ* 2020;370:m3210 / *Nature Medicine* 2020 — trial
  protocols.
- **DECIDE-AI**: Vasey B et al., *Nature Medicine* 2022;28:924–933 — early-stage clinical
  evaluation of AI decision-support systems.
All indexed at [equator-network.org](https://www.equator-network.org/).

### 5.4 EU AI Act and healthcare vs the US posture (verified 2026-08-05)

**Why medical AI is "high-risk."** The AI Act (Regulation (EU) 2024/1689) uses a risk pyramid:
unacceptable (banned), high-risk, limited-risk (transparency duties), minimal-risk. **Annex I**
lists AI systems that are safety components of, or are themselves, products already covered by
EU harmonization legislation **including the Medical Device Regulation (MDR 2017/745) and IVDR
(2017/746)**. So most AI/ML-based SaMD (diagnostic algorithms, triage tools) is **automatically
high-risk** because it is already a regulated medical device requiring third-party conformity
assessment — and the AI Act **layers additional obligations on top** of MDR/IVDR CE-marking
(risk management, data governance, technical documentation, human oversight, logging, accuracy
and robustness).

**Timeline — original vs current, through the June 2026 Digital Omnibus outcome:**
- **Aug 1, 2024** — AI Act entered into force
- **Feb 2, 2025** — prohibited practices (Article 5) applicable
- **Aug 2, 2025** — GPAI (general-purpose AI model) obligations applicable
- **Originally Aug 2, 2026** — high-risk system obligations were to become applicable
- **Nov 19, 2025** — Commission published the "Digital Omnibus" proposal to defer high-risk
  obligations, citing delays designating national competent authorities and finalizing
  harmonized standards
- Trilogue: first round (Apr 28, 2026) failed; provisional political agreement **May 6, 2026**,
  confirmed by Council **May 13, 2026**
- **European Parliament formal endorsement: June 16, 2026**
- **Council of the EU final green light: June 29, 2026** — simplification package formally
  adopted, pending Official Journal publication
- **New deadlines: Dec 2, 2027** for standalone high-risk AI systems; **Aug 2, 2028** for
  high-risk AI embedded in products

**So as of the course date (August 2026), the original Aug 2026 high-risk compliance deadline
has been legislatively deferred — this is confirmed, not speculative.**
**⚠ The Official Journal publication date / exact entry-into-force date could not be
independently confirmed beyond "third day after publication" — flag if a precise date matters
for slides.**
Sources: europarl.europa.eu legislative train file "Digital Omnibus on AI"; DLA Piper GENIE
tracker (updated through June 30, 2026); Gibson Dunn, Skadden, Addleshaw Goddard client alerts.

**Emotion recognition (Article 5(1)(f)) — a common misconception worth correcting.** The ban
covers inferring emotions from biometric data specifically in **workplace and education**
settings, and **explicitly carves out uses for "medical or safety reasons"** (detecting patient
distress, pilot fatigue). Systems assessing physical states (pain, fatigue) rather than
"emotion" are also outside the ban. **General clinical emotion/affect-inference tools are not
prohibited by Article 5.**

**US contrast — the deregulatory trajectory.**
- **Jan 20, 2025** — Trump EO 14148 rescinded Biden's EO 14110 ("Safe, Secure, and Trustworthy
  Development and Use of AI," Oct 2023)
- **Jan 23, 2025** — EO 14179, "Removing Barriers to American Leadership in Artificial
  Intelligence," framing the Biden EO as having "hindered AI innovation" via "onerous...
  government control"
- **July 23, 2025** — White House "AI Action Plan" released
- A **10-year moratorium on new state AI regulation** was included in the "One Big Beautiful
  Bill Act" but **stripped by a 99–1 Senate vote** after bipartisan pushback
- **Dec 11, 2025** — EO "Ensuring a National Policy Framework for Artificial Intelligence,"
  pursuing federal preemption of state AI law via DOJ litigation, administrative
  reinterpretation, and conditional federal funding rather than direct statutory preemption.
  Legal analysts (Ropes & Gray, Sidley) note **an EO cannot itself preempt state law** absent
  Congressional action or a court ruling — so state AI laws (including state health-AI
  transparency and consent statutes) **remain enforceable as of Aug 2026**, but under active
  federal pressure.

**The teaching contrast:** the EU has just *delayed* — not abandoned — binding high-risk
obligations under sustained industry and implementation pressure, while the US has *rescinded*
federal AI safety oversight and is now attempting (so far unsuccessfully at the legislative
level) to preempt state-level AI regulation entirely.

### 5.5 Hallucination and safety in clinical use

**Automation bias — Jabbour et al., *JAMA* 2023.** Jabbour S et al., "Measuring the Impact of
AI in the Diagnosis of Hospitalized Patients: A Randomized Clinical Vignette Survey Study,"
*JAMA* 2023;330(23):2275–2284.
[DOI](https://doi.org/10.1001/jama.2023.22295) (PMID 38112814). Per PubMed:
- Vignette survey, **457 clinicians** (hospitalists, NPs, PAs), 13 US states, April 2022–Jan
  2023, NCT06098950.
- Baseline diagnostic accuracy **73.0%** (95% CI 68.3–77.8).
- Standard AI model (no explanation): **+2.9 points**; with explanations: **+4.4 points**.
- **Systematically biased AI model: −11.3 points** vs baseline (95% CI −7.2 to −15.5).
- Biased AI + explanations: **−9.1 points** — **explanations did NOT significantly mitigate
  the harm** (nonsignificant 2.3-point improvement, CI crosses zero).
- *Conclusion:* biased models degrade clinician accuracy, and commonly-used image-based
  explanations don't fix it. **This is the single strongest study for teaching automation
  bias.**

**MedHallu benchmark.** Confirmed to exist and actively used as a standard medical-QA
hallucination benchmark in 2026 literature — e.g. one of four benchmarks (with Endoscopy,
PubMedQA, MedQA-USMLE) in Yu & Liu, *J Biomed Inform* 2026,
[DOI 10.1016/j.jbi.2026.105081](https://doi.org/10.1016/j.jbi.2026.105081) (PMID 42447946),
and in Chakraborty et al., *IEEE J Biomed Health Inform* 2026,
[DOI 10.1109/JBHI.2026.3680772](https://doi.org/10.1109/JBHI.2026.3680772) (PMID 41941786).
**⚠ The originating MedHallu paper's own citation was not directly retrieved** — flag if you
need the founding paper rather than downstream usages.

**Whisper ASR hallucination — AP investigation, Oct 26, 2024.** (AP original not
re-verified directly; corroborated across Fortune, TechCrunch/Futurism, Healthcare Brew,
Slator.)
- OpenAI's Whisper hallucinates — fabricates content — more than any other ASR tool the
  engineers and researchers interviewed had seen.
- **Nabla**, building a Whisper-based medical documentation tool, told AP the product was used
  by **30,000+ clinicians and 40+ health systems**, covering **~7 million medical visits**.
- A machine-learning engineer who studied 100+ hours of Whisper transcripts found
  hallucinations in **more than half**; a University of Michigan researcher studying public
  meetings found hallucinations in **8 of 10** transcriptions.
- Hallucinated content included **invented medical treatments and medications** and fabricated
  statements never spoken.
- [Fortune](https://fortune.com/2024/10/26/openai-transcription-tool-whisper-hallucination-rate-ai-tools-hospitals-patients-doctors) ·
  [Healthcare Brew](https://www.healthcare-brew.com/stories/2024/11/18/openai-transcription-tool-whisper-hallucinations) ·
  [Slator](https://slator.com/openais-whisper-faces-bad-press-for-hallucinations-in-healthcare-transcription/).
  Academic follow-up: arXiv 2501.11378, arXiv 2502.12414.

**Deskilling — colonoscopy ADR decline.** "Endoscopist deskilling risk after exposure to
artificial intelligence in colonoscopy: a multicentre, observational study," *Lancet
Gastroenterology & Hepatology* 2025, PII S2468-1253(25)00133-5
([abstract page](https://www.thelancet.com/journals/langas/article/PIIS2468-1253(25)00133-5/abstract)).
- 4 endoscopy centres in Poland; AI polyp-detection introduced end of 2021; part of the
  **ACCEPT trial**. 19 experienced endoscopists (2,000+ procedures each).
- ADR at **non**-AI-assisted colonoscopies: **28.4% before AI exposure → 22.4% after** regular
  AI exposure — a **20% relative / ~6-percentage-point absolute decline.**
- **⚠ The primary Lancet abstract returned 403 on fetch; percentages come from secondary
  summaries. Verify the exact figures and publication month at the Lancet URL before citing.**
  Corroborating: [EurekAlert](https://www.eurekalert.org/news-releases/1094223) ·
  [Univ. Oslo](https://www.med.uio.no/helsam/english/research/groups/clinical-effectiveness/news/2025/ai-colonoscopy.html) ·
  [ACG EBGI](https://gi.org/journals-publications/ebgi/zhou_sep2025/)
- **Do not conflate** with PMID 36719680 (*JAMA Netw Open* 2023, colonoscopy time-of-day and
  AI) — that found AI helped *offset* time-of-day ADR decline, the opposite direction.

**Patient-facing chatbot safety incidents.**
- **NEDA "Tessa" chatbot (2023).** NEDA replaced its human-staffed helpline with the Tessa
  chatbot; it gave harmful advice to eating-disorder patients — recommending a 500–1000
  calorie/day deficit, weekly weigh-ins, calorie counting, and skin-caliper body-fat
  measurement, directly contradicting ED-recovery best practice. NEDA suspended the bot.
  [NPR](https://www.npr.org/sections/health-shots/2023/06/08/1180838096/an-eating-disorders-chatbot-offered-dieting-advice-raising-fears-about-ai-in-hea) ·
  [AI Incident Database #545](https://incidentdatabase.ai/cite/545/)
  **Note this is 2023, predating the 2024–2026 window, but remains the canonical teaching
  case.**
- **⚠ GAP:** 2024–2026 patient-facing chatbot safety incidents were **not researched** — the
  search budget ran out. See the Character.AI/OpenAI litigation in §5.2 as partial coverage,
  but a targeted follow-up search is recommended.

### 5.6 Professional guidance

**AMA.** AMA hosts a "Physician Survey on Augmented Intelligence" page
([link](https://www.ama-assn.org/practice-management/digital-health/physician-survey-augmented-intelligence)).
From secondary synthesis: the **~66% figure is real — 66% of physicians reported using AI in
2024, up from 38% in 2023**, per an AMA report published **February 2025**. A **2026 survey
(published ~March 2026)** reportedly shows adoption at **81%** and physician-perceived-
advantage sentiment over 75% (up from 65% in 2023), with clinical documentation the top use
case (68%).
**⚠ The 2025/2026 figures come from secondary summaries (ASCO Post, Fierce Healthcare, TexMed)
of an AMA PDF that could not be read directly (returned as binary). Verify exact wording and
percentages against [the AMA PDF](https://www.ama-assn.org/system/files/physician-ai-sentiment-report.pdf)
before using in course materials.**
**⚠ AMA's core Augmented Intelligence *policy principles* text (distinct from the survey) was
not independently verified — flag for verification at ama-assn.org.**

**WHO guidance on large multi-modal models (Jan 2024) — confirmed.** "Ethics and governance of
artificial intelligence for health: guidance on large multi-modal models," released **18
January 2024**. Over 40 recommendations for governments, technology companies, and health
providers, covering LMM use in research, drug development, diagnosis and clinical care,
medical and nursing education, administrative tasks, and patient-facing use. Names privacy and
bias as risks spanning all three phases (development, provision, deployment).
**⚠ who.int was not fetched directly — confirm the URL before distributing.**

**AAMC — two distinct documents, both confirmed.**
1. **"Principles for Responsible AI in Medical School and Residency Selection"** — convened via
   a technical advisory committee starting Feb 2024; six guiding principles including "Balance
   Prediction and Understanding."
   [aamc.org](https://www.aamc.org/about-us/mission-areas/medical-education/principles-ai)
2. **"Principles for the Responsible Use of Artificial Intelligence in and for Medical
   Education"** — broader curriculum-integration principles (transparency and disclosure to
   learners, evaluating AI tools in their actual context of use). **Version 1.0 completed Jan
   3, 2025; Version 2.0 completed July 31, 2025** — actively iterated.
   [aamc.org](https://www.aamc.org/about-us/mission-areas/medical-education/principles-ai-use)
   **This is the most directly relevant governing document for this elective.**

**NAM AI Code of Conduct — ⚠ COULD NOT CONFIRM.** The expected URL 404'd and the search budget
ran out. NAM launched an AI Code of Conduct initiative around 2023–2024, but **current
2025–2026 status could not be certified from a primary source. Check nam.edu before citing.**

**ACGME / LCME AI expectations — ⚠ NOT RESEARCHED.** The search budget was exhausted before
this item. **Do not state a definitive ACGME or LCME position without a follow-up search of
acgme.org and lcme.org.** This is a real gap, not an omission in the writing.

### 5.7 Activities — Area 5

*(Written from the research above rather than supplied by the research passes.)*

**Activity 5.A — FDA reviewer role-play: is this a device? (60 min).**
Present 5 short product descriptions on one slide, spanning the regulatory boundary: (1) a
sepsis-risk score displayed in the EHR with no rationale shown; (2) a tool that surfaces
matching guideline text for a clinician to read; (3) an autonomous diabetic-retinopathy
screener; (4) an ambient scribe that drafts an assessment and plan; (5) a general-purpose LLM
a resident uses to generate a differential. Breakout groups of 4–5 apply the **non-device CDS
criteria** and decide device / not-device / genuinely unclear, and if a device, what pathway.
*Debrief:* reveal that the boundary itself moved — the Sept 2022 guidance was replaced Jan 6,
2026 — and that **as of March 2026 no generative-AI device had been authorized at all** even
as LLM use is widespread clinically. The gap between what is regulated and what is used is the
lesson.

**Activity 5.B — Liability moot court (60–75 min).**
Fact pattern: a physician follows an AI recommendation that departs from standard of care; the
patient is harmed. Three breakout teams — plaintiff, defense, and a "judge" panel — argue
using the Price/Gerke/Cohen 2×2 framework. Then **re-run the same fact pattern with the
physician having *rejected* a correct AI recommendation** and argue again.
*Debrief:* draw out the uncomfortable structural finding — current tort law makes following
standard of care the safest position regardless of whether the AI was right, which
systematically discourages exactly the AI use that would most change management. Close with
the fact that **no US clinical-AI malpractice case has reached verdict as of 2026**, so
students are arguing genuinely open law.

**Activity 5.C — Write the consent script (45 min).**
Groups of 4–5 each draft a verbal consent script (≤60 seconds of speech) for one scenario: an
ambient scribe recording the visit; an AI-drafted portal reply; an AI sepsis alert influencing
admission; an AI-assisted radiology read. Constraints: plain language at roughly 6th-grade
level, must state what the AI does and does not decide, and must offer a real opt-out.
*Debrief:* groups read scripts aloud and the class votes on which they'd accept as a patient.
Anchor to the Pew 60%-uncomfortable figure, the 79% opposition to mental-health chatbots, and
the **Sutter and Sharp class actions arguing HIPAA compliance alone is not informed consent**.
Note that ~13 states require all-party consent and Florida makes non-consensual recording a
felony — the script is not a formality.

**Activity 5.D — Mock institutional AI governance committee (75 min).**
The class is an institutional AI review committee. Present one proposed deployment (an ambient
scribe across primary care, or an LLM-based inbox reply drafter). Assign standing roles across
breakout rooms: clinical champion, compliance/privacy officer, health-equity officer, IT
security, patient advocate, finance. Each room prepares its position and two questions it
would require answered before approval. Plenary: run the committee, take a vote.
*Toolkit:* the HTI-1 31 predictive-DSI source attributes as the transparency checklist, the
Epic AI Trust and Assurance Suite as the monitoring mechanism, CHAI model cards as the vendor
disclosure format — and the CHAI/HHS political fight as evidence that **who gets to set these
standards is itself unsettled.**

**Activity 5.E — Hallucination hunt with a safety lens (45 min).**
Distinct from Activity 1.C (which counts fabricated citations). Here, pairs probe a free LLM
with **clinical-safety-relevant** queries — drug dosing in renal impairment, a pediatric
weight-based calculation, a contraindication check — and log any confidently-stated error.
Then present the Jabbour *JAMA* 2023 numbers (biased AI dropped clinician accuracy 11.3
points; explanations did not rescue it) and the Whisper findings (hallucinations in more than
half of transcripts studied; invented medications).
*Debrief:* the pivot question — "you just caught these errors because you were looking for
them. What happens on a busy night float when you are not?" Close on the colonoscopy
deskilling data (ADR 28.4%→22.4% at non-AI-assisted procedures) as evidence that **the risk
isn't only that AI is wrong, it's what sustained AI use does to the clinician.**

**Activity 5.F — EU vs US regulatory contrast, structured comparison (40 min).**
Half the breakout rooms are briefed as EU regulators, half as US. Each drafts the rules they
would apply to one product (an LLM-based triage chatbot). Plenary comparison against what each
jurisdiction actually did: the EU classifying it high-risk via Annex I/MDR interaction but
**deferring the compliance deadline to Dec 2027/Aug 2028** under the Digital Omnibus, versus
the US rescinding the Biden EO, failing 99–1 to preempt state law legislatively, and then
attempting preemption by executive order.
*Debrief:* both jurisdictions moved *away* from near-term binding obligations in 2025–2026,
by different mechanisms and for different stated reasons. Ask students which failure mode
worries them more.

### 5.8 Gaps in Area 5 — must be closed before teaching

1. **FDA AI-enabled device list URL 404'd.** The ~1,451 count and 76%-radiology breakdown are
   secondary (MedTech Dive). Re-verify at fda.gov.
2. **CDS guidance changed January 6, 2026** — do not describe the Sept 2022 guidance as
   current without noting the revision.
3. **No confirmed generative-AI-specific final FDA guidance** — worth one targeted search.
4. **"ChatGPT Health" product name** needs independent verification.
5. **No decided US clinical-AI malpractice verdicts** — do not state or imply otherwise.
6. **Lancet colonoscopy deskilling percentages** — primary abstract blocked by 403; verify.
7. **AMA 2025/2026 survey percentages** — primary PDF unreadable; verify.
8. **AMA Augmented Intelligence policy principles text** — not independently verified.
9. **NAM AI Code of Conduct** — current page and status could not be located.
10. **ACGME / LCME AI expectations** — not researched at all.
11. **2024–2026 patient-facing chatbot safety incidents** — not researched.
12. **MedHallu originating paper** — not directly retrieved.
13. **EU Official Journal publication date** for the Digital Omnibus package — not pinned
    down beyond "third day after publication."
14. **No Pew 2025/2026 follow-up survey found** — 2023 remains the anchor figure.

---

## Master list of items requiring re-verification

Consolidated from all five areas. Items are grouped by how badly a mistake would hurt.

**Would materially mislead students if wrong:**
- Kanjee 2023 *JAMA* exact percentages (PubMed abstract empty; verify against primary PDF).
- FDA AI-enabled device count and specialty breakdown (§5.8 item 1).
- All Area 5 regulatory statuses — this is the fastest-moving material in the report.
- Litigation statuses in §4.4 (Cigna and Humana beyond March 2025; Lokken class-cert timeline).
- Lancet colonoscopy deskilling percentages.
- AMA physician-adoption percentages for 2025/2026.

**Would weaken a claim but not invert it:**
- NRMP 2024/2026 exact fill rates and position counts.
- Sjoding *NEJM* 2020 PMID confirmation.
- eGFR "two-thirds of labs" adoption figure.
- BLS medical-transcriptionist projection wording.
- State AI-in-UM law count (14–15 vs 7 — two unreconciled lists).
- Microsoft emissions figure (three different numbers, three different scopes).

**Citations that may not resolve at all — check before assigning as reading:**
- arXiv 2604.22604 ("Vibe coding for clinicians").
- Frontiers frai.2026.1882814 (VIBE-HI framework).
- doi.org/10.3390/ai7060223 (WWAMI ECG app study).
- PDSQI-9 (preprint/AMIA only, not a peer-reviewed journal article).
- MAI-DxO (preprint/industry report, not peer-reviewed).
- 2025–2026 LLM bias follow-ups (psychiatric-diagnosis audit; "EQUITRIAGE").

**Known holes, not yet researched:**
- ACGME/LCME AI expectations (Area 5).
- 2024–2026 patient-facing chatbot safety incidents (Area 5).
- NAM AI Code of Conduct current status (Area 5).
- National whole-slide-imaging adoption rate for pathology (Area 4).

---

## Cross-cutting notes for module design

**Which activities carry a full session.** The strongest anchors for a 60–90 min block are
4.B (algorithm bias audit), 4.F (economics briefing), 5.D (governance committee), 2.A (first
build), and 1.C (fabrication hunt). Each has enough structure to fill the time and produces
something concrete.

**Which are 20–30 min add-ons.** 3.A (footprint estimation), 3.D (model ranking), 1.F (tool
bake-off). These work well as openers or closers alongside a didactic block.

**A natural throughline across the four weeks.** Several areas independently converge on the
same lesson, and saying so explicitly is stronger than teaching them as separate topics:
- **Proxies fail.** Cost stands in for need (Obermeyer); light skin stands in for normal
  reflectance (pulse ox); a benchmark stands in for clinical performance (MAI-DxO, FDA
  clearance data).
- **Efficiency gains get eaten by volume.** Jevons appears in the environmental data (Google's
  33x per-prompt gain against rising total emissions) *and* in the workforce data (imaging AI
  against rising imaging demand) *and* in the economics (PHTI's "bot wars").
- **The published number is usually the optimistic one.** Pre/post pilots from self-selected
  adopters beat RCTs (AI scribes); vendor benchmarks beat clinical validation (device
  clearances); industry preprints beat peer review (MAI-DxO).

**Two guardrails that belong in every session, not just the build session:** no PHI in any
consumer-tier tool, and verify before trusting. Pin both in Zoom chat.

**Practical Zoom logistics.** Cap breakouts at 4–5 students for genuine participation (~8–10
rooms for 40 students). Any activity requiring accounts — OpenEvidence, Doximity GPT,
Claude.ai, Google — needs students set up **before** the session; account creation alone can
consume 10+ minutes of a 60-minute block.

---

## Appendix: existing Colab notebooks (recovered and verified)

The `vibe-coding` deck ("AI-Powered Medicine: Building the Tools You Wish
Existed", IDPT 8079, Oct 2025) references two Colab notebooks that appear nowhere
in the talks repo. Both were recovered from Drive and decoded from raw `.ipynb`
JSON:

- **`ai-data-analysis-example-idpt-8079.ipynb`** — the student starter, 3 cells
  (1 code, 2 markdown). Introduces Python and notebooks, loads the Kaggle
  insurance dataset via `pandas.read_csv` from a public URL, then instructs the
  student to use Colab's built-in "generate" AI-code feature with the prompt
  *"Produce a text description of the data in the insurance data."*
- **`ai-data-analysis-example-completed-idpt-8079.ipynb`** — the completed twin,
  27 cells (9 code, 18 markdown): the same introduction plus a full Colab Data
  Science Agent regression workflow — one-hot encoding, train/test split, Linear
  Regression vs. Gradient Boosting, MAE/MSE/R², and feature importance. The
  agent's own summary finds `smoker_yes` dominant (importance 0.678), then `bmi`
  (0.186) and `age` (0.118), with Gradient Boosting outperforming Linear
  Regression (R² 0.88 vs 0.78).

**Both run in a browser with zero setup.** Verified mechanically: only `pandas`
and `scikit-learn` (both pre-installed in Colab), three public URLs, and **no API
key, login, file upload, or pip install in either**. The only requirement is being
signed into Colab to use the "generate" feature.

These pair naturally with `core-foundations` — the insurance dataset is the same
one behind the recovered ml-intro cost example, and the completed notebook is a
readable artifact of an AI agent executing a whole modeling workflow, including
choices a student should be able to question. The completed notebook is also a
ready-made critical-appraisal object: ask students what the agent decided without
being asked, and what a clinician would want to know before believing R² = 0.88.
