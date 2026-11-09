---
module: 171
type: "module"
n_genes: 24
n_plus: 17
n_minus: 7
arms_opposite: true
mean_cos_between_arms: -0.41129544377326965
label: "Sealing of the nuclear envelope (NE) by ESCRT-III"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 171

*Sealing of the nuclear envelope (NE) by ESCRT-III · 24 genes (17 in the + arm, 7 in the − arm) · [[Module 171.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.41). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

Label from the validation stage: **Sealing of the nuclear envelope (NE) by ESCRT-III** (reactome, q 0.003; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | Sealing of the nuclear envelope (NE) by ESCRT-III | reactome | 3/24 | 81.9 | 0.003 |
| - | Microtubule-dependent trafficking of connexons from Golgi to the plasma membrane | reactome | 2/7 | 392 | 0.005 |
| - | Transport of connexons to the plasma membrane | reactome | 2/7 | 359 | 0.006 |
| - | RHO GTPases Activate Formins | reactome | 3/7 | 49.7 | 0.010 |
| - | Macroautophagy | reactome | 3/7 | 49.3 | 0.010 |
| - | Gap junction assembly | reactome | 2/7 | 269 | 0.010 |
| - | Post-chaperonin tubulin folding pathway | reactome | 2/7 | 269 | 0.010 |
| - | Autophagy | reactome | 3/7 | 45.2 | 0.012 |

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 170), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Dinaciclib (drug)]] 0.5 µM (+9.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+8.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+7.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Selinexor (drug)]] 5 µM (+5.9, ⚠ cell-cycle shift); [[Ponatinib (drug)]] 5 µM (+5.6); [[Ixazomib citrate (drug)]] 5 µM (+5.5, ⚠ cell-cycle shift); [[Radotinib (drug)]] 5 µM (+4.7); [[PH-797804 (drug)]] 5 µM (+4.5); [[Bortezomib (drug)]] 0.05 µM (+4.4, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 0.5 µM (+3.9); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (+3.8); [[Cabozantinib (S-malate) (drug)]] 5 µM (+3.7); [[Trametinib (drug)]] 0.05 µM (+3.0); [[Vinblastine (sulfate) (drug)]] 0.5 µM (+2.7); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM (+2.4); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (+2.3) (134 in all, 20 with an alert ⚠; shown: the 10 strongest and the 6 next strongest without an alert)
- Lower it: [[Homoharringtonine (drug)]] 5 µM (-18.2, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-7.5, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (-7.3, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-7.1, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (-6.8, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (-5.6, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (-5.5, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (-5.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (-5.0); [[Auranofin (drug)]] 5 µM (-4.9); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (-4.1); [[(S)-Crizotinib (drug)]] 0.5 µM (-2.8); [[Thymol (drug)]] 5 µM (-2.7); [[Estrone sulfate (potassium) (drug)]] 5 µM (-2.7); [[Docetaxel (drug)]] 5 µM (-2.6); [[Larotrectinib (drug)]] 0.05 µM (-2.6); [[Diphenhydramine (drug)]] 0.5 µM (-2.6); [[PF-06260933 (drug)]] 5 µM (-2.5) (124 in all, 27 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[PANC-1 (line)]], [[NCI-H460 (line)]], [[AsPC-1 (line)]], [[SNU-423 (line)]], [[COLO 205 (line)]], [[MIA PaCa-2 (line)]], [[LOX-IMVI (line)]], [[HOP62 (line)]]

## + arm (17)

| Gene | Projection | Name |
|---|---|---|
| [[TMEM183A]] | 0.833 | transmembrane protein 183A |
| [[SNX4]] | 0.805 | sorting nexin 4 |
| [[RTCA]] | 0.803 | RNA 3'-terminal phosphate cyclase |
| [[COPS7B]] | 0.790 | COP9 signalosome subunit 7B |
| [[FBXO7]] | 0.775 | F-box protein 7 |
| [[CIZ1]] | 0.774 | CDKN1A interacting zinc finger protein 1 |
| [[MRPS35]] | 0.741 | mitochondrial ribosomal protein S35 |
| [[SAMM50]] | 0.733 | SAMM50 sorting and assembly machinery component |
| [[VTI1B]] | 0.722 | vesicle transport through interaction with t-SNAREs 1B |
| [[SACM1L]] | 0.686 | SAC1 like phosphatidylinositide phosphatase |
| [[DCAF12]] | 0.664 | DDB1 and CUL4 associated factor 12 |
| [[ADD1]] | 0.647 | adducin 1 |
| [[CDC23]] | 0.629 | cell division cycle 23 |
| [[PPP1CB]] | 0.611 | protein phosphatase 1 catalytic subunit beta |
| [[SMPDL3A]] | 0.609 | sphingomyelin phosphodiesterase acid like 3A |
| [[ABHD4]] | 0.580 | abhydrolase domain containing 4, N-acyl phospholipase B |
| [[SPAST]] | 0.569 | spastin |

## − arm (7)

| Gene | Projection | Name |
|---|---|---|
| [[TUBB4B]] | -0.738 | tubulin beta 4B class IVb |
| [[DPH1-AS1]] | -0.720 | DPH1 antisense RNA 1 |
| [[PFN1]] | -0.713 | profilin 1 |
| [[TUBA1C]] | -0.619 | tubulin alpha 1c |
| [[ZSWIM6]] | -0.574 | zinc finger SWIM-type containing 6 |
| [[ATG7]] | -0.546 | autophagy related 7 |
| [[RAPGEF6]] | -0.503 | Rap guanine nucleotide exchange factor 6 |

## Data

- `graph/nodes.parquet` — module == 171; `graph/modules.parquet` — module == 171; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [170] (drug-dose × line)
