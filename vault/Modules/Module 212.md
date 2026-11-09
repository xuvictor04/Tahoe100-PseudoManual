---
module: 212
type: "module"
n_genes: 13
n_plus: 13
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 212

*13 genes (single-armed) · [[Module 212.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 211), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[TAK-901 (drug)]] 5 µM (+6.3, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (+5.4, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (+5.2, ⚠ cell-cycle shift); [[PH-797804 (drug)]] 5 µM (+3.9); [[Belinostat (drug)]] 5 µM (+3.5, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (+3.2); [[Ixazomib citrate (drug)]] 5 µM (+3.1, ⚠ cell-cycle shift); [[Bortezomib (drug)]] 0.05 µM (+3.0, ⚠ cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 5 µM (+2.9, ⚠ toxic; cell-cycle shift); [[Ixazomib citrate (drug)]] 0.5 µM (+2.4); [[Bortezomib (drug)]] 0.5 µM (+1.9); [[Sapanisertib (drug)]] 0.5 µM (+1.6); [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM (+1.6); [[PF-06260933 (drug)]] 5 µM (+1.4); [[Abemaciclib (drug)]] 0.5 µM (+1.4); [[Vilanterol (drug)]] 5 µM (+1.4); [[TAK-733 (drug)]] 0.05 µM (+1.4) (36 in all, 15 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)
- Lower it: [[Dinaciclib (drug)]] 5 µM (-4.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (-4.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-3.9, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (-3.9, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-3.4, ⚠ cell-cycle shift); [[Belumosudil (drug)]] 5 µM (-3.2); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (-2.9); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (-2.7); [[Ponatinib (drug)]] 5 µM (-2.7); [[Cobimetinib (drug)]] 5 µM (-2.6); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM (-2.5); [[Trametinib (drug)]] 0.05 µM (-2.5); [[Homoharringtonine (drug)]] 0.05 µM (-2.3); [[Trametinib (drug)]] 0.5 µM (-2.3); [[Cobimetinib (drug)]] 0.5 µM (-2.0) (53 in all, 13 with an alert ⚠; shown: the 10 strongest and the 5 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SW480 (line)]], [[NCI-H23 (line)]], [[KATO III (line)]], [[LoVo (line)]], [[SK-MEL-2 (line)]], [[LS 180 (line)]], [[SNU-1 (line)]], [[HEC-1-A (line)]]

## + arm (13)

| Gene | Projection | Name |
|---|---|---|
| [[GP6-AS1]] | 0.847 | GP6 antisense RNA 1 |
| [[SDF2]] | 0.816 | stromal cell derived factor 2 |
| [[INTS4]] | 0.809 | integrator complex subunit 4 |
| [[ECD]] | 0.777 | ecdysoneless cell cycle regulator |
| [[ATAT1]] | 0.773 | alpha tubulin acetyltransferase 1 |
| [[WDR37]] | 0.772 | WD repeat domain 37 |
| [[GNAI3]] | 0.752 | G protein subunit alpha i3 |
| [[BIN3]] | 0.736 | bridging integrator 3 |
| [[ELOC]] | 0.698 | elongin C |
| [[TXN2]] | 0.639 | thioredoxin 2 |
| [[FBXL12]] | 0.548 | F-box and leucine rich repeat protein 12 |
| [[BSCL2]] | 0.536 | BSCL2 lipid droplet biogenesis associated, seipin |
| [[TBX20]] | 0.503 | T-box transcription factor 20 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 212; `graph/modules.parquet` — module == 212; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [211] (drug-dose × line)
