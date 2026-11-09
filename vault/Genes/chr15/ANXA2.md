---
symbol: "ANXA2"
type: "gene"
col: 11318
ensembl_id: "ENSG00000182718"
name: "annexin A2"
location: "15q22.2"
module: 111
arm: "+"
pooled_cpm: 801.73
n_lines_expressing: 46
n_dd_up: 8
n_dd_down: 16
n_dd_up_clean: 3
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 10
direction_downstream: 5
tags: ["gene", "module/111"]
generated_by: "tahoemap"
---

# ANXA2

*annexin A2* — 15q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.97× (z +13.0, q 1e-35, up in 40 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.22× (z +3.8, q 0.015, up in 22 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.592× (z -14.2, q 4e-43, down in 38 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[YWHAZ]] (+0.67, fdr 7e-06), [[ANXA1]] (+0.63, fdr 7e-06), [[IQGAP1]] (+0.62, fdr 7e-06); moves opposite to [[YBEY]] (-0.60, fdr 1e-05), [[ZNF785]] (-0.55, fdr 2e-05), [[SETDB1]] (-0.54, fdr 1e-05).
> It is in [[Module 111]], a single-armed module (Cell-Cell communication).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[F3]] → it (grade B ⚠); 5 go from it, the strongest it → [[PLS3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11318.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.97×** | +13.0 | 1e-35 | 40/45 (A-427, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.90×** | +11.9 | 6e-30 | 36/40 (A498, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.57×** | +8.0 | 2e-13 | 33/41 (A-427, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~22% of this change | **1.29×** | +4.6 | 5e-04 | 25/43 (NCI-H460, SW1417, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.55×** | +4.4 | 0.001 | 28/35 (NCI-H2347, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.22×** | +3.8 | 0.015 | 22/43 (NCI-H460, SW48, …) | two highest doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.20× | +3.5 | 0.034 | 20/44 (A-427, HCT15, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +3.5 | 0.034 | 15/44 (LS 180, HS-578T, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.034 | 19/43 (SK-MEL-2, HT-29, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.40×** | +3.4 | 0.042 | 27/44 (MIA PaCa-2, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +3.2 | 0.064 | 0/46 | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.18× | +3.2 | 0.068 | 19/44 (MIA PaCa-2, SK-MEL-2, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | 1.19× | +3.2 | 0.068 | 14/44 (MIA PaCa-2, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11318.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.592×** | -14.2 | 4e-43 | 38/45 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.654×** | -11.5 | 2e-28 | 33/44 (NCI-H1573, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.567×** | -10.9 | 2e-25 | 37/44 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.612×** | -9.1 | 2e-17 | 33/43 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.663×** | -7.9 | 3e-13 | 42/44 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.665×** | -7.8 | 5e-13 | 34/44 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.780×** | -6.8 | 1e-09 | 31/44 (NCI-H1573, LOX-IMVI, …) | rises with dose | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM |  | **0.709×** | -6.6 | 3e-09 | 34/44 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.720×** | -6.3 | 2e-08 | 34/44 (LS 180, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.723×** | -6.2 | 2e-08 | 28/44 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.756×** | -5.2 | 1e-05 | 30/44 (NCI-H460, A549, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.791×** | -4.5 | 3e-04 | 26/44 (HOP62, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.800×** | -4.3 | 7e-04 | 26/44 (NCI-H1573, SK-MEL-2, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.804×** | -4.2 | 0.001 | 28/44 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Amsacrine (drug)]] 5 µM |  | 0.857× | -4.2 | 0.001 | 15/44 (A549, J82, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.831×** | -3.6 | 0.012 | 23/44 (HEC-1-A, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.841× | -3.3 | 0.027 | 19/44 (KATO III, LS 180, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.843× | -3.3 | 0.030 | 21/44 (LoVo, LS 180, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.844× | -3.3 | 0.032 | 18/44 (LoVo, KATO III, …) | all doses, flat |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.845× | -3.2 | 0.032 | 20/44 (LS 180, NCI-H460, …) | inconsistent across doses |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | 0.854× | -3.0 | 0.060 | 12/44 (SW480, LOX-IMVI, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11318. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 1,273 | 0 | 17 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -16.8) |
| [[A549 (line)]] | wt | 1,751 | 1 (1 ⚠) | 11 (5 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.15× (z +11.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -23.2) |
| [[LS 180 (line)]] | wt | 1,216 | 1 | 10 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.64× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -16.4) |
| [[PANC-1 (line)]] | alt | 893 | 3 (3 ⚠) | 8 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.39× (z +15.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.294× (z -21.5) |
| [[HEC-1-A (line)]] | alt | 826 | 0 | 9 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.346× (z -16.3) |
| [[HOP62 (line)]] | alt | 1,010 | 2 (2 ⚠) | 7 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.27× (z +10.0) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -14.4) |
| [[LOX-IMVI (line)]] | wt | 728 | 0 | 9 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.366× (z -16.1) |
| [[MIA PaCa-2 (line)]] | alt | 477 | 7 (4 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.57× (z +14.1) ⚠ toxic; transcription drop · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 1.89× (z +13.4) | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.429× (z -12.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.608× (z -10.6) |
| [[NCI-H1573 (line)]] | alt | 992 | 1 (1 ⚠) | 8 (4 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.89× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -24.5) |
| [[A-427 (line)]] | wt | 238 | 8 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.59× (z +18.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 2.20× (z +11.1) | — |
| [[J82 (line)]] | alt | 963 | 2 (2 ⚠) | 6 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.29× (z +10.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.428× (z -11.0) |
| [[NCI-H2347 (line)]] | alt | 904 | 3 (3 ⚠) | 5 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.77× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.456× (z -18.5) |
| [[KATO III (line)]] | alt | 1,267 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -18.4) |
| [[NCI-H460 (line)]] | wt | 669 | 2 (2 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.95× (z +11.2) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -19.2) |
| [[SW480 (line)]] | alt | 881 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.28× (z +11.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.474× (z -14.1) |
| [[A-172 (line)]] | wt | 1,001 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.436× (z -12.0) |
| [[CFPAC-1 (line)]] | alt | 1,318 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.78× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -19.4) |
| [[NCI-H23 (line)]] | alt | 326 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.43× (z +12.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.69× (z +10.9) | — |
| [[AsPC-1 (line)]] | alt | 962 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.460× (z -16.7) |
| [[BT-474 (line)]] | alt | 513 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.373× (z -11.9) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.578× (z -9.4) |
| [[H4 (line)]] | wt | 746 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.522× (z -10.7) |
| [[HCT15 (line)]] | alt | 563 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.50× (z +11.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.557× (z -10.3) |
| [[HS-578T (line)]] | alt | 683 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.12× (z +10.7) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.613× (z -10.3) |
| [[NCI-H1792 (line)]] | alt | 642 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.20× (z +10.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -17.4) |
| [[NCI-H2030 (line)]] | alt | 523 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.38× (z +12.1) ⚠ toxic; transcription drop | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.437× (z -11.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[Panc 03.27 (line)]] | alt | 1,206 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 1.99× (z +9.8) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.494× (z -14.1) |
| [[SW1417 (line)]] | alt | 825 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.23× (z +12.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.588× (z -11.8) |
| [[SW48 (line)]] | wt | 1,132 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -16.1) |
| [[A498 (line)]] | wt | 520 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.40× (z +15.8) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 255 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.04× (z +12.8) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 959 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -16.7) |
| [[RPMI-7951 (line)]] | alt | 926 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.466× (z -13.8) |
| [[SK-MEL-2 (line)]] | alt | 527 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.23× (z +11.7) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.606× (z -10.5) |
| [[Hs 766T (line)]] | wt | 850 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.604× (z -10.4) |
| [[hTERT-HPNE (line)]] | wt | 637 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.01× (z +12.0) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 472 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.93× (z +9.5) ⚠ toxic; transcription drop | [[Selinexor (drug)]] 5 µM 0.582× (z -11.0) ⚠ cell-cycle shift, explains ~55% of this change |
| [[SNU-423 (line)]] | alt | 745 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.71× (z +12.4) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 281 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.04× (z +12.2) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 570 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 1.94× (z +8.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[CHP-212 (line)]] | wt | 377 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.87× (z +9.7) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 1,174 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -13.0) |
| [[SW 1088 (line)]] | alt | 909 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -9.3) |
| [[AN3 CA (line)]] | alt | 188 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 141 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 997 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 705 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 435 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 193 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 195 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 865 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11318), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YWHAZ]] | +0.67 | +0.67 / +0.74 | both halves | 7e-06 | STRING 630 |
| [[ANXA1]] | +0.63 | +0.60 / +0.61 | both halves | 7e-06 | same gene group; pathway: Muscle contraction; STRING 989 |
| [[IQGAP1]] | +0.62 | +0.58 / +0.67 | both halves | 7e-06 | STRING 680 |
| [[CAST]] | +0.61 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[EZR]] | +0.61 | +0.55 / +0.58 | both halves | 1e-05 | STRING 725 |
| [[ANXA5]] | +0.60 | +0.55 / +0.67 | both halves | 1e-05 | same gene group; STRING 833 |
| [[TPM4]] | +0.60 | +0.52 / +0.61 | both halves | 1e-05 | pathway: Muscle contraction |
| [[CORO1C]] | +0.60 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[ACTB]] | +0.59 | +0.53 / +0.61 | both halves | 1e-05 | STRING 767 |
| [[DSG2]] | +0.59 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[FLNB]] | +0.59 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[KRT8]] | +0.59 | +0.58 / +0.53 | both halves | 1e-05 | STRING 407 |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YBEY]] | -0.60 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[ZNF785]] | -0.55 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[SETDB1]] | -0.54 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[PABPN1]] | -0.54 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[NAA60]] | -0.53 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[MIR762HG]] | -0.53 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[SELENOH]] | -0.53 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[ZCCHC10]] | -0.53 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[LAMTOR4]] | -0.52 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[SUZ12P1]] | -0.52 | -0.55 / -0.38 | both halves | 6e-05 |  |
| [[GUSBP11]] | -0.52 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[LSM7]] | -0.52 | -0.45 / -0.54 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 7, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[F3]] | B | F3 activity raises ANXA2's level | lines that do not express F3 (24) vs lines expressing it (26) | 1.93× lower at baseline in the lines without F3 | 0.004 | ⚠ within organs, on part of the lines; also absent: TLR2, KRT7, EDNRA |
| [[MET]] | B | MET activity raises ANXA2's level | lines that do not express MET (9) vs lines expressing it (41) | 2.58× lower at baseline in the lines without MET | 0.006 | ⚠ within organs, on part of the lines; also absent: TGFBR2, PHLDA2, VDR |
| [[MYOF]] | B | MYOF activity raises ANXA2's level | lines that do not express MYOF (6) vs lines expressing it (44) | 2.86× lower at baseline in the lines without MYOF | 0.017 | ⚠ within organs, on part of the lines; also absent: ENSG00000286511, ACCS, CAV2 |
| [[KRT7]] | B | KRT7 activity raises ANXA2's level | lines that do not express KRT7 (34) vs lines expressing it (16) | 1.52× lower at baseline in the lines without KRT7 | 0.026 | ⚠ within organs, on part of the lines; also absent: VSIG1, GSDMC, SERPINB3 |
| [[ITGA6]] | B | ITGA6 activity raises ANXA2's level | lines that do not express ITGA6 (9) vs lines expressing it (41) | 1.60× lower at baseline in the lines without ITGA6 | 0.037 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ANXA1]] | B | ANXA1 activity raises ANXA2's level | lines that do not express ANXA1 (9) vs lines expressing it (41) | 1.99× lower at baseline in the lines without ANXA1 | 0.072 | ⚠ within organs, on part of the lines; also absent: FXYD5, CAV2, RAB27B |
| [[KRT81]] | B | KRT81 activity raises ANXA2's level | lines that do not express KRT81 (34) vs lines expressing it (16) | 1.62× lower at baseline in the lines without KRT81 | 0.089 | ⚠ within organs, on part of the lines; also absent: CARD11, ANXA8, PSG9 |
| [[PLS3]] | C | PLS3 activity raises ANXA2's level | lines that do not express PLS3 (4) vs lines expressing it (46) | 2.65× lower at baseline in the lines without PLS3 | 0.021 | ⚠ few lines (4 vs 46); across organs; also absent: FOSL1, IGF2BP2, FCHSD1; maybe low, not absent |
| [[CAV2]] | C | CAV2 activity raises ANXA2's level | lines that do not express CAV2 (8) vs lines expressing it (42) | 2.93× lower at baseline in the lines without CAV2 | 0.029 | ⚠ within organs, on part of the lines; co-absent genes; also absent: PLAUR, LRRK1, HRH1; maybe low, not absent; co-absent with the target |
| [[FLNB]] | C | FLNB activity raises ANXA2's level | lines that do not express FLNB (3) vs lines expressing it (47) | 2.80× lower at baseline in the lines without FLNB | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MYO1E, B4GALT1, SMOX; maybe low, not absent; its own permutation p |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLS3]] | C | ANXA2 activity raises PLS3's level | lines that do not express ANXA2 (4) vs lines expressing it (46) | 2.70× lower at baseline in the lines without ANXA2 | 0.081 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PHF11, RARG, NABP1; maybe low, not absent; its own permutation p |
| [[FLNA]] | C | ANXA2 activity raises FLNA's level | lines that do not express ANXA2 (4) vs lines expressing it (46) | 1.83× lower at baseline in the lines without ANXA2 | 0.081 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PHF11, RARG, NABP1; maybe low, not absent; its own permutation p |
| [[CAV2]] | C | ANXA2 activity raises CAV2's level | lines that do not express ANXA2 (4) vs lines expressing it (46) | 4.72× lower at baseline in the lines without ANXA2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PHF11, RARG, NABP1; maybe low, not absent; co-absent with the target; its own permutation p |
| [[ANXA1]] | C | ANXA2 activity raises ANXA1's level | lines that do not express ANXA2 (4) vs lines expressing it (46) | 3.04× lower at baseline in the lines without ANXA2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PHF11, RARG, NABP1; maybe low, not absent; its own permutation p |
| [[MIR762HG]] | C | ANXA2 activity lowers MIR762HG's level | lines that do not express ANXA2 (4) vs lines expressing it (46) | 1.47× higher at baseline in the lines without ANXA2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PHF11, RARG, NABP1; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 111]] — Cell-Cell communication; 43 genes; every member is in the + arm (projection on the module's main direction 0.752). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-12.4, 9.8); signed map (-10.1, 34.2). **Vector** length 146, 58.1% of its response variance represented; |z| ≥ 3 in 1,711 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *RHO GTPase Effectors* (reactome, mean cos +0.52 to 10); *RHO GTPases activate PAKs* (reactome, mean cos +0.50 to 4); *RHO GTPases activate IQGAPs* (reactome, mean cos +0.55 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.0 | +3.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.4 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.6 | +13.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.3 | +11.9 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +5.5 | +4.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +4.5 | +3.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.2 | +3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.6 | +3.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.4 | +2.0 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -9.3 | -6.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -8.3 | -6.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -8.0 | -4.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.7 | -9.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | -6.1 | -6.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.0 | -2.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -4.0 | -3.2 |
|  | [[Amsacrine (drug)]] 5 µM |  | -4.0 | -4.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -3.2 | -3.3 |
|  | [[Resveratrol (drug)]] 5 µM |  | -3.1 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | annexin A2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q22.2 — chr15:60,347,134-60,402,883 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LIP2; previously ANX2, ANX2L4, CAL1H, LPC2D |
| Gene groups (HGNC) | Annexins |
| Hallmark sets | UV_RESPONSE_DN, HYPOXIA |
| Reactome | 15 pathways, smallest: Dissolution of Fibrin Clot; Turbulent (oscillatory, disturbed) flow shear stress activates signaling by PIEZO1 and integrins in endothelial cells; Gene and protein expression by JAK-STAT signaling after Interleukin-12 stimulation |
| Matched by | ensembl_id |

**Function**, from UniProt [P07355](https://www.uniprot.org/uniprotkb/P07355) (Annexin A2):

> Calcium-regulated membrane-binding protein whose affinity for calcium is greatly enhanced by anionic phospholipids. It binds two calcium ions with high affinity. May be involved in heat-stress response. Inhibits PCSK9-enhanced LDLR degradation, probably reduces PCSK9 protein levels via a translational mechanism but also competes with LDLR for binding with PCSK9. Binds to endosomes damaged by phagocytosis of particulate wear debris and participates in endosomal membrane stabilization, thereby …

**Summary**, from NCBI Gene [302](https://www.ncbi.nlm.nih.gov/gene/302):

> This gene encodes a member of the annexin family. Members of this calcium-dependent phospholipid-binding protein family play a role in the regulation of cellular growth and in signal transduction pathways. This protein functions as an autocrine factor which heightens osteoclast formation and bone resorption. This gene has three pseudogenes located on chromosomes 4, 9 and 10, respectively. Multiple alternatively spliced transcript variants encoding different isoforms have been found for this …

**Accessions** — [HGNC:537](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:537) · Entrez [302](https://www.ncbi.nlm.nih.gov/gene/302) · UniProt [P07355](https://www.uniprot.org/uniprotkb/P07355) · Ensembl [ENSG00000182718](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182718)

## Data

Gene col 11318: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11318); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11318, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11318]; `tensor/DDL_lfc|DDL_z.npy` [11318]; `embed/gene_vectors.npy` [11318]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11318 or target_col == 11318). Every well: [[ANXA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANXA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
