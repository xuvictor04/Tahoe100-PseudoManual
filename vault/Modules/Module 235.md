---
module: 235
type: "module"
n_genes: 5
n_plus: 5
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 235

*5 genes (single-armed) · [[Module 235.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 234), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM (+11.3, ⚠ cell-cycle shift); [[Epirubicin (hydrochloride) (drug)]] 5 µM (+5.9, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+5.3); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (+5.0, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (+3.5, ⚠ cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+3.1); [[Panobinostat (drug)]] 5 µM (+1.6, ⚠ cell-cycle shift); [[Arbutin (drug)]] 0.05 µM (+1.6); [[Dinaciclib (drug)]] 5 µM (+1.5, ⚠ toxic; transcription drop; cell-cycle shift); [[Estrone sulfate (potassium) (drug)]] 5 µM (+1.5); [[Apalutamide (drug)]] 0.5 µM (+1.4); [[4EGI-1 (drug)]] 5 µM (+1.4); [[Filgotinib (drug)]] 5 µM (+1.4); [[L-Eflornithine (monohydrochloride) (drug)]] 5 µM (+1.3); [[Esmolol (hydrochloride) (drug)]] 5 µM (+1.3); [[Pimitespib (drug)]] 0.5 µM (+1.3) (35 in all, 9 with an alert ⚠; shown: the 10 strongest and the 6 next strongest without an alert)
- Lower it: [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (-5.1); [[Trametinib (drug)]] 5 µM (-4.9, ⚠ cell-cycle shift); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (-4.4); [[Trametinib (drug)]] 0.5 µM (-4.2); [[Binimetinib (drug)]] 0.5 µM (-4.2); [[Binimetinib (drug)]] 5 µM (-3.9); [[Trametinib (drug)]] 0.05 µM (-3.8); [[Homoharringtonine (drug)]] 0.5 µM (-3.8, ⚠ cell-cycle shift); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM (-3.7); [[Vinblastine (sulfate) (drug)]] 5 µM (-3.6); [[Neratinib (maleate) (drug)]] 5 µM (-3.4); [[Binimetinib (drug)]] 0.05 µM (-3.4) (83 in all, 19 with an alert ⚠; shown: the 10 strongest and the 2 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[LOX-IMVI (line)]], [[KATO III (line)]], [[SW480 (line)]], [[C32 (line)]], [[A-172 (line)]], [[BT-474 (line)]], [[A498 (line)]], [[LoVo (line)]]

## + arm (5)

| Gene | Projection | Name |
|---|---|---|
| [[CEMIP]] | 0.883 | cell migration inducing hyaluronidase 1 |
| [[ABHD17C]] | 0.731 | abhydrolase domain containing 17C, depalmitoylase |
| [[EPHA4]] | 0.702 | EPH receptor A4 |
| [[SYTL5]] | 0.695 | synaptotagmin like 5 |
| [[RGS2]] | 0.565 | regulator of G protein signaling 2 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 235; `graph/modules.parquet` — module == 235; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [234] (drug-dose × line)
