---
symbol: "SPTSSB"
type: "gene"
col: 12232
ensembl_id: "ENSG00000196542"
name: "serine palmitoyltransferase small subunit B"
location: "3q26.1"
module: 155
arm: "+"
pooled_cpm: 2.48
n_lines_expressing: 13
n_dd_up: 27
n_dd_down: 1
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 20
tags: ["gene", "module/155"]
generated_by: "tahoemap"
---

# SPTSSB

*serine palmitoyltransferase small subunit B* — 3q26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (13 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 4.22× (z +12.6, q 2e-33, up in 9 of 10 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Fenofibrate (drug)]] 0.05 µM: 0.493× (z -4.0, q 0.031, down in 0 of 11 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 5 µM in 2 lines (BT-474 0.114×, SW480 0.0819×; ⚠ cell-cycle shift, explains ~13% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (SW480 0.0543×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (SW480 0.0331×; ⚠ cell-cycle shift, explains ~52% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (BT-474 0.0906×); [[Auranofin (drug)]] 5 µM in 1 line (BT-474 0.0969×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01440]] (+0.70, fdr 7e-06), [[S100A8]] (+0.64, fdr 7e-06), [[S100A9]] (+0.62, fdr 1e-05); moves opposite to [[PGR]] (-0.47, fdr 3e-05), [[LMO3]] (-0.46, fdr 1e-04).
> It is in [[Module 155]], a single-armed module (MyD88 deficiency (TLR2/4)).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PROX1-AS1]] → it (grade C ⚠); 20 go from it, the strongest it → cells under [[Afatinib (drug)]] 0.05 µM (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12232.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **4.22×** | +12.6 | 2e-33 | 9/10 (KATO III, SW1417, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.11×** | +11.6 | 7e-29 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.60×** | +10.6 | 4e-24 | 3/6 (KATO III, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.60×** | +9.7 | 5e-20 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **4.12×** | +8.7 | 3e-16 | 8/9 (HT-29, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.23×** | +7.0 | 3e-10 | 0/9 | rises with dose | cell-cycle shift (explains ~6% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.86×** | +5.9 | 2e-07 | 1/4 (SW48) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.88×** | +5.5 | 3e-06 | 3/11 (BT-474, KATO III, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.32×** | +5.2 | 1e-05 | 5/10 (KATO III, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.37×** | +5.1 | 2e-05 | 0/7 | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.26×** | +5.0 | 3e-05 | 1/6 (NCI-H1573) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.20×** | +4.8 | 6e-05 | 0/7 | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.10×** | +4.5 | 2e-04 | 0/6 | top dose only | cell-cycle shift (explains ~18% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.02×** | +4.2 | 0.001 | 2/9 (KATO III, NCI-H1573) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.01×** | +4.1 | 0.001 | 1/8 (Hs 766T) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.95×** | +4.1 | 0.002 | 3/10 (KATO III, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.54×** | +3.7 | 0.007 | 1/9 (HT-29) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.81×** | +3.6 | 0.009 | 2/10 (KATO III, SW1417) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Bendamustine (drug)]] 5 µM |  | **1.83×** | +3.6 | 0.011 | 0/9 | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.21×** | +3.5 | 0.015 | 0/6 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.75×** | +3.4 | 0.016 | 5/11 (KATO III, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.68×** | +3.2 | 0.034 | 0/8 | inconsistent across doses | low cells (technical?) |
| [[Pimozide (drug)]] 0.05 µM |  | **1.61×** | +2.9 | 0.074 | 0/8 | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12232.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 5 µM in 2 lines (BT-474 0.114×, SW480 0.0819×; ⚠ cell-cycle shift, explains ~13% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (SW480 0.0543×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (SW480 0.0331×; ⚠ cell-cycle shift, explains ~52% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (BT-474 0.0906×); [[Auranofin (drug)]] 5 µM in 1 line (BT-474 0.0969×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.493×** | -4.0 | 0.031 | 0/11 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12232. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 87.5 | 0 | 7 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0906× (z -12.0) |
| [[SW480 (line)]] | alt | 5.09 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0543× (z -16.3) |
| [[KATO III (line)]] | alt | 5.29 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 10.2× (z +9.8) | — |
| [[A-172 (line)]] | wt | 0.261 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.210 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.246 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.209 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.379 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.285 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.330 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.249 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.528 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.409 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.910 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.248 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.527 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.435 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.272 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.228 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.320 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.237 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.349 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.309 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.291 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.195 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.243 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.283 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 0.835 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.270 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.290 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.244 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.279 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.473 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.351 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.243 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.216 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.534 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.224 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.276 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.300 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.523 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.288 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12232), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01440]] | +0.70 | +0.68 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[S100A8]] | +0.64 | +0.63 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[S100A9]] | +0.62 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[MUC5AC]] | +0.61 | +0.61 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[C2CD4A]] | +0.60 | +0.52 / +0.50 | both halves | 1e-05 | **novel candidate** |
| [[FGD5]] | +0.59 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[TMEM163]] | +0.57 | +0.58 / +0.52 | both halves | 1e-05 | **novel candidate** |
| [[KRT23]] | +0.57 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[CES1]] | +0.57 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[VSIG1]] | +0.56 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[SERPINB4]] | +0.54 | +0.57 / +0.43 | both halves | 3e-05 |  |
| [[FLRT3]] | +0.53 | +0.48 / +0.49 | both halves | 2e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PGR]] | -0.47 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[LMO3]] | -0.46 | -0.48 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PROX1-AS1]] | C | PROX1-AS1 activity raises SPTSSB's level | lines that do not express PROX1-AS1 (29) vs lines expressing it (21) | 1.44× lower at baseline in the lines without PROX1-AS1 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST18, AXIN2, PROX1; co-absent with the target |
| [[ZBTB7C]] | C | ZBTB7C activity raises SPTSSB's level | lines that do not express ZBTB7C (25) vs lines expressing it (25) | 1.72× lower at baseline in the lines without ZBTB7C | 0.093 | ⚠ within organs, on part of the lines; also absent: ENSG00000290808, FSTL4, PPARGC1A; co-absent with the target |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 2, C 18. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Afatinib (drug)]] 0.05 µM | B | SPTSSB activity lowers the cells' numbers under Afatinib 0.05 µM (makes them more sensitive) | lines that do not express SPTSSB (37) vs lines expressing it (11) | the lines without SPTSSB: 1.14× the cells of the other lines | 0.088 | ⚠ within organs, on part of the lines; also absent: PRR15L, HEPHL1, TACSTD2 |
| [[LINC01503]] | B | SPTSSB activity raises LINC01503's level | lines that do not express SPTSSB (37) vs lines expressing it (13) | 2.07× lower at baseline in the lines without SPTSSB | 0.096 | ⚠ within organs, on part of the lines; also absent: PRR15L, HEPHL1, TACSTD2 |
| [[PPL]] | C | SPTSSB activity raises PPL's level | lines that do not express SPTSSB (37) vs lines expressing it (13) | 5.03× lower at baseline in the lines without SPTSSB | 0.005 | ⚠ within organs, on part of the lines; also absent: PRR15L, HEPHL1, TACSTD2; co-absent with the target |
| [[MPZL2]] | C | SPTSSB activity raises MPZL2's level | lines that do not express SPTSSB (37) vs lines expressing it (13) | 6.04× lower at baseline in the lines without SPTSSB | 0.009 | ⚠ within organs, on part of the lines; also absent: PRR15L, HEPHL1, TACSTD2; co-absent with the target |
| [[IGFL4]] | C | SPTSSB activity raises IGFL4's level | lines that do not express SPTSSB (37) vs lines expressing it (13) | 3.77× lower at baseline in the lines without SPTSSB | 0.010 | ⚠ within organs, on part of the lines; also absent: PRR15L, HEPHL1, TACSTD2; co-absent with the target |
| [[TNNT2]] | C | SPTSSB activity raises TNNT2's level | lines that do not express SPTSSB (37) vs lines expressing it (13) | 3.07× lower at baseline in the lines without SPTSSB | 0.013 | ⚠ within organs, on part of the lines; also absent: PRR15L, HEPHL1, TACSTD2; co-absent with the target |
| [[PROX1]] | C | SPTSSB activity raises PROX1's level | lines that do not express SPTSSB (37) vs lines expressing it (13) | 4.04× lower at baseline in the lines without SPTSSB | 0.020 | ⚠ within organs, on part of the lines; also absent: PRR15L, HEPHL1, TACSTD2; co-absent with the target |
| [[GSDMC]] | C | SPTSSB activity raises GSDMC's level | lines that do not express SPTSSB (37) vs lines expressing it (13) | 2.15× lower at baseline in the lines without SPTSSB | 0.022 | ⚠ within organs, on part of the lines; also absent: PRR15L, HEPHL1, TACSTD2; co-absent with the target |
| [[PROX1-AS1]] | C | SPTSSB activity raises PROX1-AS1's level | lines that do not express SPTSSB (37) vs lines expressing it (13) | 3.38× lower at baseline in the lines without SPTSSB | 0.023 | ⚠ within organs, on part of the lines; also absent: PRR15L, HEPHL1, TACSTD2; co-absent with the target |
| [[CES1]] | C | SPTSSB activity raises CES1's level | lines that do not express SPTSSB (37) vs lines expressing it (13) | 2.19× lower at baseline in the lines without SPTSSB | 0.025 | ⚠ within organs, on part of the lines; also absent: PRR15L, HEPHL1, TACSTD2; co-absent with the target |
| [[LINC02964]] | C | SPTSSB activity raises LINC02964's level | lines that do not express SPTSSB (37) vs lines expressing it (13) | 3.20× lower at baseline in the lines without SPTSSB | 0.029 | ⚠ within organs, on part of the lines; also absent: PRR15L, HEPHL1, TACSTD2; co-absent with the target |
| [[SDR16C5]] | C | SPTSSB activity raises SDR16C5's level | lines that do not express SPTSSB (37) vs lines expressing it (13) | 3.86× lower at baseline in the lines without SPTSSB | 0.036 | ⚠ within organs, on part of the lines; also absent: PRR15L, HEPHL1, TACSTD2; co-absent with the target |

## Where it sits

- **Module**: [[Module 155]] — MyD88 deficiency (TLR2/4); 29 genes; every member is in the + arm (projection on the module's main direction 0.688). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.7, 48.6); signed map (55.3, 23.2). **Vector** length 40.3, 13.3% of its response variance represented; |z| ≥ 3 in 347 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Antimicrobial peptides* (reactome, mean cos +0.53 to 3).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +12.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +10.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.9 | +8.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.6 | +9.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +2.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.8 | +3.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +0.7 | +2.5 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +0.7 | +2.3 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -2.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -2.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | -0.9 | +0.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -0.8 | -0.4 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.8 | -2.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.8 | -1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.7 | -2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.7 | -0.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.6 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | serine palmitoyltransferase small subunit B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q26.1 — chr3:161,344,798-161,372,880 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ADMP, ssSPTb; previously C3orf57 |
| Gene groups (HGNC) | Serine palmitoyltransferase small subunits |
| Reactome | 3 pathways, smallest: Sphingolipid de novo biosynthesis; Sphingolipid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NFR3](https://www.uniprot.org/uniprotkb/Q8NFR3) (Serine palmitoyltransferase small subunit B):

> Component of the serine palmitoyltransferase multisubunit enzyme (SPT) that catalyzes the initial and rate-limiting step in sphingolipid biosynthesis by condensing L-serine and activated acyl-CoA (most commonly palmitoyl-CoA) to form long-chain bases. The SPT complex is composed of SPTLC1, SPTLC2 or SPTLC3 and SPTSSA or SPTSSB. Within this complex, the heterodimer consisting of SPTLC1 and SPTLC2/SPTLC3 forms the catalytic core. Within the SPT complex, SPTSSB stimulates the catalytic activity …

**Summary**, from NCBI Gene [165679](https://www.ncbi.nlm.nih.gov/gene/165679):

> Serine palmitoyltransferase (SPT; EC 2.3.1.50) catalyzes the first committed and rate-limiting step in sphingolipid biosynthesis. SSSPTB is a small SPT subunit that stimulates SPT activity and confers acyl-CoA preference to the SPT catalytic heterodimer of SPTLC1 (MIM 605712) and either SPTLC2 (MIM 605713) or SPTLC3 (MIM 611120) (Han et al., 2009 [PubMed 19416851]).[supplied by OMIM, Nov 2010]

**Accessions** — [HGNC:24045](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24045) · Entrez [165679](https://www.ncbi.nlm.nih.gov/gene/165679) · UniProt [Q8NFR3](https://www.uniprot.org/uniprotkb/Q8NFR3) · Ensembl [ENSG00000196542](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196542)

## Data

Gene col 12232: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12232); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12232, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12232]; `tensor/DDL_lfc|DDL_z.npy` [12232]; `embed/gene_vectors.npy` [12232]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12232 or target_col == 12232). Every well: [[SPTSSB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPTSSB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
