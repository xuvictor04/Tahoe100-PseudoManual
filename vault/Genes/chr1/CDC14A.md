---
symbol: "CDC14A"
type: "gene"
col: 1252
ensembl_id: "ENSG00000079335"
name: "cell division cycle 14A"
location: "1p21.2"
module: 14
arm: "+"
pooled_cpm: 52.61
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 9
n_dd_up_clean: 20
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# CDC14A

*cell division cycle 14A* — 1p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.82× (z +38.1, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.448× (z -16.2, q 0e+00, down in 38 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.781× (z -4.8, q 2e-04, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NFKBID]] (+0.64, fdr 1e-05), [[LHFPL6]] (+0.63, fdr 1e-05), [[UVRAG]] (+0.62, fdr 7e-06); moves opposite to [[PSMD3]] (-0.61, fdr 3e-05), [[CLPB]] (-0.60, fdr 1e-05), [[ACSF3]] (-0.60, fdr 4e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1252.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.82×** | +38.1 | 0e+00 | 46/48 (CFPAC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.72×** | +28.4 | 0e+00 | 46/48 (AsPC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.19×** | +22.4 | 0e+00 | 45/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.56×** | +18.1 | 0e+00 | 43/47 (A-172, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.49×** | +17.6 | 0e+00 | 43/49 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.98×** | +13.7 | 5e-41 | 35/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.82×** | +12.0 | 5e-31 | 35/48 (SW1417, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.79×** | +11.7 | 1e-29 | 41/48 (PANC-1, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.78×** | +11.5 | 5e-29 | 34/47 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.72×** | +10.8 | 2e-25 | 39/48 (SW1417, LoVo, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.61×** | +9.5 | 8e-20 | 37/48 (PANC-1, LoVo, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.85×** | +9.4 | 2e-19 | 38/49 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.37×** | +8.9 | 3e-17 | 30/48 (PANC-1, SNU-423, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +8.1 | 2e-14 | 31/47 (PANC-1, HOP62, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +8.0 | 6e-14 | 32/48 (SW1417, HEC-1-A, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.45×** | +7.4 | 6e-12 | 35/47 (SW1417, LoVo, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.40×** | +6.8 | 4e-10 | 27/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.02×** | +6.4 | 6e-09 | 35/48 (PANC-1, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +5.9 | 8e-08 | 25/48 (LoVo, LS 180, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1252.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.448×** | -16.2 | 0e+00 | 38/47 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.450×** | -15.5 | 0e+00 | 36/43 (NCI-H1792, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.522×** | -12.1 | 2e-31 | 33/45 (C-33 A, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.682×** | -7.7 | 1e-12 | 32/47 (SW 900, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.781×** | -4.8 | 2e-04 | 25/48 (AN3 CA, HEC-1-A, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.810×** | -4.3 | 0.002 | 22/48 (Panc 03.27, SNU-423, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.821×** | -4.0 | 0.005 | 18/48 (SNU-423, HepG2/C3A, …) | two highest doses |  |
| [[Elimusertib hydrochloride (drug)]] 5 µM | ⚠ toxic | **0.668×** | -3.7 | 0.018 | 18/45 (MIA PaCa-2, COLO 205, …) | top dose only | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.950× | -3.5 | 0.025 | 0/49 | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.843× | -3.2 | 0.075 | 15/47 (NCI-H23, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.853× | -3.1 | 0.090 | 17/47 (NCI-H23, A549, …) | rises with dose |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **0.711×** | -3.1 | 0.090 | 12/43 (SK-MEL-2, HepG2/C3A, …) | top dose only | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | 0.802× | -3.0 | 0.11 | 13/48 (NCI-H460, HT-29, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1252. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 41.0 | 13 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.85× (z +23.6) | — |
| [[PANC-1 (line)]] | alt | 39.1 | 12 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.42× (z +28.6) | [[Dinaciclib (drug)]] 5 µM 0.414× (z -10.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 62.1 | 8 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +21.1) | [[Dinaciclib (drug)]] 0.5 µM 0.314× (z -12.2) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 69.1 | 8 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +18.7) | [[Dinaciclib (drug)]] 0.05 µM 0.298× (z -10.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 59.1 | 7 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +18.5) | [[Dinaciclib (drug)]] 0.5 µM 0.343× (z -9.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 26.7 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.13× (z +23.8) | — |
| [[NCI-H23 (line)]] | alt | 67.4 | 7 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +15.5) | [[Dinaciclib (drug)]] 5 µM 0.171× (z -16.3) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 82.6 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +19.2) | — |
| [[SW48 (line)]] | wt | 62.9 | 7 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.25× (z +17.6) | [[Dinaciclib (drug)]] 5 µM 0.122× (z -13.8) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 55.4 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +16.9) | — |
| [[LOX-IMVI (line)]] | wt | 62.0 | 4 (1 ⚠) | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.22× (z +16.5) | [[Dinaciclib (drug)]] 5 µM 0.360× (z -9.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 73.8 | 4 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +20.5) | [[Dinaciclib (drug)]] 0.05 µM 0.217× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.400× (z -8.9) |
| [[SW480 (line)]] | alt | 56.5 | 5 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.74× (z +19.6) | [[Dinaciclib (drug)]] 0.05 µM 0.354× (z -13.3) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 28.9 | 6 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.76× (z +11.8) | — |
| [[J82 (line)]] | alt | 48.1 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.26× (z +20.4) | — |
| [[NCI-H2347 (line)]] | alt | 51.1 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +22.5) | [[Dinaciclib (drug)]] 5 µM 0.273× (z -13.2) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 36.9 | 5 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.38× (z +16.1) | [[Saquinavir (drug)]] 0.5 µM 0.272× (z -8.8) |
| [[LoVo (line)]] | wt | 36.4 | 5 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.14× (z +16.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 45.2 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.89× (z +19.5) | — |
| [[NCI-H1792 (line)]] | alt | 52.2 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +17.2) | [[Dinaciclib (drug)]] 5 µM 0.104× (z -20.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 79.5 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +18.2) | [[Dinaciclib (drug)]] 5 µM 0.132× (z -18.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 70.9 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +13.8) | [[Dinaciclib (drug)]] 0.05 µM 0.142× (z -13.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 65.2 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.18× (z +20.8) | [[Dinaciclib (drug)]] 5 µM 0.269× (z -11.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 56.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.70× (z +19.7) | — |
| [[CFPAC-1 (line)]] | alt | 58.7 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.0× (z +31.9) | [[Dinaciclib (drug)]] 0.5 µM 0.322× (z -11.2) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 76.6 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.40× (z +12.7) | [[Dinaciclib (drug)]] 0.5 µM 0.238× (z -10.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 58.5 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.312× (z -10.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 33.1 | 3 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.78× (z +15.0) | [[Dinaciclib (drug)]] 5 µM 0.234× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 57.2 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +16.6) | [[Dinaciclib (drug)]] 0.5 µM 0.307× (z -11.2) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 52.0 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +12.1) | [[Docetaxel (drug)]] 0.05 µM 0.177× (z -12.4) ⚠ transcription drop |
| [[A-427 (line)]] | wt | 41.0 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +10.1) | [[Dinaciclib (drug)]] 0.05 µM 0.206× (z -13.7) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 76.4 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +9.5) | [[Dinaciclib (drug)]] 0.05 µM 0.111× (z -16.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 42.0 | 3 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.44× (z +10.8) | — |
| [[H4 (line)]] | wt | 34.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.13× (z +14.7) | — |
| [[hTERT-HPNE (line)]] | wt | 34.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.44× (z +15.8) | — |
| [[LS 180 (line)]] | wt | 43.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.07× (z +18.5) | — |
| [[SHP-77 (line)]] | alt | 53.0 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +12.6) | [[Dinaciclib (drug)]] 0.05 µM 0.316× (z -8.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 38.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.77× (z +20.1) | — |
| [[AN3 CA (line)]] | alt | 139 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.239× (z -9.5) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 29.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.55× (z +20.7) | — |
| [[CHP-212 (line)]] | wt | 38.5 | 0 | 2 (1 ⚠) | — | [[Cobimetinib (drug)]] 0.05 µM 0.0927× (z -8.8) |
| [[HCT15 (line)]] | alt | 90.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.250× (z -9.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 102 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +14.8) | — |
| [[COLO 205 (line)]] | alt | 19.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.32× (z +8.9) | — |
| [[HT-29 (line)]] | alt | 58.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +11.5) | — |
| [[NCI-H2122 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 76.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1252), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NFKBID]] | +0.64 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[LHFPL6]] | +0.63 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[UVRAG]] | +0.62 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[HOXB4]] | +0.61 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[ATP23]] | +0.60 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[PARP8]] | +0.60 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[ACVR2A]] | +0.58 | +0.45 / +0.65 | both halves | 3e-05 |  |
| [[ZNF821]] | +0.58 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[MAP3K1]] | +0.58 | +0.47 / +0.60 | both halves | 2e-05 | STRING 416 |
| [[TXNDC16]] | +0.58 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[TIFA]] | +0.57 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[IRF3]] | +0.57 | +0.46 / +0.52 | both halves | 3e-05 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD3]] | -0.61 | -0.56 / -0.45 | both halves | 3e-05 | pathway: APC/C-mediated degradation of cell cycle proteins |
| [[CLPB]] | -0.60 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[ACSF3]] | -0.60 | -0.42 / -0.62 | both halves | 4e-05 |  |
| [[SIN3B]] | -0.59 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[HERC2P3]] | -0.57 | -0.46 / -0.48 | both halves | 2e-05 |  |
| [[HERC2P2]] | -0.57 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[EP400]] | -0.56 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[MTG1]] | -0.55 | -0.54 / -0.37 | both halves | 8e-05 |  |
| [[HERC2]] | -0.55 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[MIER2]] | -0.55 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[EXOC2]] | -0.53 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[NUDC]] | -0.53 | -0.44 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CDC14A's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.491). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-1.1, -26.0); signed map (44.2, -0.3). **Vector** length 97.7, 28.4% of its response variance represented; |z| ≥ 3 in 1,376 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.7 | +28.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.2 | +18.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.8 | +17.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.6 | +22.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.7 | +8.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +8.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.0 | +3.6 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +2.4 | +1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +3.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.1 | +0.5 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -6.7 | -2.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -6.6 | -2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.3 | -4.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -5.8 | +7.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.5 | -4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.9 | -1.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.4 | -2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.1 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | cell division cycle 14A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p21.2 — chr1:100,345,001-100,520,277 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Cdc14A1, Cdc14A2, cdc14, DFNB105; previously DFNB32 |
| Gene groups (HGNC) | CDC14 phosphatases |
| Reactome | 7 pathways, smallest: Conversion from APC/C:Cdc20 to APC/C:Cdh1 in late anaphase; APC/C-mediated degradation of cell cycle proteins; MAPK6/MAPK4 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UNH5](https://www.uniprot.org/uniprotkb/Q9UNH5) (Dual specificity protein phosphatase CDC14A):

> Dual-specificity phosphatase. Required for centrosome separation and productive cytokinesis during cell division. Dephosphorylates SIRT2 around early anaphase. May dephosphorylate the APC subunit FZR1/CDH1, thereby promoting APC-FZR1 dependent degradation of mitotic cyclins and subsequent exit from mitosis. Required for normal hearing.

**Summary**, from NCBI Gene [8556](https://www.ncbi.nlm.nih.gov/gene/8556):

> The protein encoded by this gene is a member of the dual specificity protein tyrosine phosphatase family. It is highly similar to Saccharomyces cerevisiae Cdc14, a protein tyrosine phosphatase involved in the exit of cell mitosis and initiation of DNA replication, suggesting a role in cell cycle control. This protein has been shown to interact with, and dephosphorylate tumor suppressor protein p53, and is thought to regulate the function of p53. Alternative splicing of this gene results in …

**Accessions** — [HGNC:1718](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1718) · Entrez [8556](https://www.ncbi.nlm.nih.gov/gene/8556) · UniProt [Q9UNH5](https://www.uniprot.org/uniprotkb/Q9UNH5) · Ensembl [ENSG00000079335](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000079335)

## Data

Gene col 1252: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1252); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1252, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1252]; `tensor/DDL_lfc|DDL_z.npy` [1252]; `embed/gene_vectors.npy` [1252]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1252 or target_col == 1252). Every well: [[CDC14A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDC14A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
