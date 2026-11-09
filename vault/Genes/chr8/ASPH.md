---
symbol: "ASPH"
type: "gene"
col: 12578
ensembl_id: "ENSG00000198363"
name: "aspartate beta-hydroxylase"
location: "8q12.3"
module: 78
arm: "+"
pooled_cpm: 1183.75
n_lines_expressing: 45
n_dd_up: 5
n_dd_down: 31
n_dd_up_clean: 2
n_dd_down_clean: 29
in_vector_space: true
direction_upstream: 6
direction_downstream: 10
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# ASPH

*aspartate beta-hydroxylase* — 8q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.88× (z +13.1, q 3e-36, up in 41 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.41× (z +7.1, q 1e-10, up in 27 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 8 lines (AsPC-1 3.69×, LoVo 3.07×, LS 180 2.76×, A-172 2.16×, …); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (C-33 A 4.52×, NCI-H1792 3.11×, SNU-1 4.80×, RKO 2.94×, …; ⚠ toxic; transcription drop); [[Ixazomib citrate (drug)]] 0.5 µM in 3 lines (COLO 205 3.40×, HT-29 2.50×, LoVo 1.80×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (COLO 205 3.40×).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.300× (z -35.1, q 0e+00, down in 41 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITGB1]] (+0.66, fdr 7e-06), [[DCBLD2]] (+0.62, fdr 7e-06), [[MSN]] (+0.61, fdr 7e-06); moves opposite to [[PPP4R3A]] (-0.60, fdr 1e-05), [[RAB9A]] (-0.59, fdr 1e-05), [[HEIH]] (-0.57, fdr 1e-05).
> It is in [[Module 078]], a single-armed module (apical junction).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[ITGA2]] → it (grade B ⚠); 10 go from it, the strongest it → [[LSM14B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12578.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 8 lines (AsPC-1 3.69×, LoVo 3.07×, LS 180 2.76×, A-172 2.16×, …); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (C-33 A 4.52×, NCI-H1792 3.11×, SNU-1 4.80×, RKO 2.94×, …; ⚠ toxic; transcription drop); [[Ixazomib citrate (drug)]] 0.5 µM in 3 lines (COLO 205 3.40×, HT-29 2.50×, LoVo 1.80×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (COLO 205 3.40×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.88×** | +13.1 | 3e-36 | 41/44 (C-33 A, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.69×** | +10.5 | 4e-23 | 33/39 (SW48, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.69×** | +10.0 | 2e-21 | 34/40 (C-33 A, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +7.1 | 1e-10 | 27/43 (AsPC-1, LoVo, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.36×** | +6.3 | 3e-08 | 26/43 (COLO 205, HT-29, …) | two highest doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | 1.18× | +3.4 | 0.055 | 17/44 (Panc 03.27, A498, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.17× | +3.3 | 0.079 | 14/43 (NCI-H1792, A549, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 1.17× | +3.3 | 0.079 | 18/43 (NCI-H1792, Panc 03.27, …) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 1.16× | +3.2 | 0.093 | 10/43 (RKO, HepG2/C3A, …) | top dose only |  |
| [[Tirabrutinib (drug)]] 0.5 µM |  | 1.16× | +3.1 | 0.093 | 14/43 (KATO III, SNU-423, …) | inconsistent across doses |  |
| [[Afatinib (drug)]] 0.5 µM |  | 1.13× | +3.1 | 0.11 | 7/44 (C-33 A, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.1 | 0.11 | 15/43 (HT-29, LoVo, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | 1.16× | +3.0 | 0.11 | 12/44 (SW48, RKO, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 55 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12578.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.300×** | -35.1 | 0e+00 | 41/43 (NCI-H1573, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.430×** | -16.7 | 0e+00 | 41/43 (NCI-H1573, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.577×** | -16.0 | 0e+00 | 36/44 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.530×** | -13.1 | 9e-37 | 40/43 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.541×** | -12.6 | 2e-34 | 42/43 (NCI-H1573, H4, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.528×** | -12.6 | 2e-34 | 37/42 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.560×** | -11.9 | 8e-31 | 35/43 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.714×** | -9.8 | 9e-21 | 31/43 (RKO, LoVo, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.623×** | -9.7 | 2e-20 | 38/43 (HEC-1-A, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.681×** | -7.9 | 2e-13 | 33/43 (HEC-1-A, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.714×** | -6.9 | 2e-10 | 36/43 (LoVo, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Amsacrine (drug)]] 5 µM |  | **0.803×** | -6.3 | 1e-08 | 25/43 (HEC-1-A, A549, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.735×** | -6.3 | 1e-08 | 28/43 (C32, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.723×** | -5.7 | 6e-07 | 30/45 (A-427, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.796×** | -5.5 | 1e-06 | 26/43 (AsPC-1, A-427, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.766×** | -5.5 | 2e-06 | 25/43 (LoVo, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12578. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 1,146 | 7 (6 ⚠) | 12 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.69× (z +20.5) | [[Trametinib (drug)]] 5 µM 0.439× (z -12.6) |
| [[NCI-H1573 (line)]] | alt | 2,140 | 1 (1 ⚠) | 18 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.25× (z +11.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.0662× (z -53.2) |
| [[LoVo (line)]] | wt | 678 | 4 (2 ⚠) | 14 (5 ⚠) | [[Auranofin (drug)]] 5 µM 3.07× (z +19.5) | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -23.0) |
| [[BT-474 (line)]] | alt | 979 | 0 | 14 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -24.2) |
| [[C32 (line)]] | wt | 1,840 | 0 | 14 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -39.0) |
| [[H4 (line)]] | wt | 1,723 | 0 | 14 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -32.2) |
| [[HEC-1-A (line)]] | alt | 2,048 | 2 (2 ⚠) | 12 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.97× (z +10.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -21.1) |
| [[HT-29 (line)]] | alt | 742 | 9 (6 ⚠) | 5 | [[Bortezomib (drug)]] 0.05 µM 2.99× (z +16.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.50× (z +14.7) | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -22.3) |
| [[A-427 (line)]] | wt | 811 | 0 | 13 | — | [[Binimetinib (drug)]] 0.5 µM 0.517× (z -13.1) |
| [[HepG2_C3A (line)]] | wt | 1,096 | 0 | 12 | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -26.1) |
| [[A549 (line)]] | wt | 1,098 | 3 (3 ⚠) | 8 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.78× (z +16.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -14.9) |
| [[NCI-H460 (line)]] | wt | 2,104 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -36.6) |
| [[HOP62 (line)]] | alt | 2,248 | 1 (1 ⚠) | 9 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.82× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -37.6) |
| [[COLO 205 (line)]] | alt | 937 | 4 (2 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.40× (z +14.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -13.5) |
| [[J82 (line)]] | alt | 1,033 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -30.5) |
| [[A-172 (line)]] | wt | 681 | 4 (3 ⚠) | 4 | [[Auranofin (drug)]] 5 µM 2.16× (z +10.6) | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -21.7) |
| [[KATO III (line)]] | alt | 811 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -24.0) |
| [[LS 180 (line)]] | wt | 1,074 | 1 | 7 | [[Auranofin (drug)]] 5 µM 2.76× (z +13.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.490× (z -13.4) |
| [[NCI-H1792 (line)]] | alt | 751 | 3 (3 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +17.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -26.1) |
| [[NCI-H2347 (line)]] | alt | 1,542 | 2 (2 ⚠) | 6 | [[Dinaciclib (drug)]] 0.5 µM 1.89× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -29.9) |
| [[PANC-1 (line)]] | alt | 866 | 1 (1 ⚠) | 7 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.83× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -30.2) |
| [[SK-MEL-2 (line)]] | alt | 697 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -35.0) |
| [[SW480 (line)]] | alt | 799 | 0 | 8 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -14.9) |
| [[LOX-IMVI (line)]] | wt | 1,577 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -25.6) |
| [[SHP-77 (line)]] | alt | 484 | 6 (3 ⚠) | 1 | [[Vinblastine (sulfate) (drug)]] 5 µM 1.73× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.542× (z -11.5) |
| [[SNU-1 (line)]] | wt | 392 | 3 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 4.80× (z +17.1) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 5 µM 0.315× (z -12.0) |
| [[A498 (line)]] | wt | 2,958 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.46× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -18.4) |
| [[HCT15 (line)]] | alt | 830 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -25.7) |
| [[Panc 03.27 (line)]] | alt | 686 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -17.9) |
| [[SW 900 (line)]] | alt | 1,648 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -27.9) |
| [[C-33 A (line)]] | alt | 410 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.52× (z +18.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -13.3) |
| [[CFPAC-1 (line)]] | alt | 1,960 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.62× (z +11.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -19.6) |
| [[CHP-212 (line)]] | wt | 481 | 2 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +12.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.99× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -15.4) |
| [[NCI-H2030 (line)]] | alt | 1,228 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 1.85× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -32.2) |
| [[RKO (line)]] | wt | 709 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.94× (z +16.5) ⚠ toxic; transcription drop | [[Selinexor (drug)]] 5 µM 0.469× (z -16.2) |
| [[SW48 (line)]] | wt | 391 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 4.31× (z +18.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.608× (z -9.1) |
| [[hTERT-HPNE (line)]] | wt | 1,432 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -24.6) |
| [[RPMI-7951 (line)]] | alt | 1,109 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -32.9) |
| [[SNU-423 (line)]] | alt | 672 | 2 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.02× (z +9.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.00× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -25.5) |
| [[SW 1088 (line)]] | alt | 794 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.55× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -15.6) |
| [[Hs 766T (line)]] | wt | 886 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.448× (z -9.9) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.474× (z -9.5) |
| [[HS-578T (line)]] | alt | 1,217 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -19.9) |
| [[SW 1271 (line)]] | alt | 606 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -10.4) |
| [[AN3 CA (line)]] | alt | 290 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 215 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1,035 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 213 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1,108 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 148 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 284 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12578), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGB1]] | +0.66 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[DCBLD2]] | +0.62 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[MSN]] | +0.61 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[G6PD]] | +0.60 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[BZW1]] | +0.60 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[CORO1C]] | +0.59 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[PSMD2]] | +0.59 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[SH3KBP1]] | +0.59 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[CAPN2]] | +0.59 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[STIP1]] | +0.58 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[COL13A1]] | +0.57 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[SRPX2]] | +0.57 | +0.46 / +0.52 | both halves | 2e-05 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP4R3A]] | -0.60 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[RAB9A]] | -0.59 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[HEIH]] | -0.57 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[RCHY1]] | -0.57 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[SAT2]] | -0.57 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[ZNF330]] | -0.56 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[TRPM7]] | -0.56 | -0.56 / -0.49 | both halves | 1e-05 | pathway: Ion channel transport |
| [[FBXL3]] | -0.56 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[PSTPIP2]] | -0.55 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[HSD11B2]] | -0.55 | -0.36 / -0.62 | both halves | 1e-04 |  |
| [[FBXO6]] | -0.55 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[EDN2]] | -0.55 | -0.49 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGA2]] | B | ITGA2 activity raises ASPH's level | lines that do not express ITGA2 (11) vs lines expressing it (39) | 2.19× lower at baseline in the lines without ITGA2 | 0.013 | ⚠ within organs, on part of the lines; also absent: GPR39, ATXN1-AS1, MET |
| [[PSD3]] | B | PSD3 activity raises ASPH's level | lines that do not express PSD3 (13) vs lines expressing it (37) | 1.99× lower at baseline in the lines without PSD3 | 0.029 | ⚠ within organs, on part of the lines; also absent: ENSG00000253557, LINC00511, ZFPM2-AS1; maybe low, not absent |
| [[S100A16]] | B | S100A16 activity raises ASPH's level | lines that do not express S100A16 (9) vs lines expressing it (41) | 1.81× lower at baseline in the lines without S100A16 | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, MET, TGFBR2 |
| [[COL13A1]] | B | COL13A1 activity raises ASPH's level | lines that do not express COL13A1 (11) vs lines expressing it (39) | 2.07× lower at baseline in the lines without COL13A1 | 0.066 | ⚠ within organs, on part of the lines; also absent: ERAP2, KIRREL1, TRIM38 |
| [[GSDMD]] | B | GSDMD activity raises ASPH's level | lines that do not express GSDMD (7) vs lines expressing it (43) | 2.45× lower at baseline in the lines without GSDMD | 0.0997 | ⚠ within organs, on part of the lines; co-absent genes; also absent: TGFBR2, VDR, IL1RAP |
| [[PFKP]] | C | PFKP activity raises ASPH's level | lines that do not express PFKP (3) vs lines expressing it (47) | 4.03× lower at baseline in the lines without PFKP | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ASPH, MAP3K5, CFAP45; maybe low, not absent; co-absent with the target; its own permutation p |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LSM14B]] | B | ASPH activity lowers LSM14B's level | lines that do not express ASPH (5) vs lines expressing it (45) | 1.52× higher at baseline in the lines without ASPH | 0.008 | ⚠ within organs, on part of the lines; also absent: HIPK2, EPS8, SCML1; maybe low, not absent |
| [[WDSUB1]] | B | ASPH activity lowers WDSUB1's level | lines that do not express ASPH (5) vs lines expressing it (45) | 1.74× higher at baseline in the lines without ASPH | 0.021 | ⚠ within organs, on part of the lines; also absent: HIPK2, EPS8, SCML1; maybe low, not absent |
| [[DYNLT3]] | B | ASPH activity raises DYNLT3's level | lines that do not express ASPH (5) vs lines expressing it (45) | 2.55× lower at baseline in the lines without ASPH | 0.021 | ⚠ within organs, on part of the lines; also absent: HIPK2, EPS8, SCML1; maybe low, not absent |
| [[ABCB8]] | B | ASPH activity lowers ABCB8's level | lines that do not express ASPH (5) vs lines expressing it (45) | 1.52× higher at baseline in the lines without ASPH | 0.024 | ⚠ within organs, on part of the lines; also absent: HIPK2, EPS8, SCML1; maybe low, not absent |
| [[ITGA2]] | B | ASPH activity raises ITGA2's level | lines that do not express ASPH (5) vs lines expressing it (45) | 4.83× lower at baseline in the lines without ASPH | 0.029 | ⚠ within organs, on part of the lines; also absent: HIPK2, EPS8, SCML1; maybe low, not absent |
| [[ZNF768]] | B | ASPH activity lowers ZNF768's level | lines that do not express ASPH (5) vs lines expressing it (45) | 1.50× higher at baseline in the lines without ASPH | 0.063 | ⚠ within organs, on part of the lines; also absent: HIPK2, EPS8, SCML1; maybe low, not absent |
| cells under [[NVP-BHG712 (drug)]] 5 µM | B | ASPH activity raises the cells' numbers under NVP-BHG712 5 µM (protects the cells) | lines that do not express ASPH (5) vs lines expressing it (43) | the lines without ASPH: 0.74× the cells of the other lines | 0.065 | ⚠ within organs, on part of the lines; also absent: HIPK2, EPS8, SCML1; maybe low, not absent |
| [[GID8]] | B | ASPH activity lowers GID8's level | lines that do not express ASPH (5) vs lines expressing it (45) | 1.42× higher at baseline in the lines without ASPH | 0.072 | ⚠ within organs, on part of the lines; also absent: HIPK2, EPS8, SCML1; maybe low, not absent |
| [[S100A16]] | B | ASPH activity raises S100A16's level | lines that do not express ASPH (5) vs lines expressing it (45) | 2.89× lower at baseline in the lines without ASPH | 0.086 | ⚠ within organs, on part of the lines; also absent: HIPK2, EPS8, SCML1; maybe low, not absent |
| [[SLC6A6]] | B | ASPH activity raises SLC6A6's level | lines that do not express ASPH (5) vs lines expressing it (45) | 2.60× lower at baseline in the lines without ASPH | 0.089 | ⚠ within organs, on part of the lines; also absent: HIPK2, EPS8, SCML1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.654). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.6, 18.2); signed map (-8.0, 37.6). **Vector** length 148, 56.1% of its response variance represented; |z| ≥ 3 in 2,176 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +8.9 | +6.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.9 | +7.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.8 | +3.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +6.0 | -0.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +6.0 | +2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +1.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.6 | +3.3 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +3.5 | +3.4 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -9.6 | -12.6 |
|  | [[Selinexor (drug)]] 5 µM |  | -8.6 | -9.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -7.7 | -5.5 |
|  | [[Trametinib (drug)]] 5 µM |  | -7.1 | -5.7 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -6.5 | -6.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -6.1 | -2.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -5.8 | -3.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -5.7 | -4.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -5.6 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | aspartate beta-hydroxylase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q12.3 — chr8:61,500,556-61,714,640 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CASQ2BP1, BAH, JCTN, HAAH |
| Gene groups (HGNC) | Aspartate beta-hydroxylase domain containing |
| Reactome | 8 pathways, smallest: Protein hydroxylation; Ion homeostasis; Gamma carboxylation, hypusinylation, hydroxylation, and arylsulfatase activation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12797](https://www.uniprot.org/uniprotkb/Q12797) (Aspartyl/asparaginyl beta-hydroxylase):

> [Isoform 1]: Specifically hydroxylates an Asp or Asn residue in certain epidermal growth factor-like (EGF) domains of a number of proteins.; [Isoform 8]: Membrane-bound Ca(2+)-sensing protein, which is a structural component of the ER-plasma membrane junctions. Isoform 8 regulates the activity of Ca(+2) released-activated Ca(+2) (CRAC) channels in T-cells.

**Summary**, from NCBI Gene [444](https://www.ncbi.nlm.nih.gov/gene/444):

> This gene is thought to play an important role in calcium homeostasis. The gene is expressed from two promoters and undergoes extensive alternative splicing. The encoded set of proteins share varying amounts of overlap near their N-termini but have substantial variations in their C-terminal domains resulting in distinct functional properties. The longest isoforms (a and f) include a C-terminal Aspartyl/Asparaginyl beta-hydroxylase domain that hydroxylates aspartic acid or asparagine residues in …

**Accessions** — [HGNC:757](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:757) · Entrez [444](https://www.ncbi.nlm.nih.gov/gene/444) · UniProt [Q12797](https://www.uniprot.org/uniprotkb/Q12797) · Ensembl [ENSG00000198363](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198363)

## Data

Gene col 12578: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12578); `tables/drug_effects.parquet` (68 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12578, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12578]; `tensor/DDL_lfc|DDL_z.npy` [12578]; `embed/gene_vectors.npy` [12578]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12578 or target_col == 12578). Every well: [[ASPH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ASPH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
