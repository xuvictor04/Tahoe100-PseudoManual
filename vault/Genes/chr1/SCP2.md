---
symbol: "SCP2"
type: "gene"
col: 3770
ensembl_id: "ENSG00000116171"
name: "sterol carrier protein 2"
location: "1p32.3"
module: 29
arm: "+"
pooled_cpm: 60.98
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 14
n_dd_up_clean: 1
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# SCP2

*sterol carrier protein 2* — 1p32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.48× (z +23.5, q 0e+00, up in 44 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.22× (z +5.2, q 2e-05, up in 19 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 8 lines (HS-578T 4.39×, SW480 2.94×, NCI-H460 3.56×, LoVo 3.07×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (LoVo 3.51×, HS-578T 4.25×, SW480 2.50×, NCI-H1573 4.69×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HS-578T 3.50×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-172 2.07×); [[Radotinib (drug)]] 5 µM in 1 line (AsPC-1 2.17×).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.600× (z -18.6, q 0e+00, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SH3BGRL]] (+0.75, fdr 7e-06), [[ATP6V1A]] (+0.68, fdr 7e-06), [[NDRG3]] (+0.67, fdr 7e-06); moves opposite to [[EPOP]] (-0.63, fdr 1e-05), [[TLNRD1]] (-0.62, fdr 1e-05), [[ZBTB7A]] (-0.60, fdr 2e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3770.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 8 lines (HS-578T 4.39×, SW480 2.94×, NCI-H460 3.56×, LoVo 3.07×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (LoVo 3.51×, HS-578T 4.25×, SW480 2.50×, NCI-H1573 4.69×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HS-578T 3.50×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-172 2.07×); [[Radotinib (drug)]] 5 µM in 1 line (AsPC-1 2.17×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.48×** | +23.5 | 0e+00 | 44/48 (LoVo, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.37×** | +21.5 | 0e+00 | 39/42 (HS-578T, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.85×** | +14.7 | 0e+00 | 37/44 (HS-578T, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 1.16× | +5.5 | 5e-06 | 18/48 (LOX-IMVI, KATO III, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.22×** | +5.2 | 2e-05 | 19/48 (KATO III, HS-578T, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.18× | +4.9 | 7e-05 | 14/48 (AsPC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.13× | +4.5 | 7e-04 | 12/48 (AsPC-1, RPMI-7951, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 1.18× | +4.3 | 0.001 | 19/48 (LS 180, RKO, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.16× | +3.7 | 0.016 | 15/47 (HEC-1-A, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.15× | +3.5 | 0.028 | 14/48 (LoVo, AsPC-1, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 1.18× | +3.1 | 0.10 | 6/48 (C32, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.10× | +3.1 | 0.10 | 8/48 (NCI-H2347, SW480, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3770.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.600×** | -18.6 | 0e+00 | 38/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.619×** | -12.4 | 1e-32 | 33/48 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.681×** | -9.9 | 9e-21 | 39/48 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.691×** | -9.5 | 3e-19 | 36/48 (SNU-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.691×** | -9.1 | 7e-18 | 28/48 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.714×** | -8.7 | 5e-16 | 37/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.794×** | -8.4 | 5e-15 | 26/48 (Hs 766T, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.723×** | -8.3 | 5e-15 | 32/48 (Panc 03.27, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.778×** | -6.5 | 7e-09 | 26/48 (PANC-1, A498, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.804×** | -5.6 | 1e-06 | 25/48 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.807×** | -5.5 | 2e-06 | 22/48 (Hs 766T, SW480, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.859× | -5.5 | 2e-06 | 18/49 (MIA PaCa-2, SW 900, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.819×** | -5.1 | 1e-05 | 22/48 (Hs 766T, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.873× | -4.9 | 4e-05 | 18/48 (MIA PaCa-2, NCI-H1792, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.828×** | -4.8 | 5e-05 | 19/48 (MIA PaCa-2, SW 900, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.837× | -4.6 | 2e-04 | 19/48 (SW 1088, LOX-IMVI, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.837× | -4.4 | 3e-04 | 17/47 (H4, MIA PaCa-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.847× | -4.3 | 5e-04 | 20/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.849× | -4.2 | 7e-04 | 16/48 (SW 900, Panc 03.27, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.853× | -4.1 | 0.001 | 16/47 (MIA PaCa-2, LOX-IMVI, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3770. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 42.1 | 2 (2 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.56× (z +15.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -18.0) |
| [[MIA PaCa-2 (line)]] | alt | 67.7 | 1 (1 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.48× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -15.7) |
| [[PANC-1 (line)]] | alt | 73.1 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.54× (z +13.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -18.0) |
| [[A498 (line)]] | wt | 68.6 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.01× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.500× (z -14.1) |
| [[NCI-H1573 (line)]] | alt | 40.6 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.69× (z +14.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.471× (z -9.7) |
| [[A-172 (line)]] | wt | 31.9 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +12.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +9.0) | — |
| [[CFPAC-1 (line)]] | alt | 85.7 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +11.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.536× (z -10.7) |
| [[LoVo (line)]] | wt | 53.3 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +16.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -13.9) |
| [[A549 (line)]] | wt | 52.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -16.2) |
| [[HS-578T (line)]] | alt | 78.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.25× (z +16.8) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 43.1 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -12.0) |
| [[NCI-H1792 (line)]] | alt | 56.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.41× (z +12.9) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 72.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.399× (z -11.2) |
| [[SNU-423 (line)]] | alt | 53.1 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.83× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.515× (z -9.3) |
| [[SW 900 (line)]] | alt | 51.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.02× (z +11.3) ⚠ toxic; transcription drop | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.351× (z -8.5) |
| [[SW480 (line)]] | alt | 61.2 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.94× (z +16.2) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.574× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 33.4 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.45× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[Radotinib (drug)]] 5 µM 2.17× (z +8.6) | — |
| [[C32 (line)]] | wt | 50.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.68× (z +12.4) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 77.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.43× (z +12.1) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 58.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.99× (z +10.5) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 106 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.318× (z -17.1) |
| [[HT-29 (line)]] | alt | 59.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.57× (z +11.9) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 82.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -15.8) |
| [[KATO III (line)]] | alt | 73.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.71× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.561× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 66.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.12× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -14.3) |
| [[A-427 (line)]] | wt | 71.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.41× (z +9.9) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 56.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.22× (z +9.3) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 78.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -12.6) |
| [[HCT15 (line)]] | alt | 64.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.28× (z +10.1) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 32.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.36× (z +9.5) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 89.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.34× (z +11.2) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 66.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -14.2) |
| [[RKO (line)]] | wt | 70.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.524× (z -9.8) |
| [[RPMI-7951 (line)]] | alt | 62.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.483× (z -9.8) |
| [[SHP-77 (line)]] | alt | 49.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.77× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 21.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.237× (z -8.5) |
| [[SNU-1 (line)]] | wt | 72.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +10.3) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 101 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 43.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 52.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 64.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 80.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 66.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 70.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3770), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH3BGRL]] | +0.75 | +0.66 / +0.77 | both halves | 7e-06 |  |
| [[ATP6V1A]] | +0.68 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[NDRG3]] | +0.67 | +0.69 / +0.74 | both halves | 7e-06 |  |
| [[SCARB2]] | +0.65 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[DLD]] | +0.65 | +0.60 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_ADIPOGENESIS |
| [[MRPL19]] | +0.65 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[TSPAN6]] | +0.64 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[UBQLN1]] | +0.64 | +0.62 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_ADIPOGENESIS |
| [[LANCL1]] | +0.64 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[TM7SF3]] | +0.63 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[PRDX3]] | +0.62 | +0.56 / +0.62 | both halves | 1e-05 | pathway: HALLMARK_ADIPOGENESIS |
| [[RAD23B]] | +0.62 | +0.61 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPOP]] | -0.63 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[TLNRD1]] | -0.62 | -0.55 / -0.67 | both halves | 1e-05 |  |
| [[ZBTB7A]] | -0.60 | -0.47 / -0.63 | both halves | 2e-05 |  |
| [[SMIM12]] | -0.58 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[TUBB4B]] | -0.58 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[MIDN]] | -0.58 | -0.57 / -0.59 | both halves | 9e-06 |  |
| [[TPRN]] | -0.56 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[TPT1-AS1]] | -0.55 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[ALG2]] | -0.55 | -0.36 / -0.59 | both halves | 9e-05 |  |
| [[CLCF1]] | -0.55 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[ORAI1]] | -0.55 | -0.39 / -0.61 | both halves | 5e-05 |  |
| [[TUBB6]] | -0.54 | -0.46 / -0.58 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.696). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-25.5, -16.9); signed map (-20.2, -40.7). **Vector** length 105, 27.7% of its response variance represented; |z| ≥ 3 in 1,044 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | +5.4 | +5.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +21.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +23.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +14.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +4.3 | +4.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.7 | +4.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.3 | +2.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | +5.2 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +2.8 | +2.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.7 | +4.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.3 | -4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.1 | -3.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.1 | -12.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.1 | -8.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.7 | -4.0 |
|  | [[vincristine (drug)]] 0.5 µM |  | -3.4 | -0.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.3 | -5.5 |

## What is on record

|  |  |
|---|---|
| Name | sterol carrier protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p32.3 — chr1:52,927,276-53,051,698 (+) |
| Ensembl biotype | protein_coding |
| Also known as | nsLTP, SCPx, SCP-X |
| Gene groups (HGNC) | MicroRNA protein coding host genes; SCP2 domain containing |
| Hallmark sets | BILE_ACID_METABOLISM, PEROXISOME, ADIPOGENESIS |
| Reactome | 13 pathways, smallest: TYSND1 cleaves peroxisomal proteins; Beta-oxidation of pristanoyl-CoA; alpha-linolenic (omega3) and linoleic (omega6) acid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P22307](https://www.uniprot.org/uniprotkb/P22307) (Sterol carrier protein 2):

> [Isoform SCPx]: Plays a crucial role in the peroxisomal oxidation of branched-chain fatty acids. Catalyzes the last step of the peroxisomal beta-oxidation of branched chain fatty acids and the side chain of the bile acid intermediates di- and trihydroxycoprostanic acids (DHCA and THCA). Also active with medium and long straight chain 3-oxoacyl-CoAs. Stimulates the microsomal conversion of 7-dehydrocholesterol to cholesterol and transfers phosphatidylcholine and 7-dehydrocholesterol between …

**Summary**, from NCBI Gene [6342](https://www.ncbi.nlm.nih.gov/gene/6342):

> This gene encodes two proteins: sterol carrier protein X (SCPx) and sterol carrier protein 2 (SCP2), as a result of transcription initiation from 2 independently regulated promoters. The transcript initiated from the proximal promoter encodes the longer SCPx protein, and the transcript initiated from the distal promoter encodes the shorter SCP2 protein, with the 2 proteins sharing a common C-terminus. Evidence suggests that the SCPx protein is a peroxisome-associated thiolase that is involved …

**Accessions** — [HGNC:10606](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10606) · Entrez [6342](https://www.ncbi.nlm.nih.gov/gene/6342) · UniProt [P22307](https://www.uniprot.org/uniprotkb/P22307) · Ensembl [ENSG00000116171](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116171)

## Data

Gene col 3770: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3770); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3770, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3770]; `tensor/DDL_lfc|DDL_z.npy` [3770]; `embed/gene_vectors.npy` [3770]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3770 or target_col == 3770). Every well: [[SCP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
