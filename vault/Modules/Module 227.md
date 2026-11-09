---
module: 227
type: "module"
n_genes: 9
n_plus: 9
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 227

*9 genes (single-armed) · [[Module 227.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 226), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Panobinostat (drug)]] 5 µM (+4.9, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (+4.8, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (+4.3, ⚠ cell-cycle shift); [[Bortezomib (drug)]] 0.05 µM (+4.3, ⚠ cell-cycle shift); [[Daptomycin (drug)]] 5 µM (+3.7, ⚠ unreliable plate only); [[5-Azacytidine (drug)]] 5 µM (+3.6); [[Pitavastatin (Calcium) (drug)]] 5 µM (+3.5, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 5 µM (+3.5, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 0.5 µM (+3.3); [[Artesunate (drug)]] 5 µM (+3.0, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (+3.0); [[Vinblastine (sulfate) (drug)]] 5 µM (+2.9); [[Pitavastatin (Calcium) (drug)]] 0.5 µM (+2.8); [[Tucidinostat (drug)]] 5 µM (+2.7); [[Neratinib (maleate) (drug)]] 5 µM (+2.5); [[Dihydroartemisinin (drug)]] 5 µM (+2.3); [[Peretinoin (drug)]] 5 µM (+2.0); [[Artesunate (drug)]] 0.5 µM (+1.9) (57 in all, 19 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[NG25 (drug)]] 5 µM (-3.2, ⚠ cell-cycle shift); [[Trametinib (drug)]] 0.5 µM (-2.3); [[Cobimetinib (drug)]] 5 µM (-2.3); [[Elimusertib hydrochloride (drug)]] 0.05 µM (-2.2); [[Selinexor (drug)]] 5 µM (-2.1, ⚠ cell-cycle shift); [[Retinoic acid (drug)]] 0.05 µM (-2.1); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM (-2.1); [[TAK-901 (drug)]] 5 µM (-2.0, ⚠ cell-cycle shift); [[Cobimetinib (drug)]] 0.5 µM (-2.0); [[Dinaciclib (drug)]] 0.5 µM (-2.0, ⚠ toxic; transcription drop; cell-cycle shift); [[PH-797804 (drug)]] 5 µM (-2.0); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (-2.0); [[Binimetinib (drug)]] 0.5 µM (-1.9); [[Radotinib (drug)]] 5 µM (-1.9) (59 in all, 17 with an alert ⚠; shown: the 10 strongest and the 4 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SW480 (line)]], [[LoVo (line)]], [[LS 180 (line)]], [[KATO III (line)]], [[HEC-1-A (line)]], [[BT-474 (line)]], [[NCI-H460 (line)]], [[MIA PaCa-2 (line)]]

## + arm (9)

| Gene | Projection | Name |
|---|---|---|
| [[NIT1]] | 0.811 | nitrilase 1 |
| [[CSGALNACT2]] | 0.779 | chondroitin sulfate N-acetylgalactosaminyltransferase 2 |
| [[PFDN2]] | 0.773 | prefoldin subunit 2 |
| [[SPIRE1]] | 0.735 | spire type actin nucleation factor 1 |
| [[C9orf72]] | 0.690 | C9orf72-SMCR8 complex subunit |
| [[BCLAF3]] | 0.682 | BCLAF1 and THRAP3 family member 3 |
| [[GK]] | 0.656 | glycerol kinase |
| [[STK40]] | 0.644 | serine/threonine kinase 40 |
| [[ZNF558]] | 0.494 | zinc finger protein 558 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 227; `graph/modules.parquet` — module == 227; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [226] (drug-dose × line)
