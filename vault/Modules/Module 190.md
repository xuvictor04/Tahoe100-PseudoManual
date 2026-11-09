---
module: 190
type: "module"
n_genes: 18
n_plus: 18
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.39888525009155273
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 190

*18 genes (single-armed) · [[Module 190.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 189), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Ixazomib citrate (drug)]] 5 µM (+2.7, ⚠ cell-cycle shift); [[Selinexor (drug)]] 5 µM (+2.6, ⚠ cell-cycle shift); [[Bortezomib (drug)]] 0.05 µM (+2.5, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+2.3, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+2.0); [[Bortezomib (drug)]] 5 µM (+1.9, ⚠ toxic; cell-cycle shift); [[Ponatinib (drug)]] 5 µM (+1.8); [[Tucidinostat (drug)]] 0.5 µM (+1.7, ⚠ cell-cycle shift); [[Radotinib (drug)]] 5 µM (+1.7); [[Selinexor (drug)]] 0.5 µM (+1.5, ⚠ cell-cycle shift); [[Cabozantinib (S-malate) (drug)]] 5 µM (+1.2); [[Cobimetinib (drug)]] 5 µM (+1.1); [[Brivudine (drug)]] 5 µM (+1.1) (14 in all, 8 with an alert ⚠; shown: the 10 strongest and the 3 next strongest without an alert)
- Lower it: [[Homoharringtonine (drug)]] 5 µM (-3.2, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-2.8, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-2.6, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (-2.6, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (-2.1, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (-1.7, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.05 µM (-1.5); [[TAK-901 (drug)]] 5 µM (-1.3, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (-1.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Thymol (drug)]] 5 µM (-1.3); [[Filgotinib (drug)]] 5 µM (-1.2); [[Belumosudil (drug)]] 5 µM (-1.2); [[Harringtonine (drug)]] 0.05 µM (-1.0) (14 in all, 9 with an alert ⚠; shown: the 10 strongest and the 3 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[NCI-H1573 (line)]], [[NCI-H460 (line)]], [[LoVo (line)]], [[A549 (line)]], [[PANC-1 (line)]], [[HOP62 (line)]], [[A498 (line)]], [[AsPC-1 (line)]]

## + arm (18)

| Gene | Projection | Name |
|---|---|---|
| [[NAPB]] | 0.873 | NSF attachment protein beta |
| [[FHIP2A]] | 0.788 | FHF complex subunit HOOK interacting protein 2A |
| [[DRAM2]] | 0.784 | DNA damage regulated autophagy modulator 2 |
| [[SLC18B1]] | 0.777 | solute carrier family 18 member B1 |
| [[WWP1]] | 0.761 | WW domain containing E3 ubiquitin protein ligase 1 |
| [[PPP1R10]] | -0.753 | protein phosphatase 1 regulatory subunit 10 |
| [[RAB12]] | 0.727 | RAB12, member RAS oncogene family |
| [[CIBAR1]] | 0.722 | CBY1 interacting BAR domain containing 1 |
| [[ZNF274]] | -0.696 | zinc finger protein 274 |
| [[RNPEP]] | 0.679 | arginyl aminopeptidase |
| [[TPD52L1]] | 0.674 | TPD52 like 1 |
| [[PAQR3]] | 0.647 | progestin and adipoQ receptor family member 3 |
| [[CYTH2]] | -0.630 | cytohesin 2 |
| [[CISD1]] | 0.562 | CDGSH iron sulfur domain 1 |
| [[ARHGAP39]] | -0.517 | Rho GTPase activating protein 39 |
| [[GDPD1]] | 0.509 | glycerophosphodiester phosphodiesterase domain containing 1 |
| [[UBE2Q2]] | 0.474 | ubiquitin conjugating enzyme E2 Q2 |
| [[ACSS1]] | 0.423 | acyl-CoA synthetase short chain family member 1 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 190; `graph/modules.parquet` — module == 190; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [189] (drug-dose × line)
