---
symbol: RB1
type: gene
tier: 2
tags: [gene, transcription-factor]
generated_by: knowledge/_build/build_vault.py
---

# RB1

> [!summary] In one line
> RB1 encodes the retinoblastoma protein, the pocket protein that holds E2F transcription factors inactive until CDK phosphorylation releases them and licenses S-phase entry.

## What it is

The first tumour suppressor cloned. Its pocket domain binds the E2F transactivation domain while a separate LxCxE surface recruits histone deacetylases and chromatin modifiers, so RB does not merely block E2F but actively represses its target promoters. RB is hypophosphorylated in G0 and early G1, then progressively phosphorylated by cyclin D–CDK4/6 and cyclin E–CDK2, releasing E2F. The [[CDKN2A]]–CDK4–RB–E2F axis is disabled in most cancers, by RB1 loss in retinoblastoma and small-cell lung cancer or by p16 deletion and cyclin D amplification — and intact RB is what CDK4/6 inhibitors require. p53 reaches RB indirectly, through [[CDKN1A]]: p21 inhibits the CDKs, RB stays hypophosphorylated, E2F targets stay off.

## Why it appears in this work

RB1 is scored in the regulon-based activity step and is among the strongest negative associations with measured [[MG53 (TRIM72)]]. The caveat is structural: RB1 is a corepressor, not a sequence-specific activator, so a regulon of "RB1 targets" is really a set of E2F-driven proliferation genes, and inferred RB1 activity is a proliferation readout with its sign flipped ([[Transcription factor activity inference]]).

## What is uncertain

Whether this is about RB1 at all. Its regulon overlaps the E2F and DREAM target set that dominates any arrest response, so an association of this shape would appear wherever some conditions slow the cycle, and it cannot be separated from p21 induction ([[The p21-DREAM axis]]). RB function is set by phosphorylation, not transcript level, so target-based inference and RB1 mRNA answer different questions. No link between RB1 and the TRIM72 promoter is reported, and TRIM72 is not a known E2F target.

## References

- Friend et al., 1986, Nature — identified the retinoblastoma susceptibility gene.
- Buchkovich, Duffy & Harlow, 1989, Cell — showed that the RB protein is phosphorylated in a cell-cycle-dependent manner.
- Litovchick et al., 2007, Molecular Cell — characterised the p130–E2F4 DREAM complex repressing cell-cycle-dependent genes in quiescence.
- Dyson, 2016, Genes & Development — review reassessing RB1 as prototype tumour suppressor and the gaps in the E2F-only account.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00298 |
| As a percentage | +0.21% |
| FDR, exposure-shuffle null | 0.0808 |
| In TP53-wild-type lines / altered lines | 0.00314 / 0.00288 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.266 raw, 0.325 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

### As a transcription factor, against MG53

| | |
|---|---|
| Regulon size used | 31 targets |
| Activity vs MG53 across exposures (r) | -0.268 (q 6.18e-14) |
| With 3 principal components removed | -0.266 (q 5.66e-14) |
| Within line, across exposures (r) | 0.014 (q 0.468) |
| Percentile against all genes | 0.5 |

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
