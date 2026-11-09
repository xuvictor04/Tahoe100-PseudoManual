---
symbol: "NUP35"
type: "gene"
col: 8616
ensembl_id: "ENSG00000163002"
name: "nucleoporin 35"
location: "2q32.1"
module: 33
arm: "+"
pooled_cpm: 37.15
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 4
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# NUP35

*nucleoporin 35* — 2q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 3.38× (z +9.6, q 4e-19, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.515× (z -9.6, q 4e-19, down in 34 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.752× (z -4.3, q 0.002, down in 24 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (SHP-77 0.0756×, Panc 03.27 0.113×, NCI-H2347 0.198×, SW480 0.385×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (NCI-H2030 0.161×, SK-MEL-2 0.220×, H4 0.0884×, A549 0.228×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (H4 0.0827×, SW1417 0.277×, A-427 0.283×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 3 lines (SK-MEL-2 0.328×, A-427 0.324×, SW480 0.487×); [[Fluvoxamine (maleate) (drug)]] 0.5 µM in 1 line (NCI-H661 0.0559×); [[Darinaparsin (drug)]] 0.05 µM in 1 line (SW 1271 0.0583×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ELP3]] (+0.61, fdr 7e-06), [[WDR75]] (+0.60, fdr 2e-05), [[PDSS1]] (+0.60, fdr 7e-06); moves opposite to [[MALAT1]] (-0.55, fdr 5e-05), [[SPTAN1]] (-0.50, fdr 3e-05), [[GDI1]] (-0.50, fdr 3e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8616.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **3.38×** | +9.6 | 4e-19 | 43/48 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.90×** | +8.4 | 1e-14 | 42/48 (LoVo, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.51×** | +8.3 | 1e-14 | 31/48 (A549, PANC-1, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.78×** | +8.3 | 1e-14 | 39/48 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.66×** | +7.6 | 3e-12 | 32/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.60×** | +7.1 | 1e-10 | 34/48 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.51×** | +6.2 | 5e-08 | 29/47 (PANC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +5.7 | 7e-07 | 28/47 (LoVo, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.39×** | +5.0 | 3e-05 | 25/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.34×** | +4.4 | 6e-04 | 26/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.34×** | +4.4 | 7e-04 | 25/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.57×** | +3.6 | 0.018 | 14/33 (PANC-1, SW480, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.54×** | +3.4 | 0.027 | 16/48 (NCI-H460, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.36×** | +3.4 | 0.033 | 14/48 (PANC-1, A498, …) | two highest doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.25×** | +3.3 | 0.033 | 14/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM |  | **1.50×** | +3.2 | 0.052 | 10/47 (C32, HCT15, …) | top dose only | cell-cycle shift (explains ~23% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.24×** | +3.1 | 0.065 | 16/47 (SW48, LOX-IMVI, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8616.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (SHP-77 0.0756×, Panc 03.27 0.113×, NCI-H2347 0.198×, SW480 0.385×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (NCI-H2030 0.161×, SK-MEL-2 0.220×, H4 0.0884×, A549 0.228×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (H4 0.0827×, SW1417 0.277×, A-427 0.283×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 3 lines (SK-MEL-2 0.328×, A-427 0.324×, SW480 0.487×); [[Fluvoxamine (maleate) (drug)]] 0.5 µM in 1 line (NCI-H661 0.0559×); [[Darinaparsin (drug)]] 0.05 µM in 1 line (SW 1271 0.0583×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.515×** | -9.6 | 4e-19 | 34/41 (SHP-77, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.533×** | -9.5 | 7e-19 | 31/45 (H4, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.545×** | -8.5 | 5e-15 | 29/44 (NCI-H2030, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.915× | -4.6 | 5e-04 | 2/48 (MIA PaCa-2, SW 1088) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.752×** | -4.3 | 0.002 | 24/48 (SK-MEL-2, A-427, …) | top dose only |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.808× | -3.2 | 0.12 | 15/48 (SW48, HEC-1-A, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 0.814× | -3.1 | 0.15 | 18/46 (Hs 766T, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Entrectinib (drug)]] 5 µM |  | 0.817× | -3.0 | 0.17 | 16/48 (J82, CHP-212, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8616. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 49.7 | 7 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +14.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.94× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.407× (z -8.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 51.2 | 1 | 3 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 3.85× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.385× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.487× (z -9.2) |
| [[A549 (line)]] | wt | 50.4 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +14.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.51× (z +9.8) | [[Dinaciclib (drug)]] 0.05 µM 0.228× (z -10.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 25.3 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.19× (z +9.8) | — |
| [[A-172 (line)]] | wt | 15.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +9.7) ⚠ cell-cycle shift, explains ~30% of this change | [[Dinaciclib (drug)]] 5 µM 0.160× (z -11.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 45.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.283× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.324× (z -9.3) |
| [[H4 (line)]] | wt | 40.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0827× (z -13.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 29.2 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.63× (z +10.6) | — |
| [[NCI-H2030 (line)]] | alt | 54.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +9.4) ⚠ cell-cycle shift, explains ~30% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.161× (z -14.4) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 30.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -13.9) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 93.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0756× (z -22.9) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 54.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.220× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.328× (z -10.0) |
| [[A498 (line)]] | wt | 44.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.329× (z -9.9) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 65.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.132× (z -10.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 45.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.215× (z -11.1) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 15.7 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0909× (z -13.1) ⚠ transcription drop |
| [[hTERT-HPNE (line)]] | wt | 17.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.104× (z -9.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 39.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -8.9) ⚠ cell-cycle shift, explains ~30% of this change |
| [[NCI-H23 (line)]] | alt | 57.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.366× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 30.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +10.0) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H661 (line)]] | alt | 60.4 | 0 | 1 | — | [[Fluvoxamine (maleate) (drug)]] 0.5 µM 0.0559× (z -11.0) |
| [[Panc 03.27 (line)]] | alt | 36.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.113× (z -16.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 36.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +11.9) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[SNU-1 (line)]] | wt | 44.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.185× (z -8.9) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 52.0 | 0 | 1 | — | [[Darinaparsin (drug)]] 0.05 µM 0.0583× (z -8.5) |
| [[SW1417 (line)]] | alt | 39.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.277× (z -11.6) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 42.6 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 4.09× (z +8.7) | — |
| [[AsPC-1 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 56.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 47.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 47.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 35.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8616), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELP3]] | +0.61 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[WDR75]] | +0.60 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[PDSS1]] | +0.60 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[QTRT2]] | +0.59 | +0.52 / +0.59 | both halves | 1e-05 | pathway: tRNA processing |
| [[TADA1]] | +0.58 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[LIN9]] | +0.57 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[NUP54]] | +0.56 | +0.51 / +0.61 | both halves | 1e-05 | same gene group; pathway: Antimicrobial mechanism of IFN-stimulated genes; STRING 993 |
| [[PRMT7]] | +0.56 | +0.69 / +0.50 | both halves | 1e-05 |  |
| [[SASS6]] | +0.56 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[PPIH]] | +0.56 | +0.59 / +0.59 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[UBA2]] | +0.56 | +0.53 / +0.57 | both halves | 1e-05 | pathway: SUMOylation |
| [[RBM26]] | +0.56 | +0.52 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MALAT1]] | -0.55 | -0.40 / -0.56 | both halves | 5e-05 |  |
| [[SPTAN1]] | -0.50 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[GDI1]] | -0.50 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[AFF4]] | -0.50 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[TALAM1]] | -0.50 | -0.35 / -0.53 | both halves | 1e-04 |  |
| [[NEAT1]] | -0.49 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[SKP1]] | -0.49 | -0.41 / -0.45 | both halves | 4e-05 | pathway: Antimicrobial mechanism of IFN-stimulated genes |
| [[UBE2A]] | -0.48 | -0.32 / -0.61 | both halves | 2e-04 |  |
| [[ATP6V0C]] | -0.48 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[JOSD1]] | -0.48 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[TAX1BP1]] | -0.48 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[UBE2H]] | -0.48 | -0.37 / -0.53 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.475). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-22.9, -42.4); signed map (-11.0, -59.6). **Vector** length 95.1, 24.5% of its response variance represented; |z| ≥ 3 in 960 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.7 | +1.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +2.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +1.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.1 | +4.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | +1.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.0 | +9.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.6 | +2.5 |
|  | [[EX229 (drug)]] 5 µM |  | +2.5 | +2.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.4 | +3.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.0 | -4.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.6 | -0.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.5 | +0.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | +1.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.2 | -1.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.5 | -2.6 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.8 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | nucleoporin 35 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q32.1 — chr2:183,117,513-183,161,680 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MP44 |
| Gene groups (HGNC) | Nucleoporins |
| Reactome | 73 pathways, smallest: Postmitotic nuclear pore complex (NPC) reformation; IP3 and IP4 transport between cytosol and nucleus; IP6 and IP7 transport between cytosol and nucleus |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NFH5](https://www.uniprot.org/uniprotkb/Q8NFH5) (Nucleoporin NUP35):

> Functions as a component of the nuclear pore complex (NPC). NPC components, collectively referred to as nucleoporins (NUPs), can play the role of both NPC structural components and of docking or interaction partners for transiently associated nuclear transport factors. May play a role in the association of MAD1 with the NPC.

**Summary**, from NCBI Gene [129401](https://www.ncbi.nlm.nih.gov/gene/129401):

> This gene encodes a member of the nucleoporin family. The encoded protein contains two membrane binding regions, is localized to the nuclear rim, and is part of the nuclear pore complex. All molecules entering or leaving the nucleus either diffuse through or are actively transported by the nuclear pore complex. Alternative splicing results in multiple transcript variants. Pseudogenes of this gene have been defined on chromosomes 7 and 10. [provided by RefSeq, Dec 2013]

**Accessions** — [HGNC:29797](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29797) · Entrez [129401](https://www.ncbi.nlm.nih.gov/gene/129401) · UniProt [Q8NFH5](https://www.uniprot.org/uniprotkb/Q8NFH5) · Ensembl [ENSG00000163002](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163002)

## Data

Gene col 8616: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8616); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8616, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8616]; `tensor/DDL_lfc|DDL_z.npy` [8616]; `embed/gene_vectors.npy` [8616]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8616 or target_col == 8616). Every well: [[NUP35 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUP35.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
