---
symbol: "MANSC1"
type: "gene"
col: 3210
ensembl_id: "ENSG00000111261"
name: "MANSC domain containing 1"
location: "12p13.2"
module: 44
arm: "+"
pooled_cpm: 4.58
n_lines_expressing: 34
n_dd_up: 10
n_dd_down: 25
n_dd_up_clean: 5
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 50
direction_downstream: 26
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# MANSC1

*MANSC domain containing 1* — 12p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.44× (z +9.1, q 5e-17, up in 7 of 15 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.39× (z +4.8, q 2e-04, up in 11 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.520× (z -9.5, q 2e-18, down in 23 of 27 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ST6GALNAC1]] (+0.72, fdr 7e-06), [[C9orf152]] (+0.67, fdr 7e-06), [[MUC5B]] (+0.67, fdr 7e-06).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 50 arrows point to it, the strongest [[ST6GALNAC1]] → it (grade B ⚠); 26 go from it, the strongest it → [[TNFRSF21]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3210.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.44×** | +9.1 | 5e-17 | 7/15 (HEC-1-A, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.48×** | +8.9 | 1e-16 | 2/4 (KATO III, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.97×** | +6.4 | 3e-08 | 4/10 (Panc 03.27, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.39×** | +4.8 | 2e-04 | 11/32 (LoVo, RKO, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +4.5 | 7e-04 | 6/22 (SW1417, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.53×** | +4.4 | 0.001 | 5/22 (HT-29, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.51×** | +4.2 | 0.002 | 13/32 (A-427, SW1417, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +3.9 | 0.007 | 11/32 (SW480, NCI-H2347, …) | rises with dose | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.46×** | +3.9 | 0.007 | 5/32 (COLO 205, SW480, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +3.6 | 0.015 | 4/32 (NCI-H2030, HepG2/C3A, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.42×** | +3.6 | 0.017 | 8/32 (NCI-H2347, BT-474, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3210.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.520×** | -9.5 | 2e-18 | 23/27 (COLO 205, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.412×** | -9.1 | 3e-17 | 24/32 (COLO 205, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.507×** | -6.9 | 7e-10 | 22/32 (KATO III, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.515×** | -6.8 | 2e-09 | 15/26 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.523×** | -6.6 | 4e-09 | 18/27 (COLO 205, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.538×** | -6.3 | 2e-08 | 18/32 (KATO III, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.576×** | -5.6 | 1e-06 | 19/32 (RKO, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.583×** | -5.5 | 2e-06 | 18/32 (LS 180, KATO III, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.602×** | -5.2 | 1e-05 | 14/32 (KATO III, HT-29, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.637×** | -4.6 | 2e-04 | 16/32 (AsPC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.638×** | -4.6 | 2e-04 | 15/32 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.627×** | -4.6 | 2e-04 | 15/31 (COLO 205, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.636×** | -4.4 | 6e-04 | 20/32 (KATO III, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.675×** | -4.0 | 0.002 | 9/32 (RPMI-7951, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.710×** | -3.5 | 0.017 | 12/31 (KATO III, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.500×** | -3.5 | 0.018 | 10/27 (LS 180, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **0.704×** | -3.4 | 0.018 | 9/32 (NCI-H1573, HepG2/C3A, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3210. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 28.4 | 0 | 8 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0863× (z -17.9) |
| [[LS 180 (line)]] | wt | 13.7 | 0 | 7 | — | [[Panobinostat (drug)]] 5 µM 0.0834× (z -12.8) |
| [[COLO 205 (line)]] | alt | 30.7 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0628× (z -20.6) |
| [[HT-29 (line)]] | alt | 16.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -11.6) |
| [[C32 (line)]] | wt | 4.99 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0300× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 4.72 | 0 | 2 | — | [[Digitoxin (drug)]] 0.05 µM 0.106× (z -9.0) |
| [[CFPAC-1 (line)]] | alt | 4.88 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -10.5) |
| [[SW 900 (line)]] | alt | 7.04 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0586× (z -9.1) |
| [[SW1417 (line)]] | alt | 5.99 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0823× (z -9.8) |
| [[A-172 (line)]] | wt | 0.512 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 5.56 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.385 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.791 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.780 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.965 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.699 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.50 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.731 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.14 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.627 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.53 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.499 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.915 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.873 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.08 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.99 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.992 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.988 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.855 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.903 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.05 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3210), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST6GALNAC1]] | +0.72 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[C9orf152]] | +0.67 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[MUC5B]] | +0.67 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[PRR15]] | +0.67 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[PROM2]] | +0.66 | +0.62 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[TSPAN8]] | +0.66 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[GJB1]] | +0.65 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[KCNE3]] | +0.64 | +0.64 / +0.57 | both halves | 9e-06 |  |
| [[CLRN3]] | +0.64 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[SORL1]] | +0.64 | +0.64 / +0.58 | both halves | 8e-06 |  |
| [[RNF43]] | +0.63 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[PPP1R1B]] | +0.63 | +0.67 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*50 arrows, 50 of them with an alert ⚠; grade A 0, B 41, C 9. Shown: the 12 strongest; 38 more arrows (38 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ST6GALNAC1]] | B | ST6GALNAC1 activity raises MANSC1's level | lines that do not express ST6GALNAC1 (37) vs lines expressing it (13) | 3.04× lower at baseline in the lines without ST6GALNAC1 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, SLC44A4, STEAP4 |
| [[CRACDL]] | B | CRACDL activity raises MANSC1's level | lines that do not express CRACDL (25) vs lines expressing it (25) | 2.29× lower at baseline in the lines without CRACDL | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CGN, MARVELD3, CASC19 |
| [[RAB25]] | B | RAB25 activity raises MANSC1's level | lines that do not express RAB25 (33) vs lines expressing it (17) | 2.85× lower at baseline in the lines without RAB25 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, TMEM30B, PRSS8 |
| [[FXYD3]] | B | FXYD3 activity raises MANSC1's level | lines that do not express FXYD3 (34) vs lines expressing it (16) | 2.76× lower at baseline in the lines without FXYD3 | 0.007 | ⚠ within organs, on part of the lines; also absent: CEACAM6, TMEM30B, TMPRSS2 |
| [[TCN1]] | B | TCN1 activity raises MANSC1's level | lines that do not express TCN1 (37) vs lines expressing it (13) | 2.42× lower at baseline in the lines without TCN1 | 0.010 | ⚠ within organs, on part of the lines; also absent: AGR3, MUC5AC, MUC5B |
| [[ERBB3]] | B | ERBB3 activity raises MANSC1's level | lines that do not express ERBB3 (27) vs lines expressing it (23) | 2.50× lower at baseline in the lines without ERBB3 | 0.011 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM |
| [[SORL1]] | B | SORL1 activity raises MANSC1's level | lines that do not express SORL1 (21) vs lines expressing it (29) | 2.12× lower at baseline in the lines without SORL1 | 0.011 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PLEKHG6, SLC52A3 |
| [[PRR15]] | B | PRR15 activity raises MANSC1's level | lines that do not express PRR15 (28) vs lines expressing it (22) | 2.35× lower at baseline in the lines without PRR15 | 0.013 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, RNF223, FAM110C |
| [[SYNPR-AS1]] | B | SYNPR-AS1 activity raises MANSC1's level | lines that do not express SYNPR-AS1 (33) vs lines expressing it (17) | 2.43× lower at baseline in the lines without SYNPR-AS1 | 0.014 | ⚠ within organs, on part of the lines; also absent: PPP1R1B, SLC6A20, FXYD3 |
| [[TMPRSS2]] | B | TMPRSS2 activity raises MANSC1's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 2.61× lower at baseline in the lines without TMPRSS2 | 0.015 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[SLC6A14]] | B | SLC6A14 activity raises MANSC1's level | lines that do not express SLC6A14 (39) vs lines expressing it (11) | 2.54× lower at baseline in the lines without SLC6A14 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DAPP1, MUC5AC, ST6GALNAC1 |
| [[CLDN3]] | B | CLDN3 activity raises MANSC1's level | lines that do not express CLDN3 (28) vs lines expressing it (22) | 2.44× lower at baseline in the lines without CLDN3 | 0.017 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, ESRP1 |

### Downstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 22, C 4. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNFRSF21]] | B | MANSC1 activity raises TNFRSF21's level | lines that do not express MANSC1 (16) vs lines expressing it (34) | 3.46× lower at baseline in the lines without MANSC1 | 0.006 | ⚠ within organs, on part of the lines; also absent: ENSG00000288656, MYO5C, EVPL; maybe low, not absent |
| [[DLG3]] | B | MANSC1 activity raises DLG3's level | lines that do not express MANSC1 (16) vs lines expressing it (34) | 2.29× lower at baseline in the lines without MANSC1 | 0.021 | ⚠ within organs, on part of the lines; also absent: ENSG00000288656, MYO5C, EVPL; maybe low, not absent |
| [[CHN2]] | B | MANSC1 activity raises CHN2's level | lines that do not express MANSC1 (16) vs lines expressing it (34) | 3.12× lower at baseline in the lines without MANSC1 | 0.030 | ⚠ within organs, on part of the lines; also absent: ENSG00000288656, MYO5C, EVPL; maybe low, not absent |
| [[TSPAN1]] | B | MANSC1 activity raises TSPAN1's level | lines that do not express MANSC1 (16) vs lines expressing it (34) | 2.61× lower at baseline in the lines without MANSC1 | 0.036 | ⚠ within organs, on part of the lines; also absent: ENSG00000288656, MYO5C, EVPL; maybe low, not absent |
| [[SULT1A1]] | B | MANSC1 activity raises SULT1A1's level | lines that do not express MANSC1 (16) vs lines expressing it (34) | 1.86× lower at baseline in the lines without MANSC1 | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000288656, MYO5C, EVPL; maybe low, not absent |
| [[CLDN3]] | B | MANSC1 activity raises CLDN3's level | lines that do not express MANSC1 (16) vs lines expressing it (34) | 3.19× lower at baseline in the lines without MANSC1 | 0.042 | ⚠ within organs, on part of the lines; also absent: ENSG00000288656, MYO5C, EVPL; maybe low, not absent |
| [[ELOVL4]] | B | MANSC1 activity lowers ELOVL4's level | lines that do not express MANSC1 (16) vs lines expressing it (34) | 2.73× higher at baseline in the lines without MANSC1 | 0.045 | ⚠ within organs, on part of the lines; also absent: ENSG00000288656, MYO5C, EVPL; maybe low, not absent |
| [[ERBB3]] | B | MANSC1 activity raises ERBB3's level | lines that do not express MANSC1 (16) vs lines expressing it (34) | 3.99× lower at baseline in the lines without MANSC1 | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000288656, MYO5C, EVPL; maybe low, not absent |
| [[TNFRSF14-AS1]] | B | MANSC1 activity raises TNFRSF14-AS1's level | lines that do not express MANSC1 (16) vs lines expressing it (34) | 1.90× lower at baseline in the lines without MANSC1 | 0.051 | ⚠ within organs, on part of the lines; also absent: ENSG00000288656, MYO5C, EVPL; maybe low, not absent |
| [[SORL1]] | B | MANSC1 activity raises SORL1's level | lines that do not express MANSC1 (16) vs lines expressing it (34) | 2.87× lower at baseline in the lines without MANSC1 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000288656, MYO5C, EVPL; maybe low, not absent |
| [[ILDR1]] | B | MANSC1 activity raises ILDR1's level | lines that do not express MANSC1 (16) vs lines expressing it (34) | 1.96× lower at baseline in the lines without MANSC1 | 0.062 | ⚠ within organs, on part of the lines; also absent: ENSG00000288656, MYO5C, EVPL; maybe low, not absent |
| [[PRR15]] | B | MANSC1 activity raises PRR15's level | lines that do not express MANSC1 (16) vs lines expressing it (34) | 2.20× lower at baseline in the lines without MANSC1 | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000288656, MYO5C, EVPL; maybe low, not absent |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.728). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.8, 49.7); signed map (64.2, 4.9). **Vector** length 61.4, 12.1% of its response variance represented; |z| ≥ 3 in 752 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Glucuronidation* (reactome, mean cos +0.55 to 4); *Aspirin ADME* (reactome, mean cos +0.55 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +8.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +9.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +6.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +3.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.7 | +4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +0.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +4.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +2.5 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.5 | +0.4 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -5.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.1 | -4.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.9 | -3.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.8 | -4.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.8 | -3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.3 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | MANSC domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.2 — chr12:12,326,056-12,350,242 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10298, LOH12CR3 |
| Matched by | ensembl_id |

UniProt [Q9H8J5](https://www.uniprot.org/uniprotkb/Q9H8J5) carries no function annotation.

**Summary**, from NCBI Gene [54682](https://www.ncbi.nlm.nih.gov/gene/54682):

> Predicted to be located in membrane. Predicted to be active in Golgi apparatus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25505](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25505) · Entrez [54682](https://www.ncbi.nlm.nih.gov/gene/54682) · UniProt [Q9H8J5](https://www.uniprot.org/uniprotkb/Q9H8J5) · Ensembl [ENSG00000111261](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111261)

## Data

Gene col 3210: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3210); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3210, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3210]; `tensor/DDL_lfc|DDL_z.npy` [3210]; `embed/gene_vectors.npy` [3210]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3210 or target_col == 3210). Every well: [[MANSC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MANSC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
