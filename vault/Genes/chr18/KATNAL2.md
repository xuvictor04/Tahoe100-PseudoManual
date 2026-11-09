---
symbol: "KATNAL2"
type: "gene"
col: 9437
ensembl_id: "ENSG00000167216"
name: "katanin catalytic subunit A1 like 2"
location: "18q21.1"
module: 10
arm: "+"
pooled_cpm: 7.11
n_lines_expressing: 42
n_dd_up: 31
n_dd_down: 12
n_dd_up_clean: 27
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 27
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# KATNAL2

*katanin catalytic subunit A1 like 2* — 18q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.69× (z +10.0, q 7e-21, up in 14 of 26 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.89× (z +9.1, q 2e-17, up in 20 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.514× (z -6.8, q 7e-09, down in 23 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKS1B]] (+0.71, fdr 7e-06), [[ZMAT1]] (+0.70, fdr 7e-06), [[ANKRD31]] (+0.70, fdr 7e-06); moves opposite to [[FBH1]] (-0.52, fdr 3e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ABCA17P]] → it (grade B ⚠); 27 go from it, the strongest it → [[CCDC144CP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9437.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.69×** | +10.0 | 7e-21 | 14/26 (LoVo, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.89×** | +9.1 | 2e-17 | 20/35 (BT-474, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.33×** | +8.2 | 4e-14 | 6/11 (SHP-77, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.18×** | +7.3 | 5e-11 | 7/15 (RPMI-7951, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.65×** | +7.2 | 9e-11 | 20/36 (SHP-77, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.63×** | +6.9 | 4e-10 | 20/39 (A-172, BT-474, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.95×** | +6.7 | 1e-09 | 20/39 (A498, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.71×** | +5.4 | 5e-06 | 14/36 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.39×** | +4.7 | 2e-04 | 15/38 (A-427, NCI-H460, …) | top dose only | low cells (technical?) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.53×** | +4.3 | 0.001 | 13/35 (A498, PANC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.52×** | +4.2 | 0.001 | 16/38 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.55×** | +4.2 | 0.001 | 16/36 (PANC-1, LoVo, …) | rises with dose |  |
| [[Afatinib (drug)]] 5 µM |  | **1.53×** | +4.1 | 0.002 | 11/38 (HEC-1-A, J82, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.53×** | +4.1 | 0.002 | 15/37 (NCI-H23, C32, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +3.9 | 0.004 | 10/33 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.47×** | +3.9 | 0.004 | 9/38 (NCI-H460, C-33 A, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.43×** | +3.6 | 0.012 | 10/34 (SHP-77, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.42×** | +3.5 | 0.013 | 12/39 (MIA PaCa-2, KATO III, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.34×** | +3.5 | 0.016 | 14/37 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9437.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.514×** | -6.8 | 7e-09 | 23/38 (LoVo, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.544×** | -6.2 | 2e-07 | 21/39 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.581×** | -5.5 | 6e-06 | 19/36 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.607×** | -5.1 | 5e-05 | 18/38 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.398×** | -4.9 | 1e-04 | 17/33 (KATO III, C-33 A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.636×** | -4.6 | 4e-04 | 16/39 (AN3 CA, MIA PaCa-2, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.730×** | -4.6 | 4e-04 | 17/37 (MIA PaCa-2, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.701×** | -3.6 | 0.020 | 14/37 (PANC-1, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.710×** | -3.5 | 0.030 | 11/39 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.705×** | -3.4 | 0.034 | 18/30 (H4, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.536×** | -3.3 | 0.046 | 11/32 (HEC-1-A, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.726×** | -3.3 | 0.051 | 12/34 (MIA PaCa-2, NCI-H23, …) | rises with dose |  |
| [[Asciminib (drug)]] 0.05 µM |  | 0.743× | -3.0 | 0.10 | 12/38 (NCI-H2030, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.744× | -3.0 | 0.10 | 10/37 (PANC-1, KATO III, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9437. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 16.7 | 0 | 6 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.106× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.188× (z -11.2) |
| [[NCI-H23 (line)]] | alt | 13.6 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0345× (z -16.4) |
| [[MIA PaCa-2 (line)]] | alt | 23.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.148× (z -9.9) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 25.5 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.101× (z -9.6) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 3.91 | 0 | 1 | — | [[Trifluridine (drug)]] 0.05 µM 0.0629× (z -8.7) |
| [[KATO III (line)]] | alt | 11.7 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0347× (z -8.6) |
| [[LoVo (line)]] | wt | 5.96 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0917× (z -11.4) |
| [[SHP-77 (line)]] | alt | 29.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +8.9) | — |
| [[A-172 (line)]] | wt | 9.71 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.11 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.66 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.56 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.76 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.49 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 8.53 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.67 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9437), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKS1B]] | +0.71 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[ZMAT1]] | +0.70 | +0.76 / +0.61 | both halves | 7e-06 |  |
| [[ANKRD31]] | +0.70 | +0.75 / +0.61 | both halves | 7e-06 |  |
| [[FRG1-DT]] | +0.67 | +0.74 / +0.53 | both halves | 1e-05 |  |
| [[FAM66C]] | +0.67 | +0.73 / +0.50 | both halves | 1e-05 |  |
| [[ANKRD18CP]] | +0.66 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[EIF1B-AS1]] | +0.66 | +0.70 / +0.57 | both halves | 1e-05 |  |
| [[SYT9-AS1]] | +0.64 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[DPH6-DT]] | +0.64 | +0.74 / +0.57 | both halves | 1e-05 |  |
| [[CRB1]] | +0.63 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[LRRIQ3]] | +0.63 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[LINC00240]] | +0.63 | +0.66 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBH1]] | -0.52 | -0.46 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABCA17P]] | B | ABCA17P activity raises KATNAL2's level | lines that do not express ABCA17P (11) vs lines expressing it (39) | 2.41× lower at baseline in the lines without ABCA17P | 0.014 | ⚠ within organs, on part of the lines; also absent: NTN1, KIF26A, DOCK3; maybe low, not absent |
| [[CCDC144CP]] | B | CCDC144CP activity raises KATNAL2's level | lines that do not express CCDC144CP (7) vs lines expressing it (43) | 2.45× lower at baseline in the lines without CCDC144CP | 0.030 | ⚠ within organs, on part of the lines; also absent: SNX10, CPPED1, GPLD1 |

### Downstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 26, C 1. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC144CP]] | B | KATNAL2 activity raises CCDC144CP's level | lines that do not express KATNAL2 (8) vs lines expressing it (42) | 2.66× lower at baseline in the lines without KATNAL2 | 0.006 | ⚠ within organs, on part of the lines; also absent: LHFPL6, TTC7B, PRKAR2B; maybe low, not absent |
| [[CASC2]] | B | KATNAL2 activity raises CASC2's level | lines that do not express KATNAL2 (8) vs lines expressing it (42) | 1.77× lower at baseline in the lines without KATNAL2 | 0.008 | ⚠ within organs, on part of the lines; also absent: LHFPL6, TTC7B, PRKAR2B; maybe low, not absent |
| [[ATP6V1E2]] | B | KATNAL2 activity raises ATP6V1E2's level | lines that do not express KATNAL2 (8) vs lines expressing it (42) | 2.31× lower at baseline in the lines without KATNAL2 | 0.009 | ⚠ within organs, on part of the lines; also absent: LHFPL6, TTC7B, PRKAR2B; maybe low, not absent |
| [[PRDX6-AS1]] | B | KATNAL2 activity raises PRDX6-AS1's level | lines that do not express KATNAL2 (8) vs lines expressing it (42) | 1.77× lower at baseline in the lines without KATNAL2 | 0.010 | ⚠ within organs, on part of the lines; also absent: LHFPL6, TTC7B, PRKAR2B; maybe low, not absent |
| [[CCDC171]] | B | KATNAL2 activity raises CCDC171's level | lines that do not express KATNAL2 (8) vs lines expressing it (42) | 1.79× lower at baseline in the lines without KATNAL2 | 0.011 | ⚠ within organs, on part of the lines; also absent: LHFPL6, TTC7B, PRKAR2B; maybe low, not absent |
| [[F8]] | B | KATNAL2 activity raises F8's level | lines that do not express KATNAL2 (8) vs lines expressing it (42) | 1.80× lower at baseline in the lines without KATNAL2 | 0.019 | ⚠ within organs, on part of the lines; also absent: LHFPL6, TTC7B, PRKAR2B; maybe low, not absent |
| [[DPH6-DT]] | B | KATNAL2 activity raises DPH6-DT's level | lines that do not express KATNAL2 (8) vs lines expressing it (42) | 2.64× lower at baseline in the lines without KATNAL2 | 0.025 | ⚠ within organs, on part of the lines; also absent: LHFPL6, TTC7B, PRKAR2B; maybe low, not absent |
| [[DPY19L2P2-1]] | B | KATNAL2 activity raises DPY19L2P2-1's level | lines that do not express KATNAL2 (8) vs lines expressing it (42) | 2.36× lower at baseline in the lines without KATNAL2 | 0.028 | ⚠ within organs, on part of the lines; also absent: LHFPL6, TTC7B, PRKAR2B; maybe low, not absent |
| [[CYB5D2]] | B | KATNAL2 activity raises CYB5D2's level | lines that do not express KATNAL2 (8) vs lines expressing it (42) | 1.35× lower at baseline in the lines without KATNAL2 | 0.030 | ⚠ within organs, on part of the lines; also absent: LHFPL6, TTC7B, PRKAR2B; maybe low, not absent |
| [[CYP2U1]] | B | KATNAL2 activity raises CYP2U1's level | lines that do not express KATNAL2 (8) vs lines expressing it (42) | 1.92× lower at baseline in the lines without KATNAL2 | 0.034 | ⚠ within organs, on part of the lines; also absent: LHFPL6, TTC7B, PRKAR2B; maybe low, not absent |
| [[LINC01505]] | B | KATNAL2 activity raises LINC01505's level | lines that do not express KATNAL2 (8) vs lines expressing it (42) | 2.00× lower at baseline in the lines without KATNAL2 | 0.035 | ⚠ within organs, on part of the lines; also absent: LHFPL6, TTC7B, PRKAR2B; maybe low, not absent |
| [[EPM2A-DT]] | B | KATNAL2 activity raises EPM2A-DT's level | lines that do not express KATNAL2 (8) vs lines expressing it (42) | 1.45× lower at baseline in the lines without KATNAL2 | 0.043 | ⚠ within organs, on part of the lines; also absent: LHFPL6, TTC7B, PRKAR2B; maybe low, not absent |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.718). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (6.9, 30.5); signed map (34.6, -9.5). **Vector** length 62.5, 11.4% of its response variance represented; |z| ≥ 3 in 888 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.8 | +7.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +8.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +10.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.9 | +7.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.1 | +3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +6.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +3.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +2.5 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -2.6 | -3.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -2.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -0.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.8 | -6.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.7 | -4.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.5 | -4.6 |
|  | [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | -1.1 | -1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.1 | -3.3 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -1.0 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | katanin catalytic subunit A1 like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.1 — chr18:46,917,492-47,103,478 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC33211, DKFZP667C165 |
| Gene groups (HGNC) | AAA ATPases; Katanin catalytic subunit family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IYT4](https://www.uniprot.org/uniprotkb/Q8IYT4) (Katanin p60 ATPase-containing subunit A-like 2):

> Severs microtubules in vitro in an ATP-dependent manner. This activity may promote rapid reorganization of cellular microtubule arrays.

**Summary**, from NCBI Gene [83473](https://www.ncbi.nlm.nih.gov/gene/83473):

> Predicted to enable ATP hydrolysis activity. Predicted to be involved in meiotic spindle organization and microtubule severing. Located in cytoplasm and cytoskeleton. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25387](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25387) · Entrez [83473](https://www.ncbi.nlm.nih.gov/gene/83473) · UniProt [Q8IYT4](https://www.uniprot.org/uniprotkb/Q8IYT4) · Ensembl [ENSG00000167216](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167216)

## Data

Gene col 9437: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9437); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9437, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9437]; `tensor/DDL_lfc|DDL_z.npy` [9437]; `embed/gene_vectors.npy` [9437]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9437 or target_col == 9437). Every well: [[KATNAL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KATNAL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
