---
type: index
tags: [index, concepts]
status: current
---

# Concepts — Map of Content

The ideas this work rests on, each explained once. If a finding note uses a term without defining it, the
definition is here.

## The biology

| Note | What it covers |
|---|---|
| [[MG53 (TRIM72)]] | what the protein does — membrane repair, insulin signalling, myogenesis — and why mRNA in cancer lines is a poor window onto any of it |
| [[The p53 pathway]] | activation, the four output arms, the MDM2 feedback loop, and how p53 is broken in these lines |
| [[p53 program P]] | the 195-gene signature derived from this dataset to stand in for p53 output |
| [[The p21-DREAM axis]] | why p53's repression arm is indirect, smaller, and the easiest thing to misread |
| [[p53 nullification in cancer cell lines]] | why a cancer panel is mostly p53-dead, and what that does to sample size |

## The locus, and the artefact it creates

| Note | What it covers |
|---|---|
| [[The TRIM72 locus]] | the geometry: TRIM72 sits 17 kb 3′ of FUS, same strand, at 1/47th its level |
| [[Readthrough spillover]] | transcription running past one gene into the next and being counted as the next — the leading account of MG53's apparent induction |

## The measurement

| Note | What it covers |
|---|---|
| [[Tahoe-100M]] | the dataset: 50 pooled lines × 379 drugs × 3 doses, 24 h, and every limit that follows |
| [[Why MG53 is hard to measure here]] | 5.89 CPM, 12.4% zeros, reliability 0.289–0.705, and two thirds of the variance being counting noise |
| [[Plate batch effects]] | MG53's 3.124 log2 plate gap, rank 1 of 16,656 genes, and the correlation it manufactures |
| [[Reliability and disattenuation]] | converting "per doubling of measured MG53" into "per doubling of true MG53", and why it is a range |

## The statistics

| Note | What it covers |
|---|---|
| [[Two-way fixed effects]] | removing both line and drug-dose means; what survives, and the cost in few-cluster standard errors |
| [[FDR calibration and the inflated null]] | the screen's analytic statistic is ~4.4× too large, 4,500 genes "pass", and what to use instead |
| [[Placebo genes and reference families]] | a correlation means nothing without a reference family, and one of this study's families was a discovery set |
| [[Cross-fitting and circularity]] | which columns were selected using the TP53 labels, and therefore which claims they cannot support |
| [[Signing genes by p53 direction]] | why an unsigned per-gene tally adds the two programme arms against each other |
| [[Transcription factor activity inference]] | inferring factor activity from regulons, and the negative result it produced here |

## How to read this vault

- [[How this vault is built]] — the generated layer, the written layer, and which one to edit
- [[How the numbers are decided]] — the provenance tiers, and which to trust for what
- [[Corrections and retractions]] — what was published wrong and what replaced it

## The shortest path through

For someone with an hour: [[What this study found]] → [[MG53 (TRIM72)]] → [[The TRIM72 locus]] →
[[Why MG53 is hard to measure here]] → [[The measurement with controls]] → [[Corrections and retractions]].
