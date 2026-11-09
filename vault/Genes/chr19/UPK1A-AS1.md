---
symbol: "UPK1A-AS1"
type: "gene"
col: 13540
ensembl_id: "ENSG00000226510"
name: "UPK1A antisense RNA 1"
location: "19q13.12"
module: 103
arm: "+"
pooled_cpm: 3.88
n_lines_expressing: 32
n_dd_up: 0
n_dd_down: 17
n_dd_up_clean: 0
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 5
direction_downstream: 5
tags: ["gene", "module/103"]
generated_by: "tahoemap"
---

# UPK1A-AS1

*UPK1A antisense RNA 1* — 19q13.12

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.422× (z -6.5, q 4e-08, down in 16 of 24 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPTBN4]] (+0.63, fdr 1e-05), [[RNF122]] (+0.61, fdr 1e-05), [[HILPDA]] (+0.61, fdr 3e-05); moves opposite to [[PARVA]] (-0.58, fdr 3e-05), [[NNT]] (-0.53, fdr 1e-04), [[CRACR2A]] (-0.52, fdr 4e-05).
> It is in [[Module 103]], a single-armed module (glycolysis).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PDZD4]] → it (grade B ⚠); 5 go from it, the strongest it → [[WDR54]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13540.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | 1.62× | +3.7 | 0.12 | 10/25 (NCI-H460, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.38× | +3.5 | 0.12 | 12/28 (SW480, NCI-H1573, …) | rises with dose |  |
| [[Flutamide (drug)]] 5 µM |  | 1.53× | +3.3 | 0.21 | 6/28 (A549, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13540.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.422×** | -6.5 | 4e-08 | 16/24 (MIA PaCa-2, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.547×** | -6.4 | 4e-08 | 17/26 (MIA PaCa-2, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.465×** | -5.5 | 4e-06 | 17/26 (SK-MEL-2, A-427, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.465×** | -5.5 | 4e-06 | 16/28 (MIA PaCa-2, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.478×** | -5.3 | 1e-05 | 14/19 (PANC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.515×** | -5.0 | 6e-05 | 17/27 (NCI-H2030, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.527×** | -4.8 | 1e-04 | 13/28 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.301×** | -4.7 | 2e-04 | 13/22 (MIA PaCa-2, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.547×** | -4.5 | 4e-04 | 17/28 (PANC-1, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.566×** | -4.3 | 0.001 | 14/27 (PANC-1, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.628×** | -3.5 | 0.025 | 13/27 (A-427, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.630×** | -3.5 | 0.026 | 11/25 (NCI-H2030, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.633×** | -3.4 | 0.027 | 10/27 (NCI-H1792, NCI-H2030, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.426×** | -3.4 | 0.032 | 12/28 (C-33 A, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.456×** | -3.1 | 0.076 | 11/27 (MIA PaCa-2, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.653×** | -3.1 | 0.077 | 15/24 (PANC-1, A-427, …) | top dose only | cell-cycle shift (explains ~16% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13540. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 8.69 | 0 | 10 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0218× (z -19.1) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.122× (z -10.9) |
| [[MIA PaCa-2 (line)]] | alt | 15.5 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0495× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.154× (z -13.1) |
| [[SK-MEL-2 (line)]] | alt | 14.7 | 0 | 3 (2 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0745× (z -11.3) ⚠ cell-cycle shift, explains ~9% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.202× (z -10.3) |
| [[A-427 (line)]] | wt | 13.1 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.127× (z -9.3) |
| [[NCI-H1573 (line)]] | alt | 4.32 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0450× (z -9.9) |
| [[NCI-H2030 (line)]] | alt | 6.88 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0342× (z -12.1) |
| [[A-172 (line)]] | wt | 6.92 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -9.6) |
| [[A549 (line)]] | wt | 8.11 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.135× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[C-33 A (line)]] | alt | 9.84 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -9.6) |
| [[H4 (line)]] | wt | 14.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 9.60 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -11.8) |
| [[NCI-H460 (line)]] | wt | 3.29 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0829× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 6.56 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -9.1) |
| [[A498 (line)]] | wt | 0.397 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.645 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.465 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.447 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.14 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.350 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.365 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.478 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.908 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.459 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.289 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.276 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.548 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.571 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.297 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.336 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.350 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.06 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.753 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.395 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.20 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13540), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPTBN4]] | +0.63 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[RNF122]] | +0.61 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[HILPDA]] | +0.61 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[ABCB9]] | +0.61 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[ARID3A]] | +0.60 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[GYS1]] | +0.60 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[NGLY1]] | +0.60 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[MAPT]] | +0.59 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[PPP2R5B]] | +0.58 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[CAMSAP3]] | +0.57 | +0.57 / +0.35 | both halves | 1e-04 |  |
| [[DLK2]] | +0.57 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[ENO2]] | +0.57 | +0.48 / +0.54 | both halves | 2e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PARVA]] | -0.58 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[NNT]] | -0.53 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[CRACR2A]] | -0.52 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[NIPAL2]] | -0.52 | -0.52 / -0.25 | both halves | 4e-04 |  |
| [[PSME3IP1]] | -0.50 | -0.40 / -0.41 | both halves | 4e-05 |  |
| [[CERS2]] | -0.50 | -0.31 / -0.43 | both halves | 2e-04 |  |
| [[AVEN]] | -0.50 | -0.39 / -0.42 | both halves | 6e-05 |  |
| [[PSME3]] | -0.50 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[SNX5]] | -0.49 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[MAPKAPK5]] | -0.49 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[ADI1]] | -0.49 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[HDHD2]] | -0.49 | -0.37 / -0.45 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDZD4]] | B | PDZD4 activity raises UPK1A-AS1's level | lines that do not express PDZD4 (22) vs lines expressing it (28) | 2.55× lower at baseline in the lines without PDZD4 | 8e-04 | ⚠ within organs, on part of the lines; also absent: CECR2, CPEB1, COLEC12 |
| [[PRAME]] | B | PRAME activity raises UPK1A-AS1's level | lines that do not express PRAME (25) vs lines expressing it (25) | 2.22× lower at baseline in the lines without PRAME | 0.058 | ⚠ within organs, on part of the lines; also absent: GLDC, NR0B1, PAX2 |
| [[TMEM145]] | B | TMEM145 activity raises UPK1A-AS1's level | lines that do not express TMEM145 (11) vs lines expressing it (39) | 2.48× lower at baseline in the lines without TMEM145 | 0.061 | ⚠ within organs, on part of the lines; also absent: GXYLT2, KCNK13, DLX1 |
| [[TOP2A]] | B | TOP2A activity raises UPK1A-AS1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ZNF404]] | C | ZNF404 activity raises UPK1A-AS1's level | lines that do not express ZNF404 (14) vs lines expressing it (36) | 2.81× lower at baseline in the lines without ZNF404 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: MIR130AHG, RAB34, PYGO1; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WDR54]] | B | UPK1A-AS1 activity raises WDR54's level | lines that do not express UPK1A-AS1 (18) vs lines expressing it (32) | 2.03× lower at baseline in the lines without UPK1A-AS1 | 0.088 | ⚠ within organs, on part of the lines; also absent: CERS4, SUSD5, WIPF1 |
| [[FBXO27]] | B | UPK1A-AS1 activity raises FBXO27's level | lines that do not express UPK1A-AS1 (18) vs lines expressing it (32) | 2.51× lower at baseline in the lines without UPK1A-AS1 | 0.095 | ⚠ within organs, on part of the lines; also absent: CERS4, SUSD5, WIPF1 |
| [[MAP3K15]] | B | UPK1A-AS1 activity raises MAP3K15's level | lines that do not express UPK1A-AS1 (18) vs lines expressing it (32) | 2.53× lower at baseline in the lines without UPK1A-AS1 | 0.099 | ⚠ within organs, on part of the lines; also absent: CERS4, SUSD5, WIPF1 |
| [[RUNX3]] | C | UPK1A-AS1 activity raises RUNX3's level | lines that do not express UPK1A-AS1 (18) vs lines expressing it (32) | 4.31× lower at baseline in the lines without UPK1A-AS1 | 0.018 | ⚠ within organs, on part of the lines; also absent: CERS4, SUSD5, WIPF1; co-absent with the target |
| [[FBXO17]] | C | UPK1A-AS1 activity raises FBXO17's level | lines that do not express UPK1A-AS1 (18) vs lines expressing it (32) | 4.53× lower at baseline in the lines without UPK1A-AS1 | 0.059 | ⚠ within organs, on part of the lines; also absent: CERS4, SUSD5, WIPF1; co-absent with the target |

## Where it sits

- **Module**: [[Module 103]] — glycolysis; 45 genes; every member is in the + arm (projection on the module's main direction 0.634). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (12.7, -14.0); signed map (-29.3, 32.9). **Vector** length 60.8, 15.0% of its response variance represented; |z| ≥ 3 in 571 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +3.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.6 | +3.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | +0.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.7 | +2.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.7 | +2.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.2 | +1.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.1 | +1.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.1 | +2.8 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.6 | -5.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | -2.5 | -2.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.2 | -5.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -2.2 | +1.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.1 | -2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.6 | -2.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.4 | -1.8 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.2 | -2.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.1 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | UPK1A antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 19q13.12 — chr19:35,667,948-35,673,304 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40603](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40603) · Entrez [100862728](https://www.ncbi.nlm.nih.gov/gene/100862728) · Ensembl [ENSG00000226510](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000226510)

## Data

Gene col 13540: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13540); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13540, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13540]; `tensor/DDL_lfc|DDL_z.npy` [13540]; `embed/gene_vectors.npy` [13540]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13540 or target_col == 13540). Every well: [[UPK1A-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UPK1A-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
