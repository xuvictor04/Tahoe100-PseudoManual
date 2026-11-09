---
symbol: "PNP"
type: "gene"
col: 12685
ensembl_id: "ENSG00000198805"
name: "purine nucleoside phosphorylase"
location: "14q11.2"
module: 110
arm: "+"
pooled_cpm: 16.03
n_lines_expressing: 50
n_dd_up: 50
n_dd_down: 21
n_dd_up_clean: 25
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/110"]
generated_by: "tahoemap"
---

# PNP

*purine nucleoside phosphorylase* — 14q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 50 drug-doses (25 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.74× (z +18.5, q 0e+00, up in 42 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (2 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 0.608× (z -6.5, q 5e-08, down in 29 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CORO2B]] (+0.71, fdr 7e-06), [[NIPAL1]] (+0.66, fdr 7e-06), [[FXYD5]] (+0.66, fdr 1e-05); moves opposite to [[LSM14A]] (-0.65, fdr 7e-06), [[SETD2]] (-0.56, fdr 1e-05), [[RABGAP1]] (-0.55, fdr 1e-05).
> It is in [[Module 110]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 51 in all, 25 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 50 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 25 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12685.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.74×** | +18.5 | 0e+00 | 42/46 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **2.54×** | +12.1 | 5e-31 | 40/47 (LoVo, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **2.38×** | +11.2 | 6e-27 | 44/47 (LoVo, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.35×** | +11.1 | 2e-26 | 35/47 (NCI-H460, LS 180, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.76×** | +10.3 | 9e-23 | 30/47 (NCI-H1792, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **2.12×** | +9.7 | 2e-20 | 35/46 (NCI-H460, LS 180, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.06×** | +9.4 | 7e-19 | 37/47 (HT-29, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **2.05×** | +8.9 | 4e-17 | 33/45 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.96×** | +8.7 | 2e-16 | 34/47 (HT-29, CFPAC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.92×** | +8.4 | 2e-15 | 34/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.94×** | +8.3 | 8e-15 | 31/46 (SW480, NCI-H460, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.83×** | +7.8 | 3e-13 | 28/47 (C32, SNU-423, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **1.84×** | +7.6 | 1e-12 | 31/42 (SW480, NCI-H460, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.51×** | +7.5 | 3e-12 | 30/48 (SW480, SW1417, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.86×** | +7.1 | 5e-11 | 32/46 (HT-29, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.58×** | +5.9 | 1e-07 | 24/44 (HEC-1-A, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.32×** | +5.1 | 1e-05 | 23/48 (NCI-H1573, MIA PaCa-2, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.42×** | +4.5 | 1e-04 | 19/46 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.40×** | +4.2 | 6e-04 | 19/47 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.35×** | +3.9 | 0.002 | 15/45 (NCI-H1573, MIA PaCa-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.51×** | +3.8 | 0.002 | 16/48 (PANC-1, NCI-H2030, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.84×** | +3.7 | 0.004 | 10/46 (NCI-H1792, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.004 | 17/48 (PANC-1, HEC-1-A, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12685.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **0.608×** | -6.5 | 5e-08 | 29/47 (RKO, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.603×** | -6.3 | 7e-08 | 28/46 (RKO, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.578×** | -6.2 | 9e-08 | 30/48 (RKO, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.656×** | -5.5 | 5e-06 | 25/47 (MIA PaCa-2, NCI-H23, …) | rises with dose | position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.733×** | -5.3 | 1e-05 | 24/48 (NCI-H23, NCI-H1573, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.664×** | -4.9 | 7e-05 | 20/47 (RKO, C32, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.735×** | -4.9 | 7e-05 | 19/48 (RKO, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.761×** | -4.8 | 1e-04 | 25/48 (NCI-H23, RKO, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.731×** | -4.7 | 1e-04 | 23/48 (NCI-H23, RKO, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.696×** | -4.5 | 3e-04 | 22/47 (RKO, J82, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.692×** | -4.2 | 0.001 | 17/46 (NCI-H23, RKO, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.723×** | -4.2 | 0.001 | 20/47 (hTERT-HPNE, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.722×** | -4.1 | 0.002 | 18/48 (MIA PaCa-2, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.735×** | -4.0 | 0.002 | 17/47 (RKO, NCI-H1573, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.751×** | -3.7 | 0.007 | 13/47 (SW 1271, RPMI-7951, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.771×** | -3.4 | 0.022 | 12/47 (Panc 03.27, A549, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.73 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12685. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 16.3 | 9 (7 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.96× (z +13.7) | — |
| [[RKO (line)]] | wt | 47.0 | 0 | 7 (3 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.139× (z -13.1) |
| [[LoVo (line)]] | wt | 17.1 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.12× (z +13.9) | — |
| [[CFPAC-1 (line)]] | alt | 23.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +10.5) | — |
| [[HEC-1-A (line)]] | alt | 18.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.43× (z +13.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 26.8 | 0 | 2 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.477× (z -14.0) ⚠ position not correctable · without an alert: [[Binimetinib (drug)]] 5 µM 0.148× (z -9.4) |
| [[NCI-H23 (line)]] | alt | 27.3 | 0 | 2 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.451× (z -16.0) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 0.05 µM 0.338× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 13.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.07× (z +10.6) | — |
| [[SW1417 (line)]] | alt | 18.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +11.1) | — |
| [[SW480 (line)]] | alt | 10.6 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.06× (z +14.8) | — |
| [[A549 (line)]] | wt | 17.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.82× (z +13.7) | — |
| [[BT-474 (line)]] | alt | 21.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.53× (z +8.9) | — |
| [[C32 (line)]] | wt | 5.79 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.06× (z +9.0) | — |
| [[HCT15 (line)]] | alt | 21.2 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.114× (z -10.2) |
| [[hTERT-HPNE (line)]] | wt | 17.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.71× (z +9.1) | — |
| [[J82 (line)]] | alt | 14.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.28× (z +9.2) | — |
| [[KATO III (line)]] | alt | 12.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.08× (z +10.5) | — |
| [[LS 180 (line)]] | wt | 18.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.53× (z +13.6) | — |
| [[NCI-H1573 (line)]] | alt | 26.3 | 1 | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 2.76× (z +8.9) | — |
| [[NCI-H1792 (line)]] | alt | 13.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.42× (z +14.2) | — |
| [[NCI-H2347 (line)]] | alt | 16.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +8.8) | — |
| [[SNU-1 (line)]] | wt | 12.4 | 0 | 1 | — | [[Clotrimazole (drug)]] 0.5 µM 0.0733× (z -8.9) |
| [[A-172 (line)]] | wt | 7.60 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.38 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.22 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.22 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12685), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CORO2B]] | +0.71 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[NIPAL1]] | +0.66 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[FXYD5]] | +0.66 | +0.57 / +0.72 | both halves | 1e-05 |  |
| [[KCTD5]] | +0.66 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[UBASH3B]] | +0.65 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[LRRC8C]] | +0.65 | +0.55 / +0.68 | both halves | 1e-05 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[ITGA2-AS1]] | +0.64 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[KIAA1549L]] | +0.64 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[KCNC4]] | +0.64 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[KBTBD8]] | +0.64 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[LINC00941]] | +0.64 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[HBEGF]] | +0.64 | +0.62 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LSM14A]] | -0.65 | -0.58 / -0.64 | both halves | 7e-06 |  |
| [[SETD2]] | -0.56 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[RABGAP1]] | -0.55 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[SRRM1]] | -0.55 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[ZNF33A]] | -0.52 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[ZNF608]] | -0.52 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[TUT4]] | -0.51 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[RNF214]] | -0.51 | -0.38 / -0.56 | both halves | 7e-05 |  |
| [[ERP29]] | -0.50 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[ARFGEF2]] | -0.50 | -0.53 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises PNP's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ZNF608]] | B | ZNF608 activity lowers PNP's level | lines that do not express ZNF608 (12) vs lines expressing it (38) | 1.44× higher at baseline in the lines without ZNF608 | 0.082 | ⚠ within organs, on part of the lines; also absent: LINC01170, GDF15 |
| [[TOP2A]] | B | TOP2A activity lowers PNP's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 9.2% of all compounds | 0.095 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[BCL2A1]] | B | BCL2A1 activity weakens PNP's drug response | lines that do not express BCL2A1 (26) vs lines expressing it (22) | the lines without BCL2A1 respond 1.33× as strongly (z diff -1.06); strongest at Digitoxin 5 µM: 2.43x vs 1.57x (z diff -2.6) | 0.099 | ⚠ within organs, on part of the lines; also absent: BASP1-AS1, TMEM156, CSGALNACT1; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 110]]; 43 genes; every member is in the + arm (projection on the module's main direction 0.802). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.6, 3.8); signed map (4.5, 47.2). **Vector** length 91.3, 23.3% of its response variance represented; |z| ≥ 3 in 1,296 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +18.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +4.8 | +8.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +4.5 | +8.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.5 | +7.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | +4.1 | +7.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +3.4 |
|  | [[vincristine (drug)]] 0.5 µM |  | +3.1 | +3.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.9 | +4.2 |
|  | [[vincristine (drug)]] 5 µM |  | +2.7 | +2.4 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -4.3 | -6.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.8 | -4.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.7 | -4.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.7 | -6.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.5 | -4.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.3 | -4.9 |

## What is on record

|  |  |
|---|---|
| Name | purine nucleoside phosphorylase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q11.2 — chr14:20,461,992-20,477,094 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PUNP; previously NP |
| Hallmark sets | DNA_REPAIR, IL2_STAT5_SIGNALING, INTERFERON_GAMMA_RESPONSE, MTORC1_SIGNALING |
| Reactome | 35 pathways, smallest: Budding; Fusion and Uncoating of the Influenza Virion; Fusion of the Influenza Virion to the Host Cell Endosome |
| Matched by | ensembl_id |

**Function**, from UniProt [P00491](https://www.uniprot.org/uniprotkb/P00491) (Purine nucleoside phosphorylase):

> Catalyzes the phosphorolytic breakdown of the N-glycosidic bond in the beta-(deoxy)ribonucleoside molecules, with the formation of the corresponding free purine bases and pentose-1-phosphate. Preferentially acts on 6-oxopurine nucleosides including inosine and guanosine.

**Summary**, from NCBI Gene [4860](https://www.ncbi.nlm.nih.gov/gene/4860):

> This gene encodes an enzyme which reversibly catalyzes the phosphorolysis of purine nucleosides. The enzyme is trimeric, containing three identical subunits. Mutations which result in nucleoside phosphorylase deficiency result in defective T-cell (cell-mediated) immunity but can also affect B-cell immunity and antibody responses. Neurologic disorders may also be apparent in patients with immune defects. A known polymorphism at aa position 51 that does not affect enzyme activity has been …

**Accessions** — [HGNC:7892](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7892) · Entrez [4860](https://www.ncbi.nlm.nih.gov/gene/4860) · UniProt [P00491](https://www.uniprot.org/uniprotkb/P00491) · Ensembl [ENSG00000198805](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198805)

## Data

Gene col 12685: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12685); `tables/drug_effects.parquet` (74 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12685, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12685]; `tensor/DDL_lfc|DDL_z.npy` [12685]; `embed/gene_vectors.npy` [12685]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12685 or target_col == 12685). Every well: [[PNP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PNP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
