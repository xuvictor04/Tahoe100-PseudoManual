---
module: 176
type: "module"
n_genes: 22
n_plus: 22
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 176

*22 genes (single-armed) · [[Module 176.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 175), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Tucidinostat (drug)]] 5 µM (+12.0); [[Panobinostat (drug)]] 5 µM (+11.2, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (+10.3, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (+9.8, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (+8.8, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+8.6, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+8.6, ⚠ toxic; transcription drop; cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (+7.7, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+6.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+5.7, ⚠ cell-cycle shift); [[Brivudine (drug)]] 5 µM (+5.5); [[Auranofin (drug)]] 5 µM (+2.8); [[Ponatinib (drug)]] 5 µM (+2.5); [[Tucidinostat (drug)]] 0.05 µM (+2.3); [[Brivudine (drug)]] 0.5 µM (+2.0); [[Clobetasol propionate (drug)]] 0.05 µM (+1.9); [[Radotinib (drug)]] 5 µM (+1.9); [[Ponatinib (drug)]] 0.5 µM (+1.9); [[Bentamapimod (drug)]] 0.05 µM (+1.5) (37 in all, 22 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)
- Lower it: [[Harringtonine (drug)]] 5 µM (-5.1, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (-4.9, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-4.7, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-4.6, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (-4.4, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (-3.9, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (-3.6, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.05 µM (-2.8); [[Digitoxin (drug)]] 5 µM (-2.7, ⚠ toxic; transcription drop; cell-cycle shift); [[Artesunate (drug)]] 5 µM (-2.2, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 0.5 µM (-1.7); [[Vinblastine (sulfate) (drug)]] 5 µM (-1.4); [[Dihydroartemisinin (drug)]] 5 µM (-1.4); [[5-Azacytidine (drug)]] 5 µM (-1.4); [[Artesunate (drug)]] 0.5 µM (-1.3); [[TAK-733 (drug)]] 0.05 µM (-1.3); [[Pitavastatin (Calcium) (drug)]] 0.5 µM (-1.3); [[Peretinoin (drug)]] 5 µM (-1.2); [[GSK1059615 (drug)]] 5 µM (-1.1) (30 in all, 15 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[PANC-1 (line)]], [[NCI-H1573 (line)]], [[LOX-IMVI (line)]], [[NCI-H460 (line)]], [[HOP62 (line)]], [[CFPAC-1 (line)]], [[NCI-H2347 (line)]], [[SW480 (line)]]

## + arm (22)

| Gene | Projection | Name |
|---|---|---|
| [[AIF1L]] | 0.844 | allograft inflammatory factor 1 like |
| [[ASIC1]] | 0.835 | acid sensing ion channel subunit 1 |
| [[PODXL2]] | 0.829 | podocalyxin like 2 |
| [[SEPTIN3]] | 0.816 | septin 3 |
| [[LRRC20]] | 0.752 | leucine rich repeat containing 20 |
| [[GLB1L2]] | 0.751 | galactosidase beta 1 like 2 |
| [[HPSE]] | 0.747 | heparanase |
| [[CGREF1]] | 0.728 | cell growth regulator with EF-hand domain 1 |
| [[MMP15]] | 0.710 | matrix metallopeptidase 15 |
| [[PRKAR2B]] | 0.705 | protein kinase cAMP-dependent type II regulatory subunit beta |
| [[TTPA]] | 0.696 | alpha tocopherol transfer protein |
| [[ADAM22]] | 0.694 | ADAM metallopeptidase domain 22 |
| [[CBX2]] | 0.656 | chromobox 2 |
| [[BTNL9]] | 0.653 | butyrophilin like 9 |
| [[RNF157]] | 0.633 | ring finger protein 157 |
| [[OTULINL]] | 0.619 | OTU deubiquitinase with linear linkage specificity like |
| [[ATP1A3]] | 0.603 | ATPase Na+/K+ transporting subunit alpha 3 |
| [[TUB]] | 0.599 | TUB bipartite transcription factor |
| [[NRG2]] | 0.537 | neuregulin 2 |
| [[RAB39A]] | 0.517 | RAB39A, member RAS oncogene family |
| [[SLC43A1]] | 0.488 | solute carrier family 43 member 1 |
| [[DENND11]] | 0.407 | DENN domain containing 11 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 176; `graph/modules.parquet` — module == 176; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [175] (drug-dose × line)
