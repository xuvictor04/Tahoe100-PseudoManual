---
module: 219
type: "module"
n_genes: 11
n_plus: 11
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.43659812211990356
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 219

*11 genes (single-armed) · [[Module 219.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.44; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 218), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Homoharringtonine (drug)]] 5 µM (+8.9, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (+7.0, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+3.2, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (+2.8, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (+2.1, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+1.8); [[Clobetasol propionate (drug)]] 0.5 µM (+1.8); [[Harringtonine (drug)]] 0.05 µM (+1.7); [[Clobetasol propionate (drug)]] 0.05 µM (+1.7); [[BAY1125976 (drug)]] 5 µM (+1.5); [[Dexamethasone (drug)]] 0.5 µM (+1.3); [[Homoharringtonine (drug)]] 0.05 µM (+1.3); [[Lactate (calcium) (drug)]] 0.5 µM (+1.2); [[Tirabrutinib (drug)]] 0.5 µM (+1.2); [[Pitavastatin (Calcium) (drug)]] 0.5 µM (+1.1) (30 in all, 11 with an alert ⚠; shown: the 10 strongest and the 5 next strongest without an alert)
- Lower it: [[Panobinostat (drug)]] 5 µM (-7.2, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (-6.2, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (-6.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (-6.0, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (-5.6, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (-3.9, ⚠ toxic; transcription drop; cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (-3.8, ⚠ cell-cycle shift); [[Niclosamide (olamine) (drug)]] 5 µM (-3.7, ⚠ toxic; cell-cycle shift); [[Radotinib (drug)]] 5 µM (-3.1); [[Epirubicin (hydrochloride) (drug)]] 5 µM (-2.7, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (-2.5); [[Ponatinib (drug)]] 5 µM (-2.2); [[Ixazomib citrate (drug)]] 0.5 µM (-1.8); [[Ponatinib (drug)]] 0.05 µM (-1.8); [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM (-1.7); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM (-1.7); [[Tofacitinib (citrate) (drug)]] 5 µM (-1.7); [[Flumatinib (mesylate) (drug)]] 5 µM (-1.7); [[Tofacitinib (drug)]] 5 µM (-1.6) (50 in all, 20 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[PANC-1 (line)]], [[A-172 (line)]], [[A549 (line)]], [[SK-MEL-2 (line)]], [[A498 (line)]], [[HepG2_C3A (line)]], [[NCI-H460 (line)]], [[SNU-423 (line)]]

## + arm (11)

| Gene | Projection | Name |
|---|---|---|
| [[TANK]] | 0.853 | TRAF family member associated NFKB activator |
| [[ZBTB38]] | 0.790 | zinc finger and BTB domain containing 38 |
| [[ZC3H12C]] | 0.779 | zinc finger CCCH-type containing 12C |
| [[RBMXL1]] | 0.755 | RBMX like 1 |
| [[IL4R]] | 0.742 | interleukin 4 receptor |
| [[SEC61A2]] | -0.726 | SEC61 translocon subunit alpha 2 |
| [[CCDC71L]] | 0.676 | coiled-coil domain containing 71 like |
| [[CSNK1D]] | 0.675 | casein kinase 1 delta |
| [[CAAP1]] | 0.596 | caspase activity and apoptosis inhibitor 1 |
| [[KYAT3]] | 0.470 | kynurenine aminotransferase 3 |
| [[ZNF672]] | 0.414 | zinc finger protein 672 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 219; `graph/modules.parquet` — module == 219; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [218] (drug-dose × line)
