---
symbol: "ASXL3"
type: "gene"
col: 6518
ensembl_id: "ENSG00000141431"
name: "ASXL transcriptional regulator 3"
location: "18q12.1"
module: 9
arm: "+"
pooled_cpm: 3.32
n_lines_expressing: 20
n_dd_up: 21
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 23
direction_downstream: 13
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# ASXL3

*ASXL transcriptional regulator 3* — 18q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (7 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 4.12× (z +15.0, q 0e+00, up in 12 of 15 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.195×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.406×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (CHP-212 0.0973×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBM20]] (+0.74, fdr 7e-06), [[KCNH7]] (+0.73, fdr 2e-05), [[KCNJ6]] (+0.70, fdr 1e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 23 arrows point to it, the strongest [[ASCL1]] → it (grade C ⚠); 13 go from it, the strongest it → [[SEMA6A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6518.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **4.12×** | +15.0 | 0e+00 | 12/15 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.76×** | +10.8 | 2e-24 | 0/9 | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.30×** | +8.6 | 2e-15 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.97×** | +7.6 | 4e-12 | 10/12 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.57×** | +6.5 | 8e-09 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.06×** | +6.0 | 2e-07 | 0/3 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.11×** | +5.6 | 2e-06 | 1/7 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.53×** | +4.9 | 5e-05 | 1/5 (CHP-212) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.87×** | +4.7 | 2e-04 | 8/14 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.53×** | +4.5 | 4e-04 | 2/15 (H4, HOP62) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.99×** | +4.3 | 1e-03 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.90×** | +4.2 | 0.002 | 0/2 | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.46×** | +4.0 | 0.003 | 3/9 (NCI-H661, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~25% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.64×** | +3.7 | 0.009 | 8/15 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.61×** | +3.6 | 0.014 | 0/5 | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.57×** | +3.3 | 0.029 | 3/9 (NCI-H460, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.58×** | +3.2 | 0.044 | 1/14 (NCI-H460) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Carbamazepine (drug)]] 5 µM |  | **1.53×** | +3.1 | 0.050 | 0/13 | top dose only |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.56×** | +3.1 | 0.052 | 0/10 | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.50×** | +3.0 | 0.069 | 7/13 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.195×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.406×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (CHP-212 0.0973×; ⚠ toxic; transcription drop).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6518. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 117 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.195× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -9.4) |
| [[CHP-212 (line)]] | wt | 41.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0973× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 1.85 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 10.7× (z +8.5) | — |
| [[PANC-1 (line)]] | alt | 1.47 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 9.36× (z +9.6) | — |
| [[A-172 (line)]] | wt | 0.470 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 4.78 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.452 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.493 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.555 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.861 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.497 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.982 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.559 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.621 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.590 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.552 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.534 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.674 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.668 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.481 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.504 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.764 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.708 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.609 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.463 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.595 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.705 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.381 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.534 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.511 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.499 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.664 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.621 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.704 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.514 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.710 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.633 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6518), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM20]] | +0.74 | +0.66 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[KCNH7]] | +0.73 | +0.48 / +0.84 | both halves | 2e-05 | **novel candidate** |
| [[KCNJ6]] | +0.70 | +0.53 / +0.75 | both halves | 1e-05 | **novel candidate** |
| [[MARCHF1]] | +0.70 | +0.49 / +0.71 | both halves | 1e-05 | **novel candidate** |
| [[NKAIN2]] | +0.70 | +0.57 / +0.74 | both halves | 9e-06 | **novel candidate** |
| [[GRIA2]] | +0.69 | +0.50 / +0.77 | both halves | 1e-05 |  |
| [[CDH10]] | +0.68 | +0.59 / +0.74 | both halves | 7e-06 |  |
| [[ADGRL3]] | +0.68 | +0.59 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[IQCM]] | +0.68 | +0.55 / +0.66 | both halves | 1e-05 | **novel candidate** |
| [[SNCA]] | +0.67 | +0.58 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[TMEM108]] | +0.65 | +0.39 / +0.75 | both halves | 6e-05 |  |
| [[NCAM2]] | +0.65 | +0.42 / +0.69 | both halves | 4e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 0, C 23. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ASCL1]] | C | ASCL1 activity raises ASXL3's level | lines that do not express ASCL1 (41) vs lines expressing it (9) | 4.35× lower at baseline in the lines without ASCL1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ENSG00000275016, SYT4; co-absent with the target |
| [[KCNH5]] | C | KCNH5 activity raises ASXL3's level | lines that do not express KCNH5 (36) vs lines expressing it (14) | 3.68× lower at baseline in the lines without KCNH5 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ASCL1, ENSG00000260958, UNC5D; co-absent with the target |
| [[SRRM4]] | C | SRRM4 activity raises ASXL3's level | lines that do not express SRRM4 (41) vs lines expressing it (9) | 3.08× lower at baseline in the lines without SRRM4 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: KCNB2, RIT2, CALCA; maybe low, not absent; co-absent with the target |
| [[LINC02197]] | C | LINC02197 activity raises ASXL3's level | lines that do not express LINC02197 (35) vs lines expressing it (15) | 2.35× lower at baseline in the lines without LINC02197 | 0.017 | ⚠ within organs, on part of the lines; also absent: RIT2, SNTG1, CALCA; maybe low, not absent; co-absent with the target |
| [[FUT9]] | C | FUT9 activity raises ASXL3's level | lines that do not express FUT9 (40) vs lines expressing it (10) | 4.52× lower at baseline in the lines without FUT9 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, KCNH7, GCG; co-absent with the target |
| [[LINC01518]] | C | LINC01518 activity raises ASXL3's level | lines that do not express LINC01518 (36) vs lines expressing it (14) | 2.61× lower at baseline in the lines without LINC01518 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000285822, CCDC144NL-AS1, PHF2P2; co-absent with the target |
| [[RUNX1T1]] | C | RUNX1T1 activity raises ASXL3's level | lines that do not express RUNX1T1 (38) vs lines expressing it (12) | 3.13× lower at baseline in the lines without RUNX1T1 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, ENSG00000232252, SYT4; co-absent with the target |
| [[LINC01035]] | C | LINC01035 activity raises ASXL3's level | lines that do not express LINC01035 (43) vs lines expressing it (7) | 5.03× lower at baseline in the lines without LINC01035 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, CALCA, GSG1L2; co-absent with the target |
| [[GABRG2]] | C | GABRG2 activity raises ASXL3's level | lines that do not express GABRG2 (36) vs lines expressing it (14) | 2.16× lower at baseline in the lines without GABRG2 | 0.041 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, PCSK1, BAGE2; maybe low, not absent; co-absent with the target |
| [[KCNH7]] | C | KCNH7 activity raises ASXL3's level | lines that do not express KCNH7 (35) vs lines expressing it (15) | 2.97× lower at baseline in the lines without KCNH7 | 0.042 | ⚠ within organs, on part of the lines; also absent: FUT9, ENSG00000289309, PI15; maybe low, not absent; co-absent with the target |
| [[CDH10]] | C | CDH10 activity raises ASXL3's level | lines that do not express CDH10 (37) vs lines expressing it (13) | 3.69× lower at baseline in the lines without CDH10 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01035, FUT9, KCNH5; co-absent with the target |
| [[CCDC144NL-AS1]] | C | CCDC144NL-AS1 activity raises ASXL3's level | lines that do not express CCDC144NL-AS1 (33) vs lines expressing it (17) | 2.29× lower at baseline in the lines without CCDC144NL-AS1 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000264660, LINC01518, ENSG00000287861; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 3, C 10. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEMA6A]] | B | ASXL3 activity raises SEMA6A's level | lines that do not express ASXL3 (30) vs lines expressing it (20) | 2.24× lower at baseline in the lines without ASXL3 | 0.030 | ⚠ within organs, on part of the lines; also absent: VIPR2, NOL4, KCNH5; maybe low, not absent |
| [[LINC00461]] | B | ASXL3 activity raises LINC00461's level | lines that do not express ASXL3 (30) vs lines expressing it (20) | 1.79× lower at baseline in the lines without ASXL3 | 0.086 | ⚠ within organs, on part of the lines; also absent: VIPR2, NOL4, KCNH5; maybe low, not absent |
| [[VWA5A]] | B | ASXL3 activity raises VWA5A's level | lines that do not express ASXL3 (30) vs lines expressing it (20) | 1.55× lower at baseline in the lines without ASXL3 | 0.087 | ⚠ within organs, on part of the lines; also absent: VIPR2, NOL4, KCNH5; maybe low, not absent |
| [[NOL4]] | C | ASXL3 activity raises NOL4's level | lines that do not express ASXL3 (30) vs lines expressing it (20) | 2.95× lower at baseline in the lines without ASXL3 | 0.011 | ⚠ within organs, on part of the lines; also absent: VIPR2, NOL4, KCNH5; maybe low, not absent; co-absent with the target |
| [[GABRA2]] | C | ASXL3 activity raises GABRA2's level | lines that do not express ASXL3 (30) vs lines expressing it (20) | 2.07× lower at baseline in the lines without ASXL3 | 0.040 | ⚠ within organs, on part of the lines; also absent: VIPR2, NOL4, KCNH5; maybe low, not absent; co-absent with the target |
| [[ADARB2]] | C | ASXL3 activity raises ADARB2's level | lines that do not express ASXL3 (30) vs lines expressing it (20) | 3.11× lower at baseline in the lines without ASXL3 | 0.044 | ⚠ within organs, on part of the lines; also absent: VIPR2, NOL4, KCNH5; maybe low, not absent; co-absent with the target |
| [[FGF14]] | C | ASXL3 activity raises FGF14's level | lines that do not express ASXL3 (30) vs lines expressing it (20) | 3.12× lower at baseline in the lines without ASXL3 | 0.053 | ⚠ within organs, on part of the lines; also absent: VIPR2, NOL4, KCNH5; maybe low, not absent; co-absent with the target |
| [[CTNNA2]] | C | ASXL3 activity raises CTNNA2's level | lines that do not express ASXL3 (30) vs lines expressing it (20) | 2.99× lower at baseline in the lines without ASXL3 | 0.058 | ⚠ within organs, on part of the lines; also absent: VIPR2, NOL4, KCNH5; maybe low, not absent; co-absent with the target |
| [[GAS7]] | C | ASXL3 activity raises GAS7's level | lines that do not express ASXL3 (30) vs lines expressing it (20) | 2.12× lower at baseline in the lines without ASXL3 | 0.060 | ⚠ within organs, on part of the lines; also absent: VIPR2, NOL4, KCNH5; maybe low, not absent; co-absent with the target |
| [[KCNH5]] | C | ASXL3 activity raises KCNH5's level | lines that do not express ASXL3 (30) vs lines expressing it (20) | 3.01× lower at baseline in the lines without ASXL3 | 0.064 | ⚠ within organs, on part of the lines; also absent: VIPR2, NOL4, KCNH5; maybe low, not absent; co-absent with the target |
| [[SLC6A15]] | C | ASXL3 activity raises SLC6A15's level | lines that do not express ASXL3 (30) vs lines expressing it (20) | 2.77× lower at baseline in the lines without ASXL3 | 0.079 | ⚠ within organs, on part of the lines; also absent: VIPR2, NOL4, KCNH5; maybe low, not absent; co-absent with the target |
| [[FUT9]] | C | ASXL3 activity raises FUT9's level | lines that do not express ASXL3 (30) vs lines expressing it (20) | 2.49× lower at baseline in the lines without ASXL3 | 0.087 | ⚠ within organs, on part of the lines; also absent: VIPR2, NOL4, KCNH5; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.738). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (39.6, 34.9); signed map (41.9, 37.4). **Vector** length 29.6, 6.43% of its response variance represented; |z| ≥ 3 in 345 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Neuronal System* (reactome, mean cos +0.51 to 15).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.6 | +5.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +8.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +15.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | +6.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.3 | +7.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +2.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +4.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.3 | +2.4 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.6 | -1.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -1.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -1.1 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.2 | -0.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.2 | -1.7 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.1 | -1.4 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.1 | -1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | ASXL transcriptional regulator 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q12.1 — chr18:33,578,219-33,751,195 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously KIAA1713 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9C0F0](https://www.uniprot.org/uniprotkb/Q9C0F0) (Putative Polycomb group protein ASXL3):

> Putative Polycomb group (PcG) protein. PcG proteins act by forming multiprotein complexes, which are required to maintain the transcriptionally repressive state of homeotic genes throughout development. PcG proteins are not required to initiate repression, but to maintain it during later stages of development. They probably act via methylation of histones, rendering chromatin heritably changed in its expressibility (By similarity). Non-catalytic component of the PR-DUB complex, a complex that …

**Summary**, from NCBI Gene [80816](https://www.ncbi.nlm.nih.gov/gene/80816):

> This gene encodes a protein containing a plant homeodomain (PHD) zinc finger domain that plays a role in the regulation of gene transcription. The encoded protein has been shown to negatively regulate lipogenesis by binding to and inhibiting the transcriptional activity of two nuclear hormone receptors, oxysterols receptor LXR-alpha (LXRalpha) and thyroid hormone receptor beta (TRbeta). The encoded protein may also inhibit histone deubiquitination. Mutations in this gene have been identified in …

**Accessions** — [HGNC:29357](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29357) · Entrez [80816](https://www.ncbi.nlm.nih.gov/gene/80816) · UniProt [Q9C0F0](https://www.uniprot.org/uniprotkb/Q9C0F0) · Ensembl [ENSG00000141431](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141431)

## Data

Gene col 6518: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6518); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6518, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6518]; `tensor/DDL_lfc|DDL_z.npy` [6518]; `embed/gene_vectors.npy` [6518]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6518 or target_col == 6518). Every well: [[ASXL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ASXL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
