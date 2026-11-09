---
module: 166
type: "module"
n_genes: 26
n_plus: 26
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 166

*26 genes (single-armed) · [[Module 166.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 165), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM (+19.3, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+11.7, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+11.6, ⚠ toxic; transcription drop; cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (+9.3, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+8.5, ⚠ toxic; transcription drop; cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 0.5 µM (+8.1, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+7.8); [[Auranofin (drug)]] 5 µM (+6.5); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (+5.0, ⚠ cell-cycle shift); [[Epirubicin (hydrochloride) (drug)]] 5 µM (+4.8, ⚠ cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+4.7); [[Cobimetinib (drug)]] 5 µM (+2.1); [[Ipatasertib (drug)]] 0.5 µM (+1.7); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM (+1.7); [[Verteporfin (drug)]] 5 µM (+1.7); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (+1.6); [[Binimetinib (drug)]] 5 µM (+1.5); [[Ponatinib (drug)]] 0.5 µM (+1.5) (73 in all, 29 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Digitoxin (drug)]] 0.5 µM (-2.5, ⚠ cell-cycle shift); [[Adagrasib (drug)]] 0.05 µM (-1.9, ⚠ position not correctable); [[Artesunate (drug)]] 0.5 µM (-1.7); [[Dexamethasone (drug)]] 0.5 µM (-1.6); [[Goserelin (acetate) (drug)]] 5 µM (-1.6); [[Lucanthone (drug)]] 0.05 µM (-1.5); [[Digitoxin (drug)]] 0.05 µM (-1.4, ⚠ cell-cycle shift); [[Mebendazole (drug)]] 5 µM (-1.4); [[Fenofibrate (drug)]] 0.05 µM (-1.3); [[Diphenhydramine (drug)]] 0.05 µM (-1.3); [[5-Azacytidine (drug)]] 5 µM (-1.3); [[(S)-Crizotinib (drug)]] 0.05 µM (-1.2); [[Benproperine (phosphate) (drug)]] 0.05 µM (-1.2) (32 in all, 8 with an alert ⚠; shown: the 10 strongest and the 3 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[CHP-212 (line)]], [[NCI-H460 (line)]], [[PANC-1 (line)]], [[HEC-1-A (line)]], [[SW480 (line)]], [[BT-474 (line)]], [[LoVo (line)]], [[MIA PaCa-2 (line)]]

## + arm (26)

| Gene | Projection | Name |
|---|---|---|
| [[OBI1-AS1]] | 0.895 | OBI1 antisense RNA 1 |
| [[CFAP20DC-DT]] | 0.884 | CFAP20DC divergent transcript |
| [[ESR1]] | 0.879 | estrogen receptor 1 |
| [[DCC]] | 0.869 | DCC netrin 1 receptor |
| [[SORCS1]] | 0.867 | sortilin related VPS10 domain containing receptor 1 |
| [[ST8SIA1]] | 0.846 | ST8 alpha-N-acetyl-neuraminide alpha-2,8-sialyltransferase 1 |
| [[HPSE2]] | 0.845 | heparanase 2 (inactive) |
| [[LINC01500]] | 0.828 | long independently transcribed non-coding RNA 1500 |
| [[SGCD]] | 0.825 | sarcoglycan delta |
| [[CNTN4]] | 0.815 | contactin 4 |
| [[SLC14A2]] | 0.772 | solute carrier family 14 member 2 |
| [[PKP4-AS1]] | 0.769 | PKP4 antisense RNA 1 |
| [[KCNIP1]] | 0.765 | potassium voltage-gated channel interacting protein 1 |
| [[LINC01358]] | 0.755 | — |
| [[SYN3]] | 0.755 | synapsin III |
| [[COL24A1]] | 0.717 | collagen type XXIV alpha 1 chain |
| [[LINC00276]] | 0.708 | long independently transcribed non-coding RNA 276 |
| [[TEX11]] | 0.702 | testis expressed 11 |
| [[LINC01524]] | 0.690 | long independently transcribed non-coding RNA 1524 |
| [[PAMR1]] | 0.603 | peptidase domain containing associated with muscle regeneration 1 |
| [[LINC01151]] | 0.595 | long independently transcribed non-coding RNA 1151 |
| [[FYB1]] | 0.575 | FYN binding protein 1 |
| [[PKIA-AS1]] | 0.553 | PKIA antisense RNA 1 |
| [[ZNF45-AS1]] | 0.530 | ZNF45 antisense RNA 1 |
| [[GRIK4]] | 0.502 | glutamate ionotropic receptor kainate type subunit 4 |
| [[MATN2]] | 0.490 | matrilin 2 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 166; `graph/modules.parquet` — module == 166; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [165] (drug-dose × line)
