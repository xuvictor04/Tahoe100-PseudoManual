---
symbol: "FAM133B"
type: "gene"
col: 13966
ensembl_id: "ENSG00000234545"
name: "family with sequence similarity 133 member B"
location: "7q21.2"
module: 17
arm: "+"
pooled_cpm: 95.5
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 4
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# FAM133B

*family with sequence similarity 133 member B* — 7q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.68× (z +26.6, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.702× (z -9.6, q 4e-19, down in 36 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 10 lines (RKO 0.386×, HEC-1-A 0.514×, NCI-H23 0.530×, A498 0.521×, …); [[Dinaciclib (drug)]] 5 µM in 6 lines (LoVo 0.232×, SW480 0.319×, CHP-212 0.0934×, SK-MEL-2 0.294×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SHP-77 0.145×, A549 0.354×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RP9]] (+0.74, fdr 7e-06), [[SLC25A12]] (+0.71, fdr 7e-06), [[HPF1]] (+0.70, fdr 1e-05); moves opposite to [[HCFC1]] (-0.66, fdr 8e-06), [[IL18BP]] (-0.64, fdr 2e-05), [[CERS2]] (-0.59, fdr 2e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 14 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13966.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.68×** | +26.6 | 0e+00 | 47/48 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.52×** | +17.6 | 0e+00 | 48/48 (SW480, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.05×** | +13.1 | 6e-37 | 47/48 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.54×** | +12.6 | 3e-34 | 48/49 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.50×** | +12.5 | 8e-34 | 46/48 (SW480, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.70×** | +10.1 | 5e-22 | 42/48 (KATO III, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.69×** | +9.9 | 2e-21 | 40/48 (KATO III, LoVo, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.47×** | +7.3 | 2e-11 | 38/48 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.39×** | +6.3 | 2e-08 | 30/48 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **1.32×** | +5.0 | 3e-05 | 27/47 (LoVo, NCI-H1792, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.30×** | +4.9 | 4e-05 | 32/48 (HT-29, LoVo, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.29×** | +4.8 | 7e-05 | 31/48 (LoVo, NCI-H1792, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.27×** | +4.5 | 3e-04 | 32/48 (LoVo, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.24×** | +4.1 | 0.001 | 23/48 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.23×** | +4.0 | 0.003 | 21/48 (KATO III, LoVo, …) | all doses, stronger at high dose |  |
| [[venetoclax (drug)]] 5 µM |  | **1.46×** | +3.7 | 0.006 | 27/48 (A498, RKO, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.21×** | +3.6 | 0.008 | 25/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.22×** | +3.6 | 0.009 | 20/47 (SW48, HEC-1-A, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.29×** | +3.4 | 0.017 | 19/49 (CFPAC-1, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.19× | +3.3 | 0.024 | 21/48 (KATO III, LoVo, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.19× | +3.2 | 0.033 | 16/49 (MIA PaCa-2, LoVo, …) | top dose only | plate-row cell shift |
| [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.037 | 12/49 (NCI-H1573, C32, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.12× | +3.0 | 0.050 | 9/48 (Panc 03.27, HT-29, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13966.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 10 lines (RKO 0.386×, HEC-1-A 0.514×, NCI-H23 0.530×, A498 0.521×, …); [[Dinaciclib (drug)]] 5 µM in 6 lines (LoVo 0.232×, SW480 0.319×, CHP-212 0.0934×, SK-MEL-2 0.294×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SHP-77 0.145×, A549 0.354×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.702×** | -9.6 | 4e-19 | 36/49 (RKO, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.713×** | -6.5 | 2e-08 | 29/49 (AsPC-1, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.743×** | -5.3 | 2e-05 | 29/45 (SHP-77, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.760×** | -5.1 | 5e-05 | 27/44 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.847× | -3.2 | 0.15 | 19/48 (NCI-H1792, LS 180, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 5 µM |  | 0.894× | -3.1 | 0.19 | 9/48 (C32, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13966. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 131 | 10 (5 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.60× (z +19.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.14× (z +16.4) | [[Dinaciclib (drug)]] 5 µM 0.232× (z -21.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 107 | 9 (3 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +22.3) | [[Dinaciclib (drug)]] 5 µM 0.319× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.654× (z -9.8) |
| [[KATO III (line)]] | alt | 105 | 8 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.34× (z +19.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.50× (z +17.6) | — |
| [[LS 180 (line)]] | wt | 123 | 6 (2 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +17.2) | [[Dinaciclib (drug)]] 5 µM 0.393× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.561× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 100 | 5 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +16.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -10.9) |
| [[PANC-1 (line)]] | alt | 76.3 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +20.0) | — |
| [[RKO (line)]] | wt | 138 | 5 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +24.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -15.9) |
| [[AsPC-1 (line)]] | alt | 168 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +21.9) | [[Dinaciclib (drug)]] 0.5 µM 0.274× (z -12.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 101 | 5 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +17.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.514× (z -11.4) |
| [[NCI-H1573 (line)]] | alt | 78.6 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +12.2) | — |
| [[A549 (line)]] | wt | 85.7 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +20.9) | [[Dinaciclib (drug)]] 0.05 µM 0.354× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.543× (z -9.3) |
| [[Panc 03.27 (line)]] | alt | 96.7 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +19.4) | — |
| [[A498 (line)]] | wt | 114 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +17.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.521× (z -10.9) |
| [[H4 (line)]] | wt | 86.5 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +15.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 108 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +14.8) | — |
| [[NCI-H1792 (line)]] | alt | 82.9 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +12.5) | — |
| [[SW48 (line)]] | wt | 145 | 2 | 2 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 4.49× (z +12.9) | [[Dinaciclib (drug)]] 0.05 µM 0.344× (z -9.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.500× (z -9.0) |
| [[AN3 CA (line)]] | alt | 156 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.273× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.452× (z -9.0) |
| [[C32 (line)]] | wt | 144 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +15.4) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 91.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +20.7) | — |
| [[COLO 205 (line)]] | alt | 47.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +13.0) | — |
| [[J82 (line)]] | alt | 80.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +15.6) | — |
| [[NCI-H23 (line)]] | alt | 89.7 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +11.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -11.2) |
| [[NCI-H2347 (line)]] | alt | 95.0 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.457× (z -10.0) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 67.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.145× (z -15.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 104 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.294× (z -12.7) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 133 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +16.8) | [[Dinaciclib (drug)]] 5 µM 0.449× (z -9.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 64.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +13.8) | — |
| [[A-427 (line)]] | wt | 75.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +9.7) | — |
| [[BT-474 (line)]] | alt | 86.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +15.4) | — |
| [[HOP62 (line)]] | alt | 68.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +15.3) | — |
| [[HS-578T (line)]] | alt | 83.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +13.7) | — |
| [[HT-29 (line)]] | alt | 66.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +19.8) | — |
| [[hTERT-HPNE (line)]] | wt | 64.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +14.6) | — |
| [[LOX-IMVI (line)]] | wt | 81.5 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.14× (z +12.2) | — |
| [[NCI-H2030 (line)]] | alt | 98.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +11.8) | — |
| [[RPMI-7951 (line)]] | alt | 76.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +12.4) | — |
| [[SW 900 (line)]] | alt | 91.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +14.7) | — |
| [[CHP-212 (line)]] | wt | 97.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0934× (z -14.1) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 76.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +8.9) | — |
| [[SNU-423 (line)]] | alt | 79.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +14.7) | — |
| [[C-33 A (line)]] | alt | 99.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 81.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 73.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 99.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 92.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13966), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RP9]] | +0.74 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[SLC25A12]] | +0.71 | +0.65 / +0.75 | both halves | 7e-06 |  |
| [[HPF1]] | +0.70 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[PRPF39]] | +0.70 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[MRPL21]] | +0.69 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[EBAG9]] | +0.69 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[METTL14]] | +0.68 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[ZC3H15]] | +0.68 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[ZNF45]] | +0.68 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[BBS5]] | +0.68 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[RIOK2]] | +0.67 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[PPP4R2]] | +0.67 | +0.65 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HCFC1]] | -0.66 | -0.61 / -0.58 | both halves | 8e-06 |  |
| [[IL18BP]] | -0.64 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[CERS2]] | -0.59 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[LY6G5B]] | -0.57 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[PRDM10]] | -0.57 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[LRP10]] | -0.57 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[SMG1P6]] | -0.56 | -0.35 / -0.56 | both halves | 1e-04 |  |
| [[RAB22A]] | -0.56 | -0.43 / -0.61 | both halves | 3e-05 |  |
| [[ATXN1L]] | -0.55 | -0.26 / -0.65 | both halves | 4e-04 |  |
| [[DVL3]] | -0.55 | -0.35 / -0.54 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.754). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-24.8, -3.3); signed map (-21.2, -10.9). **Vector** length 93.5, 29.7% of its response variance represented; |z| ≥ 3 in 1,063 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.2 | +3.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.7 | +1.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.7 | +3.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.6 | +26.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.9 | +17.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.1 | +2.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.7 | +2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +3.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +0.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.0 | -9.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~77% of this change | -6.9 | +2.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -5.6 | +10.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -5.1 | +4.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.9 | -0.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | +1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -2.5 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.5 | -1.2 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.3 | -0.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.1 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 133 member B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.2 — chr7:92,560,758-92,590,393 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC40405 |
| Matched by | ensembl_id |

UniProt [Q5BKY9](https://www.uniprot.org/uniprotkb/Q5BKY9) carries no function annotation.

**Summary**, from NCBI Gene [257415](https://www.ncbi.nlm.nih.gov/gene/257415):

> Enables RNA binding activity. Located in nucleolus and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28629](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28629) · Entrez [257415](https://www.ncbi.nlm.nih.gov/gene/257415) · UniProt [Q5BKY9](https://www.uniprot.org/uniprotkb/Q5BKY9) · Ensembl [ENSG00000234545](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000234545)

## Data

Gene col 13966: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13966); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13966, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13966]; `tensor/DDL_lfc|DDL_z.npy` [13966]; `embed/gene_vectors.npy` [13966]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13966 or target_col == 13966). Every well: [[FAM133B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM133B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
