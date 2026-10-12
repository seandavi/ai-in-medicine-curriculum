# Stanford AI in Medical Education site: review against our book

- **Reviewed:** 2026-10-07, five days before the course starts (Oct 12).
- **Site:** <https://stanfordmed.github.io/aimeded-website/learn> (the page is titled "Resources"; the nav calls it "Learn").
- **Method:** the site is a React single-page app, so a plain web fetch of `/learn` gets an HTTP 404 status (GitHub Pages serves the app through its 404 page; browsers still show it). I read the source instead. I cloned both public repositories, `stanfordmed/aimeded-website` and `stanfordmed/aimeded`, and read every content file. I downloaded both PDFs and exported the three public Google files (two decks, one handout) as text. For the six symposium videos I pulled YouTube's automatic captions and read the full transcripts of the prompting workshop, the liability talk and the closing remarks. I sampled the lightning demos and the panel at intervals. The keynote has no captions, so I did not review its content.
- **Scope rule:** nothing in the book was changed. This note only recommends.

## 1. What the site is

**Who made it.** Stanford School of Medicine's "AI in Medical Education" initiative. Leadership listed: Reena Thomas (Senior Associate Dean for Medical Education), Jonathan H. Chen (AI Faculty Champion), Joe Gayk. The curriculum team is led by Aydin Zahedivash, with Alaa Youssef, Vishnu Ravi, Gabriel Tse, Shivam Vedak, Dong-han Yao and Bethel Mieso. A medical librarian (Connie Wong, Lane Library) sits on the steering committee.

**Audience.** Stanford MD and PA students first, then "educators and clinicians" generally. Several items are Stanford-specific (SecureGPT, Stanford AI Playground, Stanford IT data-risk links).

**Dates.** The website repo was created 2026-04-23; the last content commit was 2026-08-17 (adds a student talk and makes titles clickable). The modules repo was created 2025-12-04; last push 2026-09-03. Earlier commits are by Lovable's build bot, so the site was scaffolded with an AI site builder. The newest dated item on the page is the June 2026 symposium announcement; its videos are not posted. The posted videos are from the **June 4, 2025** symposium.

**Structure.** Four pages: Home, Overview (people), Learn/Resources, Get Involved (mailing-list form). The Learn page has four sections: Documents (3), Interactive Learning Modules (3), Lectures and Talks (6 videos plus one student deck), Partner Organizations (3 links). It also links a Google Form inviting suggestions for new modules.

**Licence and terms of reuse.**

- The website footer says only "© 2026 Stanford University". No licence is stated.
- GitHub reports **no licence** for either repository (`license: null`). No LICENSE file exists.
- The AI Evaluation module's own README has a "License" heading whose entire text is "Stanford Medicine - AI in Medical Education". That is an attribution line, not a licence.
- The modules repo README invites educators to "make a pull request". That is an invitation to contribute, not a grant to reuse.
- One explicit permission exists. The Learn page describes the **"What is AI?" slide deck** as "free for anyone to use at their own institutions", with its matching handout. It does not say whether you may modify it. Several slides carry figures adapted from third parties (a Substack newsletter, a Mesko and Topol figure), which Stanford cannot license to us.
- The student toolkit by Harrison Konsker (linked from the page, hosted on his personal site) says "All free to use, modify, and share". His repo also has no licence file.
- YouTube reports no Creative Commons licence on the videos (standard YouTube licence).

**What this means for us.** Except for the "What is AI?" deck and handout (use permitted, modification unclear) and Konsker's toolkit (informal permission to modify), we **cannot copy** Stanford material into the book. We can link to it, and we can be inspired by it and build our own version. For the CSS-drawn, open-licence visuals our standards require, "build our own" is the only route anyway.

## 2. Inventory

Times marked *(est.)* are my estimates from the content; the site states none.

| # | Item | URL | Format | Length | Summary |
|---|---|---|---|---|---|
| 1 | Using AI to Learn Medicine | [PDF](https://med.stanford.edu/content/dam/sm/ai-in-meded/documents/Using%20AI%20to%20Learn%20Medicine_September%202025.pdf) | Slide deck as PDF, 42 pages | One session, Sept 29, 2025 | Lane Library workshop for first-years: word cloud, buzzword quiz, AI policy, a tool table, a group literature-search exercise, a student's study workflow, criteria for choosing tools. |
| 2 | AI in Clinical Practice: A Curriculum for Medical Students | [PDF](https://med.stanford.edu/content/dam/sm/ai-in-meded/documents/AI%20Curriculum--Module%20List.pdf) | 5-page outline, created May 30, 2025 | n/a | Four competency areas, eight modules (1A to 4B), objectives mapped to two Delphi studies, each objective paired with a resource title. The PDF has no working links. |
| 3 | Stanford MD/MSPA Generative AI Policy (handbook 3.32) | [web](https://med.stanford.edu/md/mdhandbook/section-3-md-requirements-procedures/3-32--generative-artificial-intelligence--ai--policy.html) | Policy page, updated Aug 2025 | 5 min read | Permitted uses, no PHI in public tools, disclosure of substantial AI help (tool, model, date, query), student accountable for output, AI discouraged in assessments. |
| 4 | What is AI? | [Google Slides](https://docs.google.com/presentation/d/16s0MdSmhnXFyrTyETx7PLuTzLc87_Lqn10gSwrsMbH8/edit?usp=sharing) | 16-slide deck with speaker names | 30 to 45 min live *(est.)* | Rules-based vs machine learning; four learning types (supervised, unsupervised, semi-supervised, reinforcement) with clinical examples; where LLMs fit; foundation model vs fine-tuning with cost ranges. |
| 5 | Matching activity handout | [Google Doc](https://docs.google.com/document/d/1dXUm-egnLK2KqnScwX1ty6j4dwww7nW3Qu6A6RTGIHY/edit?usp=sharing) | Two fill-in tables plus answer key | 15 min *(est.)* | Match four learning types and six model types (CNN, RNN, linear and logistic regression, decision tree, k-means) to clinical uses. Includes an honest instructor note that RL insulin pumps are research prototypes. |
| 6 | Explore AI Diagnostic Performance | [interactive](https://stanfordmed.github.io/aimeded/ai-evaluation/) | Static web page, no login | 20 to 30 min *(est.)* | Chest X-ray pneumonia example. Drag a threshold over 100 dots, watch the confusion matrix, sensitivity, FPR, PPV, NPV, F1, ROC and PR curves change. Three datasets (obvious, subtle, low prevalence) plus a prevalence slider. Three clinical questions with hidden answers. Data are hand-made, not from a real model. |
| 7 | Data Security, Privacy and AI | [interactive](https://stanfordmed.github.io/aimeded/data-security/) | Web app, no login | 25 to 35 min *(est.)* | HIPAA basics (encryption, access, audit logs, breach reporting, business associates); a clickable diagram of three cases (consumer chatbot, local model, vendor with a BAA); a "Spot the PHI" exercise on seven note excerpts; a sort-the-prompts exercise (safe for any tool vs needs a BAA tool); two Q&As. |
| 8 | Framing the Landscape: What AI Means for Medicine (J. Chen) | [YouTube](https://youtu.be/JRc03UJR4TY) | Talk, June 4, 2025 | 26 min 17 s | Not reviewed: no captions available and I did not watch it. |
| 9 | Workshop: Basics of LLMs and Prompt Engineering (Vedak, Yao) | [YouTube](https://youtu.be/xlMon7sXGig) | Talk | 40 min 46 s | Three eras of medical AI (rules, machine learning, generative); a live next-word guessing game; tokens and embeddings; prompting as "clear communication": role/style/tone, goal, context, instructions, then structure and examples. |
| 10 | Legal Liability in the Age of Medical AI (Mello) | [YouTube](https://youtu.be/p8YYIQgzscM) | Talk aimed at trainees | 29 min 31 s | Why worry (vendor disclaimers push liability onto users, informed-consent claims, jury distrust) and why not panic (few claims, hard to prove). A risk framework: chance of error, chance someone catches it, severity. Practical advice on documentation and telling patients. |
| 11 | Lightning Demos: AI Tools for Medical Education | [YouTube](https://youtu.be/R8B8k9NLtTc) | Eight short demos | 60 min 40 s | Note-mining residency learning curves; a student's NotebookLM-to-Anki workflow; a commercial case simulator (Sketchy); an AI clinical-reasoning coach; a clinic resource chatbot; an AI simulated-patient platform. Mostly Stanford-internal or commercial tools. |
| 12 | Panel: What Makes a Doctor a Doctor? | [YouTube](https://youtu.be/20Q89ZAEVxU) | Panel of 7 | 46 min 39 s | Surgeon, CMIO, residents, a first-year student and educators on team work, context, judgment, authentic presence, automation complacency, and whether AI adds or removes work. |
| 13 | Closing Reflections (J. Chen) | [YouTube](https://youtu.be/VlLvUf3qBuM) | Remarks | 4 min 18 s | A doctor is knowledge, judgment, negotiation and personal responsibility together; cites Warner Slack's line about doctors replaceable by computers. |
| 14 | From Chatbot to Workflow (Konsker, MS1) | [Google Slides](https://docs.google.com/presentation/d/1uaOcQlXT8j_cbQI2sPRvklEHLUx5VkFeFH59H7eLosY/edit?usp=sharing) | Deck with full speaker script | ~10 min talk | Five-step study workflow: distill a lecture with a Claude skill, NotebookLM podcast, ChatGPT diagram, AI mnemonic images, auto-generated Anki cards. Opens with "89% of medical students use generative AI". |
| 15 | Konsker toolkit | [web](https://harrisonkonsker.github.io/#toolkit) | Seven workflows, three downloadable Claude skills | 5 to 30 min each | Includes a "Practice Question Builder" with a coverage audit and grounding check, and a "Virtual Patient Simulator" prompt. |
| 16 | Partner links: HAI, AIMI, RAISE Health | on page | Links | n/a | Institutional home pages only. |
| 17 | Home-page news items | [site home](https://stanfordmed.github.io/aimeded-website/) | Cards | n/a | BMJ Digital Health and AI editorial "From iPatient to Ai-Patient" (2026); the HAILS leadership program (CME, paid); workshops with no linked materials. |

## 3. Mapping to our book

Verdict key: `link as Go deeper`, `adapt idea`, `reuse (licence permits)`, `replace ours (better)`, `no action`.

| Our piece | Stanford overlap | Verdict | Reason |
|---|---|---|---|
| Week 1 talk: intro and adult learning | #1 (word cloud, "what do you want to learn next"), #14 | adapt idea | Opening with a one-word feeling poll is cheap on Zoom and surfaces the avoiders. Konsker's deck is a useful foil for an adult-learning talk (see section 4, item 5). |
| Week 1 talk: history of AI | #4 slides 2 to 4, #9 "three eras" | adapt idea | The three eras (rules since about 1970, machine learning, generative since 2017) is a clean spine. Our foundations chapter already has MYCIN. The talk can name the eras; no copying needed. |
| Week 1 talk: AI to ML to deep learning to LLMs | #4, #5, #9 next-word game | adapt idea; #4/#5 `reuse (licence permits)` only if needed | The next-word game (section 4, item 3) is the best single idea on the site for a live talk. The matching handout could be used as-is under Stanford's "free to use" statement, but it has errors to fix first (section 6). |
| Friday small groups (all weeks) | #12 panel question, #5 handout, #14 | adapt idea | "What makes a doctor a doctor?" is a ready week 4 discussion prompt. Konsker's workflow is a ready week 1 discussion case. |
| core-foundations | #6, #4, #5, #9 | `link as Go deeper` (#6); adapt idea | Our chapter quotes the Epic sepsis model's AUC of 0.63, 67% missed, 18% alerted, but never teaches threshold, PPV or prevalence. #6 fills exactly that gap and is free, browser-only, no login. Our two-question sort (does the data contain the answer; number or category) is simpler than their four-type taxonomy; keep ours. |
| core-centaur-cyborg | #14, #15, #1 study workflow, home-page "Human + Computer > Human" | adapt idea | Konsker's workflow hands the organizing work to AI, which our chapter's "metacognitive laziness" section warns about. It makes a good case to argue over, not a model to copy. Friedman's "fundamental theorem" (the site's banner) is a verifiable source for our centaur framing: [@pmid:19074294]. |
| core-appraisal | #6, #1 literature-search exercise, #1 tool table | `link as Go deeper` (#6); adapt idea (#1) | #6 covers model-performance appraisal, which our appraisal chapter does not (it is about LLM answers and citations). Their semaglutide literature-search case asks students to verify AI-found articles: the same move as our fabrication hunt. Ours is more rigorous; keep ours. |
| core-bias-equity | #6 "Severe cases" vs "Subtle cases" | no action (optional mention) | #6 shows a model validated on ICU cases failing on outpatients: spectrum bias, a cousin of our dataset-shift point. Not about equity; our proxy-problem chapter is stronger. |
| enrichment-agentic-coding | none | no action | Nothing comparable on the site. |
| core-patient-communication | #7 Q&A ("why can my patient paste their data into ChatGPT but I cannot?"), #10 disclosure advice, #15 virtual patient | adapt idea | The patient-versus-clinician data question is a good Check item. Mello's two-condition rule for telling patients (real risk, and the patient could act on it) is a concrete heuristic our chapter could cite through her published work. Our chatbot-as-patient exercise is already better designed than #15. |
| enrichment-workforce-economics | #12 panel, #13 | no action | Panel is opinion, not evidence. Our chapter is built on data. |
| enrichment-environment | none | no action | Not covered by Stanford. |
| core-ethics-regulation | #10 Mello talk, #3 policy, #7 | `link as Go deeper` or Watch alternative (#10); adapt idea (#7) | Our Watch is a 48-min Mello and Guha podcast from Nov 2024. #10 is 30 min, aimed at trainees, from June 2025, and adds vendor disclaimers, informed-consent claims and a risk framework. It does not replace the podcast's three-defendant structure, which our Watch prompts use. |
| enrichment-prompting-lab | #9, #1 "prompt anatomy", #15 Practice Question Builder | `link as Go deeper` (#9); adapt idea (#15) | #9's main claim, that role prompting no longer improves accuracy but sets style and tone, supports our "organised, not correct" thesis. Our chapter is better evidenced. #15's "audit in a fresh conversation so the model checks rather than defends" is a good addition (section 4, item 6). |
| enrichment-rag-notebooklm | #1, #11, #14 (NotebookLM podcasts and outlines) | no action | Stanford presents NotebookLM as a study aid with no discussion of its failure modes. Our chapter is the corrective. |
| course/resource-log | #1 tool table | no action | Their table lists paid tiers (Elicit, Perplexity Pro, Canva, Adobe Firefly) and Stanford-only tools. |
| Syllabus "three rules" | #3 policy | `link as Go deeper` | A second school's written policy is a useful comparison for CU students to find their own. Stanford's requires disclosure of tool, model, date and query, which is more specific than ours. |

## 4. Strongest candidates

Ordered by value for the cost, with the course five days out.

**1. Explore AI Diagnostic Performance (#6) as a Go deeper or optional Do in core-foundations.**
- *Improves:* fills our biggest content gap. The book cites sensitivity-style numbers (the sepsis model "missed 67 percent", "alerted on 18 percent") and an AUC, but no chapter explains threshold, PPV, or why PPV falls when disease is rare. Grep of all chapters: zero uses of "positive predictive", "specificity" outside one workforce mention, and none of "threshold" in the appraisal sense.
- *Touches:* core-foundations, "Why performance on data it has seen tells you nothing", right after the sepsis paragraph; or the Go deeper list. A second link in core-appraisal "What a trustworthy tool looks like".
- *Cost:* 15 minutes for a Go deeper line. Writing our own threshold widget in the book's style (we already ship an overfitting widget in foundations Part A) would take a day or more and is a post-course job.
- *Conflicts:* none with browser, free, no PHI. It loads Google Analytics, which tracks visits; say so in one line. The page warns it works best on a tablet or desktop, which matters for any student on a phone. No licence, so link only. Its data are synthetic; say "illustrative".

**2. Mello's 30-minute trainee talk (#10) as the Watch alternative in core-ethics-regulation.**
- *Improves:* shorter and newer than our 48-minute podcast, and pitched at trainees. It adds three points our chapter lacks or only touches: vendors' terms of service disclaim injury liability and push it to users; failing to disclose AI use can ground a separate informed-consent claim; and a practical rule to record why you overrode a tool's output.
- *Touches:* "Watch or listen" (as "Video alternative") and possibly "The note, the patient, and the contract".
- *Cost:* 20 minutes to write the entry with three listen-for prompts.
- *Conflicts:* captions are automatic only (they misspell her name as "Melo"), a cost for ESL students. Numbers she gives aloud (2 to 5% of negligent injuries become claims; about 800 software-injury cases, about 50 in health care) are **unverified** here. Do not quote them in prose without finding her published sources; her NEJM piece [@pmid:38231630] is already in our bibliography.

**3. The next-word guessing game (from #9) for the Week 1 LLM talk, and possibly the foundations chapter.**
- *Improves:* makes "it predicts the next token, using the whole context" felt rather than told. The presenters show a sentence ending "in the last 24 hours, she has not had any ___" four times, each time with more of the history visible (pain, nausea, prior bowel obstruction surgery). Guesses move from random to "flatus". That is attention and the context window in one minute.
- *Touches:* Week 1 talk 3 live; optionally core-foundations "From tables to words", which currently uses the keyboard-suggestion analogy.
- *Cost:* 30 minutes to write our own four-step version with a different case. The idea is not copyrightable; the slides are not ours to copy.
- *Conflicts:* none. On Zoom, run it in the chat.

**4. A short "what counts as patient information" exercise, modelled on "Spot the PHI" (#7).**
- *Improves:* every Do block repeats "no patient information, ever", but no chapter teaches what makes a sentence identifying. Stanford's exercise is good: students click identifiers in seven note excerpts, including a ZIP code, an age over 89, a portal URL, and "the local chief of police accepting an award" as a unique trait.
- *Touches:* core-ethics-regulation "The note, the patient, and the contract", or a callout in core-centaur-cyborg "The practical rules". Could also be a 10-minute Friday warm-up in week 1.
- *Cost:* 2 to 3 hours to write our own excerpts and an answer key in `_answers/`. Link to Stanford's version in the meantime.
- *Conflicts:* our rule is stricter (no de-identified real cases either), and Stanford's module implies general questions are fine in any tool and PHI is fine in a BAA tool. That is compatible, but say so. Their module also has accuracy problems (section 6); do not link it without a caution.

**5. Konsker's study workflow (#14, #15) as a week 1 Friday discussion case.**
- *Improves:* gives the small group a concrete, appealing, student-made AI workflow to judge against the centaur chapter's six techniques and its "metacognitive laziness" finding. His pitch is that AI turns three hours of organizing into five minutes. Our chapter says the organizing may be where the learning happens. That disagreement is a good 30 minutes.
- *Touches:* Friday session week 1; the facilitator guide in `appendix/instructors.qmd` if one is written.
- *Cost:* 30 minutes to write four discussion questions.
- *Conflicts:* his tools use Claude skills, Gemini image generation and Anki; the "easiest path" uses free claude.ai, but the skills install path needs Claude Code. Students would only discuss it, not do it. His opening statistic, "89% of medical students", is 157 of 177 respondents from 14 of 188 US schools surveyed in late 2024 (Xu et al. 2026, [@pmid:41802232]). That is a good small appraisal exercise in itself: what population does "89% of medical students" describe?

**6. "Audit in a fresh conversation" from the Practice Question Builder (#15) for the prompting lab or centaur chapter.**
- *Improves:* adds one concrete verification habit: after a model produces something, open a new chat and ask it to check the output against the source, quoting the supporting line or marking it ungrounded. His stated reason is that a fresh chat audits instead of defending. That reasoning is plausible but **unverified**; present it as a practice tip, not a finding.
- *Touches:* enrichment-prompting-lab Step 5 ("Check two claims"), or centaur "The practical rules".
- *Cost:* 20 minutes.
- *Conflicts:* none; browser and free.

**7. The patient-versus-clinician data question (#7) as a Check item.**
- *Improves:* students will meet patients who paste their own records into chatbots. Stanford's answer: HIPAA binds the clinician as custodian, not the patient. That is a crisp, testable distinction.
- *Touches:* core-patient-communication Check, or core-ethics-regulation Check.
- *Cost:* 15 minutes, plus a line in `_answers/`.
- *Conflicts:* none. Cite HHS, not Stanford's page.

**8. Friedman's "fundamental theorem" for the centaur chapter and the Week 1 intro.**
- *Improves:* the Stanford banner shows person plus computer beating person alone. The source is Friedman, *JAMIA* 2009 [@pmid:19074294], which I looked up in PubMed. Its corollaries fit our chapter: the theorem can fail, and the resource must be informative as well as correct.
- *Touches:* core-centaur-cyborg "Two ways to work with a machine".
- *Cost:* 20 minutes, including reading the two-page paper.
- *Conflicts:* none. It is a framing essay, not evidence, so use it with a soft verb.

## 5. Ideas, not material

- **Three eras of medical AI.** Rules (expert systems, drug-interaction checks), learned prediction (sepsis, X-ray), generative. Ask "which era is this tool?" every time a tool is named. That is a cheap habit that matches our two-question sort.
- **Clinical scenarios with hidden answers inside an interactive.** #6 asks "screening: where would you set the threshold?" then reveals the reasoning. Our Check blocks could use the same reveal-after-commit pattern.
- **Same model, three populations.** #6's datasets (obvious cases, subtle cases, rare disease) show one model performing differently by setting. A paper-and-pencil version with a 2x2 table would work on Zoom with no widget.
- **The 10x10 dot grid.** 100 patients as dots, colored by truth, split by a threshold line. We could draw this in CSS as an illustrative figure for foundations.
- **"Which tool can see this sentence?" sorting.** #7 sorts prompts into "any tool" and "needs a BAA tool". A three-way sort for our rule (any tool / no tool / ask first) is a good 5-minute warm-up.
- **Buzzword speed quiz** (#1). A timed six-question vocabulary quiz with a leaderboard is a low-stakes way to start a Friday group. Zoom polls can do it.
- **One-word feeling poll** at the first session (#1), repeated at the last session, gives a before-and-after the CQI review can use.
- **A learning-objective coverage check** (#15). Ask a model to produce questions per objective, then audit the coverage in a fresh chat. As an assessment idea for us: students could write their week 4 synthesis, then have a chatbot map it against the course's AIM competencies and report gaps.
- **Commit before feedback** (#15 virtual patient). "Say your diagnosis out loud before the debrief" is a good rule for any chatbot-as-coach exercise, including our patient-communication Part B.
- **Panel prompt for week 4:** "What makes a doctor a doctor, if not knowledge?" Chen's closing answer (knowledge, judgment, negotiation, personal responsibility, together) is a usable summary for the AIM-X close.
- **Mello's risk triage** for any tool: how likely is an error, how likely is someone to catch it in time, how bad is it if not. It maps onto the FDA's software risk categories and could become a three-column worksheet for the device-line section.
- **Disclosure statement on their own deck.** The Lane deck opens by stating which AI tool generated content ideas. We already have AI-LEDGER.md; a one-line disclosure on each chapter's first page would make it visible to students.

## 6. Where ours is stronger

Honestly, on most axes.

- **It is a course; theirs is a link hub.** The site has two original interactive modules, one slide deck and a handout. The rest is recorded talks, a library workshop and a curriculum outline whose resource titles are not linked. There are no learning objectives per item, no time budgets, no checks, no answer keys.
- **Evidence.** Our chapters cite verified PMIDs for nearly every claim. Stanford's items mostly cite nothing. The curriculum outline cites two Delphi studies; the "What is AI?" deck cites a Substack newsletter for its core diagrams.
- **Accuracy problems in Stanford's material** (each checked against the source text I read):
  - The Data Security module shows a consumer chatbot "leaking" one clinician's patient details into another user's answer. It presents this as what happens, not as a possible risk. That specific path is not established for a single prompt.
  - The same module lists "Apple Intelligence" as an example of a model where prompts never leave your device. Apple routes some requests to its own cloud servers, so this is at least incomplete. *[VERIFY against Apple's documentation before repeating.]*
  - The Spot-the-PHI explanations say diagnoses and lab values are "usually not referred to as PHI". Under HIPAA, health information is PHI when it is linked to an identifier. The identifiers are what you remove to de-identify; they are not the whole of PHI. This would teach the wrong mental model.
  - The "What is AI?" deck gives Perplexity and OpenEvidence as examples of fine-tuned models, with a question mark on the latter. Both are better described as retrieval systems on top of general models. The handout pairs RNNs with ECG arrhythmia labeling, which is dated as the default example.
  - The Lane deck lists AI detectors (Grammarly) without noting how unreliable they are, and its sample prompt asks the model to find "highly cited" articles with impact factor over 7, which invites fabricated citations without saying so.
- **Failure modes.** Stanford's NotebookLM material is all upside. Our RAG chapter shows where grounding fails. Their prompting workshop says prompting is clear communication; our prompting lab shows, with three studies, that structure changes organisation reliably and correctness unreliably.
- **Access.** Several Stanford items depend on Stanford-only tools (SecureGPT, AI Playground) or paid tiers. Ours hold to free, browser-only, no install.
- **Plain language and ESL.** Their modules use jargon without definitions in places (F1, harmonic mean, "Bayesian insight"). Our standard defines every term on first use.
- **Equity, environment, workforce, agentic coding.** Stanford has nothing on these.

## 7. Gaps they cover that we do not

- **Diagnostic test metrics for AI tools:** threshold, sensitivity, specificity, PPV, NPV, prevalence effects, ROC versus PR curves. This is the main gap. It is also core AIM-2 content, and fourth-years already know these terms from Step 1 biostatistics, so the bridge is short.
- **What PHI is, concretely:** the identifier list, ages over 89, ZIP codes, unique traits, the patient-versus-clinician distinction.
- **The four learning types** (semi-supervised and reinforcement learning are absent from our foundations except RLHF). Low priority: our two-question sort is enough for practice, and the Week 1 talk can name the others.
- **Model types by name** (CNN, RNN, decision tree, k-means). Low priority for a user's course; useful vocabulary for reading papers. A Week 1 talk slide covers it.
- **Disclosure and citation of AI help in scholarly work:** ICMJE authorship rules, how to cite a chatbot in APA, MLA or Chicago, journal AI policies. Our ledger models disclosure but no chapter teaches students to do it in their own papers and abstracts.
- **A named institutional AI policy** for students to compare. Our CONTEXT notes CU's policy situation, but no chapter points students at a written student policy.
- **Vendor terms of service** as a source of liability (from Mello). Our ethics chapter has the contract section but focuses on BAAs, not injury disclaimers.

## 8. Could not access or did not verify

- **Chen keynote (#8):** no captions; content not reviewed.
- **Lightning demos (#11) and panel (#12):** sampled at intervals from automatic captions, not read in full. Speaker attributions in my summaries come from the page's speaker list, not from matching voices.
- **BMJ editorial** (Hosamani, Keet, Chi, Hom, *BMJ Digital Health and AI* 2026; [@pmid:42712307], DOI 10.1136/bmjdh-2026-000082): metadata confirmed in PubMed; the publisher page returned 403 and I did not read the text.
- **The curriculum outline's resources (#2):** the PDF has no live links. The titles ("Outcome Action Pairing", "Lead Time", "Decision Curves") look like lesson names from Stanford's Coursera "AI in Healthcare" specialization, but I did not confirm this or whether those lessons are free to audit.
- **Coursera course** linked in #1 ("Fundamentals of Machine Learning for Healthcare"): not opened. The link includes a paid-media tracking path; audit access unverified.
- **Mello's spoken figures** (claim rates, case counts, polling percentages): heard in the transcript, not checked against her papers.
- **The Data Security app's rendered text:** I read the source data files and component strings, not the running page. Wording on screen could differ slightly.
- **"What is AI?" deck figures:** I read the text export and confirmed 16 pages in the PDF export, but did not inspect each figure's licence.
- **Konsker's downloadable skills** (.zip files): not downloaded or run.
- **The June 2026 symposium:** announced on the home page; no recordings posted at review time.
- **Two citations from the curriculum outline**, both confirmed in PubMed: Çalışkan, Demir and Karaca, *PLoS One* 2022 [@pmid:35862401]; Car et al., *JAMA Network Open* 2025 (DOI 10.1001/jamanetworkopen.2024.53131; no PMID returned by the ID converter). Car et al. is already in `research/competency-frameworks.md`; Çalışkan is not, and is worth adding there as a second Delphi source.
