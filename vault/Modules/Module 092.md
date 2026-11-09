---
module: 92
type: "module"
n_genes: 49
n_plus: 49
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.29287204146385193
label: "MAPK output"
label_source: "control"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 092

*MAPK output · 49 genes (single-armed) · [[Module 092.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

Label from the validation stage: **MAPK output** (control, q 6e-13; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | MAPK output | control | 8/49 | 137 | 6e-13 |
| + | MAPK output | control | 8/49 | 137 | 6e-13 |
| all | KRAS signaling up | hallmark | 7/49 | 13.1 | 6e-04 |
| + | KRAS signaling up | hallmark | 7/49 | 13.1 | 6e-04 |
| + | Pre-NOTCH Expression and Processing | reactome | 5/49 | 27.5 | 6e-04 |
| all | Pre-NOTCH Expression and Processing | reactome | 5/49 | 27.5 | 6e-04 |
| all | MAPK family signaling cascades | reactome | 8/49 | 9.05 | 0.001 |
| + | MAPK family signaling cascades | reactome | 8/49 | 9.05 | 0.001 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 91), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM (+4.1, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+3.4); [[Tucidinostat (drug)]] 0.5 µM (+2.5, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+2.4, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+2.4, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+2.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Auranofin (drug)]] 5 µM (+1.9); [[Filgotinib (drug)]] 5 µM (+1.8); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+1.7); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (+1.6, ⚠ cell-cycle shift); [[4EGI-1 (drug)]] 5 µM (+1.2); [[BAY1125976 (drug)]] 5 µM (+1.2); [[Tirabrutinib (drug)]] 0.5 µM (+1.2); [[Temsirolimus (drug)]] 0.05 µM (+1.1); [[Ferulic acid (drug)]] 0.5 µM (+1.1); [[Diphenhydramine (drug)]] 0.5 µM (+1.1) (20 in all, 9 with an alert ⚠; shown: the 10 strongest and the 6 next strongest without an alert)
- Lower it: [[Trametinib (drug)]] 5 µM (-8.0, ⚠ cell-cycle shift); [[Trametinib (drug)]] 0.5 µM (-7.0); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM (-6.6); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (-6.3); [[Cobimetinib (drug)]] 5 µM (-6.1); [[Binimetinib (drug)]] 5 µM (-6.0); [[Panobinostat (drug)]] 0.5 µM (-5.6, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (-5.3, ⚠ cell-cycle shift); [[Binimetinib (drug)]] 0.5 µM (-5.0); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (-4.9); [[Trametinib (drug)]] 0.05 µM (-4.2); [[Cobimetinib (drug)]] 0.5 µM (-4.1); [[RMC-6236 (drug)]] 5 µM (-3.3) (44 in all, 12 with an alert ⚠; shown: the 10 strongest and the 3 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[MIA PaCa-2 (line)]], [[SW480 (line)]], [[C32 (line)]], [[NCI-H460 (line)]], [[HOP62 (line)]], [[HEC-1-A (line)]], [[SK-MEL-2 (line)]], [[A549 (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 22 candidates, none with an alert; shown: the 15 strongest.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[SPRY4-AS1]] | MAPK output | +0.70 |
| 2 | [[SPRY4]] | MAPK family signaling cascades | +0.64 |
| 3 | [[SPRY2]] | MAPK family signaling cascades | +0.63 |
| 4 | [[LINC01844]] | MAPK output | +0.61 |
| 5 | [[ADGRL4]] | MAPK family signaling cascades | +0.61 |
| 6 | [[B4GALT6]] | MAPK output | +0.60 |
| 7 | [[SPRED1]] | KRAS signaling up | +0.60 |
| 8 | [[EXTL2]] | MAPK output | +0.60 |
| 9 | [[CCND1]] | MAPK family signaling cascades | +0.57 |
| 10 | [[STAMBPL1]] | MAPK output | +0.57 |
| 11 | [[MAML3]] | MAPK output | +0.56 |
| 12 | [[SHC3]] | MAPK output | +0.56 |
| 13 | [[DUSP4]] | KRAS signaling up | +0.55 |
| 14 | [[AGO2]] | MAPK output | +0.55 |
| 15 | [[ETV1]] | MAPK family signaling cascades | +0.55 |

## + arm (49)

| Gene | Projection | Name |
|---|---|---|
| [[SPRY4-AS1]] | 0.860 | SPRY4 antisense RNA 1 |
| [[SPRY4]] | 0.849 | sprouty RTK signaling antagonist 4 |
| [[ETV4]] | 0.844 | ETS variant transcription factor 4 |
| [[SPRED1]] | 0.843 | sprouty related EVH1 domain containing 1 |
| [[SPRY2]] | 0.807 | sprouty RTK signaling antagonist 2 |
| [[ADGRL4]] | 0.804 | adhesion G protein-coupled receptor L4 |
| [[B4GALT6]] | 0.771 | beta-1,4-galactosyltransferase 6 |
| [[ETV1]] | 0.763 | ETS variant transcription factor 1 |
| [[SPRED2]] | 0.762 | sprouty related EVH1 domain containing 2 |
| [[DUSP4]] | 0.748 | dual specificity phosphatase 4 |
| [[LINC01844]] | 0.748 | — |
| [[CCND1]] | 0.737 | cyclin D1 |
| [[SHC3]] | 0.734 | SHC adaptor protein 3 |
| [[AGO2]] | 0.725 | argonaute RISC catalytic component 2 |
| [[CNIH3]] | 0.722 | cornichon family AMPA receptor auxiliary protein 3 |
| [[RASGRF2]] | 0.709 | Ras protein specific guanine nucleotide releasing factor 2 |
| [[ZFPM2-AS1]] | 0.686 | ZFPM2 antisense RNA 1 |
| [[STAMBPL1]] | 0.680 | STAM binding protein like 1 |
| [[EXTL2]] | 0.677 | exostosin like glycosyltransferase 2 |
| [[MAML3]] | 0.651 | mastermind like transcriptional coactivator 3 |
| [[TRBC2]] | 0.644 | T cell receptor beta constant 2 |
| [[NHSL1]] | 0.633 | NHS like 1 |
| [[LINC00467]] | 0.632 | long independently transcribed non-coding RNA 467 |
| [[FURIN]] | 0.621 | furin, paired basic amino acid cleaving enzyme |
| [[PICART1]] | 0.611 | p53 inducible cancer associated RNA transcript 1 |
| [[MCTP1]] | 0.610 | multiple C2 and transmembrane domain containing 1 |
| [[RASGRF1]] | 0.610 | Ras protein specific guanine nucleotide releasing factor 1 |
| [[ANKH]] | 0.604 | ANKH inorganic pyrophosphate transport regulator |
| [[LINC02458]] | 0.595 | long independently transcribed non-coding RNA 2458 |
| [[KIF13A]] | -0.581 | kinesin family member 13A |
| [[ACY1]] | 0.580 | aminoacylase 1 |
| [[SLC37A2]] | 0.571 | solute carrier family 37 member 2 |
| [[ARSG]] | 0.561 | arylsulfatase G |
| [[TEX10]] | 0.541 | testis expressed 10 |
| [[LONRF3]] | 0.538 | LON peptidase N-terminal domain and ring finger 3 |
| [[RASSF3]] | 0.519 | Ras association domain family member 3 |
| [[TRIB2]] | 0.515 | tribbles pseudokinase 2 |
| [[MBP]] | 0.496 | myelin basic protein |
| [[ST3GAL6]] | 0.482 | ST3 beta-galactoside alpha-2,3-sialyltransferase 6 |
| [[POC1B]] | 0.476 | POC1 centriolar protein B |
| [[SLC16A6]] | 0.473 | solute carrier family 16 member 6 |
| [[GOLGA7B-DT]] | 0.466 | GOLGA7B divergent transcript |
| [[NRP1]] | 0.433 | neuropilin 1 |
| [[LIMD2]] | 0.423 | LIM domain containing 2 |
| [[POT1-AS1]] | -0.415 | POT1 antisense RNA 1 |
| [[LINC00472]] | 0.415 | long independently transcribed non-coding RNA 472 |
| [[HEY1]] | 0.403 | hes related family bHLH transcription factor with YRPW motif 1 |
| [[LINC02934]] | 0.386 | long independently transcribed non-coding RNA 2934 |
| [[ST6GAL2]] | 0.378 | ST6 beta-galactoside alpha-2,6-sialyltransferase 2 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 92; `graph/modules.parquet` — module == 92; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [91] (drug-dose × line)
