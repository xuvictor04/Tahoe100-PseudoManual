---
symbol: "ACOXL"
type: "gene"
col: 7688
ensembl_id: "ENSG00000153093"
name: "acyl-CoA oxidase like"
location: "2q13"
module: 155
arm: "+"
pooled_cpm: 10.09
n_lines_expressing: 22
n_dd_up: 28
n_dd_down: 0
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 8
direction_downstream: 10
tags: ["gene", "module/155"]
generated_by: "tahoemap"
---

# ACOXL

*acyl-CoA oxidase like* — 2q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.38× (z +26.6, q 0e+00, up in 9 of 16 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 3 lines (LoVo 0.116×, PANC-1 0.127×, SW1417 0.210×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change); [[Homoharringtonine (drug)]] 5 µM in 3 lines (SW1417 0.327×, LoVo 0.376×, SW 900 0.209×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (LoVo 0.120×, SW1417 0.213×; ⚠ cell-cycle shift, explains ~41% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (Panc 03.27 0.274×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (PANC-1 0.205×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HES2]] (+0.54, fdr 4e-05), [[ANKRD29]] (+0.51, fdr 3e-05), [[UNC5A]] (+0.50, fdr 4e-05); moves opposite to [[ZNF714]] (-0.41, fdr 2e-04), [[NUP133]] (-0.39, fdr 2e-04), [[TCTN2]] (-0.39, fdr 1e-04).
> It is in [[Module 155]], a single-armed module (MyD88 deficiency (TLR2/4)).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[STK33]] → it (grade B ⚠); 10 go from it, the strongest it → [[ENDOD1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7688.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.38×** | +26.6 | 0e+00 | 9/16 (A-172, LS 180, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.69×** | +15.6 | 0e+00 | 4/17 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.47×** | +14.3 | 8e-44 | 13/19 (SW480, LS 180, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **3.11×** | +12.6 | 2e-34 | 8/18 (SK-MEL-2, A-427, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.87×** | +11.3 | 1e-27 | 2/9 (Panc 03.27, NCI-H2347) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.96×** | +11.2 | 4e-27 | 1/9 (NCI-H2347) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.47×** | +10.1 | 5e-22 | 3/14 (LS 180, A-172, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.17×** | +8.3 | 7e-15 | 5/18 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.08×** | +8.2 | 2e-14 | 15/18 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.55×** | +6.9 | 2e-10 | 4/19 (SK-MEL-2, COLO 205, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +6.2 | 3e-08 | 2/15 (HS-578T, A-172) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.71×** | +6.0 | 9e-08 | 12/19 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~9% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.68×** | +5.8 | 3e-07 | 10/19 (LS 180, PANC-1, …) | all doses, flat | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.54×** | +4.8 | 6e-05 | 9/19 (LS 180, PANC-1, …) | all doses, flat | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +4.8 | 7e-05 | 0/16 | top dose only | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.53×** | +4.8 | 7e-05 | 9/18 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +3.8 | 0.005 | 3/19 (SK-MEL-2, HT-29, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.40×** | +3.7 | 0.006 | 8/17 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.39×** | +3.7 | 0.006 | 3/17 (LS 180, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | **1.36×** | +3.3 | 0.028 | 4/19 (NCI-H2347, hTERT-HPNE, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7688.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 3 lines (LoVo 0.116×, PANC-1 0.127×, SW1417 0.210×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change); [[Homoharringtonine (drug)]] 5 µM in 3 lines (SW1417 0.327×, LoVo 0.376×, SW 900 0.209×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (LoVo 0.120×, SW1417 0.213×; ⚠ cell-cycle shift, explains ~41% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (Panc 03.27 0.274×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (PANC-1 0.205×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | 0.813× | -3.3 | 0.59 | 10/19 (PANC-1, Panc 03.27, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.765× | -3.0 | 0.63 | 2/19 (Panc 03.27, A-172) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7688. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 4.84 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 66.7× (z +18.3) | — |
| [[HS-578T (line)]] | alt | 2.92 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 33.3× (z +13.0) | — |
| [[LoVo (line)]] | wt | 51.5 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.116× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.376× (z -9.3) |
| [[PANC-1 (line)]] | alt | 13.5 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 0.05 µM 4.60× (z +8.6) | [[Digitoxin (drug)]] 5 µM 0.127× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.205× (z -9.1) |
| [[SW1417 (line)]] | alt | 28.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -9.5) |
| [[Panc 03.27 (line)]] | alt | 73.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -12.3) |
| [[SW 900 (line)]] | alt | 51.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -8.7) |
| [[hTERT-HPNE (line)]] | wt | 3.28 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.6× (z +11.5) | — |
| [[LS 180 (line)]] | wt | 4.55 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 7.69× (z +9.8) | — |
| [[SW480 (line)]] | alt | 14.6 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.69× (z +10.7) | — |
| [[A-427 (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.55 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.74 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.34 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.74 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.91 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.67 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.14 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.59 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.14 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.62 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.96 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7688), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HES2]] | +0.54 | +0.60 / +0.42 | both halves | 4e-05 |  |
| [[ANKRD29]] | +0.51 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[UNC5A]] | +0.50 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[PSEN2]] | +0.50 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[CDH3]] | +0.50 | +0.45 / +0.43 | both halves | 3e-05 |  |
| [[SCN1B]] | +0.49 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[STK33]] | +0.47 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[SKAP1]] | +0.47 | +0.40 / +0.43 | both halves | 5e-05 |  |
| [[ABLIM2]] | +0.47 | +0.41 / +0.49 | both halves | 4e-05 |  |
| [[LINC02832]] | +0.47 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[CCDC69]] | +0.46 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[SPTSSB]] | +0.46 | +0.43 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF714]] | -0.41 | -0.30 / -0.39 | both halves | 2e-04 |  |
| [[NUP133]] | -0.39 | -0.32 / -0.42 | both halves | 2e-04 |  |
| [[TCTN2]] | -0.39 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[PAAF1]] | -0.39 | -0.21 / -0.37 | both halves | 6e-04 |  |
| [[ZNF266]] | -0.38 | -0.32 / -0.34 | both halves | 2e-04 |  |
| [[MTERF1]] | -0.38 | -0.29 / -0.41 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 4, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STK33]] | B | STK33 activity raises ACOXL's level | lines that do not express STK33 (18) vs lines expressing it (32) | 2.28× lower at baseline in the lines without STK33 | 0.024 | ⚠ within organs, on part of the lines; also absent: SDK1, PGBD5, NID1; maybe low, not absent |
| [[GPR143]] | B | GPR143 activity raises ACOXL's level | lines that do not express GPR143 (19) vs lines expressing it (31) | 2.12× lower at baseline in the lines without GPR143 | 0.040 | ⚠ within organs, on part of the lines; also absent: SHROOM2, DCDC2, SCN5A; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers ACOXL's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HEYL]] | B | HEYL activity raises ACOXL's level | lines that do not express HEYL (25) vs lines expressing it (25) | 2.25× lower at baseline in the lines without HEYL | 0.060 | ⚠ within organs, on part of the lines; also absent: HCG11, GAL, LRRN2 |
| [[SLC5A1]] | C | SLC5A1 activity raises ACOXL's level | lines that do not express SLC5A1 (36) vs lines expressing it (14) | 3.58× lower at baseline in the lines without SLC5A1 | 0.016 | ⚠ within organs, on part of the lines; also absent: TMEM30B, TMPRSS2, TMEM125; co-absent with the target |
| [[ALOX5]] | C | ALOX5 activity raises ACOXL's level | lines that do not express ALOX5 (28) vs lines expressing it (22) | 2.45× lower at baseline in the lines without ALOX5 | 0.026 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ADGRF1, RASSF6; co-absent with the target |
| [[SKAP1]] | C | SKAP1 activity raises ACOXL's level | lines that do not express SKAP1 (34) vs lines expressing it (16) | 2.91× lower at baseline in the lines without SKAP1 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KCNE3, TMEM125, SLC5A1; co-absent with the target |
| [[B3GNT7]] | C | B3GNT7 activity raises ACOXL's level | lines that do not express B3GNT7 (31) vs lines expressing it (19) | 2.19× lower at baseline in the lines without B3GNT7 | 0.076 | ⚠ within organs, on part of the lines; also absent: KRT23, PROM1, HSD17B2; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 5, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ENDOD1]] | B | ACOXL activity raises ENDOD1's level | lines that do not express ACOXL (28) vs lines expressing it (22) | 1.64× lower at baseline in the lines without ACOXL | 0.019 | ⚠ within organs, on part of the lines; also absent: ILDR1, PRKCH-AS1, LRRN1; maybe low, not absent |
| [[STK33]] | B | ACOXL activity raises STK33's level | lines that do not express ACOXL (28) vs lines expressing it (22) | 1.88× lower at baseline in the lines without ACOXL | 0.033 | ⚠ within organs, on part of the lines; also absent: ILDR1, PRKCH-AS1, LRRN1; maybe low, not absent |
| [[PPM1H]] | B | ACOXL activity raises PPM1H's level | lines that do not express ACOXL (28) vs lines expressing it (22) | 1.51× lower at baseline in the lines without ACOXL | 0.058 | ⚠ within organs, on part of the lines; also absent: ILDR1, PRKCH-AS1, LRRN1; maybe low, not absent |
| [[PPL]] | B | ACOXL activity raises PPL's level | lines that do not express ACOXL (28) vs lines expressing it (22) | 2.06× lower at baseline in the lines without ACOXL | 0.092 | ⚠ within organs, on part of the lines; also absent: ILDR1, PRKCH-AS1, LRRN1; maybe low, not absent |
| [[HES2]] | B | ACOXL activity raises HES2's level | lines that do not express ACOXL (28) vs lines expressing it (22) | 1.77× lower at baseline in the lines without ACOXL | 0.0995 | ⚠ within organs, on part of the lines; also absent: ILDR1, PRKCH-AS1, LRRN1; maybe low, not absent |
| [[BSPRY]] | C | ACOXL activity raises BSPRY's level | lines that do not express ACOXL (28) vs lines expressing it (22) | 2.67× lower at baseline in the lines without ACOXL | 0.015 | ⚠ within organs, on part of the lines; also absent: ILDR1, PRKCH-AS1, LRRN1; maybe low, not absent; co-absent with the target |
| [[SLC5A1]] | C | ACOXL activity raises SLC5A1's level | lines that do not express ACOXL (28) vs lines expressing it (22) | 2.24× lower at baseline in the lines without ACOXL | 0.021 | ⚠ within organs, on part of the lines; also absent: ILDR1, PRKCH-AS1, LRRN1; maybe low, not absent; co-absent with the target |
| [[SKAP1]] | C | ACOXL activity raises SKAP1's level | lines that do not express ACOXL (28) vs lines expressing it (22) | 2.64× lower at baseline in the lines without ACOXL | 0.048 | ⚠ within organs, on part of the lines; also absent: ILDR1, PRKCH-AS1, LRRN1; maybe low, not absent; co-absent with the target |
| [[CBLC]] | C | ACOXL activity raises CBLC's level | lines that do not express ACOXL (28) vs lines expressing it (22) | 2.23× lower at baseline in the lines without ACOXL | 0.084 | ⚠ within organs, on part of the lines; also absent: ILDR1, PRKCH-AS1, LRRN1; maybe low, not absent; co-absent with the target |
| [[B3GNT7]] | C | ACOXL activity raises B3GNT7's level | lines that do not express ACOXL (28) vs lines expressing it (22) | 1.52× lower at baseline in the lines without ACOXL | 0.090 | ⚠ within organs, on part of the lines; also absent: ILDR1, PRKCH-AS1, LRRN1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 155]] — MyD88 deficiency (TLR2/4); 29 genes; every member is in the + arm (projection on the module's main direction 0.326). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (9.3, 46.6); signed map (20.2, 39.9). **Vector** length 49.6, 11.5% of its response variance represented; |z| ≥ 3 in 516 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +14.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.3 | +8.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.9 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.5 | +11.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.4 | +3.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.3 | +1.9 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.2 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +3.1 |
| fall | [[Selinexor (drug)]] 5 µM |  | -2.5 | -3.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -2.5 | +1.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.9 | -1.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.6 | -1.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | +0.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -2.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.1 | -0.6 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.1 | -1.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.0 | -0.0 |

## What is on record

|  |  |
|---|---|
| Name | acyl-CoA oxidase like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q13 — chr2:110,732,539-111,118,548 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11042, ACOX4 |
| Gene groups (HGNC) | Flavoproteins; Acyl-CoA oxidase family |
| Reactome | 4 pathways, smallest: Beta-oxidation of pristanoyl-CoA; Peroxisomal lipid metabolism; Fatty acid metabolism |
| Matched by | ensembl_id |

UniProt [Q9NUZ1](https://www.uniprot.org/uniprotkb/Q9NUZ1) carries no function annotation.

**Summary**, from NCBI Gene [55289](https://www.ncbi.nlm.nih.gov/gene/55289):

> Predicted to enable acyl-CoA oxidase activity; fatty acid binding activity; and flavin adenine dinucleotide binding activity. Predicted to be involved in fatty acid beta-oxidation using acyl-CoA oxidase. Located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25621](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25621) · Entrez [55289](https://www.ncbi.nlm.nih.gov/gene/55289) · UniProt [Q9NUZ1](https://www.uniprot.org/uniprotkb/Q9NUZ1) · Ensembl [ENSG00000153093](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153093)

## Data

Gene col 7688: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7688); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7688, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7688]; `tensor/DDL_lfc|DDL_z.npy` [7688]; `embed/gene_vectors.npy` [7688]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7688 or target_col == 7688). Every well: [[ACOXL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACOXL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
