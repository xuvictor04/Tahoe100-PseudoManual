---
symbol: "ILDR2"
type: "gene"
col: 6695
ensembl_id: "ENSG00000143195"
name: "immunoglobulin like domain containing receptor 2"
location: "1q24.1"
module: 44
arm: "+"
pooled_cpm: 3.02
n_lines_expressing: 19
n_dd_up: 33
n_dd_down: 1
n_dd_up_clean: 19
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 10
direction_downstream: 5
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# ILDR2

*immunoglobulin like domain containing receptor 2* — 1q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (14 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 4.69× (z +17.1, q 0e+00, up in 11 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Clopidogrel (drug)]] 0.05 µM: 0.579× (z -4.3, q 0.009, down in 2 of 16 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 20 here, 9 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (LS 180 0.0210×, LoVo 0.292×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LS 180 0.195×, COLO 205 0.149×); [[Harringtonine (drug)]] 5 µM in 1 line (LS 180 0.0380×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (LS 180 0.0565×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPA33]] (+0.75, fdr 7e-06), [[PCK1]] (+0.75, fdr 7e-06), [[LINC02331]] (+0.72, fdr 7e-06).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[LRP4]] → it (grade B ⚠); 5 go from it, the strongest it → [[FAM83F]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6695.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **4.69×** | +17.1 | 0e+00 | 11/14 (LoVo, CFPAC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.17×** | +15.8 | 0e+00 | 2/13 (SNU-423, J82) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.36×** | +12.6 | 3e-34 | 1/3 (SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.69×** | +12.1 | 2e-31 | 1/4 (SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **4.11×** | +10.9 | 2e-25 | 11/13 (LoVo, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.23×** | +10.4 | 2e-23 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **3.72×** | +10.3 | 8e-23 | 7/13 (SNU-423, RKO, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **3.58×** | +10.0 | 2e-21 | 8/15 (SW 900, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.26×** | +9.0 | 2e-17 | 7/12 (SW480, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.99×** | +8.6 | 6e-16 | 11/15 (HCT15, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.94×** | +8.4 | 2e-15 | 14/16 (SHP-77, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.93×** | +8.4 | 2e-15 | 8/14 (SHP-77, SW 900, …) | rises with dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.53×** | +7.0 | 1e-10 | 0/6 | top dose only | cell-cycle shift (explains ~16% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.07×** | +5.7 | 6e-07 | 0/8 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.44×** | +5.0 | 3e-05 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.86×** | +4.8 | 5e-05 | 3/9 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.41×** | +3.8 | 0.005 | 0/15 | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.63×** | +3.8 | 0.005 | 3/11 (SW480, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.48×** | +3.7 | 0.005 | 3/12 (SNU-423, RKO, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.39×** | +3.6 | 0.007 | 1/15 (LoVo) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.82×** | +3.3 | 0.021 | 0/9 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6695.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 20 here, 9 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (LS 180 0.0210×, LoVo 0.292×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LS 180 0.195×, COLO 205 0.149×); [[Harringtonine (drug)]] 5 µM in 1 line (LS 180 0.0380×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (LS 180 0.0565×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clopidogrel (drug)]] 0.05 µM |  | **0.579×** | -4.3 | 0.009 | 2/16 (J82, RKO) | inconsistent across doses |  |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | 0.624× | -3.4 | 0.16 | 1/16 (C-33 A) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM |  | 0.743× | -3.3 | 0.16 | 4/16 (SNU-423, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6695. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 39.4 | 0 | 23 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0210× (z -29.2) |
| [[COLO 205 (line)]] | alt | 22.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.149× (z -10.0) |
| [[LoVo (line)]] | wt | 10.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -9.1) |
| [[RKO (line)]] | wt | 10.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.100× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SNU-423 (line)]] | alt | 3.75 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 19.2× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 12.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.143× (z -9.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 0.440 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.509 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.552 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.394 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.610 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.648 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.452 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.399 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.837 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.606 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.404 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.454 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.417 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.411 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.345 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.636 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.513 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.979 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.346 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.462 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.314 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.404 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.309 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.345 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.363 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.338 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.666 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.568 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.337 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.376 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.802 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.965 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.544 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.395 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.950 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.350 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.88 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6695), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPA33]] | +0.75 | +0.83 / +0.62 | both halves | 7e-06 |  |
| [[PCK1]] | +0.75 | +0.68 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[LINC02331]] | +0.72 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[NPSR1]] | +0.71 | +0.73 / +0.57 | both halves | 8e-06 |  |
| [[ST6GALNAC1]] | +0.71 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[PRR15L]] | +0.70 | +0.75 / +0.59 | both halves | 7e-06 |  |
| [[LRP4]] | +0.70 | +0.61 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[C9orf152]] | +0.70 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[CFTR]] | +0.69 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[LINC01819]] | +0.69 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[CDH17]] | +0.68 | +0.74 / +0.58 | both halves | 7e-06 |  |
| [[ATP10B]] | +0.68 | +0.70 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 2, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRP4]] | B | LRP4 activity raises ILDR2's level | lines that do not express LRP4 (16) vs lines expressing it (34) | 1.75× lower at baseline in the lines without LRP4 | 0.050 | ⚠ within organs, on part of the lines |
| [[NMU]] | B | NMU activity raises ILDR2's level | lines that do not express NMU (18) vs lines expressing it (32) | 1.69× lower at baseline in the lines without NMU | 0.099 | ⚠ within organs, on part of the lines; also absent: S100A2, ANK3, FAM83F; maybe low, not absent |
| [[CALB1]] | C | CALB1 activity raises ILDR2's level | lines that do not express CALB1 (42) vs lines expressing it (8) | 3.87× lower at baseline in the lines without CALB1 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT5, ENSG00000230975, ENSG00000248588; co-absent with the target |
| [[ACSL5]] | C | ACSL5 activity raises ILDR2's level | lines that do not express ACSL5 (24) vs lines expressing it (26) | 2.24× lower at baseline in the lines without ACSL5 | 0.030 | ⚠ within organs, on part of the lines; also absent: TNFRSF14-AS1, IL20RA, TINAGL1; co-absent with the target |
| [[PIGR]] | C | PIGR activity raises ILDR2's level | lines that do not express PIGR (45) vs lines expressing it (5) | 2.26× lower at baseline in the lines without PIGR | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, TM4SF4, APOB; co-absent with the target |
| [[MUC6]] | C | MUC6 activity raises ILDR2's level | lines that do not express MUC6 (45) vs lines expressing it (5) | 2.32× lower at baseline in the lines without MUC6 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, ENSG00000230975, APOB; co-absent with the target |
| [[GRIN2B]] | C | GRIN2B activity raises ILDR2's level | lines that do not express GRIN2B (40) vs lines expressing it (10) | 3.56× lower at baseline in the lines without GRIN2B | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000237031, ENSG00000248588; co-absent with the target |
| [[LGR5]] | C | LGR5 activity raises ILDR2's level | lines that do not express LGR5 (39) vs lines expressing it (11) | 3.24× lower at baseline in the lines without LGR5 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PCK1, DSG4, ENSG00000260573; co-absent with the target |
| [[NKD1]] | C | NKD1 activity raises ILDR2's level | lines that do not express NKD1 (34) vs lines expressing it (16) | 3.12× lower at baseline in the lines without NKD1 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000265554, VSNL1, ENSG00000213981; co-absent with the target |
| [[EDAR]] | C | EDAR activity raises ILDR2's level | lines that do not express EDAR (36) vs lines expressing it (14) | 2.76× lower at baseline in the lines without EDAR | 0.053 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, KLK10, DSG3; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM83F]] | C | ILDR2 activity raises FAM83F's level | lines that do not express ILDR2 (31) vs lines expressing it (19) | 3.78× lower at baseline in the lines without ILDR2 | 0.003 | ⚠ within organs, on part of the lines; also absent: NKD1, ENSG00000265554, PADI1; co-absent with the target |
| [[B3GALT5]] | C | ILDR2 activity raises B3GALT5's level | lines that do not express ILDR2 (31) vs lines expressing it (19) | 2.32× lower at baseline in the lines without ILDR2 | 0.067 | ⚠ within organs, on part of the lines; also absent: NKD1, ENSG00000265554, PADI1; co-absent with the target |
| [[PARM1]] | C | ILDR2 activity raises PARM1's level | lines that do not express ILDR2 (31) vs lines expressing it (19) | 2.60× lower at baseline in the lines without ILDR2 | 0.071 | ⚠ within organs, on part of the lines; also absent: NKD1, ENSG00000265554, PADI1; co-absent with the target |
| [[ZNF439]] | C | ILDR2 activity raises ZNF439's level | lines that do not express ILDR2 (31) vs lines expressing it (19) | 1.74× lower at baseline in the lines without ILDR2 | 0.083 | ⚠ within organs, on part of the lines; also absent: NKD1, ENSG00000265554, PADI1; co-absent with the target |
| [[EDAR]] | C | ILDR2 activity raises EDAR's level | lines that do not express ILDR2 (31) vs lines expressing it (19) | 2.46× lower at baseline in the lines without ILDR2 | 0.092 | ⚠ within organs, on part of the lines; also absent: NKD1, ENSG00000265554, PADI1; co-absent with the target |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.719). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.7, 49.9); signed map (64.0, 6.7). **Vector** length 40.4, 10.1% of its response variance represented; |z| ≥ 3 in 463 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Defective GALNT12 causes CRCS1* (reactome, mean cos +0.53 to 5); *Defective GALNT3 causes HFTC* (reactome, mean cos +0.53 to 5); *Defective C1GALT1C1 causes TNPS* (reactome, mean cos +0.53 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +17.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.1 | +10.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.0 | +12.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.8 | +12.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.7 | +10.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +10.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.2 | +0.2 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +1.1 | +1.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +0.8 | +1.0 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -0.9 | -0.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.9 | -1.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.8 | -1.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.8 | -2.4 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.8 | -1.6 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.7 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | immunoglobulin like domain containing receptor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q24.1 — chr1:166,895,711-166,975,540 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C1orf32 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q71H61](https://www.uniprot.org/uniprotkb/Q71H61) (Immunoglobulin-like domain-containing receptor 2):

> May be involved in ER stress pathways with effects on lipid homeostasis and insulin secretion. With ILDR1 and LSR, involved in the maintain of the epithelial barrier function through the recruitment of MARVELD2/tricellulin to tricellular tight junctions (By similarity). Also functions as a B7-like protein family member expressed on immune cells and inflamed tissue and with T-cell inhibitory activity. In the inner ear, may regulate alternative pre-mRNA splicing via binding to TRA2A, TRA2B and …

**Summary**, from NCBI Gene [387597](https://www.ncbi.nlm.nih.gov/gene/387597):

> Involved in negative regulation of T cell activation. Predicted to be located in tight junction. Predicted to be active in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18131](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18131) · Entrez [387597](https://www.ncbi.nlm.nih.gov/gene/387597) · UniProt [Q71H61](https://www.uniprot.org/uniprotkb/Q71H61) · Ensembl [ENSG00000143195](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143195)

## Data

Gene col 6695: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6695); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6695, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6695]; `tensor/DDL_lfc|DDL_z.npy` [6695]; `embed/gene_vectors.npy` [6695]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6695 or target_col == 6695). Every well: [[ILDR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ILDR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
