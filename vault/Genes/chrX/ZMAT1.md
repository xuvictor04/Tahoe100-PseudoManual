---
symbol: "ZMAT1"
type: "gene"
col: 9302
ensembl_id: "ENSG00000166432"
name: "zinc finger matrin-type 1"
location: "Xq22.1"
module: 10
arm: "+"
pooled_cpm: 8.46
n_lines_expressing: 32
n_dd_up: 16
n_dd_down: 16
n_dd_up_clean: 13
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 7
direction_downstream: 13
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# ZMAT1

*zinc finger matrin-type 1* — Xq22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.84× (z +9.3, q 1e-17, up in 6 of 14 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.68× (z +6.7, q 3e-09, up in 16 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.388× (z -8.7, q 2e-15, down in 23 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KATNAL2]] (+0.70, fdr 7e-06), [[FAM227B]] (+0.70, fdr 7e-06), [[FTCDNL1]] (+0.66, fdr 1e-05); moves opposite to [[GPR89A]] (-0.56, fdr 3e-05), [[TUSC2]] (-0.54, fdr 8e-05), [[ZCCHC17]] (-0.53, fdr 1e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[ANKRD20A11P]] → it (grade B ⚠); 13 go from it, the strongest it → [[ZNF839]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9302.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.84×** | +9.3 | 1e-17 | 6/14 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.57×** | +8.7 | 8e-16 | 11/19 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.68×** | +6.7 | 3e-09 | 16/29 (A498, NCI-H2347, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.91×** | +5.5 | 5e-06 | 7/15 (NCI-H2030, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.75×** | +5.2 | 3e-05 | 12/25 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.40×** | +4.4 | 1e-03 | 10/28 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.59×** | +4.3 | 0.002 | 13/29 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +3.8 | 0.010 | 11/23 (A498, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.47×** | +3.4 | 0.037 | 9/29 (A-427, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.44×** | +3.4 | 0.038 | 9/29 (A-427, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.44×** | +3.4 | 0.039 | 6/30 (HEC-1-A, NCI-H1573, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.34×** | +3.3 | 0.046 | 9/29 (SK-MEL-2, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 0.5 µM |  | **1.43×** | +3.3 | 0.046 | 6/29 (HOP62, C-33 A, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.42×** | +3.2 | 0.053 | 9/29 (NCI-H23, C-33 A, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.61×** | +3.1 | 0.062 | 1/25 (HOP62) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 5 µM |  | **1.26×** | +3.0 | 0.100 | 3/30 (H4, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9302.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.388×** | -8.7 | 2e-15 | 23/30 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.393×** | -8.6 | 2e-15 | 22/30 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.445×** | -7.5 | 1e-11 | 19/25 (NCI-H23, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.445×** | -7.5 | 1e-11 | 21/29 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.411×** | -7.3 | 3e-11 | 18/29 (PANC-1, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.497×** | -6.4 | 1e-08 | 17/30 (PANC-1, H4, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.528×** | -5.6 | 2e-06 | 13/27 (PANC-1, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.521×** | -5.3 | 6e-06 | 16/30 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.605×** | -4.6 | 2e-04 | 15/30 (NCI-H23, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.632×** | -4.2 | 0.001 | 15/28 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.462×** | -3.7 | 0.010 | 10/28 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.693×** | -3.4 | 0.036 | 11/30 (LOX-IMVI, J82, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.510×** | -3.2 | 0.052 | 13/30 (LOX-IMVI, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.513×** | -3.2 | 0.053 | 13/25 (NCI-H1573, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ranolazine (drug)]] 0.5 µM |  | **0.718×** | -3.0 | 0.083 | 8/28 (RKO, NCI-H2030, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.629×** | -3.0 | 0.083 | 11/30 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9302. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 33.3 | 0 | 12 (4 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0782× (z -20.0) |
| [[NCI-H23 (line)]] | alt | 32.3 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0754× (z -14.4) |
| [[SK-MEL-2 (line)]] | alt | 49.0 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.139× (z -13.0) |
| [[A-427 (line)]] | wt | 15.0 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0996× (z -11.6) |
| [[H4 (line)]] | wt | 21.0 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0333× (z -13.7) |
| [[HEC-1-A (line)]] | alt | 24.4 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.232× (z -10.5) |
| [[LOX-IMVI (line)]] | wt | 16.7 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0790× (z -13.4) |
| [[HOP62 (line)]] | alt | 11.5 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.215× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 6.01 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0512× (z -11.1) |
| [[NCI-H2030 (line)]] | alt | 8.35 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.80× (z +9.2) | — |
| [[SW480 (line)]] | alt | 2.50 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.53× (z +8.7) | — |
| [[A-172 (line)]] | wt | 3.95 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.76 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.894 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.881 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.987 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.39 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.703 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.683 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.953 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.44 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.809 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.95 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9302), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KATNAL2]] | +0.70 | +0.76 / +0.61 | both halves | 7e-06 |  |
| [[FAM227B]] | +0.70 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[FTCDNL1]] | +0.66 | +0.74 / +0.51 | both halves | 1e-05 |  |
| [[F8]] | +0.66 | +0.77 / +0.53 | both halves | 1e-05 |  |
| [[KLHDC1]] | +0.66 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[TMEM9B-AS1]] | +0.66 | +0.77 / +0.48 | both halves | 2e-05 |  |
| [[RNF32]] | +0.66 | +0.76 / +0.51 | both halves | 1e-05 |  |
| [[ANKRD31]] | +0.65 | +0.75 / +0.53 | both halves | 1e-05 |  |
| [[CUTALP]] | +0.65 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[APLF]] | +0.64 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[LINC02175]] | +0.63 | +0.74 / +0.46 | both halves | 3e-05 |  |
| [[FRG1-DT]] | +0.63 | +0.73 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPR89A]] | -0.56 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[TUSC2]] | -0.54 | -0.54 / -0.37 | both halves | 8e-05 |  |
| [[ZCCHC17]] | -0.53 | -0.55 / -0.35 | both halves | 1e-04 |  |
| [[SHQ1]] | -0.52 | -0.53 / -0.36 | both halves | 9e-05 |  |
| [[SNHG30]] | -0.51 | -0.47 / -0.51 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 3, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANKRD20A11P]] | B | ANKRD20A11P activity raises ZMAT1's level | lines that do not express ANKRD20A11P (29) vs lines expressing it (21) | 2.26× lower at baseline in the lines without ANKRD20A11P | 0.044 | ⚠ within organs, on part of the lines; also absent: KCNQ2, RBM11, ANKRD20A21P |
| [[AGA-DT]] | B | AGA-DT activity raises ZMAT1's level | lines that do not express AGA-DT (6) vs lines expressing it (44) | 2.91× lower at baseline in the lines without AGA-DT | 0.067 | ⚠ within organs, on part of the lines; also absent: RUNDC3A-AS1, UTRN, TMEM144; maybe low, not absent |
| [[MIR1915HG]] | B | MIR1915HG activity raises ZMAT1's level | lines that do not express MIR1915HG (13) vs lines expressing it (37) | 2.03× lower at baseline in the lines without MIR1915HG | 0.093 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, NT5M, SOCS2; maybe low, not absent |
| [[ANKRD20A21P]] | C | ANKRD20A21P activity raises ZMAT1's level | lines that do not express ANKRD20A21P (30) vs lines expressing it (20) | 2.69× lower at baseline in the lines without ANKRD20A21P | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000229618, PAX2, ANKRD20A11P; co-absent with the target |
| [[FAM66C]] | C | FAM66C activity raises ZMAT1's level | lines that do not express FAM66C (15) vs lines expressing it (35) | 2.73× lower at baseline in the lines without FAM66C | 0.017 | ⚠ within organs, on part of the lines; also absent: MED12L, LONRF2, LMX1B; maybe low, not absent; co-absent with the target |
| [[ANKS1B]] | C | ANKS1B activity raises ZMAT1's level | lines that do not express ANKS1B (18) vs lines expressing it (32) | 2.57× lower at baseline in the lines without ANKS1B | 0.054 | ⚠ within organs, on part of the lines; also absent: LHX2, CECR2, HS6ST3; co-absent with the target |
| [[LINC00466]] | C | LINC00466 activity raises ZMAT1's level | lines that do not express LINC00466 (15) vs lines expressing it (35) | 2.63× lower at baseline in the lines without LINC00466 | 0.057 | ⚠ within organs, on part of the lines; also absent: FAM124A, NTN1, SSPOP; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 11, C 2. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF839]] | B | ZMAT1 activity raises ZNF839's level | lines that do not express ZMAT1 (18) vs lines expressing it (32) | 1.63× lower at baseline in the lines without ZMAT1 | 0.013 | ⚠ within organs, on part of the lines; also absent: NTN1, C19orf81, LMX1B |
| [[HNRNPH3]] | B | ZMAT1 activity raises HNRNPH3's level | lines that do not express ZMAT1 (18) vs lines expressing it (32) | 1.29× lower at baseline in the lines without ZMAT1 | 0.014 | ⚠ within organs, on part of the lines; also absent: NTN1, C19orf81, LMX1B |
| [[MYL5]] | B | ZMAT1 activity raises MYL5's level | lines that do not express ZMAT1 (18) vs lines expressing it (32) | 1.29× lower at baseline in the lines without ZMAT1 | 0.030 | ⚠ within organs, on part of the lines; also absent: NTN1, C19orf81, LMX1B |
| [[HHAT]] | B | ZMAT1 activity raises HHAT's level | lines that do not express ZMAT1 (18) vs lines expressing it (32) | 1.90× lower at baseline in the lines without ZMAT1 | 0.031 | ⚠ within organs, on part of the lines; also absent: NTN1, C19orf81, LMX1B |
| [[SYT9-AS1]] | B | ZMAT1 activity raises SYT9-AS1's level | lines that do not express ZMAT1 (18) vs lines expressing it (32) | 1.38× lower at baseline in the lines without ZMAT1 | 0.044 | ⚠ within organs, on part of the lines; also absent: NTN1, C19orf81, LMX1B |
| [[FTCDNL1]] | B | ZMAT1 activity raises FTCDNL1's level | lines that do not express ZMAT1 (18) vs lines expressing it (32) | 2.16× lower at baseline in the lines without ZMAT1 | 0.056 | ⚠ within organs, on part of the lines; also absent: NTN1, C19orf81, LMX1B |
| [[CEP112]] | B | ZMAT1 activity raises CEP112's level | lines that do not express ZMAT1 (18) vs lines expressing it (32) | 1.73× lower at baseline in the lines without ZMAT1 | 0.058 | ⚠ within organs, on part of the lines; also absent: NTN1, C19orf81, LMX1B |
| [[F8]] | B | ZMAT1 activity raises F8's level | lines that do not express ZMAT1 (18) vs lines expressing it (32) | 1.67× lower at baseline in the lines without ZMAT1 | 0.059 | ⚠ within organs, on part of the lines; also absent: NTN1, C19orf81, LMX1B |
| [[LINC02934]] | B | ZMAT1 activity lowers LINC02934's level | lines that do not express ZMAT1 (18) vs lines expressing it (32) | 1.55× higher at baseline in the lines without ZMAT1 | 0.089 | ⚠ within organs, on part of the lines; also absent: NTN1, C19orf81, LMX1B |
| [[APLF]] | B | ZMAT1 activity raises APLF's level | lines that do not express ZMAT1 (18) vs lines expressing it (32) | 1.46× lower at baseline in the lines without ZMAT1 | 0.097 | ⚠ within organs, on part of the lines; also absent: NTN1, C19orf81, LMX1B |
| [[MYO15B]] | B | ZMAT1 activity strengthens MYO15B's drug response | lines that do not express ZMAT1 (16) vs lines expressing it (27) | the lines without ZMAT1 respond 0.57× as strongly (z diff +1.79); strongest at Harringtonine 5 µM: 1.40x vs 0.41x (z diff +6.5) | 0.099 | ⚠ within organs, on part of the lines; also absent: NTN1, C19orf81, LMX1B; target measured in part of the lines; artifact flags |
| [[FAM66C]] | C | ZMAT1 activity raises FAM66C's level | lines that do not express ZMAT1 (18) vs lines expressing it (32) | 1.88× lower at baseline in the lines without ZMAT1 | 0.015 | ⚠ within organs, on part of the lines; also absent: NTN1, C19orf81, LMX1B; co-absent with the target |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.706). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (6.6, 29.8); signed map (34.7, -9.5). **Vector** length 69.0, 16.4% of its response variance represented; |z| ≥ 3 in 735 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.2 | +4.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +8.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +9.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.4 | +5.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +6.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +3.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.5 | +1.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +3.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.4 | +3.1 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -4.1 | -8.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.4 | -5.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.0 | -4.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.0 | -6.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -1.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -4.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.8 | -3.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.8 | -3.7 |
|  | [[EX229 (drug)]] 5 µM |  | -1.7 | -2.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.4 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger matrin-type 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq22.1 — chrX:101,882,288-101,932,031 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1789 |
| Gene groups (HGNC) | Zinc fingers matrin-type |
| Matched by | ensembl_id |

UniProt [Q5H9K5](https://www.uniprot.org/uniprotkb/Q5H9K5) carries no function annotation.

**Summary**, from NCBI Gene [84460](https://www.ncbi.nlm.nih.gov/gene/84460):

> This gene encodes a protein containing Cys2-His2 (C2H2)-type zinc fingers, which are similar to those found in the nuclear matrix protein matrin 3. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Jan 2012]

**Accessions** — [HGNC:29377](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29377) · Entrez [84460](https://www.ncbi.nlm.nih.gov/gene/84460) · UniProt [Q5H9K5](https://www.uniprot.org/uniprotkb/Q5H9K5) · Ensembl [ENSG00000166432](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166432)

## Data

Gene col 9302: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9302); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9302, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9302]; `tensor/DDL_lfc|DDL_z.npy` [9302]; `embed/gene_vectors.npy` [9302]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9302 or target_col == 9302). Every well: [[ZMAT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZMAT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
