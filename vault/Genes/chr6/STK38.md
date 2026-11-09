---
symbol: "STK38"
type: "gene"
col: 3318
ensembl_id: "ENSG00000112079"
name: "serine/threonine kinase 38"
location: "6p21.31"
module: 54
arm: "+"
pooled_cpm: 92.9
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 13
n_dd_up_clean: 8
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# STK38

*serine/threonine kinase 38* — 6p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.38× (z +9.7, q 1e-19, up in 33 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.537× (z -19.7, q 0e+00, down in 46 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.674× (z -12.1, q 7e-32, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NPEPPS]] (+0.72, fdr 1e-05), [[RNF114]] (+0.64, fdr 1e-05), [[LSM2]] (+0.63, fdr 1e-05); moves opposite to [[EMG1]] (-0.65, fdr 1e-05), [[CYB5D1]] (-0.64, fdr 1e-05), [[KRT8P12]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3318.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.38×** | +9.7 | 1e-19 | 33/47 (AsPC-1, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.25×** | +7.2 | 2e-10 | 28/50 (AsPC-1, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.21×** | +6.0 | 4e-07 | 23/49 (AsPC-1, LoVo, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.15× | +5.8 | 9e-07 | 13/48 (AsPC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.21×** | +5.5 | 4e-06 | 19/48 (AsPC-1, SW480, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.17× | +5.5 | 5e-06 | 20/49 (MIA PaCa-2, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.15× | +5.4 | 5e-06 | 16/48 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.19× | +5.3 | 1e-05 | 21/48 (AsPC-1, LoVo, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.13× | +4.9 | 7e-05 | 12/49 (HEC-1-A, MIA PaCa-2, …) | all doses, flat |  |
| [[RMC-6236 (drug)]] 5 µM |  | **1.34×** | +4.8 | 8e-05 | 20/48 (AsPC-1, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.32×** | +4.6 | 2e-04 | 20/50 (AsPC-1, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 1.16× | +4.6 | 2e-04 | 19/47 (NCI-H2030, H4, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.32×** | +4.5 | 2e-04 | 17/49 (PANC-1, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +4.5 | 3e-04 | 19/48 (A-172, SHP-77, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 1.16× | +4.5 | 3e-04 | 14/49 (C32, Panc 03.27, …) | two highest doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.15× | +4.5 | 3e-04 | 18/47 (AsPC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 1.15× | +4.3 | 4e-04 | 16/48 (C-33 A, HS-578T, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.11× | +4.3 | 4e-04 | 9/48 (HEC-1-A, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[BI-3406 (drug)]] 0.5 µM |  | 1.19× | +3.9 | 0.003 | 14/49 (HOP62, AsPC-1, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3318.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.537×** | -19.7 | 0e+00 | 46/49 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.535×** | -19.1 | 0e+00 | 36/44 (SW480, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.549×** | -17.6 | 0e+00 | 36/45 (SNU-423, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.717×** | -14.9 | 0e+00 | 31/48 (Panc 03.27, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.674×** | -12.1 | 7e-32 | 37/48 (Panc 03.27, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.509×** | -11.2 | 4e-27 | 40/49 (HOP62, NCI-H23, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.805×** | -9.7 | 2e-20 | 28/49 (NCI-H2347, KATO III, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.769×** | -8.3 | 5e-15 | 29/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.782×** | -7.8 | 4e-13 | 33/48 (HEC-1-A, NCI-H23, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.635×** | -7.5 | 3e-12 | 29/48 (HOP62, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.803×** | -6.7 | 1e-09 | 26/48 (NCI-H1573, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.816×** | -6.4 | 6e-09 | 26/48 (Panc 03.27, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.948× | -5.8 | 3e-07 | 1/50 (SW 1088) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.836× | -5.7 | 6e-07 | 21/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.857× | -4.7 | 9e-05 | 20/48 (NCI-H1573, SW480, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.874× | -4.3 | 7e-04 | 15/48 (NCI-H2347, SK-MEL-2, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.788×** | -4.0 | 0.003 | 17/48 (SW1417, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.884× | -3.6 | 0.010 | 14/47 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3318. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 56.7 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -15.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.304× (z -13.5) |
| [[Panc 03.27 (line)]] | alt | 154 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -18.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.359× (z -14.5) |
| [[HOP62 (line)]] | alt | 101 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.393× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.237× (z -11.9) |
| [[KATO III (line)]] | alt | 152 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.267× (z -17.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -12.3) |
| [[NCI-H460 (line)]] | wt | 69.1 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.353× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.566× (z -8.9) |
| [[SW1417 (line)]] | alt | 133 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.538× (z -12.1) |
| [[AsPC-1 (line)]] | alt | 78.9 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -15.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.458× (z -8.6) |
| [[BT-474 (line)]] | alt | 107 | 0 | 4 (3 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.127× (z -12.9) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.570× (z -9.5) |
| [[CFPAC-1 (line)]] | alt | 91.9 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -17.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.495× (z -8.7) |
| [[LoVo (line)]] | wt | 98.1 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.487× (z -15.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.446× (z -11.6) |
| [[LOX-IMVI (line)]] | wt | 96.5 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.369× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.221× (z -9.6) |
| [[LS 180 (line)]] | wt | 88.4 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.243× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.464× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 119 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -22.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 126 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.304× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.221× (z -11.3) |
| [[SW480 (line)]] | alt | 117 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.146× (z -30.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.564× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 81.8 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -14.5) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SNU-423 (line)]] | alt | 127 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.322× (z -14.9) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 124 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.225× (z -10.9) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 80.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -18.5) ⚠ cell-cycle shift, explains ~25% of this change |
| [[HEC-1-A (line)]] | alt | 85.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.633× (z -9.6) |
| [[HepG2_C3A (line)]] | wt | 81.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.266× (z -12.6) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 99.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.430× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.458× (z -9.0) |
| [[HT-29 (line)]] | alt | 80.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.451× (z -9.5) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 70.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -12.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.400× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 107 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.337× (z -14.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 101 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.579× (z -12.9) |
| [[PANC-1 (line)]] | alt | 108 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.542× (z -11.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 78.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.339× (z -13.3) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 74.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.456× (z -11.8) ⚠ cell-cycle shift, explains ~25% of this change |
| [[HCT15 (line)]] | alt | 121 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.403× (z -10.8) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 76.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.177× (z -19.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 74.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.501× (z -8.9) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 72.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.412× (z -9.3) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 129 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.302× (z -12.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 68.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.140× (z -21.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 61.2 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0698× (z -10.0) ⚠ toxic |
| [[A-172 (line)]] | wt | 82.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 63.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 63.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 85.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 101 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 69.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 89.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 90.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 69.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 73.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 69.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 140 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3318), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPEPPS]] | +0.72 | +0.74 / +0.56 | both halves | 1e-05 |  |
| [[RNF114]] | +0.64 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[LSM2]] | +0.63 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[LAMTOR2]] | +0.62 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[ELF2]] | +0.62 | +0.69 / +0.52 | both halves | 1e-05 |  |
| [[CDC42SE2]] | +0.61 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[CBFA2T2]] | +0.60 | +0.63 / +0.46 | both halves | 2e-05 |  |
| [[PLEKHH3]] | +0.60 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[GNB2]] | +0.59 | +0.66 / +0.45 | both halves | 3e-05 |  |
| [[DPM3]] | +0.59 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[RNF38]] | +0.59 | +0.62 / +0.43 | both halves | 3e-05 |  |
| [[PIAS1]] | +0.58 | +0.63 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EMG1]] | -0.65 | -0.70 / -0.56 | both halves | 1e-05 |  |
| [[CYB5D1]] | -0.64 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[KRT8P12]] | -0.62 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[ZNF121]] | -0.61 | -0.64 / -0.54 | both halves | 1e-05 |  |
| [[MAK16]] | -0.61 | -0.67 / -0.48 | both halves | 2e-05 |  |
| [[SERPINB8]] | -0.60 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[DCTD]] | -0.59 | -0.47 / -0.60 | both halves | 2e-05 |  |
| [[ZNF597]] | -0.58 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[TRMT6]] | -0.58 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[TOMM34]] | -0.56 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[PNO1]] | -0.56 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[RLIM]] | -0.56 | -0.47 / -0.54 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **+** arm (projection on the module's main direction 0.544). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-16.0, -33.1); signed map (-29.6, 10.1). **Vector** length 103, 26.2% of its response variance represented; |z| ≥ 3 in 1,206 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +4.6 | +6.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.2 | +5.4 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | +4.1 | +7.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.1 | +9.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.0 | +5.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.7 | +5.5 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -8.4 | -17.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.6 | -12.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.9 | -19.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.7 | -19.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.3 | -9.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.3 | -7.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.9 | -4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -7.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.8 | -1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -5.7 |

## What is on record

|  |  |
|---|---|
| Name | serine/threonine kinase 38 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.31 — chr6:36,493,892-36,547,479 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NDR, NDR1 |
| Gene groups (HGNC) | Serine/threonine kinase 38 family |
| Reactome | 6 pathways, smallest: RHOBTB1 GTPase cycle; RHOBTB2 GTPase cycle; RHOBTB GTPase Cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15208](https://www.uniprot.org/uniprotkb/Q15208) (Serine/threonine-protein kinase 38):

> Serine/threonine-protein kinase that acts as a negative regulator of MAP3K1/2 signaling. Converts MAP3K2 from its phosphorylated form to its non-phosphorylated form and inhibits autophosphorylation of MAP3K2. Acts as an ufmylation 'reader' in a kinase-independent manner: specifically recognizes and binds mono-ufmylated histone H4 in response to DNA damage, promoting the recruitment of SUV39H1 to the double-strand breaks, resulting in ATM activation.

**Summary**, from NCBI Gene [11329](https://www.ncbi.nlm.nih.gov/gene/11329):

> This gene encodes a member of the AGC serine/threonine kinase family of proteins. The kinase activity of this protein is regulated by autophosphorylation and phosphorylation by other upstream kinases. This protein has been shown to function in the cell cycle and apoptosis. This protein has also been found to regulate the protein stability and transcriptional activity of the MYC oncogene. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Feb 2015]

**Accessions** — [HGNC:17847](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17847) · Entrez [11329](https://www.ncbi.nlm.nih.gov/gene/11329) · UniProt [Q15208](https://www.uniprot.org/uniprotkb/Q15208) · Ensembl [ENSG00000112079](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112079)

## Data

Gene col 3318: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3318); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3318, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3318]; `tensor/DDL_lfc|DDL_z.npy` [3318]; `embed/gene_vectors.npy` [3318]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3318 or target_col == 3318). Every well: [[STK38 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STK38.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
