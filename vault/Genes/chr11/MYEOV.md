---
symbol: "MYEOV"
type: "gene"
col: 10316
ensembl_id: "ENSG00000172927"
name: "myeloma overexpressed"
location: "11q13.3"
module: 141
arm: "+"
pooled_cpm: 32.5
n_lines_expressing: 31
n_dd_up: 0
n_dd_down: 51
n_dd_up_clean: 0
n_dd_down_clean: 46
in_vector_space: true
direction_upstream: 28
direction_downstream: 21
tags: ["gene", "module/141"]
generated_by: "tahoemap"
---

# MYEOV

*myeloma overexpressed* — 11q13.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Harringtonine (drug)]] 5 µM in 1 line (PANC-1 4.97×; ⚠ cell-cycle shift, explains ~68% of this change).
> Pooled over the cell lines (median), lowered significantly by 51 drug-doses (5 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.187× (z -20.0, q 0e+00, down in 29 of 29 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TGFA]] (+0.77, fdr 7e-06), [[ETV4]] (+0.73, fdr 7e-06), [[FOSL1]] (+0.73, fdr 7e-06).
> It is in [[Module 141]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 28 arrows point to it, the strongest [[B3GNT3]] → it (grade B ⚠); 21 go from it, the strongest it → [[SEPTIN9]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10316.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Harringtonine (drug)]] 5 µM in 1 line (PANC-1 4.97×; ⚠ cell-cycle shift, explains ~68% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Filgotinib (drug)]] 5 µM |  | 1.32× | +3.1 | 0.96 | 11/29 (Panc 03.27, SW48, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 53 in all, 5 with an alert ⚠; shown: the 15 strongest. 51 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10316.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.187×** | -20.0 | 0e+00 | 29/29 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); noisy plate (z scaled); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.219×** | -16.7 | 0e+00 | 28/29 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **0.326×** | -15.7 | 0e+00 | 27/29 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.258×** | -14.9 | 0e+00 | 28/29 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.277×** | -14.7 | 0e+00 | 28/29 (NCI-H1573, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.334×** | -13.6 | 3e-40 | 29/29 (PANC-1, Panc 03.27, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.494×** | -11.4 | 5e-28 | 25/29 (HEC-1-A, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.354×** | -11.0 | 4e-26 | 26/29 (PANC-1, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.447×** | -10.9 | 5e-26 | 26/29 (PANC-1, Panc 03.27, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **0.505×** | -10.9 | 5e-26 | 26/29 (SK-MEL-2, Panc 03.27, …) | all doses, stronger at high dose | position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.414×** | -10.0 | 5e-22 | 22/29 (Panc 03.27, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.456×** | -8.5 | 1e-15 | 22/29 (PANC-1, HEC-1-A, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.262×** | -8.0 | 6e-14 | 22/29 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.496×** | -8.0 | 6e-14 | 23/29 (HT-29, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[RMC-6236 (drug)]] 5 µM |  | **0.263×** | -8.0 | 6e-14 | 25/29 (NCI-H1573, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10316. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 184 | 0 | 20 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.173× (z -20.6) |
| [[Panc 03.27 (line)]] | alt | 108 | 0 | 16 (1 ⚠) | — | [[Binimetinib (drug)]] 5 µM 0.122× (z -14.6) |
| [[LoVo (line)]] | wt | 51.6 | 0 | 14 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -16.7) |
| [[PANC-1 (line)]] | alt | 30.4 | 1 (1 ⚠) | 13 | [[Harringtonine (drug)]] 5 µM 4.97× (z +11.3) ⚠ cell-cycle shift, explains ~68% of this change | [[Binimetinib (drug)]] 5 µM 0.159× (z -14.6) |
| [[NCI-H1573 (line)]] | alt | 70.3 | 0 | 13 (3 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.0541× (z -24.2) |
| [[SW480 (line)]] | alt | 26.4 | 0 | 13 | — | [[Trametinib (drug)]] 0.5 µM 0.245× (z -13.0) |
| [[CFPAC-1 (line)]] | alt | 49.4 | 0 | 12 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.104× (z -16.5) |
| [[KATO III (line)]] | alt | 83.8 | 0 | 11 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.113× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.216× (z -14.8) |
| [[Hs 766T (line)]] | wt | 50.7 | 0 | 7 | — | [[Trametinib (drug)]] 5 µM 0.142× (z -12.1) |
| [[HT-29 (line)]] | alt | 114 | 0 | 7 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0658× (z -15.3) |
| [[SK-MEL-2 (line)]] | alt | 24.2 | 0 | 7 | — | [[Trametinib (drug)]] 5 µM 0.0465× (z -13.9) |
| [[SW1417 (line)]] | alt | 43.7 | 0 | 7 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.241× (z -12.7) |
| [[HOP62 (line)]] | alt | 35.8 | 0 | 6 | — | [[Trametinib (drug)]] 5 µM 0.121× (z -11.1) |
| [[LOX-IMVI (line)]] | wt | 33.7 | 0 | 6 | — | [[Trametinib (drug)]] 5 µM 0.143× (z -13.1) |
| [[NCI-H1792 (line)]] | alt | 20.3 | 0 | 6 (2 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.0850× (z -12.4) |
| [[SNU-1 (line)]] | wt | 96.2 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -16.5) |
| [[LS 180 (line)]] | wt | 35.3 | 0 | 5 | — | [[Cobimetinib (drug)]] 5 µM 0.141× (z -11.3) |
| [[AsPC-1 (line)]] | alt | 32.3 | 0 | 4 | — | [[Trametinib (drug)]] 5 µM 0.186× (z -11.7) |
| [[A-172 (line)]] | wt | 16.5 | 0 | 3 | — | [[Trametinib (drug)]] 5 µM 0.127× (z -10.4) |
| [[A498 (line)]] | wt | 19.7 | 0 | 3 | — | [[Binimetinib (drug)]] 5 µM 0.249× (z -10.0) |
| [[A549 (line)]] | wt | 36.7 | 0 | 2 | — | [[Cobimetinib (drug)]] 5 µM 0.0750× (z -14.3) |
| [[MIA PaCa-2 (line)]] | alt | 12.9 | 0 | 2 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.454× (z -11.2) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 5 µM 0.0626× (z -10.8) |
| [[SW 900 (line)]] | alt | 11.5 | 0 | 1 | — | [[Trametinib (drug)]] 0.5 µM 0.169× (z -10.4) |
| [[A-427 (line)]] | wt | 2.18 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.28 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.93 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 9.72 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.75 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.02 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.84 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.25 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.36 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.96 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.60 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 6.33 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.84 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.78 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 7.93 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.86 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.97 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.47 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.73 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 17.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10316), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TGFA]] | +0.77 | +0.76 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[ETV4]] | +0.73 | +0.74 / +0.70 | both halves | 7e-06 |  |
| [[FOSL1]] | +0.73 | +0.71 / +0.74 | both halves | 7e-06 |  |
| [[EPHA2]] | +0.72 | +0.68 / +0.77 | both halves | 7e-06 |  |
| [[RAPGEF3]] | +0.71 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[ITGB5]] | +0.70 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[ITGA6]] | +0.70 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[CCND1]] | +0.70 | +0.69 / +0.76 | both halves | 7e-06 | STRING 792 |
| [[LINC02320]] | +0.69 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[LINC00659]] | +0.66 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[SH3TC2]] | +0.66 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[MST1R]] | +0.66 | +0.61 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 21, C 7. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[B3GNT3]] | B | B3GNT3 activity raises MYEOV's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 3.34× lower at baseline in the lines without B3GNT3 | 0.007 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[KRT15]] | B | KRT15 activity raises MYEOV's level | lines that do not express KRT15 (15) vs lines expressing it (35) | 2.91× lower at baseline in the lines without KRT15 | 0.014 | ⚠ within organs, on part of the lines; also absent: MISP, PSORS1C1, ENSG00000266088 |
| [[GTF2IP7]] | B | GTF2IP7 activity raises MYEOV's level | lines that do not express GTF2IP7 (18) vs lines expressing it (32) | 2.42× lower at baseline in the lines without GTF2IP7 | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000290729, FRMD4B, TMEM92 |
| [[TOR4A]] | B | TOR4A activity raises MYEOV's level | lines that do not express TOR4A (14) vs lines expressing it (36) | 2.82× lower at baseline in the lines without TOR4A | 0.025 | ⚠ within organs, on part of the lines; also absent: PLEKHA6, CDCP1, C19orf33 |
| [[TINAGL1]] | B | TINAGL1 activity raises MYEOV's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 2.54× lower at baseline in the lines without TINAGL1 | 0.028 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19 |
| [[ITGA3]] | B | ITGA3 activity raises MYEOV's level | lines that do not express ITGA3 (10) vs lines expressing it (40) | 3.00× lower at baseline in the lines without ITGA3 | 0.032 | ⚠ within organs, on part of the lines; also absent: IL15, GBP2, CD82; maybe low, not absent |
| [[BCAR3]] | B | BCAR3 activity raises MYEOV's level | lines that do not express BCAR3 (9) vs lines expressing it (41) | 2.44× lower at baseline in the lines without BCAR3 | 0.038 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, CD59, C11orf91; maybe low, not absent |
| [[PLEK2]] | B | PLEK2 activity raises MYEOV's level | lines that do not express PLEK2 (17) vs lines expressing it (33) | 2.09× lower at baseline in the lines without PLEK2 | 0.050 | ⚠ within organs, on part of the lines; also absent: CDCP1, SAMD12, SDR16C5 |
| [[PADI1]] | B | PADI1 activity raises MYEOV's level | lines that do not express PADI1 (34) vs lines expressing it (16) | 2.51× lower at baseline in the lines without PADI1 | 0.050 | ⚠ within organs, on part of the lines; also absent: CLIC5, LINC01559, EPS8L3 |
| [[LAMA3]] | B | LAMA3 activity raises MYEOV's level | lines that do not express LAMA3 (22) vs lines expressing it (28) | 2.56× lower at baseline in the lines without LAMA3 | 0.057 | ⚠ within organs, on part of the lines; also absent: P2RY2, ELF3, MYO5B |
| [[HIVEP3]] | B | HIVEP3 activity raises MYEOV's level | lines that do not express HIVEP3 (7) vs lines expressing it (43) | 2.46× lower at baseline in the lines without HIVEP3 | 0.060 | ⚠ within organs, on part of the lines; also absent: CD82; maybe low, not absent |
| [[ST3GAL1]] | B | ST3GAL1 activity raises MYEOV's level | lines that do not express ST3GAL1 (11) vs lines expressing it (39) | 1.99× lower at baseline in the lines without ST3GAL1 | 0.069 | ⚠ within organs, on part of the lines; also absent: IL1RAP, FBXO32, PLSCR2 |

### Downstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 17, C 4. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEPTIN9]] | B | MYEOV activity raises SEPTIN9's level | lines that do not express MYEOV (19) vs lines expressing it (31) | 1.67× lower at baseline in the lines without MYEOV | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000260877, MALL, LAMC2 |
| [[TINAGL1]] | B | MYEOV activity raises TINAGL1's level | lines that do not express MYEOV (19) vs lines expressing it (31) | 3.21× lower at baseline in the lines without MYEOV | 0.017 | ⚠ within organs, on part of the lines; also absent: ENSG00000260877, MALL, LAMC2 |
| [[LAMA3]] | B | MYEOV activity raises LAMA3's level | lines that do not express MYEOV (19) vs lines expressing it (31) | 3.23× lower at baseline in the lines without MYEOV | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000260877, MALL, LAMC2 |
| [[EPHB6]] | B | MYEOV activity raises EPHB6's level | lines that do not express MYEOV (19) vs lines expressing it (31) | 2.27× lower at baseline in the lines without MYEOV | 0.040 | ⚠ within organs, on part of the lines; also absent: ENSG00000260877, MALL, LAMC2 |
| [[ITGA6]] | B | MYEOV activity raises ITGA6's level | lines that do not express MYEOV (19) vs lines expressing it (31) | 2.34× lower at baseline in the lines without MYEOV | 0.042 | ⚠ within organs, on part of the lines; also absent: ENSG00000260877, MALL, LAMC2 |
| [[ITGB5]] | B | MYEOV activity raises ITGB5's level | lines that do not express MYEOV (19) vs lines expressing it (31) | 1.28× lower at baseline in the lines without MYEOV | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000260877, MALL, LAMC2 |
| [[EHD1]] | B | MYEOV activity raises EHD1's level | lines that do not express MYEOV (19) vs lines expressing it (31) | 1.57× lower at baseline in the lines without MYEOV | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000260877, MALL, LAMC2 |
| [[DUSP5]] | B | MYEOV activity raises DUSP5's level | lines that do not express MYEOV (19) vs lines expressing it (31) | 1.82× lower at baseline in the lines without MYEOV | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000260877, MALL, LAMC2 |
| [[GPR35]] | B | MYEOV activity raises GPR35's level | lines that do not express MYEOV (19) vs lines expressing it (31) | 1.83× lower at baseline in the lines without MYEOV | 0.062 | ⚠ within organs, on part of the lines; also absent: ENSG00000260877, MALL, LAMC2 |
| [[ITGB4]] | B | MYEOV activity raises ITGB4's level | lines that do not express MYEOV (19) vs lines expressing it (31) | 3.14× lower at baseline in the lines without MYEOV | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000260877, MALL, LAMC2 |
| [[SHB]] | B | MYEOV activity raises SHB's level | lines that do not express MYEOV (19) vs lines expressing it (31) | 1.49× lower at baseline in the lines without MYEOV | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000260877, MALL, LAMC2 |
| [[KRT15]] | B | MYEOV activity raises KRT15's level | lines that do not express MYEOV (19) vs lines expressing it (31) | 2.32× lower at baseline in the lines without MYEOV | 0.075 | ⚠ within organs, on part of the lines; also absent: ENSG00000260877, MALL, LAMC2 |

## Where it sits

- **Module**: [[Module 141]] — TNF-alpha signaling via NF-kB; 33 genes; every member is in the + arm (projection on the module's main direction 0.801). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (41.9, 4.1); signed map (5.0, 40.1). **Vector** length 131, 40.8% of its response variance represented; |z| ≥ 3 in 1,147 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *TNF-alpha signaling via NF-kB* (hallmark, mean cos +0.52 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +2.6 | -6.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +1.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | +2.3 | +0.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.3 | -6.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.3 | -4.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.1 | +3.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.8 | +1.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +0.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +0.7 |
|  | [[Imiquimod (hydrochloride) (drug)]] 0.05 µM |  | +1.6 | +2.2 |
| fall | [[Trametinib (drug)]] 5 µM |  | -9.1 | -20.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -9.0 | -15.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -8.7 | -16.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | -8.0 | -13.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -7.9 | -14.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -7.7 | -14.7 |

## What is on record

|  |  |
|---|---|
| Name | myeloma overexpressed |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.3 — chr11:69,294,151-69,341,682 (+) |
| Ensembl biotype | protein_coding |
| Also known as | OCIM |
| Matched by | ensembl_id |

UniProt [Q96EZ4](https://www.uniprot.org/uniprotkb/Q96EZ4) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:7563](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7563) · Entrez [26579](https://www.ncbi.nlm.nih.gov/gene/26579) · UniProt [Q96EZ4](https://www.uniprot.org/uniprotkb/Q96EZ4) · Ensembl [ENSG00000172927](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172927)

## Data

Gene col 10316: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10316); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10316, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10316]; `tensor/DDL_lfc|DDL_z.npy` [10316]; `embed/gene_vectors.npy` [10316]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10316 or target_col == 10316). Every well: [[MYEOV — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYEOV.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
