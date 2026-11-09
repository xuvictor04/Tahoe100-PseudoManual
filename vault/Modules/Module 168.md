---
module: 168
type: "module"
n_genes: 25
n_plus: 20
n_minus: 5
arms_opposite: true
mean_cos_between_arms: -0.40483489632606506
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 168

*25 genes (20 in the + arm, 5 in the − arm) · [[Module 168.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 167), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Panobinostat (drug)]] 5 µM (+17.8, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (+17.1, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (+15.6, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+11.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+8.7, ⚠ toxic; transcription drop; cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 5 µM (+8.7, ⚠ toxic; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+8.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Belinostat (drug)]] 0.5 µM (+7.0, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+6.8, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (+6.1, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (+3.8); [[Brivudine (drug)]] 5 µM (+3.5); [[Radotinib (drug)]] 5 µM (+3.4); [[PH-797804 (drug)]] 5 µM (+2.8); [[Belinostat (drug)]] 0.05 µM (+2.3); [[Cabozantinib (S-malate) (drug)]] 5 µM (+2.3); [[Flumatinib (mesylate) (drug)]] 5 µM (+2.2); [[Ponatinib (drug)]] 5 µM (+2.2); [[Pasireotide (acetate) (drug)]] 5 µM (+2.0); [[Ipatasertib (drug)]] 0.5 µM (+2.0) (98 in all, 23 with an alert ⚠; shown: the 10 strongest and the 10 next strongest without an alert)
- Lower it: [[Homoharringtonine (drug)]] 5 µM (-28.0, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-19.4, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-12.1, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-10.9, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (-9.8, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (-7.2, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (-5.9, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (-5.6, ⚠ toxic; transcription drop; cell-cycle shift); [[Homoharringtonine (drug)]] 0.05 µM (-4.7); [[Ixazomib citrate (drug)]] 5 µM (-4.3, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 0.5 µM (-4.1); [[(S)-Crizotinib (drug)]] 0.5 µM (-3.3); [[5-Azacytidine (drug)]] 5 µM (-2.7); [[Esmolol (hydrochloride) (drug)]] 5 µM (-2.7); [[Afatinib (drug)]] 0.5 µM (-2.6); [[Busulfan (drug)]] 0.05 µM (-2.6); [[Diphenhydramine (drug)]] 0.5 µM (-2.6); [[Brimonidine (drug)]] 5 µM (-2.4); [[L-Eflornithine (monohydrochloride) (drug)]] 5 µM (-2.4) (126 in all, 25 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SW480 (line)]], [[PANC-1 (line)]], [[NCI-H460 (line)]], [[HOP62 (line)]], [[A549 (line)]], [[NCI-H2347 (line)]], [[HEC-1-A (line)]], [[AsPC-1 (line)]]

## + arm (20)

| Gene | Projection | Name |
|---|---|---|
| [[PMS2P3-1]] | 0.912 | — |
| [[SDHAP4]] | 0.902 | SDHA pseudogene 4 |
| [[RNF4]] | 0.865 | ring finger protein 4 |
| [[PMS2P3]] | 0.839 | PMS1 homolog 2, mismatch repair system component pseudogene 3 |
| [[SEC11A]] | 0.800 | SEC11 homolog A, signal peptidase complex subunit |
| [[MED17]] | 0.769 | mediator complex subunit 17 |
| [[CDS2]] | 0.760 | CDP-diacylglycerol synthase 2 |
| [[TSFM]] | 0.742 | Ts translation elongation factor, mitochondrial |
| [[FOXJ3]] | 0.738 | forkhead box J3 |
| [[SNHG30]] | 0.723 | small nucleolar RNA host gene 30 |
| [[SDHA]] | 0.658 | succinate dehydrogenase complex flavoprotein subunit A |
| [[MTRR]] | 0.657 | 5-methyltetrahydrofolate-homocysteine methyltransferase reductase |
| [[FBXO31]] | 0.649 | F-box protein 31 |
| [[NSUN5P1]] | 0.639 | NSUN5 pseudogene 1 |
| [[ARPC1A]] | 0.638 | actin related protein 2/3 complex subunit 1A |
| [[METTL9]] | 0.628 | methyltransferase 9, His-X-His N1(pi)-histidine |
| [[RPIA]] | 0.619 | ribose 5-phosphate isomerase A |
| [[ZNF141]] | 0.567 | zinc finger protein 141 |
| [[CAPN1-AS1]] | 0.553 | CAPN1 antisense RNA 1 |
| [[PMS2P1]] | 0.510 | PMS1 homolog 2, mismatch repair system component pseudogene 1 |

## − arm (5)

| Gene | Projection | Name |
|---|---|---|
| [[CUX1]] | -0.724 | cut like homeobox 1 |
| [[ZC3H11A]] | -0.698 | zinc finger CCCH-type containing 11A |
| [[MED1]] | -0.653 | mediator complex subunit 1 |
| [[JMJD1C]] | -0.597 | jumonji domain containing 1C |
| [[SPATS2]] | -0.350 | spermatogenesis associated serine rich 2 |

## Data

- `graph/nodes.parquet` — module == 168; `graph/modules.parquet` — module == 168; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [167] (drug-dose × line)
