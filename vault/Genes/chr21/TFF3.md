---
symbol: "TFF3"
type: "gene"
col: 8306
ensembl_id: "ENSG00000160180"
name: "trefoil factor 3"
location: "21q22.3"
module: 55
arm: "+"
pooled_cpm: 10.46
n_lines_expressing: 12
n_dd_up: 5
n_dd_down: 1
n_dd_up_clean: 1
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 54
direction_downstream: 75
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# TFF3

*trefoil factor 3* — 21q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 6.65× (z +8.5, q 1e-14, up in 6 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.79× (z +3.7, q 0.030, up in 1 of 9 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (BT-474 5.89×).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.429× (z -3.8, q 0.089, down in 8 of 9 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 4 lines (SW480 0.0539×, LS 180 0.0897×, SHP-77 0.125×, KATO III 0.118×); [[Homoharringtonine (drug)]] 5 µM in 3 lines (SW480 0.0570×, SHP-77 0.111×, LS 180 0.0872×); [[Belinostat (drug)]] 5 µM in 1 line (SW480 0.00816×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLRN3]] (+0.78, fdr 7e-06), [[LINC02058]] (+0.77, fdr 7e-06), [[GJB1]] (+0.77, fdr 7e-06).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 54 arrows point to it, the strongest [[MUC6]] → it (grade C ⚠); 75 go from it, the strongest it → [[BCAR3-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8306.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (BT-474 5.89×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.65×** | +8.5 | 1e-14 | 6/8 (BT-474, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.98×** | +6.9 | 1e-09 | 4/6 (BT-474, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.49×** | +5.2 | 4e-05 | 1/6 (BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +3.7 | 0.030 | 1/9 (BT-474) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.17×** | +3.4 | 0.089 | 1/8 (BT-474) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | 2.03× | +3.2 | 0.14 | 0/9 | inconsistent across doses |  |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 1.63× | +3.1 | 0.15 | 6/9 (SW480, COLO 205, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8306.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 4 lines (SW480 0.0539×, LS 180 0.0897×, SHP-77 0.125×, KATO III 0.118×); [[Homoharringtonine (drug)]] 5 µM in 3 lines (SW480 0.0570×, SHP-77 0.111×, LS 180 0.0872×); [[Belinostat (drug)]] 5 µM in 1 line (SW480 0.00816×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.429×** | -3.8 | 0.089 | 8/9 (SW480, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | 0.247× | -3.3 | 0.16 | 7/9 (KATO III, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | 0.249× | -3.3 | 0.16 | 6/9 (BT-474, COLO 205, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | 0.251× | -3.2 | 0.16 | 7/10 (COLO 205, SHP-77, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.461× | -3.2 | 0.16 | 1/9 (LS 180) | inconsistent across doses | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.470× | -3.1 | 0.17 | 2/9 (LS 180, HepG2/C3A) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.05 µM |  | 0.482× | -3.1 | 0.17 | 7/9 (BT-474, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, +0.92 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8306. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 23.7 | 0 | 8 | — | [[Belinostat (drug)]] 5 µM 0.00816× (z -19.0) |
| [[COLO 205 (line)]] | alt | 97.5 | 0 | 3 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0645× (z -10.9) ⚠ cell-cycle shift, explains ~66% of this change |
| [[LS 180 (line)]] | wt | 146 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0872× (z -13.2) |
| [[SHP-77 (line)]] | alt | 95.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -13.7) |
| [[BT-474 (line)]] | alt | 32.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.89× (z +10.3) | — |
| [[KATO III (line)]] | alt | 56.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.118× (z -8.5) |
| [[A-172 (line)]] | wt | 0.925 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.850 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.805 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.633 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.814 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.986 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.60 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.883 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.957 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.767 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.742 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.791 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.774 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.845 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.922 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.836 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.795 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.863 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.00 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.848 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.945 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.31 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8306), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLRN3]] | +0.78 | +0.81 / +0.66 | both halves | 7e-06 |  |
| [[LINC02058]] | +0.77 | +0.80 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[GJB1]] | +0.77 | +0.76 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[C9orf152]] | +0.74 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[BMP4]] | +0.73 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[NKD1]] | +0.71 | +0.71 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[KCNE3]] | +0.69 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[IL20RA]] | +0.69 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[AZGP1]] | +0.68 | +0.55 / +0.74 | both halves | 1e-05 |  |
| [[LGR5]] | +0.68 | +0.64 / +0.59 | both halves | 7e-06 | STRING 480 |
| [[KLK6]] | +0.67 | +0.70 / +0.50 | both halves | 1e-05 |  |
| [[FGD5]] | +0.67 | +0.72 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*54 arrows, 54 of them with an alert ⚠; grade A 0, B 0, C 54. Shown: the 12 strongest; 42 more arrows (42 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MUC6]] | C | MUC6 activity raises TFF3's level | lines that do not express MUC6 (45) vs lines expressing it (5) | 15.61× lower at baseline in the lines without MUC6 | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, ENSG00000230975, APOB; co-absent with the target |
| [[INPP5D]] | C | INPP5D activity raises TFF3's level | lines that do not express INPP5D (34) vs lines expressing it (16) | 4.85× lower at baseline in the lines without INPP5D | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A, TP53; also absent: CLRN3, LINC02964, LGR5; co-absent with the target |
| [[HNF1A-AS1]] | C | HNF1A-AS1 activity raises TFF3's level | lines that do not express HNF1A-AS1 (31) vs lines expressing it (19) | 4.80× lower at baseline in the lines without HNF1A-AS1 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HNF1A, EPS8L3, GCNT3; maybe low, not absent; co-absent with the target |
| [[SMOC2]] | C | SMOC2 activity raises TFF3's level | lines that do not express SMOC2 (33) vs lines expressing it (17) | 4.51× lower at baseline in the lines without SMOC2 | 0.004 | ⚠ within organs, on part of the lines; also absent: LINC01456, TFF3, MIR3667HG; maybe low, not absent; co-absent with the target |
| [[PCK1]] | C | PCK1 activity raises TFF3's level | lines that do not express PCK1 (38) vs lines expressing it (12) | 5.78× lower at baseline in the lines without PCK1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LGR5, GPX2, CPLX2; co-absent with the target |
| [[ST18]] | C | ST18 activity raises TFF3's level | lines that do not express ST18 (39) vs lines expressing it (11) | 5.41× lower at baseline in the lines without ST18 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000213981, CALCA, KCNB2; maybe low, not absent; co-absent with the target |
| [[PPP1R1B]] | C | PPP1R1B activity raises TFF3's level | lines that do not express PPP1R1B (37) vs lines expressing it (13) | 6.34× lower at baseline in the lines without PPP1R1B | 0.007 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CEACAM5, NPSR1, CDH17; co-absent with the target |
| [[LGR5]] | C | LGR5 activity raises TFF3's level | lines that do not express LGR5 (39) vs lines expressing it (11) | 5.10× lower at baseline in the lines without LGR5 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PCK1, DSG4, ENSG00000260573; co-absent with the target |
| [[TOX3]] | C | TOX3 activity raises TFF3's level | lines that do not express TOX3 (31) vs lines expressing it (19) | 4.46× lower at baseline in the lines without TOX3 | 0.008 | ⚠ within organs, on part of the lines; also absent: GPX2, ENSG00000287426, TMEM45B; co-absent with the target |
| [[LINC01559]] | C | LINC01559 activity raises TFF3's level | lines that do not express LINC01559 (38) vs lines expressing it (12) | 5.03× lower at baseline in the lines without LINC01559 | 0.010 | ⚠ within organs, on part of the lines; also absent: CLRN3, NPSR1, CDH17; co-absent with the target |
| [[PROX1]] | C | PROX1 activity raises TFF3's level | lines that do not express PROX1 (30) vs lines expressing it (20) | 3.32× lower at baseline in the lines without PROX1 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CDH17, CLRN3, LINC02964; co-absent with the target |
| [[AGR3]] | C | AGR3 activity raises TFF3's level | lines that do not express AGR3 (42) vs lines expressing it (8) | 9.01× lower at baseline in the lines without AGR3 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17; co-absent with the target |

### Downstream of this gene

*75 arrows, 75 of them with an alert ⚠; grade A 0, B 11, C 64. Shown: the 12 strongest; 63 more arrows (63 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCAR3-AS1]] | B | TFF3 activity raises BCAR3-AS1's level | lines that do not express TFF3 (38) vs lines expressing it (12) | 2.20× lower at baseline in the lines without TFF3 | 8e-04 | ⚠ within organs, on part of the lines; also absent: CEACAM5, MUC17, AGR3 |
| [[NDUFA4L2]] | B | TFF3 activity raises NDUFA4L2's level | lines that do not express TFF3 (38) vs lines expressing it (12) | 2.72× lower at baseline in the lines without TFF3 | 0.015 | ⚠ within organs, on part of the lines; also absent: CEACAM5, MUC17, AGR3 |
| [[MGST2]] | B | TFF3 activity raises MGST2's level | lines that do not express TFF3 (38) vs lines expressing it (12) | 2.42× lower at baseline in the lines without TFF3 | 0.040 | ⚠ within organs, on part of the lines; also absent: CEACAM5, MUC17, AGR3 |
| [[BCAR3-AS1]] | B | TFF3 activity strengthens BCAR3-AS1's drug response | lines that do not express TFF3 (36) vs lines expressing it (9) | the lines without TFF3 respond 0.75× as strongly (z diff +0.48); strongest at Digitoxin 0.5 µM: 0.62x vs 0.30x (z diff +3.3) | 0.059 | ⚠ within organs, on part of the lines; also absent: CEACAM5, MUC17, AGR3; target measured in part of the lines; both ways; artifact flags |
| [[F10]] | B | TFF3 activity raises F10's level | lines that do not express TFF3 (38) vs lines expressing it (12) | 2.06× lower at baseline in the lines without TFF3 | 0.069 | ⚠ within organs, on part of the lines; also absent: CEACAM5, MUC17, AGR3 |
| [[DNAJC22]] | B | TFF3 activity raises DNAJC22's level | lines that do not express TFF3 (38) vs lines expressing it (12) | 2.28× lower at baseline in the lines without TFF3 | 0.070 | ⚠ within organs, on part of the lines; also absent: CEACAM5, MUC17, AGR3 |
| [[PDK4-AS1]] | B | TFF3 activity raises PDK4-AS1's level | lines that do not express TFF3 (38) vs lines expressing it (12) | 1.72× lower at baseline in the lines without TFF3 | 0.078 | ⚠ within organs, on part of the lines; also absent: CEACAM5, MUC17, AGR3 |
| [[CA9]] | B | TFF3 activity raises CA9's level | lines that do not express TFF3 (38) vs lines expressing it (12) | 3.82× lower at baseline in the lines without TFF3 | 0.079 | ⚠ within organs, on part of the lines; also absent: CEACAM5, MUC17, AGR3 |
| [[HUNK]] | B | TFF3 activity raises HUNK's level | lines that do not express TFF3 (38) vs lines expressing it (12) | 2.62× lower at baseline in the lines without TFF3 | 0.080 | ⚠ within organs, on part of the lines; also absent: CEACAM5, MUC17, AGR3 |
| [[ENPP3]] | B | TFF3 activity raises ENPP3's level | lines that do not express TFF3 (38) vs lines expressing it (12) | 1.60× lower at baseline in the lines without TFF3 | 0.096 | ⚠ within organs, on part of the lines; also absent: CEACAM5, MUC17, AGR3 |
| [[CHDH]] | B | TFF3 activity raises CHDH's level | lines that do not express TFF3 (38) vs lines expressing it (12) | 2.58× lower at baseline in the lines without TFF3 | 0.098 | ⚠ within organs, on part of the lines; also absent: CEACAM5, MUC17, AGR3 |
| [[TOX3]] | C | TFF3 activity raises TOX3's level | lines that do not express TFF3 (38) vs lines expressing it (12) | 14.36× lower at baseline in the lines without TFF3 | 5e-05 | ⚠ within organs, on part of the lines; also absent: CEACAM5, MUC17, AGR3; co-absent with the target |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.689). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.7, 46.1); signed map (63.4, 13.2). **Vector** length 44.4, 22.3% of its response variance represented; |z| ≥ 3 in 207 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +3.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +6.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | +8.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.7 | +5.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.0 | -1.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | -0.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +0.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +2.4 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.2 | +2.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.1 | +2.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.5 | -2.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -0.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.4 | -2.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.3 | -2.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -0.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | trefoil factor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.3 — chr21:42,311,667-42,315,409 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HITF, ITF |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, GLYCOLYSIS, ESTROGEN_RESPONSE_EARLY |
| Reactome | 3 pathways, smallest: Estrogen-dependent gene expression; ESR-mediated signaling; Signaling by Nuclear Receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q07654](https://www.uniprot.org/uniprotkb/Q07654) (Trefoil factor 3):

> Involved in the maintenance and repair of the intestinal mucosa. Promotes the mobility of epithelial cells in healing processes (motogen).

**Summary**, from NCBI Gene [7033](https://www.ncbi.nlm.nih.gov/gene/7033):

> Members of the trefoil family are characterized by having at least one copy of the trefoil motif, a 40-amino acid domain that contains three conserved disulfides. They are stable secretory proteins expressed in gastrointestinal mucosa. Their functions are not defined, but they may protect the mucosa from insults, stabilize the mucus layer and affect healing of the epithelium. This gene is expressed in goblet cells of the intestines and colon. This gene and two other related trefoil family …

**Accessions** — [HGNC:11757](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11757) · Entrez [7033](https://www.ncbi.nlm.nih.gov/gene/7033) · UniProt [Q07654](https://www.uniprot.org/uniprotkb/Q07654) · Ensembl [ENSG00000160180](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160180)

## Data

Gene col 8306: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8306); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8306, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8306]; `tensor/DDL_lfc|DDL_z.npy` [8306]; `embed/gene_vectors.npy` [8306]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8306 or target_col == 8306). Every well: [[TFF3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TFF3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
