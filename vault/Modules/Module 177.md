---
module: 177
type: "module"
n_genes: 22
n_plus: 22
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 177

*22 genes (single-armed) · [[Module 177.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 176), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Dinaciclib (drug)]] 0.5 µM (+10.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+10.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (+9.5, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+7.2, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+6.5, ⚠ toxic; transcription drop; cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+4.5); [[Digitoxin (drug)]] 5 µM (+3.9, ⚠ toxic; transcription drop; cell-cycle shift); [[Ipatasertib (drug)]] 0.5 µM (+3.3); [[Homoharringtonine (drug)]] 0.5 µM (+3.2, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (+3.2, ⚠ cell-cycle shift); [[XRK3F2 (drug)]] 0.5 µM (+2.4); [[Docetaxel (Trihydrate) (drug)]] 0.5 µM (+2.4); [[Methylprednisolone succinate (drug)]] 0.5 µM (+2.2); [[BAY1125976 (drug)]] 0.5 µM (+1.9); [[Verteporfin (drug)]] 5 µM (+1.9); [[Verteporfin (drug)]] 0.5 µM (+1.8); [[Bendamustine (drug)]] 5 µM (+1.8); [[Glycyrrhizic acid (drug)]] 0.05 µM (+1.8) (92 in all, 33 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Rutin (trihydrate) (drug)]] 0.05 µM (-2.4); [[Lucanthone (drug)]] 0.05 µM (-2.4); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (-2.3); [[Topotecan (hydrochloride) (drug)]] 0.5 µM (-2.2, ⚠ cell-cycle shift); [[Adagrasib (drug)]] 0.05 µM (-2.2, ⚠ position not correctable); [[Artesunate (drug)]] 0.5 µM (-2.1); [[Fenofibrate (drug)]] 0.05 µM (-2.1); [[Erlotinib (drug)]] 0.05 µM (-2.0); [[Anethole trithione (drug)]] 0.5 µM (-2.0); [[Encorafenib (drug)]] 5 µM (-1.9); [[Mebendazole (drug)]] 5 µM (-1.9); [[MK-8353 (drug)]] 0.5 µM (-1.8) (66 in all, 9 with an alert ⚠; shown: the 10 strongest and the 2 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[LOX-IMVI (line)]], [[NCI-H460 (line)]], [[SNU-1 (line)]], [[C32 (line)]], [[C-33 A (line)]], [[A-172 (line)]], [[AN3 CA (line)]], [[CHP-212 (line)]]

## + arm (22)

| Gene | Projection | Name |
|---|---|---|
| [[FAM230C]] | 0.813 | family with sequence similarity 230 member C |
| [[LINC02335]] | 0.803 | long independently transcribed non-coding RNA 2335 |
| [[TPTE]] | 0.794 | transmembrane phosphatase with tensin homology |
| [[ANKRD20A8P]] | 0.785 | ankyrin repeat domain 20 family member A8, pseudogene |
| [[UTY]] | 0.771 | ubiquitously transcribed tetratricopeptide repeat containing, Y-linked |
| [[LINC02506]] | 0.763 | long independently transcribed non-coding RNA 2506 |
| [[CCDC144NL-AS1]] | 0.759 | CCDC144NL antisense RNA 1 |
| [[LINC02476]] | 0.724 | long independently transcribed non-coding RNA 2476 |
| [[LINC01518]] | 0.701 | long independently transcribed non-coding RNA 1518 |
| [[FAM95A]] | 0.695 | family with sequence similarity 95 member A |
| [[BAGE2]] | 0.688 | BAGE family member 2 (pseudogene) |
| [[LINC00470]] | 0.681 | long independently transcribed non-coding RNA 470 |
| [[KDM5D]] | 0.671 | lysine demethylase 5D |
| [[FBXL7]] | 0.591 | F-box and leucine rich repeat protein 7 |
| [[USP9Y]] | 0.582 | ubiquitin specific peptidase 9 Y-linked |
| [[AACSP1]] | 0.570 | acetoacetyl-CoA synthetase pseudogene 1 |
| [[PHF2P2]] | 0.569 | PHD finger protein 2 pseudogene 2 |
| [[CCDC144A]] | 0.553 | coiled-coil domain containing 144A |
| [[RNF17]] | 0.533 | ring finger protein 17 |
| [[ANKRD20A9P]] | 0.467 | ankyrin repeat domain 20 family member A9, pseudogene |
| [[FAR2P1]] | 0.464 | fatty acyl-CoA reductase 2 pseudogene 1 |
| [[LINC00408]] | 0.412 | long independently transcribed non-coding RNA 408 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 177; `graph/modules.parquet` — module == 177; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [176] (drug-dose × line)
