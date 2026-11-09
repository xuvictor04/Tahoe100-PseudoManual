---
symbol: "PLA2R1"
type: "gene"
col: 7707
ensembl_id: "ENSG00000153246"
name: "phospholipase A2 receptor 1"
location: "2q24.2"
module: 8
arm: "+"
pooled_cpm: 32.62
n_lines_expressing: 31
n_dd_up: 9
n_dd_down: 38
n_dd_up_clean: 8
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 21
direction_downstream: 7
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# PLA2R1

*phospholipase A2 receptor 1* — 2q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.50× (z +4.1, q 0.022, up in 15 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 38 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.198× (z -24.0, q 0e+00, down in 29 of 29 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MUC16]] (+0.61, fdr 1e-05), [[MUC4]] (+0.60, fdr 2e-05), [[GABRP]] (+0.59, fdr 2e-05); moves opposite to [[DDX50]] (-0.43, fdr 1e-04), [[SNX14]] (-0.40, fdr 1e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 21 arrows point to it, the strongest [[MYOM3]] → it (grade B ⚠); 7 go from it, the strongest it → [[CRYZL2P]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7707.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.50×** | +4.1 | 0.022 | 15/29 (Hs 766T, AsPC-1, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.98×** | +3.8 | 0.033 | 17/29 (AsPC-1, J82, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.43×** | +3.8 | 0.033 | 15/29 (PANC-1, HT-29, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.34×** | +3.6 | 0.043 | 13/29 (AsPC-1, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | **1.40×** | +3.5 | 0.047 | 13/29 (NCI-H1792, PANC-1, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +3.5 | 0.051 | 9/29 (LS 180, PANC-1, …) | rises with dose |  |
| [[Arbutin (drug)]] 0.05 µM |  | **1.42×** | +3.4 | 0.059 | 13/29 (LoVo, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.37×** | +3.3 | 0.059 | 15/29 (AsPC-1, NCI-H1792, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.36×** | +3.3 | 0.067 | 12/29 (LS 180, SW1417, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.23× | +3.0 | 0.12 | 11/29 (AsPC-1, Hs 766T, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.33× | +3.0 | 0.12 | 12/29 (Hs 766T, AsPC-1, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.33× | +3.0 | 0.12 | 9/29 (hTERT-HPNE, HCT15, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 38 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7707.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.198×** | -24.0 | 0e+00 | 29/29 (NCI-H460, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.201×** | -16.2 | 0e+00 | 28/29 (COLO 205, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.216×** | -16.1 | 0e+00 | 28/29 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.292×** | -12.9 | 6e-36 | 27/29 (Hs 766T, Panc 03.27, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.296×** | -12.8 | 3e-35 | 27/29 (HT-29, LoVo, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.299×** | -12.6 | 1e-34 | 29/29 (HT-29, LoVo, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.334×** | -11.5 | 2e-28 | 26/28 (NCI-H460, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.343×** | -11.2 | 2e-27 | 24/29 (HT-29, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.517×** | -9.8 | 9e-21 | 22/29 (LoVo, HT-29, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.413×** | -9.2 | 1e-18 | 28/29 (LoVo, HCT15, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.432×** | -8.8 | 9e-17 | 27/29 (LoVo, BT-474, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.458×** | -8.2 | 1e-14 | 28/29 (HT-29, Hs 766T, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.481×** | -7.7 | 8e-13 | 24/29 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.507×** | -7.1 | 5e-11 | 23/29 (HT-29, COLO 205, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | **0.522×** | -6.5 | 2e-09 | 21/28 (Panc 03.27, RPMI-7951, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.335×** | -6.0 | 7e-08 | 23/29 (HEC-1-A, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~25% here); composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.392×** | -5.1 | 1e-05 | 23/29 (HT-29, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.402×** | -5.0 | 2e-05 | 20/29 (HEC-1-A, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.550×** | -4.5 | 2e-04 | 19/29 (LoVo, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.463×** | -4.2 | 6e-04 | 18/29 (NCI-H1792, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.668×** | -4.2 | 6e-04 | 15/29 (HT-29, CFPAC-1, …) | two highest doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.491×** | -3.9 | 0.002 | 17/29 (A498, HOP62, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **0.502×** | -3.8 | 0.003 | 18/29 (NCI-H1792, LoVo, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.59 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7707. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 174 | 0 | 17 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0743× (z -24.4) |
| [[LoVo (line)]] | wt | 51.2 | 0 | 16 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -24.8) |
| [[HEC-1-A (line)]] | alt | 32.8 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -16.1) |
| [[NCI-H1792 (line)]] | alt | 54.4 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0581× (z -25.5) |
| [[Panc 03.27 (line)]] | alt | 49.5 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -19.4) |
| [[A549 (line)]] | wt | 36.1 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0507× (z -23.8) |
| [[AsPC-1 (line)]] | alt | 166 | 1 | 8 (4 ⚠) | [[Trametinib (drug)]] 0.05 µM 2.25× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -25.4) |
| [[Hs 766T (line)]] | wt | 94.1 | 1 | 8 (5 ⚠) | [[Trametinib (drug)]] 0.05 µM 2.47× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -22.1) |
| [[NCI-H23 (line)]] | alt | 19.2 | 0 | 9 (6 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0615× (z -13.5) |
| [[NCI-H460 (line)]] | wt | 81.2 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0308× (z -33.1) |
| [[BT-474 (line)]] | alt | 41.4 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -13.7) |
| [[COLO 205 (line)]] | alt | 56.5 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0383× (z -30.6) |
| [[SW1417 (line)]] | alt | 35.6 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0842× (z -23.4) |
| [[HOP62 (line)]] | alt | 33.7 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -13.7) |
| [[RPMI-7951 (line)]] | alt | 61.9 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0984× (z -21.4) |
| [[A498 (line)]] | wt | 43.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -16.4) |
| [[CFPAC-1 (line)]] | alt | 45.2 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -18.2) |
| [[HCT15 (line)]] | alt | 17.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0683× (z -15.7) |
| [[J82 (line)]] | alt | 26.3 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0727× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -9.5) |
| [[HS-578T (line)]] | alt | 60.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 13.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -12.4) |
| [[A-172 (line)]] | wt | 16.9 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.206× (z -8.8) ⚠ cell-cycle shift, explains ~32% of this change |
| [[hTERT-HPNE (line)]] | wt | 22.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.154× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[PANC-1 (line)]] | alt | 12.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -12.9) |
| [[SW48 (line)]] | wt | 21.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0743× (z -14.0) |
| [[A-427 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.23 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.61 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.47 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.17 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.83 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.68 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.23 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 8.42 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.40 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.62 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.99 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.05 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.73 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.81 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.10 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.70 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 3.14 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.32 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7707), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MUC16]] | +0.61 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[MUC4]] | +0.60 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[GABRP]] | +0.59 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[GPRIN2]] | +0.58 | +0.63 / +0.47 | both halves | 2e-05 | **novel candidate** |
| [[TM4SF4]] | +0.57 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[PLSCR4]] | +0.57 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[DAPK1]] | +0.56 | +0.55 / +0.45 | both halves | 3e-05 | **novel candidate** |
| [[CRYZL2P]] | +0.55 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[SEC16B]] | +0.54 | +0.50 / +0.43 | both halves | 3e-05 |  |
| [[TRIM31]] | +0.53 | +0.40 / +0.54 | both halves | 5e-05 |  |
| [[ALDH3B1]] | +0.53 | +0.51 / +0.37 | both halves | 7e-05 |  |
| [[CATSPERB]] | +0.53 | +0.42 / +0.57 | both halves | 4e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX50]] | -0.43 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[SNX14]] | -0.40 | -0.38 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 18, C 3. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYOM3]] | B | MYOM3 activity raises PLA2R1's level | lines that do not express MYOM3 (27) vs lines expressing it (23) | 2.62× lower at baseline in the lines without MYOM3 | 0.003 | ⚠ within organs, on part of the lines; also absent: HNF4A, EPS8L3, USH1C |
| [[SEC16B]] | B | SEC16B activity raises PLA2R1's level | lines that do not express SEC16B (13) vs lines expressing it (37) | 2.95× lower at baseline in the lines without SEC16B | 0.005 | ⚠ within organs, on part of the lines; also absent: CRYZL2P, CYP2S1, GRHL3 |
| [[DPP4]] | B | DPP4 activity raises PLA2R1's level | lines that do not express DPP4 (29) vs lines expressing it (21) | 3.03× lower at baseline in the lines without DPP4 | 0.009 | ⚠ within organs, on part of the lines; also absent: LCN2, INAVA, KLK10 |
| [[UGT1A1]] | B | UGT1A1 activity raises PLA2R1's level | lines that do not express UGT1A1 (36) vs lines expressing it (14) | 2.72× lower at baseline in the lines without UGT1A1 | 0.012 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, NPSR1 |
| [[UGT1A6]] | B | UGT1A6 activity raises PLA2R1's level | lines that do not express UGT1A6 (35) vs lines expressing it (15) | 2.75× lower at baseline in the lines without UGT1A6 | 0.024 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A9, NPSR1 |
| [[CRYZL2P]] | B | CRYZL2P activity raises PLA2R1's level | lines that do not express CRYZL2P (14) vs lines expressing it (36) | 2.81× lower at baseline in the lines without CRYZL2P | 0.032 | ⚠ within organs, on part of the lines; also absent: SEC16B |
| [[VNN1]] | B | VNN1 activity strengthens PLA2R1's drug response | lines that do not express VNN1 (16) vs lines expressing it (13) | the lines without VNN1 respond 0.70× as strongly (z diff +2.76); strongest at Homoharringtonine 0.5 µM: 0.33x vs 0.24x (z diff +3.6) | 0.033 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ENSG00000259925, MUC5B; target measured in part of the lines; artifact flags |
| [[IGFL2-AS1]] | B | IGFL2-AS1 activity raises PLA2R1's level | lines that do not express IGFL2-AS1 (36) vs lines expressing it (14) | 3.38× lower at baseline in the lines without IGFL2-AS1 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALB1, CLRN3, LINC01559 |
| [[MUC13]] | B | MUC13 activity raises PLA2R1's level | lines that do not express MUC13 (40) vs lines expressing it (10) | 2.69× lower at baseline in the lines without MUC13 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, NPSR1, CDH17 |
| [[AQP3]] | B | AQP3 activity raises PLA2R1's level | lines that do not express AQP3 (19) vs lines expressing it (31) | 2.43× lower at baseline in the lines without AQP3 | 0.048 | ⚠ within organs, on part of the lines; also absent: ABCC3, ELF3, CD24; maybe low, not absent |
| [[TRIM31]] | B | TRIM31 activity raises PLA2R1's level | lines that do not express TRIM31 (39) vs lines expressing it (11) | 2.85× lower at baseline in the lines without TRIM31 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, GCNT3, NPSR1 |
| [[ALDH3B1]] | B | ALDH3B1 activity raises PLA2R1's level | lines that do not express ALDH3B1 (9) vs lines expressing it (41) | 2.87× lower at baseline in the lines without ALDH3B1 | 0.060 | ⚠ within organs, on part of the lines; also absent: NIBAN2, IER3, FOSL1; maybe low, not absent |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CRYZL2P]] | B | PLA2R1 activity raises CRYZL2P's level | lines that do not express PLA2R1 (19) vs lines expressing it (31) | 1.79× lower at baseline in the lines without PLA2R1 | 0.043 | ⚠ within organs, on part of the lines; also absent: CYP2S1, RARRES1, IL18 |
| [[PRR15]] | B | PLA2R1 activity raises PRR15's level | lines that do not express PLA2R1 (19) vs lines expressing it (31) | 1.76× lower at baseline in the lines without PLA2R1 | 0.052 | ⚠ within organs, on part of the lines; also absent: CYP2S1, RARRES1, IL18 |
| [[SEC16B]] | B | PLA2R1 activity raises SEC16B's level | lines that do not express PLA2R1 (19) vs lines expressing it (31) | 1.55× lower at baseline in the lines without PLA2R1 | 0.067 | ⚠ within organs, on part of the lines; also absent: CYP2S1, RARRES1, IL18 |
| [[MYOM3]] | B | PLA2R1 activity raises MYOM3's level | lines that do not express PLA2R1 (19) vs lines expressing it (31) | 1.61× lower at baseline in the lines without PLA2R1 | 0.068 | ⚠ within organs, on part of the lines; also absent: CYP2S1, RARRES1, IL18 |
| [[VILL]] | B | PLA2R1 activity raises VILL's level | lines that do not express PLA2R1 (19) vs lines expressing it (31) | 1.32× lower at baseline in the lines without PLA2R1 | 0.092 | ⚠ within organs, on part of the lines; also absent: CYP2S1, RARRES1, IL18 |
| [[POU5F1]] | C | PLA2R1 activity raises POU5F1's level | lines that do not express PLA2R1 (19) vs lines expressing it (31) | 2.77× lower at baseline in the lines without PLA2R1 | 0.027 | ⚠ within organs, on part of the lines; also absent: CYP2S1, RARRES1, IL18; co-absent with the target |
| [[RARRES1]] | C | PLA2R1 activity raises RARRES1's level | lines that do not express PLA2R1 (19) vs lines expressing it (31) | 1.85× lower at baseline in the lines without PLA2R1 | 0.064 | ⚠ within organs, on part of the lines; also absent: CYP2S1, RARRES1, IL18; co-absent with the target |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.532). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.1, 56.3); signed map (62.4, 0.5). **Vector** length 81.4, 22.4% of its response variance represented; |z| ≥ 3 in 1,028 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.1 | +2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +3.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.9 | +1.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.8 | -0.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +4.0 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +0.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.1 | +3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.6 | +2.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.5 | +1.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.4 | -8.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.2 | -5.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.8 | -4.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -2.7 | -12.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.6 | -4.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.1 | -3.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.0 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | phospholipase A2 receptor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q24.2 — chr2:159,932,006-160,062,615 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PLA2G1R, PLA2IR, PLA2-R, CLEC13C |
| Gene groups (HGNC) | C-type lectin domain containing |
| Reactome | 9 pathways, smallest: Acyl chain remodelling of PI; Acyl chain remodelling of PG; Acyl chain remodelling of PS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13018](https://www.uniprot.org/uniprotkb/Q13018) (Secretory phospholipase A2 receptor):

> Receptor for secretory phospholipase A2 (sPLA2). Acts as a receptor for phospholipase sPLA2-IB/PLA2G1B but not sPLA2-IIA/PLA2G2A. Also able to bind to snake PA2-like toxins. Although its precise function remains unclear, binding of sPLA2 to its receptor participates in both positive and negative regulation of sPLA2 functions as well as clearance of sPLA2. Binding of sPLA2-IB/PLA2G1B induces various effects depending on the cell type, such as activation of the mitogen-activated protein kinase …

**Summary**, from NCBI Gene [22925](https://www.ncbi.nlm.nih.gov/gene/22925):

> This gene represents a phospholipase A2 receptor. The encoded protein likely exists as both a transmembrane form and a soluble form. The transmembrane receptor may play a role in clearance of phospholipase A2, thereby inhibiting its action. Polymorphisms at this locus have been associated with susceptibility to idiopathic membranous nephropathy. Alternatively spliced transcript variants encoding different isoforms have been identified.[provided by RefSeq, Sep 2010]

**Accessions** — [HGNC:9042](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9042) · Entrez [22925](https://www.ncbi.nlm.nih.gov/gene/22925) · UniProt [Q13018](https://www.uniprot.org/uniprotkb/Q13018) · Ensembl [ENSG00000153246](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153246)

## Data

Gene col 7707: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7707); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7707, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7707]; `tensor/DDL_lfc|DDL_z.npy` [7707]; `embed/gene_vectors.npy` [7707]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7707 or target_col == 7707). Every well: [[PLA2R1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLA2R1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
