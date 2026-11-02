---
symbol: ATF5
type: gene
tier: 2
tags: [gene, transcription-factor]
generated_by: knowledge/_build/build_vault.py
---

# ATF5

> [!summary] In one line
> ATF5 is a bZIP factor translated under the same eIF2-dependent control as [[ATF4]], best established as a brake on neural progenitor differentiation and as the mammalian mediator of a mitochondrial unfolded-protein response.

## What it is

Like [[ATF4]], ATF5 carries inhibitory upstream open reading frames and is translated preferentially when eIF2 is phosphorylated. Two functional accounts are reasonably supported. In the nervous system it keeps neural progenitors proliferating, must be downregulated for them to become neurons, and is needed for olfactory sensory neuron development. Separately, ATF5 can substitute for the worm factor ATFS-1 in mounting a mitochondrial unfolded-protein response — the leading mammalian candidate for that pathway. It is reported as pro-survival in glioma, on evidence from few laboratories. Overall ATF5 is substantially less characterised than its paralogue.

## Why it appears in this work

ATF5 came out of the activity-inference step as one of the highest-ranked candidate regulators upstream of [[MG53 (TRIM72)]]. Its interest is the same as [[ATF4]]'s: it reports stress-response tone across the compound panel, which is the chief non-p53 explanation for coordinated drug-responsive transcription here. Nothing connects it to the TRIM72 promoter.

## What is uncertain

ATF5 and [[ATF4]] share translational control, dimerisation partners and a broadly similar consensus, so their inferred activities are expected to be collinear, and a signal credited to ATF5 may belong to the family. Its regulon here is small, which makes the inferred score noisier than the percentile suggests. The mitochondrial-UPR role rests largely on cross-species complementation, and accounts of how ATF5 is held inactive — sequestration in mitochondria versus translational silence — are not reconciled.

## References

- Angelastro et al., 2003, Journal of Neuroscience — regulated ATF5 expression is required for neural progenitors to progress to neurons.
- Zhou et al., 2008, Journal of Biological Chemistry — eIF2 phosphorylation directs ATF5 translational control through its upstream open reading frames.
- Fiorese et al., 2016, Current Biology — ATF5 mediates a mammalian mitochondrial unfolded-protein response, rescuing atfs-1 loss in C. elegans.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00230 |
| As a percentage | +0.16% |
| FDR, exposure-shuffle null | 0.5765 |
| In TP53-wild-type lines / altered lines | 0.00411 / 0.00120 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.427 raw, 0.175 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

### As a transcription factor, against MG53

| | |
|---|---|
| Regulon size used | 25 targets |
| Activity vs MG53 across exposures (r) | 0.359 (q 3.27e-26) |
| With 3 principal components removed | 0.373 (q 1.03e-28) |
| Within line, across exposures (r) | -0.007 (q 0.831) |
| Percentile against all genes | 99.9 |

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
