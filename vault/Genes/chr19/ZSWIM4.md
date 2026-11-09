---
symbol: "ZSWIM4"
type: "gene"
col: 5266
ensembl_id: "ENSG00000132003"
name: "zinc finger SWIM-type containing 4"
location: "19p13.13"
module: 158
arm: "+"
pooled_cpm: 49.21
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 50
n_dd_up_clean: 11
n_dd_down_clean: 38
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/158"]
generated_by: "tahoemap"
---

# ZSWIM4

*zinc finger SWIM-type containing 4* — 19p13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.20× (z +20.1, q 0e+00, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 50 drug-doses (12 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.443× (z -14.7, q 0e+00, down in 46 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM: 0.556× (z -10.2, q 6e-22, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IER5]] (+0.70, fdr 7e-06), [[IER2]] (+0.63, fdr 7e-06), [[NFAT5]] (+0.61, fdr 1e-05); moves opposite to [[KDM1A]] (-0.57, fdr 1e-05), [[ABCB10]] (-0.55, fdr 1e-05), [[VDAC2]] (-0.54, fdr 5e-05).
> It is in [[Module 158]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5266.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.20×** | +20.1 | 0e+00 | 43/48 (A549, RKO, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.22×** | +13.8 | 4e-41 | 43/48 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.62×** | +8.7 | 6e-16 | 33/47 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.61×** | +8.7 | 7e-16 | 38/48 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +6.0 | 2e-07 | 24/48 (C32, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.37×** | +5.7 | 9e-07 | 26/48 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.35×** | +5.5 | 4e-06 | 24/48 (NCI-H460, A498, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.91×** | +5.1 | 2e-05 | 27/49 (LoVo, RPMI-7951, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.32×** | +5.1 | 2e-05 | 24/48 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.31×** | +4.9 | 5e-05 | 26/48 (HOP62, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[ULK-101 (drug)]] 0.05 µM |  | **1.29×** | +4.3 | 8e-04 | 19/49 (MIA PaCa-2, A-427, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.15× | +3.6 | 0.016 | 15/48 (Panc 03.27, NCI-H2030, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.21×** | +3.4 | 0.025 | 15/48 (LoVo, KATO III, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.20× | +3.3 | 0.042 | 13/48 (HOP62, A498, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.3 | 0.043 | 15/48 (PANC-1, LS 180, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.50×** | +3.2 | 0.045 | 17/48 (CFPAC-1, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.28×** | +3.2 | 0.045 | 17/48 (HCT15, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | 1.19× | +3.1 | 0.058 | 16/47 (Panc 03.27, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 62 in all, 15 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 50 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5266.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.443×** | -14.7 | 0e+00 | 46/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.445×** | -14.0 | 5e-42 | 25/38 (Panc 03.27, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.556×** | -10.2 | 6e-22 | 38/47 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.554×** | -9.8 | 1e-20 | 29/44 (A-172, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.600×** | -9.2 | 4e-18 | 41/49 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.590×** | -9.1 | 7e-18 | 35/47 (SW480, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.320×** | -9.0 | 2e-17 | 40/48 (NCI-H460, HepG2/C3A, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.641×** | -8.0 | 9e-14 | 31/48 (HEC-1-A, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **0.703×** | -7.9 | 1e-13 | 38/48 (SW480, BT-474, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.382×** | -7.6 | 2e-12 | 38/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.674×** | -7.3 | 1e-11 | 36/49 (BT-474, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.649×** | -7.2 | 4e-11 | 34/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.756×** | -7.1 | 7e-11 | 30/49 (PANC-1, MIA PaCa-2, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **0.412×** | -7.0 | 1e-10 | 36/48 (MIA PaCa-2, C-33 A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.413×** | -7.0 | 1e-10 | 39/48 (MIA PaCa-2, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.414×** | -7.0 | 1e-10 | 39/47 (NCI-H460, RKO, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.701×** | -6.4 | 6e-09 | 32/48 (RPMI-7951, HS-578T, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.782×** | -6.1 | 2e-08 | 28/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.713×** | -6.1 | 4e-08 | 27/48 (SNU-423, BT-474, …) | top dose only |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.722×** | -5.8 | 2e-07 | 26/48 (HOP62, AsPC-1, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5266. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 44.8 | 9 (3 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +15.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.190× (z -14.7) ⚠ unreliable plate only · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 0.377× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 75.3 | 0 | 8 (7 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.184× (z -15.9) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.123× (z -8.6) |
| [[HOP62 (line)]] | alt | 57.1 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.70× (z +12.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.300× (z -11.8) ⚠ unreliable plate only |
| [[BT-474 (line)]] | alt | 124 | 3 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.128× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Erlotinib (drug)]] 5 µM 0.258× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 76.8 | 2 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Cobimetinib (drug)]] 5 µM 0.378× (z -8.5) |
| [[A498 (line)]] | wt | 61.7 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 10.5× (z +25.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.16× (z +12.0) | — |
| [[SW480 (line)]] | alt | 36.8 | 0 | 5 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.266× (z -13.0) ⚠ unreliable plate only · without an alert: [[Cobimetinib (drug)]] 5 µM 0.343× (z -10.1) |
| [[A549 (line)]] | wt | 49.3 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +16.8) | [[Dinaciclib (drug)]] 5 µM 0.308× (z -9.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 45.3 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +13.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -11.8) ⚠ cell-cycle shift, explains ~22% of this change |
| [[RKO (line)]] | wt | 58.8 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +16.7) | [[Dinaciclib (drug)]] 0.5 µM 0.190× (z -12.4) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 40.4 | 1 | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 5.24× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.215× (z -12.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 55.1 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +14.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.340× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~49% of this change |
| [[Panc 03.27 (line)]] | alt | 114 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.192× (z -16.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 72.9 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.248× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.371× (z -8.6) |
| [[A-172 (line)]] | wt | 65.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +13.5) | [[Dinaciclib (drug)]] 0.05 µM 0.188× (z -13.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 41.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +12.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.229× (z -11.1) ⚠ unreliable plate only |
| [[C32 (line)]] | wt | 22.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +9.4) | — |
| [[HCT15 (line)]] | alt | 60.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.129× (z -14.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 28.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +9.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.289× (z -9.8) ⚠ unreliable plate only |
| [[NCI-H1573 (line)]] | alt | 67.3 | 0 | 2 (1 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.307× (z -10.1) |
| [[NCI-H23 (line)]] | alt | 51.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +9.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.333× (z -9.2) ⚠ unreliable plate only |
| [[RPMI-7951 (line)]] | alt | 75.7 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 3.11× (z +8.9) | — |
| [[A-427 (line)]] | wt | 37.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +10.2) | — |
| [[AN3 CA (line)]] | alt | 57.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.74× (z +10.0) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 36.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.138× (z -11.4) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 28.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +8.7) | — |
| [[CHP-212 (line)]] | wt | 38.2 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.120× (z -8.9) |
| [[H4 (line)]] | wt | 56.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +9.3) | — |
| [[HEC-1-A (line)]] | alt | 62.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.221× (z -15.4) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 34.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +9.9) | — |
| [[HS-578T (line)]] | alt | 64.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +12.0) | — |
| [[HT-29 (line)]] | alt | 29.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +8.6) | — |
| [[hTERT-HPNE (line)]] | wt | 36.8 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 4.89× (z +9.9) | — |
| [[J82 (line)]] | alt | 47.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +9.9) | — |
| [[LOX-IMVI (line)]] | wt | 25.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +10.5) | — |
| [[LS 180 (line)]] | wt | 22.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -10.4) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 55.6 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.07× (z +9.3) | — |
| [[SW1417 (line)]] | alt | 53.0 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.296× (z -10.5) ⚠ unreliable plate only |
| [[SW48 (line)]] | wt | 24.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +9.1) | — |
| [[COLO 205 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 65.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 37.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 56.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5266), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IER5]] | +0.70 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[IER2]] | +0.63 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[NFAT5]] | +0.61 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[ATG2A]] | +0.61 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[PIK3IP1-DT]] | +0.60 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[GOLT1A]] | +0.60 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[CLCF1]] | +0.60 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[WDR26]] | +0.60 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[FMNL1-DT]] | +0.59 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[MAFF]] | +0.59 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[DRAP1]] | +0.58 | +0.59 / +0.58 | both halves | 8e-06 |  |
| [[IER3]] | +0.58 | +0.57 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KDM1A]] | -0.57 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[ABCB10]] | -0.55 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[VDAC2]] | -0.54 | -0.40 / -0.57 | both halves | 5e-05 |  |
| [[MRS2]] | -0.54 | -0.64 / -0.45 | both halves | 3e-05 |  |
| [[TSN]] | -0.53 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[SKP2]] | -0.53 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[MRPS35]] | -0.53 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[WHAMMP1]] | -0.52 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[DERL1]] | -0.52 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[ARHGEF7]] | -0.52 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[CIPC]] | -0.52 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[FBXO7]] | -0.51 | -0.56 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises ZSWIM4's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 8.1% of all compounds | 0.042 | ⚠ off-target possible; 4 compounds |
| [[CLCF1]] | B | CLCF1 activity raises ZSWIM4's level | lines that do not express CLCF1 (7) vs lines expressing it (43) | 1.50× lower at baseline in the lines without CLCF1 | 0.044 | ⚠ within organs, on part of the lines; also absent: SIGIRR, ENSG00000256514, HTATIP2; maybe low, not absent |
| [[PHLDA2]] | B | PHLDA2 activity raises ZSWIM4's level | lines that do not express PHLDA2 (7) vs lines expressing it (43) | 1.40× lower at baseline in the lines without PHLDA2 | 0.063 | ⚠ within organs, on part of the lines; also absent: MET, TGFBR2, SDC4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 158]]; 27 genes; every member is in the + arm (projection on the module's main direction 0.635). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.1, 1.6); signed map (5.2, 25.3). **Vector** length 140, 45.6% of its response variance represented; |z| ≥ 3 in 1,679 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +9.0 | +13.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.5 | +20.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.4 | +4.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +6.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.9 | +3.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | +3.1 | +3.6 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | +2.8 | +4.3 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +2.8 | +2.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -11.1 | -14.7 |
|  | [[venetoclax (drug)]] 5 µM |  | -7.3 | -7.0 |
|  | [[EX229 (drug)]] 5 µM |  | -7.2 | -7.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -7.2 | -9.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -7.1 | -7.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -6.1 | -7.0 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger SWIM-type containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.13 — chr19:13,795,443-13,832,254 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12221 |
| Gene groups (HGNC) | Zinc fingers SWIM-type |
| Matched by | ensembl_id |

UniProt [Q9H7M6](https://www.uniprot.org/uniprotkb/Q9H7M6) carries no function annotation.

**Summary**, from NCBI Gene [65249](https://www.ncbi.nlm.nih.gov/gene/65249):

> Predicted to enable zinc ion binding activity. Predicted to be part of Cul2-RING ubiquitin ligase complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25704](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25704) · Entrez [65249](https://www.ncbi.nlm.nih.gov/gene/65249) · UniProt [Q9H7M6](https://www.uniprot.org/uniprotkb/Q9H7M6) · Ensembl [ENSG00000132003](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132003)

## Data

Gene col 5266: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5266); `tables/drug_effects.parquet` (81 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5266, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5266]; `tensor/DDL_lfc|DDL_z.npy` [5266]; `embed/gene_vectors.npy` [5266]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5266 or target_col == 5266). Every well: [[ZSWIM4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZSWIM4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
