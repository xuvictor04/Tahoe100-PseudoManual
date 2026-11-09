---
symbol: "DCTN4"
type: "gene"
col: 5390
ensembl_id: "ENSG00000132912"
name: "dynactin subunit 4"
location: "5q33.1"
module: 64
arm: "+"
pooled_cpm: 82.89
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 15
n_dd_up_clean: 11
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# DCTN4

*dynactin subunit 4* — 5q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.72× (z +18.5, q 0e+00, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.446× (z -30.9, q 0e+00, down in 47 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMIM7]] (+0.76, fdr 7e-06), [[NRDE2]] (+0.65, fdr 7e-06), [[PSMC1]] (+0.65, fdr 7e-06); moves opposite to [[TFRC]] (-0.53, fdr 2e-05), [[SLC41A1]] (-0.51, fdr 1e-05), [[KLHL29]] (-0.50, fdr 1e-05).
> It sits in the **+** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5390.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.72×** | +18.5 | 0e+00 | 47/49 (SW480, LoVo, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.87×** | +16.9 | 0e+00 | 46/48 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.91×** | +16.5 | 0e+00 | 46/48 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.06×** | +15.8 | 0e+00 | 45/48 (SW480, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.77×** | +15.3 | 0e+00 | 46/48 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.43×** | +9.6 | 5e-20 | 35/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.35×** | +8.1 | 6e-14 | 32/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.29×** | +6.8 | 6e-10 | 26/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.42×** | +6.7 | 1e-09 | 38/49 (LOX-IMVI, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.27×** | +6.4 | 8e-09 | 28/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.56×** | +6.3 | 2e-08 | 28/45 (LOX-IMVI, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.39×** | +4.6 | 2e-04 | 19/47 (C32, LoVo, …) | top dose only | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.34×** | +4.1 | 0.002 | 18/49 (HEC-1-A, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +4.1 | 0.002 | 15/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 1.15× | +3.8 | 0.006 | 6/48 (Hs 766T, HCT15, …) | all doses, flat |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.09× | +3.3 | 0.026 | 5/48 (NCI-H1792, A549, …) | all doses, flat |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 1.12× | +3.2 | 0.047 | 2/48 (Hs 766T, BT-474) | all doses, stronger at high dose |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | 1.12× | +3.1 | 0.058 | 6/49 (HEC-1-A, HOP62, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5390.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.446×** | -30.9 | 0e+00 | 47/49 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.472×** | -19.5 | 0e+00 | 47/48 (H4, HS-578T, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.503×** | -17.9 | 0e+00 | 46/50 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.590×** | -13.7 | 1e-40 | 35/44 (SNU-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.634×** | -12.3 | 8e-33 | 36/49 (COLO 205, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.660×** | -11.2 | 3e-27 | 43/48 (NCI-H1792, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.696×** | -9.0 | 1e-17 | 34/45 (SW48, A549, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.733×** | -8.4 | 3e-15 | 34/48 (NCI-H460, COLO 205, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.816×** | -7.8 | 4e-13 | 27/48 (HOP62, A-172, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.754×** | -7.6 | 1e-12 | 34/48 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.765×** | -7.3 | 2e-11 | 34/48 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.784×** | -6.3 | 1e-08 | 30/47 (A-172, CFPAC-1, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.798×** | -6.1 | 4e-08 | 27/48 (CHP-212, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.804×** | -5.9 | 1e-07 | 25/48 (CHP-212, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.878× | -5.0 | 2e-05 | 18/48 (MIA PaCa-2, A-172, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.05 µM |  | 0.852× | -4.3 | 5e-04 | 16/48 (SW480, A-172, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.832×** | -3.6 | 0.010 | 15/48 (A-427, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5390. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 94.4 | 10 (3 ⚠) | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.16× (z +19.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.353× (z -24.7) |
| [[SW480 (line)]] | alt | 84.0 | 8 (1 ⚠) | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.36× (z +17.5) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -14.9) |
| [[LS 180 (line)]] | wt | 99.5 | 6 (1 ⚠) | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.65× (z +12.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -18.4) |
| [[HEC-1-A (line)]] | alt | 81.1 | 7 (1 ⚠) | 3 | [[PH-797804 (drug)]] 5 µM 4.96× (z +12.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -15.7) |
| [[HOP62 (line)]] | alt | 80.3 | 5 | 5 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.72× (z +13.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -19.4) |
| [[PANC-1 (line)]] | alt | 87.0 | 6 | 4 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.19× (z +12.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.520× (z -15.2) |
| [[COLO 205 (line)]] | alt | 81.6 | 5 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.33× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.0997× (z -24.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -14.8) |
| [[LoVo (line)]] | wt | 106 | 6 (1 ⚠) | 2 | [[TAK-901 (drug)]] 5 µM 8.21× (z +16.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -20.2) |
| [[A-427 (line)]] | wt | 76.7 | 5 (2 ⚠) | 2 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.52× (z +10.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.27× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.359× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -11.1) |
| [[Panc 03.27 (line)]] | alt | 74.8 | 2 | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.06× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.404× (z -14.4) |
| [[A-172 (line)]] | wt | 93.4 | 1 | 5 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.83× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -18.3) |
| [[A498 (line)]] | wt | 84.7 | 1 | 5 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.78× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -18.3) |
| [[AsPC-1 (line)]] | alt | 74.9 | 3 (1 ⚠) | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.01× (z +13.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -16.6) |
| [[C32 (line)]] | wt | 89.2 | 4 | 2 | [[Ixazomib citrate (drug)]] 0.5 µM 2.60× (z +10.4) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -12.6) |
| [[HS-578T (line)]] | alt | 113 | 2 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.51× (z +9.1) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -19.4) |
| [[HT-29 (line)]] | alt | 69.8 | 3 | 3 | [[Ixazomib citrate (drug)]] 0.5 µM 2.71× (z +12.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -15.3) |
| [[KATO III (line)]] | alt | 57.0 | 5 (2 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 3.28× (z +12.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.11× (z +12.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.547× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 71.5 | 5 | 1 | [[TAK-901 (drug)]] 5 µM 6.04× (z +11.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -12.1) |
| [[LOX-IMVI (line)]] | wt | 69.0 | 4 | 1 | [[Bortezomib (drug)]] 0.05 µM 3.09× (z +12.2) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -11.5) |
| [[SW1417 (line)]] | alt | 84.0 | 4 (1 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 2.34× (z +11.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.17× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -14.3) |
| [[CFPAC-1 (line)]] | alt | 73.9 | 1 | 3 | [[TAK-901 (drug)]] 5 µM 3.83× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -17.4) |
| [[NCI-H1792 (line)]] | alt | 76.5 | 1 | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.03× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -15.8) |
| [[RKO (line)]] | wt | 81.4 | 3 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +13.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.55× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.513× (z -10.1) |
| [[SNU-1 (line)]] | wt | 112 | 2 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.71× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.121× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.394× (z -12.0) |
| [[SNU-423 (line)]] | alt | 83.6 | 1 | 3 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.16× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -16.5) |
| [[AN3 CA (line)]] | alt | 180 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -13.8) |
| [[H4 (line)]] | wt | 99.6 | 0 | 3 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.107× (z -20.2) |
| [[Hs 766T (line)]] | wt | 77.5 | 2 | 1 | [[TAK-901 (drug)]] 5 µM 7.50× (z +12.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -13.7) |
| [[hTERT-HPNE (line)]] | wt | 76.0 | 1 | 2 | [[Bortezomib (drug)]] 0.05 µM 2.46× (z +8.5) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.136× (z -19.3) |
| [[NCI-H2030 (line)]] | alt | 81.7 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.375× (z -15.2) |
| [[NCI-H23 (line)]] | alt | 71.0 | 2 | 1 | [[TAK-901 (drug)]] 5 µM 6.44× (z +11.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.322× (z -18.5) |
| [[NCI-H2347 (line)]] | alt | 81.6 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.539× (z -12.3) |
| [[RPMI-7951 (line)]] | alt | 82.1 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.170× (z -16.2) |
| [[SW 900 (line)]] | alt | 66.1 | 0 | 3 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.185× (z -16.1) |
| [[SW48 (line)]] | wt | 127 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.70× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.249× (z -19.2) |
| [[A549 (line)]] | wt | 66.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.210× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -14.4) |
| [[BT-474 (line)]] | alt | 62.5 | 1 | 1 | [[PH-797804 (drug)]] 5 µM 5.04× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.429× (z -12.3) |
| [[CHP-212 (line)]] | wt | 136 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.241× (z -13.9) |
| [[J82 (line)]] | alt | 66.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.456× (z -12.8) |
| [[MIA PaCa-2 (line)]] | alt | 79.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.546× (z -10.3) |
| [[C-33 A (line)]] | alt | 72.7 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -9.1) |
| [[HCT15 (line)]] | alt | 110 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.489× (z -9.8) |
| [[HepG2_C3A (line)]] | wt | 60.7 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.98× (z +9.4) | — |
| [[NCI-H596 (line)]] | alt | 87.3 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 5 µM 0.227× (z -8.6) |
| [[SHP-77 (line)]] | alt | 83.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -16.5) |
| [[SW 1088 (line)]] | alt | 99.5 | 0 | 1 | — | [[Eplerenone (drug)]] 0.05 µM 0.114× (z -8.8) |
| [[SW 1271 (line)]] | alt | 123 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.126× (z -10.4) |
| [[NCI-H2122 (line)]] | alt | 81.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 71.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 82.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5390), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM7]] | +0.76 | +0.72 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[NRDE2]] | +0.65 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[PSMC1]] | +0.65 | +0.63 / +0.68 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[KIAA1143]] | +0.63 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[CSTPP1]] | +0.62 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[NSFL1C]] | +0.61 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[LINC01278]] | +0.61 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[CUL5]] | +0.60 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[EFCAB7]] | +0.59 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[TXNL1]] | +0.59 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[VPS50]] | +0.59 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[E2F6]] | +0.59 | +0.62 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TFRC]] | -0.53 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[SLC41A1]] | -0.51 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[KLHL29]] | -0.50 | -0.54 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises DCTN4's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.5% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.677). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-23.4, -7.7); signed map (-21.7, -22.7). **Vector** length 110, 33.5% of its response variance represented; |z| ≥ 3 in 1,331 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +11.1 | +16.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +10.7 | +16.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +10.6 | +15.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.3 | +18.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +6.2 | +1.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.7 | +6.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.2 | +15.8 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +3.0 | +0.6 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +2.9 | -0.7 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -7.2 | -19.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -7.1 | -17.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.1 | -30.9 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -4.9 | -2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.6 | -2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -4.0 | -2.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.8 | -2.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.4 | -2.5 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -3.3 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | dynactin subunit 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q33.1 — chr5:150,708,440-150,759,095 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Dyn4, p62 |
| Gene groups (HGNC) | Dynactin subunits |
| Hallmark sets | DNA_REPAIR |
| Reactome | 17 pathways, smallest: COPI-independent Golgi-to-ER retrograde traffic; HSP90 chaperone cycle for steroid hormone receptors (SHR) in the presence of ligand; Processing of antigen in germinal center B cells |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UJW0](https://www.uniprot.org/uniprotkb/Q9UJW0) (Dynactin subunit 4):

> Part of the dynactin complex that activates the molecular motor dynein for ultra-processive transport along microtubules.

**Summary**, from NCBI Gene [51164](https://www.ncbi.nlm.nih.gov/gene/51164):

> Predicted to be involved in microtubule-based process. Located in centrosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:15518](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15518) · Entrez [51164](https://www.ncbi.nlm.nih.gov/gene/51164) · UniProt [Q9UJW0](https://www.uniprot.org/uniprotkb/Q9UJW0) · Ensembl [ENSG00000132912](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132912)

## Data

Gene col 5390: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5390); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5390, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5390]; `tensor/DDL_lfc|DDL_z.npy` [5390]; `embed/gene_vectors.npy` [5390]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5390 or target_col == 5390). Every well: [[DCTN4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DCTN4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
