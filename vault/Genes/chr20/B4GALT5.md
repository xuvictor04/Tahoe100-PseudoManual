---
symbol: "B4GALT5"
type: "gene"
col: 8166
ensembl_id: "ENSG00000158470"
name: "beta-1,4-galactosyltransferase 5"
location: "20q13.13"
module: 8
arm: "+"
pooled_cpm: 240.1
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 17
n_dd_up_clean: 7
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 20
direction_downstream: 0
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# B4GALT5

*beta-1,4-galactosyltransferase 5* — 20q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.84× (z +15.1, q 0e+00, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.376× (z -17.2, q 0e+00, down in 43 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.643× (z -11.4, q 7e-28, down in 45 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HDHD3]] (+0.56, fdr 1e-05), [[NPEPPSP1]] (+0.54, fdr 2e-05), [[MAP3K8]] (+0.53, fdr 2e-05); moves opposite to [[POLR3D]] (-0.54, fdr 1e-05), [[SRPRA]] (-0.46, fdr 2e-04), [[NEU3]] (-0.46, fdr 4e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 20 arrows point to it, the strongest [[WFDC2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8166.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.84×** | +15.1 | 0e+00 | 47/49 (NCI-H460, J82, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.76×** | +12.7 | 2e-34 | 45/48 (C32, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.76×** | +10.0 | 2e-21 | 43/47 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.53×** | +7.8 | 8e-13 | 34/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +7.1 | 1e-10 | 31/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.46×** | +7.0 | 3e-10 | 30/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.44×** | +6.8 | 1e-09 | 35/48 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.39×** | +5.8 | 5e-07 | 29/48 (NCI-H460, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.5 | 4e-04 | 23/48 (NCI-H460, PANC-1, …) | top dose only | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.26×** | +4.2 | 0.002 | 25/48 (PANC-1, RPMI-7951, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.23×** | +3.7 | 0.010 | 26/47 (LoVo, AsPC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.22×** | +3.7 | 0.010 | 22/47 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.3 | 0.039 | 21/48 (NCI-H1573, HEC-1-A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.19× | +3.2 | 0.058 | 20/48 (NCI-H1573, HCT15, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 1.19× | +3.1 | 0.063 | 18/49 (BT-474, A-427, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8166.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.376×** | -17.2 | 0e+00 | 43/44 (NCI-H2347, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.394×** | -17.0 | 0e+00 | 44/49 (NCI-H23, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.643×** | -11.4 | 7e-28 | 45/49 (Panc 03.27, A549, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.568×** | -9.6 | 2e-19 | 35/45 (NCI-H2347, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.596×** | -9.5 | 4e-19 | 41/48 (A549, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.599×** | -9.4 | 7e-19 | 37/48 (Panc 03.27, A549, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.711×** | -6.2 | 4e-08 | 34/48 (Panc 03.27, HT-29, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.727×** | -5.6 | 2e-06 | 29/50 (Panc 03.27, HT-29, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.763×** | -4.9 | 5e-05 | 30/48 (HT-29, Panc 03.27, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.828×** | -4.9 | 7e-05 | 25/48 (A-172, SW1417, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.840× | -4.5 | 3e-04 | 22/48 (Panc 03.27, A-172, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.809×** | -3.9 | 0.005 | 21/49 (NCI-H2347, BT-474, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.817×** | -3.7 | 0.011 | 25/48 (C32, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **0.824×** | -3.5 | 0.016 | 22/48 (HT-29, H4, …) | inconsistent across doses | low cells (technical?) |
| [[Filgotinib (drug)]] 5 µM |  | **0.828×** | -3.4 | 0.022 | 24/48 (A498, HS-578T, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.765×** | -3.3 | 0.036 | 18/48 (A498, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.726×** | -3.1 | 0.070 | 21/47 (Panc 03.27, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 0.851× | -2.9 | 0.096 | 20/48 (MIA PaCa-2, HT-29, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8166. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 259 | 14 (5 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.69× (z +25.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 5.00× (z +17.9) | [[Dinaciclib (drug)]] 5 µM 0.257× (z -15.1) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 303 | 0 | 16 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -16.2) |
| [[Panc 03.27 (line)]] | alt | 621 | 2 | 12 (8 ⚠) | [[TAK-901 (drug)]] 5 µM 5.08× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.184× (z -25.7) |
| [[J82 (line)]] | alt | 549 | 5 (1 ⚠) | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 7.67× (z +13.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -15.8) |
| [[A549 (line)]] | wt | 222 | 2 (1 ⚠) | 7 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +12.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 2.15× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -18.6) |
| [[NCI-H2347 (line)]] | alt | 406 | 0 | 9 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.152× (z -21.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -17.7) |
| [[A-172 (line)]] | wt | 211 | 0 | 8 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -11.7) |
| [[CFPAC-1 (line)]] | alt | 359 | 0 | 8 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -16.9) |
| [[HT-29 (line)]] | alt | 468 | 0 | 8 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.185× (z -18.1) |
| [[PANC-1 (line)]] | alt | 111 | 6 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +17.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.29× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.444× (z -10.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 468 | 2 | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 6.33× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.198× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.514× (z -9.6) |
| [[C32 (line)]] | wt | 231 | 2 | 5 (4 ⚠) | [[PH-797804 (drug)]] 5 µM 7.38× (z +11.8) | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -19.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.286× (z -14.1) |
| [[HOP62 (line)]] | alt | 133 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +12.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.78× (z +11.4) | — |
| [[LoVo (line)]] | wt | 119 | 5 (2 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 3.08× (z +14.1) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 6.24× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.502× (z -8.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 166 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.370× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.564× (z -9.0) |
| [[BT-474 (line)]] | alt | 226 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 10.6× (z +12.5) | [[Dinaciclib (drug)]] 0.5 µM 0.247× (z -14.1) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 132 | 3 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +12.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.75× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.362× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.521× (z -10.6) |
| [[LS 180 (line)]] | wt | 237 | 2 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.61× (z +11.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -12.6) |
| [[NCI-H2030 (line)]] | alt | 139 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +14.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.45× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.372× (z -10.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 209 | 2 (2 ⚠) | 3 (2 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.77× (z +9.8) ⚠ toxic | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.479× (z -10.4) |
| [[MIA PaCa-2 (line)]] | alt | 216 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.222× (z -15.0) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 78.2 | 4 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.16× (z +11.8) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 6.51× (z +10.1) | — |
| [[RPMI-7951 (line)]] | alt | 137 | 4 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.63× (z +13.7) | — |
| [[SW1417 (line)]] | alt | 504 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.259× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -15.6) |
| [[A-427 (line)]] | wt | 126 | 2 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 5.73× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.347× (z -12.8) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 212 | 1 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 4.27× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.256× (z -15.4) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 568 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -17.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.322× (z -13.6) |
| [[HepG2_C3A (line)]] | wt | 219 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.45× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.280× (z -12.7) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 415 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.206× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -10.6) |
| [[HS-578T (line)]] | alt | 143 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +15.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.46× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.396× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 257 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -13.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 197 | 2 | 1 | [[PH-797804 (drug)]] 5 µM 5.25× (z +10.3) | [[Homoharringtonine (drug)]] 0.5 µM 0.374× (z -11.7) |
| [[SK-MEL-2 (line)]] | alt | 155 | 1 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 4.67× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.314× (z -12.4) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 135 | 3 | 0 | [[TAK-901 (drug)]] 0.05 µM 3.67× (z +9.7) | — |
| [[KATO III (line)]] | alt | 192 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -11.7) |
| [[NCI-H23 (line)]] | alt | 168 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.127× (z -23.2) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 256 | 0 | 2 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.249× (z -8.9) |
| [[SW 900 (line)]] | alt | 281 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.267× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -8.7) |
| [[CHP-212 (line)]] | wt | 162 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -8.9) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 130 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.298× (z -9.1) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 126 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.29× (z +8.9) | — |
| [[hTERT-HPNE (line)]] | wt | 100 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 7.81× (z +8.7) | — |
| [[SHP-77 (line)]] | alt | 117 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.41× (z +8.6) ⚠ toxic | — |
| [[AN3 CA (line)]] | alt | 139 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 142 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 400 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 222 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 181 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 187 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 173 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8166), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HDHD3]] | +0.56 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[NPEPPSP1]] | +0.54 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[MAP3K8]] | +0.53 | +0.47 / +0.49 | both halves | 2e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[GRAMD1A]] | +0.53 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[ELF3]] | +0.53 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[PELI1]] | +0.52 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[CEACAM16-AS1]] | +0.51 | +0.38 / +0.50 | both halves | 7e-05 |  |
| [[C6orf132]] | +0.50 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[AMBRA1]] | +0.50 | +0.52 / +0.46 | both halves | 2e-05 |  |
| [[MVP-DT]] | +0.50 | +0.30 / +0.58 | both halves | 2e-04 |  |
| [[PPA1]] | +0.49 | +0.46 / +0.48 | both halves | 3e-05 |  |
| [[LYN]] | +0.48 | +0.35 / +0.46 | both halves | 1e-04 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR3D]] | -0.54 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[SRPRA]] | -0.46 | -0.30 / -0.47 | both halves | 2e-04 |  |
| [[NEU3]] | -0.46 | -0.50 / -0.42 | both halves | 4e-05 | pathway: Asparagine N-linked glycosylation |
| [[N4BP2]] | -0.45 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[SAFB2]] | -0.45 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[GOLGA3]] | -0.44 | -0.25 / -0.47 | both halves | 4e-04 |  |
| [[SCFD1]] | -0.44 | -0.43 / -0.50 | both halves | 3e-05 | pathway: Asparagine N-linked glycosylation |
| [[GDI2]] | -0.44 | -0.27 / -0.47 | both halves | 3e-04 |  |
| [[ATM]] | -0.44 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[HDLBP]] | -0.44 | -0.26 / -0.43 | both halves | 4e-04 |  |
| [[SURF4]] | -0.43 | -0.21 / -0.49 | both halves | 7e-04 |  |
| [[EOGT]] | -0.43 | -0.38 / -0.43 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 18, C 2. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WFDC2]] | B | WFDC2 activity raises B4GALT5's level | lines that do not express WFDC2 (38) vs lines expressing it (12) | 2.17× lower at baseline in the lines without WFDC2 | 0.001 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1 |
| [[MUC1]] | B | MUC1 activity raises B4GALT5's level | lines that do not express MUC1 (25) vs lines expressing it (25) | 1.73× lower at baseline in the lines without MUC1 | 0.006 | ⚠ within organs, on part of the lines; also absent: TACSTD2, UCA1, RNF223 |
| [[MMP7]] | B | MMP7 activity raises B4GALT5's level | lines that do not express MMP7 (39) vs lines expressing it (11) | 1.86× lower at baseline in the lines without MMP7 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC5B, SFTPA2, GABRP |
| [[WFDC2]] | B | WFDC2 activity strengthens B4GALT5's drug response | lines that do not express WFDC2 (38) vs lines expressing it (11) | the lines without WFDC2 respond 0.87× as strongly (z diff +0.84); strongest at Panobinostat 5 µM: 0.66x vs 0.37x (z diff +4.5) | 0.012 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1; target measured in part of the lines; both ways; artifact flags |
| [[PDZK1IP1]] | B | PDZK1IP1 activity strengthens B4GALT5's drug response | lines that do not express PDZK1IP1 (32) vs lines expressing it (17) | the lines without PDZK1IP1 respond 0.83× as strongly (z diff +1.03); strongest at Idarubicin (hydrochloride) 5 µM: 0.69x vs 0.41x (z diff +3.4) | 0.014 | ⚠ within organs, on part of the lines; also absent: MUC5B, UCA1, PRSS8; target measured in part of the lines; artifact flags |
| [[PDZK1IP1]] | B | PDZK1IP1 activity raises B4GALT5's level | lines that do not express PDZK1IP1 (32) vs lines expressing it (18) | 1.61× lower at baseline in the lines without PDZK1IP1 | 0.018 | ⚠ within organs, on part of the lines; also absent: MUC5B, UCA1, PRSS8 |
| [[TCN1]] | B | TCN1 activity raises B4GALT5's level | lines that do not express TCN1 (37) vs lines expressing it (13) | 1.66× lower at baseline in the lines without TCN1 | 0.023 | ⚠ within organs, on part of the lines; also absent: AGR3, MUC5AC, MUC5B |
| [[LINC01559]] | B | LINC01559 activity raises B4GALT5's level | lines that do not express LINC01559 (38) vs lines expressing it (12) | 1.73× lower at baseline in the lines without LINC01559 | 0.028 | ⚠ within organs, on part of the lines; also absent: CLRN3, NPSR1, CDH17 |
| [[LINC01503]] | B | LINC01503 activity raises B4GALT5's level | lines that do not express LINC01503 (14) vs lines expressing it (36) | 1.44× lower at baseline in the lines without LINC01503 | 0.039 | ⚠ within organs, on part of the lines |
| [[DUOX2]] | B | DUOX2 activity raises B4GALT5's level | lines that do not express DUOX2 (32) vs lines expressing it (18) | 1.51× lower at baseline in the lines without DUOX2 | 0.048 | ⚠ within organs, on part of the lines; also absent: MMP7, SLC44A4, MAOB |
| [[TTC22]] | B | TTC22 activity raises B4GALT5's level | lines that do not express TTC22 (32) vs lines expressing it (18) | 1.66× lower at baseline in the lines without TTC22 | 0.050 | ⚠ within organs, on part of the lines; also absent: COL17A1, TRIM15, SERPINB5 |
| [[ELF3-AS1]] | B | ELF3-AS1 activity raises B4GALT5's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 1.50× lower at baseline in the lines without ELF3-AS1 | 0.059 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.457). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.4, 41.7); signed map (49.8, -0.2). **Vector** length 113, 39.9% of its response variance represented; |z| ≥ 3 in 1,450 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.1 | +1.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +8.1 | +10.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +6.8 | +3.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.7 | +15.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | -9.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | +3.5 | +0.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.2 | +0.2 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +3.1 | +2.1 |
|  | [[Oxaprozin (drug)]] 0.5 µM |  | +3.0 | +1.6 |
| fall | [[Tofacitinib (drug)]] 0.5 µM |  | -4.0 | -2.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.0 | +7.0 |
|  | [[NG25 (drug)]] 5 µM |  | -3.8 | -3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | -6.2 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -3.1 | -1.8 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -2.8 | -0.7 |
|  | [[Cloxacillin (sodium) (drug)]] 0.05 µM |  | -2.7 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | beta-1,4-galactosyltransferase 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.13 — chr20:49,632,945-49,713,878 (-) |
| Ensembl biotype | protein_coding |
| Also known as | beta4GalT-V |
| Gene groups (HGNC) | Beta 4-glycosyltransferases |
| Hallmark sets | TNFA_SIGNALING_VIA_NFKB |
| Reactome | 14 pathways, smallest: N-Glycan antennae elongation; Glycosphingolipid biosynthesis; Keratan sulfate biosynthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [O43286](https://www.uniprot.org/uniprotkb/O43286) (Beta-1,4-galactosyltransferase 5):

> Catalyzes the synthesis of lactosylceramide (LacCer) via the transfer of galactose from UDP-galactose to glucosylceramide (GlcCer). LacCer is the starting point in the biosynthesis of all gangliosides (membrane-bound glycosphingolipids) which play pivotal roles in the CNS including neuronal maturation and axonal and myelin formation (By similarity). Plays a role in the glycosylation of BMPR1A and regulation of its protein stability (By similarity). Essential for extraembryonic development …

**Summary**, from NCBI Gene [9334](https://www.ncbi.nlm.nih.gov/gene/9334):

> This gene is one of seven beta-1,4-galactosyltransferase (beta4GalT) genes. They encode type II membrane-bound glycoproteins that appear to have exclusive specificity for the donor substrate UDP-galactose; all transfer galactose in a beta1,4 linkage to similar acceptor sugars: GlcNAc, Glc, and Xyl. Each beta4GalT has a distinct function in the biosynthesis of different glycoconjugates and saccharide structures. As type II membrane proteins, they have an N-terminal hydrophobic signal sequence …

**Accessions** — [HGNC:928](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:928) · Entrez [9334](https://www.ncbi.nlm.nih.gov/gene/9334) · UniProt [O43286](https://www.uniprot.org/uniprotkb/O43286) · Ensembl [ENSG00000158470](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158470)

## Data

Gene col 8166: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8166); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8166, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8166]; `tensor/DDL_lfc|DDL_z.npy` [8166]; `embed/gene_vectors.npy` [8166]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8166 or target_col == 8166). Every well: [[B4GALT5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/B4GALT5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
