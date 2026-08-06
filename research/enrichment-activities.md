# Enrichment research: hands-on activities, impacts, ethics

Compiled August 2026 from five parallel research threads. **Read the caveats.**
Several sub-agents flagged their own claims as unverified or fast-moving; those
flags are preserved deliberately and must not be smoothed away. Anything marked
**[VERIFY]** should be re-checked against a primary source before it goes on a
slide.

Sections 1–4 are complete. Section 5 (ethics and regulation) is **PENDING** — the
fork completed but its report did not reach the compiler; see the note at the end.

---

## 1. Hands-on LLM activities

### Evidence base

**Prompt-engineering exercises with clinical vignettes.** Published classroom
material here is thinner than the diagnostic-accuracy literature, but two recent
peer-reviewed pieces are directly relevant:

- Waldock WJ, Lam G, Baptista A, Walls R, Sam AH. "Which curriculum components do medical students find most helpful for evaluating AI outputs?" *BMC Med Educ* 2025;25(1):195. [doi:10.1186/s12909-025-06735-5](https://doi.org/10.1186/s12909-025-06735-5). Final-year Imperial students (n=148) evaluated GPT-3.5 answers to 10 clinical vignettes, 5 deliberately wrong. Median correct-evaluation rate **56%**. Students credited case-based/pathology teaching — not AI training — for catching errors. Only **5%** had heard of "clinical prompt engineering." Good justification-of-need slide.
- Choy BC, Shanmugam H, Redden HW, et al. "Artificial Intelligence and Large Language Models: A Case-Based, Peer-Teaching Workshop for Preclinical Medical Students." *MedEdPORTAL* 2026;22:11621. [doi:10.15766/mep_2374-8265.11621](https://doi.org/10.15766/mep_2374-8265.11621). A **reusable published module**: 60-min lecture plus 100-min case workshop, Harvard preclinical, n=168. Significant knowledge/self-efficacy gains (p<.01); attitude items mixed. Closest thing to a ready-made template — worth pulling the full module for structure and timing.

**LLMs and differential diagnosis** — the four studies worth teaching:

- Goh E, Gallo R, Hom J, et al. "Large Language Model Influence on Diagnostic Reasoning: A Randomized Clinical Trial." *JAMA Netw Open* 2024;7(10):e2440969. [doi:10.1001/jamanetworkopen.2024.40969](https://doi.org/10.1001/jamanetworkopen.2024.40969). 50 physicians. LLM access did **not** significantly improve physician performance (adjusted difference +2 points, 95% CI −4 to 8, p=.60) — but the **LLM alone scored 16 points higher** than physicians using conventional resources (95% CI 2–30, p=.03). The single best discussion piece in this literature.
- Kanjee Z, Crowe B, Rodman A. "Accuracy of a Generative Artificial Intelligence Model in a Complex Diagnostic Challenge." *JAMA* 2023;330(1):78–80. [doi:10.1001/jama.2023.8288](https://doi.org/10.1001/jama.2023.8288). **[VERIFY]** — PubMed returned an empty abstract field; confirm exact percentages against the primary PDF before quoting.
- Tu T, Schaekermann M, Palepu A, et al. "Towards conversational diagnostic artificial intelligence." *Nature* 2025;642(8067):442–450. [doi:10.1038/s41586-025-08866-7](https://doi.org/10.1038/s41586-025-08866-7). Google's AMIE vs. 20 PCPs, randomized double-blind crossover, 159 scenarios. AMIE superior on 30/32 specialist-rated axes and 25/26 patient-actor axes. Limitation worth teaching: synchronous text chat is not clinical practice.
- McDuff D, Schaekermann M, Tu T, et al. "Towards accurate differential diagnosis with large language models." *Nature* 2025;642(8067):451–457. [doi:10.1038/s41586-025-08869-4](https://doi.org/10.1038/s41586-025-08869-4). 302 challenging cases. AMIE standalone top-10 accuracy **59.1% vs 33.6%** unassisted clinicians; clinicians *assisted* by AMIE reached 51.7% vs 36.1% unassisted and 44.4% with search engines.
- Microsoft **MAI-DxO** (arXiv:2506.22405) — solved up to **85.5%** of 304 NEJM-CPC-derived cases vs. ~20% for 21 physicians. **This is a preprint/industry tech report, not peer-reviewed**, run on curated hard cases under constrained conditions (no open internet). Teach it as a benchmark claim, not validated performance. It is an excellent object lesson in reading vendor numbers.

**Patient communication:**

- Ayers JW, Poliak A, Dredze M, et al. *JAMA Intern Med* 2023;183(6):589–596. [doi:10.1001/jamainternmed.2023.1838](https://doi.org/10.1001/jamainternmed.2023.1838). 195 r/AskDocs exchanges; evaluators preferred chatbot responses in **78.6%** of 585 evaluations. Chatbot responses were rated good/very good 78.5% vs 22.1%, and empathetic/very empathetic 45.1% vs 4.6% — but were **4x longer** (median 211 vs 52 words).
- Garcia P, Ma SP, Shah S, et al. *JAMA Netw Open* 2024;7(3):e243201. [doi:10.1001/jamanetworkopen.2024.3201](https://doi.org/10.1001/jamanetworkopen.2024.3201). Stanford, 162 clinicians. AI-draft utilization ~20%; **no significant change in reply time**, but significant drops in task load (61.31→47.26, p<.001) and work exhaustion (1.95→1.62, p<.001). The counter-example to "AI saves time" — it reduced burden, not clock time.
- Fereydooni S, Homer R, Chartash D. *Patient Educ Couns* 2026;149:109597. [doi:10.1016/j.pec.2026.109597](https://doi.org/10.1016/j.pec.2026.109597). GPT-4-turbo rewrote 44 prostate pathology reports; significant complexity reduction (p<.001), academic vocabulary 68.47→23.16.
- Monaci M, Viviani E, Sottotetti F, Bigi S, Barello S. *Patient Educ Couns* 2026;149:109702. [doi:10.1016/j.pec.2026.109702](https://doi.org/10.1016/j.pec.2026.109702). Argues readability scores alone are insufficient; proposes comprehensibility, relevance, usability, emotional impact, empowerment. Good basis for a student-facing evaluation checklist.

**Hallucination and fabricated citations** — strong, quantified, teachable:

- Gravel J, D'Amours-Gravel M, Osmanlliu E. *Mayo Clin Proc Digit Health* 2023;1(3):226–234. [doi:10.1016/j.mcpdig.2023.05.004](https://doi.org/10.1016/j.mcpdig.2023.05.004). Of 59 references across 20 medical questions, **41 (69%) were fabricated**.
- McGowan A, Gui Y, Dobbs M, et al. *Psychiatry Res* 2023;326:115334. [doi:10.1016/j.psychres.2023.115334](https://doi.org/10.1016/j.psychres.2023.115334). Of 35 citations, **only 2 were real**.
- McLaughlin ND, Srinivas AN, Lowe ZF, et al. *Neurosurg Pract* 2026;7(3):e000244. [doi:10.1227/neuprac.0000000000000244](https://doi.org/10.1227/neuprac.0000000000000244). Five tools scored 2/1/0 (accurate/misrepresented/fabricated). **OpenEvidence: zero fabrications** (indexes PubMed directly). Claude most accurate among general-purpose models (78.0%); Gemini worst (26.2% fabrication). Striking finding: **ChatGPT's fabrication rate rose from 2.1% on clinician-framed prompts to 20.0% on patient-framed prompts** — prompt framing changes hallucination risk.
- Frutuoso Maia BK, et al. *Br J Oral Maxillofac Surg* 2026;64(3):216–222. [doi:10.1016/j.bjoms.2026.01.002](https://doi.org/10.1016/j.bjoms.2026.01.002). GPT-4 36% hallucinated citations vs Gemini 14%, DeepSeek 8.8% (p<.00001).
- Shah R, Miranda JL. *J Microbiol Biol Educ* 2026;e0019525. [doi:10.1128/jmbe.00195-25](https://doi.org/10.1128/jmbe.00195-25). The one published **classroom-exercise framework** built around AI citation errors. Biology, not medicine, but directly portable.

### Tools (August 2026)

| Tool | Access | PHI note |
|---|---|---|
| ChatGPT free | Free account | Consumer tier, no BAA — no PHI |
| Claude.ai free | Free account | Consumer tiers explicitly outside Anthropic's BAA — no PHI |
| Gemini / NotebookLM | Free Google account; NotebookLM 100 notebooks, 50 sources each, 50 queries/day | Consumer tier — no PHI |
| OpenEvidence | Free for verified US clinicians **and medical students** (student ID/transcript); NEJM and JAMA content partnerships | Vendor markets as HIPAA-compliant; verify institutional policy |
| Doximity GPT | Free for verified physicians, NPs, PAs, **and medical students** | Vendor states HIPAA/BAA support; verify |
| Consensus / Elicit / Perplexity | Free tiers with query limits | Literature tools — no PHI |
| Abridge / Nabla | Enterprise only, no meaningful student free trial | Enterprise BAA required; do not demo with real audio |

**Practical conclusion:** ChatGPT free, Claude.ai free, and Gemini/NotebookLM are
the only frictionless zero-verification options for a live session. OpenEvidence
and Doximity GPT are free and excellent but need pre-session identity
verification — have students set accounts up *before* class.

### Rubrics

- **PDSQI-9** (Provider Documentation Summarization Quality Instrument), developed with Epic: Cited, Accurate, Thorough, Useful, Organized, Comprehensible, Succinct, Synthesized, non-Stigmatizing (arXiv:2501.08977). **[VERIFY]** — preprint/conference-validated, not a peer-reviewed journal article. Clean 9-item rubric, well suited to breakout scoring.
- McLaughlin et al.'s 0/1/2 citation-accuracy scale is trivially reusable as a scoring key.
- Monaci et al. 2026 for patient-communication-specific evaluation beyond readability.

### Activity designs

1. **Naive vs. engineered prompt diagnostic lab (45 min).** Groups run a synthetic vignette with no prompt engineering, then re-run with a structured prompt (role, differential, supporting/opposing findings, next diagnostic step, specified format), then score both against a held answer key. Debrief on Waldock (only 5% knew the term) and Goh (the LLM alone beat physicians using it).
2. **Journal club jigsaw (40 min).** Four groups, four papers (Goh; Kanjee; the AMIE pair; MAI-DxO). Each produces study design, population, one major limitation. Seed question: "MAI-DxO reports 85.5% vs 20% — why might that comparison mislead?"
3. **Fabrication hunt (40 min).** Pairs ask a chatbot a clinical question, request 5 references, verify each against PubMed, score 2/1/0. Compile a class-wide fabrication rate and compare to published rates. Debrief on why retrieval-grounded tools differ structurally.
4. **Patient message and discharge rewrite (45 min).** Draft an empathetic reply and rewrite discharge instructions to 6th-grade level; check with a Flesch-Kincaid tool; then edit as the attending signing off. Debrief on Ayers (more empathetic but 4x longer — what gets cut?) and Garcia (burnout down, time unchanged — is that still worth it?).
5. **Apply a clinical-AI rubric (40 min).** Score one strong and one flawed AI output on all nine PDSQI-9 dimensions via a shared form; reveal cross-group variance and discuss inter-rater reliability.
6. **Free-tool bake-off (25 min).** Same clinical question through 2–3 tools; compare citations, differential, concision. Close on the PHI reminder.

---

## 2. Agentic coding for non-programmers

Fully written up as a module in `modules/enrichment-agentic-coding.md`. Key
research points retained here:

**Origin and current status.** Karpathy coined "vibe coding" February 2, 2025;
Collins Dictionary named it 2025 Word of the Year. By February 2026 Karpathy
himself called it "passé," proposing "agentic engineering" — orchestrating and
overseeing agents rather than accepting output blindly, with technical mastery
"even more of a multiplier than before." **[VERIFY]** the 2026 Karpathy items
against primary sources before quoting.

**Documented failure modes.** 40–62% of AI-generated code samples carry security
vulnerabilities in benchmark testing. A scan of 1,400+ vibe-coded production apps
found 65% with security issues, 58% with at least one critical vulnerability.
Reported 30–41% increases in technical debt after AI-tool adoption. **[VERIFY]**
— several of these figures come from vendor and trade sources rather than peer
review; treat as directional.

**Tool ranking for a zero-setup Zoom session.** Claude.ai Artifacts and Google AI
Studio / Gemini Canvas are the only two options with no card, durable free tier,
true browser-only operation, no seat/file caps, and fast enough generation.
Bolt.new is a solid third. **Excluded**: Claude Code and GitHub Copilot (both
require local install; Copilot's student sign-ups were additionally paused in
April 2026 **[VERIFY]**).

**Clinician-builder literature.**
- Moore JH, Tatonetti N. *BioData Mining* 2025 — editorial on vibe coding democratizing biomedical informatics ([PMC12217882](https://pmc.ncbi.nlm.nih.gov/articles/PMC12217882/)).
- "How Can Clinicians Leverage Vibe Coding for Machine Learning and Deep Learning Research?" ([PMC12602019](https://pmc.ncbi.nlm.nih.gov/articles/PMC12602019/)).
- Alqheedan & Alzughaibi, "The VIBE-HI framework," *Front Artif Intell* 2026 ([doi:10.3389/frai.2026.1882814](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2026.1882814/full)). Names **"comprehension abdication"** — a clinician deploying code they cannot explain or safely modify — as the central hazard, with four-tier risk stratification mapping to HIPAA/IEC 62304/FDA SaMD/EU AI Act. **The single most reusable guardrail framework for this course.**
- MDPI *AI* 2026;7(6):223 ([doi:10.3390/ai7060223](https://doi.org/10.3390/ai7060223)) — a faculty member vibe-coded an ECG-interpretation app for M1s, evaluated against five control sites with uMARS. **Results on exam performance were mixed and inconsistent** — a useful corrective to build-it-fast enthusiasm.

---

## 3. Environmental impact

### Data center electricity

- **IEA, "Energy and AI" (April 2025):** global data center demand projected to more than double to **~945 TWh by 2030**, just under 3% of global electricity. AI-optimized data centers **triple** 2025→2030. US and China are ~80% of growth. Data center electricity use **surged 17% in 2025**, over 5x faster than overall demand growth. [IEA](https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai)
- **LBNL 2024 US Data Center Energy Usage Report:** US data centers used **176 TWh in 2023 = 4.4% of US electricity**. Growth accelerated from ~7%/yr (2014–18) to ~18%/yr (2018–23). 2028 projection **325–580 TWh, or 6.7%–12% of US electricity**. [PDF](https://eta-publications.lbl.gov/sites/default/files/2024-12/lbnl-2024-united-states-data-center-energy-usage-report_1.pdf)
- **EPRI:** projects **9–17% of US electricity by 2030** (380–790 TWh). **[CONFLICTING]** with LBNL — different methodology and AI-adoption assumptions. Present as a range with the caveat; do not collapse to one number. [EPRI](https://powering-intelligence.epri.com/load-growth.html)

### Per-query inference energy — the best teaching point in this section

| Source | Figure | Status |
|---|---|---|
| Google, Aug 2025 | Median Gemini text prompt: **0.24 Wh, 0.03 gCO2e, 0.26 mL water**; 33x energy / 44x carbon reduction per prompt in 12 months | Technical paper, [arXiv:2508.15734](https://arxiv.org/abs/2508.15734), full-stack methodology |
| Sam Altman blog, June 2025 | ChatGPT average **0.34 Wh, ~0.32 mL water** | **Not peer-reviewed, no methodology disclosed**, ambiguous "average" |
| Epoch AI 2025 | ~**0.3 Wh** convergent; challenges the viral "~3 Wh" figure as overestimate | Independent, transparent method |
| MIT Tech Review, May 2025 | Llama 3.1 8B ~114 J with cooling; 405B ~6,706 J ≈ a microwave for 8 seconds | Independently measured; ~60x spread by model size |
| Jegham et al., [arXiv:2505.09598](https://arxiv.org/abs/2505.09598) | Most intensive proprietary models exceed **29 Wh per long prompt** — >65x the most efficient | Infrastructure-aware benchmarking, 30 models |

**Why they vary:** model size, output/reasoning length, batching, hardware
generation, datacenter PUE, and whether idle capacity, cooling, and amortized
training are counted. *"Per-query energy" is not one number* — that is the lesson.

**The "10x a Google search" claim** traces to de Vries, *Joule* 2023
([doi:10.1016/j.joule.2023.09.004](https://www.sciencedirect.com/science/article/pii/S2542435123003653)),
and the widely-repeated framing compares it against a **2009 Google blog figure**
for search energy. It assumes 100% chip utilization and ignores subsequent
efficiency gains. Teach it as an example of a number that outran its evidence.

### Training footprint

- GPT-3: **1,287 MWh, 552 tCO2e** (Patterson et al., [arXiv:2104.10350](https://arxiv.org/pdf/2104.10350)).
- BLOOM 176B: 433,195 kWh; **24.7 tCO2e** dynamic, **50.5 tCO2e** including embodied carbon (Luccioni et al., [arXiv:2211.02001](https://arxiv.org/abs/2211.02001)).
- Llama 3.1 (Meta model card, verified): 8B 1.022 GWh/420 tCO2e; 70B 4.9 GWh/2,040 tCO2e; 405B 21.588 GWh/**8,930 tCO2e**. Total **27.51 GWh, 11,390 tCO2e location-based — but 0 tCO2e market-based** via renewable PPAs. A clean illustration of location-based vs. market-based accounting. [Model card](https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md)
- Luccioni, Jernite & Strubell, FAccT 2024 ([doi:10.1145/3630106.3658542](https://dl.acm.org/doi/10.1145/3630106.3658542)): multi-purpose generative models cost orders of magnitude more per task than fine-tuned task-specific models, and **cumulative inference can rival or exceed training cost**.
- **[DATA GAP]** No comparable disclosed training-energy figures exist for GPT-4, Gemini, or Claude-generation models. Labs largely stopped publishing them. That silence is itself teachable.

### Water

- Li et al., [arXiv:2304.03271](https://arxiv.org/abs/2304.03271): training a GPT-3-scale model can directly evaporate **~700,000 L** of freshwater; global AI water withdrawal projected at **4.2–6.6 billion m³ by 2027**.
- Google 2025 environmental report: data-center water consumption rose **4.3B gallons (2021) → 6.1B gallons (2024)**.
- US data centers consumed **17.4 billion gallons in 2023**, projected **38–73 billion by 2028**, plus ~800 billion liters indirectly via power-plant cooling.
- **Equity angle:** two-thirds of data centers built or planned since 2022 sit in water-stressed regions. A Newton County, GA facility uses **500,000 gal/day — ~10% of the county's water use**. [Ceres, "Drained by Data"](https://www.ceres.org/resources/reports/drained-by-data-the-cumulative-impact-of-data-centers-on-regional-water-stress)

### Jevons paradox — the throughline

Google's total GHG emissions are **up 48% since 2019** despite the 33x per-prompt
efficiency gain. Microsoft's increase since 2020 is reported as **29.1%** (2024
report), **23.4%** (2025 report), or **80%** (Stand.earth, different scope
including gas buildout). **[CONFLICTING]** — present all three with their scopes;
do not collapse. Per-unit efficiency gains are being outpaced by volume growth.

The **xAI Memphis** case is the sharpest environmental-justice example: ~59 gas
turbines run without Clean Air Act permits in a South Memphis area already rated
"F" for ozone with ~4x national cancer risk; NAACP and SELC litigation followed.
[Earthjustice](https://earthjustice.org/case/xai-illegal-gas-power-plant-data-center-colossus)

### Healthcare angle

- Eckelman MJ, Huang K, Lagasse R, Senay E, Dubrow R, Sherman JD. "Health Care Pollution and Public Health Damage in the United States: An Update." *Health Aff* 2020;39(12):2071–2079. [doi:10.1377/hlthaff.2020.01247](https://doi.org/10.1377/hlthaff.2020.01247). US healthcare emissions **1,692 kg CO2e per capita in 2018**, highest among industrialized nations; **388,000 DALYs lost** to associated pollution. This is the denominator that makes AI's footprint look small — and is the honest framing.
- Sherman JD et al., "The Urgency of Environmentally Sustainable and Socially Just Deployment of Artificial Intelligence in Health Care," *NEJM Catalyst*. [doi:10.1056/CAT.24.0501](https://catalyst.nejm.org/doi/full/10.1056/CAT.24.0501)
- "Sustainability of large-scale artificial intelligence models in health care," *Lancet Digit Health* 2026. [Link](https://www.thelancet.com/journals/landig/article/PIIS2589-7500(26)00039-7/fulltext)
- "Sustainable AI in medicine: balancing benefits and environmental costs," *Nat Rev Nephrol* 2026. [doi:10.1038/s41581-026-01047-3](https://www.nature.com/articles/s41581-026-01047-3)
- **[UNVERIFIED — do not circulate]** The claim that "autonomous AI could reduce healthcare GHG emissions by ~80%" traces to a narrow study of autonomous diabetic-retinopathy screening replacing in-person visits. It is a single-use-case estimate, not a general finding.

### Teaching resources

MIT Technology Review's "We did the math on AI's energy footprint" (May 2025) is
the flagship explainer. [Hugging Face AI Energy Score](https://huggingface.co/spaces/AIEnergyScore/Leaderboard)
rates ~166 models 1–5 stars on standardized benchmarks. [Electricity Maps](https://app.electricitymaps.com)
shows live grid carbon intensity by region — useful for showing that *where* a
model runs matters as much as *how efficiently*.

### Activity designs

1. **"What did this elective cost the planet?" (25 min).** Groups estimate the class's total query energy (40 students × 15 queries/week × 4 weeks = 2,400 queries) before any numbers are shown. Reveal: 0.58 kWh at Google's median, 0.82 kWh at Altman's figure, 69.6 kWh at the long-prompt high end. **The ~120x spread is the lesson**, not any single number. Water parallel: ~624 mL, about 2.6 cups — trivially small individually, which sets up the scale question.
2. **Debate: "Should our hospital restrict clinical AI use on environmental grounds?" (30–35 min).** Both sides get sourced packets. Pro-restriction: rising *total* emissions despite efficiency, xAI Memphis, water-stressed siting. Pro-use: healthcare's own 1,692 kg CO2e/capita baseline dwarfs it, documented efficiency gains, use-cases that cut emissions. Debrief: both sides use real numbers; the disagreement is about scale and counterfactual. Introduce Scope 1/2/3 and the Llama location-vs-market accounting example.
3. **Draft a hospital AI-procurement sustainability memo (30 min).** Groups produce three policy asks a CMIO could use: ask vendors for an AI Energy Score, ask which accounting basis they report, ask where inference is hosted.

---

## 4. Social and economic impacts

### The Hinton prediction — the single best teaching narrative in the course

In 2016 Geoffrey Hinton said: *"People should stop training radiologists now.
It's just completely obvious within five years deep learning is going to do
better than radiologists."* In a May 2026 NYT interview he acknowledged he "spoke
too broadly," said he meant only narrow image analysis, and now predicts a
radiologist-plus-AI combination. Wrong on mechanism, not just timing.
**[VERIFY]** — the 2026 interview was accessed via secondary reporting (paywalled).

**What actually happened in radiology:**

| Year | Positions offered | Fill rate | Applicants |
|---|---|---|---|
| 2025 | 1,451 (+5.2%) | 97.4% | 1,759 (−6.4%) |
| 2026 | 1,478 (record high) | ~98.4% diagnostic | 1,741 (−14% from 2023 peak) |

**[VERIFY]** — these came from secondary reporting; confirm against the
[NRMP 2026 primary PDF](https://www.nrmp.org/wp-content/uploads/2026/05/Main_Match_Results_and_Data-2026.pdf)
before slide use. Also: >1,400 openings on the ACR Career Center; attrition
roughly doubled 2014→2022; ACR/Neiman projects the workforce 20.9% larger by 2055
against 17–27% imaging-demand growth. Doximity 2025 reports average diagnostic
radiologist compensation **$571,749, up 7.5%** — roughly double the average
specialty raise. (A competing figure of $520,000 from a different methodology
exists; **do not merge them**.)

**Why it didn't happen** — Deena Mousa, "AI isn't replacing radiologists"
([understandingai.org](https://www.understandingai.org/p/ai-isnt-replacing-radiologists)):
700+ FDA-cleared radiology AI models exist (~75% of all cleared medical AI), none
displacing labor meaningfully; models generalize poorly off their training
hospital (up to 20-point drops), with 38% of 2024 clearances validated on a single
hospital's data; clearances cluster on flashy conditions (stroke, breast/lung
cancer ≈ 60%) that aren't the case volume; **radiologists spend only ~36% of time
on image interpretation**. Historical precedent: mammography CAD reached 74%
adoption by 2010, but a 430,000-mammogram study found it increased biopsies 20%
with no detection gain; Medicare pulled the extra reimbursement in 2018.
Automation-bias study: clinicians using computer prompts identified only 50% of
malignancies vs. 68% unprompted, and were 26% more likely to follow a wrong call.

Multi-society position (ACR, CAR, ESR, RANZCR, RSNA): "for almost all AI models
with current regulatory approval, the model inference serves to augment, not
replace." ([Radiology: AI](https://pubs.rsna.org/doi/full/10.1148/ryai.230513))

**MS4 takeaway.** The most confident, most credentialed AI-job-elimination
prediction in modern medicine was wrong in both magnitude and direction. Ten years
later radiology shows record positions, near-full fill rates, a documented
shortage, and top-tier salary growth. The transferable lesson is not "AI never
disrupts" — it is that jobs reducible to a narrow benchmarked perceptual task are
rare, and most physician value is judgment under ambiguity, communication,
procedures, and liability-bearing sign-off. Pediatric radiology (2,190→2,032
radiologists, 2016–2023) is the genuine soft spot and a useful nuance against
blanket reassurance.

### Bias and equity — the canonical cases

All PubMed metadata verified except where flagged.

- **Obermeyer Z, Powers B, Vogeli C, Mullainathan S.** "Dissecting racial bias in an algorithm used to manage the health of populations." *Science* 2019;366(6464):447–453. [doi:10.1126/science.aax2342](https://doi.org/10.1126/science.aax2342). PMID 31649194. Verified verbatim: correcting the bias "would increase the percentage of Black patients receiving additional help from **17.7 to 46.5%**." The algorithm optimized for *cost* as a proxy for *need*.
- **Pulse oximetry.** Sjoding MW et al., *NEJM* 2020;383(25):2477–2478 **[VERIFY]** (likely PMID 33326721, not independently re-pulled). Fawzy A et al., *JAMA Intern Med* 2022;182(7):730–738, [doi:10.1001/jamainternmed.2022.1906](https://doi.org/10.1001/jamainternmed.2022.1906), PMID 35639368, verified. Valbuena VSM et al., *BMJ* 2022;378:e069775, PMID 35793817, verified. **FDA status as of Aug 2026: draft guidance issued Jan 7, 2025 proposing premarket diversity requirements rise from 10 to 150 participants across skin tones — still NOT finalized.**
- **Dermatology datasets.** Daneshjou R et al., *Sci Adv* 2022;8(32):eabq6147, [doi:10.1126/sciadv.abq6147](https://doi.org/10.1126/sciadv.abq6147), PMID 35960806. Adamson AS, Smith A, *JAMA Dermatol* 2018;154(11):1247–1248, PMID 30073260 (a Viewpoint, not original research). Fitzpatrick17k (Groh et al., CVPR-W 2021, arXiv:2104.09957) — Fitzpatrick V–VI severely underrepresented. **[VERIFY]** No single canonical citation was found for ISIC skin-tone underrepresentation as a standalone claim.
- **Race-based clinical algorithms.** Vyas DA, Eisenstein LG, Jones DS. "Hidden in Plain Sight." *NEJM* 2020;383(9):874–882, PMID 32853499, verified. NKF-ASN Task Force (Delgado C et al.) published simultaneously in *AJKD* 2021;79(2):268–288 and *JASN* 2021;32(12):2994–3015. **[VERIFY]** Adoption figure — "roughly two-thirds of US labs on race-free eGFR" traces to a single secondary source citing an unspecified survey. Spirometry: Bowerman C et al., *AJRCCM* 2023;207(6):768–774, PMID 36383197; race-neutral GLI-Global equations recommended April 2023, adoption uneven and **actively contested** — 2025 data show reclassification of ~22.7% of Black and ~3.3% of Southeast Asian individuals to greater impairment severity. Unresolved, not settled.
- **Chest X-ray underdiagnosis.** Seyyed-Kalantari L et al., *Nat Med* 2021;27(12):2176–2182, [doi:10.1038/s41591-021-01595-0](https://doi.org/10.1038/s41591-021-01595-0), PMID 34893776. Verified.
- **LLM-specific.** Omiye JA et al., "Large language models propagate race-based medicine," *NPJ Digit Med* 2023;6(1):195, PMID 37864012. Zack T et al., *Lancet Digit Health* 2024;6(1):e12–e22, PMID 38123252. Both verified.

**The throughline for teaching:** every one of these is a **proxy problem** — cost
standing in for need, light skin standing in for "normal" reflectance, race
standing in for unmeasured biology or environment. That single frame unifies the
whole session.

### AI scribes — the evidence-quality lesson

**Pre/post pilot studies (the ones that make headlines):** Kaiser/TPMG, *NEJM
Catalyst* 2024;5(3), [doi:10.1056/CAT.23.0404](https://doi.org/10.1056/CAT.23.0404)
— 3,442 users, 303,266 encounters, no control group. Follow-up: 7,260 physicians,
>2.5M encounters, ~15,700 documentation-hours saved. MGB/Emory (You JG et al.,
*JAMA Netw Open* 2025;8(8):e2528056, PMID 40839265) — 21.2-point burnout
reduction at MGB; 60% of participants said it made them more likely to extend
their clinical career. Six-system study (Olson KD et al., *JAMA Netw Open*
2025;8(10):e2534976, PMID 41037268) — burnout 51.9%→38.8% (OR 0.26). Stanford
(Shah SJ et al., *JAMIA* 2025;32(2):375–380, PMID 39657021; Ma SP et al.,
*JAMIA* 2025;32(2):381–385, PMID 39688515) — documentation time −6.89 min/day,
after-hours −5.17 min/day, n=45.

**Randomized evidence (2025–2026), genuinely mixed:** UCLA 3-arm RCT n=238
(PMID 40672471) — burnout and task load improved, but clinicians rated occasional
clinically significant inaccuracies on both tools. Wisconsin stepped-wedge RCT
n=66, *NEJM AI* 2025 (PMID 41625485) — work exhaustion −0.44, but **workweek-hours
reduction lost significance after outlier removal**. Duke randomized crossover
n=136, *JAMIA* 2026 (PMID 41729180) — **no meaningful difference in pajama time**.
Emory/CHOA peds n=23 (PMID 40675605) — burnout 89%→56%, but **no significant
change in pajama time or charting time**.

**The counterweight that should anchor the session:** Rotenstein LS et al., *JAMA*
2026;335(16):1408–1417, PMID 41920565 — five academic systems, n=8,581 clinicians
(1,809 adopters). Total EHR time −13.4 min/day, documentation −16.0 min/day,
+0.49 visits/week, **but after-hours EHR time did not change significantly**, and
STAT reported **79% of clinicians offered the tool declined to use it**.

**Teaching point:** the widely publicized numbers are pre/post data from
self-selected early adopters — selection bias and Hawthorne effects. The RCT
literature shows real but smaller and more heterogeneous benefits, and largely
*fails* to confirm the reduced after-hours charting that residents care about
most. Time saved may be redirected into more patients rather than recovered as
personal time. **[VERIFY]** Market-share and funding figures are trade-press
sourced and directional only.

### Payer / utilization-management AI

**This section moves fastest of anything in the course — re-verify close to the
course date.**

- **UnitedHealth nH Predict** — *Estate of Gene Lokken v. UnitedHealth* (D. Minn.), filed Nov 2023. March 2025: motion to dismiss denied on contract and good-faith claims. March 2026: discovery largely favoring plaintiffs. **Status: active discovery, not settled or dismissed.** **[VERIFY]** Class-certification timeline is press-sourced, not docket-verified.
- **Cigna PXDX** — *Kisting-Leung v. Cigna* (E.D. Cal.). ProPublica reported ~300,000 claims rejected in two months at ~1.2 seconds per claim. March 2025 mixed ruling. **[VERIFY]** Status beyond March 2025 unconfirmed.
- **Senate PSI report** — "Refusal of Recovery," published **October 17, 2024** (not October 2025 — a common conflation with 2025–2026 follow-up letters). UnitedHealthcare post-acute prior-auth denial rate **10.9% (2020) → 16.3% (2021) → 22.7% (2022)**; Humana long-term acute-care denials up 54%.
- **CMS 2024 MA/Part D Final Rule (CMS-4201-F):** AI may inform coverage decisions but **cannot be the sole basis for a denial** — must be individualized to the enrollee's actual history and clinical notes.
- **CMS WISeR Model:** launched **January 1, 2026**, a six-year CMMI pilot bringing AI-assisted prior authorization into *traditional* fee-for-service Medicare in six states (NJ, OH, OK, TX, AZ, WA). Human clinician must review before a denial finalizes. **Central criticism: contractor compensation is tied to "averted expenditures"** — a denial incentive. A May 2026 CRA repeal resolution failed 46–50.
- **State laws:** California SB 1120 (effective Jan 1, 2025) — AI cannot be the sole basis for denying/delaying/modifying care. Georgia SB 444 (effective Jan 1, 2027). Illinois SB 3114 and Texas SB 815 **[VERIFY]** effective dates unconfirmed. **[CONFLICTING]** National counts of 2026 state AI-health laws range from 7 to 15 depending on source; the lists were not reconciled.

### Economics

Rock Health: digital health venture funding **$14.2B across 482 deals in 2025**,
up 35%; AI-branded firms took 54% of dollars.

**The central independent finding** — Peterson Health Technology Institute
(non-vendor funded):
- March 2025, ambient scribes: likely reduces burnout, but **little to no evidence of financial ROI**.
- April 2026, "Administrative AI": AI reduces burden *within* organizations but is **not lowering system-wide costs and may be raising them**, via a "bot wars" dynamic — providers auto-generating appeals, payers auto-adjudicating denials, more back-and-forth without resolving the clinical question. PHTI states there is "no existing evidence" AI-accelerated prior auth lowers cost per claim once the AI's own cost is counted.
- UCSF found scribe adopters billed 5.8% more RVUs with no rise in denials — more billable output, not cost reduction.

**Workforce displacement, actually measured:** medical transcriptionists **~5%
projected decline 2024–2034** (BLS, attributed to speech recognition) **[VERIFY]**
— direct BLS fetch was blocked, corroborated via secondary sources only. But
medical records specialists **+7%** and health information technologists **+15%**
over the same period — **growth, not decline**. That contradiction is the most
useful single fact in this section: it breaks the naive "AI displaces
documentation workers" narrative in the same breath as it supports it.

**The 25% administrative-burden figure conflates three studies** with three
different denominators — Shrank et al. *JAMA* 2019 (PMID 31589283, waste overall,
of which administrative complexity is one of six categories); Himmelstein et al.
*Health Affairs* (hospital administrative costs = 25.3% of *hospital*
expenditures); Woolhandler et al. *NEJM* 2003 (~24% of total spending, 1999 data).
Teach them as three denominators, not one number.

### Activity designs

1. **"The Hinton prediction" structured debate (60 min).** Four groups, four specialties, 15 min to build a 2026-data case for "follows the radiology pattern" vs. "genuinely different." Every claim needs a citation from the packet. Debrief with the four-factor framework: task decomposition, real-world generalization, liability/regulatory structure, demand elasticity.
2. **Algorithm bias audit (75 min).** Walk Obermeyer live, then groups take one other case each and answer: what proxy caused it, who was harmed, what correction followed and its current adoption status, and **what a clinician could have caught at the bedside without knowing the algorithm's internals**. Close on the proxy throughline.
3. **Payer-denial appeal role-play (60 min).** Triads — physician appealing, utilization-review nurse operating under the algorithm, observer with rubric. Two 12-minute rounds with rotation. Debrief with the PSI denial-rate trend and CMS's "not the sole basis" rule.
4. **AI scribe evidence-grading (45 min).** Pairs sort 6–8 claims from the packet into RCT / large observational / vendor-trade-press and rate confidence. Reveal: why do the press releases look so much better than the trials?
5. **Specialty-choice forecasting (45 min).** Each student names the most automatable *task* in their intended specialty and estimates what fraction of the job it is (benchmark: radiology's ~36% image interpretation). Pairs pressure-test using the four-factor framework. Close on the caveat that even a Nobel laureate got the highest-profile version of this call wrong.
6. **"Will AI cut costs" mock policy briefing (60 min).** Four roles — hospital CFO, independent evaluator, AI vendor, displaced-worker advocate — each with assigned evidence. Three-minute pitches, then cross-examination. Close on augment-vs-replace as an unresolved policy question these students will live for thirty years.

---

## 5. Ethics and regulation

**Two sub-topics were not researched and are marked as such below. Do not
backfill them from memory — that was explicitly refused by the research agent and
the refusal was correct.**

### FDA regulation of AI/ML devices

- **Scale.** More than **1,400 AI-enabled devices** authorized since 1995; **331 cleared in 2025 alone**, the most in agency history. **[VERIFY]** — FDA's own AI-enabled-device-list URL returned HTTP 404 twice during research; the figures come from a secondary tracker (MedTech Dive, citing a May 2026 download of FDA's list). Re-check the live URL before class, and do **not** cite a specific "75–80% radiology" share without re-verifying.
- **Predetermined Change Control Plan (PCCP).** Final guidance **Dec 4, 2024**. Lets a manufacturer pre-specify anticipated modifications — a description of modifications, a modification protocol, and an impact assessment — in the original submission, so later updates within the plan don't trigger a new 510(k)/De Novo/PMA. **This is the mechanism that in principle lets a continuously-learning model update without re-review**, and it is the single most important regulatory concept for students to understand about AI devices.
- **Lifecycle guidance.** "AI-Enabled Device Software Functions: Lifecycle Management and Marketing Submission Recommendations," draft Jan 7, 2025, comment period closed April 2025, **still draft as of mid-2026**. **[VERIFY]**
- **Clinical Decision Support.** The Sept 2022 final guidance established four criteria for **non-device CDS**: (1) not intended to acquire/process/analyze a medical image or signal; (2) displays/analyzes medical information; (3) provides *recommendations* rather than a specific directive; (4) **allows the clinician to independently review the basis for the recommendation**. Criterion 4 is the one that matters pedagogically — a bare score with no visible rationale fails it. **A revised final CDS guidance was reportedly issued January 6, 2026**, framed as deregulatory but analyzed as largely preserving the four-criteria framework. **[VERIFY]** — teach the four criteria as the foundation and flag the 2026 revision as a live, moving target.
- **Generative AI as a device.** FDA's Digital Health Advisory Committee met **Nov 20–21, 2024** on generative-AI devices and recommended disclosing to patients when genAI is used and how it influenced care, user-friendly post-market error reporting, and performance evaluation that **includes hallucination-rate measurement** — acknowledging that probabilistic behavior doesn't fit a deterministic device model. **No dedicated final genAI guidance was confirmed as of Aug 2026. Do not state that FDA has finalized a genAI framework.**
- **Teaching irony worth using:** FDA's own internal reviewer LLM, "Elsa" (v1.0 June 2025, v4.0 May 2026), had documented accuracy and hallucination problems acknowledged by the Commissioner.
- **The validation critique.** Wu E, Wu K, Daneshjou R, et al. "How medical AI devices are evaluated: limitations and recommendations from an analysis of FDA approvals." *Nat Med* 2021;27:582–584. [Link](https://www.nature.com/articles/s41591-021-01312-x). Of 130 FDA decision summaries, clinical performance data was reported for only about half; roughly a quarter reported none. Among those with data, well under a third gave sex-specific results. A 2024 follow-up, "Not all AI health tools with regulatory authorization are clinically validated" ([link](https://www.nature.com/articles/s41591-024-03203-3)), finds the gap persists. **This is the paper that answers "but it's FDA-cleared, isn't it fine?"**

### Liability

- **Price WN, Gerke S, Cohen IG.** "Potential Liability for Physicians Using Artificial Intelligence." *JAMA* 2019;322(18):1765–1766. [doi:10.1001/jama.2019.15064](https://doi.org/10.1001/jama.2019.15064). PMID 31584609. The **2×2 framework**: (AI advice aligns with / departs from standard of care) × (physician follows / rejects it). Exposure is greatest when following AI advice that departs from the standard of care, or rejecting AI advice that aligned with it, when the outcome is bad. Current tort doctrine still measures the *physician* against a standard-of-care benchmark, not the AI.
- **Learned intermediary doctrine** puts the physician between manufacturer and patient, complicating direct product-liability claims against vendors and pushing liability toward the treating physician's judgment.
- **No US malpractice claim involving a clinical AI tool has reached a verdict as of 2026.** Do not present this area as though case law exists. The teaching point is that it is untested.
- **Insurers.** The Doctors Company (Q4 2025) states it carries **no AI exclusion** and will still defend and indemnify physicians in AI-involved claims. Market pattern is cautious case-by-case underwriting, with advice to notify your carrier before adopting a clinical AI tool.
- **Consumer-chatbot litigation** (not clinical malpractice, but relevant to disclosure): Character.AI/Google settled with five families in January 2026 after 10+ wrongful-death suits; *Raine v. OpenAI* (Aug 2025) plus seven further California suits in Nov 2025; a May 2025 federal ruling rejected First Amendment and Section 230 defenses, letting product-liability and negligence claims proceed. **[VERIFY]** A reported July 2026 San Francisco case alleging a chatbot minimized cardiopulmonary symptoms before a pulmonary embolism comes from a single secondary summary — confirm before using.

### Consent, transparency, disclosure — NOT RESEARCHED

No verified findings. **Specifically do not use** any previously circulated Pew
patient-attitude figure (including "60% uncomfortable") or HTI-1 source-attribute
detail without re-verifying directly against pewresearch.org and healthit.gov.
Also unconfirmed: AI-scribe consent practice and two-party-consent-law
interactions; HTI-1/HTI-2/HTI-4 DSI transparency requirements; CHAI; TRIPOD+AI,
CONSORT-AI/SPIRIT-AI, DECIDE-AI reporting standards.

### EU AI Act — NOT RESEARCHED

No primary source was fetched. **Any claim about a "Digital Omnibus" proposal or a
2026 deferral of high-risk obligations is completely unverified.** The general
framework (in force Aug 2024; prohibited practices Feb 2025; GPAI obligations Aug
2025; high-risk nominally Aug 2026/2027) is consistent with background knowledge
but was not re-verified — confirm against eur-lex.europa.eu before teaching it as
settled.

### Hallucination and safety in clinical use

- **The automation-bias study to build the session on.** Jabbour S, et al. "Measuring the Impact of AI in the Diagnosis of Hospitalized Patients: A Randomized Clinical Vignette Survey Study." *JAMA* 2023;330(23):2275–2284. [doi:10.1001/jama.2023.22295](https://doi.org/10.1001/jama.2023.22295). PMID 38112814. 457 clinicians. Baseline accuracy 73.0%. A standard AI model raised it 2.9 points (4.4 with explanations). **A systematically biased AI model lowered accuracy by 11.3 points — and adding explanations did not mitigate the harm.** That last clause is the finding worth the whole session: explainability did not rescue clinicians from a biased model.
- **Whisper ASR hallucination (AP, Oct 2024).** Nabla, a Whisper-based documentation product, was reportedly used by 30,000+ clinicians across 40+ health systems covering ~7 million visits. One engineer found hallucinations in more than half of 100+ hours of studied transcripts; a Michigan researcher found them in 8 of 10 transcriptions. Fabricated content reportedly included medications and treatments never spoken.
- **Deskilling — the colonoscopy study.** *Lancet Gastroenterol Hepatol* 2025, "Endoscopist deskilling risk after exposure to artificial intelligence in colonoscopy: a multicentre, observational study" (doi:10.1016/S2468-1253(25)00133-5). Reportedly 4 Polish centers, 19 experienced endoscopists; adenoma detection rate at *non-AI-assisted* colonoscopies reportedly fell from **28.4% to 22.4%** after regular AI exposure. **[VERIFY — IMPORTANT]** The primary abstract was blocked (403); these figures are secondary-sourced. This is the most quotable statistic in the entire deskilling literature, which is exactly why it must be confirmed against the primary source before it goes on a slide.
- **MedHallu** is an actively used medical-QA hallucination benchmark; the founding paper was not directly retrieved. **[VERIFY]**
- **NEDA "Tessa" (2023).** NEDA replaced a human-staffed eating-disorder helpline with a chatbot that recommended calorie deficits, weekly weigh-ins, and calorie counting to people in eating-disorder recovery; suspended after public reporting. ([NPR](https://www.npr.org/sections/health-shots/2023/06/08/1180838096/an-eating-disorders-chatbot-offered-dieting-advice-raising-fears-about-ai-in-hea), [AI Incident Database #545](https://incidentdatabase.ai/cite/545/)). **No 2024–2026 purpose-built clinical chatbot safety incident was independently confirmed** — Tessa remains the canonical case.

### Professional guidance

- **WHO**, "Ethics and governance of artificial intelligence for health: guidance on large multi-modal models," **Jan 18, 2024** — 40+ recommendations across research, drug development, clinical care, education, administration, and patient-facing use.
- **AAMC** — two distinct confirmed documents: "Principles for Responsible AI in Medical School and Residency Selection" (Feb 2024), and "Principles for the Responsible Use of Artificial Intelligence in and for Medical Education," **v1.0 Jan 2025, v2.0 July 31, 2025** (actively iterated).
- **AMA** — physician AI use reportedly **38% (2023) → 66% (2024)**, with a further secondary report of 81% in early 2026. **[VERIFY]** All secondary-sourced; the primary AMA PDF could not be parsed.
- **NAM AI Code of Conduct, ACGME, and LCME positions — unconfirmed or not researched.** Do not state a definitive ACGME/LCME position without a direct check.

### Activity designs

1. **FDA reviewer role-play (60–75 min).** Eight groups, each with a one-page fictional submission summary for an AI diagnostic tool (varying specialty and risk), plus the four CDS criteria and the PCCP framework as handouts. Each decides: device or non-device? What change-control plan would you require? Groups pitch rulings to the class for pushback. Surfaces the CDS-boundary controversy organically.
2. **Consent-script writing (45 min).** Pairs draft a 60-second spoken disclosure a clinician would actually say before (a) an ambient scribe records the visit, (b) an AI-assisted imaging read, (c) a chatbot triage tool. Discuss where "meaningful disclosure" collapses under time pressure. *Runs safely despite the unresearched consent section — it needs communication skill, not regulatory citation.*
3. **Mock institutional AI governance committee (75–90 min).** Roles: CMIO, risk/legal counsel, patient advocate, frontline physician, data scientist, student rep. Scenario: system-wide deployment of an LLM documentation tool. Decide approval conditions, monitoring, and the post-deployment hallucination protocol. Use Jabbour 2023 and the Whisper reporting as the risk evidence.
4. **Liability moot court (75 min).** Two teams argue a hypothetical where a clinician followed or overrode an AI recommendation with a bad outcome, using the Price/Gerke/Cohen 2×2 as the doctrinal toolkit. **State up front that no US case has been decided this way** — the exercise is rehearsing an open question, not discovering a gotcha.
5. **Hallucination hunt (45–60 min).** Groups review clinical-note excerpts, some with planted fabrications in the style of documented Whisper failures, and explain what tipped them off. Debrief on why fluent, plausible fabrications are more dangerous in clinical text than in chat.
6. **Regulatory scavenger hunt (30–40 min, async-friendly).** Each group takes one question flagged unverified in this document — EU AI Act high-risk status, ACGME expectations, NAM Code status, the Jan 2026 CDS revision — and finds the current primary-source answer before the next session. **This doubles as a live demonstration of how fast and hard-to-pin-down this space is, which is arguably the most honest lesson the course can teach.**

---

## Appendix: existing Colab notebooks (recovered)

The `vibe-coding` deck references two Colab notebooks that appear nowhere in the
talks repo. Both were recovered and verified:

- **`ai-data-analysis-example-idpt-8079.ipynb`** — student starter, 3 cells (1 code, 2 markdown). Introduces Python and notebooks, loads the Kaggle insurance dataset via `pandas.read_csv` from a public URL, then instructs the student to use Colab's built-in "generate" AI-code link with the prompt *"Produce a text description of the data in the insurance data."*
- **`ai-data-analysis-example-completed-idpt-8079.ipynb`** — the completed twin, 27 cells (9 code, 18 markdown), being the same intro plus a full Colab Data Science Agent regression workflow: one-hot encoding, train/test split, Linear Regression vs. Gradient Boosting, MAE/MSE/R², and feature importance. The agent's own summary finds `smoker_yes` dominant (importance 0.678), then `bmi` (0.186) and `age` (0.118), with Gradient Boosting outperforming Linear Regression (R² 0.88 vs 0.78).

**Both are usable as-is in a Zoom session with no setup:** only `pandas` and
`scikit-learn` (both pre-installed in Colab), three public URLs, and — verified
mechanically — **no API key, login, file upload, or pip install in either**. The
only requirement is being signed into Colab to use the "generate" feature.

Pedagogically these pair naturally with `core-foundations`: the insurance dataset
is the same one behind the ml-intro cost example, and the completed notebook is a
readable artifact of an AI agent doing a whole modeling workflow — including
choices a student should be able to question.
