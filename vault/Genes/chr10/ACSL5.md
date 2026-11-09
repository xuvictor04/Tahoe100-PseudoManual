---
symbol: "ACSL5"
type: "gene"
col: 12353
ensembl_id: "ENSG00000197142"
name: "acyl-CoA synthetase long chain family member 5"
location: "10q25.2"
module: 73
arm: "+"
pooled_cpm: 34.16
n_lines_expressing: 26
n_dd_up: 32
n_dd_down: 21
n_dd_up_clean: 20
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 77
direction_downstream: 58
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# ACSL5

*acyl-CoA synthetase long chain family member 5* — 10q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.64× (z +15.6, q 0e+00, up in 15 of 21 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.91× (z +10.4, q 6e-23, up in 9 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.420× (z -13.9, q 4e-41, down in 19 of 24 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INPP5D]] (+0.74, fdr 7e-06), [[EPS8L3]] (+0.70, fdr 7e-06), [[KIAA0040]] (+0.69, fdr 7e-06); moves opposite to [[HOXA9]] (-0.58, fdr 3e-05).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 77 arrows point to it, the strongest [[ABCC3]] → it (grade B ⚠); 58 go from it, the strongest it → [[FUT8]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12353.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.64×** | +15.6 | 0e+00 | 15/21 (NCI-H2347, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.73×** | +15.5 | 0e+00 | 12/19 (KATO III, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.24×** | +11.9 | 1e-30 | 14/20 (NCI-H2347, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.91×** | +10.4 | 6e-23 | 9/23 (SNU-423, KATO III, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +7.9 | 5e-13 | 7/24 (SNU-423, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.48×** | +6.3 | 3e-08 | 7/24 (SNU-423, SW 900, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.48×** | +6.3 | 3e-08 | 13/24 (SW 900, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.31×** | +6.2 | 5e-08 | 9/24 (SW480, AsPC-1, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.41×** | +5.5 | 3e-06 | 8/24 (SW480, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Rosiglitazone (drug)]] 5 µM |  | **1.39×** | +5.1 | 2e-05 | 9/23 (LoVo, LS 180, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.34×** | +4.7 | 2e-04 | 7/23 (SNU-423, SW 900, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.32×** | +4.5 | 3e-04 | 8/23 (HepG2/C3A, SNU-423, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.29×** | +4.1 | 0.002 | 3/24 (SNU-423, AsPC-1, …) | all doses, flat |  |
| [[Bexarotene (drug)]] 5 µM |  | **1.28×** | +3.9 | 0.004 | 12/24 (LS 180, KATO III, …) | rises with dose |  |
| [[Pioglitazone (drug)]] 5 µM |  | **1.27×** | +3.9 | 0.004 | 13/24 (LoVo, LS 180, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.27×** | +3.9 | 0.004 | 6/24 (SW480, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mifepristone (drug)]] 0.5 µM |  | **1.23×** | +3.4 | 0.022 | 8/24 (KATO III, LS 180, …) | rises with dose |  |
| [[Rosiglitazone (drug)]] 0.05 µM |  | **1.24×** | +3.1 | 0.041 | 7/23 (LoVo, COLO 205, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.041 | 8/23 (LoVo, NCI-H1792, …) | top dose only |  |
| [[Pioglitazone (drug)]] 0.5 µM |  | **1.21×** | +3.1 | 0.041 | 7/23 (LoVo, LS 180, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 1 with an alert ⚠; shown: the 15 strongest. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12353.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.420×** | -13.9 | 4e-41 | 19/24 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.494×** | -11.3 | 4e-27 | 22/24 (LS 180, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.505×** | -10.9 | 1e-25 | 21/23 (LS 180, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.615×** | -7.8 | 1e-12 | 17/24 (COLO 205, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.642×** | -7.1 | 2e-10 | 15/23 (RKO, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.466×** | -6.4 | 1e-08 | 16/24 (HT-29, HepG2/C3A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.674×** | -6.4 | 1e-08 | 13/24 (HepG2/C3A, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.720×** | -4.8 | 9e-05 | 7/24 (HepG2/C3A, CFPAC-1, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.765×** | -4.8 | 9e-05 | 13/24 (HepG2/C3A, SW48, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.767×** | -4.2 | 0.001 | 7/23 (HepG2/C3A, CFPAC-1, …) | two highest doses |  |
| [[Radotinib (drug)]] 5 µM |  | **0.833×** | -4.1 | 0.002 | 9/24 (RKO, HT-29, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.765×** | -4.1 | 0.002 | 12/23 (HepG2/C3A, CFPAC-1, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.781×** | -3.9 | 0.004 | 11/24 (HepG2/C3A, CFPAC-1, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.820×** | -3.9 | 0.004 | 15/24 (HepG2/C3A, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[RMC-6236 (drug)]] 5 µM |  | **0.641×** | -3.7 | 0.008 | 3/24 (HepG2/C3A, CFPAC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12353. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 271 | 2 (2 ⚠) | 12 | [[Digitoxin (drug)]] 0.5 µM 3.15× (z +9.0) ⚠ cell-cycle shift, explains ~62% of this change | [[Panobinostat (drug)]] 5 µM 0.193× (z -13.0) |
| [[LS 180 (line)]] | wt | 173 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -27.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0817× (z -24.8) |
| [[SW48 (line)]] | wt | 65.8 | 0 | 10 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0654× (z -15.8) |
| [[COLO 205 (line)]] | alt | 214 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -21.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0768× (z -17.6) |
| [[HT-29 (line)]] | alt | 119 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.160× (z -13.9) |
| [[SNU-423 (line)]] | alt | 23.1 | 4 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.5 µM 5.60× (z +11.6) | [[Panobinostat (drug)]] 5 µM 0.267× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 159 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.134× (z -17.5) |
| [[LoVo (line)]] | wt | 50.7 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.143× (z -16.8) |
| [[SW1417 (line)]] | alt | 93.6 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.176× (z -16.7) |
| [[AsPC-1 (line)]] | alt | 118 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.115× (z -16.1) |
| [[KATO III (line)]] | alt | 137 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -23.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.450× (z -9.9) |
| [[NCI-H1792 (line)]] | alt | 24.6 | 0 | 3 (1 ⚠) | — | [[Capmatinib (drug)]] 5 µM 0.0468× (z -9.6) |
| [[RKO (line)]] | wt | 13.9 | 0 | 3 | — | [[Belinostat (drug)]] 0.5 µM 0.0533× (z -13.2) |
| [[SW480 (line)]] | alt | 15.1 | 2 | 0 | [[Amsacrine (drug)]] 5 µM 2.75× (z +10.1) | — |
| [[HCT15 (line)]] | alt | 26.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -9.7) ⚠ cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 9.87 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0694× (z -11.3) |
| [[A-172 (line)]] | wt | 4.49 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.53 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.49 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.27 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.30 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.81 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.18 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.98 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.48 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.46 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.97 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.41 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.18 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.40 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.24 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.62 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.64 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.60 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.67 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.26 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.38 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.30 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.05 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.35 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 21.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12353), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INPP5D]] | +0.74 | +0.64 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[EPS8L3]] | +0.70 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[KIAA0040]] | +0.69 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[B3GNT3]] | +0.69 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[LINC02474]] | +0.68 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[NPSR1]] | +0.68 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[CAPN8]] | +0.67 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[KLK10]] | +0.67 | +0.76 / +0.63 | both halves | 7e-06 |  |
| [[CALB1]] | +0.67 | +0.66 / +0.57 | both halves | 9e-06 |  |
| [[MUC17]] | +0.67 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[FERMT1]] | +0.67 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[ITGB4]] | +0.67 | +0.64 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOXA9]] | -0.58 | -0.64 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*77 arrows, 77 of them with an alert ⚠; grade A 0, B 10, C 67. Shown: the 12 strongest; 65 more arrows (65 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABCC3]] | B | ABCC3 activity raises ACSL5's level | lines that do not express ABCC3 (16) vs lines expressing it (34) | 3.76× lower at baseline in the lines without ABCC3 | 0.009 | ⚠ within organs, on part of the lines; also absent: AQP3, CDC42BPG, NUP62CL |
| [[LINC02320]] | B | LINC02320 activity raises ACSL5's level | lines that do not express LINC02320 (19) vs lines expressing it (31) | 3.98× lower at baseline in the lines without LINC02320 | 0.022 | ⚠ within organs, on part of the lines; also absent: ENSG00000258919, TSPAN1, ENSG00000266088 |
| [[DSC2]] | B | DSC2 activity raises ACSL5's level | lines that do not express DSC2 (22) vs lines expressing it (28) | 3.17× lower at baseline in the lines without DSC2 | 0.044 | ⚠ within organs, on part of the lines; also absent: FAM110C, SPINT1-AS1, PRR15-DT |
| [[TJP2]] | B | TJP2 activity raises ACSL5's level | lines that do not express TJP2 (10) vs lines expressing it (40) | 3.35× lower at baseline in the lines without TJP2 | 0.050 | ⚠ within organs, on part of the lines; also absent: PYROXD2, NRIP1, ENSG00000235609; maybe low, not absent |
| [[STEAP1]] | B | STEAP1 activity raises ACSL5's level | lines that do not express STEAP1 (11) vs lines expressing it (39) | 3.75× lower at baseline in the lines without STEAP1 | 0.060 | ⚠ within organs, on part of the lines; also absent: STEAP2-AS1, STEAP2 |
| [[MAP2K1]] | B | MAP2K1 activity raises ACSL5's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.4% of all compounds | 0.067 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[INPP1]] | B | INPP1 activity raises ACSL5's level | lines that do not express INPP1 (12) vs lines expressing it (38) | 3.95× lower at baseline in the lines without INPP1 | 0.069 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[HTR1D]] | B | HTR1D activity raises ACSL5's level | lines that do not express HTR1D (15) vs lines expressing it (35) | 2.38× lower at baseline in the lines without HTR1D | 0.070 | ⚠ within organs, on part of the lines; also absent: A4GALT, ZNF185, PAPSS2; maybe low, not absent |
| [[MET]] | B | MET activity raises ACSL5's level | lines that do not express MET (9) vs lines expressing it (41) | 4.52× lower at baseline in the lines without MET | 0.092 | ⚠ within organs, on part of the lines; also absent: TGFBR2, PHLDA2, VDR |
| [[CYP3A5]] | B | CYP3A5 activity weakens ACSL5's drug response | lines that do not express CYP3A5 (13) vs lines expressing it (11) | the lines without CYP3A5 respond 1.16× as strongly (z diff -0.60); strongest at Idarubicin (hydrochloride) 5 µM: 1.29x vs 0.42x (z diff -10.0) | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HHLA2, GCNT3, HNF4A; target measured in part of the lines; both ways; artifact flags |
| [[HS3ST1]] | C | HS3ST1 activity raises ACSL5's level | lines that do not express HS3ST1 (31) vs lines expressing it (19) | 5.70× lower at baseline in the lines without HS3ST1 | 0.001 | ⚠ within organs, on part of the lines; also absent: KLK10, ADGRF1, TMPRSS4; co-absent with the target |
| [[PKP1]] | C | PKP1 activity raises ACSL5's level | lines that do not express PKP1 (33) vs lines expressing it (17) | 4.21× lower at baseline in the lines without PKP1 | 0.001 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TFF2, CLIC5; co-absent with the target |

### Downstream of this gene

*58 arrows, 58 of them with an alert ⚠; grade A 0, B 13, C 45. Shown: the 12 strongest; 46 more arrows (46 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FUT8]] | B | ACSL5 activity raises FUT8's level | lines that do not express ACSL5 (24) vs lines expressing it (26) | 1.50× lower at baseline in the lines without ACSL5 | 0.016 | ⚠ within organs, on part of the lines; also absent: TNFRSF14-AS1, IL20RA, TINAGL1 |
| [[SOX12]] | B | ACSL5 activity lowers SOX12's level | lines that do not express ACSL5 (24) vs lines expressing it (26) | 1.54× higher at baseline in the lines without ACSL5 | 0.027 | ⚠ within organs, on part of the lines; also absent: TNFRSF14-AS1, IL20RA, TINAGL1 |
| [[MET]] | B | ACSL5 activity raises MET's level | lines that do not express ACSL5 (24) vs lines expressing it (26) | 2.51× lower at baseline in the lines without ACSL5 | 0.045 | ⚠ within organs, on part of the lines; also absent: TNFRSF14-AS1, IL20RA, TINAGL1 |
| [[TJP2]] | B | ACSL5 activity raises TJP2's level | lines that do not express ACSL5 (24) vs lines expressing it (26) | 2.55× lower at baseline in the lines without ACSL5 | 0.047 | ⚠ within organs, on part of the lines; also absent: TNFRSF14-AS1, IL20RA, TINAGL1 |
| [[EPS8L1]] | B | ACSL5 activity raises EPS8L1's level | lines that do not express ACSL5 (24) vs lines expressing it (26) | 2.25× lower at baseline in the lines without ACSL5 | 0.054 | ⚠ within organs, on part of the lines; also absent: TNFRSF14-AS1, IL20RA, TINAGL1 |
| [[VSIG1]] | B | ACSL5 activity raises VSIG1's level | lines that do not express ACSL5 (24) vs lines expressing it (26) | 1.38× lower at baseline in the lines without ACSL5 | 0.062 | ⚠ within organs, on part of the lines; also absent: TNFRSF14-AS1, IL20RA, TINAGL1 |
| [[GALNT4]] | B | ACSL5 activity raises GALNT4's level | lines that do not express ACSL5 (24) vs lines expressing it (26) | 1.50× lower at baseline in the lines without ACSL5 | 0.063 | ⚠ within organs, on part of the lines; also absent: TNFRSF14-AS1, IL20RA, TINAGL1 |
| [[STEAP1]] | B | ACSL5 activity raises STEAP1's level | lines that do not express ACSL5 (24) vs lines expressing it (26) | 2.23× lower at baseline in the lines without ACSL5 | 0.081 | ⚠ within organs, on part of the lines; also absent: TNFRSF14-AS1, IL20RA, TINAGL1 |
| [[ABCC3]] | B | ACSL5 activity raises ABCC3's level | lines that do not express ACSL5 (24) vs lines expressing it (26) | 2.24× lower at baseline in the lines without ACSL5 | 0.083 | ⚠ within organs, on part of the lines; also absent: TNFRSF14-AS1, IL20RA, TINAGL1 |
| [[DSC2]] | B | ACSL5 activity raises DSC2's level | lines that do not express ACSL5 (24) vs lines expressing it (26) | 2.94× lower at baseline in the lines without ACSL5 | 0.087 | ⚠ within organs, on part of the lines; also absent: TNFRSF14-AS1, IL20RA, TINAGL1 |
| [[VPS37B]] | B | ACSL5 activity raises VPS37B's level | lines that do not express ACSL5 (24) vs lines expressing it (26) | 1.42× lower at baseline in the lines without ACSL5 | 0.089 | ⚠ within organs, on part of the lines; also absent: TNFRSF14-AS1, IL20RA, TINAGL1 |
| [[SH2D4A]] | B | ACSL5 activity raises SH2D4A's level | lines that do not express ACSL5 (24) vs lines expressing it (26) | 2.34× lower at baseline in the lines without ACSL5 | 0.089 | ⚠ within organs, on part of the lines; also absent: TNFRSF14-AS1, IL20RA, TINAGL1 |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.768). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (16.4, 50.3); signed map (65.7, 9.5). **Vector** length 86.5, 25.0% of its response variance represented; |z| ≥ 3 in 765 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.5 | +15.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.9 | +15.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.3 | +11.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.5 | +6.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +7.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +10.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +4.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.4 | +3.1 |
| fall | [[Trametinib (drug)]] 5 µM |  | -2.7 | -6.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.4 | -4.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.0 | -3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.0 | -3.9 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.8 | -3.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.8 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | acyl-CoA synthetase long chain family member 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q25.2 — chr10:112,374,116-112,428,379 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ACS5, ACS2; previously FACL5 |
| Gene groups (HGNC) | Acyl-CoA synthetase family |
| Hallmark sets | BILE_ACID_METABOLISM, PEROXISOME, FATTY_ACID_METABOLISM |
| Reactome | 4 pathways, smallest: Synthesis of very long-chain fatty acyl-CoAs; Fatty acyl-CoA biosynthesis; Fatty acid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULC5](https://www.uniprot.org/uniprotkb/Q9ULC5) (Long-chain-fatty-acid--CoA ligase 5):

> Catalyzes the conversion of long- and medium-chain fatty acids to their active form fatty acyl-CoA. May drive cellular fatty acid uptake by metabolic trapping, and regulate the channeling of fatty acids towards specific metabolic pathways such as the generation of energy by beta-oxidation or the synthesis of membrane lipids. May activate fatty acids from exogenous sources for the synthesis of triacylglycerol destined for intracellular storage (By similarity). Utilizes a wide range of saturated …

**Summary**, from NCBI Gene [51703](https://www.ncbi.nlm.nih.gov/gene/51703):

> The protein encoded by this gene is an isozyme of the long-chain fatty-acid-coenzyme A ligase family. Although differing in substrate specificity, subcellular localization, and tissue distribution, all isozymes of this family convert free long-chain fatty acids into fatty acyl-CoA esters, and thereby play a key role in lipid biosynthesis and fatty acid degradation. This isozyme is highly expressed in uterus and spleen, and in trace amounts in normal brain, but has markedly increased levels in …

**Accessions** — [HGNC:16526](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16526) · Entrez [51703](https://www.ncbi.nlm.nih.gov/gene/51703) · UniProt [Q9ULC5](https://www.uniprot.org/uniprotkb/Q9ULC5) · Ensembl [ENSG00000197142](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197142)

## Data

Gene col 12353: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12353); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12353, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12353]; `tensor/DDL_lfc|DDL_z.npy` [12353]; `embed/gene_vectors.npy` [12353]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12353 or target_col == 12353). Every well: [[ACSL5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACSL5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
