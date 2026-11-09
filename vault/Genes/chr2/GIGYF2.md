---
symbol: "GIGYF2"
type: "gene"
col: 12814
ensembl_id: "ENSG00000204120"
name: "GRB10 interacting GYF protein 2"
location: "2q37.1"
module: 28
arm: "+"
pooled_cpm: 241.8
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 5
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# GIGYF2

*GRB10 interacting GYF protein 2* — 2q37.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.57× (z +20.2, q 0e+00, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.466× (z -23.1, q 0e+00, down in 41 of 44 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (RKO 0.209×, SW 1271 0.0382×, A-427 0.246×, NCI-H23 0.316×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (C-33 A 0.151×, NCI-H23 0.240×, SW480 0.348×, A498 0.324×, …; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.183×; ⚠ toxic).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF638]] (+0.64, fdr 1e-05), [[TRIP11]] (+0.63, fdr 7e-06), [[CEP350]] (+0.63, fdr 1e-05); moves opposite to [[YWHAQ]] (-0.59, fdr 2e-05), [[CD276]] (-0.49, fdr 3e-05), [[HDAC1]] (-0.49, fdr 3e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12814.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.57×** | +20.2 | 0e+00 | 42/48 (NCI-H460, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.54×** | +13.5 | 3e-39 | 36/48 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.43×** | +11.3 | 2e-27 | 34/48 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.34×** | +9.0 | 3e-17 | 37/48 (NCI-H460, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.29×** | +7.7 | 2e-12 | 29/48 (COLO 205, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.25×** | +6.9 | 4e-10 | 27/48 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.22×** | +6.2 | 4e-08 | 26/48 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.21×** | +6.0 | 2e-07 | 25/48 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.40×** | +5.6 | 2e-06 | 28/48 (RKO, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.38×** | +5.3 | 8e-06 | 28/49 (MIA PaCa-2, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +5.2 | 1e-05 | 19/47 (LoVo, BT-474, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.11× | +3.2 | 0.070 | 10/48 (LoVo, NCI-H1573, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 12 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12814.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (RKO 0.209×, SW 1271 0.0382×, A-427 0.246×, NCI-H23 0.316×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (C-33 A 0.151×, NCI-H23 0.240×, SW480 0.348×, A498 0.324×, …; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.183×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.466×** | -23.1 | 0e+00 | 41/44 (C-33 A, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.487×** | -22.6 | 0e+00 | 46/49 (RKO, SW 1271, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.582×** | -15.6 | 0e+00 | 42/45 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.738×** | -9.2 | 5e-18 | 34/47 (RKO, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.901× | -4.7 | 3e-04 | 9/48 (RKO, HEC-1-A, …) | top dose only | low cells (technical?) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.870× | -4.4 | 1e-03 | 9/49 (CHP-212, SNU-423, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 0.870× | -4.4 | 1e-03 | 18/48 (AN3 CA, SW48, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 0.909× | -4.2 | 0.002 | 14/49 (A549, A498, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 0.882× | -3.9 | 0.005 | 16/48 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.893× | -3.6 | 0.020 | 9/48 (A498, Panc 03.27, …) | inconsistent across doses |  |
| [[Vilanterol (drug)]] 0.5 µM |  | 0.893× | -3.5 | 0.023 | 6/48 (A498, A-172, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.900× | -3.3 | 0.040 | 9/48 (HOP62, LS 180, …) | rises with dose |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.898× | -3.3 | 0.040 | 8/48 (CHP-212, NCI-H661, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~18% of this change | 0.900× | -3.2 | 0.054 | 17/47 (HCT15, SW48, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.871× | -3.1 | 0.072 | 12/48 (HCT15, BT-474, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.875× | -3.0 | 0.083 | 19/47 (A-427, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12814. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 336 | 9 (1 ⚠) | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +15.0) | [[Dinaciclib (drug)]] 5 µM 0.370× (z -18.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 309 | 7 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +18.1) | [[Dinaciclib (drug)]] 5 µM 0.444× (z -13.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 354 | 6 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +24.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.183× (z -30.3) ⚠ toxic |
| [[A549 (line)]] | wt | 265 | 3 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +15.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.534× (z -15.6) ⚠ cell-cycle shift, explains ~12% of this change |
| [[Hs 766T (line)]] | wt | 205 | 4 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +13.6) | [[Dinaciclib (drug)]] 0.5 µM 0.478× (z -11.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 259 | 4 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.32× (z +17.1) | [[Dinaciclib (drug)]] 5 µM 0.487× (z -14.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 197 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +23.0) | [[Dinaciclib (drug)]] 5 µM 0.375× (z -15.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 348 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +25.7) | [[Dinaciclib (drug)]] 0.5 µM 0.353× (z -21.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 261 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +19.1) | [[Dinaciclib (drug)]] 0.5 µM 0.373× (z -19.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 262 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +17.6) | [[Dinaciclib (drug)]] 5 µM 0.351× (z -17.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 284 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.324× (z -20.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 248 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +15.3) | — |
| [[HT-29 (line)]] | alt | 229 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +16.8) | [[Dinaciclib (drug)]] 5 µM 0.447× (z -12.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 236 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.498× (z -10.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 283 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.374× (z -14.4) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 232 | 2 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.16× (z +13.1) | [[Dinaciclib (drug)]] 0.5 µM 0.423× (z -14.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 285 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.59× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.240× (z -26.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 265 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.52× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.348× (z -22.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 226 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +11.9) | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -25.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 187 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +16.3) | [[Dinaciclib (drug)]] 0.5 µM 0.605× (z -8.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 212 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +21.1) | — |
| [[HepG2_C3A (line)]] | wt | 252 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.52× (z +8.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.390× (z -13.7) ⚠ toxic |
| [[LS 180 (line)]] | wt | 233 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +13.0) | [[Dinaciclib (drug)]] 0.5 µM 0.521× (z -12.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 187 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +15.8) | [[Dinaciclib (drug)]] 0.5 µM 0.431× (z -14.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 287 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.228× (z -18.3) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 289 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.317× (z -12.7) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 293 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.235× (z -19.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 354 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.93× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.289× (z -18.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 219 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.478× (z -12.8) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 200 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.453× (z -13.1) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 209 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.256× (z -16.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 229 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +12.7) | [[Dinaciclib (drug)]] 0.5 µM 0.395× (z -15.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 177 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.59× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.575× (z -9.4) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 277 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.470× (z -14.5) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 270 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.151× (z -29.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 156 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +10.1) | — |
| [[HEC-1-A (line)]] | alt | 191 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.59× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.494× (z -13.3) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 148 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.576× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 124 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +17.6) | — |
| [[RPMI-7951 (line)]] | alt | 254 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.418× (z -12.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 224 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.412× (z -14.1) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 239 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.490× (z -10.9) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 281 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.440× (z -8.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 230 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.502× (z -9.1) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 321 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0382× (z -25.0) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 101 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 240 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 251 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 187 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 222 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12814), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF638]] | +0.64 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[TRIP11]] | +0.63 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[CEP350]] | +0.63 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[ZC3H13]] | +0.62 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[SCAF11]] | +0.62 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[TTC17]] | +0.60 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[AK6]] | +0.60 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[CCAR1]] | +0.58 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[ZNF146]] | +0.58 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[COQ9]] | +0.58 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[RSF1]] | +0.57 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[SPG11]] | +0.57 | +0.55 / +0.55 | both halves | 1e-05 | STRING 434 |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YWHAQ]] | -0.59 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[CD276]] | -0.49 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[HDAC1]] | -0.49 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[GNB1]] | -0.49 | -0.58 / -0.38 | both halves | 7e-05 |  |
| [[PTK7]] | -0.48 | -0.46 / -0.36 | both halves | 9e-05 |  |
| [[CAPN1]] | -0.48 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[ATP13A2]] | -0.48 | -0.43 / -0.43 | both halves | 4e-05 | STRING 724 |
| [[LLGL1]] | -0.48 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[MCUB]] | -0.47 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[PLEKHB2]] | -0.47 | -0.49 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.405). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-25.6, 6.8); signed map (5.4, -15.7). **Vector** length 115, 36.9% of its response variance represented; |z| ≥ 3 in 1,191 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.7 | +9.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +5.1 | +11.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.0 | +20.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.0 | +2.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | +1.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.9 | +2.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.9 | +1.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.4 | +1.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.3 | +2.3 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.3 | -15.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.7 | -4.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.2 | -9.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.8 | -23.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | -4.4 | -4.4 |
|  | [[Diphenhydramine (drug)]] 5 µM |  | -2.6 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | -0.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.3 | -1.4 |
|  | [[Clonidine (hydrochloride) (drug)]] 5 µM |  | -2.1 | -0.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.1 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | GRB10 interacting GYF protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.1 — chr2:232,697,299-232,860,605 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0642, GYF2; previously PERQ2, PERQ3, TNRC15, PARK11 |
| Gene groups (HGNC) | GRB10 interacting GYF protein family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6Y7W6](https://www.uniprot.org/uniprotkb/Q6Y7W6) (GRB10-interacting GYF protein 2):

> Key component of the 4EHP-GYF2 complex, a multiprotein complex that acts as a repressor of translation initiation. In the 4EHP-GYF2 complex, acts as a factor that bridges EIF4E2 to ZFP36/TTP, linking translation repression with mRNA decay. Also recruits and bridges the association of the 4EHP complex with the decapping effector protein DDX6, which is required for the ZFP36/TTP-mediated down-regulation of AU-rich mRNA. May act cooperatively with GRB10 to regulate tyrosine kinase receptor …

**Summary**, from NCBI Gene [26058](https://www.ncbi.nlm.nih.gov/gene/26058):

> This gene contains CAG trinucleotide repeats and encodes a protein containing several stretches of polyglutamine residues. The encoded protein may be involved in the regulation of tyrosine kinase receptor signaling. This gene is located in a chromosomal region that was genetically linked to Parkinson disease type 11, and mutations in this gene were thought to be causative for this disease. However, more recent studies in different populations have been unable to replicate this association. …

**Accessions** — [HGNC:11960](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11960) · Entrez [26058](https://www.ncbi.nlm.nih.gov/gene/26058) · UniProt [Q6Y7W6](https://www.uniprot.org/uniprotkb/Q6Y7W6) · Ensembl [ENSG00000204120](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204120)

## Data

Gene col 12814: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12814); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12814, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12814]; `tensor/DDL_lfc|DDL_z.npy` [12814]; `embed/gene_vectors.npy` [12814]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12814 or target_col == 12814). Every well: [[GIGYF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GIGYF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
