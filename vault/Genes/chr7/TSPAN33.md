---
symbol: "TSPAN33"
type: "gene"
col: 8163
ensembl_id: "ENSG00000158457"
name: "tetraspanin 33"
location: "7q32.1"
module: 115
arm: "+"
pooled_cpm: 4.33
n_lines_expressing: 38
n_dd_up: 21
n_dd_down: 5
n_dd_up_clean: 14
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 15
direction_downstream: 35
tags: ["gene", "module/115"]
generated_by: "tahoemap"
---

# TSPAN33

*tetraspanin 33* — 7q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (7 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 5.34× (z +17.6, q 0e+00, up in 34 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.691× (z -3.9, q 0.050, down in 10 of 25 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SERAC1]] (+0.72, fdr 1e-05), [[BLVRA]] (+0.71, fdr 3e-05), [[RIMS3]] (+0.70, fdr 1e-05); moves opposite to [[PCBP1-AS1]] (-0.72, fdr 3e-05), [[ERMAP]] (-0.69, fdr 3e-05), [[ST7L]] (-0.69, fdr 3e-05).
> It is in [[Module 115]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[RNF144B]] → it (grade B ⚠); 35 go from it, the strongest it → [[ZC3H4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8163.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **5.34×** | +17.6 | 0e+00 | 34/35 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **5.18×** | +17.2 | 0e+00 | 32/36 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.05×** | +17.0 | 0e+00 | 32/35 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.32×** | +12.6 | 4e-34 | 29/36 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.15×** | +11.6 | 6e-29 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.18×** | +11.6 | 7e-29 | 24/35 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **2.66×** | +10.3 | 7e-23 | 24/28 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.33×** | +8.9 | 5e-17 | 20/32 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.35×** | +8.3 | 8e-15 | 2/5 (HEC-1-A, LoVo) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **3.66×** | +7.1 | 7e-11 | 16/32 (PANC-1, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.96×** | +7.1 | 9e-11 | 7/14 (SW480, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.76×** | +6.0 | 1e-07 | 9/19 (A-427, NCI-H2030, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.61×** | +4.8 | 6e-05 | 7/18 (KATO III, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.53×** | +4.5 | 3e-04 | 8/34 (J82, LoVo, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.06×** | +4.0 | 0.003 | 1/10 (SW480) | inconsistent across doses | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Brivudine (drug)]] 0.5 µM |  | **1.67×** | +3.7 | 0.008 | 3/33 (A-427, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.42×** | +3.5 | 0.015 | 6/30 (A549, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.38×** | +3.4 | 0.020 | 1/34 (PANC-1) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.60×** | +3.4 | 0.020 | 5/23 (SHP-77, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.38×** | +3.1 | 0.051 | 3/25 (SW1417, HEC-1-A, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8163.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.691×** | -3.9 | 0.050 | 10/25 (RKO, A-172, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.775×** | -3.7 | 0.050 | 14/28 (LoVo, A-427, …) | rises with dose | composition shift |
| [[Radotinib (drug)]] 0.05 µM |  | **0.716×** | -3.5 | 0.085 | 1/35 (Panc 03.27) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 5 µM |  | **0.538×** | -3.4 | 0.085 | 1/34 (Panc 03.27) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.714×** | -3.4 | 0.085 | 8/34 (RKO, SNU-1, …) | top dose only | cell-cycle shift (explains ~3% here); composition shift |
| [[Methylprednisolone succinate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.734× | -3.2 | 0.12 | 4/36 (SW48, BT-474, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8163. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 2.27 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 11.8× (z +9.8) | — |
| [[RKO (line)]] | wt | 9.16 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0946× (z -9.5) |
| [[A-172 (line)]] | wt | 4.08 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.02 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.799 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.544 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.719 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.799 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.663 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.40 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.626 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.841 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.906 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.999 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.75 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.902 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.19 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8163), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SERAC1]] | +0.72 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[BLVRA]] | +0.71 | +0.45 / +0.70 | both halves | 3e-05 |  |
| [[RIMS3]] | +0.70 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[RGS10]] | +0.68 | +0.44 / +0.66 | both halves | 3e-05 |  |
| [[PAFAH1B3]] | +0.68 | +0.39 / +0.52 | both halves | 6e-05 |  |
| [[SBK1]] | +0.68 | +0.52 / +0.70 | both halves | 1e-05 |  |
| [[TNNI3]] | +0.67 | +0.45 / +0.66 | both halves | 3e-05 |  |
| [[ANKRD27]] | +0.67 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[SLC29A4]] | +0.67 | +0.42 / +0.64 | both halves | 4e-05 |  |
| [[ARRB2]] | +0.67 | +0.42 / +0.63 | both halves | 4e-05 |  |
| [[ARHGAP44]] | +0.67 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[DNMT3B]] | +0.67 | +0.46 / +0.59 | both halves | 3e-05 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCBP1-AS1]] | -0.72 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[ERMAP]] | -0.69 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[ST7L]] | -0.69 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[CLHC1]] | -0.69 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[RFX3-DT]] | -0.69 | -0.50 / -0.33 | both halves | 1e-04 |  |
| [[LEKR1]] | -0.69 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[ZNF337-AS1]] | -0.68 | -0.55 / -0.15 | ⚠ one half (not replicated) | 0.001 |  |
| [[WARS2-AS1]] | -0.67 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[CYREN]] | -0.67 | -0.54 / -0.38 | both halves | 6e-05 |  |
| [[MCTS1]] | -0.67 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[CSTF3]] | -0.67 | -0.50 / -0.38 | both halves | 7e-05 |  |
| [[UBE3B]] | -0.66 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[PBLD]] | -0.66 | -0.45 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 14, C 1. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF144B]] | B | RNF144B activity lowers TSPAN33's level | lines that do not express RNF144B (15) vs lines expressing it (35) | 2.08× higher at baseline in the lines without RNF144B | 0.002 | ⚠ within organs, on part of the lines; also absent: SPTLC3, TMEM92-AS1, ITGA2; maybe low, not absent |
| [[SEMA6B]] | B | SEMA6B activity raises TSPAN33's level | lines that do not express SEMA6B (14) vs lines expressing it (36) | 2.09× lower at baseline in the lines without SEMA6B | 0.004 | ⚠ within organs, on part of the lines; also absent: FAM78B, BOLA3-DT, SLC4A3; maybe low, not absent |
| [[RET]] | B | RET activity raises TSPAN33's level | lines that do not express RET (28) vs lines expressing it (22) | 1.64× lower at baseline in the lines without RET | 0.044 | ⚠ within organs, on part of the lines; also absent: CHD5, KIF1A, NPTX1 |
| [[EGFL7]] | B | EGFL7 activity raises TSPAN33's level | lines that do not express EGFL7 (9) vs lines expressing it (41) | 1.78× lower at baseline in the lines without EGFL7 | 0.055 | ⚠ within organs, on part of the lines; also absent: KCTD15 |
| [[OTUD7A]] | B | OTUD7A activity raises TSPAN33's level | lines that do not express OTUD7A (6) vs lines expressing it (44) | 2.04× lower at baseline in the lines without OTUD7A | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000256673, WWOX, RUNDC3A-AS1; maybe low, not absent |
| [[REEP1]] | B | REEP1 activity raises TSPAN33's level | lines that do not express REEP1 (10) vs lines expressing it (40) | 1.57× lower at baseline in the lines without REEP1 | 0.067 | ⚠ within organs, on part of the lines; also absent: SEPTIN3; maybe low, not absent |
| [[LHX2]] | B | LHX2 activity raises TSPAN33's level | lines that do not express LHX2 (26) vs lines expressing it (24) | 1.90× lower at baseline in the lines without LHX2 | 0.068 | ⚠ within organs, on part of the lines; also absent: CECR2, COL4A4, GHR |
| [[RALGPS2]] | B | RALGPS2 activity lowers TSPAN33's level | lines that do not express RALGPS2 (7) vs lines expressing it (43) | 1.99× higher at baseline in the lines without RALGPS2 | 0.078 | ⚠ within organs, on part of the lines; also absent: NABP1, ITGA2-AS1, GSDMD; maybe low, not absent |
| [[CCDC69]] | B | CCDC69 activity raises TSPAN33's level | lines that do not express CCDC69 (11) vs lines expressing it (39) | 1.06× lower at baseline in the lines without CCDC69 | 0.079 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SBK1]] | B | SBK1 activity raises TSPAN33's level | lines that do not express SBK1 (16) vs lines expressing it (34) | 2.12× lower at baseline in the lines without SBK1 | 0.083 | ⚠ within organs, on part of the lines; also absent: CASZ1, LAMP3, CAMSAP3 |
| [[TPST1]] | B | TPST1 activity raises TSPAN33's level | lines that do not express TPST1 (5) vs lines expressing it (45) | 1.96× lower at baseline in the lines without TPST1 | 0.083 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CYP46A1, CSRP2, MYO5A |
| [[SLC17A7]] | B | SLC17A7 activity raises TSPAN33's level | lines that do not express SLC17A7 (9) vs lines expressing it (41) | 1.87× lower at baseline in the lines without SLC17A7 | 0.084 | ⚠ within organs, on part of the lines; also absent: GXYLT2, ITGA10, NT5M; maybe low, not absent |

### Downstream of this gene

*35 arrows, 35 of them with an alert ⚠; grade A 0, B 35, C 0. Shown: the 12 strongest; 23 more arrows (23 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZC3H4]] | B | TSPAN33 activity raises ZC3H4's level | lines that do not express TSPAN33 (12) vs lines expressing it (38) | 1.40× lower at baseline in the lines without TSPAN33 | 0.003 | ⚠ within organs, on part of the lines; also absent: SRCIN1, CRACD, GNAZ; maybe low, not absent |
| [[SBK1]] | B | TSPAN33 activity raises SBK1's level | lines that do not express TSPAN33 (12) vs lines expressing it (38) | 3.05× lower at baseline in the lines without TSPAN33 | 0.005 | ⚠ within organs, on part of the lines; also absent: SRCIN1, CRACD, GNAZ; maybe low, not absent |
| [[PRKAR1B]] | B | TSPAN33 activity raises PRKAR1B's level | lines that do not express TSPAN33 (12) vs lines expressing it (38) | 2.70× lower at baseline in the lines without TSPAN33 | 0.005 | ⚠ within organs, on part of the lines; also absent: SRCIN1, CRACD, GNAZ; maybe low, not absent |
| [[OTUD7A]] | B | TSPAN33 activity raises OTUD7A's level | lines that do not express TSPAN33 (12) vs lines expressing it (38) | 2.41× lower at baseline in the lines without TSPAN33 | 0.014 | ⚠ within organs, on part of the lines; also absent: SRCIN1, CRACD, GNAZ; maybe low, not absent |
| [[DPY19L1P2]] | B | TSPAN33 activity raises DPY19L1P2's level | lines that do not express TSPAN33 (12) vs lines expressing it (38) | 1.34× lower at baseline in the lines without TSPAN33 | 0.016 | ⚠ within organs, on part of the lines; also absent: SRCIN1, CRACD, GNAZ; maybe low, not absent |
| [[ZSCAN2]] | B | TSPAN33 activity raises ZSCAN2's level | lines that do not express TSPAN33 (12) vs lines expressing it (38) | 1.59× lower at baseline in the lines without TSPAN33 | 0.017 | ⚠ within organs, on part of the lines; also absent: SRCIN1, CRACD, GNAZ; maybe low, not absent |
| [[SLC29A4]] | B | TSPAN33 activity raises SLC29A4's level | lines that do not express TSPAN33 (12) vs lines expressing it (38) | 2.01× lower at baseline in the lines without TSPAN33 | 0.019 | ⚠ within organs, on part of the lines; also absent: SRCIN1, CRACD, GNAZ; maybe low, not absent |
| [[P2RY11]] | B | TSPAN33 activity raises P2RY11's level | lines that do not express TSPAN33 (12) vs lines expressing it (38) | 1.58× lower at baseline in the lines without TSPAN33 | 0.020 | ⚠ within organs, on part of the lines; also absent: SRCIN1, CRACD, GNAZ; maybe low, not absent |
| [[GTF2IP4]] | B | TSPAN33 activity raises GTF2IP4's level | lines that do not express TSPAN33 (12) vs lines expressing it (38) | 1.42× lower at baseline in the lines without TSPAN33 | 0.022 | ⚠ within organs, on part of the lines; also absent: SRCIN1, CRACD, GNAZ; maybe low, not absent |
| [[SEMA6B]] | B | TSPAN33 activity raises SEMA6B's level | lines that do not express TSPAN33 (12) vs lines expressing it (38) | 2.46× lower at baseline in the lines without TSPAN33 | 0.022 | ⚠ within organs, on part of the lines; also absent: SRCIN1, CRACD, GNAZ; maybe low, not absent |
| [[ASRGL1]] | B | TSPAN33 activity raises ASRGL1's level | lines that do not express TSPAN33 (12) vs lines expressing it (38) | 2.56× lower at baseline in the lines without TSPAN33 | 0.026 | ⚠ within organs, on part of the lines; also absent: SRCIN1, CRACD, GNAZ; maybe low, not absent |
| [[MFF-DT]] | B | TSPAN33 activity raises MFF-DT's level | lines that do not express TSPAN33 (12) vs lines expressing it (38) | 1.29× lower at baseline in the lines without TSPAN33 | 0.031 | ⚠ within organs, on part of the lines; also absent: SRCIN1, CRACD, GNAZ; maybe low, not absent |

## Where it sits

- **Module**: [[Module 115]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.754). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (0.8, 2.0); signed map (-38.4, -5.1). **Vector** length 52.5, 8.90% of its response variance represented; |z| ≥ 3 in 733 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +11.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.9 | +8.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.4 | +12.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.4 | +17.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.1 | +17.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.5 | +7.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.8 | +1.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.3 | +2.3 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +1.3 | +3.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.1 | -3.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -2.7 | -3.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | +1.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.8 | -2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.5 | -0.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.3 | -1.9 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.2 | -2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.1 | -0.0 |

## What is on record

|  |  |
|---|---|
| Name | tetraspanin 33 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q32.1 — chr7:129,144,707-129,169,699 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC50844, Penumbra |
| Gene groups (HGNC) | Tetraspanin family |
| Reactome | 1 pathways, smallest: Amyloid fiber formation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86UF1](https://www.uniprot.org/uniprotkb/Q86UF1) (Tetraspanin-33):

> Part of TspanC8 subgroup, composed of 6 members that interact with the transmembrane metalloprotease ADAM10. This interaction is required for ADAM10 exit from the endoplasmic reticulum and for enzymatic maturation and trafficking to the cell surface as well as substrate specificity. Different TspanC8/ADAM10 complexes have distinct substrates. Plays an important role in normal erythropoiesis (By similarity). It has a role in the differentiation of erythroid progenitors (By similarity). …

**Summary**, from NCBI Gene [340348](https://www.ncbi.nlm.nih.gov/gene/340348):

> Enables enzyme binding activity. Involved in pore complex assembly; protein localization to plasma membrane; and protein maturation. Located in plasma membrane. Part of pore complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28743](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28743) · Entrez [340348](https://www.ncbi.nlm.nih.gov/gene/340348) · UniProt [Q86UF1](https://www.uniprot.org/uniprotkb/Q86UF1) · Ensembl [ENSG00000158457](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158457)

## Data

Gene col 8163: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8163); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8163, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8163]; `tensor/DDL_lfc|DDL_z.npy` [8163]; `embed/gene_vectors.npy` [8163]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8163 or target_col == 8163). Every well: [[TSPAN33 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TSPAN33.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
