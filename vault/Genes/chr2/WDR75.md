---
symbol: "WDR75"
type: "gene"
col: 3667
ensembl_id: "ENSG00000115368"
name: "WD repeat domain 75"
location: "2q32.2"
module: 1
arm: "+"
pooled_cpm: 71.14
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 5
n_dd_up_clean: 18
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# WDR75

*WD repeat domain 75* — 2q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.42× (z +30.3, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.578× (z -12.3, q 6e-32, down in 34 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.744× (z -10.1, q 7e-22, down in 30 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 9 lines (RKO 0.278×, SNU-1 0.192×, SW1417 0.492×, LoVo 0.544×, …); [[Dinaciclib (drug)]] 0.05 µM in 6 lines (SHP-77 0.136×, NCI-H460 0.352×, RKO 0.332×, HEC-1-A 0.313×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H1573 0.113×, CHP-212 0.105×, SW480 0.477×, A-427 0.317×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 2 lines (RKO 0.428×, SW48 0.405×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPL15]] (+0.73, fdr 7e-06), [[TIMM9]] (+0.72, fdr 7e-06), [[ZNF330]] (+0.68, fdr 7e-06); moves opposite to [[NUCB1]] (-0.66, fdr 1e-05), [[SKP1]] (-0.56, fdr 5e-05), [[MTPN]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[WHRN]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3667.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.42×** | +30.3 | 0e+00 | 47/48 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.42×** | +21.5 | 0e+00 | 44/48 (A-172, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.04×** | +16.7 | 0e+00 | 44/48 (NCI-H460, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.58×** | +11.2 | 8e-27 | 39/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.56×** | +10.8 | 4e-25 | 35/48 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.51×** | +10.0 | 2e-21 | 42/48 (SW480, MIA PaCa-2, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +9.8 | 6e-21 | 37/47 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.42×** | +8.6 | 8e-16 | 37/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.41×** | +8.4 | 3e-15 | 34/48 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.38×** | +7.7 | 6e-13 | 35/48 (LOX-IMVI, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.36×** | +7.5 | 2e-12 | 27/48 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.22×** | +6.7 | 9e-10 | 23/48 (NCI-H2347, CFPAC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +6.7 | 1e-09 | 32/47 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +6.0 | 6e-08 | 19/48 (LoVo, NCI-H2347, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.58×** | +5.8 | 2e-07 | 29/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.37×** | +5.5 | 2e-06 | 30/48 (A498, NCI-H2030, …) | two highest doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.48×** | +5.0 | 2e-05 | 26/48 (A498, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.46×** | +4.8 | 4e-05 | 24/48 (MIA PaCa-2, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.22×** | +4.5 | 2e-04 | 23/47 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3667.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 9 lines (RKO 0.278×, SNU-1 0.192×, SW1417 0.492×, LoVo 0.544×, …); [[Dinaciclib (drug)]] 0.05 µM in 6 lines (SHP-77 0.136×, NCI-H460 0.352×, RKO 0.332×, HEC-1-A 0.313×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H1573 0.113×, CHP-212 0.105×, SW480 0.477×, A-427 0.317×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 2 lines (RKO 0.428×, SW48 0.405×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.578×** | -12.3 | 6e-32 | 34/45 (SHP-77, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.621×** | -11.1 | 4e-26 | 32/43 (NCI-H1573, CHP-212, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.653×** | -10.3 | 9e-23 | 31/49 (LOX-IMVI, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.744×** | -10.1 | 7e-22 | 30/48 (RKO, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.728×** | -7.7 | 2e-12 | 31/48 (RKO, SW48, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.939× | -5.2 | 2e-05 | 0/50 | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.861× | -3.6 | 0.026 | 12/48 (C-33 A, NCI-H2030, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 0.860× | -3.5 | 0.032 | 15/47 (RKO, AsPC-1, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.871× | -3.3 | 0.055 | 10/48 (PANC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Omeprazole (drug)]] 0.05 µM |  | 0.876× | -3.2 | 0.075 | 9/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.879× | -3.1 | 0.093 | 14/48 (SW48, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3667. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 58.6 | 8 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +13.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.544× (z -12.0) |
| [[NCI-H460 (line)]] | wt | 92.0 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +23.4) | [[Dinaciclib (drug)]] 0.05 µM 0.352× (z -13.2) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 61.3 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.96× (z +21.7) | [[Dinaciclib (drug)]] 0.05 µM 0.301× (z -9.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 90.2 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.76× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.277× (z -14.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 105 | 1 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -23.4) |
| [[NCI-H1573 (line)]] | alt | 61.1 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +15.0) | [[Dinaciclib (drug)]] 5 µM 0.113× (z -21.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.527× (z -9.1) |
| [[PANC-1 (line)]] | alt | 95.8 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +18.2) | [[Dinaciclib (drug)]] 5 µM 0.497× (z -10.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 55.0 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.57× (z +24.2) | [[Dinaciclib (drug)]] 5 µM 0.368× (z -8.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 84.1 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +22.3) | [[Dinaciclib (drug)]] 0.5 µM 0.376× (z -11.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 57.5 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +22.3) | [[Dinaciclib (drug)]] 0.05 µM 0.313× (z -12.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 55.3 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +18.7) | [[Dinaciclib (drug)]] 0.05 µM 0.360× (z -10.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 60.4 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +16.5) | [[Dinaciclib (drug)]] 0.05 µM 0.390× (z -9.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.545× (z -8.9) |
| [[SW48 (line)]] | wt | 105 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.355× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.405× (z -8.7) |
| [[SW480 (line)]] | alt | 82.5 | 3 (1 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 1.96× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.477× (z -12.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 106 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +19.4) | [[Dinaciclib (drug)]] 0.5 µM 0.478× (z -10.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 43.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +19.4) | — |
| [[H4 (line)]] | wt | 78.4 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +14.0) | [[Dinaciclib (drug)]] 5 µM 0.292× (z -9.3) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 69.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +21.8) | — |
| [[KATO III (line)]] | alt | 48.6 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.517× (z -9.9) |
| [[LS 180 (line)]] | wt | 63.2 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +14.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -11.5) |
| [[NCI-H1792 (line)]] | alt | 69.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +21.0) | — |
| [[NCI-H2030 (line)]] | alt | 89.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +14.2) | [[Dinaciclib (drug)]] 5 µM 0.455× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 40.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +16.1) | — |
| [[Panc 03.27 (line)]] | alt | 61.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +12.9) | — |
| [[RPMI-7951 (line)]] | alt | 73.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +14.3) | — |
| [[SNU-1 (line)]] | wt | 60.9 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.192× (z -17.3) |
| [[SW 900 (line)]] | alt | 58.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +13.6) | — |
| [[A-427 (line)]] | wt | 78.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.317× (z -12.6) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 57.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +14.6) | — |
| [[C32 (line)]] | wt | 42.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +12.8) | [[Dinaciclib (drug)]] 0.05 µM 0.214× (z -11.8) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 52.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +13.9) | — |
| [[HS-578T (line)]] | alt | 53.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +10.5) | — |
| [[HT-29 (line)]] | alt | 45.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +14.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 106 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +13.4) | — |
| [[NCI-H23 (line)]] | alt | 104 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.36× (z +11.2) | [[Dinaciclib (drug)]] 0.05 µM 0.451× (z -9.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 47.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.30× (z +22.5) | — |
| [[C-33 A (line)]] | alt | 101 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.382× (z -9.7) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 89.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.105× (z -12.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 83.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.136× (z -18.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 70.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -12.1) |
| [[AN3 CA (line)]] | alt | 71.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 58.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 56.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 68.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 63.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 76.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3667), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL15]] | +0.73 | +0.62 / +0.75 | both halves | 7e-06 |  |
| [[TIMM9]] | +0.72 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[ZNF330]] | +0.68 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[DMAC1]] | +0.67 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[MIOS]] | +0.67 | +0.64 / +0.71 | both halves | 7e-06 | same gene group |
| [[TMA16]] | +0.63 | +0.68 / +0.57 | both halves | 1e-05 | STRING 405 |
| [[ZNF485]] | +0.62 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[LSM6]] | +0.62 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[ESF1]] | +0.62 | +0.54 / +0.66 | both halves | 1e-05 | STRING 788 |
| [[RIOK1]] | +0.62 | +0.55 / +0.73 | both halves | 1e-05 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol |
| [[ANGEL1]] | +0.61 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[BRIX1]] | +0.61 | +0.49 / +0.67 | both halves | 1e-05 | STRING 897 |

## Genes that move opposite

*16 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUCB1]] | -0.66 | -0.56 / -0.69 | both halves | 1e-05 |  |
| [[SKP1]] | -0.56 | -0.39 / -0.56 | both halves | 5e-05 |  |
| [[MTPN]] | -0.56 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[UFD1]] | -0.56 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[LRP10]] | -0.55 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[DNAJB6]] | -0.53 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[RAB5C]] | -0.53 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[TAX1BP1]] | -0.53 | -0.35 / -0.60 | both halves | 1e-04 |  |
| [[BSCL2]] | -0.53 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[APLP2]] | -0.53 | -0.46 / -0.51 | both halves | 2e-05 |  |
| [[MTCH1]] | -0.51 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[MBOAT7]] | -0.51 | -0.50 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WHRN]] | C | WHRN activity raises WDR75's level | lines that do not express WHRN (4) vs lines expressing it (46) | 1.60× lower at baseline in the lines without WHRN | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CLTCL1, NKAIN1, KIAA1549; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.578). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-47.8, -9.2); signed map (-2.1, -39.6). **Vector** length 114, 33.8% of its response variance represented; |z| ≥ 3 in 1,173 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.7 | +21.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.6 | +10.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.0 | +11.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.5 | +6.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.3 | +16.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +6.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.6 | +8.6 |
|  | [[EX229 (drug)]] 5 µM |  | +4.0 | +5.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.9 | +3.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.8 | +4.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.6 | -7.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.9 | -10.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.5 | -3.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -5.5 | +1.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | +0.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.5 | +2.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.6 | -0.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.2 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat domain 75 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q32.2 — chr2:189,441,446-189,475,552 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12519, NET16, UTP17 |
| Gene groups (HGNC) | WD repeat domain containing; UTPa subcomplex |
| Reactome | 5 pathways, smallest: rRNA modification in the nucleus and cytosol; Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IWA0](https://www.uniprot.org/uniprotkb/Q8IWA0) (WD repeat-containing protein 75):

> Ribosome biogenesis factor. Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal proteins associate with the nascent pre-rRNA and work in concert to generate RNA folding, modifications, rearrangements and cleavage as well as targeted degradation of pre-ribosomal RNA by the RNA exosome. Involved in nucleolar processing of …

**Summary**, from NCBI Gene [84128](https://www.ncbi.nlm.nih.gov/gene/84128):

> Enables RNA binding activity. Involved in positive regulation of rRNA processing; positive regulation of transcription by RNA polymerase I; and ribosomal small subunit biogenesis. Located in nucleolus. Part of small-subunit processome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25725](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25725) · Entrez [84128](https://www.ncbi.nlm.nih.gov/gene/84128) · UniProt [Q8IWA0](https://www.uniprot.org/uniprotkb/Q8IWA0) · Ensembl [ENSG00000115368](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115368)

## Data

Gene col 3667: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3667); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3667, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3667]; `tensor/DDL_lfc|DDL_z.npy` [3667]; `embed/gene_vectors.npy` [3667]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3667 or target_col == 3667). Every well: [[WDR75 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDR75.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
