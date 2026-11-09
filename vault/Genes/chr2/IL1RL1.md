---
symbol: "IL1RL1"
type: "gene"
col: 3700
ensembl_id: "ENSG00000115602"
name: "interleukin 33 receptor"
location: "2q12.1"
module: 101
arm: "+"
pooled_cpm: 3.94
n_lines_expressing: 18
n_dd_up: 24
n_dd_down: 6
n_dd_up_clean: 12
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 6
direction_downstream: 10
tags: ["gene", "module/101"]
generated_by: "tahoemap"
---

# IL1RL1

*interleukin 33 receptor* — 2q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 6.76× (z +11.3, q 6e-27, up in 2 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.48× (z +7.9, q 3e-13, up in 4 of 12 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Pentamidine (isethionate) (drug)]] 5 µM: 0.593× (z -4.6, q 0.003, down in 10 of 15 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ELK3]] (+0.60, fdr 1e-05), [[FOXL1]] (+0.58, fdr 1e-05), [[THSD4]] (+0.56, fdr 1e-05); moves opposite to [[MIRLET7BHG]] (-0.48, fdr 7e-05), [[MAP3K2]] (-0.46, fdr 4e-05), [[ARHGAP35]] (-0.46, fdr 8e-05).
> It is in [[Module 101]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[SH3RF3]] → it (grade B ⚠); 10 go from it, the strongest it → [[IL18R1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3700.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.76×** | +11.3 | 6e-27 | 2/6 (AsPC-1, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.37×** | +9.1 | 3e-17 | 4/10 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.42×** | +8.2 | 4e-14 | 4/7 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.48×** | +7.9 | 3e-13 | 4/12 (HS-578T, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.84×** | +6.4 | 1e-08 | 9/13 (NCI-H1573, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.08×** | +6.4 | 2e-08 | 4/14 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.50×** | +5.4 | 5e-06 | 1/11 (A549) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **2.28×** | +5.1 | 3e-05 | 8/15 (NCI-H460, CFPAC-1, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.76×** | +4.9 | 5e-05 | 3/16 (HS-578T, CFPAC-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.69×** | +4.6 | 3e-04 | 3/15 (HS-578T, NCI-H2030, …) | rises with dose |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.75×** | +4.4 | 5e-04 | 0/8 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.11×** | +4.4 | 5e-04 | 2/9 (NCI-H460, AsPC-1) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.02×** | +4.3 | 6e-04 | 2/10 (AsPC-1, Hs 766T) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.88×** | +3.9 | 0.004 | 0/10 | inconsistent across doses | low cells (technical?); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.84×** | +3.8 | 0.006 | 2/14 (PANC-1, Panc 03.27) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.78×** | +3.5 | 0.014 | 4/15 (NCI-H1573, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 0.5 µM |  | **2.20×** | +3.5 | 0.017 | 2/10 (NCI-H460, NCI-H2030) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.48×** | +3.4 | 0.018 | 3/15 (NCI-H460, NCI-H2030, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.64×** | +3.0 | 0.064 | 4/12 (AsPC-1, NCI-H1573, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.86×** | +3.0 | 0.064 | 1/9 (AsPC-1) | inconsistent across doses | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3700.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | **0.593×** | -4.6 | 0.003 | 10/15 (NCI-H2030, CFPAC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.488×** | -4.4 | 0.003 | 9/16 (NCI-H1573, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **0.651×** | -3.7 | 0.034 | 11/15 (NCI-H2347, A549, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.575×** | -3.4 | 0.089 | 8/16 (NCI-H1573, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.502×** | -3.4 | 0.090 | 7/16 (NCI-H1573, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.586×** | -3.3 | 0.092 | 11/16 (PANC-1, NCI-H1573, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.689× | -3.2 | 0.12 | 9/15 (NCI-H1573, NCI-H2347, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.608× | -3.1 | 0.15 | 8/16 (CFPAC-1, NCI-H1573, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.658× | -3.0 | 0.16 | 9/15 (NCI-H2030, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3700. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 45.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -14.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.130× (z -9.8) |
| [[CFPAC-1 (line)]] | alt | 12.2 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0182× (z -11.1) |
| [[NCI-H2030 (line)]] | alt | 4.50 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.352× (z -9.6) ⚠ position not correctable |
| [[A-172 (line)]] | wt | 0.372 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.253 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.251 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.592 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.376 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.375 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.384 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.328 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.421 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.359 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.449 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.386 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.405 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.575 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.328 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.383 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.488 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.528 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.363 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.261 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.496 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 9.91 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.382 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.371 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.890 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.259 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.310 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.347 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.687 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.869 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.624 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.343 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.310 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3700), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELK3]] | +0.60 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[FOXL1]] | +0.58 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[THSD4]] | +0.56 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[DHRS9]] | +0.54 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[HMGA2]] | +0.52 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[IL18R1]] | +0.51 | +0.39 / +0.53 | both halves | 5e-05 | same gene group; pathway: HALLMARK_IL2_STAT5_SIGNALING; STRING 421; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[ITGA2-AS1]] | +0.50 | +0.53 / +0.42 | both halves | 4e-05 |  |
| [[B4GALT6]] | +0.50 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[SOWAHC]] | +0.50 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[MCL1]] | +0.50 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[LAMC2]] | +0.49 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[ERCC1]] | +0.48 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[PRDM1]] | +0.48 | +0.47 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIRLET7BHG]] | -0.48 | -0.46 / -0.37 | both halves | 7e-05 |  |
| [[MAP3K2]] | -0.46 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[ARHGAP35]] | -0.46 | -0.40 / -0.37 | both halves | 8e-05 |  |
| [[PKDCC]] | -0.46 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[CXXC5]] | -0.44 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[HSF2]] | -0.43 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[LGR4]] | -0.43 | -0.39 / -0.39 | both halves | 6e-05 |  |
| [[GPRC5B]] | -0.43 | -0.37 / -0.38 | both halves | 9e-05 |  |
| [[LRIG1]] | -0.43 | -0.39 / -0.37 | both halves | 8e-05 | same gene group; pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[ST3GAL4]] | -0.43 | -0.32 / -0.46 | both halves | 2e-04 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[RHOXF1]] | -0.43 | -0.39 / -0.38 | both halves | 7e-05 |  |
| [[RHOT1]] | -0.43 | -0.41 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 3, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SH3RF3]] | B | SH3RF3 activity lowers IL1RL1's level | lines that do not express SH3RF3 (14) vs lines expressing it (36) | 1.45× higher at baseline in the lines without SH3RF3 | 0.019 | ⚠ within organs, on part of the lines; also absent: DCLK2, OSBPL6, FHL1 |
| [[IL18R1]] | B | IL18R1 activity raises IL1RL1's level | lines that do not express IL18R1 (15) vs lines expressing it (35) | 2.01× lower at baseline in the lines without IL18R1 | 0.043 | ⚠ within organs, on part of the lines; also absent: JCAD |
| [[NEK10]] | B | NEK10 activity lowers IL1RL1's level | lines that do not express NEK10 (6) vs lines expressing it (44) | 2.81× higher at baseline in the lines without NEK10 | 0.081 | ⚠ within organs, on part of the lines; also absent: ZNF474, ITPR2-AS1, LINC00334; maybe low, not absent |
| [[CA2]] | C | CA2 activity raises IL1RL1's level | lines that do not express CA2 (27) vs lines expressing it (23) | 2.03× lower at baseline in the lines without CA2 | 0.031 | ⚠ within organs, on part of the lines; also absent: CCDC68, SCEL, MUC4; co-absent with the target |
| [[DHRS9]] | C | DHRS9 activity raises IL1RL1's level | lines that do not express DHRS9 (40) vs lines expressing it (10) | 2.63× lower at baseline in the lines without DHRS9 | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, PIGR, LINC01610; co-absent with the target |
| [[CLMP]] | C | CLMP activity raises IL1RL1's level | lines that do not express CLMP (25) vs lines expressing it (25) | 1.99× lower at baseline in the lines without CLMP | 0.075 | ⚠ within organs, on part of the lines; also absent: KCNMA1, PAPPA, DOCK10; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 6, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL18R1]] | B | IL1RL1 activity raises IL18R1's level | lines that do not express IL1RL1 (32) vs lines expressing it (18) | 2.81× lower at baseline in the lines without IL1RL1 | 0.001 | ⚠ within organs, on part of the lines; also absent: FAM83A, GSDMC, IGFBP1 |
| [[LGR4]] | B | IL1RL1 activity raises LGR4's level | lines that do not express IL1RL1 (32) vs lines expressing it (18) | 1.82× lower at baseline in the lines without IL1RL1 | 0.015 | ⚠ within organs, on part of the lines; also absent: FAM83A, GSDMC, IGFBP1 |
| [[ITGA2]] | B | IL1RL1 activity raises ITGA2's level | lines that do not express IL1RL1 (32) vs lines expressing it (18) | 3.35× lower at baseline in the lines without IL1RL1 | 0.088 | ⚠ within organs, on part of the lines; also absent: FAM83A, GSDMC, IGFBP1 |
| [[PRDM1]] | B | IL1RL1 activity raises PRDM1's level | lines that do not express IL1RL1 (32) vs lines expressing it (18) | 2.18× lower at baseline in the lines without IL1RL1 | 0.098 | ⚠ within organs, on part of the lines; also absent: FAM83A, GSDMC, IGFBP1 |
| [[THSD4]] | B | IL1RL1 activity raises THSD4's level | lines that do not express IL1RL1 (32) vs lines expressing it (18) | 2.82× lower at baseline in the lines without IL1RL1 | 0.099 | ⚠ within organs, on part of the lines; also absent: FAM83A, GSDMC, IGFBP1 |
| [[CDCP1]] | B | IL1RL1 activity raises CDCP1's level | lines that do not express IL1RL1 (32) vs lines expressing it (18) | 2.23× lower at baseline in the lines without IL1RL1 | 0.0997 | ⚠ within organs, on part of the lines; also absent: FAM83A, GSDMC, IGFBP1 |
| [[LAMC2]] | C | IL1RL1 activity raises LAMC2's level | lines that do not express IL1RL1 (32) vs lines expressing it (18) | 4.35× lower at baseline in the lines without IL1RL1 | 0.003 | ⚠ within organs, on part of the lines; also absent: FAM83A, GSDMC, IGFBP1; co-absent with the target |
| [[AADAC]] | C | IL1RL1 activity raises AADAC's level | lines that do not express IL1RL1 (32) vs lines expressing it (18) | 3.12× lower at baseline in the lines without IL1RL1 | 0.031 | ⚠ within organs, on part of the lines; also absent: FAM83A, GSDMC, IGFBP1; co-absent with the target |
| [[CA2]] | C | IL1RL1 activity raises CA2's level | lines that do not express IL1RL1 (32) vs lines expressing it (18) | 1.72× lower at baseline in the lines without IL1RL1 | 0.053 | ⚠ within organs, on part of the lines; also absent: FAM83A, GSDMC, IGFBP1; co-absent with the target |
| [[DHRS9]] | C | IL1RL1 activity raises DHRS9's level | lines that do not express IL1RL1 (32) vs lines expressing it (18) | 2.96× lower at baseline in the lines without IL1RL1 | 0.062 | ⚠ within organs, on part of the lines; also absent: FAM83A, GSDMC, IGFBP1; co-absent with the target |

## Where it sits

- **Module**: [[Module 101]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.454). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (35.7, 12.1); signed map (11.2, 45.8). **Vector** length 47.3, 13.8% of its response variance represented; |z| ≥ 3 in 450 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +4.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.9 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.8 | +9.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.7 | +8.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.6 | +2.6 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.3 | +2.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.3 | +5.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | +4.6 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.9 | -2.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.9 | -1.6 |
|  | [[Trametinib (drug)]] 5 µM |  | -1.8 | -4.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.7 | -0.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.7 | -3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | interleukin 33 receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q12.1 — chr2:102,311,502-102,352,037 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IL-33R, ST2, FIT-1, ST2L, ST2V, DER4, T1; previously IL1RL1 |
| Gene groups (HGNC) | I-set domain containing; Interleukin receptors; TIR domain containing |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Reactome | 8 pathways, smallest: Interleukin-33 signaling; PI5P, PP2A and IER3 Regulate PI3K/AKT Signaling; Negative regulation of the PI3K/AKT network |
| Matched by | ensembl_id |

**Function**, from UniProt [Q01638](https://www.uniprot.org/uniprotkb/Q01638) (Interleukin-1 receptor-like 1):

> Receptor for interleukin-33 (IL-33) which plays crucial roles in innate and adaptive immunity, contributing to tissue homeostasis and responses to environmental stresses together with coreceptor IL1RAP. Its stimulation recruits MYD88, IRAK1, IRAK4, and TRAF6, followed by phosphorylation of MAPK3/ERK1 and/or MAPK1/ERK2, MAPK14, and MAPK8. Possibly involved in helper T-cell function (Probable). Upon tissue injury, induces UCP2-dependent mitochondrial rewiring that attenuates the generation of …

**Summary**, from NCBI Gene [9173](https://www.ncbi.nlm.nih.gov/gene/9173):

> The protein encoded by this gene is a member of the interleukin 1 receptor family. Studies of the similar gene in mouse suggested that this receptor can be induced by proinflammatory stimuli, and may be involved in the function of helper T cells. This gene, interleukin 1 receptor, type I (IL1R1), interleukin 1 receptor, type II (IL1R2) and interleukin 1 receptor-like 2 (IL1RL2) form a cytokine receptor gene cluster in a region mapped to chromosome 2q12. Alternative splicing of this gene results …

**Accessions** — [HGNC:5998](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5998) · Entrez [9173](https://www.ncbi.nlm.nih.gov/gene/9173) · UniProt [Q01638](https://www.uniprot.org/uniprotkb/Q01638) · Ensembl [ENSG00000115602](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115602)

## Data

Gene col 3700: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3700); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3700, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3700]; `tensor/DDL_lfc|DDL_z.npy` [3700]; `embed/gene_vectors.npy` [3700]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3700 or target_col == 3700). Every well: [[IL1RL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IL1RL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
