---
module: 136
type: "module"
n_genes: 35
n_plus: 35
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.3196212351322174
label: "heme metabolism"
label_source: "hallmark"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 136

*heme metabolism · 35 genes (single-armed) · [[Module 136.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

Label from the validation stage: **heme metabolism** (hallmark, q 0.017; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | heme metabolism | hallmark | 5/35 | 12.8 | 0.017 |
| + | heme metabolism | hallmark | 5/35 | 12.8 | 0.017 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 135), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Tucidinostat (drug)]] 5 µM (+3.8); [[Panobinostat (drug)]] 5 µM (+3.0, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (+3.0, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (+3.0, ⚠ cell-cycle shift); [[Pitavastatin (Calcium) (drug)]] 0.5 µM (+2.9); [[Tucidinostat (drug)]] 0.5 µM (+2.6, ⚠ cell-cycle shift); [[Pitavastatin (Calcium) (drug)]] 5 µM (+2.5, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (+2.3, ⚠ cell-cycle shift); [[PF-06260933 (drug)]] 5 µM (+2.1); [[Daptomycin (drug)]] 5 µM (+1.8, ⚠ unreliable plate only); [[Peretinoin (drug)]] 5 µM (+1.3); [[Vinblastine (sulfate) (drug)]] 5 µM (+1.3); [[Auranofin (drug)]] 5 µM (+1.3); [[Ipatasertib (drug)]] 0.5 µM (+1.3); [[Neratinib (drug)]] 5 µM (+1.1) (18 in all, 10 with an alert ⚠; shown: the 10 strongest and the 5 next strongest without an alert)
- Lower it: [[Homoharringtonine (drug)]] 5 µM (-11.5, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-8.5, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-8.1, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (-5.9, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-5.2, ⚠ cell-cycle shift); [[Selinexor (drug)]] 5 µM (-5.1, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (-4.8, ⚠ cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 5 µM (-4.4, ⚠ toxic; cell-cycle shift); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (-4.0, ⚠ cell-cycle shift); [[TAK-901 (drug)]] 5 µM (-4.0, ⚠ cell-cycle shift); [[Trametinib (drug)]] 0.5 µM (-2.8); [[PH-797804 (drug)]] 5 µM (-2.7); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (-2.6); [[Homoharringtonine (drug)]] 0.05 µM (-2.5); [[Binimetinib (drug)]] 0.5 µM (-2.5); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM (-2.4); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (-2.2); [[Elimusertib hydrochloride (drug)]] 0.05 µM (-2.2); [[Ponatinib (drug)]] 5 µM (-2.2); [[Cobimetinib (drug)]] 5 µM (-2.2) (57 in all, 28 with an alert ⚠; shown: the 10 strongest and the 10 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[A-172 (line)]], [[A549 (line)]], [[HS-578T (line)]], [[NCI-H1792 (line)]], [[PANC-1 (line)]], [[C32 (line)]], [[NCI-H460 (line)]], [[RPMI-7951 (line)]]

## + arm (35)

| Gene | Projection | Name |
|---|---|---|
| [[ARID3B]] | 0.854 | AT-rich interaction domain 3B |
| [[MYO9B]] | 0.835 | myosin IXB |
| [[CSNK1E]] | 0.827 | casein kinase 1 epsilon |
| [[TMEM184B]] | 0.812 | transmembrane protein 184B |
| [[ZFYVE28]] | 0.792 | zinc finger FYVE-type containing 28 |
| [[FLNB]] | 0.779 | filamin B |
| [[LRRFIP1]] | 0.773 | LRR binding FLII interacting protein 1 |
| [[EHBP1L1]] | 0.772 | EH domain binding protein 1 like 1 |
| [[FLNB-AS1]] | 0.744 | FLNB antisense RNA 1 |
| [[PAQR5]] | 0.743 | progestin and adipoQ receptor family member 5 |
| [[STXBP1]] | 0.700 | syntaxin binding protein 1 |
| [[FAM131A]] | 0.691 | family with sequence similarity 131 member A |
| [[BMERB1]] | 0.673 | bMERB domain containing 1 |
| [[MEIS3]] | 0.656 | Meis homeobox 3 |
| [[RTN4]] | 0.655 | reticulon 4 |
| [[MARK3]] | 0.645 | microtubule affinity regulating kinase 3 |
| [[INPP5A]] | 0.631 | inositol polyphosphate-5-phosphatase A |
| [[TRIOBP]] | 0.629 | TRIO and F-actin binding protein |
| [[ZCCHC24]] | 0.626 | zinc finger CCHC-type containing 24 |
| [[ARPC1B]] | 0.618 | actin related protein 2/3 complex subunit 1B |
| [[MARCHF2]] | 0.614 | membrane associated ring-CH-type finger 2 |
| [[GPAT3]] | 0.607 | glycerol-3-phosphate acyltransferase 3 |
| [[MFSD10]] | 0.603 | solute carrier family 75 member 1 |
| [[PC]] | 0.595 | pyruvate carboxylase |
| [[SH3KBP1]] | 0.580 | SH3 domain containing kinase binding protein 1 |
| [[SMOX]] | 0.577 | spermine oxidase |
| [[KCTD20]] | 0.568 | potassium channel tetramerization domain containing 20 |
| [[EPOR]] | 0.567 | erythropoietin receptor |
| [[EFEMP2]] | 0.544 | EGF-like fibulin extracellular matrix protein 2 |
| [[PLCXD1]] | 0.532 | phosphatidylinositol specific phospholipase C X domain containing 1 |
| [[NAPEPLD]] | -0.518 | N-acyl phosphatidylethanolamine phospholipase D |
| [[OBSCN]] | 0.459 | obscurin, cytoskeletal calmodulin and titin-interacting RhoGEF |
| [[MAP1B]] | 0.393 | microtubule associated protein 1B |
| [[FAM85B]] | 0.375 | family with sequence similarity 85 member B |
| [[KRT81]] | 0.369 | keratin 81 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 136; `graph/modules.parquet` — module == 136; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [135] (drug-dose × line)
