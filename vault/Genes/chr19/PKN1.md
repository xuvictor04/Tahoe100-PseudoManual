---
symbol: "PKN1"
type: "gene"
col: 4407
ensembl_id: "ENSG00000123143"
name: "protein kinase N1"
location: "19p13.12"
module: 30
arm: "+"
pooled_cpm: 32.44
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 28
n_dd_up_clean: 2
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# PKN1

*protein kinase N1* — 19p13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.84× (z +9.3, q 5e-18, up in 37 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Vinblastine (sulfate) (drug)]] 5 µM: 1.23× (z +4.6, q 1e-03, up in 21 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SW480 2.88×, LoVo 3.08×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (SW480 3.56×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.543× (z -13.2, q 4e-37, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC112]] (+0.66, fdr 1e-05), [[ANKRD27]] (+0.65, fdr 1e-05), [[IFT52]] (+0.64, fdr 2e-05); moves opposite to [[MPDU1]] (-0.64, fdr 2e-05), [[EIF4G2]] (-0.58, fdr 4e-05), [[ARSB]] (-0.57, fdr 1e-04).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[STARD9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4407.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SW480 2.88×, LoVo 3.08×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (SW480 3.56×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.84×** | +9.3 | 5e-18 | 37/44 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.73×** | +8.0 | 2e-13 | 30/36 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.23×** | +4.6 | 1e-03 | 21/48 (A549, KATO III, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.73×** | +4.4 | 0.002 | 28/47 (A498, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.35×** | +4.2 | 0.002 | 19/41 (SW480, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.27×** | +3.7 | 0.020 | 17/47 (SNU-1, CFPAC-1, …) | top dose only |  |
| [[Retinoic acid (drug)]] 5 µM |  | 1.17× | +3.3 | 0.062 | 12/48 (A-172, A498, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.17× | +3.3 | 0.062 | 14/48 (RKO, PANC-1, …) | top dose only | position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 1.48× | +3.1 | 0.11 | 10/39 (RPMI-7951, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~19% of this change | 1.22× | +3.1 | 0.12 | 18/46 (KATO III, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.22× | +3.0 | 0.14 | 14/47 (hTERT-HPNE, SW 900, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4407.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.543×** | -13.2 | 4e-37 | 43/48 (MIA PaCa-2, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.567×** | -12.3 | 3e-32 | 36/48 (MIA PaCa-2, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.507×** | -10.4 | 6e-23 | 38/48 (MIA PaCa-2, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.617×** | -7.1 | 2e-10 | 32/47 (A-172, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.649×** | -6.6 | 4e-09 | 30/47 (J82, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.653×** | -6.5 | 7e-09 | 34/48 (SNU-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.446×** | -6.5 | 9e-09 | 32/43 (Panc 03.27, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.768×** | -5.7 | 8e-07 | 29/48 (MIA PaCa-2, HS-578T, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.654×** | -5.7 | 1e-06 | 27/48 (NCI-H2030, SW 1271, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.684×** | -5.6 | 1e-06 | 27/48 (SNU-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.696×** | -5.6 | 1e-06 | 28/48 (SNU-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.705×** | -5.4 | 4e-06 | 30/48 (MIA PaCa-2, HS-578T, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.719×** | -5.0 | 2e-05 | 29/48 (SK-MEL-2, C32, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.710×** | -5.0 | 2e-05 | 29/48 (C32, SW 1088, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.729×** | -4.8 | 5e-05 | 25/47 (SNU-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.596×** | -4.1 | 0.001 | 20/48 (A-427, Hs 766T, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.768×** | -4.0 | 0.002 | 21/48 (LoVo, MIA PaCa-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4407. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 32.9 | 0 | 6 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.122× (z -12.2) |
| [[MIA PaCa-2 (line)]] | alt | 71.1 | 0 | 5 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0978× (z -20.5) |
| [[A-427 (line)]] | wt | 47.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.226× (z -12.6) |
| [[HS-578T (line)]] | alt | 48.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.268× (z -11.5) |
| [[NCI-H2030 (line)]] | alt | 35.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -14.8) |
| [[SW480 (line)]] | alt | 30.5 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.56× (z +11.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.513× (z -8.9) |
| [[A-172 (line)]] | wt | 88.6 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -10.2) |
| [[C32 (line)]] | wt | 25.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.295× (z -10.6) |
| [[HEC-1-A (line)]] | alt | 62.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -10.0) |
| [[HOP62 (line)]] | alt | 23.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -10.7) |
| [[PANC-1 (line)]] | alt | 41.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.513× (z -9.1) |
| [[RPMI-7951 (line)]] | alt | 38.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.224× (z -10.5) |
| [[A498 (line)]] | wt | 32.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.238× (z -12.5) |
| [[A549 (line)]] | wt | 34.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -9.4) |
| [[CFPAC-1 (line)]] | alt | 23.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -9.1) |
| [[H4 (line)]] | wt | 19.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0653× (z -12.3) |
| [[Hs 766T (line)]] | wt | 29.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.240× (z -13.0) |
| [[J82 (line)]] | alt | 43.8 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.368× (z -8.9) |
| [[LoVo (line)]] | wt | 21.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +8.5) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 24.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -9.3) |
| [[SK-MEL-2 (line)]] | alt | 24.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -16.7) |
| [[SNU-423 (line)]] | alt | 27.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -13.0) |
| [[SW 900 (line)]] | alt | 29.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -11.8) |
| [[SW48 (line)]] | wt | 43.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.170× (z -10.4) |
| [[AN3 CA (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 77.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4407), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC112]] | +0.66 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[ANKRD27]] | +0.65 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[IFT52]] | +0.64 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[MAST3]] | +0.62 | +0.61 / +0.34 | both halves | 1e-04 |  |
| [[STX7]] | +0.62 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[TNK2]] | +0.62 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[BCAS4]] | +0.60 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[TAMM41]] | +0.60 | +0.54 / +0.40 | both halves | 5e-05 |  |
| [[E4F1]] | +0.60 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[TOMM20]] | +0.60 | +0.52 / +0.38 | both halves | 7e-05 |  |
| [[TMEM185A]] | +0.60 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[BTBD2]] | +0.60 | +0.46 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPDU1]] | -0.64 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[EIF4G2]] | -0.58 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[ARSB]] | -0.57 | -0.50 / -0.34 | both halves | 1e-04 |  |
| [[CCDC90B-AS1]] | -0.57 | -0.52 / -0.19 | ⚠ one half (not replicated) | 8e-04 |  |
| [[NXT2]] | -0.55 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[GPATCH2]] | -0.55 | -0.53 / -0.31 | both halves | 2e-04 |  |
| [[SECISBP2]] | -0.54 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[DDX5]] | -0.54 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[XNDC1N-ZNF705EP-ALG1L9P]] | -0.54 | -0.47 / -0.29 | both halves | 2e-04 |  |
| [[C17orf80]] | -0.54 | -0.53 / -0.36 | both halves | 1e-04 |  |
| [[AP5S1]] | -0.53 | -0.46 / -0.30 | both halves | 2e-04 |  |
| [[CFAP54]] | -0.53 | -0.48 / -0.21 | both halves | 6e-04 |  |
| [[RNF217-AS1]] | -0.53 | -0.32 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STARD9]] | B | STARD9 activity raises PKN1's level | lines that do not express STARD9 (8) vs lines expressing it (42) | 1.78× lower at baseline in the lines without STARD9 | 0.010 | ⚠ within organs, on part of the lines; also absent: DZIP1L, FMNL3, HEG1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises PKN1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC02405]] | B | LINC02405 activity lowers PKN1's level | lines that do not express LINC02405 (27) vs lines expressing it (23) | 1.49× higher at baseline in the lines without LINC02405 | 0.062 | ⚠ within organs, on part of the lines; also absent: ENSG00000286016, ENSG00000278266, LINC02360 |
| [[SNTA1]] | B | SNTA1 activity raises PKN1's level | lines that do not express SNTA1 (5) vs lines expressing it (45) | 1.57× lower at baseline in the lines without SNTA1 | 0.089 | ⚠ within organs, on part of the lines; also absent: SACS, CLTCL1, MXRA7; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.618). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (1.9, -3.2); signed map (-34.5, -1.9). **Vector** length 95.7, 24.0% of its response variance represented; |z| ≥ 3 in 886 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.1 | -1.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.4 | -0.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | -2.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.9 | +3.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.9 | +0.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.5 | +4.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.8 | +1.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.6 | +3.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.2 | -13.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.5 | -5.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.5 | -7.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -5.4 | -5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.8 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | -5.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.5 | -0.2 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -2.3 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | protein kinase N1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.12 — chr19:14,433,053-14,471,867 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DBK, PRK1, PKN, MGC46204, PAK1; previously PRKCL1 |
| Gene groups (HGNC) | C2 domain containing protein kinases; Protein kinase N family |
| Reactome | 10 pathways, smallest: Activated PKN1 stimulates transcription of AR (androgen receptor) regulated genes KLK2 and KLK3; RHO GTPases activate PKNs; RHOB GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16512](https://www.uniprot.org/uniprotkb/Q16512) (Serine/threonine-protein kinase N1):

> PKC-related serine/threonine-protein kinase involved in various processes such as regulation of the intermediate filaments of the actin cytoskeleton, cell migration, tumor cell invasion and transcription regulation. Part of a signaling cascade that begins with the activation of the adrenergic receptor ADRA1B and leads to the activation of MAPK14. Regulates the cytoskeletal network by phosphorylating proteins such as VIM and neurofilament proteins NEFH, NEFL and NEFM, leading to inhibit their …

**Summary**, from NCBI Gene [5585](https://www.ncbi.nlm.nih.gov/gene/5585):

> The protein encoded by this gene belongs to the protein kinase C superfamily. This kinase is activated by Rho family of small G proteins and may mediate the Rho-dependent signaling pathway. This kinase can be activated by phospholipids and by limited proteolysis. The 3-phosphoinositide dependent protein kinase-1 (PDPK1/PDK1) is reported to phosphorylate this kinase, which may mediate insulin signals to the actin cytoskeleton. The proteolytic activation of this kinase by caspase-3 or related …

**Accessions** — [HGNC:9405](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9405) · Entrez [5585](https://www.ncbi.nlm.nih.gov/gene/5585) · UniProt [Q16512](https://www.uniprot.org/uniprotkb/Q16512) · Ensembl [ENSG00000123143](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123143)

## Data

Gene col 4407: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4407); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4407, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4407]; `tensor/DDL_lfc|DDL_z.npy` [4407]; `embed/gene_vectors.npy` [4407]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4407 or target_col == 4407). Every well: [[PKN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PKN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
