---
module: 142
type: "module"
n_genes: 33
n_plus: 33
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.39957624673843384
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 142

*33 genes (single-armed) · [[Module 142.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 141), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Panobinostat (drug)]] 5 µM (+5.7, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (+5.4, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (+4.8, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+4.4, ⚠ cell-cycle shift); [[Bortezomib (drug)]] 0.05 µM (+3.2, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 5 µM (+2.7, ⚠ cell-cycle shift); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (+2.2, ⚠ cell-cycle shift); [[PH-797804 (drug)]] 5 µM (+2.2); [[Auranofin (drug)]] 5 µM (+2.1); [[TAK-901 (drug)]] 5 µM (+2.0, ⚠ cell-cycle shift); [[Bortezomib (drug)]] 0.5 µM (+1.5); [[Ixazomib citrate (drug)]] 0.5 µM (+1.4); [[NVP-BHG712 (drug)]] 0.05 µM (+1.2); [[Capivasertib (drug)]] 0.5 µM (+1.2); [[TAK-733 (drug)]] 0.05 µM (+1.1); [[Vortioxetine (drug)]] 0.5 µM (+1.1); [[GSK1059615 (drug)]] 5 µM (+1.1); [[Triamcinolone (drug)]] 5 µM (+1.1) (25 in all, 13 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Dinaciclib (drug)]] 0.5 µM (-6.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-5.5, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (-5.0, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (-5.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (-4.8, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (-4.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-3.9, ⚠ cell-cycle shift); [[Niclosamide (olamine) (drug)]] 5 µM (-2.7, ⚠ toxic; cell-cycle shift); [[Digitoxin (drug)]] 5 µM (-2.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-2.2, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.05 µM (-2.2); [[Tucidinostat (drug)]] 5 µM (-1.4); [[Gefitinib (drug)]] 5 µM (-1.3); [[Belumosudil (drug)]] 5 µM (-1.3); [[Thymol (drug)]] 5 µM (-1.2); [[Retinoic acid (drug)]] 0.05 µM (-1.2); [[Harringtonine (drug)]] 0.05 µM (-1.2); [[Cyclosporin A (drug)]] 0.05 µM (-1.2); [[Bimiralisib (drug)]] 0.5 µM (-1.1); [[Palmatine (chloride) (drug)]] 0.05 µM (-1.1) (29 in all, 15 with an alert ⚠; shown: the 10 strongest and the 10 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[A-427 (line)]], [[A498 (line)]], [[A549 (line)]], [[A-172 (line)]], [[PANC-1 (line)]], [[SW480 (line)]], [[AsPC-1 (line)]], [[HOP62 (line)]]

## + arm (33)

| Gene | Projection | Name |
|---|---|---|
| [[GPR89A]] | 0.821 | golgi pH regulator A |
| [[RARS2]] | 0.807 | arginyl-tRNA synthetase 2, mitochondrial |
| [[RNF121]] | 0.804 | ring finger protein 121 |
| [[STARD3]] | 0.804 | StAR related lipid transfer domain containing 3 |
| [[UBOX5]] | 0.800 | U-box domain containing 5 |
| [[ZCCHC17]] | 0.794 | zinc finger CCHC-type containing 17 |
| [[SLC30A6]] | 0.773 | solute carrier family 30 member 6 |
| [[C1orf52]] | 0.758 | chromosome 1 open reading frame 52 |
| [[SDHAP4-1]] | 0.756 | — |
| [[TNPO3]] | 0.750 | transportin 3 |
| [[ASB16-AS1]] | 0.740 | ASB16 antisense RNA 1 |
| [[ZNF500]] | 0.730 | zinc finger protein 500 |
| [[RAB43]] | 0.728 | RAB43, member RAS oncogene family |
| [[ZBTB49]] | 0.723 | zinc finger and BTB domain containing 49 |
| [[GPR89B]] | 0.712 | golgi pH regulator B |
| [[CERS5]] | 0.710 | ceramide synthase 5 |
| [[SS18L1]] | 0.709 | SS18L1 subunit of BAF chromatin remodeling complex |
| [[GDAP2]] | 0.708 | ganglioside induced differentiation associated protein 2 |
| [[CWF19L1]] | 0.692 | CWF19 like cell cycle control factor 1 |
| [[SAP130]] | 0.688 | Sin3A associated protein 130 |
| [[ARPC3]] | 0.666 | actin related protein 2/3 complex subunit 3 |
| [[ZNF251]] | 0.663 | zinc finger protein 251 |
| [[DPY19L3]] | 0.629 | dpy-19 like C-mannosyltransferase 3 |
| [[GTF3C5]] | 0.625 | general transcription factor IIIC subunit 5 |
| [[VPS13C]] | -0.622 | vacuolar protein sorting 13 homolog C |
| [[TBL1XR1]] | -0.620 | TBL1X/Y related 1 |
| [[DEPDC5]] | 0.608 | DEP domain containing 5, GATOR1 subcomplex subunit |
| [[ZNF668]] | 0.597 | zinc finger protein 668 |
| [[TMEM14C]] | -0.583 | transmembrane protein 14C |
| [[SH3BP5L]] | 0.556 | SH3 binding domain protein 5 like |
| [[PANK2]] | 0.553 | pantothenate kinase 2 |
| [[ENPP1]] | -0.549 | ectonucleotide pyrophosphatase/phosphodiesterase 1 |
| [[RNF31]] | 0.514 | ring finger protein 31 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 142; `graph/modules.parquet` — module == 142; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [141] (drug-dose × line)
