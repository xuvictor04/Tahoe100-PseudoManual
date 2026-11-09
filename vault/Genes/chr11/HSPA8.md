---
symbol: "HSPA8"
type: "gene"
col: 3097
ensembl_id: "ENSG00000109971"
name: "heat shock protein family A (Hsp70) member 8"
location: "11q24.1"
module: 60
arm: "+"
pooled_cpm: 215.63
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 13
n_dd_up_clean: 15
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# HSPA8

*heat shock protein family A (Hsp70) member 8* — 11q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (10 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 11.7× (z +24.7, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.598× (z -7.3, q 1e-10, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AHSA1]] (+0.81, fdr 7e-06), [[CCT3]] (+0.76, fdr 7e-06), [[HSP90AB1]] (+0.76, fdr 7e-06); moves opposite to [[YY1AP1]] (-0.64, fdr 2e-05), [[ABCA5]] (-0.57, fdr 1e-05), [[ETFRF1]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 060]] (heat shock).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3097.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **11.7×** | +24.7 | 0e+00 | 48/48 (HEC-1-A, HS-578T, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **11.1×** | +24.1 | 0e+00 | 48/48 (HT-29, SW480, …) | rises with dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **6.83×** | +19.3 | 0e+00 | 48/48 (C32, HEC-1-A, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **6.18×** | +17.3 | 0e+00 | 48/48 (HT-29, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **10.2×** | +12.2 | 4e-32 | 45/45 (HEC-1-A, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~1% here); noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **4.24×** | +10.3 | 5e-23 | 48/49 (HS-578T, SNU-423, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.86×** | +10.1 | 3e-22 | 44/47 (COLO 205, SHP-77, …) | top dose only | cell-cycle shift (explains ~9% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.05×** | +7.2 | 5e-11 | 46/48 (HT-29, CFPAC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.98×** | +6.9 | 4e-10 | 44/48 (HOP62, SK-MEL-2, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.97×** | +6.8 | 7e-10 | 44/48 (HOP62, SW480, …) | rises with dose | position effect removed |
| [[NG25 (drug)]] 5 µM |  | **3.44×** | +6.5 | 5e-09 | 45/47 (KATO III, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Infigratinib (drug)]] 5 µM |  | **2.83×** | +5.5 | 2e-06 | 47/48 (HEC-1-A, HOP62, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.63×** | +4.9 | 5e-05 | 40/48 (SW480, HOP62, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.37×** | +4.4 | 4e-04 | 28/49 (COLO 205, NCI-H1792, …) | rises with dose | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **2.18×** | +4.1 | 0.002 | 40/48 (MIA PaCa-2, HT-29, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +3.9 | 0.003 | 30/48 (A498, MIA PaCa-2, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.46×** | +3.6 | 0.010 | 32/47 (HT-29, HOP62, …) | rises with dose | position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.43×** | +3.6 | 0.011 | 35/47 (HOP62, HT-29, …) | rises with dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.41×** | +3.4 | 0.018 | 32/48 (CFPAC-1, AN3 CA, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.40×** | +3.3 | 0.022 | 29/48 (SW480, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Mebendazole (drug)]] 5 µM |  | **1.38×** | +3.1 | 0.047 | 31/48 (MIA PaCa-2, CFPAC-1, …) | top dose only | position effect removed |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.36×** | +2.9 | 0.073 | 25/49 (SW48, HOP62, …) | top dose only | plate-row cell shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3097.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.598×** | -7.3 | 1e-10 | 33/48 (C-33 A, CHP-212, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.588×** | -5.3 | 3e-05 | 48/49 (HEC-1-A, NCI-H2030, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.585×** | -5.2 | 4e-05 | 33/48 (C-33 A, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.515×** | -4.8 | 3e-04 | 45/48 (Hs 766T, SW48, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.631×** | -4.6 | 4e-04 | 29/48 (A-427, C-33 A, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.657×** | -4.2 | 0.002 | 29/48 (SW48, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.678×** | -3.9 | 0.007 | 45/49 (NCI-H2122, NCI-H2030, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.757×** | -3.8 | 0.009 | 39/49 (MIA PaCa-2, Hs 766T, …) | all doses, flat | position effect removed |
| [[Allantoin (drug)]] 0.5 µM |  | **0.711×** | -3.4 | 0.037 | 38/48 (Hs 766T, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[Bergenin (drug)]] 0.5 µM |  | **0.713×** | -3.4 | 0.037 | 37/48 (RPMI-7951, AN3 CA, …) | inconsistent across doses | position effect removed |
| [[PH-797804 (drug)]] 0.5 µM |  | **0.631×** | -3.3 | 0.049 | 35/49 (CHP-212, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[BAY1125976 (drug)]] 0.5 µM |  | **0.641×** | -3.2 | 0.066 | 38/48 (H4, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.735×** | -3.1 | 0.084 | 28/48 (CHP-212, C-33 A, …) | inconsistent across doses | position effect removed |
| [[Celecoxib (drug)]] 0.5 µM |  | 0.658× | -3.0 | 0.11 | 35/49 (SW 1271, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3097. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 296 | 12 (6 ⚠) | 1 | [[Ixazomib citrate (drug)]] 5 µM 18.3× (z +24.3) | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -9.6) |
| [[COLO 205 (line)]] | alt | 75.2 | 9 (5 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 27.4× (z +18.3) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 18.7× (z +16.8) | — |
| [[HEC-1-A (line)]] | alt | 211 | 7 (2 ⚠) | 2 | [[Ixazomib citrate (drug)]] 5 µM 16.3× (z +25.1) | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -9.7) |
| [[HOP62 (line)]] | alt | 249 | 9 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 21.7× (z +23.8) | — |
| [[CFPAC-1 (line)]] | alt | 188 | 8 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 21.6× (z +18.9) | — |
| [[HepG2_C3A (line)]] | wt | 145 | 8 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 8.61× (z +13.8) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 7.71× (z +13.1) | — |
| [[LOX-IMVI (line)]] | wt | 333 | 6 (1 ⚠) | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 14.6× (z +20.7) | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -9.9) |
| [[Panc 03.27 (line)]] | alt | 146 | 8 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 19.1× (z +23.8) | — |
| [[SHP-77 (line)]] | alt | 126 | 7 (4 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 12.2× (z +16.3) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 6.58× (z +12.7) | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -11.7) |
| [[SNU-423 (line)]] | alt | 149 | 8 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 17.2× (z +21.9) | — |
| [[SW 900 (line)]] | alt | 163 | 8 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 14.3× (z +21.1) | — |
| [[SW1417 (line)]] | alt | 276 | 8 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 14.5× (z +22.1) | — |
| [[A498 (line)]] | wt | 99.6 | 7 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 11.2× (z +20.0) | — |
| [[C-33 A (line)]] | alt | 280 | 4 | 3 | [[Auranofin (drug)]] 5 µM 6.83× (z +14.2) | [[Homoharringtonine (drug)]] 5 µM 0.0932× (z -25.0) |
| [[C32 (line)]] | wt | 83.1 | 7 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 30.2× (z +21.7) | — |
| [[HCT15 (line)]] | alt | 219 | 6 (1 ⚠) | 1 | [[Ixazomib citrate (drug)]] 5 µM 16.4× (z +20.4) | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -13.1) |
| [[Hs 766T (line)]] | wt | 141 | 7 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 10.3× (z +18.7) | — |
| [[HT-29 (line)]] | alt | 188 | 7 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 28.9× (z +25.2) | — |
| [[LS 180 (line)]] | wt | 295 | 7 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 15.2× (z +23.2) | — |
| [[NCI-H1792 (line)]] | alt | 129 | 7 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 7.40× (z +13.1) | — |
| [[NCI-H460 (line)]] | wt | 231 | 7 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 7.20× (z +16.8) | — |
| [[SK-MEL-2 (line)]] | alt | 205 | 7 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 9.31× (z +18.3) | — |
| [[SW48 (line)]] | wt | 554 | 4 | 3 | [[Ixazomib citrate (drug)]] 5 µM 10.3× (z +15.7) | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -13.9) |
| [[A-172 (line)]] | wt | 99.1 | 6 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 13.8× (z +18.2) | — |
| [[BT-474 (line)]] | alt | 280 | 4 | 2 | [[Auranofin (drug)]] 5 µM 8.47× (z +15.9) | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -13.2) |
| [[CHP-212 (line)]] | wt | 267 | 5 (1 ⚠) | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 6.63× (z +12.7) | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -16.6) |
| [[H4 (line)]] | wt | 222 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 17.9× (z +20.2) | — |
| [[HS-578T (line)]] | alt | 175 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 22.9× (z +24.4) | — |
| [[LoVo (line)]] | wt | 295 | 6 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 8.67× (z +18.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 219 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 15.3× (z +20.0) | — |
| [[RKO (line)]] | wt | 222 | 4 | 2 | [[Ixazomib citrate (drug)]] 0.5 µM 6.99× (z +14.5) | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -11.8) |
| [[RPMI-7951 (line)]] | alt | 124 | 6 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 21.3× (z +21.8) | — |
| [[SNU-1 (line)]] | wt | 276 | 6 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 7.68× (z +15.8) | — |
| [[A-427 (line)]] | wt | 254 | 3 | 2 | [[Ixazomib citrate (drug)]] 5 µM 4.51× (z +13.0) | [[Homoharringtonine (drug)]] 0.5 µM 0.0669× (z -23.3) |
| [[AsPC-1 (line)]] | alt | 307 | 5 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 7.79× (z +13.0) | — |
| [[hTERT-HPNE (line)]] | wt | 214 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 15.1× (z +20.1) | — |
| [[J82 (line)]] | alt | 135 | 4 | 1 | [[Ixazomib citrate (drug)]] 5 µM 13.2× (z +17.4) | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -8.9) |
| [[KATO III (line)]] | alt | 235 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 13.4× (z +19.7) | — |
| [[NCI-H1573 (line)]] | alt | 239 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.39× (z +13.4) | — |
| [[NCI-H2030 (line)]] | alt | 309 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 7.81× (z +16.0) | — |
| [[NCI-H23 (line)]] | alt | 244 | 3 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 5.37× (z +13.5) | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -15.1) |
| [[NCI-H2347 (line)]] | alt | 290 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 10.1× (z +15.7) | — |
| [[PANC-1 (line)]] | alt | 177 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 10.5× (z +20.3) | — |
| [[A549 (line)]] | wt | 176 | 3 | 1 | [[Ixazomib citrate (drug)]] 5 µM 6.12× (z +14.3) | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -9.7) |
| [[SW 1271 (line)]] | alt | 214 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 31.7× (z +15.1) | — |
| [[AN3 CA (line)]] | alt | 204 | 2 | 0 | [[Auranofin (drug)]] 5 µM 4.56× (z +10.4) | — |
| [[SW 1088 (line)]] | alt | 132 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 33.6× (z +11.2) | — |
| [[NCI-H661 (line)]] | alt | 101 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 10.8× (z +8.6) | — |
| [[NCI-H2122 (line)]] | alt | 209 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 194 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3097), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AHSA1]] | +0.81 | +0.85 / +0.79 | both halves | 7e-06 | STRING 930 |
| [[CCT3]] | +0.76 | +0.72 / +0.74 | both halves | 7e-06 | STRING 880 |
| [[HSP90AB1]] | +0.76 | +0.76 / +0.75 | both halves | 7e-06 | pathway: Attenuation phase; STRING 999 |
| [[HSPD1]] | +0.76 | +0.76 / +0.74 | both halves | 7e-06 | STRING 933 |
| [[TCP1]] | +0.75 | +0.74 / +0.71 | both halves | 7e-06 | STRING 931 |
| [[HSP90AA1]] | +0.74 | +0.68 / +0.74 | both halves | 7e-06 | pathway: Attenuation phase; STRING 999 |
| [[HSP90AB3P]] | +0.73 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[CCT4]] | +0.72 | +0.67 / +0.74 | both halves | 7e-06 | STRING 929 |
| [[PSMD2]] | +0.71 | +0.71 / +0.65 | both halves | 7e-06 | pathway: AUF1 (hnRNP D0) binds and destabilizes mRNA; STRING 466 |
| [[STIP1]] | +0.70 | +0.69 / +0.69 | both halves | 7e-06 | pathway: HSP90 chaperone cycle for steroid hormone receptors (SHR) in the presence of ligand; STRING 999 |
| [[HSP90AA2P]] | +0.70 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[CCT6A]] | +0.68 | +0.56 / +0.78 | both halves | 1e-05 | STRING 872 |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YY1AP1]] | -0.64 | -0.48 / -0.65 | both halves | 2e-05 |  |
| [[ABCA5]] | -0.57 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[ETFRF1]] | -0.57 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[REL]] | -0.57 | -0.50 / -0.58 | both halves | 1e-05 | STRING 775 |
| [[TYW5]] | -0.57 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[ZMYM5]] | -0.56 | -0.64 / -0.51 | both halves | 1e-05 |  |
| [[DOP1A]] | -0.56 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[CLK4]] | -0.56 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[ZNF44]] | -0.55 | -0.65 / -0.47 | both halves | 2e-05 |  |
| [[PPIG]] | -0.55 | -0.64 / -0.43 | both halves | 3e-05 | same gene group; pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[FAM200B]] | -0.55 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[CHMP4A]] | -0.55 | -0.56 / -0.47 | both halves | 2e-05 | pathway: Autophagy; STRING 522 |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.794). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-20.0, -11.7); signed map (-26.5, -29.3). **Vector** length 159, 59.7% of its response variance represented; |z| ≥ 3 in 1,564 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *heat shock* (control, mean cos +0.51 to 13); *HSF1 activation* (reactome, mean cos +0.53 to 13); *mTORC1 signaling* (hallmark, mean cos +0.54 to 13).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +12.8 | +19.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +11.9 | +17.3 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +11.6 | +12.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +11.0 | +24.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +10.7 | +24.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.6 | +10.3 |
|  | [[Infigratinib (drug)]] 5 µM |  | +4.0 | +5.5 |
|  | [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM |  | +3.5 | +1.9 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -12.2 | -5.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -11.2 | -4.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -9.5 | -7.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -8.6 | -4.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -8.2 | -1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -5.6 | -4.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.1 | -0.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.1 | -1.7 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -3.9 | -3.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -3.8 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | heat shock protein family A (Hsp70) member 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q24.1 — chr11:123,057,489-123,063,230 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HSC71, HSC70, HSP73; previously HSPA10 |
| Gene groups (HGNC) | Heat shock 70kDa proteins; Spliceosomal C complex; Spliceosomal P complex |
| Hallmark sets | G2M_CHECKPOINT |
| Reactome | 48 pathways, smallest: Lipophagy; CHL1 interactions; GABA synthesis, release, reuptake and degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [P11142](https://www.uniprot.org/uniprotkb/P11142) (Heat shock cognate 71 kDa protein):

> Molecular chaperone implicated in a wide variety of cellular processes, including protection of the proteome from stress, folding and transport of newly synthesized polypeptides, chaperone-mediated autophagy, activation of proteolysis of misfolded proteins, formation and dissociation of protein complexes, and antigen presentation. Plays a pivotal role in the protein quality control system, ensuring the correct folding of proteins, the re-folding of misfolded proteins and controlling the …

**Summary**, from NCBI Gene [3312](https://www.ncbi.nlm.nih.gov/gene/3312):

> This gene encodes a member of the heat shock protein 70 family, which contains both heat-inducible and constitutively expressed members. This protein belongs to the latter group, which are also referred to as heat-shock cognate proteins. It functions as a chaperone, and binds to nascent polypeptides to facilitate correct folding. It also functions as an ATPase in the disassembly of clathrin-coated vesicles during transport of membrane components through the cell. Alternatively spliced …

**Accessions** — [HGNC:5241](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5241) · Entrez [3312](https://www.ncbi.nlm.nih.gov/gene/3312) · UniProt [P11142](https://www.uniprot.org/uniprotkb/P11142) · Ensembl [ENSG00000109971](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109971)

## Data

Gene col 3097: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3097); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3097, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3097]; `tensor/DDL_lfc|DDL_z.npy` [3097]; `embed/gene_vectors.npy` [3097]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3097 or target_col == 3097). Every well: [[HSPA8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HSPA8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
