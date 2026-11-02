---
symbol: TWIST2
type: gene
tier: 2
tags: [gene, transcription-factor]
generated_by: knowledge/_build/build_vault.py
---

# TWIST2

> [!summary] In one line
> TWIST2, cloned originally as Dermo-1, is a basic helix-loop-helix protein closely related to TWIST1 that acts in dermal and mesenchymal lineages and was characterised from the start as a repressor rather than an activator.

## What it is

TWIST2 shares TWIST1's bHLH domain almost residue for residue, dimerises with the same E proteins and binds the same E-boxes. It was isolated as Dermo-1 in a two-hybrid screen for E12 partners; notably, the original work found it bound E-boxes with E12 but had no detectable activation capacity, repressing myogenic bHLH proteins instead. Expression rises in embryonic and neonatal dermis and falls in adult tissue. Human genetics has been the most informative source since: biallelic loss of function underlies Setleis syndrome, a recessive focal facial dermal dysplasia, while recurrent missense substitutions at one conserved glutamate in the DNA-binding basic domain cause Ablepharon-macrostomia and Barber-Say syndromes — a change of function rather than a loss, with the particular substitution predicting which phenotype appears.

## Why it appears in this work

TWIST2 scores near the top of the transcription-factor activity step, alongside [[TWIST1]]. The honest reading is that the two are one observation, not two: they bind the same motif and are frequently co-expressed. See [[Transcription factor activity inference]].

## What is uncertain

The main caveat is structural rather than biological: TWIST2's regulon overlaps TWIST1's by construction, so the adjacent high ranks are not independent support. Whether TWIST2 has outputs distinct from TWIST1 in any cell type remains partly open: the clean separations come from mouse expression domains and human syndromes, not distinct target sets. If the original characterisation as a repressor without intrinsic activation capacity holds, the activity convention here has the wrong sign for it. The Twist-box/p53 interaction was characterised for TWIST1; the twist box is conserved in TWIST2, but whether it does the same there is not established.

## References

- Li, Cserjesi & Olson, 1995, Developmental Biology — cloned Dermo-1 (TWIST2) as an E12 partner that binds E-boxes without detectable activation and represses myogenic bHLH proteins.
- Marchegiani et al., 2015, American Journal of Human Genetics — recurrent mutations in the basic domain of TWIST2 cause Ablepharon-macrostomia and Barber-Say syndromes.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00182 |
| As a percentage | +0.13% |
| FDR, exposure-shuffle null | 0.8566 |
| In TP53-wild-type lines / altered lines | -0.00684 / 0.00708 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.187 raw, 0.145 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

### As a transcription factor, against MG53

| | |
|---|---|
| Regulon size used | 29 targets |
| Activity vs MG53 across exposures (r) | 0.351 (q 7.24e-25) |
| With 3 principal components removed | 0.311 (q 6.40e-20) |
| Within line, across exposures (r) | 0.026 (q 0.032) |
| Percentile against all genes | 99.7 |

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
