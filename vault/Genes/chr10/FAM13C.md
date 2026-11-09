---
symbol: "FAM13C"
type: "gene"
col: 7295
ensembl_id: "ENSG00000148541"
name: "family with sequence similarity 13 member C"
location: "10q21.1"
module: 9
arm: "+"
pooled_cpm: 2.38
n_lines_expressing: 35
n_dd_up: 25
n_dd_down: 0
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 19
direction_downstream: 15
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# FAM13C

*family with sequence similarity 13 member C* — 10q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.06× (z +9.4, q 2e-18, up in 7 of 17 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 5 µM in 2 lines (SNU-423 0.159×, SHP-77 0.126×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (SHP-77 0.0615×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-423 0.217×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (SNU-423 0.152×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POU6F2]] (+0.61, fdr 1e-05), [[SGCD]] (+0.59, fdr 1e-05), [[GRIK4]] (+0.58, fdr 1e-05); moves opposite to [[VKORC1L1]] (-0.46, fdr 2e-04).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[LINC01611]] → it (grade B ⚠); 15 go from it, the strongest it → [[APLN]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7295.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.06×** | +9.4 | 2e-18 | 7/17 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.99×** | +9.0 | 6e-17 | 6/20 (SK-MEL-2, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.73×** | +8.9 | 7e-17 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.18×** | +6.7 | 4e-09 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.87×** | +5.6 | 3e-06 | 1/9 (NCI-H460) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.80×** | +5.4 | 5e-06 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.67×** | +4.8 | 1e-04 | 1/7 (SW480) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.67×** | +4.7 | 1e-04 | 16/28 (HOP62, SW480, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.41×** | +4.5 | 5e-04 | 3/26 (NCI-H460, A-172, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.62×** | +4.5 | 5e-04 | 8/24 (SW480, A-172, …) | all doses, stronger at high dose |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.93×** | +4.3 | 8e-04 | 1/7 (C32) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.35×** | +3.9 | 0.004 | 5/27 (A498, NCI-H460, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +3.9 | 0.004 | 4/19 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.52×** | +3.8 | 0.005 | 3/23 (BT-474, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.38×** | +3.7 | 0.010 | 4/25 (SW480, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +3.5 | 0.015 | 5/26 (NCI-H460, NCI-H23, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.46×** | +3.5 | 0.016 | 7/22 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.47×** | +3.4 | 0.020 | 6/15 (SW480, HOP62, …) | all doses, flat |  |
| [[Darinaparsin (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.020 | 2/26 (NCI-H1792, J82) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.26×** | +3.0 | 0.069 | 6/25 (NCI-H1792, hTERT-HPNE, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.37×** | +2.9 | 0.082 | 5/21 (SW480, HOP62, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7295.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 5 µM in 2 lines (SNU-423 0.159×, SHP-77 0.126×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (SHP-77 0.0615×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-423 0.217×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (SNU-423 0.152×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | 0.689× | -3.5 | 0.16 | 9/29 (H4, LS 180, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.698× | -3.4 | 0.16 | 6/25 (NCI-H1792, H4, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.700× | -3.3 | 0.16 | 10/25 (SNU-423, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.712× | -3.1 | 0.32 | 6/28 (SHP-77, CHP-212, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7295. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 20.9 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -10.9) |
| [[SHP-77 (line)]] | alt | 12.7 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0615× (z -11.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 7.25 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 16.4× (z +14.4) | [[Belinostat (drug)]] 0.5 µM 0.0929× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.453 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.833 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.588 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.870 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.454 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.631 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.05 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.532 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.465 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.642 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.684 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.835 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.923 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.532 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.04 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.458 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.864 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.682 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.511 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.554 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.712 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.812 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.407 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.691 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.410 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.516 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.498 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.743 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.524 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.504 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.976 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.50 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7295), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POU6F2]] | +0.61 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[SGCD]] | +0.59 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[GRIK4]] | +0.58 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[LINC00491]] | +0.57 | +0.62 / +0.38 | both halves | 6e-05 |  |
| [[LINC01287]] | +0.57 | +0.58 / +0.40 | both halves | 5e-05 |  |
| [[LINC01807]] | +0.55 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[CCL28]] | +0.54 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[MTCP1]] | +0.54 | +0.55 / +0.41 | both halves | 4e-05 |  |
| [[PTCHD4]] | +0.54 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[CDH12]] | +0.54 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[RALYL]] | +0.54 | +0.58 / +0.39 | both halves | 5e-05 |  |
| [[KC6]] | +0.54 | +0.47 / +0.54 | both halves | 2e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VKORC1L1]] | -0.46 | -0.49 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 18, C 1. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01611]] | B | LINC01611 activity raises FAM13C's level | lines that do not express LINC01611 (34) vs lines expressing it (16) | 2.63× lower at baseline in the lines without LINC01611 | 0.004 | ⚠ within organs, on part of the lines; also absent: CDH13, ENSG00000248973, LINC02377 |
| [[GNG2]] | B | GNG2 activity raises FAM13C's level | lines that do not express GNG2 (22) vs lines expressing it (28) | 2.16× lower at baseline in the lines without GNG2 | 0.011 | ⚠ within organs, on part of the lines; also absent: SNAI2, LBH, PLAT |
| [[LINC00491]] | B | LINC00491 activity raises FAM13C's level | lines that do not express LINC00491 (33) vs lines expressing it (17) | 2.68× lower at baseline in the lines without LINC00491 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: APCDD1L, LINC01905, ADGRG7 |
| [[POU3F2]] | B | POU3F2 activity raises FAM13C's level | lines that do not express POU3F2 (32) vs lines expressing it (18) | 2.30× lower at baseline in the lines without POU3F2 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MSR1, AMPH, SPARC |
| [[FRMPD4]] | B | FRMPD4 activity raises FAM13C's level | lines that do not express FRMPD4 (24) vs lines expressing it (26) | 2.10× lower at baseline in the lines without FRMPD4 | 0.024 | ⚠ within organs, on part of the lines; also absent: COL4A1, BICC1, NTF3 |
| [[TEX41]] | B | TEX41 activity raises FAM13C's level | lines that do not express TEX41 (29) vs lines expressing it (21) | 1.90× lower at baseline in the lines without TEX41 | 0.031 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000280241, ADAM12 |
| [[RUNX1T1]] | B | RUNX1T1 activity raises FAM13C's level | lines that do not express RUNX1T1 (38) vs lines expressing it (12) | 1.62× lower at baseline in the lines without RUNX1T1 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, ENSG00000232252, SYT4 |
| [[HTR2C]] | B | HTR2C activity raises FAM13C's level | lines that do not express HTR2C (22) vs lines expressing it (28) | 1.83× lower at baseline in the lines without HTR2C | 0.039 | ⚠ within organs, on part of the lines; also absent: ENSG00000234156, KCNJ6, PTPRN; maybe low, not absent |
| [[APLN]] | B | APLN activity raises FAM13C's level | lines that do not express APLN (13) vs lines expressing it (37) | 1.77× lower at baseline in the lines without APLN | 0.039 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[LINC01287]] | B | LINC01287 activity raises FAM13C's level | lines that do not express LINC01287 (39) vs lines expressing it (11) | 1.94× lower at baseline in the lines without LINC01287 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253642, POU6F2, RIT2 |
| [[GRIK2]] | B | GRIK2 activity raises FAM13C's level | lines that do not express GRIK2 (19) vs lines expressing it (31) | 1.86× lower at baseline in the lines without GRIK2 | 0.044 | ⚠ within organs, on part of the lines; also absent: MIR9-3HG, PCDH10, PLEKHG4B |
| [[ZNF883]] | B | ZNF883 activity raises FAM13C's level | lines that do not express ZNF883 (22) vs lines expressing it (28) | 1.96× lower at baseline in the lines without ZNF883 | 0.048 | ⚠ within organs, on part of the lines; also absent: AK5, SOX5, GAP43 |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 14, C 1. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APLN]] | B | FAM13C activity raises APLN's level | lines that do not express FAM13C (15) vs lines expressing it (35) | 1.78× lower at baseline in the lines without FAM13C | 0.009 | ⚠ within organs, on part of the lines; also absent: DENND2A, SOX5, ANK2; maybe low, not absent |
| [[REV3L]] | B | FAM13C activity raises REV3L's level | lines that do not express FAM13C (15) vs lines expressing it (35) | 1.85× lower at baseline in the lines without FAM13C | 0.030 | ⚠ within organs, on part of the lines; also absent: DENND2A, SOX5, ANK2; maybe low, not absent |
| [[EPHA3]] | B | FAM13C activity raises EPHA3's level | lines that do not express FAM13C (15) vs lines expressing it (35) | 3.16× lower at baseline in the lines without FAM13C | 0.032 | ⚠ within organs, on part of the lines; also absent: DENND2A, SOX5, ANK2; maybe low, not absent |
| [[TMEM45A]] | B | FAM13C activity raises TMEM45A's level | lines that do not express FAM13C (15) vs lines expressing it (35) | 3.55× lower at baseline in the lines without FAM13C | 0.035 | ⚠ within organs, on part of the lines; also absent: DENND2A, SOX5, ANK2; maybe low, not absent |
| [[PINCR]] | B | FAM13C activity raises PINCR's level | lines that do not express FAM13C (15) vs lines expressing it (35) | 2.00× lower at baseline in the lines without FAM13C | 0.048 | ⚠ within organs, on part of the lines; also absent: DENND2A, SOX5, ANK2; maybe low, not absent |
| [[ARHGAP25]] | B | FAM13C activity raises ARHGAP25's level | lines that do not express FAM13C (15) vs lines expressing it (35) | 1.89× lower at baseline in the lines without FAM13C | 0.056 | ⚠ within organs, on part of the lines; also absent: DENND2A, SOX5, ANK2; maybe low, not absent |
| [[TET1]] | B | FAM13C activity raises TET1's level | lines that do not express FAM13C (15) vs lines expressing it (35) | 2.92× lower at baseline in the lines without FAM13C | 0.060 | ⚠ within organs, on part of the lines; also absent: DENND2A, SOX5, ANK2; maybe low, not absent |
| [[NPAS3]] | B | FAM13C activity raises NPAS3's level | lines that do not express FAM13C (15) vs lines expressing it (35) | 3.11× lower at baseline in the lines without FAM13C | 0.073 | ⚠ within organs, on part of the lines; also absent: DENND2A, SOX5, ANK2; maybe low, not absent |
| cells under [[Entecavir (monohydrate) (drug)]] 5 µM | B | FAM13C activity raises the cells' numbers under Entecavir (monohydrate) 5 µM (protects the cells) | lines that do not express FAM13C (15) vs lines expressing it (33) | the lines without FAM13C: 0.81× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: DENND2A, SOX5, ANK2; maybe low, not absent |
| cells under [[Posaconazole (drug)]] 5 µM | B | FAM13C activity raises the cells' numbers under Posaconazole 5 µM (protects the cells) | lines that do not express FAM13C (15) vs lines expressing it (33) | the lines without FAM13C: 0.84× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: DENND2A, SOX5, ANK2; maybe low, not absent |
| [[GNG2]] | B | FAM13C activity raises GNG2's level | lines that do not express FAM13C (15) vs lines expressing it (35) | 3.48× lower at baseline in the lines without FAM13C | 0.085 | ⚠ within organs, on part of the lines; also absent: DENND2A, SOX5, ANK2; maybe low, not absent |
| [[PTCHD4]] | B | FAM13C activity raises PTCHD4's level | lines that do not express FAM13C (15) vs lines expressing it (35) | 3.28× lower at baseline in the lines without FAM13C | 0.089 | ⚠ within organs, on part of the lines; also absent: DENND2A, SOX5, ANK2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.491). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (28.9, 35.5); signed map (39.6, 18.1). **Vector** length 52.3, 10.5% of its response variance represented; |z| ≥ 3 in 764 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +5.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +8.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +6.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.4 | +9.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +9.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +4.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.0 | +3.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.8 | +4.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +4.7 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.9 | -1.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.8 | -0.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -3.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -1.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.5 | -3.3 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.3 | -1.7 |
|  | [[(S)-Crizotinib (drug)]] 0.05 µM |  | -1.2 | -0.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -2.3 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.1 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 13 member C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q21.1 — chr10:59,246,130-59,363,181 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously FAM13C1 |
| Matched by | ensembl_id |

UniProt [Q8NE31](https://www.uniprot.org/uniprotkb/Q8NE31) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:19371](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19371) · Entrez [220965](https://www.ncbi.nlm.nih.gov/gene/220965) · UniProt [Q8NE31](https://www.uniprot.org/uniprotkb/Q8NE31) · Ensembl [ENSG00000148541](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148541)

## Data

Gene col 7295: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7295); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7295, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7295]; `tensor/DDL_lfc|DDL_z.npy` [7295]; `embed/gene_vectors.npy` [7295]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7295 or target_col == 7295). Every well: [[FAM13C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM13C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
