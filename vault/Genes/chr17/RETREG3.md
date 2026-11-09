---
symbol: "RETREG3"
type: "gene"
col: 6568
ensembl_id: "ENSG00000141699"
name: "reticulophagy regulator family member 3"
location: "17q21.2"
module: 187
arm: "+"
pooled_cpm: 48.06
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 22
n_dd_up_clean: 2
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/187"]
generated_by: "tahoemap"
---

# RETREG3

*reticulophagy regulator family member 3* — 17q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 1.23× (z +3.7, q 0.090, up in 24 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.382× (z -17.4, q 0e+00, down in 42 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.641× (z -8.0, q 6e-14, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZER1]] (+0.70, fdr 1e-05), [[WIPI2]] (+0.69, fdr 7e-06), [[ZNHIT3]] (+0.68, fdr 1e-05); moves opposite to [[CYCS]] (-0.52, fdr 2e-05), [[SRSF1]] (-0.49, fdr 1e-04), [[TENM3]] (-0.48, fdr 3e-05).
> It is in [[Module 187]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6568.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.090 | 24/48 (HEC-1-A, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.46×** | +3.6 | 0.090 | 19/48 (NCI-H2030, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 5 µM |  | 1.13× | +3.2 | 0.18 | 5/49 (KATO III, PANC-1, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.13× | +3.2 | 0.18 | 19/48 (SW480, LS 180, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 1.23× | +3.2 | 0.18 | 17/48 (LS 180, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Rapamycin (drug)]] 5 µM |  | 1.13× | +3.1 | 0.18 | 7/48 (PANC-1, NCI-H2030, …) | rises with dose |  |
| [[Vortioxetine (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.18 | 7/48 (LoVo, hTERT-HPNE, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6568.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.382×** | -17.4 | 0e+00 | 42/49 (SK-MEL-2, KATO III, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.432×** | -14.1 | 2e-42 | 35/43 (SW1417, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.469×** | -13.7 | 1e-40 | 48/48 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.448×** | -12.2 | 3e-32 | 33/41 (KATO III, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.646×** | -11.2 | 5e-27 | 36/48 (hTERT-HPNE, SNU-423, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.599×** | -9.3 | 2e-18 | 40/48 (NCI-H460, NCI-H1792, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.616×** | -8.8 | 1e-16 | 40/48 (KATO III, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.641×** | -8.0 | 6e-14 | 35/48 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.430×** | -8.0 | 8e-14 | 41/48 (A498, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.462×** | -7.3 | 1e-11 | 37/48 (NCI-H1792, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.686×** | -6.8 | 5e-10 | 30/47 (A-172, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.498×** | -6.6 | 2e-09 | 39/48 (SNU-1, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.529×** | -6.0 | 7e-08 | 34/48 (CFPAC-1, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.538×** | -5.9 | 2e-07 | 30/48 (LOX-IMVI, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.729×** | -5.7 | 4e-07 | 32/48 (NCI-H460, SNU-423, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.721×** | -5.6 | 8e-07 | 32/48 (NCI-H1792, NCI-H460, …) | all doses, flat |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.758×** | -3.6 | 0.010 | 15/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.785×** | -3.1 | 0.047 | 11/48 (MIA PaCa-2, SW 900, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6568. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 41.7 | 0 | 9 (9 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0774× (z -23.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 54.7 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.107× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[venetoclax (drug)]] 5 µM 0.0486× (z -13.0) |
| [[A498 (line)]] | wt | 51.9 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.249× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Abemaciclib (drug)]] 5 µM 0.133× (z -11.9) |
| [[MIA PaCa-2 (line)]] | alt | 47.7 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.186× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Abemaciclib (drug)]] 5 µM 0.128× (z -10.5) |
| [[HS-578T (line)]] | alt | 50.9 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.189× (z -14.9) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 67.7 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.159× (z -16.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 69.6 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.169× (z -15.4) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 57.6 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -13.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 61.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -13.4) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.388× (z -9.9) |
| [[HOP62 (line)]] | alt | 58.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.213× (z -15.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 37.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0957× (z -16.0) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 72.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0678× (z -24.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 75.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.263× (z -12.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 59.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.299× (z -10.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 65.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.301× (z -11.5) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 39.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -14.2) ⚠ cell-cycle shift, explains ~44% of this change |
| [[H4 (line)]] | wt | 42.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.117× (z -12.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 50.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.252× (z -12.4) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 54.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.260× (z -12.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 64.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.116× (z -17.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 42.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0401× (z -26.1) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 44.7 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.454× (z -9.2) |
| [[A549 (line)]] | wt | 65.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.372× (z -9.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 44.8 | 0 | 1 | — | [[Betamethasone dipropionate (drug)]] 0.05 µM 0.139× (z -9.1) |
| [[CHP-212 (line)]] | wt | 68.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.184× (z -8.7) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 63.0 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.321× (z -8.6) ⚠ cell-cycle shift, explains ~35% of this change |
| [[HT-29 (line)]] | alt | 40.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.365× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[hTERT-HPNE (line)]] | wt | 59.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -16.1) ⚠ cell-cycle shift, explains ~44% of this change |
| [[J82 (line)]] | alt | 38.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.485× (z -8.8) ⚠ cell-cycle shift, explains ~44% of this change |
| [[LoVo (line)]] | wt | 36.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.357× (z -9.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 33.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.244× (z -11.7) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 46.9 | 0 | 1 | — | [[Estrone sulfate (potassium) (drug)]] 0.5 µM 0.0961× (z -9.3) |
| [[PANC-1 (line)]] | alt | 31.7 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.383× (z -9.7) ⚠ unreliable plate only |
| [[RKO (line)]] | wt | 40.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.330× (z -8.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 48.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.120× (z -18.4) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 59.1 | 0 | 1 | — | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM 0.0531× (z -11.2) |
| [[SW 900 (line)]] | alt | 40.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.286× (z -10.1) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 39.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 34.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6568), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 6 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZER1]] | +0.70 | +0.49 / +0.77 | both halves | 1e-05 |  |
| [[WIPI2]] | +0.69 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[ZNHIT3]] | +0.68 | +0.53 / +0.73 | both halves | 1e-05 |  |
| [[ATXN3]] | +0.67 | +0.53 / +0.74 | both halves | 1e-05 |  |
| [[CCNDBP1]] | +0.60 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[EAPP]] | +0.59 | +0.30 / +0.73 | both halves | 2e-04 |  |
| [[SPSB3]] | +0.59 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[WBP1L]] | +0.59 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[COX5B]] | +0.58 | +0.40 / +0.54 | both halves | 4e-05 |  |
| [[MXD4]] | +0.58 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[KLHL7]] | +0.58 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[STARD3]] | +0.58 | +0.62 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYCS]] | -0.52 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[SRSF1]] | -0.49 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[TENM3]] | -0.48 | -0.43 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 187]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.657). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (3.5, -43.8); signed map (-18.9, 11.4). **Vector** length 100, 25.6% of its response variance represented; |z| ≥ 3 in 926 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[PH-797804 (drug)]] 5 µM |  | +3.5 | +3.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.9 | +2.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +0.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.6 | +2.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.5 | +2.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | +0.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.4 | +1.8 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -8.5 | -14.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.3 | -13.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.7 | -12.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -7.4 | -17.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -6.6 | -11.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -5.8 | -7.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.4 | -6.6 |
|  | [[EX229 (drug)]] 5 µM |  | -5.3 | -6.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -5.2 | -5.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.2 | -8.0 |

## What is on record

|  |  |
|---|---|
| Name | reticulophagy regulator family member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.2 — chr17:42,579,513-42,610,623 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp686B1036, FLJ33806; previously FAM134C |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86VR2](https://www.uniprot.org/uniprotkb/Q86VR2) (Reticulophagy regulator 3):

> Endoplasmic reticulum (ER)-anchored autophagy regulator which exists in an inactive state under basal conditions but is activated following cellular stress. When activated, induces ER fragmentation and mediates ER delivery into lysosomes through sequestration into autophagosomes via interaction with ATG8 family proteins. Promotes ER membrane curvature and ER tubulation required for subsequent ER fragmentation and engulfment into autophagosomes. Required for collagen quality control in a LIR …

**Summary**, from NCBI Gene [162427](https://www.ncbi.nlm.nih.gov/gene/162427):

> Predicted to enable endoplasmic reticulum-autophagosome adaptor activity. Involved in endoplasmic reticulum tubular network organization; positive regulation of neuron projection development; and reticulophagy. Located in endoplasmic reticulum tubular network. Part of protein-containing complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27258](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27258) · Entrez [162427](https://www.ncbi.nlm.nih.gov/gene/162427) · UniProt [Q86VR2](https://www.uniprot.org/uniprotkb/Q86VR2) · Ensembl [ENSG00000141699](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141699)

## Data

Gene col 6568: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6568); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6568, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6568]; `tensor/DDL_lfc|DDL_z.npy` [6568]; `embed/gene_vectors.npy` [6568]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6568 or target_col == 6568). Every well: [[RETREG3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RETREG3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
