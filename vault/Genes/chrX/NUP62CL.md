---
symbol: "NUP62CL"
type: "gene"
col: 12527
ensembl_id: "ENSG00000198088"
name: "nucleoporin 62 C-terminal like"
location: "Xq22.3"
module: 83
arm: "-"
pooled_cpm: 8.7
n_lines_expressing: 31
n_dd_up: 21
n_dd_down: 2
n_dd_up_clean: 12
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 6
tags: ["gene", "module/083"]
generated_by: "tahoemap"
---

# NUP62CL

*nucleoporin 62 C-terminal like* — Xq22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.16× (z +14.4, q 4e-44, up in 29 of 29 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.81× (z +8.4, q 4e-15, up in 21 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Vinblastine (sulfate) (drug)]] 0.5 µM: 0.648× (z -4.4, q 0.007, down in 13 of 28 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2347 0.125×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (COLO 205 0.220×; ⚠ cell-cycle shift, explains ~68% of this change); [[Mebendazole (drug)]] 0.05 µM in 1 line (HCT15 0.0539×); [[Menadione (drug)]] 0.5 µM in 1 line (SW 900 0.0452×); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (HOP62 0.0657×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MLF1]] (+0.66, fdr 1e-05), [[MNS1]] (+0.62, fdr 3e-05), [[CFAP210]] (+0.60, fdr 1e-05); moves opposite to [[LTO1]] (-0.67, fdr 1e-05), [[WAPL]] (-0.58, fdr 1e-05), [[MTG2]] (-0.58, fdr 3e-05).
> It sits in the **-** arm of [[Module 083]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TESC]] → it (grade B ⚠); 6 go from it, the strongest it → [[FBXO30]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12527.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **4.16×** | +14.4 | 4e-44 | 29/29 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **3.40×** | +12.3 | 1e-32 | 29/29 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **3.38×** | +12.3 | 3e-32 | 29/29 (A498, NCI-H460, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.81×** | +8.4 | 4e-15 | 21/29 (PANC-1, A498, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.19×** | +7.9 | 3e-13 | 27/29 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.53×** | +6.0 | 1e-07 | 13/28 (SW1417, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.75×** | +5.6 | 1e-06 | 17/28 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.70×** | +5.3 | 6e-06 | 15/28 (SW1417, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.43×** | +5.1 | 2e-05 | 13/28 (SW1417, PANC-1, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.63×** | +4.7 | 1e-04 | 14/29 (SW1417, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.53×** | +4.3 | 0.001 | 12/27 (NCI-H2347, SW480, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.21×** | +4.2 | 0.001 | 12/28 (NCI-H2347, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.51×** | +4.0 | 0.003 | 3/14 (HT-29, HEC-1-A, …) | inconsistent across doses | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.47×** | +3.9 | 0.004 | 11/29 (HT-29, CFPAC-1, …) | inconsistent across doses | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.29×** | +3.6 | 0.010 | 9/28 (PANC-1, LoVo, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.43×** | +3.6 | 0.010 | 11/29 (HOP62, A549, …) | inconsistent across doses | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.44×** | +3.6 | 0.012 | 12/29 (SW1417, AsPC-1, …) | top dose only | cell-cycle shift (explains ~11% here); composition shift |
| [[Tofacitinib (drug)]] 0.05 µM |  | **1.38×** | +3.1 | 0.060 | 5/28 (HEC-1-A, HT-29, …) | inconsistent across doses |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **1.34×** | +2.9 | 0.088 | 4/29 (SW480, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12527.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2347 0.125×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (COLO 205 0.220×; ⚠ cell-cycle shift, explains ~68% of this change); [[Mebendazole (drug)]] 0.05 µM in 1 line (HCT15 0.0539×); [[Menadione (drug)]] 0.5 µM in 1 line (SW 900 0.0452×); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (HOP62 0.0657×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.648×** | -4.4 | 0.007 | 13/28 (CFPAC-1, COLO 205, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.753×** | -4.0 | 0.017 | 13/28 (HT-29, A498, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.717× | -3.3 | 0.16 | 12/29 (NCI-H2030, NCI-H460, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 0.730× | -3.2 | 0.22 | 13/29 (AsPC-1, HEC-1-A, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | 0.650× | -3.1 | 0.23 | 13/27 (AsPC-1, CFPAC-1, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.72 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12527. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 7.98 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 8.12× (z +10.1) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H460 (line)]] | wt | 8.45 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 6.00× (z +10.4) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[HCT15 (line)]] | alt | 12.1 | 0 | 2 | — | [[Mebendazole (drug)]] 0.05 µM 0.0539× (z -10.3) |
| [[PANC-1 (line)]] | alt | 3.16 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 12.2× (z +9.8) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[SW1417 (line)]] | alt | 24.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +12.5) | — |
| [[CFPAC-1 (line)]] | alt | 19.3 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.242× (z -8.8) |
| [[COLO 205 (line)]] | alt | 24.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -10.6) ⚠ cell-cycle shift, explains ~68% of this change |
| [[HOP62 (line)]] | alt | 4.09 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.0657× (z -8.9) |
| [[NCI-H1792 (line)]] | alt | 4.51 | 0 | 1 | — | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM 0.0744× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 6.69 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0723× (z -10.2) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 11.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.125× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 7.01 | 0 | 1 | — | [[Menadione (drug)]] 0.5 µM 0.0452× (z -9.0) |
| [[A-172 (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.904 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.813 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.703 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.06 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.779 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.718 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.999 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.63 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.927 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 9.58 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.578 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.703 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.731 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.877 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.12 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 30.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12527), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*43 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MLF1]] | +0.66 | +0.49 / +0.69 | both halves | 1e-05 |  |
| [[MNS1]] | +0.62 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[CFAP210]] | +0.60 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[RADX]] | +0.59 | +0.46 / +0.60 | both halves | 2e-05 |  |
| [[STARD5]] | +0.57 | +0.38 / +0.56 | both halves | 6e-05 |  |
| [[RFX2]] | +0.57 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[GGH]] | +0.57 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[HPSE]] | +0.56 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[USP2]] | +0.55 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[SPATA6]] | +0.55 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[OSR2]] | +0.54 | +0.46 / +0.60 | both halves | 2e-05 |  |
| [[CD83]] | +0.54 | +0.39 / +0.63 | both halves | 5e-05 |  |

## Genes that move opposite

*57 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LTO1]] | -0.67 | -0.57 / -0.60 | both halves | 1e-05 |  |
| [[WAPL]] | -0.58 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[MTG2]] | -0.58 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[CLIP1]] | -0.57 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[DNAJB14]] | -0.56 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[MAEA]] | -0.56 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[TRIM4]] | -0.54 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[SRP19]] | -0.53 | -0.55 / -0.38 | both halves | 6e-05 |  |
| [[TSSC4]] | -0.52 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[UBE2J2]] | -0.52 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[PIN4]] | -0.52 | -0.55 / -0.38 | both halves | 6e-05 |  |
| [[CEP104]] | -0.52 | -0.52 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TESC]] | B | TESC activity raises NUP62CL's level | lines that do not express TESC (23) vs lines expressing it (27) | 2.47× lower at baseline in the lines without TESC | 0.028 | ⚠ within organs, on part of the lines; also absent: HSH2D, LINC02331, PIK3AP1 |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FBXO30]] | B | NUP62CL activity lowers FBXO30's level | lines that do not express NUP62CL (19) vs lines expressing it (31) | 1.22× higher at baseline in the lines without NUP62CL | 0.052 | ⚠ within organs, on part of the lines; also absent: LINC01589, ABCC3, GOLT1A |
| [[MICALL1]] | B | NUP62CL activity lowers MICALL1's level | lines that do not express NUP62CL (19) vs lines expressing it (31) | 1.35× higher at baseline in the lines without NUP62CL | 0.053 | ⚠ within organs, on part of the lines; also absent: LINC01589, ABCC3, GOLT1A |
| [[PGAP1]] | B | NUP62CL activity lowers PGAP1's level | lines that do not express NUP62CL (19) vs lines expressing it (31) | 1.40× higher at baseline in the lines without NUP62CL | 0.060 | ⚠ within organs, on part of the lines; also absent: LINC01589, ABCC3, GOLT1A |
| [[STYXL1]] | B | NUP62CL activity raises STYXL1's level | lines that do not express NUP62CL (19) vs lines expressing it (31) | 1.14× lower at baseline in the lines without NUP62CL | 0.075 | ⚠ within organs, on part of the lines; also absent: LINC01589, ABCC3, GOLT1A |
| [[SPAG7]] | B | NUP62CL activity lowers SPAG7's level | lines that do not express NUP62CL (19) vs lines expressing it (31) | 1.22× higher at baseline in the lines without NUP62CL | 0.079 | ⚠ within organs, on part of the lines; also absent: LINC01589, ABCC3, GOLT1A |
| cells under [[Cysteamine (hydrochloride) (drug)]] 5 µM | B | NUP62CL activity raises the cells' numbers under Cysteamine (hydrochloride) 5 µM (protects the cells) | lines that do not express NUP62CL (19) vs lines expressing it (29) | the lines without NUP62CL: 0.93× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: LINC01589, ABCC3, GOLT1A |

## Where it sits

- **Module**: [[Module 083]]; 53 genes; this gene is in the **-** arm (projection on the module's main direction -0.518). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (12.5, -9.7); signed map (-0.6, 18.9). **Vector** length 65.0, 15.3% of its response variance represented; |z| ≥ 3 in 652 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.7 | +2.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.7 | +4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +8.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.6 | +5.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.4 | +5.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.5 | +2.4 |
|  | [[Gemcitabine (drug)]] 0.5 µM |  | +1.3 | +2.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.3 | +2.6 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | +1.2 | +0.5 |
| fall | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.8 | -4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | -3.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.5 | -0.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.4 | -2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | -2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.2 | -4.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.9 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | nucleoporin 62 C-terminal like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq22.3 — chrX:107,123,427-107,206,433 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20130 |
| Matched by | ensembl_id |

UniProt [Q9H1M0](https://www.uniprot.org/uniprotkb/Q9H1M0) carries no function annotation.

**Summary**, from NCBI Gene [54830](https://www.ncbi.nlm.nih.gov/gene/54830):

> This gene encodes a protein containing a domain found in nucleoporins which are glycoproteins found in nuclear pore complexes. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Sep 2011]

**Accessions** — [HGNC:25960](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25960) · Entrez [54830](https://www.ncbi.nlm.nih.gov/gene/54830) · UniProt [Q9H1M0](https://www.uniprot.org/uniprotkb/Q9H1M0) · Ensembl [ENSG00000198088](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198088)

## Data

Gene col 12527: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12527); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12527, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12527]; `tensor/DDL_lfc|DDL_z.npy` [12527]; `embed/gene_vectors.npy` [12527]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12527 or target_col == 12527). Every well: [[NUP62CL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUP62CL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
