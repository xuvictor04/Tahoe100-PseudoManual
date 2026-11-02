---
symbol: SIX1
type: gene
tier: 2
tags: [gene, transcription-factor]
generated_by: knowledge/_build/build_vault.py
---

# SIX1

> [!summary] In one line
> SIX1 is a homeodomain transcription factor that, paired with an EYA cofactor, switches from repressor to activator and drives the embryonic muscle, otic and kidney programmes.

## What it is

SIX1 is a vertebrate homologue of Drosophila sine oculis. Bound through its homeodomain and SIX domain it recruits DACH proteins and co-repressors; when an EYA protein joins, the output flips to activation, EYA's phosphatase activity being part of the switch. The SIX1-EYA module sits near the top of the skeletal muscle hierarchy, required for normal PAX3 and myogenic-regulatory-factor expression and later for the fast-twitch programme, and it also builds the otic and nephric lineages — mutations disrupting the EYA1-SIX1-DNA interface cause branchio-oto-renal syndrome. In carcinomas it is often overexpressed and reported to promote epithelial-mesenchymal transition.

## Why it appears in this work

SIX1 is a native regulator of the muscle programme [[MG53 (TRIM72)]] belongs to, upstream of [[MYOD1]], [[MYF5]] and the MEF2 factors — but unlike the rest of that programme it is expressed in epithelial tumours, so it is one of few muscle-lineage factors that could act here. See [[Transcription factor activity inference]].

## What is uncertain

Its regulon here is among the smallest scored, so the score is near an average over a handful of transcripts, and small regulons reach a ranking's extremes cheaply. Those targets come from myogenic work, the context these lines lack, so what moved may belong to other regulators. No SIX element has been described at TRIM72; the characterised site there is a MEF2 element beside an E-box.

## References

- Ruf et al., 2004, PNAS — SIX1 mutations cause branchio-oto-renal syndrome by disrupting EYA1-SIX1-DNA complexes.
- Li et al., 2003, Nature — EYA phosphatase activity converts the SIX1-DACH-EYA complex from repression to activation.
- Grifone et al., 2005, Development — Six1 and Six4 are required for Pax3 and myogenic regulatory factor expression during myogenesis.
- Laclef et al., 2003, Development — Six1-null mice show altered myogenesis and muscle patterning defects.
- Micalizzi et al., 2009, Journal of Clinical Investigation — SIX1 overexpression promotes epithelial-mesenchymal transition via TGF-beta signalling.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00642 |
| As a percentage | +0.45% |
| FDR, exposure-shuffle null | 0.2553 |
| In TP53-wild-type lines / altered lines | 0.00745 / 0.00578 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.208 raw, 0.025 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

### As a transcription factor, against MG53

| | |
|---|---|
| Regulon size used | 13 targets |
| Activity vs MG53 across exposures (r) | 0.282 (q 6.61e-17) |
| With 3 principal components removed | 0.385 (q 2.71e-29) |
| Within line, across exposures (r) | 0.013 (q 0.297) |
| Percentile against all genes | 98.3 |

## Links

- **Concepts:** [[Transcription factor activity inference]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** transcription factor, positive rank
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
- Transcription-factor activity: `upstream_tf/tables/a1a2_tf_summary.csv`
