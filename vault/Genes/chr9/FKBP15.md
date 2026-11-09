---
symbol: "FKBP15"
type: "gene"
col: 4052
ensembl_id: "ENSG00000119321"
name: "FKBP prolyl isomerase family member 15"
location: "9q32"
module: 4
arm: "-"
pooled_cpm: 69.27
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 6
n_dd_up_clean: 15
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# FKBP15

*FKBP prolyl isomerase family member 15* — 9q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.58× (z +11.6, q 2e-28, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.448× (z -19.6, q 0e+00, down in 36 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.791× (z -8.5, q 3e-15, down in 28 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 10 lines (LS 180 0.0703×, HEC-1-A 0.196×, NCI-H460 0.189×, KATO III 0.123×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 8 lines (RKO 0.241×, SNU-423 0.438×, C32 0.462×, NCI-H460 0.601×, …); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (COLO 205 0.0857×, RKO 0.173×, HEC-1-A 0.324×; ⚠ toxic; transcription drop); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 3 lines (RKO 0.287×, C32 0.414×, A-172 0.462×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HMGCL]] (+0.63, fdr 7e-06), [[FUT11]] (+0.61, fdr 1e-05), [[MRPS18C]] (+0.60, fdr 1e-05); moves opposite to [[DNAJB6]] (-0.59, fdr 1e-05), [[ZNF37BP]] (-0.55, fdr 3e-05), [[ATP11C]] (-0.55, fdr 8e-05).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 5 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4052.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.58×** | +11.6 | 2e-28 | 35/48 (LoVo, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.35×** | +10.9 | 4e-25 | 30/48 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.40×** | +8.3 | 2e-14 | 31/48 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.36×** | +7.8 | 1e-12 | 34/48 (LoVo, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.31×** | +6.7 | 2e-09 | 33/48 (A-172, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.30×** | +6.6 | 5e-09 | 30/48 (A498, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.26×** | +5.9 | 3e-07 | 25/48 (SNU-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.25×** | +5.6 | 1e-06 | 25/48 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.21×** | +4.9 | 7e-05 | 23/48 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 1.20× | +4.6 | 2e-04 | 20/48 (A498, MIA PaCa-2, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.42×** | +4.6 | 2e-04 | 20/48 (SW480, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.19× | +4.3 | 7e-04 | 18/48 (PANC-1, SNU-423, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.13× | +4.3 | 9e-04 | 11/48 (RKO, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 1.18× | +4.2 | 0.001 | 22/48 (MIA PaCa-2, A498, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.37×** | +4.2 | 0.001 | 18/48 (LOX-IMVI, SNU-423, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.25×** | +4.0 | 0.002 | 17/48 (PANC-1, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **1.35×** | +4.0 | 0.002 | 17/47 (SNU-423, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.34×** | +3.9 | 0.003 | 13/48 (SNU-423, A-172, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.31×** | +3.6 | 0.009 | 17/48 (PANC-1, A498, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | 1.14× | +3.2 | 0.045 | 9/48 (A549, HCT15, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4052.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 10 lines (LS 180 0.0703×, HEC-1-A 0.196×, NCI-H460 0.189×, KATO III 0.123×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 8 lines (RKO 0.241×, SNU-423 0.438×, C32 0.462×, NCI-H460 0.601×, …); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (COLO 205 0.0857×, RKO 0.173×, HEC-1-A 0.324×; ⚠ toxic; transcription drop); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 3 lines (RKO 0.287×, C32 0.414×, A-172 0.462×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.448×** | -19.6 | 0e+00 | 36/42 (LS 180, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.493×** | -18.0 | 0e+00 | 43/49 (COLO 205, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.545×** | -14.3 | 8e-44 | 36/45 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.667×** | -9.9 | 5e-21 | 41/47 (AN3 CA, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.791×** | -8.5 | 3e-15 | 28/49 (RKO, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.819×** | -4.9 | 9e-05 | 23/48 (RKO, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.889× | -4.2 | 0.002 | 12/48 (HOP62, Hs 766T, …) | top dose only |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.882× | -3.1 | 0.12 | 15/49 (LS 180, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4052. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 65.6 | 4 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +23.1) | [[Dinaciclib (drug)]] 0.05 µM 0.407× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.588× (z -8.6) |
| [[RKO (line)]] | wt | 309 | 1 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.37× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.241× (z -20.0) |
| [[LOX-IMVI (line)]] | wt | 99.1 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.11× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.175× (z -19.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.594× (z -8.5) |
| [[PANC-1 (line)]] | alt | 51.4 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +20.7) | [[Dinaciclib (drug)]] 0.5 µM 0.435× (z -12.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 72.9 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +12.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.564× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 99.3 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.196× (z -23.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 59.5 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +14.1) | [[Dinaciclib (drug)]] 5 µM 0.372× (z -11.2) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 66.4 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.06× (z +9.0) | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.128× (z -8.7) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 78.0 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0629× (z -15.1) ⚠ toxic |
| [[C32 (line)]] | wt | 74.2 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.280× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -11.7) |
| [[Hs 766T (line)]] | wt | 148 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.198× (z -17.2) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 59.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.242× (z -16.0) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 113 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.383× (z -13.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 48.2 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.50× (z +13.8) | [[Dinaciclib (drug)]] 5 µM 0.210× (z -16.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 52.2 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.0703× (z -26.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 77.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.189× (z -22.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.601× (z -9.9) |
| [[AsPC-1 (line)]] | alt | 50.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.365× (z -9.3) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 100 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -14.6) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 64.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.55× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.193× (z -14.3) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 49.0 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.83× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.320× (z -11.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 39.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.446× (z -9.4) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 59.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.354× (z -11.1) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 68.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.282× (z -17.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 35.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +11.6) | — |
| [[A498 (line)]] | wt | 71.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.645× (z -9.4) |
| [[BT-474 (line)]] | alt | 37.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.219× (z -11.5) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 70.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.130× (z -11.0) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 83.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0857× (z -22.8) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 69.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.333× (z -9.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 58.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.212× (z -14.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 76.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.123× (z -21.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 51.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.375× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 33.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.364× (z -9.7) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 69.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.253× (z -14.2) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 60.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.412× (z -8.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 120 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -14.5) |
| [[SW 1088 (line)]] | alt | 72.1 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.0850× (z -8.8) ⚠ cell-cycle shift, explains ~45% of this change |
| [[SW 1271 (line)]] | alt | 187 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.191× (z -9.4) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 60.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +8.6) | — |
| [[C-33 A (line)]] | alt | 60.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 42.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 65.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 66.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 68.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 56.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4052), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 4 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMGCL]] | +0.63 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[FUT11]] | +0.61 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[MRPS18C]] | +0.60 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[ZNF264]] | +0.59 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[INIP]] | +0.57 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[FRA10AC1]] | +0.56 | +0.40 / +0.62 | both halves | 5e-05 |  |
| [[MOSPD2]] | +0.56 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[KRTCAP2]] | +0.55 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[ZCCHC9]] | +0.55 | +0.45 / +0.56 | both halves | 3e-05 | same gene group |
| [[KRT10]] ⚠ | +0.55 | +0.44 / +0.50 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NKAP]] | +0.54 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[HILPDA]] | +0.54 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[XRRA1]] | +0.54 | +0.52 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJB6]] | -0.59 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[ZNF37BP]] | -0.55 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[ATP11C]] | -0.55 | -0.37 / -0.59 | both halves | 8e-05 |  |
| [[MFSD14B]] | -0.54 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[YWHAQ]] | -0.54 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[HNRNPM]] | -0.54 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[JADE3]] | -0.52 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[CASTOR3P-1]] | -0.52 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[ILF2]] | -0.52 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[CNOT6]] | -0.52 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[FGD5-AS1]] | -0.49 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[PPIA]] | -0.49 | -0.32 / -0.52 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.245). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-41.0, -12.2); signed map (-12.9, -4.8). **Vector** length 102, 24.9% of its response variance represented; |z| ≥ 3 in 969 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +4.4 | +4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.1 | +3.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.0 | +2.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.0 | +3.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +7.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.7 | +3.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.3 | +2.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +3.1 | +4.0 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.5 | -9.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.9 | -0.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.3 | -14.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.0 | -8.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -2.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.7 | +0.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -4.2 |
|  | [[crizotinib (drug)]] 5 µM |  | -2.5 | -1.8 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -2.4 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | FKBP prolyl isomerase family member 15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q32 — chr9:113,161,006-113,221,458 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PPP1R76, FKBP133, WAFL; previously KIAA0674 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; FKBP prolyl isomerase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T1M5](https://www.uniprot.org/uniprotkb/Q5T1M5) (FK506-binding protein 15):

> May be involved in the cytoskeletal organization of neuronal growth cones. Seems to be inactive as a PPIase (By similarity). Involved in the transport of early endosomes at the level of transition between microfilament-based and microtubule-based movement.

**Summary**, from NCBI Gene [23307](https://www.ncbi.nlm.nih.gov/gene/23307):

> Predicted to enable actin binding activity and peptidyl-prolyl cis-trans isomerase activity. Predicted to be involved in endocytosis. Located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23397](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23397) · Entrez [23307](https://www.ncbi.nlm.nih.gov/gene/23307) · UniProt [Q5T1M5](https://www.uniprot.org/uniprotkb/Q5T1M5) · Ensembl [ENSG00000119321](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119321)

## Data

Gene col 4052: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4052); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4052, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4052]; `tensor/DDL_lfc|DDL_z.npy` [4052]; `embed/gene_vectors.npy` [4052]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4052 or target_col == 4052). Every well: [[FKBP15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FKBP15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
