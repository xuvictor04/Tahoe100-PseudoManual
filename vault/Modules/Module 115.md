---
module: 115
type: "module"
n_genes: 42
n_plus: 42
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 115

*42 genes (single-armed) · [[Module 115.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 114), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Tucidinostat (drug)]] 5 µM (+15.6); [[Panobinostat (drug)]] 5 µM (+12.4, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (+11.2, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (+10.5, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (+10.2, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (+10.0, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+8.0, ⚠ cell-cycle shift); [[Brivudine (drug)]] 5 µM (+5.8); [[Dinaciclib (drug)]] 5 µM (+5.6, ⚠ toxic; transcription drop; cell-cycle shift); [[Belinostat (drug)]] 0.5 µM (+5.4, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 0.05 µM (+2.9); [[Brivudine (drug)]] 0.5 µM (+2.4); [[Ponatinib (drug)]] 5 µM (+2.1); [[Ponatinib (drug)]] 0.5 µM (+1.8); [[Topotecan (hydrochloride) (drug)]] 0.05 µM (+1.5); [[Bortezomib (drug)]] 0.5 µM (+1.4); [[Ipatasertib (drug)]] 0.5 µM (+1.4); [[Cobimetinib (drug)]] 5 µM (+1.3) (40 in all, 22 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM (-4.6, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (-4.1, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-3.8, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (-3.8, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (-3.3, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-2.9, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (-2.7, ⚠ toxic; transcription drop; cell-cycle shift); [[TAK-901 (drug)]] 5 µM (-2.7, ⚠ cell-cycle shift); [[PH-797804 (drug)]] 5 µM (-2.3); [[Digitoxin (drug)]] 0.05 µM (-2.3, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.05 µM (-1.9); [[Mebendazole (drug)]] 5 µM (-1.5); [[Artesunate (drug)]] 0.5 µM (-1.4); [[Abemaciclib (drug)]] 5 µM (-1.2); [[Gefitinib (drug)]] 5 µM (-1.1); [[TAK-733 (drug)]] 5 µM (-1.0); [[Clopidogrel (drug)]] 0.05 µM (-1.0) (21 in all, 13 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[PANC-1 (line)]], [[NCI-H460 (line)]], [[LOX-IMVI (line)]], [[HT-29 (line)]], [[HOP62 (line)]], [[A498 (line)]], [[NCI-H1573 (line)]], [[CFPAC-1 (line)]]

## + arm (42)

| Gene | Projection | Name |
|---|---|---|
| [[LINC00937]] | 0.852 | long independently transcribed non-coding RNA 937 |
| [[ARHGAP44]] | 0.800 | Rho GTPase activating protein 44 |
| [[SBK1]] | 0.791 | SH3 domain binding kinase 1 |
| [[PRKCQ]] | 0.756 | protein kinase C theta |
| [[TSPAN33]] | 0.754 | tetraspanin 33 |
| [[SGSM1]] | 0.723 | small G protein signaling modulator 1 |
| [[SUSD4]] | 0.706 | sushi domain containing 4 |
| [[CRACD]] | 0.695 | capping protein inhibiting regulator of actin dynamics |
| [[STRBP]] | 0.693 | spermatid perinuclear RNA binding protein |
| [[PARD6G]] | 0.691 | par-6 family cell polarity regulator gamma |
| [[SEMA4D]] | 0.685 | semaphorin 4D |
| [[ENTREP2]] | 0.670 | endosomal transmembrane epsin interactor 2 |
| [[APBA1]] | 0.670 | amyloid beta precursor protein binding family A member 1 |
| [[LHX2]] | 0.663 | LIM homeobox 2 |
| [[PTK7]] | 0.662 | protein tyrosine kinase 7 (inactive) |
| [[REEP1]] | 0.657 | receptor accessory protein 1 |
| [[MERTK]] | 0.653 | MER proto-oncogene, tyrosine kinase |
| [[CCDC69]] | 0.649 | coiled-coil domain containing 69 |
| [[EMID1]] | 0.643 | EMI domain containing 1 |
| [[VASH2]] | 0.641 | vasohibin 2 |
| [[ARHGEF26]] | 0.639 | Rho guanine nucleotide exchange factor 26 |
| [[SCD5]] | 0.638 | stearoyl-CoA desaturase 5 |
| [[MLXIPL]] | 0.636 | MLX interacting protein like |
| [[TMEM98]] | 0.632 | transmembrane protein 98 |
| [[ROR2]] | 0.629 | ROR family WNT receptor 2 |
| [[CDYL]] | 0.621 | chromodomain Y like |
| [[OTUD7A]] | 0.613 | OTU deubiquitinase 7A |
| [[HES2]] | 0.612 | hes family bHLH transcription factor 2 |
| [[FRMPD3]] | 0.588 | FERM and PDZ domain containing 3 |
| [[PLLP]] | 0.588 | plasmolipin |
| [[GLIPR2]] | 0.583 | GLI pathogenesis related 2 |
| [[PARM1]] | 0.558 | prostate androgen-regulated mucin-like protein 1 |
| [[ASRGL1]] | 0.557 | asparaginase and isoaspartyl peptidase 1 |
| [[SLC16A10]] | 0.554 | solute carrier family 16 member 10 |
| [[GAB2]] | 0.530 | GRB2 associated binding protein 2 |
| [[RBM11]] | 0.525 | RNA binding motif protein 11 |
| [[PLCG2]] | 0.499 | phospholipase C gamma 2 |
| [[ZNF385B]] | 0.474 | zinc finger protein 385B |
| [[KSR1]] | 0.450 | kinase suppressor of ras 1 |
| [[SLC29A3]] | 0.442 | solute carrier family 29 member 3 |
| [[SLC4A8]] | 0.407 | solute carrier family 4 member 8 |
| [[EPB41L4A]] | 0.369 | erythrocyte membrane protein band 4.1 like 4A |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 115; `graph/modules.parquet` — module == 115; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [114] (drug-dose × line)
