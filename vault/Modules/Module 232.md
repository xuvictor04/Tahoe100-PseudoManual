---
module: 232
type: "module"
n_genes: 6
n_plus: 6
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 232

*6 genes (single-armed) · [[Module 232.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 231), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Homoharringtonine (drug)]] 5 µM (+5.4, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+5.1, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+4.6, ⚠ toxic; transcription drop; cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (+3.9, ⚠ cell-cycle shift); [[Selinexor (drug)]] 5 µM (+3.8, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+3.8, ⚠ toxic; transcription drop; cell-cycle shift); [[Auranofin (drug)]] 5 µM (+3.5); [[Bimiralisib (drug)]] 5 µM (+3.2); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (+3.0, ⚠ cell-cycle shift); [[Trametinib (drug)]] 5 µM (+2.7, ⚠ cell-cycle shift); [[Ponatinib (drug)]] 5 µM (+2.5); [[Trametinib (drug)]] 0.5 µM (+2.1); [[Trametinib (drug)]] 0.05 µM (+2.1); [[RMC-6236 (drug)]] 5 µM (+2.0); [[GSK1059615 (drug)]] 5 µM (+2.0); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (+1.9); [[Sapanisertib (drug)]] 5 µM (+1.8); [[Rapamycin (drug)]] 5 µM (+1.8) (78 in all, 29 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[c-Kit-IN-1 (drug)]] 0.05 µM (-4.6, ⚠ unreliable plate only); [[Abemaciclib (drug)]] 5 µM (-3.4); [[c-Kit-IN-1 (drug)]] 5 µM (-3.1); [[EX229 (drug)]] 5 µM (-3.0); [[TAK-733 (drug)]] 5 µM (-2.9); [[Abemaciclib (drug)]] 0.5 µM (-2.6); [[EX229 (drug)]] 0.5 µM (-2.4); [[venetoclax (drug)]] 5 µM (-2.1); [[EX229 (drug)]] 0.05 µM (-2.0); [[Panobinostat (drug)]] 0.5 µM (-2.0, ⚠ cell-cycle shift); [[Sapanisertib (drug)]] 0.5 µM (-2.0); [[Belzutifan (drug)]] 5 µM (-1.9) (37 in all, 8 with an alert ⚠; shown: the 10 strongest and the 2 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[HOP62 (line)]], [[A498 (line)]], [[SW480 (line)]], [[HEC-1-A (line)]], [[PANC-1 (line)]], [[hTERT-HPNE (line)]], [[LoVo (line)]], [[NCI-H2347 (line)]]

## + arm (6)

| Gene | Projection | Name |
|---|---|---|
| [[RMND5A]] | 0.872 | required for meiotic nuclear division 5 homolog A |
| [[LINC02035]] | 0.757 | long independently transcribed non-coding RNA 2035 |
| [[ATP9A]] | 0.714 | ATPase phospholipid transporting 9A |
| [[UBL3]] | 0.630 | ubiquitin like 3 |
| [[RFLNA]] | 0.552 | refilin A |
| [[SLC49A4]] | 0.497 | solute carrier family 49 member 4 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 232; `graph/modules.parquet` — module == 232; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [231] (drug-dose × line)
