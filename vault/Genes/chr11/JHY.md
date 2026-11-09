---
symbol: "JHY"
type: "gene"
col: 3096
ensembl_id: "ENSG00000109944"
name: "junctional cadherin complex regulator"
location: "11q24.1"
module: 10
arm: "+"
pooled_cpm: 9.0
n_lines_expressing: 35
n_dd_up: 12
n_dd_down: 17
n_dd_up_clean: 7
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 7
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# JHY

*junctional cadherin complex regulator* — 11q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.67× (z +7.0, q 2e-09, up in 11 of 24 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.62× (z +6.6, q 1e-08, up in 20 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (12 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.424× (z -11.6, q 4e-28, down in 23 of 32 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 0.422× (z -6.1, q 2e-07, down in 18 of 30 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KCNMB3]] (+0.61, fdr 1e-05), [[UBXN2A]] (+0.61, fdr 1e-04), [[ACYP2]] (+0.59, fdr 6e-05); moves opposite to [[RERE]] (-0.58, fdr 5e-05), [[KIAA1958]] (-0.58, fdr 3e-05), [[QSOX1]] (-0.55, fdr 4e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GCAWKR]] → it (grade B ⚠); 7 go from it, the strongest it → [[GALNT7-DT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3096.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.67×** | +7.0 | 2e-09 | 11/24 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.62×** | +6.6 | 1e-08 | 20/33 (SW480, J82, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +4.9 | 2e-04 | 6/15 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.28×** | +4.8 | 2e-04 | 13/33 (HCT15, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.36×** | +4.2 | 0.003 | 8/32 (SW480, PANC-1, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.37×** | +4.1 | 0.004 | 13/30 (SW480, LoVo, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.21×** | +3.7 | 0.020 | 11/33 (A-427, NCI-H2347, …) | top dose only | low cells (technical?) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.28×** | +3.4 | 0.044 | 5/32 (SW480, J82, …) | rises with dose |  |
| [[Adagrasib (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.067 | 8/33 (NCI-H23, NCI-H2030, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.20×** | +3.1 | 0.082 | 5/33 (SW480, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.26×** | +3.1 | 0.082 | 5/31 (CFPAC-1, SK-MEL-2, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.26×** | +3.1 | 0.082 | 9/30 (CFPAC-1, A-172, …) | all doses, stronger at high dose |  |
| [[Neratinib (drug)]] 5 µM |  | 1.25× | +3.0 | 0.10 | 6/32 (NCI-H2347, CFPAC-1, …) | top dose only |  |
| [[Meloxicam (drug)]] 0.05 µM |  | 1.25× | +3.0 | 0.10 | 4/32 (NCI-H460, NCI-H2030, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3096.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.424×** | -11.6 | 4e-28 | 23/32 (PANC-1, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.430×** | -11.4 | 1e-27 | 28/33 (PANC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.498×** | -9.4 | 1e-18 | 25/33 (A-172, PANC-1, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.422×** | -6.1 | 2e-07 | 18/30 (HS-578T, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.651×** | -5.8 | 7e-07 | 15/33 (NCI-H460, J82, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.441×** | -5.8 | 7e-07 | 17/33 (PANC-1, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.658×** | -5.6 | 2e-06 | 15/32 (SW480, PANC-1, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.770×** | -4.9 | 6e-05 | 15/32 (PANC-1, HS-578T, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | **0.694×** | -4.9 | 6e-05 | 15/29 (HS-578T, NCI-H1573, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.688×** | -4.8 | 8e-05 | 10/27 (HOP62, HT-29, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.728×** | -4.2 | 0.001 | 12/32 (A-172, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **0.807×** | -4.1 | 0.002 | 13/31 (A498, SNU-423, …) | rises with dose | composition shift |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.565×** | -4.0 | 0.003 | 10/28 (Panc 03.27, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.747×** | -3.9 | 0.004 | 9/32 (PANC-1, H4, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.756×** | -3.7 | 0.007 | 14/32 (SW480, SNU-423, …) | rises with dose |  |
| [[Piroxicam (drug)]] 0.05 µM |  | **0.800×** | -3.0 | 0.092 | 5/33 (SK-MEL-2, CFPAC-1, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.853× | -3.0 | 0.092 | 7/33 (HOP62, HS-578T, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.47 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3096. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 30.2 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.336× (z -10.9) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.418× (z -8.7) |
| [[A-172 (line)]] | wt | 10.3 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0835× (z -13.1) ⚠ cell-cycle shift, explains ~40% of this change |
| [[Panc 03.27 (line)]] | alt | 12.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.175× (z -9.6) ⚠ cell-cycle shift, explains ~19% of this change |
| [[A498 (line)]] | wt | 11.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -9.2) ⚠ cell-cycle shift, explains ~90% of this change |
| [[HOP62 (line)]] | alt | 17.0 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.235× (z -9.3) ⚠ cell-cycle shift, explains ~38% of this change |
| [[A-427 (line)]] | wt | 8.39 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.925 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 6.52 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.56 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.98 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.38 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.891 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.05 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.56 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.19 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.849 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.916 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.78 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 8.92 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3096), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCNMB3]] | +0.61 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[UBXN2A]] | +0.61 | +0.61 / +0.33 | both halves | 1e-04 |  |
| [[ACYP2]] | +0.59 | +0.53 / +0.39 | both halves | 6e-05 |  |
| [[CATSPERE]] | +0.57 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[CPLANE1]] | +0.57 | +0.50 / +0.46 | both halves | 2e-05 |  |
| [[IDNK]] | +0.56 | +0.50 / +0.35 | both halves | 1e-04 |  |
| [[AGA-DT]] | +0.56 | +0.46 / +0.41 | both halves | 4e-05 |  |
| [[ITSN2]] | +0.56 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[DNAI4]] | +0.55 | +0.50 / +0.35 | both halves | 1e-04 |  |
| [[RNLS]] | +0.55 | +0.42 / +0.41 | both halves | 4e-05 |  |
| [[NEK11]] | +0.54 | +0.52 / +0.42 | both halves | 4e-05 |  |
| [[ZFR]] | +0.54 | +0.45 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RERE]] | -0.58 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[KIAA1958]] | -0.58 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[QSOX1]] | -0.55 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[MALT1]] | -0.55 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[CABIN1]] | -0.53 | -0.40 / -0.38 | both halves | 6e-05 |  |
| [[TXNDC17]] | -0.52 | -0.40 / -0.36 | both halves | 9e-05 |  |
| [[SPICE1]] | -0.52 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[ARHGEF18]] | -0.50 | -0.42 / -0.37 | both halves | 8e-05 |  |
| [[PODXL2]] | -0.50 | -0.46 / -0.34 | both halves | 1e-04 |  |
| [[SLC2A3]] | -0.50 | -0.42 / -0.33 | both halves | 1e-04 |  |
| [[TRPT1]] | -0.50 | -0.37 / -0.28 | both halves | 3e-04 |  |
| [[NHP2]] | -0.49 | -0.39 / -0.41 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GCAWKR]] | B | GCAWKR activity raises JHY's level | lines that do not express GCAWKR (20) vs lines expressing it (30) | 2.72× lower at baseline in the lines without GCAWKR | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000232386, IL31RA, BEX2 |
| [[TSPAN5]] | B | TSPAN5 activity raises JHY's level | lines that do not express TSPAN5 (9) vs lines expressing it (41) | 2.58× lower at baseline in the lines without TSPAN5 | 0.057 | ⚠ within organs, on part of the lines; also absent: KLF12 |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GALNT7-DT]] | B | JHY activity raises GALNT7-DT's level | lines that do not express JHY (15) vs lines expressing it (35) | 1.43× lower at baseline in the lines without JHY | 0.030 | ⚠ within organs, on part of the lines; also absent: RGS17, KCNS3, BHLHE41 |
| [[SUCLG2-DT]] | B | JHY activity raises SUCLG2-DT's level | lines that do not express JHY (15) vs lines expressing it (35) | 1.79× lower at baseline in the lines without JHY | 0.031 | ⚠ within organs, on part of the lines; also absent: RGS17, KCNS3, BHLHE41 |
| [[ACCS]] | B | JHY activity raises ACCS's level | lines that do not express JHY (15) vs lines expressing it (35) | 1.97× lower at baseline in the lines without JHY | 0.042 | ⚠ within organs, on part of the lines; also absent: RGS17, KCNS3, BHLHE41 |
| [[TSPAN5]] | B | JHY activity raises TSPAN5's level | lines that do not express JHY (15) vs lines expressing it (35) | 2.56× lower at baseline in the lines without JHY | 0.060 | ⚠ within organs, on part of the lines; also absent: RGS17, KCNS3, BHLHE41 |
| [[NEK11]] | B | JHY activity raises NEK11's level | lines that do not express JHY (15) vs lines expressing it (35) | 1.34× lower at baseline in the lines without JHY | 0.064 | ⚠ within organs, on part of the lines; also absent: RGS17, KCNS3, BHLHE41 |
| [[CCDC122]] | B | JHY activity raises CCDC122's level | lines that do not express JHY (15) vs lines expressing it (35) | 2.06× lower at baseline in the lines without JHY | 0.075 | ⚠ within organs, on part of the lines; also absent: RGS17, KCNS3, BHLHE41 |
| [[CC2D2A]] | B | JHY activity raises CC2D2A's level | lines that do not express JHY (15) vs lines expressing it (35) | 1.25× lower at baseline in the lines without JHY | 0.093 | ⚠ within organs, on part of the lines; also absent: RGS17, KCNS3, BHLHE41 |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.549). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-1.3, 11.1); signed map (32.2, -12.7). **Vector** length 57.0, 10.8% of its response variance represented; |z| ≥ 3 in 653 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +4.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.2 | +2.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.1 | +0.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | +6.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.1 | +4.8 |
|  | [[Neratinib (drug)]] 5 µM |  | +1.7 | +3.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.6 | +4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.6 | +1.0 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -3.2 | -11.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -2.7 | -11.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -2.7 | -9.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.7 | -5.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.7 | -5.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.4 | -2.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.3 | -6.1 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.3 | -1.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.2 | -2.3 |
|  | [[Fumaric acid (drug)]] 5 µM |  | -1.2 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | junctional cadherin complex regulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q24.1 — chr11:122,882,683-122,963,862 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23554; previously C11orf63 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6NUN7](https://www.uniprot.org/uniprotkb/Q6NUN7) (Jhy protein homolog):

> Required for the normal development of cilia in brain ependymal cells lining the ventricular surfaces.

**Summary**, from NCBI Gene [79864](https://www.ncbi.nlm.nih.gov/gene/79864):

> Predicted to be involved in axoneme assembly and brain development. Predicted to act upstream of or within several processes, including cerebrospinal fluid circulation; motile cilium assembly; and regulation of establishment of planar polarity. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26288](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26288) · Entrez [79864](https://www.ncbi.nlm.nih.gov/gene/79864) · UniProt [Q6NUN7](https://www.uniprot.org/uniprotkb/Q6NUN7) · Ensembl [ENSG00000109944](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109944)

## Data

Gene col 3096: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3096); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3096, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3096]; `tensor/DDL_lfc|DDL_z.npy` [3096]; `embed/gene_vectors.npy` [3096]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3096 or target_col == 3096). Every well: [[JHY — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/JHY.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
