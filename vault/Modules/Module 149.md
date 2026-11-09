---
module: 149
type: "module"
n_genes: 30
n_plus: 30
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.40676775574684143
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 149

*30 genes (single-armed) · [[Module 149.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 148), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Homoharringtonine (drug)]] 5 µM (+9.0, ⚠ cell-cycle shift); [[TAK-901 (drug)]] 5 µM (+6.6, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+6.2, ⚠ cell-cycle shift); [[PH-797804 (drug)]] 5 µM (+4.4); [[Harringtonine (drug)]] 5 µM (+4.0, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+3.3, ⚠ cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 5 µM (+3.3, ⚠ toxic; cell-cycle shift); [[Bortezomib (drug)]] 0.05 µM (+2.5, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (+2.4); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (+2.2, ⚠ cell-cycle shift); [[Docetaxel (Trihydrate) (drug)]] 0.5 µM (+1.6); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+1.6); [[Ipatasertib (drug)]] 0.5 µM (+1.4); [[Ponatinib (drug)]] 0.5 µM (+1.1); [[Oxaliplatin (drug)]] 0.05 µM (+1.1); [[Homoharringtonine (drug)]] 0.05 µM (+1.1); [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM (+1.1); [[PH-797804 (drug)]] 0.5 µM (+1.1) (31 in all, 21 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Dinaciclib (drug)]] 5 µM (-7.5, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (-7.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (-4.6, ⚠ toxic; transcription drop; cell-cycle shift); [[Niclosamide (olamine) (drug)]] 5 µM (-3.4, ⚠ toxic; cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (-2.1); [[Belumosudil (drug)]] 5 µM (-1.4); [[Tucidinostat (drug)]] 0.5 µM (-1.4, ⚠ cell-cycle shift); [[c-Kit-IN-1 (drug)]] 0.05 µM (-1.2, ⚠ unreliable plate only); [[Clopidogrel (drug)]] 0.05 µM (-1.1); [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM (-1.1); [[Pyridoxine (hydrochloride) (drug)]] 5 µM (-1.0) (11 in all, 6 with an alert ⚠)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[PANC-1 (line)]], [[SW480 (line)]], [[LoVo (line)]], [[LS 180 (line)]], [[MIA PaCa-2 (line)]], [[NCI-H460 (line)]], [[HEC-1-A (line)]], [[KATO III (line)]]

## + arm (30)

| Gene | Projection | Name |
|---|---|---|
| [[TTF1]] | 0.857 | transcription termination factor 1 |
| [[ZNF791]] | 0.847 | zinc finger protein 791 |
| [[ZNF3]] | 0.843 | zinc finger protein 3 |
| [[TRIM4]] | 0.842 | tripartite motif containing 4 |
| [[BRAP]] | 0.840 | BRCA1 associated protein |
| [[ZNF557]] | 0.805 | zinc finger protein 557 |
| [[ANKRD49]] | 0.801 | ankyrin repeat domain 49 |
| [[MAU2]] | 0.785 | MAU2 sister chromatid cohesion factor |
| [[NKAPD1]] | 0.785 | NKAP domain containing 1 |
| [[YJU2B]] | 0.770 | YJU2 splicing factor homolog B |
| [[ZNF766]] | 0.752 | zinc finger protein 766 |
| [[TRAPPC2B]] | 0.747 | trafficking protein particle complex subunit 2B |
| [[IP6K1]] | 0.728 | inositol hexakisphosphate kinase 1 |
| [[TTI2]] | 0.713 | TELO2 interacting protein 2 |
| [[MTRFR]] | 0.690 | mitochondrial translation release factor in rescue |
| [[TFRC]] | -0.688 | transferrin receptor |
| [[ZNF200]] | 0.678 | zinc finger protein 200 |
| [[ZNF707]] | 0.676 | zinc finger protein 707 |
| [[PSMD5]] | 0.673 | proteasome 26S subunit, non-ATPase 5 |
| [[KIN]] | 0.665 | Kin17 DNA and RNA binding protein |
| [[NAA60]] | 0.665 | N-alpha-acetyltransferase 60, NatF catalytic subunit |
| [[DPY19L1]] | -0.639 | dpy-19 like C-mannosyltransferase 1 |
| [[N4BP2L2]] | 0.638 | NEDD4 binding protein 2 like 2 |
| [[ZKSCAN5]] | 0.621 | zinc finger with KRAB and SCAN domains 5 |
| [[DNTTIP1]] | 0.611 | deoxynucleotidyltransferase terminal interacting protein 1 |
| [[AKAP8L]] | 0.595 | A-kinase anchoring protein 8 like |
| [[ISG20L2]] | 0.569 | interferon stimulated exonuclease gene 20 like 2 |
| [[ASTE1]] | 0.510 | asteroid structure-specific endonuclease 1 |
| [[OTUD7B]] | 0.494 | OTU deubiquitinase 7B |
| [[RBFOX2]] | -0.482 | RNA binding fox-1 homolog 2 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 149; `graph/modules.parquet` — module == 149; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [148] (drug-dose × line)
