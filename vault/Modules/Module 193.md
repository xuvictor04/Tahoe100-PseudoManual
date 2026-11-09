---
module: 193
type: "module"
n_genes: 17
n_plus: 17
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 193

*17 genes (single-armed) · [[Module 193.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 192), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Tucidinostat (drug)]] 5 µM (+7.0); [[Panobinostat (drug)]] 0.05 µM (+3.8, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (+3.8, ⚠ cell-cycle shift); [[Daptomycin (drug)]] 5 µM (+3.5, ⚠ unreliable plate only); [[Peretinoin (drug)]] 5 µM (+3.0); [[BAY1125976 (drug)]] 5 µM (+3.0); [[Rapamycin (drug)]] 5 µM (+2.6); [[Vinblastine (sulfate) (drug)]] 5 µM (+2.5); [[Daptomycin (drug)]] 0.5 µM (+2.3, ⚠ unreliable plate only); [[Sapanisertib (drug)]] 0.05 µM (+2.3, ⚠ cell-cycle shift); [[Vinblastine (sulfate) (drug)]] 0.5 µM (+2.1); [[Dabrafenib (drug)]] 5 µM (+2.0); [[Brivudine (drug)]] 5 µM (+1.8); [[Rapamycin (drug)]] 0.5 µM (+1.8); [[Temsirolimus (drug)]] 0.05 µM (+1.8) (51 in all, 11 with an alert ⚠; shown: the 10 strongest and the 5 next strongest without an alert)
- Lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM (-5.6, ⚠ toxic; cell-cycle shift); [[Trametinib (drug)]] 0.5 µM (-5.0); [[Binimetinib (drug)]] 0.5 µM (-4.8); [[Trametinib (drug)]] 5 µM (-4.7, ⚠ cell-cycle shift); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM (-4.7); [[Binimetinib (drug)]] 5 µM (-4.5); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (-4.1); [[Homoharringtonine (drug)]] 5 µM (-4.1, ⚠ cell-cycle shift); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (-3.6); [[Cobimetinib (drug)]] 5 µM (-3.5); [[Binimetinib (drug)]] 0.05 µM (-3.5); [[Elimusertib hydrochloride (drug)]] 0.05 µM (-3.1); [[Cobimetinib (drug)]] 0.5 µM (-3.1) (82 in all, 24 with an alert ⚠; shown: the 10 strongest and the 3 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[AsPC-1 (line)]], [[NCI-H460 (line)]], [[NCI-H1573 (line)]], [[NCI-H23 (line)]], [[MIA PaCa-2 (line)]], [[HOP62 (line)]], [[HepG2_C3A (line)]], [[RKO (line)]]

## + arm (17)

| Gene | Projection | Name |
|---|---|---|
| [[THSD4]] | 0.848 | thrombospondin type 1 domain containing 4 |
| [[BMP6]] | 0.800 | bone morphogenetic protein 6 |
| [[CDH4]] | 0.798 | cadherin 4 |
| [[NR2E3]] | 0.780 | nuclear receptor subfamily 2 group E member 3 |
| [[ASAP2]] | 0.774 | ArfGAP with SH3 domain, ankyrin repeat and PH domain 2 |
| [[DOCK4]] | 0.753 | dedicator of cytokinesis 4 |
| [[SLC35F3]] | 0.746 | solute carrier family 35 member F3 |
| [[SHANK2]] | 0.744 | SH3 and multiple ankyrin repeat domains 2 |
| [[MAMLD1]] | 0.718 | mastermind like domain containing 1 |
| [[DOCK9]] | 0.703 | dedicator of cytokinesis 9 |
| [[FMNL2]] | 0.696 | formin like 2 |
| [[RASA2]] | 0.692 | RAS p21 protein activator 2 |
| [[BMP2K]] | 0.683 | BMP2 inducible kinase |
| [[FHOD3]] | 0.681 | formin homology 2 domain containing 3 |
| [[KIFC3]] | 0.627 | kinesin family member C3 |
| [[ANKRD44]] | 0.607 | ankyrin repeat domain 44 |
| [[KLF12]] | 0.579 | KLF transcription factor 12 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 193; `graph/modules.parquet` — module == 193; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [192] (drug-dose × line)
