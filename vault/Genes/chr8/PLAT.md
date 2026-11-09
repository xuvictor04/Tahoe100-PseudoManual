---
symbol: "PLAT"
type: "gene"
col: 2450
ensembl_id: "ENSG00000104368"
name: "plasminogen activator, tissue type"
location: "8p11.21"
module: 84
arm: "+"
pooled_cpm: 70.44
n_lines_expressing: 22
n_dd_up: 10
n_dd_down: 9
n_dd_up_clean: 7
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 10
direction_downstream: 25
tags: ["gene", "module/084"]
generated_by: "tahoemap"
---

# PLAT

*plasminogen activator, tissue type* — 8p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.81× (z +9.5, q 9e-19, up in 7 of 19 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.88× (z +8.2, q 7e-14, up in 15 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.538× (z -5.3, q 7e-05, down in 13 of 19 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FN1]] (+0.60, fdr 7e-06), [[SHC4]] (+0.59, fdr 7e-06), [[PPFIBP1]] (+0.58, fdr 1e-05); moves opposite to [[RNLS]] (-0.44, fdr 3e-04), [[RAB11FIP2]] (-0.44, fdr 1e-04), [[ACTR3C]] (-0.43, fdr 4e-04).
> It is in [[Module 084]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[MILR1]] → it (grade B ⚠); 25 go from it, the strongest it → [[ADAM19]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2450.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.81×** | +9.5 | 9e-19 | 7/19 (hTERT-HPNE, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.88×** | +8.2 | 7e-14 | 15/20 (Hs 766T, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.27×** | +7.3 | 7e-11 | 3/18 (hTERT-HPNE, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.85×** | +5.2 | 2e-05 | 5/18 (C32, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.76×** | +5.0 | 7e-05 | 12/19 (Hs 766T, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 0.5 µM |  | **2.24×** | +3.8 | 0.015 | 12/19 (NCI-H1792, NCI-H460, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.46×** | +3.5 | 0.042 | 13/19 (LOX-IMVI, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.46×** | +3.3 | 0.055 | 10/19 (SK-MEL-2, HS-578T, …) | rises with dose |  |
| [[Isocorydine (drug)]] 0.5 µM |  | **1.46×** | +3.3 | 0.055 | 6/19 (SK-MEL-2, J82, …) | inconsistent across doses | position effect removed |
| [[vincristine (drug)]] 5 µM |  | **2.27×** | +3.2 | 0.092 | 6/18 (NCI-H1792, HOP62, …) | two highest doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2450.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.538×** | -5.3 | 7e-05 | 13/19 (NCI-H1792, SK-MEL-2, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.570×** | -4.9 | 2e-04 | 14/19 (A-172, CHP-212, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.551×** | -4.6 | 8e-04 | 13/21 (A-172, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.619×** | -4.4 | 0.001 | 14/19 (J82, RPMI-7951, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.625×** | -4.3 | 0.002 | 16/20 (CHP-212, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.05 µM |  | **0.752×** | -3.7 | 0.021 | 10/20 (NCI-H1792, SK-MEL-2, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.698×** | -3.3 | 0.072 | 9/19 (HOP62, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.778×** | -3.3 | 0.072 | 11/19 (Hs 766T, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.779×** | -3.3 | 0.072 | 1/20 (NCI-H460) | rises with dose |  |
| [[Hydroxyfasudil (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.722× | -3.0 | 0.14 | 4/20 (A-172, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.722× | -3.0 | 0.14 | 13/20 (A-172, NCI-H460, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2450. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 1,108 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0976× (z -18.0) |
| [[CHP-212 (line)]] | wt | 703 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0895× (z -17.4) |
| [[NCI-H1792 (line)]] | alt | 75.1 | 0 | 4 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.313× (z -18.7) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 5 µM 0.118× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 264 | 0 | 4 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.109× (z -10.6) ⚠ toxic; cell-cycle shift, explains ~46% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.133× (z -10.1) |
| [[SK-MEL-2 (line)]] | alt | 197 | 0 | 4 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.267× (z -11.3) ⚠ cell-cycle shift, explains ~79% of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 0.214× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 99.9 | 0 | 3 | — | [[Auranofin (drug)]] 5 µM 0.0726× (z -12.0) |
| [[Hs 766T (line)]] | wt | 335 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0870× (z -18.8) |
| [[CFPAC-1 (line)]] | alt | 245 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.188× (z -9.0) |
| [[H4 (line)]] | wt | 20.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -8.7) |
| [[HOP62 (line)]] | alt | 27.8 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.569× (z -8.8) ⚠ position not correctable |
| [[J82 (line)]] | alt | 41.0 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 4.46× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H460 (line)]] | wt | 25.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -10.0) |
| [[A-427 (line)]] | wt | 4.06 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 11.3 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 6.26 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.4 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.62 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 100 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.10 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 10.5 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 9.93 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.77 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.55 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 95.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.02 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.96 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.86 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.85 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.67 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.63 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.53 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 14.2 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.38 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.97 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 7.28 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 77.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.88 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.70 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 7.38 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.09 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.81 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.09 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 6.03 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2450), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FN1]] | +0.60 | +0.58 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_COAGULATION; STRING 867 |
| [[SHC4]] | +0.59 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[PPFIBP1]] | +0.58 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[ITGB3]] | +0.58 | +0.57 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_COAGULATION |
| [[RGS17]] | +0.58 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[COL13A1]] | +0.58 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[KCNN4]] | +0.57 | +0.55 / +0.50 | both halves | 1e-05 | pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[AMOTL1]] | +0.57 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[DNMBP]] | +0.57 | +0.57 / +0.47 | both halves | 2e-05 | pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[ECE1]] | +0.57 | +0.50 / +0.55 | both halves | 1e-05 | STRING 450 |
| [[PPP1R14C]] | +0.56 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[FLT1]] | +0.55 | +0.49 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNLS]] | -0.44 | -0.36 / -0.27 | both halves | 3e-04 |  |
| [[RAB11FIP2]] | -0.44 | -0.39 / -0.33 | both halves | 1e-04 |  |
| [[ACTR3C]] | -0.43 | -0.33 / -0.26 | both halves | 4e-04 |  |
| [[MIR4307HG]] | -0.43 | -0.34 / -0.36 | both halves | 1e-04 |  |
| [[PSG9]] | -0.43 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[WASHC2C]] | -0.42 | -0.43 / -0.37 | both halves | 8e-05 |  |
| [[CLIC2]] | -0.42 | -0.43 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 3, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MILR1]] | B | MILR1 activity raises PLAT's level | lines that do not express MILR1 (19) vs lines expressing it (31) | 2.63× lower at baseline in the lines without MILR1 | 0.039 | ⚠ within organs, on part of the lines; also absent: EVA1A, LINC00973, NLRP1 |
| [[EMP1]] | B | EMP1 activity raises PLAT's level | lines that do not express EMP1 (10) vs lines expressing it (40) | 3.58× lower at baseline in the lines without EMP1 | 0.071 | ⚠ within organs, on part of the lines |
| [[ADAM19]] | B | ADAM19 activity raises PLAT's level | lines that do not express ADAM19 (13) vs lines expressing it (37) | 3.35× lower at baseline in the lines without ADAM19 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: ITGA1, ABLIM3, LBH |
| [[FN1]] | C | FN1 activity raises PLAT's level | lines that do not express FN1 (29) vs lines expressing it (21) | 4.59× lower at baseline in the lines without FN1 | 0.005 | ⚠ within organs, on part of the lines; also absent: PLPP4, ENSG00000234261, IL7R; co-absent with the target |
| [[SUCNR1]] | C | SUCNR1 activity raises PLAT's level | lines that do not express SUCNR1 (44) vs lines expressing it (6) | 6.03× lower at baseline in the lines without SUCNR1 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, TBXT, ENSG00000230258; co-absent with the target |
| [[SOX7]] | C | SOX7 activity raises PLAT's level | lines that do not express SOX7 (35) vs lines expressing it (15) | 2.87× lower at baseline in the lines without SOX7 | 0.034 | ⚠ within organs, on part of the lines; also absent: COL4A6, MMRN1, PTGIS; co-absent with the target |
| [[LAMA4]] | C | LAMA4 activity raises PLAT's level | lines that do not express LAMA4 (27) vs lines expressing it (23) | 4.06× lower at baseline in the lines without LAMA4 | 0.054 | ⚠ within organs, on part of the lines; also absent: SLFN12, ARMCX1, BAALC; co-absent with the target |
| [[NES]] | C | NES activity raises PLAT's level | lines that do not express NES (26) vs lines expressing it (24) | 4.31× lower at baseline in the lines without NES | 0.065 | ⚠ within organs, on part of the lines; also absent: LAPTM5, CSPG4, ENSG00000230490; co-absent with the target |
| [[F3]] | C | F3 activity raises PLAT's level | lines that do not express F3 (24) vs lines expressing it (26) | 2.34× lower at baseline in the lines without F3 | 0.068 | ⚠ within organs, on part of the lines; also absent: TLR2, KRT7, EDNRA; co-absent with the target |
| [[SETBP1]] | C | SETBP1 activity raises PLAT's level | lines that do not express SETBP1 (19) vs lines expressing it (31) | 3.84× lower at baseline in the lines without SETBP1 | 0.070 | ⚠ within organs, on part of the lines; also absent: ADAM7-AS1, ENSG00000253471, DPYSL3; co-absent with the target |

### Downstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 16, C 9. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAM19]] | B | PLAT activity raises ADAM19's level | lines that do not express PLAT (28) vs lines expressing it (22) | 3.47× lower at baseline in the lines without PLAT | 0.008 | ⚠ within organs, on part of the lines; also absent: TIMP3, FN1, SNAI2 |
| [[RAC2]] | B | PLAT activity raises RAC2's level | lines that do not express PLAT (28) vs lines expressing it (22) | 4.08× lower at baseline in the lines without PLAT | 0.008 | ⚠ within organs, on part of the lines; also absent: TIMP3, FN1, SNAI2 |
| [[STK17B]] | B | PLAT activity raises STK17B's level | lines that do not express PLAT (28) vs lines expressing it (22) | 1.75× lower at baseline in the lines without PLAT | 0.015 | ⚠ within organs, on part of the lines; also absent: TIMP3, FN1, SNAI2 |
| [[DUSP6]] | B | PLAT activity raises DUSP6's level | lines that do not express PLAT (28) vs lines expressing it (22) | 1.62× lower at baseline in the lines without PLAT | 0.017 | ⚠ within organs, on part of the lines; also absent: TIMP3, FN1, SNAI2 |
| [[TIMP1]] | B | PLAT activity raises TIMP1's level | lines that do not express PLAT (28) vs lines expressing it (22) | 2.26× lower at baseline in the lines without PLAT | 0.018 | ⚠ within organs, on part of the lines; also absent: TIMP3, FN1, SNAI2 |
| [[PLXNA2]] | B | PLAT activity raises PLXNA2's level | lines that do not express PLAT (28) vs lines expressing it (22) | 2.14× lower at baseline in the lines without PLAT | 0.018 | ⚠ within organs, on part of the lines; also absent: TIMP3, FN1, SNAI2 |
| [[COL13A1]] | B | PLAT activity raises COL13A1's level | lines that do not express PLAT (28) vs lines expressing it (22) | 3.42× lower at baseline in the lines without PLAT | 0.024 | ⚠ within organs, on part of the lines; also absent: TIMP3, FN1, SNAI2 |
| [[EGR3]] | B | PLAT activity raises EGR3's level | lines that do not express PLAT (28) vs lines expressing it (22) | 1.63× lower at baseline in the lines without PLAT | 0.024 | ⚠ within organs, on part of the lines; also absent: TIMP3, FN1, SNAI2 |
| [[PDLIM7]] | B | PLAT activity raises PDLIM7's level | lines that do not express PLAT (28) vs lines expressing it (22) | 1.74× lower at baseline in the lines without PLAT | 0.032 | ⚠ within organs, on part of the lines; also absent: TIMP3, FN1, SNAI2 |
| [[ITGA5]] | B | PLAT activity raises ITGA5's level | lines that do not express PLAT (28) vs lines expressing it (22) | 3.49× lower at baseline in the lines without PLAT | 0.032 | ⚠ within organs, on part of the lines; also absent: TIMP3, FN1, SNAI2 |
| [[LTBP1]] | B | PLAT activity raises LTBP1's level | lines that do not express PLAT (28) vs lines expressing it (22) | 2.16× lower at baseline in the lines without PLAT | 0.035 | ⚠ within organs, on part of the lines; also absent: TIMP3, FN1, SNAI2 |
| [[SMOX]] | B | PLAT activity raises SMOX's level | lines that do not express PLAT (28) vs lines expressing it (22) | 1.93× lower at baseline in the lines without PLAT | 0.041 | ⚠ within organs, on part of the lines; also absent: TIMP3, FN1, SNAI2 |

## Where it sits

- **Module**: [[Module 084]]; 52 genes; every member is in the + arm (projection on the module's main direction 0.620). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (48.7, 6.6); signed map (6.0, 50.3). **Vector** length 78.3, 23.4% of its response variance represented; |z| ≥ 3 in 767 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +8.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.4 | +5.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.0 | +3.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.4 | +2.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +2.9 | +9.5 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.6 | +3.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | +0.9 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.4 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +0.5 |
| fall | [[Trametinib (drug)]] 5 µM |  | -3.6 | -4.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.4 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.4 | -5.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.9 | -1.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | -2.9 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.7 | -2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | plasminogen activator, tissue type |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p11.21 — chr8:42,174,718-42,207,709 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Serine proteases; Kringle domain containing |
| Hallmark sets | COAGULATION, APOPTOSIS, COMPLEMENT, KRAS_SIGNALING_UP |
| Reactome | 4 pathways, smallest: Dissolution of Fibrin Clot; Signaling by PDGF; Signaling by Receptor Tyrosine Kinases |
| Matched by | ensembl_id |

**Function**, from UniProt [P00750](https://www.uniprot.org/uniprotkb/P00750) (Tissue-type plasminogen activator):

> Converts the abundant, but inactive, zymogen plasminogen to plasmin by hydrolyzing a single Arg-Val bond in plasminogen. By controlling plasmin-mediated proteolysis, it plays an important role in tissue remodeling and degradation, in cell migration and many other physiopathological events. During oocyte activation, plays a role in cortical granule reaction in the zona reaction, which contributes to the block to polyspermy (By similarity).

**Summary**, from NCBI Gene [5327](https://www.ncbi.nlm.nih.gov/gene/5327):

> This gene encodes tissue-type plasminogen activator, a secreted serine protease that converts the proenzyme plasminogen to plasmin, a fibrinolytic enzyme. The encoded preproprotein is proteolytically processed by plasmin or trypsin to generate heavy and light chains. These chains associate via disulfide linkages to form the heterodimeric enzyme. This enzyme plays a role in cell migration and tissue remodeling. Increased enzymatic activity causes hyperfibrinolysis, which manifests as excessive …

**Accessions** — [HGNC:9051](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9051) · Entrez [5327](https://www.ncbi.nlm.nih.gov/gene/5327) · UniProt [P00750](https://www.uniprot.org/uniprotkb/P00750) · Ensembl [ENSG00000104368](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104368)

## Data

Gene col 2450: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2450); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2450, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2450]; `tensor/DDL_lfc|DDL_z.npy` [2450]; `embed/gene_vectors.npy` [2450]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2450 or target_col == 2450). Every well: [[PLAT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLAT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
