---
symbol: TGIF1
type: gene
tier: 2
tags: [gene, transcription-factor]
generated_by: knowledge/_build/build_vault.py
---

# TGIF1

> [!summary] In one line
> TGIF1 is a TALE-class homeodomain repressor that caps the output of TGF-beta and Nodal signalling by binding activated Smad2 and recruiting corepressors.

## What it is

TGIF1 is a TALE-class homeodomain protein, kin to PBX and MEIS, and acts almost entirely as a repressor. It was first described blocking RXR-dependent transcription at a retinoid-responsive element, but its characterised role is in TGF-beta signalling: TGIF1 binds activated Smad2 in the nucleus and turns the Smad complex into a repressor by recruiting mSin3/HDAC and CtBP. Because TGIF1 is itself TGF-beta-inducible, it is a feedback node rather than a constitutive brake. Heterozygous mutations and 18p deletions cause holoprosencephaly, and the disease alleles hit the DNA-binding surface, the repression domain, or the Smad2-interaction region — much of the evidence that the Smad role is the physiologically important one.

## Why it appears in this work

TGIF1 is here only as a scored regulator in the transcription-factor step: not a curated p53 effector, and its locus unrelated to [[The TRIM72 locus]]. A rank would mean TGF-beta pathway tone moves with measured [[MG53 (TRIM72)]] across this compound panel, which nothing in this design tests. See [[Transcription factor activity inference]].

## What is uncertain

The regulon used for TGIF1 is among the smallest scored here, so its activity score is close to an average over a handful of transcripts. The deeper problem is directional: TGIF1 represses, while the activity convention reads coordinated target expression as factor activity, so the sign cannot be taken at face value. The regulon is also inseparable from Smad-driven transcription, since TGIF1 is TGF-beta-induced and acts on Smad targets — the score may report pathway tone rather than TGIF1 itself. No element in TRIM72's described regulation is a TGIF1 site.

## References

- Wotton et al., 1999, Cell — identified TGIF as a Smad2-binding transcriptional corepressor of TGF-beta signalling.
- Melhuish & Wotton, 2000, Journal of Biological Chemistry — showed TGIF recruits CtBP, and that a holoprosencephaly mutation disrupts that interaction.
- Gripp et al., 2000, Nature Genetics — heterozygous TGIF mutations cause holoprosencephaly, linking Nodal signalling to human neural axis determination.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00274 |
| As a percentage | -0.19% |
| FDR, exposure-shuffle null | 0.5616 |
| In TP53-wild-type lines / altered lines | 0.00339 / -0.00646 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | -0.268 raw, -0.009 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

### As a transcription factor, against MG53

| | |
|---|---|
| Regulon size used | 7 targets |
| Activity vs MG53 across exposures (r) | -0.252 (q 4.47e-13) |
| With 3 principal components removed | -0.174 (q 4.90e-07) |
| Within line, across exposures (r) | -0.029 (q 0.042) |
| Percentile against all genes | 8.2 |

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
