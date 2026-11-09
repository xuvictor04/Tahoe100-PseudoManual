---
module: 214
type: "module"
n_genes: 13
n_plus: 13
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 214

*13 genes (single-armed) · [[Module 214.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | PTK6 Regulates RHO GTPases, RAS GTPase and MAP kinases | reactome | 2/13 | 166 | 0.024 |
| + | PTK6 Regulates RHO GTPases, RAS GTPase and MAP kinases | reactome | 2/13 | 166 | 0.024 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 213), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM (+8.5, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (+7.8, ⚠ toxic; transcription drop; cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (+6.2, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (+6.0, ⚠ cell-cycle shift); [[Niclosamide (olamine) (drug)]] 5 µM (+5.8, ⚠ toxic; cell-cycle shift); [[Ixazomib citrate (drug)]] 5 µM (+4.6, ⚠ cell-cycle shift); [[PH-797804 (drug)]] 5 µM (+3.2); [[Vinblastine (sulfate) (drug)]] 5 µM (+3.1); [[Harringtonine (drug)]] 5 µM (+3.0, ⚠ cell-cycle shift); [[Bortezomib (drug)]] 0.05 µM (+2.9, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 0.5 µM (+2.8); [[Tucidinostat (drug)]] 5 µM (+2.8); [[Neratinib (maleate) (drug)]] 5 µM (+2.4); [[Brivudine (drug)]] 5 µM (+2.2); [[Vinblastine (sulfate) (drug)]] 0.5 µM (+2.1); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (+1.8); [[Bortezomib (drug)]] 0.5 µM (+1.8); [[Radotinib (drug)]] 5 µM (+1.7) (70 in all, 23 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Dinaciclib (drug)]] 0.5 µM (-5.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (-4.7, ⚠ toxic; transcription drop; cell-cycle shift); [[Auranofin (drug)]] 5 µM (-3.7); [[Filgotinib (drug)]] 5 µM (-2.3); [[Idarubicin (hydrochloride) (drug)]] 5 µM (-2.2, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (-2.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 5 µM (-2.0, ⚠ toxic; cell-cycle shift); [[Mifepristone (drug)]] 0.5 µM (-1.9); [[Filgotinib (drug)]] 0.05 µM (-1.9); [[Diphenhydramine (drug)]] 0.5 µM (-1.9); [[Estrone sulfate (potassium) (drug)]] 5 µM (-1.9); [[(S)-Crizotinib (drug)]] 0.5 µM (-1.9); [[Carbamazepine (drug)]] 5 µM (-1.9); [[Esmolol (hydrochloride) (drug)]] 5 µM (-1.8); [[Apalutamide (drug)]] 0.5 µM (-1.7) (56 in all, 15 with an alert ⚠; shown: the 10 strongest and the 5 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SW480 (line)]], [[PANC-1 (line)]], [[NCI-H460 (line)]], [[NCI-H23 (line)]], [[NCI-H1573 (line)]], [[NCI-H1792 (line)]], [[LoVo (line)]], [[SW1417 (line)]]

## + arm (13)

| Gene | Projection | Name |
|---|---|---|
| [[ARHGAP17]] | 0.814 | Rho GTPase activating protein 17 |
| [[PPP4R1]] | 0.807 | protein phosphatase 4 regulatory subunit 1 |
| [[AGFG1]] | 0.719 | ArfGAP with FG repeats 1 |
| [[LRRFIP2]] | 0.702 | LRR binding FLII interacting protein 2 |
| [[FDX1]] | 0.699 | ferredoxin 1 |
| [[KRAS]] | 0.676 | KRas proto-oncogene, GTPase |
| [[AMFR]] | 0.674 | autocrine motility factor receptor |
| [[ELMO2]] | 0.658 | engulfment and cell motility 2 |
| [[TMEM131L]] | 0.643 | transmembrane 131 like |
| [[MRTFA]] | 0.608 | myocardin related transcription factor A |
| [[CHPT1]] | 0.593 | choline phosphotransferase 1 |
| [[REEP5]] | 0.497 | receptor accessory protein 5 |
| [[DENND5A]] | 0.416 | DENN domain containing 5A |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 214; `graph/modules.parquet` — module == 214; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [213] (drug-dose × line)
