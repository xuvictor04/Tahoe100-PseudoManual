---
symbol: "ATP1B3"
type: "gene"
col: 927
ensembl_id: "ENSG00000069849"
name: "ATPase Na+/K+ transporting subunit beta 3"
location: "3q23"
module: 7
arm: "-"
pooled_cpm: 211.73
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 6
n_dd_up_clean: 13
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# ATP1B3

*ATPase Na+/K+ transporting subunit beta 3* — 3q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (12 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 2.67× (z +16.4, q 0e+00, up in 48 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.41× (z +14.7, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.706× (z -5.0, q 4e-04, down in 37 of 50 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Bimiralisib (drug)]] 5 µM: 0.640× (z -3.9, q 0.030, down in 35 of 50 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP1A1]] (+0.53, fdr 2e-05), [[KLHL29]] (+0.52, fdr 3e-05), [[SLC19A2]] (+0.51, fdr 3e-05); moves opposite to [[ZSCAN26]] (-0.61, fdr 1e-05), [[ZNF205]] (-0.59, fdr 3e-05), [[ASB8]] (-0.58, fdr 3e-05).
> It sits in the **-** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 13 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 927.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.67×** | +16.4 | 0e+00 | 48/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.41×** | +14.7 | 0e+00 | 48/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.19×** | +13.1 | 1e-36 | 48/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.04×** | +11.9 | 1e-30 | 48/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **1.73×** | +9.1 | 8e-18 | 43/49 (Hs 766T, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.68×** | +8.3 | 1e-14 | 43/47 (LoVo, NCI-H460, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **1.66×** | +8.1 | 4e-14 | 37/44 (Hs 766T, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.53×** | +7.1 | 1e-10 | 44/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.56×** | +6.8 | 6e-10 | 37/45 (Hs 766T, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.27×** | +5.6 | 1e-06 | 27/49 (A498, SNU-423, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.40×** | +5.4 | 3e-06 | 33/48 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +5.4 | 3e-06 | 38/48 (C32, MIA PaCa-2, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.36×** | +5.1 | 1e-05 | 35/47 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.37×** | +5.0 | 2e-05 | 32/50 (C32, H4, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.34×** | +4.9 | 4e-05 | 32/48 (LoVo, KATO III, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.26×** | +3.7 | 0.008 | 28/49 (HS-578T, MIA PaCa-2, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.48×** | +3.4 | 0.019 | 23/48 (C32, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Sulfatinib (drug)]] 5 µM |  | **1.23×** | +3.3 | 0.025 | 19/49 (Hs 766T, A549, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.46×** | +3.3 | 0.025 | 24/48 (LOX-IMVI, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.45×** | +3.3 | 0.027 | 21/48 (Panc 03.27, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.21×** | +3.2 | 0.034 | 23/48 (HS-578T, AN3 CA, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.30×** | +3.1 | 0.041 | 24/48 (A498, A-427, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.20× | +3.0 | 0.055 | 20/49 (HT-29, NCI-H460, …) | top dose only |  |
| [[Budesonide (drug)]] 0.05 µM |  | 1.20× | +3.0 | 0.055 | 19/48 (HS-578T, H4, …) | inconsistent across doses |  |
| [[Arbutin (drug)]] 5 µM |  | **1.20×** | +3.0 | 0.056 | 17/48 (RPMI-7951, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 927.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.706×** | -5.0 | 4e-04 | 37/50 (SK-MEL-2, HS-578T, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.640×** | -3.9 | 0.030 | 35/50 (HS-578T, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.797×** | -3.8 | 0.032 | 31/47 (A498, HepG2/C3A, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.802×** | -3.7 | 0.035 | 26/48 (LS 180, HS-578T, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.803×** | -3.5 | 0.046 | 25/47 (hTERT-HPNE, NCI-H1792, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.798×** | -3.5 | 0.046 | 27/48 (SK-MEL-2, LoVo, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.861× | -3.4 | 0.046 | 12/48 (HepG2/C3A, SNU-423, …) | all doses, stronger at high dose |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.822× | -3.1 | 0.12 | 24/48 (A549, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 927. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 352 | 14 (7 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 9.77× (z +21.0) | — |
| [[C32 (line)]] | wt | 148 | 8 (6 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.48× (z +11.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.13× (z +10.0) | — |
| [[COLO 205 (line)]] | alt | 98.7 | 7 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.65× (z +13.5) | — |
| [[Hs 766T (line)]] | wt | 218 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.61× (z +10.1) | — |
| [[HS-578T (line)]] | alt | 294 | 6 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 2.60× (z +11.0) | — |
| [[NCI-H1573 (line)]] | alt | 203 | 6 (5 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 4.25× (z +12.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.02× (z +9.9) | — |
| [[SNU-1 (line)]] | wt | 303 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.27× (z +14.2) | — |
| [[AsPC-1 (line)]] | alt | 159 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.62× (z +13.1) | — |
| [[CFPAC-1 (line)]] | alt | 121 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +14.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.68× (z +9.7) | — |
| [[H4 (line)]] | wt | 191 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.47× (z +11.3) | — |
| [[J82 (line)]] | alt | 278 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.89× (z +13.3) | — |
| [[LoVo (line)]] | wt | 187 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.40× (z +16.8) | — |
| [[PANC-1 (line)]] | alt | 230 | 5 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.49× (z +12.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.23× (z +11.2) | — |
| [[SNU-423 (line)]] | alt | 144 | 5 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.71× (z +12.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.21× (z +11.0) | — |
| [[SW480 (line)]] | alt | 219 | 5 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.44× (z +17.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.78× (z +15.2) | — |
| [[C-33 A (line)]] | alt | 255 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.87× (z +10.5) | — |
| [[HT-29 (line)]] | alt | 120 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.54× (z +12.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.05× (z +10.8) | — |
| [[LS 180 (line)]] | wt | 195 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.70× (z +16.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 292 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.39× (z +14.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.18× (z +13.7) | — |
| [[NCI-H1792 (line)]] | alt | 123 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | — |
| [[Panc 03.27 (line)]] | alt | 239 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.76× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.50× (z +10.1) | — |
| [[RPMI-7951 (line)]] | alt | 224 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +10.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.56× (z +9.6) | — |
| [[SW1417 (line)]] | alt | 256 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.15× (z +15.2) | — |
| [[A-427 (line)]] | wt | 300 | 1 (1 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 1.96× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -19.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 133 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.02× (z +11.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.69× (z +10.2) | — |
| [[HCT15 (line)]] | alt | 197 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.77× (z +11.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.29× (z +9.0) | — |
| [[HepG2_C3A (line)]] | wt | 124 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.90× (z +10.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.77× (z +9.5) | — |
| [[HOP62 (line)]] | alt | 195 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.41× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | — |
| [[KATO III (line)]] | alt | 162 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.04× (z +11.7) | — |
| [[LOX-IMVI (line)]] | wt | 218 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.55× (z +10.5) | — |
| [[NCI-H2347 (line)]] | alt | 138 | 3 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.38× (z +9.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.09× (z +8.5) | — |
| [[SK-MEL-2 (line)]] | alt | 302 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.49× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | — |
| [[SW 900 (line)]] | alt | 163 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.10× (z +12.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.38× (z +9.3) | — |
| [[NCI-H23 (line)]] | alt | 396 | 1 (1 ⚠) | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 1.99× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -19.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 251 | 1 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.08× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.589× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 141 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.32× (z +9.5) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.14× (z +8.6) | — |
| [[A-172 (line)]] | wt | 154 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.538× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 122 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.75× (z +8.6) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[AN3 CA (line)]] | alt | 233 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.77× (z +9.1) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 191 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.13× (z +9.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 248 | 1 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.20× (z +10.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW48 (line)]] | wt | 186 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.06× (z +11.3) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 184 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 178 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 401 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 217 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 213 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 204 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 291 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 927), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*10 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP1A1]] | +0.53 | +0.55 / +0.47 | both halves | 2e-05 | same gene group; pathway: Cardiac conduction; STRING 995 |
| [[KLHL29]] | +0.52 | +0.55 / +0.46 | both halves | 3e-05 |  |
| [[SLC19A2]] | +0.51 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[HS2ST1]] | +0.49 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[NETO2]] | +0.48 | +0.40 / +0.44 | both halves | 4e-05 |  |
| [[TMEM164]] | +0.47 | +0.55 / +0.33 | both halves | 1e-04 |  |
| [[BRI3BP]] | +0.47 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[LMBR1]] | +0.47 | +0.52 / +0.46 | both halves | 2e-05 |  |
| [[MEMO1]] | +0.45 | +0.63 / +0.20 | ⚠ one half (not replicated) | 8e-04 |  |
| [[DANCR]] | +0.45 | +0.40 / +0.36 | both halves | 9e-05 |  |

## Genes that move opposite

*90 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZSCAN26]] | -0.61 | -0.62 / -0.49 | both halves | 1e-05 |  |
| [[ZNF205]] | -0.59 | -0.65 / -0.43 | both halves | 3e-05 |  |
| [[ASB8]] | -0.58 | -0.65 / -0.46 | both halves | 3e-05 |  |
| [[CRNKL1]] | -0.56 | -0.63 / -0.42 | both halves | 4e-05 |  |
| [[GCC1]] | -0.55 | -0.57 / -0.40 | both halves | 5e-05 |  |
| [[SRP68]] | -0.54 | -0.63 / -0.45 | both halves | 3e-05 |  |
| [[PSMD4]] | -0.54 | -0.60 / -0.38 | both halves | 6e-05 |  |
| [[CBLL1]] | -0.54 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[SUPT20H]] | -0.53 | -0.61 / -0.29 | both halves | 2e-04 |  |
| [[PRPF6]] | -0.53 | -0.60 / -0.38 | both halves | 6e-05 |  |
| [[ELOF1]] | -0.53 | -0.67 / -0.22 | both halves | 6e-04 |  |
| [[SMARCE1]] | -0.53 | -0.57 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **-** arm (projection on the module's main direction -0.496). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-33.6, -0.1); signed map (-18.9, 44.4). **Vector** length 107, 35.8% of its response variance represented; |z| ≥ 3 in 1,392 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 0.5 µM |  | +6.9 | +11.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +6.8 | +13.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.4 | +2.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +6.3 | +14.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.1 | +16.4 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +2.9 | +3.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.9 | +3.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.8 | +1.2 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +2.5 | +3.0 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -8.1 | -2.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.4 | -0.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.9 | -2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.7 | -1.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -6.5 | +1.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.9 | -1.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.7 | -0.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.4 | -2.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.4 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | ATPase Na+/K+ transporting subunit beta 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q23 — chr3:141,876,124-141,926,549 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ29027, CD298 |
| Gene groups (HGNC) | CD molecules; ATPase Na+/K+ transporting subunits |
| Hallmark sets | ADIPOGENESIS |
| Reactome | 12 pathways, smallest: Basigin interactions; Ion homeostasis; Ion transport by P-type ATPases |
| Matched by | ensembl_id |

**Function**, from UniProt [P54709](https://www.uniprot.org/uniprotkb/P54709) (Sodium/potassium-transporting ATPase subunit beta-3):

> This is the non-catalytic component of the active enzyme, which catalyzes the hydrolysis of ATP coupled with the exchange of Na(+) and K(+) ions across the plasma membrane. The exact function of the beta-3 subunit is not known.

**Summary**, from NCBI Gene [483](https://www.ncbi.nlm.nih.gov/gene/483):

> The protein encoded by this gene belongs to the family of Na+/K+ and H+/K+ ATPases beta chain proteins, and to the subfamily of Na+/K+ -ATPases. Na+/K+ -ATPase is an integral membrane protein responsible for establishing and maintaining the electrochemical gradients of Na and K ions across the plasma membrane. These gradients are essential for osmoregulation, for sodium-coupled transport of a variety of organic and inorganic molecules, and for electrical excitability of nerve and muscle. This …

**Accessions** — [HGNC:806](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:806) · Entrez [483](https://www.ncbi.nlm.nih.gov/gene/483) · UniProt [P54709](https://www.uniprot.org/uniprotkb/P54709) · Ensembl [ENSG00000069849](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000069849)

## Data

Gene col 927: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 927); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 927, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 927]; `tensor/DDL_lfc|DDL_z.npy` [927]; `embed/gene_vectors.npy` [927]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 927 or target_col == 927). Every well: [[ATP1B3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP1B3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
