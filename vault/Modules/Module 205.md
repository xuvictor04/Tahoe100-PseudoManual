---
module: 205
type: "module"
n_genes: 15
n_plus: 15
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 205

*15 genes (single-armed) · [[Module 205.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 204), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Panobinostat (drug)]] 5 µM (+10.2, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (+8.5, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+7.7, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (+7.3, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (+6.5, ⚠ cell-cycle shift); [[Selinexor (drug)]] 5 µM (+3.8, ⚠ cell-cycle shift); [[TAK-901 (drug)]] 5 µM (+3.0, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.05 µM (+2.8, ⚠ cell-cycle shift); [[Selinexor (drug)]] 0.5 µM (+2.6, ⚠ cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 5 µM (+2.4, ⚠ toxic; cell-cycle shift); [[Tofacitinib (drug)]] 0.05 µM (+2.3); [[Brivudine (drug)]] 5 µM (+2.2); [[Citalopram (hydrobromide) (drug)]] 0.05 µM (+2.0); [[ML264 (drug)]] 0.05 µM (+1.9); [[Afatinib (drug)]] 5 µM (+1.8); [[Ponatinib (drug)]] 0.05 µM (+1.8); [[AZD-8055 (drug)]] 0.5 µM (+1.7); [[Artemether (drug)]] 0.05 µM (+1.6); [[ERK5-IN-2 (drug)]] 0.05 µM (+1.6); [[Bentamapimod (drug)]] 0.05 µM (+1.6) (70 in all, 25 with an alert ⚠; shown: the 10 strongest and the 10 next strongest without an alert)
- Lower it: [[Tucidinostat (drug)]] 5 µM (-7.0); [[Tucidinostat (drug)]] 0.5 µM (-4.7, ⚠ cell-cycle shift); [[Vinblastine (sulfate) (drug)]] 5 µM (-3.9); [[Peretinoin (drug)]] 5 µM (-3.6); [[Auranofin (drug)]] 5 µM (-3.4); [[Harringtonine (drug)]] 0.5 µM (-3.3, ⚠ cell-cycle shift); [[Vinblastine (sulfate) (drug)]] 0.5 µM (-3.3); [[Daptomycin (drug)]] 5 µM (-2.9, ⚠ unreliable plate only); [[Daptomycin (drug)]] 0.5 µM (-2.8, ⚠ unreliable plate only); [[Peretinoin (drug)]] 0.5 µM (-2.7); [[vincristine (drug)]] 0.05 µM (-2.7); [[vincristine (drug)]] 0.5 µM (-2.7); [[Vinblastine (sulfate) (drug)]] 0.05 µM (-2.1); [[TAK-733 (drug)]] 0.05 µM (-1.9) (56 in all, 10 with an alert ⚠; shown: the 10 strongest and the 4 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SW480 (line)]], [[NCI-H460 (line)]], [[LoVo (line)]], [[RKO (line)]], [[PANC-1 (line)]], [[HEC-1-A (line)]], [[NCI-H2347 (line)]], [[KATO III (line)]]

## + arm (15)

| Gene | Projection | Name |
|---|---|---|
| [[CCDC157]] | 0.842 | coiled-coil domain containing 157 |
| [[ANKRD42]] | 0.820 | ankyrin repeat domain 42 |
| [[TMEM67]] | 0.815 | transmembrane protein 67 |
| [[CFAP69]] | 0.795 | cilia and flagella associated protein 69 |
| [[ZNF487]] | 0.762 | zinc finger protein 487 |
| [[CFAP210]] | 0.747 | cilia and flagella associated protein 210 |
| [[KIF9]] | 0.738 | kinesin family member 9 |
| [[RNF213-AS1]] | 0.734 | RNF213 antisense RNA 1 |
| [[DRC3]] | 0.726 | dynein regulatory complex subunit 3 |
| [[MOK]] | 0.723 | MOK protein kinase |
| [[DZANK1]] | 0.690 | double zinc ribbon and ankyrin repeat domains 1 |
| [[FAM174A]] | 0.684 | family with sequence similarity 174 member A |
| [[SLC25A14]] | 0.668 | solute carrier family 25 member 14 |
| [[CCDC40]] | 0.655 | coiled-coil domain 40 molecular ruler complex subunit |
| [[TCTN2]] | 0.626 | tectonic family member 2 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 205; `graph/modules.parquet` — module == 205; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [204] (drug-dose × line)
