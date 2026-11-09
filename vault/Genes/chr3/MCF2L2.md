---
symbol: "MCF2L2"
type: "gene"
col: 595
ensembl_id: "ENSG00000053524"
name: "MCF.2 cell line derived transforming sequence-like 2"
location: "3q27.1"
module: 102
arm: "+"
pooled_cpm: 30.31
n_lines_expressing: 45
n_dd_up: 11
n_dd_down: 20
n_dd_up_clean: 8
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 15
direction_downstream: 0
tags: ["gene", "module/102"]
generated_by: "tahoemap"
---

# MCF2L2

*MCF.2 cell line derived transforming sequence-like 2* — 3q27.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.66× (z +13.8, q 1e-40, up in 32 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.513× (z -12.8, q 7e-35, down in 30 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAP6]] (+0.65, fdr 1e-05), [[GNAO1]] (+0.60, fdr 1e-05), [[ANKRD6]] (+0.58, fdr 9e-06); moves opposite to [[B9D2]] (-0.46, fdr 4e-05), [[PTPRB]] (-0.45, fdr 4e-05), [[PTPRR]] (-0.45, fdr 4e-05).
> It is in [[Module 102]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[SEPTIN3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 595.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.66×** | +13.8 | 1e-40 | 32/43 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.77×** | +11.1 | 6e-26 | 22/39 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.75×** | +10.8 | 6e-25 | 31/42 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.73×** | +10.2 | 3e-22 | 20/32 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.53×** | +7.5 | 5e-12 | 20/37 (HOP62, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | 1.19× | +4.8 | 1e-04 | 18/43 (LoVo, NCI-H23, …) | rises with dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.27×** | +4.2 | 0.002 | 18/43 (PANC-1, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.24×** | +4.1 | 0.002 | 17/43 (AsPC-1, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.22×** | +3.9 | 0.006 | 9/43 (SW1417, SW480, …) | all doses, stronger at high dose |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.20×** | +3.5 | 0.023 | 6/42 (MIA PaCa-2, H4, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.41×** | +3.5 | 0.024 | 9/43 (PANC-1, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.024 | 9/42 (HOP62, NCI-H1792, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.4 | 0.028 | 13/43 (AsPC-1, PANC-1, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 1.19× | +3.3 | 0.042 | 14/42 (C-33 A, LS 180, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.20× | +3.2 | 0.048 | 6/42 (C-33 A, NCI-H1573, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Ciclopirox (drug)]] 5 µM |  | 1.12× | +3.1 | 0.065 | 8/43 (SK-MEL-2, NCI-H23, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 595.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.513×** | -12.8 | 7e-35 | 30/43 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.551×** | -11.5 | 5e-28 | 27/42 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.574×** | -10.7 | 3e-24 | 29/42 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.649×** | -8.3 | 1e-14 | 28/42 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.677×** | -7.5 | 8e-12 | 24/42 (MIA PaCa-2, A-427, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.696×** | -6.7 | 2e-09 | 25/42 (NCI-H23, A-172, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.728×** | -6.1 | 9e-08 | 25/42 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.721×** | -6.1 | 1e-07 | 21/43 (MIA PaCa-2, A-172, …) | rises with dose | composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | **0.741×** | -5.5 | 2e-06 | 19/42 (NCI-H23, A-172, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.750×** | -5.3 | 6e-06 | 21/41 (J82, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.746×** | -5.3 | 6e-06 | 21/43 (A-172, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.604×** | -5.1 | 2e-05 | 22/42 (A-172, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.776×** | -4.4 | 4e-04 | 16/43 (PANC-1, A-172, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.939× | -4.2 | 0.001 | 6/43 (NCI-H1792, HOP62, …) | inconsistent across doses |  |
| [[Gefitinib (drug)]] 5 µM |  | **0.808×** | -4.1 | 0.002 | 13/43 (NCI-H460, PANC-1, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.809×** | -4.1 | 0.002 | 16/43 (RKO, MIA PaCa-2, …) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.811×** | -4.0 | 0.002 | 10/42 (HOP62, C32, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.863× | -4.0 | 0.002 | 11/43 (CHP-212, LS 180, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.831×** | -3.5 | 0.011 | 12/43 (NCI-H1573, C32, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.833×** | -3.4 | 0.019 | 13/42 (A549, LS 180, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.876× | -3.3 | 0.026 | 8/43 (NCI-H1573, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 595. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 90.1 | 0 | 15 (12 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0659× (z -23.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.169× (z -15.3) |
| [[A-172 (line)]] | wt | 85.2 | 0 | 13 (7 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.185× (z -14.1) |
| [[PANC-1 (line)]] | alt | 43.6 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -19.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.203× (z -16.3) |
| [[J82 (line)]] | alt | 62.1 | 0 | 10 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.130× (z -16.9) |
| [[A-427 (line)]] | wt | 145 | 0 | 7 (5 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.226× (z -16.2) ⚠ cell-cycle shift, explains ~17% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.296× (z -13.3) |
| [[NCI-H23 (line)]] | alt | 43.5 | 0 | 7 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.148× (z -15.5) ⚠ toxic; cell-cycle shift, explains ~24% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.165× (z -14.6) |
| [[Panc 03.27 (line)]] | alt | 73.1 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -11.3) |
| [[AsPC-1 (line)]] | alt | 15.3 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.26× (z +14.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 16.5× (z +13.0) | — |
| [[LoVo (line)]] | wt | 31.7 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.303× (z -10.8) |
| [[NCI-H2030 (line)]] | alt | 46.5 | 0 | 5 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.230× (z -12.5) |
| [[RKO (line)]] | wt | 33.6 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.217× (z -11.2) |
| [[SW 1271 (line)]] | alt | 89.5 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0720× (z -10.5) |
| [[SW480 (line)]] | alt | 17.9 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.53× (z +10.9) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 2.15× (z +9.4) | — |
| [[A549 (line)]] | wt | 20.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.149× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 36.3 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0641× (z -10.2) ⚠ toxic |
| [[H4 (line)]] | wt | 22.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -10.4) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 27.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -9.7) ⚠ cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 8.09 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 15.7× (z +12.2) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 50.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.342× (z -8.9) |
| [[AN3 CA (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.48 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.42 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.34 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.86 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 59.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.37 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 41.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 595), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAP6]] | +0.65 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[GNAO1]] | +0.60 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[ANKRD6]] | +0.58 | +0.59 / +0.57 | both halves | 9e-06 |  |
| [[SYN2]] | +0.56 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[CYS1]] | +0.56 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[HOMER2]] | +0.56 | +0.43 / +0.54 | both halves | 4e-05 |  |
| [[RASGEF1C]] | +0.55 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[FAM78B]] | +0.54 | +0.46 / +0.48 | both halves | 3e-05 |  |
| [[FAM124A]] | +0.54 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[CAMK2B]] | +0.54 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[PDZD4]] | +0.54 | +0.53 / +0.40 | both halves | 4e-05 |  |
| [[SLC45A1]] | +0.53 | +0.47 / +0.49 | both halves | 2e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[B9D2]] | -0.46 | -0.40 / -0.47 | both halves | 4e-05 |  |
| [[PTPRB]] | -0.45 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[PTPRR]] | -0.45 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[SYNRG]] | -0.45 | -0.27 / -0.46 | both halves | 3e-04 |  |
| [[GPRC5C]] | -0.43 | -0.34 / -0.41 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 15, C 0. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEPTIN3]] | B | SEPTIN3 activity raises MCF2L2's level | lines that do not express SEPTIN3 (13) vs lines expressing it (37) | 2.69× lower at baseline in the lines without SEPTIN3 | 0.021 | ⚠ within organs, on part of the lines; also absent: SRRM3, GNG4, SEPTIN5; maybe low, not absent |
| [[KIF26A]] | B | KIF26A activity raises MCF2L2's level | lines that do not express KIF26A (17) vs lines expressing it (33) | 1.94× lower at baseline in the lines without KIF26A | 0.027 | ⚠ within organs, on part of the lines; also absent: SRRM3, LAMC3, BEGAIN |
| [[MCOLN2]] | B | MCOLN2 activity strengthens MCF2L2's drug response | lines that do not express MCOLN2 (15) vs lines expressing it (28) | the lines without MCOLN2 respond 0.67× as strongly (z diff +1.40); strongest at Ouabain (Octahydrate) 5 µM: 0.89x vs 0.37x (z diff +5.9) | 0.034 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG; target measured in part of the lines; artifact flags |
| [[CHD5]] | B | CHD5 activity raises MCF2L2's level | lines that do not express CHD5 (30) vs lines expressing it (20) | 1.86× lower at baseline in the lines without CHD5 | 0.036 | ⚠ within organs, on part of the lines; also absent: DPYSL5, RET, KIF1A; maybe low, not absent |
| [[ANKRD6]] | B | ANKRD6 activity raises MCF2L2's level | lines that do not express ANKRD6 (16) vs lines expressing it (34) | 2.16× lower at baseline in the lines without ANKRD6 | 0.039 | ⚠ within organs, on part of the lines; also absent: MAP9, RIMKLB, TUB |
| [[ABCA3]] | B | ABCA3 activity raises MCF2L2's level | lines that do not express ABCA3 (9) vs lines expressing it (41) | 2.16× lower at baseline in the lines without ABCA3 | 0.048 | ⚠ within organs, on part of the lines; also absent: SLC37A1, CCDC88C, GRTP1; maybe low, not absent |
| [[GBX1]] | B | GBX1 activity raises MCF2L2's level | lines that do not express GBX1 (17) vs lines expressing it (33) | 1.82× lower at baseline in the lines without GBX1 | 0.067 | ⚠ within organs, on part of the lines; also absent: OLFML2A, FMNL1-DT, SCN5A; maybe low, not absent |
| [[DPYSL5]] | B | DPYSL5 activity raises MCF2L2's level | lines that do not express DPYSL5 (30) vs lines expressing it (20) | 2.12× lower at baseline in the lines without DPYSL5 | 0.079 | ⚠ within organs, on part of the lines; also absent: JPH3, OLFM1, CHD5 |
| [[STOX2]] | B | STOX2 activity raises MCF2L2's level | lines that do not express STOX2 (22) vs lines expressing it (28) | 2.28× lower at baseline in the lines without STOX2 | 0.081 | ⚠ within organs, on part of the lines; also absent: SLC47A1, RBM11, FBXO27 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers MCF2L2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[SLC4A3]] | B | SLC4A3 activity raises MCF2L2's level | lines that do not express SLC4A3 (8) vs lines expressing it (42) | 2.00× lower at baseline in the lines without SLC4A3 | 0.084 | ⚠ within organs, on part of the lines; also absent: SEMA6B, SLC29A4, MYO5A |
| [[FBXO27]] | B | FBXO27 activity raises MCF2L2's level | lines that do not express FBXO27 (28) vs lines expressing it (22) | 2.04× lower at baseline in the lines without FBXO27 | 0.089 | ⚠ within organs, on part of the lines; also absent: SLFN13, DLL3, PAX2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 102]] — Neuronal System; 45 genes; every member is in the + arm (projection on the module's main direction 0.557). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (5.1, 40.4); signed map (26.6, 29.5). **Vector** length 96.3, 21.9% of its response variance represented; |z| ≥ 3 in 1,082 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.1 | +13.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.7 | +10.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.3 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.0 | +11.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.2 | +7.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.4 | +3.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.7 | +3.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.4 | +2.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.1 | +3.5 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -3.8 | -3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.0 | -3.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.8 | -4.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.7 | -3.3 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -1.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.6 | -4.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.4 | -1.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.3 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | MCF.2 cell line derived transforming sequence-like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q27.1 — chr3:183,178,041-183,428,778 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0861, ARHGEF22 |
| Gene groups (HGNC) | Dbl family Rho GEFs; CRAL-TRIO lipid binding domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86YR7](https://www.uniprot.org/uniprotkb/Q86YR7) (Probable guanine nucleotide exchange factor MCF2L2):

> Probably functions as a guanine nucleotide exchange factor.

**Summary**, from NCBI Gene [23101](https://www.ncbi.nlm.nih.gov/gene/23101):

> Predicted to enable guanyl-nucleotide exchange factor activity. Predicted to be located in cytosol. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30319](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30319) · Entrez [23101](https://www.ncbi.nlm.nih.gov/gene/23101) · UniProt [Q86YR7](https://www.uniprot.org/uniprotkb/Q86YR7) · Ensembl [ENSG00000053524](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000053524)

## Data

Gene col 595: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 595); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 595, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 595]; `tensor/DDL_lfc|DDL_z.npy` [595]; `embed/gene_vectors.npy` [595]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 595 or target_col == 595). Every well: [[MCF2L2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MCF2L2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
