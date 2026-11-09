---
module: 84
type: "module"
n_genes: 52
n_plus: 52
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 084

*52 genes (single-armed) · [[Module 084.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 83), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Tucidinostat (drug)]] 5 µM (+4.8); [[Tucidinostat (drug)]] 0.5 µM (+2.8, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (+2.6, ⚠ cell-cycle shift); [[PF-06260933 (drug)]] 5 µM (+1.5); [[Belinostat (drug)]] 0.5 µM (+1.3, ⚠ cell-cycle shift); [[BAY1125976 (drug)]] 5 µM (+1.2); [[Ferulic acid (drug)]] 0.5 µM (+1.2); [[Pitavastatin (Calcium) (drug)]] 0.5 µM (+1.1); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM (+1.1); [[Tirabrutinib (drug)]] 0.5 µM (+1.1); [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM (+1.1); [[Bentamapimod (drug)]] 5 µM (+1.0); [[Vilanterol (drug)]] 0.05 µM (+1.0) (14 in all, 4 with an alert ⚠; shown: the 10 strongest and the 3 next strongest without an alert)
- Lower it: [[Homoharringtonine (drug)]] 5 µM (-6.7, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (-6.6, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-5.8, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-5.2, ⚠ cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 5 µM (-4.7, ⚠ toxic; cell-cycle shift); [[Trametinib (drug)]] 0.5 µM (-4.2); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (-4.2, ⚠ cell-cycle shift); [[Trametinib (drug)]] 5 µM (-4.1, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (-4.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-3.9, ⚠ cell-cycle shift); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM (-3.9); [[Binimetinib (drug)]] 0.5 µM (-3.5); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (-3.5); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (-3.5); [[Binimetinib (drug)]] 5 µM (-3.3); [[Binimetinib (drug)]] 0.05 µM (-2.9); [[Trametinib (drug)]] 0.05 µM (-2.8); [[Elimusertib hydrochloride (drug)]] 0.05 µM (-2.7); [[Cobimetinib (drug)]] 5 µM (-2.6) (81 in all, 32 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[HOP62 (line)]], [[C32 (line)]], [[MIA PaCa-2 (line)]], [[NCI-H1792 (line)]], [[PANC-1 (line)]], [[RKO (line)]], [[NCI-H460 (line)]], [[LOX-IMVI (line)]]

## + arm (52)

| Gene | Projection | Name |
|---|---|---|
| [[STX1A]] | 0.854 | syntaxin 1A |
| [[RASA3]] | 0.850 | RAS p21 protein activator 3 |
| [[KCNN4]] | 0.844 | potassium calcium-activated channel subfamily N member 4 |
| [[RAC2]] | 0.833 | Rac family small GTPase 2 |
| [[COL13A1]] | 0.804 | collagen type XIII alpha 1 chain |
| [[SH2B3]] | 0.737 | SH2B adaptor protein 3 |
| [[TMEM255B]] | 0.730 | transmembrane protein 255B |
| [[ABTB3]] | 0.729 | ankyrin repeat and BTB domain containing 3 |
| [[PPFIBP1]] | 0.711 | PPFIB scaffold protein 1 |
| [[PAEP]] | 0.711 | progestagen associated endometrial protein |
| [[SHC4]] | 0.709 | SHC adaptor protein 4 |
| [[C13orf46]] | 0.704 | chromosome 13 open reading frame 46 |
| [[EFL1]] | 0.696 | elongation factor like GTPase 1 |
| [[SLC9A7]] | 0.691 | solute carrier family 9 member A7 |
| [[MTSS1]] | 0.687 | MTSS I-BAR domain containing 1 |
| [[GALNT18]] | 0.681 | polypeptide N-acetylgalactosaminyltransferase 18 |
| [[KIF21B]] | 0.680 | kinesin family member 21B |
| [[CPNE5]] | 0.677 | copine 5 |
| [[LINC02970]] | 0.676 | long independently transcribed non-coding RNA 2970 |
| [[CEP170]] | 0.668 | centrosomal protein 170 |
| [[WWTR1]] | 0.667 | WW domain containing transcription regulator 1 |
| [[CHD1L]] | 0.655 | chromodomain helicase DNA binding protein 1 like |
| [[PYGL]] | 0.652 | glycogen phosphorylase L |
| [[HTR7]] | 0.643 | 5-hydroxytryptamine receptor 7 |
| [[DNMBP]] | 0.634 | dynamin binding protein |
| [[RIN1]] | 0.634 | Ras and Rab interactor 1 |
| [[FLT1]] | 0.629 | fms related receptor tyrosine kinase 1 |
| [[PPP1R14C]] | 0.629 | protein phosphatase 1 regulatory inhibitor subunit 14C |
| [[RHBDF2]] | 0.628 | rhomboid 5 homolog 2 |
| [[AFAP1]] | 0.625 | actin filament associated protein 1 |
| [[PLAT]] | 0.620 | plasminogen activator, tissue type |
| [[PTGS1]] | 0.618 | prostaglandin-endoperoxide synthase 1 |
| [[IL1RAP]] | 0.611 | interleukin 1 receptor accessory protein |
| [[MMP17]] | 0.608 | matrix metallopeptidase 17 |
| [[UHRF2]] | 0.585 | ubiquitin like with PHD and ring finger domains 2 |
| [[ADAMTS4]] | 0.580 | ADAM metallopeptidase with thrombospondin type 1 motif 4 |
| [[TLE6]] | 0.577 | TLE family member 6, subcortical maternal complex member |
| [[SH3PXD2A]] | 0.575 | SH3 and PX domains 2A |
| [[FSCN1]] | 0.571 | fascin actin-bundling protein 1 |
| [[RASSF8]] | 0.544 | Ras association domain family member 8 |
| [[STX6]] | 0.536 | syntaxin 6 |
| [[SSH1]] | 0.530 | slingshot protein phosphatase 1 |
| [[RNF182]] | 0.502 | ring finger protein 182 |
| [[APBB2]] | 0.494 | amyloid beta precursor protein binding family B member 2 |
| [[TSPAN5]] | 0.482 | tetraspanin 5 |
| [[TSPAN9]] | 0.472 | tetraspanin 9 |
| [[OAF]] | 0.467 | out at first homolog |
| [[CEP170P1]] | 0.462 | centrosomal protein 170 pseudogene 1 |
| [[SASH1]] | 0.458 | SAM and SH3 domain containing 1 |
| [[NHSL1-AS1]] | 0.453 | NHSL1 antisense RNA 1 |
| [[NAV2]] | 0.436 | neuron navigator 2 |
| [[AKT3]] | 0.324 | AKT serine/threonine kinase 3 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 84; `graph/modules.parquet` — module == 84; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [83] (drug-dose × line)
