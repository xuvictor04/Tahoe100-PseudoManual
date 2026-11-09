---
symbol: "PTPN11"
type: "gene"
col: 11017
ensembl_id: "ENSG00000179295"
name: "protein tyrosine phosphatase non-receptor type 11"
location: "12q24.13"
module: 4
arm: "+"
pooled_cpm: 167.61
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 2
n_dd_up_clean: 18
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# PTPN11

*protein tyrosine phosphatase non-receptor type 11* — 12q24.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.03× (z +27.8, q 0e+00, up in 48 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.55× (z +10.9, q 8e-26, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.739× (z -10.7, q 6e-24, down in 33 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 10 lines (HT-29 0.465×, RKO 0.515×, NCI-H460 0.578×, SW480 0.604×, …); [[Digitoxin (drug)]] 5 µM in 1 line (SW48 0.353×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Belinostat (drug)]] 5 µM in 1 line (RKO 0.526×; ⚠ cell-cycle shift, explains ~0% of this change); [[Tolmetin (drug)]] 5 µM in 1 line (SW 1088 0.0699×); [[Ipatasertib (drug)]] 0.5 µM in 1 line (HCT15 0.321×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDAP1]] (+0.77, fdr 7e-06), [[CCT5]] (+0.74, fdr 7e-06), [[OCRL]] (+0.70, fdr 7e-06); moves opposite to [[SNHG9]] (-0.69, fdr 2e-05), [[RSRP1]] (-0.69, fdr 1e-05), [[TESK2]] (-0.68, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 50 in all, 20 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11017.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.03×** | +27.8 | 0e+00 | 48/49 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.16×** | +27.8 | 0e+00 | 44/44 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.36×** | +19.9 | 0e+00 | 44/45 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.72×** | +13.5 | 2e-39 | 47/48 (AsPC-1, NCI-H1792, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.55×** | +10.9 | 8e-26 | 40/48 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.37×** | +10.9 | 1e-25 | 28/48 (CFPAC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.38×** | +8.0 | 7e-14 | 36/48 (A-172, CFPAC-1, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.37×** | +7.9 | 3e-13 | 39/47 (NCI-H23, HT-29, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.34×** | +7.3 | 2e-11 | 33/48 (HT-29, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.35×** | +7.2 | 5e-11 | 32/48 (A-172, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.33×** | +7.1 | 6e-11 | 32/48 (C32, Hs 766T, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.32×** | +6.9 | 3e-10 | 35/48 (HT-29, SNU-423, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.21×** | +6.7 | 8e-10 | 28/49 (HT-29, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.74×** | +6.4 | 5e-09 | 39/48 (CFPAC-1, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.30×** | +6.4 | 7e-09 | 34/47 (HT-29, SNU-423, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.26×** | +5.9 | 2e-07 | 25/48 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.26×** | +5.8 | 2e-07 | 36/47 (HT-29, C32, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.64×** | +5.7 | 3e-07 | 37/48 (NCI-H460, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.58×** | +5.3 | 4e-06 | 31/48 (AsPC-1, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.22×** | +5.1 | 1e-05 | 27/48 (NCI-H1573, NCI-H2030, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.52×** | +4.8 | 3e-05 | 30/49 (MIA PaCa-2, BT-474, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.51×** | +4.8 | 4e-05 | 32/48 (AsPC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11017.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 10 lines (HT-29 0.465×, RKO 0.515×, NCI-H460 0.578×, SW480 0.604×, …); [[Digitoxin (drug)]] 5 µM in 1 line (SW48 0.353×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Belinostat (drug)]] 5 µM in 1 line (RKO 0.526×; ⚠ cell-cycle shift, explains ~0% of this change); [[Tolmetin (drug)]] 5 µM in 1 line (SW 1088 0.0699×); [[Ipatasertib (drug)]] 0.5 µM in 1 line (HCT15 0.321×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.739×** | -10.7 | 6e-24 | 33/49 (HT-29, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.760×** | -4.9 | 2e-04 | 33/48 (HCT15, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.862× | -3.7 | 0.034 | 17/49 (SW1417, BT-474, …) | two highest doses |  |
| [[Decitabine (drug)]] 0.05 µM |  | 0.870× | -3.3 | 0.11 | 12/47 (RKO, KATO III, …) | inconsistent across doses |  |
| [[ULK-101 (drug)]] 0.05 µM |  | 0.872× | -3.3 | 0.11 | 10/49 (NCI-H2122, H4, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 0.5 µM |  | 0.835× | -3.2 | 0.11 | 19/49 (PANC-1, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.838× | -3.2 | 0.12 | 18/48 (LS 180, BT-474, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.884× | -3.1 | 0.13 | 11/49 (NCI-H2347, PANC-1, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.888× | -3.0 | 0.17 | 14/48 (LOX-IMVI, HT-29, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11017. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 107 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +18.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.36× (z +11.2) | — |
| [[A498 (line)]] | wt | 119 | 7 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.63× (z +19.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.44× (z +14.0) | — |
| [[CFPAC-1 (line)]] | alt | 107 | 7 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +19.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.00× (z +9.7) | — |
| [[HOP62 (line)]] | alt | 125 | 7 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.24× (z +23.0) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 1.97× (z +9.4) | — |
| [[HT-29 (line)]] | alt | 158 | 6 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.32× (z +16.4) ⚠ toxic; transcription drop · without an alert: [[Peretinoin (drug)]] 0.5 µM 1.86× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -15.3) |
| [[C32 (line)]] | wt | 97.8 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.37× (z +18.1) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 105 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.59× (z +13.9) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 232 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +15.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.91× (z +8.9) | — |
| [[PANC-1 (line)]] | alt | 184 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.45× (z +19.3) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 1.72× (z +8.5) | — |
| [[LoVo (line)]] | wt | 215 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +18.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.605× (z -11.4) |
| [[NCI-H1573 (line)]] | alt | 127 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +15.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 1.77× (z +8.6) | — |
| [[NCI-H1792 (line)]] | alt | 156 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.82× (z +21.1) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 139 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.12× (z +14.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -11.5) |
| [[SW480 (line)]] | alt | 180 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +21.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.604× (z -12.8) |
| [[A549 (line)]] | wt | 148 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +19.1) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 157 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.63× (z +12.9) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.34× (z +8.5) | — |
| [[HCT15 (line)]] | alt | 184 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.05× (z +11.5) ⚠ toxic; transcription drop | [[Ipatasertib (drug)]] 0.5 µM 0.321× (z -8.7) |
| [[HS-578T (line)]] | alt | 99.7 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.57× (z +19.0) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 138 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +14.0) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 137 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.91× (z +18.4) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 162 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.62× (z +18.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.587× (z -10.8) |
| [[NCI-H2347 (line)]] | alt | 170 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.84× (z +15.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.68× (z +10.4) | — |
| [[NCI-H460 (line)]] | wt | 184 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.02× (z +19.1) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.578× (z -13.3) |
| [[RPMI-7951 (line)]] | alt | 135 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.51× (z +16.6) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 131 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.21× (z +18.9) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 188 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.10× (z +12.3) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.353× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.585× (z -8.6) |
| [[A-427 (line)]] | wt | 207 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.87× (z +14.5) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 235 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.40× (z +12.1) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 199 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.69× (z +13.5) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 182 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +19.0) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 165 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.66× (z +13.2) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 253 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.28× (z +17.3) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 177 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +17.2) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 102 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.03× (z +18.4) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 130 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.17× (z +14.0) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 182 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.67× (z +16.4) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 181 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.29× (z +9.6) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 119 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.69× (z +10.7) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 106 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.52× (z +15.5) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.28× (z +8.5) | — |
| [[NCI-H23 (line)]] | alt | 297 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.11× (z +16.4) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 251 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -14.3) |
| [[SHP-77 (line)]] | alt | 227 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.57× (z +14.2) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 189 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.05× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 209 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.474× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SW 1088 (line)]] | alt | 99.9 | 0 | 1 | — | [[Tolmetin (drug)]] 5 µM 0.0699× (z -9.6) |
| [[BT-474 (line)]] | alt | 220 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 230 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 191 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11017), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDAP1]] | +0.77 | +0.79 / +0.75 | both halves | 7e-06 |  |
| [[CCT5]] | +0.74 | +0.77 / +0.76 | both halves | 7e-06 |  |
| [[OCRL]] | +0.70 | +0.63 / +0.72 | both halves | 7e-06 |  |
| [[CCT2]] | +0.70 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[EIF4G1]] | +0.70 | +0.63 / +0.71 | both halves | 7e-06 | pathway: Interferon Signaling |
| [[CCT7]] | +0.69 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[HUWE1]] | +0.69 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[TMEM33]] | +0.68 | +0.59 / +0.73 | both halves | 7e-06 |  |
| [[CCT3]] | +0.68 | +0.72 / +0.72 | both halves | 7e-06 |  |
| [[LIN7C]] | +0.68 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[PSME3]] | +0.67 | +0.69 / +0.69 | both halves | 7e-06 | STRING 627 |
| [[XRCC5]] | +0.67 | +0.60 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG9]] | -0.69 | -0.47 / -0.73 | both halves | 2e-05 |  |
| [[RSRP1]] | -0.69 | -0.54 / -0.78 | both halves | 1e-05 |  |
| [[TESK2]] | -0.68 | -0.52 / -0.69 | both halves | 1e-05 |  |
| [[SNHG19]] | -0.66 | -0.56 / -0.68 | both halves | 1e-05 |  |
| [[RAB40C]] | -0.66 | -0.66 / -0.67 | both halves | 7e-06 |  |
| [[ARID4A]] | -0.66 | -0.57 / -0.64 | both halves | 1e-05 |  |
| [[DCTN6-DT]] | -0.66 | -0.59 / -0.67 | both halves | 7e-06 |  |
| [[AAMDC]] | -0.66 | -0.62 / -0.65 | both halves | 7e-06 |  |
| [[NARF]] | -0.66 | -0.55 / -0.66 | both halves | 1e-05 |  |
| [[NDUFA2]] | -0.65 | -0.47 / -0.68 | both halves | 2e-05 |  |
| [[TMEM258]] | -0.65 | -0.55 / -0.65 | both halves | 1e-05 | pathway: Cell-Cell communication |
| [[RHEBL1]] | -0.65 | -0.50 / -0.66 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.691). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-21.8, -31.9); signed map (-12.1, -44.2). **Vector** length 137, 46.7% of its response variance represented; |z| ≥ 3 in 1,451 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Folding of actin by CCT/TriC* (reactome, mean cos +0.64 to 4); *Prefoldin mediated transfer of substrate  to CCT/TriC* (reactome, mean cos +0.55 to 5); *Cooperation of Prefoldin and TriC/CCT  in actin and tubulin folding* (reactome, mean cos +0.55 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.4 | +27.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +9.3 | +13.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.8 | +27.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.5 | +19.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.9 | +8.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +5.2 | +6.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +5.1 | +6.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | +5.1 | +4.8 |
|  | [[EX229 (drug)]] 5 µM |  | +4.9 | +5.3 |
| fall | [[Ipatasertib (drug)]] 0.5 µM |  | -6.6 | -4.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.5 | -10.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -5.8 | +0.0 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -3.6 | -2.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -3.5 | -3.2 |
|  | [[Thymol (drug)]] 0.5 µM |  | -3.5 | -3.0 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | -3.3 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | protein tyrosine phosphatase non-receptor type 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.13 — chr12:112,418,351-112,509,918 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BPTP3, SH-PTP2, SHP-2, PTP2C, SHP2; previously NS1 |
| Gene groups (HGNC) | SH2 domain containing; Protein tyrosine phosphatases non-receptor type |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING, PI3K_AKT_MTOR_SIGNALING |
| Reactome | 107 pathways, smallest: Co-inhibition by BTLA; MET activates PTPN11; STAT5 Activation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q06124](https://www.uniprot.org/uniprotkb/Q06124) (Tyrosine-protein phosphatase non-receptor type 11):

> Acts downstream of various receptor and cytoplasmic protein tyrosine kinases to participate in the signal transduction from the cell surface to the nucleus. Positively regulates MAPK signal transduction pathway. Dephosphorylates GAB1, ARHGAP35 and EGFR. Dephosphorylates ROCK2 at 'Tyr-722' resulting in stimulation of its RhoA binding activity. Dephosphorylates CDC73. Dephosphorylates SOX9 on tyrosine residues, leading to inactivate SOX9 and promote ossification (By similarity). Dephosphorylates …

**Summary**, from NCBI Gene [5781](https://www.ncbi.nlm.nih.gov/gene/5781):

> The protein encoded by this gene is a member of the protein tyrosine phosphatase (PTP) family. PTPs are known to be signaling molecules that regulate a variety of cellular processes including cell growth, differentiation, mitotic cycle, and oncogenic transformation. This PTP contains two tandem Src homology-2 domains, which function as phospho-tyrosine binding domains and mediate the interaction of this PTP with its substrates. This PTP is widely expressed in most tissues and plays a regulatory …

**Accessions** — [HGNC:9644](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9644) · Entrez [5781](https://www.ncbi.nlm.nih.gov/gene/5781) · UniProt [Q06124](https://www.uniprot.org/uniprotkb/Q06124) · Ensembl [ENSG00000179295](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179295)

## Data

Gene col 11017: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11017); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11017, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11017]; `tensor/DDL_lfc|DDL_z.npy` [11017]; `embed/gene_vectors.npy` [11017]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11017 or target_col == 11017). Every well: [[PTPN11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTPN11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
