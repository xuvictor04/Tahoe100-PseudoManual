---
symbol: "BIRC3"
type: "gene"
col: 345
ensembl_id: "ENSG00000023445"
name: "baculoviral IAP repeat containing 3"
location: "11q22.2"
module: 139
arm: "+"
pooled_cpm: 234.3
n_lines_expressing: 45
n_dd_up: 43
n_dd_down: 28
n_dd_up_clean: 35
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 5
direction_downstream: 7
tags: ["gene", "module/139"]
generated_by: "tahoemap"
---

# BIRC3

*baculoviral IAP repeat containing 3* — 11q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 43 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 8.01× (z +50.1, q 0e+00, up in 43 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.465× (z -18.4, q 0e+00, down in 38 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TNFAIP3]] (+0.75, fdr 7e-06), [[CCL20]] (+0.74, fdr 7e-06), [[TXNIP]] (+0.64, fdr 1e-05); moves opposite to [[MTCH1]] (-0.55, fdr 1e-05), [[GDAP2]] (-0.53, fdr 1e-05), [[UFD1]] (-0.52, fdr 1e-05).
> It is in [[Module 139]], a single-armed module (Interleukin-4 and Interleukin-13 signaling).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[SNAI2]] → it (grade B ⚠); 7 go from it, the strongest it → [[SDC4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 51 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 43 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 345.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **8.01×** | +50.1 | 0e+00 | 43/43 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **9.79×** | +37.4 | 0e+00 | 43/43 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **5.41×** | +28.8 | 0e+00 | 43/43 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **5.21×** | +28.1 | 0e+00 | 43/43 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.09×** | +19.3 | 0e+00 | 39/43 (KATO III, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.15×** | +18.5 | 0e+00 | 39/43 (HT-29, A498, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.50×** | +15.6 | 0e+00 | 38/43 (KATO III, HOP62, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **4.31×** | +13.0 | 6e-37 | 39/44 (PANC-1, HS-578T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.14×** | +12.9 | 2e-36 | 41/43 (A549, SNU-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.91×** | +11.1 | 1e-26 | 37/43 (KATO III, BT-474, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.90×** | +11.0 | 3e-26 | 33/43 (J82, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.89×** | +10.9 | 5e-26 | 34/44 (HT-29, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.84×** | +10.4 | 9e-24 | 36/43 (BT-474, KATO III, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.81×** | +10.1 | 3e-22 | 28/43 (NCI-H460, J82, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.77×** | +9.7 | 1e-20 | 31/43 (J82, AsPC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.84×** | +9.7 | 2e-20 | 40/42 (A549, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.62×** | +8.2 | 7e-15 | 31/43 (J82, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.53×** | +7.0 | 9e-11 | 25/44 (NCI-H2347, SW 900, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.40×** | +5.8 | 2e-07 | 21/43 (NCI-H2347, HS-578T, …) | all doses, flat | position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | **1.37×** | +5.4 | 1e-06 | 25/43 (Panc 03.27, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 345.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.465×** | -18.4 | 0e+00 | 38/44 (PANC-1, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.473×** | -12.7 | 1e-34 | 37/43 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.538×** | -10.1 | 7e-22 | 39/43 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.555×** | -9.4 | 5e-19 | 37/43 (PANC-1, HT-29, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.677×** | -9.4 | 9e-19 | 32/43 (HEC-1-A, PANC-1, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.592×** | -8.9 | 5e-17 | 30/43 (A498, HT-29, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.370×** | -8.8 | 7e-17 | 38/40 (PANC-1, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.400×** | -8.1 | 3e-14 | 37/42 (PANC-1, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.617×** | -7.9 | 2e-13 | 33/45 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.635×** | -7.7 | 7e-13 | 39/44 (RKO, SNU-423, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.648×** | -7.4 | 9e-12 | 29/43 (A-427, NCI-H2030, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.695×** | -6.2 | 3e-08 | 28/43 (PANC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.690×** | -6.1 | 6e-08 | 28/42 (MIA PaCa-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.701×** | -6.0 | 8e-08 | 34/43 (HT-29, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.785×** | -5.8 | 3e-07 | 28/44 (COLO 205, MIA PaCa-2, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.626×** | -5.7 | 5e-07 | 32/43 (PANC-1, CFPAC-1, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.564×** | -5.1 | 1e-05 | 30/44 (PANC-1, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **0.772×** | -4.4 | 3e-04 | 26/43 (H4, SW 1271, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 345. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 345 | 30 (2 ⚠) | 6 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 5.21× (z +17.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.231× (z -22.3) |
| [[NCI-H2347 (line)]] | alt | 199 | 33 (4 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +33.8) | [[Auranofin (drug)]] 5 µM 0.310× (z -11.9) |
| [[HS-578T (line)]] | alt | 128 | 30 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.7× (z +30.4) | — |
| [[SW 900 (line)]] | alt | 277 | 27 (5 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.47× (z +20.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -11.7) |
| [[Hs 766T (line)]] | wt | 111 | 28 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.0× (z +28.9) | — |
| [[Panc 03.27 (line)]] | alt | 411 | 26 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 9.59× (z +31.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -14.2) |
| [[PANC-1 (line)]] | alt | 537 | 11 (2 ⚠) | 15 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 16.9× (z +54.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.163× (z -34.8) |
| [[A549 (line)]] | wt | 453 | 12 (2 ⚠) | 9 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.47× (z +34.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.203× (z -27.1) |
| [[CFPAC-1 (line)]] | alt | 540 | 15 (4 ⚠) | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.0× (z +41.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.327× (z -20.0) |
| [[NCI-H460 (line)]] | wt | 118 | 18 (8 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.95× (z +21.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -11.5) |
| [[AsPC-1 (line)]] | alt | 104 | 18 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 65.9× (z +39.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 487 | 7 (1 ⚠) | 10 (4 ⚠) | [[Harringtonine (drug)]] 0.5 µM 7.91× (z +19.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.232× (z -19.1) |
| [[LoVo (line)]] | wt | 101 | 14 (4 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 11.8× (z +34.8) | [[Ixazomib citrate (drug)]] 5 µM 0.360× (z -10.1) |
| [[NCI-H1573 (line)]] | alt | 598 | 10 (3 ⚠) | 6 (4 ⚠) | [[Harringtonine (drug)]] 5 µM 6.77× (z +19.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -13.0) |
| [[NCI-H2030 (line)]] | alt | 453 | 3 | 12 (4 ⚠) | [[Harringtonine (drug)]] 5 µM 6.39× (z +17.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -16.6) |
| [[RKO (line)]] | wt | 198 | 4 | 11 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.227× (z -18.7) |
| [[SW48 (line)]] | wt | 524 | 7 | 7 (3 ⚠) | [[Harringtonine (drug)]] 0.5 µM 19.3× (z +20.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.213× (z -14.8) |
| [[A-172 (line)]] | wt | 102 | 13 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.01× (z +24.5) | — |
| [[HEC-1-A (line)]] | alt | 248 | 8 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.57× (z +26.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -20.8) |
| [[J82 (line)]] | alt | 85.4 | 12 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.0× (z +32.6) | — |
| [[KATO III (line)]] | alt | 101 | 11 (5 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +26.1) | [[Ixazomib citrate (drug)]] 5 µM 0.307× (z -9.1) |
| [[NCI-H1792 (line)]] | alt | 328 | 9 (2 ⚠) | 3 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 6.75× (z +21.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -15.4) |
| [[H4 (line)]] | wt | 159 | 7 (1 ⚠) | 4 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 12.0× (z +18.4) | [[Ixazomib citrate (drug)]] 5 µM 0.190× (z -12.3) |
| [[HT-29 (line)]] | alt | 174 | 6 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 11.2× (z +29.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.222× (z -18.4) |
| [[BT-474 (line)]] | alt | 162 | 8 (4 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +22.8) | [[Dinaciclib (drug)]] 5 µM 0.161× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 127 | 10 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.1× (z +29.2) | — |
| [[hTERT-HPNE (line)]] | wt | 70.4 | 10 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.1× (z +22.7) | — |
| [[LS 180 (line)]] | wt | 107 | 9 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 7.99× (z +26.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.481× (z -9.2) |
| [[SNU-423 (line)]] | alt | 242 | 8 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +30.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -11.0) |
| [[NCI-H23 (line)]] | alt | 203 | 2 | 7 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.315× (z -15.2) |
| [[SNU-1 (line)]] | wt | 88.9 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +22.6) | — |
| [[COLO 205 (line)]] | alt | 121 | 6 (2 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.11× (z +22.9) | [[Ixazomib citrate (drug)]] 5 µM 0.203× (z -12.4) |
| [[RPMI-7951 (line)]] | alt | 111 | 6 | 0 | [[Harringtonine (drug)]] 5 µM 18.6× (z +22.0) | — |
| [[SW1417 (line)]] | alt | 96.4 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.0× (z +31.5) | — |
| [[A-427 (line)]] | wt | 773 | 3 | 2 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 6.30× (z +13.7) | [[Ponatinib (drug)]] 5 µM 0.265× (z -10.2) |
| [[SK-MEL-2 (line)]] | alt | 92.8 | 3 | 2 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 8.54× (z +14.5) | [[Selinexor (drug)]] 5 µM 0.317× (z -11.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 0.261× (z -9.1) |
| [[SW 1271 (line)]] | alt | 761 | 3 | 2 | [[Homoharringtonine (drug)]] 5 µM 6.99× (z +14.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.196× (z -11.8) |
| [[LOX-IMVI (line)]] | wt | 120 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.2× (z +27.3) | — |
| [[HCT15 (line)]] | alt | 106 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +10.1) | — |
| [[HepG2_C3A (line)]] | wt | 163 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.67× (z +17.5) | — |
| [[CHP-212 (line)]] | wt | 84.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.24× (z +11.2) | — |
| [[AN3 CA (line)]] | alt | 31.3 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 19.3 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 41.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 77.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.4 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 204 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 41.9 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 345), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNFAIP3]] | +0.75 | +0.74 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_KRAS_SIGNALING_UP; STRING 916 |
| [[CCL20]] | +0.74 | +0.72 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_KRAS_SIGNALING_UP; STRING 576 |
| [[TXNIP]] | +0.64 | +0.52 / +0.60 | both halves | 1e-05 | pathway: HALLMARK_APOPTOSIS |
| [[TIGD2]] | +0.64 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[BIRC2]] | +0.64 | +0.60 / +0.65 | both halves | 7e-06 | same gene group; pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 996; ⚠ same locus (7.8 kb, same strand: neighbours can correlate without regulation) |
| [[SAA2-SAA4]] | +0.63 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[NFKBIA]] | +0.63 | +0.63 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 827 |
| [[SAA2]] | +0.62 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[MT1A]] | +0.62 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[TIPARP]] | +0.62 | +0.56 / +0.60 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[SAA1]] | +0.62 | +0.57 / +0.59 | both halves | 1e-05 | pathway: MyD88-independent TLR4 cascade |
| [[EBI3]] | +0.62 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[MT2A]] | +0.60 | +0.52 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTCH1]] | -0.55 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[GDAP2]] | -0.53 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[UFD1]] | -0.52 | -0.51 / -0.58 | both halves | 1e-05 | pathway: Deubiquitination |
| [[FAM227A]] | -0.52 | -0.29 / -0.59 | both halves | 2e-04 |  |
| [[PSMB5]] | -0.52 | -0.43 / -0.50 | both halves | 3e-05 | pathway: Deubiquitination; STRING 447 |
| [[UNKL]] | -0.51 | -0.48 / -0.46 | both halves | 3e-05 | same gene group |
| [[UBFD1]] | -0.51 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[RNF139-DT]] | -0.51 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[ZFAND2A]] | -0.50 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[SERPINH1]] | -0.50 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[MBOAT7]] | -0.50 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[PPP1R26-AS1]] | -0.49 | -0.38 / -0.47 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SNAI2]] | B | SNAI2 activity lowers BIRC3's level | lines that do not express SNAI2 (23) vs lines expressing it (27) | 1.44× higher at baseline in the lines without SNAI2 | 0.034 | ⚠ within organs, on part of the lines; also absent: GNG2, LBH, PLAT |
| [[TOP2A]] | B | TOP2A activity raises BIRC3's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[JAK2]] | B | JAK2 activity raises BIRC3's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 5.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[NR3C1]] | B | NR3C1 activity raises BIRC3's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 6.4% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[NFKBIZ]] | C | NFKBIZ activity raises BIRC3's level | lines that do not express NFKBIZ (3) vs lines expressing it (47) | 3.82× lower at baseline in the lines without NFKBIZ | 0.062 | ⚠ few lines (3 vs 47); across organs; also absent: CPEB2, PKIA-AS1; maybe low, not absent |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SDC4]] | B | BIRC3 activity raises SDC4's level | lines that do not express BIRC3 (5) vs lines expressing it (45) | 4.85× lower at baseline in the lines without BIRC3 | 0.026 | ⚠ within organs, on part of the lines; also absent: LRRC8E, TRIM34, IFI35 |
| [[NFKBIA]] | B | BIRC3 activity raises NFKBIA's level | lines that do not express BIRC3 (5) vs lines expressing it (45) | 2.42× lower at baseline in the lines without BIRC3 | 0.036 | ⚠ within organs, on part of the lines; also absent: LRRC8E, TRIM34, IFI35 |
| [[ANGPTL4]] | B | BIRC3 activity raises ANGPTL4's level | lines that do not express BIRC3 (5) vs lines expressing it (45) | 3.72× lower at baseline in the lines without BIRC3 | 0.042 | ⚠ within organs, on part of the lines; also absent: LRRC8E, TRIM34, IFI35 |
| [[MBOAT7]] | B | BIRC3 activity raises MBOAT7's level | lines that do not express BIRC3 (5) vs lines expressing it (45) | 1.22× lower at baseline in the lines without BIRC3 | 0.062 | ⚠ within organs, on part of the lines; also absent: LRRC8E, TRIM34, IFI35 |
| [[LIFR]] | B | BIRC3 activity lowers LIFR's level | lines that do not express BIRC3 (5) vs lines expressing it (45) | 1.50× higher at baseline in the lines without BIRC3 | 0.078 | ⚠ within organs, on part of the lines; also absent: LRRC8E, TRIM34, IFI35 |
| [[ZC3H12A]] | B | BIRC3 activity raises ZC3H12A's level | lines that do not express BIRC3 (5) vs lines expressing it (45) | 2.66× lower at baseline in the lines without BIRC3 | 0.084 | ⚠ within organs, on part of the lines; also absent: LRRC8E, TRIM34, IFI35 |
| [[EREG]] | B | BIRC3 activity raises EREG's level | lines that do not express BIRC3 (5) vs lines expressing it (45) | 4.00× lower at baseline in the lines without BIRC3 | 0.094 | ⚠ within organs, on part of the lines; also absent: LRRC8E, TRIM34, IFI35 |

## Where it sits

- **Module**: [[Module 139]] — Interleukin-4 and Interleukin-13 signaling; 34 genes; every member is in the + arm (projection on the module's main direction 0.682). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.0, 9.8); signed map (13.1, 28.9). **Vector** length 151, 53.1% of its response variance represented; |z| ≥ 3 in 2,344 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +15.8 | +18.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +12.4 | +10.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +11.7 | +28.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.6 | +37.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +7.7 | +8.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +7.5 | +4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +7.1 | +12.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +6.7 | +9.7 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +5.7 | +7.0 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | -13.2 | -9.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -12.6 | -12.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -10.0 | -8.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -9.7 | -6.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.8 | -18.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -6.0 | -3.4 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -5.4 | -5.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -5.1 | -7.7 |

## What is on record

|  |  |
|---|---|
| Name | baculoviral IAP repeat containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q22.2 — chr11:102,317,484-102,339,403 (+) |
| Ensembl biotype | protein_coding |
| Also known as | cIAP2, hiap-1, MIHC, RNF49, MALT2, c-IAP2; previously API2 |
| Gene groups (HGNC) | Ring finger proteins; Baculoviral IAP repeat containing; Caspase recruitment domain containing; RING finger E3 ubiquitin protein ligases |
| Hallmark sets | APOPTOSIS, KRAS_SIGNALING_UP, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 24 pathways, smallest: TNF receptor superfamily (TNFSF) members mediating non-canonical NF-kB pathway; TICAM1, RIP1-mediated IKK complex recruitment; IKK complex recruitment mediated by RIP1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13489](https://www.uniprot.org/uniprotkb/Q13489) (Baculoviral IAP repeat-containing protein 3):

> Multi-functional protein which regulates not only caspases and apoptosis, but also modulates inflammatory signaling and immunity, mitogenic kinase signaling and cell proliferation, as well as cell invasion and metastasis. Acts as an E3 ubiquitin-protein ligase regulating NF-kappa-B signaling. Regulates both canonical and non-canonical NF-kappa-B signaling by acting in opposite directions: acts as a positive regulator of the canonical pathway and suppresses constitutive activation of …

**Summary**, from NCBI Gene [330](https://www.ncbi.nlm.nih.gov/gene/330):

> This gene encodes a member of the IAP family of proteins that inhibit apoptosis by binding to tumor necrosis factor receptor-associated factors TRAF1 and TRAF2, probably by interfering with activation of ICE-like proteases. The encoded protein inhibits apoptosis induced by serum deprivation but does not affect apoptosis resulting from exposure to menadione, a potent inducer of free radicals. It contains 3 baculovirus IAP repeats and a ring finger domain. Transcript variants encoding the same …

**Accessions** — [HGNC:591](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:591) · Entrez [330](https://www.ncbi.nlm.nih.gov/gene/330) · UniProt [Q13489](https://www.uniprot.org/uniprotkb/Q13489) · Ensembl [ENSG00000023445](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000023445)

## Data

Gene col 345: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 345); `tables/drug_effects.parquet` (81 rows, flagged included); `relations/gene_relations.parquet` (col_a == 345, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 345]; `tensor/DDL_lfc|DDL_z.npy` [345]; `embed/gene_vectors.npy` [345]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 345 or target_col == 345). Every well: [[BIRC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BIRC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
