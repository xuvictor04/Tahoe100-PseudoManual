---
symbol: "DMKN"
type: "gene"
col: 8424
ensembl_id: "ENSG00000161249"
name: "dermokine"
location: "19q13.12"
module: 73
arm: "+"
pooled_cpm: 19.0
n_lines_expressing: 26
n_dd_up: 19
n_dd_down: 2
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 19
direction_downstream: 20
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# DMKN

*dermokine* — 19q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.71× (z +14.4, q 6e-44, up in 14 of 17 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.69× (z +8.2, q 6e-14, up in 10 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.761× (z -4.2, q 0.013, down in 16 of 23 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (NCI-H2347 0.402×, LoVo 0.371×, SW480 0.547×, NCI-H2030 0.425×); [[Panobinostat (drug)]] 5 µM in 2 lines (NCI-H23 0.297×, HEC-1-A 0.416×); [[Belinostat (drug)]] 5 µM in 2 lines (HEC-1-A 0.421×, NCI-H23 0.346×; ⚠ cell-cycle shift, explains ~85% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (HEC-1-A 0.392×).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BAGE2]] (+0.53, fdr 3e-05), [[ZNF860]] (+0.52, fdr 8e-05), [[SH2D3A]] (+0.50, fdr 9e-05); moves opposite to [[CKAP4]] (-0.38, fdr 2e-04).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[LINC02832]] → it (grade B ⚠); 20 go from it, the strongest it → [[PSD4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8424.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.71×** | +14.4 | 6e-44 | 14/17 (LS 180, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.81×** | +14.1 | 1e-42 | 9/13 (CFPAC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.69×** | +8.2 | 6e-14 | 10/23 (HOP62, HepG2/C3A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.10×** | +8.1 | 7e-14 | 7/23 (HOP62, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.13×** | +7.6 | 2e-12 | 12/14 (NCI-H2030, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.79×** | +6.4 | 2e-08 | 7/23 (HOP62, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +4.8 | 2e-04 | 5/23 (NCI-H2347, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.44×** | +4.0 | 0.004 | 6/23 (HOP62, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +4.0 | 0.004 | 9/19 (CFPAC-1, KATO III, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +3.9 | 0.005 | 5/23 (NCI-H23, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.42×** | +3.8 | 0.007 | 7/22 (NCI-H1573, A-427, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.37×** | +3.4 | 0.028 | 10/23 (NCI-H2030, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.86×** | +3.3 | 0.038 | 3/11 (NCI-H2347, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.60×** | +3.2 | 0.065 | 8/21 (NCI-H2347, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.079 | 7/23 (HOP62, CFPAC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.55×** | +3.0 | 0.099 | 7/23 (A-427, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.31×** | +2.9 | 0.099 | 4/23 (A549, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8424.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (NCI-H2347 0.402×, LoVo 0.371×, SW480 0.547×, NCI-H2030 0.425×); [[Panobinostat (drug)]] 5 µM in 2 lines (NCI-H23 0.297×, HEC-1-A 0.416×); [[Belinostat (drug)]] 5 µM in 2 lines (HEC-1-A 0.421×, NCI-H23 0.346×; ⚠ cell-cycle shift, explains ~85% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (HEC-1-A 0.392×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.761×** | -4.2 | 0.013 | 16/23 (NCI-H2347, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.718×** | -3.6 | 0.081 | 0/24 | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | 0.757× | -3.1 | 0.37 | 11/22 (SHP-77, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.743× | -3.0 | 0.37 | 2/23 (LoVo, C-33 A) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8424. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 127 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.392× (z -9.9) |
| [[NCI-H23 (line)]] | alt | 47.0 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.297× (z -10.1) |
| [[SW480 (line)]] | alt | 71.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.547× (z -9.5) |
| [[LoVo (line)]] | wt | 32.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -10.6) |
| [[NCI-H2030 (line)]] | alt | 38.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -9.2) |
| [[NCI-H2347 (line)]] | alt | 44.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -11.1) |
| [[SHP-77 (line)]] | alt | 5.41 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0856× (z -9.0) |
| [[A-172 (line)]] | wt | 2.69 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 42.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.20 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 6.10 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.46 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.41 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.98 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.35 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.51 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.36 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.07 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.69 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.21 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.68 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.41 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.81 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.95 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.58 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 8.07 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.16 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.43 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.33 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 52.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8424), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BAGE2]] | +0.53 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[ZNF860]] | +0.52 | +0.45 / +0.37 | both halves | 8e-05 |  |
| [[SH2D3A]] | +0.50 | +0.44 / +0.37 | both halves | 9e-05 |  |
| [[LAD1]] | +0.49 | +0.38 / +0.54 | both halves | 6e-05 |  |
| [[CISD3]] | +0.49 | +0.43 / +0.50 | both halves | 4e-05 |  |
| [[LARGE2]] | +0.49 | +0.42 / +0.34 | both halves | 1e-04 |  |
| [[CAPN8]] | +0.47 | +0.41 / +0.43 | both halves | 4e-05 |  |
| [[C19orf33]] | +0.46 | +0.36 / +0.55 | both halves | 9e-05 |  |
| [[LINC01357]] | +0.46 | +0.43 / +0.40 | both halves | 5e-05 |  |
| [[AGMAT]] | +0.46 | +0.31 / +0.44 | both halves | 2e-04 |  |
| [[CTSE]] | +0.45 | +0.32 / +0.40 | both halves | 2e-04 |  |
| [[MUC2]] | +0.45 | +0.36 / +0.43 | both halves | 1e-04 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CKAP4]] | -0.38 | -0.31 / -0.34 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 4, C 15. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02832]] | B | LINC02832 activity raises DMKN's level | lines that do not express LINC02832 (26) vs lines expressing it (24) | 2.74× lower at baseline in the lines without LINC02832 | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000235337, ENSG00000288902, ENSG00000239498 |
| [[TMC6]] | B | TMC6 activity raises DMKN's level | lines that do not express TMC6 (12) vs lines expressing it (38) | 3.39× lower at baseline in the lines without TMC6 | 0.027 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, FGFR4, LSR |
| [[KRT18]] | B | KRT18 activity raises DMKN's level | lines that do not express KRT18 (19) vs lines expressing it (31) | 2.91× lower at baseline in the lines without KRT18 | 0.033 | ⚠ within organs, on part of the lines; also absent: MISP, SFN, GRB7; maybe low, not absent |
| [[CCND1]] | B | CCND1 activity raises DMKN's level | lines that do not express CCND1 (7) vs lines expressing it (43) | 1.83× lower at baseline in the lines without CCND1 | 0.088 | ⚠ within organs, on part of the lines; also absent: FSTL3, ADAMTSL5; maybe low, not absent |
| [[BSPRY]] | C | BSPRY activity raises DMKN's level | lines that do not express BSPRY (29) vs lines expressing it (21) | 4.53× lower at baseline in the lines without BSPRY | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPCAM, RAB25; co-absent with the target |
| [[SH2D3A]] | C | SH2D3A activity raises DMKN's level | lines that do not express SH2D3A (24) vs lines expressing it (26) | 3.80× lower at baseline in the lines without SH2D3A | 0.006 | ⚠ within organs, on part of the lines; also absent: GRB7, MYO5B, CRB3; co-absent with the target |
| [[ZNF860]] | C | ZNF860 activity raises DMKN's level | lines that do not express ZNF860 (16) vs lines expressing it (34) | 3.38× lower at baseline in the lines without ZNF860 | 0.007 | ⚠ within organs, on part of the lines; also absent: CRYBG2, IL18, TMC4; co-absent with the target |
| [[AP1M2]] | C | AP1M2 activity raises DMKN's level | lines that do not express AP1M2 (24) vs lines expressing it (26) | 3.13× lower at baseline in the lines without AP1M2 | 0.021 | ⚠ within organs, on part of the lines; also absent: CRB3, SPINT1-AS1, GRB7; co-absent with the target |
| [[ZBED2]] | C | ZBED2 activity raises DMKN's level | lines that do not express ZBED2 (39) vs lines expressing it (11) | 4.28× lower at baseline in the lines without ZBED2 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SPON1, ENSG00000289850, KLK11; co-absent with the target |
| [[CKMT1B]] | C | CKMT1B activity raises DMKN's level | lines that do not express CKMT1B (28) vs lines expressing it (22) | 2.85× lower at baseline in the lines without CKMT1B | 0.032 | ⚠ within organs, on part of the lines; also absent: CKMT1A, SYK, PPP1R1B; co-absent with the target |
| [[LAD1]] | C | LAD1 activity raises DMKN's level | lines that do not express LAD1 (30) vs lines expressing it (20) | 3.18× lower at baseline in the lines without LAD1 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ST14, KDF1; co-absent with the target |
| [[IQANK1]] | C | IQANK1 activity raises DMKN's level | lines that do not express IQANK1 (18) vs lines expressing it (32) | 3.11× lower at baseline in the lines without IQANK1 | 0.041 | ⚠ within organs, on part of the lines; also absent: LSR, ENTPD2, FAM83H; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 7, C 13. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSD4]] | B | DMKN activity raises PSD4's level | lines that do not express DMKN (24) vs lines expressing it (26) | 2.28× lower at baseline in the lines without DMKN | 0.012 | ⚠ within organs, on part of the lines; also absent: SPINT1, BSPRY, SMPDL3B |
| [[TMC6]] | B | DMKN activity raises TMC6's level | lines that do not express DMKN (24) vs lines expressing it (26) | 2.98× lower at baseline in the lines without DMKN | 0.013 | ⚠ within organs, on part of the lines; also absent: SPINT1, BSPRY, SMPDL3B |
| cells under [[9-ING-41 (drug)]] 5 µM | B | DMKN activity lowers the cells' numbers under 9-ING-41 5 µM (makes them more sensitive) | lines that do not express DMKN (24) vs lines expressing it (24) | the lines without DMKN: 1.18× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; also absent: SPINT1, BSPRY, SMPDL3B |
| [[KRT18]] | B | DMKN activity raises KRT18's level | lines that do not express DMKN (24) vs lines expressing it (26) | 2.66× lower at baseline in the lines without DMKN | 0.055 | ⚠ within organs, on part of the lines; also absent: SPINT1, BSPRY, SMPDL3B |
| [[SLC29A2]] | B | DMKN activity raises SLC29A2's level | lines that do not express DMKN (24) vs lines expressing it (26) | 2.51× lower at baseline in the lines without DMKN | 0.077 | ⚠ within organs, on part of the lines; also absent: SPINT1, BSPRY, SMPDL3B |
| [[COPG2IT1]] | B | DMKN activity raises COPG2IT1's level | lines that do not express DMKN (24) vs lines expressing it (26) | 1.70× lower at baseline in the lines without DMKN | 0.081 | ⚠ within organs, on part of the lines; also absent: SPINT1, BSPRY, SMPDL3B |
| [[SPTBN2]] | B | DMKN activity raises SPTBN2's level | lines that do not express DMKN (24) vs lines expressing it (26) | 2.03× lower at baseline in the lines without DMKN | 0.097 | ⚠ within organs, on part of the lines; also absent: SPINT1, BSPRY, SMPDL3B |
| [[LAD1]] | C | DMKN activity raises LAD1's level | lines that do not express DMKN (24) vs lines expressing it (26) | 3.56× lower at baseline in the lines without DMKN | 0.010 | ⚠ within organs, on part of the lines; also absent: SPINT1, BSPRY, SMPDL3B; co-absent with the target |
| [[CKMT1B]] | C | DMKN activity raises CKMT1B's level | lines that do not express DMKN (24) vs lines expressing it (26) | 2.41× lower at baseline in the lines without DMKN | 0.011 | ⚠ within organs, on part of the lines; also absent: SPINT1, BSPRY, SMPDL3B; co-absent with the target |
| [[SH2D3A]] | C | DMKN activity raises SH2D3A's level | lines that do not express DMKN (24) vs lines expressing it (26) | 3.56× lower at baseline in the lines without DMKN | 0.017 | ⚠ within organs, on part of the lines; also absent: SPINT1, BSPRY, SMPDL3B; co-absent with the target |
| [[MST1R]] | C | DMKN activity raises MST1R's level | lines that do not express DMKN (24) vs lines expressing it (26) | 3.19× lower at baseline in the lines without DMKN | 0.018 | ⚠ within organs, on part of the lines; also absent: SPINT1, BSPRY, SMPDL3B; co-absent with the target |
| [[BSPRY]] | C | DMKN activity raises BSPRY's level | lines that do not express DMKN (24) vs lines expressing it (26) | 3.41× lower at baseline in the lines without DMKN | 0.035 | ⚠ within organs, on part of the lines; also absent: SPINT1, BSPRY, SMPDL3B; co-absent with the target |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.311). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (14.8, 50.6); signed map (69.4, 12.4). **Vector** length 40.0, 8.17% of its response variance represented; |z| ≥ 3 in 368 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +8.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +14.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +14.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.6 | +4.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.5 | +7.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +0.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.3 | +2.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.2 | +2.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -2.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.3 | -2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.3 | -2.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -2.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -2.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.9 | -2.2 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -0.9 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | dermokine |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.12 — chr19:35,497,220-35,513,658 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZD52F10 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6E0U4](https://www.uniprot.org/uniprotkb/Q6E0U4) (Dermokine):

> May act as a soluble regulator of keratinocyte differentiation.

**Summary**, from NCBI Gene [93099](https://www.ncbi.nlm.nih.gov/gene/93099):

> This gene is upregulated in inflammatory diseases, and it was first observed as expressed in the differentiated layers of skin. The most interesting aspect of this gene is the differential use of promoters and terminators to generate isoforms with unique cellular distributions and domain components. Alternatively spliced transcript variants encoding different isoforms have been identified for this gene. [provided by RefSeq, Jun 2010]

**Accessions** — [HGNC:25063](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25063) · Entrez [93099](https://www.ncbi.nlm.nih.gov/gene/93099) · UniProt [Q6E0U4](https://www.uniprot.org/uniprotkb/Q6E0U4) · Ensembl [ENSG00000161249](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161249)

## Data

Gene col 8424: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8424); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8424, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8424]; `tensor/DDL_lfc|DDL_z.npy` [8424]; `embed/gene_vectors.npy` [8424]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8424 or target_col == 8424). Every well: [[DMKN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DMKN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
