---
symbol: "LUC7L3"
type: "gene"
col: 3004
ensembl_id: "ENSG00000108848"
name: "LUC7 like 3 pre-mRNA splicing factor"
location: "17q21.33"
module: 21
arm: "+"
pooled_cpm: 366.34
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 2
n_dd_up_clean: 12
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# LUC7L3

*LUC7 like 3 pre-mRNA splicing factor* — 17q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.62× (z +17.6, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.720× (z -8.4, q 2e-14, down in 40 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 9 lines (CHP-212 0.504×, HEC-1-A 0.595×, SW480 0.616×, hTERT-HPNE 0.577×, …).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PNISR]] (+0.73, fdr 7e-06), [[PABPN1]] (+0.69, fdr 7e-06), [[VAMP2]] (+0.67, fdr 7e-06); moves opposite to [[TINF2]] (-0.62, fdr 1e-05), [[EIF2B2]] (-0.58, fdr 2e-05), [[PSMD8]] (-0.55, fdr 1e-05).
> It is in [[Module 021]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3004.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.62×** | +17.6 | 0e+00 | 48/48 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.57×** | +17.2 | 0e+00 | 48/48 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.62×** | +12.4 | 3e-33 | 43/48 (NCI-H1792, SK-MEL-2, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.94×** | +12.1 | 2e-31 | 48/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.86×** | +11.4 | 5e-28 | 47/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.83×** | +11.1 | 2e-26 | 42/48 (C32, HS-578T, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.63×** | +9.0 | 2e-17 | 43/48 (C32, LoVo, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +7.6 | 2e-12 | 44/47 (COLO 205, LoVo, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.45×** | +6.8 | 9e-10 | 35/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.37×** | +5.8 | 4e-07 | 36/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.34×** | +4.9 | 4e-05 | 31/45 (C32, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~10% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.28×** | +4.6 | 2e-04 | 30/48 (KATO III, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.52×** | +4.0 | 0.002 | 36/49 (KATO III, RPMI-7951, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.31×** | +3.5 | 0.017 | 35/48 (MIA PaCa-2, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.27×** | +3.2 | 0.056 | 29/48 (NCI-H1792, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.074 | 19/48 (C32, RPMI-7951, …) | inconsistent across doses |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.26×** | +3.0 | 0.074 | 25/48 (HT-29, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.12× | +3.0 | 0.074 | 8/48 (LoVo, KATO III, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.17× | +2.9 | 0.089 | 21/48 (KATO III, LS 180, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3004.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 9 lines (CHP-212 0.504×, HEC-1-A 0.595×, SW480 0.616×, hTERT-HPNE 0.577×, …).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.720×** | -8.4 | 2e-14 | 40/49 (CHP-212, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.903× | -6.5 | 3e-08 | 1/50 (SW 1271) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.800×** | -4.1 | 0.009 | 32/48 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.842× | -3.1 | 0.25 | 23/48 (NCI-H1573, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3004. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 363 | 10 (3 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.40× (z +24.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.652× (z -8.7) |
| [[KATO III (line)]] | alt | 336 | 8 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.16× (z +26.6) | — |
| [[LoVo (line)]] | wt | 367 | 8 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.72× (z +20.7) | — |
| [[NCI-H1792 (line)]] | alt | 254 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +22.3) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.78× (z +15.8) | — |
| [[BT-474 (line)]] | alt | 1,025 | 7 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.85× (z +19.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.80× (z +19.2) | — |
| [[NCI-H23 (line)]] | alt | 417 | 7 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.65× (z +14.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.42× (z +12.6) | — |
| [[C32 (line)]] | wt | 217 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +18.5) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.55× (z +15.9) | — |
| [[H4 (line)]] | wt | 362 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.54× (z +13.2) | — |
| [[LS 180 (line)]] | wt | 352 | 5 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.30× (z +24.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.614× (z -9.8) |
| [[PANC-1 (line)]] | alt | 408 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.73× (z +21.5) | — |
| [[RKO (line)]] | wt | 269 | 6 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.57× (z +12.3) | — |
| [[SW480 (line)]] | alt | 510 | 5 (1 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 3.39× (z +18.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.05× (z +16.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.616× (z -10.4) |
| [[COLO 205 (line)]] | alt | 399 | 5 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.40× (z +16.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.39× (z +16.5) | — |
| [[HepG2_C3A (line)]] | wt | 295 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.28× (z +15.0) | — |
| [[HOP62 (line)]] | alt | 341 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +17.5) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.32× (z +14.1) | — |
| [[HS-578T (line)]] | alt | 284 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +16.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.68× (z +15.5) | — |
| [[HT-29 (line)]] | alt | 330 | 4 (1 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 2.73× (z +14.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.24× (z +11.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.604× (z -9.9) |
| [[hTERT-HPNE (line)]] | wt | 343 | 4 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.58× (z +12.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.577× (z -10.0) |
| [[J82 (line)]] | alt | 341 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +13.7) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.43× (z +12.6) | — |
| [[SNU-1 (line)]] | wt | 354 | 5 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.70× (z +11.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +11.5) | — |
| [[SW 900 (line)]] | alt | 327 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.35× (z +15.1) | — |
| [[A498 (line)]] | wt | 323 | 3 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +16.6) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.32× (z +11.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.650× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 452 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.13× (z +9.2) | — |
| [[NCI-H1573 (line)]] | alt | 297 | 4 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.63× (z +13.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.33× (z +12.7) | — |
| [[Panc 03.27 (line)]] | alt | 436 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.26× (z +13.4) | — |
| [[RPMI-7951 (line)]] | alt | 323 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.01× (z +13.2) | — |
| [[SK-MEL-2 (line)]] | alt | 353 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +20.1) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.94× (z +9.9) | — |
| [[SNU-423 (line)]] | alt | 283 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +17.7) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +10.9) | — |
| [[SW48 (line)]] | wt | 316 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.40× (z +16.0) | — |
| [[HCT15 (line)]] | alt | 501 | 2 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.86× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.636× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 357 | 3 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 1.90× (z +8.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 1.88× (z +8.8) | — |
| [[NCI-H2030 (line)]] | alt | 260 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.76× (z +11.3) | — |
| [[NCI-H2347 (line)]] | alt | 290 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.74× (z +14.5) | — |
| [[SHP-77 (line)]] | alt | 337 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.47× (z +12.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.45× (z +12.8) | — |
| [[SW1417 (line)]] | alt | 408 | 3 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.89× (z +14.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.80× (z +13.8) | — |
| [[A-172 (line)]] | wt | 284 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +11.2) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[A-427 (line)]] | wt | 334 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.10× (z +11.7) | — |
| [[A549 (line)]] | wt | 340 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +16.4) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.69× (z +13.2) | — |
| [[AsPC-1 (line)]] | alt | 263 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.42× (z +13.2) | — |
| [[CFPAC-1 (line)]] | alt | 357 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +11.6) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.94× (z +8.8) | — |
| [[CHP-212 (line)]] | wt | 918 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.38× (z +11.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -12.3) |
| [[HEC-1-A (line)]] | alt | 491 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.57× (z +9.3) ⚠ cell-cycle shift, explains ~34% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.595× (z -10.6) |
| [[Hs 766T (line)]] | wt | 319 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.38× (z +10.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.09× (z +8.5) | — |
| [[SW 1271 (line)]] | alt | 396 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.31× (z +10.5) | — |
| [[AN3 CA (line)]] | alt | 322 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.36× (z +11.4) | — |
| [[C-33 A (line)]] | alt | 413 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 389 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 448 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 348 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 248 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3004), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNISR]] | +0.73 | +0.76 / +0.75 | both halves | 7e-06 | STRING 999 |
| [[PABPN1]] | +0.69 | +0.68 / +0.65 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[VAMP2]] | +0.67 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[PRPF4B]] | +0.63 | +0.64 / +0.53 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 860 |
| [[SRSF11]] ⚠ | +0.61 | +0.63 / +0.50 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 915; ⚠ in the vector space only through flagged drug-doses |
| [[CSKMT]] | +0.56 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[ARGLU1]] | +0.55 | +0.56 / +0.63 | both halves | 1e-05 | STRING 728 |
| [[ZNF706]] | +0.55 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[RENO1]] | +0.54 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[HNRNPH1]] | +0.54 | +0.64 / +0.39 | both halves | 5e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[YTHDC1]] | +0.53 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[CELF1]] | +0.52 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[HEXD]] | +0.51 | +0.44 / +0.54 | both halves | 3e-05 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TINF2]] | -0.62 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[EIF2B2]] | -0.58 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[PSMD8]] | -0.55 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[EIF2S1]] | -0.54 | -0.54 / -0.48 | both halves | 2e-05 | pathway: HALLMARK_E2F_TARGETS |
| [[RRAGA]] | -0.54 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[CPSF3]] | -0.50 | -0.27 / -0.52 | both halves | 3e-04 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[KARS1]] | -0.50 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[GPS1]] | -0.49 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[TLN1]] | -0.49 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[VPS4A]] | -0.48 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[PPP1CA]] | -0.48 | -0.42 / -0.53 | both halves | 4e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[TXNDC9]] | -0.48 | -0.35 / -0.46 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.299). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-20.3, -4.5); signed map (-6.5, 2.1). **Vector** length 121, 49.6% of its response variance represented; |z| ≥ 3 in 1,082 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.1 | +3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.4 | +9.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.8 | +1.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | +2.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +17.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.5 | +3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.5 | +0.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.9 | -0.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.0 | -8.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -8.6 | -1.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -8.0 | +1.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.8 | +1.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.8 | +4.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -4.0 | -2.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.7 | +2.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.3 | -1.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -3.1 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | LUC7 like 3 pre-mRNA splicing factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.33 — chr17:50,719,565-50,756,219 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LUC7A, CROP, OA48-18, CREAP-1, FLJ11063, CRA, hLuc7A |
| Hallmark sets | E2F_TARGETS |
| Reactome | 4 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [O95232](https://www.uniprot.org/uniprotkb/O95232) (Luc7-like protein 3):

> Binds cAMP regulatory element DNA sequence. May play a role in RNA splicing.

**Summary**, from NCBI Gene [51747](https://www.ncbi.nlm.nih.gov/gene/51747):

> This gene encodes a protein with an N-terminal half that contains cysteine/histidine motifs and leucine zipper-like repeats, and the C-terminal half is rich in arginine and glutamate residues (RE domain) and arginine and serine residues (RS domain). This protein localizes with a speckled pattern in the nucleus, and could be involved in the formation of splicesome via the RE and RS domains. Two alternatively spliced transcript variants encoding the same protein have been found for this gene. …

**Accessions** — [HGNC:24309](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24309) · Entrez [51747](https://www.ncbi.nlm.nih.gov/gene/51747) · UniProt [O95232](https://www.uniprot.org/uniprotkb/O95232) · Ensembl [ENSG00000108848](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108848)

## Data

Gene col 3004: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3004); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3004, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3004]; `tensor/DDL_lfc|DDL_z.npy` [3004]; `embed/gene_vectors.npy` [3004]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3004 or target_col == 3004). Every well: [[LUC7L3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LUC7L3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
