---
symbol: "ZBTB18"
type: "gene"
col: 11036
ensembl_id: "ENSG00000179456"
name: "zinc finger and BTB domain containing 18"
location: "1q44"
module: 4
arm: "-"
pooled_cpm: 24.98
n_lines_expressing: 49
n_dd_up: 18
n_dd_down: 5
n_dd_up_clean: 9
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# ZBTB18

*zinc finger and BTB domain containing 18* — 1q44

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.78× (z +15.9, q 0e+00, up in 35 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.776× (z -4.7, q 0.001, down in 21 of 45 measured lines) ⚠ cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Clobetasol propionate (drug)]] 0.05 µM: 0.811× (z -4.1, q 0.010, down in 14 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H1573 0.141×, Panc 03.27 0.329×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (HT-29 0.305×, LS 180 0.413×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A498 0.527×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (A498 0.463×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HOXA3]] (+0.55, fdr 2e-05), [[ZNF652]] (+0.55, fdr 3e-05), [[SATB2-AS1]] (+0.54, fdr 2e-05); moves opposite to [[CCT2]] (-0.55, fdr 2e-05), [[HARS1]] (-0.54, fdr 2e-05), [[RBM19]] (-0.54, fdr 1e-05).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 13 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11036.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +15.9 | 0e+00 | 35/45 (HEC-1-A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.42×** | +9.7 | 1e-19 | 27/46 (NCI-H460, CFPAC-1, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.47×** | +7.5 | 1e-11 | 28/45 (SW480, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.40×** | +6.5 | 9e-09 | 26/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.39×** | +6.3 | 3e-08 | 18/47 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.38×** | +6.2 | 4e-08 | 20/46 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.79×** | +5.9 | 2e-07 | 21/47 (LS 180, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +5.9 | 3e-07 | 22/41 (KATO III, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.35×** | +5.8 | 4e-07 | 20/44 (NCI-H23, SW480, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.35×** | +5.8 | 4e-07 | 19/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **1.34×** | +5.5 | 2e-06 | 23/43 (A-172, HOP62, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +5.1 | 2e-05 | 20/47 (NCI-H460, SK-MEL-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.27×** | +4.6 | 2e-04 | 16/47 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.26×** | +4.5 | 3e-04 | 15/46 (SW480, PANC-1, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.20×** | +3.5 | 0.015 | 17/46 (SW480, NCI-H460, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.37×** | +3.2 | 0.044 | 6/46 (NCI-H460, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **1.35×** | +3.0 | 0.070 | 2/43 (C32, RPMI-7951) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11036.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H1573 0.141×, Panc 03.27 0.329×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (HT-29 0.305×, LS 180 0.413×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A498 0.527×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (A498 0.463×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.776×** | -4.7 | 0.001 | 21/45 (SW480, LS 180, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.811×** | -4.1 | 0.010 | 14/46 (A498, Panc 03.27, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.675×** | -4.0 | 0.010 | 8/46 (J82, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.823×** | -3.8 | 0.017 | 16/46 (COLO 205, SW480, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.713×** | -3.5 | 0.056 | 10/27 (LoVo, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.851× | -3.2 | 0.13 | 14/47 (A498, NCI-H23, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.848× | -3.1 | 0.14 | 9/45 (LoVo, A498, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11036. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 15.3 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.42× (z +11.1) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.68× (z +11.0) | — |
| [[A498 (line)]] | wt | 60.0 | 0 | 2 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.527× (z -10.2) |
| [[A549 (line)]] | wt | 16.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +10.0) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +9.9) | — |
| [[HT-29 (line)]] | alt | 39.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.305× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 15.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.203× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 53.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +8.6) ⚠ cell-cycle shift, explains ~51% of this change | [[Dinaciclib (drug)]] 5 µM 0.413× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 18.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.141× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 18.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +14.2) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +9.8) | — |
| [[CFPAC-1 (line)]] | alt | 24.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +10.9) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[HCT15 (line)]] | alt | 28.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +9.2) | — |
| [[HEC-1-A (line)]] | alt | 16.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.54× (z +14.0) | — |
| [[LoVo (line)]] | wt | 23.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +8.5) | — |
| [[NCI-H23 (line)]] | alt | 12.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.179× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~25% of this change |
| [[Panc 03.27 (line)]] | alt | 30.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.329× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 13.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +9.0) | — |
| [[RKO (line)]] | wt | 14.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.25× (z +8.9) | — |
| [[A-172 (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 134 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.23 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 33.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11036), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOXA3]] | +0.55 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[ZNF652]] | +0.55 | +0.57 / +0.46 | both halves | 3e-05 | same gene group |
| [[SATB2-AS1]] | +0.54 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[ATP8B1]] | +0.53 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[PITX2]] | +0.53 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[NR2F1]] | +0.52 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[PURA]] | +0.52 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[CNOT6L]] | +0.52 | +0.40 / +0.51 | both halves | 5e-05 |  |
| [[ZIC2]] | +0.51 | +0.44 / +0.51 | both halves | 3e-05 | same gene group |
| [[CUTA]] | +0.51 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[LCORL]] | +0.51 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[PAIP2B]] | +0.51 | +0.39 / +0.52 | both halves | 6e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCT2]] | -0.55 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[HARS1]] | -0.54 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[RBM19]] | -0.54 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[HERC2P9-1]] | -0.51 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[CCT5]] | -0.50 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[DFFA]] | -0.50 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[TATDN1]] | -0.50 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[PTPN11]] | -0.49 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[FAM83H]] | -0.48 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[FKTN]] | -0.48 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[ABCA15P]] | -0.48 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[PUM3]] | -0.48 | -0.45 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises ZBTB18's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[NR3C2]] | B | NR3C2 activity raises ZBTB18's level | lines that do not express NR3C2 (15) vs lines expressing it (35) | 1.63× lower at baseline in the lines without NR3C2 | 0.072 | ⚠ within organs, on part of the lines; also absent: ENSG00000249631, ENSG00000287292, SATB1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.444). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (14.0, -42.7); signed map (-5.2, 8.0). **Vector** length 83.5, 16.0% of its response variance represented; |z| ≥ 3 in 864 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +15.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.6 | +5.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +2.9 | +9.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +2.6 | +7.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.4 | +1.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +2.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | +2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +1.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | +3.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.8 | +1.9 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -5.3 | -3.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.1 | -3.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | -4.1 | -4.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.6 | -3.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.5 | -2.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.2 | -4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger and BTB domain containing 18 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q44 — chr1:244,048,547-244,057,476 (+) |
| Ensembl biotype | protein_coding |
| Also known as | C2H2-171, TAZ-1, RP58; previously ZNF238 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99592](https://www.uniprot.org/uniprotkb/Q99592) (Zinc finger and BTB domain-containing protein 18):

> Transcriptional repressor that plays a role in various developmental processes such as myogenesis and brain development. Plays a key role in myogenesis by directly repressing the expression of ID2 and ID3, 2 inhibitors of skeletal myogenesis. Also involved in controlling cell division of progenitor cells and regulating the survival of postmitotic cortical neurons. Specifically binds the consensus DNA sequence 5'-[AC]ACATCTG[GT][AC]-3' which contains the E box core, and acts by recruiting …

**Summary**, from NCBI Gene [10472](https://www.ncbi.nlm.nih.gov/gene/10472):

> This gene encodes a C2H2-type zinc finger protein which acts a transcriptional repressor of genes involved in neuronal development. The encoded protein recognizes a specific sequence motif and recruits components of chromatin to target genes. Alternative splicing results in multiple transcript variants. [provided by RefSeq, May 2013]

**Accessions** — [HGNC:13030](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13030) · Entrez [10472](https://www.ncbi.nlm.nih.gov/gene/10472) · UniProt [Q99592](https://www.uniprot.org/uniprotkb/Q99592) · Ensembl [ENSG00000179456](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179456)

## Data

Gene col 11036: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11036); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11036, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11036]; `tensor/DDL_lfc|DDL_z.npy` [11036]; `embed/gene_vectors.npy` [11036]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11036 or target_col == 11036). Every well: [[ZBTB18 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZBTB18.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
