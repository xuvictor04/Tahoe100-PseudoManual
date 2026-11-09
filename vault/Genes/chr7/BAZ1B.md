---
symbol: "BAZ1B"
type: "gene"
col: 195
ensembl_id: "ENSG00000009954"
name: "bromodomain adjacent to zinc finger domain 1B"
location: "7q11.23"
module: 51
arm: "+"
pooled_cpm: 220.21
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 1
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# BAZ1B

*bromodomain adjacent to zinc finger domain 1B* — 7q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.93× (z +19.8, q 0e+00, up in 46 of 48 measured lines) ⚠ cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.08× (z +15.7, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.858× (z -4.6, q 0.002, down in 20 of 48 measured lines) ⚠ cell-cycle shift, would explain all of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (A498 0.522×, AsPC-1 0.628×, HEC-1-A 0.686×, A-172 0.643×; ⚠ cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 2 lines (A-427 0.419×, A498 0.618×; ⚠ cell-cycle shift, would explain all of this change); [[Pentoxifylline (drug)]] 0.05 µM in 1 line (NCI-H596 0.107×; ⚠ transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SETD2]] (+0.71, fdr 7e-06), [[SRSF4]] (+0.68, fdr 1e-05), [[TCHP]] (+0.67, fdr 7e-06); moves opposite to [[ATP6AP2]] (-0.57, fdr 1e-05), [[GM2A]] (-0.56, fdr 1e-05), [[QSOX1]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 15 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 195.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.93×** | +19.8 | 0e+00 | 46/48 (A549, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.19×** | +16.1 | 0e+00 | 48/48 (PANC-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.08×** | +15.7 | 0e+00 | 47/48 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.78×** | +12.3 | 2e-32 | 47/48 (A549, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.61×** | +9.8 | 9e-21 | 45/47 (LoVo, PANC-1, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.50×** | +8.6 | 5e-16 | 42/48 (LoVo, SHP-77, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.46×** | +8.1 | 7e-14 | 45/48 (LoVo, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.44×** | +7.8 | 4e-13 | 42/48 (A549, C32, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.43×** | +7.7 | 1e-12 | 35/48 (SNU-423, C32, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.94×** | +7.4 | 7e-12 | 42/49 (SW480, COLO 205, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | **1.39×** | +7.0 | 1e-10 | 30/49 (NCI-H1792, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.38×** | +6.8 | 4e-10 | 35/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.37×** | +6.7 | 8e-10 | 39/48 (LoVo, PANC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.32×** | +5.9 | 1e-07 | 33/48 (LoVo, PANC-1, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.62×** | +5.4 | 3e-06 | 33/48 (C32, SW1417, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.29×** | +5.4 | 3e-06 | 30/48 (NCI-H460, C32, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.26×** | +4.9 | 4e-05 | 31/48 (NCI-H460, SW48, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **1.39×** | +3.7 | 0.006 | 25/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.16× | +3.1 | 0.041 | 20/47 (NCI-H460, HOP62, …) | all doses, flat |  |
| [[AZD-7648 (drug)]] 0.5 µM |  | **1.22×** | +3.0 | 0.063 | 19/48 (LS 180, PANC-1, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 195.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (A498 0.522×, AsPC-1 0.628×, HEC-1-A 0.686×, A-172 0.643×; ⚠ cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 2 lines (A-427 0.419×, A498 0.618×; ⚠ cell-cycle shift, would explain all of this change); [[Pentoxifylline (drug)]] 0.05 µM in 1 line (NCI-H596 0.107×; ⚠ transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.858× | -4.6 | 0.002 | 20/48 (A-427, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.869× | -4.2 | 0.006 | 19/49 (A498, AsPC-1, …) | top dose only |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.771×** | -4.0 | 0.014 | 23/48 (A-427, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.849× | -3.5 | 0.064 | 23/48 (SW 900, SW48, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.868× | -3.0 | 0.28 | 14/48 (A-427, H4, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 195. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 223 | 9 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +16.9) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.35× (z +12.8) | — |
| [[C32 (line)]] | wt | 232 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +15.4) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 2.32× (z +11.4) | — |
| [[NCI-H1792 (line)]] | alt | 167 | 8 (6 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.63× (z +16.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.12× (z +14.9) | — |
| [[NCI-H460 (line)]] | wt | 200 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +17.2) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.40× (z +14.3) | — |
| [[PANC-1 (line)]] | alt | 233 | 8 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +25.8) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.79× (z +16.8) | — |
| [[SW480 (line)]] | alt | 239 | 7 (4 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.58× (z +15.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.35× (z +14.0) | — |
| [[LS 180 (line)]] | wt | 161 | 6 (3 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.77× (z +13.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.09× (z +10.1) | — |
| [[A498 (line)]] | wt | 424 | 3 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +14.4) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.73× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.522× (z -16.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 158 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +28.5) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.52× (z +18.7) | — |
| [[AsPC-1 (line)]] | alt | 215 | 4 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +13.6) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.97× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.628× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 359 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +19.8) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.34× (z +15.1) | — |
| [[HS-578T (line)]] | alt | 190 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +17.6) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.39× (z +12.9) | — |
| [[KATO III (line)]] | alt | 254 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +13.7) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.53× (z +11.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 306 | 5 (4 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.20× (z +10.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 1.91× (z +9.0) | — |
| [[RPMI-7951 (line)]] | alt | 147 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +12.1) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.36× (z +9.4) | — |
| [[SHP-77 (line)]] | alt | 170 | 5 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.27× (z +11.6) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.05× (z +10.2) | — |
| [[SNU-423 (line)]] | alt | 152 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +16.2) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.76× (z +11.5) | — |
| [[A-427 (line)]] | wt | 220 | 3 (2 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.17× (z +10.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 1.83× (z +8.5) | [[Selinexor (drug)]] 5 µM 0.419× (z -17.4) ⚠ cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 202 | 4 (3 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.79× (z +10.0) ⚠ toxic; cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.42× (z +8.9) | — |
| [[HOP62 (line)]] | alt | 154 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +13.7) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.26× (z +11.6) | — |
| [[NCI-H1573 (line)]] | alt | 137 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +16.5) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.28× (z +11.9) | — |
| [[NCI-H2347 (line)]] | alt | 169 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +21.3) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.60× (z +15.8) | — |
| [[SNU-1 (line)]] | wt | 218 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.99× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.467× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change |
| [[SW 900 (line)]] | alt | 232 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +15.0) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.02× (z +10.6) | [[Panobinostat (drug)]] 5 µM 0.565× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 273 | 2 (1 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 1.94× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.643× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 111 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +17.0) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.90× (z +13.1) | — |
| [[COLO 205 (line)]] | alt | 124 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +11.1) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.32× (z +8.8) | — |
| [[HepG2_C3A (line)]] | wt | 150 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +16.5) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.48× (z +10.1) | — |
| [[HT-29 (line)]] | alt | 209 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +13.7) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.45× (z +12.4) | — |
| [[J82 (line)]] | alt | 288 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +16.7) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.16× (z +12.5) | — |
| [[LOX-IMVI (line)]] | wt | 124 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +11.4) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.19× (z +8.9) | — |
| [[NCI-H2030 (line)]] | alt | 237 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +12.4) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.09× (z +10.9) | — |
| [[Panc 03.27 (line)]] | alt | 188 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +13.2) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.99× (z +9.9) | — |
| [[SW1417 (line)]] | alt | 291 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +15.9) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.93× (z +12.0) | — |
| [[BT-474 (line)]] | alt | 223 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +11.8) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.14× (z +9.9) | — |
| [[C-33 A (line)]] | alt | 301 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.05× (z +9.9) | — |
| [[HCT15 (line)]] | alt | 237 | 2 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.80× (z +10.7) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[RKO (line)]] | wt | 257 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +13.0) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[CHP-212 (line)]] | wt | 200 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +9.9) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[Hs 766T (line)]] | wt | 149 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.06× (z +8.9) | — |
| [[NCI-H23 (line)]] | alt | 185 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 1.93× (z +8.5) | — |
| [[NCI-H596 (line)]] | alt | 180 | 0 | 1 (1 ⚠) | — | [[Pentoxifylline (drug)]] 0.05 µM 0.107× (z -15.6) ⚠ transcription drop |
| [[SK-MEL-2 (line)]] | alt | 203 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +9.1) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[SW48 (line)]] | wt | 340 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.05× (z +9.0) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[AN3 CA (line)]] | alt | 423 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 112 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 334 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 227 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 195), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SETD2]] | +0.71 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[SRSF4]] | +0.68 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[TCHP]] | +0.67 | +0.74 / +0.62 | both halves | 7e-06 |  |
| [[SMC3]] | +0.66 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[JADE1]] | +0.62 | +0.58 / +0.59 | both halves | 7e-06 | same gene group |
| [[SENP1]] | +0.61 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[OBI1]] | +0.61 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[PPIG]] | +0.60 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[UBE3A]] | +0.60 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[CPLANE1]] | +0.60 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[ERCC4]] | +0.60 | +0.65 / +0.56 | both halves | 1e-05 | pathway: DNA Double-Strand Break Repair |
| [[ZFP91]] | +0.59 | +0.73 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP6AP2]] | -0.57 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[GM2A]] | -0.56 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[QSOX1]] | -0.56 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[IDS]] | -0.56 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[TOR1B]] | -0.55 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[MLF2]] | -0.55 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[TMED4]] | -0.54 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[ISCA1]] | -0.54 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[CRELD1]] | -0.54 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[PIGF]] | -0.53 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[GUK1]] | -0.53 | -0.59 / -0.46 | both halves | 2e-05 |  |
| [[BRK1]] | -0.53 | -0.62 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.548). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-23.9, 5.8); signed map (11.4, -33.7). **Vector** length 120, 46.4% of its response variance represented; |z| ≥ 3 in 1,302 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.4 | +15.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +5.8 | +16.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.7 | +12.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.6 | +7.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +5.2 | +19.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.9 | +2.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.9 | +0.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.8 | +4.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.7 | +0.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.8 | -4.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.6 | -4.6 |
|  | [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -3.9 | -4.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.4 | -0.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -2.8 |
|  | [[Decitabine (drug)]] 0.05 µM |  | -2.1 | -1.7 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.0 | -1.8 |
|  | [[Gallic acid (drug)]] 5 µM |  | -1.9 | -1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | -2.9 |
|  | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | -1.9 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | bromodomain adjacent to zinc finger domain 1B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.23 — chr7:73,440,406-73,522,293 (-) |
| Ensembl biotype | protein_coding |
| Also known as | WSTF; previously WBSCR9, WBSCR10 |
| Gene groups (HGNC) | PHD finger proteins; Bromodomain containing; B-WICH chromatin-remodelling complex subunits; WICH complex |
| Reactome | 7 pathways, smallest: B-WICH complex positively regulates rRNA expression; Recruitment and ATM-mediated phosphorylation of repair and signaling proteins at DNA double strand breaks; Positive epigenetic regulation of rRNA expression |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UIG0](https://www.uniprot.org/uniprotkb/Q9UIG0) (Tyrosine-protein kinase BAZ1B):

> Atypical tyrosine-protein kinase that plays a central role in chromatin remodeling and acts as a transcription regulator. Involved in DNA damage response by phosphorylating 'Tyr-142' of histone H2AX (H2AXY142ph). H2AXY142ph plays a central role in DNA repair and acts as a mark that distinguishes between apoptotic and repair responses to genotoxic stress. Regulatory subunit of the ATP-dependent WICH-1 and WICH-5 ISWI chromatin remodeling complexes, which form ordered nucleosome arrays on …

**Summary**, from NCBI Gene [9031](https://www.ncbi.nlm.nih.gov/gene/9031):

> This gene encodes a member of the bromodomain protein family. The bromodomain is a structural motif characteristic of proteins involved in chromatin-dependent regulation of transcription. This gene is deleted in Williams-Beuren syndrome, a developmental disorder caused by deletion of multiple genes at 7q11.23. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:961](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:961) · Entrez [9031](https://www.ncbi.nlm.nih.gov/gene/9031) · UniProt [Q9UIG0](https://www.uniprot.org/uniprotkb/Q9UIG0) · Ensembl [ENSG00000009954](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000009954)

## Data

Gene col 195: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 195); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 195, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 195]; `tensor/DDL_lfc|DDL_z.npy` [195]; `embed/gene_vectors.npy` [195]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 195 or target_col == 195). Every well: [[BAZ1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BAZ1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
