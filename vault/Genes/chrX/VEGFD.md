---
symbol: "VEGFD"
type: "gene"
col: 9086
ensembl_id: "ENSG00000165197"
name: "vascular endothelial growth factor D"
location: "Xp22.2"
module: 117
arm: "+"
pooled_cpm: 6.65
n_lines_expressing: 37
n_dd_up: 23
n_dd_down: 15
n_dd_up_clean: 21
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 10
tags: ["gene", "module/117"]
generated_by: "tahoemap"
---

# VEGFD

*vascular endothelial growth factor D* — Xp22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (2 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 4.67× (z +13.5, q 1e-38, up in 29 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.463× (z -10.1, q 3e-21, down in 22 of 33 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.361× (z -9.1, q 3e-17, down in 21 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIR]] (+0.88, fdr 7e-06, ⚠ same locus), [[NMRAL2P]] (+0.72, fdr 7e-06), [[GCLM]] (+0.68, fdr 7e-06), [[NMRAL2P-1]] (+0.67, fdr 7e-06); moves opposite to [[NOTCH2NLA]] (-0.48, fdr 4e-05), [[MMD]] (-0.46, fdr 5e-05), [[STMN3]] (-0.45, fdr 4e-05).
> It is in [[Module 117]], a single-armed module (NRF2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 10 go from it, the strongest it → [[CYP39A1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9086.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **4.67×** | +13.5 | 1e-38 | 29/32 (NCI-H1792, SW480, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **3.58×** | +11.8 | 1e-29 | 24/33 (HEC-1-A, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **3.37×** | +11.2 | 5e-27 | 23/31 (C32, HEC-1-A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **3.04×** | +10.3 | 1e-22 | 23/34 (NCI-H1792, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.76×** | +6.7 | 2e-09 | 14/33 (NCI-H1792, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **3.40×** | +5.9 | 3e-07 | 5/14 (SW480, A549, …) | all doses, flat | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.61×** | +4.7 | 2e-04 | 10/34 (C32, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.69×** | +4.7 | 2e-04 | 17/31 (SK-MEL-2, A498, …) | all doses, stronger at high dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | **1.43×** | +4.7 | 2e-04 | 11/33 (KATO III, C32, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.50×** | +4.7 | 2e-04 | 9/32 (NCI-H1573, SK-MEL-2, …) | two highest doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.45×** | +4.3 | 8e-04 | 7/34 (C32, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +4.0 | 0.003 | 5/22 (SW48, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.35×** | +3.8 | 0.008 | 10/34 (C32, Hs 766T, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.46×** | +3.5 | 0.020 | 11/34 (SK-MEL-2, NCI-H1573, …) | all doses, flat |  |
| [[Auranofin (drug)]] 0.5 µM |  | **1.45×** | +3.4 | 0.022 | 10/32 (KATO III, HEC-1-A, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.47×** | +3.4 | 0.022 | 11/31 (NCI-H1573, C32, …) | all doses, flat |  |
| [[Menadione (drug)]] 5 µM |  | **1.47×** | +3.4 | 0.022 | 6/31 (Hs 766T, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9086.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.463×** | -10.1 | 3e-21 | 22/33 (A549, A-427, …) | top dose only | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.361×** | -9.1 | 3e-17 | 21/33 (PANC-1, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.257×** | -6.6 | 9e-09 | 20/33 (NCI-H460, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.693×** | -4.8 | 2e-04 | 16/31 (NCI-H460, SNU-1, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.628×** | -4.3 | 0.001 | 14/34 (PANC-1, NCI-H460, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.628×** | -4.3 | 0.001 | 16/33 (PANC-1, NCI-H460, …) | two highest doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.657×** | -3.9 | 0.007 | 9/32 (PANC-1, RPMI-7951, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.472×** | -3.6 | 0.019 | 13/31 (A-427, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.676×** | -3.5 | 0.029 | 9/33 (SNU-423, Hs 766T, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.689×** | -3.3 | 0.056 | 9/31 (PANC-1, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.684×** | -3.3 | 0.056 | 10/27 (C32, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **0.706×** | -3.2 | 0.056 | 9/32 (SW 900, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.698×** | -3.2 | 0.056 | 7/32 (A-427, LS 180, …) | top dose only |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **0.702×** | -3.2 | 0.063 | 2/34 (HEC-1-A, BT-474) | top dose only | plate-row cell shift |
| [[Selinexor (drug)]] 0.5 µM |  | **0.724×** | -3.0 | 0.098 | 7/32 (SNU-1, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9086. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 27.4 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.229× (z -12.9) |
| [[NCI-H1573 (line)]] | alt | 39.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0579× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 5.30 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.136× (z -9.5) |
| [[A-172 (line)]] | wt | 2.67 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -8.6) ⚠ cell-cycle shift, explains ~33% of this change |
| [[A-427 (line)]] | wt | 9.56 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -9.2) ⚠ cell-cycle shift, explains ~33% of this change |
| [[A549 (line)]] | wt | 5.32 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -10.4) ⚠ cell-cycle shift, explains ~33% of this change |
| [[HEC-1-A (line)]] | alt | 3.95 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 10.5× (z +8.6) | — |
| [[KATO III (line)]] | alt | 14.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.255× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 3.09 | 0 | 1 | — | [[Clotrimazole (drug)]] 0.5 µM 0.0700× (z -9.2) |
| [[SNU-1 (line)]] | wt | 16.9 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0976× (z -8.8) |
| [[A498 (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.909 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.762 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.882 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.883 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.10 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.971 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.981 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 8.15 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.927 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 8.58 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.03 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9086), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIR]] | +0.88 | +0.88 / +0.85 | both halves | 7e-06 | STRING 459; ⚠ same locus (0.4 kb, same strand: neighbours can correlate without regulation) |
| [[NMRAL2P]] | +0.72 | +0.65 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[GCLM]] | +0.68 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[NMRAL2P-1]] | +0.67 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[SLC7A11]] | +0.64 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[EGF]] | +0.63 | +0.54 / +0.64 | both halves | 1e-05 | pathway: Platelet activation, signaling and aggregation; STRING 509 |
| [[AKR1C1]] | +0.63 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[CYP4F11]] | +0.63 | +0.58 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[ME1]] | +0.62 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[ABCC2]] | +0.60 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[ANKRD23]] | +0.59 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[TDO2]] | +0.58 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[TXNRD1]] | +0.57 | +0.54 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOTCH2NLA]] | -0.48 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[MMD]] | -0.46 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[STMN3]] | -0.45 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[ZDHHC23]] | -0.44 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[ZNF670]] | -0.44 | -0.42 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers VEGFD's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[PIR]] | C | PIR activity raises VEGFD's level | lines that do not express PIR (10) vs lines expressing it (40) | 3.34× lower at baseline in the lines without PIR | 0.004 | ⚠ within organs, on part of the lines; also absent: VEGFD, ELMO1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CYP39A1]] | B | VEGFD activity raises CYP39A1's level | lines that do not express VEGFD (13) vs lines expressing it (37) | 1.72× lower at baseline in the lines without VEGFD | 0.020 | ⚠ within organs, on part of the lines; also absent: PIR, ELMO1 |
| [[ANKRD13A]] | B | VEGFD activity lowers ANKRD13A's level | lines that do not express VEGFD (13) vs lines expressing it (37) | 1.19× higher at baseline in the lines without VEGFD | 0.045 | ⚠ within organs, on part of the lines; also absent: PIR, ELMO1 |
| [[ME1]] | B | VEGFD activity raises ME1's level | lines that do not express VEGFD (13) vs lines expressing it (37) | 2.72× lower at baseline in the lines without VEGFD | 0.056 | ⚠ within organs, on part of the lines; also absent: PIR, ELMO1 |
| [[GSEC]] | B | VEGFD activity raises GSEC's level | lines that do not express VEGFD (13) vs lines expressing it (37) | 1.15× lower at baseline in the lines without VEGFD | 0.079 | ⚠ within organs, on part of the lines; also absent: PIR, ELMO1 |
| [[OLMALINC]] | B | VEGFD activity raises OLMALINC's level | lines that do not express VEGFD (13) vs lines expressing it (37) | 1.38× lower at baseline in the lines without VEGFD | 0.080 | ⚠ within organs, on part of the lines; also absent: PIR, ELMO1 |
| [[TRIM16L-1]] | B | VEGFD activity raises TRIM16L-1's level | lines that do not express VEGFD (13) vs lines expressing it (37) | 1.61× lower at baseline in the lines without VEGFD | 0.089 | ⚠ within organs, on part of the lines; also absent: PIR, ELMO1 |
| [[CAPS2]] | B | VEGFD activity raises CAPS2's level | lines that do not express VEGFD (13) vs lines expressing it (37) | 1.49× lower at baseline in the lines without VEGFD | 0.089 | ⚠ within organs, on part of the lines; also absent: PIR, ELMO1 |
| [[XKR9]] | B | VEGFD activity raises XKR9's level | lines that do not express VEGFD (13) vs lines expressing it (37) | 1.97× lower at baseline in the lines without VEGFD | 0.091 | ⚠ within organs, on part of the lines; also absent: PIR, ELMO1 |
| [[FTL]] | B | VEGFD activity lowers FTL's level | lines that do not express VEGFD (13) vs lines expressing it (37) | 1.12× higher at baseline in the lines without VEGFD | 0.094 | ⚠ within organs, on part of the lines; also absent: PIR, ELMO1 |
| [[PIR]] | C | VEGFD activity raises PIR's level | lines that do not express VEGFD (13) vs lines expressing it (37) | 4.33× lower at baseline in the lines without VEGFD | 2e-04 | ⚠ within organs, on part of the lines; also absent: PIR, ELMO1; co-absent with the target |

## Where it sits

- **Module**: [[Module 117]] — NRF2; 41 genes; every member is in the + arm (projection on the module's main direction 0.770). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-8.4, 48.2); signed map (51.3, -10.3). **Vector** length 83.3, 19.4% of its response variance represented; |z| ≥ 3 in 866 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *NRF2* (control, mean cos +0.56 to 8); *Nuclear events mediated by NFE2L2* (reactome, mean cos +0.59 to 7); *KEAP1-NFE2L2 pathway* (reactome, mean cos +0.59 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +7.0 | +13.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.6 | +10.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.3 | +11.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.9 | +11.2 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +4.0 | +5.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.2 | +4.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.0 | +6.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +3.4 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -3.2 | -6.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.9 | -9.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -0.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -1.9 | -10.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -2.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.7 | -3.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -2.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.5 | -2.8 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.5 | -3.3 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.5 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | vascular endothelial growth factor D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.2 — chrX:15,345,596-15,384,413 (-) |
| Ensembl biotype | protein_coding |
| Also known as | VEGF-D; previously FIGF |
| Gene groups (HGNC) | VEGF family |
| Reactome | 8 pathways, smallest: VEGF binds to VEGFR leading to receptor dimerization; VEGF ligand-receptor interactions; Signaling by VEGF |
| Matched by | ensembl_id |

**Function**, from UniProt [O43915](https://www.uniprot.org/uniprotkb/O43915) (Vascular endothelial growth factor D):

> Growth factor active in angiogenesis, lymphangiogenesis and endothelial cell growth, stimulating their proliferation and migration and also has effects on the permeability of blood vessels. May function in the formation of the venous and lymphatic vascular systems during embryogenesis, and also in the maintenance of differentiated lymphatic endothelium in adults. Binds and activates VEGFR-2 (KDR/FLK1) and VEGFR-3 (FLT4) receptors.

**Summary**, from NCBI Gene [2277](https://www.ncbi.nlm.nih.gov/gene/2277):

> The protein encoded by this gene is a member of the platelet-derived growth factor/vascular endothelial growth factor (PDGF/VEGF) family and is active in angiogenesis, lymphangiogenesis, and endothelial cell growth. This secreted protein undergoes a complex proteolytic maturation, generating multiple processed forms which bind and activate VEGFR-2 and VEGFR-3 receptors. This protein is structurally and functionally similar to vascular endothelial growth factor C. Read-through transcription has …

**Accessions** — [HGNC:3708](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3708) · Entrez [2277](https://www.ncbi.nlm.nih.gov/gene/2277) · UniProt [O43915](https://www.uniprot.org/uniprotkb/O43915) · Ensembl [ENSG00000165197](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165197)

## Data

Gene col 9086: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9086); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9086, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9086]; `tensor/DDL_lfc|DDL_z.npy` [9086]; `embed/gene_vectors.npy` [9086]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9086 or target_col == 9086). Every well: [[VEGFD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VEGFD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
