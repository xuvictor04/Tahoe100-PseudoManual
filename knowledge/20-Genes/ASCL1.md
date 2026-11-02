---
symbol: ASCL1
type: gene
tier: 2
tags: [gene, transcription-factor]
generated_by: knowledge/_build/build_vault.py
---

# ASCL1

> [!summary] In one line
> ASCL1 is a basic helix-loop-helix transcription factor that drives neuronal and neuroendocrine lineage commitment, and acts as a lineage-dependency oncogene in small-cell lung cancer.

## What it is

ASCL1 (Mash1) heterodimerises with E-proteins and binds E-boxes, and is one of the proneural factors: mice lacking it fail to make olfactory and autonomic neurons, and ASCL1 is the indispensable member of the three-factor cocktail that converts fibroblasts directly into neurons. Notch-HES signalling and rapid turnover keep it pulsatile in progenitors, and it must be extinguished for differentiation to finish. In cancer it defines a lineage state rather than a mutation: ASCL1-high small-cell lung cancer, the SCLC-A subtype, depends on it for survival, and its enhancer programme is distinct from the NEUROD1-driven alternative.

## Why it appears in this work

ASCL1 is a candidate upstream regulator of [[MG53 (TRIM72)]] from the activity-inference step, and it is on that list for a structural reason: the TRIM72 promoter's characterised element is an E-box next to a MEF2 site, read in muscle by the myogenic bHLH factors ([[MYOD1]], [[MYOG]], [[MYF5]], [[MYF6]]). ASCL1 reads the same class of E-box. See [[The TRIM72 locus]].

## What is uncertain

There is no evidence that ASCL1 regulates TRIM72; the shared E-box consensus is enough to make inferred bHLH activities overlap, so a score here may be reporting generic E-box occupancy, or the neuroendocrine lines in the panel, rather than ASCL1. The well-supported part of this gene's biology — proneural specification and SCLC lineage dependency — is largely orthogonal to the question this study asks.

## References

- Guillemot et al., 1993, Cell — Mash1-null mice lack olfactory and autonomic neurons.
- Vierbuchen et al., 2010, Nature — Ascl1 with Brn2 and Myt1l converts fibroblasts into functional neurons.
- Augustyn et al., 2014, PNAS — ASCL1 is a lineage-specific oncogene required for survival of ASCL1-high small-cell lung cancer.
- Borromeo et al., 2016, Cell Reports — ASCL1 and NEUROD1 bind distinct enhancer programmes defining SCLC subtypes.
- Rudin et al., 2019, Nature Reviews Cancer — synthesis defining SCLC subtypes, with SCLC-A keyed to ASCL1.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.01320 |
| As a percentage | +0.92% |
| FDR, exposure-shuffle null | 0.0642 |
| In TP53-wild-type lines / altered lines | 0.00869 / 0.01594 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.196 raw, -0.073 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

### As a transcription factor, against MG53

| | |
|---|---|
| Regulon size used | 47 targets |
| Activity vs MG53 across exposures (r) | 0.306 (q 1.80e-19) |
| With 3 principal components removed | 0.217 (q 4.01e-10) |
| Within line, across exposures (r) | 0.035 (q 0.008) |
| Percentile against all genes | 97.9 |

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
