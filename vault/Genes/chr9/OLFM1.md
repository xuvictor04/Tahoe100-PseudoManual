---
symbol: "OLFM1"
type: "gene"
col: 5082
ensembl_id: "ENSG00000130558"
name: "olfactomedin 1"
location: "9q34.3"
module: 61
arm: "+"
pooled_cpm: 5.92
n_lines_expressing: 23
n_dd_up: 19
n_dd_down: 8
n_dd_up_clean: 11
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 11
direction_downstream: 5
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# OLFM1

*olfactomedin 1* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.82× (z +11.8, q 3e-29, up in 3 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.24× (z +10.4, q 8e-23, up in 11 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.646× (z -4.0, q 0.022, down in 10 of 18 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.656× (z -3.9, q 0.022, down in 7 of 18 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[N4BP3]] (+0.62, fdr 1e-05), [[SNAP25]] (+0.57, fdr 2e-05), [[CA8]] (+0.57, fdr 3e-05); moves opposite to [[ZCCHC4]] (-0.48, fdr 1e-04), [[FAM185A]] (-0.47, fdr 2e-04), [[TDRD3]] (-0.46, fdr 1e-04).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[KLRC3]] → it (grade B ⚠); 5 go from it, the strongest it → [[UNC5A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5082.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.82×** | +11.8 | 3e-29 | 3/6 (NCI-H2030, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.24×** | +10.4 | 8e-23 | 11/19 (SW480, SW1417, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.68×** | +9.0 | 4e-17 | 6/13 (NCI-H2030, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.45×** | +8.2 | 4e-14 | 15/19 (HOP62, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.88×** | +8.1 | 4e-14 | 9/19 (SW1417, BT-474, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.17×** | +7.1 | 1e-10 | 13/21 (HOP62, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.08×** | +6.2 | 5e-08 | 3/8 (HOP62, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.85×** | +5.6 | 1e-06 | 11/21 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.82×** | +5.5 | 3e-06 | 7/18 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.81×** | +5.4 | 4e-06 | 7/18 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **1.74×** | +5.1 | 2e-05 | 7/15 (HOP62, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM |  | **1.70×** | +4.9 | 6e-05 | 10/20 (HOP62, CHP-212, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +4.0 | 0.003 | 4/16 (NCI-H2030, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +3.8 | 0.006 | 2/19 (A549, BT-474) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.79×** | +3.8 | 0.006 | 3/16 (SW480, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.70×** | +3.5 | 0.018 | 2/16 (NCI-H23, NCI-H460) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Vilanterol (drug)]] 0.5 µM |  | **1.42×** | +3.2 | 0.046 | 5/17 (H4, NCI-H2030, …) | two highest doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5082.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.646×** | -4.0 | 0.022 | 10/18 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.656×** | -3.9 | 0.022 | 7/18 (SW480, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.657×** | -3.9 | 0.022 | 10/21 (SHP-77, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.668×** | -3.7 | 0.030 | 4/19 (NCI-H2030, A-172, …) | top dose only |  |
| [[Pexidartinib (hydrochloride) (drug)]] 0.05 µM |  | **0.660×** | -3.5 | 0.036 | 3/18 (NCI-H23, C-33 A, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 5 µM |  | **0.674×** | -3.5 | 0.036 | 4/19 (C-33 A, NCI-H1573, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.663×** | -3.5 | 0.036 | 2/19 (SW480, SHP-77) | inconsistent across doses |  |
| [[Torkinib (drug)]] 0.05 µM |  | **0.670×** | -3.5 | 0.036 | 5/19 (A549, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5082. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW1417 (line)]] | alt | 7.94 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 0.05 µM 0.0572× (z -11.6) |
| [[SHP-77 (line)]] | alt | 22.4 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.123× (z -14.6) |
| [[SW480 (line)]] | alt | 13.4 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.126× (z -12.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.239× (z -8.8) |
| [[A-427 (line)]] | wt | 19.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -12.7) ⚠ cell-cycle shift, explains ~36% of this change |
| [[H4 (line)]] | wt | 14.3 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0438× (z -10.5) ⚠ cell-cycle shift, explains ~75% of this change |
| [[NCI-H460 (line)]] | wt | 23.4 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.77× (z +9.3) | — |
| [[A-172 (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.619 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 5.66 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.545 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.603 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.506 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.551 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.490 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.453 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.628 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.748 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.413 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.470 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.78 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.645 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.518 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.389 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.459 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.747 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.493 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.532 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.640 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.862 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.604 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.52 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.607 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5082), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[N4BP3]] | +0.62 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[SNAP25]] | +0.57 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[CA8]] | +0.57 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[SH3GL2]] | +0.56 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[MAN1C1]] | +0.56 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[SPTB]] | +0.56 | +0.61 / +0.38 | both halves | 6e-05 |  |
| [[NCAM1]] | +0.56 | +0.37 / +0.60 | both halves | 9e-05 |  |
| [[CHST8]] | +0.55 | +0.59 / +0.42 | both halves | 4e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE |
| [[KLRC2]] | +0.55 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[DUSP2]] | +0.54 | +0.44 / +0.44 | both halves | 3e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE |
| [[PCSK1]] | +0.54 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[NR4A1]] | +0.54 | +0.43 / +0.50 | both halves | 3e-05 | pathway: HALLMARK_UV_RESPONSE_UP |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZCCHC4]] | -0.48 | -0.43 / -0.36 | both halves | 1e-04 |  |
| [[FAM185A]] | -0.47 | -0.30 / -0.33 | both halves | 2e-04 |  |
| [[TDRD3]] | -0.46 | -0.34 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 2, C 9.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLRC3]] | B | KLRC3 activity raises OLFM1's level | lines that do not express KLRC3 (27) vs lines expressing it (23) | 1.78× lower at baseline in the lines without KLRC3 | 0.083 | ⚠ within organs, on part of the lines; also absent: KLRK1, KLRC2, IGFL4 |
| [[UNC5A]] | B | UNC5A activity raises OLFM1's level | lines that do not express UNC5A (21) vs lines expressing it (29) | 1.47× lower at baseline in the lines without UNC5A | 0.086 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, KCNK5, CGN |
| [[UNC13A]] | C | UNC13A activity raises OLFM1's level | lines that do not express UNC13A (29) vs lines expressing it (21) | 3.47× lower at baseline in the lines without UNC13A | 0.001 | ⚠ within organs, on part of the lines; also absent: CDH19, LINC02864, SCG3; maybe low, not absent; co-absent with the target |
| [[RGS7]] | C | RGS7 activity raises OLFM1's level | lines that do not express RGS7 (25) vs lines expressing it (25) | 2.81× lower at baseline in the lines without RGS7 | 0.001 | ⚠ within organs, on part of the lines; also absent: KCNQ5, NRXN3, ENSG00000253553; maybe low, not absent; co-absent with the target |
| [[GNG4]] | C | GNG4 activity raises OLFM1's level | lines that do not express GNG4 (20) vs lines expressing it (30) | 4.02× lower at baseline in the lines without GNG4 | 0.001 | ⚠ within organs, on part of the lines; also absent: OLFM1, JPH3, LRRC4B; co-absent with the target |
| [[NPTX1]] | C | NPTX1 activity raises OLFM1's level | lines that do not express NPTX1 (25) vs lines expressing it (25) | 3.01× lower at baseline in the lines without NPTX1 | 0.034 | ⚠ within organs, on part of the lines; also absent: JAM3, SNAP91, CECR2; co-absent with the target |
| [[JAKMIP1]] | C | JAKMIP1 activity raises OLFM1's level | lines that do not express JAKMIP1 (27) vs lines expressing it (23) | 4.11× lower at baseline in the lines without JAKMIP1 | 0.036 | ⚠ within organs, on part of the lines; also absent: CHST8, JPH3, GABBR2; co-absent with the target |
| [[SPTB]] | C | SPTB activity raises OLFM1's level | lines that do not express SPTB (22) vs lines expressing it (28) | 3.04× lower at baseline in the lines without SPTB | 0.036 | ⚠ within organs, on part of the lines; also absent: MAP7, DMKN, ICA1; maybe low, not absent; co-absent with the target |
| [[CHGB]] | C | CHGB activity raises OLFM1's level | lines that do not express CHGB (33) vs lines expressing it (17) | 3.16× lower at baseline in the lines without CHGB | 0.044 | ⚠ within organs, on part of the lines; also absent: MAGEA4, SLC6A11, CTNNA2; co-absent with the target |
| [[CHST8]] | C | CHST8 activity raises OLFM1's level | lines that do not express CHST8 (29) vs lines expressing it (21) | 3.91× lower at baseline in the lines without CHST8 | 0.055 | ⚠ within organs, on part of the lines; also absent: PLEKHG4B, JAKMIP1, SNAP91; co-absent with the target |
| [[SH3GL2]] | C | SH3GL2 activity raises OLFM1's level | lines that do not express SH3GL2 (18) vs lines expressing it (32) | 2.86× lower at baseline in the lines without SH3GL2 | 0.068 | ⚠ within organs, on part of the lines; also absent: FAM124A, SLC16A10, OLFM1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UNC5A]] | B | OLFM1 activity raises UNC5A's level | lines that do not express OLFM1 (27) vs lines expressing it (23) | 1.29× lower at baseline in the lines without OLFM1 | 0.029 | ⚠ within organs, on part of the lines; also absent: JPH3, DPYSL5, CHST8 |
| [[FAM185A]] | B | OLFM1 activity raises FAM185A's level | lines that do not express OLFM1 (27) vs lines expressing it (23) | 1.19× lower at baseline in the lines without OLFM1 | 0.075 | ⚠ within organs, on part of the lines; also absent: JPH3, DPYSL5, CHST8 |
| [[PTPRG-AS1]] | B | OLFM1 activity raises PTPRG-AS1's level | lines that do not express OLFM1 (27) vs lines expressing it (23) | 1.96× lower at baseline in the lines without OLFM1 | 0.089 | ⚠ within organs, on part of the lines; also absent: JPH3, DPYSL5, CHST8 |
| [[GNG4]] | C | OLFM1 activity raises GNG4's level | lines that do not express OLFM1 (27) vs lines expressing it (23) | 3.62× lower at baseline in the lines without OLFM1 | 0.049 | ⚠ within organs, on part of the lines; also absent: JPH3, DPYSL5, CHST8; co-absent with the target |
| [[UNC13A]] | C | OLFM1 activity raises UNC13A's level | lines that do not express OLFM1 (27) vs lines expressing it (23) | 2.63× lower at baseline in the lines without OLFM1 | 0.089 | ⚠ within organs, on part of the lines; also absent: JPH3, DPYSL5, CHST8; co-absent with the target |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.578). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.5, 33.9); signed map (32.8, 29.2). **Vector** length 42.7, 9.43% of its response variance represented; |z| ≥ 3 in 423 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +10.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.0 | +9.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +11.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +6.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.1 | +5.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +2.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.5 | +1.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +3.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.3 | -4.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -3.5 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.6 | -2.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.5 | -3.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.5 | -2.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.5 | -1.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -2.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.3 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | olfactomedin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.3 — chr9:135,075,422-135,121,180 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NOE1, OlfA, AMY, NOELIN |
| Gene groups (HGNC) | Olfactomedin domain containing |
| Hallmark sets | UV_RESPONSE_UP, ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99784](https://www.uniprot.org/uniprotkb/Q99784) (Noelin):

> Contributes to the regulation of axonal growth in the embryonic and adult central nervous system by inhibiting interactions between RTN4R and LINGO1. Inhibits RTN4R-mediated axon growth cone collapse (By similarity). May play an important role in regulating the production of neural crest cells by the neural tube (By similarity). May be required for normal responses to olfactory stimuli (By similarity).

**Summary**, from NCBI Gene [10439](https://www.ncbi.nlm.nih.gov/gene/10439):

> This gene product shares extensive sequence similarity with the rat neuronal olfactomedin-related ER localized protein. While the exact function of the encoded protein is not known, its abundant expression in brain suggests that it may have an essential role in nerve tissue. Several alternatively spliced transcripts encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:17187](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17187) · Entrez [10439](https://www.ncbi.nlm.nih.gov/gene/10439) · UniProt [Q99784](https://www.uniprot.org/uniprotkb/Q99784) · Ensembl [ENSG00000130558](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130558)

## Data

Gene col 5082: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5082); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5082, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5082]; `tensor/DDL_lfc|DDL_z.npy` [5082]; `embed/gene_vectors.npy` [5082]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5082 or target_col == 5082). Every well: [[OLFM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OLFM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
