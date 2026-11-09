---
symbol: "TRIM6"
type: "gene"
col: 4260
ensembl_id: "ENSG00000121236"
name: "tripartite motif containing 6"
location: "11p15.4"
module: 9
arm: "+"
pooled_cpm: 7.02
n_lines_expressing: 33
n_dd_up: 21
n_dd_down: 19
n_dd_up_clean: 18
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 5
direction_downstream: 3
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# TRIM6

*tripartite motif containing 6* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.87× (z +9.7, q 3e-19, up in 21 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.543× (z -9.3, q 5e-18, down in 18 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIM34]] (+0.59, fdr 1e-05, ⚠ same locus), [[HLTF]] (+0.54, fdr 2e-05), [[MEF2C]] (+0.54, fdr 1e-05), [[AR]] (+0.53, fdr 4e-05); moves opposite to [[ZNF778]] (-0.51, fdr 4e-05), [[RABL2B]] (-0.48, fdr 2e-04), [[RABL2A]] (-0.48, fdr 2e-04).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[HMGN3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4260.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.87×** | +9.7 | 3e-19 | 21/30 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.06×** | +7.8 | 1e-12 | 20/30 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.79×** | +6.3 | 4e-08 | 10/17 (SNU-423, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.73×** | +5.8 | 1e-06 | 4/9 (SNU-423, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.74×** | +5.5 | 3e-06 | 3/12 (NCI-H2347, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.59×** | +5.0 | 5e-05 | 12/30 (NCI-H2030, J82, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.57×** | +4.9 | 8e-05 | 8/30 (NCI-H2030, NCI-H1573, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.57×** | +4.7 | 2e-04 | 8/30 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.34×** | +4.5 | 3e-04 | 10/30 (HOP62, NCI-H2030, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **2.22×** | +4.5 | 3e-04 | 10/23 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.46×** | +4.1 | 0.002 | 4/30 (A498, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.46×** | +4.0 | 0.003 | 8/30 (AsPC-1, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.26×** | +3.5 | 0.021 | 4/30 (AsPC-1, NCI-H2347, …) | all doses, flat |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **1.33×** | +3.1 | 0.068 | 5/30 (PANC-1, A498, …) | inconsistent across doses |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.35×** | +3.1 | 0.068 | 6/30 (NCI-H2347, AsPC-1, …) | inconsistent across doses | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.28×** | +3.1 | 0.068 | 7/30 (AsPC-1, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.32×** | +3.1 | 0.073 | 5/30 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Furosemide (drug)]] 5 µM |  | **1.22×** | +3.0 | 0.077 | 4/30 (COLO 205, A498, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4260.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.543×** | -9.3 | 5e-18 | 18/28 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.447×** | -8.4 | 2e-14 | 15/23 (A498, SNU-423, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.496×** | -7.6 | 6e-12 | 16/30 (LOX-IMVI, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.514×** | -7.2 | 8e-11 | 16/30 (PANC-1, A498, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.542×** | -6.4 | 2e-08 | 16/25 (PANC-1, H4, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.594×** | -5.6 | 2e-06 | 16/30 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.609×** | -5.4 | 6e-06 | 13/25 (A498, PANC-1, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.627×** | -5.1 | 3e-05 | 13/30 (hTERT-HPNE, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.631×** | -5.0 | 4e-05 | 12/30 (A498, NCI-H2030, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.674×** | -4.3 | 0.001 | 11/30 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.479×** | -4.2 | 0.002 | 10/29 (PANC-1, NCI-H2030, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.781×** | -3.8 | 0.007 | 11/31 (PANC-1, NCI-H2347, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.696×** | -3.8 | 0.007 | 5/30 (A498, PANC-1, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.518×** | -3.7 | 0.008 | 9/25 (NCI-H2030, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.705×** | -3.6 | 0.014 | 8/30 (PANC-1, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.728×** | -3.4 | 0.021 | 11/30 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~13% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4260. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 38.2 | 0 | 8 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.139× (z -22.3) |
| [[A498 (line)]] | wt | 20.9 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -10.7) |
| [[NCI-H2030 (line)]] | alt | 33.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 5.87 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.160× (z -10.0) |
| [[NCI-H2347 (line)]] | alt | 7.61 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 4.05× (z +10.8) | — |
| [[A549 (line)]] | wt | 12.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.223× (z -10.7) |
| [[H4 (line)]] | wt | 8.52 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0592× (z -8.6) |
| [[SNU-423 (line)]] | alt | 8.70 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0916× (z -9.9) |
| [[A-172 (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.65 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.733 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.558 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.582 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.506 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.37 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.445 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.920 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.538 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.423 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.66 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.508 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.582 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.535 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.573 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.830 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.534 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.728 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4260), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM34]] | +0.59 | +0.64 / +0.50 | both halves | 1e-05 | same gene group; pathway: Interferon Signaling; ⚠ same locus (6.8 kb, same strand: neighbours can correlate without regulation) |
| [[HLTF]] | +0.54 | +0.47 / +0.54 | both halves | 2e-05 | same gene group |
| [[MEF2C]] | +0.54 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[AR]] | +0.53 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[HMGN3]] | +0.52 | +0.31 / +0.59 | both halves | 2e-04 |  |
| [[KLHL13]] | +0.51 | +0.27 / +0.53 | both halves | 3e-04 |  |
| [[AMOT]] | +0.51 | +0.39 / +0.52 | both halves | 5e-05 |  |
| [[MAPRE2]] | +0.51 | +0.36 / +0.53 | both halves | 9e-05 |  |
| [[SSX2IP]] | +0.50 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[LIMA1]] | +0.49 | +0.44 / +0.42 | both halves | 4e-05 |  |
| [[CXADR]] | +0.49 | +0.31 / +0.45 | both halves | 2e-04 |  |
| [[CNTNAP3C]] | +0.49 | +0.41 / +0.48 | both halves | 4e-05 |  |
| [[DUSP19]] | +0.48 | +0.45 / +0.51 | both halves | 3e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF778]] | -0.51 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[RABL2B]] | -0.48 | -0.31 / -0.52 | both halves | 2e-04 |  |
| [[RABL2A]] | -0.48 | -0.32 / -0.49 | both halves | 2e-04 |  |
| [[PTRH1]] | -0.47 | -0.31 / -0.47 | both halves | 2e-04 |  |
| [[GATD1-DT]] | -0.47 | -0.32 / -0.45 | both halves | 2e-04 |  |
| [[ZNF26]] | -0.46 | -0.36 / -0.42 | both halves | 9e-05 |  |
| [[HMGA2]] | -0.45 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[SMUG1]] | -0.44 | -0.32 / -0.30 | both halves | 2e-04 |  |
| [[TPTEP2-CSNK1E]] | -0.44 | -0.41 / -0.37 | both halves | 8e-05 |  |
| [[MOSMO]] | -0.44 | -0.32 / -0.39 | both halves | 2e-04 |  |
| [[AOC2]] | -0.43 | -0.37 / -0.32 | both halves | 2e-04 |  |
| [[FAM120B]] | -0.43 | -0.32 / -0.40 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises TRIM6's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CXADR]] | B | CXADR activity raises TRIM6's level | lines that do not express CXADR (16) vs lines expressing it (34) | 1.18× lower at baseline in the lines without CXADR | 0.067 | ⚠ within organs, on part of the lines; also absent: LSR, ENTPD2, LMTK3 |
| [[MAP2K1]] | B | MAP2K1 activity lowers TRIM6's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[TSPAN7]] | B | TSPAN7 activity lowers TRIM6's level | lines that do not express TSPAN7 (22) vs lines expressing it (28) | 1.58× higher at baseline in the lines without TSPAN7 | 0.093 | ⚠ within organs, on part of the lines; also absent: LINC02147, LINC00992, PINCR; maybe low, not absent |
| [[ZFHX4]] | C | ZFHX4 activity raises TRIM6's level | lines that do not express ZFHX4 (23) vs lines expressing it (27) | 2.48× lower at baseline in the lines without ZFHX4 | 0.088 | ⚠ within organs, on part of the lines; also absent: SNCA, UCHL1, SLITRK5; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HMGN3]] | B | TRIM6 activity lowers HMGN3's level | lines that do not express TRIM6 (17) vs lines expressing it (33) | 1.63× higher at baseline in the lines without TRIM6 | 0.019 | ⚠ within organs, on part of the lines; also absent: TFPI2, KMO, ENSG00000289526 |
| [[TRIM34]] | B | TRIM6 activity raises TRIM34's level | lines that do not express TRIM6 (17) vs lines expressing it (33) | 2.07× lower at baseline in the lines without TRIM6 | 0.030 | ⚠ within organs, on part of the lines; also absent: TFPI2, KMO, ENSG00000289526 |
| [[ZNF778]] | B | TRIM6 activity lowers ZNF778's level | lines that do not express TRIM6 (17) vs lines expressing it (33) | 1.00× higher at baseline in the lines without TRIM6 | 0.068 | ⚠ within organs, on part of the lines; also absent: TFPI2, KMO, ENSG00000289526 |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.298). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.9, 38.6); signed map (37.7, 37.8). **Vector** length 62.3, 13.1% of its response variance represented; |z| ≥ 3 in 684 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +9.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.6 | +7.8 |
|  | [[NG25 (drug)]] 5 µM |  | +2.9 | +4.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +5.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.4 | +4.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +5.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.0 | +4.5 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.8 | +3.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.7 | -9.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.1 | -8.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | -3.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.9 | -5.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.8 | -7.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.7 | -5.0 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.7 | -1.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.6 | -2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.5 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | tripartite motif containing 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:5,596,109-5,612,958 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RNF89 |
| Gene groups (HGNC) | Ring finger proteins; Tripartite motif family; RING finger E3 ubiquitin protein ligases |
| Reactome | 3 pathways, smallest: Interferon gamma signaling; Interferon Signaling; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9C030](https://www.uniprot.org/uniprotkb/Q9C030) (Tripartite motif-containing protein 6):

> E3 ubiquitin ligase that plays a crucial role in the activation of the IKBKE-dependent branch of the type I interferon signaling pathway. In concert with the ubiquitin-conjugating E2 enzyme UBE2K, synthesizes unanchored 'Lys-48'-linked polyubiquitin chains that promote the oligomerization and autophosphorylation of IKBKE leading to stimulation of an antiviral response. Also ubiquitinates MYC and inhibits its transcription activation activity, maintaining the pluripotency of embryonic stem cells …

**Summary**, from NCBI Gene [117854](https://www.ncbi.nlm.nih.gov/gene/117854):

> The protein encoded by this gene is a member of the tripartite motif (TRIM) family. The TRIM motif includes three zinc-binding domains, a RING, B-box type 1 and B-box type 2 domain, and a coiled-coil region. The protein localizes to the nucleus, but its specific function has not been identified. This gene is mapped to chromosome 11p15, where it resides within a TRIM gene cluster. Alternative splicing results in multiple transcript variants. A read-through transcript from this gene into the …

**Accessions** — [HGNC:16277](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16277) · Entrez [117854](https://www.ncbi.nlm.nih.gov/gene/117854) · UniProt [Q9C030](https://www.uniprot.org/uniprotkb/Q9C030) · Ensembl [ENSG00000121236](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121236)

## Data

Gene col 4260: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4260); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4260, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4260]; `tensor/DDL_lfc|DDL_z.npy` [4260]; `embed/gene_vectors.npy` [4260]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4260 or target_col == 4260). Every well: [[TRIM6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIM6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
