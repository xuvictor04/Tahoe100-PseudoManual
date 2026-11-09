---
module: 179
type: "module"
n_genes: 22
n_plus: 15
n_minus: 7
arms_opposite: true
mean_cos_between_arms: -0.36713629961013794
label: "RHOA GTPase cycle"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 179

*RHOA GTPase cycle · 22 genes (15 in the + arm, 7 in the − arm) · [[Module 179.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

Label from the validation stage: **RHOA GTPase cycle** (reactome, q 0.013; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| - | RHOA GTPase cycle | reactome | 3/7 | 44.6 | 0.013 |

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 178), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Idarubicin (hydrochloride) (drug)]] 5 µM (+10.5, ⚠ cell-cycle shift); [[TAK-901 (drug)]] 5 µM (+9.1, ⚠ cell-cycle shift); [[PH-797804 (drug)]] 5 µM (+7.6); [[Topotecan (hydrochloride) (drug)]] 5 µM (+6.8, ⚠ toxic; cell-cycle shift); [[Selinexor (drug)]] 5 µM (+5.3, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (+4.8); [[Adagrasib (drug)]] 0.05 µM (+4.4, ⚠ position not correctable); [[Bortezomib (drug)]] 0.05 µM (+4.0, ⚠ cell-cycle shift); [[Lonafarnib (drug)]] 5 µM (+3.5, ⚠ toxic); [[Goserelin (acetate) (drug)]] 5 µM (+3.1); [[TAK-733 (drug)]] 0.05 µM (+3.0); [[Ipatasertib (drug)]] 0.5 µM (+3.0); [[Gallic acid (drug)]] 5 µM (+2.9); [[NVP-BHG712 (drug)]] 0.05 µM (+2.9); [[GSK1059615 (drug)]] 5 µM (+2.8); [[Bortezomib (drug)]] 0.5 µM (+2.7); [[Capivasertib (drug)]] 0.5 µM (+2.7) (159 in all, 22 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)
- Lower it: [[Homoharringtonine (drug)]] 5 µM (-19.7, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-17.1, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (-15.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (-13.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (-12.1, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-11.8, ⚠ cell-cycle shift); [[Belumosudil (drug)]] 5 µM (-7.0); [[Homoharringtonine (drug)]] 0.05 µM (-6.6); [[Dinaciclib (drug)]] 0.05 µM (-5.9, ⚠ toxic; transcription drop; cell-cycle shift); [[Niclosamide (olamine) (drug)]] 5 µM (-5.7, ⚠ toxic; cell-cycle shift); [[Mifepristone (drug)]] 0.5 µM (-3.7); [[Berbamine (drug)]] 0.05 µM (-3.5); [[Thymol (drug)]] 5 µM (-3.4); [[Busulfan (drug)]] 0.05 µM (-3.4); [[Clobetasol propionate (drug)]] 0.05 µM (-3.3); [[Gallic acid (hydrate) (drug)]] 0.05 µM (-3.3); [[Retinoic acid (drug)]] 0.05 µM (-3.3); [[Temsirolimus (drug)]] 0.05 µM (-3.3) (189 in all, 34 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[PANC-1 (line)]], [[A498 (line)]], [[NCI-H2347 (line)]], [[NCI-H1792 (line)]], [[SW480 (line)]], [[SNU-423 (line)]], [[HOP62 (line)]], [[CFPAC-1 (line)]]

## + arm (15)

| Gene | Projection | Name |
|---|---|---|
| [[CDC26]] | 0.827 | cell division cycle 26 |
| [[KHDC4]] | 0.809 | KH domain containing 4, pre-mRNA splicing factor |
| [[RNF139-DT]] | 0.799 | RNF139 divergent transcript |
| [[SNHG21]] | 0.740 | small nucleolar RNA host gene 21 |
| [[TMED7-TICAM2]] | 0.729 | TMED7-TICAM2 readthrough |
| [[HYPK]] | 0.724 | huntingtin interacting protein K |
| [[ZFC3H1]] | 0.698 | zinc finger C3H1-type containing |
| [[USPL1]] | 0.690 | ubiquitin specific peptidase like 1 |
| [[CHST7]] | 0.679 | carbohydrate sulfotransferase 7 |
| [[EDRF1]] | 0.641 | erythroid differentiation regulatory factor 1 |
| [[RHCE]] | 0.626 | Rh blood group CcEe antigens |
| [[ZNF75D]] | 0.564 | zinc finger protein 75D |
| [[LINC02210-CRHR1]] | 0.547 | LINC02210-CRHR1 readthrough |
| [[CCNH]] | 0.470 | cyclin H |
| [[RBM14]] | 0.457 | RNA binding motif protein 14 |

## − arm (7)

| Gene | Projection | Name |
|---|---|---|
| [[ROCK2]] | -0.776 | Rho associated coiled-coil containing protein kinase 2 |
| [[SLK]] | -0.655 | STE20 like kinase |
| [[EEA1]] | -0.651 | early endosome antigen 1 |
| [[SMC6]] | -0.611 | structural maintenance of chromosomes 6 |
| [[KTN1]] | -0.596 | kinectin 1 |
| [[CPT1A]] | -0.557 | carnitine palmitoyltransferase 1A |
| [[TACC1]] | -0.546 | transforming acidic coiled-coil containing protein 1 |

## Data

- `graph/nodes.parquet` — module == 179; `graph/modules.parquet` — module == 179; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [178] (drug-dose × line)
