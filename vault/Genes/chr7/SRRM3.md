---
symbol: "SRRM3"
type: "gene"
col: 10850
ensembl_id: "ENSG00000177679"
name: "serine/arginine repetitive matrix 3"
location: "7q11.23"
module: 191
arm: "+"
pooled_cpm: 10.21
n_lines_expressing: 33
n_dd_up: 25
n_dd_down: 0
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 8
direction_downstream: 17
tags: ["gene", "module/191"]
generated_by: "tahoemap"
---

# SRRM3

*serine/arginine repetitive matrix 3* — 7q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 9.07× (z +21.6, q 0e+00, up in 28 of 29 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Sunitinib (drug)]] 0.05 µM in 1 line (NCI-H460 0.0390×); [[Simotinib (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0724×); [[Decitabine (drug)]] 5 µM in 1 line (SK-MEL-2 0.0524×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC39]] (+0.61, fdr 1e-05), [[COL26A1]] (+0.59, fdr 7e-06), [[XKR7]] (+0.58, fdr 7e-05); moves opposite to [[PMS1]] (-0.53, fdr 1e-04), [[GSTCD]] (-0.51, fdr 2e-04), [[LIG3]] (-0.51, fdr 1e-04).
> It is in [[Module 191]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[SCG3]] → it (grade B ⚠); 17 go from it, the strongest it → [[MAPK8IP2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10850.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **9.07×** | +21.6 | 0e+00 | 28/29 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **7.97×** | +20.3 | 0e+00 | 28/29 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **4.16×** | +19.7 | 0e+00 | 18/23 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **4.68×** | +15.1 | 0e+00 | 25/29 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.35×** | +11.8 | 3e-30 | 20/29 (PANC-1, SK-MEL-2, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.22×** | +11.0 | 4e-26 | 16/22 (A549, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.13×** | +10.7 | 6e-25 | 3/6 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.67×** | +9.6 | 6e-20 | 11/16 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.87×** | +9.5 | 9e-20 | 5/9 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.13×** | +7.4 | 9e-12 | 13/29 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.13×** | +7.1 | 6e-11 | 5/17 (A498, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.04×** | +7.0 | 2e-10 | 14/28 (SK-MEL-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.84×** | +6.0 | 1e-07 | 9/29 (C32, SK-MEL-2, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.80×** | +5.5 | 1e-06 | 13/27 (LoVo, SW480, …) | top dose only | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.76×** | +5.5 | 1e-06 | 9/23 (NCI-H2030, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.43×** | +5.0 | 2e-05 | 8/29 (A498, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **2.50×** | +4.7 | 1e-04 | 10/27 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.93×** | +4.3 | 6e-04 | 2/21 (SW480, SW1417) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.66×** | +3.3 | 0.026 | 1/25 (A498) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10850.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Sunitinib (drug)]] 0.05 µM in 1 line (NCI-H460 0.0390×); [[Simotinib (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0724×); [[Decitabine (drug)]] 5 µM in 1 line (SK-MEL-2 0.0524×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.711× | -3.1 | 0.56 | 2/29 (SW 900, LoVo) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10850. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 2.98 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 18.9× (z +10.8) | [[Sunitinib (drug)]] 0.05 µM 0.0390× (z -12.0) |
| [[PANC-1 (line)]] | alt | 4.30 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 10.8× (z +11.7) | — |
| [[SW480 (line)]] | alt | 16.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.88× (z +12.9) | — |
| [[A549 (line)]] | wt | 3.67 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 19.8× (z +9.2) | — |
| [[LoVo (line)]] | wt | 6.60 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 8.58× (z +9.1) | — |
| [[NCI-H2030 (line)]] | alt | 3.92 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +12.9) | [[Simotinib (drug)]] 0.5 µM 0.0724× (z -9.8) |
| [[SW1417 (line)]] | alt | 222 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.538× (z -9.2) |
| [[A498 (line)]] | wt | 7.83 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 7.83× (z +10.1) | — |
| [[C32 (line)]] | wt | 5.58 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 18.3× (z +9.7) | — |
| [[SK-MEL-2 (line)]] | alt | 4.73 | 0 | 1 | — | [[Decitabine (drug)]] 5 µM 0.0524× (z -9.3) |
| [[A-172 (line)]] | wt | 5.77 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.21 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.37 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.22 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.96 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.52 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.65 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.99 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.48 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.85 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10850), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC39]] | +0.61 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[COL26A1]] | +0.59 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[XKR7]] | +0.58 | +0.59 / +0.37 | both halves | 7e-05 |  |
| [[SLC17A7]] | +0.58 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[SMPD3]] | +0.57 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[SYP]] | +0.57 | +0.34 / +0.65 | both halves | 1e-04 |  |
| [[DNAH3]] | +0.57 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[TMEM266]] | +0.57 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[MAL2-AS1]] | +0.57 | +0.34 / +0.62 | both halves | 1e-04 |  |
| [[RUNDC3B]] | +0.57 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[ETFBKMT]] | +0.57 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[CYP2U1-AS1]] | +0.56 | +0.46 / +0.55 | both halves | 3e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PMS1]] | -0.53 | -0.47 / -0.35 | both halves | 1e-04 |  |
| [[GSTCD]] | -0.51 | -0.29 / -0.44 | both halves | 2e-04 |  |
| [[LIG3]] | -0.51 | -0.58 / -0.35 | both halves | 1e-04 |  |
| [[DPAGT1]] | -0.50 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[DPY19L1P1]] | -0.50 | -0.41 / -0.39 | both halves | 6e-05 |  |
| [[TAS2R30]] | -0.50 | -0.36 / -0.50 | both halves | 9e-05 |  |
| [[ANGEL2]] | -0.49 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[ATR]] | -0.49 | -0.28 / -0.42 | both halves | 3e-04 |  |
| [[MCM9]] | -0.48 | -0.46 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 6, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SCG3]] | B | SCG3 activity raises SRRM3's level | lines that do not express SCG3 (39) vs lines expressing it (11) | 3.33× lower at baseline in the lines without SCG3 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHL1, PCSK1, CALCA |
| [[NFASC]] | B | NFASC activity raises SRRM3's level | lines that do not express NFASC (27) vs lines expressing it (23) | 2.08× lower at baseline in the lines without NFASC | 0.003 | ⚠ within organs, on part of the lines; also absent: DPYSL5, JPH3, KIF1A |
| [[XKR7]] | B | XKR7 activity raises SRRM3's level | lines that do not express XKR7 (39) vs lines expressing it (11) | 3.32× lower at baseline in the lines without XKR7 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, LINC01205, BMP5 |
| [[MAPK8IP2]] | B | MAPK8IP2 activity raises SRRM3's level | lines that do not express MAPK8IP2 (18) vs lines expressing it (32) | 2.01× lower at baseline in the lines without MAPK8IP2 | 0.047 | ⚠ within organs, on part of the lines; also absent: AP3B2, FBXO27, LTB; maybe low, not absent |
| [[HS6ST3]] | B | HS6ST3 activity raises SRRM3's level | lines that do not express HS6ST3 (19) vs lines expressing it (31) | 1.79× lower at baseline in the lines without HS6ST3 | 0.096 | ⚠ within organs, on part of the lines; also absent: LHX2, CECR2, NPTX1; maybe low, not absent |
| [[ETNK2]] | B | ETNK2 activity raises SRRM3's level | lines that do not express ETNK2 (11) vs lines expressing it (39) | 1.88× lower at baseline in the lines without ETNK2 | 0.099 | ⚠ within organs, on part of the lines; also absent: DLK2, FBXL2, DUSP15; maybe low, not absent |
| [[CHGB]] | C | CHGB activity raises SRRM3's level | lines that do not express CHGB (33) vs lines expressing it (17) | 2.58× lower at baseline in the lines without CHGB | 0.006 | ⚠ within organs, on part of the lines; also absent: MAGEA4, SLC6A11, CTNNA2; co-absent with the target |
| [[RAB39A]] | C | RAB39A activity raises SRRM3's level | lines that do not express RAB39A (20) vs lines expressing it (30) | 1.99× lower at baseline in the lines without RAB39A | 0.009 | ⚠ within organs, on part of the lines; also absent: RBM20, NOVA2, SDK2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 16, C 1. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAPK8IP2]] | B | SRRM3 activity raises MAPK8IP2's level | lines that do not express SRRM3 (17) vs lines expressing it (33) | 2.03× lower at baseline in the lines without SRRM3 | 0.007 | ⚠ within organs, on part of the lines; also absent: B4GALNT4, KIF26A, SEPTIN3; maybe low, not absent |
| [[HTRA3]] | B | SRRM3 activity lowers HTRA3's level | lines that do not express SRRM3 (17) vs lines expressing it (33) | 1.88× higher at baseline in the lines without SRRM3 | 0.008 | ⚠ within organs, on part of the lines; also absent: B4GALNT4, KIF26A, SEPTIN3; maybe low, not absent |
| [[ATP1A3]] | B | SRRM3 activity raises ATP1A3's level | lines that do not express SRRM3 (17) vs lines expressing it (33) | 2.20× lower at baseline in the lines without SRRM3 | 0.013 | ⚠ within organs, on part of the lines; also absent: B4GALNT4, KIF26A, SEPTIN3; maybe low, not absent |
| [[MCM9]] | B | SRRM3 activity raises MCM9's level | lines that do not express SRRM3 (17) vs lines expressing it (33) | 1.36× lower at baseline in the lines without SRRM3 | 0.016 | ⚠ within organs, on part of the lines; also absent: B4GALNT4, KIF26A, SEPTIN3; maybe low, not absent |
| [[METRNL]] | B | SRRM3 activity lowers METRNL's level | lines that do not express SRRM3 (17) vs lines expressing it (33) | 2.33× higher at baseline in the lines without SRRM3 | 0.020 | ⚠ within organs, on part of the lines; also absent: B4GALNT4, KIF26A, SEPTIN3; maybe low, not absent |
| [[CELF5]] | B | SRRM3 activity raises CELF5's level | lines that do not express SRRM3 (17) vs lines expressing it (33) | 1.68× lower at baseline in the lines without SRRM3 | 0.031 | ⚠ within organs, on part of the lines; also absent: B4GALNT4, KIF26A, SEPTIN3; maybe low, not absent |
| [[SYP]] | B | SRRM3 activity raises SYP's level | lines that do not express SRRM3 (17) vs lines expressing it (33) | 1.97× lower at baseline in the lines without SRRM3 | 0.045 | ⚠ within organs, on part of the lines; also absent: B4GALNT4, KIF26A, SEPTIN3; maybe low, not absent |
| [[ATR]] | B | SRRM3 activity weakens ATR's drug response | lines that do not express SRRM3 (17) vs lines expressing it (33) | the lines without SRRM3 respond 1.62× as strongly (z diff -1.71); strongest at Epirubicin (hydrochloride) 5 µM: 2.14x vs 1.45x (z diff -2.6) | 0.046 | ⚠ within organs, on part of the lines; also absent: B4GALNT4, KIF26A, SEPTIN3; maybe low, not absent; artifact flags |
| [[ACHE]] | B | SRRM3 activity raises ACHE's level | lines that do not express SRRM3 (17) vs lines expressing it (33) | 1.88× lower at baseline in the lines without SRRM3 | 0.049 | ⚠ within organs, on part of the lines; also absent: B4GALNT4, KIF26A, SEPTIN3; maybe low, not absent |
| [[LIG3]] | B | SRRM3 activity raises LIG3's level | lines that do not express SRRM3 (17) vs lines expressing it (33) | 1.30× lower at baseline in the lines without SRRM3 | 0.054 | ⚠ within organs, on part of the lines; also absent: B4GALNT4, KIF26A, SEPTIN3; maybe low, not absent |
| [[TCN2]] | B | SRRM3 activity lowers TCN2's level | lines that do not express SRRM3 (17) vs lines expressing it (33) | 1.51× higher at baseline in the lines without SRRM3 | 0.060 | ⚠ within organs, on part of the lines; also absent: B4GALNT4, KIF26A, SEPTIN3; maybe low, not absent |
| [[EFHD1]] | B | SRRM3 activity raises EFHD1's level | lines that do not express SRRM3 (17) vs lines expressing it (33) | 2.03× lower at baseline in the lines without SRRM3 | 0.069 | ⚠ within organs, on part of the lines; also absent: B4GALNT4, KIF26A, SEPTIN3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 191]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.639). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (20.7, 34.7); signed map (27.5, 17.9). **Vector** length 48.5, 8.90% of its response variance represented; |z| ≥ 3 in 588 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +10.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.7 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +9.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +11.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.1 | +19.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +6.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +4.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.7 | +3.2 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +1.5 | +2.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.0 | -1.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.9 | -2.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -2.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -2.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.4 | +1.0 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.3 | -3.1 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.2 | -1.9 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.2 | -2.5 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | -1.2 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | serine/arginine repetitive matrix 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.23 — chr7:76,201,896-76,287,288 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ37078 |
| Matched by | ensembl_id |

**Function**, from UniProt [A6NNA2](https://www.uniprot.org/uniprotkb/A6NNA2) (Serine/arginine repetitive matrix protein 3):

> RNA splicing factor that regulates inclusion of microexons in mRNA transcripts. Required for motor coordination. In cortical neurons, acts redundantly with SRRM4 and regulates many alternative splicing events, including inclusion of exon 4 into the transcriptional repressor REST transcript, leading to REST inactivation. REST inactivation de-represses potassium-chloride cotransporter 2/SLC12A5 expression, resulting in the switch in GABAergic neurotransmission from immature excitatory to …

**Summary**, from NCBI Gene [222183](https://www.ncbi.nlm.nih.gov/gene/222183):

> Predicted to enable mRNA binding activity. Involved in RNA splicing and negative regulation of insulin secretion. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26729](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26729) · Entrez [222183](https://www.ncbi.nlm.nih.gov/gene/222183) · UniProt [A6NNA2](https://www.uniprot.org/uniprotkb/A6NNA2) · Ensembl [ENSG00000177679](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177679)

## Data

Gene col 10850: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10850); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10850, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10850]; `tensor/DDL_lfc|DDL_z.npy` [10850]; `embed/gene_vectors.npy` [10850]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10850 or target_col == 10850). Every well: [[SRRM3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SRRM3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
