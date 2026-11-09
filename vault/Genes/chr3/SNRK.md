---
symbol: "SNRK"
type: "gene"
col: 8777
ensembl_id: "ENSG00000163788"
name: "SNF related kinase"
location: "3p22.1"
module: 34
arm: "+"
pooled_cpm: 56.73
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 13
n_dd_up_clean: 0
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 30
direction_downstream: 1
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# SNRK

*SNF related kinase* — 3p22.1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 2.50×; ⚠ cell-cycle shift, explains ~20% of this change).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.525× (z -10.8, q 3e-24, down in 38 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.593× (z -8.7, q 4e-16, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HS3ST1]] (+0.54, fdr 1e-05), [[GJB3]] (+0.53, fdr 2e-05), [[STK39]] (+0.53, fdr 2e-05); moves opposite to [[CLN3]] (-0.43, fdr 3e-04), [[SPATA24]] (-0.42, fdr 8e-05), [[SCAMP3]] (-0.40, fdr 2e-04).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 30 arrows point to it, the strongest [[C1orf116]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Minodronic acid (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8777.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 2.50×; ⚠ cell-cycle shift, explains ~20% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | 1.23× | +3.4 | 0.20 | 22/48 (AsPC-1, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | 1.22× | +3.4 | 0.20 | 18/48 (LoVo, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8777.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.525×** | -10.8 | 3e-24 | 38/46 (SW48, LS 180, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.562×** | -9.3 | 6e-18 | 30/42 (AsPC-1, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.553×** | -9.2 | 1e-17 | 32/44 (A-427, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.593×** | -8.7 | 4e-16 | 40/48 (SW 1271, NCI-H23, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.670×** | -6.4 | 1e-08 | 33/47 (LoVo, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.761×** | -4.6 | 5e-04 | 22/48 (CFPAC-1, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change | **0.782×** | -4.1 | 0.003 | 24/47 (NCI-H460, SW480, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.844× | -4.0 | 0.004 | 19/48 (LS 180, AsPC-1, …) | all doses, flat | low cells (technical?) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.810×** | -3.5 | 0.026 | 17/48 (SW1417, LS 180, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM |  | **0.811×** | -3.5 | 0.027 | 19/49 (NCI-H2122, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **0.817×** | -3.4 | 0.037 | 19/47 (SNU-1, NCI-H2030, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **0.819×** | -3.3 | 0.038 | 20/47 (SW1417, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Bendamustine (drug)]] 5 µM |  | **0.819×** | -3.2 | 0.057 | 16/47 (A549, LoVo, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | **0.826×** | -3.1 | 0.086 | 10/48 (SW 1088, AsPC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8777. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 221 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0993× (z -22.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 92.0 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.234× (z -12.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 65.5 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.135× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.326× (z -10.0) |
| [[SW480 (line)]] | alt | 53.3 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.322× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.462× (z -9.5) |
| [[LoVo (line)]] | wt | 91.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.300× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 29.8 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.326× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 144 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.340× (z -10.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 45.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.196× (z -14.5) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 61.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.207× (z -12.1) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 127 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.292× (z -11.8) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 101 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -12.1) ⚠ cell-cycle shift, explains ~95% of this change |
| [[KATO III (line)]] | alt | 85.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.204× (z -15.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 120 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.149× (z -14.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 55.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.298× (z -11.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 90.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -13.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 45.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.348× (z -9.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 35.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.314× (z -10.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 57.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.156× (z -9.4) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 52.3 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.0622× (z -13.3) |
| [[HOP62 (line)]] | alt | 41.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.391× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 22.2 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +9.6) ⚠ cell-cycle shift, explains ~20% of this change | — |
| [[NCI-H1573 (line)]] | alt | 38.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.375× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 29.0 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.292× (z -10.2) |
| [[PANC-1 (line)]] | alt | 32.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.376× (z -10.4) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 46.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.239× (z -9.2) |
| [[SW 1271 (line)]] | alt | 66.5 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0483× (z -11.6) |
| [[SW48 (line)]] | wt | 45.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0818× (z -16.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 34.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 44.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 42.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 37.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 80.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 31.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8777), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HS3ST1]] | +0.54 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[GJB3]] | +0.53 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[STK39]] | +0.53 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[CAB39]] | +0.53 | +0.50 / +0.51 | both halves | 1e-05 | STRING 821 |
| [[FERMT1]] | +0.52 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[TTC9]] | +0.51 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[TMC7]] | +0.50 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[PTK2B]] | +0.50 | +0.41 / +0.49 | both halves | 4e-05 |  |
| [[MALL]] | +0.48 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[TGFA]] | +0.48 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[BTBD10]] | +0.47 | +0.50 / +0.40 | both halves | 5e-05 |  |
| [[BCL2L1]] | +0.47 | +0.46 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLN3]] | -0.43 | -0.28 / -0.46 | both halves | 3e-04 |  |
| [[SPATA24]] | -0.42 | -0.37 / -0.38 | both halves | 8e-05 |  |
| [[SCAMP3]] | -0.40 | -0.49 / -0.30 | both halves | 2e-04 |  |
| [[CELF6]] | -0.40 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[STX4]] | -0.40 | -0.37 / -0.38 | both halves | 8e-05 |  |
| [[PPP1R3E]] | -0.40 | -0.33 / -0.42 | both halves | 1e-04 |  |
| [[ATM]] | -0.39 | -0.42 / -0.37 | both halves | 8e-05 | STRING 444 |
| [[CPVL]] | -0.39 | -0.25 / -0.46 | both halves | 4e-04 |  |
| [[ODAD4]] | -0.39 | -0.40 / -0.38 | both halves | 7e-05 |  |
| [[CNOT2]] | -0.39 | -0.19 / -0.39 | ⚠ not reproduced | 9e-04 |  |
| [[IQUB]] | -0.39 | -0.41 / -0.32 | both halves | 2e-04 |  |
| [[ALDH2]] | -0.39 | -0.29 / -0.45 | both halves | 2e-04 |  |
| [[TMEM132D]] | -0.38 | -0.42 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*30 arrows, 30 of them with an alert ⚠; grade A 0, B 30, C 0. Shown: the 12 strongest; 18 more arrows (18 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C1orf116]] | B | C1orf116 activity raises SNRK's level | lines that do not express C1orf116 (31) vs lines expressing it (19) | 1.72× lower at baseline in the lines without C1orf116 | 0.007 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[FAM83B]] | B | FAM83B activity raises SNRK's level | lines that do not express FAM83B (30) vs lines expressing it (20) | 1.74× lower at baseline in the lines without FAM83B | 0.007 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14 |
| [[CEACAM1]] | B | CEACAM1 activity raises SNRK's level | lines that do not express CEACAM1 (27) vs lines expressing it (23) | 1.54× lower at baseline in the lines without CEACAM1 | 0.009 | ⚠ within organs, on part of the lines; also absent: TOX3, FOXQ1, TRIM29 |
| [[INAVA]] | B | INAVA activity raises SNRK's level | lines that do not express INAVA (29) vs lines expressing it (21) | 1.60× lower at baseline in the lines without INAVA | 0.010 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[MYO5B]] | B | MYO5B activity raises SNRK's level | lines that do not express MYO5B (26) vs lines expressing it (24) | 1.58× lower at baseline in the lines without MYO5B | 0.012 | ⚠ within organs, on part of the lines; also absent: CRB3, KDF1, MARVELD3 |
| [[B3GNT3]] | B | B3GNT3 activity raises SNRK's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 1.76× lower at baseline in the lines without B3GNT3 | 0.012 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[SCEL]] | B | SCEL activity raises SNRK's level | lines that do not express SCEL (35) vs lines expressing it (15) | 1.76× lower at baseline in the lines without SCEL | 0.012 | ⚠ within organs, on part of the lines; also absent: FGFBP1, MUC4, DAPP1 |
| [[CRYBG2]] | B | CRYBG2 activity raises SNRK's level | lines that do not express CRYBG2 (23) vs lines expressing it (27) | 1.69× lower at baseline in the lines without CRYBG2 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SPINT1-AS1, SMPDL3B, LAD1 |
| [[HS3ST1]] | B | HS3ST1 activity raises SNRK's level | lines that do not express HS3ST1 (31) vs lines expressing it (19) | 1.68× lower at baseline in the lines without HS3ST1 | 0.022 | ⚠ within organs, on part of the lines; also absent: KLK10, ADGRF1, TMPRSS4 |
| [[KIAA0040]] | B | KIAA0040 activity raises SNRK's level | lines that do not express KIAA0040 (24) vs lines expressing it (26) | 1.50× lower at baseline in the lines without KIAA0040 | 0.022 | ⚠ within organs, on part of the lines; also absent: ENSG00000226281, CLDN3, ESRP1 |
| [[INPP5D]] | B | INPP5D activity raises SNRK's level | lines that do not express INPP5D (34) vs lines expressing it (16) | 1.67× lower at baseline in the lines without INPP5D | 0.027 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A, TP53; also absent: CLRN3, LINC02964, LGR5 |
| [[MST1R]] | B | MST1R activity raises SNRK's level | lines that do not express MST1R (24) vs lines expressing it (26) | 1.58× lower at baseline in the lines without MST1R | 0.035 | ⚠ within organs, on part of the lines; also absent: SLC52A3, SPINT1, MAP7 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Minodronic acid (drug)]] 0.5 µM | C | SNRK's natural level lowers the cells' numbers under Minodronic acid 0.5 µM (makes them more sensitive) | SNRK's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.68 | 0.285 over the table, 0.038 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.391). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.0, 53.2); signed map (1.6, 38.9). **Vector** length 91.0, 20.3% of its response variance represented; |z| ≥ 3 in 1,020 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +4.7 | +3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.5 | +2.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.5 | +2.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | +3.2 | +2.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.7 | +0.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.7 | +1.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.5 | +1.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.4 | +3.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.4 | -8.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.8 | -4.0 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -4.8 | -4.6 |
|  | [[Selinexor (drug)]] 0.05 µM |  | -4.5 | -3.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~95% of this change | -3.2 | -2.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.4 | -3.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.2 | -0.8 |
|  | [[Afatinib (drug)]] 5 µM |  | -1.9 | -0.9 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -1.9 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | SNF related kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p22.1 — chr3:43,286,512-43,424,764 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20224, HSNFRK, KIAA0096 |
| Gene groups (HGNC) | SNRK family kinases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRH2](https://www.uniprot.org/uniprotkb/Q9NRH2) (SNF-related serine/threonine-protein kinase):

> May play a role in hematopoietic cell proliferation or differentiation. Potential mediator of neuronal apoptosis.

**Summary**, from NCBI Gene [54861](https://www.ncbi.nlm.nih.gov/gene/54861):

> SNRK is a member of the sucrose nonfermenting (SNF)-related kinase family of serine/threonine kinases (Kertesz et al., 2002 [PubMed 12234663]).[supplied by OMIM, Apr 2009]

**Accessions** — [HGNC:30598](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30598) · Entrez [54861](https://www.ncbi.nlm.nih.gov/gene/54861) · UniProt [Q9NRH2](https://www.uniprot.org/uniprotkb/Q9NRH2) · Ensembl [ENSG00000163788](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163788)

## Data

Gene col 8777: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8777); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8777, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8777]; `tensor/DDL_lfc|DDL_z.npy` [8777]; `embed/gene_vectors.npy` [8777]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8777 or target_col == 8777). Every well: [[SNRK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNRK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
