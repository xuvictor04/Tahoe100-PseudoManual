---
symbol: "NTNG1"
type: "gene"
col: 8549
ensembl_id: "ENSG00000162631"
name: "netrin G1"
location: "1p13.3"
module: 13
arm: "+"
pooled_cpm: 11.14
n_lines_expressing: 17
n_dd_up: 19
n_dd_down: 1
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 12
direction_downstream: 7
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# NTNG1

*netrin G1* — 1p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.43× (z +17.3, q 0e+00, up in 5 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Dihydroartemisinin (drug)]] 5 µM: 0.648× (z -4.3, q 0.007, down in 0 of 14 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Belumosudil (drug)]] 5 µM in 1 line (J82 0.0430×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A498 0.303×); [[Adagrasib (drug)]] 0.05 µM in 1 line (HOP62 0.555×; ⚠ position not correctable).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FGF5]] (+0.63, fdr 1e-05), [[NOL4]] (+0.62, fdr 1e-05), [[CFAP299]] (+0.61, fdr 3e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[LSAMP]] → it (grade B ⚠); 7 go from it, the strongest it → [[PDE4DIPP2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8549.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.43×** | +17.3 | 0e+00 | 5/14 (SK-MEL-2, SNU-423, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.32×** | +11.0 | 1e-25 | 1/9 (SNU-423) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.06×** | +10.7 | 3e-24 | 1/9 (CFPAC-1) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.96×** | +9.5 | 5e-19 | 8/15 (CFPAC-1, SNU-423, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.28×** | +8.2 | 3e-14 | 1/13 (CFPAC-1) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.77×** | +8.0 | 9e-14 | 4/14 (HOP62, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.95×** | +6.6 | 3e-09 | 6/14 (CFPAC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.81×** | +5.9 | 3e-07 | 5/15 (HOP62, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.80×** | +5.8 | 4e-07 | 5/14 (HOP62, A498, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.53×** | +4.2 | 0.001 | 1/14 (BT-474) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.51×** | +4.1 | 0.002 | 9/15 (CFPAC-1, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.49×** | +4.0 | 0.004 | 6/14 (HOP62, BT-474, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +3.8 | 0.007 | 0/14 | top dose only | cell-cycle shift (explains ~13% here) |
| [[vincristine (drug)]] 0.5 µM |  | **1.65×** | +3.6 | 0.016 | 2/14 (SK-MEL-2, H4) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.40×** | +3.3 | 0.035 | 3/14 (SK-MEL-2, H4, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +3.1 | 0.070 | 1/14 (H4) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.36×** | +2.9 | 0.097 | 0/14 | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8549.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Belumosudil (drug)]] 5 µM in 1 line (J82 0.0430×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A498 0.303×); [[Adagrasib (drug)]] 0.05 µM in 1 line (HOP62 0.555×; ⚠ position not correctable).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.648×** | -4.3 | 0.007 | 0/14 | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.880× | -4.2 | 0.007 | 2/15 (HOP62, SW 1088) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8549. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 21.8 | 4 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.60× (z +12.7) | [[Adagrasib (drug)]] 0.05 µM 0.555× (z -10.4) ⚠ position not correctable |
| [[A498 (line)]] | wt | 81.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -10.5) |
| [[J82 (line)]] | alt | 11.0 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.0430× (z -12.0) |
| [[A-172 (line)]] | wt | 0.993 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.978 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 159 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.956 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.874 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.71 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.834 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.967 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.24 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8549), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FGF5]] | +0.63 | +0.54 / +0.69 | both halves | 1e-05 | **novel candidate** |
| [[NOL4]] | +0.62 | +0.54 / +0.60 | both halves | 1e-05 | **novel candidate** |
| [[CFAP299]] | +0.61 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[MSR1]] | +0.61 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[LINC01060]] | +0.61 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[LINC01117]] | +0.61 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[ADAMTS12]] | +0.60 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[RGS4]] | +0.60 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[NETO1]] | +0.60 | +0.49 / +0.56 | both halves | 1e-05 | STRING 536 |
| [[DSCAM]] | +0.58 | +0.48 / +0.56 | both halves | 2e-05 | STRING 469 |
| [[KCNQ5]] | +0.57 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[NALF1]] | +0.57 | +0.52 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 2, C 10.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LSAMP]] | B | LSAMP activity raises NTNG1's level | lines that do not express LSAMP (19) vs lines expressing it (31) | 2.00× lower at baseline in the lines without LSAMP | 0.090 | ⚠ within organs, on part of the lines; also absent: FRG1JP, ENSG00000289153, CA9; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers NTNG1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[LINC02899]] | C | LINC02899 activity raises NTNG1's level | lines that do not express LINC02899 (40) vs lines expressing it (10) | 4.14× lower at baseline in the lines without LINC02899 | 0.005 | ⚠ within organs, on part of the lines; also absent: LINC02999, MUC6, SIM1; co-absent with the target |
| [[LINC00993]] | C | LINC00993 activity raises NTNG1's level | lines that do not express LINC00993 (35) vs lines expressing it (15) | 3.73× lower at baseline in the lines without LINC00993 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ANKRD30A, KCNH5, KCNB2; maybe low, not absent; co-absent with the target |
| [[KCNH5]] | C | KCNH5 activity raises NTNG1's level | lines that do not express KCNH5 (36) vs lines expressing it (14) | 4.38× lower at baseline in the lines without KCNH5 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ASCL1, ENSG00000260958, UNC5D; co-absent with the target |
| [[NALF1]] | C | NALF1 activity raises NTNG1's level | lines that do not express NALF1 (28) vs lines expressing it (22) | 3.16× lower at baseline in the lines without NALF1 | 0.014 | ⚠ within organs, on part of the lines; also absent: EPHA5, COL3A1, ENSG00000248837; co-absent with the target |
| [[NETO1]] | C | NETO1 activity raises NTNG1's level | lines that do not express NETO1 (43) vs lines expressing it (7) | 5.36× lower at baseline in the lines without NETO1 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, SYT4; co-absent with the target |
| [[OR3A2]] | C | OR3A2 activity raises NTNG1's level | lines that do not express OR3A2 (27) vs lines expressing it (23) | 1.98× lower at baseline in the lines without OR3A2 | 0.043 | ⚠ within organs, on part of the lines; also absent: GRIK1, PAPPA2, LINC01266; maybe low, not absent; co-absent with the target |
| [[MSR1]] | C | MSR1 activity raises NTNG1's level | lines that do not express MSR1 (36) vs lines expressing it (14) | 4.73× lower at baseline in the lines without MSR1 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC02438, SAMMSON, ENSG00000286523; co-absent with the target |
| [[TOX]] | C | TOX activity raises NTNG1's level | lines that do not express TOX (30) vs lines expressing it (20) | 2.83× lower at baseline in the lines without TOX | 0.055 | ⚠ within organs, on part of the lines; also absent: CDH6, DKK3, MXRA5; co-absent with the target |
| [[DSCAM]] | C | DSCAM activity raises NTNG1's level | lines that do not express DSCAM (37) vs lines expressing it (13) | 3.14× lower at baseline in the lines without DSCAM | 0.090 | ⚠ within organs, on part of the lines; also absent: CGA, RIT2, LINC01456; maybe low, not absent; co-absent with the target |
| [[NOL4]] | C | NOL4 activity raises NTNG1's level | lines that do not express NOL4 (30) vs lines expressing it (20) | 3.08× lower at baseline in the lines without NOL4 | 0.095 | ⚠ within organs, on part of the lines; also absent: KCTD8, ASXL3, DSCAM; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 1, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDE4DIPP2]] | B | NTNG1 activity raises PDE4DIPP2's level | lines that do not express NTNG1 (33) vs lines expressing it (17) | 2.56× lower at baseline in the lines without NTNG1 | 0.070 | ⚠ within organs, on part of the lines; also absent: ANKRD30A, FUT9, ACSS3 |
| [[NPFFR2]] | C | NTNG1 activity raises NPFFR2's level | lines that do not express NTNG1 (33) vs lines expressing it (17) | 2.68× lower at baseline in the lines without NTNG1 | 0.023 | ⚠ within organs, on part of the lines; also absent: ANKRD30A, FUT9, ACSS3; co-absent with the target |
| [[CDH18]] | C | NTNG1 activity raises CDH18's level | lines that do not express NTNG1 (33) vs lines expressing it (17) | 2.31× lower at baseline in the lines without NTNG1 | 0.030 | ⚠ within organs, on part of the lines; also absent: ANKRD30A, FUT9, ACSS3; co-absent with the target |
| [[LINC02899]] | C | NTNG1 activity raises LINC02899's level | lines that do not express NTNG1 (33) vs lines expressing it (17) | 3.43× lower at baseline in the lines without NTNG1 | 0.031 | ⚠ within organs, on part of the lines; also absent: ANKRD30A, FUT9, ACSS3; co-absent with the target |
| [[NRG3]] | C | NTNG1 activity raises NRG3's level | lines that do not express NTNG1 (33) vs lines expressing it (17) | 3.24× lower at baseline in the lines without NTNG1 | 0.054 | ⚠ within organs, on part of the lines; also absent: ANKRD30A, FUT9, ACSS3; co-absent with the target |
| [[NOL4]] | C | NTNG1 activity raises NOL4's level | lines that do not express NTNG1 (33) vs lines expressing it (17) | 3.07× lower at baseline in the lines without NTNG1 | 0.079 | ⚠ within organs, on part of the lines; also absent: ANKRD30A, FUT9, ACSS3; co-absent with the target |
| [[LINC00993]] | C | NTNG1 activity raises LINC00993's level | lines that do not express NTNG1 (33) vs lines expressing it (17) | 2.55× lower at baseline in the lines without NTNG1 | 0.098 | ⚠ within organs, on part of the lines; also absent: ANKRD30A, FUT9, ACSS3; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.481). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.8, 22.3); signed map (17.8, 45.3). **Vector** length 48.1, 14.9% of its response variance represented; |z| ≥ 3 in 366 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +10.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.0 | +8.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +11.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +17.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +9.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +5.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.2 | +1.5 |
|  | [[Vitamin K4 (drug)]] 0.05 µM |  | +1.2 | +1.5 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -1.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.8 | -2.5 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.6 | -1.9 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.4 | -0.8 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.4 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | netrin G1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.3 — chr1:107,140,007-107,484,923 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0976, Lmnt1, NetG1, NetrinG1 |
| Gene groups (HGNC) | Netrins |
| Hallmark sets | APICAL_SURFACE |
| Reactome | 1 pathways, smallest: Post-translational modification: synthesis of GPI-anchored proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2I2](https://www.uniprot.org/uniprotkb/Q9Y2I2) (Netrin-G1):

> Involved in controlling patterning and neuronal circuit formation at the laminar, cellular, subcellular and synaptic levels. Promotes neurite outgrowth of both axons and dendrites.

**Summary**, from NCBI Gene [22854](https://www.ncbi.nlm.nih.gov/gene/22854):

> This gene encodes a preproprotein that is processed into a secreted protein containing eukaroytic growth factor (EGF)-like domains. This protein acts to guide axon growth during neuronal development. Polymorphisms in this gene may be associated with schizophrenia. Alternative splicing results in multiple transcript variants encoding distinct isoforms. [provided by RefSeq, Aug 2015]

**Accessions** — [HGNC:23319](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23319) · Entrez [22854](https://www.ncbi.nlm.nih.gov/gene/22854) · UniProt [Q9Y2I2](https://www.uniprot.org/uniprotkb/Q9Y2I2) · Ensembl [ENSG00000162631](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162631)

## Data

Gene col 8549: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8549); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8549, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8549]; `tensor/DDL_lfc|DDL_z.npy` [8549]; `embed/gene_vectors.npy` [8549]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8549 or target_col == 8549). Every well: [[NTNG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NTNG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
