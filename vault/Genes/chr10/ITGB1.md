---
symbol: "ITGB1"
type: "gene"
col: 7426
ensembl_id: "ENSG00000150093"
name: "integrin subunit beta 1"
location: "10p11.22"
module: 78
arm: "+"
pooled_cpm: 720.65
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 25
n_dd_up_clean: 4
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# ITGB1

*integrin subunit beta 1* — 10p11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.61× (z +9.0, q 9e-17, up in 36 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 1.52× (z +8.3, q 3e-14, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.577× (z -15.3, q 0e+00, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CORO1C]] (+0.72, fdr 7e-06), [[CAP1]] (+0.68, fdr 7e-06), [[ITGA6]] (+0.67, fdr 7e-06); moves opposite to [[THAP3]] (-0.66, fdr 7e-06), [[PHC3]] (-0.62, fdr 4e-05), [[COIL]] (-0.61, fdr 7e-06).
> It is in [[Module 078]], a single-armed module (apical junction).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CCN2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7426.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.61×** | +9.0 | 9e-17 | 36/44 (A498, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.57×** | +9.0 | 9e-17 | 38/49 (C32, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.52×** | +8.3 | 3e-14 | 46/48 (NCI-H460, SW480, …) | two highest doses | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.50×** | +8.0 | 2e-13 | 43/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.06×** | +7.0 | 2e-10 | 44/49 (Hs 766T, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.46×** | +6.9 | 7e-10 | 31/45 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.34×** | +5.8 | 7e-07 | 35/48 (NCI-H460, SW480, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.28×** | +4.9 | 6e-05 | 30/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.53×** | +4.1 | 0.002 | 29/38 (SNU-423, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.23×** | +4.0 | 0.004 | 26/47 (HT-29, CFPAC-1, …) | two highest doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.43×** | +3.5 | 0.028 | 25/48 (RPMI-7951, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.18× | +3.3 | 0.053 | 22/48 (HT-29, CFPAC-1, …) | two highest doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.37×** | +3.1 | 0.095 | 24/48 (SW480, BT-474, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7426.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.577×** | -15.3 | 0e+00 | 39/48 (J82, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.717×** | -9.3 | 6e-18 | 33/49 (RKO, A549, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.620×** | -9.0 | 3e-17 | 39/48 (CFPAC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.670×** | -7.9 | 5e-13 | 36/48 (HEC-1-A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.697×** | -7.1 | 1e-10 | 33/48 (A-172, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.719×** | -6.3 | 4e-08 | 34/47 (A549, A-427, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.736×** | -6.0 | 1e-07 | 36/48 (A549, J82, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.743×** | -5.8 | 4e-07 | 37/48 (RKO, MIA PaCa-2, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.814×** | -5.6 | 2e-06 | 28/49 (SW48, SW480, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.750×** | -5.4 | 3e-06 | 28/48 (A549, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.780×** | -4.9 | 5e-05 | 30/49 (NCI-H23, SW48, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.782×** | -4.8 | 6e-05 | 32/48 (NCI-H23, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.786×** | -4.7 | 1e-04 | 27/48 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | 0.847× | -4.6 | 2e-04 | 21/48 (AN3 CA, C-33 A, …) | rises with dose | low cells (technical?) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.827×** | -4.6 | 2e-04 | 27/48 (NCI-H23, SW48, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.796×** | -4.5 | 3e-04 | 26/48 (HEC-1-A, A-172, …) | all doses, stronger at high dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.853× | -4.4 | 3e-04 | 19/48 (A549, J82, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.802×** | -4.3 | 5e-04 | 26/48 (AsPC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.839× | -4.3 | 6e-04 | 23/48 (SW48, SW480, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7426. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 1,224 | 1 (1 ⚠) | 14 (5 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.96× (z +9.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.272× (z -18.2) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -16.3) |
| [[SW48 (line)]] | wt | 568 | 0 | 14 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -16.9) |
| [[NCI-H23 (line)]] | alt | 863 | 0 | 11 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -13.8) |
| [[NCI-H460 (line)]] | wt | 422 | 9 (7 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.57× (z +15.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.56× (z +15.5) | — |
| [[PANC-1 (line)]] | alt | 828 | 2 (2 ⚠) | 6 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.18× (z +10.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.437× (z -11.8) |
| [[A-172 (line)]] | wt | 547 | 3 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 2.39× (z +12.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.530× (z -12.9) |
| [[AsPC-1 (line)]] | alt | 1,711 | 2 (1 ⚠) | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.35× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.461× (z -11.6) |
| [[HT-29 (line)]] | alt | 501 | 4 (1 ⚠) | 3 | [[Vinblastine (sulfate) (drug)]] 5 µM 1.63× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.589× (z -9.9) |
| [[NCI-H1792 (line)]] | alt | 609 | 6 (5 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.53× (z +13.3) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.15× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.643× (z -9.2) |
| [[SNU-423 (line)]] | alt | 756 | 5 (4 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.45× (z +12.2) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 1.87× (z +8.9) | [[Harringtonine (drug)]] 5 µM 0.427× (z -11.6) |
| [[SW480 (line)]] | alt | 358 | 5 (3 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.56× (z +13.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.24× (z +11.7) | [[Trametinib (drug)]] 0.5 µM 0.591× (z -9.2) |
| [[A-427 (line)]] | wt | 1,138 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.467× (z -12.8) |
| [[AN3 CA (line)]] | alt | 518 | 4 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.35× (z +12.0) ⚠ toxic; transcription drop · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 1.93× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.516× (z -9.5) |
| [[H4 (line)]] | wt | 458 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.50× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -16.5) |
| [[HEC-1-A (line)]] | alt | 660 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.473× (z -15.8) |
| [[LoVo (line)]] | wt | 316 | 3 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 1.91× (z +10.8) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 2.94× (z +8.8) | [[Harringtonine (drug)]] 0.5 µM 0.512× (z -11.1) |
| [[C32 (line)]] | wt | 263 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.07× (z +13.8) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 4.66× (z +9.3) | [[Harringtonine (drug)]] 5 µM 0.481× (z -8.5) |
| [[J82 (line)]] | alt | 629 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -21.2) |
| [[NCI-H1573 (line)]] | alt | 960 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -16.6) |
| [[RKO (line)]] | wt | 1,828 | 1 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.87× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -16.6) |
| [[CFPAC-1 (line)]] | alt | 1,469 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -16.0) |
| [[LS 180 (line)]] | wt | 517 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -17.6) |
| [[MIA PaCa-2 (line)]] | alt | 992 | 2 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 2.14× (z +9.6) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.95× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -16.0) |
| [[HOP62 (line)]] | alt | 840 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.23× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.596× (z -8.9) |
| [[HS-578T (line)]] | alt | 855 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.16× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.553× (z -11.4) |
| [[KATO III (line)]] | alt | 403 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 1.94× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.499× (z -13.6) |
| [[NCI-H2030 (line)]] | alt | 996 | 2 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.14× (z +10.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.03× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.564× (z -10.8) |
| [[NCI-H2347 (line)]] | alt | 608 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.526× (z -15.0) |
| [[Panc 03.27 (line)]] | alt | 841 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.490× (z -14.2) |
| [[SHP-77 (line)]] | alt | 207 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.17× (z +13.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.587× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 324 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.54× (z +13.0) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 963 | 1 | 2 | [[TAK-901 (drug)]] 5 µM 6.49× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.446× (z -11.7) |
| [[A498 (line)]] | wt | 766 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.38× (z +13.3) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 533 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -14.4) |
| [[CHP-212 (line)]] | wt | 280 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.15× (z +12.0) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 295 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.66× (z +11.1) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 868 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.508× (z -13.5) |
| [[RPMI-7951 (line)]] | alt | 1,146 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 2.95× (z +8.8) | [[Harringtonine (drug)]] 5 µM 0.543× (z -9.7) |
| [[SW 1088 (line)]] | alt | 767 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -11.9) |
| [[SW 900 (line)]] | alt | 439 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 1.89× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.486× (z -14.7) |
| [[BT-474 (line)]] | alt | 472 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.495× (z -8.9) ⚠ cell-cycle shift, explains ~23% of this change |
| [[COLO 205 (line)]] | alt | 292 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.46× (z +13.0) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 1,028 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.491× (z -12.9) |
| [[Hs 766T (line)]] | wt | 364 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.61× (z +11.0) | — |
| [[hTERT-HPNE (line)]] | wt | 1,280 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.501× (z -11.8) |
| [[NCI-H2122 (line)]] | alt | 695 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 625 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 638 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 667 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 504 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7426), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CORO1C]] | +0.72 | +0.75 / +0.70 | both halves | 7e-06 |  |
| [[CAP1]] | +0.68 | +0.76 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_APICAL_JUNCTION |
| [[ITGA6]] | +0.67 | +0.63 / +0.65 | both halves | 7e-06 | same gene group; pathway: Basigin interactions; STRING 999 |
| [[SEPTIN10]] | +0.66 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[ADGRE3]] | +0.66 | +0.74 / +0.56 | both halves | 1e-05 |  |
| [[ASPH]] | +0.66 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[DIAPH1]] | +0.65 | +0.65 / +0.61 | both halves | 7e-06 | pathway: RHO GTPase Effectors |
| [[TPM4]] | +0.65 | +0.65 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[ACTN1]] | +0.64 | +0.69 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_APICAL_JUNCTION; STRING 974 |
| [[APLP2]] | +0.64 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[ARPC2]] | +0.64 | +0.68 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_APICAL_JUNCTION |
| [[LAMC1]] | +0.63 | +0.71 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 982 |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THAP3]] | -0.66 | -0.64 / -0.58 | both halves | 7e-06 |  |
| [[PHC3]] | -0.62 | -0.61 / -0.41 | both halves | 4e-05 |  |
| [[COIL]] | -0.61 | -0.58 / -0.61 | both halves | 7e-06 |  |
| [[FNBP4]] | -0.61 | -0.64 / -0.43 | both halves | 3e-05 |  |
| [[ZCCHC10]] | -0.61 | -0.53 / -0.62 | both halves | 1e-05 |  |
| [[RBM5]] | -0.61 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[WHAMM]] | -0.60 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[CCDC59]] | -0.60 | -0.69 / -0.44 | both halves | 3e-05 |  |
| [[BTN2A1]] | -0.60 | -0.60 / -0.46 | both halves | 2e-05 |  |
| [[FDX2]] | -0.59 | -0.64 / -0.51 | both halves | 1e-05 |  |
| [[CCDC174]] | -0.58 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[PPIG]] | -0.58 | -0.66 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCN2]] | B | CCN2 activity raises ITGB1's level | lines that do not express CCN2 (17) vs lines expressing it (33) | 1.63× lower at baseline in the lines without CCN2 | 0.016 | ⚠ within organs, on part of the lines; also absent: GDNF-AS1, CPEB1, TRIML2 |
| [[MAP2K1]] | B | MAP2K1 activity raises ITGB1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.777). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (40.0, 5.4); signed map (-8.7, 38.0). **Vector** length 150, 60.4% of its response variance represented; |z| ≥ 3 in 1,889 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +11.1 | +6.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +7.5 | -4.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.2 | +9.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.1 | +9.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +6.9 | -2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +0.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.1 | -1.0 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +3.5 | +2.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +3.4 | +2.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.2 | +2.1 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -11.1 | -9.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -10.0 | -7.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.8 | -7.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.7 | -15.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.1 | -6.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.1 | -4.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.9 | -3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.9 | -4.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.7 | -4.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -4.7 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | integrin subunit beta 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p11.22 — chr10:32,887,273-33,005,792 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CD29, GPIIA; previously FNRB, MSK12, MDF2 |
| Gene groups (HGNC) | CD molecules; Integrin beta subunits |
| Hallmark sets | MYOGENESIS, APICAL_JUNCTION, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 64 pathways, smallest: Localization of the PINCH-ILK-PARVIN complex to focal adhesions; MET interacts with TNS proteins; CHL1 interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [P05556](https://www.uniprot.org/uniprotkb/P05556) (Integrin beta-1):

> Integrins alpha-1/beta-1, alpha-2/beta-1, alpha-10/beta-1 and alpha-11/beta-1 are receptors for collagen. Integrins alpha-1/beta-1 and alpha-2/beta-2 recognize the proline-hydroxylated sequence G-F-P-G-E-R in collagen. Integrins alpha-2/beta-1, alpha-3/beta-1, alpha-4/beta-1, alpha-5/beta-1, alpha-8/beta-1, alpha-10/beta-1, alpha-11/beta-1 and alpha-V/beta-1 are receptors for fibronectin. Alpha-4/beta-1 recognizes one or more domains within the alternatively spliced CS-1 and CS-5 regions of …

**Summary**, from NCBI Gene [3688](https://www.ncbi.nlm.nih.gov/gene/3688):

> Integrins are heterodimeric proteins made up of alpha and beta subunits. At least 18 alpha and 8 beta subunits have been described in mammals. Integrin family members are membrane receptors involved in cell adhesion and recognition in a variety of processes including embryogenesis, hemostasis, tissue repair, immune response and metastatic diffusion of tumor cells. This gene encodes a beta subunit. Multiple alternatively spliced transcript variants which encode different protein isoforms have …

**Accessions** — [HGNC:6153](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6153) · Entrez [3688](https://www.ncbi.nlm.nih.gov/gene/3688) · UniProt [P05556](https://www.uniprot.org/uniprotkb/P05556) · Ensembl [ENSG00000150093](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000150093)

## Data

Gene col 7426: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7426); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7426, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7426]; `tensor/DDL_lfc|DDL_z.npy` [7426]; `embed/gene_vectors.npy` [7426]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7426 or target_col == 7426). Every well: [[ITGB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ITGB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
