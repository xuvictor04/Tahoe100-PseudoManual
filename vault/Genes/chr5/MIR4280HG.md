---
symbol: "MIR4280HG"
type: "gene"
col: 13927
ensembl_id: "ENSG00000233828"
name: "MIR4280 host gene"
location: "5q14.3"
module: 196
arm: "+"
pooled_cpm: 2.49
n_lines_expressing: 29
n_dd_up: 12
n_dd_down: 11
n_dd_up_clean: 4
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 10
direction_downstream: 11
tags: ["gene", "module/196"]
generated_by: "tahoemap"
---

# MIR4280HG

*MIR4280 host gene* — 5q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.36× (z +13.1, q 3e-36, up in 11 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (none with an alert); the strongest is [[Trametinib (drug)]] 5 µM: 0.436× (z -6.5, q 6e-08, down in 20 of 25 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RDUR]] (+0.73, fdr 7e-06), [[ZPLD1]] (+0.66, fdr 1e-05), [[EVA1A]] (+0.66, fdr 7e-06); moves opposite to [[TOM1]] (-0.51, fdr 3e-05), [[KIF13A]] (-0.48, fdr 9e-05), [[THAP8]] (-0.47, fdr 1e-04).
> It is in [[Module 196]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[ZFPM2-AS1]] → it (grade B ⚠); 11 go from it, the strongest it → [[ZNF697]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13927.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.36×** | +13.1 | 3e-36 | 11/20 (NCI-H2347, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.51×** | +9.6 | 2e-19 | 2/9 (SNU-423, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.69×** | +9.6 | 2e-19 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.78×** | +7.2 | 8e-11 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.61×** | +5.1 | 3e-05 | 3/24 (SW480, SNU-423, …) | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.17×** | +4.2 | 0.002 | 0/7 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.70×** | +4.1 | 0.004 | 3/23 (NCI-H2347, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +3.7 | 0.015 | 3/24 (SW480, NCI-H2347, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.61×** | +3.6 | 0.018 | 0/8 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.39×** | +3.5 | 0.029 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.30×** | +3.3 | 0.047 | 0/2 | inconsistent across doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.51×** | +3.2 | 0.074 | 1/13 (SNU-423) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Bendamustine (drug)]] 5 µM |  | 1.51× | +3.0 | 0.10 | 0/16 | top dose only |  |
| [[Saquinavir (drug)]] 5 µM |  | 1.32× | +3.0 | 0.11 | 2/17 (KATO III, SNU-423) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13927.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.436×** | -6.5 | 6e-08 | 20/25 (HOP62, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.496×** | -5.3 | 3e-05 | 15/24 (LOX-IMVI, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.543×** | -4.6 | 5e-04 | 12/24 (SW480, HOP62, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.544×** | -4.6 | 5e-04 | 14/21 (RKO, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.534×** | -4.4 | 0.001 | 11/24 (SW480, HOP62, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.578×** | -4.2 | 0.003 | 17/23 (SK-MEL-2, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.579×** | -4.2 | 0.003 | 11/24 (SW480, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.421×** | -3.4 | 0.042 | 6/20 (LOX-IMVI, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.700×** | -3.3 | 0.065 | 10/24 (SK-MEL-2, COLO 205, …) | all doses, flat | noisy plate (z scaled) |
| [[RMC-6236 (drug)]] 5 µM |  | **0.447×** | -3.2 | 0.074 | 7/23 (SK-MEL-2, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.782×** | -3.2 | 0.074 | 11/25 (SW480, HOP62, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13927. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 14.7 | 0 | 3 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0900× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.105× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 10.6 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0676× (z -9.6) |
| [[RKO (line)]] | wt | 11.5 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0192× (z -15.8) |
| [[LOX-IMVI (line)]] | wt | 20.4 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0709× (z -12.0) |
| [[Panc 03.27 (line)]] | alt | 8.66 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0429× (z -9.6) ⚠ cell-cycle shift, explains ~8% of this change |
| [[SW480 (line)]] | alt | 2.29 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.0543× (z -9.7) |
| [[A-172 (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.304 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.940 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.374 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.494 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.583 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.308 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.395 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.946 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.439 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.464 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.828 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.563 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.566 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.674 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.618 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.561 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.17 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.398 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.701 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.393 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.873 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.472 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.441 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.461 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.782 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.351 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.348 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.467 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.811 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.404 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13927), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RDUR]] | +0.73 | +0.61 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[ZPLD1]] | +0.66 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[EVA1A]] | +0.66 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[DOCK2]] | +0.65 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[CACNA2D4]] | +0.64 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[TGFA]] | +0.64 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[LAPTM5]] | +0.62 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[MANCR]] | +0.62 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[SIGLEC15]] | +0.61 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[MYEOV]] | +0.61 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[LINC00973]] | +0.60 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[LINC02454]] | +0.60 | +0.47 / +0.66 | both halves | 2e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOM1]] | -0.51 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[KIF13A]] | -0.48 | -0.37 / -0.44 | both halves | 9e-05 |  |
| [[THAP8]] | -0.47 | -0.35 / -0.49 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 5, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZFPM2-AS1]] | B | ZFPM2-AS1 activity raises MIR4280HG's level | lines that do not express ZFPM2-AS1 (16) vs lines expressing it (34) | 1.80× lower at baseline in the lines without ZFPM2-AS1 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: MIR3142HG, FRMD4A, TLR6 |
| [[SIGLEC15]] | B | SIGLEC15 activity raises MIR4280HG's level | lines that do not express SIGLEC15 (27) vs lines expressing it (23) | 1.87× lower at baseline in the lines without SIGLEC15 | 0.042 | ⚠ within organs, on part of the lines; also absent: LINC01615, ZNF257, NLRP1 |
| [[MAST4]] | B | MAST4 activity raises MIR4280HG's level | lines that do not express MAST4 (11) vs lines expressing it (39) | 1.64× lower at baseline in the lines without MAST4 | 0.094 | ⚠ within organs, on part of the lines; also absent: TSPAN12, AHR, TLE4; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises MIR4280HG's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MAP2K2]] | B | MAP2K2 activity raises MIR4280HG's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[LINC01812]] | C | LINC01812 activity raises MIR4280HG's level | lines that do not express LINC01812 (35) vs lines expressing it (15) | 2.02× lower at baseline in the lines without LINC01812 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235495, ENSG00000224865, ENSG00000287622; co-absent with the target |
| [[EVA1A]] | C | EVA1A activity raises MIR4280HG's level | lines that do not express EVA1A (21) vs lines expressing it (29) | 1.82× lower at baseline in the lines without EVA1A | 0.038 | ⚠ within organs, on part of the lines; also absent: NLRP1, MILR1, SNAI2; co-absent with the target |
| [[RDUR]] | C | RDUR activity raises MIR4280HG's level | lines that do not express RDUR (28) vs lines expressing it (22) | 1.80× lower at baseline in the lines without RDUR | 0.052 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: LNCOG, ENSG00000287622, GYPC; co-absent with the target |
| [[VEPH1]] | C | VEPH1 activity raises MIR4280HG's level | lines that do not express VEPH1 (26) vs lines expressing it (24) | 1.90× lower at baseline in the lines without VEPH1 | 0.066 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000222032, PHACTR1, GYPC; co-absent with the target |
| [[CARD11]] | C | CARD11 activity raises MIR4280HG's level | lines that do not express CARD11 (33) vs lines expressing it (17) | 1.42× lower at baseline in the lines without CARD11 | 0.069 | ⚠ within organs, on part of the lines; also absent: TNFSF14, KRT81, C3; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 7, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF697]] | B | MIR4280HG activity raises ZNF697's level | lines that do not express MIR4280HG (21) vs lines expressing it (29) | 1.94× lower at baseline in the lines without MIR4280HG | 0.044 | ⚠ within organs, on part of the lines; also absent: EVA1A, MILR1, LNX1; maybe low, not absent |
| [[SLC45A3]] | B | MIR4280HG activity raises SLC45A3's level | lines that do not express MIR4280HG (21) vs lines expressing it (29) | 1.34× lower at baseline in the lines without MIR4280HG | 0.050 | ⚠ within organs, on part of the lines; also absent: EVA1A, MILR1, LNX1; maybe low, not absent |
| [[CACNA2D4]] | B | MIR4280HG activity raises CACNA2D4's level | lines that do not express MIR4280HG (21) vs lines expressing it (29) | 1.97× lower at baseline in the lines without MIR4280HG | 0.054 | ⚠ within organs, on part of the lines; also absent: EVA1A, MILR1, LNX1; maybe low, not absent |
| [[NFIL3]] | B | MIR4280HG activity raises NFIL3's level | lines that do not express MIR4280HG (21) vs lines expressing it (29) | 1.50× lower at baseline in the lines without MIR4280HG | 0.061 | ⚠ within organs, on part of the lines; also absent: EVA1A, MILR1, LNX1; maybe low, not absent |
| [[ITGA3]] | B | MIR4280HG activity raises ITGA3's level | lines that do not express MIR4280HG (21) vs lines expressing it (29) | 1.94× lower at baseline in the lines without MIR4280HG | 0.067 | ⚠ within organs, on part of the lines; also absent: EVA1A, MILR1, LNX1; maybe low, not absent |
| [[LRCH1]] | B | MIR4280HG activity raises LRCH1's level | lines that do not express MIR4280HG (21) vs lines expressing it (29) | 1.41× lower at baseline in the lines without MIR4280HG | 0.086 | ⚠ within organs, on part of the lines; also absent: EVA1A, MILR1, LNX1; maybe low, not absent |
| [[WNK4]] | B | MIR4280HG activity raises WNK4's level | lines that do not express MIR4280HG (21) vs lines expressing it (29) | 2.02× lower at baseline in the lines without MIR4280HG | 0.096 | ⚠ within organs, on part of the lines; also absent: EVA1A, MILR1, LNX1; maybe low, not absent |
| [[CARD11]] | C | MIR4280HG activity raises CARD11's level | lines that do not express MIR4280HG (21) vs lines expressing it (29) | 2.86× lower at baseline in the lines without MIR4280HG | 0.012 | ⚠ within organs, on part of the lines; also absent: EVA1A, MILR1, LNX1; maybe low, not absent; co-absent with the target |
| [[SHROOM4]] | C | MIR4280HG activity raises SHROOM4's level | lines that do not express MIR4280HG (21) vs lines expressing it (29) | 2.81× lower at baseline in the lines without MIR4280HG | 0.063 | ⚠ within organs, on part of the lines; also absent: EVA1A, MILR1, LNX1; maybe low, not absent; co-absent with the target |
| [[EVA1A]] | C | MIR4280HG activity raises EVA1A's level | lines that do not express MIR4280HG (21) vs lines expressing it (29) | 3.13× lower at baseline in the lines without MIR4280HG | 0.087 | ⚠ within organs, on part of the lines; also absent: EVA1A, MILR1, LNX1; maybe low, not absent; co-absent with the target |
| [[LCP1]] | C | MIR4280HG activity raises LCP1's level | lines that do not express MIR4280HG (21) vs lines expressing it (29) | 2.16× lower at baseline in the lines without MIR4280HG | 0.099 | ⚠ within organs, on part of the lines; also absent: EVA1A, MILR1, LNX1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 196]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.561). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (47.8, 10.9); signed map (15.4, 47.3). **Vector** length 55.7, 13.5% of its response variance represented; |z| ≥ 3 in 684 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +13.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +7.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | +1.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.3 | +1.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.1 | +1.4 |
| fall | [[Trametinib (drug)]] 5 µM |  | -2.9 | -6.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.5 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.4 | -4.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.3 | -3.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.2 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.2 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | MIR4280 host gene |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5q14.3 — chr5:87,048,858-87,138,397 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | MicroRNA non-coding host genes |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:54975](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:54975) · Entrez [117751736](https://www.ncbi.nlm.nih.gov/gene/117751736) · Ensembl [ENSG00000233828](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000233828)

## Data

Gene col 13927: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13927); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13927, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13927]; `tensor/DDL_lfc|DDL_z.npy` [13927]; `embed/gene_vectors.npy` [13927]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13927 or target_col == 13927). Every well: [[MIR4280HG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIR4280HG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
