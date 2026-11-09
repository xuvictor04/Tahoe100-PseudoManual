---
module: 174
type: "module"
n_genes: 23
n_plus: 23
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 174

*23 genes (single-armed) · [[Module 174.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 173), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Tucidinostat (drug)]] 5 µM (+3.2); [[Tucidinostat (drug)]] 0.5 µM (+2.4, ⚠ cell-cycle shift); [[BAY1125976 (drug)]] 5 µM (+2.1); [[Tirabrutinib (drug)]] 0.5 µM (+1.8); [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM (+1.5); [[Panobinostat (drug)]] 0.05 µM (+1.5, ⚠ cell-cycle shift); [[Diphenhydramine (drug)]] 0.5 µM (+1.5); [[Sapanisertib (drug)]] 0.05 µM (+1.4, ⚠ cell-cycle shift); [[4EGI-1 (drug)]] 0.5 µM (+1.4, ⚠ cell-cycle shift); [[Dabrafenib (drug)]] 5 µM (+1.4); [[Clobetasol propionate (drug)]] 0.5 µM (+1.3); [[Fingolimod (hydrochloride) (drug)]] 0.05 µM (+1.3); [[4EGI-1 (drug)]] 5 µM (+1.3); [[Pexidartinib (hydrochloride) (drug)]] 5 µM (+1.3) (34 in all, 5 with an alert ⚠; shown: the 10 strongest and the 4 next strongest without an alert)
- Lower it: [[Homoharringtonine (drug)]] 5 µM (-17.4, ⚠ cell-cycle shift); [[Trametinib (drug)]] 5 µM (-9.8, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-9.4, ⚠ cell-cycle shift); [[Trametinib (drug)]] 0.5 µM (-9.1); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM (-9.0); [[Cobimetinib (drug)]] 5 µM (-8.6); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (-8.5); [[Idarubicin (hydrochloride) (drug)]] 5 µM (-8.3, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-8.1, ⚠ cell-cycle shift); [[Binimetinib (drug)]] 5 µM (-7.8); [[Binimetinib (drug)]] 0.5 µM (-6.8); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (-6.5); [[Cobimetinib (drug)]] 0.5 µM (-6.5); [[Trametinib (drug)]] 0.05 µM (-6.0); [[Ponatinib (drug)]] 5 µM (-5.2) (97 in all, 39 with an alert ⚠; shown: the 10 strongest and the 5 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[NCI-H460 (line)]], [[NCI-H1573 (line)]], [[PANC-1 (line)]], [[HOP62 (line)]], [[C32 (line)]], [[SK-MEL-2 (line)]], [[SW 900 (line)]], [[NCI-H1792 (line)]]

## + arm (23)

| Gene | Projection | Name |
|---|---|---|
| [[PHC2]] | 0.883 | polyhomeotic homolog 2 |
| [[ITGB5]] | 0.856 | integrin subunit beta 5 |
| [[PTPN12]] | 0.853 | protein tyrosine phosphatase non-receptor type 12 |
| [[DUSP6]] | 0.825 | dual specificity phosphatase 6 |
| [[RGS17]] | 0.811 | regulator of G protein signaling 17 |
| [[NIBAN2]] | 0.810 | niban apoptosis regulator 2 |
| [[ST3GAL1]] | 0.803 | ST3 beta-galactoside alpha-2,3-sialyltransferase 1 |
| [[PITPNC1]] | 0.792 | phosphatidylinositol transfer protein cytoplasmic 1 |
| [[HPCAL1]] | 0.790 | hippocalcin like 1 |
| [[NPAS2]] | 0.780 | neuronal PAS domain protein 2 |
| [[DOCK5]] | 0.756 | dedicator of cytokinesis 5 |
| [[ADGRE2]] | 0.749 | adhesion G protein-coupled receptor E2 |
| [[ETV5]] | 0.740 | ETS variant transcription factor 5 |
| [[SLC20A1]] | 0.728 | solute carrier family 20 member 1 |
| [[MAP3K5]] | 0.687 | mitogen-activated protein kinase kinase kinase 5 |
| [[EFNA5]] | 0.664 | ephrin A5 |
| [[TGM2]] | 0.641 | transglutaminase 2 |
| [[ITPRIP]] | 0.621 | inositol 1,4,5-trisphosphate receptor interacting protein |
| [[GBA2]] | 0.598 | glucosylceramidase beta 2 |
| [[STN1]] | 0.598 | STN1 subunit of CST complex |
| [[MYL12A]] | 0.576 | myosin light chain 12A |
| [[ROR1]] | 0.481 | ROR family WNT receptor 1 |
| [[MLPH]] | 0.430 | melanophilin |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 174; `graph/modules.parquet` — module == 174; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [173] (drug-dose × line)
