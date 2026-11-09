---
symbol: "HR"
type: "gene"
col: 9653
ensembl_id: "ENSG00000168453"
name: "HR lysine demethylase and nuclear receptor corepressor"
location: "8p21.3"
module: 55
arm: "+"
pooled_cpm: 4.89
n_lines_expressing: 27
n_dd_up: 4
n_dd_down: 10
n_dd_up_clean: 1
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 16
direction_downstream: 35
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# HR

*HR lysine demethylase and nuclear receptor corepressor* — 8p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.22× (z +7.8, q 3e-12, up in 2 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.67× (z +5.1, q 6e-05, up in 11 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.457× (z -5.5, q 1e-05, down in 14 of 23 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01819]] (+0.70, fdr 7e-06), [[CTSE]] (+0.67, fdr 7e-06), [[SLC52A3]] (+0.67, fdr 7e-06); moves opposite to [[FAU]] (-0.48, fdr 5e-05), [[PRKRIP1]] (-0.47, fdr 4e-05).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[GDA]] → it (grade B ⚠); 35 go from it, the strongest it → [[ITPK1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9653.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.22×** | +7.8 | 3e-12 | 2/5 (SW1417, SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.81×** | +6.7 | 8e-09 | 3/7 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.15×** | +5.3 | 2e-05 | 5/10 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.67×** | +5.1 | 6e-05 | 11/24 (LS 180, Hs 766T, …) | rises with dose | position effect removed |
| [[Omeprazole (drug)]] 0.05 µM |  | 1.60× | +3.2 | 0.13 | 6/24 (COLO 205, SK-MEL-2, …) | inconsistent across doses | position effect removed |
| [[Mifepristone (drug)]] 0.5 µM |  | 1.56× | +3.1 | 0.18 | 9/23 (LS 180, KATO III, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9653.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.457×** | -5.5 | 1e-05 | 14/23 (CHP-212, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.460×** | -5.5 | 1e-05 | 17/23 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.504×** | -4.8 | 3e-04 | 16/23 (LoVo, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.511×** | -4.7 | 3e-04 | 12/23 (SK-MEL-2, NCI-H460, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.552×** | -4.2 | 0.003 | 14/22 (LS 180, LoVo, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.670×** | -4.0 | 0.006 | 12/24 (SK-MEL-2, KATO III, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.575×** | -3.9 | 0.007 | 15/22 (LoVo, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.576×** | -3.9 | 0.007 | 14/23 (NCI-H460, SW480, …) | two highest doses | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.631×** | -3.2 | 0.076 | 9/23 (LoVo, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.639×** | -3.1 | 0.093 | 6/24 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.647× | -3.1 | 0.11 | 7/23 (A-172, SW480, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9653. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 14.7 | 0 | 7 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0331× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0393× (z -14.0) |
| [[NCI-H460 (line)]] | wt | 39.6 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0524× (z -14.2) |
| [[SW480 (line)]] | alt | 7.00 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.0809× (z -11.0) |
| [[CHP-212 (line)]] | wt | 13.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0384× (z -8.7) |
| [[LS 180 (line)]] | wt | 5.59 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0534× (z -9.9) |
| [[SW1417 (line)]] | alt | 8.25 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.0506× (z -11.0) |
| [[A-172 (line)]] | wt | 9.60 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.315 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.287 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.946 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.474 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.719 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.396 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.586 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.493 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.615 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.583 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.575 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.724 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.637 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.390 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.451 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.823 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.809 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.405 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.426 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.877 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.759 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 11.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9653), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01819]] | +0.70 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[CTSE]] | +0.67 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[SLC52A3]] | +0.67 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[AFAP1L2]] | +0.66 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[KCNH8]] | +0.65 | +0.63 / +0.57 | both halves | 9e-06 |  |
| [[LAD1]] | +0.65 | +0.71 / +0.50 | both halves | 1e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[GPX2]] | +0.64 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[EDAR]] | +0.63 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[TPRXL]] | +0.62 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[CAPN8]] | +0.62 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[LGR6]] | +0.62 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[KLK6]] | +0.61 | +0.57 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAU]] | -0.48 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[PRKRIP1]] | -0.47 | -0.42 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 5, C 11. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GDA]] | B | GDA activity raises HR's level | lines that do not express GDA (35) vs lines expressing it (15) | 1.78× lower at baseline in the lines without GDA | 0.079 | ⚠ within organs, on part of the lines; also absent: HHLA2, GPA33, LGALS4 |
| [[MISP]] | B | MISP activity raises HR's level | lines that do not express MISP (23) vs lines expressing it (27) | 1.69× lower at baseline in the lines without MISP | 0.084 | ⚠ within organs, on part of the lines; also absent: GRB7, KRT18, MYO5B |
| [[MMP28]] | B | MMP28 activity raises HR's level | lines that do not express MMP28 (27) vs lines expressing it (23) | 1.59× lower at baseline in the lines without MMP28 | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000285743, LINC02582, LINP1; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises HR's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MYO16-AS1]] | B | MYO16-AS1 activity raises HR's level | lines that do not express MYO16-AS1 (23) vs lines expressing it (27) | 1.52× lower at baseline in the lines without MYO16-AS1 | 0.097 | ⚠ within organs, on part of the lines; also absent: ENSG00000275216, KRT18, LAMC2 |
| [[LINC01819]] | C | LINC01819 activity raises HR's level | lines that do not express LINC01819 (29) vs lines expressing it (21) | 1.99× lower at baseline in the lines without LINC01819 | 0.011 | ⚠ within organs, on part of the lines; also absent: MOGAT3, LGR6, A1CF; maybe low, not absent; co-absent with the target |
| [[MYOM3]] | C | MYOM3 activity raises HR's level | lines that do not express MYOM3 (27) vs lines expressing it (23) | 2.15× lower at baseline in the lines without MYOM3 | 0.011 | ⚠ within organs, on part of the lines; also absent: HNF4A, EPS8L3, USH1C; co-absent with the target |
| [[INPP5D]] | C | INPP5D activity raises HR's level | lines that do not express INPP5D (34) vs lines expressing it (16) | 2.56× lower at baseline in the lines without INPP5D | 0.025 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A, TP53; also absent: CLRN3, LINC02964, LGR5; co-absent with the target |
| [[ZNF736P9Y]] | C | ZNF736P9Y activity raises HR's level | lines that do not express ZNF736P9Y (40) vs lines expressing it (10) | 2.19× lower at baseline in the lines without ZNF736P9Y | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SPINK13, SUCNR1, ENSG00000260364; co-absent with the target |
| [[EDAR]] | C | EDAR activity raises HR's level | lines that do not express EDAR (36) vs lines expressing it (14) | 2.08× lower at baseline in the lines without EDAR | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, KLK10, DSG3; co-absent with the target |
| [[SPON1]] | C | SPON1 activity raises HR's level | lines that do not express SPON1 (39) vs lines expressing it (11) | 1.96× lower at baseline in the lines without SPON1 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALB1, DSG4, KRT6A; co-absent with the target |
| [[ANO1]] | C | ANO1 activity raises HR's level | lines that do not express ANO1 (30) vs lines expressing it (20) | 1.61× lower at baseline in the lines without ANO1 | 0.079 | ⚠ within organs, on part of the lines; also absent: COL17A1, CLIC5, TMPRSS2; co-absent with the target |

### Downstream of this gene

*35 arrows, 35 of them with an alert ⚠; grade A 0, B 13, C 22. Shown: the 12 strongest; 23 more arrows (23 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITPK1]] | B | HR activity raises ITPK1's level | lines that do not express HR (23) vs lines expressing it (27) | 2.03× lower at baseline in the lines without HR | 0.007 | ⚠ within organs, on part of the lines; also absent: SULF2, CEACAM1, HNF1A-AS1 |
| [[PLCD3]] | B | HR activity raises PLCD3's level | lines that do not express HR (23) vs lines expressing it (27) | 1.68× lower at baseline in the lines without HR | 0.021 | ⚠ within organs, on part of the lines; also absent: SULF2, CEACAM1, HNF1A-AS1 |
| [[DLG3]] | B | HR activity raises DLG3's level | lines that do not express HR (23) vs lines expressing it (27) | 2.04× lower at baseline in the lines without HR | 0.030 | ⚠ within organs, on part of the lines; also absent: SULF2, CEACAM1, HNF1A-AS1 |
| [[CYP3A5]] | B | HR activity raises CYP3A5's level | lines that do not express HR (23) vs lines expressing it (27) | 2.66× lower at baseline in the lines without HR | 0.032 | ⚠ within organs, on part of the lines; also absent: SULF2, CEACAM1, HNF1A-AS1 |
| [[ZNF860]] | B | HR activity raises ZNF860's level | lines that do not express HR (23) vs lines expressing it (27) | 1.63× lower at baseline in the lines without HR | 0.033 | ⚠ within organs, on part of the lines; also absent: SULF2, CEACAM1, HNF1A-AS1 |
| [[MISP]] | B | HR activity raises MISP's level | lines that do not express HR (23) vs lines expressing it (27) | 2.83× lower at baseline in the lines without HR | 0.043 | ⚠ within organs, on part of the lines; also absent: SULF2, CEACAM1, HNF1A-AS1 |
| [[SLC9A3]] | B | HR activity raises SLC9A3's level | lines that do not express HR (23) vs lines expressing it (27) | 1.73× lower at baseline in the lines without HR | 0.054 | ⚠ within organs, on part of the lines; also absent: SULF2, CEACAM1, HNF1A-AS1 |
| [[SLC12A2]] | B | HR activity raises SLC12A2's level | lines that do not express HR (23) vs lines expressing it (27) | 1.87× lower at baseline in the lines without HR | 0.070 | ⚠ within organs, on part of the lines; also absent: SULF2, CEACAM1, HNF1A-AS1 |
| [[ABHD11]] | B | HR activity raises ABHD11's level | lines that do not express HR (23) vs lines expressing it (27) | 1.68× lower at baseline in the lines without HR | 0.074 | ⚠ within organs, on part of the lines; also absent: SULF2, CEACAM1, HNF1A-AS1 |
| [[SLC52A3]] | B | HR activity raises SLC52A3's level | lines that do not express HR (23) vs lines expressing it (27) | 2.21× lower at baseline in the lines without HR | 0.078 | ⚠ within organs, on part of the lines; also absent: SULF2, CEACAM1, HNF1A-AS1 |
| [[RPH3AL]] | B | HR activity raises RPH3AL's level | lines that do not express HR (23) vs lines expressing it (27) | 1.80× lower at baseline in the lines without HR | 0.079 | ⚠ within organs, on part of the lines; also absent: SULF2, CEACAM1, HNF1A-AS1 |
| cells under [[Topotecan (hydrochloride) (drug)]] 0.5 µM | B | HR activity lowers the cells' numbers under Topotecan (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express HR (23) vs lines expressing it (25) | the lines without HR: 1.01× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: SULF2, CEACAM1, HNF1A-AS1 |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.644). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (18.4, 49.0); signed map (65.7, 10.3). **Vector** length 56.3, 13.2% of its response variance represented; |z| ≥ 3 in 657 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +5.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.7 | +6.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +5.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +1.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.7 | +3.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.4 | +1.3 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.9 | -3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.8 | -4.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.5 | -3.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -2.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.5 | -5.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.5 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -0.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.3 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | HR lysine demethylase and nuclear receptor corepressor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.3 — chr8:22,114,419-22,133,384 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KDM3D, AU; previously ALUNC |
| Gene groups (HGNC) | Lysine demethylase 3 family |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Matched by | ensembl_id |

**Function**, from UniProt [O43593](https://www.uniprot.org/uniprotkb/O43593) (Lysine-specific demethylase hairless):

> Histone demethylase that specifically demethylates both mono- and dimethylated 'Lys-9' of histone H3. May act as a transcription regulator controlling hair biology (via targeting of collagens), neural activity, and cell cycle.

**Summary**, from NCBI Gene [55806](https://www.ncbi.nlm.nih.gov/gene/55806):

> This gene encodes a protein that is involved in hair growth. This protein functions as a transcriptional corepressor of multiple nuclear receptors, including thyroid hormone receptor, the retinoic acid receptor-related orphan receptors and the vitamin D receptors, and it interacts with histone deacetylases. The translation of this protein is modulated by a regulatory open reading frame (ORF) that exists upstream of the primary ORF. Mutations in this upstream ORF cause Marie Unna hereditary …

**Accessions** — [HGNC:5172](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5172) · Entrez [55806](https://www.ncbi.nlm.nih.gov/gene/55806) · UniProt [O43593](https://www.uniprot.org/uniprotkb/O43593) · Ensembl [ENSG00000168453](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168453)

## Data

Gene col 9653: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9653); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9653, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9653]; `tensor/DDL_lfc|DDL_z.npy` [9653]; `embed/gene_vectors.npy` [9653]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9653 or target_col == 9653). Every well: [[HR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
