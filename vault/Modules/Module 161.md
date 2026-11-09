---
module: 161
type: "module"
n_genes: 26
n_plus: 26
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 161

*26 genes (single-armed) · [[Module 161.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 160), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Panobinostat (drug)]] 5 µM (+9.0, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (+7.9, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (+7.8, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+6.6); [[Panobinostat (drug)]] 0.05 µM (+5.5, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (+4.3, ⚠ cell-cycle shift); [[Belinostat (drug)]] 0.5 µM (+3.8, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (+3.0, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+2.6, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+2.6, ⚠ toxic; transcription drop; cell-cycle shift); [[Brivudine (drug)]] 5 µM (+2.4); [[Ipatasertib (drug)]] 0.5 µM (+2.0); [[9-ING-41 (drug)]] 0.5 µM (+1.3); [[Tucidinostat (drug)]] 0.05 µM (+1.3); [[PF-06260933 (drug)]] 5 µM (+1.3); [[Auranofin (drug)]] 5 µM (+1.2); [[Vilanterol (drug)]] 5 µM (+1.2); [[Pitavastatin (Calcium) (drug)]] 0.5 µM (+1.2); [[HI-TOPK-032 (drug)]] 5 µM (+1.2) (32 in all, 15 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)
- Lower it: [[Harringtonine (drug)]] 0.5 µM (-3.8, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-2.4, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.05 µM (-2.4); [[Ouabain (Octahydrate) (drug)]] 5 µM (-2.2, ⚠ cell-cycle shift); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (-2.1); [[Digitoxin (drug)]] 0.5 µM (-2.1, ⚠ cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (-2.0); [[TAK-901 (drug)]] 5 µM (-1.9, ⚠ cell-cycle shift); [[Epirubicin (hydrochloride) (drug)]] 5 µM (-1.9, ⚠ cell-cycle shift); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (-1.9, ⚠ cell-cycle shift); [[PH-797804 (drug)]] 5 µM (-1.7); [[Budesonide (drug)]] 5 µM (-1.5); [[Budesonide (drug)]] 0.05 µM (-1.4); [[Ixazomib citrate (drug)]] 0.5 µM (-1.4); [[TAK-733 (drug)]] 5 µM (-1.4); [[Clobetasol propionate (drug)]] 5 µM (-1.4); [[Dexamethasone (drug)]] 0.05 µM (-1.4) (51 in all, 21 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SW480 (line)]], [[KATO III (line)]], [[LoVo (line)]], [[NCI-H460 (line)]], [[LS 180 (line)]], [[NCI-H2030 (line)]], [[SW1417 (line)]], [[Panc 03.27 (line)]]

## + arm (26)

| Gene | Projection | Name |
|---|---|---|
| [[ASMTL]] | 0.809 | acetylserotonin O-methyltransferase like |
| [[BAIAP3]] | 0.802 | BAI1 associated protein 3 |
| [[AHDC1]] | 0.801 | AT-hook DNA binding motif containing 1 |
| [[TBC1D10A]] | 0.786 | TBC1 domain family member 10A |
| [[SEMA3F]] | 0.784 | semaphorin 3F |
| [[CLIP2]] | 0.777 | CAP-Gly domain containing linker protein 2 |
| [[LMTK3]] | 0.753 | lemur tail kinase 3 |
| [[CADM4]] | 0.717 | cell adhesion molecule 4 |
| [[SYP]] | 0.715 | synaptophysin |
| [[ATP2A3]] | 0.704 | ATPase sarcoplasmic/endoplasmic reticulum Ca2+ transporting 3 |
| [[TGFB1]] | 0.694 | transforming growth factor beta 1 |
| [[SHF]] | 0.692 | Src homology 2 domain containing F |
| [[SPNS2]] | 0.664 | SPNS lysolipid transporter 2, sphingosine-1-phosphate |
| [[ANKDD1A]] | 0.663 | ankyrin repeat and death domain containing 1A |
| [[ATOSB]] | 0.600 | atos homolog B |
| [[FAM102A]] | 0.579 | estrogen-induced osteoclastogenesis regulator 1 |
| [[UNC5B]] | 0.575 | unc-5 netrin receptor B |
| [[CASTOR1]] | 0.546 | cytosolic arginine sensor for mTORC1 subunit 1 |
| [[LIPE]] | 0.537 | lipase E, hormone sensitive type |
| [[SH3BP1]] | 0.534 | SH3 domain binding protein 1 |
| [[MYADM]] | 0.524 | myeloid associated differentiation marker |
| [[ASPHD1]] | 0.476 | aspartate beta-hydroxylase domain containing 1 |
| [[CARD10]] | 0.450 | caspase recruitment domain family member 10 |
| [[VIM]] | 0.399 | vimentin |
| [[WHRN]] | 0.343 | whirlin |
| [[UACA]] | 0.243 | uveal autoantigen with coiled-coil domains and ankyrin repeats |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 161; `graph/modules.parquet` — module == 161; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [160] (drug-dose × line)
