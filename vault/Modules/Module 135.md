---
module: 135
type: "module"
n_genes: 35
n_plus: 20
n_minus: 15
arms_opposite: true
mean_cos_between_arms: -0.38576391339302063
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 135

*35 genes (20 in the + arm, 15 in the − arm) · [[Module 135.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.39). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 134), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Homoharringtonine (drug)]] 5 µM (+22.3, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+16.7, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+14.3, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (+13.2); [[Harringtonine (drug)]] 5 µM (+12.9, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (+11.5, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 5 µM (+11.0, ⚠ cell-cycle shift); [[Bortezomib (drug)]] 0.05 µM (+10.1, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 0.5 µM (+9.9); [[Dinaciclib (drug)]] 5 µM (+8.8, ⚠ toxic; transcription drop; cell-cycle shift); [[Homoharringtonine (drug)]] 0.05 µM (+8.3); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+4.9); [[5-Azacytidine (drug)]] 5 µM (+4.4); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (+4.1); [[Harringtonine (drug)]] 0.05 µM (+3.6); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (+3.4); [[Trametinib (drug)]] 0.5 µM (+3.4); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM (+3.3) (101 in all, 37 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Panobinostat (drug)]] 5 µM (-15.9, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (-15.2, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (-14.8, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (-9.2, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (-6.9); [[Belinostat (drug)]] 0.5 µM (-5.7, ⚠ cell-cycle shift); [[Brivudine (drug)]] 5 µM (-5.3); [[Tucidinostat (drug)]] 0.5 µM (-3.9, ⚠ cell-cycle shift); [[HI-TOPK-032 (drug)]] 5 µM (-2.4); [[Ipatasertib (drug)]] 0.5 µM (-2.3); [[PH-797804 (drug)]] 0.5 µM (-1.8); [[Brivudine (drug)]] 0.5 µM (-1.8); [[Tofacitinib (citrate) (drug)]] 0.5 µM (-1.7); [[Thymol (drug)]] 0.5 µM (-1.5); [[Ipatasertib (drug)]] 0.05 µM (-1.5); [[Tofacitinib (citrate) (drug)]] 5 µM (-1.4) (48 in all, 9 with an alert ⚠; shown: the 10 strongest and the 6 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[PANC-1 (line)]], [[SW480 (line)]], [[HOP62 (line)]], [[LOX-IMVI (line)]], [[MIA PaCa-2 (line)]], [[A498 (line)]], [[LoVo (line)]], [[HS-578T (line)]]

## + arm (20)

| Gene | Projection | Name |
|---|---|---|
| [[RNF6]] | 0.910 | ring finger protein 6 |
| [[ZXDA]] | 0.820 | zinc finger X-linked duplicated A |
| [[POLR2M]] | 0.818 | RNA polymerase II subunit M |
| [[FBXO30]] | 0.812 | F-box protein 30 |
| [[EIF5]] | 0.768 | eukaryotic translation initiation factor 5 |
| [[HTATIP2]] | 0.748 | HIV-1 Tat interactive protein 2 |
| [[MTHFSD]] | 0.747 | methenyltetrahydrofolate synthetase domain containing |
| [[AP5M1]] | 0.746 | adaptor related protein complex 5 subunit mu 1 |
| [[BAG2]] | 0.738 | BAG cochaperone 2 |
| [[TDP2]] | 0.734 | tyrosyl-DNA phosphodiesterase 2 |
| [[C17orf75]] | 0.692 | chromosome 17 open reading frame 75 |
| [[TSR2]] | 0.686 | TSR2 ribosome maturation factor |
| [[AIFM2]] | 0.659 | AIF family member 2, ferroptosis suppressor |
| [[CLIP1]] | 0.654 | CAP-Gly domain containing linker protein 1 |
| [[KICS2]] | 0.649 | KICSTOR subunit 2 |
| [[MTX3]] | 0.640 | metaxin 3 |
| [[DNAJB4]] | 0.625 | DnaJ heat shock protein family (Hsp40) member B4 |
| [[DUS4L]] | 0.587 | dihydrouridine synthase 4 like |
| [[RIT1]] | 0.499 | Ras like without CAAX 1 |
| [[ZFTA]] | 0.493 | zinc finger translocation associated |

## − arm (15)

| Gene | Projection | Name |
|---|---|---|
| [[PIBF1]] | -0.723 | progesterone immunomodulatory binding factor 1 |
| [[PI4KA]] | -0.709 | phosphatidylinositol 4-kinase alpha |
| [[EFHC1]] | -0.697 | EF-hand domain containing 1 |
| [[CKLF]] | -0.683 | chemokine like factor |
| [[ST3GAL5]] | -0.655 | ST3 beta-galactoside alpha-2,3-sialyltransferase 5 |
| [[RNF168]] | -0.647 | ring finger protein 168 |
| [[CTXN1]] | -0.630 | cortexin 1 |
| [[CD320]] | -0.629 | CD320 molecule |
| [[SLC35B2]] | -0.602 | solute carrier family 35 member B2 |
| [[NME7]] | -0.569 | NME/NM23 family member 7 |
| [[GRAMD1C]] | -0.557 | GRAM domain containing 1C |
| [[ABCA7]] | -0.538 | ATP binding cassette subfamily A member 7 |
| [[ADARB1]] | -0.475 | adenosine deaminase RNA specific B1 |
| [[TMEM63A]] | -0.392 | transmembrane protein 63A |
| [[CCNJL]] | -0.378 | cyclin J like |

## Data

- `graph/nodes.parquet` — module == 135; `graph/modules.parquet` — module == 135; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [134] (drug-dose × line)
