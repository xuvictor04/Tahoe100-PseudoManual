---
symbol: SMAD4
type: gene
tier: 2
tags: [gene, transcription-factor]
generated_by: knowledge/_build/build_vault.py
---

# SMAD4

> [!summary] In one line
> SMAD4 is the shared partner SMAD through which both TGF-beta and BMP signals reach the nucleus, and one of the most frequently deleted tumour suppressors in gastrointestinal cancer.

## What it is

Receptor-activated SMADs — SMAD2/3 for TGF-beta, SMAD1/5/8 for BMP — are phosphorylated at their C-termini, bind SMAD4 through MH2 contacts and accumulate in the nucleus as a complex whose weak MH1 DNA binding is given specificity by partners such as FOX and RUNX proteins. Because it is common to both branches, losing SMAD4 removes both. Biallelic inactivation occurs in roughly half of pancreatic ductal adenocarcinomas, where the gene was identified as DPC4, and is common in colorectal cancer; germline loss-of-function causes juvenile polyposis, while mutation at a single MH2 codon causes the gain-of-function Myhre syndrome. TGF-beta's cytostatic arm converges on CDKN1A induction and MYC repression, where it meets p53 biology.

## Why it appears in this work

SMAD4 carries one of the larger curated regulons scored here and sits among the positively correlated factors. TGF-beta output, EMT and stress transcription move under much of this compound panel, so a hub that broad is the kind of factor whose apparent activity means little without the matched-gene reference. See [[Transcription factor activity inference]].

## What is uncertain

A substantial minority of lines in a pooled cancer panel are SMAD4-deleted, so inferred "SMAD4 activity" is partly a readout of genotype heterogeneity rather than signalling. Its regulon overlaps SMAD2/3 and AP-1 sets by construction and cannot separate them. No SMAD element has been reported at [[The TRIM72 locus]], so a correlation here predicts nothing.

## References

- Hahn et al., 1996, Science — identified DPC4/SMAD4 as a candidate tumour suppressor homozygously deleted in pancreatic cancer.
- Howe et al., 1998, Science — germline SMAD4 mutations cause juvenile polyposis.
- Le Goff et al., 2011, Nature Genetics — mutations at a single codon in the MH2 domain cause Myhre syndrome.
- Massague, 2008, Cell — review of TGF-beta signalling in cancer, including the cytostatic programme.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00706 |
| As a percentage | -0.49% |
| FDR, exposure-shuffle null | 0.0003 |
| In TP53-wild-type lines / altered lines | -0.00683 / -0.00720 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | -0.441 raw, -0.109 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

### As a transcription factor, against MG53

| | |
|---|---|
| Regulon size used | 106 targets |
| Activity vs MG53 across exposures (r) | 0.293 (q 3.72e-18) |
| With 3 principal components removed | 0.260 (q 2.42e-14) |
| Within line, across exposures (r) | 9.65e-04 (q 0.967) |
| Percentile against all genes | 95.3 |

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
