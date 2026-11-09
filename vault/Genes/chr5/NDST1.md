---
symbol: "NDST1"
type: "gene"
col: 958
ensembl_id: "ENSG00000070614"
name: "N-deacetylase and N-sulfotransferase 1"
location: "5q33.1"
module: 5
arm: "+"
pooled_cpm: 31.91
n_lines_expressing: 48
n_dd_up: 0
n_dd_down: 17
n_dd_up_clean: 0
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# NDST1

*N-deacetylase and N-sulfotransferase 1* — 5q33.1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.219× (z -19.9, q 0e+00, down in 44 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF142]] (+0.59, fdr 1e-05), [[PRDM11]] (+0.58, fdr 3e-04), [[DZIP1L]] (+0.58, fdr 3e-05); moves opposite to [[GCC2]] (-0.60, fdr 1e-05), [[BTG1]] (-0.59, fdr 1e-05), [[MINDY2]] (-0.55, fdr 1e-04).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[ADAM28]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 958.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.26× | +3.0 | 0.86 | 15/46 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 958.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.219×** | -19.9 | 0e+00 | 44/46 (A-172, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.227×** | -19.4 | 0e+00 | 46/46 (A-172, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.326×** | -14.7 | 0e+00 | 46/46 (A-172, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.636×** | -8.4 | 8e-15 | 30/46 (C32, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.537×** | -8.1 | 5e-14 | 35/46 (SW48, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.539×** | -8.1 | 6e-14 | 27/46 (A-172, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.599×** | -6.4 | 9e-09 | 34/46 (HOP62, NCI-H23, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.602×** | -6.4 | 1e-08 | 35/46 (LOX-IMVI, A-172, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.728×** | -5.9 | 3e-07 | 28/45 (A-172, HS-578T, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.646×** | -5.7 | 7e-07 | 29/46 (A-172, HS-578T, …) | two highest doses | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change | **0.671×** | -5.2 | 1e-05 | 21/42 (A-172, HEC-1-A, …) | two highest doses | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.675×** | -5.1 | 1e-05 | 28/46 (SK-MEL-2, BT-474, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.684×** | -4.8 | 8e-05 | 23/46 (AsPC-1, A-172, …) | two highest doses | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change | **0.690×** | -4.7 | 1e-04 | 19/32 (NCI-H460, A-172, …) | two highest doses | composition shift |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.585×** | -3.7 | 0.010 | 22/46 (SW1417, Panc 03.27, …) | rises with dose | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.773×** | -3.3 | 0.029 | 16/46 (A-172, HOP62, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | **0.787×** | -3.0 | 0.084 | 16/46 (SW1417, AN3 CA, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 958. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 138 | 0 | 15 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0615× (z -23.8) |
| [[AsPC-1 (line)]] | alt | 29.3 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -16.1) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.183× (z -9.4) |
| [[A-427 (line)]] | wt | 25.4 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.185× (z -11.4) |
| [[C32 (line)]] | wt | 28.1 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -17.6) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.152× (z -12.0) |
| [[HEC-1-A (line)]] | alt | 56.8 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.162× (z -15.5) |
| [[HOP62 (line)]] | alt | 39.3 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.159× (z -14.0) |
| [[HS-578T (line)]] | alt | 65.8 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.168× (z -13.8) |
| [[J82 (line)]] | alt | 46.9 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.186× (z -12.4) |
| [[NCI-H460 (line)]] | wt | 22.7 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0978× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.199× (z -12.4) |
| [[SK-MEL-2 (line)]] | alt | 43.9 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.124× (z -14.4) |
| [[LoVo (line)]] | wt | 27.3 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.121× (z -17.3) |
| [[MIA PaCa-2 (line)]] | alt | 47.3 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.169× (z -13.9) |
| [[SW48 (line)]] | wt | 29.3 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0863× (z -12.5) |
| [[A498 (line)]] | wt | 41.7 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.282× (z -11.7) |
| [[AN3 CA (line)]] | alt | 82.9 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.105× (z -11.6) |
| [[Hs 766T (line)]] | wt | 37.9 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.143× (z -12.5) |
| [[LOX-IMVI (line)]] | wt | 24.5 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.166× (z -12.6) |
| [[NCI-H1792 (line)]] | alt | 22.8 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.161× (z -11.4) |
| [[RKO (line)]] | wt | 34.3 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.119× (z -13.8) |
| [[A549 (line)]] | wt | 36.1 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.227× (z -10.3) |
| [[C-33 A (line)]] | alt | 32.9 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.153× (z -10.7) |
| [[KATO III (line)]] | alt | 13.1 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.180× (z -9.7) |
| [[SNU-1 (line)]] | wt | 42.0 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.129× (z -12.2) |
| [[HepG2_C3A (line)]] | wt | 28.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.140× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 30.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.161× (z -9.7) |
| [[LS 180 (line)]] | wt | 12.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -11.5) ⚠ cell-cycle shift, explains ~55% of this change |
| [[NCI-H23 (line)]] | alt | 18.5 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.106× (z -12.7) |
| [[NCI-H2347 (line)]] | alt | 22.8 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.228× (z -12.0) |
| [[Panc 03.27 (line)]] | alt | 27.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.227× (z -9.9) |
| [[PANC-1 (line)]] | alt | 34.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.298× (z -10.7) |
| [[RPMI-7951 (line)]] | alt | 33.0 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.247× (z -9.1) |
| [[SNU-423 (line)]] | alt | 52.3 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.264× (z -10.3) |
| [[SW 900 (line)]] | alt | 14.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.109× (z -10.4) |
| [[SW1417 (line)]] | alt | 20.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.222× (z -10.2) |
| [[SW480 (line)]] | alt | 11.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.221× (z -10.4) |
| [[BT-474 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.49 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 40.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.79 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 9.45 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 51.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 958), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF142]] | +0.59 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[PRDM11]] | +0.58 | +0.28 / +0.64 | both halves | 3e-04 |  |
| [[DZIP1L]] | +0.58 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[PYGO1]] | +0.58 | +0.38 / +0.49 | both halves | 7e-05 |  |
| [[ANKRD52]] | +0.58 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[ANKRD40]] | +0.58 | +0.37 / +0.56 | both halves | 8e-05 |  |
| [[HOMER2]] | +0.57 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[LETM1]] | +0.56 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[C1orf216]] | +0.56 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[TOR3A]] | +0.55 | +0.47 / +0.39 | both halves | 5e-05 |  |
| [[ZNF746]] | +0.55 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[USP46]] | +0.55 | +0.47 / +0.51 | both halves | 2e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GCC2]] | -0.60 | -0.65 / -0.55 | both halves | 1e-05 |  |
| [[BTG1]] | -0.59 | -0.56 / -0.51 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA |
| [[MINDY2]] | -0.55 | -0.34 / -0.52 | both halves | 1e-04 |  |
| [[ARID4A]] | -0.54 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[GCAT]] | -0.53 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[ANKRD37]] | -0.52 | -0.22 / -0.53 | both halves | 6e-04 |  |
| [[GOLPH3L]] | -0.52 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[INIP]] | -0.52 | -0.53 / -0.39 | both halves | 6e-05 |  |
| [[NOSIP]] | -0.52 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[CCNI]] | -0.51 | -0.37 / -0.48 | both halves | 7e-05 |  |
| [[PIBF1]] | -0.51 | -0.31 / -0.51 | both halves | 2e-04 |  |
| [[MAP3K13]] | -0.51 | -0.56 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAM28]] | B | ADAM28 activity lowers NDST1's level | lines that do not express ADAM28 (31) vs lines expressing it (19) | 1.44× higher at baseline in the lines without ADAM28 | 0.005 | ⚠ within organs, on part of the lines; also absent: DHRS9, BATF, IGFBP5 |
| [[NCS1]] | B | NCS1 activity raises NDST1's level | lines that do not express NCS1 (6) vs lines expressing it (44) | 2.50× lower at baseline in the lines without NCS1 | 0.006 | ⚠ within organs, on part of the lines; also absent: SH3BP5, ZNF618, PBK; maybe low, not absent |
| [[DZIP1L]] | B | DZIP1L activity raises NDST1's level | lines that do not express DZIP1L (8) vs lines expressing it (42) | 2.18× lower at baseline in the lines without DZIP1L | 0.008 | ⚠ within organs, on part of the lines; also absent: STARD9, CYP46A1, RECK; maybe low, not absent |
| [[HEG1]] | B | HEG1 activity raises NDST1's level | lines that do not express HEG1 (11) vs lines expressing it (39) | 2.22× lower at baseline in the lines without HEG1 | 0.008 | ⚠ within organs, on part of the lines; also absent: CCDC88A, STARD9, RECK |
| [[SLC4A3]] | B | SLC4A3 activity raises NDST1's level | lines that do not express SLC4A3 (8) vs lines expressing it (42) | 2.28× lower at baseline in the lines without SLC4A3 | 0.038 | ⚠ within organs, on part of the lines; also absent: SEMA6B, SLC29A4, MYO5A |
| [[PYGO1]] | B | PYGO1 activity raises NDST1's level | lines that do not express PYGO1 (16) vs lines expressing it (34) | 1.86× lower at baseline in the lines without PYGO1 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with ACVR2A; also absent: MIR130AHG, RBMS3, TCF7L1 |
| [[ADCY3]] | B | ADCY3 activity raises NDST1's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 1.64× lower at baseline in the lines without ADCY3 | 0.042 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |
| [[TOP2A]] | B | TOP2A activity raises NDST1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[FAM171A1]] | B | FAM171A1 activity raises NDST1's level | lines that do not express FAM171A1 (7) vs lines expressing it (43) | 1.61× lower at baseline in the lines without FAM171A1 | 0.088 | ⚠ within organs, on part of the lines; also absent: PORCN, CMTM7, ANXA6 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.472). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-9.5, 11.0); signed map (24.0, -38.6). **Vector** length 87.8, 20.6% of its response variance represented; |z| ≥ 3 in 1,001 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +6.5 | -1.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +4.9 | -1.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.7 | +3.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change | +4.7 | -4.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.3 | +0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | -1.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.8 | +1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.8 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | -1.0 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +2.5 | +2.1 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -2.5 | -19.4 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -1.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.2 | -19.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.2 | -14.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.2 | -5.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.9 | -1.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.8 | -1.5 |
|  | [[Terfenadine (drug)]] 5 µM |  | -1.7 | -2.0 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.6 | -1.1 |
|  | [[Glycyrrhizic acid (drug)]] 5 µM |  | -1.5 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | N-deacetylase and N-sulfotransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q33.1 — chr5:150,485,818-150,558,211 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NST1; previously HSST |
| Gene groups (HGNC) | Sulfotransferases, membrane bound |
| Hallmark sets | HYPOXIA |
| Reactome | 4 pathways, smallest: HS-GAG biosynthesis; Heparan sulfate/heparin (HS-GAG) metabolism; Glycosaminoglycan metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P52848](https://www.uniprot.org/uniprotkb/P52848) (Bifunctional heparan sulfate N-deacetylase/N-sulfotransferase 1):

> [Isoform 1]: Essential bifunctional enzyme that catalyzes both the N-deacetylation and the N-sulfation of glucosamine (GlcNAc) of the glycosaminoglycan in heparan sulfate. Modifies the GlcNAc-GlcA disaccharide repeating sugar backbone to make N-sulfated heparosan, a prerequisite substrate for later modifications in heparin biosynthesis. Plays a role in determining the extent and pattern of sulfation of heparan sulfate. Participates in biosynthesis of heparan sulfate that can ultimately serve as …

**Summary**, from NCBI Gene [3340](https://www.ncbi.nlm.nih.gov/gene/3340):

> This gene encodes a member of the heparan sulfate/heparin GlcNAc N-deacetylase/ N-sulfotransferase family. The encoded enzyme is a type II transmembrane protein that resides in the Golgi apparatus. The encoded protein catalyzes the transfer of sulfate from 3'-phosphoadenosine 5'-phosphosulfate to nitrogen of glucosamine in heparan sulfate. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2014]

**Accessions** — [HGNC:7680](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7680) · Entrez [3340](https://www.ncbi.nlm.nih.gov/gene/3340) · UniProt [P52848](https://www.uniprot.org/uniprotkb/P52848) · Ensembl [ENSG00000070614](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000070614)

## Data

Gene col 958: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 958); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 958, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 958]; `tensor/DDL_lfc|DDL_z.npy` [958]; `embed/gene_vectors.npy` [958]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 958 or target_col == 958). Every well: [[NDST1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDST1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
