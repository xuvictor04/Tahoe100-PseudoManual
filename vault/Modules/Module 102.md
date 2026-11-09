---
module: 102
type: "module"
n_genes: 45
n_plus: 45
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: "Neuronal System"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 102

*Neuronal System · 45 genes (single-armed) · [[Module 102.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

Label from the validation stage: **Neuronal System** (reactome, q 9e-04; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | Neuronal System | reactome | 8/45 | 9.50 | 9e-04 |
| + | Neuronal System | reactome | 8/45 | 9.50 | 9e-04 |
| all | Transmission across Chemical Synapses | reactome | 6/45 | 10.6 | 0.009 |
| + | Transmission across Chemical Synapses | reactome | 6/45 | 10.6 | 0.009 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 101), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM (+12.9, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+11.1); [[Dinaciclib (drug)]] 5 µM (+9.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (+8.0, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+7.7, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+6.8, ⚠ toxic; transcription drop; cell-cycle shift); [[Auranofin (drug)]] 5 µM (+5.1); [[Panobinostat (drug)]] 0.05 µM (+4.3, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (+3.6, ⚠ cell-cycle shift); [[Bortezomib (drug)]] 5 µM (+3.4, ⚠ toxic; cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+2.7); [[Tucidinostat (drug)]] 0.05 µM (+2.4); [[Brivudine (drug)]] 5 µM (+2.0); [[Ipatasertib (drug)]] 0.5 µM (+1.5); [[Bortezomib (drug)]] 0.5 µM (+1.4); [[Brivudine (drug)]] 0.5 µM (+1.3); [[Amsacrine (drug)]] 5 µM (+1.2); [[Saquinavir (drug)]] 5 µM (+1.2) (48 in all, 26 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Digitoxin (drug)]] 0.5 µM (-3.4, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-3.4, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-2.7, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (-2.3, ⚠ cell-cycle shift); [[TAK-901 (drug)]] 5 µM (-2.2, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.05 µM (-2.0, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (-1.8, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.05 µM (-1.8, ⚠ cell-cycle shift); [[PH-797804 (drug)]] 5 µM (-1.7); [[Artesunate (drug)]] 0.5 µM (-1.3); [[Clopidogrel (drug)]] 0.05 µM (-1.2); [[Mebendazole (drug)]] 5 µM (-1.2); [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM (-1.1); [[Malotilate (drug)]] 5 µM (-1.1); [[Relugolix (drug)]] 0.5 µM (-1.1); [[HI-TOPK-032 (drug)]] 5 µM (-1.0); [[Lucanthone (drug)]] 0.05 µM (-1.0); [[Pravastatin (sodium) (drug)]] 5 µM (-1.0) (21 in all, 11 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[NCI-H23 (line)]], [[SNU-1 (line)]], [[C-33 A (line)]], [[A-427 (line)]], [[NCI-H460 (line)]], [[A-172 (line)]], [[HOP62 (line)]], [[SW480 (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 3 candidates, none with an alert.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[CDH23]] | Transmission across Chemical Synapses | +0.56 |
| 2 | [[GRID1]] | Transmission across Chemical Synapses | +0.55 |
| 3 | [[NKAIN1]] | Transmission across Chemical Synapses | +0.50 |

*⚠ 1 of its 45 genes are in the vector space only through drug-doses that carry an alert (`embed/genes.parquet` evidence_flagged_only): their place here may reflect what those drug-doses did to the cells. They are marked in the tables of this note.*

## + arm (45)

| Gene | Projection | Name | Alert |
|---|---|---|---|
| [[GRID1]] | 0.828 | glutamate ionotropic receptor delta type subunit 1 |  |
| [[CDH23]] | 0.807 | cadherin related 23 |  |
| [[MEGF11]] | 0.785 | multiple EGF like domains 11 |  |
| [[SYN2]] | 0.775 | synapsin II |  |
| [[SDK2]] | 0.759 | sidekick cell adhesion molecule 2 |  |
| [[MSI1]] | 0.751 | musashi RNA binding protein 1 |  |
| [[RASGEF1C]] | 0.741 | RasGEF domain family member 1C |  |
| [[NKAIN1]] | 0.721 | sodium/potassium transporting ATPase interacting 1 |  |
| [[MED12L]] | 0.707 | mediator complex subunit 12L |  |
| [[RBPMS2]] | 0.707 | RNA binding protein, mRNA processing factor 2 |  |
| [[ZNF536]] | 0.700 | zinc finger protein 536 |  |
| [[DOCK3]] | 0.694 | dedicator of cytokinesis 3 |  |
| [[PHF21B]] | 0.693 | PHD finger protein 21B |  |
| [[DGCR5]] | 0.692 | DiGeorge syndrome critical region gene 5 |  |
| [[GNAL]] | 0.687 | G protein subunit alpha L |  |
| [[LRRN2]] | 0.681 | leucine rich repeat neuronal 2 |  |
| [[FAM184A]] | 0.678 | family with sequence similarity 184 member A |  |
| [[CACNA2D2]] | 0.674 | calcium voltage-gated channel auxiliary subunit alpha2delta 2 |  |
| [[RHBDL3]] | 0.667 | rhomboid like 3 |  |
| [[EBF4]] | 0.665 | EBF transcription factor 4 |  |
| [[HAGLR]] | 0.656 | HOXD antisense growth-associated long non-coding RNA |  |
| [[CCDC136]] | 0.649 | coiled-coil domain containing 136 |  |
| [[ADAM23]] | 0.644 | ADAM metallopeptidase domain 23 |  |
| [[GPM6B]] | 0.634 | glycoprotein M6B |  |
| [[KCNG3]] | 0.633 | potassium voltage-gated channel modifier subfamily G member 3 |  |
| [[SLC47A1]] | 0.615 | solute carrier family 47 member 1 |  |
| [[SUGCT]] | 0.611 | succinyl-CoA:glutarate-CoA transferase |  |
| [[CAMK2B]] | 0.607 | calcium/calmodulin dependent protein kinase II beta |  |
| [[GABRB3]] | 0.601 | gamma-aminobutyric acid type A receptor subunit beta3 |  |
| [[PTCHD1]] | 0.583 | patched domain containing 1 |  |
| [[MCF2L2]] | 0.557 | MCF.2 cell line derived transforming sequence-like 2 |  |
| [[ANKRD6]] | 0.553 | ankyrin repeat domain 6 |  |
| [[BVES-AS1]] | 0.534 | POPDC1 antisense RNA 1 |  |
| [[HOMER2]] | 0.522 | homer scaffold protein 2 |  |
| [[KCNIP3]] | 0.515 | potassium voltage-gated channel interacting protein 3 |  |
| [[CHMP1B2P]] | 0.504 | charged multivesicular body protein 1B2, pseudogene |  |
| [[DBNDD1]] | 0.489 | dysbindin domain containing 1 |  |
| [[CELF2]] | 0.481 | CUGBP Elav-like family member 2 |  |
| [[SMO]] | 0.479 | smoothened, frizzled class receptor |  |
| [[SRC]] | 0.456 | SRC proto-oncogene, non-receptor tyrosine kinase |  |
| [[AATK]] | 0.421 | lemur tail kinase 1 |  |
| [[KALRN]] | 0.385 | kalirin RhoGEF kinase |  |
| [[SLC38A4]] | 0.291 | solute carrier family 38 member 4 |  |
| [[LINC02099]] | 0.265 | long independently transcribed non-coding RNA 2099 |  |
| [[BMP10]] | 0.222 | bone morphogenetic protein 10 | ⚠ only flagged evidence |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 102; `graph/modules.parquet` — module == 102; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [101] (drug-dose × line)
