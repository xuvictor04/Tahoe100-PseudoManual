---
symbol: STAT4
type: gene
tier: 2
tags: [gene, transcription-factor]
generated_by: knowledge/_build/build_vault.py
---

# STAT4

> [!summary] In one line
> STAT4 is the signal transducer downstream of interleukin-12 that drives T helper 1 differentiation and interferon-gamma production.

## What it is

STAT4 is one of seven mammalian STATs. After IL-12 engages its receptor, JAK2 and TYK2 phosphorylate a single C-terminal tyrosine; STAT4 then dimerises through reciprocal SH2-phosphotyrosine contacts, enters the nucleus and binds GAS elements. Its output is the Th1 programme — IFNG induction in T and NK cells, with TBX21 as lineage partner — and Stat4-null mice lose essentially all IL-12 responses. Expression is largely confined to lymphoid and myeloid cells. STAT4 is also one of the better-replicated autoimmunity loci, with risk variants in rheumatoid arthritis, lupus and Sjogren's syndrome.

## Why it appears in this work

STAT4 sits among the positively correlated factors in the activity step. The reason to read that as a property of the method rather than of biology is the mismatch of context: STAT4's pathway is immune, these are non-haematopoietic tumour lines, and there is no IL-12 in the medium. See [[Transcription factor activity inference]].

## What is uncertain

A factor whose own transcript is near-absent across most of this panel cannot have had meaningful activity, so the score reports the regulon, not STAT4. That regulon is among the smallest scored, and its members are cytokine- and interferon-inducible genes shared with STAT1 and STAT2 — genes that move under many cytotoxic compounds through interferon responses unrelated to IL-12. The score cannot be separated from generic interferon tone, and nothing links STAT4 to TRIM72.

## References

- Thierfelder et al., 1996, Nature — Stat4-deficient mice fail to mount IL-12-mediated responses in NK and T cells.
- Kaplan et al., 1996, Nature — an independent Stat4 knockout showing impaired IL-12 responses and enhanced Th2 development.
- Remmers et al., 2007, New England Journal of Medicine — a STAT4 haplotype confers risk of rheumatoid arthritis and systemic lupus erythematosus.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.01545 |
| As a percentage | +1.08% |
| FDR, exposure-shuffle null | 0.1193 |
| In TP53-wild-type lines / altered lines | 0.00213 / 0.02286 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.203 raw, 0.048 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

### As a transcription factor, against MG53

| | |
|---|---|
| Regulon size used | 14 targets |
| Activity vs MG53 across exposures (r) | 0.284 (q 4.32e-18) |
| With 3 principal components removed | 0.219 (q 1.65e-11) |
| Within line, across exposures (r) | 0.024 (q 0.033) |
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
