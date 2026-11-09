---
symbol: "FXYD3"
type: "gene"
col: 1587
ensembl_id: "ENSG00000089356"
name: "FXYD domain containing ion transport regulator 3"
location: "19q13.12"
module: 44
arm: "+"
pooled_cpm: 8.69
n_lines_expressing: 16
n_dd_up: 6
n_dd_down: 5
n_dd_up_clean: 2
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 109
direction_downstream: 109
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# FXYD3

*FXYD domain containing ion transport regulator 3* — 19q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.26× (z +11.3, q 7e-27, up in 9 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Entrectinib (drug)]] 5 µM: 1.68× (z +3.5, q 0.046, up in 8 of 14 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H1573 15.2×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.525× (z -4.2, q 0.014, down in 10 of 14 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRR15]] (+0.81, fdr 7e-06), [[TSPAN1]] (+0.81, fdr 7e-06), [[TSPAN8]] (+0.80, fdr 7e-06).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 109 arrows point to it, the strongest [[FUT2]] → it (grade B ⚠); 109 go from it, the strongest it → [[FUT2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1587.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H1573 15.2×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.26×** | +11.3 | 7e-27 | 9/12 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.07×** | +9.2 | 1e-17 | 6/9 (LS 180, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.10×** | +4.7 | 5e-04 | 3/11 (NCI-H1573, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.82×** | +4.1 | 0.007 | 4/12 (SW1417, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Entrectinib (drug)]] 5 µM |  | **1.68×** | +3.5 | 0.046 | 8/14 (KATO III, LS 180, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +3.4 | 0.076 | 3/14 (AsPC-1, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.59× | +3.0 | 0.17 | 3/13 (NCI-H2347, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1587.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.525×** | -4.2 | 0.014 | 10/14 (LoVo, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.583×** | -3.7 | 0.062 | 12/14 (Hs 766T, LoVo, …) | inconsistent across doses |  |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.566×** | -3.6 | 0.062 | 2/14 (Panc 03.27, AsPC-1) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.605×** | -3.4 | 0.086 | 9/14 (LoVo, COLO 205, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM |  | **0.611×** | -3.4 | 0.091 | 12/14 (LoVo, COLO 205, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.620× | -3.3 | 0.10 | 5/14 (LoVo, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.628× | -3.2 | 0.12 | 10/13 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.637× | -3.1 | 0.14 | 6/14 (LoVo, C32, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 0.728× | -3.1 | 0.14 | 4/14 (NCI-H2347, LS 180, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1587. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 63.4 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -14.0) |
| [[LoVo (line)]] | wt | 65.0 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0527× (z -23.8) |
| [[BT-474 (line)]] | alt | 28.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -14.5) |
| [[COLO 205 (line)]] | alt | 12.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0623× (z -13.7) |
| [[LS 180 (line)]] | wt | 75.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -14.9) |
| [[Hs 766T (line)]] | wt | 14.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0857× (z -14.5) |
| [[HT-29 (line)]] | alt | 13.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -12.7) |
| [[NCI-H1573 (line)]] | alt | 9.66 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 15.2× (z +10.3) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 6.65 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0931× (z -14.9) |
| [[Panc 03.27 (line)]] | alt | 8.17 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0836× (z -12.7) |
| [[A-172 (line)]] | wt | 0.744 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.602 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.620 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.615 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.787 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.863 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.713 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.745 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.689 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.920 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.608 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.899 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.563 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.564 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.656 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.639 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.661 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.863 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.560 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.702 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.931 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.628 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.803 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.882 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.757 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.799 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.57 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.07 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1587), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRR15]] | +0.81 | +0.80 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[TSPAN1]] | +0.81 | +0.77 / +0.76 | both halves | 7e-06 | STRING 420 |
| [[TSPAN8]] | +0.80 | +0.79 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[PPP1R1B]] | +0.79 | +0.81 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[UGT1A1]] | +0.78 | +0.80 / +0.70 | both halves | 7e-06 |  |
| [[PRR15L]] | +0.78 | +0.79 / +0.67 | both halves | 7e-06 | STRING 488 |
| [[CLDN3]] | +0.77 | +0.74 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[MUC5B]] | +0.77 | +0.73 / +0.68 | both halves | 7e-06 | same gene group |
| [[LGALS4]] | +0.77 | +0.77 / +0.71 | both halves | 7e-06 |  |
| [[ST6GALNAC1]] | +0.76 | +0.76 / +0.69 | both halves | 7e-06 |  |
| [[MUC3A]] | +0.74 | +0.78 / +0.67 | both halves | 7e-06 |  |
| [[FAM3D]] | +0.72 | +0.67 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*109 arrows, 109 of them with an alert ⚠; grade A 0, B 5, C 104. Shown: the 12 strongest; 97 more arrows (97 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FUT2]] | B | FUT2 activity raises FXYD3's level | lines that do not express FUT2 (12) vs lines expressing it (38) | 2.68× lower at baseline in the lines without FUT2 | 0.023 | ⚠ within organs, on part of the lines; also absent: EFNB2, SH3TC1, PTPRE; maybe low, not absent |
| [[PLAAT4]] | B | PLAAT4 activity raises FXYD3's level | lines that do not express PLAAT4 (21) vs lines expressing it (29) | 2.12× lower at baseline in the lines without PLAAT4 | 0.045 | ⚠ within organs, on part of the lines; also absent: PTPRB, TNFSF10, EPSTI1 |
| [[MMP28]] | B | MMP28 activity raises FXYD3's level | lines that do not express MMP28 (27) vs lines expressing it (23) | 1.49× lower at baseline in the lines without MMP28 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000285743, LINC02582, LINP1; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises FXYD3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[GNA14]] | B | GNA14 activity raises FXYD3's level | lines that do not express GNA14 (5) vs lines expressing it (45) | 2.24× lower at baseline in the lines without GNA14 | 0.078 | ⚠ within organs, on part of the lines; also absent: SSUH2, EXT1, SAMSN1; maybe low, not absent |
| [[ST6GALNAC1]] | C | ST6GALNAC1 activity raises FXYD3's level | lines that do not express ST6GALNAC1 (37) vs lines expressing it (13) | 5.83× lower at baseline in the lines without ST6GALNAC1 | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, SLC44A4, STEAP4; co-absent with the target |
| [[PLA2G2A]] | C | PLA2G2A activity raises FXYD3's level | lines that do not express PLA2G2A (41) vs lines expressing it (9) | 7.98× lower at baseline in the lines without PLA2G2A | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, CALB1; co-absent with the target |
| [[CEACAM6]] | C | CEACAM6 activity raises FXYD3's level | lines that do not express CEACAM6 (37) vs lines expressing it (13) | 7.14× lower at baseline in the lines without CEACAM6 | 7e-04 | ⚠ within organs, on part of the lines; also absent: DAPP1, TMPRSS2, CDH17; co-absent with the target |
| [[MUC2]] | C | MUC2 activity raises FXYD3's level | lines that do not express MUC2 (42) vs lines expressing it (8) | 7.96× lower at baseline in the lines without MUC2 | 8e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, DSG4; co-absent with the target |
| [[TMPRSS2]] | C | TMPRSS2 activity raises FXYD3's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 6.38× lower at baseline in the lines without TMPRSS2 | 8e-04 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6; co-absent with the target |
| [[CYP4F12]] | C | CYP4F12 activity raises FXYD3's level | lines that do not express CYP4F12 (32) vs lines expressing it (18) | 4.76× lower at baseline in the lines without CYP4F12 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD3, CDH17, MUC13; co-absent with the target |
| [[TMEM30B]] | C | TMEM30B activity raises FXYD3's level | lines that do not express TMEM30B (35) vs lines expressing it (15) | 6.35× lower at baseline in the lines without TMEM30B | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ANKRD22, RAB25; co-absent with the target |

### Downstream of this gene

*109 arrows, 109 of them with an alert ⚠; grade A 0, B 20, C 89. Shown: the 12 strongest; 97 more arrows (97 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FUT2]] | B | FXYD3 activity raises FUT2's level | lines that do not express FXYD3 (34) vs lines expressing it (16) | 2.86× lower at baseline in the lines without FXYD3 | 0.004 | ⚠ within organs, on part of the lines; also absent: CEACAM6, TMEM30B, TMPRSS2 |
| [[MANSC1]] | B | FXYD3 activity raises MANSC1's level | lines that do not express FXYD3 (34) vs lines expressing it (16) | 2.76× lower at baseline in the lines without FXYD3 | 0.007 | ⚠ within organs, on part of the lines; also absent: CEACAM6, TMEM30B, TMPRSS2 |
| [[CMTM3]] | B | FXYD3 activity lowers CMTM3's level | lines that do not express FXYD3 (34) vs lines expressing it (16) | 2.83× higher at baseline in the lines without FXYD3 | 0.011 | ⚠ within organs, on part of the lines; also absent: CEACAM6, TMEM30B, TMPRSS2 |
| [[TNFRSF14]] | B | FXYD3 activity raises TNFRSF14's level | lines that do not express FXYD3 (34) vs lines expressing it (16) | 2.53× lower at baseline in the lines without FXYD3 | 0.013 | ⚠ within organs, on part of the lines; also absent: CEACAM6, TMEM30B, TMPRSS2 |
| [[PROM2]] | B | FXYD3 activity raises PROM2's level | lines that do not express FXYD3 (34) vs lines expressing it (16) | 2.66× lower at baseline in the lines without FXYD3 | 0.013 | ⚠ within organs, on part of the lines; also absent: CEACAM6, TMEM30B, TMPRSS2 |
| [[CTSH]] | B | FXYD3 activity raises CTSH's level | lines that do not express FXYD3 (34) vs lines expressing it (16) | 1.92× lower at baseline in the lines without FXYD3 | 0.029 | ⚠ within organs, on part of the lines; also absent: CEACAM6, TMEM30B, TMPRSS2 |
| [[RHBDL2]] | B | FXYD3 activity raises RHBDL2's level | lines that do not express FXYD3 (34) vs lines expressing it (16) | 1.87× lower at baseline in the lines without FXYD3 | 0.030 | ⚠ within organs, on part of the lines; also absent: CEACAM6, TMEM30B, TMPRSS2 |
| [[ELMO3]] | B | FXYD3 activity raises ELMO3's level | lines that do not express FXYD3 (34) vs lines expressing it (16) | 2.28× lower at baseline in the lines without FXYD3 | 0.033 | ⚠ within organs, on part of the lines; also absent: CEACAM6, TMEM30B, TMPRSS2 |
| [[CDC42EP5]] | B | FXYD3 activity raises CDC42EP5's level | lines that do not express FXYD3 (34) vs lines expressing it (16) | 1.86× lower at baseline in the lines without FXYD3 | 0.036 | ⚠ within organs, on part of the lines; also absent: CEACAM6, TMEM30B, TMPRSS2 |
| [[RSPH1]] | B | FXYD3 activity raises RSPH1's level | lines that do not express FXYD3 (34) vs lines expressing it (16) | 2.13× lower at baseline in the lines without FXYD3 | 0.037 | ⚠ within organs, on part of the lines; also absent: CEACAM6, TMEM30B, TMPRSS2 |
| [[ASS1]] | B | FXYD3 activity raises ASS1's level | lines that do not express FXYD3 (34) vs lines expressing it (16) | 3.41× lower at baseline in the lines without FXYD3 | 0.042 | ⚠ within organs, on part of the lines; also absent: CEACAM6, TMEM30B, TMPRSS2 |
| cells under [[Minodronic acid (drug)]] 0.5 µM | B | FXYD3 activity lowers the cells' numbers under Minodronic acid 0.5 µM (makes them more sensitive) | lines that do not express FXYD3 (34) vs lines expressing it (14) | the lines without FXYD3: 1.20× the cells of the other lines | 0.043 | ⚠ within organs, on part of the lines; also absent: CEACAM6, TMEM30B, TMPRSS2 |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.837). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.3, 51.7); signed map (63.6, 5.3). **Vector** length 60.2, 26.3% of its response variance represented; |z| ≥ 3 in 305 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Defective GALNT12 causes CRCS1* (reactome, mean cos +0.63 to 5); *Defective GALNT3 causes HFTC* (reactome, mean cos +0.63 to 5); *Defective C1GALT1C1 causes TNPS* (reactome, mean cos +0.63 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.9 | +4.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.8 | +9.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.5 | +2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +1.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.8 | +1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +1.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.7 | +1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.6 | +3.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.4 | -3.7 |
|  | [[EX229 (drug)]] 5 µM |  | -1.2 | -1.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.2 | -1.7 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.1 | -1.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.1 | -0.8 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.1 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | FXYD domain containing ion transport regulator 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.12 — chr19:35,115,823-35,124,324 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MAT-8; previously PLML |
| Gene groups (HGNC) | MicroRNA protein coding host genes; FXYD domain containing ion transport regulators |
| Reactome | 9 pathways, smallest: Ion homeostasis; Ion transport by P-type ATPases; Potential therapeutics for SARS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14802](https://www.uniprot.org/uniprotkb/Q14802) (FXYD domain-containing ion transport regulator 3):

> Associates with and regulates the activity of the sodium/potassium-transporting ATPase (NKA) which transports Na(+) out of the cell and K(+) into the cell. Reduces glutathionylation of the NKA beta-1 subunit ATP1B1, thus reversing glutathionylation-mediated inhibition of ATP1B1. Induces a hyperpolarization-activated chloride current when expressed in Xenopus oocytes.; [Isoform 1]: Decreases the apparent K+ and Na+ affinity of the sodium/potassium-transporting ATPase over a large range of …

**Summary**, from NCBI Gene [5349](https://www.ncbi.nlm.nih.gov/gene/5349):

> This gene belongs to a small family of FXYD-domain containing regulators of Na+/K+ ATPases which share a 35-amino acid signature sequence domain, beginning with the sequence PFXYD, and containing 7 invariant and 6 highly conserved amino acids. This gene encodes a cell membrane protein that may regulate the function of ion-pumps and ion-channels. This gene may also play a role in tumor progression. Alternative splicing results in multiple transcript variants encoding distinct isoforms.[provided …

**Accessions** — [HGNC:4027](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4027) · Entrez [5349](https://www.ncbi.nlm.nih.gov/gene/5349) · UniProt [Q14802](https://www.uniprot.org/uniprotkb/Q14802) · Ensembl [ENSG00000089356](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000089356)

## Data

Gene col 1587: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1587); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1587, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1587]; `tensor/DDL_lfc|DDL_z.npy` [1587]; `embed/gene_vectors.npy` [1587]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1587 or target_col == 1587). Every well: [[FXYD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FXYD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
