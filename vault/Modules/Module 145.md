---
module: 145
type: "module"
n_genes: 31
n_plus: 31
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.20713500678539276
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 145

*31 genes (single-armed) · [[Module 145.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.21; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 144), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM (+6.3, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (+4.2, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (+4.2, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (+3.8, ⚠ cell-cycle shift); [[Belinostat (drug)]] 0.5 µM (+3.0, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (+2.4, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (+2.1, ⚠ cell-cycle shift); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (+2.1, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (+2.0, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (+1.8, ⚠ toxic; transcription drop; cell-cycle shift); [[Brivudine (drug)]] 5 µM (+1.7); [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM (+1.5); [[HI-TOPK-032 (drug)]] 5 µM (+1.4); [[ULK-101 (drug)]] 0.05 µM (+1.4); [[Temsirolimus (drug)]] 0.5 µM (+1.3); [[Rapamycin (drug)]] 5 µM (+1.3); [[Ipatasertib (drug)]] 0.5 µM (+1.2); [[Bimiralisib (drug)]] 5 µM (+1.2); [[RMC-6236 (drug)]] 5 µM (+1.2); [[Pitavastatin (Calcium) (drug)]] 0.5 µM (+1.1) (26 in all, 13 with an alert ⚠; shown: the 10 strongest and the 10 next strongest without an alert)
- Lower it: [[c-Kit-IN-1 (drug)]] 0.05 µM (-11.9, ⚠ unreliable plate only); [[TAK-733 (drug)]] 5 µM (-6.5); [[Dinaciclib (drug)]] 5 µM (-6.1, ⚠ toxic; transcription drop; cell-cycle shift); [[EX229 (drug)]] 5 µM (-6.0); [[Abemaciclib (drug)]] 5 µM (-6.0); [[c-Kit-IN-1 (drug)]] 5 µM (-5.8); [[Dinaciclib (drug)]] 0.05 µM (-5.5, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (-5.1, ⚠ toxic; transcription drop; cell-cycle shift); [[venetoclax (drug)]] 5 µM (-5.1); [[Homoharringtonine (drug)]] 0.5 µM (-4.3, ⚠ cell-cycle shift); [[Abemaciclib (drug)]] 0.5 µM (-3.8); [[EX229 (drug)]] 0.05 µM (-3.8); [[EX229 (drug)]] 0.5 µM (-3.2); [[Belzutifan (drug)]] 5 µM (-3.1); [[Sapanisertib (drug)]] 0.5 µM (-2.4) (34 in all, 14 with an alert ⚠; shown: the 10 strongest and the 5 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[MIA PaCa-2 (line)]], [[SW1417 (line)]], [[SW480 (line)]], [[HT-29 (line)]], [[A498 (line)]], [[NCI-H460 (line)]], [[KATO III (line)]], [[LoVo (line)]]

## + arm (31)

| Gene | Projection | Name |
|---|---|---|
| [[FBXL20]] | 0.862 | F-box and leucine rich repeat protein 20 |
| [[MAP3K3]] | 0.839 | mitogen-activated protein kinase kinase kinase 3 |
| [[ZER1]] | 0.781 | zyg-11 related cell cycle regulator |
| [[HAGH]] | 0.777 | hydroxyacylglutathione hydrolase |
| [[MXD4]] | 0.776 | MAX dimerization protein 4 |
| [[ULK1]] | 0.773 | unc-51 like autophagy activating kinase 1 |
| [[MOB2]] | 0.760 | MOB kinase activator 2 |
| [[TMEM50A]] | 0.757 | transmembrane protein 50A |
| [[GATAD2B]] | 0.747 | GATA zinc finger domain containing 2B |
| [[SAP30L]] | 0.729 | SAP30 like |
| [[PINK1]] | 0.711 | PTEN induced kinase 1 |
| [[CRAMP1]] | 0.706 | cramped chromatin regulator 1 |
| [[WDTC1]] | 0.661 | WD and tetratricopeptide repeats 1 |
| [[CASTOR2]] | 0.637 | cytosolic arginine sensor for mTORC1 subunit 2 |
| [[ZNRF2]] | 0.616 | zinc and ring finger 2 |
| [[PPM1B]] | 0.614 | protein phosphatase, Mg2+/Mn2+ dependent 1B |
| [[BRD3]] | 0.613 | bromodomain containing 3 |
| [[OTUD5]] | 0.612 | OTU deubiquitinase 5 |
| [[SRGAP2B]] | 0.605 | SLIT-ROBO Rho GTPase activating protein 2B |
| [[GARRE1]] | 0.600 | granule associated Rac and RHOG effector 1 |
| [[SRGAP2C]] | 0.575 | SLIT-ROBO Rho GTPase activating protein 2C |
| [[UBALD1]] | 0.560 | UBA like domain containing 1 |
| [[DHX8]] | 0.555 | DEAH-box helicase 8 |
| [[RSBN1L]] | 0.509 | round spermatid basic protein 1 like |
| [[PSEN1]] | 0.493 | presenilin 1 |
| [[PHLPP1]] | 0.485 | PH domain and leucine rich repeat protein phosphatase 1 |
| [[PANX2]] | 0.482 | pannexin 2 |
| [[GAB1]] | 0.444 | GRB2 associated binding protein 1 |
| [[KIRREL1]] | -0.371 | kirre like nephrin family adhesion molecule 1 |
| [[KDM5C]] | 0.201 | lysine demethylase 5C |
| [[NR1H2]] | 0.193 | nuclear receptor subfamily 1 group H member 2 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 145; `graph/modules.parquet` — module == 145; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [144] (drug-dose × line)
