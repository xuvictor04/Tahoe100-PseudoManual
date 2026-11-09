---
module: 120
type: "module"
n_genes: 41
n_plus: 41
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.21641333401203156
label: "RHOA GTPase cycle"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 120

*RHOA GTPase cycle · 41 genes (single-armed) · [[Module 120.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

Label from the validation stage: **RHOA GTPase cycle** (reactome, q 0.018; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | RHO GTPase cycle | reactome | 9/41 | 7.80 | 9e-04 |
| + | RHO GTPase cycle | reactome | 9/41 | 7.80 | 9e-04 |
| + | Signaling by Rho GTPases | reactome | 10/41 | 6.05 | 0.002 |
| all | Signaling by Rho GTPases | reactome | 10/41 | 6.05 | 0.002 |
| + | Signaling by Rho GTPases, Miro GTPases and RHOBTB3 | reactome | 10/41 | 5.90 | 0.002 |
| all | Signaling by Rho GTPases, Miro GTPases and RHOBTB3 | reactome | 10/41 | 5.90 | 0.002 |
| all | RHOA GTPase cycle | reactome | 5/41 | 12.7 | 0.018 |
| + | RHOA GTPase cycle | reactome | 5/41 | 12.7 | 0.018 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 119), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Homoharringtonine (drug)]] 5 µM (+6.2, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+4.3, ⚠ cell-cycle shift); [[TAK-901 (drug)]] 5 µM (+3.2, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (+3.2, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+2.9); [[Daptomycin (drug)]] 5 µM (+2.6, ⚠ unreliable plate only); [[Ouabain (Octahydrate) (drug)]] 5 µM (+2.6, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (+2.5, ⚠ cell-cycle shift); [[Peretinoin (drug)]] 5 µM (+2.5); [[Daptomycin (drug)]] 0.5 µM (+2.3, ⚠ unreliable plate only); [[Filgotinib (drug)]] 5 µM (+1.9); [[PH-797804 (drug)]] 5 µM (+1.8); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+1.8); [[Vinblastine (sulfate) (drug)]] 5 µM (+1.6); [[Peretinoin (drug)]] 0.5 µM (+1.5); [[vincristine (drug)]] 0.5 µM (+1.5); [[Busulfan (drug)]] 0.05 µM (+1.4); [[Vinblastine (sulfate) (drug)]] 0.5 µM (+1.4) (43 in all, 18 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Panobinostat (drug)]] 0.5 µM (-4.1, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (-3.7, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (-3.5, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 5 µM (-3.3, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 0.5 µM (-2.8); [[Bortezomib (drug)]] 0.05 µM (-2.7, ⚠ cell-cycle shift); [[c-Kit-IN-1 (drug)]] 0.05 µM (-2.7, ⚠ unreliable plate only); [[Ponatinib (drug)]] 5 µM (-2.5); [[Pitavastatin (Calcium) (drug)]] 5 µM (-2.4, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (-2.3, ⚠ cell-cycle shift); [[Pitavastatin (Calcium) (drug)]] 0.5 µM (-2.1); [[Abemaciclib (drug)]] 5 µM (-2.0); [[venetoclax (drug)]] 5 µM (-1.8); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM (-1.7); [[TAK-733 (drug)]] 5 µM (-1.7); [[GSK1059615 (drug)]] 5 µM (-1.6); [[Trametinib (drug)]] 0.5 µM (-1.5); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (-1.4) (44 in all, 16 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[MIA PaCa-2 (line)]], [[NCI-H23 (line)]], [[HepG2_C3A (line)]], [[SW480 (line)]], [[HT-29 (line)]], [[A-427 (line)]], [[LOX-IMVI (line)]], [[C32 (line)]]

## + arm (41)

| Gene | Projection | Name |
|---|---|---|
| [[DDAH1]] | 0.849 | dimethylarginine dimethylaminohydrolase 1 |
| [[SRGAP1]] | 0.846 | SLIT-ROBO Rho GTPase activating protein 1 |
| [[CCN1]] | 0.827 | cellular communication network factor 1 |
| [[CCN2]] | 0.765 | cellular communication network factor 2 |
| [[DLC1]] | 0.740 | DLC1 Rho GTPase activating protein |
| [[ENC1]] | 0.723 | ectodermal-neural cortex 1 |
| [[CRIM1]] | 0.710 | cysteine rich transmembrane BMP regulator 1 |
| [[SFTA1P]] | 0.710 | surfactant associated 1, lncRNA |
| [[STARD13]] | 0.706 | StAR related lipid transfer domain containing 13 |
| [[FJX1]] | 0.703 | four-jointed box kinase 1 |
| [[ARHGEF28]] | 0.678 | Rho guanine nucleotide exchange factor 28 |
| [[SMURF2]] | 0.663 | SMAD specific E3 ubiquitin protein ligase 2 |
| [[IGF2BP2]] | 0.648 | insulin like growth factor 2 mRNA binding protein 2 |
| [[ANKRD1]] | 0.647 | ankyrin repeat domain 1 |
| [[RASAL2]] | 0.647 | RAS protein activator like 2 |
| [[NCEH1]] | 0.640 | neutral cholesterol ester hydrolase 1 |
| [[SH3RF1]] | 0.639 | SH3 domain containing ring finger 1 |
| [[LINC00707]] | 0.630 | — |
| [[CTNNAL1]] | 0.629 | catenin alpha like 1 |
| [[PRKG1-AS1]] | 0.623 | PRKG1 antisense RNA 1 |
| [[DKK1]] | 0.591 | dickkopf Wnt signaling pathway inhibitor 1 |
| [[ABL2]] | 0.587 | ABL proto-oncogene 2, non-receptor tyrosine kinase |
| [[RBMS2]] | 0.572 | RNA binding motif single stranded interacting protein 2 |
| [[NEDD4L]] | 0.571 | NEDD4 like E3 ubiquitin protein ligase |
| [[DAW1]] | 0.563 | dynein assembly factor with WD repeats 1 |
| [[GPR39]] | 0.552 | G protein-coupled receptor 39 |
| [[AMIGO2]] | 0.547 | adhesion molecule with Ig like domain 2 |
| [[VGLL3]] | 0.518 | vestigial like family member 3 |
| [[MYL12B]] | 0.514 | myosin light chain 12B |
| [[ARHGAP18]] | 0.514 | Rho GTPase activating protein 18 |
| [[SERTAD4]] | 0.487 | SERTA domain containing 4 |
| [[PCED1B]] | 0.477 | PC-esterase domain containing 1B |
| [[PTPN14]] | 0.454 | protein tyrosine phosphatase non-receptor type 14 |
| [[S1PR3]] | 0.443 | sphingosine-1-phosphate receptor 3 |
| [[GREB1L]] | 0.438 | GREB1 like retinoic acid receptor coactivator |
| [[LY6K]] | 0.408 | lymphocyte antigen 6 family member K |
| [[CD109]] | -0.396 | CD109 molecule |
| [[KIF23-AS1]] | 0.366 | KIF23 and PAQR5 antisense RNA 1 |
| [[RIN2]] | 0.331 | Ras and Rab interactor 2 |
| [[RAB38]] | 0.199 | RAB38, member RAS oncogene family |
| [[USP32]] | 0.164 | ubiquitin specific peptidase 32 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 120; `graph/modules.parquet` — module == 120; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [119] (drug-dose × line)
