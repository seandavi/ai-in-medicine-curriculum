# Competency framework

Nine domains, six core and three extension, plus one cross-cutting stance. Each
carries a stable ID (`AIM-1` … `AIM-9`, `AIM-X`) so modules can tag themselves
and be remapped later without rewriting anything.

Derived from the synthesis in `research/competency-frameworks.md`, which reviews
eleven published frameworks. The two US anchors are Russell et al. (*Acad Med*
2023) and Hunt et al. (*npj Digit Med* 2026, a scoping review of 54 studies from
22 countries). The core/extension split follows DECODE's mandatory/discretionary
structure and is corroborated by the Korean Delphi (Lee et al., *Acad Med* 2024),
where data science and AI research were rated optional while foundations, ethics,
and clinical application were rated essential.

## Why these IDs exist

The AAMC's national AI competencies are expected in **fall 2026** — after this
course runs. LCME's proposed revised Standard 7, Element 7.2 names "appropriate
use of artificial intelligence and other emerging technologies in diagnosis and
patient management" and requires *experiential* learning; it was approved in
principle in February 2025 but is not yet in force. The AMA adopted AI-literacy
policy in November 2025 with model learning objectives still forthcoming.

So: build now, remap later. Tagging every module to a stable ID makes the eventual
crosswalk a mapping exercise rather than a rewrite.

---

## Core

### AIM-1 — Foundations of AI and data
What AI and machine learning are; supervised vs. unsupervised learning; how LLMs
differ from earlier AI; training data, model outputs, and probabilistic reasoning;
why hallucination is a property of the mechanism rather than a bug; the role of
human curation and RLHF.

*In every framework reviewed; 79% of existing programs.*

### AIM-2 — Critical appraisal of AI tools and outputs
Evaluating accuracy, calibration, contextual appropriateness, and
generalizability; validation, dataset shift, and performance degradation across
populations; recognizing hallucination and fabricated citations; knowing when AI
is the wrong tool. Extends to appraising the *evidence* about AI — distinguishing
a vendor pre/post pilot from a randomized trial.

*Top-three recurring emphasis in Hunt et al. Russell domain 4.*

### AIM-3 — Bias, equity, and social implications
Sources of bias in data and outputs; how proxy choice encodes inequity; black-box
models and interpretability; differential performance across demographic groups;
how social and economic systems shape which tools get built and deployed.

*Russell domain 2; Hunt domain 1; the two highest-ranked competencies in the
Chinese CAIP consensus.*

### AIM-4 — Ethics, law, regulation, and professionalism
Data privacy and HIPAA; informed consent and transparency; liability and
accountability; FDA pathways for AI-enabled devices and the device/non-device
boundary; attribution and academic integrity; automation bias and deliberate skill
preservation; professional responsibility for AI-influenced decisions.

*The most-emphasized area across the entire corpus, and the single most common
required topic in US medical schools per AAMC survey data.*

### AIM-5 — Clinical application and practical use
Using AI in real workflows; clinical decision support; ambient documentation;
diagnostic and imaging AI; prompt construction and iteration; interpreting AI
output inside clinical reasoning; keeping decision-making physician-led.

*Present in 100% of existing programs. The proposed LCME element requires
experiential learning here specifically — this domain cannot be met by lecture.*

### AIM-6 — Communication with patients about AI
Explaining when and how AI is involved in a patient's care; disclosure and consent
conversations; addressing concerns and misconceptions; recognizing that
AI-generated patient-facing information is systematically less persuasive and
needs clinician mediation.

*Named in nearly every framework — Russell, Singla, Hunt, and the AAMC's stated
goals — and taught in only 21% of existing programs. **This is the largest gap
between consensus and practice and the signature element of this course.***

---

## Extension

### AIM-7 — Workflow, systems, and implementation
How AI changes teams, roles, and responsibilities; human factors and alert
fatigue; local governance and procurement; monitoring deployed tools.

### AIM-8 — Health data science
Data provenance, quality, and governance; statistics for model evaluation
(sensitivity/specificity, AUC, calibration); working with EHR data; collaborating
with data scientists.

*Rated optional by a higher proportion of Delphi experts. Required-light,
elective-deep is a defensible split.*

### AIM-9 — Research, innovation, and scholarship
Appraising AI research and reporting standards; using AI in literature search and
synthesis with proper attribution; IRB considerations; participating in validation
studies.

---

## Cross-cutting

### AIM-X — Professional identity and adaptability
Not a content domain but a stance. Every framework asserts it; most curricula omit
it. The AI-PACE analysis finds the affective domain consistently
under-represented, and the Macy Foundation recommendations call for reevaluating
foundational physician competencies for the AI era.

Concretely: self-assessment of one's own AI knowledge gaps, a personal learning
plan, comfort with rapid change, and a considered, defensible position on what
parts of clinical judgment should never be delegated.

For an ungraded four-week elective with MS4s weeks from residency, this domain is
not decoration — it is the part most likely to still matter in five years, when
every specific tool taught here has been replaced.

---

## Coverage rules

- Every module tags the domains it serves.
- **AIM-1 through AIM-6 must each be touched at least once** in any assembled
  four-week offering; AIM-4 and AIM-5 should recur, since they are the ones
  accreditation will eventually ask about.
- AIM-7 through AIM-9 are optional and belong to enrichment modules.
- *Fall 2026 exception (decided 2026-10-07):* the core chapters do not include
  bias and equity; AIM-3 is covered by a week 2 Friday scenario card and the
  bias chapter on the menu. See constraint 5 in `design-constraints.md`.
- AIM-X is not a session. It is the recurring closing question — *what did this
  change about how you will practice?* — and the subject of the final session.
