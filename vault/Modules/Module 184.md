---
module: 184
type: "module"
n_genes: 20
n_plus: 13
n_minus: 7
arms_opposite: true
mean_cos_between_arms: -0.38961485028266907
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 184

*20 genes (13 in the + arm, 7 in the − arm) · [[Module 184.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.39). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 183), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Panobinostat (drug)]] 0.5 µM (+19.4, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (+19.4, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (+17.4, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (+11.4, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+9.2); [[Belinostat (drug)]] 0.5 µM (+7.7, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+7.2, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (+7.1); [[Tucidinostat (drug)]] 0.5 µM (+5.5, ⚠ cell-cycle shift); [[Daptomycin (drug)]] 5 µM (+5.3, ⚠ unreliable plate only); [[Brivudine (drug)]] 5 µM (+5.0); [[Peretinoin (drug)]] 5 µM (+4.8); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+4.0); [[Vinblastine (sulfate) (drug)]] 5 µM (+4.0); [[vincristine (drug)]] 0.5 µM (+3.4); [[Peretinoin (drug)]] 0.5 µM (+3.3); [[Vinblastine (sulfate) (drug)]] 0.5 µM (+3.2); [[PF-06260933 (drug)]] 5 µM (+3.1) (100 in all, 29 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[TAK-901 (drug)]] 5 µM (-10.2, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (-9.9, ⚠ cell-cycle shift); [[PH-797804 (drug)]] 5 µM (-7.0); [[Ouabain (Octahydrate) (drug)]] 5 µM (-6.0, ⚠ cell-cycle shift); [[Selinexor (drug)]] 5 µM (-4.8, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (-4.4, ⚠ toxic; transcription drop; cell-cycle shift); [[Niclosamide (olamine) (drug)]] 5 µM (-4.0, ⚠ toxic; cell-cycle shift); [[NG25 (drug)]] 5 µM (-4.0, ⚠ cell-cycle shift); [[Ponatinib (drug)]] 5 µM (-3.5); [[Harringtonine (drug)]] 5 µM (-3.2, ⚠ cell-cycle shift); [[Cabozantinib (S-malate) (drug)]] 5 µM (-3.1); [[Clobetasol propionate (drug)]] 5 µM (-2.8); [[TAK-901 (drug)]] 0.05 µM (-2.7); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (-2.7); [[GSK1059615 (drug)]] 5 µM (-2.3); [[Ponatinib (drug)]] 0.5 µM (-2.2); [[Budesonide (drug)]] 0.05 µM (-2.0); [[Binimetinib (drug)]] 0.05 µM (-2.0) (97 in all, 22 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SW480 (line)]], [[PANC-1 (line)]], [[NCI-H460 (line)]], [[KATO III (line)]], [[SW1417 (line)]], [[LoVo (line)]], [[HEC-1-A (line)]], [[SW 900 (line)]]

## + arm (13)

| Gene | Projection | Name |
|---|---|---|
| [[SH3BGRL3]] | 0.808 | SH3 domain binding glutamate rich protein like 3 |
| [[ELOVL1]] | 0.795 | ELOVL fatty acid elongase 1 |
| [[RHOC]] | 0.760 | ras homolog family member C |
| [[EHD4]] | 0.747 | EH domain containing 4 |
| [[ORMDL2]] | 0.724 | ORMDL sphingolipid biosynthesis regulator 2 |
| [[UCHL3]] | 0.694 | ubiquitin C-terminal hydrolase L3 |
| [[KCTD5]] | 0.646 | potassium channel tetramerization domain containing 5 |
| [[RELL2]] | 0.635 | RELT like 2 |
| [[DYNLT1]] | 0.593 | dynein light chain Tctex-type 1 |
| [[KDM7A]] | 0.568 | lysine demethylase 7A |
| [[ARHGAP29]] | 0.509 | Rho GTPase activating protein 29 |
| [[PLCXD2]] | 0.506 | phosphatidylinositol specific phospholipase C X domain containing 2 |
| [[ZFAND6]] | 0.471 | zinc finger AN1-type containing 6 |

## − arm (7)

| Gene | Projection | Name |
|---|---|---|
| [[RPRD2]] | -0.755 | regulation of nuclear pre-mRNA domain containing 2 |
| [[SAFB]] | -0.724 | scaffold attachment factor B |
| [[LUC7L2]] | -0.723 | LUC7 like 2, pre-mRNA splicing factor |
| [[PRPF4B]] | -0.671 | pre-mRNA processing factor kinase PRP4K |
| [[NHLRC3]] | -0.612 | NHL repeat containing 3 |
| [[HDGF]] | -0.577 | heparin binding growth factor |
| [[SRRM1]] | -0.568 | serine and arginine repetitive matrix 1 |

## Data

- `graph/nodes.parquet` — module == 184; `graph/modules.parquet` — module == 184; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [183] (drug-dose × line)
