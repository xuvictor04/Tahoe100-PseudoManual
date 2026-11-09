---
symbol: "RBM5"
type: "gene"
col: 37
ensembl_id: "ENSG00000003756"
name: "RNA binding motif protein 5"
location: "3p21.31"
module: 51
arm: "+"
pooled_cpm: 161.51
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 12
n_dd_up_clean: 12
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# RBM5

*RNA binding motif protein 5* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.67× (z +32.4, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.392× (z -21.9, q 0e+00, down in 48 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.476× (z -17.3, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GTF2IRD2B]] (+0.77, fdr 7e-06), [[EPC1]] (+0.72, fdr 7e-06), [[RFX1]] (+0.71, fdr 7e-06); moves opposite to [[CORO1C]] (-0.62, fdr 2e-05), [[ITGB1]] (-0.61, fdr 3e-05), [[USB1]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠; shown: the 15 strongest. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 37.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.67×** | +32.4 | 0e+00 | 48/48 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.88×** | +24.7 | 0e+00 | 48/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.28×** | +19.3 | 0e+00 | 47/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.13×** | +17.0 | 0e+00 | 47/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.06×** | +16.9 | 0e+00 | 47/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.85×** | +14.4 | 6e-45 | 45/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.71×** | +12.6 | 2e-34 | 40/48 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.36×** | +10.5 | 9e-24 | 41/48 (SW480, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.24×** | +9.8 | 5e-21 | 41/49 (SW480, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.37×** | +7.4 | 1e-11 | 32/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.29×** | +5.9 | 2e-07 | 30/48 (SNU-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.25×** | +5.2 | 1e-05 | 23/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.20×** | +4.3 | 6e-04 | 24/48 (LoVo, A498, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~5% of this change | 1.19× | +4.1 | 0.002 | 23/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 1.16× | +3.5 | 0.020 | 15/48 (NCI-H2030, A-427, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 37.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.392×** | -21.9 | 0e+00 | 48/49 (NCI-H2347, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.401×** | -20.5 | 0e+00 | 42/44 (SK-MEL-2, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.476×** | -17.3 | 0e+00 | 47/48 (RPMI-7951, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.484×** | -16.9 | 0e+00 | 48/48 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.496×** | -16.4 | 0e+00 | 48/48 (CFPAC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.531×** | -14.8 | 0e+00 | 48/48 (SNU-423, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.578×** | -11.8 | 2e-30 | 36/45 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.715×** | -11.1 | 1e-26 | 42/48 (SW480, SNU-423, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.682×** | -8.9 | 3e-17 | 43/48 (RPMI-7951, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.695×** | -8.5 | 1e-15 | 41/49 (SK-MEL-2, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.776×** | -8.4 | 3e-15 | 30/49 (RPMI-7951, LOX-IMVI, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.531×** | -7.7 | 6e-13 | 43/49 (SW480, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 0.846× | -3.9 | 0.004 | 21/48 (SNU-423, SW 1088, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.859× | -3.5 | 0.016 | 19/48 (SW1417, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.901× | -3.4 | 0.023 | 2/48 (Hs 766T, SW 1088) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.911× | -3.1 | 0.078 | 7/48 (A-172, RPMI-7951, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 37. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 214 | 11 (2 ⚠) | 9 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +28.6) | [[Dinaciclib (drug)]] 5 µM 0.261× (z -23.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.05 µM 0.495× (z -12.7) |
| [[NCI-H460 (line)]] | wt | 129 | 12 (2 ⚠) | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +32.5) | [[Panobinostat (drug)]] 5 µM 0.420× (z -14.9) |
| [[LOX-IMVI (line)]] | wt | 182 | 7 (1 ⚠) | 9 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +21.8) | [[Dinaciclib (drug)]] 5 µM 0.269× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.359× (z -13.9) |
| [[RPMI-7951 (line)]] | alt | 238 | 8 (1 ⚠) | 8 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +18.3) | [[Dinaciclib (drug)]] 0.5 µM 0.286× (z -20.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.361× (z -16.4) |
| [[NCI-H1573 (line)]] | alt | 121 | 9 (1 ⚠) | 5 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.34× (z +20.5) | [[Panobinostat (drug)]] 5 µM 0.355× (z -12.6) |
| [[SNU-423 (line)]] | alt | 184 | 5 (1 ⚠) | 9 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +17.2) | [[Dinaciclib (drug)]] 0.5 µM 0.197× (z -23.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.373× (z -14.2) |
| [[SW1417 (line)]] | alt | 247 | 6 (1 ⚠) | 8 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +25.0) | [[Dinaciclib (drug)]] 5 µM 0.242× (z -21.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.469× (z -12.1) |
| [[A549 (line)]] | wt | 123 | 8 (1 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.72× (z +30.2) | [[Panobinostat (drug)]] 0.5 µM 0.468× (z -10.4) |
| [[HS-578T (line)]] | alt | 152 | 6 (1 ⚠) | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +23.2) | [[Panobinostat (drug)]] 5 µM 0.405× (z -12.8) |
| [[HOP62 (line)]] | alt | 196 | 5 (1 ⚠) | 7 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.86× (z +14.3) | [[Dinaciclib (drug)]] 0.5 µM 0.260× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.301× (z -16.3) |
| [[hTERT-HPNE (line)]] | wt | 177 | 5 (1 ⚠) | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +14.9) | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.383× (z -12.1) |
| [[J82 (line)]] | alt | 164 | 4 (1 ⚠) | 8 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +15.4) | [[Dinaciclib (drug)]] 5 µM 0.169× (z -26.2) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.505× (z -10.5) |
| [[NCI-H1792 (line)]] | alt | 156 | 6 (1 ⚠) | 6 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.15× (z +19.7) | [[Dinaciclib (drug)]] 0.5 µM 0.353× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.443× (z -11.2) |
| [[PANC-1 (line)]] | alt | 111 | 7 (1 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +30.2) | [[Dinaciclib (drug)]] 0.5 µM 0.463× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.484× (z -11.7) |
| [[SW 900 (line)]] | alt | 154 | 5 (1 ⚠) | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +16.9) | [[Dinaciclib (drug)]] 5 µM 0.337× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.380× (z -13.2) |
| [[HEC-1-A (line)]] | alt | 270 | 8 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +29.2) | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -22.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 122 | 8 (1 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.74× (z +22.2) | [[Belinostat (drug)]] 5 µM 0.426× (z -12.2) |
| [[LoVo (line)]] | wt | 126 | 9 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.11× (z +26.3) | [[Dinaciclib (drug)]] 0.5 µM 0.392× (z -13.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 181 | 4 (1 ⚠) | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +22.4) | [[Dinaciclib (drug)]] 0.5 µM 0.254× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.408× (z -13.2) |
| [[A-172 (line)]] | wt | 147 | 2 | 8 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +19.8) | [[Panobinostat (drug)]] 5 µM 0.406× (z -13.7) |
| [[AsPC-1 (line)]] | alt | 146 | 5 (1 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +24.7) | [[Belinostat (drug)]] 5 µM 0.403× (z -12.1) |
| [[COLO 205 (line)]] | alt | 124 | 6 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +23.1) | [[Belinostat (drug)]] 5 µM 0.453× (z -9.8) |
| [[NCI-H2347 (line)]] | alt | 304 | 3 (1 ⚠) | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +18.3) | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -24.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.369× (z -16.0) |
| [[RKO (line)]] | wt | 165 | 9 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.89× (z +31.3) | [[Dinaciclib (drug)]] 0.5 µM 0.300× (z -13.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 129 | 7 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +23.4) | [[Panobinostat (drug)]] 0.5 µM 0.483× (z -9.4) |
| [[CFPAC-1 (line)]] | alt | 117 | 3 (1 ⚠) | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +15.6) | [[Panobinostat (drug)]] 0.5 µM 0.352× (z -15.7) |
| [[MIA PaCa-2 (line)]] | alt | 114 | 6 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +15.6) | [[Dinaciclib (drug)]] 0.5 µM 0.415× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.469× (z -9.6) |
| [[SK-MEL-2 (line)]] | alt | 191 | 2 | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +17.0) | [[Dinaciclib (drug)]] 5 µM 0.0615× (z -37.2) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.491× (z -9.8) |
| [[C32 (line)]] | wt | 175 | 2 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +15.4) | [[Panobinostat (drug)]] 5 µM 0.378× (z -11.9) |
| [[HepG2_C3A (line)]] | wt | 150 | 5 (1 ⚠) | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.66× (z +15.3) | [[Dinaciclib (drug)]] 5 µM 0.354× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.435× (z -9.8) |
| [[HT-29 (line)]] | alt | 107 | 4 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +20.1) | [[Panobinostat (drug)]] 5 µM 0.430× (z -10.8) |
| [[NCI-H23 (line)]] | alt | 135 | 6 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +17.9) | [[Dinaciclib (drug)]] 5 µM 0.307× (z -15.0) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 158 | 5 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.90× (z +13.8) | [[Dinaciclib (drug)]] 5 µM 0.275× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 0.630× (z -8.5) |
| [[A498 (line)]] | wt | 81.8 | 4 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +29.8) | [[Panobinostat (drug)]] 5 µM 0.487× (z -10.2) |
| [[SNU-1 (line)]] | wt | 209 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +17.6) | [[Dinaciclib (drug)]] 0.5 µM 0.374× (z -11.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 110 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +22.2) | [[Dinaciclib (drug)]] 5 µM 0.252× (z -16.4) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 161 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +14.5) | [[Dinaciclib (drug)]] 0.5 µM 0.408× (z -10.8) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 134 | 3 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.01× (z +14.3) | [[Dinaciclib (drug)]] 0.5 µM 0.383× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.05 µM 0.508× (z -8.9) |
| [[LS 180 (line)]] | wt | 183 | 4 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +16.5) | [[Dinaciclib (drug)]] 5 µM 0.247× (z -14.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 160 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +19.1) | [[Dinaciclib (drug)]] 5 µM 0.327× (z -11.9) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 200 | 4 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +18.6) | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -15.8) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 207 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +11.0) | [[Dinaciclib (drug)]] 0.05 µM 0.139× (z -15.3) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 111 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +12.5) | [[Panobinostat (drug)]] 0.5 µM 0.360× (z -9.7) |
| [[HCT15 (line)]] | alt | 246 | 1 | 4 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.67× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.189× (z -18.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.447× (z -9.3) |
| [[AN3 CA (line)]] | alt | 246 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.356× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 168 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.249× (z -9.1) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 201 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.151× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H2122 (line)]] | alt | 215 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 182 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 146 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 37), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2IRD2B]] | +0.77 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[EPC1]] | +0.72 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[RFX1]] | +0.71 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[ZCCHC10]] | +0.71 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[UNK]] | +0.70 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[SETDB1]] | +0.69 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[PI4KB]] | +0.68 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[RNF115]] | +0.68 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[PPP4R3A]] | +0.68 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[MAU2]] | +0.67 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[NFYC]] | +0.67 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[CREBBP]] | +0.66 | +0.53 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CORO1C]] | -0.62 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[ITGB1]] | -0.61 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[USB1]] | -0.60 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[BLTP2]] | -0.59 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[ATP13A2]] | -0.58 | -0.50 / -0.37 | both halves | 8e-05 |  |
| [[METAP1]] | -0.58 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[TMED7]] | -0.57 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[BCAP31]] | -0.56 | -0.41 / -0.47 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises RBM5's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises RBM5's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.681). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-42.0, 18.9); signed map (-3.2, -9.3). **Vector** length 103, 39.2% of its response variance represented; |z| ≥ 3 in 1,465 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.4 | +32.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +6.7 | +2.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.4 | +17.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.1 | +12.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.9 | +2.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +4.8 | -0.2 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +4.6 | +0.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.8 | -2.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.1 | +0.2 |
| fall | [[Panobinostat (drug)]] 0.05 µM |  | -7.3 | -14.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -6.9 | -8.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.1 | -11.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.8 | -8.5 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -4.7 | -0.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -4.5 | -2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.3 | +0.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.2 | -7.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.5 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | RNA binding motif protein 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:50,088,919-50,119,021 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LUCA15, LUCA-15, H37 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; Zinc fingers RANBP2-type; G-patch domain containing; RNA binding motif containing; Spliceosomal A complex |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 9 pathways, smallest: mRNA Polyadenylation; mRNA 3'-end processing; mRNA Splicing - Major Pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [P52756](https://www.uniprot.org/uniprotkb/P52756) (RNA-binding protein 5):

> Component of the spliceosome A complex. Binds to ssRNA containing the consensus sequence 5'-AGGUAA-3'. Regulates alternative splicing of a number of mRNAs. May modulate splice site pairing after recruitment of the U1 and U2 snRNPs to the 5' and 3' splice sites of the intron. May both positively and negatively regulate apoptosis by regulating the alternative splicing of several genes involved in this process, including FAS and CASP2/caspase-2. In the case of FAS, promotes exclusion of exon 6 …

**Summary**, from NCBI Gene [10181](https://www.ncbi.nlm.nih.gov/gene/10181):

> This gene is a candidate tumor suppressor gene which encodes a nuclear RNA binding protein that is a component of the spliceosome A complex. The encoded protein plays a role in the induction of cell cycle arrest and apoptosis through pre-mRNA splicing of multiple target genes including the tumor suppressor protein p53. This gene is located within the tumor suppressor region 3p21.3, and may play a role in the inhibition of tumor transformation and progression of several malignancies including …

**Accessions** — [HGNC:9902](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9902) · Entrez [10181](https://www.ncbi.nlm.nih.gov/gene/10181) · UniProt [P52756](https://www.uniprot.org/uniprotkb/P52756) · Ensembl [ENSG00000003756](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000003756)

## Data

Gene col 37: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 37); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 37, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 37]; `tensor/DDL_lfc|DDL_z.npy` [37]; `embed/gene_vectors.npy` [37]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 37 or target_col == 37). Every well: [[RBM5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBM5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
