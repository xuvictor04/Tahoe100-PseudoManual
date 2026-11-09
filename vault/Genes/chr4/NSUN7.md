---
symbol: "NSUN7"
type: "gene"
col: 11018
ensembl_id: "ENSG00000179299"
name: "NOP2/Sun RNA methyltransferase family member 7"
location: "4p14"
module: 8
arm: "+"
pooled_cpm: 9.36
n_lines_expressing: 28
n_dd_up: 12
n_dd_down: 14
n_dd_up_clean: 7
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 26
direction_downstream: 11
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# NSUN7

*NOP2/Sun RNA methyltransferase family member 7* — 4p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.25× (z +16.8, q 0e+00, up in 6 of 19 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.43× (z +5.1, q 5e-05, up in 13 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.556× (z -8.4, q 3e-14, down in 19 of 24 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADCY4]] (+0.67, fdr 7e-06), [[FAAH2]] (+0.66, fdr 7e-06), [[TMC4]] (+0.63, fdr 1e-05); moves opposite to [[ASAP1]] (-0.47, fdr 8e-05), [[GALNT1]] (-0.46, fdr 1e-04), [[CD59]] (-0.45, fdr 5e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 26 arrows point to it, the strongest [[SMPDL3B]] → it (grade B ⚠); 11 go from it, the strongest it → [[ARHGAP30]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11018.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.25×** | +16.8 | 0e+00 | 6/19 (SW 900, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.76×** | +13.9 | 3e-41 | 4/12 (NCI-H2347, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.14×** | +10.0 | 2e-21 | 2/15 (SW 900, PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.43×** | +5.1 | 5e-05 | 13/24 (LS 180, CFPAC-1, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +5.0 | 6e-05 | 2/22 (J82, C-33 A) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.35×** | +4.3 | 0.002 | 4/23 (SW 900, A549, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +4.2 | 0.002 | 5/25 (PANC-1, Hs 766T, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.32×** | +3.9 | 0.007 | 3/23 (SW480, J82, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.31×** | +3.8 | 0.007 | 7/23 (PANC-1, SW 900, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.43×** | +3.6 | 0.017 | 2/19 (BT-474, NCI-H23) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.25×** | +3.2 | 0.071 | 0/24 | two highest doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.26×** | +3.1 | 0.080 | 3/23 (NCI-H23, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11018.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.556×** | -8.4 | 3e-14 | 19/24 (NCI-H23, HT-29, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.606×** | -7.2 | 2e-10 | 17/24 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.618×** | -6.9 | 1e-09 | 20/25 (NCI-H1573, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.514×** | -5.0 | 9e-05 | 15/23 (COLO 205, LS 180, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.733×** | -4.4 | 0.001 | 12/25 (NCI-H1792, HT-29, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.743×** | -4.2 | 0.002 | 13/24 (SW480, HT-29, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.766×** | -3.8 | 0.011 | 10/24 (NCI-H1573, LS 180, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.762×** | -3.7 | 0.013 | 13/24 (COLO 205, NCI-H1792, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.775×** | -3.6 | 0.017 | 10/24 (SW480, BT-474, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **0.627×** | -3.5 | 0.027 | 13/22 (HT-29, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.639×** | -3.3 | 0.042 | 19/23 (HT-29, CFPAC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.645×** | -3.3 | 0.047 | 7/22 (NCI-H661, Panc 03.27, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.796×** | -3.3 | 0.047 | 17/21 (COLO 205, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.794×** | -3.2 | 0.060 | 3/24 (NCI-H1792, PANC-1, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11018. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 29.2 | 0 | 6 (4 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.0202× (z -13.9) |
| [[COLO 205 (line)]] | alt | 35.6 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.195× (z -10.2) |
| [[NCI-H1792 (line)]] | alt | 26.3 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -15.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.262× (z -8.5) |
| [[LS 180 (line)]] | wt | 41.4 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.311× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[NCI-H1573 (line)]] | alt | 19.9 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0994× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.273× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 12.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.116× (z -10.6) |
| [[SW480 (line)]] | alt | 10.8 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.196× (z -11.6) |
| [[A-172 (line)]] | wt | 7.13 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.161× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 16.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.237× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[SHP-77 (line)]] | alt | 24.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.147× (z -10.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 9.68 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.95 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.08 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.61 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.56 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.30 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.76 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.982 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.77 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.19 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 9.16 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11018), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADCY4]] | +0.67 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[FAAH2]] | +0.66 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[TMC4]] | +0.63 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[C11orf52]] | +0.62 | +0.65 / +0.40 | both halves | 4e-05 |  |
| [[ESRP1]] | +0.61 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[RORC]] | +0.59 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[LINC02253]] | +0.59 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[ERBB3]] | +0.58 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[ILDR1]] | +0.58 | +0.61 / +0.40 | both halves | 5e-05 |  |
| [[EPCAM-DT]] | +0.57 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[ICA1]] | +0.56 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[LINC02967]] | +0.56 | +0.49 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASAP1]] | -0.47 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[GALNT1]] | -0.46 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[CD59]] | -0.45 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[PHC2]] | -0.44 | -0.42 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 23, C 3. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMPDL3B]] | B | SMPDL3B activity raises NSUN7's level | lines that do not express SMPDL3B (23) vs lines expressing it (27) | 3.08× lower at baseline in the lines without SMPDL3B | 0.010 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HOOK1, BSPRY, SPINT1-AS1 |
| [[FAAH2]] | B | FAAH2 activity raises NSUN7's level | lines that do not express FAAH2 (26) vs lines expressing it (24) | 2.11× lower at baseline in the lines without FAAH2 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent |
| [[BSPRY]] | B | BSPRY activity raises NSUN7's level | lines that do not express BSPRY (29) vs lines expressing it (21) | 2.68× lower at baseline in the lines without BSPRY | 0.011 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPCAM, RAB25 |
| [[MAL2]] | B | MAL2 activity raises NSUN7's level | lines that do not express MAL2 (31) vs lines expressing it (19) | 2.08× lower at baseline in the lines without MAL2 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RAB25, TMEM125, CDH1 |
| [[RASSF6]] | B | RASSF6 activity raises NSUN7's level | lines that do not express RASSF6 (28) vs lines expressing it (22) | 2.60× lower at baseline in the lines without RASSF6 | 0.028 | ⚠ within organs, on part of the lines; also absent: TOX3, ELF3, ITGB6 |
| [[GALM]] | B | GALM activity raises NSUN7's level | lines that do not express GALM (11) vs lines expressing it (39) | 2.03× lower at baseline in the lines without GALM | 0.050 | ⚠ within organs, on part of the lines; also absent: ACOT11, GRIN2D, STAP2; maybe low, not absent |
| [[KCNE3]] | B | KCNE3 activity raises NSUN7's level | lines that do not express KCNE3 (37) vs lines expressing it (13) | 2.79× lower at baseline in the lines without KCNE3 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SKAP1, SLC5A1, VWA2 |
| [[TTC22]] | B | TTC22 activity raises NSUN7's level | lines that do not express TTC22 (32) vs lines expressing it (18) | 2.51× lower at baseline in the lines without TTC22 | 0.052 | ⚠ within organs, on part of the lines; also absent: COL17A1, TRIM15, SERPINB5 |
| [[ELF3]] | B | ELF3 activity raises NSUN7's level | lines that do not express ELF3 (23) vs lines expressing it (27) | 2.26× lower at baseline in the lines without ELF3 | 0.054 | ⚠ within organs, on part of the lines; also absent: RASSF6, GOLT1A, LAMA3 |
| [[FUT3]] | B | FUT3 activity raises NSUN7's level | lines that do not express FUT3 (29) vs lines expressing it (21) | 1.81× lower at baseline in the lines without FUT3 | 0.055 | ⚠ within organs, on part of the lines; also absent: ATP2C2, TMEM125, ENSG00000243004 |
| [[TMEM125]] | B | TMEM125 activity raises NSUN7's level | lines that do not express TMEM125 (33) vs lines expressing it (17) | 2.50× lower at baseline in the lines without TMEM125 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14 |
| [[TCEA3]] | B | TCEA3 activity raises NSUN7's level | lines that do not express TCEA3 (14) vs lines expressing it (36) | 2.16× lower at baseline in the lines without TCEA3 | 0.058 | ⚠ within organs, on part of the lines; also absent: ZNF43, ENSG00000267383, ZNF681; maybe low, not absent |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 10, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGAP30]] | B | NSUN7 activity weakens ARHGAP30's drug response | lines that do not express NSUN7 (13) vs lines expressing it (13) | (z diff -3.24); strongest at Homoharringtonine 5 µM: 2.25x vs 0.27x (z diff -9.3) | 0.016 | ⚠ within organs, on part of the lines; also absent: NEBL, KIF1A, FRMPD3; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[TCEA3]] | B | NSUN7 activity raises TCEA3's level | lines that do not express NSUN7 (22) vs lines expressing it (28) | 2.33× lower at baseline in the lines without NSUN7 | 0.030 | ⚠ within organs, on part of the lines; also absent: NEBL, KIF1A, FRMPD3; maybe low, not absent |
| [[PROM2]] | B | NSUN7 activity raises PROM2's level | lines that do not express NSUN7 (22) vs lines expressing it (28) | 1.78× lower at baseline in the lines without NSUN7 | 0.060 | ⚠ within organs, on part of the lines; also absent: NEBL, KIF1A, FRMPD3; maybe low, not absent |
| [[HOTAIR]] | B | NSUN7 activity raises HOTAIR's level | lines that do not express NSUN7 (22) vs lines expressing it (28) | 1.54× lower at baseline in the lines without NSUN7 | 0.060 | ⚠ within organs, on part of the lines; also absent: NEBL, KIF1A, FRMPD3; maybe low, not absent |
| [[SLC28A3]] | B | NSUN7 activity raises SLC28A3's level | lines that do not express NSUN7 (22) vs lines expressing it (28) | 1.72× lower at baseline in the lines without NSUN7 | 0.083 | ⚠ within organs, on part of the lines; also absent: NEBL, KIF1A, FRMPD3; maybe low, not absent |
| [[EPCAM-DT]] | B | NSUN7 activity raises EPCAM-DT's level | lines that do not express NSUN7 (22) vs lines expressing it (28) | 1.85× lower at baseline in the lines without NSUN7 | 0.086 | ⚠ within organs, on part of the lines; also absent: NEBL, KIF1A, FRMPD3; maybe low, not absent |
| [[RINL]] | B | NSUN7 activity raises RINL's level | lines that do not express NSUN7 (22) vs lines expressing it (28) | 1.37× lower at baseline in the lines without NSUN7 | 0.087 | ⚠ within organs, on part of the lines; also absent: NEBL, KIF1A, FRMPD3; maybe low, not absent |
| [[SYTL1]] | B | NSUN7 activity raises SYTL1's level | lines that do not express NSUN7 (22) vs lines expressing it (28) | 1.65× lower at baseline in the lines without NSUN7 | 0.089 | ⚠ within organs, on part of the lines; also absent: NEBL, KIF1A, FRMPD3; maybe low, not absent |
| [[ICA1]] | B | NSUN7 activity raises ICA1's level | lines that do not express NSUN7 (22) vs lines expressing it (28) | 2.39× lower at baseline in the lines without NSUN7 | 0.094 | ⚠ within organs, on part of the lines; also absent: NEBL, KIF1A, FRMPD3; maybe low, not absent |
| [[RORC]] | B | NSUN7 activity raises RORC's level | lines that do not express NSUN7 (22) vs lines expressing it (28) | 1.75× lower at baseline in the lines without NSUN7 | 0.099 | ⚠ within organs, on part of the lines; also absent: NEBL, KIF1A, FRMPD3; maybe low, not absent |
| [[LINC01876]] | C | NSUN7 activity raises LINC01876's level | lines that do not express NSUN7 (22) vs lines expressing it (28) | 3.41× lower at baseline in the lines without NSUN7 | 0.009 | ⚠ within organs, on part of the lines; also absent: NEBL, KIF1A, FRMPD3; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.632). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.0, 49.4); signed map (57.3, 4.5). **Vector** length 48.8, 10.3% of its response variance represented; |z| ≥ 3 in 513 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.9 | +13.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.6 | +16.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.2 | +10.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +5.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.4 | +1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +4.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.2 | +3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +0.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +5.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.6 | +0.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.6 | -8.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.7 | -4.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -1.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -1.4 | -6.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.4 | -1.8 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.4 | -1.2 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.3 | -1.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.3 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | NOP2/Sun RNA methyltransferase family member 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p14 — chr4:40,749,925-40,811,184 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14001 |
| Gene groups (HGNC) | NOP2/Sun RNA methyltransferase family; DNA/RNA methyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NE18](https://www.uniprot.org/uniprotkb/Q8NE18) (Protein NSUN7):

> Plays an essential for sperm flagellum assembly.

**Summary**, from NCBI Gene [79730](https://www.ncbi.nlm.nih.gov/gene/79730):

> Predicted to enable RNA binding activity and methyltransferase activity. Predicted to be involved in methylation. Predicted to act upstream of or within flagellated sperm motility and sperm mitochondrion organization. Predicted to be located in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25857](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25857) · Entrez [79730](https://www.ncbi.nlm.nih.gov/gene/79730) · UniProt [Q8NE18](https://www.uniprot.org/uniprotkb/Q8NE18) · Ensembl [ENSG00000179299](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179299)

## Data

Gene col 11018: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11018); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11018, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11018]; `tensor/DDL_lfc|DDL_z.npy` [11018]; `embed/gene_vectors.npy` [11018]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11018 or target_col == 11018). Every well: [[NSUN7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NSUN7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
