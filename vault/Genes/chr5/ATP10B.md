---
symbol: "ATP10B"
type: "gene"
col: 3982
ensembl_id: "ENSG00000118322"
name: "ATPase phospholipid transporting 10B (putative)"
location: "5q34"
module: 44
arm: "+"
pooled_cpm: 21.3
n_lines_expressing: 10
n_dd_up: 8
n_dd_down: 4
n_dd_up_clean: 5
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 100
direction_downstream: 140
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# ATP10B

*ATPase phospholipid transporting 10B (putative)* — 5q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.72× (z +8.3, q 8e-14, up in 0 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.81× (z +6.9, q 8e-10, up in 0 of 8 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.588× (z -4.4, q 0.006, down in 8 of 8 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (COLO 205 0.0594×, HT-29 0.0722×, LoVo 0.131×, LS 180 0.163×, …); [[Auranofin (drug)]] 5 µM in 4 lines (COLO 205 0.0124×, LoVo 0.0427×, KATO III 0.0517×, HT-29 0.0637×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (COLO 205 0.0173×, LoVo 0.0386×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (COLO 205 0.0200×, LoVo 0.0813×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRR15L]] (+0.81, fdr 7e-06), [[MUC13]] (+0.80, fdr 7e-06), [[TMPRSS2]] (+0.76, fdr 7e-06).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 100 arrows point to it, the strongest [[BOLA3-DT]] → it (grade B ⚠); 140 go from it, the strongest it → [[C4orf19]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3982.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.72×** | +8.3 | 8e-14 | 0/8 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.54×** | +7.4 | 3e-11 | 0/6 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +6.9 | 8e-10 | 0/8 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.45×** | +6.8 | 1e-09 | 0/7 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.62×** | +4.7 | 3e-04 | 6/8 (KATO III, LS 180, …) | two highest doses | noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +3.7 | 0.018 | 3/8 (SW1417, LS 180, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.59×** | +3.5 | 0.040 | 6/8 (LS 180, HT-29, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.72×** | +3.2 | 0.094 | 0/8 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 5 µM | ⚠ toxic | 2.08× | +3.1 | 0.14 | 2/8 (KATO III, LS 180) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3982.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (COLO 205 0.0594×, HT-29 0.0722×, LoVo 0.131×, LS 180 0.163×, …); [[Auranofin (drug)]] 5 µM in 4 lines (COLO 205 0.0124×, LoVo 0.0427×, KATO III 0.0517×, HT-29 0.0637×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (COLO 205 0.0173×, LoVo 0.0386×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (COLO 205 0.0200×, LoVo 0.0813×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.588×** | -4.4 | 0.006 | 8/8 (LS 180, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.655×** | -3.5 | 0.078 | 7/8 (HT-29, LoVo, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.657×** | -3.5 | 0.078 | 7/8 (COLO 205, C32, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.659×** | -3.5 | 0.078 | 7/8 (COLO 205, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3982. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 270 | 0 | 19 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0173× (z -24.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.0124× (z -18.9) |
| [[LoVo (line)]] | wt | 238 | 0 | 13 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0386× (z -23.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.0427× (z -16.3) |
| [[HT-29 (line)]] | alt | 104 | 0 | 9 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0722× (z -15.9) |
| [[KATO III (line)]] | alt | 44.6 | 0 | 9 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0316× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.0517× (z -12.7) |
| [[C32 (line)]] | wt | 81.6 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.140× (z -12.7) |
| [[LS 180 (line)]] | wt | 105 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.163× (z -13.7) |
| [[SK-MEL-2 (line)]] | alt | 39.4 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0814× (z -11.8) ⚠ cell-cycle shift, explains ~64% of this change |
| [[A-172 (line)]] | wt | 2.45 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.87 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.99 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.98 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.31 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.78 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.48 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.57 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.60 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.85 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.77 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.60 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.82 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.93 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.73 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.96 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.22 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.01 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.99 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.00 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.31 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.18 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.79 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.09 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.52 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.65 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.63 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.51 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.67 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.58 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.36 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.05 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.19 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3982), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRR15L]] | +0.81 | +0.82 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[MUC13]] | +0.80 | +0.77 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[TMPRSS2]] | +0.76 | +0.71 / +0.78 | both halves | 7e-06 |  |
| [[PRR15]] | +0.75 | +0.73 / +0.70 | both halves | 7e-06 |  |
| [[GCNT3]] | +0.74 | +0.74 / +0.73 | both halves | 7e-06 |  |
| [[LINC02331]] | +0.74 | +0.75 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[NPSR1]] | +0.74 | +0.76 / +0.67 | both halves | 7e-06 |  |
| [[CLIC5]] | +0.74 | +0.63 / +0.76 | both halves | 7e-06 |  |
| [[MYO7B]] | +0.73 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[FGFR2]] | +0.73 | +0.70 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[HEPH]] | +0.73 | +0.71 / +0.75 | both halves | 7e-06 |  |
| [[SMIM2-AS1]] | +0.72 | +0.82 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*100 arrows, 100 of them with an alert ⚠; grade A 0, B 3, C 97. Shown: the 12 strongest; 88 more arrows (88 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BOLA3-DT]] | B | BOLA3-DT activity lowers ATP10B's level | lines that do not express BOLA3-DT (10) vs lines expressing it (40) | 4.80× higher at baseline in the lines without BOLA3-DT | 0.038 | ⚠ within organs, on part of the lines; also absent: GIHCG, KATNAL1, LIX1L |
| [[PLEKHS1]] | B | PLEKHS1 activity raises ATP10B's level | lines that do not express PLEKHS1 (15) vs lines expressing it (35) | 2.60× lower at baseline in the lines without PLEKHS1 | 0.080 | ⚠ within organs, on part of the lines; also absent: ENSG00000261227, CYP4F3, CRYM; maybe low, not absent |
| [[MAP2K2]] | B | MAP2K2 activity lowers ATP10B's level | compounds that target MAP2K2: 2 of 2 raise it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; shared targets |
| [[NPSR1]] | C | NPSR1 activity raises ATP10B's level | lines that do not express NPSR1 (42) vs lines expressing it (8) | 13.44× lower at baseline in the lines without NPSR1 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, MUC17, CDH17; co-absent with the target |
| [[FAM3D]] | C | FAM3D activity raises ATP10B's level | lines that do not express FAM3D (43) vs lines expressing it (7) | 13.62× lower at baseline in the lines without FAM3D | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, ENSG00000230975, NPSR1; maybe low, not absent; co-absent with the target |
| [[CDH17]] | C | CDH17 activity raises ATP10B's level | lines that do not express CDH17 (40) vs lines expressing it (10) | 9.43× lower at baseline in the lines without CDH17 | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, MUC13, CLRN3; co-absent with the target |
| [[SMIM2-AS1]] | C | SMIM2-AS1 activity raises ATP10B's level | lines that do not express SMIM2-AS1 (37) vs lines expressing it (13) | 7.97× lower at baseline in the lines without SMIM2-AS1 | 1e-03 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ATP10B, CFTR, TRIM31; maybe low, not absent; co-absent with the target |
| [[MUC13]] | C | MUC13 activity raises ATP10B's level | lines that do not express MUC13 (40) vs lines expressing it (10) | 8.64× lower at baseline in the lines without MUC13 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, NPSR1, CDH17; co-absent with the target |
| [[CEACAM5]] | C | CEACAM5 activity raises ATP10B's level | lines that do not express CEACAM5 (39) vs lines expressing it (11) | 6.62× lower at baseline in the lines without CEACAM5 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, ENSG00000267881; co-absent with the target |
| [[GCNT3]] | C | GCNT3 activity raises ATP10B's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 5.90× lower at baseline in the lines without GCNT3 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13; co-absent with the target |
| [[UGT1A1]] | C | UGT1A1 activity raises ATP10B's level | lines that do not express UGT1A1 (36) vs lines expressing it (14) | 3.95× lower at baseline in the lines without UGT1A1 | 0.001 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, NPSR1; co-absent with the target |
| [[TRIM31]] | C | TRIM31 activity raises ATP10B's level | lines that do not express TRIM31 (39) vs lines expressing it (11) | 6.98× lower at baseline in the lines without TRIM31 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, GCNT3, NPSR1; co-absent with the target |

### Downstream of this gene

*140 arrows, 140 of them with an alert ⚠; grade A 0, B 27, C 113. Shown: the 12 strongest; 128 more arrows (128 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C4orf19]] | B | ATP10B activity raises C4orf19's level | lines that do not express ATP10B (40) vs lines expressing it (10) | 4.68× lower at baseline in the lines without ATP10B | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17 |
| [[PLEKHS1]] | B | ATP10B activity raises PLEKHS1's level | lines that do not express ATP10B (40) vs lines expressing it (10) | 4.17× lower at baseline in the lines without ATP10B | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17 |
| [[FUT2]] | B | ATP10B activity raises FUT2's level | lines that do not express ATP10B (40) vs lines expressing it (10) | 3.51× lower at baseline in the lines without ATP10B | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17 |
| [[TRIM2]] | B | ATP10B activity raises TRIM2's level | lines that do not express ATP10B (40) vs lines expressing it (10) | 6.48× lower at baseline in the lines without ATP10B | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17 |
| [[LINC00511]] | B | ATP10B activity raises LINC00511's level | lines that do not express ATP10B (40) vs lines expressing it (10) | 4.94× lower at baseline in the lines without ATP10B | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17 |
| [[ABHD11]] | B | ATP10B activity raises ABHD11's level | lines that do not express ATP10B (40) vs lines expressing it (10) | 2.78× lower at baseline in the lines without ATP10B | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17 |
| [[TNFRSF21]] | B | ATP10B activity raises TNFRSF21's level | lines that do not express ATP10B (40) vs lines expressing it (10) | 4.33× lower at baseline in the lines without ATP10B | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17 |
| [[DAB2IP]] | B | ATP10B activity raises DAB2IP's level | lines that do not express ATP10B (40) vs lines expressing it (10) | 2.20× lower at baseline in the lines without ATP10B | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17 |
| [[TSPAN3]] | B | ATP10B activity raises TSPAN3's level | lines that do not express ATP10B (40) vs lines expressing it (10) | 2.12× lower at baseline in the lines without ATP10B | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17 |
| [[ELF3-AS1]] | B | ATP10B activity raises ELF3-AS1's level | lines that do not express ATP10B (40) vs lines expressing it (10) | 2.96× lower at baseline in the lines without ATP10B | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17 |
| [[FZD5]] | B | ATP10B activity raises FZD5's level | lines that do not express ATP10B (40) vs lines expressing it (10) | 2.10× lower at baseline in the lines without ATP10B | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17 |
| [[MUC12]] | B | ATP10B activity raises MUC12's level | lines that do not express ATP10B (40) vs lines expressing it (10) | 2.70× lower at baseline in the lines without ATP10B | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17 |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.793). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.1, 52.1); signed map (62.5, 5.2). **Vector** length 71.2, 42.0% of its response variance represented; |z| ≥ 3 in 327 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Defective GALNT12 causes CRCS1* (reactome, mean cos +0.63 to 5); *Defective GALNT3 causes HFTC* (reactome, mean cos +0.63 to 5); *Defective C1GALT1C1 causes TNPS* (reactome, mean cos +0.63 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +8.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +6.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +3.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +7.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.5 | +6.9 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.7 | +1.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +2.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.3 | +2.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.3 | +4.7 |
| fall | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -2.5 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.2 | -1.3 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.2 | -0.5 |
|  | [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -1.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -2.3 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.1 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | ATPase phospholipid transporting 10B (putative) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q34 — chr5:160,563,120-160,852,214 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ATPVB, KIAA0715, FLJ21477 |
| Gene groups (HGNC) | ATPase phospholipid transporting |
| Reactome | 3 pathways, smallest: Ion transport by P-type ATPases; Ion channel transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [O94823](https://www.uniprot.org/uniprotkb/O94823) (Phospholipid-transporting ATPase VB):

> Catalytic component of a P4-ATPase flippase complex, which catalyzes the hydrolysis of ATP coupled to the transport of glucosylceramide (GlcCer) from the outer to the inner leaflet of lysosome membranes. Plays an important role in the maintenance of lysosome membrane integrity and function in cortical neurons.

**Summary**, from NCBI Gene [23120](https://www.ncbi.nlm.nih.gov/gene/23120):

> Enables glycosylceramide flippase activity and phosphatidylcholine flippase activity. Involved in lysosomal membrane organization. Located in endoplasmic reticulum; late endosome membrane; and lysosomal membrane. Part of phospholipid-translocating ATPase complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13543](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13543) · Entrez [23120](https://www.ncbi.nlm.nih.gov/gene/23120) · UniProt [O94823](https://www.uniprot.org/uniprotkb/O94823) · Ensembl [ENSG00000118322](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118322)

## Data

Gene col 3982: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3982); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3982, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3982]; `tensor/DDL_lfc|DDL_z.npy` [3982]; `embed/gene_vectors.npy` [3982]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3982 or target_col == 3982). Every well: [[ATP10B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP10B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
