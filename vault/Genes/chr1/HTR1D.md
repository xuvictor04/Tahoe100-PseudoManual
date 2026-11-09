---
symbol: "HTR1D"
type: "gene"
col: 11042
ensembl_id: "ENSG00000179546"
name: "5-hydroxytryptamine receptor 1D"
location: "1p36.12"
module: 73
arm: "+"
pooled_cpm: 2.14
n_lines_expressing: 35
n_dd_up: 20
n_dd_down: 3
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 22
direction_downstream: 22
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# HTR1D

*5-hydroxytryptamine receptor 1D* — 1p36.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.59× (z +12.0, q 3e-30, up in 3 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 2.04× (z +8.2, q 3e-14, up in 9 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.515× (z -5.4, q 3e-05, down in 16 of 29 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 4 lines (LoVo 0.0326×, LS 180 0.0709×, AsPC-1 0.0726×, Panc 03.27 0.0327×); [[Belinostat (drug)]] 5 µM in 4 lines (J82 0.0263×, LoVo 0.134×, LS 180 0.113×, NCI-H460 0.111×; ⚠ cell-cycle shift, explains ~35% of this change); [[Panobinostat (drug)]] 0.5 µM in 3 lines (LoVo 0.0740×, AsPC-1 0.115×, Hs 766T 0.0587×); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2347 0.180×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02474]] (+0.65, fdr 1e-05), [[SLC6A20]] (+0.63, fdr 7e-06), [[COL17A1]] (+0.62, fdr 2e-05); moves opposite to [[VKORC1]] (-0.55, fdr 7e-05), [[CFDP1]] (-0.53, fdr 4e-05), [[KIAA1328]] (-0.53, fdr 9e-05).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 22 arrows point to it, the strongest [[LINC02582]] → it (grade B ⚠); 22 go from it, the strongest it → [[DSC2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11042.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.59×** | +12.0 | 3e-30 | 3/3 (NCI-H2347, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.03×** | +9.0 | 5e-17 | 4/11 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.07×** | +8.5 | 5e-15 | 1/5 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.04×** | +8.2 | 3e-14 | 9/22 (HepG2/C3A, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +5.4 | 6e-06 | 2/21 (A-172, HOP62) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.94×** | +5.4 | 6e-06 | 2/10 (LS 180, NCI-H2347) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.53×** | +4.9 | 8e-05 | 8/28 (J82, PANC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.49×** | +4.6 | 3e-04 | 6/28 (A-172, PANC-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +4.3 | 1e-03 | 2/17 (LoVo, NCI-H1792) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.71×** | +4.2 | 0.001 | 0/7 | top dose only | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +4.2 | 0.002 | 1/14 (HOP62) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.54×** | +3.5 | 0.019 | 3/25 (NCI-H1573, A549, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.53×** | +3.5 | 0.023 | 3/29 (KATO III, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.53×** | +3.4 | 0.023 | 1/19 (J82) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.51×** | +3.4 | 0.029 | 0/13 | inconsistent across doses | low cells (technical?) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.43×** | +2.9 | 0.097 | 5/28 (COLO 205, NCI-H460, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.48×** | +2.9 | 0.097 | 0/13 | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11042.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 4 lines (LoVo 0.0326×, LS 180 0.0709×, AsPC-1 0.0726×, Panc 03.27 0.0327×); [[Belinostat (drug)]] 5 µM in 4 lines (J82 0.0263×, LoVo 0.134×, LS 180 0.113×, NCI-H460 0.111×; ⚠ cell-cycle shift, explains ~35% of this change); [[Panobinostat (drug)]] 0.5 µM in 3 lines (LoVo 0.0740×, AsPC-1 0.115×, Hs 766T 0.0587×); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2347 0.180×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.515×** | -5.4 | 3e-05 | 16/29 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.586×** | -4.4 | 0.004 | 13/29 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.596×** | -4.2 | 0.005 | 14/26 (LoVo, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.678× | -3.2 | 0.21 | 11/29 (LoVo, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.664× | -3.1 | 0.23 | 1/28 (NCI-H1573) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11042. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 7.41 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0326× (z -17.2) |
| [[AsPC-1 (line)]] | alt | 10.2 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0726× (z -10.7) |
| [[LS 180 (line)]] | wt | 7.42 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0709× (z -11.1) |
| [[NCI-H460 (line)]] | wt | 3.33 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.111× (z -8.7) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Naproxen (drug)]] 0.05 µM 0.0959× (z -8.6) |
| [[Hs 766T (line)]] | wt | 4.70 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0587× (z -8.7) |
| [[J82 (line)]] | alt | 3.60 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0263× (z -11.0) ⚠ cell-cycle shift, explains ~35% of this change |
| [[NCI-H2347 (line)]] | alt | 3.76 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 3.61 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0327× (z -9.8) |
| [[A-172 (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.572 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.40 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.409 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.422 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.289 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.977 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.335 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.386 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.442 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.546 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.482 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.413 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.600 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.341 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.864 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.855 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.262 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.451 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.264 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.563 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.283 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.657 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.881 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.360 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.447 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11042), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02474]] | +0.65 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[SLC6A20]] | +0.63 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[COL17A1]] | +0.62 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[SH2D4A]] | +0.62 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[LINC01836]] | +0.61 | +0.56 / +0.40 | both halves | 5e-05 |  |
| [[LINC00857]] | +0.61 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[PLEKHA6]] | +0.61 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[TMEM30B]] | +0.61 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[MUC17]] | +0.60 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[DENND2D]] | +0.59 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[ATP8B4]] | +0.59 | +0.55 / +0.34 | both halves | 1e-04 |  |
| [[C4BPB]] | +0.58 | +0.57 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VKORC1]] | -0.55 | -0.50 / -0.38 | both halves | 7e-05 |  |
| [[CFDP1]] | -0.53 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[KIAA1328]] | -0.53 | -0.49 / -0.37 | both halves | 9e-05 |  |
| [[ARL3]] | -0.50 | -0.37 / -0.35 | both halves | 1e-04 |  |
| [[CABIN1]] | -0.49 | -0.37 / -0.38 | both halves | 7e-05 |  |
| [[DNAAF9]] | -0.49 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[UBE2O]] | -0.49 | -0.40 / -0.34 | both halves | 1e-04 |  |
| [[PFKFB4]] | -0.48 | -0.38 / -0.43 | both halves | 7e-05 |  |
| [[METTL26]] | -0.48 | -0.31 / -0.28 | both halves | 3e-04 |  |
| [[PHKA2]] | -0.48 | -0.45 / -0.25 | both halves | 4e-04 |  |
| [[SNAPC3]] | -0.47 | -0.36 / -0.40 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 21, C 1. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02582]] | B | LINC02582 activity raises HTR1D's level | lines that do not express LINC02582 (41) vs lines expressing it (9) | 2.14× lower at baseline in the lines without LINC02582 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, ENSG00000250920, ENSG00000230975 |
| [[UGT1A1]] | B | UGT1A1 activity raises HTR1D's level | lines that do not express UGT1A1 (36) vs lines expressing it (14) | 1.88× lower at baseline in the lines without UGT1A1 | 0.013 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, NPSR1 |
| [[NPSR1]] | B | NPSR1 activity raises HTR1D's level | lines that do not express NPSR1 (42) vs lines expressing it (8) | 2.40× lower at baseline in the lines without NPSR1 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, MUC17, CDH17 |
| [[GPA33]] | B | GPA33 activity raises HTR1D's level | lines that do not express GPA33 (41) vs lines expressing it (9) | 2.26× lower at baseline in the lines without GPA33 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17 |
| [[PSORS1C1]] | B | PSORS1C1 activity raises HTR1D's level | lines that do not express PSORS1C1 (15) vs lines expressing it (35) | 1.61× lower at baseline in the lines without PSORS1C1 | 0.033 | ⚠ within organs, on part of the lines; also absent: IL15, MGLL, SH3TC2 |
| [[C4BPB]] | B | C4BPB activity raises HTR1D's level | lines that do not express C4BPB (37) vs lines expressing it (13) | 2.02× lower at baseline in the lines without C4BPB | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, LINC02964, REG4 |
| [[SEPTIN9-DT]] | B | SEPTIN9-DT activity raises HTR1D's level | lines that do not express SEPTIN9-DT (13) vs lines expressing it (37) | 1.82× lower at baseline in the lines without SEPTIN9-DT | 0.042 | ⚠ within organs, on part of the lines; also absent: MALL, CDCP1, EPHA2; maybe low, not absent |
| [[MYOM3]] | B | MYOM3 activity raises HTR1D's level | lines that do not express MYOM3 (27) vs lines expressing it (23) | 1.44× lower at baseline in the lines without MYOM3 | 0.050 | ⚠ within organs, on part of the lines; also absent: HNF4A, EPS8L3, USH1C |
| [[MUC17]] | B | MUC17 activity raises HTR1D's level | lines that do not express MUC17 (44) vs lines expressing it (6) | 2.23× lower at baseline in the lines without MUC17 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, FGFR2, NPSR1 |
| [[CDH17]] | B | CDH17 activity raises HTR1D's level | lines that do not express CDH17 (40) vs lines expressing it (10) | 1.98× lower at baseline in the lines without CDH17 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, MUC13, CLRN3 |
| [[IGFL2]] | B | IGFL2 activity raises HTR1D's level | lines that do not express IGFL2 (38) vs lines expressing it (12) | 1.80× lower at baseline in the lines without IGFL2 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, REG4, GPA33 |
| [[LINC00857]] | B | LINC00857 activity raises HTR1D's level | lines that do not express LINC00857 (17) vs lines expressing it (33) | 1.88× lower at baseline in the lines without LINC00857 | 0.076 | ⚠ within organs, on part of the lines; also absent: KRT18, C19orf33, OCLN |

### Downstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 22, C 0. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DSC2]] | B | HTR1D activity raises DSC2's level | lines that do not express HTR1D (15) vs lines expressing it (35) | 2.55× lower at baseline in the lines without HTR1D | 0.018 | ⚠ within organs, on part of the lines; also absent: A4GALT, ZNF185, PAPSS2; maybe low, not absent |
| [[SH3RF2]] | B | HTR1D activity raises SH3RF2's level | lines that do not express HTR1D (15) vs lines expressing it (35) | 2.47× lower at baseline in the lines without HTR1D | 0.020 | ⚠ within organs, on part of the lines; also absent: A4GALT, ZNF185, PAPSS2; maybe low, not absent |
| [[PSORS1C1]] | B | HTR1D activity raises PSORS1C1's level | lines that do not express HTR1D (15) vs lines expressing it (35) | 2.02× lower at baseline in the lines without HTR1D | 0.020 | ⚠ within organs, on part of the lines; also absent: A4GALT, ZNF185, PAPSS2; maybe low, not absent |
| [[EHF]] | B | HTR1D activity raises EHF's level | lines that do not express HTR1D (15) vs lines expressing it (35) | 1.79× lower at baseline in the lines without HTR1D | 0.036 | ⚠ within organs, on part of the lines; also absent: A4GALT, ZNF185, PAPSS2; maybe low, not absent |
| [[ABCC3]] | B | HTR1D activity raises ABCC3's level | lines that do not express HTR1D (15) vs lines expressing it (35) | 1.93× lower at baseline in the lines without HTR1D | 0.042 | ⚠ within organs, on part of the lines; also absent: A4GALT, ZNF185, PAPSS2; maybe low, not absent |
| [[FAM83H]] | B | HTR1D activity raises FAM83H's level | lines that do not express HTR1D (15) vs lines expressing it (35) | 1.67× lower at baseline in the lines without HTR1D | 0.046 | ⚠ within organs, on part of the lines; also absent: A4GALT, ZNF185, PAPSS2; maybe low, not absent |
| [[TMPRSS2]] | B | HTR1D activity raises TMPRSS2's level | lines that do not express HTR1D (15) vs lines expressing it (35) | 2.01× lower at baseline in the lines without HTR1D | 0.049 | ⚠ within organs, on part of the lines; also absent: A4GALT, ZNF185, PAPSS2; maybe low, not absent |
| [[SEPTIN9-DT]] | B | HTR1D activity raises SEPTIN9-DT's level | lines that do not express HTR1D (15) vs lines expressing it (35) | 1.45× lower at baseline in the lines without HTR1D | 0.051 | ⚠ within organs, on part of the lines; also absent: A4GALT, ZNF185, PAPSS2; maybe low, not absent |
| [[LINC00857]] | B | HTR1D activity raises LINC00857's level | lines that do not express HTR1D (15) vs lines expressing it (35) | 1.85× lower at baseline in the lines without HTR1D | 0.054 | ⚠ within organs, on part of the lines; also absent: A4GALT, ZNF185, PAPSS2; maybe low, not absent |
| [[GCNT3]] | B | HTR1D activity raises GCNT3's level | lines that do not express HTR1D (15) vs lines expressing it (35) | 2.48× lower at baseline in the lines without HTR1D | 0.057 | ⚠ within organs, on part of the lines; also absent: A4GALT, ZNF185, PAPSS2; maybe low, not absent |
| [[PRKCH-AS1]] | B | HTR1D activity raises PRKCH-AS1's level | lines that do not express HTR1D (15) vs lines expressing it (35) | 1.56× lower at baseline in the lines without HTR1D | 0.058 | ⚠ within organs, on part of the lines; also absent: A4GALT, ZNF185, PAPSS2; maybe low, not absent |
| [[MISP]] | B | HTR1D activity raises MISP's level | lines that do not express HTR1D (15) vs lines expressing it (35) | 1.98× lower at baseline in the lines without HTR1D | 0.060 | ⚠ within organs, on part of the lines; also absent: A4GALT, ZNF185, PAPSS2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.688). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (17.2, 47.6); signed map (52.4, 5.9). **Vector** length 43.3, 7.07% of its response variance represented; |z| ≥ 3 in 672 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +12.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +8.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +5.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.2 | +8.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +4.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +1.9 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.2 | +1.5 |
| fall | [[Abemaciclib (drug)]] 5 µM |  | -1.3 | -2.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.2 | -4.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -1.2 | -2.5 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -1.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.1 | -1.6 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -0.9 | -2.5 |
|  | [[EX229 (drug)]] 0.05 µM |  | -0.9 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | 5-hydroxytryptamine receptor 1D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.12 — chr1:23,191,895-23,217,502 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RDC4, HT1DA, 5-HT1D; previously HTRL |
| Gene groups (HGNC) | 5-hydroxytryptamine receptors, G protein-coupled |
| Hallmark sets | KRAS_SIGNALING_DN |
| Reactome | 7 pathways, smallest: Serotonin receptors; Amine ligand-binding receptors; Class A/1 (Rhodopsin-like receptors) |
| Matched by | ensembl_id |

**Function**, from UniProt [P28221](https://www.uniprot.org/uniprotkb/P28221) (5-hydroxytryptamine receptor 1D):

> G protein-coupled receptor for 5-hydroxytryptamine (serotonin). Also functions as a receptor for ergot alkaloid derivatives, various anxiolytic and antidepressant drugs and other psychoactive substances. Ligand binding causes a conformation change that triggers signaling via guanine nucleotide-binding proteins (G proteins) and modulates the activity of downstream effectors, such as adenylate cyclase. HTR1D is coupled to G(i)/G(o) G alpha proteins and mediates inhibitory neurotransmission by …

**Summary**, from NCBI Gene [3352](https://www.ncbi.nlm.nih.gov/gene/3352):

> Enables Gi/o-coupled serotonin receptor activity. Involved in adenylate cyclase-inhibiting serotonin receptor signaling pathway and intestine smooth muscle contraction. Located in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:5289](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5289) · Entrez [3352](https://www.ncbi.nlm.nih.gov/gene/3352) · UniProt [P28221](https://www.uniprot.org/uniprotkb/P28221) · Ensembl [ENSG00000179546](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179546)

## Data

Gene col 11042: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11042); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11042, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11042]; `tensor/DDL_lfc|DDL_z.npy` [11042]; `embed/gene_vectors.npy` [11042]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11042 or target_col == 11042). Every well: [[HTR1D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HTR1D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
