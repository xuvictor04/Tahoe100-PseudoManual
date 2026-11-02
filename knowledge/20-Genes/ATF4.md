---
symbol: ATF4
type: gene
tier: 2
tags: [gene, transcription-factor]
generated_by: knowledge/_build/build_vault.py
---

# ATF4

> [!summary] In one line
> ATF4 is the bZIP transcription factor at the output end of the integrated stress response, translated preferentially when eIF2α is phosphorylated.

## What it is

Four kinases — PERK, GCN2, HRI and PKR — respond to ER stress, amino acid scarcity, haem or mitochondrial defects and oxidative stress by phosphorylating eIF2α. That lowers general initiation but raises translation of ATF4 specifically, through upstream open reading frames in its 5′ leader that ribosomes bypass only under stress. ATF4 then dimerises with other bZIPs at CARE/CRE-like elements and turns on amino acid transporters, aminoacyl-tRNA synthetases, one-carbon and serine synthesis genes, [[ATF3]], CHOP and [[GDF15]]. The programme is adaptive at first and lethal if the stress persists.

## Why it appears in this work

ATF4 was scored as a high-ranking candidate regulator upstream of [[MG53 (TRIM72)]]. Its more useful role here is as the main alternative explanation for drug-responsive transcription: across a panel this size many exposures provoke proteotoxic, nutrient or mitochondrial stress, and the ATF4 programme overlaps p53's at several genes, [[GDF15]] among them. Anything that looks like p53 output deserves a check against this axis.

## What is uncertain

ATF4's regulation is translational, so its own mRNA level is a poor proxy for its activity — the transcript and inferred-activity rows below measure different things. Which genes are ATF4's direct targets rather than CHOP's or ATF3's is not cleanly resolved, and the adaptive-versus-lethal split depends on stress duration in ways a single timepoint cannot separate. Where ATF4 and p53 share a target, attribution from expression alone is not possible.

## References

- Harding et al., 2000, Molecular Cell — regulated translation initiation controls stress-induced gene expression through ATF4.
- Vattem and Wek, 2004, PNAS — upstream open reading frames direct ATF4 translational control.
- Harding et al., 2003, Molecular Cell — defined the integrated stress response governing amino acid metabolism and oxidative stress resistance.
- Han et al., 2013, Nature Cell Biology — ATF4 and CHOP drive protein synthesis and ATP depletion toward cell death.
- Pakos-Zebrucka et al., 2016, EMBO Reports — review of the integrated stress response.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00220 |
| As a percentage | +0.15% |
| FDR, exposure-shuffle null | 0.2376 |
| In TP53-wild-type lines / altered lines | 0.00296 / 0.00173 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.274 raw, -0.011 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

### As a transcription factor, against MG53

| | |
|---|---|
| Regulon size used | 104 targets |
| Activity vs MG53 across exposures (r) | 0.357 (q 8.62e-26) |
| With 3 principal components removed | 0.409 (q 5.61e-34) |
| Within line, across exposures (r) | -0.008 (q 0.776) |
| Percentile against all genes | 99.4 |

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
