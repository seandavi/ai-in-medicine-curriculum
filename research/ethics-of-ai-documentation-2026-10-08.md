# The ethics of AI documentation: what the literature says, for the week 4 chapter

Prepared 2026-10-08 by Claude Code (Opus 5.5) at the course director's request.
This is a design file, not student-facing content. It has not been checked by
a person yet. Every PMID below was looked up in PubMed on 2026-10-08 and its
title, journal, year, and abstract were read. Full text was read only where
the evidence table says so. Guidance documents were read on the issuing
body's own site where the table says so.

The director judged `chapters/core-ethics-regulation.qmd` to be about
liability, not ethics. This note asks what the ethical questions are, and
what the evidence says about each, so the chapter can be rebalanced.

## 1. Question and method

**Question.** What genuinely ethical questions (not legal or regulatory ones)
arise when clinicians use AI documentation tools: ambient scribes, AI-drafted
notes, and AI-drafted patient messages? What do empirical studies and serious
ethics scholarship say about each?

**What other chapters already own.** The patient communication chapter owns
the disclosure conversation, the Duke portal-message studies
[@pmid:40067301; @pmid:42412426], the UK GP survey [@pmid:42386325], and the
"what can be refused" table. The bias and equity chapter owns proxies and
Jabbour [@pmid:38112814]. The centaur and cyborg chapter owns deskilling
[@pmid:40816301] and the drafted-reply workload study [@pmid:38506805]. This
note points to those and does not repeat them.

**Searches run in PubMed on 2026-10-08.** "Screened" means the title was read;
"abstracts" means the abstract was opened and read.

| # | Search (short form) | Limits | Total | Titles screened | Abstracts read |
|---|---|---|---|---|---|
| 1 | ambient OR AI scribe OR digital scribe AND ethic/consent/autonomy/trust (all fields) | 2022 on | 2,299 | 40 | 0 (dominated by air-pollution papers; replaced by 3) |
| 2 | ambient AI scribe randomized trial burnout | 2024 on | 7 | 7 | 6 |
| 3 | ambient/scribe/AI-generated/documentation in title AND ethic/consent/moral/responsibility/accountab in title AND AI | 2022 on | 63 | 50 | 10 |
| 4 | ambient or scribe in title AND patient(s) in title AND perspective/attitude/perception/experience/survey | 2023 on | 36 | 36 | 10 |
| 5 | "Racial disparities in automated speech recognition" (title) | none | 2 | 2 | 1 |
| 6 | ambient/scribe AND language/Spanish/limited English/interpreter/equity/disparity/accent | 2023 on | 137 | 137 | 6 |
| 7 | "responsibility gap" AND medicine/health/clinical | none | 16 | 16 | 3 |
| 8 | "moral deskilling", or deskilling AND ethic (title) AND AI | none | 21 | 21 | 0 new |
| 9 | Char 2018 NEJM (title); patient message/portal/inbox AND disclosure AND AI; automation bias/complacency/overreliance AND scribe/documentation | 2023 on | 1; 4; 23 | all | 5 |
| 10 | open notes AND AI/ambient/scribe; ACP AI position paper (title); scribe recordings AND privacy/secondary use | 2023 on | 18; 1; 2 | all | 5 |
| 11 | Reis 2024 believed AI involvement (title); disclosure/label AND trust AND AI AND experiment | 2023 on | 1; 3 | all | 1 |
| 12 | Goddu 2018 stigmatizing language (title); stigmatizing language AND scribe/LLM; ambient/scribe AND resident/trainee/student/education (title) | 2023 on for 2nd and 3rd | 3; 5; 55 | all | 5 |

About 400 titles screened and about 56 records opened. Six records had no
abstract; four of those were read in full text from PubMed Central (table).
Two (a *Lancet Digital Health* comment on the "consent gap" [PMID 42665470]
and a reply by Sun and colleagues [PMID 41229189]) could not be read beyond
the title and are **not** cited. Twelve keys already used in the book's
chapters (Price, Mello, the juror studies, Jabbour, Wu, and others) are
named here only as pointers; their titles were re-checked in PubMed, and
the abstracts of three of them (Duke survey, Duke interviews, UK GP survey)
were re-read. Semantic Scholar was not used. Prose is about 3,650 words; the
two tables add about 1,350.

**Guidance documents.** The AMA's November 2024 board report, *Augmented
Intelligence Development, Deployment, and Use in Health Care*, was read in
full as a PDF from ama-assn.org. WHO's 2021 *Ethics and governance of
artificial intelligence for health*: the publication page and the WHO news
release listing the six principles were read; the PDF was not. WHO's 2025
guidance on large multi-modal models: only the publication page was read (the
PDF returned HTTP 403). The ACP position paper [@pmid:38830215]: abstract
only (the journal page returned HTTP 403). AAMC principles were not
re-read; they address medical education, not documentation.

**What this method misses.** Philosophy journals outside PubMed (for
example, the original "responsibility gap" and "moral deskilling" papers);
non-English work; grey literature beyond the AMA and WHO pages; legal
scholarship by design.

**How strong is the field?** Thin and new. Most ethics papers are 2025 to
2026 commentary. The empirical base is three small-to-mid randomized trials
of clinician outcomes, large but uncontrolled patient surveys, simulation
studies of errors, and one QI pilot of note quality. No study randomizes
patients to consent methods, and none measures harm to patients from scribe
errors in real care.

## 2. What the evidence says, by area

Mr. Alvarez, for reference: stopped apixaban for nosebleeds, taking
over-the-counter naproxen, plan left as "we'll come back to it"; the draft
says he "continues apixaban without bleeding complications."

### 2.1 Frameworks, and the confusion of ethics with liability (area 1)

**What it says.** A 2025 scoping review of 34 papers on digital health found
that moral responsibility "is often equated with liability or
accountability, without clear justification" [@pmid:39614032]. That is the
director's critique of the chapter, stated in the literature. The same review
describes the "responsibility gap": the worry that no one can be fully
responsible for an AI-generated outcome. A 2026 *JME* paper argues the gap
can be narrowed by asking who authored and who selected the cause of an
error [@pmid:40441855]. A 2026 WHO *Bulletin* paper adds that when
responsibility is spread across clinicians, institutions, and vendors, harm
falls unequally [@pmid:42819652].

The frameworks used for documentation specifically are mostly the four
principles plus justice and safety. Sun, Miller, and Hull map equity, the
clinician-patient relationship, and transparency onto autonomy and
accountability [@pmid:40436441]. Anderson and colleagues name safety, bias,
data ownership, and justice [@pmid:41453133]. WHO's six principles (protect
autonomy; well-being and safety; transparency; responsibility and
accountability; inclusiveness and equity; responsive and sustainable AI) are
the most widely used official set (WHO news release, 28 June 2021). Ursin
and Salloch take a different line: a scribe is an "epistemic agent" that
shapes what is known about the patient, not a transcription tool, with risks
to the patient's narrative and to "epistemic justice" [@pmid:42060927].

There is a real disagreement worth teaching. Armitage argues that within
documentation, Sun's concerns "either do not arise or are easily mitigated"
by clinician review, because the source is the clinician's own visit
[@pmid:40717487] (full text read). The empirical sections below test that
premise: review is uneven (2.4), the tool errs more for some speakers (2.5),
and drafts shift what clinicians decide (2.7).

**Strength.** Conceptual. The scoping review is the only systematic piece.

**Use in the chapter.** Pose Armitage's claim ("review fixes it") and let
Mr. Alvarez's draft test it: the clinician did review, and the sentence is
still wrong.

### 2.2 The record as a moral object (area 2)

**What it says.** The note is read by the next clinician, and its words
change their care. In a randomized vignette study, 413 trainees who read a
note with stigmatizing language about a man with sickle cell disease had
more negative attitudes and chose less aggressive pain treatment than those
who read a neutral note about the same patient [@pmid:29374357]. A 2026
*Hastings Center Report* paper argues that documentation ethics (language,
power, justice) belongs in undergraduate teaching [@pmid:42475140].

Several 2026 papers argue that a scribe's note mixes things that should be
kept apart. Roth and Ayers separate generated narrative, generated
observation, and generated diagnostic reasoning, each with its own failure
mode [@pmid:42586083]. McGaughey and colleagues call the third "inference
impersonation": in the assessment and plan, the scribe does not transcribe
reasoning, it writes it, and the reader cannot tell which is which
[@pmid:42745555]. Chen, Leung, and Bajra list four aims of a note: a note to
self (reasoning), to others, for billing and law, and to the patient in the
era of open notes [@pmid:42258767]. Calvert argues that generated notes may
flatten the illness narrative the patient later reads [@pmid:42617064].

On attestation: a content analysis of 74 official guidance documents found a
shared "drafting fiction": AI text is treated as provisional until the
clinician authenticates it, which rests on an "underspecified human control
assumption" with no defined standard for review or protected review time
[@pmid:42837370]. A thematic analysis of 484 clinician comments on Reddit
found clinicians describing the signature as a "legal shock absorber" for
institutional liability [@pmid:42378622] (low-grade evidence: self-selected
online comments).

**Strength.** One randomized vignette study (Goddu) for "words in the record
change care". The rest is argument and document analysis.

**Use in the chapter.** "Continue apixaban" is inference impersonation: the
patient never said it, the clinician never decided it, and the next team
will act on it.

### 2.3 Consent as respect, not a statute (area 3)

**What it says.** Patients' agreement depends on what they are told. In one
academic pilot, 81.6% consented after basic information and 55.3% after
hearing about AI features, data storage, and corporate involvement; 64.1%
held the physician responsible for errors and 76.7% held vendors responsible
for breaches [@pmid:40694347] (already in the chapter). In a Canadian online
survey of 12,153 adults, only 28.3% were aware of AI scribe use and 61.8%
were reluctant about future use; privacy concern lowered the odds of
willingness (aOR 0.65) [@pmid:41350107]. Before rollout at UC Davis, 48% of
1,893 respondents were favorable and 19% unfavorable, and patients rated
previsit education and permission as very important; the response rate was
20% and skewed older and White [@pmid:41308194]. After use, at Stanford,
70.1% of 2,202 respondents found the scribe helpful and 73.6% wanted it
again [@pmid:42290933]: these are people who had already agreed.

Is "no" a real choice in the room? O'Neil, Rodman, and Lehmann argue that a
physician's authority "may inadvertently pressure patients," and suggest
advance notice, nonclinical staff confirming the preference, and opting in or
out without physician pressure. They also ask what happens if clinicians
start refusing patients who decline [@pmid:41767129] (full text read). In a
small mixed-methods study (n = 20), patients asked for advance notice so they
could decide [@pmid:42648708]. Physicians in a drafted-reply pilot named
consent and patient misunderstanding of AI's role as ethical concerns
[@pmid:41726446].

Ongoing versus one-time consent: raised as an open question
[@pmid:41767129], but no study compares them.

**Strength.** Surveys and QI with selection bias; no trial of consent
methods. The drop from 81.6% to 55.3% is the most teachable number.

**Use in the chapter.** Ask whether Mr. Alvarez, told by his own doctor at
the start of the visit, could comfortably have said no, and what would make
that easier.

### 2.4 Justice: who the tool serves and fails (area 4)

**What it says.** The speech-recognition layer is not equal. Five commercial
systems had an average word error rate of 0.35 for Black speakers and 0.19
for White speakers, on matched audio [@pmid:32205437]. In simulated visits,
one scribe's summaries were stable across seven accents but recognition
dropped sharply for phonological speech impairment [@pmid:42031419]. In
simulated English and Spanish visits, scribes carried interpreter errors
into the note [@pmid:42520279]. UK GPs reported more errors in non-English
consultations (31%) [@pmid:42386325]. In the Canadian survey, people with
lower education and income were less favorable toward scribes
[@pmid:41350107]. A nursing commentary argues that scribe studies treat
equity "as a caveat" instead of measuring it [@pmid:42202251].

Who bears the cost of errors is argued, not measured: the WHO *Bulletin*
paper says diffused responsibility distributes harm inequitably
[@pmid:42819652].

**Strength.** Koenecke is strong for 2019-era speech recognition but
predates current scribes. The scribe studies are simulations. No real-world
study reports error rates by patient race, language, or disability.

**Use in the chapter.** If Mr. Alvarez had spoken through an interpreter,
the draft might have been more likely to be wrong, and he less able to
read and correct it. Link to the bias chapter, do not repeat it.

### 2.5 The relationship, and the trade-off (area 5)

**What it says.** The clinician benefit is now tested in randomized trials.
In a stepped-wedge trial of 66 clinicians, ambient AI reduced work
exhaustion and interpersonal disengagement (-0.44 on a five-point scale);
the increase in professional fulfillment was not significant; note time fell
0.36 hours a day [@pmid:41625485]. In a three-arm trial of 238 physicians,
one of two scribes cut time in notes by 9.5% and the other did not;
burnout and task-load measures improved as secondary outcomes needing
confirmation; clinicians reported clinically significant inaccuracies
"occasionally" [@pmid:41497288]. A crossover trial of 160 clinicians found
both products reduced burnout scores but not after-hours EHR time
[@pmid:41729180].

The patient-side benefit is less clear. In an open-label phase patients said
the physician was more focused on them, but in a masked comparison of 304
patients the relationship score did not differ [@pmid:38834180]. In 31,917
surveys, patient ratings of communication did not change relative to
controls [@pmid:42334196]. In 8,120 surveys, scribe use was linked to one
small gain (satisfaction with time spent) and no difference in other domains
[@pmid:41760358]. A 2026 rapid scoping review concluded the evidence "does
not yet support widespread adoption" [@pmid:42712310]. A commentary argues
scribes move effort from writing to checking rather than removing it
[@pmid:42202251].

**Strength.** Moderate for clinician well-being (randomized, but short,
single-system, and unblinded); weak to null for patient-perceived presence.

**Use in the chapter.** Name the trade honestly: the tool helps you (good
evidence) and has not been shown to help Mr. Alvarez's experience of the
visit (null so far), while the error risk is his.

### 2.6 Honesty and disclosure (area 6)

**What it says.** Telling people AI was involved costs some trust. In two
preregistered experiments (n = 2,280), identical medical advice labeled "AI"
or "human + AI" was rated less reliable and less empathetic than advice
labeled "human," and people were less willing to follow it
[@pmid:39054373]. The Duke survey found a smaller effect for portal replies
[@pmid:40067301] (owned by the patient communication chapter).

The AMA's 2024 policy goes further than most: AI "cannot augment, create, or
otherwise generate records, communications, or other content on behalf of a
physician without that physician's consent and final review"; use that
"directly impacts... the medical record" should be documented in it; and
"where patient-facing content is generated by AI, the use of AI in
generating that content should be disclosed or otherwise noted within the
content." The AMA report separates disclosure from informed consent and
grounds disclosure in its Code of Medical Ethics, which "physician use of AI
is not an exception to." Sun and colleagues propose telling patients when
AI-generated documentation "meaningfully impacts their understanding of
care" [@pmid:40436441]; Armitage argues this is unnecessary once the
clinician has edited the text [@pmid:40717487].

**Strength.** Experimental evidence on the trust cost is decent (preregistered,
large, but vignettes). Whether disclosure changes outcomes is unknown.

**Use in the chapter.** One line connecting to week 3: honesty may cost a
little trust, and the chapter's ethical question is whether a cost to you
justifies not telling him.

### 2.7 Professional responsibility and the duty to review (area 7)

**What it says.** Review is the safeguard, and it is uneven. In the pilot
the chapter already uses, 14.9% of notes were signed with no edits, and the
share of words physicians changed ranged from 1.9% to 69.3% across
physicians [@pmid:41996389]. In a simulation with six radiation
oncologists, GPT-4 drafts of patient-message replies posed a risk of severe
harm in 7.1% of assessments and death in 0.6%; edited replies were closer
in content to the drafts than to the physicians' own replies, which the
authors read as anchoring and automation bias [@pmid:38664108] (full text
read). Physicians in a drafted-reply pilot placed ethical responsibility on
users, not the technology [@pmid:41726446].

For trainees, McGaughey [@pmid:42745555] and an internal medicine program's
guardrails from a pilot with 48 residents [@pmid:41627656] both recommend
that learners reason before seeing the draft. In first-year students who
wrote their own OSCE note before seeing an AI note, the hybrid note was no
worse, and the authors credit that order of work [@pmid:42125891].

Professional bodies: WHO's principle 4 says stakeholders are responsible for
use "under appropriate conditions"; the AMA requires final physician review
(above); the ACP grounds its positions in its Ethics Manual
[@pmid:38830215] (abstract only; specific recommendations
[VERIFY: journal page blocked]). "Moral deskilling" as a named concept did
not appear in PubMed documentation papers; Ursin and Salloch use "cognitive
deskilling" and "deprofessionalization" [@pmid:42060927].

**Strength.** Chen is a small simulation but the cleanest evidence that
drafts change decisions, not just wording. Taylor is real-world but one
system and self-selected reviewers.

**Use in the chapter.** The plan line is where Mr. Alvarez's draft does the
reasoning; the duty is to decide the anticoagulation plan yourself before
reading what the draft decided.

### 2.8 Data and privacy as an ethical question (area 8)

**What it says.** O'Neil and colleagues argue that a full visit transcript
may capture things a clinician typing would have left out, such as abortion
counseling in a restrictive state or immigration status, and that HIPAA puts
no limit on use of de-identified data [@pmid:41767129] (full text; their
claim that transcripts are legally discoverable is a legal assertion,
[VERIFY]). Patients care: consent fell when storage and corporate
involvement were explained [@pmid:40694347]; privacy concern was the
strongest negative predictor in the Canadian survey [@pmid:41350107]; 15% of
concern comments at UC Davis were about privacy [@pmid:41308194]. Blease
connects open notes, chatbots, and "surveillance capitalism"
[@pmid:38050159]. The AMA report calls for data minimization and ways to
"grant, deny, or revoke consent" for data use.

**Gap.** No PubMed study found here measures what patients expect about
vendors training models on their recorded visits, or what vendors do.

**Use in the chapter.** Mr. Alvarez talked about nosebleeds and a knee; ask
what else people say in a visit, and whether "I'll find out where it goes"
is an answer you owe before the recording, not after.

## 3. Evidence table

FT = full text read; Abs = abstract read.

| Key | First author, year, journal | Design | n / setting | Finding to cite | Read |
|---|---|---|---|---|---|
| [@pmid:39614032] | Meier, 2025, *Med Health Care Philos* | Scoping review | 34 papers | Moral responsibility often equated with liability without justification | Abs |
| [@pmid:40441855] | Barman, 2026, *J Med Ethics* | Ethics analysis | n/a | Responsibility gap reframed via causal selection and authorship | Abs |
| [@pmid:42819652] | Mourão, 2026, *Bull WHO* | Policy analysis | n/a | Diffused responsibility distributes harm inequitably | Abs |
| [@pmid:40436441] | Sun, 2026, *J Med Ethics* | Ethics analysis | n/a | Equity, relationship, transparency; notify patients; require review | Abs |
| [@pmid:40717487] | Armitage, 2025, *J Eval Clin Pract* | Reply | n/a | Review by the clinician mitigates Sun's concerns | FT |
| [@pmid:41453133] | Anderson, 2026, *JAMIA* | Ethics analysis | n/a | Safety, bias, data ownership, justice | Abs |
| [@pmid:42060927] | Ursin, 2026, *JMIR Med Inform* | Ethics analysis | n/a | Scribes as epistemic agents; narrative and epistemic justice risks | Abs |
| [@pmid:41767129] | O'Neil, 2026, *Mayo Clin Proc Digit Health* | Ethics analysis | n/a | Authority may pressure consent; sensitive content captured | FT |
| [@pmid:29374357] | Goddu, 2018, *J Gen Intern Med* | Randomized vignette | 413 trainees | Stigmatizing note language worsened attitudes and pain treatment | Abs |
| [@pmid:42475140] | Wilfand, 2026, *Hastings Cent Rep* | Ethics/education | n/a | Teach documentation ethics in medical school | Abs |
| [@pmid:42586083] | Roth, 2026, *Lancet Psychiatry* | Personal view | n/a | Narrative, observation, reasoning are distinct operations | Abs |
| [@pmid:42745555] | McGaughey, 2026, *Acad Med* | Perspective | n/a | "Inference impersonation" in the assessment and plan | Abs |
| [@pmid:42258767] | Chen CA, 2026, *JMIR Med Educ* | Perspective | n/a | Four aims of a note, incl. the patient reader | Abs |
| [@pmid:42617064] | Calvert, 2026, *Clin Infect Dis* | Essay | n/a | Generated notes may flatten the illness narrative | Abs |
| [@pmid:42837370] | Atiku, 2026, *PLOS Digit Health* | Document analysis | 74 guidance documents | "Drafting fiction"; review standard undefined | Abs |
| [@pmid:42378622] | Atiku, 2026, *J Eval Clin Pract* | Thematic analysis | 484 Reddit comments | Signature as "legal shock absorber" | Abs |
| [@pmid:40694347] | Lawrence, 2025, *JAMA Netw Open* | QI, mixed methods | 18 clinicians, 103 patients | Consent 81.6% to 55.3% with more detail | Abs |
| [@pmid:41350107] | Chandrasekaran, 2026, *JAMIA* | Cross-sectional survey | 12,153 Canadian adults | Awareness 28.3%; 61.8% reluctant; privacy aOR 0.65 | Abs |
| [@pmid:41308194] | Leiserowitz, 2025, *JMIR Med Inform* | Pre-implementation survey | 1,893 patients, UC Davis | 48% favorable, 19% unfavorable; consent valued | Abs |
| [@pmid:42290933] | Shah, 2026, *JAMIA Open* | QI survey | 2,202 patients, Stanford | 70.1% helpful; 73.6% want future use | Abs |
| [@pmid:42648708] | Nguyen, 2026, *Appl Clin Inform* | Mixed methods | 20 patients | Patients want advance notice | Abs |
| [@pmid:41726446] | Hu, 2024, *AMIA Annu Symp Proc* | Interviews | 21 physicians | Consent, transparency; responsibility lies with users | Abs |
| [@pmid:32205437] | Koenecke, 2020, *PNAS* | Audit of 5 ASR systems | 115 speakers | WER 0.35 Black vs 0.19 White | Abs |
| [@pmid:42031419] | Draper, 2026, *BMJ Health Care Inform* | Simulation | 1 scribe, actors | Accents stable; phonological impairment worse | Abs |
| [@pmid:42520279] | Rabotin, 2026, *JMIR Med Inform* | Simulation | English and Spanish visits | Interpreter errors propagated into notes | Abs |
| [@pmid:42202251] | Ronquillo, 2026, *J Med Internet Res* | Commentary | n/a | Equity treated as caveat; effort moves to verification | Abs |
| [@pmid:41625485] | Afshar, 2025, *NEJM AI* | Stepped-wedge RCT | 66 clinicians | Exhaustion -0.44; fulfillment not significant | Abs |
| [@pmid:41497288] | Lukac, 2025, *NEJM AI* | 3-arm RCT | 238 physicians, UCLA | One scribe cut note time 9.5%; inaccuracies "occasionally" | Abs |
| [@pmid:41729180] | Chowdhury, 2026, *JAMIA* | Crossover RCT | 160 clinicians, Duke | Both reduced burnout; after-hours time unchanged | Abs |
| [@pmid:38834180] | Owens, 2024, *Appl Clin Inform* | Observational, masked arm | 304 patients | No difference in relationship score | Abs |
| [@pmid:42334196] | Taylor, 2026, *JAMIA* | Difference-in-differences | 31,917 surveys | No change in communication ratings | Abs |
| [@pmid:41760358] | Patel, 2026, *Appl Clin Inform* | Observational | 8,120 patients | Small gain in perceived time only | Abs |
| [@pmid:42712310] | Lawrence R, 2026, *BMJ Digit Health AI* | Rapid scoping review | 21 studies | Evidence does not yet support wide adoption | Abs |
| [@pmid:39054373] | Reis, 2024, *Nat Med* | Preregistered experiments | 2,280 adults | "AI" label lowered reliability, empathy, willingness | Abs |
| [@pmid:41996389] | Taylor, 2026, *JMIR Med Inform* | QI pilot | 356 notes reviewed | 14.9% unedited; edits 1.9% to 69.3% by physician | Abs |
| [@pmid:38664108] | Chen S, 2024, *Lancet Digit Health* | Simulation | 6 oncologists, 100 messages | Drafts: severe harm 7.1%; edits anchored to drafts | FT |
| [@pmid:41627656] | Abernethy, 2026, *J Gen Intern Med* | Program report | 48 residents | Seven guardrails for trainees | Abs |
| [@pmid:42125891] | Talwalkar, 2026, *JMIR Med Educ* | Nonrandomized trial | 104 first-year students | Own note first, then AI: no loss in quality | Abs |
| [@pmid:38830215] | Daneshvar, 2024, *Ann Intern Med* | ACP position paper | n/a | Positions grounded in ACP Ethics Manual | Abs |
| [@pmid:38050159] | Blease, 2024, *J Med Ethics* | Ethics analysis | n/a | Open notes, chatbots, and privacy | Abs |
| AMA 2024 | AMA Board report, Nov 2024 | Policy | n/a | Final physician review; disclose AI in patient-facing content | FT (ama-assn.org PDF) |
| WHO 2021 | WHO, 28 June 2021 | Guidance | n/a | Six principles | News release and publication page |

## 4. What the current chapter has, and what is missing

**Has.** A strong scenario and draft note; the error data
[@pmid:41996389]; the four elements of negligence; the learned intermediary
doctrine; the Price, Gerke, and Cohen grid and two juror studies; Jabbour;
the consent figures [@pmid:40694347] and the Sharp, Sutter, and MemorialCare
lawsuits; HIPAA and BAAs; an FDA summary; a good Do (draft, mark each
sentence, decide the apixaban plan, role-play the explanation). Ethics
appears in one sentence ("an ethical question first") and is not developed.

**Missing.**
- What the clinician owes, as distinct from what the clinician risks: the
  record as a promise to the patient and the next clinician.
- Any ethics source. Every citation in the body is legal, regulatory, or an
  error study.
- Consent as a choice: power in the room, who asks, when, and how often.
- Justice: who the tool fails, and who bears the error.
- The honest trade-off between clinician well-being (now randomized
  evidence) and patient risk.
- The duty to review as a professional virtue, with evidence that drafts
  shape decisions [@pmid:38664108].
- Privacy beyond the BAA.
- A reasoned disagreement (Sun versus Armitage) for students to weigh.

## 5. Proposed outline for a rebalanced chapter

**Recommendation (mine, for the director to accept or change).** About 3,200
words of reading, about 60 minutes in all. Retitle: "Ethics of the drafted
note: what you owe when you sign." Keep Mr. Alvarez, the draft, the
pipeline, and the Do. Move the liability grid, juror studies, Jabbour, and
the FDA summary to Go deeper.

1. **Objectives** (rewritten): name what a signed note promises and to whom;
   judge whether consent was a real choice; say who a scribe is most likely
   to fail; weigh clinician benefit against patient risk with evidence; say
   what you would disclose; decide what you would do before signing.
2. **Scenario** (keep, about 250 words). Change the closing question from
   "who wrote this sentence?" to "what did you owe Mr. Alvarez when you
   signed?" The risk manager can stay as a minor beat.
3. **Why this matters** (about 200). UCHealth rollout; the clinician benefit
   is real [@pmid:41625485; @pmid:41497288]; ethics asks what you owe, law
   asks what you risk [@pmid:39614032].
4. **How it works** (about 2,000):
   a. *How a scribe turns a conversation into a note* (keep, trimmed). Add
      that the plan is generated, not transcribed [@pmid:42745555].
   b. *A note is a promise* (about 400): the next reader [@pmid:29374357],
      the patient reader [@pmid:42258767], attestation as honesty, the
      "drafting fiction" [@pmid:42837370].
   c. *Does review fix it?* (about 350): Armitage versus Sun
      [@pmid:40717487; @pmid:40436441], then the evidence: 14.9% unedited
      [@pmid:41996389], drafts anchor decisions [@pmid:38664108].
   d. *Consent he can refuse* (about 350): [@pmid:40694347],
      [@pmid:41767129], [@pmid:41350107]; the conversation itself links to
      week 3.
   e. *Who the tool fails* (about 300): [@pmid:32205437],
      [@pmid:42520279], [@pmid:42031419]; link to the bias chapter.
   f. *Your relief, his risk* (about 300): trials versus null patient
      measures [@pmid:42334196; @pmid:38834180]; the trade, named.
   g. *What happens to the recording* (about 150): [@pmid:41767129]; what
      you can and cannot promise.
   h. *The law, in one section* (about 250): you sign, you answer; no
      verdict yet; consent lawsuits are allegations; BAA in two sentences;
      link to Go deeper.
5. **Watch or listen.** Keep Stanford Legal as optional, or replace with an
   ethics episode [VERIFY: none found and checked in this pass].
6. **Do** (about 40 minutes). Part A unchanged except step 3 adds: "Before
   reading the draft's plan, write your own plan for the apixaban." Part B
   role-play adds one patient question: "Do I have to say yes?" Add a
   two-minute written step: one sentence each for what you owe the patient,
   the next clinician, and yourself.
7. **Check.** Replace "A box for the original note" with "What you owed, and
   to whom."
8. **Standing question.** "What did you owe Mr. Alvarez before you signed,
   and what would you have needed (time, a tool setting, a policy) to give
   it?" Keep the week 1 callback.
9. **Go deeper.** The liability grid [@pmid:31584609], Mello and Guha
   [@pmid:38231630], juror studies [@pmid:32978285; @pmid:42242875],
   Jabbour [@pmid:38112814], cleared is not validated [@pmid:33820998;
   @pmid:39187696], the regulatory detail section unchanged, the Sun and
   Armitage exchange, the AMA policy and WHO principles, and the trainee
   guardrails [@pmid:41627656].

The answer key in `_answers/` would need matching changes.

## 6. Gaps and [VERIFY] items

- [VERIFY] ACP position paper's specific recommendations on documentation
  and disclosure: only the abstract was read.
- [VERIFY] WHO 2025 large multi-modal model guidance: whether it addresses
  clinical documentation, automation bias, or skill loss. PDF blocked (403).
- [VERIFY] O'Neil and colleagues' statement that visit transcripts are
  legally discoverable: a legal claim, not checked.
- [VERIFY] A real, dated ethics podcast or talk on scribes, to replace or
  sit beside the Stanford Legal episode.
- Not cited, could not read: Ngcobo, *Lancet Digit Health* 2026, "The
  consent gap in ambient clinical artificial intelligence" (no abstract, not
  in PMC); Sun and colleagues' reply to Armitage (no abstract).
- No empirical study found on patient expectations about vendors training
  models on recorded visits.
- No real-world scribe error rates by patient race, language, or
  disability.
- No trial of consent methods, and no study of ongoing versus one-time
  consent.
- No study measuring patient harm from scribe errors in real care.
- "Moral deskilling" and the original "responsibility gap" literature sit in
  philosophy journals outside PubMed and were not searched.
- The Lukac trial was also posted as a preprint (PMID 40672471); cite the
  NEJM AI version [@pmid:41497288].
- The AMA report is a board report adopted as policy in November 2024; check
  whether a later version supersedes it before the chapter quotes it.
