---
symbol: "BMP6"
type: "gene"
col: 7697
ensembl_id: "ENSG00000153162"
name: "bone morphogenetic protein 6"
location: "6p24.3"
module: 193
arm: "+"
pooled_cpm: 50.24
n_lines_expressing: 27
n_dd_up: 40
n_dd_down: 25
n_dd_up_clean: 30
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/193"]
generated_by: "tahoemap"
---

# BMP6

*bone morphogenetic protein 6* — 6p24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 40 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.13× (z +20.7, q 0e+00, up in 19 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (none with an alert); the strongest is [[Binimetinib (drug)]] 0.5 µM: 0.578× (z -9.6, q 3e-19, down in 20 of 25 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NR2E3]] (+0.74, fdr 7e-06), [[THSD4]] (+0.71, fdr 7e-06), [[CDCP1]] (+0.68, fdr 1e-05); moves opposite to [[TET2]] (-0.53, fdr 1e-04), [[PHC3]] (-0.52, fdr 3e-05), [[RPRD2]] (-0.52, fdr 3e-05).
> It is in [[Module 193]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NR2E3]] → it (grade B ⚠); 2 go from it, the strongest it → [[ALG12]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 40 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7697.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.13×** | +20.7 | 0e+00 | 19/25 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.64×** | +20.1 | 0e+00 | 17/25 (SW480, SK-MEL-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.84×** | +19.7 | 0e+00 | 19/25 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.68×** | +19.0 | 0e+00 | 18/24 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.15×** | +16.8 | 0e+00 | 17/25 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +10.8 | 3e-25 | 9/25 (SW480, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.93×** | +9.6 | 8e-20 | 11/24 (SW480, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.78×** | +8.4 | 3e-15 | 14/24 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.59×** | +6.7 | 9e-10 | 17/24 (AsPC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +6.2 | 2e-08 | 11/24 (NCI-H1792, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **1.52×** | +6.1 | 6e-08 | 0/22 | inconsistent across doses | composition shift |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.42×** | +5.1 | 1e-05 | 15/24 (AsPC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.42×** | +5.1 | 1e-05 | 13/24 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.42×** | +4.9 | 3e-05 | 5/25 (SW480, NCI-H1792, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.40×** | +4.9 | 4e-05 | 11/24 (AsPC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.26×** | +4.8 | 5e-05 | 12/25 (MIA PaCa-2, SK-MEL-2, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.38×** | +4.5 | 2e-04 | 15/24 (AsPC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.33×** | +4.2 | 8e-04 | 10/24 (BT-474, HS-578T, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Rapamycin (drug)]] 5 µM |  | **1.23×** | +4.2 | 9e-04 | 5/25 (AsPC-1, A-172, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.46×** | +4.0 | 0.002 | 5/25 (MIA PaCa-2, SW480, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7697.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Binimetinib (drug)]] 0.5 µM |  | **0.578×** | -9.6 | 3e-19 | 20/25 (AsPC-1, HepG2/C3A, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.555×** | -8.6 | 2e-15 | 19/24 (HepG2/C3A, AsPC-1, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.550×** | -8.4 | 8e-15 | 17/24 (AsPC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.676×** | -7.7 | 1e-12 | 17/25 (AsPC-1, HepG2/C3A, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.588×** | -7.5 | 9e-12 | 16/24 (AsPC-1, HepG2/C3A, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.613×** | -7.2 | 6e-11 | 16/25 (NCI-H23, AsPC-1, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.589×** | -7.2 | 6e-11 | 16/24 (AsPC-1, HepG2/C3A, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.629×** | -6.8 | 7e-10 | 16/24 (AsPC-1, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.691×** | -6.6 | 2e-09 | 16/25 (AsPC-1, HepG2/C3A, …) | all doses, flat | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.603×** | -6.6 | 3e-09 | 19/25 (AsPC-1, HepG2/C3A, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.726×** | -6.5 | 3e-09 | 13/25 (AsPC-1, HepG2/C3A, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **0.603×** | -6.5 | 4e-09 | 18/25 (AsPC-1, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.666×** | -6.3 | 1e-08 | 18/25 (AsPC-1, HepG2/C3A, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.765×** | -5.5 | 1e-06 | 13/25 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.902× | -5.2 | 8e-06 | 4/25 (NCI-H23, NCI-H2030, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | **0.830×** | -3.9 | 0.004 | 12/25 (AsPC-1, NCI-H23, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7697. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 198 | 4 (2 ⚠) | 23 (5 ⚠) | [[Mebendazole (drug)]] 5 µM 5.58× (z +9.4) | [[Binimetinib (drug)]] 0.5 µM 0.0422× (z -21.5) |
| [[HepG2_C3A (line)]] | wt | 44.7 | 0 | 12 (2 ⚠) | — | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.00929× (z -22.6) |
| [[A549 (line)]] | wt | 168 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0357× (z -25.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.183× (z -12.7) |
| [[NCI-H23 (line)]] | alt | 79.7 | 0 | 6 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.420× (z -20.6) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -11.8) |
| [[PANC-1 (line)]] | alt | 162 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -15.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -12.2) |
| [[SW480 (line)]] | alt | 13.4 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 7.30× (z +13.3) | — |
| [[A-427 (line)]] | wt | 17.4 | 4 | 1 | [[Panobinostat (drug)]] 5 µM 6.36× (z +10.4) | [[Cobimetinib (drug)]] 0.5 µM 0.190× (z -9.4) |
| [[LoVo (line)]] | wt | 23.3 | 0 | 5 (3 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.195× (z -10.4) |
| [[NCI-H2030 (line)]] | alt | 245 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.224× (z -16.3) |
| [[NCI-H460 (line)]] | wt | 182 | 1 (1 ⚠) | 4 (3 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 4.24× (z +8.6) ⚠ toxic | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -13.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -10.7) |
| [[MIA PaCa-2 (line)]] | alt | 14.4 | 2 | 2 (1 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 5.25× (z +10.5) | [[Adagrasib (drug)]] 0.05 µM 0.408× (z -14.7) ⚠ position not correctable · without an alert: [[Cobimetinib (drug)]] 0.5 µM 0.142× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 13.1 | 2 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 6.10× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -13.6) ⚠ cell-cycle shift, explains ~27% of this change |
| [[BT-474 (line)]] | alt | 20.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.07× (z +11.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 6.04× (z +9.8) | — |
| [[NCI-H1573 (line)]] | alt | 149 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0919× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 43.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0959× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 13.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.22× (z +9.1) | — |
| [[HS-578T (line)]] | alt | 13.4 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.19× (z +9.0) | — |
| [[NCI-H1792 (line)]] | alt | 30.3 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 5.52× (z +9.2) ⚠ toxic | — |
| [[Panc 03.27 (line)]] | alt | 12.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 8.19× (z +9.1) | — |
| [[SW1417 (line)]] | alt | 98.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -9.2) |
| [[A-172 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.57 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 12.5 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 7.65 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 7.67 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.79 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.29 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.05 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.70 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 11.8 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 6.44 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.92 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.66 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.91 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 6.93 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 7.14 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.59 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.01 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.19 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.42 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.34 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 9.03 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 60.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.67 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.26 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7697), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NR2E3]] | +0.74 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[THSD4]] | +0.71 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[CDCP1]] | +0.68 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[ITGA2]] | +0.66 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[DOCK4]] | +0.66 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[SLC35F3]] | +0.64 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[SEPTIN10]] | +0.63 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[PAQR5]] | +0.62 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[ASAP2]] | +0.61 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[CDH4]] | +0.61 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[DOCK5]] | +0.60 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[DUSP5]] | +0.60 | +0.61 / +0.49 | both halves | 2e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TET2]] | -0.53 | -0.36 / -0.51 | both halves | 1e-04 |  |
| [[PHC3]] | -0.52 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[RPRD2]] | -0.52 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[ALG12]] | -0.52 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[DNAJC27]] | -0.52 | -0.51 / -0.39 | both halves | 5e-05 |  |
| [[CYB561]] | -0.51 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[PRRT2]] | -0.50 | -0.43 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR2E3]] | B | NR2E3 activity raises BMP6's level | lines that do not express NR2E3 (23) vs lines expressing it (27) | 2.50× lower at baseline in the lines without NR2E3 | 0.056 | ⚠ within organs, on part of the lines; also absent: THSD4, SLC35F3, MPV17L |
| [[MAP2K1]] | B | MAP2K1 activity raises BMP6's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ALG12]] | B | BMP6 activity lowers ALG12's level | lines that do not express BMP6 (23) vs lines expressing it (27) | 1.17× higher at baseline in the lines without BMP6 | 0.043 | ⚠ within organs, on part of the lines; also absent: ENSG00000289418, LRRN2, LINC02864 |
| [[FMNL2]] | B | BMP6 activity raises FMNL2's level | lines that do not express BMP6 (23) vs lines expressing it (27) | 1.65× lower at baseline in the lines without BMP6 | 0.081 | ⚠ within organs, on part of the lines; also absent: ENSG00000289418, LRRN2, LINC02864 |

## Where it sits

- **Module**: [[Module 193]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.800). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (41.8, 8.5); signed map (8.5, 44.2). **Vector** length 106, 31.3% of its response variance represented; |z| ≥ 3 in 953 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.5 | +20.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.3 | +9.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.7 | +19.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.6 | +20.7 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +3.5 | +6.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.2 | +4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +8.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.8 | +4.8 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.6 | +4.9 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.7 | -7.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.2 | -8.6 |
|  | [[Trametinib (drug)]] 5 µM |  | -4.2 | -6.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -4.0 | -9.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.9 | -8.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.8 | -6.6 |

## What is on record

|  |  |
|---|---|
| Name | bone morphogenetic protein 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p24.3 — chr6:7,726,099-7,881,728 (+) |
| Ensembl biotype | protein_coding |
| Also known as | VGR1; previously VGR |
| Gene groups (HGNC) | Bone morphogenetic proteins |
| Hallmark sets | BILE_ACID_METABOLISM |
| Matched by | ensembl_id |

**Function**, from UniProt [P22004](https://www.uniprot.org/uniprotkb/P22004) (Bone morphogenetic protein 6):

> Growth factor of the TGF-beta superfamily that plays essential roles in many developmental processes including cartilage and bone formation. Also plays an important role in the regulation of HAMP/hepcidin expression and iron metabolism by acting as a ligand for hemojuvelin/HJV. Also acts to promote expression of HAMP, potentially via the interaction with its receptor BMPR1A/ALK3. Initiates the canonical BMP signaling cascade by associating with type I receptor ACVR1 and type II receptor ACVR2B. …

**Summary**, from NCBI Gene [654](https://www.ncbi.nlm.nih.gov/gene/654):

> This gene encodes a secreted ligand of the TGF-beta (transforming growth factor-beta) superfamily of proteins. Ligands of this family bind various TGF-beta receptors leading to recruitment and activation of SMAD family transcription factors that regulate gene expression. The encoded preproprotein is proteolytically processed to generate each subunit of the disulfide-linked homodimer. This protein regulates a wide range of biological processes including iron homeostasis, fat and bone …

**Accessions** — [HGNC:1073](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1073) · Entrez [654](https://www.ncbi.nlm.nih.gov/gene/654) · UniProt [P22004](https://www.uniprot.org/uniprotkb/P22004) · Ensembl [ENSG00000153162](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153162)

## Data

Gene col 7697: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7697); `tables/drug_effects.parquet` (66 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7697, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7697]; `tensor/DDL_lfc|DDL_z.npy` [7697]; `embed/gene_vectors.npy` [7697]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7697 or target_col == 7697). Every well: [[BMP6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BMP6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
