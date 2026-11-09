---
symbol: "UVRAG"
type: "gene"
col: 12582
ensembl_id: "ENSG00000198382"
name: "UV radiation resistance associated"
location: "11q13.5"
module: 14
arm: "+"
pooled_cpm: 150.56
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 7
n_dd_up_clean: 17
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# UVRAG

*UV radiation resistance associated* — 11q13.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.10× (z +45.7, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.530× (z -17.4, q 0e+00, down in 37 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[GSK1059615 (drug)]] 0.5 µM: 0.785× (z -4.9, q 7e-05, down in 22 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (NCI-H23 0.139×, SW 1271 0.0536×, PANC-1 0.396×, SW480 0.416×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (NCI-H23 0.0752×, A-427 0.269×, SW480 0.407×, PANC-1 0.390×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-427 0.261×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (LOX-IMVI 0.588×); [[Tucidinostat (drug)]] 5 µM in 1 line (SW480 0.746×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPPL3]] (+0.63, fdr 2e-05), [[CDC14A]] (+0.62, fdr 7e-06), [[NCOA1]] (+0.60, fdr 1e-05); moves opposite to [[MIER2]] (-0.60, fdr 1e-05), [[YKT6]] (-0.54, fdr 2e-05), [[HIF1AN]] (-0.53, fdr 2e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12582.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.10×** | +45.7 | 0e+00 | 47/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.39×** | +24.9 | 0e+00 | 44/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.37×** | +23.6 | 0e+00 | 46/48 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **4.72×** | +21.9 | 0e+00 | 47/49 (HEC-1-A, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.15×** | +21.8 | 0e+00 | 45/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.78×** | +16.4 | 0e+00 | 44/48 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.74×** | +15.8 | 0e+00 | 41/48 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +12.9 | 5e-36 | 31/49 (NCI-H460, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +12.0 | 3e-31 | 35/47 (PANC-1, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.51×** | +11.7 | 4e-30 | 37/48 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +11.3 | 9e-28 | 38/50 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +11.0 | 2e-26 | 39/48 (A-172, NCI-H460, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.05×** | +10.1 | 2e-22 | 39/48 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.27×** | +9.6 | 4e-20 | 28/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.38×** | +9.1 | 4e-18 | 35/48 (LS 180, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.34×** | +8.4 | 1e-15 | 31/48 (LS 180, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.23×** | +5.9 | 1e-07 | 26/48 (BT-474, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12582.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (NCI-H23 0.139×, SW 1271 0.0536×, PANC-1 0.396×, SW480 0.416×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (NCI-H23 0.0752×, A-427 0.269×, SW480 0.407×, PANC-1 0.390×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-427 0.261×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (LOX-IMVI 0.588×); [[Tucidinostat (drug)]] 5 µM in 1 line (SW480 0.746×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.530×** | -17.4 | 0e+00 | 37/44 (NCI-H23, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.560×** | -16.5 | 0e+00 | 41/49 (NCI-H23, SW 1271, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.663×** | -10.8 | 5e-25 | 32/45 (A-427, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.711×** | -9.3 | 1e-18 | 36/47 (RKO, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.789×** | -6.8 | 1e-09 | 28/48 (SW1417, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.785×** | -4.9 | 7e-05 | 22/48 (RKO, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.894× | -4.5 | 5e-04 | 13/48 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.824×** | -3.9 | 0.006 | 18/48 (COLO 205, LS 180, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.883× | -3.5 | 0.025 | 11/48 (LOX-IMVI, NCI-H1573, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.884× | -3.5 | 0.026 | 12/47 (HT-29, LS 180, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.887× | -3.2 | 0.078 | 12/47 (C32, RKO, …) | inconsistent across doses | low cells (technical?) |
| [[Mifepristone (drug)]] 0.5 µM |  | 0.898× | -3.1 | 0.094 | 9/48 (NCI-H1573, SNU-423, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 0.898× | -3.1 | 0.094 | 22/48 (NCI-H2347, LS 180, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12582. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 230 | 11 (2 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +39.1) | [[Dinaciclib (drug)]] 0.5 µM 0.396× (z -18.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 134 | 11 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 12.0× (z +37.9) | [[Dinaciclib (drug)]] 0.5 µM 0.361× (z -11.0) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 77.5 | 13 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.33× (z +40.5) | — |
| [[A-427 (line)]] | wt | 180 | 10 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +26.9) | [[Dinaciclib (drug)]] 5 µM 0.269× (z -21.0) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 429 | 9 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +19.3) | [[Dinaciclib (drug)]] 5 µM 0.200× (z -14.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 165 | 9 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +22.6) | [[Dinaciclib (drug)]] 5 µM 0.300× (z -12.7) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 106 | 10 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.42× (z +26.8) | — |
| [[J82 (line)]] | alt | 160 | 10 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.81× (z +36.7) | — |
| [[HepG2_C3A (line)]] | wt | 149 | 7 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +24.0) | [[Dinaciclib (drug)]] 0.5 µM 0.225× (z -16.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 157 | 8 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +24.6) | [[Dinaciclib (drug)]] 5 µM 0.416× (z -13.4) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 131 | 6 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.86× (z +36.2) | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -14.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 201 | 6 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.07× (z +25.3) | [[Dinaciclib (drug)]] 0.5 µM 0.300× (z -11.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 175 | 4 (1 ⚠) | 5 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.31× (z +15.2) | [[Dinaciclib (drug)]] 0.5 µM 0.393× (z -17.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 143 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +20.4) | — |
| [[NCI-H23 (line)]] | alt | 180 | 6 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +17.8) | [[Dinaciclib (drug)]] 5 µM 0.0752× (z -37.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 223 | 6 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.21× (z +36.0) | [[Dinaciclib (drug)]] 0.05 µM 0.393× (z -13.3) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 119 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.49× (z +27.3) | — |
| [[H4 (line)]] | wt | 104 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.28× (z +17.9) | — |
| [[HEC-1-A (line)]] | alt | 116 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +27.3) | — |
| [[HOP62 (line)]] | alt | 72.3 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +19.5) | — |
| [[A549 (line)]] | wt | 125 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +26.1) | [[Dinaciclib (drug)]] 5 µM 0.455× (z -10.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 171 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.41× (z +24.5) | [[Dinaciclib (drug)]] 0.5 µM 0.405× (z -9.3) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 151 | 4 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +20.1) | [[Dinaciclib (drug)]] 0.5 µM 0.450× (z -13.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 108 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +13.4) | [[Dinaciclib (drug)]] 0.5 µM 0.378× (z -13.3) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 158 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +19.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.262× (z -17.0) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 80.9 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.03× (z +29.0) | — |
| [[C32 (line)]] | wt | 140 | 3 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +12.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.486× (z -8.9) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 135 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.80× (z +18.5) | — |
| [[LOX-IMVI (line)]] | wt | 145 | 3 (1 ⚠) | 2 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 1.80× (z +9.9) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.81× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.581× (z -9.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.588× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 150 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +25.0) | — |
| [[NCI-H1792 (line)]] | alt | 118 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +15.3) | — |
| [[RPMI-7951 (line)]] | alt | 116 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +18.7) | — |
| [[C-33 A (line)]] | alt | 106 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +10.6) | [[Dinaciclib (drug)]] 0.05 µM 0.242× (z -14.3) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 141 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +18.8) | — |
| [[SW480 (line)]] | alt | 178 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.22× (z +15.2) | [[Dinaciclib (drug)]] 0.5 µM 0.416× (z -18.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 109 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +16.9) | [[Dinaciclib (drug)]] 0.5 µM 0.418× (z -8.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 84.0 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +12.4) | — |
| [[NCI-H2030 (line)]] | alt | 205 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.328× (z -13.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 245 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.426× (z -13.9) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 54.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +15.7) | — |
| [[SW48 (line)]] | wt | 115 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.376× (z -9.9) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 108 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.140× (z -18.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 115 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +13.0) | [[Dinaciclib (drug)]] 0.05 µM 0.285× (z -11.9) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 232 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0536× (z -21.0) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 297 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 123 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 177 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 83.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12582), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPPL3]] | +0.63 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[CDC14A]] | +0.62 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[NCOA1]] | +0.60 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[TRPM7]] | +0.60 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[ARID1B]] | +0.58 | +0.41 / +0.58 | both halves | 4e-05 |  |
| [[CPNE8]] | +0.56 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[FCHSD2]] | +0.56 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[DYRK1A]] | +0.56 | +0.36 / +0.52 | both halves | 9e-05 |  |
| [[GPHN]] | +0.55 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[STAP2]] | +0.55 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[QKI]] | +0.55 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[ARID2]] | +0.55 | +0.37 / +0.47 | both halves | 9e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIER2]] | -0.60 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[YKT6]] | -0.54 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[HIF1AN]] | -0.53 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[AP1M1]] | -0.52 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[SZT2]] | -0.50 | -0.38 / -0.54 | both halves | 7e-05 |  |
| [[HAPSTR1]] | -0.50 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[LINC02693]] | -0.49 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[TPD52L2]] | -0.49 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[LRRC59]] | -0.48 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[TXLNA]] | -0.48 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[GOLGA3]] | -0.48 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[GCN1]] | -0.47 | -0.43 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.436). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-1.1, -26.0); signed map (43.9, -0.3). **Vector** length 114, 39.3% of its response variance represented; |z| ≥ 3 in 1,479 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +11.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | +5.5 | +5.1 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.1 | +9.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.9 | +23.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.7 | +3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.6 | +2.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.6 | +0.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.5 | +0.8 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +3.4 | +2.7 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.2 | -9.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.6 | -17.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.4 | -3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.1 | -4.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.0 | +1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.6 | -1.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -1.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.4 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | UV radiation resistance associated |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.5 — chr11:75,815,210-76,144,232 (+) |
| Ensembl biotype | protein_coding |
| Also known as | VPS38 |
| Gene groups (HGNC) | C2 domain containing; PIK3C3 complex subunits |
| Reactome | 11 pathways, smallest: SARS-CoV-2 modulates autophagy; Translation of Replicase and Assembly of the Replication Transcription Complex_9679504; Translation of Replicase and Assembly of the Replication Transcription Complex_9694676 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P2Y5](https://www.uniprot.org/uniprotkb/Q9P2Y5) (UV radiation resistance-associated gene protein):

> Versatile protein that is involved in regulation of different cellular pathways implicated in membrane trafficking. Involved in regulation of the COPI-dependent retrograde transport from Golgi and the endoplasmic reticulum by associating with the NRZ complex; the function is dependent on its binding to phosphatidylinositol 3-phosphate (PtdIns(3)P). During autophagy acts as a regulatory subunit of the alternative PI3K complex II (PI3KC3-C2) that mediates formation of phosphatidylinositol …

**Summary**, from NCBI Gene [7405](https://www.ncbi.nlm.nih.gov/gene/7405):

> This gene complements the ultraviolet sensitivity of xeroderma pigmentosum group C cells and encodes a protein with a C2 domain. The protein activates the Beclin1-PI(3)KC3 complex, promoting autophagy and suppressing the proliferation and tumorigenicity of human colon cancer cells. Chromosomal aberrations involving this gene are associated with left-right axis malformation and mutations in this gene have been associated with colon cancer. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:12640](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12640) · Entrez [7405](https://www.ncbi.nlm.nih.gov/gene/7405) · UniProt [Q9P2Y5](https://www.uniprot.org/uniprotkb/Q9P2Y5) · Ensembl [ENSG00000198382](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198382)

## Data

Gene col 12582: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12582); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12582, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12582]; `tensor/DDL_lfc|DDL_z.npy` [12582]; `embed/gene_vectors.npy` [12582]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12582 or target_col == 12582). Every well: [[UVRAG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UVRAG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
