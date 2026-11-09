---
symbol: "PI4K2B"
type: "gene"
col: 449
ensembl_id: "ENSG00000038210"
name: "phosphatidylinositol 4-kinase type 2 beta"
location: "4p15.2"
module: 1
arm: "-"
pooled_cpm: 49.01
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 21
n_dd_up_clean: 9
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# PI4K2B

*phosphatidylinositol 4-kinase type 2 beta* — 4p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.99× (z +23.0, q 0e+00, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (10 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.651× (z -10.7, q 8e-24, down in 35 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 0.444× (z -10.5, q 2e-23, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DYRK4]] (+0.59, fdr 2e-05), [[CIAO2A]] (+0.56, fdr 3e-05), [[MICB]] (+0.56, fdr 2e-05); moves opposite to [[SERBP1]] (-0.60, fdr 1e-05), [[UTP14A]] (-0.55, fdr 1e-05), [[RIOK1]] (-0.53, fdr 4e-05).
> It sits in the **-** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 449.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.99×** | +23.0 | 0e+00 | 41/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +12.2 | 5e-32 | 40/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +9.2 | 5e-18 | 35/48 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +7.8 | 1e-12 | 29/48 (HEC-1-A, J82, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.31×** | +6.7 | 2e-09 | 27/48 (KATO III, LS 180, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.29×** | +6.3 | 2e-08 | 25/48 (LS 180, HOP62, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.29×** | +6.1 | 8e-08 | 27/47 (NCI-H1573, SW480, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.20×** | +4.9 | 7e-05 | 18/48 (SW480, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.23×** | +4.9 | 7e-05 | 22/48 (LS 180, A498, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.24×** | +4.8 | 7e-05 | 17/48 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.14× | +4.4 | 4e-04 | 11/48 (SW480, AsPC-1, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | 1.18× | +4.1 | 0.002 | 17/48 (RKO, PANC-1, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.16× | +4.0 | 0.003 | 11/48 (SW480, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 1.16× | +4.0 | 0.003 | 16/48 (NCI-H2347, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 1.17× | +4.0 | 0.003 | 14/48 (MIA PaCa-2, SW480, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.17× | +3.9 | 0.003 | 15/47 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.12× | +3.7 | 0.006 | 7/48 (RPMI-7951, NCI-H460, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.16× | +3.7 | 0.007 | 11/48 (KATO III, J82, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 13 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 449.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.651×** | -10.7 | 8e-24 | 35/48 (SW480, HEC-1-A, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.444×** | -10.5 | 2e-23 | 33/48 (MIA PaCa-2, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.654×** | -10.1 | 7e-22 | 32/47 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **0.745×** | -9.7 | 3e-20 | 30/47 (HS-578T, H4, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.490×** | -9.2 | 3e-18 | 31/49 (PANC-1, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.731×** | -7.8 | 6e-13 | 28/48 (SW480, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.739×** | -7.1 | 1e-10 | 25/47 (NCI-H2347, HEC-1-A, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.761×** | -6.8 | 8e-10 | 25/47 (PANC-1, H4, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.758×** | -6.6 | 2e-09 | 26/48 (HS-578T, RPMI-7951, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.790×** | -5.8 | 3e-07 | 23/48 (SW480, LS 180, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.789×** | -5.1 | 2e-05 | 21/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.682×** | -5.0 | 3e-05 | 23/48 (PANC-1, A-172, …) | rises with dose | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.693×** | -4.8 | 8e-05 | 17/36 (HS-578T, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.826×** | -4.7 | 8e-05 | 20/48 (H4, PANC-1, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.697×** | -4.7 | 1e-04 | 21/48 (SK-MEL-2, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.703×** | -4.6 | 2e-04 | 18/48 (HEC-1-A, SNU-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.843× | -4.2 | 7e-04 | 19/48 (NCI-H460, SW480, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.887× | -4.0 | 0.002 | 13/48 (CFPAC-1, COLO 205, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.846× | -4.0 | 0.002 | 18/48 (SNU-423, A498, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.741×** | -3.9 | 0.003 | 14/48 (PANC-1, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.867× | -3.6 | 0.009 | 14/48 (BT-474, KATO III, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.864× | -3.5 | 0.011 | 11/47 (COLO 205, BT-474, …) | rises with dose |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.827×** | -3.4 | 0.017 | 9/48 (Hs 766T, PANC-1, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 5 µM |  | 0.874× | -3.4 | 0.017 | 11/48 (PANC-1, A-427, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 449. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 53.9 | 3 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +17.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.461× (z -10.4) ⚠ cell-cycle shift, explains ~36% of this change |
| [[A498 (line)]] | wt | 84.0 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.424× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change |
| [[HS-578T (line)]] | alt | 47.5 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -18.4) ⚠ cell-cycle shift, explains ~72% of this change |
| [[NCI-H460 (line)]] | wt | 25.4 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.94× (z +14.8) | — |
| [[PANC-1 (line)]] | alt | 43.0 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.65× (z +8.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.433× (z -10.9) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.285× (z -8.6) |
| [[A-172 (line)]] | wt | 92.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -13.0) ⚠ cell-cycle shift, explains ~72% of this change |
| [[H4 (line)]] | wt | 67.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -13.2) ⚠ cell-cycle shift, explains ~72% of this change |
| [[HEC-1-A (line)]] | alt | 60.6 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +13.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.503× (z -8.5) ⚠ unreliable plate only |
| [[HOP62 (line)]] | alt | 47.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.355× (z -10.1) ⚠ cell-cycle shift, explains ~43% of this change |
| [[HT-29 (line)]] | alt | 34.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.63× (z +14.5) | — |
| [[J82 (line)]] | alt | 62.7 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +11.8) | — |
| [[RPMI-7951 (line)]] | alt | 57.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -12.1) ⚠ cell-cycle shift, explains ~72% of this change |
| [[A549 (line)]] | wt | 40.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.466× (z -9.6) ⚠ cell-cycle shift, explains ~72% of this change |
| [[AsPC-1 (line)]] | alt | 34.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +13.2) | — |
| [[CFPAC-1 (line)]] | alt | 46.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +9.4) | — |
| [[COLO 205 (line)]] | alt | 53.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.138× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 85.1 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0868× (z -11.4) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 51.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.64× (z +9.9) | — |
| [[KATO III (line)]] | alt | 36.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +8.9) | — |
| [[LoVo (line)]] | wt | 38.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.78× (z +16.6) | — |
| [[LOX-IMVI (line)]] | wt | 24.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +9.1) | — |
| [[LS 180 (line)]] | wt | 66.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +14.4) | — |
| [[NCI-H1792 (line)]] | alt | 46.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +8.7) | — |
| [[NCI-H2030 (line)]] | alt | 33.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +9.6) | — |
| [[NCI-H23 (line)]] | alt | 40.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -11.1) ⚠ cell-cycle shift, explains ~72% of this change |
| [[Panc 03.27 (line)]] | alt | 24.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.29× (z +11.2) | — |
| [[RKO (line)]] | wt | 32.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +9.5) | — |
| [[SNU-1 (line)]] | wt | 32.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -12.0) ⚠ cell-cycle shift, explains ~72% of this change |
| [[SNU-423 (line)]] | alt | 55.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +10.7) | — |
| [[SW1417 (line)]] | alt | 27.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.64× (z +10.2) | — |
| [[SW48 (line)]] | wt | 33.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.43× (z +9.7) | — |
| [[A-427 (line)]] | wt | 60.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 75.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 53.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 40.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 73.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 80.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 72.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 449), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DYRK4]] | +0.59 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[CIAO2A]] | +0.56 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[MICB]] | +0.56 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[SAP30L-AS1]] | +0.56 | +0.39 / +0.46 | both halves | 6e-05 |  |
| [[BABAM1]] | +0.53 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[METTL4]] | +0.53 | +0.42 / +0.39 | both halves | 5e-05 |  |
| [[RAB27A]] | +0.52 | +0.43 / +0.42 | both halves | 4e-05 |  |
| [[MICA]] | +0.52 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[ERAP2]] | +0.52 | +0.55 / +0.32 | both halves | 2e-04 |  |
| [[BTN3A3]] | +0.52 | +0.53 / +0.40 | both halves | 4e-05 |  |
| [[IFI27L1]] | +0.51 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[MFSD8]] | +0.51 | +0.43 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SERBP1]] | -0.60 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[UTP14A]] | -0.55 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[RIOK1]] | -0.53 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[NR4A1]] | -0.53 | -0.54 / -0.36 | both halves | 1e-04 |  |
| [[IER2]] | -0.53 | -0.53 / -0.36 | both halves | 1e-04 |  |
| [[DDX10]] | -0.53 | -0.38 / -0.57 | both halves | 6e-05 |  |
| [[CCDC57]] | -0.52 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[SMARCA4]] | -0.52 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[TMEM185B]] | -0.51 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[EGR1]] | -0.50 | -0.55 / -0.34 | both halves | 1e-04 |  |
| [[BTBD2]] | -0.49 | -0.41 / -0.27 | both halves | 3e-04 |  |
| [[EFNB2]] | -0.49 | -0.45 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PI4K2B's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **-** arm (projection on the module's main direction -0.319). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-24.4, -55.7); signed map (-22.1, -28.3). **Vector** length 103, 25.4% of its response variance represented; |z| ≥ 3 in 1,108 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.3 | +12.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.3 | +2.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +6.3 | +6.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +9.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +23.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +7.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.3 | +4.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.9 | +3.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.7 | +6.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | -4.8 | -9.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -0.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.4 | -10.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -4.4 | +3.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | +0.0 |
|  | [[EX229 (drug)]] 5 µM |  | -4.0 | -4.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | -0.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.2 | -7.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.0 | -10.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.7 | -5.0 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylinositol 4-kinase type 2 beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p15.2 — chr4:25,160,663-25,279,204 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PI4KIIB, FLJ11105, PIK42B |
| Gene groups (HGNC) | Minor histocompatibility antigens; Phosphatidylinositol 4-kinase type 2 family |
| Reactome | 7 pathways, smallest: Synthesis of PIPs at the ER membrane; Synthesis of PIPs at the early endosome membrane; Synthesis of PIPs at the Golgi membrane |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TCG2](https://www.uniprot.org/uniprotkb/Q8TCG2) (Phosphatidylinositol 4-kinase type 2-beta):

> Together with PI4K2A and the type III PI4Ks (PIK4CA and PIK4CB) it contributes to the overall PI4-kinase activity of the cell. This contribution may be especially significant in plasma membrane, endosomal and Golgi compartments. The phosphorylation of phosphatidylinositol (PI) to PI4P is the first committed step in the generation of phosphatidylinositol 4,5-bisphosphate (PIP2), a precursor of the second messenger inositol 1,4,5-trisphosphate (InsP3). Contributes to the production of InsP3 in …

**Summary**, from NCBI Gene [55300](https://www.ncbi.nlm.nih.gov/gene/55300):

> This gene encodes a member of the type II PI4 kinase protein family. The encoded protein is primarily cytosolic and contributes to overall PI4-kinase activity along with other protein family members. This protein is involved in early T cell activation. [provided by RefSeq, Dec 2016]

**Accessions** — [HGNC:18215](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18215) · Entrez [55300](https://www.ncbi.nlm.nih.gov/gene/55300) · UniProt [Q8TCG2](https://www.uniprot.org/uniprotkb/Q8TCG2) · Ensembl [ENSG00000038210](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000038210)

## Data

Gene col 449: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 449); `tables/drug_effects.parquet` (69 rows, flagged included); `relations/gene_relations.parquet` (col_a == 449, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 449]; `tensor/DDL_lfc|DDL_z.npy` [449]; `embed/gene_vectors.npy` [449]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 449 or target_col == 449). Every well: [[PI4K2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PI4K2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
