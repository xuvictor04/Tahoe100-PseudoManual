---
module: 95
type: "module"
n_genes: 48
n_plus: 40
n_minus: 8
arms_opposite: true
mean_cos_between_arms: -0.3626810610294342
label: "Chromatin organization"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 095

*Chromatin organization · 48 genes (40 in the + arm, 8 in the − arm) · [[Module 095.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.36). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

Label from the validation stage: **Chromatin organization** (reactome, q 0.006; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| + | Chromatin organization | reactome | 7/40 | 8.82 | 0.006 |
| + | Activation of HOX genes during differentiation | reactome | 4/40 | 24.7 | 0.009 |
| + | Activation of anterior HOX genes in hindbrain development during early embryogenesis | reactome | 4/40 | 24.7 | 0.009 |
| - | Processing of SMDT1 | reactome | 2/8 | 236 | 0.013 |
| all | Chromatin organization | reactome | 7/48 | 7.35 | 0.017 |
| all | Activation of HOX genes during differentiation | reactome | 4/48 | 20.6 | 0.017 |
| all | Activation of anterior HOX genes in hindbrain development during early embryogenesis | reactome | 4/48 | 20.6 | 0.017 |
| - | Mitochondrial calcium ion transport | reactome | 2/8 | 171 | 0.022 |

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 94), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Homoharringtonine (drug)]] 5 µM (+28.3, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (+20.9, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+19.3, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+14.6, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (+13.3, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (+12.9, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (+11.9, ⚠ toxic; transcription drop; cell-cycle shift); [[TAK-901 (drug)]] 5 µM (+10.8, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (+8.6, ⚠ cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+8.1); [[Homoharringtonine (drug)]] 0.05 µM (+7.6); [[PH-797804 (drug)]] 5 µM (+5.7); [[Harringtonine (drug)]] 0.05 µM (+3.9); [[GSK1059615 (drug)]] 0.5 µM (+2.7); [[Filgotinib (drug)]] 5 µM (+2.7); [[XRK3F2 (drug)]] 0.5 µM (+2.6); [[Auranofin (drug)]] 5 µM (+2.5); [[Bimiralisib (drug)]] 0.5 µM (+2.5); [[Sulfatinib (drug)]] 5 µM (+2.2) (104 in all, 33 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)
- Lower it: [[Panobinostat (drug)]] 5 µM (-29.3, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (-27.7, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (-25.3, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (-19.4, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (-14.8); [[Belinostat (drug)]] 0.5 µM (-12.7, ⚠ cell-cycle shift); [[Brivudine (drug)]] 5 µM (-11.5); [[Tucidinostat (drug)]] 0.5 µM (-9.0, ⚠ cell-cycle shift); [[Bortezomib (drug)]] 0.05 µM (-5.5, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 5 µM (-5.2, ⚠ cell-cycle shift); [[HI-TOPK-032 (drug)]] 5 µM (-3.6); [[Ixazomib citrate (drug)]] 0.5 µM (-3.1); [[Brivudine (drug)]] 0.5 µM (-2.9); [[Belinostat (drug)]] 0.05 µM (-2.8); [[Bortezomib (drug)]] 0.5 µM (-2.3); [[Vinblastine (sulfate) (drug)]] 5 µM (-2.1); [[Verteporfin (drug)]] 5 µM (-2.1); [[Irinotecan (drug)]] 0.5 µM (-1.9) (96 in all, 21 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[PANC-1 (line)]], [[NCI-H460 (line)]], [[SW480 (line)]], [[HEC-1-A (line)]], [[LoVo (line)]], [[NCI-H1573 (line)]], [[LOX-IMVI (line)]], [[A549 (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 15 candidates, none with an alert.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[ZFX]] | Chromatin organization | +0.63 |
| 2 | [[INO80D]] | Chromatin organization | +0.63 |
| 3 | [[AP5S1]] | Activation of HOX genes during differentiation | +0.61 |
| 4 | [[UNK]] | Activation of HOX genes during differentiation | +0.60 |
| 5 | [[RFX1]] | Activation of HOX genes during differentiation | +0.60 |
| 6 | [[ZBED5]] | Activation of HOX genes during differentiation | +0.60 |
| 7 | [[LINC02307]] | Activation of HOX genes during differentiation | +0.57 |
| 8 | [[SON]] | Activation of HOX genes during differentiation | +0.56 |
| 9 | [[KDM3B]] | Activation of HOX genes during differentiation | +0.55 |
| 10 | [[DDX6]] | Chromatin organization | +0.55 |
| 11 | [[TET2]] | Chromatin organization | +0.55 |
| 12 | [[ZNF827]] | Activation of HOX genes during differentiation | +0.54 |
| 13 | [[GGPS1]] | Activation of HOX genes during differentiation | +0.53 |
| 14 | [[CCDC125]] | Activation of HOX genes during differentiation | +0.51 |
| 15 | [[LINC00869-1]] | Chromatin organization | +0.51 |

## + arm (40)

| Gene | Projection | Name |
|---|---|---|
| [[INO80D]] | 0.903 | INO80 complex subunit D |
| [[CREBBP]] | 0.851 | CREB binding lysine acetyltransferase |
| [[EP300]] | 0.821 | EP300 lysine acetyltransferase |
| [[ZFX]] | 0.818 | zinc finger protein X-linked |
| [[ZBED5]] | 0.812 | zinc finger BED-type containing 5 |
| [[AP5S1]] | 0.787 | adaptor related protein complex 5 subunit sigma 1 |
| [[UNK]] | 0.782 | unk zinc finger |
| [[LINC00869-1]] | 0.776 | — |
| [[GGPS1]] | 0.771 | geranylgeranyl diphosphate synthase 1 |
| [[LINC02307]] | 0.750 | long independently transcribed non-coding RNA 2307 |
| [[KDM3B]] | 0.749 | lysine demethylase 3B |
| [[ZNF827]] | 0.747 | zinc finger protein 827 |
| [[DDX6]] | 0.744 | DEAD-box helicase 6 |
| [[ZBTB1]] | 0.738 | zinc finger and BTB domain containing 1 |
| [[LINC01138]] | 0.735 | long independently transcribed non-coding RNA 1138 |
| [[ZBTB2]] | 0.727 | zinc finger and BTB domain containing 2 |
| [[SON]] | 0.718 | SON DNA and RNA binding protein |
| [[LINC00623]] | 0.695 | long independently transcribed non-coding RNA 623 |
| [[ATXN7]] | 0.691 | ataxin 7 |
| [[IGF2BP1]] | 0.680 | insulin like growth factor 2 mRNA binding protein 1 |
| [[RNF115]] | 0.679 | ring finger protein 115 |
| [[LINC01145-1]] | 0.678 | — |
| [[TET2]] | 0.646 | tet methylcytosine dioxygenase 2 |
| [[ZNF532]] | 0.623 | zinc finger protein 532 |
| [[SOCS6]] | 0.619 | suppressor of cytokine signaling 6 |
| [[RFX1]] | 0.615 | regulatory factor X1 |
| [[CCDC125]] | 0.614 | coiled-coil domain containing 125 |
| [[HOXB2]] | 0.586 | homeobox B2 |
| [[ZNF335]] | 0.575 | zinc finger protein 335 |
| [[ZEB1-AS1]] | 0.574 | ZEB1 antisense RNA 1 |
| [[RAB34]] | 0.573 | RAB34, member RAS oncogene family |
| [[EMP3]] | 0.551 | epithelial membrane protein 3 (MAM blood group) |
| [[DDX17]] | 0.537 | DEAD-box helicase 17 |
| [[MEX3C]] | 0.521 | mex-3 RNA binding family member C |
| [[KAT6B]] | 0.483 | lysine acetyltransferase 6B |
| [[LINC01836]] | 0.473 | long independently transcribed non-coding RNA 1836 |
| [[TK2]] | 0.449 | thymidine kinase 2 |
| [[TGIF1]] | 0.434 | TGFB induced factor homeobox 1 |
| [[RAB11B-AS1]] | 0.408 | RAB11B antisense RNA 1 |
| [[B9D2]] | 0.405 | B9 domain containing 2 |

## − arm (8)

| Gene | Projection | Name |
|---|---|---|
| [[WASF3]] | -0.818 | WASP family member 3 |
| [[SH3PXD2B]] | -0.720 | SH3 and PX domains 2B |
| [[PIP4K2A]] | -0.690 | phosphatidylinositol-5-phosphate 4-kinase type 2 alpha |
| [[C1orf21]] | -0.606 | chromosome 1 open reading frame 21 |
| [[MCUB]] | -0.515 | mitochondrial calcium uniporter dominant negative subunit beta |
| [[OSBPL6]] | -0.492 | oxysterol binding protein like 6 |
| [[MCU]] | -0.456 | mitochondrial calcium uniporter |
| [[EML6]] | -0.442 | EMAP like 6 |

## Data

- `graph/nodes.parquet` — module == 95; `graph/modules.parquet` — module == 95; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [94] (drug-dose × line)
