---
module: 186
type: "module"
n_genes: 20
n_plus: 20
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.391129732131958
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 186

*20 genes (single-armed) · [[Module 186.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 185), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM (+5.4, ⚠ cell-cycle shift); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (+3.7, ⚠ cell-cycle shift); [[Brivudine (drug)]] 5 µM (+2.9); [[Ouabain (Octahydrate) (drug)]] 5 µM (+2.4, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+2.4); [[Idarubicin (hydrochloride) (drug)]] 0.5 µM (+2.3, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (+2.2, ⚠ cell-cycle shift); [[Epirubicin (hydrochloride) (drug)]] 5 µM (+2.1, ⚠ cell-cycle shift); [[TAK-901 (drug)]] 5 µM (+2.0, ⚠ cell-cycle shift); [[PH-797804 (drug)]] 5 µM (+2.0); [[Ponatinib (drug)]] 5 µM (+1.7); [[Tomivosertib (drug)]] 5 µM (+1.7); [[Flumatinib (mesylate) (drug)]] 5 µM (+1.6); [[Epirubicin (hydrochloride) (drug)]] 0.5 µM (+1.6); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (+1.5); [[Verteporfin (drug)]] 5 µM (+1.5); [[Ipatasertib (drug)]] 5 µM (+1.5) (51 in all, 21 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)
- Lower it: [[Dinaciclib (drug)]] 0.5 µM (-8.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (-8.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (-6.4, ⚠ toxic; transcription drop; cell-cycle shift); [[Auranofin (drug)]] 5 µM (-4.8); [[Homoharringtonine (drug)]] 0.5 µM (-4.4, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (-4.1, ⚠ cell-cycle shift); [[Docetaxel (drug)]] 0.05 µM (-2.6, ⚠ transcription drop; cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (-2.0, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (-2.0, ⚠ cell-cycle shift); [[Belzutifan (drug)]] 5 µM (-1.9); [[Carbamazepine (drug)]] 5 µM (-1.7); [[Belumosudil (drug)]] 5 µM (-1.7); [[Mifepristone (drug)]] 0.5 µM (-1.5); [[Thymol (drug)]] 5 µM (-1.5); [[GSK1059615 (drug)]] 0.5 µM (-1.5); [[4EGI-1 (drug)]] 5 µM (-1.5); [[Filgotinib (drug)]] 0.05 µM (-1.5); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM (-1.5) (53 in all, 13 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[C32 (line)]], [[NCI-H460 (line)]], [[NCI-H23 (line)]], [[A-427 (line)]], [[LoVo (line)]], [[NCI-H2030 (line)]], [[LOX-IMVI (line)]], [[SW480 (line)]]

## + arm (20)

| Gene | Projection | Name |
|---|---|---|
| [[PPP2R5E]] | 0.837 | protein phosphatase 2 regulatory subunit B'epsilon |
| [[BMPR1A]] | 0.829 | bone morphogenetic protein receptor type 1A |
| [[PDE7A]] | 0.799 | phosphodiesterase 7A |
| [[VGLL4]] | 0.751 | vestigial like family member 4 |
| [[NDC1]] | 0.726 | NDC1 transmembrane nucleoporin |
| [[EED]] | 0.723 | embryonic ectoderm development |
| [[SRPK2]] | 0.712 | SRSF protein kinase 2 |
| [[ZNF674]] | -0.696 | zinc finger protein 674 |
| [[PTPRJ]] | 0.696 | protein tyrosine phosphatase receptor type J |
| [[FZD3]] | 0.689 | frizzled class receptor 3 |
| [[SMAD5]] | 0.669 | SMAD family member 5 |
| [[NFATC3]] | 0.667 | nuclear factor of activated T cells 3 |
| [[POU2F1]] | 0.636 | POU class 2 homeobox 1 |
| [[STIM1]] | 0.622 | stromal interaction molecule 1 |
| [[SLC35D1]] | 0.580 | solute carrier family 35 member D1 |
| [[CDK8]] | 0.556 | cyclin dependent kinase 8 |
| [[TLCD4]] | 0.522 | TLC domain containing 4 |
| [[WHAMMP2]] | 0.401 | WHAMM pseudogene 2 |
| [[PLEKHA1]] | 0.340 | pleckstrin homology domain containing A1 |
| [[ALDH9A1]] | 0.179 | aldehyde dehydrogenase 9 family member A1 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 186; `graph/modules.parquet` — module == 186; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [185] (drug-dose × line)
