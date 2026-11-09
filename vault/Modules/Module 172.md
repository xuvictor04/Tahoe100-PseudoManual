---
module: 172
type: "module"
n_genes: 24
n_plus: 24
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.36299777030944824
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 172

*24 genes (single-armed) · [[Module 172.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 171), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Homoharringtonine (drug)]] 5 µM (+4.5, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (+4.2, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 5 µM (+3.8, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (+3.5, ⚠ cell-cycle shift); [[Bortezomib (drug)]] 0.05 µM (+3.3, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (+2.6, ⚠ toxic; transcription drop; cell-cycle shift); [[Ixazomib citrate (drug)]] 0.5 µM (+2.6); [[Digitoxin (drug)]] 0.5 µM (+2.3, ⚠ cell-cycle shift); [[Rapamycin (drug)]] 5 µM (+2.1); [[Homoharringtonine (drug)]] 0.5 µM (+2.0, ⚠ cell-cycle shift); [[Temsirolimus (drug)]] 5 µM (+1.8); [[5-Azacytidine (drug)]] 5 µM (+1.7); [[Bimiralisib (drug)]] 5 µM (+1.5); [[Temsirolimus (drug)]] 0.05 µM (+1.5); [[ULK-101 (drug)]] 0.05 µM (+1.5); [[Neratinib (maleate) (drug)]] 5 µM (+1.4); [[Bortezomib (drug)]] 0.5 µM (+1.3); [[MK-3903 (drug)]] 5 µM (+1.3) (37 in all, 19 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Dinaciclib (drug)]] 0.5 µM (-5.7, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (-4.6, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (-4.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (-3.4); [[Panobinostat (drug)]] 0.5 µM (-2.9, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (-2.8, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (-2.8, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (-2.4, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (-2.4, ⚠ cell-cycle shift); [[Docetaxel (drug)]] 0.05 µM (-2.3, ⚠ transcription drop; cell-cycle shift); [[Hesperidin (drug)]] 0.05 µM (-1.2); [[Terfenadine (drug)]] 0.5 µM (-1.2); [[HI-TOPK-032 (drug)]] 5 µM (-1.0); [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM (-1.0); [[Fluvoxamine (maleate) (drug)]] 0.5 µM (-1.0) (19 in all, 13 with an alert ⚠; shown: the 10 strongest and the 5 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[NCI-H460 (line)]], [[KATO III (line)]], [[SW480 (line)]], [[NCI-H23 (line)]], [[HT-29 (line)]], [[COLO 205 (line)]], [[RKO (line)]], [[Hs 766T (line)]]

## + arm (24)

| Gene | Projection | Name |
|---|---|---|
| [[SLC38A7]] | 0.855 | solute carrier family 38 member 7 |
| [[PHYKPL]] | 0.789 | 5-phosphohydroxy-L-lysine phospho-lyase |
| [[GPATCH3]] | 0.756 | G-patch domain containing 3 |
| [[GUSBP11]] | 0.753 | GUSB pseudogene 11 |
| [[PPP6R2]] | 0.715 | protein phosphatase 6 regulatory subunit 2 |
| [[PLEKHM2]] | 0.706 | pleckstrin homology and RUN domain containing M2 |
| [[MRPL45P2]] | 0.704 | — |
| [[WDR81]] | 0.699 | WD repeat domain 81 |
| [[NCOA6]] | 0.672 | nuclear receptor coactivator 6 |
| [[EPB41L2]] | -0.655 | erythrocyte membrane protein band 4.1 like 2 |
| [[TBCA]] | 0.648 | tubulin folding cofactor A |
| [[RABEP1]] | 0.642 | rabaptin, RAB GTPase binding effector protein 1 |
| [[ZNF609]] | 0.634 | zinc finger protein 609 |
| [[NCBP3]] | 0.630 | nuclear cap binding subunit 3 |
| [[ARL5B]] | -0.611 | ARF like GTPase 5B |
| [[MAP3K10]] | 0.611 | mitogen-activated protein kinase kinase kinase 10 |
| [[LRSAM1]] | 0.594 | leucine rich repeat and sterile alpha motif containing 1 |
| [[ZNF254]] | 0.574 | zinc finger protein 254 |
| [[PISD]] | 0.536 | phosphatidylserine decarboxylase |
| [[SCAMP4]] | 0.526 | secretory carrier membrane protein 4 |
| [[ERICH1]] | 0.518 | glutamate rich 1 |
| [[PITPNM2]] | 0.482 | phosphatidylinositol transfer protein membrane associated 2 |
| [[WWP2]] | 0.419 | WW domain containing E3 ubiquitin protein ligase 2 |
| [[UBE2W]] | 0.364 | ubiquitin conjugating enzyme E2 W |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 172; `graph/modules.parquet` — module == 172; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [171] (drug-dose × line)
