---
module: 222
type: "module"
n_genes: 10
n_plus: 10
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.425986111164093
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 222

*10 genes (single-armed) · [[Module 222.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.43; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 221), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Tucidinostat (drug)]] 0.5 µM (+2.8, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+2.7); [[Ponatinib (drug)]] 5 µM (+2.4); [[Rapamycin (drug)]] 5 µM (+2.3); [[Bimiralisib (drug)]] 5 µM (+1.9); [[Larotrectinib sulfate (drug)]] 0.5 µM (+1.7, ⚠ unreliable plate only); [[Binimetinib (drug)]] 0.05 µM (+1.5); [[Cobimetinib (drug)]] 5 µM (+1.5); [[Rapamycin (drug)]] 0.5 µM (+1.5); [[Pitavastatin (Calcium) (drug)]] 5 µM (+1.5, ⚠ cell-cycle shift); [[Trametinib (drug)]] 0.05 µM (+1.4); [[BAY1125976 (drug)]] 5 µM (+1.4); [[5-Azacytidine (drug)]] 5 µM (+1.4) (49 in all, 11 with an alert ⚠; shown: the 10 strongest and the 3 next strongest without an alert)
- Lower it: [[Panobinostat (drug)]] 0.5 µM (-8.3, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (-7.8, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (-6.4, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (-5.6, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (-5.4, ⚠ toxic; transcription drop; cell-cycle shift); [[Belinostat (drug)]] 5 µM (-5.0, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (-4.7, ⚠ cell-cycle shift); [[TAK-901 (drug)]] 5 µM (-4.5, ⚠ cell-cycle shift); [[Docetaxel (drug)]] 0.05 µM (-4.2, ⚠ transcription drop; cell-cycle shift); [[c-Kit-IN-1 (drug)]] 0.05 µM (-3.9, ⚠ unreliable plate only); [[Abemaciclib (drug)]] 5 µM (-3.4); [[TAK-733 (drug)]] 5 µM (-3.0); [[c-Kit-IN-1 (drug)]] 5 µM (-2.6); [[Abemaciclib (drug)]] 0.5 µM (-2.5); [[EX229 (drug)]] 0.05 µM (-2.4); [[Belzutifan (drug)]] 5 µM (-2.4); [[Auranofin (drug)]] 5 µM (-2.1); [[PH-797804 (drug)]] 5 µM (-2.0); [[venetoclax (drug)]] 5 µM (-2.0); [[Harringtonine (drug)]] 0.05 µM (-1.7) (47 in all, 19 with an alert ⚠; shown: the 10 strongest and the 10 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[A549 (line)]], [[LOX-IMVI (line)]], [[A-427 (line)]], [[LoVo (line)]], [[NCI-H23 (line)]], [[C-33 A (line)]], [[SW480 (line)]], [[MIA PaCa-2 (line)]]

## + arm (10)

| Gene | Projection | Name |
|---|---|---|
| [[DENND5B]] | 0.847 | DENN domain containing 5B |
| [[GKAP1]] | 0.781 | G kinase anchoring protein 1 |
| [[PLEKHA5]] | 0.774 | pleckstrin homology domain containing A5 |
| [[BEND7]] | 0.754 | BEN domain containing 7 |
| [[ARHGAP1]] | -0.722 | Rho GTPase activating protein 1 |
| [[TBL1X]] | 0.707 | transducin beta like 1 X-linked |
| [[STAU2]] | 0.704 | staufen double-stranded RNA binding protein 2 |
| [[TBCCD1]] | -0.674 | TBCC domain containing 1 |
| [[PARD3]] | 0.659 | par-3 family cell polarity regulator |
| [[FAM171A1]] | 0.553 | family with sequence similarity 171 member A1 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 222; `graph/modules.parquet` — module == 222; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [221] (drug-dose × line)
