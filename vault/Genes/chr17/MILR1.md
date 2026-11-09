---
symbol: "MILR1"
type: "gene"
col: 15690
ensembl_id: "ENSG00000271605"
name: "mast cell immunoglobulin like receptor 1"
location: "17q23.3"
module: 196
arm: "+"
pooled_cpm: 3.02
n_lines_expressing: 31
n_dd_up: 12
n_dd_down: 22
n_dd_up_clean: 5
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 20
direction_downstream: 37
tags: ["gene", "module/196"]
generated_by: "tahoemap"
---

# MILR1

*mast cell immunoglobulin like receptor 1* — 17q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.15× (z +10.5, q 7e-23, up in 8 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.424× (z -8.3, q 7e-14, down in 16 of 27 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PECAM1]] (+0.67, fdr 7e-06, ⚠ same locus), [[IL19]] (+0.66, fdr 1e-05), [[FKBP9P1-1]] (+0.59, fdr 7e-06), [[VSIG1]] (+0.58, fdr 7e-06); moves opposite to [[KIF13A]] (-0.53, fdr 4e-05), [[NCOA6]] (-0.44, fdr 8e-05), [[ADCY9]] (-0.44, fdr 1e-04).
> It is in [[Module 196]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 20 arrows point to it, the strongest [[ADAM28]] → it (grade B ⚠); 37 go from it, the strongest it → [[NRP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15690.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.15×** | +10.5 | 7e-23 | 8/24 (A-172, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.07×** | +10.4 | 7e-23 | 1/7 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.09×** | +7.1 | 3e-10 | 3/13 (A498, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.01×** | +6.2 | 6e-08 | 1/10 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.75×** | +5.4 | 7e-06 | 7/24 (A498, LOX-IMVI, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.28×** | +4.2 | 0.003 | 1/5 (SHP-77) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.53×** | +4.1 | 0.004 | 8/26 (SW480, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.34×** | +4.0 | 0.005 | 7/28 (HS-578T, Hs 766T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +3.7 | 0.011 | 2/18 (SW 900, RPMI-7951) | top dose only |  |
| [[Lenalidomide (hemihydrate) (drug)]] 0.05 µM |  | **1.43×** | +3.4 | 0.033 | 2/25 (COLO 205, NCI-H1792) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +3.2 | 0.076 | 1/14 (CFPAC-1) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.84×** | +3.1 | 0.098 | 1/6 (SW480) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, none with an alert; shown: the 15 strongest. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15690.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.424×** | -8.3 | 7e-14 | 16/27 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.484×** | -6.7 | 5e-09 | 18/25 (CFPAC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Trametinib (drug)]] 5 µM |  | **0.503×** | -6.4 | 2e-08 | 17/28 (RPMI-7951, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.521×** | -6.3 | 5e-08 | 14/25 (CFPAC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.532×** | -6.1 | 1e-07 | 15/25 (HS-578T, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.553×** | -5.7 | 1e-06 | 13/27 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.584×** | -4.8 | 1e-04 | 7/26 (SHP-77, SW480, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.609×** | -4.6 | 3e-04 | 10/22 (C32, SW480, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.665×** | -3.9 | 0.005 | 10/26 (SW480, SHP-77, …) | all doses, flat |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.461×** | -3.9 | 0.005 | 5/28 (H4, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.683×** | -3.7 | 0.012 | 5/26 (HOP62, LOX-IMVI, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.763×** | -3.6 | 0.014 | 9/28 (C32, SHP-77, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.694×** | -3.5 | 0.018 | 9/27 (HS-578T, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.703×** | -3.4 | 0.027 | 11/25 (Panc 03.27, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.782×** | -3.3 | 0.031 | 8/28 (HS-578T, SHP-77, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15690. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RPMI-7951 (line)]] | alt | 20.9 | 0 | 5 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0946× (z -10.7) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.101× (z -10.4) |
| [[HS-578T (line)]] | alt | 16.3 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0746× (z -11.3) |
| [[Panc 03.27 (line)]] | alt | 12.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -12.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.107× (z -9.3) |
| [[SNU-423 (line)]] | alt | 5.42 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0427× (z -11.2) |
| [[C32 (line)]] | wt | 5.98 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0638× (z -9.4) |
| [[CFPAC-1 (line)]] | alt | 5.23 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 15.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -12.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 4.46 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.124× (z -8.6) |
| [[A-172 (line)]] | wt | 0.798 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.288 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.519 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.419 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.670 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.446 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.570 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 8.06 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.93 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.707 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.970 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.824 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.365 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.454 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.301 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.444 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.490 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.342 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.430 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.406 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.258 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.407 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.333 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.384 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15690), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PECAM1]] | +0.67 | +0.62 / +0.65 | both halves | 7e-06 | same gene group; ⚠ same locus (35.3 kb: neighbours can correlate without regulation) |
| [[IL19]] | +0.66 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[FKBP9P1-1]] | +0.59 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[VSIG1]] | +0.58 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[DNAH2]] | +0.58 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[LAPTM5]] | +0.57 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[LINC02813]] | +0.57 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[TMEM163]] | +0.56 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[STRA6]] | +0.56 | +0.66 / +0.44 | both halves | 3e-05 |  |
| [[MIR4280HG]] | +0.56 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[ATP6V0A4]] | +0.56 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[OPRD1]] | +0.56 | +0.42 / +0.42 | both halves | 4e-05 |  |
| [[ANGPTL2]] | +0.56 | +0.52 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIF13A]] | -0.53 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[NCOA6]] | -0.44 | -0.38 / -0.37 | both halves | 8e-05 |  |
| [[ADCY9]] | -0.44 | -0.40 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 10, C 10. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAM28]] | B | ADAM28 activity raises MILR1's level | lines that do not express ADAM28 (31) vs lines expressing it (19) | 2.25× lower at baseline in the lines without ADAM28 | 0.003 | ⚠ within organs, on part of the lines; also absent: DHRS9, BATF, IGFBP5 |
| [[MIR3681HG]] | B | MIR3681HG activity raises MILR1's level | lines that do not express MIR3681HG (27) vs lines expressing it (23) | 1.90× lower at baseline in the lines without MIR3681HG | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000225649, BAALC, LINC02930; maybe low, not absent |
| [[CCDC33]] | B | CCDC33 activity raises MILR1's level | lines that do not express CCDC33 (24) vs lines expressing it (26) | 1.70× lower at baseline in the lines without CCDC33 | 0.037 | ⚠ within organs, on part of the lines; also absent: STRA6, ENSG00000261543, KLF8 |
| [[ADAM28]] | B | ADAM28 activity strengthens MILR1's drug response | lines that do not express ADAM28 (16) vs lines expressing it (12) | the lines without ADAM28 respond 0.81× as strongly (z diff +0.66); strongest at Panobinostat 5 µM: 0.49x vs 0.25x (z diff +2.8) | 0.055 | ⚠ within organs, on part of the lines; also absent: DHRS9, BATF, IGFBP5; target measured in part of the lines; both ways; artifact flags |
| [[CCDC152]] | B | CCDC152 activity raises MILR1's level | lines that do not express CCDC152 (30) vs lines expressing it (20) | 2.32× lower at baseline in the lines without CCDC152 | 0.059 | ⚠ within organs, on part of the lines; also absent: PLAT, SNTG1, COL19A1; maybe low, not absent |
| [[LINC02970]] | B | LINC02970 activity raises MILR1's level | lines that do not express LINC02970 (24) vs lines expressing it (26) | 2.01× lower at baseline in the lines without LINC02970 | 0.064 | ⚠ within organs, on part of the lines; also absent: TOX, MXRA5, ENSG00000255595 |
| [[ETV1]] | B | ETV1 activity raises MILR1's level | lines that do not express ETV1 (11) vs lines expressing it (39) | 2.02× lower at baseline in the lines without ETV1 | 0.078 | ⚠ within organs, on part of the lines; also absent: LINC02454, KATNAL1, CCDC136 |
| [[SHC4]] | B | SHC4 activity raises MILR1's level | lines that do not express SHC4 (23) vs lines expressing it (27) | 1.85× lower at baseline in the lines without SHC4 | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000250137, AR, GNG2; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises MILR1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[LINC02405]] | B | LINC02405 activity raises MILR1's level | lines that do not express LINC02405 (27) vs lines expressing it (23) | 1.85× lower at baseline in the lines without LINC02405 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000286016, ENSG00000278266, LINC02360 |
| [[NLRP1]] | C | NLRP1 activity raises MILR1's level | lines that do not express NLRP1 (21) vs lines expressing it (29) | 2.79× lower at baseline in the lines without NLRP1 | 0.003 | ⚠ within organs, on part of the lines; also absent: EVA1A, NRP2, SLFN12; co-absent with the target |
| [[ITGB3]] | C | ITGB3 activity raises MILR1's level | lines that do not express ITGB3 (25) vs lines expressing it (25) | 2.29× lower at baseline in the lines without ITGB3 | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000259753, BICC1, ENSG00000291130; co-absent with the target |

### Downstream of this gene

*37 arrows, 37 of them with an alert ⚠; grade A 0, B 24, C 13. Shown: the 12 strongest; 25 more arrows (25 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NRP1]] | B | MILR1 activity raises NRP1's level | lines that do not express MILR1 (19) vs lines expressing it (31) | 3.63× lower at baseline in the lines without MILR1 | 0.001 | ⚠ within organs, on part of the lines; also absent: EVA1A, LINC00973, NLRP1 |
| [[LINC02970]] | B | MILR1 activity raises LINC02970's level | lines that do not express MILR1 (19) vs lines expressing it (31) | 2.47× lower at baseline in the lines without MILR1 | 0.007 | ⚠ within organs, on part of the lines; also absent: EVA1A, LINC00973, NLRP1 |
| [[ADAM19]] | B | MILR1 activity raises ADAM19's level | lines that do not express MILR1 (19) vs lines expressing it (31) | 3.36× lower at baseline in the lines without MILR1 | 0.008 | ⚠ within organs, on part of the lines; also absent: EVA1A, LINC00973, NLRP1 |
| [[ZNF697]] | B | MILR1 activity raises ZNF697's level | lines that do not express MILR1 (19) vs lines expressing it (31) | 2.14× lower at baseline in the lines without MILR1 | 0.012 | ⚠ within organs, on part of the lines; also absent: EVA1A, LINC00973, NLRP1 |
| [[GNA15]] | B | MILR1 activity raises GNA15's level | lines that do not express MILR1 (19) vs lines expressing it (31) | 1.99× lower at baseline in the lines without MILR1 | 0.014 | ⚠ within organs, on part of the lines; also absent: EVA1A, LINC00973, NLRP1 |
| [[TGFA]] | B | MILR1 activity raises TGFA's level | lines that do not express MILR1 (19) vs lines expressing it (31) | 2.83× lower at baseline in the lines without MILR1 | 0.021 | ⚠ within organs, on part of the lines; also absent: EVA1A, LINC00973, NLRP1 |
| [[PLB1]] | B | MILR1 activity raises PLB1's level | lines that do not express MILR1 (19) vs lines expressing it (31) | 1.67× lower at baseline in the lines without MILR1 | 0.021 | ⚠ within organs, on part of the lines; also absent: EVA1A, LINC00973, NLRP1 |
| [[IL19]] | B | MILR1 activity raises IL19's level | lines that do not express MILR1 (19) vs lines expressing it (31) | 1.77× lower at baseline in the lines without MILR1 | 0.021 | ⚠ within organs, on part of the lines; also absent: EVA1A, LINC00973, NLRP1 |
| [[PECAM1]] | B | MILR1 activity raises PECAM1's level | lines that do not express MILR1 (19) vs lines expressing it (31) | 1.88× lower at baseline in the lines without MILR1 | 0.036 | ⚠ within organs, on part of the lines; also absent: EVA1A, LINC00973, NLRP1 |
| [[LOXL4]] | B | MILR1 activity raises LOXL4's level | lines that do not express MILR1 (19) vs lines expressing it (31) | 2.14× lower at baseline in the lines without MILR1 | 0.037 | ⚠ within organs, on part of the lines; also absent: EVA1A, LINC00973, NLRP1 |
| [[TMEM163]] | B | MILR1 activity raises TMEM163's level | lines that do not express MILR1 (19) vs lines expressing it (31) | 2.05× lower at baseline in the lines without MILR1 | 0.039 | ⚠ within organs, on part of the lines; also absent: EVA1A, LINC00973, NLRP1 |
| [[PLAT]] | B | MILR1 activity raises PLAT's level | lines that do not express MILR1 (19) vs lines expressing it (31) | 2.63× lower at baseline in the lines without MILR1 | 0.039 | ⚠ within organs, on part of the lines; also absent: EVA1A, LINC00973, NLRP1 |

## Where it sits

- **Module**: [[Module 196]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.723). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (51.7, 8.0); signed map (10.6, 53.1). **Vector** length 54.3, 10.8% of its response variance represented; |z| ≥ 3 in 718 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.3 | +10.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.6 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.4 | +6.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +10.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +5.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +1.7 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.6 | +1.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.4 | +0.2 |
| fall | [[Trametinib (drug)]] 5 µM |  | -2.6 | -6.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.6 | -4.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.1 | -3.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.0 | -3.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.7 | -2.1 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.6 | -1.4 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.6 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | mast cell immunoglobulin like receptor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q23.3 — chr17:64,449,037-64,468,643 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Allergin-1, MCA-32; previously C17orf60 |
| Gene groups (HGNC) | Immunoglobulin like domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z6M3](https://www.uniprot.org/uniprotkb/Q7Z6M3) (Allergin-1):

> Immunoglobulin-like receptor which plays an inhibitory role in degranulation of mast cells. Negatively regulates IgE-mediated mast cell activation and suppresses the type I immediate hypersensitivity reaction (By similarity).

**Summary**, from NCBI Gene [284021](https://www.ncbi.nlm.nih.gov/gene/284021):

> Predicted to enable transmembrane signaling receptor activity. Predicted to be involved in cell surface receptor signaling pathway; mast cell degranulation; and negative regulation of mast cell activation. Predicted to be located in plasma membrane. Predicted to be active in external side of plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27570](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27570) · Entrez [284021](https://www.ncbi.nlm.nih.gov/gene/284021) · UniProt [Q7Z6M3](https://www.uniprot.org/uniprotkb/Q7Z6M3) · Ensembl [ENSG00000271605](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000271605)

## Data

Gene col 15690: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15690); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15690, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15690]; `tensor/DDL_lfc|DDL_z.npy` [15690]; `embed/gene_vectors.npy` [15690]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15690 or target_col == 15690). Every well: [[MILR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MILR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
