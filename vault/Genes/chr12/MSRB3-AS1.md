---
symbol: "MSRB3-AS1"
type: "gene"
col: 14711
ensembl_id: "ENSG00000250748"
name: "MSRB3 antisense RNA 1"
location: "12q14.3"
module: 87
arm: "+"
pooled_cpm: 66.09
n_lines_expressing: 8
n_dd_up: 8
n_dd_down: 16
n_dd_up_clean: 4
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 7
direction_downstream: 17
tags: ["gene", "module/087"]
generated_by: "tahoemap"
---

# MSRB3-AS1

*MSRB3 antisense RNA 1* — 12q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.17× (z +6.9, q 2e-09, up in 0 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.57× (z +5.7, q 2e-06, up in 0 of 6 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.498× (z -6.3, q 2e-07, down in 4 of 6 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01812]] (+0.74, fdr 7e-06), [[RDUR]] (+0.59, fdr 1e-05), [[PARVB]] (+0.56, fdr 4e-05); moves opposite to [[DCT]] (-0.57, fdr 2e-05), [[ATP6V1A]] (-0.45, fdr 1e-04), [[ARL6IP5]] (-0.43, fdr 2e-04).
> It is in [[Module 087]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 17 go from it, the strongest it → [[TERT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14711.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.17×** | +6.9 | 2e-09 | 0/6 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.20×** | +6.5 | 2e-08 | 0/5 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +5.7 | 2e-06 | 0/6 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.93×** | +5.7 | 2e-06 | 0/4 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.79×** | +3.7 | 0.020 | 0/6 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.51×** | +3.7 | 0.022 | 1/6 (AN3 CA) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.50×** | +3.5 | 0.034 | 1/6 (SNU-423) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.44×** | +3.3 | 0.066 | 0/6 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here); position effect removed |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | 1.46× | +3.1 | 0.11 | 0/6 | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.61× | +3.1 | 0.12 | 0/6 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14711.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.498×** | -6.3 | 2e-07 | 4/6 (SK-MEL-2, A-427, …) | top dose only | cell-cycle shift (explains ~2% here); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.502×** | -5.7 | 3e-06 | 2/6 (SK-MEL-2, RKO) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.680×** | -4.8 | 3e-04 | 2/6 (SK-MEL-2, A-427) | all doses, flat | position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **0.571×** | -4.6 | 6e-04 | 4/7 (SK-MEL-2, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.590×** | -4.6 | 6e-04 | 5/6 (SK-MEL-2, A-427, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.688×** | -4.4 | 8e-04 | 3/6 (SK-MEL-2, A-427, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.629×** | -4.2 | 0.003 | 5/6 (SK-MEL-2, A-427, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.641×** | -4.0 | 0.004 | 5/6 (SK-MEL-2, A-427, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.652×** | -3.8 | 0.008 | 3/6 (SK-MEL-2, A-427, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Binimetinib (drug)]] 5 µM |  | **0.653×** | -3.6 | 0.018 | 4/6 (SK-MEL-2, A-427, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **0.767×** | -3.4 | 0.039 | 3/6 (SK-MEL-2, A-427, …) | rises with dose |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.690×** | -3.3 | 0.040 | 0/6 | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.903× | -3.3 | 0.040 | 0/6 | inconsistent across doses |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **0.685×** | -3.3 | 0.045 | 1/6 (SK-MEL-2) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.699×** | -3.2 | 0.050 | 4/6 (SK-MEL-2, A-427, …) | all doses, flat |  |
| [[Artesunate (drug)]] 0.5 µM |  | **0.707×** | -3.1 | 0.066 | 0/6 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14711. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 1,363 | 0 | 25 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.00762× (z -28.6) |
| [[RKO (line)]] | wt | 1,783 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0564× (z -16.0) |
| [[A-427 (line)]] | wt | 403 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0441× (z -19.7) |
| [[SNU-423 (line)]] | alt | 46.4 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0864× (z -9.9) |
| [[A-172 (line)]] | wt | 5.00 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.20 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.88 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.19 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.32 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.44 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 9.30 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.14 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.32 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 6.89 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.51 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.04 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 5.63 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.08 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 10.2 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.96 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 8.58 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.20 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.30 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 5.58 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.96 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.42 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 10.0 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.61 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.78 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.74 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 8.32 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 7.83 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.93 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 4.46 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 5.78 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 63.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.16 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.29 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.02 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.06 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.30 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.92 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 7.64 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 7.22 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 5.47 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 15.8 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.62 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14711), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01812]] | +0.74 | +0.66 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[RDUR]] | +0.59 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[PARVB]] | +0.56 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[LEF1]] | +0.52 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[PTPRZ1]] | +0.51 | +0.19 / +0.41 | ⚠ not reproduced | 8e-04 |  |
| [[LEF1-AS1]] | +0.51 | +0.39 / +0.41 | both halves | 6e-05 | same gene group |
| [[LINC02454]] | +0.50 | +0.46 / +0.46 | both halves | 3e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[GLDC]] | +0.49 | +0.28 / +0.40 | both halves | 3e-04 |  |
| [[LINC01205]] | +0.49 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[RGS4]] | +0.48 | +0.33 / +0.52 | both halves | 1e-04 |  |
| [[RHBDF2]] | +0.48 | +0.39 / +0.44 | both halves | 6e-05 |  |
| [[MIR100HG]] | +0.47 | +0.41 / +0.45 | both halves | 4e-05 |  |
| [[SIPA1L1]] | +0.47 | +0.43 / +0.44 | both halves | 3e-05 |  |
| [[ST6GAL1]] | +0.47 | +0.42 / +0.47 | both halves | 4e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCT]] | -0.57 | -0.48 / -0.51 | both halves | 2e-05 | **novel candidate** |
| [[ATP6V1A]] | -0.45 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[ARL6IP5]] | -0.43 | -0.33 / -0.30 | both halves | 2e-04 |  |
| [[SCPEP1]] | -0.42 | -0.37 / -0.43 | both halves | 8e-05 |  |
| [[DSTN]] | -0.41 | -0.36 / -0.39 | both halves | 9e-05 |  |
| [[CCN3]] | -0.40 | -0.36 / -0.39 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 1, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises MSRB3-AS1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.5% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[LNCOG]] | C | LNCOG activity raises MSRB3-AS1's level | lines that do not express LNCOG (30) vs lines expressing it (20) | 2.88× lower at baseline in the lines without LNCOG | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GYPC, HS3ST3A1, LAMA1; co-absent with the target |
| [[LINC01205]] | C | LINC01205 activity raises MSRB3-AS1's level | lines that do not express LINC01205 (44) vs lines expressing it (6) | 9.37× lower at baseline in the lines without LINC01205 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, ENSG00000241168, GPR15; maybe low, not absent; co-absent with the target |
| [[GCG]] | C | GCG activity raises MSRB3-AS1's level | lines that do not express GCG (46) vs lines expressing it (4) | 7.40× lower at baseline in the lines without GCG | 0.009 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: GPR15, LINC01205, APOB; co-absent with the target |
| [[LEF1-AS1]] | C | LEF1-AS1 activity raises MSRB3-AS1's level | lines that do not express LEF1-AS1 (33) vs lines expressing it (17) | 3.09× lower at baseline in the lines without LEF1-AS1 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL19A1, ENSG00000226043, DCT; maybe low, not absent; co-absent with the target |
| [[RGS4]] | C | RGS4 activity raises MSRB3-AS1's level | lines that do not express RGS4 (35) vs lines expressing it (15) | 2.48× lower at baseline in the lines without RGS4 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, CCDC190, ENSG00000243486; co-absent with the target |
| [[LINC01812]] | C | LINC01812 activity raises MSRB3-AS1's level | lines that do not express LINC01812 (35) vs lines expressing it (15) | 2.38× lower at baseline in the lines without LINC01812 | 0.080 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235495, ENSG00000224865, ENSG00000287622; co-absent with the target |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 8, C 9. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TERT]] | B | MSRB3-AS1 activity raises TERT's level | lines that do not express MSRB3-AS1 (42) vs lines expressing it (8) | 1.94× lower at baseline in the lines without MSRB3-AS1 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GCG, LINC01205, COX7B2 |
| [[RASGEF1C]] | B | MSRB3-AS1 activity weakens RASGEF1C's drug response | lines that do not express MSRB3-AS1 (28) vs lines expressing it (5) | (z diff -2.29); strongest at Idarubicin (hydrochloride) 5 µM: 1.14x vs 0.46x (z diff -5.5) | 0.029 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GCG, LINC01205, COX7B2; target measured in part of the lines; artifact flags |
| cells under [[Lonafarnib (drug)]] 0.05 µM | B | MSRB3-AS1 activity raises the cells' numbers under Lonafarnib 0.05 µM (protects the cells) | lines that do not express MSRB3-AS1 (42) vs lines expressing it (6) | the lines without MSRB3-AS1: 0.68× the cells of the other lines | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GCG, LINC01205, COX7B2 |
| cells under [[Infigratinib (drug)]] 0.05 µM | B | MSRB3-AS1 activity raises the cells' numbers under Infigratinib 0.05 µM (protects the cells) | lines that do not express MSRB3-AS1 (42) vs lines expressing it (6) | the lines without MSRB3-AS1: 0.74× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GCG, LINC01205, COX7B2 |
| cells under [[Futibatinib (drug)]] 0.5 µM | B | MSRB3-AS1 activity raises the cells' numbers under Futibatinib 0.5 µM (protects the cells) | lines that do not express MSRB3-AS1 (42) vs lines expressing it (6) | the lines without MSRB3-AS1: 0.80× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GCG, LINC01205, COX7B2 |
| cells under [[Pralsetinib (drug)]] 0.05 µM | B | MSRB3-AS1 activity raises the cells' numbers under Pralsetinib 0.05 µM (protects the cells) | lines that do not express MSRB3-AS1 (42) vs lines expressing it (6) | the lines without MSRB3-AS1: 0.70× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GCG, LINC01205, COX7B2 |
| cells under [[Tofacitinib (drug)]] 0.05 µM | B | MSRB3-AS1 activity lowers the cells' numbers under Tofacitinib 0.05 µM (makes them more sensitive) | lines that do not express MSRB3-AS1 (42) vs lines expressing it (6) | the lines without MSRB3-AS1: 1.39× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GCG, LINC01205, COX7B2 |
| cells under [[Selinexor (drug)]] 0.5 µM | B | MSRB3-AS1 activity lowers the cells' numbers under Selinexor 0.5 µM (makes them more sensitive) | lines that do not express MSRB3-AS1 (42) vs lines expressing it (6) | the lines without MSRB3-AS1: 1.23× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GCG, LINC01205, COX7B2 |
| [[LINC01205]] | C | MSRB3-AS1 activity raises LINC01205's level | lines that do not express MSRB3-AS1 (42) vs lines expressing it (8) | 5.01× lower at baseline in the lines without MSRB3-AS1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GCG, LINC01205, COX7B2; co-absent with the target |
| [[COX7B2]] | C | MSRB3-AS1 activity raises COX7B2's level | lines that do not express MSRB3-AS1 (42) vs lines expressing it (8) | 3.95× lower at baseline in the lines without MSRB3-AS1 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GCG, LINC01205, COX7B2; co-absent with the target |
| [[LINC01812]] | C | MSRB3-AS1 activity raises LINC01812's level | lines that do not express MSRB3-AS1 (42) vs lines expressing it (8) | 2.31× lower at baseline in the lines without MSRB3-AS1 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GCG, LINC01205, COX7B2; co-absent with the target |
| [[GCG]] | C | MSRB3-AS1 activity raises GCG's level | lines that do not express MSRB3-AS1 (42) vs lines expressing it (8) | 3.11× lower at baseline in the lines without MSRB3-AS1 | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GCG, LINC01205, COX7B2; co-absent with the target |

## Where it sits

- **Module**: [[Module 087]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.437). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (54.9, 28.3); signed map (14.8, 48.2). **Vector** length 33.0, 12.5% of its response variance represented; |z| ≥ 3 in 206 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.2 | +6.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.1 | -0.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.0 | +5.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.0 | +5.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +0.8 | +6.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | +0.7 | +1.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +0.6 | +0.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +0.6 | -0.4 |
|  | [[vincristine (drug)]] 0.5 µM |  | +0.6 | +2.8 |
| fall | [[Radotinib (drug)]] 5 µM |  | -1.1 | -3.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -0.9 | -1.4 |
|  | [[Trametinib (drug)]] 5 µM |  | -0.9 | -4.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -0.8 | -3.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -0.8 | -4.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -0.8 | -3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.7 | -5.7 |

## What is on record

|  |  |
|---|---|
| Name | MSRB3 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 12q14.3 — chr12:65,466,820-65,642,372 (-) |
| Ensembl biotype | lncRNA |
| Also known as | RP11-230G5.2 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53386](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53386) · Entrez [100507065](https://www.ncbi.nlm.nih.gov/gene/100507065) · Ensembl [ENSG00000250748](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000250748)

## Data

Gene col 14711: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14711); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14711, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14711]; `tensor/DDL_lfc|DDL_z.npy` [14711]; `embed/gene_vectors.npy` [14711]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14711 or target_col == 14711). Every well: [[MSRB3-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MSRB3-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
