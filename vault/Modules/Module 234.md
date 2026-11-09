---
module: 234
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

# Module 234

*5 genes (single-armed) · [[Module 234.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 233), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM (+6.1, ⚠ cell-cycle shift); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (+6.0, ⚠ cell-cycle shift); [[Epirubicin (hydrochloride) (drug)]] 5 µM (+4.2, ⚠ cell-cycle shift); [[GSK1059615 (drug)]] 5 µM (+4.1); [[Ouabain (Octahydrate) (drug)]] 5 µM (+3.7, ⚠ cell-cycle shift); [[Pitavastatin (Calcium) (drug)]] 5 µM (+3.3, ⚠ cell-cycle shift); [[Pitavastatin (Calcium) (drug)]] 0.5 µM (+2.8); [[RMC-6236 (drug)]] 5 µM (+2.7); [[Bimiralisib (drug)]] 5 µM (+2.7); [[BAY1125976 (drug)]] 5 µM (+2.6); [[Dihydroartemisinin (drug)]] 5 µM (+2.4); [[Sapanisertib (drug)]] 5 µM (+2.3); [[Tomivosertib (drug)]] 5 µM (+2.2); [[Bimiralisib (drug)]] 0.05 µM (+2.1); [[Artesunate (drug)]] 0.5 µM (+2.0) (109 in all, 16 with an alert ⚠; shown: the 10 strongest and the 5 next strongest without an alert)
- Lower it: [[Dinaciclib (drug)]] 0.5 µM (-15.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (-14.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (-12.1, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (-11.5, ⚠ toxic; transcription drop; cell-cycle shift); [[Panobinostat (drug)]] 5 µM (-11.0, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-10.5, ⚠ cell-cycle shift); [[c-Kit-IN-1 (drug)]] 0.05 µM (-9.7, ⚠ unreliable plate only); [[Belinostat (drug)]] 5 µM (-9.6, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (-9.4); [[Homoharringtonine (drug)]] 5 µM (-7.8, ⚠ cell-cycle shift); [[TAK-733 (drug)]] 5 µM (-6.1); [[c-Kit-IN-1 (drug)]] 5 µM (-5.5); [[Abemaciclib (drug)]] 5 µM (-5.4); [[venetoclax (drug)]] 5 µM (-5.3); [[Ixazomib citrate (drug)]] 0.5 µM (-5.0); [[EX229 (drug)]] 5 µM (-4.7); [[Homoharringtonine (drug)]] 0.05 µM (-3.6); [[Belumosudil (drug)]] 5 µM (-3.3); [[Tucidinostat (drug)]] 5 µM (-3.0) (127 in all, 31 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[NCI-H1792 (line)]], [[MIA PaCa-2 (line)]], [[PANC-1 (line)]], [[HOP62 (line)]], [[A549 (line)]], [[LOX-IMVI (line)]], [[SNU-423 (line)]], [[SW480 (line)]]

## + arm (5)

| Gene | Projection | Name |
|---|---|---|
| [[HERPUD2]] | 0.864 | HERPUD family member 2 |
| [[GPBP1L1]] | 0.843 | GC-rich promoter binding protein 1 like 1 |
| [[CDK19]] | 0.801 | cyclin dependent kinase 19 |
| [[SOS2]] | 0.778 | SOS Ras/Rho guanine nucleotide exchange factor 2 |
| [[FCHO2]] | 0.759 | FCH and mu domain containing endocytic adaptor 2 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 234; `graph/modules.parquet` — module == 234; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [233] (drug-dose × line)
