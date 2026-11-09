---
symbol: "SPOCK1"
type: "gene"
col: 7618
ensembl_id: "ENSG00000152377"
name: "SPARC (osteonectin), cwcv and kazal like domains proteoglycan 1"
location: "5q31.2"
module: 13
arm: "+"
pooled_cpm: 145.35
n_lines_expressing: 21
n_dd_up: 11
n_dd_down: 22
n_dd_up_clean: 7
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 38
direction_downstream: 108
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# SPOCK1

*SPARC (osteonectin), cwcv and kazal like domains proteoglycan 1* — 5q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.72× (z +12.2, q 2e-31, up in 8 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (none with an alert); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.656× (z -6.2, q 3e-07, down in 7 of 19 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADAMTS6]] (+0.73, fdr 7e-06), [[NMNAT2]] (+0.66, fdr 7e-06), [[CDH13]] (+0.65, fdr 1e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 38 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 108 go from it, the strongest it → [[PPFIBP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7618.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.72×** | +12.2 | 2e-31 | 8/19 (C32, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.13×** | +12.0 | 1e-30 | 5/20 (A498, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.87×** | +9.5 | 2e-19 | 4/17 (SW 900, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.61×** | +7.5 | 6e-12 | 6/20 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.62×** | +7.1 | 1e-10 | 3/17 (C32, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.33×** | +6.5 | 1e-08 | 5/19 (A-172, C32, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +4.9 | 5e-05 | 1/20 (SW 900) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.38×** | +4.9 | 5e-05 | 11/19 (A498, C32, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +4.0 | 0.004 | 1/21 (H4) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vilanterol (drug)]] 0.5 µM |  | **1.27×** | +3.8 | 0.007 | 4/19 (C32, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.39×** | +3.7 | 0.011 | 0/19 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 1.15× | +3.1 | 0.10 | 7/19 (J82, RPMI-7951, …) | rises with dose |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 1.14× | +3.0 | 0.11 | 2/19 (A498, hTERT-HPNE) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 3 with an alert ⚠; shown: the 15 strongest. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7618.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.656×** | -6.2 | 3e-07 | 7/19 (A549, NCI-H460, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.762×** | -6.0 | 6e-07 | 6/19 (A549, SHP-77, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.713×** | -5.4 | 1e-05 | 10/19 (NCI-H2030, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Triamcinolone (drug)]] 5 µM |  | **0.797×** | -5.1 | 5e-05 | 13/19 (HOP62, J82, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.781×** | -4.7 | 2e-04 | 8/19 (A549, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.761×** | -4.6 | 3e-04 | 8/21 (J82, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.749×** | -4.6 | 4e-04 | 11/19 (HOP62, J82, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.809×** | -4.1 | 0.003 | 9/19 (J82, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.776×** | -4.0 | 0.004 | 11/19 (J82, HOP62, …) | two highest doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.790×** | -3.8 | 0.010 | 9/20 (A549, NCI-H460, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.798×** | -3.6 | 0.018 | 9/19 (HOP62, J82, …) | all doses, stronger at high dose |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.659×** | -3.5 | 0.025 | 2/19 (J82, NCI-H460) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.805×** | -3.4 | 0.025 | 9/19 (HOP62, A549, …) | all doses, flat | position effect removed |
| [[Larotrectinib (drug)]] 5 µM |  | 0.859× | -3.4 | 0.025 | 15/19 (RPMI-7951, HS-578T, …) | rises with dose | position effect removed |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.807×** | -3.4 | 0.025 | 8/19 (HOP62, A549, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7618. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 1,407 | 0 | 8 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.335× (z -15.3) |
| [[J82 (line)]] | alt | 318 | 0 | 7 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.250× (z -15.4) |
| [[HOP62 (line)]] | alt | 436 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -14.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -11.7) |
| [[RPMI-7951 (line)]] | alt | 370 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.227× (z -15.2) |
| [[A-172 (line)]] | wt | 52.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.48× (z +18.4) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[C32 (line)]] | wt | 38.1 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 4.92× (z +14.8) | — |
| [[NCI-H596 (line)]] | alt | 145 | 0 | 2 (1 ⚠) | — | [[Citalopram (hydrobromide) (drug)]] 0.05 µM 0.159× (z -9.7) |
| [[NCI-H2030 (line)]] | alt | 168 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.493× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 986 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.201× (z -13.9) |
| [[A-427 (line)]] | wt | 16.0 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 155 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 89.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.8 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 11.8 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 13.7 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 20.4 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 17.4 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 16.3 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 23.9 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 58.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.4 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 16.6 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 17.7 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 21.6 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 15.4 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 202 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 17.9 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 15.7 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 10.7 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.8 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 12.8 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 92.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 67.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.32 n.m. | — | — | — | — |
| [[NCI-H661 (line)]] | alt | 20.5 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 10.0 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 29.0 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 11.4 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 24.1 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 14.2 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 222 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 243 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.6 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 14.3 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 10.3 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7618), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAMTS6]] | +0.73 | +0.69 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[NMNAT2]] | +0.66 | +0.59 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[CDH13]] | +0.65 | +0.57 / +0.70 | both halves | 1e-05 | **novel candidate** |
| [[BMPER]] | +0.65 | +0.60 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[TMEM200A]] | +0.64 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[SAMD3]] | +0.64 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[SCUBE1]] | +0.64 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[GPR68]] | +0.63 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[SYNDIG1]] | +0.62 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[VEGFC]] | +0.62 | +0.61 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[AFF3]] | +0.62 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[INSYN2B]] | +0.61 | +0.56 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*38 arrows, 38 of them with an alert ⚠; grade A 0, B 4, C 34. Shown: the 12 strongest; 26 more arrows (26 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises SPOCK1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[RNF152]] | B | RNF152 activity raises SPOCK1's level | lines that do not express RNF152 (18) vs lines expressing it (32) | 2.44× lower at baseline in the lines without RNF152 | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000267175, SNCAIP, OR9Q1; maybe low, not absent |
| [[RBFOX1]] | B | RBFOX1 activity raises SPOCK1's level | lines that do not express RBFOX1 (6) vs lines expressing it (44) | 3.61× lower at baseline in the lines without RBFOX1 | 0.082 | ⚠ within organs, on part of the lines; also absent: LINC02932, ZNF474, DNAH6; maybe low, not absent |
| [[LRRC8C]] | B | LRRC8C activity raises SPOCK1's level | lines that do not express LRRC8C (8) vs lines expressing it (42) | 3.78× lower at baseline in the lines without LRRC8C | 0.091 | ⚠ within organs, on part of the lines; also absent: ZNF474, ACOT12, PPP4R4; maybe low, not absent |
| [[SIRLNT]] | C | SIRLNT activity raises SPOCK1's level | lines that do not express SIRLNT (32) vs lines expressing it (18) | 7.09× lower at baseline in the lines without SIRLNT | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1; co-absent with the target |
| [[BMPER]] | C | BMPER activity raises SPOCK1's level | lines that do not express BMPER (21) vs lines expressing it (29) | 5.75× lower at baseline in the lines without BMPER | 0.003 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000253471, IL7R; co-absent with the target |
| [[PAPPA]] | C | PAPPA activity raises SPOCK1's level | lines that do not express PAPPA (33) vs lines expressing it (17) | 7.19× lower at baseline in the lines without PAPPA | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HTRA3, MSC-AS1, PDGFRB; co-absent with the target |
| [[EPHB1]] | C | EPHB1 activity raises SPOCK1's level | lines that do not express EPHB1 (16) vs lines expressing it (34) | 4.62× lower at baseline in the lines without EPHB1 | 0.015 | ⚠ within organs, on part of the lines; also absent: KCNG1, DOCK2, GLIS1; maybe low, not absent; co-absent with the target |
| [[CDH13]] | C | CDH13 activity raises SPOCK1's level | lines that do not express CDH13 (35) vs lines expressing it (15) | 4.40× lower at baseline in the lines without CDH13 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, APCDD1L, ENSG00000222032; co-absent with the target |
| [[ITGA11]] | C | ITGA11 activity raises SPOCK1's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 6.41× lower at baseline in the lines without ITGA11 | 0.018 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411; co-absent with the target |
| [[ABI3BP]] | C | ABI3BP activity raises SPOCK1's level | lines that do not express ABI3BP (32) vs lines expressing it (18) | 4.58× lower at baseline in the lines without ABI3BP | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000280241, FLI1, DKK3; maybe low, not absent; co-absent with the target |
| [[COL15A1]] | C | COL15A1 activity raises SPOCK1's level | lines that do not express COL15A1 (28) vs lines expressing it (22) | 5.32× lower at baseline in the lines without COL15A1 | 0.020 | ⚠ within organs, on part of the lines; also absent: LINC01583, PHACTR1, GYPC; co-absent with the target |

### Downstream of this gene

*108 arrows, 108 of them with an alert ⚠; grade A 0, B 58, C 50. Shown: the 12 strongest; 96 more arrows (96 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPFIBP1]] | B | SPOCK1 activity raises PPFIBP1's level | lines that do not express SPOCK1 (29) vs lines expressing it (21) | 1.50× lower at baseline in the lines without SPOCK1 | 0.006 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| [[CHD1L]] | B | SPOCK1 activity raises CHD1L's level | lines that do not express SPOCK1 (29) vs lines expressing it (21) | 1.96× lower at baseline in the lines without SPOCK1 | 0.010 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| [[CD44]] | B | SPOCK1 activity raises CD44's level | lines that do not express SPOCK1 (29) vs lines expressing it (21) | 3.53× lower at baseline in the lines without SPOCK1 | 0.011 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| [[PRSS23]] | B | SPOCK1 activity raises PRSS23's level | lines that do not express SPOCK1 (29) vs lines expressing it (21) | 2.69× lower at baseline in the lines without SPOCK1 | 0.013 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| cells under [[Peretinoin (drug)]] 0.5 µM | B | SPOCK1 activity lowers the cells' numbers under Peretinoin 0.5 µM (makes them more sensitive) | lines that do not express SPOCK1 (29) vs lines expressing it (19) | the lines without SPOCK1: 1.54× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| cells under [[Macitentan (drug)]] 5 µM | B | SPOCK1 activity lowers the cells' numbers under Macitentan 5 µM (makes them more sensitive) | lines that do not express SPOCK1 (29) vs lines expressing it (19) | the lines without SPOCK1: 1.34× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| cells under [[Clopidogrel (drug)]] 0.05 µM | B | SPOCK1 activity raises the cells' numbers under Clopidogrel 0.05 µM (protects the cells) | lines that do not express SPOCK1 (29) vs lines expressing it (19) | the lines without SPOCK1: 0.75× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| cells under [[Lactate (calcium) (drug)]] 0.05 µM | B | SPOCK1 activity raises the cells' numbers under Lactate (calcium) 0.05 µM (protects the cells) | lines that do not express SPOCK1 (29) vs lines expressing it (19) | the lines without SPOCK1: 0.79× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| cells under [[Irinotecan (hydrochloride) (drug)]] 5 µM | B | SPOCK1 activity raises the cells' numbers under Irinotecan (hydrochloride) 5 µM (protects the cells) | lines that do not express SPOCK1 (29) vs lines expressing it (19) | the lines without SPOCK1: 0.81× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| cells under [[Methylthiouracil (drug)]] 0.05 µM | B | SPOCK1 activity raises the cells' numbers under Methylthiouracil 0.05 µM (protects the cells) | lines that do not express SPOCK1 (29) vs lines expressing it (19) | the lines without SPOCK1: 0.82× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| cells under [[Ivermectin (drug)]] 0.5 µM | B | SPOCK1 activity lowers the cells' numbers under Ivermectin 0.5 µM (makes them more sensitive) | lines that do not express SPOCK1 (29) vs lines expressing it (19) | the lines without SPOCK1: 1.21× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| cells under [[Vinblastine (sulfate) (drug)]] 5 µM | B | SPOCK1 activity lowers the cells' numbers under Vinblastine (sulfate) 5 µM (makes them more sensitive) | lines that do not express SPOCK1 (29) vs lines expressing it (19) | the lines without SPOCK1: 1.18× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.700). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.5, 14.9); signed map (20.6, 48.2). **Vector** length 86.2, 30.0% of its response variance represented; |z| ≥ 3 in 705 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Defective B3GALTL causes PpS* (reactome, mean cos +0.52 to 8); *O-glycosylation of TSR domain-containing proteins* (reactome, mean cos +0.52 to 8); *Diseases associated with O-glycosylation of proteins* (reactome, mean cos +0.52 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.3 | +12.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.8 | +9.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.8 | +7.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +12.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.4 | +7.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +0.5 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.7 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +3.7 |
| fall | [[Triamcinolone (drug)]] 5 µM |  | -2.9 | -5.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.8 | -6.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.7 | -3.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.7 | -2.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.6 | -4.0 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.5 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | SPARC (osteonectin), cwcv and kazal like domains proteoglycan 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.2 — chr5:136,975,298-137,598,379 (-) |
| Ensembl biotype | protein_coding |
| Also known as | testican-1; previously TIC1, SPOCK |
| Gene groups (HGNC) | SPARC family |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Matched by | ensembl_id |

**Function**, from UniProt [Q08629](https://www.uniprot.org/uniprotkb/Q08629) (Testican-1):

> May play a role in cell-cell and cell-matrix interactions. May contribute to various neuronal mechanisms in the central nervous system.

**Summary**, from NCBI Gene [6695](https://www.ncbi.nlm.nih.gov/gene/6695):

> This gene encodes the protein core of a seminal plasma proteoglycan containing chondroitin- and heparan-sulfate chains. The protein's function is unknown, although similarity to thyropin-type cysteine protease-inhibitors suggests its function may be related to protease inhibition. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11251](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11251) · Entrez [6695](https://www.ncbi.nlm.nih.gov/gene/6695) · UniProt [Q08629](https://www.uniprot.org/uniprotkb/Q08629) · Ensembl [ENSG00000152377](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152377)

## Data

Gene col 7618: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7618); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7618, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7618]; `tensor/DDL_lfc|DDL_z.npy` [7618]; `embed/gene_vectors.npy` [7618]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7618 or target_col == 7618). Every well: [[SPOCK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPOCK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
