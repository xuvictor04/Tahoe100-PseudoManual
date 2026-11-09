---
symbol: "SHROOM1"
type: "gene"
col: 8943
ensembl_id: "ENSG00000164403"
name: "shroom family member 1"
location: "5q31.1"
module: 11
arm: "+"
pooled_cpm: 4.86
n_lines_expressing: 48
n_dd_up: 16
n_dd_down: 17
n_dd_up_clean: 9
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# SHROOM1

*shroom family member 1* — 5q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.67× (z +5.4, q 4e-05, up in 1 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 1.59× (z +5.1, q 1e-04, up in 14 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.297× (z -13.2, q 3e-37, down in 34 of 43 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZSCAN29]] (+0.62, fdr 1e-05), [[KCNMB3]] (+0.61, fdr 4e-05), [[AUP1]] (+0.60, fdr 2e-05); moves opposite to [[CETN2]] (-0.61, fdr 2e-04), [[GM2A]] (-0.57, fdr 4e-05), [[GLG1]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[THNSL2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8943.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.67×** | +5.4 | 4e-05 | 1/9 (HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.59×** | +5.1 | 1e-04 | 14/42 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.84×** | +4.8 | 3e-04 | 11/33 (COLO 205, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.54×** | +4.7 | 3e-04 | 9/22 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +4.7 | 4e-04 | 10/28 (LoVo, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Thymol (drug)]] 0.5 µM |  | **1.44×** | +4.0 | 0.006 | 11/33 (SW480, SW48, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.67×** | +4.0 | 0.006 | 8/32 (HOP62, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.39×** | +3.6 | 0.025 | 10/35 (LoVo, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.37×** | +3.5 | 0.031 | 15/41 (LS 180, H4, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.37×** | +3.5 | 0.031 | 6/29 (CFPAC-1, A-427, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.37×** | +3.2 | 0.070 | 4/12 (SW1417, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.50×** | +3.2 | 0.070 | 4/37 (HepG2/C3A, SNU-423, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.33×** | +3.2 | 0.070 | 4/33 (CFPAC-1, HS-578T, …) | inconsistent across doses | position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +3.1 | 0.076 | 0/14 | top dose only | noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.49×** | +3.1 | 0.076 | 4/18 (SW1417, HS-578T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.32×** | +3.0 | 0.086 | 9/43 (SNU-1, A549, …) | two highest doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8943.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.297×** | -13.2 | 3e-37 | 34/43 (COLO 205, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.324×** | -12.3 | 3e-32 | 33/43 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.335×** | -11.9 | 2e-30 | 33/42 (SW1417, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.425×** | -9.3 | 2e-18 | 28/43 (KATO III, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.518×** | -7.2 | 8e-11 | 25/45 (NCI-H23, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.551×** | -6.5 | 8e-09 | 21/40 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.561×** | -6.3 | 2e-08 | 18/33 (A-427, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.339×** | -6.2 | 5e-08 | 22/41 (MIA PaCa-2, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.579×** | -6.0 | 2e-07 | 22/38 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.358×** | -5.9 | 3e-07 | 19/41 (LoVo, SW1417, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.387×** | -5.4 | 3e-06 | 22/34 (SK-MEL-2, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.700×** | -3.9 | 0.005 | 14/40 (LS 180, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.709×** | -3.7 | 0.008 | 9/44 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.713×** | -3.7 | 0.009 | 12/40 (SNU-1, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.793×** | -3.6 | 0.013 | 20/37 (COLO 205, SK-MEL-2, …) | rises with dose | position effect removed |
| [[Hexylresorcinol (drug)]] 0.5 µM |  | **0.753×** | -3.1 | 0.067 | 4/42 (SW480, HepG2/C3A, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8943. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 10.5 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0728× (z -14.4) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0372× (z -12.9) |
| [[SW480 (line)]] | alt | 8.28 | 0 | 3 | — | [[Belinostat (drug)]] 0.5 µM 0.258× (z -8.9) |
| [[KATO III (line)]] | alt | 3.19 | 0 | 2 | — | [[Panobinostat (drug)]] 0.05 µM 0.0256× (z -11.6) |
| [[LoVo (line)]] | wt | 5.93 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.101× (z -11.7) |
| [[MIA PaCa-2 (line)]] | alt | 8.27 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.0892× (z -10.5) |
| [[NCI-H460 (line)]] | wt | 2.66 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0759× (z -10.5) |
| [[SW1417 (line)]] | alt | 8.94 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0959× (z -11.5) |
| [[A-427 (line)]] | wt | 9.58 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.107× (z -10.3) |
| [[AsPC-1 (line)]] | alt | 8.46 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.122× (z -9.4) |
| [[HT-29 (line)]] | alt | 6.81 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0859× (z -9.8) |
| [[J82 (line)]] | alt | 3.45 | 0 | 1 | — | [[Arbutin (drug)]] 5 µM 0.0620× (z -9.1) |
| [[LS 180 (line)]] | wt | 8.87 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.135× (z -10.1) |
| [[NCI-H1792 (line)]] | alt | 3.91 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0807× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 3.94 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0530× (z -9.3) |
| [[RKO (line)]] | wt | 9.95 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.123× (z -9.1) |
| [[A-172 (line)]] | wt | 5.62 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.530 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.97 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.485 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.30 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.92 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8943), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZSCAN29]] | +0.62 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[KCNMB3]] | +0.61 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[AUP1]] | +0.60 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[EIF5]] | +0.60 | +0.56 / +0.38 | both halves | 7e-05 |  |
| [[GABPB2]] | +0.58 | +0.51 / +0.37 | both halves | 8e-05 |  |
| [[TRIM47]] | +0.58 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[CRCP]] | +0.57 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[FAM83H]] | +0.56 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[NME6]] | +0.56 | +0.47 / +0.46 | both halves | 3e-05 |  |
| [[WASHC1]] | +0.56 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[FIZ1]] | +0.56 | +0.52 / +0.29 | both halves | 2e-04 |  |
| [[PBDC1]] | +0.56 | +0.42 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CETN2]] | -0.61 | -0.48 / -0.29 | both halves | 2e-04 |  |
| [[GM2A]] | -0.57 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[GLG1]] | -0.56 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[EFHC1]] | -0.55 | -0.49 / -0.26 | both halves | 4e-04 |  |
| [[HSP90B1]] | -0.55 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[PCYOX1]] | -0.54 | -0.33 / -0.55 | both halves | 1e-04 |  |
| [[TMED4]] | -0.54 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[BSG]] | -0.54 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[ATP6AP2]] | -0.54 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[MLEC]] | -0.53 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[CALM3]] | -0.53 | -0.46 / -0.34 | both halves | 1e-04 |  |
| [[PARK7]] ⚠ | -0.53 | -0.33 / -0.49 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[DNAAF3]] | -0.53 | -0.34 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[THNSL2]] | B | THNSL2 activity raises SHROOM1's level | lines that do not express THNSL2 (19) vs lines expressing it (31) | 1.30× lower at baseline in the lines without THNSL2 | 0.099 | ⚠ within organs, on part of the lines; also absent: CRABP2, NPTX2, SULT4A1 |
| [[TRIM47]] | C | TRIM47 activity raises SHROOM1's level | lines that do not express TRIM47 (4) vs lines expressing it (46) | 2.12× lower at baseline in the lines without TRIM47 | 0.089 | ⚠ few lines (4 vs 46); across organs; also absent: PERP, SOX13, ABCA5 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.515). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (0.1, -22.8); signed map (12.1, -22.5). **Vector** length 56.4, 8.11% of its response variance represented; |z| ≥ 3 in 878 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.2 | +4.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | +4.1 | -3.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +5.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.9 | +1.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.8 | +2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +1.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +2.0 | +2.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +4.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.9 | +2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +1.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.7 | -6.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.6 | -6.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.1 | -13.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.1 | -7.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.8 | -11.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | -5.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | -5.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -0.8 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.2 | -2.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | shroom family member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.1 — chr5:132,822,141-132,830,659 (-) |
| Ensembl biotype | protein_coding |
| Also known as | APXL2, KIAA1960 |
| Gene groups (HGNC) | Shroom family |
| Hallmark sets | MITOTIC_SPINDLE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q2M3G4](https://www.uniprot.org/uniprotkb/Q2M3G4) (Protein Shroom1):

> May be involved in the assembly of microtubule arrays during cell elongation.

**Summary**, from NCBI Gene [134549](https://www.ncbi.nlm.nih.gov/gene/134549):

> SHROOM family members play diverse roles in the development of the nervous system and other tissues (Hagens et al., 2006 [PubMed 16615870]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:24084](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24084) · Entrez [134549](https://www.ncbi.nlm.nih.gov/gene/134549) · UniProt [Q2M3G4](https://www.uniprot.org/uniprotkb/Q2M3G4) · Ensembl [ENSG00000164403](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164403)

## Data

Gene col 8943: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8943); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8943, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8943]; `tensor/DDL_lfc|DDL_z.npy` [8943]; `embed/gene_vectors.npy` [8943]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8943 or target_col == 8943). Every well: [[SHROOM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SHROOM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
