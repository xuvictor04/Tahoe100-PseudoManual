---
symbol: SMAD6
type: gene
tier: 2
tags: [gene, transcription-factor]
generated_by: knowledge/_build/build_vault.py
---

# SMAD6

> [!summary] In one line
> SMAD6 is an inhibitory SMAD: a BMP-induced brake that blocks signalling through its own pathway rather than transmitting it.

## What it is

SMAD6 and SMAD7 lack the C-terminal SSXS motif that makes receptor SMADs phosphorylation substrates, and work as antagonists. SMAD6 acts mainly on the BMP branch: it competes with [[SMAD4]] for binding to activated SMAD1, and recruits the ubiquitin ligase SMURF1 to receptors and SMADs. It is a BMP target gene, which closes a negative-feedback loop. A nuclear repressor role is also reported, with MH1-like DNA binding and recruitment of CtBP and histone deacetylases. Smad6-null mice have valve and outflow-tract defects, and rare human loss-of-function variants are associated with craniosynostosis and bicuspid aortic valve.

## Why it appears in this work

SMAD6 is scored as a transcription factor here and ranks at the negative extreme of the correlation with measured MG53. That direction is only interesting if the regulon means what it claims: a brake's inferred activity reads as the inverse of BMP tone, not as SMAD6 occupying promoters. See [[Transcription factor activity inference]].

## What is uncertain

SMAD6 is a weak case for regulon-based inference. It is not a classical sequence-specific activator; its direct DNA binding is reported in few systems, and most of its output is indirect, through sequestration and degradation. The curated target set is small and its signs are inherited from BMP-response experiments, so the inferred activity is as likely to report BMP tone as SMAD6. No link between SMAD6 and TRIM72 has been reported.

## References

- Imamura et al., 1997, Nature — identified Smad6 as an inhibitor of signalling by the TGF-beta superfamily.
- Hata et al., 1998, Genes & Development — Smad6 inhibits BMP/Smad1 signalling by competing with SMAD4.
- Galvin et al., 2000, Nature Genetics — Smad6-null mice show cardiovascular developmental defects.
- Timberlake et al., 2016, eLife — rare SMAD6 loss-of-function variants with a common BMP2 risk allele in midline craniosynostosis.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00330 |
| As a percentage | +0.23% |
| FDR, exposure-shuffle null | 0.6484 |
| In TP53-wild-type lines / altered lines | 0.00206 / 0.00411 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | -0.340 raw, 0.001 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

### As a transcription factor, against MG53

| | |
|---|---|
| Regulon size used | 18 targets |
| Activity vs MG53 across exposures (r) | -0.263 (q 2.34e-13) |
| With 3 principal components removed | -0.248 (q 5.05e-12) |
| Within line, across exposures (r) | -0.017 (q 0.150) |
| Percentile against all genes | 2.0 |

## Links

- **Concepts:** [[Transcription factor activity inference]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** transcription factor, negative rank
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
- Transcription-factor activity: `upstream_tf/tables/a1a2_tf_summary.csv`
