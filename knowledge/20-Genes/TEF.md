---
symbol: TEF
type: gene
tier: 2
tags: [gene, transcription-factor]
generated_by: knowledge/_build/build_vault.py
---

# TEF

> [!summary] In one line
> TEF is a PAR-bZIP transcription factor, one of three clock-output factors with DBP and HLF, found as an activator of the thyrotropin-beta promoter in the embryonic pituitary.

## What it is

TEF (thyrotroph embryonic factor) binds as a homo- or heterodimer to a short TA-rich element shared with DBP, HLF and the repressor [[NFIL3]], which occupies the same site. Cloned from the developing anterior pituitary, where it appears with thyroid-stimulating hormone, it transactivates TSHB; in the adult it is broadly expressed, accumulating on a circadian rhythm in liver and kidney. Function is largely redundant: single knockouts are near-normal, whereas mice lacking DBP, HLF and TEF together develop spontaneous and audiogenic seizures, traced partly to reduced pyridoxal kinase. The three also set the rhythm of hepatic xenobiotic-detoxification genes.

## Why it appears in this work

TEF sits among the positively correlated factors in the activity step. The point a reader needs is the mismatch of timescale: these are 24-hour exposures in pooled, unsynchronised culture, where a circadian output factor has no coherent phase to act in. See [[Transcription factor activity inference]].

## What is uncertain

Two reasons to discount the rank. The regulon is among the smallest scored, so the score averages a handful of transcripts. And the symbol is treacherous: "TEF-1" was the original name for TEAD1, an unrelated factor, so target sets built from older literature can carry TEAD-derived assignments under this label. Redundancy compounds both: targets attributed to TEF are generally shared with DBP and HLF, and the score cannot separate them.

## References

- Drolet et al., 1991, Genes & Development — cloned TEF from the embryonic anterior pituitary and showed transactivation of the TSHB promoter by a new class of leucine-zipper protein.
- Gachon et al., 2004, Genes & Development — mice lacking DBP, HLF and TEF develop epilepsy, with pyridoxal kinase identified as a target gene.
- Gachon et al., 2006, Cell Metabolism — the circadian PAR-bZIP factors control basal and inducible xenobiotic detoxification.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.01401 |
| As a percentage | +0.98% |
| FDR, exposure-shuffle null | 0.0427 |
| In TP53-wild-type lines / altered lines | 0.02115 / 0.00967 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.191 raw, -0.039 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

### As a transcription factor, against MG53

| | |
|---|---|
| Regulon size used | 12 targets |
| Activity vs MG53 across exposures (r) | 0.285 (q 1.12e-16) |
| With 3 principal components removed | 0.232 (q 1.05e-11) |
| Within line, across exposures (r) | 0.020 (q 0.059) |
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
