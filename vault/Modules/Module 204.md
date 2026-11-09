---
module: 204
type: "module"
n_genes: 15
n_plus: 15
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.543161153793335
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 204

*15 genes (single-armed) · [[Module 204.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.54; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 203), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM (+5.0, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (+4.3, ⚠ toxic; transcription drop; cell-cycle shift); [[PH-797804 (drug)]] 5 µM (+3.2); [[Digitoxin (drug)]] 0.5 µM (+3.1, ⚠ cell-cycle shift); [[TAK-901 (drug)]] 5 µM (+2.8, ⚠ cell-cycle shift); [[Tomivosertib (drug)]] 5 µM (+2.3); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (+2.3, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (+2.2, ⚠ cell-cycle shift); [[Brivudine (drug)]] 5 µM (+2.2); [[Belinostat (drug)]] 0.5 µM (+2.1, ⚠ cell-cycle shift); [[Dimethyl fumarate (drug)]] 5 µM (+1.9); [[Verteporfin (drug)]] 5 µM (+1.6); [[Fumaric acid (drug)]] 5 µM (+1.6); [[Irinotecan (hydrochloride) (drug)]] 0.5 µM (+1.5); [[Pravastatin (sodium) (drug)]] 5 µM (+1.5); [[Erlotinib (drug)]] 0.05 µM (+1.4); [[Asciminib (drug)]] 0.05 µM (+1.4) (47 in all, 15 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)
- Lower it: [[Dinaciclib (drug)]] 0.5 µM (-8.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (-8.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (-6.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Auranofin (drug)]] 5 µM (-3.8); [[Topotecan (hydrochloride) (drug)]] 5 µM (-3.4, ⚠ toxic; cell-cycle shift); [[Docetaxel (drug)]] 0.05 µM (-2.3, ⚠ transcription drop; cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-2.2, ⚠ cell-cycle shift); [[Megestrol (drug)]] 0.05 µM (-2.1, ⚠ cell-cycle shift); [[Darinaparsin (drug)]] 5 µM (-2.1, ⚠ cell-cycle shift); [[Thymol (drug)]] 5 µM (-2.0); [[Retinoic acid (drug)]] 0.05 µM (-2.0); [[Belumosudil (drug)]] 5 µM (-2.0); [[Larotrectinib (drug)]] 0.05 µM (-1.9); [[Carbamazepine (drug)]] 5 µM (-1.8); [[Gallic acid (hydrate) (drug)]] 0.05 µM (-1.8); [[Busulfan (drug)]] 0.05 µM (-1.7); [[Filgotinib (drug)]] 5 µM (-1.7); [[Palmatine (chloride) (drug)]] 0.05 µM (-1.6) (60 in all, 13 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SW480 (line)]], [[LS 180 (line)]], [[NCI-H2347 (line)]], [[SW1417 (line)]], [[LoVo (line)]], [[NCI-H1573 (line)]], [[PANC-1 (line)]], [[C32 (line)]]

## + arm (15)

| Gene | Projection | Name |
|---|---|---|
| [[USP3]] | 0.842 | ubiquitin specific peptidase 3 |
| [[TAF2]] | -0.835 | TATA-box binding protein associated factor 2 |
| [[TBC1D12]] | 0.820 | TBC1 domain family member 12 |
| [[PPP1R2]] | 0.803 | protein phosphatase 1 regulatory inhibitor subunit 2 |
| [[REXO1]] | -0.773 | RNA exonuclease 1 homolog |
| [[FNBP1L]] | 0.771 | formin binding protein 1 like |
| [[CNOT6L]] | 0.746 | CCR4-NOT transcription complex subunit 6 like |
| [[PPP2R5A]] | 0.744 | protein phosphatase 2 regulatory subunit B'alpha |
| [[LRP5L]] | 0.729 | LDL receptor related protein 5 like (pseudogene) |
| [[GTF2IP4]] | 0.723 | general transcription factor IIi pseudogene 4 |
| [[TRIM33]] | 0.703 | tripartite motif containing 33 |
| [[EPB41L4B]] | 0.679 | erythrocyte membrane protein band 4.1 like 4B |
| [[RREB1]] | 0.585 | ras responsive element binding protein 1 |
| [[TFEB]] | 0.568 | transcription factor EB |
| [[PTPRA]] | 0.562 | protein tyrosine phosphatase receptor type A |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 204; `graph/modules.parquet` — module == 204; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [203] (drug-dose × line)
