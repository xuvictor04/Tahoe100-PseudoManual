---
symbol: "CDHR2"
type: "gene"
col: 1075
ensembl_id: "ENSG00000074276"
name: "cadherin related family member 2"
location: "5q35.2"
module: 8
arm: "+"
pooled_cpm: 9.35
n_lines_expressing: 20
n_dd_up: 19
n_dd_down: 1
n_dd_up_clean: 13
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 43
direction_downstream: 65
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# CDHR2

*cadherin related family member 2* — 5q35.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 7.28× (z +29.1, q 0e+00, up in 11 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.603× (z -5.3, q 8e-05, down in 9 of 15 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (HT-29 0.0860×); [[Homoharringtonine (drug)]] 5 µM in 1 line (COLO 205 0.286×); [[Panobinostat (drug)]] 0.5 µM in 1 line (COLO 205 0.172×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ixazomib citrate (drug)]] 5 µM in 1 line (A-427 0.0649×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01559]] (+0.66, fdr 1e-05), [[LINC02580]] (+0.63, fdr 1e-05), [[TMPRSS2]] (+0.62, fdr 1e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 43 arrows point to it, the strongest [[VNN1]] → it (grade B ⚠); 65 go from it, the strongest it → [[KPNA7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1075.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **7.28×** | +29.1 | 0e+00 | 11/14 (HEC-1-A, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.82×** | +10.3 | 1e-22 | 1/7 (LS 180) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.65×** | +10.1 | 1e-21 | 1/11 (LoVo) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.65×** | +9.3 | 1e-18 | 1/8 (LoVo) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.83×** | +8.9 | 9e-17 | 2/13 (AsPC-1, LoVo) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.11×** | +7.5 | 8e-12 | 2/12 (HEC-1-A, LoVo) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.03×** | +7.4 | 1e-11 | 3/15 (HEC-1-A, SW480, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.67×** | +5.1 | 2e-05 | 8/15 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +4.6 | 2e-04 | 3/16 (KATO III, HepG2/C3A, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +4.4 | 7e-04 | 2/13 (SW48, LoVo) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.46×** | +3.9 | 0.004 | 8/15 (HepG2/C3A, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.44×** | +3.8 | 0.008 | 0/16 | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.43×** | +3.7 | 0.009 | 7/15 (LS 180, SW48, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Thymol (drug)]] 0.5 µM |  | **1.42×** | +3.7 | 0.011 | 1/13 (NCI-H1573) | inconsistent across doses | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.91×** | +3.5 | 0.017 | 0/5 | top dose only | noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 0.05 µM |  | **1.38×** | +3.3 | 0.028 | 3/15 (CFPAC-1, COLO 205, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.30×** | +3.1 | 0.062 | 5/16 (AsPC-1, SW480, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1075.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (HT-29 0.0860×); [[Homoharringtonine (drug)]] 5 µM in 1 line (COLO 205 0.286×); [[Panobinostat (drug)]] 0.5 µM in 1 line (COLO 205 0.172×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ixazomib citrate (drug)]] 5 µM in 1 line (A-427 0.0649×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.603×** | -5.3 | 8e-05 | 9/15 (NCI-H1573, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~16% here); position effect removed |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | 0.719× | -3.2 | 0.43 | 0/16 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1075. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 176 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -8.7) |
| [[LoVo (line)]] | wt | 7.34 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.36× (z +11.5) | — |
| [[A-427 (line)]] | wt | 3.06 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0649× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 108 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +9.8) | — |
| [[HEC-1-A (line)]] | alt | 3.66 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.7× (z +13.1) | — |
| [[HT-29 (line)]] | alt | 7.60 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0860× (z -8.7) |
| [[A-172 (line)]] | wt | 1.74 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.74 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.79 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 102 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.05 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.31 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.32 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.85 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1075), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01559]] | +0.66 | +0.71 / +0.54 | both halves | 1e-05 |  |
| [[LINC02580]] | +0.63 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[TMPRSS2]] | +0.62 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[MUC20]] | +0.60 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[IGFL2-AS1]] | +0.59 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[SLC44A4]] | +0.59 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[EPS8L1]] | +0.59 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[ST14]] | +0.59 | +0.66 / +0.48 | both halves | 2e-05 |  |
| [[TRIM31]] | +0.58 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[TTC39A]] | +0.57 | +0.58 / +0.41 | both halves | 4e-05 |  |
| [[PIP5K1B]] | +0.57 | +0.65 / +0.44 | both halves | 3e-05 |  |
| [[FUT2]] | +0.57 | +0.66 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*43 arrows, 43 of them with an alert ⚠; grade A 0, B 1, C 42. Shown: the 12 strongest; 31 more arrows (31 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VNN1]] | B | VNN1 activity raises CDHR2's level | lines that do not express VNN1 (27) vs lines expressing it (23) | 1.96× lower at baseline in the lines without VNN1 | 0.085 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ENSG00000259925, MUC5B |
| [[GCNT3]] | C | GCNT3 activity raises CDHR2's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 6.44× lower at baseline in the lines without GCNT3 | 8e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13; co-absent with the target |
| [[CDH17]] | C | CDH17 activity raises CDHR2's level | lines that do not express CDH17 (40) vs lines expressing it (10) | 5.85× lower at baseline in the lines without CDH17 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, MUC13, CLRN3; co-absent with the target |
| [[MUC13]] | C | MUC13 activity raises CDHR2's level | lines that do not express MUC13 (40) vs lines expressing it (10) | 5.49× lower at baseline in the lines without MUC13 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, NPSR1, CDH17; co-absent with the target |
| [[NPSR1-AS1]] | C | NPSR1-AS1 activity raises CDHR2's level | lines that do not express NPSR1-AS1 (34) vs lines expressing it (16) | 4.85× lower at baseline in the lines without NPSR1-AS1 | 0.002 | ⚠ within organs, on part of the lines; also absent: VIL1, A1CF, EPS8L3; maybe low, not absent; co-absent with the target |
| [[MYO7B]] | C | MYO7B activity raises CDHR2's level | lines that do not express MYO7B (36) vs lines expressing it (14) | 3.00× lower at baseline in the lines without MYO7B | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CLRN3, LINC01559, PHGR1; co-absent with the target |
| [[TOX3]] | C | TOX3 activity raises CDHR2's level | lines that do not express TOX3 (31) vs lines expressing it (19) | 3.62× lower at baseline in the lines without TOX3 | 0.003 | ⚠ within organs, on part of the lines; also absent: GPX2, ENSG00000287426, TMEM45B; co-absent with the target |
| [[HNF1A-AS1]] | C | HNF1A-AS1 activity raises CDHR2's level | lines that do not express HNF1A-AS1 (31) vs lines expressing it (19) | 4.03× lower at baseline in the lines without HNF1A-AS1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HNF1A, EPS8L3, GCNT3; maybe low, not absent; co-absent with the target |
| [[TMPRSS2]] | C | TMPRSS2 activity raises CDHR2's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 3.58× lower at baseline in the lines without TMPRSS2 | 0.004 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6; co-absent with the target |
| [[TRIM31]] | C | TRIM31 activity raises CDHR2's level | lines that do not express TRIM31 (39) vs lines expressing it (11) | 5.05× lower at baseline in the lines without TRIM31 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, GCNT3, NPSR1; co-absent with the target |
| [[LGALS4]] | C | LGALS4 activity raises CDHR2's level | lines that do not express LGALS4 (39) vs lines expressing it (11) | 4.95× lower at baseline in the lines without LGALS4 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13; maybe low, not absent; co-absent with the target |
| [[EPS8L3]] | C | EPS8L3 activity raises CDHR2's level | lines that do not express EPS8L3 (35) vs lines expressing it (15) | 5.61× lower at baseline in the lines without EPS8L3 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02964, EDAR, HNF4A; co-absent with the target |

### Downstream of this gene

*65 arrows, 65 of them with an alert ⚠; grade A 0, B 19, C 46. Shown: the 12 strongest; 53 more arrows (53 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KPNA7]] | B | CDHR2 activity raises KPNA7's level | lines that do not express CDHR2 (30) vs lines expressing it (20) | 2.71× lower at baseline in the lines without CDHR2 | 0.005 | ⚠ within organs, on part of the lines; also absent: VIL1, NPSR1-AS1, EPS8L3; maybe low, not absent |
| [[GCLC]] | B | CDHR2 activity raises GCLC's level | lines that do not express CDHR2 (30) vs lines expressing it (20) | 2.89× lower at baseline in the lines without CDHR2 | 0.007 | ⚠ within organs, on part of the lines; also absent: VIL1, NPSR1-AS1, EPS8L3; maybe low, not absent |
| [[SDCBP2]] | B | CDHR2 activity raises SDCBP2's level | lines that do not express CDHR2 (30) vs lines expressing it (20) | 3.34× lower at baseline in the lines without CDHR2 | 0.008 | ⚠ within organs, on part of the lines; also absent: VIL1, NPSR1-AS1, EPS8L3; maybe low, not absent |
| [[SERINC5]] | B | CDHR2 activity raises SERINC5's level | lines that do not express CDHR2 (30) vs lines expressing it (20) | 2.19× lower at baseline in the lines without CDHR2 | 0.008 | ⚠ within organs, on part of the lines; also absent: VIL1, NPSR1-AS1, EPS8L3; maybe low, not absent |
| [[EPS8L1]] | B | CDHR2 activity raises EPS8L1's level | lines that do not express CDHR2 (30) vs lines expressing it (20) | 3.03× lower at baseline in the lines without CDHR2 | 0.011 | ⚠ within organs, on part of the lines; also absent: VIL1, NPSR1-AS1, EPS8L3; maybe low, not absent |
| [[LINC02580]] | B | CDHR2 activity raises LINC02580's level | lines that do not express CDHR2 (30) vs lines expressing it (20) | 1.97× lower at baseline in the lines without CDHR2 | 0.023 | ⚠ within organs, on part of the lines; also absent: VIL1, NPSR1-AS1, EPS8L3; maybe low, not absent |
| [[MUC12]] | B | CDHR2 activity raises MUC12's level | lines that do not express CDHR2 (30) vs lines expressing it (20) | 1.92× lower at baseline in the lines without CDHR2 | 0.044 | ⚠ within organs, on part of the lines; also absent: VIL1, NPSR1-AS1, EPS8L3; maybe low, not absent |
| [[RASGEF1B]] | B | CDHR2 activity raises RASGEF1B's level | lines that do not express CDHR2 (30) vs lines expressing it (20) | 2.24× lower at baseline in the lines without CDHR2 | 0.055 | ⚠ within organs, on part of the lines; also absent: VIL1, NPSR1-AS1, EPS8L3; maybe low, not absent |
| [[HGD]] | B | CDHR2 activity raises HGD's level | lines that do not express CDHR2 (30) vs lines expressing it (20) | 2.67× lower at baseline in the lines without CDHR2 | 0.059 | ⚠ within organs, on part of the lines; also absent: VIL1, NPSR1-AS1, EPS8L3; maybe low, not absent |
| [[CEMIP2]] | B | CDHR2 activity raises CEMIP2's level | lines that do not express CDHR2 (30) vs lines expressing it (20) | 1.72× lower at baseline in the lines without CDHR2 | 0.062 | ⚠ within organs, on part of the lines; also absent: VIL1, NPSR1-AS1, EPS8L3; maybe low, not absent |
| [[ITPKC]] | B | CDHR2 activity raises ITPKC's level | lines that do not express CDHR2 (30) vs lines expressing it (20) | 2.20× lower at baseline in the lines without CDHR2 | 0.064 | ⚠ within organs, on part of the lines; also absent: VIL1, NPSR1-AS1, EPS8L3; maybe low, not absent |
| [[EPS8L1]] | B | CDHR2 activity strengthens EPS8L1's drug response | lines that do not express CDHR2 (18) vs lines expressing it (16) | the lines without CDHR2 respond 0.67× as strongly (z diff +0.99); strongest at Panobinostat 5 µM: 0.76x vs 0.30x (z diff +4.7) | 0.073 | ⚠ within organs, on part of the lines; also absent: VIL1, NPSR1-AS1, EPS8L3; maybe low, not absent; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.636). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.7, 53.0); signed map (62.7, 2.4). **Vector** length 40.7, 10.4% of its response variance represented; |z| ≥ 3 in 376 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +29.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +10.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +9.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +7.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.6 | +2.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.3 | +2.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.1 | -5.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.1 | -2.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.0 | -0.2 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.0 | -2.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -1.9 |
|  | [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -2.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.9 | -2.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -0.8 | -2.0 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -0.8 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | cadherin related family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.2 — chr5:176,542,511-176,595,974 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PC-LKC, FLJ20124, FLJ20383, PCLKC; previously PCDH24 |
| Gene groups (HGNC) | Cadherin related |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BYE9](https://www.uniprot.org/uniprotkb/Q9BYE9) (Cadherin-related family member 2):

> Intermicrovillar adhesion molecule that forms, via its extracellular domain, calcium-dependent heterophilic complexes with CDHR5 on adjacent microvilli. Thereby, controls the packing of microvilli at the apical membrane of epithelial cells. Through its cytoplasmic domain, interacts with microvillus cytoplasmic proteins to form the intermicrovillar adhesion complex/IMAC. This complex plays a central role in microvilli and epithelial brush border differentiation. May also play a role in cell-cell …

**Summary**, from NCBI Gene [54825](https://www.ncbi.nlm.nih.gov/gene/54825):

> This gene is a member of the protocadherin family, which represents a subset of the larger cadherin superfamily. The members of the protocadherin family encode non-classical cadherins that function as calcium-dependent cell-cell adhesion molecules. This protocadherin represents a new candidate for tumor suppression. Alternatively spliced transcript variants that encode the same protein have been identified. [provided by RefSeq, Jan 2010]

**Accessions** — [HGNC:18231](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18231) · Entrez [54825](https://www.ncbi.nlm.nih.gov/gene/54825) · UniProt [Q9BYE9](https://www.uniprot.org/uniprotkb/Q9BYE9) · Ensembl [ENSG00000074276](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000074276)

## Data

Gene col 1075: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1075); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1075, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1075]; `tensor/DDL_lfc|DDL_z.npy` [1075]; `embed/gene_vectors.npy` [1075]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1075 or target_col == 1075). Every well: [[CDHR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDHR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
