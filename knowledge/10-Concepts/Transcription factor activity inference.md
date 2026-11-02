---
type: concept
tags: [concept, method, transcription-factors]
status: current
---

# Transcription factor activity inference

> [!summary] In one line
> You cannot see a transcription factor's activity in mRNA, so you infer it from its targets' behaviour —
> and in this study the answer was that no inferred factor explains MG53's movement.

## Why infer it at all

A transcription factor's mRNA level is a poor proxy for its activity: the protein may be present but
unphosphorylated, cytoplasmic, or bound by an inhibitor. p53 is the textbook case — its mRNA barely moves
while its activity swings enormously, because regulation is at the protein level through [[MDM2]].

So activity is inferred from consequence instead: take a curated **regulon** — the set of genes a factor is
known to regulate, with signs — and ask how coherently that set moved in a given condition. If a factor's
targets rose together, the factor was probably active. This study uses two regulon collections, CollecTRI
and DoRothEA, and scores 679 factors per drug-dose.

## How it was done here

| Choice | What was used |
|---|---|
| Regulons | CollecTRI (primary) and DoRothEA (replicate) |
| Scoring | univariate linear model over the regulon's members, plus a mean-z variant as a method check |
| Unit | per drug-dose, and separately within cell line across drug-doses |
| Covariates | transcriptome-wide activity, cell counts, cell-cycle phase, UMI depth |
| Robustness | the same correlation after removing 3 and 10 principal components |
| Reference | matched genes and all genes, as a percentile |

Three design points worth knowing, because they are what make the negative result credible:

1. **A positive control.** TP53's own inferred activity was checked against the independently derived p53
   programme and the TP53 genotype labels, so the inference machinery is shown to work on a factor whose
   answer is known (`a3_tp53_positive_control.csv`).
2. **Overlap removal.** A factor's regulon may contain genes near the TRIM72 locus, or mediators that sit
   between the factor and MG53. Both were removed and the correlation recomputed
   (`r_dd_TRIM72_minus_overlap`, `r_dd_TRIM72_plus_mediators`).
3. **A readthrough-aware variant.** Every factor's correlation was recomputed against a readthrough-corrected
   MG53 (`r_dd_TRIM72_rt_*`), because otherwise a factor that drives [[FUS]] would look like a factor that
   drives TRIM72. See [[Readthrough spillover]].

## What it found

The result that matters most is a negative one, and it is clean: **the transcription factors that drive
TRIM72 in its native tissue are not doing so here, because they are not present.** The muscle programme —
MYOD1, MYOG, MYF5, MYF6, the MEF2 family, SRF — is silent or absent in this panel of cancer lines. MYOD1, for
instance, is not even in the expressed gene list. A muscle gene in non-muscle cells has no muscle regulator
to respond to.

What correlations do appear are small, are strongly attenuated by removing principal components, and sit
unremarkably against the matched-gene and all-gene reference distributions. The honest summary is that
**MG53's expression tracks its own genomic neighbourhood far more than any transcription factor** — which is
the same conclusion [[The TRIM72 locus]] reaches from a completely different direction, and the agreement of
two independent lines of evidence is the strongest thing about it.

The p53 pathway as a *candidate regulator of MG53* is treated as part of this question, in
[[Upstream of MG53]].

## What inference of this kind cannot do

- It is only as good as the regulon. CollecTRI and DoRothEA are literature-assembled, biased toward
  well-studied factors, and incomplete for everything else.
- Collinearity between regulons is severe — factors sharing targets get correlated scores, so "factor X's
  activity correlates with MG53" rarely isolates X.
- It cannot distinguish a factor acting on a gene from a factor acting on the cell state that moves the gene.
  The covariate sets and the PC removals are attempts at this, and they are partial.
- With 679 factors tested, the multiplicity is severe and the percentile-against-matched-genes framing is
  what keeps it honest.

## Links

- [[MG53 (TRIM72)]] · [[The TRIM72 locus]] · [[Readthrough spillover]]
- [[Upstream of MG53]] — the findings
- [[Placebo genes and reference families]] — the matched-gene reference used here
- Gene notes: [[MYOD1]], [[MYOG]], [[MYF5]], [[MYF6]], [[MEF2A]], [[MEF2C]], [[SRF]], [[TP53]]

## Sources

- `upstream_tf/tables/a1a2_tf_summary.csv` — 679 factors × 77 columns; the per-factor numbers in every
  transcription-factor gene note come from here.
- `upstream_tf/tables/a4_muscle_promoter_tfs.csv` — the nine muscle factors, with their expression in this
  panel.
- `upstream_tf/tables/a3_tp53_positive_control.csv` — the positive control.
- `upstream_tf/tables/a0_regulons_used.csv.gz`, `a0_regulon_sizes.csv` — the regulons as used.
