---
symbol: APEX1
type: gene
tier: 2
tags: [gene, transcription-factor]
generated_by: knowledge/_build/build_vault.py
---

# APEX1

> [!summary] In one line
> APEX1 encodes APE1/Ref-1: the main AP endonuclease of base-excision repair and, separately, a redox cofactor that keeps other transcription factors able to bind DNA.

## What it is

APE1 incises the DNA backbone at abasic sites left by glycosylases, the committed step of base-excision repair. It is abundant, largely nuclear, and essential: homozygous loss is early-embryonic lethal in mice. Its second function was discovered independently, as Ref-1, an activity that restores DNA binding to oxidised AP-1, and was later extended to NF-κB, HIF-1α, STAT3 and p53 — redox chemistry, not sequence-specific DNA binding of its own. The two activities are separable: APX3330 blocks the redox function and spares the endonuclease.

## Why it appears in this work

APEX1 is in the vault because the activity-inference step scored it high as a candidate regulator upstream of [[MG53 (TRIM72)]]. It is better read as a redox reporter than a factor at a promoter: if its inferred activity moves, the likelier cause is an exposure's oxidative tone acting on its partners. Its reported stimulation of p53 DNA binding is this gene's one direct line into [[The p53 pathway]].

## What is uncertain

APE1 is not a sequence-specific transcription factor, so its assigned regulon is borrowed from the factors it reduces, and a high inferred activity may be reporting AP-1, NF-κB or HIF-1α output instead — a limitation of [[Transcription factor activity inference]] applied to a cofactor. How much of the redox function operates at endogenous protein levels, rather than in vitro on oxidised substrate, remains argued. The repair activity itself is not in doubt.

## References

- Demple et al., 1991, PNAS — cloned the major human apurinic/apyrimidinic endonuclease.
- Xanthoudakis and Curran, 1992, EMBO Journal — identified Ref-1 as a nuclear factor that restores AP-1 DNA binding.
- Xanthoudakis et al., 1996, PNAS — Apex-null mouse embryos die early, establishing the gene as essential.
- Jayaraman et al., 1997, Genes and Development — Ref-1 stimulates the DNA binding and transcriptional activity of p53 in vitro.
- Gaiddon et al., 1999, EMBO Journal — Ref-1 associates with p53 in cells, and is required for its transactivation and pro-apoptotic function.
- Tell et al., 2009, Antioxidants and Redox Signaling — review of APE1/Ref-1's dual repair and redox roles.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00182 |
| As a percentage | -0.13% |
| FDR, exposure-shuffle null | 0.5924 |
| In TP53-wild-type lines / altered lines | -0.00413 / -0.00041 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.111 raw, -0.134 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

### As a transcription factor, against MG53

| | |
|---|---|
| Regulon size used | 33 targets |
| Activity vs MG53 across exposures (r) | 0.314 (q 2.20e-23) |
| With 3 principal components removed | 0.262 (q 9.42e-16) |
| Within line, across exposures (r) | 0.020 (q 0.113) |
| Percentile against all genes | 99.5 |

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
