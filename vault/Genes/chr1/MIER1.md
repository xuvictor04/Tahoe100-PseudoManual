---
symbol: "MIER1"
type: "gene"
col: 12542
ensembl_id: "ENSG00000198160"
name: "MIER1 transcriptional regulator"
location: "1p31.3"
module: 17
arm: "+"
pooled_cpm: 157.01
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 7
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# MIER1

*MIER1 transcriptional regulator* — 1p31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.82× (z +20.3, q 0e+00, up in 45 of 48 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.95× (z +16.1, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.691× (z -8.6, q 5e-15, down in 32 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.737× (z -7.4, q 5e-11, down in 34 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 9 lines (NCI-H23 0.0937×, BT-474 0.206×, A-427 0.404×, HEC-1-A 0.443×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (NCI-H23 0.627×, NCI-H2347 0.613×, HS-578T 0.616×; ⚠ cell-cycle shift, explains ~16% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H2347 0.403×, RKO 0.468×; ⚠ toxic; cell-cycle shift, explains ~29% of this change); [[Auranofin (drug)]] 5 µM in 2 lines (NCI-H460 0.557×, H4 0.458×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPP4R2]] (+0.70, fdr 7e-06), [[XPA]] (+0.68, fdr 7e-06), [[ATG3]] (+0.68, fdr 7e-06); moves opposite to [[SMG1P6]] (-0.65, fdr 1e-05), [[PDCD6]] (-0.59, fdr 1e-05), [[NPIPB11]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12542.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.82×** | +20.3 | 0e+00 | 45/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.95×** | +16.1 | 0e+00 | 48/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.98×** | +15.8 | 0e+00 | 46/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.85×** | +14.8 | 0e+00 | 46/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.73×** | +13.2 | 2e-37 | 47/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.63×** | +11.8 | 4e-30 | 42/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.24×** | +10.2 | 3e-22 | 44/49 (SW480, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.48×** | +9.4 | 5e-19 | 40/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +8.8 | 6e-17 | 38/47 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.41×** | +8.3 | 7e-15 | 38/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.40×** | +8.0 | 4e-14 | 35/48 (A-172, PANC-1, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.67×** | +6.4 | 6e-09 | 38/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.26×** | +5.1 | 1e-05 | 26/48 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.22×** | +4.7 | 9e-05 | 22/48 (A-427, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.20×** | +4.1 | 0.002 | 25/47 (A549, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.15× | +3.4 | 0.020 | 21/48 (SK-MEL-2, LoVo, …) | rises with dose |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.15× | +3.4 | 0.026 | 15/48 (HOP62, A549, …) | inconsistent across doses | low cells (technical?) |
| [[Hexylresorcinol (drug)]] 5 µM |  | 1.10× | +3.1 | 0.051 | 1/49 (NCI-H2030) | top dose only | position effect removed |
| [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | 1.13× | +2.9 | 0.098 | 6/49 (J82, HT-29, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 9 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12542.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 9 lines (NCI-H23 0.0937×, BT-474 0.206×, A-427 0.404×, HEC-1-A 0.443×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (NCI-H23 0.627×, NCI-H2347 0.613×, HS-578T 0.616×; ⚠ cell-cycle shift, explains ~16% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H2347 0.403×, RKO 0.468×; ⚠ toxic; cell-cycle shift, explains ~29% of this change); [[Auranofin (drug)]] 5 µM in 2 lines (NCI-H460 0.557×, H4 0.458×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.691×** | -8.6 | 5e-15 | 32/44 (NCI-H23, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.737×** | -7.4 | 5e-11 | 34/48 (NCI-H460, H4, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.817×** | -6.9 | 8e-10 | 27/49 (NCI-H23, NCI-H2347, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.771×** | -6.1 | 2e-07 | 32/47 (NCI-H2347, RKO, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.783×** | -5.9 | 4e-07 | 27/49 (NCI-H2347, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | 0.874× | -4.6 | 4e-04 | 13/48 (HS-578T, SNU-423, …) | rises with dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.830×** | -4.5 | 5e-04 | 23/48 (HEC-1-A, AsPC-1, …) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 0.836× | -4.2 | 0.002 | 24/48 (HS-578T, NCI-H23, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 0.843× | -4.0 | 0.004 | 20/50 (HS-578T, NCI-H2347, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.849× | -4.0 | 0.004 | 19/48 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.854× | -3.8 | 0.006 | 11/48 (CFPAC-1, HOP62, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.863× | -3.6 | 0.016 | 16/48 (COLO 205, SW480, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.864× | -3.5 | 0.018 | 17/48 (HepG2/C3A, NCI-H2347, …) | two highest doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.909× | -3.3 | 0.044 | 5/48 (C-33 A, SW 1271, …) | top dose only |  |
| [[OTS514 (drug)]] 5 µM |  | **0.781×** | -3.1 | 0.065 | 16/46 (A-172, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 0.875× | -3.1 | 0.065 | 14/49 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12542. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 99.5 | 11 (4 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 3.22× (z +17.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.89× (z +15.5) | [[Auranofin (drug)]] 5 µM 0.557× (z -8.6) |
| [[PANC-1 (line)]] | alt | 168 | 11 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +36.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.76× (z +26.1) | — |
| [[SW480 (line)]] | alt | 134 | 11 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +19.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.50× (z +18.8) | — |
| [[H4 (line)]] | wt | 164 | 8 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +12.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.82× (z +11.2) | [[Auranofin (drug)]] 5 µM 0.458× (z -8.5) |
| [[HOP62 (line)]] | alt | 160 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +15.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.73× (z +13.8) | — |
| [[LoVo (line)]] | wt | 123 | 8 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.37× (z +17.1) | — |
| [[A549 (line)]] | wt | 120 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +19.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.63× (z +12.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.617× (z -8.7) ⚠ cell-cycle shift, explains ~16% of this change |
| [[NCI-H23 (line)]] | alt | 156 | 4 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +21.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.16× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.0937× (z -36.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 186 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +20.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.74× (z +13.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.468× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~29% of this change |
| [[A-427 (line)]] | wt | 152 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +12.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.10× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.404× (z -13.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 167 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +19.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.52× (z +15.6) | — |
| [[C32 (line)]] | wt | 138 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +14.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.37× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.439× (z -9.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 255 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.02× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.616× (z -9.4) ⚠ cell-cycle shift, explains ~16% of this change |
| [[J82 (line)]] | alt | 144 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +13.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.04× (z +10.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 145 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +12.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.75× (z +11.7) | — |
| [[NCI-H2347 (line)]] | alt | 264 | 1 | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.97× (z +9.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.403× (z -12.3) ⚠ toxic; cell-cycle shift, explains ~29% of this change |
| [[A-172 (line)]] | wt | 148 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +15.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 2.70× (z +14.8) | — |
| [[AsPC-1 (line)]] | alt | 154 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +12.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.70× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.458× (z -9.1) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 78.7 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.67× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.206× (z -16.9) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 162 | 4 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.24× (z +10.6) | — |
| [[HT-29 (line)]] | alt | 131 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +15.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +11.8) | — |
| [[KATO III (line)]] | alt | 94.3 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.82× (z +15.0) | — |
| [[LOX-IMVI (line)]] | wt | 194 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +12.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.11× (z +10.5) | — |
| [[LS 180 (line)]] | wt | 151 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.74× (z +16.3) | — |
| [[SW 900 (line)]] | alt | 172 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.64× (z +11.7) | — |
| [[SW1417 (line)]] | alt | 188 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +10.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.14× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.459× (z -10.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 190 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +14.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.14× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.443× (z -10.6) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 133 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.67× (z +10.9) | — |
| [[NCI-H1573 (line)]] | alt | 134 | 3 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.79× (z +13.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.65× (z +13.2) | — |
| [[SK-MEL-2 (line)]] | alt | 111 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +18.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.55× (z +11.2) | — |
| [[CFPAC-1 (line)]] | alt | 210 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +11.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.03× (z +8.9) | — |
| [[COLO 205 (line)]] | alt | 150 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.53× (z +11.4) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 4.26× (z +9.7) | — |
| [[NCI-H1792 (line)]] | alt | 130 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.65× (z +11.5) | — |
| [[Panc 03.27 (line)]] | alt | 164 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +12.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.04× (z +9.7) | — |
| [[SNU-423 (line)]] | alt | 140 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +13.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.06× (z +9.2) | — |
| [[C-33 A (line)]] | alt | 179 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.08× (z +9.0) | — |
| [[NCI-H2030 (line)]] | alt | 198 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.56× (z +9.4) | — |
| [[RPMI-7951 (line)]] | alt | 176 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 2.16× (z +8.6) | — |
| [[SHP-77 (line)]] | alt | 138 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.433× (z -9.7) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 120 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.57× (z +8.9) | — |
| [[AN3 CA (line)]] | alt | 208 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 88.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 153 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 179 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 205 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 158 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 143 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12542), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP4R2]] | +0.70 | +0.66 / +0.73 | both halves | 7e-06 |  |
| [[XPA]] | +0.68 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[ATG3]] | +0.68 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[C16orf87]] | +0.65 | +0.72 / +0.60 | both halves | 7e-06 | STRING 735 |
| [[VAPA]] | +0.65 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[ZC3H15]] | +0.64 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[METTL14]] | +0.63 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[HPF1]] | +0.63 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[RAB30]] | +0.63 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[ZNF592]] | +0.63 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[EBAG9]] | +0.62 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[SCAF11]] | +0.61 | +0.57 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMG1P6]] | -0.65 | -0.51 / -0.64 | both halves | 1e-05 |  |
| [[PDCD6]] | -0.59 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[NPIPB11]] | -0.58 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[PIGG]] | -0.57 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[RBM14-RBM4]] | -0.57 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[MAD1L1]] | -0.57 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[ZNF587]] | -0.57 | -0.44 / -0.63 | both halves | 3e-05 |  |
| [[PMPCA]] | -0.56 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[CUL4A]] | -0.56 | -0.39 / -0.62 | both halves | 5e-05 |  |
| [[ZNF731P]] | -0.56 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[FUBP3]] | -0.56 | -0.40 / -0.56 | both halves | 5e-05 |  |
| [[SENP5]] | -0.55 | -0.53 / -0.59 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.563). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-21.5, -3.6); signed map (-22.4, -9.7). **Vector** length 103, 34.5% of its response variance represented; |z| ≥ 3 in 1,210 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.0 | +8.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.0 | +14.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.0 | +11.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.0 | +2.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.2 | +2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.7 | -0.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.9 | -0.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.9 | +4.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.5 | -7.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.2 | -0.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.3 | +4.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.9 | -1.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.4 | -0.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.7 | +6.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.6 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | +3.4 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.3 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | MIER1 transcriptional regulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.3 — chr1:66,924,895-66,988,619 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hMI-ER1, MI-ER1, KIAA1610 |
| Gene groups (HGNC) | Myb/SANT domain containing; MIER complex subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N108](https://www.uniprot.org/uniprotkb/Q8N108) (Mesoderm induction early response protein 1):

> Transcriptional repressor regulating the expression of a number of genes including SP1 target genes. Probably functions through recruitment of HDAC1 a histone deacetylase involved in chromatin silencing.

**Summary**, from NCBI Gene [57708](https://www.ncbi.nlm.nih.gov/gene/57708):

> This gene encodes a protein that was first identified in Xenopus laevis by its role in a mesoderm induction early response (MIER). The encoded protein functions as a transcriptional regulator. Alternatively spliced transcript variants encode multiple isoforms, some of which lack a C-terminal nuclear localization signal. [provided by RefSeq, May 2013]

**Accessions** — [HGNC:29657](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29657) · Entrez [57708](https://www.ncbi.nlm.nih.gov/gene/57708) · UniProt [Q8N108](https://www.uniprot.org/uniprotkb/Q8N108) · Ensembl [ENSG00000198160](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198160)

## Data

Gene col 12542: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12542); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12542, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12542]; `tensor/DDL_lfc|DDL_z.npy` [12542]; `embed/gene_vectors.npy` [12542]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12542 or target_col == 12542). Every well: [[MIER1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIER1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
