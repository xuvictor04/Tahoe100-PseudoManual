---
module: 216
type: "module"
n_genes: 12
n_plus: 12
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.34965699911117554
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 216

*12 genes (single-armed) · [[Module 216.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 215), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Tucidinostat (drug)]] 5 µM (+4.8); [[c-Kit-IN-1 (drug)]] 0.05 µM (+3.6, ⚠ unreliable plate only); [[Tucidinostat (drug)]] 0.5 µM (+3.4, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (+3.1, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (+2.9, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (+2.8, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (+2.7, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (+2.7, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (+2.4, ⚠ cell-cycle shift); [[Brivudine (drug)]] 5 µM (+2.3); [[Cobimetinib (drug)]] 5 µM (+2.2); [[EX229 (drug)]] 5 µM (+1.7); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (+1.6); [[Cobimetinib (drug)]] 0.5 µM (+1.5); [[RMC-6236 (drug)]] 5 µM (+1.5); [[Cepharanthine (drug)]] 5 µM (+1.5); [[Berbamine (drug)]] 5 µM (+1.3); [[Clobetasol propionate (drug)]] 5 µM (+1.3) (33 in all, 13 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[TAK-901 (drug)]] 5 µM (-4.0, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (-2.8, ⚠ cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 5 µM (-2.7, ⚠ toxic; cell-cycle shift); [[Docetaxel (drug)]] 0.05 µM (-2.2, ⚠ transcription drop; cell-cycle shift); [[PH-797804 (drug)]] 5 µM (-2.0); [[Ipatasertib (drug)]] 0.5 µM (-1.7); [[Docetaxel (Trihydrate) (drug)]] 0.5 µM (-1.5); [[Vilanterol (drug)]] 5 µM (-1.2); [[Tofacitinib (citrate) (drug)]] 5 µM (-1.2); [[Filgotinib (drug)]] 0.5 µM (-1.2); [[Auranofin (drug)]] 5 µM (-1.2); [[Lactate (calcium) (drug)]] 5 µM (-1.1); [[Tofacitinib (citrate) (drug)]] 0.5 µM (-1.1); [[XRK3F2 (drug)]] 0.5 µM (-1.0) (18 in all, 7 with an alert ⚠; shown: the 10 strongest and the 4 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[HT-29 (line)]], [[PANC-1 (line)]], [[HEC-1-A (line)]], [[HOP62 (line)]], [[NCI-H2347 (line)]], [[A498 (line)]], [[Hs 766T (line)]], [[SW480 (line)]]

## + arm (12)

| Gene | Projection | Name |
|---|---|---|
| [[EFR3A]] | 0.791 | EFR3 homolog A |
| [[USP25]] | 0.752 | ubiquitin specific peptidase 25 |
| [[PPIL3]] | -0.743 | peptidylprolyl isomerase like 3 |
| [[RFK]] | 0.705 | riboflavin kinase |
| [[ENAH]] | 0.699 | ENAH actin regulator |
| [[PANK3]] | 0.660 | pantothenate kinase 3 |
| [[STK3]] | 0.650 | serine/threonine kinase 3 |
| [[NR6A1]] | 0.624 | nuclear receptor subfamily 6 group A member 1 |
| [[ACSL4]] | 0.611 | acyl-CoA synthetase long chain family member 4 |
| [[MYCBP2]] | 0.606 | MYC binding protein 2 |
| [[FAM156A]] | -0.583 | family with sequence similarity 156 member A |
| [[TXNDC15]] | -0.426 | thioredoxin domain containing 15 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 216; `graph/modules.parquet` — module == 216; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [215] (drug-dose × line)
