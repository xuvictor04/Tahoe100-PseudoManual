---
module: 160
type: "module"
n_genes: 27
n_plus: 22
n_minus: 5
arms_opposite: true
mean_cos_between_arms: -0.25503239035606384
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 160

*27 genes (22 in the + arm, 5 in the − arm) · [[Module 160.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 159), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Panobinostat (drug)]] 0.5 µM (+12.5, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (+12.5, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (+11.0, ⚠ cell-cycle shift); [[Belinostat (drug)]] 0.5 µM (+6.6, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (+6.5); [[Panobinostat (drug)]] 0.05 µM (+5.2, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+2.9, ⚠ cell-cycle shift); [[PF-06260933 (drug)]] 5 µM (+2.8); [[TAK-901 (drug)]] 5 µM (+2.7, ⚠ cell-cycle shift); [[Bergenin (drug)]] 0.5 µM (+2.6); [[Celecoxib (drug)]] 0.5 µM (+2.3); [[Pitavastatin (Calcium) (drug)]] 0.5 µM (+2.3); [[Ipatasertib (drug)]] 0.5 µM (+2.2); [[BAY1125976 (drug)]] 0.5 µM (+2.2); [[vincristine (drug)]] 5 µM (+2.0); [[PH-797804 (drug)]] 0.5 µM (+2.0); [[Estrone sulfate (potassium) (drug)]] 5 µM (+1.9) (92 in all, 15 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)
- Lower it: [[Selinexor (drug)]] 5 µM (-7.4, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (-7.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (-6.5, ⚠ toxic; transcription drop; cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-6.2, ⚠ cell-cycle shift); [[Ponatinib (drug)]] 5 µM (-5.7); [[Dinaciclib (drug)]] 0.05 µM (-5.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (-5.0, ⚠ cell-cycle shift); [[Selinexor (drug)]] 0.5 µM (-4.1, ⚠ cell-cycle shift); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (-4.1); [[Homoharringtonine (drug)]] 0.05 µM (-3.9); [[Cobimetinib (drug)]] 5 µM (-3.7); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM (-3.5); [[Radotinib (drug)]] 5 µM (-3.3); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (-3.1); [[Binimetinib (drug)]] 0.5 µM (-2.8); [[Cabozantinib (S-malate) (drug)]] 5 µM (-2.6); [[Belumosudil (drug)]] 5 µM (-2.5) (124 in all, 27 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SW480 (line)]], [[A-172 (line)]], [[MIA PaCa-2 (line)]], [[KATO III (line)]], [[NCI-H23 (line)]], [[NCI-H460 (line)]], [[LOX-IMVI (line)]], [[SNU-423 (line)]]

## + arm (22)

| Gene | Projection | Name |
|---|---|---|
| [[NECTIN2]] | 0.785 | nectin cell adhesion molecule 2 |
| [[LUZP1]] | 0.784 | leucine zipper protein 1 |
| [[MAPKAPK2]] | 0.783 | MAPK activated protein kinase 2 |
| [[FRMD8]] | 0.775 | FERM domain containing 8 |
| [[CYTH1]] | 0.749 | cytohesin 1 |
| [[SLC66A2]] | 0.741 | solute carrier family 66 member 2 |
| [[ARHGEF18]] | 0.735 | Rho/Rac guanine nucleotide exchange factor 18 |
| [[RCOR1]] | 0.735 | REST corepressor 1 |
| [[LRRC8A]] | 0.716 | leucine rich repeat containing 8 VRAC subunit A |
| [[GPR153]] | 0.684 | G protein-coupled receptor 153 |
| [[FBXO46]] | 0.661 | F-box protein 46 |
| [[SMURF1]] | 0.660 | SMAD specific E3 ubiquitin protein ligase 1 |
| [[GRIN2D]] | 0.636 | glutamate ionotropic receptor NMDA type subunit 2D |
| [[SLC25A25]] | 0.609 | solute carrier family 25 member 25 |
| [[ZBTB46]] | 0.590 | zinc finger and BTB domain containing 46 |
| [[TBC1D2]] | 0.585 | TBC1 domain family member 2 |
| [[NXN]] | 0.565 | nucleoredoxin |
| [[MAP3K9-DT]] | 0.497 | MAP3K9 divergent transcript |
| [[OSBP2]] | 0.466 | oxysterol binding protein 2 |
| [[MAGI1]] | 0.380 | membrane associated guanylate kinase, WW and PDZ domain containing 1 |
| [[CAB39]] | 0.374 | calcium binding protein 39 |
| [[PACS1]] | 0.301 | phosphofurin acidic cluster sorting protein 1 |

## − arm (5)

| Gene | Projection | Name |
|---|---|---|
| [[NT5DC1]] | -0.632 | 5'-nucleotidase domain containing 1 |
| [[MTARC2]] | -0.612 | mitochondrial amidoxime reducing component 2 |
| [[WBP11]] | -0.438 | WW domain binding protein 11 |
| [[RNF14]] | -0.321 | ring finger protein 14 |
| [[MID2]] | -0.202 | midline 2 |

## Data

- `graph/nodes.parquet` — module == 160; `graph/modules.parquet` — module == 160; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [159] (drug-dose × line)
