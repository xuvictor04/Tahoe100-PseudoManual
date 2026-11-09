---
module: 231
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

# Module 231

*6 genes (single-armed) · [[Module 231.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 230), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM (+7.1, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+7.0, ⚠ cell-cycle shift); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (+6.9, ⚠ cell-cycle shift); [[Epirubicin (hydrochloride) (drug)]] 5 µM (+5.2, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (+4.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (+3.9, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (+2.8, ⚠ cell-cycle shift); [[Cobimetinib (drug)]] 5 µM (+2.7); [[Trametinib (drug)]] 0.5 µM (+2.6); [[Selinexor (drug)]] 0.5 µM (+2.6, ⚠ cell-cycle shift); [[Binimetinib (drug)]] 5 µM (+2.3); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM (+2.2); [[Bimiralisib (drug)]] 5 µM (+2.1); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (+2.0); [[PH-797804 (drug)]] 5 µM (+2.0); [[RMC-6236 (drug)]] 5 µM (+1.9); [[Verteporfin (drug)]] 5 µM (+1.8); [[Binimetinib (drug)]] 0.5 µM (+1.8) (65 in all, 20 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Panobinostat (drug)]] 0.5 µM (-14.4, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (-14.3, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (-13.8, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (-11.8, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (-11.8, ⚠ toxic; transcription drop; cell-cycle shift); [[Belinostat (drug)]] 5 µM (-10.1, ⚠ cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 5 µM (-8.9, ⚠ toxic; cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (-7.3); [[Panobinostat (drug)]] 0.05 µM (-5.8, ⚠ cell-cycle shift); [[c-Kit-IN-1 (drug)]] 0.05 µM (-4.3, ⚠ unreliable plate only); [[Belumosudil (drug)]] 5 µM (-4.1); [[c-Kit-IN-1 (drug)]] 5 µM (-2.9); [[TAK-733 (drug)]] 5 µM (-2.9); [[Abemaciclib (drug)]] 5 µM (-2.7); [[Brivudine (drug)]] 5 µM (-2.6); [[Pralsetinib (drug)]] 5 µM (-2.5); [[vincristine (drug)]] 0.5 µM (-2.2); [[vincristine (drug)]] 5 µM (-1.9); [[Filgotinib (drug)]] 5 µM (-1.8) (73 in all, 23 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[CFPAC-1 (line)]], [[Panc 03.27 (line)]], [[NCI-H2347 (line)]], [[NCI-H1573 (line)]], [[LOX-IMVI (line)]], [[HT-29 (line)]], [[SW 900 (line)]], [[SW1417 (line)]]

## + arm (6)

| Gene | Projection | Name |
|---|---|---|
| [[ARID4B]] | 0.875 | AT-rich interaction domain 4B |
| [[SOS1]] | 0.795 | SOS Ras/Rac guanine nucleotide exchange factor 1 |
| [[RC3H1]] | 0.775 | ring finger and CCCH-type domains 1 |
| [[BBX]] | 0.765 | BBX high mobility group box domain containing |
| [[BMPR2]] | 0.721 | bone morphogenetic protein receptor type 2 |
| [[GPBP1]] | 0.637 | GC-rich promoter binding protein 1 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 231; `graph/modules.parquet` — module == 231; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [230] (drug-dose × line)
