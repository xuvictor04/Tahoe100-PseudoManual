---
symbol: "CATSPERB"
type: "gene"
col: 5491
ensembl_id: "ENSG00000133962"
name: "catsper channel auxiliary subunit beta"
location: "14q32.12"
module: 8
arm: "+"
pooled_cpm: 46.83
n_lines_expressing: 20
n_dd_up: 7
n_dd_down: 6
n_dd_up_clean: 3
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 150
direction_downstream: 160
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# CATSPERB

*catsper channel auxiliary subunit beta* — 14q32.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.46× (z +10.7, q 9e-24, up in 4 of 19 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.57× (z +7.5, q 7e-12, up in 6 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.667× (z -4.6, q 0.002, down in 15 of 18 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TC2N]] (+0.84, fdr 7e-06, ⚠ same locus), [[TMEM45B]] (+0.81, fdr 7e-06), [[ITGB6]] (+0.75, fdr 7e-06), [[GCNT3]] (+0.75, fdr 7e-06).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 150 arrows point to it, the strongest [[PLEKHS1]] → it (grade B ⚠); 160 go from it, the strongest it → [[LMO7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5491.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.46×** | +10.7 | 9e-24 | 4/19 (A549, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.07×** | +8.2 | 5e-14 | 3/16 (A549, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.00×** | +7.6 | 7e-12 | 3/17 (AsPC-1, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.57×** | +7.5 | 7e-12 | 6/18 (SW480, A549, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +5.4 | 8e-06 | 1/19 (A549) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.53×** | +5.0 | 4e-05 | 7/19 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +3.6 | 0.024 | 2/18 (LS 180, NCI-H460) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5491.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.667×** | -4.6 | 0.002 | 15/18 (COLO 205, BT-474, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.693×** | -4.4 | 0.002 | 11/18 (BT-474, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.693×** | -4.4 | 0.002 | 14/18 (NCI-H1573, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.782×** | -4.2 | 0.005 | 11/18 (LoVo, KATO III, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.581×** | -3.4 | 0.083 | 15/18 (BT-474, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Larotrectinib (drug)]] 5 µM |  | **0.824×** | -3.3 | 0.097 | 11/18 (LoVo, HT-29, …) | top dose only | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | 0.603× | -3.1 | 0.14 | 9/18 (HEC-1-A, LS 180, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5491. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 374 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0562× (z -25.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -11.7) |
| [[BT-474 (line)]] | alt | 769 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -15.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.219× (z -13.8) |
| [[KATO III (line)]] | alt | 154 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -18.2) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.204× (z -15.5) |
| [[HEC-1-A (line)]] | alt | 30.4 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -13.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.250× (z -10.3) |
| [[LoVo (line)]] | wt | 214 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -13.0) |
| [[HT-29 (line)]] | alt | 89.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -15.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -8.9) |
| [[LS 180 (line)]] | wt | 90.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -13.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.243× (z -9.8) |
| [[CFPAC-1 (line)]] | alt | 126 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -14.7) ⚠ cell-cycle shift, explains ~33% of this change |
| [[NCI-H1573 (line)]] | alt | 122 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -11.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.217× (z -10.4) |
| [[SW48 (line)]] | wt | 35.3 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.0918× (z -9.9) |
| [[A-172 (line)]] | wt | 4.34 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 8.63 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.45 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.85 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.82 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.33 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.93 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.73 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.48 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.19 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.11 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.82 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.67 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.48 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.16 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.97 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 6.01 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.89 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.18 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.23 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.04 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.27 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.80 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.36 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.90 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.17 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.73 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.94 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 5.52 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.1 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 19.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5491), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TC2N]] | +0.84 | +0.82 / +0.88 | both halves | 7e-06 | STRING 690; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[TMEM45B]] | +0.81 | +0.76 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[ITGB6]] | +0.75 | +0.74 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[GCNT3]] | +0.75 | +0.69 / +0.76 | both halves | 7e-06 |  |
| [[MUC5B]] | +0.75 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[CEACAM5]] | +0.74 | +0.74 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[TMC5]] | +0.73 | +0.67 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[SLC6A14]] | +0.72 | +0.69 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[SLC28A3]] | +0.72 | +0.70 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[TMPRSS4]] | +0.72 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[POF1B]] | +0.72 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[ST14]] | +0.71 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[SIDT1]] | +0.71 | +0.72 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*150 arrows, 150 of them with an alert ⚠; grade A 0, B 18, C 132. Shown: the 12 strongest; 138 more arrows (138 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEKHS1]] | B | PLEKHS1 activity raises CATSPERB's level | lines that do not express PLEKHS1 (15) vs lines expressing it (35) | 3.22× lower at baseline in the lines without PLEKHS1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000261227, CYP4F3, CRYM; maybe low, not absent |
| [[SLC44A3-AS1]] | B | SLC44A3-AS1 activity raises CATSPERB's level | lines that do not express SLC44A3-AS1 (13) vs lines expressing it (37) | 3.49× lower at baseline in the lines without SLC44A3-AS1 | 0.028 | ⚠ within organs, on part of the lines; also absent: SLC44A3, CRYBG2, ENSG00000287306; maybe low, not absent |
| [[NOSTRIN]] | B | NOSTRIN activity raises CATSPERB's level | lines that do not express NOSTRIN (16) vs lines expressing it (34) | 3.98× lower at baseline in the lines without NOSTRIN | 0.041 | ⚠ within organs, on part of the lines; also absent: SLC9A2, SLPI, SULT2B1; maybe low, not absent |
| [[MUC20]] | B | MUC20 activity raises CATSPERB's level | lines that do not express MUC20 (14) vs lines expressing it (36) | 3.10× lower at baseline in the lines without MUC20 | 0.045 | ⚠ within organs, on part of the lines; also absent: MUC12, PRAG1; maybe low, not absent |
| [[RNF220]] | B | RNF220 activity lowers CATSPERB's level | lines that do not express RNF220 (9) vs lines expressing it (41) | 2.90× higher at baseline in the lines without RNF220 | 0.046 | ⚠ within organs, on part of the lines; also absent: GNAZ, ENSG00000287400, CTXN1; maybe low, not absent |
| [[SPATA6L]] | B | SPATA6L activity raises CATSPERB's level | lines that do not express SPATA6L (15) vs lines expressing it (35) | 3.57× lower at baseline in the lines without SPATA6L | 0.046 | ⚠ within organs, on part of the lines; also absent: RHOV, ANO9, ELF3; maybe low, not absent |
| [[SRMS]] | B | SRMS activity raises CATSPERB's level | lines that do not express SRMS (14) vs lines expressing it (36) | 2.49× lower at baseline in the lines without SRMS | 0.048 | ⚠ within organs, on part of the lines; also absent: MX1, OAS2, RSAD2 |
| [[LMO7]] | B | LMO7 activity raises CATSPERB's level | lines that do not express LMO7 (11) vs lines expressing it (39) | 3.29× lower at baseline in the lines without LMO7 | 0.049 | ⚠ within organs, on part of the lines; also absent: LMO7DN, KITLG, TLE4; maybe low, not absent |
| [[LGALS9]] | B | LGALS9 activity raises CATSPERB's level | lines that do not express LGALS9 (13) vs lines expressing it (37) | 3.04× lower at baseline in the lines without LGALS9 | 0.057 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ATP8B1, CTSS; maybe low, not absent |
| [[BCAS1]] | B | BCAS1 activity weakens CATSPERB's drug response | lines that do not express BCAS1 (10) vs lines expressing it (9) | the lines without BCAS1 respond 46.98× as strongly (z diff -1.36); strongest at Idarubicin (hydrochloride) 5 µM: 0.71x vs 0.30x (z diff -5.0) | 0.068 | ⚠ within organs, on part of the lines; also absent: SLC6A14, AGR3, LYZ; target measured in part of the lines; both ways; artifact flags |
| [[C4orf19]] | B | C4orf19 activity raises CATSPERB's level | lines that do not express C4orf19 (13) vs lines expressing it (37) | 2.75× lower at baseline in the lines without C4orf19 | 0.071 | ⚠ within organs, on part of the lines; also absent: RASEF, ARHGEF35-AS1, LNX1; maybe low, not absent |
| [[ZNF503-AS1]] | B | ZNF503-AS1 activity raises CATSPERB's level | lines that do not express ZNF503-AS1 (20) vs lines expressing it (30) | 2.80× lower at baseline in the lines without ZNF503-AS1 | 0.075 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, LINC02147; maybe low, not absent |

### Downstream of this gene

*160 arrows, 160 of them with an alert ⚠; grade A 0, B 50, C 110. Shown: the 12 strongest; 148 more arrows (148 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LMO7]] | B | CATSPERB activity raises LMO7's level | lines that do not express CATSPERB (30) vs lines expressing it (20) | 4.32× lower at baseline in the lines without CATSPERB | 0.001 | ⚠ within organs, on part of the lines; also absent: SGPP2, TC2N, ST14 |
| [[SDCBP2]] | B | CATSPERB activity raises SDCBP2's level | lines that do not express CATSPERB (30) vs lines expressing it (20) | 4.17× lower at baseline in the lines without CATSPERB | 0.001 | ⚠ within organs, on part of the lines; also absent: SGPP2, TC2N, ST14 |
| [[ZNF25]] | B | CATSPERB activity lowers ZNF25's level | lines that do not express CATSPERB (30) vs lines expressing it (20) | 1.92× higher at baseline in the lines without CATSPERB | 0.002 | ⚠ within organs, on part of the lines; also absent: SGPP2, TC2N, ST14 |
| [[STS]] | B | CATSPERB activity raises STS's level | lines that do not express CATSPERB (30) vs lines expressing it (20) | 2.85× lower at baseline in the lines without CATSPERB | 0.003 | ⚠ within organs, on part of the lines; also absent: SGPP2, TC2N, ST14 |
| [[SLC44A3-AS1]] | B | CATSPERB activity raises SLC44A3-AS1's level | lines that do not express CATSPERB (30) vs lines expressing it (20) | 2.94× lower at baseline in the lines without CATSPERB | 0.003 | ⚠ within organs, on part of the lines; also absent: SGPP2, TC2N, ST14 |
| [[TMEM184A]] | B | CATSPERB activity raises TMEM184A's level | lines that do not express CATSPERB (30) vs lines expressing it (20) | 2.55× lower at baseline in the lines without CATSPERB | 0.004 | ⚠ within organs, on part of the lines; also absent: SGPP2, TC2N, ST14 |
| [[PLCH1]] | B | CATSPERB activity raises PLCH1's level | lines that do not express CATSPERB (30) vs lines expressing it (20) | 3.61× lower at baseline in the lines without CATSPERB | 0.006 | ⚠ within organs, on part of the lines; also absent: SGPP2, TC2N, ST14 |
| [[TNFRSF21]] | B | CATSPERB activity raises TNFRSF21's level | lines that do not express CATSPERB (30) vs lines expressing it (20) | 3.43× lower at baseline in the lines without CATSPERB | 0.006 | ⚠ within organs, on part of the lines; also absent: SGPP2, TC2N, ST14 |
| [[BAG1]] | B | CATSPERB activity raises BAG1's level | lines that do not express CATSPERB (30) vs lines expressing it (20) | 1.92× lower at baseline in the lines without CATSPERB | 0.006 | ⚠ within organs, on part of the lines; also absent: SGPP2, TC2N, ST14 |
| [[MUC20]] | B | CATSPERB activity raises MUC20's level | lines that do not express CATSPERB (30) vs lines expressing it (20) | 3.42× lower at baseline in the lines without CATSPERB | 0.008 | ⚠ within organs, on part of the lines; also absent: SGPP2, TC2N, ST14 |
| [[NT5C2]] | B | CATSPERB activity raises NT5C2's level | lines that do not express CATSPERB (30) vs lines expressing it (20) | 1.46× lower at baseline in the lines without CATSPERB | 0.008 | ⚠ within organs, on part of the lines; also absent: SGPP2, TC2N, ST14 |
| [[C3orf18]] | B | CATSPERB activity lowers C3orf18's level | lines that do not express CATSPERB (30) vs lines expressing it (20) | 1.48× higher at baseline in the lines without CATSPERB | 0.009 | ⚠ within organs, on part of the lines; also absent: SGPP2, TC2N, ST14 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.780). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.8, 55.8); signed map (59.7, 7.0). **Vector** length 88.0, 36.4% of its response variance represented; |z| ≥ 3 in 560 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Dectin-2 family* (reactome, mean cos +0.53 to 5); *O-linked glycosylation of mucins* (reactome, mean cos +0.55 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.9 | +7.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.4 | +10.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +8.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +7.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.6 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +2.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.9 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +2.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.7 | +0.8 |
| fall | [[Radotinib (drug)]] 5 µM |  | -2.6 | -4.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.0 | -2.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.9 | -1.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -1.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.7 | -1.8 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.6 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | catsper channel auxiliary subunit beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.12 — chr14:91,580,696-91,780,707 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14298; previously C14orf161 |
| Gene groups (HGNC) | CatSpermasome complex |
| Reactome | 3 pathways, smallest: Sperm Motility And Taxes; Fertilization; Reproduction |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H7T0](https://www.uniprot.org/uniprotkb/Q9H7T0) (Cation channel sperm-associated auxiliary subunit beta):

> Auxiliary component of the CatSper complex, a complex involved in sperm cell hyperactivation. Sperm cell hyperactivation is needed for sperm motility which is essential late in the preparation of sperm for fertilization.

**Summary**, from NCBI Gene [79820](https://www.ncbi.nlm.nih.gov/gene/79820):

> Predicted to be involved in flagellated sperm motility and sperm capacitation. Predicted to be located in sperm principal piece. Predicted to be part of CatSper complex. Predicted to be active in cilium. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20500](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20500) · Entrez [79820](https://www.ncbi.nlm.nih.gov/gene/79820) · UniProt [Q9H7T0](https://www.uniprot.org/uniprotkb/Q9H7T0) · Ensembl [ENSG00000133962](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133962)

## Data

Gene col 5491: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5491); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5491, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5491]; `tensor/DDL_lfc|DDL_z.npy` [5491]; `embed/gene_vectors.npy` [5491]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5491 or target_col == 5491). Every well: [[CATSPERB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CATSPERB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
