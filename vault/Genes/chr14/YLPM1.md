---
symbol: "YLPM1"
type: "gene"
col: 4082
ensembl_id: "ENSG00000119596"
name: "YLP motif containing 1"
location: "14q24.3"
module: 1
arm: "+"
pooled_cpm: 132.37
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 5
n_dd_up_clean: 7
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# YLPM1

*YLP motif containing 1* — 14q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 1.49× (z +9.4, q 2e-18, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.732× (z -7.7, q 5e-12, down in 35 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (A-427 0.236×, HEC-1-A 0.405×, SNU-1 0.262×, Panc 03.27 0.334×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (NCI-H460 0.601×, A549 0.582×, SNU-1 0.550×, C32 0.604×, …); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (LOX-IMVI 0.370×, C32 0.366×, NCI-H460 0.535×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 1 line (SW480 0.628×); [[Tolmetin (drug)]] 5 µM in 1 line (SW 1088 0.0866×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DIS3L2]] (+0.72, fdr 7e-06), [[LTV1]] (+0.67, fdr 7e-06), [[RAD54L2]] (+0.65, fdr 7e-06); moves opposite to [[CSRP2]] (-0.63, fdr 1e-05), [[MXD1]] (-0.57, fdr 1e-05), [[CXCR4]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ZNF239]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4082.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **1.49×** | +9.4 | 2e-18 | 32/48 (A-427, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.34×** | +7.2 | 1e-10 | 28/48 (Hs 766T, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.21×** | +6.7 | 4e-09 | 23/48 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.65×** | +6.5 | 9e-09 | 34/49 (LoVo, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.28×** | +6.0 | 2e-07 | 28/48 (A498, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.57×** | +5.9 | 4e-07 | 35/48 (C32, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.26×** | +5.6 | 1e-06 | 28/48 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.24×** | +5.3 | 1e-05 | 24/48 (CFPAC-1, RPMI-7951, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.23×** | +5.1 | 3e-05 | 27/48 (CFPAC-1, NCI-H2347, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.21×** | +4.8 | 1e-04 | 25/48 (NCI-H460, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 1.17× | +3.8 | 0.008 | 21/48 (H4, HOP62, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.18× | +3.7 | 0.011 | 20/47 (SW48, NCI-H2347, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.5 | 0.022 | 19/48 (LoVo, C-33 A, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | 1.16× | +3.4 | 0.032 | 19/48 (A-172, NCI-H1792, …) | inconsistent across doses |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.14× | +3.3 | 0.040 | 9/48 (CFPAC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | 1.14× | +3.2 | 0.051 | 14/48 (A549, NCI-H1573, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.13× | +3.1 | 0.072 | 11/48 (NCI-H460, NCI-H1573, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4082.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (A-427 0.236×, HEC-1-A 0.405×, SNU-1 0.262×, Panc 03.27 0.334×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (NCI-H460 0.601×, A549 0.582×, SNU-1 0.550×, C32 0.604×, …); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (LOX-IMVI 0.370×, C32 0.366×, NCI-H460 0.535×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 1 line (SW480 0.628×); [[Tolmetin (drug)]] 5 µM in 1 line (SW 1088 0.0866×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.732×** | -7.7 | 5e-12 | 35/48 (SW480, Panc 03.27, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.810×** | -7.4 | 3e-11 | 27/49 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.775×** | -6.3 | 5e-08 | 28/49 (C-33 A, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.780×** | -5.9 | 4e-07 | 23/44 (A-427, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.774×** | -5.9 | 4e-07 | 26/45 (LOX-IMVI, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 0.867× | -3.6 | 0.034 | 12/49 (CHP-212, HOP62, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.908× | -3.4 | 0.052 | 4/48 (COLO 205, LS 180, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4082. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 146 | 4 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.59× (z +16.5) | [[Dinaciclib (drug)]] 5 µM 0.498× (z -11.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 171 | 1 | 3 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 1.72× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.405× (z -16.5) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 141 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.601× (z -12.5) |
| [[C32 (line)]] | wt | 129 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.366× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.604× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 283 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.537× (z -9.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 161 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.04× (z +8.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.501× (z -9.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SW 1088 (line)]] | alt | 93.5 | 0 | 3 | — | [[Tolmetin (drug)]] 5 µM 0.0866× (z -8.9) |
| [[SW48 (line)]] | wt | 271 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.36× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.456× (z -9.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 185 | 2 | 1 | [[Harringtonine (drug)]] 5 µM 1.65× (z +9.8) | [[Auranofin (drug)]] 5 µM 0.628× (z -9.7) |
| [[A-427 (line)]] | wt | 134 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.05× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.236× (z -20.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 129 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.58× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.582× (z -11.2) |
| [[LS 180 (line)]] | wt | 137 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.10× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.508× (z -9.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 200 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.262× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.550× (z -10.5) |
| [[A498 (line)]] | wt | 78.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +11.7) | — |
| [[C-33 A (line)]] | alt | 212 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.371× (z -13.9) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 103 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.16× (z +8.5) | — |
| [[LOX-IMVI (line)]] | wt | 133 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.370× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 181 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.414× (z -13.7) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 118 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 1.86× (z +8.8) | — |
| [[Panc 03.27 (line)]] | alt | 200 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.334× (z -15.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 97.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.597× (z -8.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 91.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.408× (z -8.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 69.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 152 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 55.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 165 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 108 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 173 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 73.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 67.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 69.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 102 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 117 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 89.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 189 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 148 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4082), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DIS3L2]] | +0.72 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[LTV1]] | +0.67 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[RAD54L2]] | +0.65 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[COA1]] | +0.65 | +0.57 / +0.68 | both halves | 1e-05 |  |
| [[EXOG]] | +0.64 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[THADA]] | +0.63 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[NOL11]] | +0.63 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[NAA25]] | +0.62 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[NOL9]] | +0.62 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[BYSL]] | +0.62 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[DDX10]] | +0.62 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[LAS1L]] | +0.61 | +0.56 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSRP2]] | -0.63 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[MXD1]] | -0.57 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[CXCR4]] | -0.55 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[ERO1B]] | -0.55 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[PNPLA8]] | -0.54 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[FAM117A]] | -0.51 | -0.35 / -0.49 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF239]] | B | ZNF239 activity lowers YLPM1's level | lines that do not express ZNF239 (8) vs lines expressing it (42) | 1.35× higher at baseline in the lines without ZNF239 | 0.079 | ⚠ within organs, on part of the lines |
| [[PUDP]] | C | PUDP activity lowers YLPM1's level | lines that do not express PUDP (4) vs lines expressing it (46) | 1.89× higher at baseline in the lines without PUDP | 0.011 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF264, ENSG00000287188 |
| [[ERO1B]] | C | ERO1B activity raises YLPM1's level | lines that do not express ERO1B (3) vs lines expressing it (47) | 1.72× lower at baseline in the lines without ERO1B | 0.097 | ⚠ few lines (3 vs 47); across organs; also absent: ARHGEF26, ZNF483, RUNDC3A-AS1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.647). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-18.7, -41.0); signed map (-9.5, -47.3). **Vector** length 99.6, 25.7% of its response variance represented; |z| ≥ 3 in 891 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 0.05 µM |  | +3.9 | +3.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.7 | +5.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.0 | +6.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +2.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.6 | -0.7 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +2.3 | +3.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.2 | +1.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.8 | -7.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.0 | -7.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.6 | -3.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | -5.5 | -3.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -2.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.6 | -2.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.3 | -1.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.2 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | YLP motif containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3 — chr14:74,763,316-74,859,435 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ZAP, PPP1R169; previously C14orf170 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [P49750](https://www.uniprot.org/uniprotkb/P49750) (YLP motif-containing protein 1):

> Plays a role in the reduction of telomerase activity during differentiation of embryonic stem cells by binding to the core promoter of TERT and controlling its down-regulation.

**Summary**, from NCBI Gene [56252](https://www.ncbi.nlm.nih.gov/gene/56252):

> Enables RNA binding activity. Predicted to be involved in regulation of telomere maintenance. Predicted to act upstream of or within negative regulation of transcription by RNA polymerase II. Located in nuclear speck. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17798](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17798) · Entrez [56252](https://www.ncbi.nlm.nih.gov/gene/56252) · UniProt [P49750](https://www.uniprot.org/uniprotkb/P49750) · Ensembl [ENSG00000119596](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119596)

## Data

Gene col 4082: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4082); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4082, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4082]; `tensor/DDL_lfc|DDL_z.npy` [4082]; `embed/gene_vectors.npy` [4082]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4082 or target_col == 4082). Every well: [[YLPM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/YLPM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
