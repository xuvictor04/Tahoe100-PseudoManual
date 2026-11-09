---
module: 192
type: "module"
n_genes: 17
n_plus: 17
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.5039470791816711
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 192

*17 genes (single-armed) · [[Module 192.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.50; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 191), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Tucidinostat (drug)]] 5 µM (+2.8); [[Panobinostat (drug)]] 0.5 µM (+2.7, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (+2.2, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (+2.1, ⚠ cell-cycle shift); [[Ipatasertib (drug)]] 0.5 µM (+2.0); [[Belinostat (drug)]] 0.5 µM (+1.9, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (+1.9, ⚠ cell-cycle shift); [[Pitavastatin (Calcium) (drug)]] 5 µM (+1.7, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (+1.6, ⚠ cell-cycle shift); [[Pitavastatin (Calcium) (drug)]] 0.5 µM (+1.6); [[Thymol (drug)]] 0.5 µM (+1.5); [[9-ING-41 (drug)]] 0.5 µM (+1.4); [[Entrectinib (drug)]] 5 µM (+1.3); [[Methylprednisolone succinate (drug)]] 0.5 µM (+1.3); [[Celecoxib (drug)]] 0.5 µM (+1.2); [[Auranofin (drug)]] 5 µM (+1.1); [[XRK3F2 (drug)]] 0.5 µM (+1.1) (22 in all, 10 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)
- Lower it: [[Homoharringtonine (drug)]] 0.5 µM (-3.5, ⚠ cell-cycle shift); [[c-Kit-IN-1 (drug)]] 0.05 µM (-3.2, ⚠ unreliable plate only); [[Homoharringtonine (drug)]] 5 µM (-3.1, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (-2.6, ⚠ toxic; transcription drop; cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (-2.3, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (-2.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Epirubicin (hydrochloride) (drug)]] 5 µM (-2.0, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (-1.9, ⚠ toxic; transcription drop; cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (-1.8); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (-1.8, ⚠ cell-cycle shift); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (-1.7); [[c-Kit-IN-1 (drug)]] 5 µM (-1.5); [[TAK-733 (drug)]] 5 µM (-1.5); [[Homoharringtonine (drug)]] 0.05 µM (-1.5); [[Ponatinib (drug)]] 5 µM (-1.4); [[Glycyrrhizic acid (drug)]] 0.5 µM (-1.4); [[Erlotinib (drug)]] 0.05 µM (-1.3); [[EX229 (drug)]] 5 µM (-1.3); [[Anethole trithione (drug)]] 0.5 µM (-1.2) (42 in all, 20 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[MIA PaCa-2 (line)]], [[A-172 (line)]], [[Hs 766T (line)]], [[NCI-H2030 (line)]], [[HCT15 (line)]], [[NCI-H23 (line)]], [[NCI-H2347 (line)]], [[A-427 (line)]]

## + arm (17)

| Gene | Projection | Name |
|---|---|---|
| [[PLIN3]] | 0.886 | perilipin 3 |
| [[FAM89B]] | 0.850 | family with sequence similarity 89 member B |
| [[RTN2]] | 0.830 | reticulon 2 |
| [[RRAS]] | 0.819 | RAS related |
| [[FUBP1]] | -0.795 | far upstream element binding protein 1 |
| [[DNASE1L1]] | 0.766 | deoxyribonuclease 1 like 1 |
| [[NNT]] | -0.750 | nicotinamide nucleotide transhydrogenase |
| [[AGPAT2]] | 0.730 | 1-acylglycerol-3-phosphate O-acyltransferase 2 |
| [[ATG2A]] | 0.702 | autophagy related 2A |
| [[MIDN]] | 0.670 | midnolin |
| [[SLC8B1]] | 0.666 | solute carrier family 8 member B1 |
| [[LGALS1]] | 0.660 | galectin 1 |
| [[TBC1D25]] | 0.632 | TBC1 domain family member 25 |
| [[FKBP1B]] | 0.626 | FKBP prolyl isomerase 1B |
| [[DAGLB]] | 0.562 | diacylglycerol lipase beta |
| [[ST3GAL2]] | 0.512 | ST3 beta-galactoside alpha-2,3-sialyltransferase 2 |
| [[TLE3]] | 0.432 | TLE family member 3, transcriptional corepressor |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 192; `graph/modules.parquet` — module == 192; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [191] (drug-dose × line)
