---
module: 180
type: "module"
n_genes: 22
n_plus: 22
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 180

*22 genes (single-armed) · [[Module 180.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 179), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[PF-06260933 (drug)]] 5 µM (+3.3); [[c-Kit-IN-1 (drug)]] 0.05 µM (+3.0, ⚠ unreliable plate only); [[Artesunate (drug)]] 5 µM (+2.1, ⚠ cell-cycle shift); [[Fumaric acid (drug)]] 5 µM (+1.9); [[Vinblastine (sulfate) (drug)]] 5 µM (+1.9); [[Daptomycin (drug)]] 5 µM (+1.9, ⚠ unreliable plate only); [[Niclosamide (olamine) (drug)]] 0.5 µM (+1.9); [[Abemaciclib (drug)]] 5 µM (+1.8); [[Pitavastatin (Calcium) (drug)]] 0.5 µM (+1.7); [[Pravastatin (sodium) (drug)]] 5 µM (+1.6); [[Abemaciclib (drug)]] 0.5 µM (+1.6); [[Dimethyl fumarate (drug)]] 5 µM (+1.6); [[Sapanisertib (drug)]] 0.5 µM (+1.5) (35 in all, 7 with an alert ⚠; shown: the 10 strongest and the 3 next strongest without an alert)
- Lower it: [[Homoharringtonine (drug)]] 5 µM (-9.2, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-8.4, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (-7.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (-6.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (-6.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Niclosamide (olamine) (drug)]] 5 µM (-6.0, ⚠ toxic; cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-5.6, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (-5.3, ⚠ cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 5 µM (-5.2, ⚠ toxic; cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (-4.5); [[Belumosudil (drug)]] 5 µM (-2.7); [[Clobetasol propionate (drug)]] 0.05 µM (-2.6); [[Retinoic acid (drug)]] 0.05 µM (-2.4); [[Palmatine (chloride) (drug)]] 0.05 µM (-2.0); [[PH-797804 (drug)]] 5 µM (-1.8); [[TAK-901 (drug)]] 0.05 µM (-1.8); [[Berbamine (drug)]] 0.05 µM (-1.8); [[Filgotinib (drug)]] 5 µM (-1.7); [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM (-1.6) (59 in all, 20 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[NCI-H1792 (line)]], [[C32 (line)]], [[LOX-IMVI (line)]], [[SNU-423 (line)]], [[HS-578T (line)]], [[A549 (line)]], [[A-172 (line)]], [[RPMI-7951 (line)]]

## + arm (22)

| Gene | Projection | Name |
|---|---|---|
| [[ENO2]] | 0.869 | enolase 2 |
| [[PPP2R5B]] | 0.830 | protein phosphatase 2 regulatory subunit B'beta |
| [[NGLY1]] | 0.824 | N-glycanase 1 |
| [[NDRG1]] | 0.814 | N-myc downstream regulated 1 |
| [[PPFIA1]] | 0.755 | PPFI scaffold protein A1 |
| [[SMAP1]] | 0.753 | small ArfGAP 1 |
| [[ARFGEF3]] | 0.745 | ARFGEF family member 3 |
| [[RAB11FIP5]] | 0.723 | RAB11 family interacting protein 5 |
| [[SH3D21]] | 0.700 | manchette microtubule inner protein 1 |
| [[NCKIPSD]] | 0.695 | NCK interacting protein with SH3 domain |
| [[GOLGA6L9]] | 0.691 | golgin A6 family like 9 |
| [[PTPRF]] | 0.688 | protein tyrosine phosphatase receptor type F |
| [[CLK3]] | 0.670 | CDC like kinase 3 |
| [[SLC26A6]] | 0.648 | solute carrier family 26 member 6 |
| [[KXD1]] | 0.626 | KxDL motif containing 1 |
| [[QSOX1]] | 0.619 | quiescin sulfhydryl oxidase 1 |
| [[VEGFA]] | 0.617 | vascular endothelial growth factor A |
| [[PIGA]] | 0.594 | phosphatidylinositol glycan anchor biosynthesis class A |
| [[C1GALT1]] | 0.587 | core 1 synthase, glycoprotein-N-acetylgalactosamine 3-beta-galactosyltransferase 1 |
| [[CRYBG3]] | 0.567 | crystallin beta-gamma domain containing 3 |
| [[GAN]] | 0.511 | gigaxonin |
| [[NPPB]] | 0.367 | natriuretic peptide B |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 180; `graph/modules.parquet` — module == 180; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [179] (drug-dose × line)
