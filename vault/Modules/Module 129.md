---
module: 129
type: "module"
n_genes: 37
n_plus: 37
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.3089933395385742
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 129

*37 genes (single-armed) · [[Module 129.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 128), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Panobinostat (drug)]] 0.5 µM (+5.9, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (+5.4, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (+4.7, ⚠ cell-cycle shift); [[TAK-901 (drug)]] 5 µM (+4.2, ⚠ cell-cycle shift); [[PH-797804 (drug)]] 5 µM (+3.2); [[Topotecan (hydrochloride) (drug)]] 5 µM (+3.0, ⚠ toxic; cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (+2.8, ⚠ cell-cycle shift); [[Belinostat (drug)]] 0.5 µM (+2.2, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+2.2); [[Topotecan (hydrochloride) (drug)]] 0.5 µM (+1.8, ⚠ cell-cycle shift); [[Brivudine (drug)]] 5 µM (+1.8); [[Bimiralisib (drug)]] 0.05 µM (+1.4); [[Clobetasol propionate (drug)]] 0.5 µM (+1.4); [[TAK-901 (drug)]] 0.05 µM (+1.3); [[Ponatinib (drug)]] 5 µM (+1.3); [[ULK-101 (drug)]] 0.05 µM (+1.2); [[Lactate (calcium) (drug)]] 0.5 µM (+1.1); [[Neratinib (maleate) (drug)]] 5 µM (+1.1) (29 in all, 13 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM (-5.9, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (-5.9, ⚠ toxic; transcription drop; cell-cycle shift); [[Epirubicin (hydrochloride) (drug)]] 5 µM (-5.3, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (-4.7, ⚠ toxic; transcription drop; cell-cycle shift); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (-4.4, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-4.3, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (-3.9, ⚠ toxic; transcription drop; cell-cycle shift); [[Niclosamide (olamine) (drug)]] 5 µM (-3.8, ⚠ toxic; cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (-2.7, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (-2.6, ⚠ toxic; transcription drop; cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (-2.0); [[Cyclosporin A (drug)]] 0.05 µM (-1.4); [[Abemaciclib (drug)]] 5 µM (-1.4); [[Gefitinib (drug)]] 5 µM (-1.3); [[Mebendazole (drug)]] 5 µM (-1.3); [[Sulfatinib (drug)]] 5 µM (-1.2); [[Clopidogrel (drug)]] 0.05 µM (-1.2); [[Allopurinol (drug)]] 0.05 µM (-1.1); [[9-ING-41 (drug)]] 0.5 µM (-1.1); [[Thymol (drug)]] 5 µM (-1.1) (28 in all, 15 with an alert ⚠; shown: the 10 strongest and the 10 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[NCI-H23 (line)]], [[A-172 (line)]], [[HOP62 (line)]], [[HEC-1-A (line)]], [[SK-MEL-2 (line)]], [[A-427 (line)]], [[NCI-H2347 (line)]], [[SW480 (line)]]

## + arm (37)

| Gene | Projection | Name |
|---|---|---|
| [[ZNF329]] | 0.847 | zinc finger protein 329 |
| [[ZNF559]] | 0.837 | zinc finger protein 559 |
| [[ZNF567]] | 0.833 | zinc finger protein 567 |
| [[ZNF790-AS1]] | 0.803 | ZNF790 antisense RNA 1 |
| [[ZNF461]] | 0.789 | zinc finger protein 461 |
| [[SMIM8]] | 0.774 | small integral membrane protein 8 |
| [[ZNF420]] | 0.767 | zinc finger protein 420 |
| [[DHX57]] | 0.761 | DExH-box helicase 57 |
| [[ZNF71]] | 0.757 | zinc finger protein 71 |
| [[ZNF559-ZNF177]] | 0.749 | ZNF559-ZNF177 readthrough |
| [[ZNF527]] | 0.741 | zinc finger protein 527 |
| [[ZNF566]] | 0.731 | zinc finger protein 566 |
| [[ZNF569]] | 0.728 | zinc finger protein 569 |
| [[ZFP82]] | 0.717 | ZFP82 zinc finger protein |
| [[ZNF583]] | 0.706 | zinc finger protein 583 |
| [[PGBD1]] | 0.697 | piggyBac transposable element derived 1 |
| [[ZNF212]] | 0.690 | zinc finger protein 212 |
| [[ZNF322]] | 0.680 | zinc finger protein 322 |
| [[ZNF177]] | 0.674 | zinc finger protein 177 |
| [[EXO5-DT]] | 0.668 | EXO5 divergent transcript |
| [[ZNF571]] | 0.662 | zinc finger protein 571 |
| [[ZNF568]] | 0.635 | zinc finger protein 568 |
| [[ZNF549]] | 0.619 | zinc finger protein 549 |
| [[ZIM2-AS1]] | 0.607 | ZIM2 antisense RNA 1 |
| [[BTBD2]] | 0.589 | BTB domain containing 2 |
| [[ZNF470]] | 0.583 | zinc finger protein 470 |
| [[ZFP28]] | 0.575 | ZFP28 zinc finger protein |
| [[PELP1]] | 0.567 | proline, glutamate and leucine rich protein 1 |
| [[MTMR9]] | 0.534 | myotubularin related protein 9 |
| [[ZNF865]] | 0.524 | zinc finger protein 865 |
| [[USP4]] | 0.518 | ubiquitin specific peptidase 4 |
| [[BAIAP2]] | -0.512 | BAR/IMD domain containing adaptor protein 2 |
| [[ZGPAT]] | 0.429 | zinc finger CCCH-type and G-patch domain containing |
| [[FAM118B]] | 0.398 | SIR2 antiphage like 1 |
| [[RMND5B]] | 0.320 | required for meiotic nuclear division 5 homolog B |
| [[RNF34]] | 0.208 | ring finger protein 34 |
| [[OSBPL11]] | 0.117 | oxysterol binding protein like 11 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 129; `graph/modules.parquet` — module == 129; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [128] (drug-dose × line)
