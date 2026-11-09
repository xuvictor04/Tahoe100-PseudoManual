---
module: 228
type: "module"
n_genes: 8
n_plus: 8
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 228

*8 genes (single-armed) · [[Module 228.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 227), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Homoharringtonine (drug)]] 5 µM (+14.9, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+10.0); [[Tucidinostat (drug)]] 0.5 µM (+6.8, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (+6.4, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+5.2, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+5.1, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (+3.5); [[Dinaciclib (drug)]] 0.05 µM (+3.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (+3.0, ⚠ cell-cycle shift); [[PF-06260933 (drug)]] 5 µM (+2.3); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+2.3); [[Rapamycin (drug)]] 5 µM (+2.0); [[Meloxicam (drug)]] 0.05 µM (+2.0); [[Bestatin (hydrochloride) (drug)]] 0.05 µM (+1.9); [[Harringtonine (drug)]] 0.05 µM (+1.6); [[Tucidinostat (drug)]] 0.05 µM (+1.6); [[4EGI-1 (drug)]] 5 µM (+1.6) (60 in all, 16 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)
- Lower it: [[NG25 (drug)]] 5 µM (-3.3, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (-3.2, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-3.2, ⚠ cell-cycle shift); [[Triamcinolone (drug)]] 0.5 µM (-3.1); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (-2.9, ⚠ cell-cycle shift); [[PH-797804 (drug)]] 5 µM (-2.7); [[Niclosamide (olamine) (drug)]] 5 µM (-2.7, ⚠ toxic; cell-cycle shift); [[Clobetasol propionate (drug)]] 5 µM (-2.7); [[Triamcinolone (drug)]] 5 µM (-2.7); [[Dexamethasone (drug)]] 0.5 µM (-2.5); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (-2.4); [[Dexamethasone (drug)]] 5 µM (-2.4); [[Budesonide (drug)]] 5 µM (-2.3); [[Betamethasone dipropionate (drug)]] 5 µM (-2.2); [[Betamethasone dipropionate (drug)]] 0.05 µM (-2.0) (69 in all, 15 with an alert ⚠; shown: the 10 strongest and the 5 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[J82 (line)]], [[MIA PaCa-2 (line)]], [[RKO (line)]], [[A-172 (line)]], [[A498 (line)]], [[HS-578T (line)]], [[HOP62 (line)]], [[PANC-1 (line)]]

## + arm (8)

| Gene | Projection | Name |
|---|---|---|
| [[BMP2]] | 0.839 | bone morphogenetic protein 2 |
| [[DNAH17]] | 0.771 | dynein axonemal heavy chain 17 |
| [[PGBD5]] | 0.756 | piggyBac transposable element derived 5 |
| [[COL22A1]] | 0.750 | collagen type XXII alpha 1 chain |
| [[EPHB2]] | 0.738 | EPH receptor B2 |
| [[CAMK1D]] | 0.710 | calcium/calmodulin dependent protein kinase ID |
| [[ITGA1]] | 0.664 | integrin subunit alpha 1 |
| [[RAP2B]] | 0.639 | RAP2B, member of RAS oncogene family |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 228; `graph/modules.parquet` — module == 228; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [227] (drug-dose × line)
