---
symbol: "VIM"
type: "gene"
col: 368
ensembl_id: "ENSG00000026025"
name: "vimentin"
location: "10p13"
module: 161
arm: "+"
pooled_cpm: 1484.3
n_lines_expressing: 32
n_dd_up: 3
n_dd_down: 6
n_dd_up_clean: 0
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 4
tags: ["gene", "module/161"]
generated_by: "tahoemap"
---

# VIM

*vimentin* — 10p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.40× (z +6.8, q 5e-09, up in 28 of 28 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SW 900 4.11×, A498 4.11×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (A498 4.00×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.655× (z -4.8, q 8e-04, down in 24 of 30 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 9 lines (AN3 CA 0.213×, H4 0.217×, HOP62 0.279×, LOX-IMVI 0.298×, …); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (MIA PaCa-2 0.302×, C32 0.362×, SW 1088 0.311×, AN3 CA 0.422×, …; ⚠ cell-cycle shift, explains ~27% of this change).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LGALS1]] (+0.72, fdr 7e-06), [[MYADM]] (+0.60, fdr 1e-05), [[CALM1]] (+0.58, fdr 6e-05); moves opposite to [[MRM1]] (-0.52, fdr 2e-04), [[ZNF304]] (-0.50, fdr 1e-04), [[PIGW]] (-0.49, fdr 3e-04).
> It is in [[Module 161]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TSPAN4]] → it (grade B ⚠); 4 go from it, the strongest it → [[KHDRBS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 368.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SW 900 4.11×, A498 4.11×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (A498 4.00×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.40×** | +6.8 | 5e-09 | 28/28 (A498, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.50×** | +6.7 | 5e-09 | 29/31 (SW 900, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.61×** | +3.6 | 0.065 | 20/28 (NCI-H2347, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 368.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 9 lines (AN3 CA 0.213×, H4 0.217×, HOP62 0.279×, LOX-IMVI 0.298×, …); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (MIA PaCa-2 0.302×, C32 0.362×, SW 1088 0.311×, AN3 CA 0.422×, …; ⚠ cell-cycle shift, explains ~27% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.655×** | -4.8 | 8e-04 | 24/30 (AN3 CA, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.677×** | -4.4 | 0.003 | 24/31 (MIA PaCa-2, C32, …) | rises with dose |  |
| [[Budesonide (drug)]] 5 µM |  | **0.612×** | -4.0 | 0.013 | 30/30 (HOP62, PANC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.586×** | -3.9 | 0.013 | 27/30 (C32, MIA PaCa-2, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.650×** | -3.5 | 0.058 | 24/30 (LOX-IMVI, J82, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.654×** | -3.4 | 0.059 | 24/30 (A-172, CFPAC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.754× | -3.2 | 0.11 | 21/30 (PANC-1, NCI-H23, …) | rises with dose | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | 0.485× | -3.1 | 0.16 | 23/30 (AN3 CA, A-427, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.646× | -3.0 | 0.16 | 20/29 (AN3 CA, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, +0.81 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 368. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 1,590 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.00× (z +9.1) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 2,979 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -16.5) |
| [[A-427 (line)]] | wt | 3,600 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -11.6) |
| [[C32 (line)]] | wt | 2,339 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.362× (z -10.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[CHP-212 (line)]] | wt | 1,254 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -10.2) |
| [[H4 (line)]] | wt | 1,674 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -15.1) |
| [[HOP62 (line)]] | alt | 4,727 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -12.9) |
| [[LOX-IMVI (line)]] | wt | 3,127 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -12.2) |
| [[MIA PaCa-2 (line)]] | alt | 4,055 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -12.4) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H460 (line)]] | wt | 1,279 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -9.2) |
| [[RPMI-7951 (line)]] | alt | 3,718 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -8.9) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SK-MEL-2 (line)]] | alt | 2,758 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -10.4) |
| [[SW 1088 (line)]] | alt | 2,180 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -9.8) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW 900 (line)]] | alt | 828 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.11× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 609 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -11.2) |
| [[A-172 (line)]] | wt | 3,225 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1,598 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1,368 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 95.5 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 243 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 869 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 82.3 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 93.5 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 86.9 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 89.2 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 103 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2,748 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 103 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4,621 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 582 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 76.9 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 80.2 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 76.0 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 80.1 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1,852 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2,177 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 864 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1,161 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 449 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1,295 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2,120 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 243 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3,445 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 94.3 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 75.7 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 97.7 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3,050 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1,803 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 78.8 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 105 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 368), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LGALS1]] | +0.72 | +0.68 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 879 |
| [[MYADM]] | +0.60 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[CALM1]] | +0.58 | +0.64 / +0.38 | both halves | 6e-05 | pathway: Muscle contraction |
| [[UACA]] | +0.57 | +0.52 / +0.45 | both halves | 3e-05 | pathway: Apoptosis |
| [[CLIP2]] | +0.55 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[CCNI]] | +0.51 | +0.40 / +0.45 | both halves | 5e-05 |  |
| [[TNNT1]] | +0.51 | +0.51 / +0.38 | both halves | 7e-05 | pathway: Muscle contraction |
| [[TMEM158]] | +0.50 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[TSPAN4]] | +0.49 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[MYO10]] | +0.49 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[DLGAP4]] | +0.49 | +0.44 / +0.43 | both halves | 3e-05 |  |
| [[PRSS23]] | +0.49 | +0.47 / +0.51 | both halves | 2e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRM1]] | -0.52 | -0.42 / -0.30 | both halves | 2e-04 |  |
| [[ZNF304]] | -0.50 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[PIGW]] | -0.49 | -0.32 / -0.28 | both halves | 3e-04 |  |
| [[MGST1]] | -0.49 | -0.48 / -0.39 | both halves | 6e-05 |  |
| [[SPRYD4]] | -0.49 | -0.31 / -0.33 | both halves | 2e-04 |  |
| [[PLXNB1]] | -0.48 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[MTX1]] | -0.48 | -0.33 / -0.38 | both halves | 1e-04 |  |
| [[LPAR1]] | -0.48 | -0.32 / -0.43 | both halves | 1e-04 |  |
| [[ATP8B4]] | -0.47 | -0.50 / -0.10 | ⚠ one half (not replicated) | 0.003 |  |
| [[SCO1]] | -0.47 | -0.46 / -0.36 | both halves | 9e-05 |  |
| [[MOV10]] | -0.46 | -0.29 / -0.34 | both halves | 2e-04 |  |
| [[FOXG1]] | -0.46 | -0.43 / -0.22 | both halves | 6e-04 |  |
| [[C1RL-AS1]] | -0.46 | -0.32 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TSPAN4]] | B | TSPAN4 activity raises VIM's level | lines that do not express TSPAN4 (7) vs lines expressing it (43) | 10.90× lower at baseline in the lines without TSPAN4 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: TRPC1, EMP3, PXDC1; maybe low, not absent |
| [[ZCCHC24]] | B | ZCCHC24 activity raises VIM's level | lines that do not express ZCCHC24 (5) vs lines expressing it (45) | 5.44× lower at baseline in the lines without ZCCHC24 | 0.098 | ⚠ within organs, on part of the lines; also absent: CNTNAP1, KIF17, SLC29A4; maybe low, not absent |
| [[LGALS1]] | C | LGALS1 activity raises VIM's level | lines that do not express LGALS1 (12) vs lines expressing it (38) | 12.49× lower at baseline in the lines without LGALS1 | 0.002 | ⚠ within organs, on part of the lines; also absent: EMP3, AXL, VIM; co-absent with the target |
| [[SFRP1]] | C | SFRP1 activity raises VIM's level | lines that do not express SFRP1 (32) vs lines expressing it (18) | 5.25× lower at baseline in the lines without SFRP1 | 0.080 | ⚠ within organs, on part of the lines; also absent: LAYN, INSYN2B, EVC2; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KHDRBS1]] | B | VIM activity raises KHDRBS1's level | lines that do not express VIM (18) vs lines expressing it (32) | 1.12× lower at baseline in the lines without VIM | 0.075 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: LOXL2, ADAMTS18, MAP1B |
| [[MAPK8]] | B | VIM activity raises MAPK8's level | lines that do not express VIM (18) vs lines expressing it (32) | 1.02× lower at baseline in the lines without VIM | 0.093 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: LOXL2, ADAMTS18, MAP1B |
| [[TSPAN4]] | B | VIM activity raises TSPAN4's level | lines that do not express VIM (18) vs lines expressing it (32) | 2.42× lower at baseline in the lines without VIM | 0.094 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: LOXL2, ADAMTS18, MAP1B |
| [[LGALS1]] | C | VIM activity raises LGALS1's level | lines that do not express VIM (18) vs lines expressing it (32) | 5.81× lower at baseline in the lines without VIM | 0.040 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: LOXL2, ADAMTS18, MAP1B; co-absent with the target |

## Where it sits

- **Module**: [[Module 161]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.399). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (49.9, 1.6); signed map (-7.6, 41.3). **Vector** length 78.3, 32.6% of its response variance represented; |z| ≥ 3 in 451 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +1.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | -1.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.0 | +0.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.0 | +1.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.0 | -0.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | +1.8 | +2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | -2.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -4.4 | -4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.7 | -2.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.4 | +6.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.3 | +3.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -3.2 | -3.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.2 | -1.0 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.2 | -1.7 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.1 | -4.0 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -2.0 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | vimentin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p13 — chr10:17,228,241-17,237,593 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Intermediate filaments Type III |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 25 pathways, smallest: Caspase-mediated cleavage of cytoskeletal proteins; Striated Muscle Contraction; Chaperone Mediated Autophagy |
| Matched by | ensembl_id |

**Function**, from UniProt [P08670](https://www.uniprot.org/uniprotkb/P08670) (Vimentin):

> Vimentins are class-III intermediate filaments found in various non-epithelial cells, especially mesenchymal cells. Vimentin is attached to the nucleus, endoplasmic reticulum, and mitochondria, either laterally or terminally. Plays a role in cell directional movement, orientation, cell sheet organization and Golgi complex polarization at the cell migration front (By similarity). Protects SCRIB from proteasomal degradation and facilitates its localization to intermediate filaments in a cell …

**Summary**, from NCBI Gene [7431](https://www.ncbi.nlm.nih.gov/gene/7431):

> This gene encodes a type III intermediate filament protein. Intermediate filaments, along with microtubules and actin microfilaments, make up the cytoskeleton. The encoded protein is responsible for maintaining cell shape and integrity of the cytoplasm, and stabilizing cytoskeletal interactions. This protein is involved in neuritogenesis and cholesterol transport and functions as an organizer of a number of other critical proteins involved in cell attachment, migration, and signaling. Bacterial …

**Accessions** — [HGNC:12692](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12692) · Entrez [7431](https://www.ncbi.nlm.nih.gov/gene/7431) · UniProt [P08670](https://www.uniprot.org/uniprotkb/P08670) · Ensembl [ENSG00000026025](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000026025)

## Data

Gene col 368: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 368); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 368, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 368]; `tensor/DDL_lfc|DDL_z.npy` [368]; `embed/gene_vectors.npy` [368]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 368 or target_col == 368). Every well: [[VIM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VIM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
