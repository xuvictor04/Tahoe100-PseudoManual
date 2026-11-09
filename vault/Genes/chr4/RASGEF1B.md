---
symbol: "RASGEF1B"
type: "gene"
col: 6210
ensembl_id: "ENSG00000138670"
name: "RasGEF domain family member 1B"
location: "4q21.21"
module: 8
arm: "+"
pooled_cpm: 8.99
n_lines_expressing: 40
n_dd_up: 37
n_dd_down: 0
n_dd_up_clean: 28
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 28
direction_downstream: 27
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# RASGEF1B

*RasGEF domain family member 1B* — 4q21.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.23× (z +24.1, q 0e+00, up in 27 of 29 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H2347 0.144×, KATO III 0.200×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H2347 0.158×, COLO 205 0.0806×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2347 0.146×; ⚠ toxic; transcription drop); [[Harringtonine (drug)]] 0.5 µM in 1 line (COLO 205 0.145×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCIN]] (+0.71, fdr 7e-06), [[SELENOP]] (+0.64, fdr 7e-06), [[KLF4]] (+0.58, fdr 1e-05); moves opposite to [[FBXW2]] (-0.53, fdr 3e-05), [[EEFSEC]] (-0.47, fdr 1e-04), [[FAM86DP-1]] (-0.47, fdr 6e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 28 arrows point to it, the strongest [[STEAP4]] → it (grade B ⚠); 27 go from it, the strongest it → [[MYLIP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 9 with an alert ⚠; shown: the 15 strongest. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6210.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.23×** | +24.1 | 0e+00 | 27/29 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.55×** | +21.2 | 0e+00 | 26/30 (LoVo, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **3.48×** | +20.8 | 0e+00 | 34/36 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **3.37×** | +14.3 | 2e-44 | 34/36 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.33×** | +14.2 | 9e-44 | 29/35 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[TAK-901 (drug)]] 5 µM |  | **9.23×** | +13.7 | 8e-41 | 27/31 (LoVo, SW480, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.09×** | +13.3 | 1e-38 | 27/35 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.65×** | +11.5 | 9e-29 | 26/32 (C32, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.52×** | +10.9 | 6e-26 | 26/36 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[PH-797804 (drug)]] 5 µM |  | **4.65×** | +9.5 | 1e-19 | 19/28 (LoVo, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.27×** | +9.3 | 6e-19 | 19/26 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.25×** | +9.2 | 2e-18 | 19/30 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.12×** | +8.8 | 4e-17 | 25/34 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.17×** | +8.8 | 5e-17 | 20/32 (LoVo, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.99×** | +8.1 | 2e-14 | 20/29 (NCI-H2347, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6210.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H2347 0.144×, KATO III 0.200×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H2347 0.158×, COLO 205 0.0806×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2347 0.146×; ⚠ toxic; transcription drop); [[Harringtonine (drug)]] 0.5 µM in 1 line (COLO 205 0.145×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Abemaciclib (drug)]] 5 µM |  | 0.557× | -3.6 | 0.13 | 10/31 (SW1417, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.744× | -3.5 | 0.13 | 12/36 (KATO III, NCI-H2347, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6210. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 16.4 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.05× (z +12.1) | — |
| [[NCI-H2347 (line)]] | alt | 29.7 | 1 | 3 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.62× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.144× (z -12.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 2.34 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 24.5× (z +15.1) | — |
| [[A498 (line)]] | wt | 3.25 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.4× (z +13.0) | — |
| [[LS 180 (line)]] | wt | 19.3 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 5.53× (z +10.6) | — |
| [[SW480 (line)]] | alt | 8.27 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.50× (z +10.0) | — |
| [[COLO 205 (line)]] | alt | 81.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0806× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.145× (z -8.8) |
| [[HOP62 (line)]] | alt | 2.60 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.39× (z +9.5) | — |
| [[KATO III (line)]] | alt | 20.4 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.172× (z -10.5) ⚠ unreliable plate only |
| [[SW1417 (line)]] | alt | 21.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +9.4) | — |
| [[A549 (line)]] | wt | 2.53 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.3× (z +9.1) | — |
| [[BT-474 (line)]] | alt | 12.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.25× (z +11.2) | — |
| [[C32 (line)]] | wt | 4.93 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 15.7× (z +11.4) | — |
| [[CFPAC-1 (line)]] | alt | 6.55 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.77× (z +11.0) | — |
| [[HEC-1-A (line)]] | alt | 8.13 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.87× (z +10.6) | — |
| [[NCI-H1792 (line)]] | alt | 8.16 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.45× (z +9.1) | — |
| [[A-172 (line)]] | wt | 1.85 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.18 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.50 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.38 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.17 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.98 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.14 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.21 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.02 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.80 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6210), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCIN]] | +0.71 | +0.61 / +0.75 | both halves | 7e-06 |  |
| [[SELENOP]] | +0.64 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[KLF4]] | +0.58 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[BCL2L11]] | +0.58 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[MTUS1-DT]] | +0.57 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[YBX3]] | +0.56 | +0.55 / +0.46 | both halves | 2e-05 |  |
| [[ELF3]] | +0.56 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[FMO5]] | +0.55 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[PLCL1]] | +0.55 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[ATF3]] | +0.54 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[EFNA1]] | +0.54 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[LNX1]] | +0.54 | +0.57 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXW2]] | -0.53 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[EEFSEC]] | -0.47 | -0.35 / -0.35 | both halves | 1e-04 |  |
| [[FAM86DP-1]] | -0.47 | -0.40 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 28, C 0. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STEAP4]] | B | STEAP4 activity raises RASGEF1B's level | lines that do not express STEAP4 (38) vs lines expressing it (12) | 4.55× lower at baseline in the lines without STEAP4 | 2e-04 | ⚠ within organs, on part of the lines; also absent: ADGRF1, WFDC2, SLC5A1 |
| [[ELF3]] | B | ELF3 activity raises RASGEF1B's level | lines that do not express ELF3 (23) vs lines expressing it (27) | 3.02× lower at baseline in the lines without ELF3 | 3e-04 | ⚠ within organs, on part of the lines; also absent: RASSF6, GOLT1A, LAMA3 |
| [[MPZL3]] | B | MPZL3 activity raises RASGEF1B's level | lines that do not express MPZL3 (25) vs lines expressing it (25) | 2.81× lower at baseline in the lines without MPZL3 | 6e-04 | ⚠ within organs, on part of the lines; also absent: RNF39, MYO5B, CDH1 |
| [[LNX1]] | B | LNX1 activity raises RASGEF1B's level | lines that do not express LNX1 (20) vs lines expressing it (30) | 2.56× lower at baseline in the lines without LNX1 | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, EGF, KLF8 |
| [[MTUS1-DT]] | B | MTUS1-DT activity raises RASGEF1B's level | lines that do not express MTUS1-DT (17) vs lines expressing it (33) | 2.55× lower at baseline in the lines without MTUS1-DT | 0.003 | ⚠ within organs, on part of the lines; co-absent genes; also absent: MTUS1, ELF3-AS1, ELF3 |
| [[FGF9]] | B | FGF9 activity raises RASGEF1B's level | lines that do not express FGF9 (31) vs lines expressing it (19) | 2.93× lower at baseline in the lines without FGF9 | 0.005 | ⚠ within organs, on part of the lines; also absent: VWA2, LINC02253, PRR15L |
| [[FRMD4B]] | B | FRMD4B activity raises RASGEF1B's level | lines that do not express FRMD4B (20) vs lines expressing it (30) | 2.35× lower at baseline in the lines without FRMD4B | 0.006 | ⚠ within organs, on part of the lines; also absent: LINC01589, ENSG00000290729, FRK; maybe low, not absent |
| [[BCAS1]] | B | BCAS1 activity raises RASGEF1B's level | lines that do not express BCAS1 (32) vs lines expressing it (18) | 2.16× lower at baseline in the lines without BCAS1 | 0.006 | ⚠ within organs, on part of the lines; also absent: SLC6A14, AGR3, LYZ |
| [[ELF3-AS1]] | B | ELF3-AS1 activity raises RASGEF1B's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 2.39× lower at baseline in the lines without ELF3-AS1 | 0.017 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[SLC40A1]] | B | SLC40A1 activity raises RASGEF1B's level | lines that do not express SLC40A1 (28) vs lines expressing it (22) | 2.38× lower at baseline in the lines without SLC40A1 | 0.024 | ⚠ within organs, on part of the lines; also absent: RASSF6, WFDC2, TOX3 |
| [[PDZK1IP1]] | B | PDZK1IP1 activity raises RASGEF1B's level | lines that do not express PDZK1IP1 (32) vs lines expressing it (18) | 2.24× lower at baseline in the lines without PDZK1IP1 | 0.031 | ⚠ within organs, on part of the lines; also absent: MUC5B, UCA1, PRSS8 |
| [[EFNA1]] | B | EFNA1 activity raises RASGEF1B's level | lines that do not express EFNA1 (13) vs lines expressing it (37) | 2.10× lower at baseline in the lines without EFNA1 | 0.037 | ⚠ within organs, on part of the lines; also absent: ELF3-AS1, ANO9, GPRC5A; maybe low, not absent |

### Downstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 27, C 0. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYLIP]] | B | RASGEF1B activity raises MYLIP's level | lines that do not express RASGEF1B (10) vs lines expressing it (40) | 1.82× lower at baseline in the lines without RASGEF1B | 0.027 | ⚠ within organs, on part of the lines; also absent: FBXW10B; maybe low, not absent |
| [[ELF3-AS1]] | B | RASGEF1B activity raises ELF3-AS1's level | lines that do not express RASGEF1B (10) vs lines expressing it (40) | 2.20× lower at baseline in the lines without RASGEF1B | 0.037 | ⚠ within organs, on part of the lines; also absent: FBXW10B; maybe low, not absent |
| cells under [[Irinotecan (drug)]] 0.5 µM | B | RASGEF1B activity raises the cells' numbers under Irinotecan 0.5 µM (protects the cells) | lines that do not express RASGEF1B (10) vs lines expressing it (38) | the lines without RASGEF1B: 0.76× the cells of the other lines | 0.038 | ⚠ within organs, on part of the lines; also absent: FBXW10B; maybe low, not absent |
| [[MPZL3]] | B | RASGEF1B activity raises MPZL3's level | lines that do not express RASGEF1B (10) vs lines expressing it (40) | 3.39× lower at baseline in the lines without RASGEF1B | 0.039 | ⚠ within organs, on part of the lines; also absent: FBXW10B; maybe low, not absent |
| [[LNX1]] | B | RASGEF1B activity raises LNX1's level | lines that do not express RASGEF1B (10) vs lines expressing it (40) | 3.45× lower at baseline in the lines without RASGEF1B | 0.041 | ⚠ within organs, on part of the lines; also absent: FBXW10B; maybe low, not absent |
| [[ELF3]] | B | RASGEF1B activity raises ELF3's level | lines that do not express RASGEF1B (10) vs lines expressing it (40) | 3.55× lower at baseline in the lines without RASGEF1B | 0.045 | ⚠ within organs, on part of the lines; also absent: FBXW10B; maybe low, not absent |
| [[FMO5]] | B | RASGEF1B activity raises FMO5's level | lines that do not express RASGEF1B (10) vs lines expressing it (40) | 1.52× lower at baseline in the lines without RASGEF1B | 0.067 | ⚠ within organs, on part of the lines; also absent: FBXW10B; maybe low, not absent |
| [[FRMD4B]] | B | RASGEF1B activity raises FRMD4B's level | lines that do not express RASGEF1B (10) vs lines expressing it (40) | 2.47× lower at baseline in the lines without RASGEF1B | 0.067 | ⚠ within organs, on part of the lines; also absent: FBXW10B; maybe low, not absent |
| [[BCL2L15]] | B | RASGEF1B activity raises BCL2L15's level | lines that do not express RASGEF1B (10) vs lines expressing it (40) | 1.89× lower at baseline in the lines without RASGEF1B | 0.071 | ⚠ within organs, on part of the lines; also absent: FBXW10B; maybe low, not absent |
| cells under [[Aliskiren (drug)]] 0.5 µM | B | RASGEF1B activity raises the cells' numbers under Aliskiren 0.5 µM (protects the cells) | lines that do not express RASGEF1B (10) vs lines expressing it (38) | the lines without RASGEF1B: 0.75× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: FBXW10B; maybe low, not absent |
| cells under [[Lonafarnib (drug)]] 0.05 µM | B | RASGEF1B activity lowers the cells' numbers under Lonafarnib 0.05 µM (makes them more sensitive) | lines that do not express RASGEF1B (10) vs lines expressing it (38) | the lines without RASGEF1B: 1.32× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: FBXW10B; maybe low, not absent |
| cells under [[vincristine (drug)]] 0.05 µM | B | RASGEF1B activity raises the cells' numbers under vincristine 0.05 µM (protects the cells) | lines that do not express RASGEF1B (10) vs lines expressing it (38) | the lines without RASGEF1B: 0.82× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: FBXW10B; maybe low, not absent |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.450). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.7, 52.1); signed map (53.6, 1.2). **Vector** length 76.5, 16.2% of its response variance represented; |z| ≥ 3 in 1,068 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.7 | +20.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.4 | +11.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +24.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.7 | +5.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +7.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.2 | +9.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.1 | +4.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.0 | +4.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.9 | +4.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.2 | -3.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.2 | -2.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.0 | -2.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.0 | -3.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.7 | -2.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.7 | -1.5 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.6 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | RasGEF domain family member 1B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q21.21 — chr4:81,426,393-82,044,244 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GPIG4, FLJ31695 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q0VAM2](https://www.uniprot.org/uniprotkb/Q0VAM2) (Ras-GEF domain-containing family member 1B):

> Guanine nucleotide exchange factor (GEF) with specificity for RAP2A, it does not seem to activate other Ras family proteins (in vitro).

**Summary**, from NCBI Gene [153020](https://www.ncbi.nlm.nih.gov/gene/153020):

> Enables guanyl-nucleotide exchange factor activity. Predicted to be involved in Ras protein signal transduction. Predicted to be located in early endosome; late endosome; and midbody. Predicted to be active in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24881](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24881) · Entrez [153020](https://www.ncbi.nlm.nih.gov/gene/153020) · UniProt [Q0VAM2](https://www.uniprot.org/uniprotkb/Q0VAM2) · Ensembl [ENSG00000138670](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138670)

## Data

Gene col 6210: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6210); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6210, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6210]; `tensor/DDL_lfc|DDL_z.npy` [6210]; `embed/gene_vectors.npy` [6210]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6210 or target_col == 6210). Every well: [[RASGEF1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RASGEF1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
