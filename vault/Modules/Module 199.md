---
module: 199
type: "module"
n_genes: 16
n_plus: 16
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.3858512341976166
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 199

*16 genes (single-armed) · [[Module 199.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 198), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Panobinostat (drug)]] 5 µM (+8.3, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (+7.9, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (+7.6, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 5 µM (+3.9, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (+3.8, ⚠ cell-cycle shift); [[Belinostat (drug)]] 0.5 µM (+3.2, ⚠ cell-cycle shift); [[TAK-901 (drug)]] 5 µM (+3.1, ⚠ cell-cycle shift); [[Bortezomib (drug)]] 0.05 µM (+2.8, ⚠ cell-cycle shift); [[c-Kit-IN-1 (drug)]] 0.05 µM (+2.7, ⚠ unreliable plate only); [[Ixazomib citrate (drug)]] 0.5 µM (+2.7); [[Brivudine (drug)]] 5 µM (+2.5); [[PH-797804 (drug)]] 5 µM (+2.5); [[Tucidinostat (drug)]] 5 µM (+1.5); [[Abemaciclib (drug)]] 0.5 µM (+1.3); [[TAK-901 (drug)]] 0.05 µM (+1.2); [[Clobetasol propionate (drug)]] 5 µM (+1.2); [[Budesonide (drug)]] 5 µM (+1.1); [[c-Kit-IN-1 (drug)]] 5 µM (+1.1); [[EX229 (drug)]] 5 µM (+1.1) (27 in all, 14 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)
- Lower it: [[Homoharringtonine (drug)]] 5 µM (-4.4, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-4.3, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (-3.4, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (-2.8, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-2.3, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.05 µM (-1.5); [[Bimiralisib (drug)]] 0.5 µM (-1.4); [[GSK1059615 (drug)]] 0.5 µM (-1.2); [[Entrectinib (drug)]] 5 µM (-1.1) (9 in all, 5 with an alert ⚠)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[HOP62 (line)]], [[NCI-H2347 (line)]], [[AsPC-1 (line)]], [[LoVo (line)]], [[NCI-H1792 (line)]], [[PANC-1 (line)]], [[SNU-423 (line)]], [[J82 (line)]]

## + arm (16)

| Gene | Projection | Name |
|---|---|---|
| [[FBXW2]] | 0.838 | F-box and WD repeat domain containing 2 |
| [[GTF2E2]] | 0.807 | general transcription factor IIE subunit 2 |
| [[LRFN3]] | 0.781 | leucine rich repeat and fibronectin type III domain containing 3 |
| [[WDR5]] | 0.768 | WD repeat domain 5 |
| [[ATG5]] | 0.758 | autophagy related 5 |
| [[NAPG]] | 0.751 | NSF attachment protein gamma |
| [[CTNNBL1]] | 0.750 | catenin beta like 1 |
| [[PAFAH1B2]] | 0.750 | platelet activating factor acetylhydrolase 1b catalytic subunit 2 |
| [[PLS3-AS1]] | -0.748 | PLS3 antisense RNA 1 |
| [[CPSF4]] | 0.725 | cleavage and polyadenylation specific factor 4 |
| [[NTAQ1]] | 0.715 | N-terminal glutamine amidase 1 |
| [[USB1]] | 0.694 | U6 snRNA biogenesis phosphodiesterase 1 |
| [[SNX16]] | -0.643 | sorting nexin 16 |
| [[MTERF2]] | -0.499 | mitochondrial transcription termination factor 2 |
| [[EIF1AY]] | -0.496 | eukaryotic translation initiation factor 1A Y-linked |
| [[SMC5]] | 0.484 | structural maintenance of chromosomes 5 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 199; `graph/modules.parquet` — module == 199; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [198] (drug-dose × line)
