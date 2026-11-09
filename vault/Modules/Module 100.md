---
module: 100
type: "module"
n_genes: 46
n_plus: 46
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 100

*46 genes (single-armed) · [[Module 100.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | Signaling by LRP5 mutants | reactome | 2/46 | 131 | 0.034 |
| + | Signaling by LRP5 mutants | reactome | 2/46 | 131 | 0.034 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 99), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Tucidinostat (drug)]] 5 µM (+10.8); [[Panobinostat (drug)]] 5 µM (+9.1, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (+8.7, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+8.4, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (+7.9, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (+7.8, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (+7.7, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+6.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Belinostat (drug)]] 0.5 µM (+4.9, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+4.7, ⚠ toxic; transcription drop; cell-cycle shift); [[Brivudine (drug)]] 5 µM (+4.4); [[Tucidinostat (drug)]] 0.05 µM (+2.7); [[Ipatasertib (drug)]] 0.5 µM (+2.2); [[Brivudine (drug)]] 0.5 µM (+2.1); [[Ponatinib (drug)]] 5 µM (+1.8); [[Radotinib (drug)]] 5 µM (+1.6); [[Ponatinib (drug)]] 0.5 µM (+1.6); [[Auranofin (drug)]] 5 µM (+1.5); [[XRK3F2 (drug)]] 0.5 µM (+1.5) (40 in all, 15 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)
- Lower it: [[Homoharringtonine (drug)]] 0.5 µM (-5.4, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (-4.8, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-4.5, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (-4.3, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (-3.6, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-3.2, ⚠ cell-cycle shift); [[TAK-901 (drug)]] 5 µM (-2.8, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.05 µM (-2.8); [[Digitoxin (drug)]] 0.05 µM (-2.8, ⚠ cell-cycle shift); [[c-Kit-IN-1 (drug)]] 0.05 µM (-2.7, ⚠ unreliable plate only); [[PH-797804 (drug)]] 5 µM (-2.3); [[5-Azacytidine (drug)]] 5 µM (-1.9); [[Belumosudil (drug)]] 5 µM (-1.7); [[TAK-733 (drug)]] 5 µM (-1.4); [[Sapanisertib (drug)]] 5 µM (-1.3); [[Artesunate (drug)]] 0.5 µM (-1.3); [[Ixazomib citrate (drug)]] 0.5 µM (-1.3); [[Abemaciclib (drug)]] 5 µM (-1.3); [[Mebendazole (drug)]] 5 µM (-1.3) (31 in all, 12 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[PANC-1 (line)]], [[NCI-H460 (line)]], [[SW480 (line)]], [[LS 180 (line)]], [[NCI-H1573 (line)]], [[HOP62 (line)]], [[KATO III (line)]], [[CFPAC-1 (line)]]

## + arm (46)

| Gene | Projection | Name |
|---|---|---|
| [[SLC29A4]] | 0.781 | solute carrier family 29 member 4 |
| [[NRTN]] | 0.779 | neurturin |
| [[MAST1]] | 0.779 | microtubule associated serine/threonine kinase 1 |
| [[SEMA6B]] | 0.774 | semaphorin 6B |
| [[FOXO6]] | 0.757 | forkhead box O6 |
| [[PDZD7]] | 0.727 | PDZ domain containing 7 |
| [[ADGRB2]] | 0.719 | adhesion G protein-coupled receptor B2 |
| [[ITGA7]] | 0.716 | integrin subunit alpha 7 |
| [[CCDC88B]] | 0.702 | coiled-coil and HOOK domain protein 88B |
| [[KNDC1]] | 0.698 | kinase non-catalytic C-lobe domain containing 1 |
| [[TMCC2]] | 0.693 | transmembrane and coiled-coil domain family 2 |
| [[RPS6KA1]] | 0.691 | ribosomal protein S6 kinase A1 |
| [[CIB2]] | 0.689 | calcium and integrin binding family member 2 |
| [[SMARCD3]] | 0.680 | SWI/SNF related BAF chromatin remodeling complex subunit D3 |
| [[SPTBN4]] | 0.668 | spectrin beta, non-erythrocytic 4 |
| [[MAPT]] | 0.667 | microtubule associated protein tau |
| [[TMEM266]] | 0.665 | transmembrane protein 266 |
| [[NOL4L]] | 0.660 | nucleolar protein 4 like |
| [[ELL3]] | 0.657 | elongation factor for RNA polymerase II 3 |
| [[TLE2]] | 0.656 | TLE family member 2, transcriptional corepressor |
| [[ADGRL1]] | 0.650 | adhesion G protein-coupled receptor L1 |
| [[SYNGR1]] | 0.650 | synaptogyrin 1 |
| [[REEP2]] | 0.646 | receptor accessory protein 2 |
| [[IGSF3]] | 0.641 | immunoglobulin superfamily member 3 |
| [[ANO8]] | 0.620 | anoctamin 8 |
| [[KANK3]] | 0.616 | KN motif and ankyrin repeat domains 3 |
| [[CELF5]] | 0.613 | CUGBP Elav-like family member 5 |
| [[FADS3]] | 0.607 | fatty acid desaturase 3 |
| [[CASZ1]] | 0.583 | castor zinc finger 1 |
| [[EFHD1]] | 0.566 | EF-hand domain family member D1 |
| [[KREMEN1]] | 0.560 | kringle containing transmembrane protein 1 |
| [[KREMEN2]] | 0.560 | kringle containing transmembrane protein 2 |
| [[HIP1]] | 0.555 | huntingtin interacting protein 1 |
| [[PDE4A]] | 0.555 | phosphodiesterase 4A |
| [[PADI2]] | 0.547 | peptidyl arginine deiminase 2 |
| [[CD276]] | 0.492 | CD276 molecule |
| [[ZMIZ1-AS1]] | 0.470 | ZMIZ1 antisense RNA 1 |
| [[DNAI1]] | 0.456 | dynein axonemal intermediate chain 1 |
| [[PREX1]] | 0.453 | phosphatidylinositol-3,4,5-trisphosphate dependent Rac exchange factor 1 |
| [[ESPN]] | 0.447 | espin |
| [[GRTP1]] | 0.442 | growth hormone regulated TBC protein 1 |
| [[LGI4]] | 0.433 | leucine rich repeat LGI family member 4 |
| [[TSPAN14]] | 0.429 | tetraspanin 14 |
| [[FBLN2]] | 0.398 | fibulin 2 |
| [[TEAD3]] | 0.367 | TEA domain transcription factor 3 |
| [[INHBB]] | 0.261 | inhibin subunit beta B |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 100; `graph/modules.parquet` — module == 100; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [99] (drug-dose × line)
