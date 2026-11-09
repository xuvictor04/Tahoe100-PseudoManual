---
symbol: "FKBP8"
type: "gene"
col: 2648
ensembl_id: "ENSG00000105701"
name: "FKBP prolyl isomerase 8"
location: "19p13.11"
module: 76
arm: "+"
pooled_cpm: 42.89
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 12
n_dd_up_clean: 0
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# FKBP8

*FKBP prolyl isomerase 8* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.27× (z +13.3, q 1e-37, up in 46 of 47 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (HEC-1-A 5.11×, NCI-H1573 7.85×, PANC-1 4.18×, HOP62 4.08×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (KATO III 5.11×, HEC-1-A 4.09×, PANC-1 4.30×, LoVo 5.34×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HEC-1-A 3.57×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.348× (z -17.6, q 0e+00, down in 47 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OS9]] (+0.80, fdr 7e-06), [[PBXIP1]] (+0.68, fdr 7e-06), [[C20orf96]] (+0.65, fdr 1e-05); moves opposite to [[NOP56]] (-0.66, fdr 7e-06), [[NIP7]] (-0.61, fdr 2e-05), [[GPATCH4]] (-0.60, fdr 2e-05).
> It is in [[Module 076]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2648.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (HEC-1-A 5.11×, NCI-H1573 7.85×, PANC-1 4.18×, HOP62 4.08×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (KATO III 5.11×, HEC-1-A 4.09×, PANC-1 4.30×, LoVo 5.34×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HEC-1-A 3.57×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.27×** | +13.3 | 1e-37 | 46/47 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.65×** | +11.2 | 1e-26 | 38/39 (KATO III, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.12×** | +8.3 | 2e-14 | 39/44 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | **1.51×** | +5.0 | 9e-05 | 34/47 (KATO III, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +4.2 | 0.003 | 1/49 (MIA PaCa-2) | inconsistent across doses | noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | 1.31× | +3.2 | 0.13 | 21/48 (KATO III, SW 900, …) | top dose only | position effect removed |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.30× | +3.2 | 0.13 | 19/47 (SW1417, KATO III, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2648.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.348×** | -17.6 | 0e+00 | 47/47 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.334×** | -13.1 | 9e-37 | 47/47 (MIA PaCa-2, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.567×** | -6.5 | 1e-08 | 40/48 (AsPC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.601×** | -6.1 | 2e-07 | 38/48 (AsPC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.612×** | -5.9 | 5e-07 | 39/48 (AsPC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.646×** | -5.2 | 2e-05 | 36/48 (HT-29, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.659×** | -5.0 | 6e-05 | 32/48 (AsPC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.695×** | -4.3 | 0.001 | 36/48 (BT-474, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.710×** | -4.1 | 0.003 | 28/48 (SW 900, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.699×** | -3.9 | 0.005 | 28/48 (MIA PaCa-2, SW48, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.726×** | -3.8 | 0.007 | 26/48 (HT-29, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.727×** | -3.8 | 0.007 | 26/47 (RKO, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~47% of this change | 0.758× | -3.0 | 0.12 | 20/48 (SK-MEL-2, AN3 CA, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2648. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 37.7 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.08× (z +10.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -12.0) |
| [[KATO III (line)]] | alt | 32.4 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 5.11× (z +11.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -11.2) |
| [[LoVo (line)]] | wt | 28.9 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 5.34× (z +11.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -15.0) |
| [[PANC-1 (line)]] | alt | 34.9 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 4.30× (z +11.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -13.7) |
| [[SW480 (line)]] | alt | 32.9 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.44× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -12.2) |
| [[A-172 (line)]] | wt | 70.1 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.473× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 76.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.11× (z +13.2) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 35.8 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.36× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -15.1) |
| [[J82 (line)]] | alt | 38.3 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -16.9) |
| [[LOX-IMVI (line)]] | wt | 44.3 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.59× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -18.9) |
| [[LS 180 (line)]] | wt | 47.7 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.55× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -17.0) |
| [[NCI-H460 (line)]] | wt | 29.1 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -18.5) |
| [[Panc 03.27 (line)]] | alt | 78.5 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.36× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -14.9) |
| [[A-427 (line)]] | wt | 55.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.25× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -9.1) |
| [[A498 (line)]] | wt | 45.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +10.3) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 32.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -15.3) |
| [[CFPAC-1 (line)]] | alt | 50.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -14.3) |
| [[COLO 205 (line)]] | alt | 35.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -9.2) |
| [[HS-578T (line)]] | alt | 58.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.73× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 56.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.137× (z -15.4) |
| [[NCI-H1573 (line)]] | alt | 21.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 7.85× (z +12.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -9.5) |
| [[NCI-H1792 (line)]] | alt | 41.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -10.9) |
| [[NCI-H2347 (line)]] | alt | 48.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -13.8) |
| [[SNU-1 (line)]] | wt | 42.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.165× (z -9.8) |
| [[SNU-423 (line)]] | alt | 45.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -9.4) |
| [[A549 (line)]] | wt | 29.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -10.6) |
| [[BT-474 (line)]] | alt | 16.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -12.1) |
| [[C-33 A (line)]] | alt | 42.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -10.3) ⚠ cell-cycle shift, explains ~50% of this change |
| [[C32 (line)]] | wt | 28.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -8.8) |
| [[H4 (line)]] | wt | 49.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -9.4) |
| [[HCT15 (line)]] | alt | 69.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -17.2) |
| [[Hs 766T (line)]] | wt | 36.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 56.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.265× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 55.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -11.4) |
| [[NCI-H23 (line)]] | alt | 42.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.201× (z -11.7) |
| [[RKO (line)]] | wt | 35.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -10.7) |
| [[RPMI-7951 (line)]] | alt | 55.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -9.7) |
| [[SHP-77 (line)]] | alt | 58.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.93× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 36.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -8.6) |
| [[SW 1271 (line)]] | alt | 55.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -11.9) |
| [[SW 900 (line)]] | alt | 42.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.254× (z -10.0) |
| [[SW48 (line)]] | wt | 32.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -10.3) |
| [[AN3 CA (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 49.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 32.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2648), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OS9]] | +0.80 | +0.76 / +0.74 | both halves | 7e-06 |  |
| [[PBXIP1]] | +0.68 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[C20orf96]] | +0.65 | +0.67 / +0.49 | both halves | 1e-05 |  |
| [[NUCB1]] | +0.65 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[MAPK3]] | +0.64 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[SLC25A23]] | +0.63 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[MOSPD3]] | +0.62 | +0.75 / +0.53 | both halves | 1e-05 |  |
| [[GM2A]] | +0.62 | +0.66 / +0.46 | both halves | 3e-05 |  |
| [[KDELR1]] | +0.61 | +0.76 / +0.52 | both halves | 1e-05 |  |
| [[GTF2IP4]] | +0.60 | +0.59 / +0.29 | both halves | 2e-04 |  |
| [[CALCOCO1]] | +0.60 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[GRN]] | +0.59 | +0.58 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOP56]] | -0.66 | -0.69 / -0.63 | both halves | 7e-06 |  |
| [[NIP7]] | -0.61 | -0.64 / -0.47 | both halves | 2e-05 |  |
| [[GPATCH4]] | -0.60 | -0.69 / -0.48 | both halves | 2e-05 |  |
| [[EIF3J]] | -0.58 | -0.68 / -0.50 | both halves | 1e-05 |  |
| [[NME6]] | -0.56 | -0.62 / -0.32 | both halves | 2e-04 |  |
| [[TMA16]] | -0.56 | -0.61 / -0.43 | both halves | 3e-05 |  |
| [[ST7L]] | -0.55 | -0.69 / -0.38 | both halves | 6e-05 |  |
| [[METTL1]] | -0.54 | -0.53 / -0.36 | both halves | 9e-05 |  |
| [[METTL8]] | -0.53 | -0.60 / -0.41 | both halves | 4e-05 |  |
| [[PPRC1]] | -0.53 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[ITPRIPL2]] | -0.52 | -0.52 / -0.34 | both halves | 1e-04 |  |
| [[TASOR2]] | -0.52 | -0.48 / -0.51 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises FKBP8's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.608). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.3, -20.2); signed map (-30.0, -4.3). **Vector** length 64.6, 15.9% of its response variance represented; |z| ≥ 3 in 770 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.8 | -0.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.0 | -1.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.1 | -5.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | +2.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +1.9 | -6.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +1.1 | +0.2 |
|  | [[Cloxacillin (sodium) (drug)]] 0.05 µM |  | +1.1 | +0.2 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +1.1 | +1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.1 | -2.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.4 | -13.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | -1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -2.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.8 | -17.6 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -2.1 | -0.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.5 | -0.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.5 | -0.3 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -1.5 | -0.6 |
|  | [[vincristine (drug)]] 0.5 µM |  | -1.4 | +1.4 |

## What is on record

|  |  |
|---|---|
| Name | FKBP prolyl isomerase 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:18,531,751-18,544,077 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FKBP38, FKBPr38 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing; FKBP prolyl isomerase family |
| Reactome | 2 pathways, smallest: Ub-specific processing proteases; Deubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14318](https://www.uniprot.org/uniprotkb/Q14318) (Peptidyl-prolyl cis-trans isomerase FKBP8):

> Constitutively inactive PPiase, which becomes active when bound to calmodulin and calcium. Seems to act as a chaperone for BCL2, targets it to the mitochondria and modulates its phosphorylation state. The BCL2/FKBP8/calmodulin/calcium complex probably interferes with the binding of BCL2 to its targets. The active form of FKBP8 may therefore play a role in the regulation of apoptosis. Involved in the inhibition of viral infection by influenza A viruses (IAV).

**Summary**, from NCBI Gene [23770](https://www.ncbi.nlm.nih.gov/gene/23770):

> The protein encoded by this gene is a member of the immunophilin protein family, which play a role in immunoregulation and basic cellular processes involving protein folding and trafficking. Unlike the other members of the family, this encoded protein does not seem to have PPIase/rotamase activity. It may have a role in neurons associated with memory function. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:3724](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3724) · Entrez [23770](https://www.ncbi.nlm.nih.gov/gene/23770) · UniProt [Q14318](https://www.uniprot.org/uniprotkb/Q14318) · Ensembl [ENSG00000105701](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105701)

## Data

Gene col 2648: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2648); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2648, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2648]; `tensor/DDL_lfc|DDL_z.npy` [2648]; `embed/gene_vectors.npy` [2648]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2648 or target_col == 2648). Every well: [[FKBP8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FKBP8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
