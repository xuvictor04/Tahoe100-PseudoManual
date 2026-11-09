---
symbol: "ATP1A1"
type: "gene"
col: 8685
ensembl_id: "ENSG00000163399"
name: "ATPase Na+/K+ transporting subunit alpha 1"
location: "1p13.1"
module: 97
arm: "+"
pooled_cpm: 177.46
n_lines_expressing: 50
n_dd_up: 38
n_dd_down: 9
n_dd_up_clean: 22
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/097"]
generated_by: "tahoemap"
---

# ATP1A1

*ATPase Na+/K+ transporting subunit alpha 1* — 1p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (16 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.59× (z +19.6, q 0e+00, up in 46 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.62× (z +14.0, q 5e-42, up in 38 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.538× (z -12.8, q 1e-34, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CPD]] (+0.70, fdr 7e-06), [[LAMB1]] (+0.67, fdr 7e-06), [[ADAM15]] (+0.66, fdr 9e-06); moves opposite to [[MSANTD3]] (-0.58, fdr 2e-05), [[C15orf48]] (-0.58, fdr 1e-05), [[GORAB]] (-0.57, fdr 2e-05).
> It is in [[Module 097]], a single-armed module (estrogen response early).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 20 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8685.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.59×** | +19.6 | 0e+00 | 46/49 (SW480, A-427, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.60×** | +18.9 | 0e+00 | 43/44 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +14.0 | 5e-42 | 38/49 (LOX-IMVI, J82, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.97×** | +12.9 | 9e-36 | 42/45 (HS-578T, SK-MEL-2, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.83×** | +12.4 | 3e-33 | 46/48 (C32, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.65×** | +10.3 | 6e-23 | 39/48 (C32, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.60×** | +9.7 | 4e-20 | 42/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | **1.56×** | +9.1 | 6e-18 | 32/48 (NCI-H1573, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.61×** | +9.1 | 6e-18 | 29/47 (NCI-H1573, Hs 766T, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.54×** | +8.5 | 9e-16 | 34/49 (NCI-H1573, Hs 766T, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.51×** | +8.5 | 1e-15 | 29/48 (NCI-H1573, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.50×** | +8.3 | 6e-15 | 29/48 (NCI-H1573, Hs 766T, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.49×** | +8.2 | 1e-14 | 32/48 (NCI-H1573, Hs 766T, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | **1.47×** | +8.0 | 7e-14 | 31/48 (NCI-H1573, Hs 766T, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **1.48×** | +7.8 | 3e-13 | 33/47 (NCI-H1792, LoVo, …) | top dose only |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.46×** | +7.8 | 3e-13 | 30/48 (NCI-H1573, Hs 766T, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.44×** | +7.6 | 1e-12 | 28/48 (NCI-H1573, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **1.40×** | +6.9 | 1e-10 | 29/48 (NCI-H1573, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.40×** | +6.9 | 1e-10 | 28/48 (NCI-H1573, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.24×** | +6.3 | 7e-09 | 28/48 (NCI-H1573, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +6.2 | 2e-08 | 28/48 (HOP62, A549, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +5.9 | 1e-07 | 28/48 (SW480, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8685.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.538×** | -12.8 | 1e-34 | 44/48 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.716×** | -9.8 | 5e-20 | 32/48 (HepG2/C3A, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.703×** | -7.3 | 6e-11 | 36/48 (A-172, SW480, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.697×** | -7.2 | 1e-10 | 38/48 (A-172, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.752×** | -5.9 | 5e-07 | 31/48 (A-172, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.748×** | -5.8 | 8e-07 | 37/49 (A498, NCI-H460, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.766×** | -5.5 | 3e-06 | 35/48 (NCI-H1573, SW480, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.761×** | -5.1 | 2e-05 | 28/50 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.678×** | -4.2 | 0.002 | 27/49 (SW480, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 0.838× | -3.5 | 0.022 | 19/47 (SK-MEL-2, HepG2/C3A, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.881× | -3.5 | 0.022 | 16/48 (SK-MEL-2, SW480, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.874× | -3.5 | 0.024 | 14/49 (SW480, C32, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.856× | -3.2 | 0.057 | 18/48 (KATO III, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8685. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 213 | 26 (1 ⚠) | 1 | [[Dexamethasone (drug)]] 5 µM 10.3× (z +25.6) | [[5-Azacytidine (drug)]] 5 µM 0.387× (z -10.4) |
| [[Hs 766T (line)]] | wt | 190 | 22 (2 ⚠) | 3 | [[Dexamethasone (drug)]] 5 µM 5.08× (z +19.6) | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -15.9) |
| [[NCI-H460 (line)]] | wt | 119 | 24 (8 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Dexamethasone (drug)]] 5 µM 2.56× (z +12.7) | — |
| [[A549 (line)]] | wt | 91.4 | 23 (3 ⚠) | 0 | [[Dexamethasone (drug)]] 5 µM 4.02× (z +15.0) | — |
| [[NCI-H2347 (line)]] | alt | 174 | 21 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +12.8) | — |
| [[AsPC-1 (line)]] | alt | 116 | 20 (5 ⚠) | 0 | [[Dexamethasone (drug)]] 5 µM 3.70× (z +15.8) | — |
| [[A498 (line)]] | wt | 212 | 19 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.43× (z +14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Budesonide (drug)]] 0.05 µM 2.06× (z +12.5) | — |
| [[CFPAC-1 (line)]] | alt | 166 | 18 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.83× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Triamcinolone (drug)]] 0.5 µM 2.64× (z +11.1) | — |
| [[HS-578T (line)]] | alt | 207 | 18 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.12× (z +14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Clobetasol propionate (drug)]] 5 µM 2.74× (z +13.3) | — |
| [[H4 (line)]] | wt | 102 | 14 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.42× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Dexamethasone (drug)]] 5 µM 3.11× (z +10.0) | [[Homoharringtonine (drug)]] 0.5 µM 0.379× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 320 | 5 (5 ⚠) | 10 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.97× (z +15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Trametinib (drug)]] 5 µM 0.409× (z -14.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Binimetinib (drug)]] 5 µM 0.415× (z -13.2) |
| [[SW480 (line)]] | alt | 269 | 9 (8 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.95× (z +16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.52× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -22.2) |
| [[Panc 03.27 (line)]] | alt | 218 | 14 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.69× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Betamethasone dipropionate (drug)]] 0.5 µM 2.17× (z +10.1) | — |
| [[PANC-1 (line)]] | alt | 93.6 | 12 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Dexamethasone (drug)]] 5 µM 2.23× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -13.9) |
| [[KATO III (line)]] | alt | 270 | 7 (7 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.00× (z +14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.476× (z -13.5) |
| [[LoVo (line)]] | wt | 170 | 7 (5 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.25× (z +15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +11.8) | [[Harringtonine (drug)]] 5 µM 0.424× (z -10.9) |
| [[NCI-H1792 (line)]] | alt | 105 | 8 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.64× (z +15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.97× (z +9.4) | — |
| [[BT-474 (line)]] | alt | 154 | 6 | 1 | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 3.67× (z +11.6) | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -11.8) |
| [[HT-29 (line)]] | alt | 169 | 7 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.93× (z +14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +11.7) | — |
| [[HCT15 (line)]] | alt | 157 | 5 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.60× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -10.3) |
| [[LS 180 (line)]] | wt | 292 | 5 (5 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.69× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.480× (z -8.8) |
| [[SHP-77 (line)]] | alt | 153 | 5 (5 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.10× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.486× (z -8.7) |
| [[A-172 (line)]] | wt | 130 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -21.9) |
| [[C-33 A (line)]] | alt | 93.7 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.32× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.515× (z -9.4) |
| [[C32 (line)]] | wt | 439 | 5 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.40× (z +15.0) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[HepG2_C3A (line)]] | wt | 439 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -25.4) |
| [[HOP62 (line)]] | alt | 139 | 5 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.18× (z +14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +11.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 104 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.58× (z +16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 0.05 µM 0.453× (z -8.7) |
| [[SW 900 (line)]] | alt | 129 | 5 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.65× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.80× (z +8.9) | — |
| [[HEC-1-A (line)]] | alt | 122 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.54× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.74× (z +11.3) | — |
| [[J82 (line)]] | alt | 172 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +13.4) | — |
| [[LOX-IMVI (line)]] | wt | 177 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +13.4) | — |
| [[RKO (line)]] | wt | 162 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -20.7) |
| [[A-427 (line)]] | wt | 74.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -24.8) |
| [[NCI-H2030 (line)]] | alt | 153 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.41× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.606× (z -9.2) |
| [[RPMI-7951 (line)]] | alt | 126 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.92× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +9.7) | — |
| [[SNU-1 (line)]] | wt | 73.2 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.49× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +8.6) | — |
| [[SNU-423 (line)]] | alt | 128 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.36× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SW48 (line)]] | wt | 166 | 2 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.44× (z +9.5) ⚠ cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.535× (z -9.3) |
| [[COLO 205 (line)]] | alt | 266 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.263× (z -11.7) |
| [[AN3 CA (line)]] | alt | 79.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.04× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[CHP-212 (line)]] | wt | 85.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.94× (z +8.9) | — |
| [[NCI-H23 (line)]] | alt | 149 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.560× (z -9.8) |
| [[SW1417 (line)]] | alt | 420 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.521× (z -9.2) |
| [[hTERT-HPNE (line)]] | wt | 215 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 182 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 91.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 187 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 121 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8685), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPD]] | +0.70 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[LAMB1]] | +0.67 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[ADAM15]] | +0.66 | +0.69 / +0.57 | both halves | 9e-06 |  |
| [[TMEM164]] | +0.65 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[FAH]] | +0.64 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[PACSIN2]] | +0.63 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[SHC1]] | +0.62 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[HIP1R]] | +0.61 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[TBC1D8]] | +0.61 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[ABHD2]] | +0.61 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[SNED1]] | +0.58 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[MMP15]] | +0.58 | +0.53 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSANTD3]] | -0.58 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[C15orf48]] | -0.58 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[GORAB]] | -0.57 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[TIPRL]] | -0.56 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[NEURL3]] | -0.55 | -0.63 / -0.45 | both halves | 3e-05 |  |
| [[ZNF624]] | -0.54 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[OTUD7B]] | -0.54 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[FOXA1]] | -0.54 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[HDAC9]] | -0.54 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[TCEANC]] | -0.54 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[CCDC174]] | -0.53 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[NME6]] | -0.53 | -0.48 / -0.52 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ATP1A1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NR3C1]] | B | NR3C1 activity raises ATP1A1's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 5.9% of all compounds | 0.079 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 097]] — estrogen response early; 48 genes; every member is in the + arm (projection on the module's main direction 0.718). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (32.0, 13.2); signed map (15.5, 34.1). **Vector** length 151, 55.2% of its response variance represented; |z| ≥ 3 in 2,051 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Clobetasol propionate (drug)]] 5 µM |  | +8.5 | +6.9 |
|  | [[Budesonide (drug)]] 5 µM |  | +8.5 | +8.0 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | +8.4 | +9.1 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +8.1 | +9.1 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +8.1 | +7.6 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -14.2 | -12.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -12.9 | -7.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -11.9 | -9.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -10.9 | -5.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -9.5 | -7.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.6 | -5.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.2 | -3.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.9 | -3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.3 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | ATPase Na+/K+ transporting subunit alpha 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.1 — chr1:116,372,668-116,410,261 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | ATPase Na+/K+ transporting subunits |
| Hallmark sets | PROTEIN_SECRETION |
| Reactome | 9 pathways, smallest: Ion homeostasis; Ion transport by P-type ATPases; Potential therapeutics for SARS |
| Matched by | ensembl_id |

**Function**, from UniProt [P05023](https://www.uniprot.org/uniprotkb/P05023) (Sodium/potassium-transporting ATPase subunit alpha-1):

> Catalytic subunit of the Na(+)/K(+)-ATPase pump that hydrolyzes ATP to exchange ions across the plasma membrane, exporting 3 Na(+) and importing 2 K(+) per cycle against electrochemical gradients. It undergoes ATP-driven conformational changes that allow alternating binding and release of Na(+) and K(+) ions across the membrane. This process maintains essential Na(+) and K(+) gradients for membrane potential and cellular function. Could also be part of an osmosensory signaling pathway that …

**Summary**, from NCBI Gene [476](https://www.ncbi.nlm.nih.gov/gene/476):

> The protein encoded by this gene belongs to the family of P-type cation transport ATPases, and to the subfamily of Na+/K+ -ATPases. Na+/K+ -ATPase is an integral membrane protein responsible for establishing and maintaining the electrochemical gradients of Na and K ions across the plasma membrane. These gradients are essential for osmoregulation, for sodium-coupled transport of a variety of organic and inorganic molecules, and for electrical excitability of nerve and muscle. This enzyme is …

**Accessions** — [HGNC:799](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:799) · Entrez [476](https://www.ncbi.nlm.nih.gov/gene/476) · UniProt [P05023](https://www.uniprot.org/uniprotkb/P05023) · Ensembl [ENSG00000163399](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163399)

## Data

Gene col 8685: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8685); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8685, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8685]; `tensor/DDL_lfc|DDL_z.npy` [8685]; `embed/gene_vectors.npy` [8685]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8685 or target_col == 8685). Every well: [[ATP1A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP1A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
