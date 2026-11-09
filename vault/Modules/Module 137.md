---
module: 137
type: "module"
n_genes: 34
n_plus: 29
n_minus: 5
arms_opposite: true
mean_cos_between_arms: -0.42583543062210083
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 137

*34 genes (29 in the + arm, 5 in the − arm) · [[Module 137.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 136), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Idarubicin (hydrochloride) (drug)]] 5 µM (+17.6, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (+15.7, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+13.5, ⚠ cell-cycle shift); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (+11.8, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (+11.6, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (+8.9, ⚠ cell-cycle shift); [[Epirubicin (hydrochloride) (drug)]] 5 µM (+8.8, ⚠ cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 5 µM (+7.9, ⚠ toxic; cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 0.5 µM (+7.5, ⚠ cell-cycle shift); [[Selinexor (drug)]] 5 µM (+7.5, ⚠ cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+7.2); [[Homoharringtonine (drug)]] 0.05 µM (+6.1); [[Belumosudil (drug)]] 5 µM (+5.9); [[TAK-901 (drug)]] 0.05 µM (+4.1); [[Clobetasol propionate (drug)]] 0.05 µM (+3.4); [[5-Azacytidine (drug)]] 5 µM (+3.3); [[Amsacrine (drug)]] 5 µM (+3.1); [[Harringtonine (drug)]] 0.05 µM (+2.8); [[Benztropine (mesylate) (drug)]] 0.05 µM (+2.8); [[Abiraterone acetate (drug)]] 0.05 µM (+2.8) (148 in all, 38 with an alert ⚠; shown: the 10 strongest and the 10 next strongest without an alert)
- Lower it: [[Panobinostat (drug)]] 0.5 µM (-21.0, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (-20.6, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (-19.5, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (-12.9, ⚠ cell-cycle shift); [[Belinostat (drug)]] 0.5 µM (-10.7, ⚠ cell-cycle shift); [[Brivudine (drug)]] 5 µM (-7.2); [[Tucidinostat (drug)]] 5 µM (-7.1); [[Tucidinostat (drug)]] 0.5 µM (-5.4, ⚠ cell-cycle shift); [[HI-TOPK-032 (drug)]] 5 µM (-2.9); [[Belinostat (drug)]] 0.05 µM (-2.9); [[Fumaric acid (drug)]] 5 µM (-2.5); [[Niclosamide (olamine) (drug)]] 0.5 µM (-2.3); [[Ipatasertib (drug)]] 0.5 µM (-2.2); [[Pimitespib (drug)]] 5 µM (-2.1); [[Brivudine (drug)]] 0.5 µM (-2.1); [[Silodosin (drug)]] 5 µM (-2.0) (124 in all, 15 with an alert ⚠; shown: the 10 strongest and the 6 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SW480 (line)]], [[SNU-1 (line)]], [[LS 180 (line)]], [[HT-29 (line)]], [[LoVo (line)]], [[KATO III (line)]], [[Panc 03.27 (line)]], [[HOP62 (line)]]

## + arm (29)

| Gene | Projection | Name |
|---|---|---|
| [[FAIM]] | 0.892 | Fas apoptotic inhibitory molecule |
| [[GTF3C6]] | 0.858 | general transcription factor IIIC subunit 6 |
| [[SLC25A21]] | 0.848 | solute carrier family 25 member 21 |
| [[SPRY3]] | 0.811 | sprouty RTK signaling antagonist 3 |
| [[KLHL42]] | 0.805 | kelch like family member 42 |
| [[EFCAB2]] | 0.800 | dynein regulatory complex subunit 8 |
| [[UBTF]] | 0.788 | upstream binding transcription factor |
| [[NIPAL2]] | 0.756 | NIPA like domain containing 2 |
| [[RCBTB2]] | 0.750 | RCC1 and BTB domain containing protein 2 |
| [[ST7]] | 0.744 | suppression of tumorigenicity 7 |
| [[PRDM11]] | 0.738 | PR/SET domain 11 |
| [[FAM169A]] | 0.729 | family with sequence similarity 169 member A |
| [[PHACTR2]] | 0.717 | phosphatase and actin regulator 2 |
| [[GRIP1]] | 0.716 | glutamate receptor interacting protein 1 |
| [[RMDN2]] | 0.711 | regulator of microtubule dynamics 2 |
| [[TMCO4]] | 0.708 | transmembrane and coiled-coil domains 4 |
| [[ANGEL2]] | 0.702 | angel homolog 2 |
| [[DHRS4]] | 0.693 | dehydrogenase/reductase 4 |
| [[DLG5]] | 0.665 | discs large MAGUK scaffold protein 5 |
| [[ARID1B]] | 0.662 | AT-rich interaction domain 1B |
| [[POGLUT1]] | 0.661 | protein O-glucosyltransferase 1 |
| [[FZD6]] | 0.641 | frizzled class receptor 6 |
| [[FBXL17]] | 0.625 | F-box and leucine rich repeat protein 17 |
| [[N4BP2]] | 0.600 | NEDD4 binding protein 2 |
| [[TDRD3]] | 0.569 | tudor domain containing 3 |
| [[AMMECR1]] | 0.563 | AMMECR nuclear protein 1 |
| [[HIPK3]] | 0.541 | homeodomain interacting protein kinase 3 |
| [[ARHGEF35-AS1]] | 0.354 | ARHGEF35 antisense RNA 1 |
| [[CFAP58]] | 0.207 | cilia and flagella associated protein 58 |

## − arm (5)

| Gene | Projection | Name |
|---|---|---|
| [[DNAAF3]] | -0.808 | dynein axonemal assembly factor 3 |
| [[SFXN3]] | -0.659 | sideroflexin 3 |
| [[CDK18]] | -0.651 | cyclin dependent kinase 18 |
| [[SBF2]] | -0.628 | SET binding factor 2 |
| [[CDA]] | -0.491 | cytidine deaminase |

## Data

- `graph/nodes.parquet` — module == 137; `graph/modules.parquet` — module == 137; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [136] (drug-dose × line)
