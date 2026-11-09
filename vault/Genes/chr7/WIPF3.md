---
symbol: "WIPF3"
type: "gene"
col: 4354
ensembl_id: "ENSG00000122574"
name: "WAS/WASL interacting protein family member 3"
location: "7p14.3"
module: 61
arm: "+"
pooled_cpm: 4.95
n_lines_expressing: 29
n_dd_up: 30
n_dd_down: 0
n_dd_up_clean: 20
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 6
direction_downstream: 6
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# WIPF3

*WAS/WASL interacting protein family member 3* — 7p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.01× (z +17.7, q 0e+00, up in 15 of 26 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (A549 0.0662×, SW1417 0.0978×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change); [[Belumosudil (drug)]] 5 µM in 1 line (NCI-H23 0.0465×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.138×); [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM in 1 line (Hs 766T 0.102×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RASGRP1]] (+0.65, fdr 7e-06), [[OLFM2]] (+0.63, fdr 1e-05), [[LINC00937]] (+0.62, fdr 1e-05); moves opposite to [[ATF7]] (-0.48, fdr 2e-05).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[SH3GL2]] → it (grade B ⚠); 6 go from it, the strongest it → [[LINC00592]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4354.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.01×** | +17.7 | 0e+00 | 15/26 (HOP62, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.80×** | +16.6 | 0e+00 | 10/25 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.22×** | +12.8 | 2e-35 | 22/27 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.62×** | +10.9 | 1e-25 | 20/26 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.36×** | +9.4 | 6e-19 | 2/4 (PANC-1, J82) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.95×** | +7.6 | 3e-12 | 14/25 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.96×** | +7.1 | 1e-10 | 1/9 (J82) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.85×** | +7.0 | 2e-10 | 11/26 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.78×** | +6.5 | 4e-09 | 3/17 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.68×** | +5.6 | 1e-06 | 11/27 (BT-474, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.58×** | +5.2 | 1e-05 | 10/27 (HOP62, HCT15, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +4.7 | 1e-04 | 8/23 (A549, NCI-H460, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.13×** | +4.5 | 3e-04 | 2/14 (HEC-1-A, C-33 A) | top dose only | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.62×** | +3.9 | 0.004 | 2/23 (CFPAC-1, C-33 A) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.59×** | +3.8 | 0.006 | 1/12 (SW1417) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.24×** | +3.5 | 0.017 | 6/26 (Panc 03.27, HOP62, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.35×** | +3.4 | 0.020 | 8/27 (PANC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Monocrotaline (drug)]] 0.05 µM |  | **1.38×** | +3.3 | 0.024 | 1/23 (LoVo) | inconsistent across doses |  |
| [[Silodosin (drug)]] 5 µM |  | **1.33×** | +3.1 | 0.053 | 1/22 (NCI-H2030) | top dose only |  |
| [[Saquinavir (drug)]] 5 µM |  | **1.21×** | +3.0 | 0.057 | 5/26 (SK-MEL-2, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (A549 0.0662×, SW1417 0.0978×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change); [[Belumosudil (drug)]] 5 µM in 1 line (NCI-H23 0.0465×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.138×); [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM in 1 line (Hs 766T 0.102×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4354. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 3.52 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 5.43× (z +10.5) | — |
| [[A-427 (line)]] | wt | 29.0 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.138× (z -14.4) |
| [[Hs 766T (line)]] | wt | 8.23 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.02× (z +9.5) | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM 0.102× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 1.53 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.46× (z +8.8) | — |
| [[A549 (line)]] | wt | 6.55 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0662× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change |
| [[BT-474 (line)]] | alt | 3.23 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +9.2) | — |
| [[C-33 A (line)]] | alt | 11.2 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0631× (z -10.4) ⚠ cell-cycle shift, explains ~8% of this change |
| [[CFPAC-1 (line)]] | alt | 2.30 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +10.6) | — |
| [[HOP62 (line)]] | alt | 1.74 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.9× (z +12.7) | — |
| [[LoVo (line)]] | wt | 39.9 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.123× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 3.04 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.0× (z +11.1) | — |
| [[NCI-H23 (line)]] | alt | 12.1 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.0465× (z -14.8) |
| [[SW1417 (line)]] | alt | 6.25 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0978× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change |
| [[SW480 (line)]] | alt | 2.49 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 8.42× (z +11.6) | — |
| [[A-172 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.554 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.687 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.54 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.741 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.675 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.718 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.561 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.767 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.638 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.574 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.571 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.835 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.609 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.604 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.888 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.776 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.638 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4354), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RASGRP1]] | +0.65 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[OLFM2]] | +0.63 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[LINC00937]] | +0.62 | +0.49 / +0.71 | both halves | 1e-05 |  |
| [[GLIPR2]] | +0.61 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[RBFOX3]] | +0.61 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[CDH23]] | +0.60 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[NTN1]] | +0.60 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[RGS7]] | +0.58 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[MEGF11]] | +0.58 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[RHBDL3]] | +0.57 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[PAX5]] | +0.56 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[NEURL1]] | +0.56 | +0.50 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATF7]] | -0.48 | -0.46 / -0.50 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SH3GL2]] | B | SH3GL2 activity raises WIPF3's level | lines that do not express SH3GL2 (18) vs lines expressing it (32) | 1.92× lower at baseline in the lines without SH3GL2 | 0.045 | ⚠ within organs, on part of the lines; also absent: FAM124A, SLC16A10, OLFM1; maybe low, not absent |
| [[ENTREP1]] | B | ENTREP1 activity raises WIPF3's level | lines that do not express ENTREP1 (18) vs lines expressing it (32) | 1.68× lower at baseline in the lines without ENTREP1 | 0.047 | ⚠ within organs, on part of the lines; also absent: LHX2, OLFM1, COL4A4 |
| [[KCNG3]] | B | KCNG3 activity raises WIPF3's level | lines that do not express KCNG3 (20) vs lines expressing it (30) | 1.85× lower at baseline in the lines without KCNG3 | 0.060 | ⚠ within organs, on part of the lines; also absent: ELOVL2, LHX2, MAPK8IP2 |
| [[RASGEF1C]] | B | RASGEF1C activity raises WIPF3's level | lines that do not express RASGEF1C (14) vs lines expressing it (36) | 1.46× lower at baseline in the lines without RASGEF1C | 0.099 | ⚠ within organs, on part of the lines; also absent: FAM124A, RAB6B, STOX2; maybe low, not absent |
| [[STOX2]] | C | STOX2 activity raises WIPF3's level | lines that do not express STOX2 (22) vs lines expressing it (28) | 1.92× lower at baseline in the lines without STOX2 | 0.008 | ⚠ within organs, on part of the lines; also absent: SLC47A1, RBM11, FBXO27; co-absent with the target |
| [[KLHL13]] | C | KLHL13 activity raises WIPF3's level | lines that do not express KLHL13 (23) vs lines expressing it (27) | 1.85× lower at baseline in the lines without KLHL13 | 0.090 | ⚠ within organs, on part of the lines; also absent: IQGAP2, ANKRD20A11P, MAPK4; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00592]] | B | WIPF3 activity raises LINC00592's level | lines that do not express WIPF3 (21) vs lines expressing it (29) | 1.43× lower at baseline in the lines without WIPF3 | 0.032 | ⚠ within organs, on part of the lines; also absent: RBM11, EPB41L4A, COL4A3 |
| [[LGALSL-DT]] | B | WIPF3 activity raises LGALSL-DT's level | lines that do not express WIPF3 (21) vs lines expressing it (29) | 1.46× lower at baseline in the lines without WIPF3 | 0.044 | ⚠ within organs, on part of the lines; also absent: RBM11, EPB41L4A, COL4A3 |
| [[SH3GL2]] | B | WIPF3 activity raises SH3GL2's level | lines that do not express WIPF3 (21) vs lines expressing it (29) | 2.17× lower at baseline in the lines without WIPF3 | 0.057 | ⚠ within organs, on part of the lines; also absent: RBM11, EPB41L4A, COL4A3 |
| [[SDK2]] | B | WIPF3 activity strengthens SDK2's drug response | lines that do not express WIPF3 (13) vs lines expressing it (19) | the lines without WIPF3 respond 0.45× as strongly (z diff +1.72); strongest at Bortezomib 5 µM: 1.31x vs 5.09x (z diff +3.5) | 0.060 | ⚠ within organs, on part of the lines; also absent: RBM11, EPB41L4A, COL4A3; target measured in part of the lines; artifact flags |
| [[RASGRP1]] | B | WIPF3 activity raises RASGRP1's level | lines that do not express WIPF3 (21) vs lines expressing it (29) | 1.39× lower at baseline in the lines without WIPF3 | 0.075 | ⚠ within organs, on part of the lines; also absent: RBM11, EPB41L4A, COL4A3 |
| [[RBM11]] | C | WIPF3 activity raises RBM11's level | lines that do not express WIPF3 (21) vs lines expressing it (29) | 2.21× lower at baseline in the lines without WIPF3 | 0.031 | ⚠ within organs, on part of the lines; also absent: RBM11, EPB41L4A, COL4A3; co-absent with the target |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.624). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (5.2, 35.3); signed map (30.0, 24.0). **Vector** length 58.0, 12.2% of its response variance represented; |z| ≥ 3 in 619 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.9 | +12.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.1 | +10.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.7 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.4 | +6.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.6 | +17.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.6 | +2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +5.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +3.9 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +1.7 | +2.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -2.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.1 | -0.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.9 | -2.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.7 | -2.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.6 | -1.8 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.5 | -1.6 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.5 | -2.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.3 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | WAS/WASL interacting protein family member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p14.3 — chr7:29,806,486-29,917,061 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CR16, FLJ36931 |
| Reactome | 15 pathways, smallest: RHO GTPases Activate WASPs and WAVEs; FCGR3A-mediated phagocytosis; Leishmania phagocytosis |
| Matched by | ensembl_id |

**Function**, from UniProt [A6NGB9](https://www.uniprot.org/uniprotkb/A6NGB9) (WAS/WASL-interacting protein family member 3):

> May be a regulator of cytoskeletal organization. May have a role in spermatogenesis (By similarity).

**Summary**, from NCBI Gene [644150](https://www.ncbi.nlm.nih.gov/gene/644150):

> Predicted to enable actin binding activity and alpha-tubulin binding activity. Predicted to be involved in Arp2/3 complex-mediated actin nucleation; endosomal transport; and exocytosis. Predicted to be located in cytosol. Predicted to be part of WASH complex. Predicted to be active in early endosome; recycling endosome; and synapse. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:22004](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22004) · Entrez [644150](https://www.ncbi.nlm.nih.gov/gene/644150) · UniProt [A6NGB9](https://www.uniprot.org/uniprotkb/A6NGB9) · Ensembl [ENSG00000122574](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122574)

## Data

Gene col 4354: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4354); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4354, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4354]; `tensor/DDL_lfc|DDL_z.npy` [4354]; `embed/gene_vectors.npy` [4354]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4354 or target_col == 4354). Every well: [[WIPF3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WIPF3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
