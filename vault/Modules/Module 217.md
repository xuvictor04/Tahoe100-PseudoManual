---
module: 217
type: "module"
n_genes: 12
n_plus: 12
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 217

*12 genes (single-armed) · [[Module 217.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 216), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Homoharringtonine (drug)]] 5 µM (+11.4, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (+8.2, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+4.9); [[Clobetasol propionate (drug)]] 0.05 µM (+4.0); [[Homoharringtonine (drug)]] 0.5 µM (+3.9, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (+3.8, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+3.0, ⚠ cell-cycle shift); [[Clobetasol propionate (drug)]] 5 µM (+2.9); [[Clobetasol propionate (drug)]] 0.5 µM (+2.8); [[Ponatinib (drug)]] 5 µM (+2.8); [[Budesonide (drug)]] 0.5 µM (+2.7); [[Betamethasone dipropionate (drug)]] 0.05 µM (+2.5); [[Cobimetinib (drug)]] 5 µM (+2.5); [[Betamethasone dipropionate (drug)]] 5 µM (+2.4); [[Budesonide (drug)]] 0.05 µM (+2.4) (74 in all, 16 with an alert ⚠; shown: the 10 strongest and the 5 next strongest without an alert)
- Lower it: [[Panobinostat (drug)]] 5 µM (-7.6, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (-7.4, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (-5.2); [[Belinostat (drug)]] 5 µM (-4.2, ⚠ cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 5 µM (-4.1, ⚠ toxic; cell-cycle shift); [[Ixazomib citrate (drug)]] 5 µM (-4.1, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 0.5 µM (-3.7); [[c-Kit-IN-1 (drug)]] 0.05 µM (-3.6, ⚠ unreliable plate only); [[Bortezomib (drug)]] 0.05 µM (-3.5, ⚠ cell-cycle shift); [[Vinblastine (sulfate) (drug)]] 5 µM (-3.2); [[Vinblastine (sulfate) (drug)]] 0.5 µM (-2.9); [[5-Azacytidine (drug)]] 5 µM (-2.9); [[Abemaciclib (drug)]] 5 µM (-2.3); [[Peretinoin (drug)]] 5 µM (-2.2); [[TAK-733 (drug)]] 5 µM (-2.1); [[c-Kit-IN-1 (drug)]] 5 µM (-1.8); [[Peretinoin (drug)]] 0.5 µM (-1.8) (48 in all, 15 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SW480 (line)]], [[HEC-1-A (line)]], [[KATO III (line)]], [[Panc 03.27 (line)]], [[SW1417 (line)]], [[HT-29 (line)]], [[SHP-77 (line)]], [[A549 (line)]]

## + arm (12)

| Gene | Projection | Name |
|---|---|---|
| [[ZNF608]] | 0.817 | zinc finger protein 608 |
| [[MBNL1]] | 0.755 | muscleblind like splicing regulator 1 |
| [[CAVIN2]] | 0.743 | caveolae associated protein 2 |
| [[MAP3K1]] | 0.718 | mitogen-activated protein kinase kinase kinase 1 |
| [[YAP1]] | 0.703 | Yes1 associated transcriptional regulator |
| [[JADE1]] | 0.691 | jade family PHD finger 1 |
| [[ZFHX3]] | 0.678 | zinc finger homeobox 3 |
| [[RHOBTB3]] | 0.669 | Rho related BTB domain containing 3 |
| [[NFIA]] | 0.634 | nuclear factor I A |
| [[MMD]] | 0.592 | monocyte to macrophage differentiation associated |
| [[AASS]] | 0.564 | aminoadipate-semialdehyde synthase |
| [[CNKSR3]] | 0.476 | CNKSR family member 3 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 217; `graph/modules.parquet` — module == 217; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [216] (drug-dose × line)
