---
module: 108
type: "module"
n_genes: 44
n_plus: 44
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 108

*44 genes (single-armed) · [[Module 108.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 107), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM (+10.5, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+9.4, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+9.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+6.5, ⚠ toxic; transcription drop; cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+5.4); [[Tucidinostat (drug)]] 0.5 µM (+3.1, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 0.5 µM (+2.9, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (+2.8); [[Epirubicin (hydrochloride) (drug)]] 5 µM (+2.8, ⚠ cell-cycle shift); [[Docetaxel (drug)]] 0.05 µM (+2.7, ⚠ transcription drop; cell-cycle shift); [[Ipatasertib (drug)]] 0.5 µM (+2.6); [[Ponatinib (drug)]] 0.5 µM (+2.1); [[XRK3F2 (drug)]] 0.5 µM (+2.0); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+2.0); [[Cobimetinib (drug)]] 5 µM (+2.0); [[Docetaxel (Trihydrate) (drug)]] 0.5 µM (+1.9); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (+1.8); [[Verteporfin (drug)]] 5 µM (+1.8) (78 in all, 24 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Digitoxin (drug)]] 0.5 µM (-3.2, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (-2.0, ⚠ cell-cycle shift); [[Mebendazole (drug)]] 5 µM (-2.0); [[Lucanthone (drug)]] 0.05 µM (-2.0); [[Adagrasib (drug)]] 0.05 µM (-1.9, ⚠ position not correctable); [[Artesunate (drug)]] 0.5 µM (-1.9); [[Digitoxin (drug)]] 0.05 µM (-1.9, ⚠ cell-cycle shift); [[Diphenhydramine (drug)]] 0.05 µM (-1.8); [[Erlotinib (drug)]] 0.05 µM (-1.8); [[Pravastatin (sodium) (drug)]] 5 µM (-1.7); [[Rutin (trihydrate) (drug)]] 0.05 µM (-1.7); [[Clopidogrel (drug)]] 0.05 µM (-1.7); [[Anethole trithione (drug)]] 0.5 µM (-1.6); [[(S)-Crizotinib (drug)]] 0.05 µM (-1.6) (67 in all, 17 with an alert ⚠; shown: the 10 strongest and the 4 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SK-MEL-2 (line)]], [[COLO 205 (line)]], [[C-33 A (line)]], [[A-427 (line)]], [[LOX-IMVI (line)]], [[NCI-H1573 (line)]], [[NCI-H23 (line)]], [[NCI-H460 (line)]]

## + arm (44)

| Gene | Projection | Name |
|---|---|---|
| [[KC6]] | 0.853 | — |
| [[MIR3171HG]] | 0.818 | MIR3171 host gene |
| [[LINC02377]] | 0.779 | long independently transcribed non-coding RNA 2377 |
| [[GABRA3]] | 0.775 | gamma-aminobutyric acid type A receptor subunit alpha3 |
| [[LINC01242]] | 0.770 | long independently transcribed non-coding RNA 1242 |
| [[MIR548XHG]] | 0.769 | MIR548X host gene |
| [[MSC-AS1]] | 0.763 | MSC antisense RNA 1 |
| [[LINC01446]] | 0.738 | long independently transcribed non-coding RNA 1446 |
| [[LINC02267]] | 0.732 | long independently transcribed non-coding RNA 2267 |
| [[NETO1]] | 0.688 | neuropilin and tolloid like 1 |
| [[KCNH5]] | 0.686 | potassium voltage-gated channel subfamily H member 5 |
| [[ZNF521]] | 0.682 | zinc finger protein 521 |
| [[MAGEA3-DT]] | 0.681 | MAGEA3 divergent transcript |
| [[LINC01266]] | 0.676 | long independently transcribed non-coding RNA 1266 |
| [[LINC00648]] | 0.667 | long independently transcribed non-coding RNA 648 |
| [[ADGRB3]] | 0.666 | adhesion G protein-coupled receptor B3 |
| [[LINC02109]] | 0.656 | long independently transcribed non-coding RNA 2109 |
| [[PAX3]] | 0.655 | paired box 3 |
| [[LINC02616]] | 0.654 | long independently transcribed non-coding RNA 2616 |
| [[LINC00879]] | 0.638 | long independently transcribed non-coding RNA 879 |
| [[MGAT4C]] | 0.627 | MGAT4 family member C |
| [[JAKMIP2]] | 0.615 | janus kinase and microtubule interacting protein 2 |
| [[LINC00993]] | 0.612 | long independently transcribed non-coding RNA 993 |
| [[IHO1]] | 0.612 | interactor of HORMAD1 1 |
| [[CCDC102B]] | 0.605 | coiled-coil domain containing 102B |
| [[LINC02211]] | 0.604 | long independently transcribed non-coding RNA 2211 |
| [[COX7B2]] | 0.604 | cytochrome c oxidase subunit 7B2 |
| [[LINC02055]] | 0.600 | long independently transcribed non-coding RNA 2055 |
| [[ZNF208]] | 0.595 | zinc finger protein 208 |
| [[LINC02882]] | 0.587 | long independently transcribed non-coding RNA 2882 |
| [[FGF14]] | 0.587 | fibroblast growth factor 14 |
| [[MIR646HG]] | 0.582 | MIR646 host gene |
| [[LINC01098]] | 0.578 | long independently transcribed non-coding RNA 1098 |
| [[MEF2C-AS1]] | 0.569 | MEF2C antisense RNA 1 |
| [[ZNF883]] | 0.567 | zinc finger protein 883 |
| [[NOL4]] | 0.558 | nucleolar protein 4 |
| [[ANKRD30A]] | 0.553 | ankyrin repeat domain 30A |
| [[TENM2]] | 0.528 | teneurin transmembrane protein 2 |
| [[CCNYL2]] | 0.516 | cyclin Y like 2 (pseudogene) |
| [[LINC02899]] | 0.502 | long independently transcribed non-coding RNA 2899 |
| [[FAM106A]] | 0.458 | family with sequence similarity 106 member A |
| [[ADGRG7]] | 0.424 | adhesion G protein-coupled receptor G7 |
| [[TBX18]] | 0.414 | T-box transcription factor 18 |
| [[OR3A2]] | 0.405 | olfactory receptor family 3 subfamily A member 2 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 108; `graph/modules.parquet` — module == 108; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [107] (drug-dose × line)
