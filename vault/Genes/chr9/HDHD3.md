---
symbol: "HDHD3"
type: "gene"
col: 4068
ensembl_id: "ENSG00000119431"
name: "haloacid dehalogenase like hydrolase domain containing 3"
location: "9q32"
module: 8
arm: "+"
pooled_cpm: 6.46
n_lines_expressing: 49
n_dd_up: 17
n_dd_down: 9
n_dd_up_clean: 10
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# HDHD3

*haloacid dehalogenase like hydrolase domain containing 3* — 9q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.28× (z +8.7, q 2e-15, up in 9 of 11 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.81× (z +6.5, q 1e-08, up in 22 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.601× (z -7.9, q 2e-12, down in 27 of 39 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.618× (z -5.3, q 4e-05, down in 15 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LMTK2]] (+0.64, fdr 1e-05), [[FUT2]] (+0.58, fdr 1e-05), [[METTL27]] (+0.57, fdr 2e-05); moves opposite to [[MTR]] (-0.56, fdr 1e-05), [[CYB5D1]] (-0.56, fdr 3e-05), [[PAN2]] (-0.53, fdr 3e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[CYP4F3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠; shown: the 15 strongest. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4068.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.28×** | +8.7 | 2e-15 | 9/11 (A498, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.57×** | +7.0 | 7e-10 | 20/44 (MIA PaCa-2, A-172, …) | rises with dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.81×** | +6.5 | 1e-08 | 22/45 (NCI-H2347, HT-29, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.68×** | +5.7 | 2e-06 | 23/43 (HT-29, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.58×** | +5.0 | 6e-05 | 12/24 (A498, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.56×** | +4.6 | 4e-04 | 17/41 (CFPAC-1, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.50×** | +4.5 | 6e-04 | 14/45 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.75×** | +4.2 | 0.002 | 9/28 (KATO III, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +4.1 | 0.002 | 9/44 (A498, CFPAC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.43×** | +3.9 | 0.005 | 9/45 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.40×** | +3.7 | 0.009 | 16/46 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.40×** | +3.7 | 0.011 | 4/41 (A-172, NCI-H23, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.37×** | +3.4 | 0.025 | 8/30 (J82, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.36×** | +3.4 | 0.025 | 8/42 (A498, SHP-77, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.55×** | +3.3 | 0.033 | 4/38 (HEC-1-A, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4068.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.601×** | -7.9 | 2e-12 | 27/39 (LoVo, LS 180, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.618×** | -5.3 | 4e-05 | 15/35 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.650×** | -4.5 | 0.001 | 18/34 (C-33 A, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.476×** | -4.3 | 0.003 | 17/40 (LoVo, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.689×** | -3.9 | 0.010 | 12/37 (RKO, LS 180, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.793×** | -3.6 | 0.029 | 12/37 (LS 180, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.712×** | -3.6 | 0.029 | 14/44 (LoVo, COLO 205, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.733×** | -3.4 | 0.048 | 11/44 (LoVo, SW480, …) | inconsistent across doses | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.559×** | -3.3 | 0.055 | 8/35 (A-172, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 0.745× | -3.1 | 0.11 | 10/37 (NCI-H23, COLO 205, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 0.755× | -3.1 | 0.11 | 9/46 (COLO 205, LS 180, …) | top dose only | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4068. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 17.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0946× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.325× (z -9.5) |
| [[LoVo (line)]] | wt | 14.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -16.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.162× (z -11.1) |
| [[LS 180 (line)]] | wt | 18.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -12.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -10.2) |
| [[MIA PaCa-2 (line)]] | alt | 6.86 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.126× (z -8.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 10.5 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0898× (z -9.9) |
| [[A-172 (line)]] | wt | 4.39 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.87 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.25 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.13 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.34 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.76 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.37 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.58 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4068), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LMTK2]] | +0.64 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[FUT2]] | +0.58 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[METTL27]] | +0.57 | +0.46 / +0.57 | both halves | 2e-05 |  |
| [[B4GALT5]] | +0.56 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[KRAS]] | +0.56 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[ATP6V0E1]] | +0.56 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[FAM241B]] | +0.55 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[HSPA1A]] | +0.55 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[TRIP4]] | +0.55 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[LYN]] | +0.55 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[ARHGEF10L]] | +0.55 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[HSPA1B]] | +0.54 | +0.55 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTR]] | -0.56 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[CYB5D1]] | -0.56 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[PAN2]] | -0.53 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[POLE3]] | -0.53 | -0.47 / -0.51 | both halves | 2e-05 | ⚠ same locus (30.2 kb, same strand: neighbours can correlate without regulation) |
| [[LNP1]] | -0.52 | -0.51 / -0.30 | both halves | 2e-04 |  |
| [[HNRNPUL1]] | -0.52 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[CCDC15]] | -0.50 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[SLC30A9]] | -0.49 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[SLC37A2]] | -0.49 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[CCDC18]] | -0.49 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[RB1]] | -0.49 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[MLH1]] | -0.48 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[AXL]] | -0.48 | -0.48 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CYP4F3]] | B | CYP4F3 activity raises HDHD3's level | lines that do not express CYP4F3 (29) vs lines expressing it (21) | 1.75× lower at baseline in the lines without CYP4F3 | 0.023 | ⚠ within organs, on part of the lines; also absent: P2RY2, CYP3A5, ITGB6 |
| [[CKMT1B]] | B | CKMT1B activity raises HDHD3's level | lines that do not express CKMT1B (28) vs lines expressing it (22) | 1.76× lower at baseline in the lines without CKMT1B | 0.026 | ⚠ within organs, on part of the lines; also absent: CKMT1A, SYK, PPP1R1B |
| [[MUC3A]] | B | MUC3A activity raises HDHD3's level | lines that do not express MUC3A (25) vs lines expressing it (25) | 1.71× lower at baseline in the lines without MUC3A | 0.029 | ⚠ within organs, on part of the lines; also absent: HSH2D, ADGRF1, CKMT1B |
| [[IGFL2-AS1]] | B | IGFL2-AS1 activity raises HDHD3's level | lines that do not express IGFL2-AS1 (36) vs lines expressing it (14) | 1.80× lower at baseline in the lines without IGFL2-AS1 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALB1, CLRN3, LINC01559 |
| [[TOP2A]] | B | TOP2A activity raises HDHD3's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CMTM8]] | B | CMTM8 activity raises HDHD3's level | lines that do not express CMTM8 (9) vs lines expressing it (41) | 1.83× lower at baseline in the lines without CMTM8 | 0.077 | ⚠ within organs, on part of the lines; also absent: ALDH5A1, NUP210, PLEKHG3; maybe low, not absent |
| [[CBLC]] | B | CBLC activity raises HDHD3's level | lines that do not express CBLC (31) vs lines expressing it (19) | 1.72× lower at baseline in the lines without CBLC | 0.086 | ⚠ within organs, on part of the lines; also absent: KDF1, CLDN7, PRSS8 |
| [[SOAT1]] | C | SOAT1 activity lowers HDHD3's level | lines that do not express SOAT1 (3) vs lines expressing it (47) | 3.39× higher at baseline in the lines without SOAT1 | 0.004 | ⚠ few lines (3 vs 47); across organs; also absent: NKAIN1, CEP85L, CFL2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.350). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-21.9, 19.0); signed map (-19.2, 31.7). **Vector** length 65.8, 11.1% of its response variance represented; |z| ≥ 3 in 749 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +5.1 | +6.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +5.1 | +7.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.5 | +4.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.0 | +5.7 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.2 | +1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +4.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.1 | +0.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.0 | +2.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.6 | +1.6 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.7 | -5.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.5 | -3.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -2.3 | -7.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.2 | -3.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -1.8 | -4.5 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.5 | -1.2 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.4 | -1.2 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.2 | -1.4 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.2 | -2.1 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.1 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | haloacid dehalogenase like hydrolase domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q32 — chr9:113,373,419-113,376,986 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC12904; previously C9orf158 |
| Gene groups (HGNC) | Haloacid dehalogenase like hydrolase domain containing |
| Matched by | ensembl_id |

UniProt [Q9BSH5](https://www.uniprot.org/uniprotkb/Q9BSH5) carries no function annotation.

**Summary**, from NCBI Gene [81932](https://www.ncbi.nlm.nih.gov/gene/81932):

> Predicted to enable hydrolase activity. Located in nucleolus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28171](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28171) · Entrez [81932](https://www.ncbi.nlm.nih.gov/gene/81932) · UniProt [Q9BSH5](https://www.uniprot.org/uniprotkb/Q9BSH5) · Ensembl [ENSG00000119431](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119431)

## Data

Gene col 4068: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4068); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4068, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4068]; `tensor/DDL_lfc|DDL_z.npy` [4068]; `embed/gene_vectors.npy` [4068]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4068 or target_col == 4068). Every well: [[HDHD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HDHD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
