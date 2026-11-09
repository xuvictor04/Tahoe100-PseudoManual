---
symbol: "ENSA"
type: "gene"
col: 6740
ensembl_id: "ENSG00000143420"
name: "endosulfine alpha"
location: "1q21.3"
module: 77
arm: "-"
pooled_cpm: 124.57
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 1
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# ENSA

*endosulfine alpha* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.49× (z +26.4, q 0e+00, up in 47 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.88× (z +25.9, q 0e+00, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.780× (z -10.2, q 2e-21, down in 32 of 48 measured lines) ⚠ cell-cycle shift, explains ~31% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 5 lines (Hs 766T 0.439×, SNU-423 0.537×, NCI-H1792 0.574×, J82 0.636×, …; ⚠ cell-cycle shift, explains ~31% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (NCI-H23 0.551×, A498 0.541×, BT-474 0.576×, RKO 0.559×, …; ⚠ cell-cycle shift, explains ~3% of this change); [[c-Kit-IN-1 (drug)]] 0.05 µM in 1 line (NCI-H460 0.529×; ⚠ unreliable plate only); [[Saquinavir (drug)]] 0.05 µM in 1 line (SW 1088 0.0936×); [[Lenalidomide (hemihydrate) (drug)]] 0.05 µM in 1 line (SW 1088 0.0941×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARMH4]] (+0.62, fdr 1e-05), [[LINC00641]] (+0.60, fdr 1e-05), [[C11orf54]] (+0.55, fdr 2e-05); moves opposite to [[POMGNT2]] (-0.61, fdr 1e-05), [[GEMIN5]] (-0.57, fdr 1e-05), [[MRPS26]] (-0.57, fdr 2e-05).
> It sits in the **-** arm of [[Module 077]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6740.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.49×** | +26.4 | 0e+00 | 47/49 (SW480, LS 180, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.88×** | +25.9 | 0e+00 | 43/48 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.13×** | +21.1 | 0e+00 | 42/44 (Panc 03.27, SW480, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.19×** | +21.0 | 0e+00 | 41/45 (KATO III, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.80×** | +17.0 | 0e+00 | 46/48 (LoVo, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.58×** | +13.2 | 4e-38 | 43/48 (SNU-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.56×** | +12.8 | 1e-35 | 44/48 (A-172, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.51×** | +11.4 | 2e-28 | 33/48 (A-172, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.40×** | +9.7 | 2e-20 | 38/48 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +9.5 | 1e-19 | 2/50 (SW 1271, NCI-H661) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.36×** | +8.3 | 4e-15 | 29/48 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +7.2 | 2e-11 | 26/48 (HT-29, A-427, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.25×** | +6.5 | 4e-09 | 29/49 (A-172, HOP62, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.23×** | +5.7 | 4e-07 | 22/47 (HEC-1-A, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.33×** | +4.3 | 7e-04 | 22/48 (Hs 766T, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Gefitinib (drug)]] 5 µM |  | 1.13× | +3.5 | 0.013 | 8/48 (NCI-H460, A-172, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.12× | +3.2 | 0.037 | 8/48 (A498, LoVo, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.08× | +3.2 | 0.041 | 6/48 (C32, Hs 766T, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.11× | +3.1 | 0.058 | 12/48 (A-172, COLO 205, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.07× | +2.9 | 0.089 | 10/48 (A549, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6740.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 5 lines (Hs 766T 0.439×, SNU-423 0.537×, NCI-H1792 0.574×, J82 0.636×, …; ⚠ cell-cycle shift, explains ~31% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (NCI-H23 0.551×, A498 0.541×, BT-474 0.576×, RKO 0.559×, …; ⚠ cell-cycle shift, explains ~3% of this change); [[c-Kit-IN-1 (drug)]] 0.05 µM in 1 line (NCI-H460 0.529×; ⚠ unreliable plate only); [[Saquinavir (drug)]] 0.05 µM in 1 line (SW 1088 0.0936×); [[Lenalidomide (hemihydrate) (drug)]] 0.05 µM in 1 line (SW 1088 0.0941×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.780×** | -10.2 | 2e-21 | 32/48 (Hs 766T, SNU-423, …) | rises with dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | 0.873× | -5.6 | 6e-06 | 19/49 (NCI-H23, A498, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.861× | -4.2 | 0.006 | 19/48 (LoVo, COLO 205, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.893× | -3.3 | 0.14 | 13/48 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[Roxadustat (drug)]] 5 µM |  | 0.893× | -3.1 | 0.19 | 7/48 (RPMI-7951, A-427, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6740. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 124 | 11 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +26.0) | — |
| [[SW480 (line)]] | alt | 120 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +22.4) | — |
| [[LoVo (line)]] | wt | 130 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +21.7) | — |
| [[HOP62 (line)]] | alt | 88.8 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +19.2) | — |
| [[NCI-H460 (line)]] | wt | 164 | 6 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +23.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.529× (z -10.5) ⚠ unreliable plate only |
| [[MIA PaCa-2 (line)]] | alt | 115 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +18.6) | — |
| [[RKO (line)]] | wt | 142 | 5 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.88× (z +12.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.559× (z -10.1) ⚠ cell-cycle shift, explains ~3% of this change |
| [[SW48 (line)]] | wt | 79.5 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +15.2) | — |
| [[A498 (line)]] | wt | 86.3 | 4 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.39× (z +12.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.61× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.541× (z -12.5) ⚠ cell-cycle shift, explains ~3% of this change |
| [[AsPC-1 (line)]] | alt | 77.4 | 5 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.77× (z +13.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.20× (z +11.9) | — |
| [[J82 (line)]] | alt | 102 | 4 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +20.7) | [[Selinexor (drug)]] 5 µM 0.636× (z -9.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[KATO III (line)]] | alt | 97.0 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +16.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.11× (z +10.3) | — |
| [[LS 180 (line)]] | wt | 133 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.00× (z +16.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.97× (z +14.5) | — |
| [[PANC-1 (line)]] | alt | 141 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +16.1) | — |
| [[SNU-1 (line)]] | wt | 134 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +15.3) | — |
| [[SNU-423 (line)]] | alt | 82.3 | 4 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +14.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.90× (z +11.2) | [[Selinexor (drug)]] 5 µM 0.537× (z -10.8) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A-427 (line)]] | wt | 131 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.67× (z +12.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.17× (z +10.2) | — |
| [[C-33 A (line)]] | alt | 137 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +12.2) | — |
| [[HEC-1-A (line)]] | alt | 107 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.73× (z +14.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.70× (z +11.3) | — |
| [[Hs 766T (line)]] | wt | 99.1 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.13× (z +9.9) ⚠ toxic; transcription drop | [[Selinexor (drug)]] 5 µM 0.439× (z -15.2) ⚠ cell-cycle shift, explains ~31% of this change |
| [[LOX-IMVI (line)]] | wt | 97.8 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.78× (z +13.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.83× (z +11.4) | — |
| [[NCI-H1792 (line)]] | alt | 129 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +13.6) | [[Selinexor (drug)]] 5 µM 0.574× (z -10.0) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H2030 (line)]] | alt | 161 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +14.8) | — |
| [[C32 (line)]] | wt | 77.5 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +15.0) | — |
| [[CFPAC-1 (line)]] | alt | 146 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.30× (z +13.3) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 177 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.23× (z +14.8) | — |
| [[HCT15 (line)]] | alt | 191 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.61× (z +12.9) | — |
| [[HepG2_C3A (line)]] | wt | 97.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +9.3) | — |
| [[hTERT-HPNE (line)]] | wt | 68.9 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +13.6) | — |
| [[NCI-H2347 (line)]] | alt | 73.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.81× (z +13.6) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 101 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.97× (z +15.5) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 57.0 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +11.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.27× (z +11.3) | — |
| [[SW 900 (line)]] | alt | 125 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.01× (z +12.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.53× (z +10.9) | — |
| [[A549 (line)]] | wt | 96.4 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.49× (z +12.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.76× (z +10.5) | — |
| [[AN3 CA (line)]] | alt | 82.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +9.4) | — |
| [[H4 (line)]] | wt | 105 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.58× (z +11.6) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 74.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +14.1) | — |
| [[HT-29 (line)]] | alt | 151 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.42× (z +13.8) | — |
| [[NCI-H23 (line)]] | alt | 234 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +13.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.551× (z -13.2) ⚠ cell-cycle shift, explains ~3% of this change |
| [[RPMI-7951 (line)]] | alt | 118 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +15.4) | — |
| [[SHP-77 (line)]] | alt | 180 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +15.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.12× (z +10.0) | — |
| [[SW 1088 (line)]] | alt | 86.7 | 0 | 2 | — | [[Saquinavir (drug)]] 0.05 µM 0.0936× (z -8.7) |
| [[SW1417 (line)]] | alt | 72.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.74× (z +11.4) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 181 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.576× (z -10.5) ⚠ cell-cycle shift, explains ~3% of this change |
| [[NCI-H1573 (line)]] | alt | 332 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.474× (z -8.8) ⚠ cell-cycle shift, explains ~61% of this change |
| [[CHP-212 (line)]] | wt | 141 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 119 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6740), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*34 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARMH4]] | +0.62 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[LINC00641]] | +0.60 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[C11orf54]] | +0.55 | +0.46 / +0.49 | both halves | 2e-05 |  |
| [[SDCBP2-AS1]] | +0.55 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[OCIAD1]] | +0.53 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[PCF11]] | +0.53 | +0.61 / +0.44 | both halves | 3e-05 |  |
| [[DCAF8]] | +0.52 | +0.48 / +0.46 | both halves | 2e-05 |  |
| [[CHMP4A]] | +0.50 | +0.52 / +0.37 | both halves | 7e-05 |  |
| [[MZF1]] | +0.50 | +0.39 / +0.41 | both halves | 6e-05 |  |
| [[NDUFA6-DT]] | +0.49 | +0.60 / +0.33 | both halves | 1e-04 |  |
| [[USP16]] | +0.49 | +0.37 / +0.50 | both halves | 8e-05 |  |
| [[USP34]] | +0.49 | +0.38 / +0.40 | both halves | 6e-05 |  |

## Genes that move opposite

*66 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POMGNT2]] | -0.61 | -0.64 / -0.51 | both halves | 1e-05 |  |
| [[GEMIN5]] | -0.57 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[MRPS26]] | -0.57 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[ZNF74]] | -0.55 | -0.48 / -0.40 | both halves | 4e-05 |  |
| [[TAF5L]] | -0.53 | -0.56 / -0.46 | both halves | 2e-05 |  |
| [[MACIR]] | -0.52 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[SLC15A4]] | -0.52 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[MTMR12]] | -0.52 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[PLEKHF1]] | -0.51 | -0.40 / -0.41 | both halves | 4e-05 |  |
| [[NOD1]] | -0.51 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[DBR1]] | -0.51 | -0.31 / -0.61 | both halves | 2e-04 |  |
| [[TEX264]] | -0.51 | -0.17 / -0.59 | ⚠ one half (not replicated) | 0.001 |  |
| [[MKRN2]] | -0.51 | -0.50 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **-** arm (projection on the module's main direction -0.480). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (-1.1, -3.8); signed map (16.4, -1.0). **Vector** length 126, 38.2% of its response variance represented; |z| ≥ 3 in 1,141 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +7.6 | +17.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +7.5 | +12.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.5 | +26.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.1 | +21.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.1 | +13.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +4.0 | +6.5 |
|  | [[Gefitinib (drug)]] 5 µM |  | +3.1 | +3.5 |
|  | [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +1.5 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +2.5 | +2.7 |
|  | [[Lactate (calcium) (drug)]] 0.5 µM |  | +2.3 | +1.3 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -7.9 | -10.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | -7.1 | -5.6 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.2 | -1.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | -2.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -1.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.5 | -4.2 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -3.4 | -1.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.0 | -1.6 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.4 | -0.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.2 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | endosulfine alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:150,600,851-150,629,612 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC4319, MGC8394, MGC78563, ARPP-19e |
| Reactome | 5 pathways, smallest: MASTL Facilitates Mitotic Progression; Mitotic Prophase; M Phase |
| Matched by | ensembl_id |

**Function**, from UniProt [O43768](https://www.uniprot.org/uniprotkb/O43768) (Alpha-endosulfine):

> Protein phosphatase inhibitor that specifically inhibits protein phosphatase 2A (PP2A) during mitosis. When phosphorylated at Ser-67 during mitosis, specifically interacts with PPP2R2D (PR55-delta) and inhibits its activity, leading to inactivation of PP2A, an essential condition to keep cyclin-B1-CDK1 activity high during M phase (By similarity). Also acts as a stimulator of insulin secretion by interacting with sulfonylurea receptor (ABCC8), thereby preventing sulfonylurea from binding to its …

**Summary**, from NCBI Gene [2029](https://www.ncbi.nlm.nih.gov/gene/2029):

> The protein encoded by this gene belongs to a highly conserved cAMP-regulated phosphoprotein (ARPP) family. This protein was identified as an endogenous ligand for the sulfonylurea receptor, ABCC8/SUR1. ABCC8 is the regulatory subunit of the ATP-sensitive potassium (KATP) channel, which is located on the plasma membrane of pancreatic beta cells and plays a key role in the control of insulin release from pancreatic beta cells. This protein is thought to be an endogenous regulator of KATP …

**Accessions** — [HGNC:3360](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3360) · Entrez [2029](https://www.ncbi.nlm.nih.gov/gene/2029) · UniProt [O43768](https://www.uniprot.org/uniprotkb/O43768) · Ensembl [ENSG00000143420](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143420)

## Data

Gene col 6740: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6740); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6740, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6740]; `tensor/DDL_lfc|DDL_z.npy` [6740]; `embed/gene_vectors.npy` [6740]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6740 or target_col == 6740). Every well: [[ENSA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ENSA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
