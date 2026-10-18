# Answer key: enrichment-writing-voice

Not rendered. Instructor notes for the chapter "Writing with AI and still
sounding like you" (week 2 menu, paired with the Wednesday talk
"Professional work with AI: writing and beyond"). Written 2026-10-18. The
chapter has not yet been run by a student in ChatGPT Edu; the notes on what
to expect are from the design, not from observation. Record what students
actually see.

## The opening scenario

Fictional notes and a composed reply, not a transcript of any tool or any
real applicant. What a student should notice in the AI draft:

- **Details dropped:** the paper log, the minimum count for each item,
  teaching the first-years, "hasn't run out since".
- **Honest line dropped:** "boring job but I liked it".
- **Chatbot vocabulary:** pivotal, underscored, critical importance,
  spearheaded, comprehensive, fostered, seamless, showcased.
- **Inflated claims:** "spearheaded the development of a comprehensive
  inventory management system" for a paper log; "Supply Coordinator", a
  title the notes never gave.
- **A view the student never stated:** "deepened my lifelong commitment to
  serving underserved communities". It may be true; it was not in the notes.
  This is the Jakesch point (doi:10.1145/3544548.3581196) in small form.

A model first two sentences for "What this changes", part 1 (any version in
the student's own words with the dropped details is fine):

> For two years I ran the supply room at our student-run free clinic on
> Saturday mornings. When we ran out of glucose test strips twice in one
> January, I made a paper log with a minimum count for every item and taught
> the first-years to use it, and we have not run out since.

The interviewer test: the student should be able to say what the log looked
like, why strips ran out, and what they learned ("a lot of problems that
look like people problems are system problems") without reading.

## The figure

Reader accuracy at telling AI from human personal statements:

| Study | Readers | Accuracy | Source |
|---|---|---|---|
| Avetisian 2026, orthopaedic surgery residency | 8 (6 attendings, 2 residents) | 41 of 79 = 52%; computed from the paper's 19 of 40 (AI) and 22 of 39 (human), P = .43 | pmid:42005879 |
| Vaccaro 2026, medical school admissions, single-blind RCT | 17 readers, 325 rubrics, 309 essays | 56%; ZeroGPT 91%. AI essays scored 5.02 vs 4.67 (7-point), P = .020 | pmid:41051105 |
| Curry 2025, pediatrics residency | 4 faculty | 59%; negative ICCs (raters disagreed) | pmid:41584952 |

If a student says "so the detector is better than people": in Vaccaro it
was (91%), but the authors judged its false-positive rate still
"unacceptably high" for admissions, and Liang (pmid:37521038) shows the
false positives fall on non-native writers.

## Numbers in the chapter, with sources

- Traylor 2026 (pmid:42890249): 62,132 statements, 5 specialties, one US
  center, 2017 to 2024. 27 LLM-associated words; prevalence 27.9% before
  2024, 45.6% in 2024; about 3 fewer first-person pronouns. It measures
  words, not who used a chatbot.
- Padmakumar & He, ICLR 2024 (doi:10.48550/arXiv.2309.05196): InstructGPT,
  not base GPT-3, reduced diversity; the effect came from model-contributed
  text; user text unaffected.
- Doshi & Hauser 2024 (pmid:38996021): AI ideas raised novelty (8.1% with
  five ideas) and usefulness (9.0%); stories more similar to each other. Do
  not quote "10.7% more similar"; that figure is a share of the human-only
  similarity range.
- Agarwal, Naaman, Vashistha, CHI 2025 (doi:10.1145/3706598.3713564): 118
  participants from India and the US; Indian writing shifted toward Western
  styles.
- Gao 2023 (pmid:37100871): reviewers caught 68% of generated abstracts and
  wrongly flagged 14% of real ones; suspected ones were "vaguer and more
  formulaic".
- Lee, Yin, Jia, Wakslak, Sci Rep 2026;16:13583
  (doi:10.1038/s41598-026-42312-6): pre-registered experiment, N = 269, plus
  a survey; passive copying lowered self-efficacy, ownership, and meaning;
  draft-first "comparable to independent work".
- Gero et al., DIS 2026 (doi:10.48550/arXiv.2604.11009): N = 253; any AI
  help lowered ownership; planning help least, drafting help most; more AI
  contribution raised quality.
- Jakesch et al., CHI 2023 (doi:10.1145/3544548.3581196): N = 1,506;
  opinionated assistant shifted written opinions and later survey attitudes.
- Liang et al. 2023 (pmid:37521038): short report in *Patterns* (PubMed type
  "News"); 7 detectors, 91 TOEFL essays, 61.3% average false positives; US
  eighth-grade essays classified accurately.
- Subillaga 2025 (pmid:40537315): 1,490 general-surgery statements; flagged
  by both GPTZero and Copyleaks in 2023-24, more non-native features (38.7%
  vs 19.6%).
- Krishna et al., NeurIPS 2023 (doi:10.48550/arXiv.2303.13408): DIPPER
  paraphrasing dropped DetectGPT from 70.3% to 4.6% at 1% false positives.
- Kobak et al. 2025 (pmid:40601754): at least 13.5% of 2024 abstracts, up to
  40% in subcorpora. Excess words named in the paper include delves,
  underscores, showcasing, potential, findings, crucial; style words such as
  intricate and notably; and it cites earlier work for pivotal, intricate,
  showcasing, realm, and meticulously. "Foster", "seamless", and "spearhead"
  in Step 5 come from the opening scenario, not from Kobak; the chapter says
  so.
- Wang et al., Findings of EMNLP 2025 (doi:10.48550/arXiv.2509.14543):
  few-shot beats zero-shot for style imitation; more examples add little;
  output drifts to a generic tone, especially for informal writing.
- AAMC "Personal Statement" page, checked 2026-10-18: "The use of AI tools is
  acceptable for brainstorming, proofreading, or editing the personal
  statement, but the final submission should represent your own work." The
  page refers to the 2027 ERAS season. A forum post quotes an older version
  that also excluded "the product of artificial intelligence"; not verified,
  so the chapter does not claim the wording changed.

## The Do: what to look for

- **Step 1 rubric.** Three lines, specific. "Program director; that I fix
  systems; I'd talk about the strip log" is good. "Admissions; that I'm
  passionate; my passion" is the generic answer the chapter is trying to
  move away from; push for a concrete detail.
- **Step 2 interview.** Expected from the design: the chatbot asks good
  follow-up questions and, sometimes, offers a draft anyway despite "do not
  write any part of it". If it does, the student should ignore the draft.
- **Step 3.** The draft is the student's. 100 to 250 words, first person,
  two details from Step 2. Rough is fine.
- **Step 4.** The deliverable is the student's own revision. A student who
  pastes a chatbot rewrite and edits lightly has not met objective 2; the
  Check says so.
- **Step 5, words.** The finding is a decision per word, not zero words.
  "Crucial" in an abstract can be fine. "Delve" rarely is.
- **Step 5, voice check.** A heuristic, nothing more. No study has tested
  whether a chatbot can judge "same author". Credit a student who rereads a
  flagged sentence and keeps it because it is theirs. Do not credit "the AI
  said it sounds like me, so it's fine".
- **Step 6, disclosure.** Names the tool and what it did. "AI was used" does
  not meet it.

## Objectives to activities

| Objective | Where assessed |
|---|---|
| 1 Why "readers can't tell" does not settle it | Why this matters, @fig-readers; Check row 1 |
| 2 Chatbot as interviewer and critic, core by the student | Do Steps 1 to 4; Check row 2 |
| 3 Words and voice checked | Do Step 5; Check row 3 |
| 4 Rules and a disclosure | What the rules say; Do Step 6; Check row 4 |
| 5 Detectors and humanizers | Detectors and "humanizers"; Check row 5 |

## Model Check answers

- Row 1: "Readers can't tell AI from human statements, so the reason to
  draft myself is not getting caught. It is that my statement would sound
  like everyone else's and feel less like mine."
- Row 5: "A detector score is not proof of cheating: detectors flag
  writing by non-native English speakers as AI far more often, and
  paraphrasing defeats them."

## Questions students may ask

- **"Can I use AI to fix my English?"** Yes; the AAMC allows proofreading
  and editing. The chapter's point is to keep the content and details yours.
  The Agarwal study is a reason to check that "fixing" did not also flatten
  the writing toward an American default.
- **"Will programs run my statement through a detector?"** The chapter does
  not answer this. The research notes record an AAMC page saying ERAS itself
  does not use AI to evaluate applications and that its tools do not
  determine whether essays were written with AI; that page was not re-read
  for this chapter. Programs may do their own thing.
- **"Is the brain-scan study real?"** Kosmyna et al. 2025
  (doi:10.48550/arXiv.2506.08872) is a preprint, 54 participants, 9 per arm
  in the key comparison, EEG methods criticized in a later comment. In
  session 1, 15 of 18 in the chatbot group could not correctly quote their
  own essay. Suggestive, not settled.
