---
symbol: "PLA2G2A"
type: "gene"
col: 11995
ensembl_id: "ENSG00000188257"
name: "phospholipase A2 group IIA"
location: "1p36.13"
module: 44
arm: "+"
pooled_cpm: 4.44
n_lines_expressing: 9
n_dd_up: 13
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 42
direction_downstream: 53
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# PLA2G2A

*phospholipase A2 group IIA* — 1p36.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 7.82× (z +10.6, q 1e-23, up in 4 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.02× (z +5.1, q 4e-05, up in 2 of 6 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (COLO 205 0.0266×, LoVo 0.0303×, LS 180 0.122×); [[Homoharringtonine (drug)]] 5 µM in 3 lines (COLO 205 0.0990×, HepG2/C3A 0.220×, LoVo 0.163×; ⚠ cell-cycle shift, explains ~82% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (LoVo 0.0671×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LYZ]] (+0.69, fdr 1e-05), [[PHGR1]] (+0.67, fdr 7e-06), [[PRR15L]] (+0.64, fdr 1e-05); moves opposite to [[PRKG2-AS1]] (-0.44, fdr 1e-04).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 42 arrows point to it, the strongest [[NPSR1]] → it (grade C ⚠); 53 go from it, the strongest it → [[FAM3B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11995.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **7.82×** | +10.6 | 1e-23 | 4/6 (LS 180, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **8.04×** | +10.3 | 1e-22 | 1/2 (LS 180) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **6.34×** | +8.8 | 2e-16 | 1/3 (LS 180) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.02×** | +5.1 | 4e-05 | 2/6 (LS 180, HepG2/C3A) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.31×** | +4.3 | 0.002 | 0/7 | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **2.19×** | +4.1 | 0.005 | 0/6 | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.18×** | +3.9 | 0.009 | 1/6 (KATO III) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **3.32×** | +3.8 | 0.012 | 3/6 (BT-474, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.04×** | +3.7 | 0.014 | 1/6 (LS 180) | top dose only | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.88×** | +3.5 | 0.027 | 6/7 (BT-474, HepG2/C3A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.86×** | +3.3 | 0.051 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.49×** | +3.3 | 0.053 | 0/2 | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.87×** | +3.1 | 0.079 | 2/5 (LS 180, COLO 205) | top dose only | cell-cycle shift (explains ~20% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11995.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (COLO 205 0.0266×, LoVo 0.0303×, LS 180 0.122×); [[Homoharringtonine (drug)]] 5 µM in 3 lines (COLO 205 0.0990×, HepG2/C3A 0.220×, LoVo 0.163×; ⚠ cell-cycle shift, explains ~82% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (LoVo 0.0671×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 0.5 µM |  | 0.527× | -3.3 | 0.48 | 1/7 (COLO 205) | two highest doses |  |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.517× | -3.1 | 0.48 | 0/7 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11995. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 138 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0266× (z -13.1) |
| [[LoVo (line)]] | wt | 9.42 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0303× (z -12.0) |
| [[LS 180 (line)]] | wt | 26.2 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.113× (z -9.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.122× (z -8.7) |
| [[HepG2_C3A (line)]] | wt | 109 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -9.1) ⚠ cell-cycle shift, explains ~82% of this change |
| [[A-172 (line)]] | wt | 0.549 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.393 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.440 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.303 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.533 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.591 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.488 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.541 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.627 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.524 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.536 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.556 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.483 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.825 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.654 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.367 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.601 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.370 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.454 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.342 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.438 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.417 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.487 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.418 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.782 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.439 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.359 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.491 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.390 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.381 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.414 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.518 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.552 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.543 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.558 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.467 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.629 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.404 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11995), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LYZ]] | +0.69 | +0.67 / +0.53 | both halves | 1e-05 | pathway: Antimicrobial peptides; STRING 410 |
| [[PHGR1]] | +0.67 | +0.58 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[PRR15L]] | +0.64 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[AGR3]] | +0.62 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[HNF1A-AS1]] | +0.62 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[FXYD3]] | +0.61 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[PPP1R1B]] | +0.60 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[MYB]] | +0.60 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[LINC02331]] | +0.60 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[SLC40A1]] | +0.60 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[TSPAN8]] | +0.59 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[ST6GALNAC1]] | +0.59 | +0.51 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKG2-AS1]] | -0.44 | -0.42 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*42 arrows, 42 of them with an alert ⚠; grade A 0, B 0, C 42. Shown: the 12 strongest; 30 more arrows (30 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NPSR1]] | C | NPSR1 activity raises PLA2G2A's level | lines that do not express NPSR1 (42) vs lines expressing it (8) | 5.31× lower at baseline in the lines without NPSR1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, MUC17, CDH17; co-absent with the target |
| [[PHGR1]] | C | PHGR1 activity raises PLA2G2A's level | lines that do not express PHGR1 (43) vs lines expressing it (7) | 5.34× lower at baseline in the lines without PHGR1 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FAM3D, GPA33, KRT20; co-absent with the target |
| [[ST6GALNAC1]] | C | ST6GALNAC1 activity raises PLA2G2A's level | lines that do not express ST6GALNAC1 (37) vs lines expressing it (13) | 4.14× lower at baseline in the lines without ST6GALNAC1 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, SLC44A4, STEAP4; co-absent with the target |
| [[FAM3D]] | C | FAM3D activity raises PLA2G2A's level | lines that do not express FAM3D (43) vs lines expressing it (7) | 5.33× lower at baseline in the lines without FAM3D | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, ENSG00000230975, NPSR1; maybe low, not absent; co-absent with the target |
| [[AGR3]] | C | AGR3 activity raises PLA2G2A's level | lines that do not express AGR3 (42) vs lines expressing it (8) | 5.06× lower at baseline in the lines without AGR3 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17; co-absent with the target |
| [[MUC5B]] | C | MUC5B activity raises PLA2G2A's level | lines that do not express MUC5B (37) vs lines expressing it (13) | 2.42× lower at baseline in the lines without MUC5B | 0.016 | ⚠ within organs, on part of the lines; also absent: DAPP1, AGR3, ENSG00000259925; co-absent with the target |
| [[ATP10B]] | C | ATP10B activity raises PLA2G2A's level | lines that do not express ATP10B (40) vs lines expressing it (10) | 3.60× lower at baseline in the lines without ATP10B | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17; co-absent with the target |
| [[TFF3]] | C | TFF3 activity raises PLA2G2A's level | lines that do not express TFF3 (38) vs lines expressing it (12) | 4.46× lower at baseline in the lines without TFF3 | 0.021 | ⚠ within organs, on part of the lines; also absent: CEACAM5, MUC17, AGR3; co-absent with the target |
| [[BCAS1]] | C | BCAS1 activity raises PLA2G2A's level | lines that do not express BCAS1 (32) vs lines expressing it (18) | 2.75× lower at baseline in the lines without BCAS1 | 0.023 | ⚠ within organs, on part of the lines; also absent: SLC6A14, AGR3, LYZ; co-absent with the target |
| [[PCK1]] | C | PCK1 activity raises PLA2G2A's level | lines that do not express PCK1 (38) vs lines expressing it (12) | 4.30× lower at baseline in the lines without PCK1 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LGR5, GPX2, CPLX2; co-absent with the target |
| [[MUC13]] | C | MUC13 activity raises PLA2G2A's level | lines that do not express MUC13 (40) vs lines expressing it (10) | 3.58× lower at baseline in the lines without MUC13 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, NPSR1, CDH17; co-absent with the target |
| [[CYP4F12]] | C | CYP4F12 activity raises PLA2G2A's level | lines that do not express CYP4F12 (32) vs lines expressing it (18) | 3.08× lower at baseline in the lines without CYP4F12 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD3, CDH17, MUC13; co-absent with the target |

### Downstream of this gene

*53 arrows, 53 of them with an alert ⚠; grade A 0, B 5, C 48. Shown: the 12 strongest; 41 more arrows (41 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM3B]] | B | PLA2G2A activity raises FAM3B's level | lines that do not express PLA2G2A (41) vs lines expressing it (9) | 3.34× lower at baseline in the lines without PLA2G2A | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, CALB1 |
| [[LIMK2]] | B | PLA2G2A activity raises LIMK2's level | lines that do not express PLA2G2A (41) vs lines expressing it (9) | 1.71× lower at baseline in the lines without PLA2G2A | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, CALB1 |
| [[BCL2L14]] | B | PLA2G2A activity raises BCL2L14's level | lines that do not express PLA2G2A (41) vs lines expressing it (9) | 1.52× lower at baseline in the lines without PLA2G2A | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, CALB1 |
| [[MANSC1]] | B | PLA2G2A activity raises MANSC1's level | lines that do not express PLA2G2A (41) vs lines expressing it (9) | 2.57× lower at baseline in the lines without PLA2G2A | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, CALB1 |
| [[PLEKHS1]] | B | PLA2G2A activity raises PLEKHS1's level | lines that do not express PLA2G2A (41) vs lines expressing it (9) | 1.78× lower at baseline in the lines without PLA2G2A | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, CALB1 |
| [[PCK1]] | C | PLA2G2A activity raises PCK1's level | lines that do not express PLA2G2A (41) vs lines expressing it (9) | 6.42× lower at baseline in the lines without PLA2G2A | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, CALB1; co-absent with the target |
| [[FXYD3]] | C | PLA2G2A activity raises FXYD3's level | lines that do not express PLA2G2A (41) vs lines expressing it (9) | 7.98× lower at baseline in the lines without PLA2G2A | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, CALB1; co-absent with the target |
| [[TSPAN8]] | C | PLA2G2A activity raises TSPAN8's level | lines that do not express PLA2G2A (41) vs lines expressing it (9) | 7.23× lower at baseline in the lines without PLA2G2A | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, CALB1; co-absent with the target |
| [[LINC01559]] | C | PLA2G2A activity raises LINC01559's level | lines that do not express PLA2G2A (41) vs lines expressing it (9) | 4.73× lower at baseline in the lines without PLA2G2A | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, CALB1; co-absent with the target |
| [[PRR15]] | C | PLA2G2A activity raises PRR15's level | lines that do not express PLA2G2A (41) vs lines expressing it (9) | 5.53× lower at baseline in the lines without PLA2G2A | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, CALB1; co-absent with the target |
| [[ATP10B]] | C | PLA2G2A activity raises ATP10B's level | lines that do not express PLA2G2A (41) vs lines expressing it (9) | 5.89× lower at baseline in the lines without PLA2G2A | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, CALB1; co-absent with the target |
| [[UGT1A1]] | C | PLA2G2A activity raises UGT1A1's level | lines that do not express PLA2G2A (41) vs lines expressing it (9) | 4.94× lower at baseline in the lines without PLA2G2A | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, CALB1; co-absent with the target |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.666). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.3, 50.5); signed map (65.2, 5.3). **Vector** length 33.7, 14.6% of its response variance represented; |z| ≥ 3 in 196 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Defective GALNT12 causes CRCS1* (reactome, mean cos +0.50 to 5); *Defective GALNT3 causes HFTC* (reactome, mean cos +0.50 to 5); *Defective C1GALT1C1 causes TNPS* (reactome, mean cos +0.50 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +1.4 | +3.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.3 | +8.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.3 | +2.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.3 | +5.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +1.2 | +3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.0 | +2.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.0 | +3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.9 | +0.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +0.9 | +1.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -0.8 | -1.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.8 | -2.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.6 | -2.8 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.6 | -1.6 |
|  | [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.6 | -1.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.6 | +0.5 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.6 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | phospholipase A2 group IIA |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.13 — chr1:19,975,431-19,980,416 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously PLA2B, PLA2L |
| Gene groups (HGNC) | Phospholipases |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING |
| Reactome | 11 pathways, smallest: Acyl chain remodelling of PI; Acyl chain remodelling of PG; Acyl chain remodelling of PS |
| Matched by | ensembl_id |

**Function**, from UniProt [P14555](https://www.uniprot.org/uniprotkb/P14555) (Phospholipase A2, membrane associated):

> Secretory calcium-dependent phospholipase A2 that primarily targets extracellular phospholipids with implications in host antimicrobial defense, inflammatory response and tissue regeneration. Hydrolyzes the ester bond of the fatty acyl group attached at sn-2 position of phospholipids (phospholipase A2 activity) with preference for phosphatidylethanolamines and phosphatidylglycerols over phosphatidylcholines. Contributes to lipid remodeling of cellular membranes and generation of lipid mediators …

**Summary**, from NCBI Gene [5320](https://www.ncbi.nlm.nih.gov/gene/5320):

> The protein encoded by this gene is a member of the phospholipase A2 family (PLA2). PLA2s constitute a diverse family of enzymes with respect to sequence, function, localization, and divalent cation requirements. This gene product belongs to group II, which contains secreted form of PLA2, an extracellular enzyme that has a low molecular mass and requires calcium ions for catalysis. It catalyzes the hydrolysis of the sn-2 fatty acid acyl ester bond of phosphoglycerides, releasing free fatty …

**Accessions** — [HGNC:9031](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9031) · Entrez [5320](https://www.ncbi.nlm.nih.gov/gene/5320) · UniProt [P14555](https://www.uniprot.org/uniprotkb/P14555) · Ensembl [ENSG00000188257](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188257)

## Data

Gene col 11995: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11995); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11995, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11995]; `tensor/DDL_lfc|DDL_z.npy` [11995]; `embed/gene_vectors.npy` [11995]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11995 or target_col == 11995). Every well: [[PLA2G2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLA2G2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
