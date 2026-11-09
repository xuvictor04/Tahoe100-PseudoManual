---
symbol: "SLC6A16"
type: "gene"
col: 719
ensembl_id: "ENSG00000063127"
name: "solute carrier family 6 member 16"
location: "19q13.33"
module: 26
arm: "+"
pooled_cpm: 7.74
n_lines_expressing: 39
n_dd_up: 10
n_dd_down: 27
n_dd_up_clean: 7
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 5
direction_downstream: 4
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# SLC6A16

*solute carrier family 6 member 16* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.78× (z +9.3, q 5e-18, up in 24 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.293× (z -14.0, q 5e-42, down in 28 of 33 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TEAD2]] (+0.68, fdr 1e-05, ⚠ same locus), [[DPY19L2P3]] (+0.57, fdr 2e-05), [[DNMT3A]] (+0.57, fdr 3e-05), [[PIPOX]] (+0.55, fdr 1e-04); moves opposite to [[MRPS31P4]] (-0.57, fdr 3e-05), [[DBT]] (-0.56, fdr 2e-05), [[NUDT12]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[SIRPA]] → it (grade B ⚠); 4 go from it, the strongest it → cells under [[ERK5-IN-2 (drug)]] 0.5 µM (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 719.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +9.3 | 5e-18 | 24/33 (HS-578T, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.88×** | +7.0 | 7e-10 | 5/14 (A-172, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.81×** | +6.8 | 2e-09 | 9/24 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.62×** | +5.2 | 4e-05 | 6/18 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +4.2 | 0.003 | 4/37 (NCI-H23, NCI-H2030, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.45×** | +4.1 | 0.004 | 12/34 (NCI-H23, A549, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +3.9 | 0.008 | 10/32 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.26×** | +3.5 | 0.038 | 6/36 (NCI-H23, SW 1271, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.30×** | +3.4 | 0.038 | 12/35 (LOX-IMVI, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.061 | 11/37 (LOX-IMVI, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.083 | 8/35 (A549, A-427, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 719.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.293×** | -14.0 | 5e-42 | 28/33 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.473×** | -12.1 | 4e-31 | 26/33 (C32, BT-474, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.336×** | -12.0 | 8e-31 | 25/35 (C32, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.467×** | -8.7 | 5e-16 | 27/36 (SW480, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.502×** | -7.9 | 5e-13 | 25/36 (C-33 A, A498, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.290×** | -7.4 | 1e-11 | 20/35 (C32, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.529×** | -7.3 | 3e-11 | 21/36 (C-33 A, C32, …) | two highest doses | cell-cycle shift (explains ~23% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.311×** | -7.0 | 2e-10 | 21/32 (C32, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.560×** | -6.6 | 3e-09 | 19/36 (C-33 A, C32, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.588×** | -6.1 | 8e-08 | 21/35 (LOX-IMVI, C32, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.599×** | -5.8 | 3e-07 | 16/36 (C32, PANC-1, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **0.722×** | -5.2 | 8e-06 | 18/36 (C32, A-427, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.462×** | -4.6 | 2e-04 | 13/34 (A498, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.664×** | -4.4 | 4e-04 | 8/34 (PANC-1, A498, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.484×** | -4.3 | 6e-04 | 7/11 (C32, A-172, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.630×** | -3.7 | 0.006 | 7/36 (SK-MEL-2, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.719×** | -3.7 | 0.006 | 11/36 (NCI-H2030, SW 1271, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.539×** | -3.7 | 0.007 | 9/29 (C32, BT-474, …) | top dose only | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.710×** | -3.6 | 0.010 | 10/32 (A-172, SNU-423, …) | all doses, stronger at high dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 719. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 33.0 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -15.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.121× (z -14.3) |
| [[BT-474 (line)]] | alt | 15.5 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0861× (z -15.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.113× (z -9.7) |
| [[NCI-H460 (line)]] | wt | 8.98 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.138× (z -10.8) |
| [[LOX-IMVI (line)]] | wt | 15.3 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.152× (z -9.9) |
| [[SW480 (line)]] | alt | 9.48 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.118× (z -12.9) |
| [[C-33 A (line)]] | alt | 48.7 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.163× (z -11.6) |
| [[RKO (line)]] | wt | 15.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -13.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Glycyrrhizic acid (drug)]] 0.05 µM 0.123× (z -10.1) |
| [[A-172 (line)]] | wt | 11.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -11.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.149× (z -9.7) |
| [[A549 (line)]] | wt | 9.23 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0842× (z -10.3) |
| [[A-427 (line)]] | wt | 13.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -10.8) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A498 (line)]] | wt | 19.4 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.276× (z -8.9) |
| [[CHP-212 (line)]] | wt | 16.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0552× (z -11.5) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H2030 (line)]] | alt | 14.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.113× (z -10.7) |
| [[NCI-H23 (line)]] | alt | 8.78 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.1000× (z -9.4) |
| [[PANC-1 (line)]] | alt | 4.65 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0549× (z -15.0) |
| [[AN3 CA (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.827 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.798 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.54 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.28 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.72 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.732 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.826 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.933 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 719), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TEAD2]] | +0.68 | +0.70 / +0.55 | both halves | 1e-05 | ⚠ same locus (15.4 kb, same strand: neighbours can correlate without regulation) |
| [[DPY19L2P3]] | +0.57 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[DNMT3A]] | +0.57 | +0.43 / +0.56 | both halves | 3e-05 | same gene group |
| [[PIPOX]] | +0.55 | +0.36 / +0.60 | both halves | 1e-04 |  |
| [[PSMD6-AS2]] | +0.54 | +0.43 / +0.48 | both halves | 3e-05 |  |
| [[MYL6B-AS1]] | +0.53 | +0.37 / +0.48 | both halves | 8e-05 |  |
| [[SNHG14]] | +0.53 | +0.50 / +0.41 | both halves | 4e-05 |  |
| [[SIK3]] | +0.52 | +0.58 / +0.29 | both halves | 2e-04 |  |
| [[DPY19L1P1]] | +0.52 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[STARD4-AS1]] | +0.52 | +0.36 / +0.41 | both halves | 1e-04 |  |
| [[POU6F1]] | +0.51 | +0.40 / +0.52 | both halves | 4e-05 |  |
| [[CDK2AP1]] | +0.51 | +0.42 / +0.41 | both halves | 4e-05 |  |
| [[PRDM15]] | +0.51 | +0.50 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS31P4]] | -0.57 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[DBT]] | -0.56 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[NUDT12]] | -0.56 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[GEMIN2]] | -0.55 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[SUPT20H]] | -0.53 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[BLOC1S5]] | -0.53 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[ADH5]] | -0.51 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[RAD17]] | -0.51 | -0.50 / -0.30 | both halves | 2e-04 |  |
| [[STAM2]] | -0.50 | -0.52 / -0.26 | both halves | 4e-04 |  |
| [[FAM114A2]] | -0.49 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[ZNF184]] | -0.49 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[SKIC3]] | -0.49 | -0.42 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SIRPA]] | B | SIRPA activity raises SLC6A16's level | lines that do not express SIRPA (12) vs lines expressing it (38) | 2.62× lower at baseline in the lines without SIRPA | 0.019 | ⚠ within organs, on part of the lines; also absent: EID2B, LIX1L, FHL1 |
| [[MAP2K1]] | B | MAP2K1 activity lowers SLC6A16's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 1.7% of all compounds | 0.025 | ⚠ off-target possible; 3 compounds |
| [[TTC28]] | B | TTC28 activity raises SLC6A16's level | lines that do not express TTC28 (15) vs lines expressing it (35) | 2.39× lower at baseline in the lines without TTC28 | 0.037 | ⚠ within organs, on part of the lines; also absent: SAMD11, RASSF8-AS1, AOX1 |
| [[MAP2K2]] | B | MAP2K2 activity lowers SLC6A16's level | compounds that target MAP2K2: 2 of 2 raise it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; shared targets |
| [[TEAD2]] | C | TEAD2 activity raises SLC6A16's level | lines that do not express TEAD2 (9) vs lines expressing it (41) | 3.89× lower at baseline in the lines without TEAD2 | 0.006 | ⚠ within organs, on part of the lines; also absent: ENSG00000197813, SLC6A16, FBXO17; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | B | SLC6A16 activity lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | lines that do not express SLC6A16 (11) vs lines expressing it (37) | the lines without SLC6A16: 1.16× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: ENSG00000197813, TEAD2, ZNF71; maybe low, not absent |
| [[GATD1-DT]] | B | SLC6A16 activity raises GATD1-DT's level | lines that do not express SLC6A16 (11) vs lines expressing it (39) | 1.21× lower at baseline in the lines without SLC6A16 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000197813, TEAD2, ZNF71; maybe low, not absent |
| cells under [[Tetracycline (hydrochloride) (drug)]] 0.5 µM | B | SLC6A16 activity raises the cells' numbers under Tetracycline (hydrochloride) 0.5 µM (protects the cells) | lines that do not express SLC6A16 (11) vs lines expressing it (37) | the lines without SLC6A16: 0.92× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: ENSG00000197813, TEAD2, ZNF71; maybe low, not absent |
| [[TEAD2]] | C | SLC6A16 activity raises TEAD2's level | lines that do not express SLC6A16 (11) vs lines expressing it (39) | 3.65× lower at baseline in the lines without SLC6A16 | 0.001 | ⚠ within organs, on part of the lines; also absent: ENSG00000197813, TEAD2, ZNF71; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.378). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-6.7, 12.5); signed map (9.7, -5.0). **Vector** length 74.0, 15.8% of its response variance represented; |z| ≥ 3 in 847 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +9.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.7 | +3.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | -0.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +2.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +2.3 | -0.7 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.7 | +1.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.5 | +4.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.3 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +2.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.2 | -8.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.0 | -12.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.0 | -14.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -6.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.5 | -7.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.2 | -3.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.8 | -3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.7 | +0.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 6 member 16 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:49,289,638-49,325,215 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NTT5 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Solute carrier family 6 |
| Matched by | ensembl_id |

UniProt [Q9GZN6](https://www.uniprot.org/uniprotkb/Q9GZN6) carries no function annotation.

**Summary**, from NCBI Gene [28968](https://www.ncbi.nlm.nih.gov/gene/28968):

> SLC6A16 shows structural characteristics of an Na(+)- and Cl(-)-dependent neurotransmitter transporter, including 12 transmembrane (TM) domains, intracellular N and C termini, and large extracellular loops containing multiple N-glycosylation sites.[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:13622](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13622) · Entrez [28968](https://www.ncbi.nlm.nih.gov/gene/28968) · UniProt [Q9GZN6](https://www.uniprot.org/uniprotkb/Q9GZN6) · Ensembl [ENSG00000063127](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000063127)

## Data

Gene col 719: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 719); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 719, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 719]; `tensor/DDL_lfc|DDL_z.npy` [719]; `embed/gene_vectors.npy` [719]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 719 or target_col == 719). Every well: [[SLC6A16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC6A16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
