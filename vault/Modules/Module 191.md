---
module: 191
type: "module"
n_genes: 18
n_plus: 18
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 191

*18 genes (single-armed) · [[Module 191.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 190), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Homoharringtonine (drug)]] 5 µM (+23.1, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (+20.5, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+18.5, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (+17.9); [[Panobinostat (drug)]] 0.5 µM (+17.8, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (+13.2, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+13.1); [[Dinaciclib (drug)]] 5 µM (+12.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+11.6, ⚠ toxic; transcription drop; cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+10.7, ⚠ cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+4.7); [[Brivudine (drug)]] 5 µM (+3.8); [[Homoharringtonine (drug)]] 0.05 µM (+2.2); [[Ipatasertib (drug)]] 0.5 µM (+1.9); [[Cobimetinib (drug)]] 5 µM (+1.7); [[Cepharanthine (drug)]] 5 µM (+1.7); [[Verteporfin (drug)]] 5 µM (+1.7); [[Tucidinostat (drug)]] 0.05 µM (+1.7) (76 in all, 36 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Digitoxin (drug)]] 0.5 µM (-2.7, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.05 µM (-2.4, ⚠ cell-cycle shift); [[Adagrasib (drug)]] 0.05 µM (-2.2, ⚠ position not correctable); [[Topotecan (hydrochloride) (drug)]] 0.5 µM (-1.7, ⚠ cell-cycle shift); [[Lucanthone (drug)]] 0.05 µM (-1.4); [[Methotrexate (drug)]] 5 µM (-1.4); [[Asciminib (drug)]] 0.05 µM (-1.3); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (-1.3, ⚠ cell-cycle shift); [[Fenofibrate (drug)]] 0.05 µM (-1.3); [[Trifluridine (drug)]] 0.5 µM (-1.2, ⚠ cell-cycle shift); [[Malotilate (drug)]] 5 µM (-1.2); [[Valdecoxib (drug)]] 5 µM (-1.2); [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM (-1.2); [[5-Azacytidine (drug)]] 5 µM (-1.2); [[Goserelin (acetate) (drug)]] 5 µM (-1.2); [[Diphenhydramine (drug)]] 0.05 µM (-1.1) (27 in all, 8 with an alert ⚠; shown: the 10 strongest and the 6 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SW480 (line)]], [[PANC-1 (line)]], [[NCI-H460 (line)]], [[HEC-1-A (line)]], [[A498 (line)]], [[KATO III (line)]], [[A549 (line)]], [[LoVo (line)]]

## + arm (18)

| Gene | Projection | Name |
|---|---|---|
| [[COL26A1]] | 0.905 | collagen type XXVI alpha 1 chain |
| [[HULC]] | 0.877 | hepatocellular carcinoma up-regulated long non-coding RNA |
| [[DNAH3]] | 0.869 | dynein axonemal heavy chain 3 |
| [[LINC00624]] | 0.840 | long independently transcribed non-coding RNA 624 |
| [[KCNAB1]] | 0.830 | potassium voltage-gated channel subfamily A regulatory beta subunit 1 |
| [[CCDC144NL-1]] | 0.826 | — |
| [[CEACAM22P-1]] | 0.764 | — |
| [[LINC00243]] | 0.739 | long independently transcribed non-coding RNA 243 |
| [[CALN1]] | 0.720 | calneuron 1 |
| [[RUNDC3B]] | 0.686 | RUN domain containing 3B |
| [[RFTN2]] | 0.682 | raftlin family member 2 |
| [[DYNLRB2-AS1]] | 0.643 | DYNLRB2 antisense RNA 1 |
| [[SRRM3]] | 0.639 | serine/arginine repetitive matrix 3 |
| [[GNG7]] | 0.639 | G protein subunit gamma 7 |
| [[ZNF815P]] | 0.631 | zinc finger protein 815, pseudogene |
| [[VAV1]] | 0.617 | vav guanine nucleotide exchange factor 1 |
| [[TCN2]] | 0.611 | transcobalamin 2 |
| [[LINC03002]] | 0.538 | long independently transcribed non-coding RNA 3002 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 191; `graph/modules.parquet` — module == 191; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [190] (drug-dose × line)
