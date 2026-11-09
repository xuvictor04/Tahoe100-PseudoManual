---
symbol: "JAKMIP2-AS1"
type: "gene"
col: 15967
ensembl_id: "ENSG00000280780"
name: "JAKMIP2 antisense RNA 1"
location: "5q32"
module: 27
arm: "+"
pooled_cpm: 6.29
n_lines_expressing: 12
n_dd_up: 9
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 36
direction_downstream: 42
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# JAKMIP2-AS1

*JAKMIP2 antisense RNA 1* — 5q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.94× (z +9.2, q 2e-17, up in 1 of 4 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW480 0.0818×); [[Digitoxin (drug)]] 5 µM in 1 line (SW480 0.0307×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (SW480 0.0414×; ⚠ cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (SW480 0.0775×); [[Auranofin (drug)]] 5 µM in 1 line (SW480 0.0892×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[APCDD1]] (+0.87, fdr 7e-06), [[ST18]] (+0.84, fdr 7e-06), [[F10]] (+0.83, fdr 7e-06); moves opposite to [[PASD1]] (-0.64, fdr 1e-05).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 36 arrows point to it, the strongest [[TRPV4]] → it (grade B ⚠); 42 go from it, the strongest it → [[MIAT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15967.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.94×** | +9.2 | 2e-17 | 1/4 (A-172) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.00×** | +8.0 | 2e-13 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.70×** | +7.9 | 5e-13 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.72×** | +5.6 | 3e-06 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **2.17×** | +5.2 | 2e-05 | 3/6 (SW480, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.86×** | +3.6 | 0.031 | 2/5 (SW480, SW1417) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.52×** | +3.5 | 0.039 | 3/6 (SW480, LOX-IMVI, …) | all doses, flat |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.18×** | +3.4 | 0.054 | 1/3 (SW1417) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **2.10×** | +3.2 | 0.090 | 1/4 (LOX-IMVI) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 1.73× | +3.1 | 0.10 | 1/5 (SW480) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.60× | +3.0 | 0.12 | 2/8 (SW480, A-172) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.51× | +3.0 | 0.12 | 1/6 (SW480) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15967.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW480 0.0818×); [[Digitoxin (drug)]] 5 µM in 1 line (SW480 0.0307×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (SW480 0.0414×; ⚠ cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (SW480 0.0775×); [[Auranofin (drug)]] 5 µM in 1 line (SW480 0.0892×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | 0.543× | -3.7 | 0.12 | 4/6 (SW480, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.581× | -3.3 | 0.28 | 2/7 (SW480, A-172) | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | 0.606× | -3.0 | 0.36 | 0/7 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.43 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15967. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 96.9 | 0 | 14 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0818× (z -16.2) |
| [[A-172 (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.902 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.861 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.966 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.945 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.832 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.869 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.946 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.940 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.812 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.871 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.915 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.891 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.918 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.937 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.919 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.808 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.769 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.960 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.23 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15967), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APCDD1]] | +0.87 | +0.85 / +0.85 | both halves | 7e-06 | **novel candidate** |
| [[ST18]] | +0.84 | +0.78 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[F10]] | +0.83 | +0.78 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[FGF20]] | +0.78 | +0.79 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[NOTUM]] | +0.76 | +0.68 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[PSD2]] | +0.75 | +0.77 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[B3GAT1-DT]] | +0.75 | +0.77 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[SMOC2]] | +0.74 | +0.71 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[LINC01980]] | +0.74 | +0.78 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[LINC02058]] | +0.74 | +0.61 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[RMST]] | +0.73 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[VWA2]] | +0.71 | +0.69 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PASD1]] | -0.64 | -0.62 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*36 arrows, 36 of them with an alert ⚠; grade A 0, B 2, C 34. Shown: the 12 strongest; 24 more arrows (24 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRPV4]] | B | TRPV4 activity raises JAKMIP2-AS1's level | lines that do not express TRPV4 (26) vs lines expressing it (24) | 1.44× lower at baseline in the lines without TRPV4 | 0.068 | ⚠ within organs, on part of the lines; also absent: SHROOM4, IRAG2, ADAMTS4; maybe low, not absent |
| [[MAP2K2]] | B | MAP2K2 activity lowers JAKMIP2-AS1's level | compounds that target MAP2K2: 2 of 2 raise it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; shared targets |
| [[PSG1]] | C | PSG1 activity raises JAKMIP2-AS1's level | lines that do not express PSG1 (45) vs lines expressing it (5) | 4.33× lower at baseline in the lines without PSG1 | 1e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, KRT5, APOB; co-absent with the target |
| [[KRT5]] | C | KRT5 activity raises JAKMIP2-AS1's level | lines that do not express KRT5 (46) vs lines expressing it (4) | 6.37× lower at baseline in the lines without KRT5 | 4e-04 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, BMP10, TBXT; co-absent with the target |
| [[SHISA9]] | C | SHISA9 activity raises JAKMIP2-AS1's level | lines that do not express SHISA9 (38) vs lines expressing it (12) | 2.09× lower at baseline in the lines without SHISA9 | 0.002 | ⚠ within organs, on part of the lines; also absent: LHFPL3-AS1, S100A1, LINC01456; maybe low, not absent; co-absent with the target |
| [[PHYHIPL]] | C | PHYHIPL activity raises JAKMIP2-AS1's level | lines that do not express PHYHIPL (39) vs lines expressing it (11) | 2.24× lower at baseline in the lines without PHYHIPL | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, AFP, CALCA; co-absent with the target |
| [[SLC25A24P1]] | C | SLC25A24P1 activity raises JAKMIP2-AS1's level | lines that do not express SLC25A24P1 (40) vs lines expressing it (10) | 2.19× lower at baseline in the lines without SLC25A24P1 | 0.004 | ⚠ within organs, on part of the lines; also absent: LINC01425, ENSG00000275016, MAGEB2; co-absent with the target |
| [[HS3ST5]] | C | HS3ST5 activity raises JAKMIP2-AS1's level | lines that do not express HS3ST5 (29) vs lines expressing it (21) | 1.65× lower at baseline in the lines without HS3ST5 | 0.008 | ⚠ within organs, on part of the lines; also absent: NOL4, ESRRG, RUNX1T1; maybe low, not absent; co-absent with the target |
| [[MIR3667HG]] | C | MIR3667HG activity raises JAKMIP2-AS1's level | lines that do not express MIR3667HG (38) vs lines expressing it (12) | 2.00× lower at baseline in the lines without MIR3667HG | 0.013 | ⚠ within organs, on part of the lines; also absent: GTSF1, ENSG00000288098, CALCA; co-absent with the target |
| [[LINC00491]] | C | LINC00491 activity raises JAKMIP2-AS1's level | lines that do not express LINC00491 (33) vs lines expressing it (17) | 1.72× lower at baseline in the lines without LINC00491 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: APCDD1L, LINC01905, ADGRG7; co-absent with the target |
| [[PASD1]] | C | PASD1 activity raises JAKMIP2-AS1's level | lines that do not express PASD1 (41) vs lines expressing it (9) | 2.35× lower at baseline in the lines without PASD1 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SSX1, LINC00879, RNF17; maybe low, not absent; co-absent with the target |
| [[LINC02315]] | C | LINC02315 activity raises JAKMIP2-AS1's level | lines that do not express LINC02315 (31) vs lines expressing it (19) | 1.68× lower at baseline in the lines without LINC02315 | 0.036 | ⚠ within organs, on part of the lines; also absent: GABRG2, COX7B2, SLC25A24P1; co-absent with the target |

### Downstream of this gene

*42 arrows, 42 of them with an alert ⚠; grade A 0, B 7, C 35. Shown: the 12 strongest; 30 more arrows (30 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIAT]] | B | JAKMIP2-AS1 activity raises MIAT's level | lines that do not express JAKMIP2-AS1 (38) vs lines expressing it (12) | 2.68× lower at baseline in the lines without JAKMIP2-AS1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent |
| [[DKK2]] | B | JAKMIP2-AS1 activity raises DKK2's level | lines that do not express JAKMIP2-AS1 (38) vs lines expressing it (12) | 2.31× lower at baseline in the lines without JAKMIP2-AS1 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent |
| [[MAN1A1]] | B | JAKMIP2-AS1 activity raises MAN1A1's level | lines that do not express JAKMIP2-AS1 (38) vs lines expressing it (12) | 2.00× lower at baseline in the lines without JAKMIP2-AS1 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent |
| [[F10]] | B | JAKMIP2-AS1 activity raises F10's level | lines that do not express JAKMIP2-AS1 (38) vs lines expressing it (12) | 1.50× lower at baseline in the lines without JAKMIP2-AS1 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent |
| [[LARGE2]] | B | JAKMIP2-AS1 activity raises LARGE2's level | lines that do not express JAKMIP2-AS1 (38) vs lines expressing it (12) | 1.46× lower at baseline in the lines without JAKMIP2-AS1 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent |
| [[RGCC]] | B | JAKMIP2-AS1 activity raises RGCC's level | lines that do not express JAKMIP2-AS1 (38) vs lines expressing it (12) | 1.58× lower at baseline in the lines without JAKMIP2-AS1 | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent |
| [[FGD3]] | B | JAKMIP2-AS1 activity raises FGD3's level | lines that do not express JAKMIP2-AS1 (38) vs lines expressing it (12) | 1.31× lower at baseline in the lines without JAKMIP2-AS1 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent |
| [[RMST]] | C | JAKMIP2-AS1 activity raises RMST's level | lines that do not express JAKMIP2-AS1 (38) vs lines expressing it (12) | 3.80× lower at baseline in the lines without JAKMIP2-AS1 | 9e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent; co-absent with the target |
| [[ST18]] | C | JAKMIP2-AS1 activity raises ST18's level | lines that do not express JAKMIP2-AS1 (38) vs lines expressing it (12) | 3.02× lower at baseline in the lines without JAKMIP2-AS1 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent; co-absent with the target |
| [[PSG1]] | C | JAKMIP2-AS1 activity raises PSG1's level | lines that do not express JAKMIP2-AS1 (38) vs lines expressing it (12) | 1.07× lower at baseline in the lines without JAKMIP2-AS1 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent; co-absent with the target |
| [[RIMBP2]] | C | JAKMIP2-AS1 activity raises RIMBP2's level | lines that do not express JAKMIP2-AS1 (38) vs lines expressing it (12) | 3.64× lower at baseline in the lines without JAKMIP2-AS1 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent; co-absent with the target |
| [[HS3ST5]] | C | JAKMIP2-AS1 activity raises HS3ST5's level | lines that do not express JAKMIP2-AS1 (38) vs lines expressing it (12) | 3.74× lower at baseline in the lines without JAKMIP2-AS1 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.805). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.8, 43.4); signed map (62.7, 16.2). **Vector** length 35.5, 18.5% of its response variance represented; |z| ≥ 3 in 158 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.1 | +8.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.0 | +2.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.0 | +5.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +0.8 | +1.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +0.8 | +3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +0.7 | +3.6 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +0.7 | +1.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.0 | -3.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -0.9 | -2.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.8 | -2.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -0.8 | -3.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.6 | -3.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.6 | -3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.5 | -1.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.5 | -3.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.5 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | JAKMIP2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5q32 — chr5:147,559,994-147,694,827 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:27203](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27203) · Entrez [153469](https://www.ncbi.nlm.nih.gov/gene/153469) · Ensembl [ENSG00000280780](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000280780)

## Data

Gene col 15967: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15967); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15967, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15967]; `tensor/DDL_lfc|DDL_z.npy` [15967]; `embed/gene_vectors.npy` [15967]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15967 or target_col == 15967). Every well: [[JAKMIP2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/JAKMIP2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
