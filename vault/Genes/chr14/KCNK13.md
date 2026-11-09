---
symbol: "KCNK13"
type: "gene"
col: 7614
ensembl_id: "ENSG00000152315"
name: "potassium two pore domain channel subfamily K member 13"
location: "14q32.11"
module: 82
arm: "+"
pooled_cpm: 2.83
n_lines_expressing: 41
n_dd_up: 29
n_dd_down: 1
n_dd_up_clean: 21
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 10
direction_downstream: 12
tags: ["gene", "module/082"]
generated_by: "tahoemap"
---

# KCNK13

*potassium two pore domain channel subfamily K member 13* — 14q32.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.25× (z +22.1, q 0e+00, up in 17 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.652× (z -4.6, q 0.002, down in 15 of 34 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (SNU-423 0.0791×, HepG2/C3A 0.162×, A-427 0.169×); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (HepG2/C3A 0.102×, SNU-423 0.115×, BT-474 0.0743×; ⚠ toxic; transcription drop); [[Harringtonine (drug)]] 5 µM in 2 lines (A-427 0.0933×, SW480 0.180×; ⚠ cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (A-427 0.110×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (BT-474 0.0561×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[JAKMIP1]] (+0.69, fdr 7e-06), [[RET]] (+0.67, fdr 7e-06), [[DACH2]] (+0.63, fdr 1e-05); moves opposite to [[ZNF280D]] (-0.50, fdr 6e-05), [[TIA1]] (-0.50, fdr 2e-04), [[CASD1]] (-0.49, fdr 5e-05).
> It is in [[Module 082]], a single-armed module (Muscle contraction).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[C14orf132]] → it (grade B ⚠); 12 go from it, the strongest it → [[SGSM1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7614.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.25×** | +22.1 | 0e+00 | 17/20 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **3.41×** | +18.8 | 0e+00 | 26/31 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.67×** | +16.1 | 0e+00 | 2/5 (HOP62, HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **4.15×** | +15.4 | 0e+00 | 29/36 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.35×** | +13.1 | 4e-37 | 24/31 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.96×** | +11.7 | 7e-30 | 21/32 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.90×** | +11.5 | 8e-29 | 2/10 (SW480, PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.56×** | +10.2 | 2e-22 | 16/23 (BT-474, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.53×** | +10.1 | 5e-22 | 20/33 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.43×** | +8.9 | 3e-17 | 1/5 (SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.83×** | +6.6 | 2e-09 | 8/26 (LOX-IMVI, Panc 03.27, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.52×** | +6.4 | 7e-09 | 7/22 (LoVo, C32, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.85×** | +5.9 | 1e-07 | 3/7 (BT-474, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.69×** | +5.7 | 5e-07 | 7/29 (SW480, SW 900, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +5.5 | 1e-06 | 4/15 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.53×** | +4.6 | 1e-04 | 11/30 (HepG2/C3A, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.19×** | +4.4 | 3e-04 | 11/26 (PANC-1, NCI-H2030, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +4.2 | 9e-04 | 1/21 (NCI-H460) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.45×** | +4.1 | 0.002 | 8/20 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~8% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7614.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (SNU-423 0.0791×, HepG2/C3A 0.162×, A-427 0.169×); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (HepG2/C3A 0.102×, SNU-423 0.115×, BT-474 0.0743×; ⚠ toxic; transcription drop); [[Harringtonine (drug)]] 5 µM in 2 lines (A-427 0.0933×, SW480 0.180×; ⚠ cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (A-427 0.110×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (BT-474 0.0561×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.652×** | -4.6 | 0.002 | 15/34 (A-427, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.898× | -4.1 | 0.013 | 8/37 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.727× | -3.4 | 0.11 | 11/32 (A-427, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | 0.746× | -3.2 | 0.23 | 3/28 (NCI-H460, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7614. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 20.6 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0791× (z -15.4) |
| [[A-427 (line)]] | wt | 11.1 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0933× (z -11.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.110× (z -10.8) |
| [[PANC-1 (line)]] | alt | 1.04 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 12.0× (z +9.0) | — |
| [[BT-474 (line)]] | alt | 10.2 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0561× (z -9.8) |
| [[HepG2_C3A (line)]] | wt | 18.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -10.8) |
| [[A-172 (line)]] | wt | 3.51 | 0 | 1 | — | [[Clobetasol propionate (drug)]] 0.5 µM 0.0587× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 1.38 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 14.1× (z +8.5) | — |
| [[NCI-H460 (line)]] | wt | 0.785 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.7× (z +9.8) | — |
| [[SW480 (line)]] | alt | 7.28 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.180× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 0.627 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.576 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.00 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.811 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.674 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.828 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.601 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.654 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.707 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.984 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.595 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.880 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.588 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.684 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.771 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.721 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.854 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7614), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JAKMIP1]] | +0.69 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[RET]] | +0.67 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[DACH2]] | +0.63 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[LPAR3]] | +0.62 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[GBX1]] | +0.61 | +0.52 / +0.73 | both halves | 1e-05 |  |
| [[CELF5]] | +0.61 | +0.44 / +0.69 | both halves | 3e-05 |  |
| [[SH3GL3]] | +0.61 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[KHDRBS3]] | +0.61 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[HS6ST3]] | +0.61 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[SUSD4]] | +0.60 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[SPSB1]] | +0.60 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[BMP8B]] | +0.59 | +0.50 / +0.68 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF280D]] | -0.50 | -0.38 / -0.46 | both halves | 6e-05 |  |
| [[TIA1]] | -0.50 | -0.29 / -0.55 | both halves | 2e-04 |  |
| [[CASD1]] | -0.49 | -0.40 / -0.41 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C14orf132]] | B | C14orf132 activity raises KCNK13's level | lines that do not express C14orf132 (19) vs lines expressing it (31) | 1.85× lower at baseline in the lines without C14orf132 | 0.003 | ⚠ within organs, on part of the lines; also absent: SLC22A17, ZFP28, ADAMTS7 |
| [[LMX1B]] | B | LMX1B activity raises KCNK13's level | lines that do not express LMX1B (24) vs lines expressing it (26) | 1.55× lower at baseline in the lines without LMX1B | 0.010 | ⚠ within organs, on part of the lines; also absent: JPH3, JAKMIP1, GABBR2 |
| [[DPYSL5]] | B | DPYSL5 activity raises KCNK13's level | lines that do not express DPYSL5 (30) vs lines expressing it (20) | 1.74× lower at baseline in the lines without DPYSL5 | 0.027 | ⚠ within organs, on part of the lines; also absent: JPH3, OLFM1, CHD5 |
| [[EPB41L4A]] | B | EPB41L4A activity raises KCNK13's level | lines that do not express EPB41L4A (26) vs lines expressing it (24) | 1.26× lower at baseline in the lines without EPB41L4A | 0.035 | ⚠ within organs, on part of the lines; also absent: COL4A4, COL4A3, ANKRD20A11P |
| [[RET]] | B | RET activity raises KCNK13's level | lines that do not express RET (28) vs lines expressing it (22) | 1.51× lower at baseline in the lines without RET | 0.046 | ⚠ within organs, on part of the lines; also absent: CHD5, KIF1A, NPTX1 |
| [[EBF2]] | B | EBF2 activity raises KCNK13's level | lines that do not express EBF2 (18) vs lines expressing it (32) | 1.51× lower at baseline in the lines without EBF2 | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000249738, LMX1B, CAPN14; maybe low, not absent |
| [[CRMP1]] | B | CRMP1 activity raises KCNK13's level | lines that do not express CRMP1 (19) vs lines expressing it (31) | 1.61× lower at baseline in the lines without CRMP1 | 0.052 | ⚠ within organs, on part of the lines; also absent: JAM3, NHSL2, ENSG00000286033; maybe low, not absent |
| [[SDK1]] | B | SDK1 activity raises KCNK13's level | lines that do not express SDK1 (22) vs lines expressing it (28) | 1.63× lower at baseline in the lines without SDK1 | 0.054 | ⚠ within organs, on part of the lines; also absent: PCBP3, ACKR3, SLIT3 |
| [[JAKMIP1]] | B | JAKMIP1 activity raises KCNK13's level | lines that do not express JAKMIP1 (27) vs lines expressing it (23) | 1.48× lower at baseline in the lines without JAKMIP1 | 0.073 | ⚠ within organs, on part of the lines; also absent: CHST8, JPH3, GABBR2 |
| [[SLC6A17]] | B | SLC6A17 activity raises KCNK13's level | lines that do not express SLC6A17 (28) vs lines expressing it (22) | 1.47× lower at baseline in the lines without SLC6A17 | 0.091 | ⚠ within organs, on part of the lines; also absent: TWIST1, LINC00470, MAGEA3-DT |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 11, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SGSM1]] | B | KCNK13 activity raises SGSM1's level | lines that do not express KCNK13 (9) vs lines expressing it (41) | 1.62× lower at baseline in the lines without KCNK13 | 0.025 | ⚠ within organs, on part of the lines; also absent: TMEM170B, TMEM145, LINC02609; maybe low, not absent |
| [[SDK1]] | B | KCNK13 activity raises SDK1's level | lines that do not express KCNK13 (9) vs lines expressing it (41) | 4.85× lower at baseline in the lines without KCNK13 | 0.032 | ⚠ within organs, on part of the lines; also absent: TMEM170B, TMEM145, LINC02609; maybe low, not absent |
| [[DISP3]] | B | KCNK13 activity raises DISP3's level | lines that do not express KCNK13 (9) vs lines expressing it (41) | 1.85× lower at baseline in the lines without KCNK13 | 0.042 | ⚠ within organs, on part of the lines; also absent: TMEM170B, TMEM145, LINC02609; maybe low, not absent |
| [[CELF5]] | B | KCNK13 activity raises CELF5's level | lines that do not express KCNK13 (9) vs lines expressing it (41) | 1.56× lower at baseline in the lines without KCNK13 | 0.044 | ⚠ within organs, on part of the lines; also absent: TMEM170B, TMEM145, LINC02609; maybe low, not absent |
| [[KIF26A]] | B | KCNK13 activity raises KIF26A's level | lines that do not express KCNK13 (9) vs lines expressing it (41) | 2.19× lower at baseline in the lines without KCNK13 | 0.048 | ⚠ within organs, on part of the lines; also absent: TMEM170B, TMEM145, LINC02609; maybe low, not absent |
| [[MAPT]] | B | KCNK13 activity raises MAPT's level | lines that do not express KCNK13 (9) vs lines expressing it (41) | 4.73× lower at baseline in the lines without KCNK13 | 0.055 | ⚠ within organs, on part of the lines; also absent: TMEM170B, TMEM145, LINC02609; maybe low, not absent |
| [[ROR2]] | B | KCNK13 activity raises ROR2's level | lines that do not express KCNK13 (9) vs lines expressing it (41) | 2.84× lower at baseline in the lines without KCNK13 | 0.063 | ⚠ within organs, on part of the lines; also absent: TMEM170B, TMEM145, LINC02609; maybe low, not absent |
| [[FIBCD1]] | B | KCNK13 activity raises FIBCD1's level | lines that do not express KCNK13 (9) vs lines expressing it (41) | 1.52× lower at baseline in the lines without KCNK13 | 0.067 | ⚠ within organs, on part of the lines; also absent: TMEM170B, TMEM145, LINC02609; maybe low, not absent |
| [[EPHB1]] | B | KCNK13 activity raises EPHB1's level | lines that do not express KCNK13 (9) vs lines expressing it (41) | 2.74× lower at baseline in the lines without KCNK13 | 0.085 | ⚠ within organs, on part of the lines; also absent: TMEM170B, TMEM145, LINC02609; maybe low, not absent |
| [[C14orf132]] | B | KCNK13 activity raises C14orf132's level | lines that do not express KCNK13 (9) vs lines expressing it (41) | 4.59× lower at baseline in the lines without KCNK13 | 0.091 | ⚠ within organs, on part of the lines; also absent: TMEM170B, TMEM145, LINC02609; maybe low, not absent |
| [[BMP8A]] | B | KCNK13 activity raises BMP8A's level | lines that do not express KCNK13 (9) vs lines expressing it (41) | 1.83× lower at baseline in the lines without KCNK13 | 0.096 | ⚠ within organs, on part of the lines; also absent: TMEM170B, TMEM145, LINC02609; maybe low, not absent |
| [[FAM124A]] | C | KCNK13 activity raises FAM124A's level | lines that do not express KCNK13 (9) vs lines expressing it (41) | 2.53× lower at baseline in the lines without KCNK13 | 0.092 | ⚠ within organs, on part of the lines; also absent: TMEM170B, TMEM145, LINC02609; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 082]] — Muscle contraction; 55 genes; every member is in the + arm (projection on the module's main direction 0.682). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (5.5, 38.6); signed map (27.6, 27.7). **Vector** length 58.2, 10.8% of its response variance represented; |z| ≥ 3 in 886 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.9 | +18.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.9 | +16.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.7 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.4 | +11.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +8.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +6.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.9 | +2.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.5 | +3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +0.9 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.0 | -4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -1.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.9 | -4.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -2.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.8 | -1.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -0.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.3 | -1.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -0.8 |
|  | [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | -1.1 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | potassium two pore domain channel subfamily K member 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.11 — chr14:90,061,994-90,185,853 (+) |
| Ensembl biotype | protein_coding |
| Also known as | K2p13.1, THIK-1, THIK1 |
| Gene groups (HGNC) | Potassium two pore domain channel subfamily K |
| Reactome | 6 pathways, smallest: Tandem pore domain potassium channels; Phase 4 - resting membrane potential; Potassium Channels |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HB14](https://www.uniprot.org/uniprotkb/Q9HB14) (Potassium channel subfamily K member 13):

> K(+) channel that conducts outward rectifying tonic currents potentiated by purinergic signals. Homo- and heterodimerizes to form functional channels with distinct regulatory and gating properties. Contributes most of K(+) currents at the plasma membrane of resting microglia. Maintains a depolarized membrane potential required for proper ramified microglia morphology and phagocytosis, selectively mediating microglial pruning of presynaptic compartments at hippocampal excitatory synapses. Upon …

**Summary**, from NCBI Gene [56659](https://www.ncbi.nlm.nih.gov/gene/56659):

> Potassium channels represent the most complex class of voltage-gated ion channels from both functional and structural standpoints. Their diverse functions include regulating neurotransmitter release, heart rate, insulin secretion, neuronal excitability, epithelial electrolyte transport, smooth muscle contraction, and cell volume. This gene encodes a potassium channel containing two pore-forming domains. This protein is an open channel that can be stimulated by arachidonic acid and inhibited by …

**Accessions** — [HGNC:6275](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6275) · Entrez [56659](https://www.ncbi.nlm.nih.gov/gene/56659) · UniProt [Q9HB14](https://www.uniprot.org/uniprotkb/Q9HB14) · Ensembl [ENSG00000152315](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152315)

## Data

Gene col 7614: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7614); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7614, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7614]; `tensor/DDL_lfc|DDL_z.npy` [7614]; `embed/gene_vectors.npy` [7614]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7614 or target_col == 7614). Every well: [[KCNK13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCNK13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
