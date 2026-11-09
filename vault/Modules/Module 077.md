---
module: 77
type: "module"
n_genes: 59
n_plus: 41
n_minus: 18
arms_opposite: true
mean_cos_between_arms: -0.4409700036048889
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 077

*59 genes (41 in the + arm, 18 in the − arm) · [[Module 077.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 76), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Belinostat (drug)]] 5 µM (+15.0, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (+14.5, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (+13.2, ⚠ cell-cycle shift); [[Belinostat (drug)]] 0.5 µM (+9.2, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (+9.0, ⚠ cell-cycle shift); [[Brivudine (drug)]] 5 µM (+5.6); [[c-Kit-IN-1 (drug)]] 0.05 µM (+4.7, ⚠ unreliable plate only); [[Tucidinostat (drug)]] 5 µM (+4.0); [[PH-797804 (drug)]] 5 µM (+3.2); [[Ixazomib citrate (drug)]] 5 µM (+2.9, ⚠ cell-cycle shift); [[Vinblastine (sulfate) (drug)]] 5 µM (+2.7); [[EX229 (drug)]] 5 µM (+2.3); [[Vinblastine (sulfate) (drug)]] 0.5 µM (+2.3); [[Ipatasertib (drug)]] 0.5 µM (+2.3); [[Baicalin (drug)]] 5 µM (+2.0); [[Belinostat (drug)]] 0.05 µM (+1.9); [[Bortezomib (drug)]] 0.5 µM (+1.9) (69 in all, 13 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)
- Lower it: [[Homoharringtonine (drug)]] 5 µM (-32.5, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-21.1, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-18.4, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (-16.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (-15.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (-12.0, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (-11.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-8.4, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (-8.3, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.05 µM (-6.2); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (-6.2); [[Auranofin (drug)]] 5 µM (-4.4); [[Harringtonine (drug)]] 0.05 µM (-3.6); [[Cobimetinib (drug)]] 5 µM (-3.3); [[Cobimetinib (drug)]] 0.5 µM (-2.9); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (-2.9); [[Trametinib (drug)]] 0.5 µM (-2.7); [[Binimetinib (drug)]] 0.5 µM (-2.5); [[Retinoic acid (drug)]] 0.05 µM (-2.5) (99 in all, 30 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[PANC-1 (line)]], [[A-172 (line)]], [[NCI-H1573 (line)]], [[NCI-H460 (line)]], [[SW480 (line)]], [[HOP62 (line)]], [[HEC-1-A (line)]], [[NCI-H2030 (line)]]

## + arm (41)

| Gene | Projection | Name |
|---|---|---|
| [[TMEM120B]] | 0.866 | transmembrane protein 120B |
| [[ANKRD27]] | 0.860 | ankyrin repeat domain 27 |
| [[LPCAT4]] | 0.833 | lysophosphatidylcholine acyltransferase 4 |
| [[TSEN54]] | 0.818 | tRNA splicing endonuclease subunit 54 |
| [[TAF5L]] | 0.816 | TATA-box binding protein associated factor 5 like |
| [[GFOD2]] | 0.796 | Gfo/Idh/MocA-like oxidoreductase domain containing 2 |
| [[GNA12]] | 0.781 | G protein subunit alpha 12 |
| [[LPCAT1]] | 0.781 | lysophosphatidylcholine acyltransferase 1 |
| [[IMPDH1]] | 0.762 | inosine monophosphate dehydrogenase 1 |
| [[RGS10]] | 0.751 | regulator of G protein signaling 10 |
| [[BICD2]] | 0.747 | BICD cargo adaptor 2 |
| [[ATP7B]] | 0.745 | ATPase copper transporting beta |
| [[SPTLC2]] | 0.743 | serine palmitoyltransferase long chain base subunit 2 |
| [[PBX4]] | 0.741 | PBX homeobox 4 |
| [[BRF1]] | 0.732 | BRF1 general transcription factor IIIB subunit |
| [[MTMR12]] | 0.720 | myotubularin related protein 12 |
| [[EPHB4]] | 0.719 | EPH receptor B4 |
| [[HMOX2]] | 0.718 | heme oxygenase 2 |
| [[TRIM35]] | 0.712 | tripartite motif containing 35 |
| [[ZDHHC9]] | 0.709 | zDHHC palmitoyltransferase 9 |
| [[SSBP4]] | 0.699 | single stranded DNA binding protein 4 |
| [[SMG1P2]] | 0.697 | SMG1 pseudogene 2 |
| [[GRAMD4]] | 0.682 | GRAM domain containing 4 |
| [[MPZL1]] | 0.673 | myelin protein zero like 1 |
| [[BCR]] | 0.666 | BCR activator of RhoGEF and GTPase |
| [[MINK1]] | 0.664 | misshapen like kinase 1 |
| [[NT5DC3]] | 0.649 | 5'-nucleotidase domain containing 3 |
| [[FAM24B]] | 0.633 | family with sequence similarity 24 member B |
| [[PAQR4]] | 0.617 | progestin and adipoQ receptor family member 4 |
| [[PRR5-ARHGAP8]] | 0.609 | PRR5-ARHGAP8 readthrough |
| [[WDFY2]] | 0.588 | WD repeat and FYVE domain containing 2 |
| [[PDCD10]] | 0.579 | programmed cell death 10 |
| [[AMD1]] | 0.568 | adenosylmethionine decarboxylase 1 |
| [[ADA]] | 0.566 | adenosine deaminase |
| [[EVI5]] | 0.556 | ecotropic viral integration site 5 |
| [[BORCS5]] | 0.555 | BLOC-1 related complex subunit 5 |
| [[ZYG11A]] | 0.552 | zyg-11 family member A, cell cycle regulator |
| [[WDR59]] | 0.486 | WD repeat domain 59 |
| [[SLC25A33]] | 0.478 | solute carrier family 25 member 33 |
| [[MAP3K21]] | 0.450 | mitogen-activated protein kinase kinase kinase 21 |
| [[TTC19]] | 0.409 | tetratricopeptide repeat domain 19 |

## − arm (18)

| Gene | Projection | Name |
|---|---|---|
| [[TIA1]] | -0.855 | TIA1 cytotoxic granule associated RNA binding protein |
| [[BAZ2B]] | -0.840 | bromodomain adjacent to zinc finger domain 2B |
| [[C11orf58]] | -0.833 | chromosome 11 open reading frame 58 |
| [[CGGBP1]] | -0.773 | CGG triplet repeat binding protein 1 |
| [[OCIAD1]] | -0.766 | OCIA domain containing 1 |
| [[DCAF8]] | -0.763 | DDB1 and CUL4 associated factor 8 |
| [[THAP9]] | -0.740 | THAP domain containing 9 |
| [[CASC9]] | -0.730 | cancer susceptibility 9 |
| [[TAF9B]] | -0.718 | TATA-box binding protein associated factor 9b |
| [[TAF9]] | -0.689 | TATA-box binding protein associated factor 9 |
| [[RAP2C]] | -0.676 | RAP2C, member of RAS oncogene family |
| [[ARMT1]] | -0.633 | damage control phosphatase 1 |
| [[LGALS8]] | -0.625 | galectin 8 |
| [[SMARCA1]] | -0.599 | SNF2 related chromatin remodeling ATPase 1 |
| [[TSPAN31]] | -0.530 | tetraspanin 31 |
| [[MED29]] | -0.497 | mediator complex subunit 29 |
| [[ENSA]] | -0.480 | endosulfine alpha |
| [[SELENOT]] | -0.476 | selenoprotein T |

## Data

- `graph/nodes.parquet` — module == 77; `graph/modules.parquet` — module == 77; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [76] (drug-dose × line)
