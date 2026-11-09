---
symbol: "HNRNPH1"
type: "gene"
col: 9743
ensembl_id: "ENSG00000169045"
name: "heterogeneous nuclear ribonucleoprotein H1"
location: "5q35.3"
module: 12
arm: "+"
pooled_cpm: 341.75
n_lines_expressing: 50
n_dd_up: 36
n_dd_down: 0
n_dd_up_clean: 20
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# HNRNPH1

*heterogeneous nuclear ribonucleoprotein H1* — 5q35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.20× (z +19.1, q 0e+00, up in 47 of 48 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.71× (z +12.7, q 2e-34, up in 47 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Methylthiouracil (drug)]] 5 µM in 1 line (NCI-H596 0.195×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CPT1B]] (+0.66, fdr 1e-05), [[CDK3]] (+0.64, fdr 1e-05), [[RBM39]] (+0.64, fdr 1e-05); moves opposite to [[DPM2]] (-0.59, fdr 6e-05), [[GRB2]] (-0.54, fdr 9e-05), [[EMC4]] (-0.53, fdr 1e-04).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 16 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9743.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **3.20×** | +19.1 | 0e+00 | 47/48 (COLO 205, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.71×** | +12.7 | 2e-34 | 47/48 (C32, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.69×** | +12.6 | 3e-34 | 49/49 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **2.33×** | +10.4 | 5e-23 | 47/48 (COLO 205, PANC-1, …) | rises with dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.02×** | +8.9 | 4e-17 | 48/48 (KATO III, LS 180, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.05×** | +8.8 | 1e-16 | 42/44 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.96×** | +8.6 | 8e-16 | 48/48 (LS 180, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +6.8 | 8e-10 | 44/47 (COLO 205, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~25% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.85×** | +5.6 | 1e-06 | 41/45 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.78×** | +5.2 | 1e-05 | 47/47 (NCI-H460, C-33 A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.50×** | +5.1 | 1e-05 | 37/48 (HS-578T, HEC-1-A, …) | rises with dose | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.76×** | +5.1 | 1e-05 | 47/48 (LoVo, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.76×** | +5.1 | 1e-05 | 48/48 (NCI-H460, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.44×** | +4.6 | 2e-04 | 35/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.43×** | +4.5 | 3e-04 | 31/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.64×** | +4.5 | 3e-04 | 47/48 (Hs 766T, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.61×** | +4.3 | 5e-04 | 48/49 (LoVo, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 0.5 µM |  | **1.56×** | +4.0 | 0.002 | 43/49 (AsPC-1, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.37×** | +3.9 | 0.002 | 33/48 (SNU-423, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.36×** | +3.9 | 0.003 | 32/48 (KATO III, HT-29, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.34×** | +3.7 | 0.006 | 32/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.50×** | +3.7 | 0.006 | 46/48 (AsPC-1, SW480, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Saquinavir (drug)]] 0.5 µM |  | **1.33×** | +3.6 | 0.008 | 39/48 (SK-MEL-2, Panc 03.27, …) | inconsistent across doses |  |
| [[AZD-7648 (drug)]] 0.5 µM |  | **1.47×** | +3.5 | 0.012 | 40/48 (LoVo, HEC-1-A, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.44×** | +3.3 | 0.018 | 39/48 (PANC-1, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.43×** | +3.2 | 0.023 | 39/48 (LS 180, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9743.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Methylthiouracil (drug)]] 5 µM in 1 line (NCI-H596 0.195×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 0.5 µM |  | 0.773× | -3.3 | 0.50 | 39/48 (HEC-1-A, RKO, …) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.792× | -3.0 | 0.73 | 29/48 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.58 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9743. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 324 | 10 (9 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +18.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.78× (z +15.2) | — |
| [[KATO III (line)]] | alt | 213 | 8 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +16.3) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.66× (z +9.8) | — |
| [[LoVo (line)]] | wt | 469 | 8 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +20.3) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.53× (z +13.7) | — |
| [[SW480 (line)]] | alt | 363 | 8 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +15.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.17× (z +10.0) | — |
| [[COLO 205 (line)]] | alt | 220 | 7 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.23× (z +22.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.71× (z +9.3) | — |
| [[HS-578T (line)]] | alt | 298 | 7 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.22× (z +18.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.88× (z +13.7) | — |
| [[NCI-H1573 (line)]] | alt | 254 | 7 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.42× (z +20.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.87× (z +14.6) | — |
| [[NCI-H1792 (line)]] | alt | 234 | 7 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.27× (z +21.3) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.35× (z +12.0) | — |
| [[PANC-1 (line)]] | alt | 278 | 7 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +18.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.16× (z +12.4) | — |
| [[LS 180 (line)]] | wt | 293 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +15.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.11× (z +11.3) | — |
| [[HT-29 (line)]] | alt | 248 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +17.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.70× (z +10.3) | — |
| [[hTERT-HPNE (line)]] | wt | 306 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.80× (z +19.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.66× (z +12.4) | — |
| [[J82 (line)]] | alt | 384 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +15.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.79× (z +9.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 367 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.56× (z +11.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.36× (z +11.0) | — |
| [[SW1417 (line)]] | alt | 350 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +16.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.11× (z +10.9) | — |
| [[A498 (line)]] | wt | 294 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +15.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.79× (z +9.8) | — |
| [[AsPC-1 (line)]] | alt | 261 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.10× (z +21.2) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.53× (z +9.3) | — |
| [[HEC-1-A (line)]] | alt | 348 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +19.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.13× (z +16.0) | — |
| [[RKO (line)]] | wt | 261 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +13.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.46× (z +9.4) | — |
| [[RPMI-7951 (line)]] | alt | 260 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +12.2) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.73× (z +9.1) | — |
| [[SNU-423 (line)]] | alt | 264 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.44× (z +16.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.73× (z +8.5) | — |
| [[SW48 (line)]] | wt | 383 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +13.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.64× (z +12.0) | — |
| [[A-172 (line)]] | wt | 390 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +14.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.56× (z +11.9) | — |
| [[A549 (line)]] | wt | 316 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +14.0) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[C32 (line)]] | wt | 282 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.08× (z +19.3) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.81× (z +16.3) | — |
| [[H4 (line)]] | wt | 384 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +13.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.02× (z +12.4) | — |
| [[HepG2_C3A (line)]] | wt | 301 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +13.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.53× (z +8.9) | — |
| [[HOP62 (line)]] | alt | 328 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.61× (z +16.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.99× (z +9.2) | — |
| [[LOX-IMVI (line)]] | wt | 354 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +15.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.37× (z +8.8) | — |
| [[Panc 03.27 (line)]] | alt | 439 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +17.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.73× (z +10.9) | — |
| [[SW 900 (line)]] | alt | 531 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +16.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.31× (z +12.2) | — |
| [[AN3 CA (line)]] | alt | 445 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +10.0) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[Hs 766T (line)]] | wt | 261 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +13.0) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H23 (line)]] | alt | 371 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +10.7) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 302 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.26× (z +9.5) | — |
| [[SK-MEL-2 (line)]] | alt | 330 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +14.2) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.27× (z +8.5) | — |
| [[A-427 (line)]] | wt | 436 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.26× (z +9.4) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 350 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +14.4) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[CFPAC-1 (line)]] | alt | 279 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +13.2) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[HCT15 (line)]] | alt | 427 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.58× (z +11.6) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 375 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +10.6) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H596 (line)]] | alt | 372 | 0 | 1 | — | [[Methylthiouracil (drug)]] 5 µM 0.195× (z -10.0) |
| [[SNU-1 (line)]] | wt | 315 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.47× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SW 1088 (line)]] | alt | 309 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.88× (z +11.3) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[SW 1271 (line)]] | alt | 497 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +9.4) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[C-33 A (line)]] | alt | 444 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 359 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 335 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 662 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 409 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9743), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPT1B]] | +0.66 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[CDK3]] | +0.64 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[RBM39]] | +0.64 | +0.60 / +0.54 | both halves | 1e-05 | same gene group; pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 639 |
| [[CIRBP]] | +0.64 | +0.69 / +0.55 | both halves | 1e-05 | same gene group |
| [[MYL5]] | +0.60 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[SREK1]] | +0.60 | +0.63 / +0.47 | both halves | 2e-05 | same gene group; STRING 512 |
| [[RXRB]] | +0.59 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[SRSF11]] ⚠ | +0.59 | +0.61 / +0.50 | both halves | 1e-05 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 696; ⚠ in the vector space only through flagged drug-doses |
| [[HNRNPH3]] | +0.58 | +0.60 / +0.52 | both halves | 1e-05 | same gene group; STRING 960 |
| [[AGER]] | +0.56 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[MAP3K2-DT]] | +0.55 | +0.55 / +0.46 | both halves | 3e-05 |  |
| [[CUTALP]] | +0.55 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[SNHG11]] | +0.55 | +0.72 / +0.40 | both halves | 4e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPM2]] | -0.59 | -0.39 / -0.58 | both halves | 6e-05 |  |
| [[GRB2]] | -0.54 | -0.55 / -0.36 | both halves | 9e-05 | pathway: Signaling by FGFR |
| [[EMC4]] | -0.53 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[NIPA2]] | -0.53 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[GGCT]] | -0.52 | -0.49 / -0.40 | both halves | 4e-05 |  |
| [[TMEM147]] | -0.51 | -0.59 / -0.32 | both halves | 2e-04 |  |
| [[ARPC5]] | -0.51 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[PHB1]] | -0.50 | -0.41 / -0.35 | both halves | 1e-04 | STRING 409 |
| [[GDAP2]] | -0.50 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[TMED7]] | -0.50 | -0.57 / -0.34 | both halves | 1e-04 |  |
| [[BAG5]] | -0.50 | -0.33 / -0.57 | both halves | 1e-04 |  |
| [[MLX]] | -0.48 | -0.41 / -0.45 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.299). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (23.8, -9.8); signed map (3.8, -9.6). **Vector** length 96.4, 41.1% of its response variance represented; |z| ≥ 3 in 1,164 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +7.7 | +19.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.4 | +12.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +5.1 | +5.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +4.1 | +5.2 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +4.0 | +5.1 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +3.4 | +3.3 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +3.4 | +4.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.0 | +0.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.9 | +1.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -2.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -1.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.2 | +1.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -3.0 | -3.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.5 | -0.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.4 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | heterogeneous nuclear ribonucleoprotein H1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.3 — chr5:179,614,178-179,634,784 (-) |
| Ensembl biotype | protein_coding |
| Also known as | hnRNPH; previously HNRPH1 |
| Gene groups (HGNC) | RNA binding motif containing; Heterogeneous nuclear ribonucleoproteins |
| Reactome | 13 pathways, smallest: FGFR2 alternative splicing; Signaling by FGFR2; Signaling by FGFR |
| Matched by | ensembl_id |

**Function**, from UniProt [P31943](https://www.uniprot.org/uniprotkb/P31943) (Heterogeneous nuclear ribonucleoprotein H):

> This protein is a component of the heterogeneous nuclear ribonucleoprotein (hnRNP) complexes which provide the substrate for the processing events that pre-mRNAs undergo before becoming functional, translatable mRNAs in the cytoplasm. Mediates pre-mRNA alternative splicing regulation. Inhibits, together with CUGBP1, insulin receptor (IR) pre-mRNA exon 11 inclusion in myoblast. Binds to the IR RNA. Binds poly(RG).

**Summary**, from NCBI Gene [3187](https://www.ncbi.nlm.nih.gov/gene/3187):

> This gene encodes a member of a subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA binding proteins that complex with heterogeneous nuclear RNA. These proteins are associated with pre-mRNAs in the nucleus and appear to influence pre-mRNA processing and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present in the nucleus, some may shuttle between the nucleus and the cytoplasm. The hnRNP proteins have distinct …

**Accessions** — [HGNC:5041](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5041) · Entrez [3187](https://www.ncbi.nlm.nih.gov/gene/3187) · UniProt [P31943](https://www.uniprot.org/uniprotkb/P31943) · Ensembl [ENSG00000169045](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169045)

## Data

Gene col 9743: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9743); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9743, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9743]; `tensor/DDL_lfc|DDL_z.npy` [9743]; `embed/gene_vectors.npy` [9743]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9743 or target_col == 9743). Every well: [[HNRNPH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HNRNPH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
