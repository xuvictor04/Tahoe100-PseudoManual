---
symbol: "ATP6V0D2"
type: "gene"
col: 7206
ensembl_id: "ENSG00000147614"
name: "ATPase H+ transporting V0 subunit d2"
location: "8q21.3"
module: 229
arm: "+"
pooled_cpm: 4.22
n_lines_expressing: 32
n_dd_up: 27
n_dd_down: 8
n_dd_up_clean: 17
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 11
direction_downstream: 9
tags: ["gene", "module/229"]
generated_by: "tahoemap"
---

# ATP6V0D2

*ATPase H+ transporting V0 subunit d2* — 8q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (10 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 3.40× (z +9.7, q 1e-19, up in 21 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.483× (z -5.8, q 3e-06, down in 18 of 25 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01705]] (+0.70, fdr 7e-06), [[RABGEF1P3]] (+0.68, fdr 7e-06), [[RPLP0P2]] (+0.65, fdr 3e-05); moves opposite to [[SKA2]] (-0.51, fdr 2e-05), [[CAV1]] (-0.50, fdr 2e-05), [[CTDSP1]] (-0.49, fdr 2e-04).
> It is in [[Module 229]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[STK32A]] → it (grade B ⚠); 9 go from it, the strongest it → [[UBE2Q2P1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7206.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **3.40×** | +9.7 | 1e-19 | 21/27 (A498, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **3.59×** | +9.6 | 2e-19 | 18/25 (SK-MEL-2, A498, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.30×** | +9.4 | 2e-18 | 22/28 (NCI-H2347, HS-578T, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.97×** | +7.6 | 3e-12 | 9/25 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **5.04×** | +6.7 | 2e-09 | 5/8 (NCI-H2030, C32, …) | all doses, flat | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.36×** | +6.6 | 5e-09 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.27×** | +6.5 | 5e-09 | 19/27 (PANC-1, SNU-423, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.73×** | +6.2 | 4e-08 | 17/27 (H4, A498, …) | all doses, flat | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.13×** | +6.0 | 1e-07 | 12/27 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **2.06×** | +5.8 | 5e-07 | 14/27 (A498, H4, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.02×** | +5.6 | 1e-06 | 12/27 (A498, PANC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM |  | **1.99×** | +5.5 | 2e-06 | 16/28 (SW 900, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.85×** | +4.9 | 4e-05 | 16/25 (H4, SW 900, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.83×** | +4.8 | 6e-05 | 1/13 (NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.28×** | +4.7 | 1e-04 | 9/28 (A498, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.50×** | +4.5 | 2e-04 | 8/28 (NCI-H2347, CFPAC-1, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **2.81×** | +4.3 | 6e-04 | 12/25 (PANC-1, SNU-423, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.69×** | +4.2 | 9e-04 | 10/24 (NCI-H2347, C32, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.57×** | +3.6 | 0.011 | 11/27 (A498, C32, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.82×** | +3.4 | 0.017 | 5/25 (PANC-1, SNU-423, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **1.73×** | +3.1 | 0.044 | 3/27 (PANC-1, SK-MEL-2, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7206.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.483×** | -5.8 | 3e-06 | 18/25 (RPMI-7951, SW 900, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Triamcinolone (drug)]] 5 µM |  | **0.626×** | -5.3 | 3e-05 | 14/28 (NCI-H2347, SNU-423, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.851× | -4.6 | 8e-04 | 9/28 (HepG2/C3A, NCI-H2347, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 0.05 µM |  | **0.590×** | -4.2 | 0.003 | 16/26 (Hs 766T, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.605×** | -4.0 | 0.006 | 12/28 (A498, NCI-H2347, …) | top dose only | composition shift; position effect removed |
| [[Dexamethasone (drug)]] 5 µM |  | **0.639×** | -3.6 | 0.031 | 9/27 (NCI-H2347, SNU-423, …) | rises with dose |  |
| [[Budesonide (drug)]] 5 µM |  | **0.643×** | -3.5 | 0.032 | 12/28 (NCI-H2347, SNU-423, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.651×** | -3.4 | 0.040 | 10/24 (A498, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.666×** | -3.3 | 0.071 | 6/27 (NCI-H2347, A549, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.678× | -3.1 | 0.10 | 9/27 (NCI-H2347, HOP62, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7206. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 34.8 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0655× (z -21.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0969× (z -18.6) |
| [[A498 (line)]] | wt | 4.27 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 9.31× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 14.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0524× (z -11.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 2.09 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 20.2× (z +9.6) ⚠ unreliable plate only | — |
| [[RPMI-7951 (line)]] | alt | 17.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -11.9) ⚠ cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 13.3 | 1 | 0 | [[Bortezomib (drug)]] 0.05 µM 12.8× (z +8.7) | — |
| [[SW 900 (line)]] | alt | 30.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.230× (z -10.8) |
| [[A-172 (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.675 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.885 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.780 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.991 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.637 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 6.77 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.15 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.827 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.701 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.779 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.787 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.78 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.667 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.974 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.797 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.886 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 8.90 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.902 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.830 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.757 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.777 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.743 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7206), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01705]] | +0.70 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[RABGEF1P3]] | +0.68 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[RPLP0P2]] | +0.65 | +0.45 / +0.69 | both halves | 3e-05 |  |
| [[LDAF1]] | +0.61 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[GSDME]] | +0.60 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[LINC00536]] | +0.57 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[BEX2]] | +0.56 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[CLDN12]] | +0.55 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[BEX4]] | +0.55 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[TM4SF19]] | +0.55 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[TM4SF19-DYNLT2B]] | +0.54 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[KCP]] | +0.54 | +0.26 / +0.63 | both halves | 4e-04 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SKA2]] | -0.51 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[CAV1]] | -0.50 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[CTDSP1]] | -0.49 | -0.45 / -0.29 | both halves | 2e-04 |  |
| [[CLPTM1L]] | -0.48 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[ARMC8]] | -0.48 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[ADGRG6]] | -0.48 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[CCND3]] | -0.48 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[HOPX]] | -0.47 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[SCLT1]] | -0.46 | -0.39 / -0.36 | both halves | 9e-05 |  |
| [[TNS2]] | -0.46 | -0.36 / -0.49 | both halves | 9e-05 |  |
| [[SMC1A]] | -0.46 | -0.40 / -0.38 | both halves | 6e-05 |  |
| [[CCDC57]] | -0.46 | -0.42 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 6, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STK32A]] | B | STK32A activity raises ATP6V0D2's level | lines that do not express STK32A (23) vs lines expressing it (27) | 2.40× lower at baseline in the lines without STK32A | 0.019 | ⚠ within organs, on part of the lines; also absent: CHSY3, FRMPD4, SAA1 |
| [[LINC02257]] | B | LINC02257 activity raises ATP6V0D2's level | lines that do not express LINC02257 (15) vs lines expressing it (35) | 2.33× lower at baseline in the lines without LINC02257 | 0.019 | ⚠ within organs, on part of the lines; also absent: CTSS, PAG1, ZNF365; maybe low, not absent |
| [[GRB10]] | B | GRB10 activity raises ATP6V0D2's level | lines that do not express GRB10 (11) vs lines expressing it (39) | 1.97× lower at baseline in the lines without GRB10 | 0.048 | ⚠ within organs, on part of the lines; also absent: FAM107B, DGKG, GEM |
| [[LINC02882]] | B | LINC02882 activity raises ATP6V0D2's level | lines that do not express LINC02882 (28) vs lines expressing it (22) | 2.04× lower at baseline in the lines without LINC02882 | 0.052 | ⚠ within organs, on part of the lines; also absent: VGLL3, ANXA10, DDX43 |
| [[CRYM]] | B | CRYM activity raises ATP6V0D2's level | lines that do not express CRYM (12) vs lines expressing it (38) | 1.81× lower at baseline in the lines without CRYM | 0.080 | ⚠ within organs, on part of the lines; also absent: GBP3, CD44, SERPINE2; maybe low, not absent |
| [[GCKR]] | B | GCKR activity raises ATP6V0D2's level | lines that do not express GCKR (24) vs lines expressing it (26) | 1.63× lower at baseline in the lines without GCKR | 0.091 | ⚠ within organs, on part of the lines; also absent: G0S2, IGFBP1, AADAC; maybe low, not absent |
| [[ROR1-AS1]] | C | ROR1-AS1 activity raises ATP6V0D2's level | lines that do not express ROR1-AS1 (26) vs lines expressing it (24) | 3.01× lower at baseline in the lines without ROR1-AS1 | 0.002 | ⚠ within organs, on part of the lines; also absent: LINC01705, COL4A2, ADAMTS9-AS2; co-absent with the target |
| [[LINC01705]] | C | LINC01705 activity raises ATP6V0D2's level | lines that do not express LINC01705 (27) vs lines expressing it (23) | 3.08× lower at baseline in the lines without LINC01705 | 0.003 | ⚠ within organs, on part of the lines; also absent: ROR1-AS1, TIMP3, ENSG00000250137; co-absent with the target |
| [[ENTHD1]] | C | ENTHD1 activity raises ATP6V0D2's level | lines that do not express ENTHD1 (28) vs lines expressing it (22) | 3.11× lower at baseline in the lines without ENTHD1 | 0.008 | ⚠ within organs, on part of the lines; also absent: CRLF2, TNFAIP6, ENSG00000289600; co-absent with the target |
| [[CRTAC1]] | C | CRTAC1 activity raises ATP6V0D2's level | lines that do not express CRTAC1 (27) vs lines expressing it (23) | 2.47× lower at baseline in the lines without CRTAC1 | 0.039 | ⚠ within organs, on part of the lines; also absent: ITGB3, ADAMTS9-AS2, CRLF2; co-absent with the target |
| [[ARMCX1]] | C | ARMCX1 activity raises ATP6V0D2's level | lines that do not express ARMCX1 (23) vs lines expressing it (27) | 3.07× lower at baseline in the lines without ARMCX1 | 0.067 | ⚠ within organs, on part of the lines; also absent: CTHRC1, CDH2, RFTN1; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 7, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UBE2Q2P1]] | B | ATP6V0D2 activity raises UBE2Q2P1's level | lines that do not express ATP6V0D2 (18) vs lines expressing it (32) | 1.54× lower at baseline in the lines without ATP6V0D2 | 0.047 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, KMT2D, ARID1A; also absent: GBP5, NALCN, IGFBP7; maybe low, not absent |
| [[CLIP4]] | B | ATP6V0D2 activity raises CLIP4's level | lines that do not express ATP6V0D2 (18) vs lines expressing it (32) | 3.24× lower at baseline in the lines without ATP6V0D2 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, KMT2D, ARID1A; also absent: GBP5, NALCN, IGFBP7; maybe low, not absent |
| [[RABGEF1P3]] | B | ATP6V0D2 activity raises RABGEF1P3's level | lines that do not express ATP6V0D2 (18) vs lines expressing it (32) | 1.42× lower at baseline in the lines without ATP6V0D2 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, KMT2D, ARID1A; also absent: GBP5, NALCN, IGFBP7; maybe low, not absent |
| [[LDAF1]] | B | ATP6V0D2 activity raises LDAF1's level | lines that do not express ATP6V0D2 (18) vs lines expressing it (32) | 1.31× lower at baseline in the lines without ATP6V0D2 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, KMT2D, ARID1A; also absent: GBP5, NALCN, IGFBP7; maybe low, not absent |
| [[HLA-F-AS1]] | B | ATP6V0D2 activity raises HLA-F-AS1's level | lines that do not express ATP6V0D2 (18) vs lines expressing it (32) | 1.16× lower at baseline in the lines without ATP6V0D2 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, KMT2D, ARID1A; also absent: GBP5, NALCN, IGFBP7; maybe low, not absent |
| [[KCNIP4]] | B | ATP6V0D2 activity raises KCNIP4's level | lines that do not express ATP6V0D2 (18) vs lines expressing it (32) | 1.66× lower at baseline in the lines without ATP6V0D2 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, KMT2D, ARID1A; also absent: GBP5, NALCN, IGFBP7; maybe low, not absent |
| [[SPSB1]] | B | ATP6V0D2 activity raises SPSB1's level | lines that do not express ATP6V0D2 (18) vs lines expressing it (32) | 1.52× lower at baseline in the lines without ATP6V0D2 | 0.098 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, KMT2D, ARID1A; also absent: GBP5, NALCN, IGFBP7; maybe low, not absent |
| [[BEX4]] | C | ATP6V0D2 activity raises BEX4's level | lines that do not express ATP6V0D2 (18) vs lines expressing it (32) | 2.70× lower at baseline in the lines without ATP6V0D2 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, KMT2D, ARID1A; also absent: GBP5, NALCN, IGFBP7; maybe low, not absent; co-absent with the target |
| [[ROR1-AS1]] | C | ATP6V0D2 activity raises ROR1-AS1's level | lines that do not express ATP6V0D2 (18) vs lines expressing it (32) | 2.77× lower at baseline in the lines without ATP6V0D2 | 0.092 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, KMT2D, ARID1A; also absent: GBP5, NALCN, IGFBP7; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 229]]; 6 genes; every member is in the + arm (projection on the module's main direction 0.772). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.45; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.1, -3.1); signed map (14.6, 53.2). **Vector** length 69.9, 16.6% of its response variance represented; |z| ≥ 3 in 756 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +5.8 | +6.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +9.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.5 | +9.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.3 | +9.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.2 | +4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.0 | +5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +3.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.9 | +5.8 |
|  | [[EX229 (drug)]] 5 µM |  | +2.2 | +2.1 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -2.3 | -3.1 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.2 | -3.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -2.1 | -4.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -2.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.1 | -3.0 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.0 | -3.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.0 | -5.3 |

## What is on record

|  |  |
|---|---|
| Name | ATPase H+ transporting V0 subunit d2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q21.3 — chr8:85,987,323-86,154,225 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ38708, VMA6; previously ATP6D2 |
| Gene groups (HGNC) | V-type ATPase subunits |
| Reactome | 13 pathways, smallest: Insulin receptor recycling; ROS and RNS production in phagocytes; Transferrin endocytosis and recycling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N8Y2](https://www.uniprot.org/uniprotkb/Q8N8Y2) (V-type proton ATPase subunit d 2):

> Subunit of the V0 complex of vacuolar(H+)-ATPase (V-ATPase), a multisubunit enzyme composed of a peripheral complex (V1) that hydrolyzes ATP and a membrane integral complex (V0) that translocates protons. V-ATPase is responsible for acidifying and maintaining the pH of intracellular compartments and in some cell types, is targeted to the plasma membrane, where it is responsible for acidifying the extracellular environment (By similarity). May play a role in coupling of proton transport and ATP …

**Summary**, from NCBI Gene [245972](https://www.ncbi.nlm.nih.gov/gene/245972):

> Predicted to contribute to proton-transporting ATPase activity, rotational mechanism. Predicted to be involved in vacuolar acidification and vacuolar transport. Located in apical plasma membrane. Part of vacuolar proton-transporting V-type ATPase complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18266](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18266) · Entrez [245972](https://www.ncbi.nlm.nih.gov/gene/245972) · UniProt [Q8N8Y2](https://www.uniprot.org/uniprotkb/Q8N8Y2) · Ensembl [ENSG00000147614](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147614)

## Data

Gene col 7206: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7206); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7206, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7206]; `tensor/DDL_lfc|DDL_z.npy` [7206]; `embed/gene_vectors.npy` [7206]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7206 or target_col == 7206). Every well: [[ATP6V0D2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP6V0D2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
