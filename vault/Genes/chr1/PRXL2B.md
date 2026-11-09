---
symbol: "PRXL2B"
type: "gene"
col: 8109
ensembl_id: "ENSG00000157870"
name: "peroxiredoxin like 2B"
location: "1p36.32"
module: 31
arm: "+"
pooled_cpm: 5.59
n_lines_expressing: 49
n_dd_up: 16
n_dd_down: 11
n_dd_up_clean: 10
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 11
direction_downstream: 0
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# PRXL2B

*peroxiredoxin like 2B* — 1p36.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.68× (z +11.2, q 1e-26, up in 6 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[XRK3F2 (drug)]] 0.5 µM: 1.77× (z +4.8, q 2e-04, up in 8 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.309× (z -7.1, q 9e-10, down in 24 of 38 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CRACR2B]] (+0.60, fdr 1e-05), [[RHPN1]] (+0.56, fdr 4e-05), [[TRAF4]] (+0.55, fdr 1e-05); moves opposite to [[MESD]] (-0.47, fdr 2e-04), [[ARPC3]] (-0.46, fdr 2e-04), [[TMED5]] (-0.46, fdr 2e-04).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[PCDH1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8109.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.68×** | +11.2 | 1e-26 | 6/9 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.28×** | +9.8 | 4e-20 | 16/21 (HT-29, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.82×** | +6.6 | 1e-08 | 7/16 (LS 180, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.52×** | +4.9 | 1e-04 | 12/28 (AsPC-1, Panc 03.27, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.77×** | +4.8 | 2e-04 | 8/25 (SW480, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.53×** | +4.6 | 3e-04 | 8/32 (J82, SW480, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.46×** | +4.4 | 7e-04 | 11/44 (MIA PaCa-2, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~8% here); position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.64×** | +4.2 | 0.002 | 9/37 (HOP62, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ferulic acid (drug)]] 5 µM |  | **1.36×** | +3.5 | 0.029 | 3/43 (J82, SW 900, …) | rises with dose | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.50×** | +3.4 | 0.033 | 4/31 (PANC-1, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +3.4 | 0.033 | 5/25 (HOP62, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.76×** | +3.4 | 0.033 | 3/14 (HEC-1-A, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **1.33×** | +3.3 | 0.038 | 7/33 (CFPAC-1, NCI-H2347, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.32×** | +3.2 | 0.051 | 7/40 (NCI-H23, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Bicalutamide (drug)]] 0.5 µM |  | **1.31×** | +3.1 | 0.063 | 3/43 (A498, KATO III, …) | inconsistent across doses | position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.067 | 5/43 (BT-474, NCI-H23, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8109.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.309×** | -7.1 | 9e-10 | 24/38 (Panc 03.27, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.339×** | -6.5 | 2e-08 | 23/35 (Panc 03.27, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.601×** | -6.1 | 2e-07 | 17/45 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.626×** | -5.3 | 2e-05 | 16/43 (HT-29, LoVo, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.665×** | -4.9 | 1e-04 | 19/44 (PANC-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.672×** | -4.8 | 2e-04 | 17/37 (PANC-1, HT-29, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.682×** | -4.6 | 4e-04 | 17/45 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.770×** | -4.4 | 6e-04 | 15/44 (NCI-H1573, SW1417, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.737×** | -3.7 | 0.015 | 13/43 (LoVo, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.739×** | -3.6 | 0.016 | 13/42 (SW 900, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.834× | -3.1 | 0.092 | 14/37 (SW480, CFPAC-1, …) | two highest doses | composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.761×** | -3.1 | 0.092 | 13/43 (SW1417, HEC-1-A, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.779× | -3.0 | 0.11 | 15/43 (HepG2/C3A, KATO III, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8109. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 8.71 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0581× (z -10.5) |
| [[PANC-1 (line)]] | alt | 7.61 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.207× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 14.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 9.58 | 0 | 1 | — | [[Trimetrexate (drug)]] 0.05 µM 0.0692× (z -10.1) |
| [[SHP-77 (line)]] | alt | 5.98 | 0 | 1 | — | [[Fluvoxamine (maleate) (drug)]] 0.5 µM 0.107× (z -8.7) |
| [[SW480 (line)]] | alt | 5.51 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.09 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.84 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.38 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 9.76 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.48 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.73 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.54 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8109), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRACR2B]] | +0.60 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[RHPN1]] | +0.56 | +0.53 / +0.42 | both halves | 4e-05 |  |
| [[TRAF4]] | +0.55 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[NAPRT]] | +0.55 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[CYP2S1]] | +0.54 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[ARHGEF16]] | +0.52 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[ROGDI]] | +0.51 | +0.39 / +0.41 | both halves | 5e-05 |  |
| [[ABHD11]] | +0.51 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[SAMD10]] | +0.50 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[CISD3]] | +0.50 | +0.45 / +0.40 | both halves | 5e-05 |  |
| [[SLC37A4]] | +0.50 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[ESRP2]] | +0.50 | +0.57 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MESD]] | -0.47 | -0.29 / -0.41 | both halves | 2e-04 |  |
| [[ARPC3]] | -0.46 | -0.48 / -0.32 | both halves | 2e-04 |  |
| [[TMED5]] | -0.46 | -0.31 / -0.46 | both halves | 2e-04 |  |
| [[ANKUB1]] | -0.44 | -0.39 / -0.37 | both halves | 9e-05 |  |
| [[TMEM167A]] | -0.44 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[SEM1]] | -0.43 | -0.43 / -0.26 | both halves | 4e-04 |  |
| [[PCGF3-AS1]] | -0.43 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[USP34-DT]] | -0.43 | -0.35 / -0.27 | both halves | 3e-04 |  |
| [[LINC01019]] | -0.42 | -0.36 / -0.36 | both halves | 1e-04 |  |
| [[SDHC]] | -0.42 | -0.37 / -0.36 | both halves | 1e-04 |  |
| [[METTL25]] | -0.41 | -0.34 / -0.33 | both halves | 1e-04 |  |
| [[NUDT13]] | -0.41 | -0.32 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCDH1]] | B | PCDH1 activity raises PRXL2B's level | lines that do not express PCDH1 (20) vs lines expressing it (30) | 1.77× lower at baseline in the lines without PCDH1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29 |
| [[CRACR2B]] | B | CRACR2B activity raises PRXL2B's level | lines that do not express CRACR2B (11) vs lines expressing it (39) | 1.77× lower at baseline in the lines without CRACR2B | 0.008 | ⚠ within organs, on part of the lines; also absent: PNPLA4, ENSG00000285679, DAPK2 |
| [[ERBB3]] | B | ERBB3 activity raises PRXL2B's level | lines that do not express ERBB3 (27) vs lines expressing it (23) | 1.66× lower at baseline in the lines without ERBB3 | 0.020 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM |
| [[TJP3]] | B | TJP3 activity raises PRXL2B's level | lines that do not express TJP3 (29) vs lines expressing it (21) | 1.59× lower at baseline in the lines without TJP3 | 0.020 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1 |
| [[CLDN3]] | B | CLDN3 activity raises PRXL2B's level | lines that do not express CLDN3 (28) vs lines expressing it (22) | 1.52× lower at baseline in the lines without CLDN3 | 0.028 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, ESRP1 |
| [[CGN]] | B | CGN activity raises PRXL2B's level | lines that do not express CGN (21) vs lines expressing it (29) | 1.56× lower at baseline in the lines without CGN | 0.030 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, CRACDL, CAMSAP3 |
| [[PRR36]] | B | PRR36 activity raises PRXL2B's level | lines that do not express PRR36 (19) vs lines expressing it (31) | 1.41× lower at baseline in the lines without PRR36 | 0.055 | ⚠ within organs, on part of the lines; also absent: NUP210, TTC9, CGN |
| [[CCDC88C]] | B | CCDC88C activity raises PRXL2B's level | lines that do not express CCDC88C (8) vs lines expressing it (42) | 1.71× lower at baseline in the lines without CCDC88C | 0.063 | ⚠ within organs, on part of the lines; also absent: SPTBN2, NUP210, NOXA1 |
| [[ARHGAP45]] | B | ARHGAP45 activity raises PRXL2B's level | lines that do not express ARHGAP45 (7) vs lines expressing it (43) | 1.78× lower at baseline in the lines without ARHGAP45 | 0.076 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[CLDN7]] | B | CLDN7 activity raises PRXL2B's level | lines that do not express CLDN7 (30) vs lines expressing it (20) | 1.67× lower at baseline in the lines without CLDN7 | 0.089 | ⚠ within organs, on part of the lines; also absent: ESRP1, ENSG00000262302, ST14 |
| [[ARHGEF16]] | B | ARHGEF16 activity raises PRXL2B's level | lines that do not express ARHGEF16 (14) vs lines expressing it (36) | 1.47× lower at baseline in the lines without ARHGEF16 | 0.089 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, KRT18, NRARP |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.356). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-9.6, 33.5); signed map (31.9, -34.3). **Vector** length 55.1, 7.46% of its response variance represented; |z| ≥ 3 in 932 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.7 | +2.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | +1.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | -0.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.1 | +4.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | +1.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.9 | +4.8 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.8 | +4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.6 | +2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +3.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.4 | +3.1 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -2.7 | -7.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.3 | -5.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | -6.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | -4.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -2.0 | -3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -3.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.3 | -1.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.2 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | peroxiredoxin like 2B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.32 — chr1:2,586,491-2,591,469 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC26818; previously C1orf93, FAM213B |
| Reactome | 4 pathways, smallest: Synthesis of Prostaglandins (PG) and Thromboxanes (TX); Arachidonate metabolism; Fatty acid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TBF2](https://www.uniprot.org/uniprotkb/Q8TBF2) (Prostamide/prostaglandin F synthase):

> Catalyzes the reduction of prostaglandin-ethanolamide H(2) (prostamide H(2)) to prostamide F(2alpha) with NADPH as proton donor. Also able to reduce prostaglandin H(2) to prostaglandin F(2alpha) (By similarity).

**Summary**, from NCBI Gene [127281](https://www.ncbi.nlm.nih.gov/gene/127281):

> Predicted to enable prostaglandin F synthase activity and thioredoxin peroxidase activity. Predicted to be involved in prostaglandin biosynthetic process. Located in extracellular exosome and mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28390](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28390) · Entrez [127281](https://www.ncbi.nlm.nih.gov/gene/127281) · UniProt [Q8TBF2](https://www.uniprot.org/uniprotkb/Q8TBF2) · Ensembl [ENSG00000157870](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157870)

## Data

Gene col 8109: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8109); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8109, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8109]; `tensor/DDL_lfc|DDL_z.npy` [8109]; `embed/gene_vectors.npy` [8109]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8109 or target_col == 8109). Every well: [[PRXL2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRXL2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
