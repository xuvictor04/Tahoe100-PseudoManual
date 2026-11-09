---
symbol: "MAL2"
type: "gene"
col: 7213
ensembl_id: "ENSG00000147676"
name: "mal, T cell differentiation protein 2"
location: "8q24.12"
module: 8
arm: "+"
pooled_cpm: 97.64
n_lines_expressing: 19
n_dd_up: 17
n_dd_down: 20
n_dd_up_clean: 10
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 84
direction_downstream: 115
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# MAL2

*mal, T cell differentiation protein 2* — 8q24.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.07× (z +25.4, q 0e+00, up in 16 of 18 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Docetaxel (Trihydrate) (drug)]] 0.5 µM: 1.58× (z +8.3, q 2e-14, up in 1 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.884× (z -7.7, q 9e-12, down in 0 of 19 measured lines) ⚠ position not correctable. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.713× (z -6.1, q 3e-07, down in 12 of 17 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ST14]] (+0.72, fdr 7e-06), [[CDH1]] (+0.67, fdr 7e-06), [[TC2N]] (+0.65, fdr 3e-05); moves opposite to [[RBX1]] (-0.47, fdr 1e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 84 arrows point to it, the strongest [[JUP]] → it (grade B ⚠); 115 go from it, the strongest it → [[ST3GAL3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7213.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.07×** | +25.4 | 0e+00 | 16/18 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.27×** | +20.6 | 0e+00 | 15/16 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.90×** | +17.8 | 0e+00 | 13/16 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.58×** | +8.3 | 2e-14 | 1/17 (RPMI-7951) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +7.8 | 5e-13 | 3/17 (RPMI-7951, SW480, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.18×** | +7.4 | 2e-11 | 8/12 (NCI-H2347, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +6.8 | 1e-09 | 2/17 (HepG2/C3A, SW480) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +6.3 | 2e-08 | 1/19 (NCI-H2347) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +5.7 | 7e-07 | 9/17 (LoVo, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Verteporfin (drug)]] 0.5 µM |  | **1.36×** | +5.6 | 1e-06 | 0/18 | all doses, flat | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~18% of this change | **1.28×** | +4.4 | 5e-04 | 2/17 (HCT15, HepG2/C3A) | inconsistent across doses | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **1.53×** | +4.0 | 0.003 | 11/18 (BT-474, SW48, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM |  | **1.26×** | +3.9 | 0.004 | 0/17 | inconsistent across doses |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | **1.24×** | +3.9 | 0.004 | 0/17 | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.6 | 0.010 | 1/18 (NCI-H2347) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.15× | +3.6 | 0.011 | 4/18 (LS 180, LoVo, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.32×** | +3.6 | 0.012 | 1/17 (SW480) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.018 | 0/18 | all doses, flat | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.21×** | +3.3 | 0.033 | 0/17 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Erythromycin (drug)]] 5 µM |  | 1.19× | +3.2 | 0.042 | 0/17 | top dose only |  |
| [[Cyclosporin A (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.042 | 8/17 (BT-474, NCI-H2347, …) | two highest doses |  |
| [[Bimatoprost (drug)]] 0.5 µM |  | 1.17× | +2.9 | 0.088 | 0/18 | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7213.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.884× | -7.7 | 9e-12 | 0/19 | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.713×** | -6.1 | 3e-07 | 12/17 (HEC-1-A, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.706×** | -5.8 | 1e-06 | 0/17 | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.806×** | -5.5 | 6e-06 | 15/17 (Panc 03.27, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.743×** | -5.1 | 3e-05 | 13/17 (Panc 03.27, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Artesunate (drug)]] 0.5 µM |  | **0.770×** | -4.7 | 2e-04 | 0/17 | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.05 µM |  | **0.755×** | -4.7 | 2e-04 | 0/17 | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.837× | -4.4 | 1e-03 | 0/17 | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.790×** | -4.2 | 0.001 | 3/17 (COLO 205, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Futibatinib (drug)]] 0.05 µM |  | **0.790×** | -4.0 | 0.003 | 0/17 | inconsistent across doses | position effect removed |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.787×** | -4.0 | 0.003 | 0/17 | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.662×** | -3.9 | 0.005 | 4/18 (Panc 03.27, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 0.05 µM |  | **0.803×** | -3.7 | 0.008 | 0/17 | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.821×** | -3.5 | 0.017 | 0/17 | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.05 µM |  | **0.829×** | -3.4 | 0.029 | 1/17 (RPMI-7951) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.832×** | -3.3 | 0.033 | 1/17 (Panc 03.27) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7213. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Panc 03.27 (line)]] | alt | 693 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -23.8) |
| [[HEC-1-A (line)]] | alt | 310 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.62× (z +10.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -14.8) |
| [[NCI-H1573 (line)]] | alt | 211 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -16.3) |
| [[SW480 (line)]] | alt | 26.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.95× (z +13.3) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 227 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -16.7) |
| [[HT-29 (line)]] | alt | 579 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -11.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.492× (z -10.8) |
| [[KATO III (line)]] | alt | 248 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.443× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.510× (z -9.4) |
| [[SW1417 (line)]] | alt | 196 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.529× (z -9.9) |
| [[COLO 205 (line)]] | alt | 190 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -10.8) |
| [[HepG2_C3A (line)]] | wt | 45.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.78× (z +8.5) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 124 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.534× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 166 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.514× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 480 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -11.4) |
| [[RPMI-7951 (line)]] | alt | 31.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +9.6) | — |
| [[A-172 (line)]] | wt | 8.57 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 6.69 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 10.0 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 6.94 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 14.9 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 9.93 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 203 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.65 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 8.17 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 11.5 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 8.27 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.41 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 18.2 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 7.64 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.0 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 12.2 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 23.1 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.33 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 6.97 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 8.46 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.27 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 7.71 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 78.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.77 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 6.37 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 8.39 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 14.0 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.38 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 9.76 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 10.0 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 15.2 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 9.12 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 20.6 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 125 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7213), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST14]] | +0.72 | +0.79 / +0.63 | both halves | 7e-06 |  |
| [[CDH1]] | +0.67 | +0.71 / +0.66 | both halves | 7e-06 | STRING 457 |
| [[TC2N]] | +0.65 | +0.70 / +0.45 | both halves | 3e-05 |  |
| [[OCLN]] | +0.65 | +0.75 / +0.50 | both halves | 1e-05 | same gene group; STRING 644 |
| [[SLC44A4]] | +0.64 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[ITGB6]] | +0.64 | +0.69 / +0.57 | both halves | 1e-05 |  |
| [[MUC16]] | +0.63 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[TSPAN1]] | +0.63 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[ADGRF1]] | +0.62 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[RAB25]] | +0.62 | +0.61 / +0.61 | both halves | 7e-06 | STRING 495 |
| [[SPINT1]] | +0.62 | +0.78 / +0.44 | both halves | 3e-05 |  |
| [[GALNT3]] | +0.61 | +0.68 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBX1]] | -0.47 | -0.39 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*84 arrows, 84 of them with an alert ⚠; grade A 0, B 4, C 80. Shown: the 12 strongest; 72 more arrows (72 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[JUP]] | B | JUP activity raises MAL2's level | lines that do not express JUP (16) vs lines expressing it (34) | 4.31× lower at baseline in the lines without JUP | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |
| [[EPS8L1]] | B | EPS8L1 activity raises MAL2's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 3.83× lower at baseline in the lines without EPS8L1 | 0.049 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |
| [[PLEKHG1]] | B | PLEKHG1 activity raises MAL2's level | lines that do not express PLEKHG1 (17) vs lines expressing it (33) | 2.73× lower at baseline in the lines without PLEKHG1 | 0.086 | ⚠ within organs, on part of the lines; also absent: HLA-V-1, LSR, ARHGAP8 |
| [[PRR36]] | B | PRR36 activity raises MAL2's level | lines that do not express PRR36 (19) vs lines expressing it (31) | 2.89× lower at baseline in the lines without PRR36 | 0.094 | ⚠ within organs, on part of the lines; also absent: NUP210, TTC9, CGN |
| [[RAB25]] | C | RAB25 activity raises MAL2's level | lines that do not express RAB25 (33) vs lines expressing it (17) | 16.66× lower at baseline in the lines without RAB25 | 1e-06 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, TMEM30B, PRSS8; co-absent with the target |
| [[TMEM125]] | C | TMEM125 activity raises MAL2's level | lines that do not express TMEM125 (33) vs lines expressing it (17) | 15.90× lower at baseline in the lines without TMEM125 | 5e-06 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14; co-absent with the target |
| [[TMEM30B]] | C | TMEM30B activity raises MAL2's level | lines that do not express TMEM30B (35) vs lines expressing it (15) | 15.51× lower at baseline in the lines without TMEM30B | 7e-06 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ANKRD22, RAB25; co-absent with the target |
| [[TMPRSS4]] | C | TMPRSS4 activity raises MAL2's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 14.64× lower at baseline in the lines without TMPRSS4 | 9e-06 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B; co-absent with the target |
| [[CDH1]] | C | CDH1 activity raises MAL2's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 13.28× lower at baseline in the lines without CDH1 | 1e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1; co-absent with the target |
| [[BSPRY]] | C | BSPRY activity raises MAL2's level | lines that do not express BSPRY (29) vs lines expressing it (21) | 10.17× lower at baseline in the lines without BSPRY | 3e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPCAM, RAB25; co-absent with the target |
| [[MPZL2]] | C | MPZL2 activity raises MAL2's level | lines that do not express MPZL2 (29) vs lines expressing it (21) | 10.91× lower at baseline in the lines without MPZL2 | 3e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, IRF6, ST14; co-absent with the target |
| [[ST14]] | C | ST14 activity raises MAL2's level | lines that do not express ST14 (32) vs lines expressing it (18) | 13.55× lower at baseline in the lines without ST14 | 3e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1; co-absent with the target |

### Downstream of this gene

*115 arrows, 115 of them with an alert ⚠; grade A 0, B 36, C 79. Shown: the 12 strongest; 103 more arrows (103 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ST3GAL3]] | B | MAL2 activity lowers ST3GAL3's level | lines that do not express MAL2 (31) vs lines expressing it (19) | 2.53× higher at baseline in the lines without MAL2 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RAB25, TMEM125, CDH1 |
| [[EPS8L1]] | B | MAL2 activity raises EPS8L1's level | lines that do not express MAL2 (31) vs lines expressing it (19) | 4.45× lower at baseline in the lines without MAL2 | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RAB25, TMEM125, CDH1 |
| [[JUP]] | B | MAL2 activity raises JUP's level | lines that do not express MAL2 (31) vs lines expressing it (19) | 5.50× lower at baseline in the lines without MAL2 | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RAB25, TMEM125, CDH1 |
| [[ARHGEF16]] | B | MAL2 activity raises ARHGEF16's level | lines that do not express MAL2 (31) vs lines expressing it (19) | 3.66× lower at baseline in the lines without MAL2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RAB25, TMEM125, CDH1 |
| [[ELMO3]] | B | MAL2 activity raises ELMO3's level | lines that do not express MAL2 (31) vs lines expressing it (19) | 2.54× lower at baseline in the lines without MAL2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RAB25, TMEM125, CDH1 |
| [[ANXA11]] | B | MAL2 activity raises ANXA11's level | lines that do not express MAL2 (31) vs lines expressing it (19) | 2.97× lower at baseline in the lines without MAL2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RAB25, TMEM125, CDH1 |
| [[TMEM51-AS1]] | B | MAL2 activity raises TMEM51-AS1's level | lines that do not express MAL2 (31) vs lines expressing it (19) | 2.62× lower at baseline in the lines without MAL2 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RAB25, TMEM125, CDH1 |
| [[SPATS2]] | B | MAL2 activity lowers SPATS2's level | lines that do not express MAL2 (31) vs lines expressing it (19) | 1.47× higher at baseline in the lines without MAL2 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RAB25, TMEM125, CDH1 |
| [[OCLN]] | B | MAL2 activity strengthens OCLN's drug response | lines that do not express MAL2 (13) vs lines expressing it (17) | the lines without MAL2 respond 0.15× as strongly (z diff +4.88); strongest at Homoharringtonine 5 µM: 1.14x vs 0.44x (z diff +8.0) | 0.012 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RAB25, TMEM125, CDH1; target measured in part of the lines; artifact flags |
| cells under [[Aliskiren (drug)]] 0.5 µM | B | MAL2 activity raises the cells' numbers under Aliskiren 0.5 µM (protects the cells) | lines that do not express MAL2 (31) vs lines expressing it (17) | the lines without MAL2: 0.73× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RAB25, TMEM125, CDH1 |
| cells under [[Berbamine (dihydrochloride) (drug)]] 0.5 µM | B | MAL2 activity lowers the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express MAL2 (31) vs lines expressing it (17) | the lines without MAL2: 1.18× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RAB25, TMEM125, CDH1 |
| cells under [[Afatinib (drug)]] 0.5 µM | B | MAL2 activity lowers the cells' numbers under Afatinib 0.5 µM (makes them more sensitive) | lines that do not express MAL2 (31) vs lines expressing it (17) | the lines without MAL2: 1.14× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RAB25, TMEM125, CDH1 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.610). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (19.9, 57.1); signed map (58.1, 7.0). **Vector** length 65.1, 21.7% of its response variance represented; |z| ≥ 3 in 438 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.2 | +25.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.9 | +20.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.5 | +17.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +7.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +1.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.6 | +3.6 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.5 | +2.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.3 | +8.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.7 | -6.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.4 | -5.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.1 | -3.2 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.9 | -4.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | +0.0 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.3 | -3.2 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.2 | -2.9 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.1 | -5.8 |
|  | [[Futibatinib (drug)]] 0.05 µM |  | -1.1 | -4.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.0 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | mal, T cell differentiation protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.12 — chr8:119,165,034-119,245,673 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | MARVEL domain containing |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969L2](https://www.uniprot.org/uniprotkb/Q969L2) (Protein MAL2):

> Member of the machinery of polarized transport. Required for the indirect transcytotic route at the step of the egress of the transcytosing cargo from perinuclear endosomes in order for it to travel to the apical surface via a raft-dependent pathway.

**Summary**, from NCBI Gene [114569](https://www.ncbi.nlm.nih.gov/gene/114569):

> This gene encodes a multispan transmembrane protein belonging to the MAL proteolipid family. The protein is a component of lipid rafts and, in polarized cells, it primarily localizes to endosomal structures beneath the apical membrane. It is required for transcytosis, an intracellular transport pathway used to deliver membrane-bound proteins and exogenous cargos from the basolateral to the apical surface. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:13634](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13634) · Entrez [114569](https://www.ncbi.nlm.nih.gov/gene/114569) · UniProt [Q969L2](https://www.uniprot.org/uniprotkb/Q969L2) · Ensembl [ENSG00000147676](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147676)

## Data

Gene col 7213: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7213); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7213, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7213]; `tensor/DDL_lfc|DDL_z.npy` [7213]; `embed/gene_vectors.npy` [7213]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7213 or target_col == 7213). Every well: [[MAL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
