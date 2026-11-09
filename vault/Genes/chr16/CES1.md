---
symbol: "CES1"
type: "gene"
col: 12707
ensembl_id: "ENSG00000198848"
name: "carboxylesterase 1"
location: "16q12.2"
module: 155
arm: "+"
pooled_cpm: 19.27
n_lines_expressing: 8
n_dd_up: 8
n_dd_down: 6
n_dd_up_clean: 3
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 16
direction_downstream: 8
tags: ["gene", "module/155"]
generated_by: "tahoemap"
---

# CES1

*carboxylesterase 1* — 16q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.87× (z +9.1, q 8e-17, up in 3 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 2.10× (z +3.5, q 0.032, up in 0 of 4 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.591× (z -5.0, q 3e-04, down in 4 of 4 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[S100A8]] (+0.85, fdr 7e-06), [[S100A9]] (+0.85, fdr 7e-06), [[GSDMC]] (+0.79, fdr 7e-06); moves opposite to [[PRLR]] (-0.51, fdr 4e-05), [[ANKRD30A]] (-0.51, fdr 3e-05), [[PGR]] (-0.50, fdr 4e-05).
> It is in [[Module 155]], a single-armed module (MyD88 deficiency (TLR2/4)).
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[CEACAM5]] → it (grade C ⚠); 8 go from it, the strongest it → [[CEACAM5]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12707.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.87×** | +9.1 | 8e-17 | 3/4 (AsPC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.47×** | +8.0 | 3e-13 | 2/2 (NCI-H1573, PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.87×** | +6.5 | 1e-08 | 1/4 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.14×** | +5.1 | 5e-05 | 0/4 | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.98×** | +4.6 | 5e-04 | 0/4 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.10×** | +3.5 | 0.032 | 0/4 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.46×** | +3.5 | 0.032 | 0/6 | rises with dose |  |
| [[Mifepristone (drug)]] 0.05 µM |  | **1.77×** | +3.5 | 0.032 | 0/4 | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12707.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.591×** | -5.0 | 3e-04 | 4/4 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.595×** | -3.5 | 0.080 | 3/4 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pimozide (drug)]] 5 µM |  | **0.601×** | -3.5 | 0.080 | 1/5 (AN3 CA) | inconsistent across doses | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.582×** | -3.4 | 0.080 | 2/5 (BT-474, PANC-1) | inconsistent across doses |  |
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | **0.589×** | -3.4 | 0.080 | 0/4 | inconsistent across doses | position effect removed |
| [[Folic acid (drug)]] 5 µM |  | **0.711×** | -3.3 | 0.095 | 3/6 (AsPC-1, AN3 CA, …) | top dose only |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.727× | -3.1 | 0.16 | 1/6 (AN3 CA) | rises with dose | position effect removed |
| [[Ivabradine (hydrochloride) (drug)]] 0.5 µM | ⚠ transcription drop; unreliable plate only | 0.639× | -3.0 | 0.16 | 0/4 | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12707. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 8.43 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0196× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 644 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0846× (z -15.1) |
| [[A-172 (line)]] | wt | 1.88 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.51 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.09 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.11 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.93 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.72 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.06 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.01 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.95 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.05 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.08 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.20 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.91 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.73 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.38 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.12 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.86 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 9.24 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.00 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.23 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.81 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.50 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.65 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.21 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.76 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12707), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[S100A8]] | +0.85 | +0.75 / +0.85 | both halves | 7e-06 | **novel candidate** |
| [[S100A9]] | +0.85 | +0.74 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[GSDMC]] | +0.79 | +0.75 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[LINC01440]] | +0.71 | +0.68 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[SERPINB4]] | +0.67 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[SERPINB3]] | +0.66 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[MUC5AC]] | +0.64 | +0.61 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[PI3]] | +0.64 | +0.62 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[C2CD4A]] | +0.61 | +0.54 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[SERPINA1]] | +0.60 | +0.48 / +0.57 | both halves | 2e-05 | **novel candidate** |
| [[UBE2QL1]] | +0.60 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[SPTSSB]] | +0.57 | +0.57 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRLR]] | -0.51 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[ANKRD30A]] | -0.51 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[PGR]] | -0.50 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[TENM2]] | -0.42 | -0.47 / -0.39 | both halves | 5e-05 |  |
| [[LMO3]] | -0.39 | -0.38 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 0, C 16. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CEACAM5]] | C | CEACAM5 activity raises CES1's level | lines that do not express CEACAM5 (39) vs lines expressing it (11) | 2.92× lower at baseline in the lines without CEACAM5 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, ENSG00000267881; co-absent with the target |
| [[C2CD4A]] | C | C2CD4A activity raises CES1's level | lines that do not express C2CD4A (38) vs lines expressing it (12) | 2.69× lower at baseline in the lines without C2CD4A | 0.022 | ⚠ within organs, on part of the lines; also absent: CEACAM5, AGR3, PRR15L; co-absent with the target |
| [[SPTSSB]] | C | SPTSSB activity raises CES1's level | lines that do not express SPTSSB (37) vs lines expressing it (13) | 2.19× lower at baseline in the lines without SPTSSB | 0.025 | ⚠ within organs, on part of the lines; also absent: PRR15L, HEPHL1, TACSTD2; co-absent with the target |
| [[S100A14]] | C | S100A14 activity raises CES1's level | lines that do not express S100A14 (33) vs lines expressing it (17) | 1.91× lower at baseline in the lines without S100A14 | 0.033 | ⚠ within organs, on part of the lines; also absent: PRSS8, RAB25, TMPRSS4; co-absent with the target |
| [[S100A9]] | C | S100A9 activity raises CES1's level | lines that do not express S100A9 (42) vs lines expressing it (8) | 3.86× lower at baseline in the lines without S100A9 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, GSDMC, KRT20; co-absent with the target |
| [[TNNT2]] | C | TNNT2 activity raises CES1's level | lines that do not express TNNT2 (29) vs lines expressing it (21) | 1.84× lower at baseline in the lines without TNNT2 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ATP2C2, ST14; co-absent with the target |
| [[CEACAM6]] | C | CEACAM6 activity raises CES1's level | lines that do not express CEACAM6 (37) vs lines expressing it (13) | 2.40× lower at baseline in the lines without CEACAM6 | 0.040 | ⚠ within organs, on part of the lines; also absent: DAPP1, TMPRSS2, CDH17; co-absent with the target |
| [[S100P]] | C | S100P activity raises CES1's level | lines that do not express S100P (34) vs lines expressing it (16) | 2.03× lower at baseline in the lines without S100P | 0.054 | ⚠ within organs, on part of the lines; also absent: POF1B, ENSG00000287426, CEACAM6; co-absent with the target |
| [[TMEM45B]] | C | TMEM45B activity raises CES1's level | lines that do not express TMEM45B (32) vs lines expressing it (18) | 1.82× lower at baseline in the lines without TMEM45B | 0.057 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TRIM15, CDH1, ENSG00000267881; co-absent with the target |
| [[S100A8]] | C | S100A8 activity raises CES1's level | lines that do not express S100A8 (46) vs lines expressing it (4) | 16.53× lower at baseline in the lines without S100A8 | 0.060 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, BMP10, TBXT; co-absent with the target; its own permutation p |
| [[FAM83A]] | C | FAM83A activity raises CES1's level | lines that do not express FAM83A (37) vs lines expressing it (13) | 2.34× lower at baseline in the lines without FAM83A | 0.065 | ⚠ within organs, on part of the lines; also absent: GSDMC, DAPP1, S100A9; co-absent with the target |
| [[MPZL2]] | C | MPZL2 activity raises CES1's level | lines that do not express MPZL2 (29) vs lines expressing it (21) | 1.67× lower at baseline in the lines without MPZL2 | 0.072 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, IRF6, ST14; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 0, C 8.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CEACAM5]] | C | CES1 activity raises CEACAM5's level | lines that do not express CES1 (42) vs lines expressing it (8) | 4.34× lower at baseline in the lines without CES1 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, CGA, SLC15A5; co-absent with the target |
| [[CEACAM6]] | C | CES1 activity raises CEACAM6's level | lines that do not express CES1 (42) vs lines expressing it (8) | 6.18× lower at baseline in the lines without CES1 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, CGA, SLC15A5; co-absent with the target |
| [[S100A9]] | C | CES1 activity raises S100A9's level | lines that do not express CES1 (42) vs lines expressing it (8) | 6.21× lower at baseline in the lines without CES1 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, CGA, SLC15A5; co-absent with the target |
| [[S100P]] | C | CES1 activity raises S100P's level | lines that do not express CES1 (42) vs lines expressing it (8) | 3.36× lower at baseline in the lines without CES1 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, CGA, SLC15A5; co-absent with the target |
| [[TMEM45B]] | C | CES1 activity raises TMEM45B's level | lines that do not express CES1 (42) vs lines expressing it (8) | 3.23× lower at baseline in the lines without CES1 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, CGA, SLC15A5; co-absent with the target |
| [[S100A8]] | C | CES1 activity raises S100A8's level | lines that do not express CES1 (42) vs lines expressing it (8) | 3.79× lower at baseline in the lines without CES1 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, CGA, SLC15A5; co-absent with the target |
| [[CAPN8]] | C | CES1 activity raises CAPN8's level | lines that do not express CES1 (42) vs lines expressing it (8) | 2.18× lower at baseline in the lines without CES1 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, CGA, SLC15A5; co-absent with the target |
| [[MUC2]] | C | CES1 activity raises MUC2's level | lines that do not express CES1 (42) vs lines expressing it (8) | 1.41× lower at baseline in the lines without CES1 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, CGA, SLC15A5; co-absent with the target |

## Where it sits

- **Module**: [[Module 155]] — MyD88 deficiency (TLR2/4); 29 genes; every member is in the + arm (projection on the module's main direction 0.817). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.2, 48.5); signed map (55.0, 23.7). **Vector** length 26.1, 13.9% of its response variance represented; |z| ≥ 3 in 101 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MyD88 deficiency (TLR2/4)* (reactome, mean cos +0.66 to 4); *IRAK4 deficiency (TLR2/4)* (reactome, mean cos +0.66 to 4); *Regulation of TLR by endogenous ligand* (reactome, mean cos +0.66 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.0 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.7 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.7 | +9.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.2 | +2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.1 | +3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.8 | -0.3 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +0.5 | +2.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +0.4 | +1.6 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +0.4 | +1.1 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -0.6 | -1.8 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -0.5 | -2.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -0.5 | +0.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.5 | -3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -0.5 | -0.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.4 | -2.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -0.4 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | carboxylesterase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q12.2 — chr16:55,802,851-55,833,337 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HMSE, CES2, HMSE1, SES1, CEH, CES1A1, CES1A2 |
| Gene groups (HGNC) | Carboxylesterases |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Reactome | 9 pathways, smallest: Metabolism of Angiotensinogen to Angiotensins; Physiological factors; Aspirin ADME |
| Matched by | ensembl_id |

**Function**, from UniProt [P23141](https://www.uniprot.org/uniprotkb/P23141) (Liver carboxylesterase 1):

> Involved in the detoxification of xenobiotics and in the activation of ester and amide prodrugs. Hydrolyzes aromatic and aliphatic esters, but has no catalytic activity toward amides or a fatty acyl-CoA ester. Hydrolyzes the methyl ester group of cocaine to form benzoylecgonine. Catalyzes the transesterification of cocaine to form cocaethylene. Displays fatty acid ethyl ester synthase activity, catalyzing the ethyl esterification of oleic acid to ethyloleate. Converts monoacylglycerides to free …

**Summary**, from NCBI Gene [1066](https://www.ncbi.nlm.nih.gov/gene/1066):

> This gene encodes a member of the carboxylesterase large family. The family members are responsible for the hydrolysis or transesterification of various xenobiotics, such as cocaine and heroin, and endogenous substrates with ester, thioester, or amide bonds. They may participate in fatty acyl and cholesterol ester metabolism, and may play a role in the blood-brain barrier system. This enzyme is the major liver enzyme and functions in liver drug clearance. Mutations of this gene cause …

**Accessions** — [HGNC:1863](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1863) · Entrez [1066](https://www.ncbi.nlm.nih.gov/gene/1066) · UniProt [P23141](https://www.uniprot.org/uniprotkb/P23141) · Ensembl [ENSG00000198848](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198848)

## Data

Gene col 12707: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12707); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12707, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12707]; `tensor/DDL_lfc|DDL_z.npy` [12707]; `embed/gene_vectors.npy` [12707]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12707 or target_col == 12707). Every well: [[CES1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CES1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
