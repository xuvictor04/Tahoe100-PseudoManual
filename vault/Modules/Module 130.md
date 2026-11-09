---
module: 130
type: "module"
n_genes: 36
n_plus: 36
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 130

*36 genes (single-armed) · [[Module 130.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 129), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Homoharringtonine (drug)]] 5 µM (+7.8, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+5.6, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (+3.4, ⚠ cell-cycle shift); [[TAK-901 (drug)]] 5 µM (+3.1, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+2.8, ⚠ cell-cycle shift); [[Selinexor (drug)]] 5 µM (+2.0, ⚠ cell-cycle shift); [[Epirubicin (hydrochloride) (drug)]] 5 µM (+1.9, ⚠ cell-cycle shift); [[Ponatinib (drug)]] 5 µM (+1.9); [[PH-797804 (drug)]] 5 µM (+1.8); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (+1.7, ⚠ cell-cycle shift); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM (+1.5); [[Binimetinib (drug)]] 0.5 µM (+1.5); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (+1.5); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (+1.5); [[Trametinib (drug)]] 0.5 µM (+1.4); [[Binimetinib (drug)]] 5 µM (+1.2); [[Radotinib (drug)]] 5 µM (+1.2); [[Terfenadine (drug)]] 5 µM (+1.2) (27 in all, 14 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[c-Kit-IN-1 (drug)]] 0.05 µM (-5.3, ⚠ unreliable plate only); [[Panobinostat (drug)]] 5 µM (-4.2, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (-3.9, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (-3.3, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (-3.1); [[EX229 (drug)]] 5 µM (-2.6); [[c-Kit-IN-1 (drug)]] 5 µM (-2.5); [[Tucidinostat (drug)]] 5 µM (-2.5); [[TAK-733 (drug)]] 5 µM (-2.4); [[Abemaciclib (drug)]] 5 µM (-2.2); [[venetoclax (drug)]] 5 µM (-1.9); [[Sapanisertib (drug)]] 0.5 µM (-1.5); [[EX229 (drug)]] 0.5 µM (-1.5); [[Abemaciclib (drug)]] 0.5 µM (-1.5) (26 in all, 8 with an alert ⚠; shown: the 10 strongest and the 4 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SW480 (line)]], [[NCI-H460 (line)]], [[PANC-1 (line)]], [[KATO III (line)]], [[SW1417 (line)]], [[A549 (line)]], [[HEC-1-A (line)]], [[LS 180 (line)]]

## + arm (36)

| Gene | Projection | Name |
|---|---|---|
| [[CDKN1B]] | 0.824 | cyclin dependent kinase inhibitor 1B |
| [[TAPT1]] | 0.783 | transmembrane anterior posterior transformation 1 |
| [[FBXO8]] | 0.780 | F-box protein 8 |
| [[DNAJC27]] | 0.752 | DnaJ heat shock protein family (Hsp40) member C27 |
| [[CCDC115]] | 0.751 | vacuolar ATPase assembly factor VMA22 |
| [[ACBD5]] | 0.749 | acyl-CoA binding domain containing 5 |
| [[CHASERR]] | 0.723 | CHD2 adjacent suppressive regulatory RNA |
| [[FBXL3]] | 0.721 | F-box and leucine rich repeat protein 3 |
| [[ZNF451]] | 0.718 | zinc finger protein 451 |
| [[HOXC10]] | 0.696 | homeobox C10 |
| [[CEP57]] | 0.681 | centrosomal protein 57 |
| [[LNX2]] | 0.655 | ligand of numb-protein X 2 |
| [[CMC4]] | 0.651 | C-X9-C motif containing 4 |
| [[MAT2B]] | 0.650 | methionine adenosyltransferase 2 non-catalytic beta subunit |
| [[RBM33]] | 0.649 | RNA binding motif protein 33 |
| [[ATG2B]] | 0.633 | autophagy related 2B |
| [[FMR1]] | 0.616 | fragile X messenger ribonucleoprotein 1 |
| [[ZHX1]] | 0.612 | zinc fingers and homeoboxes 1 |
| [[WAC]] | 0.604 | WW domain containing adaptor with coiled-coil |
| [[FAM76B]] | 0.594 | family with sequence similarity 76 member B |
| [[GID8]] | 0.592 | GID complex subunit 8 homolog |
| [[UBR5]] | 0.581 | ubiquitin protein ligase E3 component n-recognin 5 |
| [[NABP2]] | 0.561 | nucleic acid binding protein 2 |
| [[SPACA9]] | 0.556 | sperm acrosome associated 9 |
| [[BROX]] | 0.546 | BRO1 domain and CAAX motif containing |
| [[MAF1]] | 0.529 | MAF1 negative regulator of RNA polymerase III |
| [[POLDIP3]] | 0.522 | DNA polymerase delta interacting protein 3 |
| [[TPRA1]] | 0.519 | transmembrane protein adipocyte associated 1 |
| [[LRRC27]] | 0.515 | leucine rich repeat containing 27 |
| [[DYRK1B]] | 0.510 | dual specificity tyrosine phosphorylation regulated kinase 1B |
| [[NSD3]] | 0.507 | nuclear receptor binding SET domain protein 3 |
| [[PLEKHA3]] | 0.491 | pleckstrin homology domain containing A3 |
| [[AIP]] | 0.458 | AHR interacting HSP90 co-chaperone |
| [[CREBL2]] | 0.424 | cAMP responsive element binding protein like 2 |
| [[SHISA4]] | 0.402 | shisa family member 4 |
| [[SMARCA2]] | 0.333 | SWI/SNF related BAF chromatin remodeling complex subunit ATPase 2 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 130; `graph/modules.parquet` — module == 130; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [129] (drug-dose × line)
