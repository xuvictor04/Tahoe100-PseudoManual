---
module: 194
type: "module"
n_genes: 17
n_plus: 12
n_minus: 5
arms_opposite: true
mean_cos_between_arms: -0.4318091571331024
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 194

*17 genes (12 in the + arm, 5 in the − arm) · [[Module 194.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 193), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Homoharringtonine (drug)]] 5 µM (+22.4, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+17.9, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (+15.7, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+15.1, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+12.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+11.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (+10.4, ⚠ cell-cycle shift); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (+9.9, ⚠ cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+9.9); [[Ouabain (Octahydrate) (drug)]] 5 µM (+9.0, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.05 µM (+6.9); [[Belumosudil (drug)]] 5 µM (+4.6); [[5-Azacytidine (drug)]] 5 µM (+3.8); [[PH-797804 (drug)]] 5 µM (+3.5); [[Auranofin (drug)]] 5 µM (+3.5); [[TAK-901 (drug)]] 0.05 µM (+3.4); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (+3.3); [[Cobimetinib (drug)]] 0.5 µM (+3.0); [[Lidocaine (hydrochloride) (drug)]] 5 µM (+2.9) (175 in all, 36 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)
- Lower it: [[Panobinostat (drug)]] 0.5 µM (-19.1, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (-18.7, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (-18.2, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (-13.0); [[Panobinostat (drug)]] 0.05 µM (-10.6, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (-8.7, ⚠ cell-cycle shift); [[Belinostat (drug)]] 0.5 µM (-6.9, ⚠ cell-cycle shift); [[Brivudine (drug)]] 5 µM (-4.9); [[Ipatasertib (drug)]] 0.5 µM (-3.6); [[GSK1059615 (drug)]] 0.5 µM (-3.4); [[Tucidinostat (drug)]] 0.05 µM (-3.2); [[HI-TOPK-032 (drug)]] 5 µM (-2.8); [[Osimertinib (mesylate) (drug)]] 5 µM (-2.7); [[PF-06260933 (drug)]] 5 µM (-2.6); [[Niclosamide (olamine) (drug)]] 0.5 µM (-2.1); [[Pimitespib (drug)]] 5 µM (-2.1) (128 in all, 16 with an alert ⚠; shown: the 10 strongest and the 6 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SW480 (line)]], [[PANC-1 (line)]], [[LoVo (line)]], [[KATO III (line)]], [[LOX-IMVI (line)]], [[MIA PaCa-2 (line)]], [[RKO (line)]], [[Panc 03.27 (line)]]

## + arm (12)

| Gene | Projection | Name |
|---|---|---|
| [[CPSF2]] | 0.884 | cleavage and polyadenylation specific factor 2 |
| [[ZMYND11]] | 0.879 | zinc finger MYND-type containing 11 |
| [[ZFP91]] | 0.802 | ZFP91 zinc finger protein, atypical E3 ubiquitin ligase |
| [[NSD1]] | 0.792 | nuclear receptor binding SET domain protein 1 |
| [[DPP8]] | 0.762 | dipeptidyl peptidase 8 |
| [[TRAPPC8]] | 0.728 | trafficking protein particle complex subunit 8 |
| [[NDUFS1]] | 0.721 | NADH:ubiquinone oxidoreductase core subunit S1 |
| [[ZNF236]] | 0.666 | zinc finger protein 236 |
| [[TAOK1]] | 0.624 | TAO kinase 1 |
| [[UEVLD]] | 0.607 | UEV and lactate/malate dehyrogenase domains |
| [[CLOCK]] | 0.597 | clock circadian regulator |
| [[TMEM131]] | 0.571 | transmembrane protein 131 |

## − arm (5)

| Gene | Projection | Name |
|---|---|---|
| [[CARHSP1]] | -0.803 | calcium regulated heat stable protein 1 |
| [[RAB11FIP1]] | -0.736 | RAB11 family interacting protein 1 |
| [[RHPN2]] | -0.700 | rhophilin Rho GTPase binding protein 2 |
| [[CLMN]] | -0.641 | calmin |
| [[PELO]] | -0.527 | pelota mRNA surveillance and ribosome rescue factor |

## Data

- `graph/nodes.parquet` — module == 194; `graph/modules.parquet` — module == 194; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [193] (drug-dose × line)
