---
symbol: "GNA14"
type: "gene"
col: 7944
ensembl_id: "ENSG00000156049"
name: "G protein subunit alpha 14"
location: "9q21.2"
module: 44
arm: "+"
pooled_cpm: 3.82
n_lines_expressing: 45
n_dd_up: 12
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 7
direction_downstream: 18
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# GNA14

*G protein subunit alpha 14* — 9q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.16× (z +9.8, q 5e-20, up in 11 of 26 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (HT-29 0.00814×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (HT-29 0.0654×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (HT-29 0.0626×; ⚠ cell-cycle shift, explains ~51% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HT-29 0.172×); [[Auranofin (drug)]] 5 µM in 1 line (HT-29 0.0903×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UGT1A9]] (+0.73, fdr 7e-06), [[CRACDL]] (+0.69, fdr 7e-06), [[UGT1A1]] (+0.67, fdr 7e-06); moves opposite to [[SEMA4F]] (-0.51, fdr 2e-04).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[AGR3]] → it (grade B ⚠); 18 go from it, the strongest it → [[FBXW10B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7944.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.16×** | +9.8 | 5e-20 | 11/26 (A-172, A549, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.11×** | +9.5 | 4e-19 | 14/29 (NCI-H2030, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.98×** | +9.5 | 5e-19 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.67×** | +8.2 | 3e-14 | 1/6 (Hs 766T) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.40×** | +7.9 | 3e-13 | 3/11 (HS-578T, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.76×** | +7.2 | 4e-11 | 8/38 (A498, BT-474, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +4.7 | 2e-04 | 2/19 (HEC-1-A, A498) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.57×** | +4.1 | 0.003 | 6/37 (CFPAC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.53×** | +3.8 | 0.008 | 4/30 (HOP62, A-172, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.49×** | +3.5 | 0.028 | 4/28 (COLO 205, J82, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.03×** | +3.3 | 0.043 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.45×** | +3.2 | 0.060 | 1/14 (LoVo) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7944.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (HT-29 0.00814×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (HT-29 0.0654×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (HT-29 0.0626×; ⚠ cell-cycle shift, explains ~51% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HT-29 0.172×); [[Auranofin (drug)]] 5 µM in 1 line (HT-29 0.0903×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 0.5 µM |  | 0.703× | -3.2 | 0.85 | 6/39 (SK-MEL-2, HCT15, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7944. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 76.2 | 0 | 12 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.00814× (z -23.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.0654× (z -18.5) |
| [[A498 (line)]] | wt | 2.81 | 0 | 1 | — | [[Phenytoin (sodium) (drug)]] 0.05 µM 0.0675× (z -8.8) |
| [[A549 (line)]] | wt | 1.25 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.6× (z +9.0) | — |
| [[HEC-1-A (line)]] | alt | 3.08 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.99× (z +9.4) | — |
| [[NCI-H2030 (line)]] | alt | 1.11 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.6× (z +9.7) | — |
| [[A-172 (line)]] | wt | 1.23 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.655 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.966 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.700 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.973 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.885 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.879 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.11 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.928 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7944), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UGT1A9]] | +0.73 | +0.64 / +0.74 | both halves | 7e-06 |  |
| [[CRACDL]] | +0.69 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[UGT1A1]] | +0.67 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[UGT1A8]] | +0.66 | +0.58 / +0.65 | both halves | 8e-06 |  |
| [[PLCH1]] | +0.65 | +0.57 / +0.65 | both halves | 9e-06 |  |
| [[CFTR]] | +0.65 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[TM4SF4]] | +0.65 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[LINC02580]] | +0.64 | +0.71 / +0.55 | both halves | 1e-05 |  |
| [[STK31]] | +0.64 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[UGT1A6]] | +0.64 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[MGAM2]] | +0.64 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[HNF1A-AS1]] | +0.64 | +0.59 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEMA4F]] | -0.51 | -0.52 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AGR3]] | B | AGR3 activity raises GNA14's level | lines that do not express AGR3 (42) vs lines expressing it (8) | 2.85× lower at baseline in the lines without AGR3 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17 |
| [[TM4SF4]] | B | TM4SF4 activity raises GNA14's level | lines that do not express TM4SF4 (42) vs lines expressing it (8) | 2.26× lower at baseline in the lines without TM4SF4 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PIGR, MUC17, HHLA2 |
| [[ST6GALNAC1]] | B | ST6GALNAC1 activity raises GNA14's level | lines that do not express ST6GALNAC1 (37) vs lines expressing it (13) | 1.93× lower at baseline in the lines without ST6GALNAC1 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, SLC44A4, STEAP4 |
| [[FAM3D]] | B | FAM3D activity raises GNA14's level | lines that do not express FAM3D (43) vs lines expressing it (7) | 2.65× lower at baseline in the lines without FAM3D | 0.070 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, ENSG00000230975, NPSR1; maybe low, not absent |
| [[PRKCH-AS1]] | B | PRKCH-AS1 activity raises GNA14's level | lines that do not express PRKCH-AS1 (34) vs lines expressing it (16) | 1.93× lower at baseline in the lines without PRKCH-AS1 | 0.070 | ⚠ within organs, on part of the lines; also absent: SLC5A1, TMEM30B, TMPRSS2; maybe low, not absent |
| [[GABRP]] | B | GABRP activity raises GNA14's level | lines that do not express GABRP (44) vs lines expressing it (6) | 2.12× lower at baseline in the lines without GABRP | 0.086 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT20, FGFR2, SLC34A2 |
| [[FAM3B]] | B | FAM3B activity raises GNA14's level | lines that do not express FAM3B (12) vs lines expressing it (38) | 1.40× lower at baseline in the lines without FAM3B | 0.088 | ⚠ within organs, on part of the lines; also absent: TXNIP, CADPS2, PLAC4; maybe low, not absent |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 18, C 0. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FBXW10B]] | B | GNA14 activity raises FBXW10B's level | lines that do not express GNA14 (5) vs lines expressing it (45) | 2.40× lower at baseline in the lines without GNA14 | 0.027 | ⚠ within organs, on part of the lines; also absent: SSUH2, EXT1, SAMSN1; maybe low, not absent |
| [[FBXO17]] | B | GNA14 activity lowers FBXO17's level | lines that do not express GNA14 (5) vs lines expressing it (45) | 2.99× higher at baseline in the lines without GNA14 | 0.028 | ⚠ within organs, on part of the lines; also absent: SSUH2, EXT1, SAMSN1; maybe low, not absent |
| [[MOB3B]] | B | GNA14 activity raises MOB3B's level | lines that do not express GNA14 (5) vs lines expressing it (45) | 2.50× lower at baseline in the lines without GNA14 | 0.028 | ⚠ within organs, on part of the lines; also absent: SSUH2, EXT1, SAMSN1; maybe low, not absent |
| [[PTPRB]] | B | GNA14 activity raises PTPRB's level | lines that do not express GNA14 (5) vs lines expressing it (45) | 4.92× lower at baseline in the lines without GNA14 | 0.032 | ⚠ within organs, on part of the lines; also absent: SSUH2, EXT1, SAMSN1; maybe low, not absent |
| [[GRHL2]] | B | GNA14 activity raises GRHL2's level | lines that do not express GNA14 (5) vs lines expressing it (45) | 3.69× lower at baseline in the lines without GNA14 | 0.044 | ⚠ within organs, on part of the lines; also absent: SSUH2, EXT1, SAMSN1; maybe low, not absent |
| [[BAG1]] | B | GNA14 activity raises BAG1's level | lines that do not express GNA14 (5) vs lines expressing it (45) | 1.37× lower at baseline in the lines without GNA14 | 0.061 | ⚠ within organs, on part of the lines; also absent: SSUH2, EXT1, SAMSN1; maybe low, not absent |
| [[PRR15]] | B | GNA14 activity raises PRR15's level | lines that do not express GNA14 (5) vs lines expressing it (45) | 1.88× lower at baseline in the lines without GNA14 | 0.069 | ⚠ within organs, on part of the lines; also absent: SSUH2, EXT1, SAMSN1; maybe low, not absent |
| [[TNFSF15]] | B | GNA14 activity raises TNFSF15's level | lines that do not express GNA14 (5) vs lines expressing it (45) | 2.03× lower at baseline in the lines without GNA14 | 0.074 | ⚠ within organs, on part of the lines; also absent: SSUH2, EXT1, SAMSN1; maybe low, not absent |
| cells under [[Homoharringtonine (drug)]] 0.05 µM | B | GNA14 activity raises the cells' numbers under Homoharringtonine 0.05 µM (protects the cells) | lines that do not express GNA14 (5) vs lines expressing it (43) | the lines without GNA14: 0.69× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: SSUH2, EXT1, SAMSN1; maybe low, not absent |
| [[ABO]] | B | GNA14 activity raises ABO's level | lines that do not express GNA14 (5) vs lines expressing it (45) | 1.44× lower at baseline in the lines without GNA14 | 0.077 | ⚠ within organs, on part of the lines; also absent: SSUH2, EXT1, SAMSN1; maybe low, not absent |
| [[FXYD3]] | B | GNA14 activity raises FXYD3's level | lines that do not express GNA14 (5) vs lines expressing it (45) | 2.24× lower at baseline in the lines without GNA14 | 0.078 | ⚠ within organs, on part of the lines; also absent: SSUH2, EXT1, SAMSN1; maybe low, not absent |
| cells under [[Harringtonine (drug)]] 0.5 µM | B | GNA14 activity raises the cells' numbers under Harringtonine 0.5 µM (protects the cells) | lines that do not express GNA14 (5) vs lines expressing it (43) | the lines without GNA14: 0.50× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: SSUH2, EXT1, SAMSN1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.627). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.5, 50.9); signed map (63.0, 2.3). **Vector** length 51.1, 7.37% of its response variance represented; |z| ≥ 3 in 950 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Glucuronidation* (reactome, mean cos +0.68 to 4); *Aspirin ADME* (reactome, mean cos +0.68 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.7 | +9.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +8.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +9.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +9.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.4 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +3.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.7 | +2.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.4 | +1.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.1 | +0.2 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | -1.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | +0.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.2 | -1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.2 | -1.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.0 | -1.4 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -1.0 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | G protein subunit alpha 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.2 — chr9:77,423,079-77,648,322 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | G protein subunits alpha, group q |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING |
| Reactome | 22 pathways, smallest: Fatty Acids bound to GPR40 (FFAR1) regulate insulin secretion; Acetylcholine regulates insulin secretion; Free fatty acids regulate insulin secretion |
| Matched by | ensembl_id |

**Function**, from UniProt [O95837](https://www.uniprot.org/uniprotkb/O95837) (Guanine nucleotide-binding protein subunit alpha-14):

> Guanine nucleotide-binding proteins (G proteins) are involved as modulators or transducers in various transmembrane signaling systems.

**Summary**, from NCBI Gene [9630](https://www.ncbi.nlm.nih.gov/gene/9630):

> This gene encodes a member of the guanine nucleotide-binding, or G protein family. G proteins are heterotrimers consisting of alpha, beta and gamma subunits. The encoded protein is a member of the alpha family of G proteins, more specifically the alpha q subfamily of G proteins. The encoded protein may play a role in pertussis-toxin resistant activation of phospholipase C-beta and its downstream effectors.[provided by RefSeq, Feb 2009]

**Accessions** — [HGNC:4382](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4382) · Entrez [9630](https://www.ncbi.nlm.nih.gov/gene/9630) · UniProt [O95837](https://www.uniprot.org/uniprotkb/O95837) · Ensembl [ENSG00000156049](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156049)

## Data

Gene col 7944: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7944); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7944, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7944]; `tensor/DDL_lfc|DDL_z.npy` [7944]; `embed/gene_vectors.npy` [7944]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7944 or target_col == 7944). Every well: [[GNA14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GNA14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
