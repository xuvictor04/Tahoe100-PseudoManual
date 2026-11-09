---
symbol: "SPTBN1"
type: "gene"
col: 3655
ensembl_id: "ENSG00000115306"
name: "spectrin beta, non-erythrocytic 1"
location: "2p16.2"
module: 25
arm: "+"
pooled_cpm: 611.58
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 23
n_dd_up_clean: 0
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# SPTBN1

*spectrin beta, non-erythrocytic 1* — 2p16.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.72× (z +10.5, q 7e-23, up in 42 of 49 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (RKO 3.18×, HEC-1-A 2.92×, MIA PaCa-2 3.43×, SW480 2.32×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (SW480 2.28×, C-33 A 2.56×, HEC-1-A 2.50×, MIA PaCa-2 2.91×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 3 lines (J82 1.56×, hTERT-HPNE 1.64×, A498 1.48×); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (SHP-77 2.09×); [[Peretinoin (drug)]] 5 µM in 1 line (SHP-77 2.02×).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.455× (z -21.5, q 0e+00, down in 45 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DYNC1H1]] (+0.69, fdr 7e-06), [[MYH9]] (+0.68, fdr 1e-05), [[YWHAZ]] (+0.67, fdr 1e-05); moves opposite to [[LSM7]] (-0.68, fdr 1e-05), [[TMEM258]] (-0.66, fdr 1e-05), [[MRPL23]] (-0.64, fdr 1e-04).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3655.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (RKO 3.18×, HEC-1-A 2.92×, MIA PaCa-2 3.43×, SW480 2.32×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (SW480 2.28×, C-33 A 2.56×, HEC-1-A 2.50×, MIA PaCa-2 2.91×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 3 lines (J82 1.56×, hTERT-HPNE 1.64×, A498 1.48×); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (SHP-77 2.09×); [[Peretinoin (drug)]] 5 µM in 1 line (SHP-77 2.02×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.72×** | +10.5 | 7e-23 | 42/49 (RKO, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.68×** | +9.6 | 2e-19 | 38/44 (SW480, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.46×** | +6.3 | 4e-08 | 35/45 (HEC-1-A, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 16 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3655.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.455×** | -21.5 | 0e+00 | 45/49 (KATO III, A549, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.491×** | -13.2 | 2e-37 | 43/47 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.562×** | -11.1 | 2e-26 | 45/48 (LS 180, A549, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.607×** | -9.6 | 8e-20 | 43/48 (LS 180, CFPAC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.647×** | -8.4 | 5e-15 | 43/48 (LS 180, A549, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.666×** | -7.5 | 4e-12 | 40/48 (NCI-H460, C32, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.695×** | -7.0 | 2e-10 | 40/48 (C32, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.782×** | -6.7 | 1e-09 | 29/48 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.711×** | -6.6 | 3e-09 | 34/48 (NCI-H460, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.738×** | -5.9 | 2e-07 | 34/48 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.744×** | -5.7 | 6e-07 | 36/48 (HOP62, SNU-423, …) | top dose only |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.815×** | -5.6 | 1e-06 | 30/48 (A549, SK-MEL-2, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.776×** | -4.9 | 4e-05 | 34/48 (BT-474, SK-MEL-2, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.794×** | -4.3 | 7e-04 | 28/50 (NCI-H460, LS 180, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.745×** | -4.1 | 0.002 | 34/48 (HepG2/C3A, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.709×** | -3.5 | 0.017 | 25/48 (KATO III, LoVo, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.813×** | -3.4 | 0.018 | 31/47 (C32, A-172, …) | all doses, stronger at high dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.780×** | -3.4 | 0.018 | 32/48 (NCI-H460, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.832×** | -3.4 | 0.018 | 24/48 (NCI-H460, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Bergenin (drug)]] 0.5 µM |  | 0.847× | -3.2 | 0.036 | 17/48 (SNU-1, A498, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 0.5 µM |  | **0.798×** | -3.1 | 0.046 | 23/49 (SK-MEL-2, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.893× | -3.1 | 0.048 | 14/48 (HOP62, A549, …) | rises with dose |  |
| [[BAY1125976 (drug)]] 0.5 µM |  | **0.805×** | -3.0 | 0.058 | 29/48 (HOP62, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **0.815×** | -2.8 | 0.086 | 23/49 (J82, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3655. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 871 | 0 | 14 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -21.0) |
| [[SNU-1 (line)]] | wt | 342 | 2 (2 ⚠) | 10 (6 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.76× (z +13.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.508× (z -12.8) |
| [[KATO III (line)]] | alt | 1,086 | 0 | 11 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.215× (z -23.9) |
| [[A549 (line)]] | wt | 1,528 | 0 | 10 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.247× (z -22.8) |
| [[LS 180 (line)]] | wt | 1,235 | 0 | 10 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -20.3) |
| [[HOP62 (line)]] | alt | 595 | 1 (1 ⚠) | 8 (6 ⚠) | [[Harringtonine (drug)]] 0.5 µM 1.66× (z +8.6) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -21.8) |
| [[HEC-1-A (line)]] | alt | 446 | 3 (3 ⚠) | 5 (4 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.92× (z +15.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.514× (z -13.7) |
| [[SW480 (line)]] | alt | 442 | 3 (3 ⚠) | 5 (4 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.32× (z +13.9) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.503× (z -16.1) |
| [[C32 (line)]] | wt | 598 | 0 | 7 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -21.7) |
| [[CFPAC-1 (line)]] | alt | 1,483 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -20.3) |
| [[SK-MEL-2 (line)]] | alt | 629 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -17.2) |
| [[A498 (line)]] | wt | 943 | 3 (3 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.38× (z +13.5) ⚠ toxic; transcription drop | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.491× (z -10.5) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.652× (z -9.3) |
| [[HepG2_C3A (line)]] | wt | 1,665 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -18.4) |
| [[NCI-H1792 (line)]] | alt | 216 | 2 (2 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.53× (z +13.1) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -18.0) |
| [[SW 900 (line)]] | alt | 593 | 1 (1 ⚠) | 5 (4 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.88× (z +8.9) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -18.7) |
| [[AsPC-1 (line)]] | alt | 705 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.452× (z -16.8) |
| [[COLO 205 (line)]] | alt | 1,234 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.363× (z -13.8) |
| [[LoVo (line)]] | wt | 516 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -17.7) |
| [[MIA PaCa-2 (line)]] | alt | 191 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +14.8) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -14.9) |
| [[SNU-423 (line)]] | alt | 805 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -15.8) |
| [[A-172 (line)]] | wt | 954 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.414× (z -12.7) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.570× (z -11.8) |
| [[BT-474 (line)]] | alt | 211 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.520× (z -11.8) |
| [[HCT15 (line)]] | alt | 465 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.28× (z +10.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -13.5) |
| [[Hs 766T (line)]] | wt | 220 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.83× (z +11.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -14.4) |
| [[HS-578T (line)]] | alt | 565 | 1 (1 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.88× (z +9.8) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.500× (z -14.9) |
| [[hTERT-HPNE (line)]] | wt | 561 | 2 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.02× (z +9.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.64× (z +8.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.399× (z -11.3) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 236 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.13× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -15.0) |
| [[NCI-H1573 (line)]] | alt | 256 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.353× (z -17.2) |
| [[NCI-H23 (line)]] | alt | 308 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 1.98× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -17.9) |
| [[PANC-1 (line)]] | alt | 433 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.38× (z +12.1) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -17.5) |
| [[J82 (line)]] | alt | 427 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.571× (z -12.1) |
| [[NCI-H2030 (line)]] | alt | 597 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -19.1) |
| [[NCI-H2347 (line)]] | alt | 459 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.496× (z -10.7) ⚠ cell-cycle shift, explains ~35% of this change |
| [[Panc 03.27 (line)]] | alt | 475 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.39× (z +12.1) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -21.7) |
| [[RKO (line)]] | wt | 211 | 1 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +15.8) ⚠ toxic; transcription drop | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.383× (z -12.5) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 704 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -18.9) |
| [[SHP-77 (line)]] | alt | 505 | 3 (1 ⚠) | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 2.09× (z +14.6) | — |
| [[A-427 (line)]] | wt | 380 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.594× (z -11.7) |
| [[AN3 CA (line)]] | alt | 403 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.59× (z +9.5) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 322 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.56× (z +12.9) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 653 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -10.0) |
| [[HT-29 (line)]] | alt | 559 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -17.2) |
| [[SW1417 (line)]] | alt | 555 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.493× (z -15.6) |
| [[H4 (line)]] | wt | 350 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -9.9) |
| [[SW 1088 (line)]] | alt | 665 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -9.2) |
| [[SW48 (line)]] | wt | 256 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.620× (z -8.6) |
| [[NCI-H2122 (line)]] | alt | 560 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 538 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 367 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 322 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3655), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DYNC1H1]] | +0.69 | +0.58 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[MYH9]] | +0.68 | +0.55 / +0.70 | both halves | 1e-05 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 671 |
| [[YWHAZ]] | +0.67 | +0.50 / +0.75 | both halves | 1e-05 |  |
| [[NONO]] | +0.67 | +0.58 / +0.69 | both halves | 8e-06 |  |
| [[YWHAQ]] | +0.67 | +0.60 / +0.73 | both halves | 7e-06 |  |
| [[EIF4H]] | +0.66 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[DCTN1]] | +0.65 | +0.57 / +0.71 | both halves | 9e-06 | pathway: Asparagine N-linked glycosylation |
| [[HUWE1]] | +0.65 | +0.51 / +0.72 | both halves | 1e-05 |  |
| [[LIN7C]] | +0.64 | +0.36 / +0.72 | both halves | 1e-04 |  |
| [[PRELID3B]] | +0.63 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[ZNF664]] | +0.61 | +0.43 / +0.69 | both halves | 3e-05 |  |
| [[TGOLN2]] | +0.61 | +0.47 / +0.70 | both halves | 2e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 6 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LSM7]] | -0.68 | -0.56 / -0.72 | both halves | 1e-05 |  |
| [[TMEM258]] | -0.66 | -0.51 / -0.69 | both halves | 1e-05 | pathway: Asparagine N-linked glycosylation |
| [[MRPL23]] | -0.64 | -0.36 / -0.72 | both halves | 1e-04 |  |
| [[DNLZ]] | -0.63 | -0.44 / -0.61 | both halves | 3e-05 |  |
| [[UBE2CP5]] | -0.63 | -0.58 / -0.61 | both halves | 7e-06 |  |
| [[RBX1]] | -0.63 | -0.54 / -0.61 | both halves | 1e-05 | pathway: MAPK family signaling cascades |
| [[SELENOH]] | -0.62 | -0.34 / -0.64 | both halves | 1e-04 |  |
| [[SNHG9]] | -0.62 | -0.46 / -0.66 | both halves | 3e-05 |  |
| [[ZNF593]] | -0.61 | -0.39 / -0.69 | both halves | 6e-05 |  |
| [[ZCCHC10]] | -0.61 | -0.53 / -0.62 | both halves | 1e-05 |  |
| [[TMEM101]] | -0.59 | -0.37 / -0.62 | both halves | 7e-05 |  |
| [[NAA60]] | -0.59 | -0.44 / -0.61 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SPTBN1's level | compounds that target TOP2A: 4 of 5 lower it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MYO5A]] | B | MYO5A activity lowers SPTBN1's level | lines that do not express MYO5A (6) vs lines expressing it (44) | 1.82× higher at baseline in the lines without MYO5A | 0.089 | ⚠ within organs, on part of the lines; also absent: TPST1, CYP46A1, CSRP2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.658). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-34.8, -18.8); signed map (-19.7, -36.3). **Vector** length 134, 46.8% of its response variance represented; |z| ≥ 3 in 1,422 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.3 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.0 | +6.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.2 | +2.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.1 | +9.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.6 | +1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.9 | +0.0 |
|  | [[Malotilate (drug)]] 0.05 µM |  | +3.1 | +2.3 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | +2.8 | +1.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.7 | +2.5 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -11.5 | -13.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -6.8 | -7.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -5.6 | -4.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.2 | -6.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.8 | -5.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -4.5 | -3.4 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -4.2 | -3.4 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | -4.0 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | spectrin beta, non-erythrocytic 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p16.2 — chr2:54,456,327-54,671,446 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Spectrins |
| Hallmark sets | TGF_BETA_SIGNALING, MITOTIC_SPINDLE |
| Reactome | 28 pathways, smallest: Signaling by FLT3 fusion proteins; Nephrin family interactions; Interaction between L1 and Ankyrins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q01082](https://www.uniprot.org/uniprotkb/Q01082) (Spectrin beta chain, non-erythrocytic 1):

> Fodrin, which seems to be involved in secretion, interacts with calmodulin in a calcium-dependent manner and is thus candidate for the calcium-dependent movement of the cytoskeleton at the membrane. Plays a critical role in central nervous system development and function.

**Summary**, from NCBI Gene [6711](https://www.ncbi.nlm.nih.gov/gene/6711):

> Spectrin is an actin crosslinking and molecular scaffold protein that links the plasma membrane to the actin cytoskeleton, and functions in the determination of cell shape, arrangement of transmembrane proteins, and organization of organelles. It is composed of two antiparallel dimers of alpha- and beta- subunits. This gene is one member of a family of beta-spectrin genes. The encoded protein contains an N-terminal actin-binding domain, and 17 spectrin repeats which are involved in dimer …

**Accessions** — [HGNC:11275](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11275) · Entrez [6711](https://www.ncbi.nlm.nih.gov/gene/6711) · UniProt [Q01082](https://www.uniprot.org/uniprotkb/Q01082) · Ensembl [ENSG00000115306](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115306)

## Data

Gene col 3655: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3655); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3655, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3655]; `tensor/DDL_lfc|DDL_z.npy` [3655]; `embed/gene_vectors.npy` [3655]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3655 or target_col == 3655). Every well: [[SPTBN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPTBN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
