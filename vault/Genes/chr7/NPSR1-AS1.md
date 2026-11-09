---
symbol: "NPSR1-AS1"
type: "gene"
col: 12339
ensembl_id: "ENSG00000197085"
name: "NPSR1 antisense RNA 1"
location: "7p14.3"
module: 55
arm: "+"
pooled_cpm: 31.75
n_lines_expressing: 16
n_dd_up: 18
n_dd_down: 3
n_dd_up_clean: 13
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 74
direction_downstream: 87
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# NPSR1-AS1

*NPSR1 antisense RNA 1* — 7p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.64× (z +15.7, q 0e+00, up in 4 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 0.5 µM: 0.683× (z -4.3, q 0.008, down in 8 of 12 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NPSR1]] (+0.75, fdr 7e-06, ⚠ same locus), [[MYO7B]] (+0.74, fdr 7e-06), [[C9orf152]] (+0.74, fdr 7e-06), [[LINC02331]] (+0.74, fdr 7e-06).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 74 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 87 go from it, the strongest it → [[NOSTRIN]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12339.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.64×** | +15.7 | 0e+00 | 4/14 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.80×** | +11.8 | 2e-29 | 5/12 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.83×** | +9.8 | 3e-20 | 1/13 (NCI-H460) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.09×** | +8.4 | 5e-15 | 7/13 (NCI-H460, SW1417, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.15×** | +8.4 | 6e-15 | 3/11 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.59×** | +7.5 | 7e-12 | 7/14 (NCI-H460, KATO III, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.91×** | +7.3 | 2e-11 | 4/14 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +6.9 | 3e-10 | 1/12 (NCI-H460) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.77×** | +6.5 | 4e-09 | 3/13 (CFPAC-1, SW480, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.75×** | +5.9 | 2e-07 | 1/11 (NCI-H460) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +5.2 | 1e-05 | 4/12 (NCI-H460, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.49×** | +4.4 | 5e-04 | 0/12 | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.39×** | +3.8 | 0.007 | 7/13 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.5 | 0.019 | 5/14 (SW480, KATO III, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.34×** | +3.3 | 0.032 | 4/13 (HepG2/C3A, SW1417, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.34×** | +3.2 | 0.048 | 6/13 (HepG2/C3A, SW480, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.32×** | +3.1 | 0.055 | 0/13 | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12339.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 0.5 µM |  | **0.683×** | -4.3 | 0.008 | 8/12 (SW480, LoVo, …) | two highest doses | cell-cycle shift (explains ~4% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.714×** | -3.7 | 0.066 | 10/12 (LS 180, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.734×** | -3.5 | 0.084 | 10/13 (LoVo, LS 180, …) | two highest doses | cell-cycle shift (explains ~19% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.925× | -3.1 | 0.27 | 0/14 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12339. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 348 | 0 | 18 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0725× (z -24.9) |
| [[COLO 205 (line)]] | alt | 633 | 0 | 14 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0442× (z -28.0) |
| [[LoVo (line)]] | wt | 128 | 0 | 9 (7 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.100× (z -15.7) |
| [[KATO III (line)]] | alt | 82.7 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -17.5) |
| [[NCI-H460 (line)]] | wt | 10.2 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.1× (z +22.9) | — |
| [[HepG2_C3A (line)]] | wt | 88.3 | 2 (2 ⚠) | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 6.02× (z +11.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.126× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 59.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -10.2) |
| [[HEC-1-A (line)]] | alt | 53.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -10.0) |
| [[A-172 (line)]] | wt | 5.98 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 4.27 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 5.20 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 5.46 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.32 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 6.29 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.68 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.40 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.99 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.66 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 6.09 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.32 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.58 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.22 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.63 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 6.58 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.29 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.19 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.70 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.72 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.61 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 5.07 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.96 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 4.73 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.46 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.60 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.75 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.52 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.59 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.99 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.70 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.70 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 7.82 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.09 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 17.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12339), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPSR1]] | +0.75 | +0.75 / +0.73 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[MYO7B]] | +0.74 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[C9orf152]] | +0.74 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[LINC02331]] | +0.74 | +0.76 / +0.59 | both halves | 7e-06 |  |
| [[TPRXL]] | +0.71 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[HNF4A]] | +0.71 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[BMP4]] | +0.70 | +0.74 / +0.62 | both halves | 7e-06 |  |
| [[EPS8L3]] | +0.70 | +0.71 / +0.58 | both halves | 7e-06 |  |
| [[LINC01559]] | +0.70 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[LINC01819]] | +0.70 | +0.75 / +0.61 | both halves | 7e-06 |  |
| [[ABO]] | +0.69 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[LINC03040]] | +0.69 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[LINC02580]] | +0.68 | +0.64 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*74 arrows, 74 of them with an alert ⚠; grade A 0, B 2, C 72. Shown: the 12 strongest; 62 more arrows (62 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NPSR1-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HGD]] | B | HGD activity raises NPSR1-AS1's level | lines that do not express HGD (15) vs lines expressing it (35) | 2.42× lower at baseline in the lines without HGD | 0.074 | ⚠ within organs, on part of the lines; also absent: PCSK5, AQP3, FAAH2; maybe low, not absent |
| [[NPSR1]] | C | NPSR1 activity raises NPSR1-AS1's level | lines that do not express NPSR1 (42) vs lines expressing it (8) | 10.41× lower at baseline in the lines without NPSR1 | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, MUC17, CDH17; co-absent with the target |
| [[GCNT3]] | C | GCNT3 activity raises NPSR1-AS1's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 6.64× lower at baseline in the lines without GCNT3 | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13; co-absent with the target |
| [[CLRN3]] | C | CLRN3 activity raises NPSR1-AS1's level | lines that do not express CLRN3 (40) vs lines expressing it (10) | 7.93× lower at baseline in the lines without CLRN3 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13; co-absent with the target |
| [[CDH17]] | C | CDH17 activity raises NPSR1-AS1's level | lines that do not express CDH17 (40) vs lines expressing it (10) | 7.16× lower at baseline in the lines without CDH17 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, MUC13, CLRN3; co-absent with the target |
| [[MUC13]] | C | MUC13 activity raises NPSR1-AS1's level | lines that do not express MUC13 (40) vs lines expressing it (10) | 6.95× lower at baseline in the lines without MUC13 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, NPSR1, CDH17; co-absent with the target |
| [[LGALS4]] | C | LGALS4 activity raises NPSR1-AS1's level | lines that do not express LGALS4 (39) vs lines expressing it (11) | 7.13× lower at baseline in the lines without LGALS4 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13; maybe low, not absent; co-absent with the target |
| [[LINC02474]] | C | LINC02474 activity raises NPSR1-AS1's level | lines that do not express LINC02474 (40) vs lines expressing it (10) | 5.47× lower at baseline in the lines without LINC02474 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC4, SFTPA2, ENSG00000230975; co-absent with the target |
| [[LINC01559]] | C | LINC01559 activity raises NPSR1-AS1's level | lines that do not express LINC01559 (38) vs lines expressing it (12) | 5.59× lower at baseline in the lines without LINC01559 | 0.004 | ⚠ within organs, on part of the lines; also absent: CLRN3, NPSR1, CDH17; co-absent with the target |
| [[EPS8L3]] | C | EPS8L3 activity raises NPSR1-AS1's level | lines that do not express EPS8L3 (35) vs lines expressing it (15) | 6.09× lower at baseline in the lines without EPS8L3 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02964, EDAR, HNF4A; co-absent with the target |
| [[PCK1]] | C | PCK1 activity raises NPSR1-AS1's level | lines that do not express PCK1 (38) vs lines expressing it (12) | 5.00× lower at baseline in the lines without PCK1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LGR5, GPX2, CPLX2; co-absent with the target |

### Downstream of this gene

*87 arrows, 87 of them with an alert ⚠; grade A 0, B 14, C 73. Shown: the 12 strongest; 75 more arrows (75 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NOSTRIN]] | B | NPSR1-AS1 activity raises NOSTRIN's level | lines that do not express NPSR1-AS1 (34) vs lines expressing it (16) | 3.18× lower at baseline in the lines without NPSR1-AS1 | 0.006 | ⚠ within organs, on part of the lines; also absent: VIL1, A1CF, EPS8L3; maybe low, not absent |
| [[HGD]] | B | NPSR1-AS1 activity raises HGD's level | lines that do not express NPSR1-AS1 (34) vs lines expressing it (16) | 3.59× lower at baseline in the lines without NPSR1-AS1 | 0.007 | ⚠ within organs, on part of the lines; also absent: VIL1, A1CF, EPS8L3; maybe low, not absent |
| [[HNF4G]] | B | NPSR1-AS1 activity raises HNF4G's level | lines that do not express NPSR1-AS1 (34) vs lines expressing it (16) | 3.45× lower at baseline in the lines without NPSR1-AS1 | 0.019 | ⚠ within organs, on part of the lines; also absent: VIL1, A1CF, EPS8L3; maybe low, not absent |
| [[FZD5]] | B | NPSR1-AS1 activity raises FZD5's level | lines that do not express NPSR1-AS1 (34) vs lines expressing it (16) | 2.55× lower at baseline in the lines without NPSR1-AS1 | 0.020 | ⚠ within organs, on part of the lines; also absent: VIL1, A1CF, EPS8L3; maybe low, not absent |
| [[LINC02580]] | B | NPSR1-AS1 activity raises LINC02580's level | lines that do not express NPSR1-AS1 (34) vs lines expressing it (16) | 2.06× lower at baseline in the lines without NPSR1-AS1 | 0.022 | ⚠ within organs, on part of the lines; also absent: VIL1, A1CF, EPS8L3; maybe low, not absent |
| [[DNAJC15]] | B | NPSR1-AS1 activity raises DNAJC15's level | lines that do not express NPSR1-AS1 (34) vs lines expressing it (16) | 3.08× lower at baseline in the lines without NPSR1-AS1 | 0.024 | ⚠ within organs, on part of the lines; also absent: VIL1, A1CF, EPS8L3; maybe low, not absent |
| [[FUT2]] | B | NPSR1-AS1 activity raises FUT2's level | lines that do not express NPSR1-AS1 (34) vs lines expressing it (16) | 2.17× lower at baseline in the lines without NPSR1-AS1 | 0.032 | ⚠ within organs, on part of the lines; also absent: VIL1, A1CF, EPS8L3; maybe low, not absent |
| [[VILL]] | B | NPSR1-AS1 activity raises VILL's level | lines that do not express NPSR1-AS1 (34) vs lines expressing it (16) | 2.29× lower at baseline in the lines without NPSR1-AS1 | 0.038 | ⚠ within organs, on part of the lines; also absent: VIL1, A1CF, EPS8L3; maybe low, not absent |
| [[MUC12]] | B | NPSR1-AS1 activity raises MUC12's level | lines that do not express NPSR1-AS1 (34) vs lines expressing it (16) | 2.19× lower at baseline in the lines without NPSR1-AS1 | 0.042 | ⚠ within organs, on part of the lines; also absent: VIL1, A1CF, EPS8L3; maybe low, not absent |
| [[SLC44A3]] | B | NPSR1-AS1 activity raises SLC44A3's level | lines that do not express NPSR1-AS1 (34) vs lines expressing it (16) | 2.39× lower at baseline in the lines without NPSR1-AS1 | 0.060 | ⚠ within organs, on part of the lines; also absent: VIL1, A1CF, EPS8L3; maybe low, not absent |
| [[ZNF503-AS1]] | B | NPSR1-AS1 activity raises ZNF503-AS1's level | lines that do not express NPSR1-AS1 (34) vs lines expressing it (16) | 2.17× lower at baseline in the lines without NPSR1-AS1 | 0.087 | ⚠ within organs, on part of the lines; also absent: VIL1, A1CF, EPS8L3; maybe low, not absent |
| [[PSD4]] | B | NPSR1-AS1 activity raises PSD4's level | lines that do not express NPSR1-AS1 (34) vs lines expressing it (16) | 2.37× lower at baseline in the lines without NPSR1-AS1 | 0.096 | ⚠ within organs, on part of the lines; also absent: VIL1, A1CF, EPS8L3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.781). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.8, 49.2); signed map (63.3, 8.5). **Vector** length 65.6, 25.8% of its response variance represented; |z| ≥ 3 in 372 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +7.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +11.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.7 | +5.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +8.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +3.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.7 | +1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.7 | +2.7 |
| fall | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -1.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -1.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.1 | -1.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.0 | -1.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.0 | -1.9 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -0.9 | -1.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -0.9 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | NPSR1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 7p14.3 — chr7:34,346,512-34,871,582 (-) |
| Ensembl biotype | lncRNA |
| Also known as | AAA1, IMAGE:4827585 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [404744](https://www.ncbi.nlm.nih.gov/gene/404744):

> This gene is located within a region that has been associated with asthma susceptibility. The locus is considered non-protein-coding based on lack of protein homology and a lack of experimental support for an encoded protein. Three alternatively spliced transcript variants have been identified for this gene. [provided by RefSeq, May 2010]

**Accessions** — [HGNC:22128](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22128) · Entrez [404744](https://www.ncbi.nlm.nih.gov/gene/404744) · Ensembl [ENSG00000197085](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197085)

## Data

Gene col 12339: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12339); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12339, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12339]; `tensor/DDL_lfc|DDL_z.npy` [12339]; `embed/gene_vectors.npy` [12339]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12339 or target_col == 12339). Every well: [[NPSR1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NPSR1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
