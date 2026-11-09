---
module: 183
type: "module"
n_genes: 21
n_plus: 21
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.3179183006286621
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 183

*21 genes (single-armed) · [[Module 183.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 182), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM (+6.1, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (+4.9, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (+4.9, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (+4.8, ⚠ cell-cycle shift); [[Selinexor (drug)]] 5 µM (+4.0, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (+3.6, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (+3.4, ⚠ cell-cycle shift); [[Bortezomib (drug)]] 0.05 µM (+3.2, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+3.0); [[Belinostat (drug)]] 0.5 µM (+3.0, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (+2.6); [[Ponatinib (drug)]] 5 µM (+2.4); [[Brivudine (drug)]] 5 µM (+2.4); [[Ixazomib citrate (drug)]] 0.5 µM (+2.1); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+2.0); [[Radotinib (drug)]] 5 µM (+1.6); [[Cabozantinib (S-malate) (drug)]] 5 µM (+1.5); [[Cobimetinib (drug)]] 5 µM (+1.4); [[Bortezomib (drug)]] 0.5 µM (+1.3) (37 in all, 24 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)
- Lower it: [[Digitoxin (drug)]] 0.5 µM (-2.5, ⚠ cell-cycle shift); [[c-Kit-IN-1 (drug)]] 0.05 µM (-1.7, ⚠ unreliable plate only); [[Ouabain (Octahydrate) (drug)]] 5 µM (-1.7, ⚠ cell-cycle shift); [[Adagrasib (drug)]] 0.05 µM (-1.3, ⚠ position not correctable); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (-1.3, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (-1.2, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.05 µM (-1.2, ⚠ cell-cycle shift); [[Gefitinib (drug)]] 5 µM (-1.0); [[5-Azacytidine (drug)]] 5 µM (-1.0) (9 in all, 7 with an alert ⚠)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[LoVo (line)]], [[HEC-1-A (line)]], [[J82 (line)]], [[A-172 (line)]], [[HT-29 (line)]], [[PANC-1 (line)]], [[NCI-H460 (line)]], [[HOP62 (line)]]

## + arm (21)

| Gene | Projection | Name |
|---|---|---|
| [[USP30]] | 0.880 | ubiquitin specific peptidase 30 |
| [[CGRRF1]] | 0.794 | cell growth regulator with ring finger domain 1 |
| [[JKAMP]] | 0.780 | JNK1/MAPK8 associated membrane protein |
| [[FRG1DP]] | 0.756 | FSHD region gene 1 family member D, pseudogene |
| [[TRAPPC2]] | 0.753 | trafficking protein particle complex subunit 2 |
| [[CDC40]] | 0.746 | cell division cycle 40 |
| [[ACOT8]] | 0.726 | acyl-CoA thioesterase 8 |
| [[ZNF836]] | 0.694 | zinc finger protein 836 |
| [[FRG1GP]] | 0.690 | FSHD region gene 1 family member G, pseudogene |
| [[LINC01012]] | 0.676 | long independently transcribed non-coding RNA 1012 |
| [[LINC00674]] | 0.666 | long independently transcribed non-coding RNA 674 |
| [[ZSCAN2]] | 0.646 | zinc finger and SCAN domain containing 2 |
| [[LEPROTL1]] | 0.611 | leptin receptor overlapping transcript like 1 |
| [[CYCS]] | -0.597 | cytochrome c, somatic |
| [[BCL9]] | 0.579 | BCL9 transcription coactivator |
| [[FRG1JP]] | 0.568 | FSHD region gene 1 family member J, pseudogene |
| [[SLIT2]] | -0.557 | slit guidance ligand 2 |
| [[ITPR2]] | -0.518 | inositol 1,4,5-trisphosphate receptor type 2 |
| [[ADAMTS17]] | -0.477 | ADAM metallopeptidase with thrombospondin type 1 motif 17 |
| [[MICE]] | 0.380 | MHC class I polypeptide-related sequence E (pseudogene) |
| [[EMC7]] | 0.288 | ER membrane protein complex subunit 7 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 183; `graph/modules.parquet` — module == 183; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [182] (drug-dose × line)
