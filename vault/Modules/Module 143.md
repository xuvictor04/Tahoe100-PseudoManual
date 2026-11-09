---
module: 143
type: "module"
n_genes: 32
n_plus: 32
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.3131271302700043
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 143

*32 genes (single-armed) · [[Module 143.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 142), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Homoharringtonine (drug)]] 5 µM (+6.7, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (+4.3, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+4.2, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (+2.9, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+2.8); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (+2.6, ⚠ cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+2.4); [[Digitoxin (drug)]] 0.5 µM (+2.4, ⚠ cell-cycle shift); [[Niclosamide (olamine) (drug)]] 5 µM (+2.1, ⚠ toxic; cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (+2.1, ⚠ cell-cycle shift); [[Cobimetinib (drug)]] 5 µM (+2.0); [[TAK-901 (drug)]] 0.05 µM (+2.0); [[Belumosudil (drug)]] 5 µM (+1.9); [[Bimiralisib (drug)]] 5 µM (+1.8); [[Trametinib (drug)]] 0.05 µM (+1.7); [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM (+1.6); [[XRK3F2 (drug)]] 5 µM (+1.6); [[Brimonidine (drug)]] 5 µM (+1.6) (80 in all, 20 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Panobinostat (drug)]] 0.5 µM (-7.3, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (-6.5, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (-5.3, ⚠ cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 5 µM (-2.6, ⚠ toxic; cell-cycle shift); [[Docetaxel (drug)]] 0.05 µM (-2.5, ⚠ transcription drop; cell-cycle shift); [[Abemaciclib (drug)]] 5 µM (-1.9); [[Ixazomib citrate (drug)]] 0.5 µM (-1.9); [[Auranofin (drug)]] 5 µM (-1.8); [[Sapanisertib (drug)]] 0.5 µM (-1.7); [[Ipatasertib (drug)]] 0.5 µM (-1.7); [[Docetaxel (Trihydrate) (drug)]] 0.5 µM (-1.6); [[Mebendazole (drug)]] 5 µM (-1.6); [[Abemaciclib (drug)]] 0.5 µM (-1.6); [[Vilanterol (drug)]] 5 µM (-1.5); [[Methylprednisolone succinate (drug)]] 0.5 µM (-1.5) (46 in all, 12 with an alert ⚠; shown: the 10 strongest and the 5 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SW480 (line)]], [[NCI-H2347 (line)]], [[HEC-1-A (line)]], [[Panc 03.27 (line)]], [[A498 (line)]], [[HT-29 (line)]], [[SNU-423 (line)]], [[KATO III (line)]]

## + arm (32)

| Gene | Projection | Name |
|---|---|---|
| [[TCF12]] | 0.818 | transcription factor 12 |
| [[PARD3B]] | 0.799 | par-3 family cell polarity regulator beta |
| [[ATE1]] | 0.775 | arginyltransferase 1 |
| [[ADGRA3]] | 0.765 | adhesion G protein-coupled receptor A3 |
| [[ARAP2]] | 0.759 | ArfGAP with RhoGAP domain, ankyrin repeat and PH domain 2 |
| [[NFIB]] | 0.757 | nuclear factor I B |
| [[PTPRK]] | 0.752 | protein tyrosine phosphatase receptor type K |
| [[SLC25A13]] | 0.733 | solute carrier family 25 member 13 |
| [[USP13]] | 0.714 | ubiquitin specific peptidase 13 |
| [[TULP4]] | 0.700 | TUB like protein 4 |
| [[PSPC1]] | 0.693 | paraspeckle component 1 |
| [[JADE3]] | 0.672 | jade family PHD finger 3 |
| [[FOXP1]] | 0.668 | forkhead box P1 |
| [[ATF7IP]] | 0.662 | activating transcription factor 7 interacting protein |
| [[CACHD1]] | 0.648 | cache domain containing 1 |
| [[TTC39C]] | 0.640 | tetratricopeptide repeat domain 39C |
| [[ATXN7L1]] | 0.628 | ataxin 7 like 1 |
| [[SH3D19]] | 0.623 | SH3 domain containing 19 |
| [[REEP3]] | 0.622 | receptor accessory protein 3 |
| [[ZNF704]] | 0.618 | zinc finger protein 704 |
| [[PPM1L]] | 0.610 | protein phosphatase, Mg2+/Mn2+ dependent 1L |
| [[PLXNB3]] | -0.570 | plexin B3 |
| [[ERBIN]] | 0.570 | erbb2 interacting protein |
| [[WWC3]] | 0.551 | WWC family member 3 |
| [[ZNF17]] | -0.508 | zinc finger protein 17 |
| [[ITGB8]] | 0.482 | integrin subunit beta 8 |
| [[WWC2]] | 0.472 | WW and C2 domain containing 2 |
| [[MAN1A2]] | 0.464 | mannosidase alpha class 1A member 2 |
| [[MDFIC]] | 0.452 | MyoD family inhibitor domain containing |
| [[SGMS1]] | 0.444 | sphingomyelin synthase 1 |
| [[RIMKLB]] | 0.406 | ribosomal modification protein rimK like family member B |
| [[LRATD2]] | 0.379 | LRAT domain containing 2 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 143; `graph/modules.parquet` — module == 143; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [142] (drug-dose × line)
