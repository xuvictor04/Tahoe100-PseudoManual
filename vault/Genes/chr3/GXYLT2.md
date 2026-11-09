---
symbol: "GXYLT2"
type: "gene"
col: 10326
ensembl_id: "ENSG00000172986"
name: "glucoside xylosyltransferase 2"
location: "3p13"
module: 45
arm: "+"
pooled_cpm: 21.91
n_lines_expressing: 39
n_dd_up: 31
n_dd_down: 39
n_dd_up_clean: 28
n_dd_down_clean: 33
in_vector_space: true
direction_upstream: 17
direction_downstream: 24
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# GXYLT2

*glucoside xylosyltransferase 2* — 3p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.71× (z +11.1, q 6e-26, up in 28 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 39 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.484× (z -10.6, q 2e-23, down in 26 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HMGN3]] (+0.62, fdr 1e-05), [[DPYSL3]] (+0.60, fdr 1e-05), [[FAM229B]] (+0.60, fdr 1e-05); moves opposite to [[ENOX2]] (-0.53, fdr 5e-05), [[MYH3]] (-0.50, fdr 1e-04), [[TLNRD1]] (-0.50, fdr 3e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[LINC01583]] → it (grade B ⚠); 24 go from it, the strongest it → [[GLIS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10326.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.71×** | +11.1 | 6e-26 | 28/37 (HEC-1-A, SW1417, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.85×** | +8.7 | 1e-15 | 23/36 (HOP62, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.79×** | +8.6 | 2e-15 | 27/37 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.79×** | +8.5 | 3e-15 | 20/32 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.64×** | +7.3 | 5e-11 | 25/37 (HEC-1-A, SW1417, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.42×** | +6.2 | 5e-08 | 18/37 (SW480, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **2.33×** | +6.2 | 5e-08 | 25/37 (LoVo, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +6.1 | 8e-08 | 15/24 (C32, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.49×** | +5.6 | 1e-06 | 18/37 (HOP62, SW480, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.45×** | +5.5 | 2e-06 | 17/37 (HOP62, J82, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.46×** | +5.5 | 2e-06 | 20/37 (SW480, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **1.40×** | +5.4 | 3e-06 | 19/37 (HOP62, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.30×** | +5.3 | 5e-06 | 17/37 (HOP62, SW480, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.30×** | +5.3 | 5e-06 | 19/37 (SW480, HOP62, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.42×** | +5.1 | 1e-05 | 20/36 (HOP62, SW480, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.34×** | +5.1 | 1e-05 | 17/37 (HOP62, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.41×** | +5.1 | 1e-05 | 14/37 (NCI-H1573, LoVo, …) | rises with dose | cell-cycle shift (explains ~2% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 39 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10326.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.484×** | -10.6 | 2e-23 | 26/35 (RPMI-7951, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.499×** | -9.8 | 3e-20 | 28/33 (HS-578T, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.641×** | -9.2 | 7e-18 | 25/37 (RPMI-7951, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.549×** | -8.8 | 3e-16 | 23/37 (PANC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.552×** | -8.7 | 4e-16 | 26/37 (A-172, A549, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.555×** | -8.6 | 6e-16 | 24/37 (RPMI-7951, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.570×** | -8.2 | 1e-14 | 27/37 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.571×** | -8.2 | 2e-14 | 28/37 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.592×** | -7.7 | 1e-12 | 25/37 (HCT15, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.593×** | -7.7 | 1e-12 | 25/37 (LOX-IMVI, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.620×** | -7.0 | 1e-10 | 22/36 (NCI-H1792, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.630×** | -6.8 | 7e-10 | 23/37 (PANC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.624×** | -6.6 | 1e-09 | 20/37 (SK-MEL-2, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.731×** | -6.5 | 4e-09 | 20/37 (H4, RPMI-7951, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.644×** | -6.4 | 5e-09 | 23/37 (A-172, H4, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.737×** | -6.3 | 9e-09 | 24/37 (A-172, SNU-423, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.664×** | -6.0 | 7e-08 | 20/37 (SK-MEL-2, C32, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.682×** | -5.6 | 7e-07 | 20/36 (RPMI-7951, A-172, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10326. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 58.5 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -10.0) |
| [[LOX-IMVI (line)]] | wt | 44.7 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -12.4) |
| [[RPMI-7951 (line)]] | alt | 139 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -18.1) |
| [[A-172 (line)]] | wt | 37.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -11.4) |
| [[HOP62 (line)]] | alt | 37.1 | 4 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.70× (z +13.8) ⚠ position not correctable · without an alert: [[Cobimetinib (drug)]] 5 µM 4.11× (z +9.8) | — |
| [[AN3 CA (line)]] | alt | 81.1 | 0 | 3 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.107× (z -11.9) |
| [[SW480 (line)]] | alt | 24.7 | 2 | 1 (1 ⚠) | [[Binimetinib (drug)]] 0.05 µM 2.35× (z +9.4) | [[Niclosamide (olamine) (drug)]] 5 µM 0.321× (z -8.7) ⚠ toxic |
| [[A549 (line)]] | wt | 16.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -10.6) |
| [[H4 (line)]] | wt | 39.4 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.164× (z -9.5) ⚠ toxic · without an alert: [[Selinexor (drug)]] 5 µM 0.303× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 35.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.225× (z -11.4) |
| [[SNU-423 (line)]] | alt | 86.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -14.8) |
| [[A-427 (line)]] | wt | 13.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -9.5) |
| [[A498 (line)]] | wt | 65.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.505× (z -10.3) |
| [[HEC-1-A (line)]] | alt | 17.8 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.62× (z +9.8) | — |
| [[HS-578T (line)]] | alt | 27.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.178× (z -11.4) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 11.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.90× (z +10.0) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 7.49 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.112× (z -8.9) |
| [[PANC-1 (line)]] | alt | 18.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -13.0) |
| [[SW1417 (line)]] | alt | 7.31 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.43× (z +9.0) | — |
| [[AsPC-1 (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.68 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.65 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.25 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.11 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.03 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10326), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMGN3]] | +0.62 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[DPYSL3]] | +0.60 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[FAM229B]] | +0.60 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[RARB]] | +0.60 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[CAT]] | +0.60 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[OLFML2A]] | +0.59 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[NREP]] | +0.58 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[SCPEP1]] | +0.58 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[NIPSNAP1]] | +0.57 | +0.40 / +0.57 | both halves | 5e-05 |  |
| [[CDON]] | +0.57 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[TMEM14A]] | +0.56 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[TTLL7]] | +0.56 | +0.45 / +0.58 | both halves | 3e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENOX2]] | -0.53 | -0.39 / -0.48 | both halves | 5e-05 |  |
| [[MYH3]] | -0.50 | -0.40 / -0.32 | both halves | 1e-04 |  |
| [[TLNRD1]] | -0.50 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[HSD17B2-AS1]] | -0.49 | -0.42 / -0.31 | both halves | 2e-04 |  |
| [[DPH5-DT]] | -0.48 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[AOC2]] | -0.47 | -0.40 / -0.28 | both halves | 3e-04 |  |
| [[SMIM12]] | -0.47 | -0.36 / -0.35 | both halves | 1e-04 |  |
| [[E2F3]] | -0.47 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[NOP16]] | -0.47 | -0.40 / -0.43 | both halves | 4e-05 |  |
| [[GNG12-AS1]] | -0.46 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[SMUG1]] | -0.46 | -0.34 / -0.28 | both halves | 3e-04 |  |
| [[NUP50-DT]] | -0.46 | -0.31 / -0.39 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 16, C 1. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01583]] | B | LINC01583 activity raises GXYLT2's level | lines that do not express LINC01583 (28) vs lines expressing it (22) | 3.25× lower at baseline in the lines without LINC01583 | 0.006 | ⚠ within organs, on part of the lines; also absent: INSYN2B, ADAM12, ZEB2 |
| [[ARHGEF6]] | B | ARHGEF6 activity raises GXYLT2's level | lines that do not express ARHGEF6 (20) vs lines expressing it (30) | 3.19× lower at baseline in the lines without ARHGEF6 | 0.013 | ⚠ within organs, on part of the lines; also absent: SRPX, MSRB3, ENSG00000230615; maybe low, not absent |
| [[GLIS1]] | B | GLIS1 activity raises GXYLT2's level | lines that do not express GLIS1 (24) vs lines expressing it (26) | 3.02× lower at baseline in the lines without GLIS1 | 0.028 | ⚠ within organs, on part of the lines; also absent: CPEB1, SPOCK1, DZIP1; maybe low, not absent |
| [[HOOK1]] | B | HOOK1 activity lowers GXYLT2's level | lines that do not express HOOK1 (22) vs lines expressing it (28) | 2.18× higher at baseline in the lines without HOOK1 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SMPDL3B, BSPRY, SPINT1-AS1 |
| [[PKIG]] | B | PKIG activity raises GXYLT2's level | lines that do not express PKIG (6) vs lines expressing it (44) | 4.55× lower at baseline in the lines without PKIG | 0.039 | ⚠ within organs, on part of the lines; also absent: GPR155, TTC7B, CIBAR1 |
| [[SDC2]] | B | SDC2 activity raises GXYLT2's level | lines that do not express SDC2 (26) vs lines expressing it (24) | 2.46× lower at baseline in the lines without SDC2 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GDNF-AS1, TENM2, AMPH |
| [[SLC8A1]] | B | SLC8A1 activity raises GXYLT2's level | lines that do not express SLC8A1 (26) vs lines expressing it (24) | 2.57× lower at baseline in the lines without SLC8A1 | 0.054 | ⚠ within organs, on part of the lines; also absent: DPY19L2, MAGI2, MAGI2-AS3 |
| [[KCTD16]] | B | KCTD16 activity raises GXYLT2's level | lines that do not express KCTD16 (18) vs lines expressing it (32) | 3.32× lower at baseline in the lines without KCTD16 | 0.055 | ⚠ within organs, on part of the lines; also absent: DMD, DOCK2, PRKD1; maybe low, not absent |
| [[LAYN]] | B | LAYN activity raises GXYLT2's level | lines that do not express LAYN (31) vs lines expressing it (19) | 2.07× lower at baseline in the lines without LAYN | 0.055 | ⚠ within organs, on part of the lines; also absent: COL1A1, ITGA11, LUM |
| [[FBN1]] | B | FBN1 activity raises GXYLT2's level | lines that do not express FBN1 (28) vs lines expressing it (22) | 2.84× lower at baseline in the lines without FBN1 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GYPC, TENM2, ENSG00000280241 |
| [[SLIT3]] | B | SLIT3 activity raises GXYLT2's level | lines that do not express SLIT3 (31) vs lines expressing it (19) | 2.19× lower at baseline in the lines without SLIT3 | 0.069 | ⚠ within organs, on part of the lines; also absent: GLYATL2, KIRREL3, NTRK3 |
| [[SPARC]] | B | SPARC activity raises GXYLT2's level | lines that do not express SPARC (34) vs lines expressing it (16) | 3.36× lower at baseline in the lines without SPARC | 0.071 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, MMP2, ENSG00000222032 |

### Downstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 23, C 1. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GLIS1]] | B | GXYLT2 activity raises GLIS1's level | lines that do not express GXYLT2 (11) vs lines expressing it (39) | 3.68× lower at baseline in the lines without GXYLT2 | 0.009 | ⚠ within organs, on part of the lines; also absent: TMEM145, SLC17A7, FAM171B |
| [[ARHGEF6]] | B | GXYLT2 activity raises ARHGEF6's level | lines that do not express GXYLT2 (11) vs lines expressing it (39) | 2.70× lower at baseline in the lines without GXYLT2 | 0.013 | ⚠ within organs, on part of the lines; also absent: TMEM145, SLC17A7, FAM171B |
| [[TTLL7]] | B | GXYLT2 activity raises TTLL7's level | lines that do not express GXYLT2 (11) vs lines expressing it (39) | 3.84× lower at baseline in the lines without GXYLT2 | 0.014 | ⚠ within organs, on part of the lines; also absent: TMEM145, SLC17A7, FAM171B |
| [[ATRNL1]] | B | GXYLT2 activity raises ATRNL1's level | lines that do not express GXYLT2 (11) vs lines expressing it (39) | 2.89× lower at baseline in the lines without GXYLT2 | 0.016 | ⚠ within organs, on part of the lines; also absent: TMEM145, SLC17A7, FAM171B |
| [[PKIG]] | B | GXYLT2 activity raises PKIG's level | lines that do not express GXYLT2 (11) vs lines expressing it (39) | 2.64× lower at baseline in the lines without GXYLT2 | 0.023 | ⚠ within organs, on part of the lines; also absent: TMEM145, SLC17A7, FAM171B |
| [[SDC2]] | B | GXYLT2 activity raises SDC2's level | lines that do not express GXYLT2 (11) vs lines expressing it (39) | 4.84× lower at baseline in the lines without GXYLT2 | 0.028 | ⚠ within organs, on part of the lines; also absent: TMEM145, SLC17A7, FAM171B |
| [[FAM229B]] | B | GXYLT2 activity raises FAM229B's level | lines that do not express GXYLT2 (11) vs lines expressing it (39) | 2.12× lower at baseline in the lines without GXYLT2 | 0.038 | ⚠ within organs, on part of the lines; also absent: TMEM145, SLC17A7, FAM171B |
| [[KCTD16]] | B | GXYLT2 activity raises KCTD16's level | lines that do not express GXYLT2 (11) vs lines expressing it (39) | 3.55× lower at baseline in the lines without GXYLT2 | 0.038 | ⚠ within organs, on part of the lines; also absent: TMEM145, SLC17A7, FAM171B |
| [[NREP]] | B | GXYLT2 activity raises NREP's level | lines that do not express GXYLT2 (11) vs lines expressing it (39) | 3.90× lower at baseline in the lines without GXYLT2 | 0.050 | ⚠ within organs, on part of the lines; also absent: TMEM145, SLC17A7, FAM171B |
| [[NPTXR]] | B | GXYLT2 activity raises NPTXR's level | lines that do not express GXYLT2 (11) vs lines expressing it (39) | 2.19× lower at baseline in the lines without GXYLT2 | 0.051 | ⚠ within organs, on part of the lines; also absent: TMEM145, SLC17A7, FAM171B |
| [[SCPEP1]] | B | GXYLT2 activity raises SCPEP1's level | lines that do not express GXYLT2 (11) vs lines expressing it (39) | 1.64× lower at baseline in the lines without GXYLT2 | 0.056 | ⚠ within organs, on part of the lines; also absent: TMEM145, SLC17A7, FAM171B |
| [[SMARCD3]] | B | GXYLT2 activity raises SMARCD3's level | lines that do not express GXYLT2 (11) vs lines expressing it (39) | 2.04× lower at baseline in the lines without GXYLT2 | 0.063 | ⚠ within organs, on part of the lines; also absent: TMEM145, SLC17A7, FAM171B |

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.581). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (50.9, 25.6); signed map (29.5, 42.7). **Vector** length 95.3, 22.3% of its response variance represented; |z| ≥ 3 in 1,177 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.6 | +11.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.4 | +8.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.9 | +7.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.8 | +8.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.7 | +3.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.6 | +6.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.8 | +5.5 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.8 | -8.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.7 | -8.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.6 | -7.7 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.6 | -6.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.2 | -2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -4.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.9 | -6.4 |

## What is on record

|  |  |
|---|---|
| Name | glucoside xylosyltransferase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p13 — chr3:72,888,046-72,998,138 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously GLT8D4 |
| Gene groups (HGNC) | Glycosyltransferase family 8 |
| Reactome | 3 pathways, smallest: Regulation of MITF-M-dependent genes involved in extracellular matrix, focal adhesion and epithelial-to-mesenchymal transition; MITF-M-dependent gene expression; MITF-M-regulated melanocyte development |
| Matched by | ensembl_id |

**Function**, from UniProt [A0PJZ3](https://www.uniprot.org/uniprotkb/A0PJZ3) (Glucoside xylosyltransferase 2):

> Glycosyltransferase which elongates the O-linked glucose attached to EGF-like repeats in the extracellular domain of Notch proteins by catalyzing the addition of xylose.

**Summary**, from NCBI Gene [727936](https://www.ncbi.nlm.nih.gov/gene/727936):

> The protein encoded by this gene is a xylosyltransferase that elongates O-linked glucose bound to epidermal growth factor (EGF) repeats. The encoded protein catalyzes the addition of xylose to the O-glucose-modified residues of EGF repeats of Notch proteins. [provided by RefSeq, Sep 2016]

**Accessions** — [HGNC:33383](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33383) · Entrez [727936](https://www.ncbi.nlm.nih.gov/gene/727936) · UniProt [A0PJZ3](https://www.uniprot.org/uniprotkb/A0PJZ3) · Ensembl [ENSG00000172986](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172986)

## Data

Gene col 10326: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10326); `tables/drug_effects.parquet` (70 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10326, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10326]; `tensor/DDL_lfc|DDL_z.npy` [10326]; `embed/gene_vectors.npy` [10326]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10326 or target_col == 10326). Every well: [[GXYLT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GXYLT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
