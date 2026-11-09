---
module: 197
type: "module"
n_genes: 16
n_plus: 16
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.45229923725128174
label: "Nervous system development"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 197

*Nervous system development · 16 genes (single-armed) · [[Module 197.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.45; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

Label from the validation stage: **Nervous system development** (reactome, q 0.044; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | Nervous system development | reactome | 5/16 | 9.46 | 0.044 |
| + | Nervous system development | reactome | 5/16 | 9.46 | 0.044 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 196), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Homoharringtonine (drug)]] 5 µM (+12.8, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (+9.2, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+7.7); [[Dinaciclib (drug)]] 0.5 µM (+6.5, ⚠ toxic; transcription drop; cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+5.5, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (+5.4, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+5.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (+5.0, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+4.6, ⚠ toxic; transcription drop; cell-cycle shift); [[Niclosamide (olamine) (drug)]] 5 µM (+3.8, ⚠ toxic; cell-cycle shift); [[Brivudine (drug)]] 5 µM (+3.2); [[Cobimetinib (drug)]] 5 µM (+2.8); [[Cobimetinib (drug)]] 0.5 µM (+2.5); [[Trametinib (drug)]] 0.05 µM (+2.2); [[Trametinib (drug)]] 0.5 µM (+1.8); [[Filgotinib (drug)]] 5 µM (+1.8); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (+1.8); [[Busulfan (drug)]] 0.05 µM (+1.7); [[Binimetinib (drug)]] 5 µM (+1.7) (71 in all, 21 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)
- Lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM (-3.7, ⚠ toxic; cell-cycle shift); [[Abemaciclib (drug)]] 5 µM (-3.0); [[Idarubicin (hydrochloride) (drug)]] 5 µM (-2.8, ⚠ cell-cycle shift); [[c-Kit-IN-1 (drug)]] 0.05 µM (-2.7, ⚠ unreliable plate only); [[Bortezomib (drug)]] 0.05 µM (-2.7, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 5 µM (-2.6, ⚠ cell-cycle shift); [[Artesunate (drug)]] 5 µM (-2.5, ⚠ cell-cycle shift); [[Docetaxel (drug)]] 0.05 µM (-2.4, ⚠ transcription drop; cell-cycle shift); [[Auranofin (drug)]] 5 µM (-2.4); [[Ixazomib citrate (drug)]] 0.5 µM (-2.3); [[Sapanisertib (drug)]] 0.5 µM (-2.3); [[Docetaxel (Trihydrate) (drug)]] 0.5 µM (-2.2); [[EX229 (drug)]] 0.5 µM (-2.1); [[c-Kit-IN-1 (drug)]] 5 µM (-2.0); [[Abemaciclib (drug)]] 0.5 µM (-2.0); [[Ipatasertib (drug)]] 0.5 µM (-2.0); [[Vinblastine (sulfate) (drug)]] 5 µM (-1.8) (53 in all, 11 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[HOP62 (line)]], [[HS-578T (line)]], [[A-172 (line)]], [[NCI-H2347 (line)]], [[hTERT-HPNE (line)]], [[PANC-1 (line)]], [[NCI-H460 (line)]], [[SNU-423 (line)]]

## + arm (16)

| Gene | Projection | Name |
|---|---|---|
| [[CDH2]] | 0.806 | cadherin 2 |
| [[ALCAM]] | 0.791 | activated leukocyte cell adhesion molecule |
| [[PLCB4]] | 0.779 | phospholipase C beta 4 |
| [[FAT1]] | 0.760 | FAT atypical cadherin 1 |
| [[CDK6]] | 0.743 | cyclin dependent kinase 6 |
| [[ARHGEF12]] | 0.710 | Rho guanine nucleotide exchange factor 12 |
| [[KRBOX4]] | -0.703 | KRAB domain containing 4 |
| [[PLCE1]] | 0.698 | phospholipase C epsilon 1 |
| [[ITGAV]] | 0.680 | integrin subunit alpha V |
| [[NAB1]] | 0.678 | NGFI-A binding protein 1 |
| [[NEO1]] | 0.648 | neogenin 1 |
| [[TPM1]] | 0.631 | tropomyosin 1 |
| [[STIM2]] | 0.621 | stromal interaction molecule 2 |
| [[SYNE2]] | 0.600 | spectrin repeat containing nuclear envelope protein 2 |
| [[COBL]] | 0.589 | cordon-bleu WH2 repeat protein |
| [[LRP6]] | 0.575 | LDL receptor related protein 6 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 197; `graph/modules.parquet` — module == 197; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [196] (drug-dose × line)
