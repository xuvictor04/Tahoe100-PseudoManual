---
module: 107
type: "module"
n_genes: 44
n_plus: 44
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.1638219803571701
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 107

*44 genes (single-armed) · [[Module 107.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.16; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 106), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM (+6.1, ⚠ cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 5 µM (+4.5, ⚠ toxic; cell-cycle shift); [[Selinexor (drug)]] 5 µM (+4.2, ⚠ cell-cycle shift); [[TAK-901 (drug)]] 5 µM (+4.0, ⚠ cell-cycle shift); [[PH-797804 (drug)]] 5 µM (+3.4); [[Ixazomib citrate (drug)]] 5 µM (+2.8, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (+2.6, ⚠ cell-cycle shift); [[Bortezomib (drug)]] 0.05 µM (+2.6, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (+2.5, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+2.3, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 0.5 µM (+1.9); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+1.4); [[Ponatinib (drug)]] 5 µM (+1.4); [[Homoharringtonine (drug)]] 0.05 µM (+1.3); [[venetoclax (drug)]] 5 µM (+1.2); [[TAK-901 (drug)]] 0.05 µM (+1.1) (27 in all, 20 with an alert ⚠; shown: the 10 strongest and the 6 next strongest without an alert)
- Lower it: [[Dinaciclib (drug)]] 0.5 µM (-3.6, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (-2.6, ⚠ toxic; transcription drop; cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (-2.4); [[Digitoxin (drug)]] 5 µM (-2.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (-1.9, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-1.8, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (-1.7, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (-1.2, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (-1.1, ⚠ toxic; transcription drop; cell-cycle shift) (9 in all, 8 with an alert ⚠)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SW480 (line)]], [[RKO (line)]], [[PANC-1 (line)]], [[A-427 (line)]], [[KATO III (line)]], [[HEC-1-A (line)]], [[LoVo (line)]], [[C-33 A (line)]]

## + arm (44)

| Gene | Projection | Name |
|---|---|---|
| [[SLC25A38]] | 0.793 | solute carrier family 25 member 38 |
| [[LRRC47]] | 0.766 | leucine rich repeat containing 47 |
| [[BRMS1]] | 0.755 | BRMS1 transcriptional repressor and anoikis regulator |
| [[FASTKD3]] | 0.744 | FASTK mitochondrial RNA regulator 3 |
| [[ZNF343]] | 0.735 | zinc finger protein 343 |
| [[ZNF777]] | 0.731 | zinc finger protein 777 |
| [[ZNF2]] | 0.718 | zinc finger protein 2 |
| [[TFIP11]] | 0.718 | tuftelin interacting protein 11 |
| [[TADA2B]] | 0.701 | transcriptional adaptor 2B |
| [[ZNF16]] | 0.699 | zinc finger protein 16 |
| [[COASY]] | 0.691 | Coenzyme A synthase |
| [[PTPN23]] | 0.672 | protein tyrosine phosphatase non-receptor type 23 |
| [[UCK1]] | 0.663 | uridine-cytidine kinase 1 |
| [[ZNF581]] | 0.655 | zinc finger protein 581 |
| [[XAB2]] | 0.651 | XPA binding protein 2 |
| [[SF3A2]] | 0.642 | splicing factor 3a subunit 2 |
| [[ESS2]] | 0.639 | ess-2 spliceosome associated protein |
| [[LYSMD1]] | 0.633 | LysM domain containing 1 |
| [[TEX264]] | 0.618 | testis expressed 264, ER-phagy receptor |
| [[METTL13]] | 0.609 | methyltransferase 13, eEF1A N-terminus and K55 |
| [[PEX16]] | 0.594 | peroxisomal biogenesis factor 16 |
| [[RNF8]] | 0.593 | ring finger protein 8 |
| [[ZNF708]] | 0.592 | zinc finger protein 708 |
| [[WDR83]] | 0.590 | WD repeat domain 83 |
| [[SUPV3L1]] | 0.588 | Suv3 like RNA helicase |
| [[ZNF266]] | 0.585 | zinc finger protein 266 |
| [[PEAK1]] | -0.584 | pseudopodium enriched atypical kinase 1 |
| [[WDR24]] | 0.574 | WD repeat domain 24 |
| [[ZNF282]] | 0.574 | zinc finger protein 282 |
| [[KANSL2]] | 0.570 | KAT8 regulatory NSL complex subunit 2 |
| [[DBR1]] | 0.568 | debranching RNA lariats 1 |
| [[CCT6P1]] | 0.557 | chaperonin containing TCP1 family member 6A2, pseudogene |
| [[TRMT2A]] | 0.557 | tRNA methyltransferase 2A |
| [[PPP1R8]] | 0.549 | protein phosphatase 1 regulatory subunit 8 |
| [[OGFOD2]] | 0.537 | 2-oxoglutarate and iron dependent oxygenase domain containing 2 |
| [[ELOA]] | 0.499 | elongin A |
| [[STBD1]] | 0.470 | starch binding domain 1 |
| [[ZNF398]] | 0.460 | zinc finger protein 398 |
| [[AARS2]] | 0.458 | alanyl-tRNA synthetase 2, mitochondrial |
| [[PGAP4]] | 0.371 | post-GPI attachment to proteins GalNAc transferase 4 |
| [[ZNF786]] | 0.345 | zinc finger protein 786 |
| [[EPB41L5]] | -0.338 | erythrocyte membrane protein band 4.1 like 5 |
| [[ZNF280C]] | -0.270 | zinc finger protein 280C |
| [[THEM4]] | -0.0422 | thioesterase superfamily member 4 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 107; `graph/modules.parquet` — module == 107; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [106] (drug-dose × line)
