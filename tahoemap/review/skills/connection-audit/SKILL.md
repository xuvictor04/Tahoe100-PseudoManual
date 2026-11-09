---
name: connection-audit
description: How to judge each relation of a Tahoe dossier against the literature - the verdict rubric (established, indirect, plausible, unexpected, contradicted), what counts as evidence for co-variation of mRNA, how to treat protein-level knowledge such as STRING physical interactions, the usual reasons an expected connection is absent, confidence levels, and how to fill the review's sections.
---

# Auditing connections

A relation in a dossier is one of: two genes whose mRNAs co-vary (or anti-vary) across ~1,100 drug-doses in ~50 cell
lines at 24 h; a drug that raises or lowers a gene; a line that a drug depletes, or that expresses a gene unusually
high or low. For each relation you examine, ask: does a retrieved paper report this relation, or something that
predicts it, in a comparable setting?

## Verdicts

Give one `connection_verdicts` entry per partner you examined, with this rubric:

| verdict | use it when | citations |
|---|---|---|
| `established` | a retrieved paper reports this relation: the two genes co-regulated (e.g. both shown as targets of one factor in one study, or co-induced by the same stimulus), in the same complex or pathway with co-expression or co-regulation shown, one regulating the other's transcription, or, for a drug, the drug's known effect on the gene (or on its direct regulator, with the gene named as a target) | required |
| `indirect` | no paper on the pair, but retrieved papers place both genes under one regulator or process that the drugs are known to drive (each gene shown as an NRF2 target in its own paper; both p53 targets; both E2F/DREAM cell-cycle genes) | required: at least one per gene, or a review naming both (submit_review refuses an `indirect` with one citation that is not a review) |
| `plausible` | consistent with known biology (related function, the drug's mechanism could explain it) but no paper ties the two or a shared regulator | optional (background only) |
| `unexpected` | no support after the searches you list (pair query with aliases in PubMed; Europe PMC including full text; the shared-regulator query) | none; list the queries in `unexpected[].literature_checked` |
| `contradicted` | a retrieved paper reports the opposite direction in a comparable setting (a drug lowering a gene that the data show raised; anti-correlation where the data show co-variation) | required |

Before `contradicted`, compare the settings: species, cell type, dose and time (24 h here), and the Tahoe baseline
(the median drugged well, not vehicle). A paper on mouse liver at 6 h that disagrees with human cancer lines at 24 h
is a difference of context; say so instead of calling a contradiction.

Call a relation `unexpected` only when the data side is strong: evidence `both halves`, fdr <= 0.05, |cos| >= 0.5,
low mutual rank (<= 10-20), specificity >= 3, not the same locus; for drugs, a clean significant response at more
than one dose or in several lines. Weak data with no literature is uninformative, not unexpected; leave it out or
mention it as weak.

Give no verdict to genomic neighbours (`same locus`, `READTHROUGH RISK`): their co-variation is explained by the
genome. Mention them once in the note's caveats. Pairs with evidence `not reproduced` get a verdict only when they
are the entity's most notable relations, and then the note says they are weak.

## Probable directions

A gene dossier's "Probable direction" tables hold arrows SOURCE → TARGET: the source's state (a recorded mutation, its
absence from some lines, compounds that target its protein, or its natural level) goes with a change of the target
(its level, its drug response, or the cells' numbers under a drug-dose). The sign says what the source's ACTIVITY
probably does to the target: *raises* / *lowers* a level or the cells' numbers; *strengthens* / *weakens* a drug
response, in the target's own direction at each drug-dose. Read induction or repression from ALL the drug-doses the
row lists ("drug-doses carrying the difference"), not from the first one: when every listed fold is below 1x,
"strengthens" means the source deepens the fall - it **represses** the target there, and a paper showing that
repression supports the arrow (do not call it `contradicted` for not "inducing" it); when every one is above 1x, the
source induces it. When the row carries the alert "rises at some drug-doses, falls at others", the sign says only
how strongly the target responds: judge who acts on whom, and do not count papers on induction or repression for or
against the sign. Judge an arrow as a relation with a direction and a sign:

| verdict | use it when | citations |
|---|---|---|
| `established` | a retrieved paper shows the source acting on the target this way: the source's knockdown, knockout, loss-of-function mutation or activation changing the target's mRNA (or its drug response) with this sign, or the target shown as a direct transcriptional target the source induces (or represses); for an arrow to the cells, the source's loss or mutation changing sensitivity to that drug or its class as the sign says | required |
| `indirect` | papers put the target downstream of the source through a named intermediate, or show the target regulated by a factor the source is shown to control, with the sign the data show | required: one per step, or a review naming the chain |
| `plausible` | the source's known function makes the arrow likely, but no paper links the two | optional |
| `unexpected` | a grade A or B arrow without a co-occurrence alert (another alteration on either side), and no paper after the pair searched both ways and with aliases | none; list the queries |
| `contradicted` | a paper shows the opposite sign in a comparable setting (the source's activity lowers what the arrow says it raises; for a drug response, the source's activity making the target respond less where the arrow says it strengthens the response), or the target acting on the source where the paper rules out this direction | required |

- Give the verdict as a `connection_verdicts` entry on the other gene (its symbol as in the dossier; for an arrow to
  the cells, `drug:<the drug's name as in the dossier>`). Its `data_evidence` begins with `probable direction` and the
  arrow as the dossier writes it, then the grade, the sign sentence, the evidence kind, q and the alerts that matter
  ("probable direction TP53 → CDKN1A, grade B: TP53 activity strengthens CDKN1A's drug response (CDKN1A rises:
  1.32x vs 3.00x); recorded TP53 loss-of-function in 10 lines vs 8; q 0.025; KMT2D, CTNNB1 alterations on the other
  side"). Its `relation` says what the papers report about who
  acts on whom, with the sign ("TP53 transactivates CDKN1A; TP53 knockdown abolishes its induction by DNA damage").
  A gene that also has a co-variation verdict gets a second entry; the two are judged separately.
- A paper on the reverse direction alone is not a contradiction: feedback loops are common (TP53 induces MDM2, MDM2
  degrades TP53). Call it `contradicted` only when the paper shows this arrow's sign reversed, or tests this direction
  and finds none.
- Grade C arrows (a gene's natural level, a result significant only within its own group, a comparison the tissue
  can explain, a natural knockout with few lines or concentrated in organs) are leads: give a verdict only when the
  literature speaks clearly, and never `unexpected`.
- An arrow from compounds that target the source (`drug target: level`) concerns inhibiting or activating the source's
  protein: a paper on that inhibition (or on the drug class) can establish it; drugs also act on other proteins, and a
  row naming several targets (HDAC1, HDAC2, ...) is one test that any of them could explain.
- An arrow whose alerts say "co-occurs with X" may be X's effect: say so in `relation` when a paper ties the target
  to X rather than to the source. "tissue-confounded" arrows may be tissue programmes.
- The absence of an arrow says nothing: only recorded mutations, genes absent from some lines, drug targets and
  related pairs (for levels) are tested.

## Transcript-level versus protein-level knowledge

Tahoe sees mRNA, so ask whether the literature relation predicts co-variation of mRNA:

- Subunits of large stable complexes are often transcribed together by shared factors (ribosomal proteins;
  proteasome subunits through NFE2L1/NRF1; respiratory-chain subunits; histones in S phase): absence among the
  partners is surprising and worth a sentence.
- Physical interactions in signalling (kinase-substrate, receptor-adaptor, E3 ligase-substrate, chaperone-client),
  enzyme-substrate pairs and most STRING edges need not co-vary in mRNA at all. Their absence is expected:
  `likely_reason` = "protein-level interaction; no reason for co-regulated mRNA".
- Transcription factors are often activated without a change in their own mRNA (NRF2 stabilised when KEAP1 is
  inactivated, p53 when MDM2 is blocked, HIF1A by hypoxia, NF-kB by IkB degradation, HSF1 by trimerisation). The
  factor's mRNA not moving with its targets is expected; its feedback targets moving with the other targets (MDM2
  with CDKN1A) are the transcriptional signature.
- "Same Reactome pathway" alone is weak: many pathways list hundreds of genes acting at the protein level.
- Paralogs (same HGNC gene group) that co-vary may share regulation, or share reads where their sequences are close.

## Why an expected connection is absent (`missing[].likely_reason`)

Use the dossier's numbers first: a known partner at rank 120 with cos close to the 100th partner's is "nearly
present"; one at cos ~ 0 is unrelated in these data; one "not in the vector space" or "not measured" could not be a
partner at all. Then the usual reasons:

1. not measured in most lines, or not in the vector space because no drug moved it (name the drugs that would be
   expected to);
2. a protein-level relation (above);
3. post-translational activation of a transcription factor (above);
4. the relation needs a stimulus absent from the drug set or from culture: hypoxia, cytokines, infection,
   differentiation signals, tissue or immune context;
5. cell-type or species restriction (the papers are on neurons, hepatocytes, immune cells, or mouse);
6. timing: an early transient response back to baseline by 24 h, or a late secondary one;
7. one partner constitutively saturated, deleted or silenced in many lines (e.g. 9p21 deletions);
8. the pooled median hides a response in a minority of lines: check the single-line tables or tahoe_lookup;
9. the literature link is context-dependent or opposite in direction.

## Confidence

- `high`: a strong, replicated data relation (both halves, fdr <= 0.05; or a drug response at several doses or
  drugs) and a paper reporting exactly this relation in human cells, read in its abstract.
- `medium`: one side weaker (one-half evidence, a single drug-dose, a flagged dose; or a paper in another species or
  cell type, or a review-level statement).
- `low`: weak data (not reproduced, single well, flagged) or only indirect literature.

## Filling the review

- `established`: one item per supported relation, stated as the papers state it, with the dossier's numbers in
  `data_evidence` (cos, evidence, fdr; or fold, z, doses, lines) and the citations you read.
- `unexpected`: strong data, no support; `why_unexpected` says what the literature would predict instead (or that
  nothing links them); `literature_checked` lists the exact queries.
- `missing`: the important known-but-absent partners (and, for drugs and lines, expected responses that are absent):
  `source` STRING, pathway or literature; `data_status` from the dossier (cos and rank, not in the space, not
  measured); `likely_reason`; citations only if a paper supports the expectation.
- `contradicted`: rare; needs a paper with the opposite direction in a comparable setting.
- `connection_verdicts`: the partners you examined, typically 8-20 entries: the strongest replicated partners on
  both sides, every novel candidate, any partner named in another section, and the probable-direction arrows you
  examined (one entry each, as "Probable directions" above describes). Write genes as their symbols in the
  dossier, drugs as `drug:<name as in the dossier>`, cell lines as `line:<cell name>`. Each entry says, in one short
  sentence each, `relation`: what the cited papers report, with its direction ("each an NRF2 target, induced by
  electrophiles"; for `plausible` / `unexpected` the reasoning or "no paper found"), and `data_evidence`: the
  relation in this run's data with its direction and numbers ("moves opposite: cos -0.37, both halves, fdr 0.01").
  The citation checker reads both, and grades a verdict whose papers report the opposite direction from the data as
  not supported: papers showing two genes co-induced do not make a pair that moves opposite `established`.
- `open_questions`: concrete and testable ("Does DMF induce PIR through NRF2 in these lines? NFE2L2 knockdown plus
  DMF, PIR mRNA at 24 h").
