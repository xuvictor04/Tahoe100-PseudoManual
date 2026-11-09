---
module: 132
type: "module"
n_genes: 36
n_plus: 36
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 132

*36 genes (single-armed) · [[Module 132.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 131), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Tucidinostat (drug)]] 5 µM (+8.0); [[Tucidinostat (drug)]] 0.5 µM (+6.3, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+5.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+4.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (+3.6, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+2.4, ⚠ toxic; transcription drop; cell-cycle shift); [[Brivudine (drug)]] 5 µM (+2.2); [[Tucidinostat (drug)]] 0.05 µM (+2.0); [[Panobinostat (drug)]] 5 µM (+1.8, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (+1.6, ⚠ cell-cycle shift); [[Bentamapimod (drug)]] 0.05 µM (+1.4); [[Ponatinib (drug)]] 5 µM (+1.3); [[Pitavastatin (Calcium) (drug)]] 0.5 µM (+1.3); [[Brivudine (drug)]] 0.5 µM (+1.2); [[Ponatinib (drug)]] 0.5 µM (+1.2); [[Neratinib (maleate) (drug)]] 5 µM (+1.2); [[Bestatin (hydrochloride) (drug)]] 0.05 µM (+1.1) (23 in all, 11 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)
- Lower it: [[Homoharringtonine (drug)]] 5 µM (-10.7, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-7.9, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-7.6, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-7.5, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (-6.0, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (-5.8, ⚠ toxic; transcription drop; cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (-5.5, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (-5.0, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (-4.3, ⚠ cell-cycle shift); [[TAK-901 (drug)]] 5 µM (-3.6, ⚠ cell-cycle shift); [[PH-797804 (drug)]] 5 µM (-2.8); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (-2.6); [[Ixazomib citrate (drug)]] 0.5 µM (-1.8); [[Homoharringtonine (drug)]] 0.05 µM (-1.7); [[Abemaciclib (drug)]] 5 µM (-1.4); [[Sulfatinib (drug)]] 5 µM (-1.4); [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM (-1.3); [[Abemaciclib (drug)]] 0.5 µM (-1.2); [[Mebendazole (drug)]] 5 µM (-1.1); [[HI-TOPK-032 (drug)]] 5 µM (-1.1) (30 in all, 19 with an alert ⚠; shown: the 10 strongest and the 10 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[MIA PaCa-2 (line)]], [[PANC-1 (line)]], [[LOX-IMVI (line)]], [[NCI-H460 (line)]], [[NCI-H2030 (line)]], [[LoVo (line)]], [[SW480 (line)]], [[NCI-H23 (line)]]

## + arm (36)

| Gene | Projection | Name |
|---|---|---|
| [[GNAZ]] | 0.857 | G protein subunit alpha z |
| [[SHANK3]] | 0.837 | SH3 and multiple ankyrin repeat domains 3 |
| [[RAB6B]] | 0.814 | RAB6B, member RAS oncogene family |
| [[BRSK2]] | 0.813 | BR serine/threonine kinase 2 |
| [[PDZD4]] | 0.795 | PDZ domain containing 4 |
| [[SEPTIN5]] | 0.783 | septin 5 |
| [[SULT4A1]] | 0.714 | sulfotransferase family 4A member 1 |
| [[SDC3]] | 0.707 | syndecan 3 |
| [[CACNA1H]] | 0.705 | calcium voltage-gated channel subunit alpha1 H |
| [[TMOD2]] | 0.689 | tropomodulin 2 |
| [[KIF1A]] | 0.684 | kinesin family member 1A |
| [[JAM3]] | 0.670 | junctional adhesion molecule 3 |
| [[GNB5]] | 0.649 | G protein subunit beta 5 |
| [[ZNF483]] | 0.647 | zinc finger protein 483 |
| [[B4GALNT4]] | 0.645 | beta-1,4-N-acetyl-galactosaminyltransferase 4 |
| [[JAG2]] | 0.643 | jagged canonical Notch ligand 2 |
| [[SLC4A3]] | 0.627 | solute carrier family 4 member 3 |
| [[FHL1]] | 0.626 | four and a half LIM domains 1 |
| [[ANXA6]] | 0.621 | annexin A6 |
| [[MCAM]] | 0.604 | melanoma cell adhesion molecule |
| [[SNX10]] | 0.598 | sorting nexin 10 |
| [[FAM78B]] | 0.553 | family with sequence similarity 78 member B |
| [[PTPRU]] | 0.550 | protein tyrosine phosphatase receptor type U |
| [[KRBA1]] | 0.529 | KRAB domain containing 3 |
| [[RNF130]] | 0.528 | ring finger protein 130 |
| [[APBA2]] | 0.519 | amyloid beta precursor protein binding family A member 2 |
| [[MAP3K15]] | 0.506 | mitogen-activated protein kinase kinase kinase 15 |
| [[DOCK11]] | 0.506 | dedicator of cytokinesis 11 |
| [[SNPH]] | 0.500 | syntaphilin |
| [[SPEG]] | 0.487 | striated muscle enriched protein kinase |
| [[GJA3]] | 0.482 | gap junction protein alpha 3 |
| [[RETREG1]] | 0.464 | reticulophagy regulator 1 |
| [[TFR2]] | 0.455 | transferrin receptor 2 |
| [[EHD3]] | 0.455 | EH domain containing 3 |
| [[ARHGAP45]] | 0.308 | Rho GTPase activating protein 45 |
| [[ZDHHC2]] | 0.283 | zDHHC palmitoyltransferase 2 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 132; `graph/modules.parquet` — module == 132; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [131] (drug-dose × line)
