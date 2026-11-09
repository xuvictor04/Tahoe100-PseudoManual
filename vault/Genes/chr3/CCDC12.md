---
symbol: "CCDC12"
type: "gene"
col: 8384
ensembl_id: "ENSG00000160799"
name: "coiled-coil domain containing 12"
location: "3p21.31"
module: 119
arm: "+"
pooled_cpm: 50.06
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 18
n_dd_up_clean: 11
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/119"]
generated_by: "tahoemap"
---

# CCDC12

*coiled-coil domain containing 12* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.64× (z +16.3, q 0e+00, up in 45 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.383× (z -23.2, q 0e+00, down in 45 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Epirubicin (hydrochloride) (drug)]] 5 µM: 0.494× (z -16.4, q 0e+00, down in 42 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[METTL16]] (+0.70, fdr 7e-06), [[GTF3C2]] (+0.67, fdr 7e-06), [[NGDN]] (+0.67, fdr 1e-05); moves opposite to [[RO60]] (-0.65, fdr 7e-06), [[MYBL1]] (-0.57, fdr 1e-05), [[PRKAR1A]] (-0.56, fdr 1e-05).
> It is in [[Module 119]], a single-armed module (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8384.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.64×** | +16.3 | 0e+00 | 45/49 (SW480, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.57×** | +10.8 | 7e-25 | 41/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.34×** | +10.8 | 1e-24 | 39/48 (SW480, HEC-1-A, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.41×** | +8.3 | 1e-14 | 39/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.42×** | +7.9 | 2e-13 | 35/48 (PANC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.33×** | +6.8 | 7e-10 | 26/48 (SW480, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.27×** | +5.7 | 1e-06 | 26/47 (MIA PaCa-2, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.24×** | +5.1 | 2e-05 | 22/48 (NCI-H2030, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.24×** | +5.1 | 2e-05 | 23/48 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.34×** | +5.1 | 2e-05 | 20/48 (PANC-1, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.20× | +4.4 | 6e-04 | 17/48 (NCI-H460, RKO, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **1.39×** | +4.1 | 0.002 | 13/48 (Hs 766T, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.04× | +3.3 | 0.044 | 0/49 | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.28×** | +3.2 | 0.062 | 12/43 (HEC-1-A, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.20×** | +3.1 | 0.062 | 10/48 (MIA PaCa-2, A549, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Piroxicam (drug)]] 0.05 µM |  | 1.13× | +3.0 | 0.095 | 6/48 (RPMI-7951, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8384.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.383×** | -23.2 | 0e+00 | 45/48 (A-427, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.392×** | -21.8 | 0e+00 | 38/42 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.494×** | -16.4 | 0e+00 | 42/49 (HOP62, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.518×** | -15.3 | 0e+00 | 38/48 (HOP62, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.550×** | -14.5 | 3e-45 | 46/48 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.569×** | -13.6 | 3e-40 | 44/48 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.596×** | -12.5 | 4e-34 | 42/48 (A498, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.652×** | -10.3 | 3e-23 | 42/48 (A498, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.735×** | -9.7 | 1e-20 | 36/48 (NCI-H1792, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.787×** | -7.1 | 8e-11 | 30/48 (A498, NCI-H2347, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **0.812×** | -6.4 | 7e-09 | 25/48 (NCI-H2347, A498, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.757×** | -6.2 | 2e-08 | 26/45 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.772×** | -6.0 | 7e-08 | 27/48 (J82, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.791×** | -5.7 | 5e-07 | 28/48 (A-172, SW48, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.804×** | -5.3 | 5e-06 | 25/48 (HOP62, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.810×** | -5.1 | 1e-05 | 21/48 (HS-578T, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.676×** | -4.9 | 3e-05 | 23/48 (SK-MEL-2, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.828×** | -4.6 | 2e-04 | 21/48 (HS-578T, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Terfenadine (drug)]] 0.5 µM |  | 0.848× | -4.0 | 0.002 | 14/48 (SW48, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8384. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 60.3 | 3 | 5 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.04× (z +11.5) | [[Dinaciclib (drug)]] 0.05 µM 0.140× (z -22.1) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -9.6) |
| [[PANC-1 (line)]] | alt | 41.2 | 2 | 6 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.64× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -18.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.467× (z -10.0) |
| [[NCI-H2347 (line)]] | alt | 76.0 | 1 | 6 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.88× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.192× (z -21.9) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -11.0) |
| [[SW480 (line)]] | alt | 68.9 | 2 | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.22× (z +15.9) | [[Dinaciclib (drug)]] 5 µM 0.280× (z -20.4) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -10.6) |
| [[A498 (line)]] | wt | 41.8 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.285× (z -14.0) |
| [[LS 180 (line)]] | wt | 54.2 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.04× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.205× (z -17.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 61.3 | 0 | 5 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.206× (z -15.2) |
| [[SW1417 (line)]] | alt | 84.6 | 1 | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.26× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.270× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.372× (z -12.0) |
| [[HS-578T (line)]] | alt | 55.3 | 0 | 4 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -11.8) |
| [[LOX-IMVI (line)]] | wt | 41.8 | 0 | 4 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -13.0) |
| [[RPMI-7951 (line)]] | alt | 62.3 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.192× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.286× (z -11.3) |
| [[A-172 (line)]] | wt | 35.4 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -10.3) |
| [[A-427 (line)]] | wt | 52.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0997× (z -23.9) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -8.6) |
| [[C32 (line)]] | wt | 41.8 | 1 | 2 | [[PH-797804 (drug)]] 5 µM 7.48× (z +8.6) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.240× (z -11.1) |
| [[H4 (line)]] | wt | 34.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.100× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.310× (z -10.4) |
| [[HOP62 (line)]] | alt | 42.2 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.212× (z -15.9) |
| [[J82 (line)]] | alt | 53.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.351× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.421× (z -9.7) |
| [[LoVo (line)]] | wt | 57.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.205× (z -18.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.396× (z -14.2) |
| [[Panc 03.27 (line)]] | alt | 56.0 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.72× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.283× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.392× (z -8.9) |
| [[RKO (line)]] | wt | 53.4 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.39× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.189× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -10.1) |
| [[SNU-423 (line)]] | alt | 41.0 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.193× (z -15.1) |
| [[SW48 (line)]] | wt | 57.7 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.96× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.283× (z -9.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 77.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -12.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 54.0 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -11.1) ⚠ cell-cycle shift, explains ~8% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.416× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 46.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -14.4) |
| [[NCI-H2030 (line)]] | alt | 63.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -13.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 56.8 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -9.7) |
| [[SW 900 (line)]] | alt | 44.0 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -9.7) |
| [[A549 (line)]] | wt | 38.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.374× (z -9.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 42.1 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.341× (z -8.6) |
| [[C-33 A (line)]] | alt | 58.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.212× (z -12.3) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 45.7 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.124× (z -8.6) ⚠ toxic |
| [[HT-29 (line)]] | alt | 43.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.227× (z -15.2) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 55.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.492× (z -8.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 36.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.313× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 27.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.30× (z +8.8) | — |
| [[NCI-H460 (line)]] | wt | 40.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.378× (z -11.0) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 71.1 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 55.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 46.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 37.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 69.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8384), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METTL16]] | +0.70 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[GTF3C2]] | +0.67 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[NGDN]] | +0.67 | +0.50 / +0.73 | both halves | 1e-05 |  |
| [[GPATCH3]] | +0.67 | +0.54 / +0.70 | both halves | 1e-05 |  |
| [[ZNF787]] | +0.66 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[EIF4E2]] | +0.66 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[NCBP2AS2]] | +0.65 | +0.38 / +0.68 | both halves | 6e-05 |  |
| [[AAR2]] | +0.65 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[EIF3CL]] | +0.65 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[TAF6L]] | +0.64 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[ZNF16]] | +0.64 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[CTU1]] | +0.64 | +0.60 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RO60]] | -0.65 | -0.70 / -0.67 | both halves | 7e-06 |  |
| [[MYBL1]] | -0.57 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[PRKAR1A]] | -0.56 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[NEMP1]] | -0.55 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[ARL5B]] | -0.52 | -0.39 / -0.51 | both halves | 6e-05 |  |
| [[NOTCH2NLB]] | -0.52 | -0.60 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises CCDC12's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 119]] — Mitochondrial ribosome-associated quality control; 41 genes; every member is in the + arm (projection on the module's main direction 0.715). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-33.2, -8.7); signed map (-14.3, -20.6). **Vector** length 98.6, 26.3% of its response variance represented; |z| ≥ 3 in 1,159 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +8.2 | +2.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.9 | +10.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.9 | +7.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.4 | +16.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.1 | +8.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.5 | +10.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.4 | +5.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.3 | +2.4 |
|  | [[EX229 (drug)]] 5 µM |  | +3.1 | +4.1 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.3 | -6.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.5 | -16.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.5 | -21.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.4 | -5.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.4 | -23.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | -7.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.0 | -0.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.0 | -2.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.9 | +0.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.9 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:46,921,726-46,982,010 (-) |
| Ensembl biotype | protein_coding |
| Also known as | cwf18, MGC23918 |
| Gene groups (HGNC) | Spliceosomal Bact complex; Spliceosomal C complex; Spliceosomal P complex |
| Reactome | 4 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

UniProt [Q8WUD4](https://www.uniprot.org/uniprotkb/Q8WUD4) carries no function annotation.

**Summary**, from NCBI Gene [151903](https://www.ncbi.nlm.nih.gov/gene/151903):

> Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28332](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28332) · Entrez [151903](https://www.ncbi.nlm.nih.gov/gene/151903) · UniProt [Q8WUD4](https://www.uniprot.org/uniprotkb/Q8WUD4) · Ensembl [ENSG00000160799](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160799)

## Data

Gene col 8384: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8384); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8384, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8384]; `tensor/DDL_lfc|DDL_z.npy` [8384]; `embed/gene_vectors.npy` [8384]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8384 or target_col == 8384). Every well: [[CCDC12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
