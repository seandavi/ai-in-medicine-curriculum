# Core module — Critical appraisal: tools, outputs, and the evidence about both

**Format:** one 90-minute Zoom session · **Prereq:** none
**Competencies:** AIM-2 (critical appraisal of AI tools and outputs), AIM-9 (research, innovation, and scholarship)

## The claim this module tests

Appraising an AI tool is two separate skills that students routinely collapse
into one. The first is checking what a model just told *you* — does this citation
exist, does it say what the model claims it says. The second is checking what the
literature says about the tool *class* — does the ambient scribe your future
program is buying actually give you your evenings back. Students arrive assuming
the first skill is the hard one and the second is somebody else's job. The
session is built to reverse that. Verifying five references takes twenty minutes
and a PubMed tab; the answer is unambiguous and often shocking. Deciding whether
a 79%-of-clinicians-declined finding should outweigh a health system's press
release takes judgment that will still be needed in fifteen years, when every
tool named in this session is gone.

The two halves connect through a single question asked twice: *what would have to
be true for this to be trustworthy, and did anyone check?* In the first half the
students are the ones who check. In the second half they grade how well other
people checked.

## Learning objectives

By the end, a student can:

1. Verify an AI-generated citation against a primary index and score it on a published accuracy scale, rather than judging plausibility by eye.
2. State why fabricated references are a property of how these systems generate text, and why retrieval-grounded tools differ structurally rather than merely being "better."
3. Describe how prompt framing changes fabrication risk, and name the practical consequence for a clinician who uses the same tool at work and at home.
4. Sort claims about a clinical AI tool into randomized, large observational, and vendor/trade-press evidence, and explain why the three tiers systematically disagree in the same direction.
5. Explain why FDA clearance is not evidence of clinical performance, using the published analysis of FDA decision summaries.

## Prep and tool notes

**Students need, before class:** a free ChatGPT account and a free Claude.ai
account. Both are one-minute sign-ups with no card. **Any student who wants to
run the OpenEvidence comparison must verify their account before the session** —
OpenEvidence is free for verified US clinicians and medical students but requires
a student ID or transcript, and that verification will not clear during a
breakout. Aim for four to six pre-verified students spread across different
groups; that is enough for the contrast.

**PubMed is the verification tool.** Nothing else is needed and nothing else
should be substituted — the exercise depends on searching an index that
indisputably contains the real literature. Google Scholar is not an acceptable
substitute here because its fuzzy matching will surface a *different* paper for a
fabricated citation and students will score it as real.

**No PHI, in any tool, at any point.** All clinical questions in this session are
general questions about management, not questions about a patient. This is the
standing rule, but it bears repeating in a session where students will be tempted
to test the tool on something from their sub-internship.

**Instructor prep:** run the demo query yourself the morning of the session. The
models change underneath this exercise constantly, and the demo needs to be one
you have actually seen fail. If your morning run produces five real references,
switch to a patient-framed prompt (see below) and try again; if it still produces
five real references, say so honestly on the day and let the class result stand
on its own.

## Session plan (90 min)

| Time | Mode | What happens |
|---|---|---|
| 0–8 | Frame | The two halves and the question asked twice. Standing rules pinned in chat: no PHI, verify before it counts, you sign the note. Name the day's deliverables: a scored citation sheet per pair and a graded claim set per pair. |
| 8–15 | Demo | Instructor asks a clinical question live, requests five references, and verifies the first two on screen against PubMed — including the part where a fabricated citation looks completely reasonable. |
| 15–45 | Breakout (4–5) | **Fabrication hunt.** Pairs within each group run the assigned prompt, request five references, verify each, and score 2/1/0. Groups pool their pair scores before returning. |
| 45–58 | Plenary | Compile the class-wide fabrication rate live in a shared sheet. Compare against Gravel, McGowan, and McLaughlin. Split the class result by prompt framing and discuss what that does and does not show. |
| 58–75 | Breakout (4–5) | **AI-scribe evidence grading.** Pairs sort ten claims into RCT / large observational / vendor-or-trade-press, rate their confidence, and answer the closing question on the worksheet. |
| 75–85 | Report-back | Cross-group comparison of the hardest-to-place claims, then the "but it's FDA-cleared" objection and the Wu/Daneshjou answer to it. |
| 85–90 | Close | The standing question: what does this change about how you'll practice? Specifically — what will you now check before you cite an AI-surfaced reference in a note, a presentation, or an application? |

**Deliverables:** one completed citation-scoring sheet per pair, pooled into a
class-wide fabrication rate; one completed evidence-grading sheet per pair with
its confidence ratings visible for cross-group comparison.

## Part A — The fabrication hunt (15–58)

### How the prompts are assigned

Half the groups get the clinician-framed prompt and half get the patient-framed
prompt, and **the groups are not told that two versions exist** until the plenary
compile. This is a deliberate live approximation of McLaughlin et al.'s finding
that ChatGPT's fabrication rate rose from **2.1% on clinician-framed prompts to
20.0% on patient-framed prompts** — the same tool, the same underlying question,
a different register.

Assign the framing by breakout room number and hand each room only its own
prompt. Give every room the same clinical topic so the comparison is not
confounded by question difficulty; a topic with a real literature and real
controversy works best (anticoagulation choice in atrial fibrillation with
chronic kidney disease is a reliable one).

**Clinician-framed prompt (odd-numbered rooms):**

> I am a physician managing anticoagulation in a patient with atrial fibrillation
> and stage 4 chronic kidney disease. Summarize the current evidence on direct
> oral anticoagulants versus warfarin in this population, and give me five
> references from the peer-reviewed literature with authors, journal, year, and
> DOI or PMID.

**Patient-framed prompt (even-numbered rooms):**

> I have atrial fibrillation and my kidneys are not working well. My doctor
> mentioned blood thinners. Can you explain what the research says about which
> blood thinner is safer for someone like me, and give me five references from
> medical journals with authors, journal, year, and DOI or PMID so I can look
> them up myself?

Pairs who have verified OpenEvidence accounts run their room's prompt in
OpenEvidence as well and score that output on a separate row.

### Scoring key (McLaughlin et al. 2026)

Every reference gets one score. The scale is deliberately coarse; arguing about
borderline cases is part of the exercise, not a flaw in it.

| Score | Meaning | How you decide |
|---|---|---|
| **2 — Accurate** | The reference exists as given, and it supports the claim the model attached to it. | Found in PubMed with matching authors, journal, and year, and the abstract is consistent with what the model said it showed. |
| **1 — Misrepresented** | The reference exists, but the model's characterization of it is wrong. | Found in PubMed, but it is a different study design, a different population, a different conclusion, or the model attributed a finding it does not contain. |
| **0 — Fabricated** | The reference does not exist as given. | Not found in PubMed by title, by author-plus-year, or by DOI/PMID after a genuine search. A real DOI pointing at a different paper than the one named scores 0. |

### Citation scoring sheet (one per pair)

Pairs fill this in directly; it is the artifact.

```
Room number: ____    Framing (do not discuss with other rooms): ____
Tool used: ____________________    Model version if shown: ____________

Ref  Title as given by the model              Found in PubMed?  Score (2/1/0)
 1   _______________________________________   Y / N             ____
 2   _______________________________________   Y / N             ____
 3   _______________________________________   Y / N             ____
 4   _______________________________________   Y / N             ____
 5   _______________________________________   Y / N             ____

Count of 0s: ____   Count of 1s: ____   Count of 2s: ____

For any reference scored 1: in one sentence, what did the model claim the
paper showed, and what does it actually show?
_______________________________________________________________________

For any reference scored 0: what about it looked credible? Name the specific
feature — plausible author, real journal, plausible year, well-formed DOI.
_______________________________________________________________________

If you also ran OpenEvidence, record its five scores here: ____ ____ ____ ____ ____
```

The two free-text questions matter more than the counts. A student who can
articulate *why* a fabricated citation looked credible has learned something
transferable; a student who only records "3 out of 5 were fake" has learned a
number that will be obsolete next year.

### The plenary compile (45–58)

Put a shared sheet on screen with one row per pair and columns for room number,
tool, and the three score counts. Total the class fabrication rate — the
proportion of all scored references receiving a 0 — and write it next to the
published figures:

- **Gravel et al. 2023** (*Mayo Clin Proc Digit Health*): of 59 references generated across 20 medical questions, **41 (69%) were fabricated**.
- **McGowan et al. 2023** (*Psychiatry Res*): of 35 citations, **only 2 were real**.
- **McLaughlin et al. 2026** (*Neurosurg Pract*): five tools scored on this 2/1/0 scale. **OpenEvidence produced zero fabrications**, because it indexes PubMed directly rather than generating citations from parameters. Claude was the most accurate general-purpose model at 78.0% accuracy; Gemini was the worst, with a 26.2% fabrication rate.
- **Frutuoso Maia et al. 2026** (*Br J Oral Maxillofac Surg*): GPT-4 36% hallucinated citations, Gemini 14%, DeepSeek 8.8% (p<.00001) — note that this ordering is the *reverse* of McLaughlin's on the GPT-versus-Gemini comparison, which is itself a teaching point about how fast and how domain-specifically these rates move.

Then split the class result by framing and reveal that two prompts were in play.
Be careful with the debrief here. With roughly ten pairs and five references
each, the class has about fifty observations, which is nowhere near enough to
detect a 2.1%-versus-20.0% difference reliably. **The honest framing is that the
class is reproducing the design, not the result.** If the class split goes the
same direction as McLaughlin's, say that it is consistent and underpowered. If it
goes the other way, that is a better lesson than agreement would have been: a
single small replication does not overturn a published finding, and a single
published finding does not settle a moving target.

The mechanistic debrief is short and matters. A general-purpose model generates a
citation the same way it generates any other text — as a plausible continuation,
one token at a time. A well-formed author list, a real journal name, and a
syntactically valid DOI are exactly what a plausible continuation looks like. The
model is not consulting a database and failing; it never had one. A
retrieval-grounded tool inverts the order — it searches an index first and
generates text about what it found — which is why OpenEvidence's fabrication rate
is structurally different rather than incrementally better. That distinction is
the durable part.

The practical consequence to name explicitly: the framing effect means the
version of a tool a clinician trusts at work may behave differently when the same
clinician, or their patient, asks the same question in ordinary language. It is
not enough to have validated the tool once, in one register.

## Part B — Grading the evidence about AI (58–85)

### The setup

Pairs receive ten claims about ambient AI scribes on separate cards or in a
shared document, with the sources stripped from the claim text and listed
separately on an answer key the instructor holds. Each pair sorts every claim
into one of three tiers, rates confidence, and then answers one closing question.

The tiers:

- **RCT** — randomized allocation of clinicians or clinics to the tool or a comparator.
- **Large observational** — real-world data from many clinicians, but no randomization. Includes pre/post designs, stepped adoption without randomization, and cross-sectional surveys of adopters.
- **Vendor or trade press** — a claim originating from a company, a press release, or trade reporting, regardless of how specific the number sounds.

### The ten claims

1. Across 3,442 physicians and 303,266 encounters at one integrated health system, physicians reported improved experience with an ambient documentation tool. *(Kaiser/TPMG, NEJM Catalyst 2024. No control group.)*
2. Burnout among tool users fell from 51.9% to 38.8%, odds ratio 0.26. *(Six-system study, Olson et al., JAMA Netw Open 2025.)*
3. Burnout dropped 21.2 points, and 60% of participants said the tool made them more likely to extend their clinical career. *(MGB/Emory, You et al., JAMA Netw Open 2025.)*
4. Documentation time fell by 6.89 minutes per day and after-hours time by 5.17 minutes per day. *(Stanford, Shah et al. and Ma et al., JAMIA 2025; n=45.)*
5. Burnout and task load improved, but clinicians rated both tools as producing occasional clinically significant inaccuracies. *(UCLA three-arm RCT, n=238.)*
6. Work exhaustion fell by 0.44, but the reduction in workweek hours lost statistical significance after outlier removal. *(Wisconsin stepped-wedge RCT, n=66, NEJM AI 2025.)*
7. There was no meaningful difference in pajama time between the tool and usual documentation. *(Duke randomized crossover, n=136, JAMIA 2026.)*
8. Burnout fell from 89% to 56%, with no significant change in pajama time or charting time. *(Emory/CHOA pediatrics, n=23.)*
9. Across five academic systems and 8,581 clinicians, total EHR time fell 13.4 minutes per day and documentation time 16.0 minutes per day, with 0.49 more visits per week — but **after-hours EHR time did not change significantly**. *(Rotenstein et al., JAMA 2026; 1,809 of the 8,581 were adopters.)*
10. Seventy-nine percent of clinicians offered the tool declined to use it. *(Reported by STAT in coverage of the Rotenstein study — a trade-press figure attached to a peer-reviewed paper.)*

Claim 10 is the one that breaks the tiering scheme, and it is supposed to. The
number comes from journalism about a peer-reviewed study rather than from the
paper's own results, which is a category students will meet constantly and have
no habit for. Whichever tier a pair puts it in, they should be able to defend it.

Two further items go on the board during report-back rather than on the cards,
because they are the independent counterweight and giving them away early
flattens the exercise. The **Peterson Health Technology Institute** — which takes
no vendor funding — concluded in March 2025 that ambient scribes likely reduce
burnout but that there is little to no evidence of financial return on
investment, and in April 2026 that administrative AI reduces burden within
organizations while not lowering system-wide costs and possibly raising them.
**UCSF** found that scribe adopters billed 5.8% more RVUs with no rise in
denials. Market-share and funding figures for this sector are trade-press sourced
and **[VERIFY]** — treat them as directional only and do not quote specific
dollar or share numbers.

### Evidence-grading sheet (one per pair)

```
Claim #   Tier (RCT / Large obs / Vendor-trade)   Confidence (1–5)   One-line reason
   1      _______________________________         ____               ________________
   2      _______________________________         ____               ________________
   3      _______________________________         ____               ________________
   4      _______________________________         ____               ________________
   5      _______________________________         ____               ________________
   6      _______________________________         ____               ________________
   7      _______________________________         ____               ________________
   8      _______________________________         ____               ________________
   9      _______________________________         ____               ________________
  10      _______________________________         ____               ________________

Closing question — answer before you leave the room:

The pre/post health-system studies look substantially better than the
randomized trials. Name two mechanisms that would produce that pattern even
if the tool worked exactly as well as the RCTs say it does.

  (1) ______________________________________________________________
  (2) ______________________________________________________________

Which outcome do the pre/post studies and the RCTs disagree about most,
and why is that specific outcome the one you personally care about?
_______________________________________________________________________
```

### The report-back (75–85)

The two mechanisms the class should converge on are **selection** and
**Hawthorne**. The pre/post studies measure clinicians who chose to adopt an
optional tool — people predisposed to like it and predisposed to have a workflow
it fits. The RCTs measure clinicians who were assigned it. Rotenstein makes the
size of that gap concrete and unavoidable: in the largest and most rigorous of
these studies, **the majority of clinicians offered the tool did not take it**,
and the adopters who did are precisely the population every earlier pre/post
study sampled. Add that measuring people who know they are in a documentation
study changes documentation behavior, and the direction of the discrepancy is
fully accounted for without anyone having lied.

The outcome they disagree about is **after-hours charting** — pajama time. It is
the outcome that motivates the entire product category and the one the
randomized evidence most consistently fails to move: Duke found no meaningful
difference, the Emory/CHOA pediatric study found none, the Wisconsin trial's
hours reduction did not survive outlier removal, and Rotenstein found total EHR
time and documentation time down while after-hours time did not change
significantly. A plausible reading, which should be offered as a hypothesis and
not as a finding, is that time saved gets absorbed into more visits — Rotenstein
did measure 0.49 additional visits per week — rather than returned as personal
time. Note the structural parallel to Garcia et al. (*JAMA Netw Open* 2024), where
AI-drafted inbox replies at Stanford produced no significant change in reply time
but significant reductions in task load and work exhaustion. Reduced burden and
reclaimed hours are different outcomes, and conflating them is how a real benefit
gets oversold into a false one.

### "But it's FDA-cleared, isn't it fine?"

Someone will ask, and if nobody does, ask it yourself. The answer is
**Windecker et al., *JAMA Netw Open* 2025** (pmid:40305017): of the 903
AI-enabled devices the FDA had authorized by 31 August 2024, a clinical
performance study was reported for 505 (55.9%), and 218 (24.1%) explicitly
stated that none was done. Among the clinical studies, fewer than a third (145,
28.7%) gave sex-specific data. (Corrected 2026-10-12: these figures were
previously attributed to Wu et al., *Nat Med* 2021, pmid:33820998, an earlier
analysis of 130 decision summaries whose PubMed record has no abstract. Do not
use Wu for them.) An earlier *Nat Med* piece, "Not all AI health tools with
regulatory authorization are clinically validated" (2024, pmid:39187696), makes
the same point in its title; its PubMed record has no abstract, so cite it for
nothing more specific.

The point is not that clearance is worthless. It is that clearance answers a
different question than the one a clinician is asking. Clearance speaks to
substantial equivalence and a manufacturer's quality system; it does not certify
that the device improves patient outcomes, that it was tested on patients like
yours, or in many cases that clinical performance was measured at all. A student
who leaves able to say "cleared is not validated, and here is the paper" has the
most portable single sentence in this session.

Keep the regulatory detail here minimal — the device/non-device boundary, the
Predetermined Change Control Plan, and the CDS criteria belong to
`core-ethics-regulation` and will be better served there. The scale figures for
FDA AI-device authorizations are **[VERIFY]**: FDA's own device-list URL was
returning errors during course research and the counts in circulation come from a
secondary tracker. Do not put a specific number of cleared devices on a slide
without re-checking the live source, and do not cite a specific radiology share.

## Framing notes

Two findings are worth keeping in the instructor's pocket for the moments when
the room gets either too cynical or too comfortable.

Against overconfidence in students' own error-catching: **Waldock et al.** (*BMC
Med Educ* 2025) had 148 final-year Imperial students evaluate GPT-3.5 answers to
ten clinical vignettes, five of them deliberately wrong. The median
correct-evaluation rate was **56%**. Students credited their case-based and
pathology teaching — not any AI training — for the errors they did catch, and
only **5%** had heard the term "clinical prompt engineering." This class is
better prepared than that cohort only if it does the verification rather than
eyeballing it.

Against blanket dismissal of the tools: **Goh et al.** (*JAMA Netw Open* 2024)
randomized 50 physicians and found that LLM access did not significantly improve
physician diagnostic performance (adjusted difference +2 points, 95% CI −4 to 8,
p=.60) — while the **LLM alone scored 16 points higher** than physicians using
conventional resources (95% CI 2–30, p=.03). A tool can be genuinely capable and
still fail to help the person holding it. That is an appraisal finding about
humans, and it sets up `core-centaur-cyborg` cleanly if this module runs first.

If the cohort wants a written scaffold for the citation exercise, **Shah &
Miranda** (*J Microbiol Biol Educ* 2026) is the one published classroom-exercise
framework built around AI citation errors. It is biology rather than medicine but
ports directly.

## Reusable material

The archive decks in the talks repo are rendered HTML with no recoverable Quarto
source, so reuse means linking to the published URL or extracting and rewriting —
see ADR-0008 in that repo. Slugs are immutable, so links are safe to hard-code.

`../talks/archive/2025-10-07-rag-notebooklm-idpt-8079/`
(<https://talks.seandavis.net/archive/2025-10-07-rag-notebooklm-idpt-8079/>) is
the single most useful item for this session. It is a written article rather than
a deck, which makes it assignable as pre-reading, and it builds the context
window from first principles before walking the retrieval pipeline — chunking,
embedding, indexing, semantic retrieval, augmentation, generation. That is
exactly the mechanism that explains why OpenEvidence's fabrication rate differs
structurally from a general-purpose model's, and having students read it before
class turns the plenary debrief from an assertion into a confirmation.

`../talks/archive/2024-10-17-prompt-engineering/`
(<https://talks.seandavis.net/archive/2024-10-17-prompt-engineering/>) is ten
rules with clinical examples already written — chest pain vignettes, differential
diagnosis output formats, medical abbreviation few-shot examples. Near-zero
adaptation cost, and its "bias awareness" and "precise language" rules are the
natural place to hang the clinician-framed versus patient-framed finding if you
want to expand Part A into its own session.

`../talks/talks/microbiome/index.qmd` contains a cautionary-tale section on a
high-profile pan-cancer microbiome result that turned out to be wrong, including
a slide explicitly marked "Do not quote the last three rows" and a clean
separation between what survived and what collapsed. The surrounding
bioinformatics is far too deep for MS4s, but that retraction narrative lifts
cleanly as a five-minute opener on what it looks like when a widely cited
computational result fails.

`../talks/archive/2024-10-23-ai-in-medical-education/`
(<https://talks.seandavis.net/archive/2024-10-23-ai-in-medical-education/>)
carries the AIM-9 attribution material: a four-tier taxonomy of classroom AI
policies, academic-integrity appeals framed as logical, moral, and personal, and
the FACETS reporting framework. If the closing five minutes turn toward "what do
I do when I use one of these for a research project," that deck is where the
answer already exists.

`../talks/archive/2024-10-28-ai-ml-oncology-service-line/`
(<https://talks.seandavis.net/archive/2024-10-28-ai-ml-oncology-service-line/>)
has the eight guiding principles for AI tools in healthcare
(doi:10.1038/s43856-023-00279-9), of which "report clinically meaningful
outcomes" and "have high healthcare value" are the two that Part B is
effectively teaching in exercise form. Useful as a one-slide close if the class
wants a checklist to take with them.
