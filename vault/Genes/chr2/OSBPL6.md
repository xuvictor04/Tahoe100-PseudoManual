---
symbol: "OSBPL6"
type: "gene"
col: 1243
ensembl_id: "ENSG00000079156"
name: "oxysterol binding protein like 6"
location: "2q31.2"
module: 95
arm: "-"
pooled_cpm: 40.91
n_lines_expressing: 38
n_dd_up: 27
n_dd_down: 14
n_dd_up_clean: 20
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 9
tags: ["gene", "module/095"]
generated_by: "tahoemap"
---

# OSBPL6

*oxysterol binding protein like 6* — 2q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.69× (z +26.6, q 0e+00, up in 34 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.555× (z -12.0, q 3e-30, down in 23 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 0.749× (z -8.3, q 1e-14, down in 20 of 36 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OSTF1]] (+0.60, fdr 3e-05), [[KHDRBS3]] (+0.59, fdr 1e-05), [[FYN]] (+0.58, fdr 5e-05); moves opposite to [[RBM48]] (-0.56, fdr 3e-04), [[WDR73]] (-0.55, fdr 8e-05), [[AHI1-DT]] (-0.54, fdr 1e-04).
> It sits in the **-** arm of [[Module 095]] (Chromatin organization).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[KCNG1]] → it (grade B ⚠); 9 go from it, the strongest it → [[KCNG1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1243.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.69×** | +26.6 | 0e+00 | 34/36 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.46×** | +25.3 | 0e+00 | 33/35 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.30×** | +24.3 | 0e+00 | 34/36 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.16×** | +22.2 | 0e+00 | 32/36 (SW1417, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.84×** | +21.3 | 0e+00 | 35/36 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.04×** | +14.5 | 1e-45 | 33/35 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.94×** | +13.5 | 2e-39 | 30/35 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.50×** | +11.6 | 2e-29 | 21/36 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **3.32×** | +10.3 | 7e-23 | 31/36 (PANC-1, SW1417, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.65×** | +10.2 | 1e-22 | 26/35 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.36×** | +8.9 | 4e-17 | 19/36 (A498, LoVo, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **2.10×** | +6.3 | 1e-08 | 24/35 (SW480, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.23×** | +5.9 | 1e-07 | 19/36 (NCI-H2030, C-33 A, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.33×** | +5.8 | 2e-07 | 17/35 (SW 900, A498, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.34×** | +5.8 | 2e-07 | 21/35 (A498, A-172, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.30×** | +5.4 | 2e-06 | 18/35 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.29×** | +5.2 | 6e-06 | 16/35 (LOX-IMVI, NCI-H23, …) | top dose only |  |
| [[Neratinib (drug)]] 5 µM |  | **1.29×** | +5.1 | 8e-06 | 15/35 (NCI-H460, NCI-H2030, …) | rises with dose |  |
| [[Brivudine (drug)]] 0.5 µM |  | **1.33×** | +4.2 | 8e-04 | 11/36 (SW480, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1243.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.555×** | -12.0 | 3e-30 | 23/35 (J82, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.556×** | -11.5 | 6e-28 | 19/30 (A-172, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.555×** | -11.1 | 3e-26 | 21/33 (NCI-H1792, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.749×** | -8.3 | 1e-14 | 20/36 (A498, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.382×** | -8.2 | 2e-14 | 24/37 (A-172, J82, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.691×** | -7.5 | 6e-12 | 21/36 (LOX-IMVI, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~25% of this change | **0.734×** | -6.3 | 3e-08 | 20/35 (hTERT-HPNE, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.917× | -5.9 | 3e-07 | 3/37 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.593×** | -4.5 | 5e-04 | 12/28 (LOX-IMVI, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **0.813×** | -4.2 | 0.002 | 13/36 (HOP62, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.815×** | -4.1 | 0.002 | 13/36 (NCI-H460, A-172, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.755×** | -4.1 | 0.002 | 12/34 (CHP-212, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.623×** | -4.0 | 0.002 | 12/34 (J82, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.642×** | -3.8 | 0.006 | 12/35 (HS-578T, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.839× | -3.5 | 0.015 | 16/35 (J82, A-172, …) | all doses, flat |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.784×** | -3.5 | 0.015 | 8/35 (HOP62, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.891× | -3.3 | 0.032 | 13/36 (HOP62, A-172, …) | top dose only |  |
| [[Sulfatinib (drug)]] 5 µM |  | 0.852× | -3.1 | 0.055 | 8/35 (J82, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.55 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1243. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 75.1 | 5 | 6 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.93× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.0436× (z -32.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.513× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 63.7 | 9 (2 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.74× (z +14.6) | [[Selinexor (drug)]] 5 µM 0.584× (z -8.5) |
| [[A498 (line)]] | wt | 37.7 | 8 (3 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 6.00× (z +15.8) | [[Selinexor (drug)]] 5 µM 0.408× (z -11.3) |
| [[SW480 (line)]] | alt | 43.4 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +16.3) | — |
| [[A-427 (line)]] | wt | 55.7 | 5 | 3 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.35× (z +10.6) | [[Dinaciclib (drug)]] 0.05 µM 0.160× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.455× (z -9.7) |
| [[LoVo (line)]] | wt | 20.9 | 8 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 8.87× (z +15.9) | — |
| [[LOX-IMVI (line)]] | wt | 58.2 | 6 | 2 (1 ⚠) | [[Belinostat (drug)]] 5 µM 5.00× (z +15.8) | [[Selinexor (drug)]] 5 µM 0.450× (z -11.2) |
| [[SW1417 (line)]] | alt | 50.9 | 7 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.68× (z +17.6) | [[Dinaciclib (drug)]] 5 µM 0.307× (z -10.9) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 225 | 1 | 6 (2 ⚠) | [[Pentamidine (isethionate) (drug)]] 5 µM 1.88× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.248× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.418× (z -13.1) |
| [[PANC-1 (line)]] | alt | 18.4 | 6 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 8.77× (z +18.2) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.358× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 16.0 | 6 | 0 | [[Tucidinostat (drug)]] 5 µM 5.37× (z +14.8) | — |
| [[J82 (line)]] | alt | 94.4 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.221× (z -17.3) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 16.2 | 6 | 0 | [[Tucidinostat (drug)]] 5 µM 6.30× (z +15.9) | — |
| [[NCI-H23 (line)]] | alt | 48.5 | 6 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.60× (z +13.0) | — |
| [[Panc 03.27 (line)]] | alt | 12.6 | 5 | 1 | [[Belinostat (drug)]] 5 µM 8.47× (z +10.5) | [[Temsirolimus (drug)]] 0.5 µM 0.146× (z -9.4) |
| [[SK-MEL-2 (line)]] | alt | 44.5 | 6 | 0 | [[Tucidinostat (drug)]] 5 µM 3.02× (z +11.9) | — |
| [[SW 900 (line)]] | alt | 28.8 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.44× (z +12.6) | — |
| [[C32 (line)]] | wt | 49.1 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +10.3) | [[Selinexor (drug)]] 5 µM 0.362× (z -9.7) |
| [[hTERT-HPNE (line)]] | wt | 53.4 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +13.6) | [[Docetaxel (drug)]] 0.05 µM 0.208× (z -10.4) ⚠ transcription drop; cell-cycle shift, explains ~25% of this change |
| [[NCI-H2030 (line)]] | alt | 27.5 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 10.4× (z +16.8) | — |
| [[RPMI-7951 (line)]] | alt | 99.1 | 4 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.93× (z +10.6) | [[Docetaxel (drug)]] 0.05 µM 0.385× (z -9.5) ⚠ transcription drop; cell-cycle shift, explains ~25% of this change |
| [[A549 (line)]] | wt | 20.3 | 4 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 6.24× (z +11.0) | — |
| [[HS-578T (line)]] | alt | 58.1 | 0 | 4 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.281× (z -11.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 70.0 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.172× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.497× (z -9.5) |
| [[C-33 A (line)]] | alt | 95.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.126× (z -16.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 53.8 | 1 | 2 (2 ⚠) | [[Belinostat (drug)]] 5 µM 2.60× (z +9.1) | [[Digitoxin (drug)]] 5 µM 0.338× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 42.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.76× (z +10.8) | — |
| [[AN3 CA (line)]] | alt | 86.2 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0989× (z -12.5) |
| [[H4 (line)]] | wt | 41.5 | 2 | 0 | [[Belinostat (drug)]] 5 µM 6.00× (z +9.3) | — |
| [[CHP-212 (line)]] | wt | 36.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -10.4) |
| [[HCT15 (line)]] | alt | 34.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.97× (z +8.5) | — |
| [[SHP-77 (line)]] | alt | 100 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.365× (z -10.8) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 103 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.135× (z -8.6) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 7.74 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 10.1 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 7.96 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.33 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.58 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.41 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.30 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.0 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 10.1 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.88 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 177 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.54 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.39 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 47.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1243), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OSTF1]] | +0.60 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[KHDRBS3]] | +0.59 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[FYN]] | +0.58 | +0.39 / +0.59 | both halves | 5e-05 |  |
| [[C1orf21]] | +0.58 | +0.34 / +0.47 | both halves | 1e-04 |  |
| [[APBB2]] | +0.58 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[INPP5F]] | +0.57 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[EIF4EBP1]] | +0.57 | +0.35 / +0.39 | both halves | 1e-04 |  |
| [[WDFY2]] | +0.56 | +0.33 / +0.46 | both halves | 1e-04 |  |
| [[WASF3]] | +0.56 | +0.36 / +0.55 | both halves | 9e-05 |  |
| [[GPT2]] | +0.56 | +0.40 / +0.45 | both halves | 5e-05 |  |
| [[GALNT12]] | +0.55 | +0.35 / +0.40 | both halves | 1e-04 |  |
| [[TOX2]] | +0.54 | +0.42 / +0.47 | both halves | 4e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM48]] | -0.56 | -0.27 / -0.54 | both halves | 3e-04 |  |
| [[WDR73]] | -0.55 | -0.37 / -0.39 | both halves | 8e-05 |  |
| [[AHI1-DT]] | -0.54 | -0.34 / -0.38 | both halves | 1e-04 |  |
| [[CDKL3]] | -0.52 | -0.28 / -0.32 | both halves | 3e-04 |  |
| [[ATP6V1C1]] | -0.52 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[MED28]] | -0.51 | -0.38 / -0.42 | both halves | 7e-05 |  |
| [[AEBP2]] | -0.51 | -0.28 / -0.40 | both halves | 3e-04 |  |
| [[ENTPD3-AS1]] | -0.50 | -0.28 / -0.33 | both halves | 3e-04 |  |
| [[HNRNPH2]] | -0.49 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[THBS4]] | -0.49 | -0.22 / -0.38 | both halves | 6e-04 |  |
| [[C5orf15]] | -0.49 | -0.35 / -0.36 | both halves | 1e-04 |  |
| [[LINC01134]] | -0.49 | -0.10 / -0.46 | ⚠ not reproduced | 0.003 |  |
| [[DAZAP2]] | -0.48 | -0.22 / -0.50 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNG1]] | B | KCNG1 activity raises OSBPL6's level | lines that do not express KCNG1 (18) vs lines expressing it (32) | 3.25× lower at baseline in the lines without KCNG1 | 0.029 | ⚠ within organs, on part of the lines; also absent: AOX1, RASSF8, MSRB3 |
| [[FYN]] | B | FYN activity raises OSBPL6's level | lines that do not express FYN (8) vs lines expressing it (42) | 2.51× lower at baseline in the lines without FYN | 0.050 | ⚠ within organs, on part of the lines; also absent: RHOBTB3; maybe low, not absent |
| [[CLTCL1]] | C | CLTCL1 activity raises OSBPL6's level | lines that do not express CLTCL1 (3) vs lines expressing it (47) | 6.90× lower at baseline in the lines without CLTCL1 | 0.052 | ⚠ few lines (3 vs 47); across organs; also absent: NKAIN1, WHRN, SUGCT |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNG1]] | B | OSBPL6 activity raises KCNG1's level | lines that do not express OSBPL6 (12) vs lines expressing it (38) | 2.61× lower at baseline in the lines without OSBPL6 | 0.012 | ⚠ within organs, on part of the lines; also absent: RECK, LHFPL6, GLIPR2; maybe low, not absent |
| [[TTLL7]] | B | OSBPL6 activity raises TTLL7's level | lines that do not express OSBPL6 (12) vs lines expressing it (38) | 4.52× lower at baseline in the lines without OSBPL6 | 0.013 | ⚠ within organs, on part of the lines; also absent: RECK, LHFPL6, GLIPR2; maybe low, not absent |
| [[CLTCL1]] | B | OSBPL6 activity raises CLTCL1's level | lines that do not express OSBPL6 (12) vs lines expressing it (38) | 1.91× lower at baseline in the lines without OSBPL6 | 0.037 | ⚠ within organs, on part of the lines; also absent: RECK, LHFPL6, GLIPR2; maybe low, not absent |
| [[TOX2]] | B | OSBPL6 activity raises TOX2's level | lines that do not express OSBPL6 (12) vs lines expressing it (38) | 2.87× lower at baseline in the lines without OSBPL6 | 0.071 | ⚠ within organs, on part of the lines; also absent: RECK, LHFPL6, GLIPR2; maybe low, not absent |
| [[APBB2]] | B | OSBPL6 activity raises APBB2's level | lines that do not express OSBPL6 (12) vs lines expressing it (38) | 1.68× lower at baseline in the lines without OSBPL6 | 0.078 | ⚠ within organs, on part of the lines; also absent: RECK, LHFPL6, GLIPR2; maybe low, not absent |
| [[SH3PXD2B]] | B | OSBPL6 activity raises SH3PXD2B's level | lines that do not express OSBPL6 (12) vs lines expressing it (38) | 2.17× lower at baseline in the lines without OSBPL6 | 0.090 | ⚠ within organs, on part of the lines; also absent: RECK, LHFPL6, GLIPR2; maybe low, not absent |
| cells under [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM | B | OSBPL6 activity raises the cells' numbers under Sivelestat (sodium tetrahydrate) 5 µM (protects the cells) | lines that do not express OSBPL6 (12) vs lines expressing it (36) | the lines without OSBPL6: 0.87× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: RECK, LHFPL6, GLIPR2; maybe low, not absent |
| cells under [[Ixazomib (drug)]] 0.05 µM | B | OSBPL6 activity lowers the cells' numbers under Ixazomib 0.05 µM (makes them more sensitive) | lines that do not express OSBPL6 (12) vs lines expressing it (36) | the lines without OSBPL6: 1.22× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; also absent: RECK, LHFPL6, GLIPR2; maybe low, not absent |
| [[JAZF1]] | C | OSBPL6 activity raises JAZF1's level | lines that do not express OSBPL6 (12) vs lines expressing it (38) | 2.91× lower at baseline in the lines without OSBPL6 | 0.046 | ⚠ within organs, on part of the lines; also absent: RECK, LHFPL6, GLIPR2; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 095]] — Chromatin organization; 48 genes; this gene is in the **-** arm (projection on the module's main direction -0.492). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.36).
- **Nodal map** (x, y) = (36.7, 6.5); signed map (-2.4, 50.7). **Vector** length 105, 26.7% of its response variance represented; |z| ≥ 3 in 1,180 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.4 | +22.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.8 | +13.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.4 | +21.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.4 | +10.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.4 | +10.3 |
|  | [[Neratinib (drug)]] 5 µM |  | +2.9 | +5.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.7 | +1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.7 | +0.2 |
| fall | [[Selinexor (drug)]] 5 µM |  | -7.2 | -8.3 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -5.4 | -7.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.8 | -8.2 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.7 | -2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.6 | -3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -4.1 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -2.7 | -1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | -3.3 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -2.2 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | oxysterol binding protein like 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.2 — chr2:178,194,481-178,402,893 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ORP6 |
| Gene groups (HGNC) | Oxysterol binding proteins |
| Reactome | 4 pathways, smallest: Synthesis of bile acids and bile salts; Bile acid and bile salt metabolism; Metabolism of steroids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BZF3](https://www.uniprot.org/uniprotkb/Q9BZF3) (Oxysterol-binding protein-related protein 6):

> Regulates cellular transport and efflux of cholesterol. Plays a role in phosphatidylinositol-4-phosphate (PI4P) turnover at the neuronal membrane. Localizes at the neurons plasma membrane-endoplasmic reticulum contact sites, and exchanges phosphatidylserine (1,2-diacyl-sn-glycero-3-phospho-L-serine, PS) from the endoplasmic reticulum for phosphatidylinositol-4-phosphate (1,2-diacyl-sn-glycero-3-phospho-(1D-myo-inositol 4-phosphate), PI(4)P) from the plasma membrane (By similarity). Binds via …

**Summary**, from NCBI Gene [114880](https://www.ncbi.nlm.nih.gov/gene/114880):

> This gene encodes a member of the oxysterol-binding protein (OSBP) family, a group of intracellular lipid receptors. Most members contain an N-terminal pleckstrin homology domain and a highly conserved C-terminal OSBP-like sterol-binding domain. Transcript variants encoding different isoforms have been identified. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:16388](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16388) · Entrez [114880](https://www.ncbi.nlm.nih.gov/gene/114880) · UniProt [Q9BZF3](https://www.uniprot.org/uniprotkb/Q9BZF3) · Ensembl [ENSG00000079156](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000079156)

## Data

Gene col 1243: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1243); `tables/drug_effects.parquet` (61 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1243, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1243]; `tensor/DDL_lfc|DDL_z.npy` [1243]; `embed/gene_vectors.npy` [1243]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1243 or target_col == 1243). Every well: [[OSBPL6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OSBPL6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
