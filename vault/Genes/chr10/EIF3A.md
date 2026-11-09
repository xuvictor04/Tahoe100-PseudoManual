---
symbol: "EIF3A"
type: "gene"
col: 2861
ensembl_id: "ENSG00000107581"
name: "eukaryotic translation initiation factor 3 subunit A"
location: "10q26.11"
module: 1
arm: "+"
pooled_cpm: 370.21
n_lines_expressing: 50
n_dd_up: 39
n_dd_down: 0
n_dd_up_clean: 27
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# EIF3A

*eukaryotic translation initiation factor 3 subunit A* — 10q26.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.26× (z +18.6, q 0e+00, up in 46 of 48 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.23× (z +13.3, q 6e-38, up in 47 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (LoVo 0.564×, RKO 0.556×, AN3 CA 0.506×, SW480 0.599×, …; ⚠ cell-cycle shift, explains ~11% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (HepG2/C3A 0.508×; ⚠ cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (AN3 CA 0.463×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RSL1D1]] (+0.68, fdr 7e-06), [[PNN]] (+0.66, fdr 7e-06), [[RBM25]] (+0.65, fdr 7e-06); moves opposite to [[MPC2]] (-0.51, fdr 3e-05), [[ANKRD37]] (-0.48, fdr 2e-05), [[BRK1]] (-0.48, fdr 3e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 14 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2861.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.26×** | +18.6 | 0e+00 | 46/48 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.23×** | +13.3 | 6e-38 | 47/48 (NCI-H1792, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.91×** | +10.7 | 1e-24 | 45/48 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.79×** | +9.7 | 5e-20 | 45/48 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.77×** | +9.5 | 3e-19 | 48/48 (Hs 766T, SW 900, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.79×** | +8.9 | 5e-17 | 49/49 (COLO 205, SNU-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.59×** | +8.3 | 1e-14 | 44/48 (C32, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.64×** | +8.2 | 1e-14 | 42/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.59×** | +7.7 | 6e-13 | 42/48 (NCI-H460, SW 900, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +7.6 | 1e-12 | 45/47 (COLO 205, Hs 766T, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.54×** | +7.2 | 3e-11 | 38/48 (AN3 CA, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.53×** | +7.1 | 8e-11 | 42/49 (A498, HT-29, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.50×** | +6.7 | 7e-10 | 44/48 (SNU-423, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.52×** | +6.7 | 1e-09 | 39/48 (NCI-H1573, COLO 205, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.44×** | +5.6 | 8e-07 | 35/45 (HT-29, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[EX229 (drug)]] 5 µM |  | **1.83×** | +5.3 | 5e-06 | 44/48 (C32, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.35×** | +4.9 | 2e-05 | 35/47 (Hs 766T, SNU-423, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.32×** | +4.6 | 1e-04 | 32/48 (MIA PaCa-2, A-427, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.69×** | +4.6 | 1e-04 | 41/48 (CFPAC-1, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.65×** | +4.4 | 3e-04 | 42/48 (Hs 766T, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.19× | +4.0 | 0.002 | 23/49 (CFPAC-1, NCI-H2030, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +3.9 | 0.002 | 29/48 (HCT15, CFPAC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2861.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (LoVo 0.564×, RKO 0.556×, AN3 CA 0.506×, SW480 0.599×, …; ⚠ cell-cycle shift, explains ~11% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (HepG2/C3A 0.508×; ⚠ cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (AN3 CA 0.463×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.815× | -3.4 | 0.20 | 28/49 (NCI-H2122, COLO 205, …) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.817× | -3.4 | 0.20 | 31/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.826× | -3.2 | 0.26 | 25/48 (KATO III, NCI-H2030, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2861. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 222 | 10 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +15.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.62× (z +10.5) | — |
| [[SNU-423 (line)]] | alt | 328 | 10 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +21.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.36× (z +14.0) | — |
| [[NCI-H460 (line)]] | wt | 477 | 9 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +17.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.05× (z +13.1) | — |
| [[SW480 (line)]] | alt | 415 | 8 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +10.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.90× (z +9.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.599× (z -10.7) ⚠ cell-cycle shift, explains ~11% of this change |
| [[COLO 205 (line)]] | alt | 254 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +19.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.59× (z +12.4) | — |
| [[LoVo (line)]] | wt | 434 | 7 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +17.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.39× (z +12.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.564× (z -11.2) ⚠ cell-cycle shift, explains ~11% of this change |
| [[SW 900 (line)]] | alt | 368 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +16.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.75× (z +12.8) | — |
| [[A-172 (line)]] | wt | 264 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +14.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.35× (z +11.9) | — |
| [[NCI-H1573 (line)]] | alt | 223 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +23.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.90× (z +16.0) | — |
| [[C32 (line)]] | wt | 257 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +16.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.85× (z +11.9) | — |
| [[H4 (line)]] | wt | 237 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +19.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.10× (z +16.5) | — |
| [[NCI-H1792 (line)]] | alt | 246 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +21.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.82× (z +17.2) | — |
| [[A498 (line)]] | wt | 343 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +14.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.52× (z +14.0) | — |
| [[CFPAC-1 (line)]] | alt | 267 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +20.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.41× (z +14.7) | — |
| [[HT-29 (line)]] | alt | 398 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +12.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.16× (z +10.6) | — |
| [[NCI-H2030 (line)]] | alt | 417 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +19.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.25× (z +11.9) | — |
| [[PANC-1 (line)]] | alt | 519 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +16.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.14× (z +11.4) | — |
| [[AsPC-1 (line)]] | alt | 400 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +22.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.96× (z +13.4) | — |
| [[HCT15 (line)]] | alt | 459 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +12.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.15× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.528× (z -10.4) ⚠ cell-cycle shift, explains ~11% of this change |
| [[HOP62 (line)]] | alt | 247 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +16.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.14× (z +13.1) | — |
| [[HS-578T (line)]] | alt | 197 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +18.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.01× (z +15.1) | — |
| [[KATO III (line)]] | alt | 303 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +16.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.02× (z +14.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 428 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +16.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.68× (z +14.0) | — |
| [[A549 (line)]] | wt | 367 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +15.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.20× (z +10.1) | — |
| [[AN3 CA (line)]] | alt | 749 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 3.14× (z +13.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -10.9) ⚠ cell-cycle shift, explains ~11% of this change |
| [[LOX-IMVI (line)]] | wt | 423 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +11.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.66× (z +11.0) | — |
| [[LS 180 (line)]] | wt | 409 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.37× (z +12.6) | — |
| [[RKO (line)]] | wt | 485 | 2 (1 ⚠) | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 4.32× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.556× (z -11.0) ⚠ cell-cycle shift, explains ~11% of this change |
| [[HEC-1-A (line)]] | alt | 350 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +12.7) ⚠ cell-cycle shift, explains ~26% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.612× (z -9.0) ⚠ cell-cycle shift, explains ~11% of this change |
| [[HepG2_C3A (line)]] | wt | 718 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +9.0) ⚠ cell-cycle shift, explains ~26% of this change | [[Panobinostat (drug)]] 5 µM 0.508× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 340 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +14.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.05× (z +13.9) | — |
| [[J82 (line)]] | alt | 276 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +12.1) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H23 (line)]] | alt | 464 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +12.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.13× (z +8.9) | — |
| [[NCI-H2347 (line)]] | alt | 343 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +15.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.57× (z +12.5) | — |
| [[Panc 03.27 (line)]] | alt | 404 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +12.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.61× (z +12.3) | — |
| [[RPMI-7951 (line)]] | alt | 245 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +14.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.81× (z +10.6) | — |
| [[SHP-77 (line)]] | alt | 290 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +11.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.08× (z +9.7) | — |
| [[SK-MEL-2 (line)]] | alt | 358 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +17.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.50× (z +10.9) | — |
| [[SW1417 (line)]] | alt | 436 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.51× (z +9.1) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[SNU-1 (line)]] | wt | 402 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.48× (z +10.0) | — |
| [[SW 1088 (line)]] | alt | 221 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +9.2) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[SW48 (line)]] | wt | 623 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 2.18× (z +9.6) | — |
| [[A-427 (line)]] | wt | 445 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 177 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 483 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 424 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 353 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 371 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 368 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 254 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2861), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RSL1D1]] | +0.68 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[PNN]] | +0.66 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[RBM25]] | +0.65 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[MTIF2]] | +0.64 | +0.60 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_ALLOGRAFT_REJECTION; STRING 541 |
| [[TCERG1]] | +0.62 | +0.52 / +0.60 | both halves | 1e-05 | STRING 603 |
| [[NCL]] | +0.62 | +0.63 / +0.61 | both halves | 7e-06 | same gene group; STRING 879 |
| [[UBE3A]] | +0.62 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[NOP14]] | +0.59 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[BAZ1B]] | +0.58 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[GNL3L]] | +0.57 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[EIF5B]] | +0.57 | +0.66 / +0.54 | both halves | 1e-05 | pathway: Cap-dependent Translation Initiation; STRING 851 |
| [[SSB]] | +0.57 | +0.60 / +0.51 | both halves | 1e-05 | STRING 518 |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPC2]] | -0.51 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[ANKRD37]] | -0.48 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[BRK1]] | -0.48 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[SAP30-DT]] | -0.48 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[WDR54]] | -0.47 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[NARF]] | -0.47 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[AKR7A2]] | -0.47 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[RNF122]] | -0.46 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[MLLT3]] | -0.46 | -0.46 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.492). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-24.7, -40.6); signed map (4.4, -43.7). **Vector** length 109, 46.0% of its response variance represented; |z| ≥ 3 in 1,547 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +5.8 | +5.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.8 | +9.5 |
|  | [[EX229 (drug)]] 5 µM |  | +5.6 | +5.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +5.0 | +7.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.9 | +1.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.4 | +1.5 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | +4.4 | +2.9 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +4.2 | +2.4 |
| fall | [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -3.4 | -3.4 |
|  | [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -0.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.0 | +10.7 |
|  | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | -3.0 | -2.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.9 | +9.7 |
|  | [[Decitabine (drug)]] 0.05 µM |  | -2.9 | -1.6 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.7 | -1.8 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -2.7 | -1.3 |
|  | [[Ritonavir (drug)]] 0.5 µM |  | -2.7 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation initiation factor 3 subunit A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.11 — chr10:119,033,670-119,080,817 (-) |
| Ensembl biotype | protein_coding |
| Also known as | eIF3-theta, eIF3-p170, KIAA0139, TIF32; previously EIF3, EIF3S10 |
| Gene groups (HGNC) | Eukaryotic translation initiation factor 3 complex subunits; Armadillo like helical domain containing; Small nucleolar RNA protein coding host genes |
| Hallmark sets | ALLOGRAFT_REJECTION |
| Reactome | 14 pathways, smallest: Formation of the ternary complex, and subsequently, the 43S complex; Ribosomal scanning and start codon recognition; Translation initiation complex formation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14152](https://www.uniprot.org/uniprotkb/Q14152) (Eukaryotic translation initiation factor 3 subunit A):

> RNA-binding component of the eukaryotic translation initiation factor 3 (eIF-3) complex, which is required for several steps in the initiation of protein synthesis. The eIF-3 complex associates with the 40S ribosome and facilitates the recruitment of eIF-1, eIF-1A, eIF-2:GTP:methionyl-tRNAi and eIF-5 to form the 43S pre-initiation complex (43S PIC). The eIF-3 complex stimulates mRNA recruitment to the 43S PIC and scanning of the mRNA for AUG recognition. The eIF-3 complex is also required for …

**Summary**, from NCBI Gene [8661](https://www.ncbi.nlm.nih.gov/gene/8661):

> Enables RNA binding activity. Contributes to translation initiation factor activity. Involved in IRES-dependent viral translational initiation; formation of cytoplasmic translation initiation complex; and viral translational termination-reinitiation. Located in cytosol. Part of eukaryotic translation initiation factor 3 complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:3271](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3271) · Entrez [8661](https://www.ncbi.nlm.nih.gov/gene/8661) · UniProt [Q14152](https://www.uniprot.org/uniprotkb/Q14152) · Ensembl [ENSG00000107581](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107581)

## Data

Gene col 2861: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2861); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2861, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2861]; `tensor/DDL_lfc|DDL_z.npy` [2861]; `embed/gene_vectors.npy` [2861]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2861 or target_col == 2861). Every well: [[EIF3A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF3A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
