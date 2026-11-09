---
symbol: "WSCD1"
type: "gene"
col: 11019
ensembl_id: "ENSG00000179314"
name: "WSC domain sialate O sulfotransferase 1"
location: "17p13.2"
module: 34
arm: "+"
pooled_cpm: 3.27
n_lines_expressing: 27
n_dd_up: 21
n_dd_down: 2
n_dd_up_clean: 10
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 5
direction_downstream: 1
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# WSCD1

*WSC domain sialate O sulfotransferase 1* — 17p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 5.59× (z +15.8, q 0e+00, up in 20 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.583× (z -5.0, q 3e-04, down in 16 of 25 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 16 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (HEC-1-A 0.105×, A549 0.134×, SNU-1 0.146×; ⚠ cell-cycle shift, explains ~32% of this change); [[Harringtonine (drug)]] 5 µM in 3 lines (HEC-1-A 0.144×, A549 0.0746×, NCI-H1792 0.0900×); [[Digitoxin (drug)]] 5 µM in 2 lines (A549 0.0303×, SNU-1 0.0890×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HEC-1-A 0.258×, NCI-H1792 0.234×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (HEC-1-A 0.120×, A549 0.107×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GALNT12]] (+0.74, fdr 7e-06), [[PKIA]] (+0.69, fdr 1e-05), [[WNT7B]] (+0.69, fdr 7e-06); moves opposite to [[EFCAB2]] (-0.56, fdr 6e-05), [[RNF146]] (-0.54, fdr 2e-04), [[FOXG1]] (-0.53, fdr 2e-04).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[XACT]] → it (grade B ⚠); 1 goes from it, the strongest it → [[RIMKLA]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 11 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11019.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **5.59×** | +15.8 | 0e+00 | 20/24 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **3.33×** | +15.7 | 0e+00 | 19/22 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.27×** | +13.3 | 2e-38 | 20/22 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.57×** | +11.7 | 2e-29 | 20/24 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.53×** | +11.1 | 9e-27 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.34×** | +11.1 | 1e-26 | 22/24 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.00×** | +9.3 | 9e-19 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.12×** | +6.9 | 3e-10 | 1/10 (C-33 A) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.57×** | +6.8 | 6e-10 | 12/19 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.92×** | +6.0 | 1e-07 | 11/17 (LoVo, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +5.9 | 2e-07 | 3/17 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +4.8 | 9e-05 | 2/13 (LoVo, C-33 A) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.63×** | +4.6 | 2e-04 | 10/20 (NCI-H460, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.03×** | +4.6 | 2e-04 | 0/8 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +4.4 | 4e-04 | 1/15 (A-427) | top dose only |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.53×** | +3.6 | 0.010 | 2/15 (SNU-1, NCI-H23) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11019.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 16 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (HEC-1-A 0.105×, A549 0.134×, SNU-1 0.146×; ⚠ cell-cycle shift, explains ~32% of this change); [[Harringtonine (drug)]] 5 µM in 3 lines (HEC-1-A 0.144×, A549 0.0746×, NCI-H1792 0.0900×); [[Digitoxin (drug)]] 5 µM in 2 lines (A549 0.0303×, SNU-1 0.0890×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HEC-1-A 0.258×, NCI-H1792 0.234×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (HEC-1-A 0.120×, A549 0.107×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.583×** | -5.0 | 3e-04 | 16/25 (SNU-1, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.578×** | -4.7 | 8e-04 | 7/23 (HEC-1-A, Hs 766T, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.903× | -3.4 | 0.12 | 7/25 (NCI-H1792, NCI-H1573, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.704× | -3.3 | 0.16 | 11/22 (SNU-1, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | 0.747× | -3.1 | 0.21 | 8/24 (HEC-1-A, A549, …) | rises with dose | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.719× | -3.1 | 0.21 | 5/23 (HEC-1-A, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11019. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 28.1 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -21.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -13.1) |
| [[SNU-1 (line)]] | wt | 18.6 | 0 | 6 (4 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0315× (z -15.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0907× (z -10.7) |
| [[A549 (line)]] | wt | 14.4 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0303× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.0746× (z -12.4) |
| [[NCI-H1792 (line)]] | alt | 12.8 | 0 | 5 | — | [[Harringtonine (drug)]] 5 µM 0.0900× (z -10.2) |
| [[A-427 (line)]] | wt | 5.30 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0497× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 6.67 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.1000× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 1.79 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 8.29× (z +9.6) | — |
| [[SW480 (line)]] | alt | 0.873 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 18.9× (z +9.8) | — |
| [[A-172 (line)]] | wt | 0.533 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.411 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.379 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.989 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.338 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.912 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.469 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.303 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.414 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.379 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.404 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.264 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.338 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 7.78 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.368 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.670 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.281 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.443 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.663 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.305 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.449 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.844 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.301 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.439 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.645 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.354 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.350 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11019), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GALNT12]] | +0.74 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[PKIA]] | +0.69 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[WNT7B]] | +0.69 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[SGSM1]] | +0.67 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[JAKMIP1]] | +0.65 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[FAM124A]] | +0.64 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[SYT13]] | +0.64 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[CALB2]] | +0.63 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[OTUB2]] | +0.63 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[GPRIN1]] | +0.63 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[ARID3B]] | +0.62 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[SH3GL3]] | +0.61 | +0.44 / +0.53 | both halves | 3e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFCAB2]] | -0.56 | -0.40 / -0.39 | both halves | 6e-05 |  |
| [[RNF146]] | -0.54 | -0.40 / -0.32 | both halves | 2e-04 |  |
| [[FOXG1]] | -0.53 | -0.49 / -0.32 | both halves | 2e-04 |  |
| [[C1RL]] | -0.52 | -0.44 / -0.33 | both halves | 1e-04 |  |
| [[CFLAR]] | -0.51 | -0.39 / -0.34 | both halves | 1e-04 |  |
| [[RPRD2]] | -0.50 | -0.27 / -0.45 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[XACT]] | B | XACT activity raises WSCD1's level | lines that do not express XACT (30) vs lines expressing it (20) | 2.00× lower at baseline in the lines without XACT | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000248515, ENSG00000267284, LINC02438 |
| [[IL33]] | B | IL33 activity raises WSCD1's level | lines that do not express IL33 (35) vs lines expressing it (15) | 1.46× lower at baseline in the lines without IL33 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01133, MUC2, LINC01411 |
| [[NTF3]] | B | NTF3 activity raises WSCD1's level | lines that do not express NTF3 (26) vs lines expressing it (24) | 1.54× lower at baseline in the lines without NTF3 | 0.044 | ⚠ within organs, on part of the lines; also absent: COL4A1, MME, HS3ST3A1 |
| [[SH3GL3]] | B | SH3GL3 activity raises WSCD1's level | lines that do not express SH3GL3 (21) vs lines expressing it (29) | 1.66× lower at baseline in the lines without SH3GL3 | 0.059 | ⚠ within organs, on part of the lines; also absent: S1PR3, SPANXA2-OT1, SALL1 |
| [[ARL4C]] | B | ARL4C activity raises WSCD1's level | lines that do not express ARL4C (14) vs lines expressing it (36) | 1.41× lower at baseline in the lines without ARL4C | 0.086 | ⚠ within organs, on part of the lines; also absent: NLRP1, ENSG00000225330, TRPM8 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RIMKLA]] | B | WSCD1 activity raises RIMKLA's level | lines that do not express WSCD1 (23) vs lines expressing it (27) | 2.12× lower at baseline in the lines without WSCD1 | 0.047 | ⚠ within organs, on part of the lines; also absent: JPH3, FAR2P1, ANKRD20A11P |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.633). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.1, -0.3); signed map (1.5, 46.4). **Vector** length 57.3, 13.4% of its response variance represented; |z| ≥ 3 in 671 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +15.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.2 | +6.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.6 | +11.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.8 | +11.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.8 | +15.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +4.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.2 | +0.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.2 | +2.3 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.0 | +1.8 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -2.2 | -2.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.0 | -0.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | +0.0 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.0 | -3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -4.7 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.8 | -2.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.7 | -0.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.6 | +1.0 |

## What is on record

|  |  |
|---|---|
| Name | WSC domain sialate O sulfotransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.2 — chr17:6,057,807-6,124,427 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0523 |
| Gene groups (HGNC) | Sulfotransferases, membrane bound |
| Matched by | ensembl_id |

**Function**, from UniProt [Q658N2](https://www.uniprot.org/uniprotkb/Q658N2) (Sialate:O-sulfotransferase 1):

> Sialate:O-sulfotransferase which catalyzes 8-O-sulfation at the Sia-glycan level using 3'-phosphoadenosine 5'-phosphosulfate (PAPS) as a donor, forming 8-O-sulfated Sia (Sia8S)-glycans. Displays selectivity toward glycolipids such as GM1 gangliosides.

**Summary**, from NCBI Gene [23302](https://www.ncbi.nlm.nih.gov/gene/23302):

> Predicted to enable sulfotransferase activity. Predicted to be located in Golgi membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29060](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29060) · Entrez [23302](https://www.ncbi.nlm.nih.gov/gene/23302) · UniProt [Q658N2](https://www.uniprot.org/uniprotkb/Q658N2) · Ensembl [ENSG00000179314](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179314)

## Data

Gene col 11019: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11019); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11019, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11019]; `tensor/DDL_lfc|DDL_z.npy` [11019]; `embed/gene_vectors.npy` [11019]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11019 or target_col == 11019). Every well: [[WSCD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WSCD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
