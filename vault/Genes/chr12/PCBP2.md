---
symbol: "PCBP2"
type: "gene"
col: 12343
ensembl_id: "ENSG00000197111"
name: "poly(rC) binding protein 2"
location: "12q13.13"
module: 43
arm: "+"
pooled_cpm: 458.73
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 1
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# PCBP2

*poly(rC) binding protein 2* — 12q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.19× (z +16.6, q 0e+00, up in 48 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.44× (z +7.7, q 1e-12, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Ribociclib (drug)]] 0.05 µM: 0.823× (z -4.1, q 0.021, down in 27 of 49 measured lines) ⚠ unreliable plate only; position not correctable.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.568×; ⚠ toxic; cell-cycle shift, explains ~57% of this change).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CSDE1]] (+0.75, fdr 7e-06), [[HNRNPA1]] (+0.69, fdr 7e-06), [[NPM1]] (+0.68, fdr 7e-06); moves opposite to [[TRAPPC4]] (-0.60, fdr 2e-05), [[POLR3K]] (-0.59, fdr 5e-05), [[ORAI1]] (-0.57, fdr 5e-05).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12343.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.19×** | +16.6 | 0e+00 | 48/49 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.23×** | +16.2 | 0e+00 | 43/44 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.71×** | +10.5 | 2e-23 | 43/45 (C-33 A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.34×** | +8.7 | 4e-16 | 31/48 (A498, COLO 205, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.44×** | +7.7 | 1e-12 | 36/48 (KATO III, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~17% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.92×** | +7.2 | 7e-11 | 46/49 (AsPC-1, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.72×** | +6.0 | 2e-07 | 37/48 (KATO III, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.31×** | +5.7 | 7e-07 | 38/48 (RPMI-7951, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.29×** | +5.2 | 1e-05 | 32/47 (COLO 205, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +5.0 | 3e-05 | 30/50 (MIA PaCa-2, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.50×** | +4.4 | 4e-04 | 42/47 (KATO III, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.9 | 0.004 | 20/49 (NCI-H2347, AsPC-1, …) | top dose only |  |
| [[Ixazomib (drug)]] 5 µM |  | **1.42×** | +3.8 | 0.005 | 37/48 (KATO III, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +3.8 | 0.005 | 33/48 (RPMI-7951, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | 1.19× | +3.4 | 0.025 | 17/48 (LS 180, SK-MEL-2, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.05 µM |  | 1.17× | +3.0 | 0.092 | 15/48 (A-427, SK-MEL-2, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12343.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.568×; ⚠ toxic; cell-cycle shift, explains ~57% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.823×** | -4.1 | 0.021 | 27/49 (NCI-H2347, SW480, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 0.843× | -3.6 | 0.080 | 19/48 (A-427, SK-MEL-2, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12343. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 526 | 8 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +15.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.68× (z +15.2) | — |
| [[AsPC-1 (line)]] | alt | 486 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +18.3) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.24× (z +9.8) | — |
| [[LoVo (line)]] | wt | 621 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.84× (z +20.2) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 2.56× (z +9.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 401 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.17× (z +16.2) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +11.4) | — |
| [[KATO III (line)]] | alt | 431 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +19.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.54× (z +16.9) | — |
| [[NCI-H1573 (line)]] | alt | 484 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +14.9) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.67× (z +9.0) | — |
| [[A498 (line)]] | wt | 313 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +21.6) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[COLO 205 (line)]] | alt | 301 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +20.8) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.49× (z +9.0) | — |
| [[HEC-1-A (line)]] | alt | 390 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.53× (z +15.9) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 1.69× (z +8.6) | — |
| [[HOP62 (line)]] | alt | 346 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.86× (z +13.6) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 392 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.30× (z +12.4) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 415 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.64× (z +16.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.79× (z +9.8) | — |
| [[NCI-H1792 (line)]] | alt | 1,180 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +14.4) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 581 | 3 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.13× (z +12.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.73× (z +9.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.568× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~57% of this change |
| [[PANC-1 (line)]] | alt | 416 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.67× (z +17.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.68× (z +9.1) | — |
| [[RPMI-7951 (line)]] | alt | 342 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.34× (z +12.1) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 1.89× (z +9.4) | — |
| [[SW480 (line)]] | alt | 623 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.44× (z +17.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.61× (z +9.5) | — |
| [[A-172 (line)]] | wt | 270 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.89× (z +15.6) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 740 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.36× (z +15.7) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 468 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.63× (z +11.5) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 415 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +15.3) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 291 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +12.8) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[Hs 766T (line)]] | wt | 274 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.41× (z +11.3) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 408 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.24× (z +14.8) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 412 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +13.4) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[LOX-IMVI (line)]] | wt | 462 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.28× (z +13.6) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 567 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.28× (z +13.5) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 381 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.08× (z +11.1) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 460 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.19× (z +11.4) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 506 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.83× (z +13.8) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 446 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.93× (z +9.5) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 521 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.18× (z +9.5) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 516 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.02× (z +11.2) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 277 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.72× (z +11.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 481 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +9.8) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[RKO (line)]] | wt | 374 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.35× (z +13.2) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 1.77× (z +8.5) | — |
| [[SHP-77 (line)]] | alt | 297 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.77× (z +14.6) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 474 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.51× (z +11.4) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 329 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 2.84× (z +8.5) | — |
| [[H4 (line)]] | wt | 366 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +12.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 495 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.76× (z +12.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 379 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.70× (z +9.4) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 458 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +13.9) ⚠ toxic; transcription drop | — |
| [[SW 1271 (line)]] | alt | 386 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +9.7) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[SW1417 (line)]] | alt | 439 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.95× (z +11.1) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 672 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 433 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 467 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 487 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 347 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12343), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSDE1]] | +0.75 | +0.68 / +0.72 | both halves | 7e-06 | STRING 644 |
| [[HNRNPA1]] | +0.69 | +0.64 / +0.75 | both halves | 7e-06 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 940 |
| [[NPM1]] | +0.68 | +0.67 / +0.69 | both halves | 7e-06 | pathway: SARS-CoV-1 Infection |
| [[EEF1A1]] | +0.67 | +0.61 / +0.69 | both halves | 7e-06 | pathway: SARS-CoV-1 Infection; STRING 490 |
| [[EEF2]] | +0.63 | +0.68 / +0.66 | both halves | 7e-06 | STRING 587 |
| [[KIAA1191]] | +0.62 | +0.72 / +0.58 | both halves | 7e-06 |  |
| [[RBM3]] | +0.62 | +0.54 / +0.58 | both halves | 1e-05 | STRING 539 |
| [[RPL10]] | +0.62 | +0.43 / +0.70 | both halves | 3e-05 |  |
| [[CNOT1]] | +0.61 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[RPL14]] | +0.61 | +0.51 / +0.69 | both halves | 1e-05 |  |
| [[PABPC1]] | +0.61 | +0.51 / +0.75 | both halves | 1e-05 | STRING 922 |
| [[PAPOLA]] | +0.60 | +0.59 / +0.62 | both halves | 7e-06 | pathway: Dengue Virus-Host Interactions; STRING 480 |

## Genes that move opposite

*29 of its nearest partners move opposite, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAPPC4]] | -0.60 | -0.48 / -0.67 | both halves | 2e-05 |  |
| [[POLR3K]] | -0.59 | -0.40 / -0.61 | both halves | 5e-05 |  |
| [[ORAI1]] | -0.57 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[MRPL36]] | -0.56 | -0.36 / -0.59 | both halves | 1e-04 |  |
| [[MTMR9]] | -0.55 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[EXOSC4]] | -0.55 | -0.31 / -0.58 | both halves | 2e-04 |  |
| [[POP7]] | -0.53 | -0.40 / -0.56 | both halves | 5e-05 |  |
| [[MRPL12]] | -0.52 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[C16orf91]] | -0.52 | -0.20 / -0.60 | ⚠ one half (not replicated) | 8e-04 |  |
| [[RPUSD2]] | -0.51 | -0.31 / -0.52 | both halves | 2e-04 |  |
| [[HAUS7]] | -0.51 | -0.29 / -0.61 | both halves | 3e-04 |  |
| [[EMC6]] | -0.51 | -0.30 / -0.55 | both halves | 2e-04 |  |
| [[DHRS7B]] | -0.51 | -0.26 / -0.59 | both halves | 4e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.190). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-30.3, -25.5); signed map (-22.6, -33.3). **Vector** length 117, 41.3% of its response variance represented; |z| ≥ 3 in 882 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +16.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.6 | +16.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +10.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +4.2 | +1.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +2.1 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +3.9 | +0.9 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | +2.9 | +1.7 |
|  | [[Sapanisertib (drug)]] 5 µM |  | +2.8 | +0.1 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -8.6 | -1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.7 | -1.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~57% of this change | -5.6 | -2.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.6 | +1.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.6 | +2.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -5.1 | -2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | +0.4 |
|  | [[vincristine (drug)]] 0.5 µM |  | -2.5 | +0.6 |
|  | [[vincristine (drug)]] 5 µM |  | -2.2 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | poly(rC) binding protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.13 — chr12:53,452,102-53,481,162 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HNRPE2, hnRNP-E2, HNRNPE2 |
| Gene groups (HGNC) | Heterogeneous nuclear ribonucleoproteins |
| Reactome | 16 pathways, smallest: Negative regulators of DDX58/IFIH1 signaling; SARS-CoV-1 activates/modulates innate immune responses; DDX58/IFIH1-mediated induction of interferon-alpha/beta |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15366](https://www.uniprot.org/uniprotkb/Q15366) (Poly(rC)-binding protein 2):

> Single-stranded nucleic acid binding protein that binds preferentially to oligo dC. Major cellular poly(rC)-binding protein. Also binds poly(rU). Acts as a negative regulator of antiviral signaling. Negatively regulates cellular antiviral responses mediated by MAVS signaling. It acts as an adapter between MAVS and the E3 ubiquitin ligase ITCH, therefore triggering MAVS ubiquitination and degradation. Negativeley regulates the cGAS-STING pathway via interaction with CGAS, preventing the …

**Summary**, from NCBI Gene [5094](https://www.ncbi.nlm.nih.gov/gene/5094):

> The protein encoded by this gene appears to be multifunctional. Along with PCBP-1 and hnRNPK, it is one of the major cellular poly(rC)-binding proteins. The encoded protein contains three K-homologous (KH) domains which may be involved in RNA binding. Together with PCBP-1, this protein also functions as a translational coactivator of poliovirus RNA via a sequence-specific interaction with stem-loop IV of the IRES, promoting poliovirus RNA replication by binding to its 5'-terminal cloverleaf …

**Accessions** — [HGNC:8648](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8648) · Entrez [5094](https://www.ncbi.nlm.nih.gov/gene/5094) · UniProt [Q15366](https://www.uniprot.org/uniprotkb/Q15366) · Ensembl [ENSG00000197111](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197111)

## Data

Gene col 12343: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12343); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12343, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12343]; `tensor/DDL_lfc|DDL_z.npy` [12343]; `embed/gene_vectors.npy` [12343]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12343 or target_col == 12343). Every well: [[PCBP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCBP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
