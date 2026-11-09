---
symbol: "IL6ST"
type: "gene"
col: 5553
ensembl_id: "ENSG00000134352"
name: "interleukin 6 cytokine family signal transducer"
location: "5q11.2"
module: 3
arm: "-"
pooled_cpm: 250.76
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 10
n_dd_up_clean: 13
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# IL6ST

*interleukin 6 cytokine family signal transducer* — 5q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.92× (z +34.8, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.918× (z -5.1, q 2e-04, down in 3 of 50 measured lines) ⚠ position not correctable. The strongest without an alert is [[Tofacitinib (citrate) (drug)]] 5 µM: 0.830× (z -4.7, q 4e-04, down in 22 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIP12]] (+0.73, fdr 7e-06), [[NCOA4]] (+0.70, fdr 7e-06), [[LEPROT]] (+0.69, fdr 7e-06); moves opposite to [[SDHAP2]] (-0.72, fdr 7e-06), [[SCAI]] (-0.66, fdr 7e-06), [[SDHAP1]] (-0.65, fdr 1e-05).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5553.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.92×** | +34.8 | 0e+00 | 48/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.31×** | +20.7 | 0e+00 | 48/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.92×** | +19.3 | 0e+00 | 47/48 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.94×** | +11.9 | 2e-30 | 46/48 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.81×** | +10.3 | 8e-23 | 37/44 (HOP62, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.98×** | +10.2 | 2e-22 | 42/45 (HOP62, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.72×** | +9.7 | 2e-20 | 41/49 (HOP62, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.03×** | +9.4 | 4e-19 | 46/49 (SW480, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.52×** | +7.6 | 2e-12 | 43/48 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.41×** | +6.2 | 3e-08 | 34/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.38×** | +5.8 | 4e-07 | 38/48 (NCI-H460, BT-474, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.30×** | +4.7 | 1e-04 | 25/48 (A498, NCI-H2347, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.20×** | +4.6 | 1e-04 | 22/48 (MIA PaCa-2, HOP62, …) | rises with dose |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | **1.24×** | +3.9 | 0.004 | 30/48 (J82, A-427, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.54×** | +3.7 | 0.009 | 26/48 (HEC-1-A, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.010 | 23/48 (A498, SW 900, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +3.4 | 0.024 | 16/48 (LS 180, A-172, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | 1.18× | +2.9 | 0.091 | 18/48 (A-172, HT-29, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5553.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.918× | -5.1 | 2e-04 | 3/50 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.830×** | -4.7 | 4e-04 | 22/49 (C32, COLO 205, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.664×** | -4.7 | 4e-04 | 38/48 (hTERT-HPNE, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.787×** | -4.3 | 0.002 | 29/48 (RKO, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.788×** | -4.3 | 0.002 | 31/48 (LOX-IMVI, A-427, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | 0.846× | -4.3 | 0.002 | 19/49 (C32, SK-MEL-2, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.812×** | -3.7 | 0.015 | 30/48 (RKO, SNU-423, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.824×** | -3.3 | 0.058 | 25/47 (J82, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.835× | -3.2 | 0.069 | 20/49 (LOX-IMVI, SNU-423, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.829×** | -3.2 | 0.069 | 20/49 (HepG2/C3A, SW 900, …) | top dose only |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **0.760×** | -3.2 | 0.075 | 24/49 (A-427, J82, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.883× | -3.2 | 0.075 | 13/48 (RKO, C32, …) | top dose only |  |
| [[BAY1125976 (drug)]] 0.5 µM |  | **0.766×** | -3.1 | 0.092 | 19/48 (hTERT-HPNE, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.769×** | -3.0 | 0.100 | 21/48 (A-427, HepG2/C3A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5553. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 272 | 24 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +23.8) | — |
| [[HOP62 (line)]] | alt | 122 | 10 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.40× (z +34.4) | — |
| [[LoVo (line)]] | wt | 152 | 10 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.79× (z +38.9) | — |
| [[NCI-H460 (line)]] | wt | 218 | 10 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.15× (z +34.6) | — |
| [[A549 (line)]] | wt | 252 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.42× (z +34.5) | — |
| [[BT-474 (line)]] | alt | 101 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.95× (z +25.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 157 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.34× (z +25.0) | — |
| [[SNU-1 (line)]] | wt | 218 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.41× (z +30.8) | — |
| [[HEC-1-A (line)]] | alt | 177 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.10× (z +33.2) | — |
| [[hTERT-HPNE (line)]] | wt | 321 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.16× (z +23.3) | — |
| [[LS 180 (line)]] | wt | 72.5 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +26.1) | — |
| [[NCI-H2347 (line)]] | alt | 397 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +29.6) | — |
| [[RPMI-7951 (line)]] | alt | 307 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +22.0) | — |
| [[SW48 (line)]] | wt | 93.4 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.73× (z +20.4) | — |
| [[SW480 (line)]] | alt | 158 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.00× (z +30.4) | — |
| [[A-172 (line)]] | wt | 262 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +25.1) | — |
| [[A-427 (line)]] | wt | 330 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +23.2) | — |
| [[J82 (line)]] | alt | 493 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +18.8) | — |
| [[KATO III (line)]] | alt | 107 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +21.2) | — |
| [[NCI-H2030 (line)]] | alt | 211 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +21.7) | — |
| [[PANC-1 (line)]] | alt | 299 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +25.2) | — |
| [[RKO (line)]] | wt | 301 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +19.4) | — |
| [[AsPC-1 (line)]] | alt | 280 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +19.2) | — |
| [[C32 (line)]] | wt | 314 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +20.5) | — |
| [[HS-578T (line)]] | alt | 601 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.42× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.98× (z +8.6) | — |
| [[Panc 03.27 (line)]] | alt | 359 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +24.3) | — |
| [[SK-MEL-2 (line)]] | alt | 199 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +24.5) | — |
| [[CFPAC-1 (line)]] | alt | 345 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +27.3) | — |
| [[HCT15 (line)]] | alt | 200 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.16× (z +21.4) | — |
| [[Hs 766T (line)]] | wt | 243 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.95× (z +26.0) | — |
| [[HT-29 (line)]] | alt | 258 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.12× (z +27.9) | — |
| [[LOX-IMVI (line)]] | wt | 253 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.16× (z +24.0) | — |
| [[NCI-H1573 (line)]] | alt | 102 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.08× (z +26.7) | — |
| [[NCI-H1792 (line)]] | alt | 365 | 2 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.20× (z +12.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 302 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +16.8) | — |
| [[SNU-423 (line)]] | alt | 363 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +23.8) | — |
| [[SW 900 (line)]] | alt | 457 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +20.2) | — |
| [[SW1417 (line)]] | alt | 120 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +25.7) | — |
| [[AN3 CA (line)]] | alt | 293 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.59× (z +11.2) | — |
| [[C-33 A (line)]] | alt | 143 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.79× (z +11.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.87× (z +9.5) | — |
| [[COLO 205 (line)]] | alt | 197 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +11.9) | — |
| [[H4 (line)]] | wt | 378 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +14.6) | — |
| [[HepG2_C3A (line)]] | wt | 266 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +16.4) | — |
| [[CHP-212 (line)]] | wt | 206 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +13.0) | — |
| [[SHP-77 (line)]] | alt | 125 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.78× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW 1088 (line)]] | alt | 513 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +10.0) | — |
| [[SW 1271 (line)]] | alt | 382 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +13.4) | — |
| [[NCI-H2122 (line)]] | alt | 226 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 205 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 196 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5553), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*40 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIP12]] | +0.73 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[NCOA4]] | +0.70 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[LEPROT]] | +0.69 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[HNRNPK]] | +0.68 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[ZNF655]] | +0.68 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[CFLAR]] | +0.65 | +0.61 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[THBS1]] | +0.63 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[YWHAE]] | +0.63 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[TUG1]] | +0.63 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[PRKAR1A]] | +0.62 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[PARVA]] | +0.62 | +0.48 / +0.57 | both halves | 2e-05 | pathway: Cell junction organization |
| [[EIF4G2]] | +0.62 | +0.54 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*60 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAP2]] | -0.72 | -0.65 / -0.67 | both halves | 7e-06 |  |
| [[SCAI]] | -0.66 | -0.58 / -0.62 | both halves | 7e-06 |  |
| [[SDHAP1]] | -0.65 | -0.64 / -0.56 | both halves | 1e-05 |  |
| [[PTMAP2]] ⚠ | -0.65 | -0.53 / -0.63 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MPG]] | -0.64 | -0.48 / -0.65 | both halves | 2e-05 |  |
| [[ATP5MJ]] | -0.63 | -0.46 / -0.61 | both halves | 3e-05 |  |
| [[ANKS3]] | -0.63 | -0.48 / -0.63 | both halves | 2e-05 |  |
| [[MRPL34]] | -0.62 | -0.47 / -0.62 | both halves | 2e-05 |  |
| [[ELP2]] | -0.61 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[SDHAP4-1]] | -0.61 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[SNHG19]] | -0.61 | -0.38 / -0.63 | both halves | 7e-05 |  |
| [[CAMLG]] | -0.61 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[POP7]] | -0.61 | -0.32 / -0.60 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.707). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-10.3, 1.0); signed map (16.8, -32.6). **Vector** length 152, 54.7% of its response variance represented; |z| ≥ 3 in 1,493 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +11.3 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +10.5 | +9.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +10.4 | +10.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +9.8 | +11.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +9.1 | +20.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.8 | +4.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.5 | +6.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +4.7 | +3.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.7 | +2.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +4.6 | +4.7 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -6.3 | -4.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -5.5 | -4.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.7 | -3.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | -0.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -2.2 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -4.5 | -4.7 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -4.1 | -3.0 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -3.9 | -4.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.8 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | interleukin 6 cytokine family signal transducer |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q11.2 — chr5:55,935,095-55,995,022 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GP130, CD130, sGP130, IL-6RB |
| Gene groups (HGNC) | CD molecules; Fibronectin type III domain containing; Interleukin receptors |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING, UV_RESPONSE_UP, ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 18 pathways, smallest: MAPK1 (ERK2) activation; Interleukin-27 signaling; MAPK3 (ERK1) activation |
| Matched by | ensembl_id |

**Function**, from UniProt [P40189](https://www.uniprot.org/uniprotkb/P40189) (Interleukin-6 receptor subunit beta):

> Functions as a shared signal-transducing subunit not only for IL6 but also for other cytokine receptor complexes, including IL6, LIF, OSM, CNTF, IL11, CTF1, BSF3, MT-RNR2/humanin, CLCF1 and the heterodimeric complex CRLF1-CLCF1. Engages site 2 of CNTF, CLCF1, LIF, and IL-6, and site 3 of IL27 and IL6. Initiates signal transmission through three mechanisms. Binding of cytokines, such as IL6 or IL11 to the alpha-chains of their specific cell surface receptor triggers homodimerization of …

**Summary**, from NCBI Gene [3572](https://www.ncbi.nlm.nih.gov/gene/3572):

> The protein encoded by this gene is a signal transducer shared by many cytokines, including interleukin 6 (IL6), ciliary neurotrophic factor (CNTF), leukemia inhibitory factor (LIF), and oncostatin M (OSM). This protein functions as a part of the cytokine receptor complex. The activation of this protein is dependent upon the binding of cytokines to their receptors. vIL6, a protein related to IL6 and encoded by the Kaposi sarcoma-associated herpesvirus, can bypass the interleukin 6 receptor …

**Accessions** — [HGNC:6021](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6021) · Entrez [3572](https://www.ncbi.nlm.nih.gov/gene/3572) · UniProt [P40189](https://www.uniprot.org/uniprotkb/P40189) · Ensembl [ENSG00000134352](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134352)

## Data

Gene col 5553: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5553); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5553, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5553]; `tensor/DDL_lfc|DDL_z.npy` [5553]; `embed/gene_vectors.npy` [5553]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5553 or target_col == 5553). Every well: [[IL6ST — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IL6ST.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
