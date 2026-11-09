---
symbol: "GNA15"
type: "gene"
col: 688
ensembl_id: "ENSG00000060558"
name: "G protein subunit alpha 15"
location: "19p13.3"
module: 34
arm: "+"
pooled_cpm: 9.51
n_lines_expressing: 25
n_dd_up: 12
n_dd_down: 20
n_dd_up_clean: 7
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 9
direction_downstream: 9
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# GNA15

*G protein subunit alpha 15* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.75× (z +9.7, q 2e-19, up in 3 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (none with an alert); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.629× (z -5.2, q 9e-05, down in 3 of 23 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDE2A]] (+0.64, fdr 1e-05), [[RAC2]] (+0.63, fdr 1e-05), [[LINC02970]] (+0.62, fdr 1e-05); moves opposite to [[USP24]] (-0.47, fdr 1e-04), [[ZZZ3]] (-0.45, fdr 2e-04), [[ZMYND11]] (-0.45, fdr 9e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[MILR1]] → it (grade B ⚠); 9 go from it, the strongest it → [[RAC2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 688.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +9.7 | 2e-19 | 3/20 (C32, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.14×** | +8.9 | 9e-17 | 0/12 | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.07×** | +8.9 | 9e-17 | 4/23 (SW48, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.78×** | +7.0 | 3e-10 | 2/23 (SW48, hTERT-HPNE) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.70×** | +6.5 | 9e-09 | 1/13 (LOX-IMVI) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.67×** | +6.3 | 3e-08 | 4/21 (RKO, HT-29, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +6.0 | 2e-07 | 9/23 (Hs 766T, hTERT-HPNE, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.55×** | +5.3 | 7e-06 | 0/22 | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.44×** | +4.4 | 6e-04 | 5/22 (HT-29, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.45×** | +4.2 | 0.001 | 0/12 | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.26×** | +4.1 | 0.003 | 2/21 (Panc 03.27, C32) | top dose only | composition shift |
| [[PF-06260933 (drug)]] 5 µM |  | **1.70×** | +3.4 | 0.034 | 4/18 (HOP62, CFPAC-1, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 1 with an alert ⚠; shown: the 15 strongest. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 688.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.629×** | -5.2 | 9e-05 | 3/23 (PANC-1, Hs 766T, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.661×** | -5.1 | 1e-04 | 13/23 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM |  | **0.675×** | -4.8 | 3e-04 | 11/23 (PANC-1, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.687×** | -4.6 | 6e-04 | 8/22 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.737×** | -4.4 | 0.001 | 8/22 (PANC-1, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.771×** | -4.4 | 0.001 | 7/23 (PANC-1, Hs 766T, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.704×** | -4.3 | 0.001 | 9/23 (PANC-1, Hs 766T, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.696×** | -4.3 | 0.001 | 13/22 (HT-29, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.715×** | -4.1 | 0.003 | 10/22 (PANC-1, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.717×** | -4.1 | 0.003 | 11/22 (PANC-1, HT-29, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.734×** | -3.8 | 0.008 | 11/23 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.740×** | -3.5 | 0.019 | 14/17 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.753×** | -3.5 | 0.023 | 6/23 (Hs 766T, HOP62, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.753×** | -3.3 | 0.034 | 5/22 (SK-MEL-2, hTERT-HPNE, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.763×** | -3.3 | 0.036 | 13/21 (HOP62, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 688. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 39.7 | 0 | 11 (5 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0787× (z -17.2) |
| [[PANC-1 (line)]] | alt | 20.5 | 0 | 11 (5 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.149× (z -13.8) |
| [[CFPAC-1 (line)]] | alt | 44.9 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.180× (z -18.5) |
| [[HT-29 (line)]] | alt | 14.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -11.1) ⚠ cell-cycle shift, explains ~17% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.172× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 30.1 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.215× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -10.0) |
| [[Hs 766T (line)]] | wt | 56.1 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -9.5) |
| [[AsPC-1 (line)]] | alt | 13.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -9.2) |
| [[COLO 205 (line)]] | alt | 13.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.230× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 24.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -9.5) |
| [[SW 900 (line)]] | alt | 13.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.153× (z -9.3) |
| [[A-172 (line)]] | wt | 2.27 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.86 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.93 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.67 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.33 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.94 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.61 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.874 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.28 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.99 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.07 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 688), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDE2A]] | +0.64 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[RAC2]] | +0.63 | +0.61 / +0.55 | both halves | 1e-05 | pathway: Platelet activation, signaling and aggregation |
| [[LINC02970]] | +0.62 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[ADAM8]] | +0.61 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[ARAP1]] | +0.61 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[KCNK3]] | +0.59 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[TMEM145]] | +0.59 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[PLCH2]] | +0.58 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[SEMA3F]] | +0.58 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[PAEP]] | +0.57 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[HPCAL1]] | +0.56 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[GIPR]] | +0.56 | +0.48 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP24]] | -0.47 | -0.34 / -0.37 | both halves | 1e-04 |  |
| [[ZZZ3]] | -0.45 | -0.31 / -0.42 | both halves | 2e-04 |  |
| [[ZMYND11]] | -0.45 | -0.39 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MILR1]] | B | MILR1 activity raises GNA15's level | lines that do not express MILR1 (19) vs lines expressing it (31) | 1.99× lower at baseline in the lines without MILR1 | 0.014 | ⚠ within organs, on part of the lines; also absent: EVA1A, LINC00973, NLRP1 |
| [[ADAM8]] | B | ADAM8 activity raises GNA15's level | lines that do not express ADAM8 (28) vs lines expressing it (22) | 2.38× lower at baseline in the lines without ADAM8 | 0.020 | ⚠ within organs, on part of the lines; also absent: PLAU, ENSG00000233539, CST6; maybe low, not absent |
| [[TMCC3]] | B | TMCC3 activity raises GNA15's level | lines that do not express TMCC3 (19) vs lines expressing it (31) | 2.12× lower at baseline in the lines without TMCC3 | 0.032 | ⚠ within organs, on part of the lines; also absent: PTPRB, KRT7, ADGRF4 |
| [[MTSS1]] | B | MTSS1 activity raises GNA15's level | lines that do not express MTSS1 (20) vs lines expressing it (30) | 1.99× lower at baseline in the lines without MTSS1 | 0.034 | ⚠ within organs, on part of the lines; also absent: RASD1, GATA3, TREM1 |
| [[CRACR2B]] | B | CRACR2B activity raises GNA15's level | lines that do not express CRACR2B (11) vs lines expressing it (39) | 2.26× lower at baseline in the lines without CRACR2B | 0.034 | ⚠ within organs, on part of the lines; also absent: PNPLA4, ENSG00000285679, DAPK2 |
| [[RAC2]] | B | RAC2 activity raises GNA15's level | lines that do not express RAC2 (19) vs lines expressing it (31) | 2.49× lower at baseline in the lines without RAC2 | 0.060 | ⚠ within organs, on part of the lines; also absent: BHLHE41, ADTRP, MANCR |
| [[PTPRE]] | B | PTPRE activity raises GNA15's level | lines that do not express PTPRE (13) vs lines expressing it (37) | 1.76× lower at baseline in the lines without PTPRE | 0.061 | ⚠ within organs, on part of the lines; also absent: PTPN22, FUT2, JPH1 |
| [[WNT7B]] | B | WNT7B activity raises GNA15's level | lines that do not express WNT7B (20) vs lines expressing it (30) | 1.85× lower at baseline in the lines without WNT7B | 0.090 | ⚠ within organs, on part of the lines; also absent: ABCC3, NHS, PPARG |
| [[PLEK2]] | C | PLEK2 activity raises GNA15's level | lines that do not express PLEK2 (17) vs lines expressing it (33) | 2.77× lower at baseline in the lines without PLEK2 | 0.007 | ⚠ within organs, on part of the lines; also absent: CDCP1, SAMD12, SDR16C5; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 7, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAC2]] | B | GNA15 activity raises RAC2's level | lines that do not express GNA15 (25) vs lines expressing it (25) | 2.72× lower at baseline in the lines without GNA15 | 0.025 | ⚠ within organs, on part of the lines; also absent: GDPD4, LINC02725, RDUR; maybe low, not absent |
| [[MAST4]] | B | GNA15 activity raises MAST4's level | lines that do not express GNA15 (25) vs lines expressing it (25) | 1.93× lower at baseline in the lines without GNA15 | 0.063 | ⚠ within organs, on part of the lines; also absent: GDPD4, LINC02725, RDUR; maybe low, not absent |
| [[MTSS1]] | B | GNA15 activity raises MTSS1's level | lines that do not express GNA15 (25) vs lines expressing it (25) | 2.05× lower at baseline in the lines without GNA15 | 0.067 | ⚠ within organs, on part of the lines; also absent: GDPD4, LINC02725, RDUR; maybe low, not absent |
| [[TCIRG1]] | B | GNA15 activity raises TCIRG1's level | lines that do not express GNA15 (25) vs lines expressing it (25) | 1.64× lower at baseline in the lines without GNA15 | 0.069 | ⚠ within organs, on part of the lines; also absent: GDPD4, LINC02725, RDUR; maybe low, not absent |
| [[ADAM28]] | B | GNA15 activity raises ADAM28's level | lines that do not express GNA15 (25) vs lines expressing it (25) | 2.34× lower at baseline in the lines without GNA15 | 0.077 | ⚠ within organs, on part of the lines; also absent: GDPD4, LINC02725, RDUR; maybe low, not absent |
| [[ADGRE2]] | B | GNA15 activity weakens ADGRE2's drug response | lines that do not express GNA15 (13) vs lines expressing it (10) | the lines without GNA15 respond 1.30× as strongly (z diff -0.61); strongest at Dinaciclib 0.05 µM: 0.97x vs 0.25x (z diff -5.6) | 0.085 | ⚠ within organs, on part of the lines; also absent: GDPD4, LINC02725, RDUR; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[ADAM8]] | B | GNA15 activity raises ADAM8's level | lines that do not express GNA15 (25) vs lines expressing it (25) | 2.23× lower at baseline in the lines without GNA15 | 0.0998 | ⚠ within organs, on part of the lines; also absent: GDPD4, LINC02725, RDUR; maybe low, not absent |
| [[PLEK2]] | C | GNA15 activity raises PLEK2's level | lines that do not express GNA15 (25) vs lines expressing it (25) | 3.10× lower at baseline in the lines without GNA15 | 0.046 | ⚠ within organs, on part of the lines; also absent: GDPD4, LINC02725, RDUR; maybe low, not absent; co-absent with the target |
| [[FAM83A]] | C | GNA15 activity raises FAM83A's level | lines that do not express GNA15 (25) vs lines expressing it (25) | 3.21× lower at baseline in the lines without GNA15 | 0.085 | ⚠ within organs, on part of the lines; also absent: GDPD4, LINC02725, RDUR; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.525). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.1, -0.6); signed map (-0.2, 48.4). **Vector** length 63.1, 16.0% of its response variance represented; |z| ≥ 3 in 617 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +6.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +6.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.3 | +4.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.2 | +8.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +2.0 | +5.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.3 | +3.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.2 | +0.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.0 | +0.1 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.3 | -5.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -1.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.9 | -4.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.6 | -4.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.5 | -3.3 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.4 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -5.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.3 | -4.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.2 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.2 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | G protein subunit alpha 15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:3,136,033-3,163,749 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GNA16 |
| Gene groups (HGNC) | G protein subunits alpha, group q |
| Hallmark sets | INFLAMMATORY_RESPONSE, APOPTOSIS |
| Reactome | 22 pathways, smallest: Fatty Acids bound to GPR40 (FFAR1) regulate insulin secretion; Acetylcholine regulates insulin secretion; Free fatty acids regulate insulin secretion |
| Matched by | ensembl_id |

**Function**, from UniProt [P30679](https://www.uniprot.org/uniprotkb/P30679) (Guanine nucleotide-binding protein subunit alpha-15):

> Member of the G protein alpha subunit family that plays a crucial role in intracellular signaling. Functions as a molecular switch, transducing signals from G protein-coupled receptors (GPCRs) to downstream effectors. In collaboration with the adapter protein TTC1, promotes HRAS activation and ERK1/2 phosphorylation independently of phospholipase Cbeta signaling. Also initiates EMR2-mediated signaling, leading to activation of Akt, MAPK, and NF-kappa-B, which in turn drives macrophage …

**Summary**, from NCBI Gene [2769](https://www.ncbi.nlm.nih.gov/gene/2769):

> Enables G protein-coupled receptor binding activity. Acts upstream of or within with a positive effect on calcium-mediated signaling. Predicted to be located in plasma membrane. Predicted to be part of heterotrimeric G-protein complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:4383](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4383) · Entrez [2769](https://www.ncbi.nlm.nih.gov/gene/2769) · UniProt [P30679](https://www.uniprot.org/uniprotkb/P30679) · Ensembl [ENSG00000060558](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000060558)

## Data

Gene col 688: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 688); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 688, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 688]; `tensor/DDL_lfc|DDL_z.npy` [688]; `embed/gene_vectors.npy` [688]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 688 or target_col == 688). Every well: [[GNA15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GNA15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
