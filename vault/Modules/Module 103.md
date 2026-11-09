---
module: 103
type: "module"
n_genes: 45
n_plus: 45
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: "glycolysis"
label_source: "hallmark"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 103

*glycolysis · 45 genes (single-armed) · [[Module 103.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

Label from the validation stage: **glycolysis** (hallmark, q 0.007; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | glycolysis | hallmark | 6/45 | 11.0 | 0.007 |
| + | glycolysis | hallmark | 6/45 | 11.0 | 0.007 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 102), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Entrectinib (drug)]] 5 µM (+1.7); [[Cobimetinib (drug)]] 5 µM (+1.7); [[Pimitespib (drug)]] 5 µM (+1.5); [[Ipatasertib (drug)]] 0.5 µM (+1.4); [[Carbamazepine (drug)]] 5 µM (+1.4); [[Ponatinib (drug)]] 0.5 µM (+1.3); [[Roxadustat (drug)]] 5 µM (+1.3); [[PF-06260933 (drug)]] 5 µM (+1.3); [[Bicalutamide (drug)]] 0.05 µM (+1.3); [[Estrone sulfate (potassium) (drug)]] 5 µM (+1.3) (26 in all, 2 with an alert ⚠; shown: the 10 strongest)
- Lower it: [[Homoharringtonine (drug)]] 5 µM (-9.0, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-7.9, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-7.7, ⚠ cell-cycle shift); [[Niclosamide (olamine) (drug)]] 5 µM (-6.7, ⚠ toxic; cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (-6.3, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-6.0, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (-5.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (-4.6, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (-3.8, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (-3.6, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 0.5 µM (-3.1); [[PH-797804 (drug)]] 5 µM (-2.1); [[5-Azacytidine (drug)]] 5 µM (-2.0); [[Vinblastine (sulfate) (drug)]] 5 µM (-1.8); [[Vinblastine (sulfate) (drug)]] 0.5 µM (-1.8); [[Belumosudil (drug)]] 5 µM (-1.8); [[GSK1059615 (drug)]] 5 µM (-1.7); [[Mebendazole (drug)]] 5 µM (-1.6); [[Peretinoin (drug)]] 0.5 µM (-1.3); [[Peretinoin (drug)]] 5 µM (-1.3) (48 in all, 26 with an alert ⚠; shown: the 10 strongest and the 10 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[C32 (line)]], [[NCI-H1792 (line)]], [[NCI-H460 (line)]], [[MIA PaCa-2 (line)]], [[PANC-1 (line)]], [[SNU-423 (line)]], [[LOX-IMVI (line)]], [[HOP62 (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 1 candidates, none with an alert.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[DDX41]] | glycolysis | +0.59 |

## + arm (45)

| Gene | Projection | Name |
|---|---|---|
| [[PPFIA4]] | 0.832 | PPFI scaffold protein A4 |
| [[GYS1]] | 0.792 | glycogen synthase 1 |
| [[DDX41]] | 0.771 | DEAD-box helicase 41 |
| [[NRN1]] | 0.751 | neuritin 1 |
| [[DPYSL4]] | 0.733 | dihydropyrimidinase like 4 |
| [[ABCB6]] | 0.697 | ATP binding cassette subfamily B member 6 (LAN blood group) |
| [[LINC03047]] | 0.697 | long independently transcribed non-coding RNA 3047 |
| [[ZNF8-DT]] | 0.692 | ZNF8 divergent transcript |
| [[HOXA13]] | 0.676 | homeobox A13 |
| [[ISM2]] | 0.675 | isthmin 2 |
| [[DPCD]] | 0.660 | deleted in primary ciliary dyskinesia homolog (mouse) |
| [[SMAD9]] | 0.654 | SMAD family member 9 |
| [[TMEM45A]] | 0.646 | transmembrane protein 45A |
| [[TBC1D9B]] | 0.637 | TBC1 domain family member 9B |
| [[TMEM39B]] | 0.635 | transmembrane protein 39B |
| [[UPK1A-AS1]] | 0.634 | UPK1A antisense RNA 1 |
| [[ZNF404]] | 0.632 | zinc finger protein 404 |
| [[LZTS2]] | 0.614 | leucine zipper tumor suppressor 2 |
| [[SCAND2P]] | 0.608 | SCAN domain containing 2 pseudogene |
| [[PPFIA3]] | 0.602 | PPFI scaffold protein A3 |
| [[LINC02575]] | 0.600 | long independently transcribed non-coding RNA 2575 |
| [[TMEM74B]] | 0.590 | transmembrane protein 74B |
| [[KDM2B]] | 0.583 | lysine demethylase 2B |
| [[PRSS53]] | 0.581 | serine protease 53 |
| [[TMEM145]] | 0.580 | transmembrane protein 145 |
| [[APLN]] | 0.577 | apelin |
| [[CEP250]] | 0.564 | centrosomal protein 250 |
| [[CCDC47]] | 0.557 | coiled-coil domain containing 47 |
| [[WNK3]] | 0.549 | WNK lysine deficient protein kinase 3 |
| [[SPAG4]] | 0.544 | sperm associated antigen 4 |
| [[TET1]] | 0.540 | tet methylcytosine dioxygenase 1 |
| [[CRABP2]] | 0.538 | cellular retinoic acid binding protein 2 |
| [[PFKL]] | 0.538 | phosphofructokinase, liver type |
| [[B3GNT4]] | 0.518 | UDP-GlcNAc:betaGal beta-1,3-N-acetylglucosaminyltransferase 4 |
| [[MPI]] | 0.517 | mannose phosphate isomerase |
| [[EOLA1]] | 0.499 | endothelium and lymphocyte associated ASCH domain 1 |
| [[C2orf72]] | 0.494 | chromosome 2 open reading frame 72 |
| [[CA9]] | 0.477 | carbonic anhydrase 9 |
| [[RASSF4]] | 0.442 | Ras association domain family member 4 |
| [[ABL1]] | 0.412 | ABL proto-oncogene 1, non-receptor tyrosine kinase |
| [[BRSK1]] | 0.405 | BR serine/threonine kinase 1 |
| [[FGF11]] | 0.390 | fibroblast growth factor 11 |
| [[ICAM5]] | 0.383 | intercellular adhesion molecule 5 |
| [[HSF4]] | 0.365 | heat shock transcription factor 4 |
| [[SUOX]] | 0.291 | sulfite oxidase |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 103; `graph/modules.parquet` — module == 103; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [102] (drug-dose × line)
