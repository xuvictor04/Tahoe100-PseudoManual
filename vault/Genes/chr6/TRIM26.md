---
symbol: "TRIM26"
type: "gene"
col: 13938
ensembl_id: "ENSG00000234127"
name: "tripartite motif containing 26"
location: "6p22.1"
module: 32
arm: "+"
pooled_cpm: 41.78
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 3
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# TRIM26

*tripartite motif containing 26* — 6p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.90× (z +15.1, q 0e+00, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.458× (z -13.0, q 4e-36, down in 42 of 47 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (LoVo 0.133×, A-172 0.106×, HEC-1-A 0.138×, NCI-H23 0.161×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H2347 0.244×, Panc 03.27 0.234×, CFPAC-1 0.267×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H2347 0.290×, NCI-H2030 0.204×; ⚠ toxic; transcription drop); [[Azithromycin (hydrate) (drug)]] 5 µM in 1 line (CHP-212 0.158×); [[Larotrectinib (drug)]] 0.5 µM in 1 line (SW 1271 0.0742×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IFIT5]] (+0.60, fdr 1e-05), [[USP18]] (+0.59, fdr 1e-05), [[TMEM62]] (+0.58, fdr 1e-05); moves opposite to [[PABPC1]] (-0.47, fdr 6e-05), [[OSBPL8]] (-0.43, fdr 4e-05), [[TMEM14B]] (-0.43, fdr 1e-04).
> It is in [[Module 032]], a single-armed module (interferon alpha response).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13938.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.90×** | +15.1 | 0e+00 | 39/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.88×** | +10.4 | 6e-23 | 44/48 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.85×** | +10.1 | 6e-22 | 44/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.81×** | +9.8 | 1e-20 | 42/48 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.81×** | +9.5 | 3e-19 | 41/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.67×** | +8.5 | 2e-15 | 39/49 (NCI-H460, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.66×** | +7.9 | 2e-13 | 39/48 (A498, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.60×** | +7.7 | 7e-13 | 38/48 (J82, RKO, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.19×** | +6.8 | 7e-10 | 31/43 (RKO, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.49×** | +6.6 | 2e-09 | 32/48 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.47×** | +6.3 | 1e-08 | 26/48 (A498, RKO, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.29×** | +5.9 | 2e-07 | 27/48 (LS 180, NCI-H460, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.92×** | +5.6 | 7e-07 | 33/48 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.39×** | +5.5 | 2e-06 | 28/47 (J82, NCI-H460, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.57×** | +5.3 | 4e-06 | 26/49 (RKO, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.36×** | +5.1 | 1e-05 | 24/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.35×** | +4.9 | 3e-05 | 24/48 (C32, RKO, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.25×** | +3.7 | 0.007 | 20/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.23×** | +3.2 | 0.041 | 17/47 (NCI-H460, COLO 205, …) | all doses, stronger at high dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13938.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (LoVo 0.133×, A-172 0.106×, HEC-1-A 0.138×, NCI-H23 0.161×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H2347 0.244×, Panc 03.27 0.234×, CFPAC-1 0.267×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H2347 0.290×, NCI-H2030 0.204×; ⚠ toxic; transcription drop); [[Azithromycin (hydrate) (drug)]] 5 µM in 1 line (CHP-212 0.158×); [[Larotrectinib (drug)]] 0.5 µM in 1 line (SW 1271 0.0742×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.458×** | -13.0 | 4e-36 | 42/47 (LoVo, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.450×** | -12.8 | 4e-35 | 33/38 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.716×** | -5.2 | 4e-05 | 26/44 (NCI-H2347, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.869× | -3.4 | 0.11 | 13/49 (A-172, HT-29, …) | rises with dose | position effect removed |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | 0.825× | -3.2 | 0.13 | 17/48 (LoVo, NCI-H23, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.821× | -3.2 | 0.13 | 14/48 (NCI-H23, LoVo, …) | top dose only | position effect removed |
| [[Tofacitinib (drug)]] 5 µM |  | 0.878× | -3.1 | 0.15 | 14/48 (LoVo, C-33 A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13938. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 38.3 | 13 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.28× (z +27.8) | — |
| [[LS 180 (line)]] | wt | 71.0 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.81× (z +20.2) | — |
| [[HEC-1-A (line)]] | alt | 26.6 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +13.2) | [[Dinaciclib (drug)]] 0.5 µM 0.138× (z -17.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 85.0 | 3 (1 ⚠) | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.35× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.456× (z -9.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 35.3 | 3 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.23× (z +9.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 2.32× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.374× (z -11.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 38.5 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +11.2) | — |
| [[A498 (line)]] | wt | 33.8 | 2 | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.77× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.385× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 37.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.232× (z -14.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 38.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.225× (z -11.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 34.5 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.75× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.236× (z -10.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 41.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.267× (z -10.8) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 47.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -12.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 32.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.309× (z -9.1) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 54.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -12.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 55.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.133× (z -21.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 38.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.282× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 39.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +12.6) | [[Dinaciclib (drug)]] 0.05 µM 0.204× (z -10.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 59.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.234× (z -12.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 49.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +10.4) | — |
| [[SW48 (line)]] | wt | 36.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.203× (z -9.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 38.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.106× (z -18.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 66.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.165× (z -8.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 52.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +8.5) | — |
| [[BT-474 (line)]] | alt | 63.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +8.5) | — |
| [[CHP-212 (line)]] | wt | 29.0 | 0 | 1 | — | [[Azithromycin (hydrate) (drug)]] 5 µM 0.158× (z -9.7) |
| [[HCT15 (line)]] | alt | 35.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.195× (z -9.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 54.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.331× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 46.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -14.5) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 40.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.253× (z -9.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 31.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.163× (z -12.3) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 51.6 | 0 | 1 | — | [[Larotrectinib (drug)]] 0.5 µM 0.0742× (z -8.7) |
| [[A-427 (line)]] | wt | 36.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 36.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 40.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 63.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13938), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFIT5]] | +0.60 | +0.59 / +0.57 | both halves | 1e-05 | pathway: Interferon Signaling |
| [[USP18]] | +0.59 | +0.58 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[TMEM62]] | +0.58 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[CMPK2]] | +0.58 | +0.55 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[TRIM21]] | +0.56 | +0.51 / +0.56 | both halves | 1e-05 | same gene group; pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[IFIT1]] | +0.55 | +0.59 / +0.48 | both halves | 2e-05 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[ZC3HAV1]] | +0.55 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[PML]] | +0.55 | +0.48 / +0.49 | both halves | 2e-05 | same gene group; pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[OASL]] | +0.54 | +0.55 / +0.51 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[IFI44]] | +0.54 | +0.53 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[SHFL]] | +0.54 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[ZNF107]] | +0.54 | +0.46 / +0.57 | both halves | 2e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PABPC1]] | -0.47 | -0.39 / -0.49 | both halves | 6e-05 |  |
| [[OSBPL8]] | -0.43 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[TMEM14B]] | -0.43 | -0.52 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.552). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.8, 55.9); signed map (65.9, 34.1). **Vector** length 90.9, 22.9% of its response variance represented; |z| ≥ 3 in 1,119 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *IFIT antiviral response* (reactome, mean cos +0.52 to 9); *OAS antiviral response* (reactome, mean cos +0.52 to 5); *Viral strategies to evade IFIT action* (reactome, mean cos +0.51 to 3).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +4.5 | +7.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | +4.3 | +5.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.8 | +6.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~62% of this change | +3.5 | +4.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.4 | +6.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +4.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.3 | +3.2 |
|  | [[venetoclax (drug)]] 0.05 µM |  | +2.3 | +2.3 |
|  | [[Docetaxel (drug)]] 5 µM |  | +2.2 | +2.7 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.6 | -13.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.3 | -12.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.6 | +2.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | -2.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.4 | +2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -1.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.1 | -3.4 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -2.8 | -3.2 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.8 | -3.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.8 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | tripartite motif containing 26 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.1 — chr6:30,184,455-30,213,427 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RNF95; previously ZNF173 |
| Gene groups (HGNC) | Ring finger proteins; Tripartite motif family; RING finger E3 ubiquitin protein ligases |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, INTERFERON_GAMMA_RESPONSE |
| Reactome | 3 pathways, smallest: Interferon gamma signaling; Interferon Signaling; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12899](https://www.uniprot.org/uniprotkb/Q12899) (Tripartite motif-containing protein 26):

> E3 ubiquitin-protein ligase which regulates the IFN-beta production and antiviral response downstream of various DNA-encoded pattern-recognition receptors (PRRs). Also plays a central role in determining the response to different forms of oxidative stress by controlling levels of DNA glycosylases NEIL1, NEIL3 and NTH1 that are involved in repair of damaged DNA. Promotes nuclear IRF3 ubiquitination and proteasomal degradation. Bridges together TBK1 and NEMO during the innate response to viral …

**Summary**, from NCBI Gene [7726](https://www.ncbi.nlm.nih.gov/gene/7726):

> The protein encoded by this gene is a member of the tripartite motif (TRIM) family. The TRIM motif includes three zinc-binding domains, a RING, a B-box type 1 and a B-box type 2, and a coiled-coil region. The protein localizes to cytoplasmic bodies. Although the function of the protein is unknown, the RING domain suggests that the protein may have DNA-binding activity. The gene localizes to the major histocompatibility complex (MHC) class I region on chromosome 6. Alternatively spliced …

**Accessions** — [HGNC:12962](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12962) · Entrez [7726](https://www.ncbi.nlm.nih.gov/gene/7726) · UniProt [Q12899](https://www.uniprot.org/uniprotkb/Q12899) · Ensembl [ENSG00000234127](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000234127)

## Data

Gene col 13938: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13938); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13938, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13938]; `tensor/DDL_lfc|DDL_z.npy` [13938]; `embed/gene_vectors.npy` [13938]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13938 or target_col == 13938). Every well: [[TRIM26 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIM26.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
