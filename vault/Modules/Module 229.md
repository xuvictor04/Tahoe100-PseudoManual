---
module: 229
type: "module"
n_genes: 6
n_plus: 6
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.4459552764892578
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 229

*6 genes (single-armed) · [[Module 229.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.45; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 228), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[c-Kit-IN-1 (drug)]] 0.05 µM (+3.9, ⚠ unreliable plate only); [[Ixazomib citrate (drug)]] 5 µM (+3.8, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 0.5 µM (+3.2); [[Auranofin (drug)]] 5 µM (+3.0); [[Bortezomib (drug)]] 0.05 µM (+2.7, ⚠ cell-cycle shift); [[Osimertinib (mesylate) (drug)]] 5 µM (+2.5); [[Sapanisertib (drug)]] 0.5 µM (+2.4); [[Abemaciclib (drug)]] 0.5 µM (+2.1); [[Belzutifan (drug)]] 5 µM (+2.1); [[Abemaciclib (drug)]] 5 µM (+2.1); [[Ipatasertib (drug)]] 0.5 µM (+2.0); [[EX229 (drug)]] 5 µM (+2.0); [[EX229 (drug)]] 0.5 µM (+1.9) (69 in all, 20 with an alert ⚠; shown: the 10 strongest and the 3 next strongest without an alert)
- Lower it: [[Panobinostat (drug)]] 0.5 µM (-5.8, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (-5.3, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (-4.5, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (-3.4, ⚠ cell-cycle shift); [[Trametinib (drug)]] 5 µM (-3.4, ⚠ cell-cycle shift); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (-3.3); [[Adagrasib (drug)]] 0.05 µM (-3.1, ⚠ position not correctable); [[Trametinib (drug)]] 0.5 µM (-3.0); [[Binimetinib (drug)]] 5 µM (-2.9); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM (-2.9); [[Binimetinib (drug)]] 0.5 µM (-2.8); [[Elimusertib hydrochloride (drug)]] 0.05 µM (-2.7); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (-2.7); [[Cobimetinib (drug)]] 0.5 µM (-2.5); [[Triamcinolone (drug)]] 5 µM (-2.3); [[Trametinib (drug)]] 0.05 µM (-2.3) (65 in all, 18 with an alert ⚠; shown: the 10 strongest and the 6 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[HEC-1-A (line)]], [[LOX-IMVI (line)]], [[SNU-423 (line)]], [[RKO (line)]], [[CFPAC-1 (line)]], [[NCI-H1573 (line)]], [[A549 (line)]], [[SW480 (line)]]

## + arm (6)

| Gene | Projection | Name |
|---|---|---|
| [[TM4SF19]] | 0.860 | transmembrane 4 L six family member 19 |
| [[RABGEF1P3]] | 0.835 | RABGEF1 pseudogene 3 |
| [[TM4SF19-DYNLT2B]] | 0.830 | TM4SF19-DYNLT2B readthrough (NMD candidate) |
| [[ATP6V0D2]] | 0.772 | ATPase H+ transporting V0 subunit d2 |
| [[ARMC8]] | -0.682 | armadillo repeat containing 8 |
| [[MYH16]] | 0.637 | myosin heavy chain 16 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 229; `graph/modules.parquet` — module == 229; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [228] (drug-dose × line)
