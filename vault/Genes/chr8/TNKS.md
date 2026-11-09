---
symbol: "TNKS"
type: "gene"
col: 10368
ensembl_id: "ENSG00000173273"
name: "tankyrase"
location: "8p23.1"
module: 76
arm: "+"
pooled_cpm: 243.43
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 9
n_dd_up_clean: 13
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# TNKS

*tankyrase* — 8p23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 2.14× (z +14.5, q 7e-45, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.390× (z -19.0, q 0e+00, down in 49 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.690× (z -7.5, q 8e-12, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIK3C3]] (+0.73, fdr 7e-06), [[HMBOX1]] (+0.67, fdr 7e-06), [[UBR2]] (+0.66, fdr 7e-06); moves opposite to [[LONRF3]] (-0.48, fdr 3e-05), [[AKIRIN1]] (-0.48, fdr 5e-05), [[RBBP8]] (-0.47, fdr 4e-05).
> It is in [[Module 076]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10368.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **2.14×** | +14.5 | 7e-45 | 47/48 (NCI-H1792, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.97×** | +13.7 | 2e-40 | 46/48 (NCI-H1573, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.93×** | +13.3 | 8e-38 | 47/48 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.92×** | +13.2 | 2e-37 | 48/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.78×** | +12.5 | 1e-33 | 48/49 (NCI-H460, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.44×** | +10.4 | 3e-23 | 41/48 (RKO, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.95×** | +10.1 | 3e-22 | 46/48 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.63×** | +9.8 | 6e-21 | 42/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.41×** | +6.9 | 3e-10 | 36/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.35×** | +6.1 | 7e-08 | 36/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.71×** | +5.0 | 3e-05 | 35/45 (SNU-1, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.52×** | +4.5 | 4e-04 | 37/49 (NCI-H1792, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.21×** | +3.8 | 0.007 | 24/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.20×** | +3.5 | 0.016 | 22/49 (SNU-423, SHP-77, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.44×** | +3.4 | 0.026 | 27/49 (A498, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | 1.17× | +3.2 | 0.044 | 11/48 (A549, SNU-423, …) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 1.18× | +3.0 | 0.074 | 7/48 (LOX-IMVI, hTERT-HPNE, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10368.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.390×** | -19.0 | 0e+00 | 49/49 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.385×** | -18.5 | 0e+00 | 43/44 (A498, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.480×** | -14.2 | 9e-44 | 47/47 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.557×** | -10.9 | 1e-25 | 36/45 (NCI-H2347, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.690×** | -7.5 | 8e-12 | 44/48 (MIA PaCa-2, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.777×** | -7.2 | 7e-11 | 34/48 (SK-MEL-2, A-172, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.753×** | -5.7 | 8e-07 | 35/48 (KATO III, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.780×** | -5.0 | 4e-05 | 30/49 (NCI-H2347, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.831×** | -3.7 | 0.011 | 25/48 (NCI-H1792, RKO, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10368. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 196 | 11 (2 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +17.7) | [[Dinaciclib (drug)]] 0.5 µM 0.325× (z -19.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 205 | 9 (1 ⚠) | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 3.19× (z +15.4) | [[Dinaciclib (drug)]] 0.5 µM 0.345× (z -14.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 251 | 8 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.38× (z +13.9) | [[Dinaciclib (drug)]] 5 µM 0.303× (z -18.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 406 | 4 | 6 (6 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.40× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.216× (z -22.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 226 | 7 | 3 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.41× (z +12.5) | [[Dinaciclib (drug)]] 0.5 µM 0.322× (z -16.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 100 | 10 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.80× (z +18.9) | — |
| [[Hs 766T (line)]] | wt | 279 | 5 | 4 (4 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.34× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.292× (z -16.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 234 | 5 | 4 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.22× (z +11.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.254× (z -19.2) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.550× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 245 | 7 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.09× (z +15.5) | [[Dinaciclib (drug)]] 0.5 µM 0.354× (z -14.3) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 302 | 8 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +19.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.388× (z -12.3) ⚠ toxic |
| [[A498 (line)]] | wt | 309 | 3 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.203× (z -22.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 244 | 5 | 3 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.10× (z +11.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.480× (z -10.9) ⚠ toxic |
| [[HOP62 (line)]] | alt | 214 | 5 | 3 (3 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.23× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.332× (z -15.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 399 | 4 | 4 (4 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.29× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -14.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 277 | 5 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.316× (z -15.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 337 | 4 | 4 (4 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.34× (z +11.9) | [[Dinaciclib (drug)]] 0.5 µM 0.302× (z -16.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 215 | 6 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.28× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.339× (z -14.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 283 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +15.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.423× (z -18.0) ⚠ cell-cycle shift, explains ~52% of this change |
| [[COLO 205 (line)]] | alt | 160 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.09× (z +12.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.430× (z -9.2) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 300 | 3 | 4 (4 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.55× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.341× (z -12.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 203 | 7 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.69× (z +13.2) | — |
| [[SK-MEL-2 (line)]] | alt | 343 | 4 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.81× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.329× (z -17.0) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 291 | 5 (1 ⚠) | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.95× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.409× (z -10.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 215 | 2 | 4 (4 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.40× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.295× (z -17.2) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 359 | 1 | 5 (5 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.13× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.145× (z -22.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 290 | 3 | 3 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.81× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.234× (z -14.4) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 212 | 2 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.403× (z -11.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 204 | 4 | 2 (2 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.08× (z +10.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.480× (z -10.4) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 265 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.20× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.390× (z -13.4) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 391 | 1 | 4 (4 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.67× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -14.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 244 | 4 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.64× (z +11.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.476× (z -8.5) ⚠ toxic |
| [[HT-29 (line)]] | alt | 96.7 | 4 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.31× (z +10.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.450× (z -9.3) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 188 | 2 | 3 (3 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.16× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.390× (z -12.1) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 251 | 5 | 0 | [[TAK-901 (drug)]] 0.05 µM 4.05× (z +13.7) | — |
| [[NCI-H2347 (line)]] | alt | 284 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.303× (z -18.9) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 401 | 2 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.03× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.375× (z -13.3) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 278 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.315× (z -14.2) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 364 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.115× (z -18.1) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 485 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -18.2) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 227 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.07× (z +8.8) | — |
| [[J82 (line)]] | alt | 122 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.434× (z -11.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 318 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.190× (z -14.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 218 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.408× (z -10.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 105 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.475× (z -9.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 250 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 272 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 234 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 301 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 233 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10368), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIK3C3]] | +0.73 | +0.64 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[HMBOX1]] | +0.67 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[UBR2]] | +0.66 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[UBE4B]] | +0.62 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[TENT2]] | +0.62 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[UBR3]] | +0.61 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[SNX13]] | +0.59 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[RELCH]] | +0.58 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[ST13]] | +0.58 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[TTC9C]] | +0.58 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[IFT43]] | +0.57 | +0.40 / +0.54 | both halves | 5e-05 |  |
| [[GMPR2]] | +0.57 | +0.44 / +0.67 | both halves | 3e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LONRF3]] | -0.48 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[AKIRIN1]] | -0.48 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[RBBP8]] | -0.47 | -0.43 / -0.42 | both halves | 4e-05 | same gene group |
| [[NANP]] | -0.47 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[CYCS]] | -0.46 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[ZNF121]] | -0.46 | -0.47 / -0.39 | both halves | 6e-05 |  |
| [[LRRC8B]] | -0.45 | -0.41 / -0.47 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.468). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.2, -11.6); signed map (-21.6, 3.8). **Vector** length 99.0, 42.0% of its response variance represented; |z| ≥ 3 in 1,301 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +7.1 | +14.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.0 | +13.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.2 | +13.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +2.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +0.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.8 | -0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +0.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.6 | +3.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.5 | +4.5 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -8.5 | -14.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -7.5 | -7.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.4 | -3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.4 | -7.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.5 | -5.0 |
|  | [[EX229 (drug)]] 5 µM |  | -3.7 | -2.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.3 | -2.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -3.2 | +0.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | tankyrase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p23.1 — chr8:9,555,912-9,782,346 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TIN1, TINF1, TNKS1, PARP-5a, PARP5A, pART5, ARTD5 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; Poly(ADP-ribose) polymerases; Sterile alpha motif domain containing; MicroRNA protein coding host genes |
| Reactome | 11 pathways, smallest: Signaling by WNT in cancer; Degradation of AXIN; Regulation of PTEN stability and activity |
| Matched by | ensembl_id |

**Function**, from UniProt [O95271](https://www.uniprot.org/uniprotkb/O95271) (Poly):

> Poly-ADP-ribosyltransferase involved in various processes such as Wnt signaling pathway, necroptosis, telomere length and vesicle trafficking. Acts as an activator of the Wnt signaling pathway by mediating poly-ADP-ribosylation (PARsylation) of AXIN1 and AXIN2, 2 key components of the beta-catenin destruction complex: poly-ADP-ribosylated target proteins are recognized by RNF146, which mediates their ubiquitination and subsequent degradation. Acts as an inhibitor of necroptosis by mediating …

**Summary**, from NCBI Gene [8658](https://www.ncbi.nlm.nih.gov/gene/8658):

> Enables several functions, including pentosyltransferase activity; telomerase inhibitor activity; and zinc ion binding activity. Involved in several processes, including positive regulation of canonical Wnt signaling pathway; post-translational protein modification; and regulation of chromosome organization. Acts upstream of or within peptidyl-serine phosphorylation and peptidyl-threonine phosphorylation. Located in Golgi apparatus; chromosome, telomeric region; and mitotic spindle pole. …

**Accessions** — [HGNC:11941](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11941) · Entrez [8658](https://www.ncbi.nlm.nih.gov/gene/8658) · UniProt [O95271](https://www.uniprot.org/uniprotkb/O95271) · Ensembl [ENSG00000173273](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173273)

## Data

Gene col 10368: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10368); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10368, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10368]; `tensor/DDL_lfc|DDL_z.npy` [10368]; `embed/gene_vectors.npy` [10368]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10368 or target_col == 10368). Every well: [[TNKS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TNKS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
