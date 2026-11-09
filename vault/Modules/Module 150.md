---
module: 150
type: "module"
n_genes: 30
n_plus: 30
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 150

*30 genes (single-armed) · [[Module 150.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 149), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM (+21.2, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (+12.1, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+9.9, ⚠ toxic; transcription drop; cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+9.6); [[Dinaciclib (drug)]] 5 µM (+9.6, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+8.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 0.5 µM (+7.4, ⚠ cell-cycle shift); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (+6.2, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (+6.1, ⚠ cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+5.9); [[Auranofin (drug)]] 5 µM (+5.4); [[Clobetasol propionate (drug)]] 0.05 µM (+2.3); [[Cobimetinib (drug)]] 5 µM (+2.2); [[Ponatinib (drug)]] 5 µM (+2.1); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (+1.9); [[Ponatinib (drug)]] 0.5 µM (+1.9); [[Trametinib (drug)]] 0.5 µM (+1.8); [[Cobimetinib (drug)]] 0.5 µM (+1.8) (73 in all, 27 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Digitoxin (drug)]] 0.5 µM (-2.3, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.05 µM (-1.7, ⚠ cell-cycle shift); [[Pravastatin (sodium) (drug)]] 5 µM (-1.7); [[Ouabain (Octahydrate) (drug)]] 0.05 µM (-1.6, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-1.6, ⚠ cell-cycle shift); [[Adagrasib (drug)]] 0.05 µM (-1.5, ⚠ position not correctable); [[Clopidogrel (drug)]] 0.05 µM (-1.4); [[Artesunate (drug)]] 5 µM (-1.4, ⚠ cell-cycle shift); [[Goserelin (acetate) (drug)]] 5 µM (-1.3); [[Niclosamide (olamine) (drug)]] 0.5 µM (-1.3); [[Ranolazine (drug)]] 0.5 µM (-1.3); [[Mebendazole (drug)]] 5 µM (-1.3); [[Lucanthone (drug)]] 0.05 µM (-1.2); [[Hexylresorcinol (drug)]] 5 µM (-1.2); [[Fumaric acid (drug)]] 5 µM (-1.1); [[Tomivosertib (drug)]] 5 µM (-1.1) (26 in all, 7 with an alert ⚠; shown: the 10 strongest and the 6 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[NCI-H460 (line)]], [[HOP62 (line)]], [[C-33 A (line)]], [[SK-MEL-2 (line)]], [[HEC-1-A (line)]], [[SW480 (line)]], [[Panc 03.27 (line)]], [[NCI-H23 (line)]]

## + arm (30)

| Gene | Projection | Name |
|---|---|---|
| [[THSD7B]] | 0.862 | thrombospondin type 1 domain containing 7B |
| [[FAT3]] | 0.835 | FAT atypical cadherin 3 |
| [[LINC02268]] | 0.827 | long independently transcribed non-coding RNA 2268 |
| [[COL25A1]] | 0.819 | collagen type XXV alpha 1 chain |
| [[GRID2]] | 0.815 | glutamate ionotropic receptor delta type subunit 2 |
| [[SYNPO2]] | 0.802 | synaptopodin 2 |
| [[LUZP2]] | 0.786 | leucine zipper protein 2 |
| [[LAMA2]] | 0.762 | laminin subunit alpha 2 |
| [[LINC01122]] | 0.750 | long independently transcribed non-coding RNA 1122 |
| [[IPCEF1]] | 0.749 | interaction protein for cytohesin exchange factors 1 |
| [[PRDM6]] | 0.747 | PR/SET domain 6 |
| [[MYO3B]] | 0.725 | myosin IIIB |
| [[PPFIA2]] | 0.718 | PPFI scaffold protein A2 |
| [[SPAG17]] | 0.712 | sperm associated antigen 17 |
| [[AGBL4]] | 0.701 | AGBL carboxypeptidase 4 |
| [[PCDH11X]] | 0.651 | protocadherin 11 X-linked |
| [[LINC00607]] | 0.633 | long independently transcribed non-coding RNA 607 |
| [[RERG]] | 0.632 | RAS like estrogen regulated growth inhibitor |
| [[SVEP1]] | 0.624 | sushi, von Willebrand factor type A, EGF and pentraxin domain containing 1 |
| [[TRPM2]] | 0.587 | transient receptor potential cation channel subfamily M member 2 |
| [[ARHGEF26-AS1]] | 0.581 | ARHGEF26 antisense RNA 1 |
| [[LINC01798]] | 0.576 | long independently transcribed non-coding RNA 1798 |
| [[LINC01807]] | 0.575 | long independently transcribed non-coding RNA 1807 |
| [[MAP1LC3B2]] | 0.560 | microtubule associated protein 1 light chain 3 beta 2 |
| [[EMILIN2]] | 0.560 | elastin microfibril interfacer 2 |
| [[STAT4]] | 0.559 | signal transducer and activator of transcription 4 |
| [[LINC01117]] | 0.555 | long independently transcribed non-coding RNA 1117 |
| [[PCDHA6]] | 0.554 | protocadherin alpha 6 |
| [[DGUOK-AS1]] | 0.538 | DGUOK antisense RNA 1 |
| [[DCLK1]] | 0.378 | doublecortin like kinase 1 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 150; `graph/modules.parquet` — module == 150; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [149] (drug-dose × line)
