---
symbol: ELK4
type: gene
tier: 2
tags: [gene, transcription-factor]
generated_by: knowledge/_build/build_vault.py
---

# ELK4

> [!summary] In one line
> ELK4 (SAP-1) is a ternary complex factor: an ETS-domain protein that docks onto DNA-bound SRF to carry growth-factor signals to serum response elements.

## What it is

ELK4 is one of three ternary complex factors, with ELK1 and ELK3, and was isolated as a protein recruited by serum response factor to the c-fos SRE; it cannot occupy its site unless SRF is bound: its B-box contacts the SRF dimer while its ETS domain contacts a GGA(A/T) motif beside the CArG box. ERK phosphorylation of C-terminal sites converts it into an activator, carrying mitogen signalling to immediate-early genes such as FOS and EGR1. The TCFs compete with the myocardin/MRTF family for the same surface on [[SRF]], switching it between mitogenic and cytoskeletal programmes. A recurrent SLC45A3-ELK4 chimeric transcript occurs in prostate cancer.

## Why it appears in this work

ELK4 ranks at the top of the regulon-based activity step, and is entangled with [[SRF]], a candidate native-tissue regulator of [[MG53 (TRIM72)]] in this vault. They share CArG-box targets by construction, so a ranking placing both high reports one body of overlapping evidence. See [[Transcription factor activity inference]].

## What is uncertain

ELK4's regulon here is among the smallest of any factor scored, making its activity close to an average over a handful of immediate-early transcripts — and those move under nearly any perturbation, so a high rank across this compound panel may report generic stress. The score is not separable from ELK1 or SRF. Nothing links ELK4 to TRIM72: the one characterised element there is a MEF2 site beside an E-box, with no CArG or Ets element described.

## References

- Dalton & Treisman, 1992, Cell — characterised SAP-1 as a protein recruited by serum response factor to the c-fos serum response element.
- Mo et al., 2001, Journal of Molecular Biology — crystal structure of a ternary SAP-1/SRF/c-fos SRE DNA complex.
- Rickman et al., 2009, Cancer Research — identified SLC45A3-ELK4 as a recurrent chimeric transcript in prostate cancer.
- Jung & Ko, 2010, Biochemical and Biophysical Research Communications — TRIM72 is transcriptionally activated by the synergism of MyoD (or myogenin) with MEF2.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00229 |
| As a percentage | +0.16% |
| FDR, exposure-shuffle null | 0.2251 |
| In TP53-wild-type lines / altered lines | 0.00303 / 0.00184 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.018 raw, 0.156 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

### As a transcription factor, against MG53

| | |
|---|---|
| Regulon size used | 6 targets |
| Activity vs MG53 across exposures (r) | 0.346 (q 2.63e-22) |
| With 3 principal components removed | 0.461 (q 3.71e-38) |
| Within line, across exposures (r) | 0.046 (q 0.193) |
| Percentile against all genes | 99.1 |

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
