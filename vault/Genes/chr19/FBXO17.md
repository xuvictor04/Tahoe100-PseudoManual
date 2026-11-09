---
symbol: "FBXO17"
type: "gene"
col: 15616
ensembl_id: "ENSG00000269190"
name: "F-box protein 17"
location: "19q13.2"
module: 18
arm: "+"
pooled_cpm: 64.42
n_lines_expressing: 32
n_dd_up: 1
n_dd_down: 25
n_dd_up_clean: 0
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 11
direction_downstream: 9
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# FBXO17

*F-box protein 17* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.53× (z +6.6, q 2e-08, up in 17 of 28 measured lines) ⚠ toxic; transcription drop.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (HOP62 2.57×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.312× (z -25.3, q 0e+00, down in 30 of 30 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CNTNAP3B]] (+0.56, fdr 1e-05), [[ZNF544]] (+0.53, fdr 3e-05), [[RILPL1]] (+0.52, fdr 1e-05); moves opposite to [[SEPTIN9-DT]] (-0.48, fdr 8e-04, ⚠ one half only (not replicated)), [[MUC5B]] (-0.47, fdr 2e-04), [[GNA14]] (-0.46, fdr 7e-04), [[TSPAN1]] (-0.45, fdr 2e-04).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[GNA14]] → it (grade B ⚠); 9 go from it, the strongest it → [[ZNF304]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15616.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (HOP62 2.57×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.53×** | +6.6 | 2e-08 | 17/28 (HOP62, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15616.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.312×** | -25.3 | 0e+00 | 30/30 (C32, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.422×** | -18.7 | 0e+00 | 29/30 (HOP62, C32, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.363×** | -15.6 | 0e+00 | 26/30 (MIA PaCa-2, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.382×** | -14.8 | 0e+00 | 25/30 (MIA PaCa-2, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.444×** | -12.5 | 1e-33 | 26/30 (A-427, NCI-H23, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.453×** | -12.2 | 5e-32 | 25/30 (C32, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.266×** | -10.6 | 1e-24 | 26/30 (HOP62, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.507×** | -10.0 | 1e-21 | 21/30 (C32, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.509×** | -10.0 | 2e-21 | 23/30 (C32, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.546×** | -8.9 | 2e-17 | 24/29 (C32, MIA PaCa-2, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.727×** | -6.9 | 3e-10 | 19/30 (C32, PANC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.644×** | -6.7 | 8e-10 | 21/30 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.449×** | -6.4 | 6e-09 | 21/30 (HOP62, C32, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.790×** | -5.1 | 2e-05 | 14/30 (HOP62, A-172, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.723×** | -5.0 | 3e-05 | 17/30 (NCI-H1792, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.723×** | -5.0 | 3e-05 | 16/30 (A549, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~17% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.40 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15616. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 129 | 0 | 18 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0777× (z -30.2) |
| [[MIA PaCa-2 (line)]] | alt | 155 | 0 | 14 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -26.0) |
| [[PANC-1 (line)]] | alt | 433 | 0 | 12 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.398× (z -19.5) |
| [[HOP62 (line)]] | alt | 79.9 | 1 (1 ⚠) | 10 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.57× (z +10.3) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.192× (z -25.5) |
| [[A-172 (line)]] | wt | 71.7 | 0 | 10 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -18.3) |
| [[NCI-H460 (line)]] | wt | 40.9 | 0 | 10 | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -21.0) |
| [[A549 (line)]] | wt | 196 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -24.0) |
| [[HepG2_C3A (line)]] | wt | 101 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -19.8) |
| [[NCI-H1792 (line)]] | alt | 45.2 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -16.8) |
| [[A498 (line)]] | wt | 77.0 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -17.1) |
| [[SW480 (line)]] | alt | 49.4 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -19.0) |
| [[NCI-H23 (line)]] | alt | 64.1 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.178× (z -15.6) |
| [[A-427 (line)]] | wt | 94.1 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.150× (z -19.3) |
| [[C-33 A (line)]] | alt | 101 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.201× (z -14.0) |
| [[LOX-IMVI (line)]] | wt | 35.7 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -16.4) |
| [[SK-MEL-2 (line)]] | alt | 36.0 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -18.8) |
| [[H4 (line)]] | wt | 72.7 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.188× (z -17.6) |
| [[HEC-1-A (line)]] | alt | 78.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -15.0) |
| [[Panc 03.27 (line)]] | alt | 23.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -11.8) |
| [[HS-578T (line)]] | alt | 43.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.460× (z -9.2) |
| [[SNU-423 (line)]] | alt | 32.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -11.9) |
| [[AN3 CA (line)]] | alt | 70.7 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0592× (z -14.5) |
| [[CHP-212 (line)]] | wt | 58.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.177× (z -11.9) |
| [[hTERT-HPNE (line)]] | wt | 25.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -10.2) |
| [[NCI-H2347 (line)]] | alt | 16.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -9.6) |
| [[AsPC-1 (line)]] | alt | 4.04 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.72 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 6.58 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.82 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.27 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 10.8 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.90 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 14.4 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.67 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.95 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.55 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.87 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.00 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 256 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.98 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.34 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.31 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.75 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.55 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15616), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNTNAP3B]] | +0.56 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[ZNF544]] | +0.53 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[RILPL1]] | +0.52 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[APBA2]] | +0.51 | +0.48 / +0.41 | both halves | 4e-05 |  |
| [[RAB11FIP3]] | +0.51 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[DNAAF9]] | +0.50 | +0.55 / +0.32 | both halves | 2e-04 |  |
| [[ST6GAL1]] | +0.49 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[ZNF354A]] | +0.47 | +0.33 / +0.44 | both halves | 1e-04 |  |
| [[FBXO27]] | +0.47 | +0.44 / +0.44 | both halves | 3e-05 | same gene group; pathway: Antigen processing: Ubiquitination & Proteasome degradation; STRING 431; ⚠ same locus (15.0 kb, same strand: neighbours can correlate without regulation) |
| [[XYLB]] | +0.47 | +0.48 / +0.34 | both halves | 1e-04 |  |
| [[UPK1A-AS1]] | +0.46 | +0.50 / +0.30 | both halves | 2e-04 |  |
| [[PUS7]] | +0.46 | +0.46 / +0.42 | both halves | 4e-05 |  |
| [[WIPF1]] | +0.46 | +0.55 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEPTIN9-DT]] | -0.48 | -0.50 / -0.20 | ⚠ one half (not replicated) | 8e-04 |  |
| [[MUC5B]] | -0.47 | -0.45 / -0.32 | both halves | 2e-04 |  |
| [[GNA14]] | -0.46 | -0.48 / -0.21 | both halves | 7e-04 |  |
| [[TSPAN1]] | -0.45 | -0.48 / -0.32 | both halves | 2e-04 |  |
| [[PROM2]] | -0.45 | -0.46 / -0.38 | both halves | 6e-05 |  |
| [[MAGED2]] | -0.44 | -0.39 / -0.37 | both halves | 9e-05 |  |
| [[PITPNM3]] | -0.44 | -0.43 / -0.34 | both halves | 1e-04 |  |
| [[CEACAM6]] | -0.44 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[MYO7B]] | -0.43 | -0.46 / -0.21 | both halves | 6e-04 |  |
| [[ZNF503-AS1]] | -0.43 | -0.45 / -0.28 | both halves | 3e-04 |  |
| [[ST6GALNAC1]] | -0.43 | -0.45 / -0.32 | both halves | 2e-04 |  |
| [[DGKA]] | -0.43 | -0.37 / -0.37 | both halves | 9e-05 |  |
| [[CEACAM5]] | -0.43 | -0.43 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 8, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GNA14]] | B | GNA14 activity lowers FBXO17's level | lines that do not express GNA14 (5) vs lines expressing it (45) | 2.99× higher at baseline in the lines without GNA14 | 0.028 | ⚠ within organs, on part of the lines; also absent: SSUH2, EXT1, SAMSN1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises FBXO17's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CEACAM6]] | B | CEACAM6 activity lowers FBXO17's level | lines that do not express CEACAM6 (37) vs lines expressing it (13) | 4.52× higher at baseline in the lines without CEACAM6 | 0.032 | ⚠ within organs, on part of the lines; also absent: DAPP1, TMPRSS2, CDH17 |
| [[P2RY2]] | B | P2RY2 activity lowers FBXO17's level | lines that do not express P2RY2 (27) vs lines expressing it (23) | 3.61× higher at baseline in the lines without P2RY2 | 0.034 | ⚠ within organs, on part of the lines; also absent: C6orf132, FAM83B, RNF223 |
| [[FBXO27]] | B | FBXO27 activity raises FBXO17's level | lines that do not express FBXO27 (28) vs lines expressing it (22) | 3.72× lower at baseline in the lines without FBXO27 | 0.054 | ⚠ within organs, on part of the lines; also absent: SLFN13, DLL3, PAX2 |
| [[KLF8]] | B | KLF8 activity weakens FBXO17's drug response | lines that do not express KLF8 (17) vs lines expressing it (13) | the lines without KLF8 respond 1.41× as strongly (z diff -2.63); strongest at Epirubicin (hydrochloride) 5 µM: 0.42x vs 0.68x (z diff -4.6) | 0.066 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, LMO3, ENSG00000259692; target measured in part of the lines; artifact flags |
| [[CEACAM5]] | B | CEACAM5 activity lowers FBXO17's level | lines that do not express CEACAM5 (39) vs lines expressing it (11) | 4.92× higher at baseline in the lines without CEACAM5 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, ENSG00000267881 |
| [[SEC14L4]] | B | SEC14L4 activity raises FBXO17's level | lines that do not express SEC14L4 (29) vs lines expressing it (21) | 2.22× lower at baseline in the lines without SEC14L4 | 0.097 | ⚠ within organs, on part of the lines; also absent: WT1-AS, ACP7, PLTP |
| [[UPK1A-AS1]] | C | UPK1A-AS1 activity raises FBXO17's level | lines that do not express UPK1A-AS1 (18) vs lines expressing it (32) | 4.53× lower at baseline in the lines without UPK1A-AS1 | 0.059 | ⚠ within organs, on part of the lines; also absent: CERS4, SUSD5, WIPF1; co-absent with the target |
| [[DNAAF9]] | C | DNAAF9 activity raises FBXO17's level | lines that do not express DNAAF9 (12) vs lines expressing it (38) | 8.54× lower at baseline in the lines without DNAAF9 | 0.060 | ⚠ within organs, on part of the lines; also absent: CHST10, ENSG00000268163, RIMKLB; co-absent with the target; its own permutation p |
| [[CERS4]] | C | CERS4 activity raises FBXO17's level | lines that do not express CERS4 (17) vs lines expressing it (33) | 4.90× lower at baseline in the lines without CERS4 | 0.097 | ⚠ within organs, on part of the lines; also absent: UPK1A-AS1, PCSK1N, CHST10; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 7, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF304]] | B | FBXO17 activity raises ZNF304's level | lines that do not express FBXO17 (18) vs lines expressing it (32) | 2.44× lower at baseline in the lines without FBXO17 | 0.040 | ⚠ within organs, on part of the lines; also absent: ENSG00000269547, MRC2, MIR130AHG |
| [[PCOLCE2]] | B | FBXO17 activity raises PCOLCE2's level | lines that do not express FBXO17 (18) vs lines expressing it (32) | 2.66× lower at baseline in the lines without FBXO17 | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000269547, MRC2, MIR130AHG |
| [[SEC14L4]] | B | FBXO17 activity raises SEC14L4's level | lines that do not express FBXO17 (18) vs lines expressing it (32) | 1.57× lower at baseline in the lines without FBXO17 | 0.056 | ⚠ within organs, on part of the lines; also absent: ENSG00000269547, MRC2, MIR130AHG |
| [[RHBDF2]] | B | FBXO17 activity raises RHBDF2's level | lines that do not express FBXO17 (18) vs lines expressing it (32) | 2.05× lower at baseline in the lines without FBXO17 | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000269547, MRC2, MIR130AHG |
| [[PGBD1]] | B | FBXO17 activity raises PGBD1's level | lines that do not express FBXO17 (18) vs lines expressing it (32) | 1.74× lower at baseline in the lines without FBXO17 | 0.072 | ⚠ within organs, on part of the lines; also absent: ENSG00000269547, MRC2, MIR130AHG |
| [[P2RY2]] | B | FBXO17 activity lowers P2RY2's level | lines that do not express FBXO17 (18) vs lines expressing it (32) | 2.61× higher at baseline in the lines without FBXO17 | 0.085 | ⚠ within organs, on part of the lines; also absent: ENSG00000269547, MRC2, MIR130AHG |
| [[CEACAM5]] | B | FBXO17 activity lowers CEACAM5's level | lines that do not express FBXO17 (18) vs lines expressing it (32) | 4.19× higher at baseline in the lines without FBXO17 | 0.092 | ⚠ within organs, on part of the lines; also absent: ENSG00000269547, MRC2, MIR130AHG |
| [[DNAAF9]] | C | FBXO17 activity raises DNAAF9's level | lines that do not express FBXO17 (18) vs lines expressing it (32) | 6.20× lower at baseline in the lines without FBXO17 | 2e-04 | ⚠ within organs, on part of the lines; also absent: ENSG00000269547, MRC2, MIR130AHG; co-absent with the target |
| [[WIPF1]] | C | FBXO17 activity raises WIPF1's level | lines that do not express FBXO17 (18) vs lines expressing it (32) | 4.95× lower at baseline in the lines without FBXO17 | 0.021 | ⚠ within organs, on part of the lines; also absent: ENSG00000269547, MRC2, MIR130AHG; co-absent with the target |

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.300). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (7.5, 44.9); signed map (-27.3, 37.2). **Vector** length 84.9, 23.1% of its response variance represented; |z| ≥ 3 in 798 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | -1.3 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.0 | +2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.6 | +0.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.6 | +1.4 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.3 | +1.7 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.0 | -10.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -5.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -2.8 | -8.9 |
|  | [[Selinexor (drug)]] 5 µM |  | -2.8 | -6.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.5 | -18.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | -6.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.6 | -1.0 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -1.5 | -0.0 |

## What is on record

|  |  |
|---|---|
| Name | F-box protein 17 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:38,941,401-38,975,742 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FBG4, FLJ25205, MGC9379, FLJ11798, Fbx17; previously FBXO26 |
| Gene groups (HGNC) | F-boxes other |
| Reactome | 4 pathways, smallest: Neddylation; Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96EF6](https://www.uniprot.org/uniprotkb/Q96EF6) (F-box only protein 17):

> Substrate-recognition component of the SCF (SKP1-CUL1-F-box protein)-type E3 ubiquitin ligase complex. Able to recognize and bind denatured glycoproteins, which are modified with complex-type oligosaccharides. Also recognizes sulfated glycans. Does not bind high-mannose glycoproteins.

**Summary**, from NCBI Gene [115290](https://www.ncbi.nlm.nih.gov/gene/115290):

> This gene encodes a member of the F-box protein family which is characterized by the F-box motif. The F-box proteins constitute one of the four subunits of the ubiquitin protein ligase complex called SCFs (SKP1-cullin-F-box), which function in phosphorylation-dependent ubiquitination. The F-box proteins are divided into 3 classes: Fbws containing WD-40 domains, Fbls containing leucine-rich repeats, and Fbxs containing either different protein-protein interaction modules or no recognizable …

**Accessions** — [HGNC:18754](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18754) · Entrez [115290](https://www.ncbi.nlm.nih.gov/gene/115290) · UniProt [Q96EF6](https://www.uniprot.org/uniprotkb/Q96EF6) · Ensembl [ENSG00000269190](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000269190)

## Data

Gene col 15616: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15616); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15616, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15616]; `tensor/DDL_lfc|DDL_z.npy` [15616]; `embed/gene_vectors.npy` [15616]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15616 or target_col == 15616). Every well: [[FBXO17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXO17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
