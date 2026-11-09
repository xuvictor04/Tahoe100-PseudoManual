---
symbol: "PON2"
type: "gene"
col: 2676
ensembl_id: "ENSG00000105854"
name: "paraoxonase 2"
location: "7q21.3"
module: 29
arm: "+"
pooled_cpm: 73.52
n_lines_expressing: 49
n_dd_up: 10
n_dd_down: 19
n_dd_up_clean: 5
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# PON2

*paraoxonase 2* — 7q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.11× (z +26.9, q 0e+00, up in 46 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.23× (z +6.9, q 1e-09, up in 21 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.327× (z -37.3, q 0e+00, down in 46 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FUCA2]] (+0.68, fdr 7e-06), [[TMEM123]] (+0.68, fdr 7e-06), [[CD99L2]] (+0.68, fdr 1e-05); moves opposite to [[DNTTIP1]] (-0.68, fdr 8e-06), [[ING2]] (-0.62, fdr 1e-05), [[PMM1]] (-0.61, fdr 2e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PON3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2676.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.11×** | +26.9 | 0e+00 | 46/47 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.72×** | +22.8 | 0e+00 | 38/41 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.22×** | +17.5 | 0e+00 | 40/44 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +6.9 | 1e-09 | 21/47 (A498, AsPC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +6.5 | 7e-09 | 22/45 (NCI-H2030, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.62×** | +6.0 | 2e-07 | 20/35 (HEC-1-A, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.23×** | +5.0 | 5e-05 | 19/48 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.21×** | +4.6 | 3e-04 | 19/47 (C32, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.21×** | +4.5 | 4e-04 | 23/47 (LoVo, AsPC-1, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~3% of this change | 1.20× | +4.2 | 0.001 | 16/47 (A549, SNU-423, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 1.18× | +3.8 | 0.007 | 13/48 (LoVo, AsPC-1, …) | rises with dose |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | 1.17× | +3.7 | 0.011 | 14/47 (LoVo, AsPC-1, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.11× | +3.7 | 0.011 | 16/47 (C32, SNU-423, …) | rises with dose | low cells (technical?) |
| [[Megestrol (drug)]] 5 µM |  | 1.11× | +3.5 | 0.019 | 7/48 (A549, NCI-H2347, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | 1.15× | +3.3 | 0.034 | 13/47 (LoVo, AsPC-1, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.15× | +3.2 | 0.042 | 16/47 (COLO 205, PANC-1, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | 1.10× | +3.1 | 0.053 | 6/47 (A-172, HepG2/C3A, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.27×** | +3.0 | 0.086 | 9/47 (C32, SNU-423, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2676.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.327×** | -37.3 | 0e+00 | 46/47 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.343×** | -25.2 | 0e+00 | 45/47 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.408×** | -21.1 | 0e+00 | 45/47 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.410×** | -21.0 | 0e+00 | 45/47 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.454×** | -18.6 | 0e+00 | 38/47 (RKO, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.611×** | -11.6 | 4e-29 | 38/47 (SW48, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.601×** | -11.6 | 5e-29 | 36/47 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.649×** | -10.2 | 2e-22 | 36/47 (PANC-1, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.755×** | -9.4 | 5e-19 | 29/48 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.668×** | -9.0 | 2e-17 | 30/47 (SW 900, AN3 CA, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.707×** | -8.2 | 2e-14 | 29/47 (A498, AsPC-1, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.741×** | -7.1 | 8e-11 | 25/47 (HepG2/C3A, SW48, …) | two highest doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.635×** | -5.6 | 9e-07 | 26/48 (PANC-1, C-33 A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.806×** | -5.1 | 2e-05 | 21/47 (A498, HepG2/C3A, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.811×** | -4.9 | 3e-05 | 23/47 (NCI-H460, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.696×** | -4.5 | 3e-04 | 21/46 (HT-29, NCI-H23, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2676. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 70.4 | 20 (2 ⚠) | 7 | [[Clobetasol propionate (drug)]] 0.05 µM 5.40× (z +16.5) | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -28.3) |
| [[AsPC-1 (line)]] | alt | 208 | 17 | 6 | [[Triamcinolone (drug)]] 5 µM 2.67× (z +14.4) | [[Panobinostat (drug)]] 0.5 µM 0.279× (z -13.2) |
| [[A549 (line)]] | wt | 187 | 7 (1 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 3.59× (z +11.1) ⚠ toxic; transcription drop · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 3.12× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -19.6) |
| [[NCI-H2030 (line)]] | alt | 128 | 4 (4 ⚠) | 8 | [[Dinaciclib (drug)]] 0.5 µM 2.51× (z +12.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -35.6) |
| [[PANC-1 (line)]] | alt | 77.9 | 3 (3 ⚠) | 8 | [[Dinaciclib (drug)]] 0.5 µM 3.61× (z +20.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -32.4) |
| [[A498 (line)]] | wt | 160 | 3 (3 ⚠) | 7 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.27× (z +16.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -25.9) |
| [[LS 180 (line)]] | wt | 134 | 3 (3 ⚠) | 7 | [[Dinaciclib (drug)]] 5 µM 2.87× (z +12.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -20.3) |
| [[NCI-H460 (line)]] | wt | 47.5 | 1 (1 ⚠) | 9 | [[Dinaciclib (drug)]] 0.5 µM 2.27× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -26.6) |
| [[HepG2_C3A (line)]] | wt | 117 | 1 (1 ⚠) | 8 | [[Dinaciclib (drug)]] 0.5 µM 2.64× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -24.6) |
| [[LOX-IMVI (line)]] | wt | 40.8 | 3 (3 ⚠) | 6 | [[Dinaciclib (drug)]] 0.5 µM 4.32× (z +14.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -22.6) |
| [[SW48 (line)]] | wt | 88.0 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -18.1) |
| [[SW480 (line)]] | alt | 80.1 | 1 (1 ⚠) | 8 | [[Dinaciclib (drug)]] 0.5 µM 2.22× (z +11.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.125× (z -29.7) |
| [[J82 (line)]] | alt | 33.5 | 2 (2 ⚠) | 6 | [[Dinaciclib (drug)]] 5 µM 3.34× (z +10.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -17.9) |
| [[SW 900 (line)]] | alt | 114 | 2 (2 ⚠) | 6 | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -18.8) |
| [[C-33 A (line)]] | alt | 78.7 | 3 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 3.16× (z +10.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.252× (z -13.5) |
| [[MIA PaCa-2 (line)]] | alt | 39.0 | 2 (2 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -14.1) |
| [[NCI-H23 (line)]] | alt | 62.5 | 1 (1 ⚠) | 6 | [[Dinaciclib (drug)]] 0.5 µM 3.54× (z +13.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -17.4) |
| [[RKO (line)]] | wt | 64.1 | 2 (2 ⚠) | 5 | [[Dinaciclib (drug)]] 0.05 µM 3.59× (z +10.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.0748× (z -23.4) |
| [[A-172 (line)]] | wt | 69.3 | 4 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.14× (z +11.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.85× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -11.8) |
| [[A-427 (line)]] | wt | 60.1 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 0.05 µM 2.75× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.324× (z -12.1) |
| [[C32 (line)]] | wt | 115 | 4 (4 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.06× (z +14.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -12.9) |
| [[H4 (line)]] | wt | 79.5 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -18.0) |
| [[HT-29 (line)]] | alt | 54.4 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 2.79× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -15.8) |
| [[NCI-H1573 (line)]] | alt | 58.0 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 5.11× (z +13.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -25.0) |
| [[HCT15 (line)]] | alt | 59.9 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 5.19× (z +12.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -9.5) |
| [[HS-578T (line)]] | alt | 53.8 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.91× (z +13.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -20.4) |
| [[SNU-423 (line)]] | alt | 38.7 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.55× (z +12.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -11.3) |
| [[AN3 CA (line)]] | alt | 160 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -14.0) |
| [[HEC-1-A (line)]] | alt | 51.4 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +11.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.456× (z -9.3) |
| [[HOP62 (line)]] | alt | 41.2 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.25× (z +14.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -16.2) |
| [[Hs 766T (line)]] | wt | 24.5 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.44× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -10.4) |
| [[Panc 03.27 (line)]] | alt | 36.3 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.39× (z +10.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.268× (z -11.7) |
| [[CFPAC-1 (line)]] | alt | 42.6 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +11.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -12.6) |
| [[NCI-H2347 (line)]] | alt | 114 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.46× (z +11.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -14.7) |
| [[SK-MEL-2 (line)]] | alt | 47.1 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.24× (z +13.9) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -9.5) |
| [[SNU-1 (line)]] | wt | 64.3 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.71× (z +10.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.240× (z -11.8) |
| [[SW1417 (line)]] | alt | 72.6 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.312× (z -14.9) |
| [[COLO 205 (line)]] | alt | 53.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -13.9) |
| [[hTERT-HPNE (line)]] | wt | 34.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.60× (z +9.3) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 47.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.13× (z +12.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -18.8) |
| [[SHP-77 (line)]] | alt | 28.2 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.226× (z -10.4) |
| [[BT-474 (line)]] | alt | 41.5 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.360× (z -8.8) |
| [[RPMI-7951 (line)]] | alt | 33.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -13.9) |
| [[CHP-212 (line)]] | wt | 43.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 68.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 67.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 65.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 72.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2676), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FUCA2]] | +0.68 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[TMEM123]] | +0.68 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[CD99L2]] | +0.68 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[PPT1]] | +0.68 | +0.65 / +0.68 | both halves | 7e-06 | pathway: Fatty acid metabolism |
| [[SH3BGRL]] | +0.63 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[ALDH5A1]] | +0.63 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[MRPL42]] | +0.62 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[STT3B]] | +0.61 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[EMB]] | +0.60 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[PRDX3]] | +0.60 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[PTGFRN]] | +0.60 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[DHX15]] | +0.60 | +0.48 / +0.61 | both halves | 2e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNTTIP1]] | -0.68 | -0.57 / -0.60 | both halves | 8e-06 |  |
| [[ING2]] | -0.62 | -0.51 / -0.62 | both halves | 1e-05 |  |
| [[PMM1]] | -0.61 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[ZNF324]] | -0.60 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[JMJD6]] | -0.58 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[RGP1]] | -0.58 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[POLD4]] | -0.57 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[FAM32A]] | -0.57 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[NOSIP]] | -0.57 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[KCTD5]] | -0.57 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[SRSF9]] ⚠ | -0.56 | -0.52 / -0.58 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[VRK3]] | -0.56 | -0.32 / -0.62 | both halves | 2e-04 |  |
| [[MYO9B]] | -0.56 | -0.31 / -0.57 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PON3]] | B | PON3 activity raises PON2's level | lines that do not express PON3 (22) vs lines expressing it (28) | 1.79× lower at baseline in the lines without PON3 | 0.049 | ⚠ within organs, on part of the lines; also absent: ESRP2, GOLT1A, ARHGEF5 |
| [[NFIA]] | B | NFIA activity strengthens PON2's drug response | lines that do not express NFIA (11) vs lines expressing it (37) | the lines without NFIA respond 0.85× as strongly (z diff +1.52); strongest at Panobinostat 0.5 µM: 0.56x vs 0.37x (z diff +3.8) | 0.081 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, PCAT7; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.726). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-26.4, -20.4); signed map (-21.9, -39.6). **Vector** length 112, 33.1% of its response variance represented; |z| ≥ 3 in 1,445 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.9 | +26.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.7 | +17.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.7 | +22.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.3 | +6.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.9 | +3.7 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +3.7 | +2.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.6 | +4.5 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +3.3 | +2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.9 | +2.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.8 | -8.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.5 | -11.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.2 | -11.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.1 | -37.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.7 | -18.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.4 | -2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.4 | -3.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.3 | -2.3 |
|  | [[vincristine (drug)]] 0.5 µM |  | -2.8 | +0.7 |

## What is on record

|  |  |
|---|---|
| Name | paraoxonase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.3 — chr7:95,404,862-95,435,329 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Paraoxonases |
| Reactome | 4 pathways, smallest: Synthesis of 5-eicosatetraenoic acids; Arachidonate metabolism; Fatty acid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15165](https://www.uniprot.org/uniprotkb/Q15165) (Serum paraoxonase/arylesterase 2):

> Capable of hydrolyzing lactones and a number of aromatic carboxylic acid esters. Has antioxidant activity. Is not associated with high density lipoprotein. Prevents LDL lipid peroxidation, reverses the oxidation of mildly oxidized LDL, and inhibits the ability of MM-LDL to induce monocyte chemotaxis.

**Summary**, from NCBI Gene [5445](https://www.ncbi.nlm.nih.gov/gene/5445):

> This gene encodes a member of the paraoxonase gene family, which includes three known members located adjacent to each other on the long arm of chromosome 7. The encoded protein is ubiquitously expressed in human tissues, membrane-bound, and may act as a cellular antioxidant, protecting cells from oxidative stress. Hydrolytic activity against acylhomoserine lactones, important bacterial quorum-sensing mediators, suggests the encoded protein may also play a role in defense responses to …

**Accessions** — [HGNC:9205](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9205) · Entrez [5445](https://www.ncbi.nlm.nih.gov/gene/5445) · UniProt [Q15165](https://www.uniprot.org/uniprotkb/Q15165) · Ensembl [ENSG00000105854](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105854)

## Data

Gene col 2676: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2676); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2676, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2676]; `tensor/DDL_lfc|DDL_z.npy` [2676]; `embed/gene_vectors.npy` [2676]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2676 or target_col == 2676). Every well: [[PON2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PON2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
