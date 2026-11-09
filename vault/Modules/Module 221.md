---
module: 221
type: "module"
n_genes: 10
n_plus: 10
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.39941778779029846
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 221

*10 genes (single-armed) · [[Module 221.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 220), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Selinexor (drug)]] 5 µM (+5.5, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+3.9, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+3.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Selinexor (drug)]] 0.5 µM (+2.9, ⚠ cell-cycle shift); [[Ponatinib (drug)]] 5 µM (+2.6); [[Topotecan (hydrochloride) (drug)]] 5 µM (+2.5, ⚠ toxic; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+2.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Docetaxel (drug)]] 0.05 µM (+2.0, ⚠ transcription drop; cell-cycle shift); [[Bimiralisib (drug)]] 0.5 µM (+1.8); [[XRK3F2 (drug)]] 0.5 µM (+1.7); [[Neratinib (maleate) (drug)]] 5 µM (+1.7); [[Rapamycin (drug)]] 5 µM (+1.6); [[Temsirolimus (drug)]] 0.5 µM (+1.6); [[GSK1059615 (drug)]] 0.5 µM (+1.5); [[Ponatinib (drug)]] 0.5 µM (+1.5); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (+1.5); [[Neratinib (drug)]] 5 µM (+1.5) (40 in all, 16 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)
- Lower it: [[Homoharringtonine (drug)]] 5 µM (-8.9, ⚠ cell-cycle shift); [[TAK-901 (drug)]] 5 µM (-4.9, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-4.8, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-4.6, ⚠ cell-cycle shift); [[PH-797804 (drug)]] 5 µM (-4.2); [[Ouabain (Octahydrate) (drug)]] 5 µM (-3.8, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (-3.6, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (-2.6, ⚠ toxic; transcription drop; cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (-2.5, ⚠ cell-cycle shift); [[Niclosamide (olamine) (drug)]] 5 µM (-1.9, ⚠ toxic; cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (-1.4); [[Malotilate (drug)]] 0.05 µM (-1.3); [[TAK-901 (drug)]] 0.05 µM (-1.2); [[ERK5-IN-2 (drug)]] 5 µM (-1.1); [[Gefitinib (drug)]] 5 µM (-1.0) (18 in all, 12 with an alert ⚠; shown: the 10 strongest and the 5 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SNU-1 (line)]], [[NCI-H460 (line)]], [[LOX-IMVI (line)]], [[HOP62 (line)]], [[A549 (line)]], [[NCI-H1792 (line)]], [[NCI-H23 (line)]], [[A-172 (line)]]

## + arm (10)

| Gene | Projection | Name |
|---|---|---|
| [[IAH1]] | 0.805 | isoamyl acetate hydrolyzing esterase 1 (putative) |
| [[UBE2Q2P1]] | 0.801 | UBE2Q2 pseudogene 1 |
| [[FAM219B]] | 0.751 | family with sequence similarity 219 member B |
| [[ECHDC3]] | 0.738 | enoyl-CoA hydratase domain containing 3 |
| [[FBXO44]] | 0.726 | F-box protein 44 |
| [[SVIL-AS1-1]] | 0.720 | — |
| [[ZDHHC24]] | 0.699 | zDHHC palmitoyltransferase 24 |
| [[STPG1]] | 0.686 | sperm tail PG-rich repeat containing 1 |
| [[NT5C3B]] | 0.658 | 5'-nucleotidase, cytosolic IIIB |
| [[CFAP44]] | -0.629 | cilia and flagella associated protein 44 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 221; `graph/modules.parquet` — module == 221; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [220] (drug-dose × line)
