---
symbol: "DHX40"
type: "gene"
col: 2943
ensembl_id: "ENSG00000108406"
name: "DEAH-box helicase 40"
location: "17q23.1"
module: 74
arm: "+"
pooled_cpm: 78.06
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 29
n_dd_up_clean: 2
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# DHX40

*DEAH-box helicase 40* — 17q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[NG25 (drug)]] 5 µM: 1.68× (z +5.8, q 4e-06, up in 33 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.473× (z -22.5, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC28A]] (+0.65, fdr 7e-06), [[PHF3]] (+0.62, fdr 7e-06), [[LTN1]] (+0.61, fdr 1e-05); moves opposite to [[ARSB]] (-0.54, fdr 4e-05), [[TIMM23B-AGAP6]] (-0.53, fdr 2e-05), [[HNRNPAB]] (-0.52, fdr 3e-05).
> It is in [[Module 074]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2943.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM |  | **1.68×** | +5.8 | 4e-06 | 33/47 (BT-474, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.32×** | +4.2 | 0.008 | 23/48 (LS 180, LoVo, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 1.13× | +3.7 | 0.042 | 7/48 (A-427, BT-474, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 1.18× | +3.6 | 0.043 | 19/48 (BT-474, LoVo, …) | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.25×** | +3.5 | 0.060 | 15/47 (HCT15, COLO 205, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.17× | +3.3 | 0.081 | 21/49 (HT-29, HEC-1-A, …) | rises with dose | composition shift |
| [[Ixazomib (drug)]] 5 µM |  | 1.33× | +3.2 | 0.12 | 11/48 (KATO III, HOP62, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | 1.16× | +3.1 | 0.13 | 10/48 (NCI-H23, HEC-1-A, …) | top dose only | plate-row cell shift; position effect removed |
| [[Silodosin (drug)]] 5 µM |  | 1.16× | +3.1 | 0.13 | 12/47 (A498, LS 180, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | 1.31× | +3.0 | 0.15 | 12/49 (BT-474, A498, …) | two highest doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2943.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.473×** | -22.5 | 0e+00 | 46/48 (SNU-423, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~8% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.560×** | -12.3 | 4e-32 | 47/48 (CFPAC-1, NCI-H2347, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.609×** | -10.5 | 2e-23 | 42/48 (LOX-IMVI, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.654×** | -8.6 | 9e-16 | 42/48 (NCI-H460, H4, …) | top dose only | cell-cycle shift (explains ~22% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.760×** | -8.2 | 3e-14 | 31/48 (MIA PaCa-2, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.686×** | -8.0 | 2e-13 | 34/48 (C-33 A, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.694×** | -7.7 | 9e-13 | 33/48 (C32, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.897× | -7.7 | 9e-13 | 1/50 (RPMI-7951) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.699×** | -7.6 | 2e-12 | 32/48 (SNU-423, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.736×** | -6.2 | 3e-08 | 29/48 (SNU-1, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.708×** | -5.9 | 2e-07 | 28/48 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.606×** | -5.6 | 1e-06 | 31/48 (COLO 205, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.763×** | -5.5 | 2e-06 | 29/50 (H4, C32, …) | rises with dose | position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.634×** | -5.0 | 2e-05 | 31/48 (A498, LOX-IMVI, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.639×** | -5.0 | 3e-05 | 30/48 (NCI-H1792, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.732×** | -4.7 | 9e-05 | 30/48 (C-33 A, NCI-H1792, …) | all doses, flat | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.657×** | -4.7 | 1e-04 | 25/48 (COLO 205, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.806×** | -4.5 | 2e-04 | 25/47 (H4, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.784×** | -4.5 | 2e-04 | 27/48 (NCI-H1792, SW48, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2943. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 102 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -19.3) |
| [[SNU-423 (line)]] | alt | 103 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.265× (z -21.3) |
| [[MIA PaCa-2 (line)]] | alt | 127 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -27.4) |
| [[PANC-1 (line)]] | alt | 53.2 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.500× (z -12.6) |
| [[A-172 (line)]] | wt | 89.1 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.511× (z -10.7) |
| [[A498 (line)]] | wt | 99.5 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.567× (z -10.9) |
| [[C-33 A (line)]] | alt | 83.2 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.479× (z -9.8) |
| [[CFPAC-1 (line)]] | alt | 106 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -16.2) |
| [[H4 (line)]] | wt | 118 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.218× (z -13.4) |
| [[LOX-IMVI (line)]] | wt | 66.3 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.466× (z -12.6) |
| [[CHP-212 (line)]] | wt | 203 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.349× (z -12.7) |
| [[COLO 205 (line)]] | alt | 54.8 | 0 | 2 | — | [[venetoclax (drug)]] 5 µM 0.0568× (z -12.4) |
| [[HOP62 (line)]] | alt | 64.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -12.9) |
| [[HS-578T (line)]] | alt | 66.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.516× (z -9.9) |
| [[hTERT-HPNE (line)]] | wt | 75.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -10.5) |
| [[NCI-H23 (line)]] | alt | 100 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -10.6) |
| [[NCI-H460 (line)]] | wt | 76.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -16.2) |
| [[RPMI-7951 (line)]] | alt | 67.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -12.0) |
| [[SNU-1 (line)]] | wt | 97.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -14.0) |
| [[SW 900 (line)]] | alt | 83.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -11.0) |
| [[SW48 (line)]] | wt | 57.1 | 0 | 2 | — | [[TAK-901 (drug)]] 0.05 µM 0.194× (z -10.2) |
| [[SW480 (line)]] | alt | 78.8 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -14.4) |
| [[A549 (line)]] | wt | 112 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.482× (z -13.1) |
| [[AN3 CA (line)]] | alt | 93.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.196× (z -13.5) |
| [[AsPC-1 (line)]] | alt | 34.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -8.9) |
| [[BT-474 (line)]] | alt | 191 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.483× (z -12.4) |
| [[HEC-1-A (line)]] | alt | 83.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.602× (z -8.7) |
| [[Hs 766T (line)]] | wt | 45.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -9.2) |
| [[KATO III (line)]] | alt | 91.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -14.6) |
| [[LoVo (line)]] | wt | 46.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.499× (z -11.3) |
| [[LS 180 (line)]] | wt | 48.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -12.8) |
| [[NCI-H1792 (line)]] | alt | 132 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -14.7) |
| [[NCI-H2030 (line)]] | alt | 67.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.521× (z -10.1) |
| [[NCI-H2347 (line)]] | alt | 86.9 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.507× (z -9.6) ⚠ unreliable plate only |
| [[Panc 03.27 (line)]] | alt | 67.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -15.1) |
| [[RKO (line)]] | wt | 42.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -10.1) |
| [[SHP-77 (line)]] | alt | 70.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -10.1) |
| [[SK-MEL-2 (line)]] | alt | 127 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.452× (z -12.1) |
| [[A-427 (line)]] | wt | 118 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 74.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 82.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 72.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 75.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 36.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2943), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC28A]] | +0.65 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[PHF3]] | +0.62 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[LTN1]] | +0.61 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[CRBN]] | +0.60 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[PJA2]] | +0.60 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[TBC1D17]] | +0.58 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[CFAP36]] | +0.58 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[SCAMP1]] | +0.58 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[UBE2B]] | +0.57 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[ACTR6]] | +0.57 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[IK]] | +0.56 | +0.33 / +0.60 | both halves | 1e-04 |  |
| [[MXI1]] | +0.55 | +0.59 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARSB]] | -0.54 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[TIMM23B-AGAP6]] | -0.53 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[HNRNPAB]] | -0.52 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[PRDM15]] | -0.52 | -0.39 / -0.46 | both halves | 6e-05 |  |
| [[CCNJ]] | -0.52 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[TLNRD1]] | -0.51 | -0.53 / -0.39 | both halves | 6e-05 |  |
| [[E2F3]] | -0.51 | -0.48 / -0.40 | both halves | 4e-05 |  |
| [[MRM1]] | -0.50 | -0.46 / -0.36 | both halves | 1e-04 |  |
| [[SLFNL1-AS1]] | -0.50 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[SATB2]] | -0.49 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[GATAD2A]] | -0.49 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[SLC20A2]] | -0.48 | -0.42 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.589). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-3.1, -48.0); signed map (-17.1, 7.4). **Vector** length 118, 33.4% of its response variance represented; |z| ≥ 3 in 1,008 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.0 | -2.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | -2.2 |
|  | [[NG25 (drug)]] 5 µM |  | +4.1 | +5.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +2.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.0 | +2.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.8 | +3.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.8 | +4.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +3.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.7 | +1.5 |
|  | [[Glycyrrhizic acid (drug)]] 5 µM |  | +2.3 | +2.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.4 | -22.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.7 | -12.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.4 | -8.6 |
|  | [[EX229 (drug)]] 5 µM |  | -5.0 | -5.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.9 | -4.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.7 | -5.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.5 | -5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.0 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | DEAH-box helicase 40 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q23.1 — chr17:59,565,558-59,608,345 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ARG147, PAD, FLJ22060; previously DDX40 |
| Gene groups (HGNC) | DEAH-box helicases; NTC associated proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IX18](https://www.uniprot.org/uniprotkb/Q8IX18) (Probable ATP-dependent RNA helicase DHX40):

> Probable ATP-dependent RNA helicase.

**Summary**, from NCBI Gene [79665](https://www.ncbi.nlm.nih.gov/gene/79665):

> This gene encodes a member of the DExH/D box family of ATP-dependent RNA helicases that have an essential role in RNA metabolism. Alternate splicing results in multiple transcript variants. A pseudogene of this gene is found on chromosome 17.[provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:18018](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18018) · Entrez [79665](https://www.ncbi.nlm.nih.gov/gene/79665) · UniProt [Q8IX18](https://www.uniprot.org/uniprotkb/Q8IX18) · Ensembl [ENSG00000108406](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108406)

## Data

Gene col 2943: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2943); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2943, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2943]; `tensor/DDL_lfc|DDL_z.npy` [2943]; `embed/gene_vectors.npy` [2943]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2943 or target_col == 2943). Every well: [[DHX40 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DHX40.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
