---
symbol: "ZRANB1"
type: "gene"
col: 317
ensembl_id: "ENSG00000019995"
name: "zinc finger RANBP2-type containing 1"
location: "10q26.13"
module: 74
arm: "+"
pooled_cpm: 91.43
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 5
n_dd_up_clean: 6
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# ZRANB1

*zinc finger RANBP2-type containing 1* — 10q26.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.07× (z +21.6, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.447× (z -16.3, q 0e+00, down in 41 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.837× (z -3.8, q 0.017, down in 22 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (A-427 0.0633×, SK-MEL-2 0.148×, Panc 03.27 0.257×, AsPC-1 0.267×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (A-427 0.111×, KATO III 0.129×, AsPC-1 0.196×, C-33 A 0.132×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (HS-578T 0.145×, SK-MEL-2 0.145×, C32 0.160×, SW1417 0.278×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 1 line (MIA PaCa-2 0.451×); [[Canagliflozin (drug)]] 0.05 µM in 1 line (SW48 0.328×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CEP350]] (+0.67, fdr 7e-06), [[AKAP9]] (+0.65, fdr 1e-05), [[NKAP]] (+0.64, fdr 1e-05); moves opposite to [[SORD]] (-0.61, fdr 1e-05), [[EFTUD2]] (-0.59, fdr 1e-05), [[ADAT2]] (-0.58, fdr 1e-05).
> It is in [[Module 074]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 317.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.07×** | +21.6 | 0e+00 | 44/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.70×** | +11.2 | 2e-26 | 42/48 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.45×** | +7.8 | 1e-12 | 37/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.75×** | +6.2 | 1e-07 | 34/49 (SW480, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.33×** | +5.8 | 1e-06 | 29/48 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.63×** | +5.4 | 7e-06 | 31/48 (C32, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.16× | +3.1 | 0.14 | 20/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.1 | 0.14 | 17/48 (LoVo, NCI-H460, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.1 | 0.14 | 18/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 317.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (A-427 0.0633×, SK-MEL-2 0.148×, Panc 03.27 0.257×, AsPC-1 0.267×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (A-427 0.111×, KATO III 0.129×, AsPC-1 0.196×, C-33 A 0.132×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (HS-578T 0.145×, SK-MEL-2 0.145×, C32 0.160×, SW1417 0.278×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 1 line (MIA PaCa-2 0.451×); [[Canagliflozin (drug)]] 0.05 µM in 1 line (SW48 0.328×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.447×** | -16.3 | 0e+00 | 41/44 (A-427, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.485×** | -15.2 | 0e+00 | 44/49 (A-427, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.488×** | -14.0 | 4e-42 | 40/45 (HS-578T, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.770×** | -5.3 | 2e-05 | 33/47 (SW1417, RKO, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Auranofin (drug)]] 5 µM |  | 0.837× | -3.8 | 0.017 | 22/48 (MIA PaCa-2, HEC-1-A, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.838× | -3.7 | 0.017 | 20/48 (AsPC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.732×** | -3.4 | 0.049 | 17/48 (MIA PaCa-2, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 0.854× | -3.3 | 0.060 | 13/48 (SW48, NCI-H1792, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.856× | -3.3 | 0.065 | 12/48 (AsPC-1, NCI-H460, …) | rises with dose |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.862× | -3.1 | 0.093 | 12/49 (NCI-H2030, KATO III, …) | inconsistent across doses |  |
| [[Pexidartinib (hydrochloride) (drug)]] 0.5 µM |  | 0.863× | -3.1 | 0.093 | 4/48 (LS 180, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.864× | -3.1 | 0.093 | 12/49 (HEC-1-A, COLO 205, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.959× | -3.1 | 0.097 | 0/50 | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.862× | -3.0 | 0.10 | 19/48 (AsPC-1, J82, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 317. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 88.4 | 7 (3 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +20.1) | [[Dinaciclib (drug)]] 0.5 µM 0.303× (z -15.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 104 | 5 (3 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.10× (z +16.0) | [[Dinaciclib (drug)]] 0.5 µM 0.498× (z -9.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 100.0 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +20.7) | [[Dinaciclib (drug)]] 5 µM 0.396× (z -12.4) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 88.4 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +13.1) | [[Dinaciclib (drug)]] 0.5 µM 0.284× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.451× (z -9.4) |
| [[NCI-H1573 (line)]] | alt | 111 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +17.8) | [[Dinaciclib (drug)]] 5 µM 0.341× (z -13.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 91.6 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.427× (z -10.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 78.3 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +22.4) | [[Dinaciclib (drug)]] 5 µM 0.448× (z -10.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 146 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.196× (z -18.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 60.6 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +11.5) | [[Dinaciclib (drug)]] 0.05 µM 0.160× (z -16.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 126 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +12.5) | [[Dinaciclib (drug)]] 0.05 µM 0.250× (z -15.0) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 103 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.320× (z -10.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 96.1 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +15.8) | [[Dinaciclib (drug)]] 0.5 µM 0.148× (z -21.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 137 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +10.3) | [[Dinaciclib (drug)]] 0.05 µM 0.270× (z -13.2) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 116 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +9.8) | [[Dinaciclib (drug)]] 0.05 µM 0.278× (z -15.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 99.9 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.278× (z -14.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 76.3 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +14.3) | [[Lonafarnib (drug)]] 5 µM 0.0658× (z -20.1) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 74.7 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.392× (z -10.3) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 71.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +17.2) | [[Dinaciclib (drug)]] 0.05 µM 0.145× (z -20.6) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 103 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.267× (z -15.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 81.2 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +15.3) | [[Dinaciclib (drug)]] 5 µM 0.129× (z -21.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 88.8 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.334× (z -11.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 93.5 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.255× (z -15.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 123 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -17.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 86.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0633× (z -34.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 72.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +16.0) | [[Dinaciclib (drug)]] 0.5 µM 0.365× (z -9.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 63.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +17.6) | — |
| [[NCI-H2030 (line)]] | alt | 94.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.407× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 60.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.422× (z -9.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 90.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +13.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.345× (z -10.9) ⚠ toxic |
| [[SW48 (line)]] | wt | 76.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.351× (z -9.0) ⚠ toxic; transcription drop · without an alert: [[Canagliflozin (drug)]] 0.05 µM 0.328× (z -8.8) |
| [[SW480 (line)]] | alt | 83.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +14.4) | — |
| [[A-172 (line)]] | wt | 47.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +9.2) | — |
| [[AN3 CA (line)]] | alt | 130 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.248× (z -9.2) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 96.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.132× (z -18.4) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 111 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.279× (z -8.8) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 119 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.370× (z -10.3) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 94.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +16.8) | — |
| [[J82 (line)]] | alt | 79.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +10.0) | — |
| [[LS 180 (line)]] | wt | 88.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +11.3) | — |
| [[RPMI-7951 (line)]] | alt | 67.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +14.2) | — |
| [[SHP-77 (line)]] | alt | 66.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.397× (z -8.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 75.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +12.1) | — |
| [[SNU-423 (line)]] | alt | 142 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.444× (z -9.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 161 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 90.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 78.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 77.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 317), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP350]] | +0.67 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[AKAP9]] | +0.65 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[NKAP]] | +0.64 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[GOLGB1]] | +0.62 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[RSF1]] | +0.62 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[SLU7]] | +0.61 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[SHOC2]] | +0.61 | +0.58 / +0.59 | both halves | 8e-06 |  |
| [[PNRC1]] | +0.60 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[GCC2]] | +0.60 | +0.50 / +0.60 | both halves | 1e-05 | STRING 423 |
| [[CCDC186]] | +0.59 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[FOXO3]] | +0.58 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[TMF1]] | +0.58 | +0.55 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SORD]] | -0.61 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[EFTUD2]] | -0.59 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[ADAT2]] | -0.58 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[LAPTM4B]] | -0.57 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[EMC1]] | -0.55 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[LINC03009]] | -0.54 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[PPT1]] | -0.53 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[NBL1]] | -0.53 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[VMA21]] | -0.53 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[RFT1]] | -0.53 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[SENP3]] | -0.53 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[MRPL42]] | -0.52 | -0.50 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.696). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-4.4, -47.4); signed map (-11.0, -4.0). **Vector** length 92.2, 24.4% of its response variance represented; |z| ≥ 3 in 895 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.4 | +21.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.1 | +1.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.0 | +11.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.6 | +2.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.5 | +5.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.3 | +2.8 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.2 | +1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.1 | +2.8 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.9 | -14.0 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -4.9 | -2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.6 | -3.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.4 | -3.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.1 | +0.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.2 | -2.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.2 | -3.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.7 | -0.4 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.7 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger RANBP2-type containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.13 — chr10:124,942,123-124,988,189 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TRABID |
| Gene groups (HGNC) | Zinc fingers RANBP2-type; OTU domain containing |
| Reactome | 4 pathways, smallest: Ovarian tumor domain proteases; Degradation of beta-catenin by the destruction complex; Deubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UGI0](https://www.uniprot.org/uniprotkb/Q9UGI0) (Ubiquitin thioesterase ZRANB1):

> Ubiquitin thioesterase, which specifically hydrolyzes 'Lys-29'-linked and 'Lys-33'-linked diubiquitin. Also cleaves 'Lys-63'-linked chains, but with 40-fold less efficiency compared to 'Lys-29'-linked ones. Positive regulator of the Wnt signaling pathway that deubiquitinates APC protein, a negative regulator of Wnt-mediated transcription. Acts as a regulator of autophagy by mediating deubiquitination of PIK3C3/VPS34, thereby promoting autophagosome maturation. Plays a role in the regulation of …

**Summary**, from NCBI Gene [54764](https://www.ncbi.nlm.nih.gov/gene/54764):

> Enables K63-linked polyubiquitin modification-dependent protein binding activity and cysteine-type deubiquitinase activity. Involved in positive regulation of Wnt signaling pathway and protein deubiquitination. Located in cytosol and nucleoplasm. Is active in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18224](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18224) · Entrez [54764](https://www.ncbi.nlm.nih.gov/gene/54764) · UniProt [Q9UGI0](https://www.uniprot.org/uniprotkb/Q9UGI0) · Ensembl [ENSG00000019995](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000019995)

## Data

Gene col 317: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 317); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 317, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 317]; `tensor/DDL_lfc|DDL_z.npy` [317]; `embed/gene_vectors.npy` [317]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 317 or target_col == 317). Every well: [[ZRANB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZRANB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
