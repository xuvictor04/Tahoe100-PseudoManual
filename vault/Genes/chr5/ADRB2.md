---
symbol: "ADRB2"
type: "gene"
col: 9787
ensembl_id: "ENSG00000169252"
name: "adrenoceptor beta 2"
location: "5q32"
module: 113
arm: "+"
pooled_cpm: 6.18
n_lines_expressing: 27
n_dd_up: 25
n_dd_down: 1
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 6
direction_downstream: 4
tags: ["gene", "module/113"]
generated_by: "tahoemap"
---

# ADRB2

*adrenoceptor beta 2* — 5q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 10.2× (z +21.9, q 0e+00, up in 24 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.659× (z -4.0, q 0.039, down in 8 of 24 measured lines) ⚠ unreliable plate only.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (SNU-423 0.125×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (NCI-H1792 0.104×; ⚠ cell-cycle shift, would explain all of this change); [[Auranofin (drug)]] 5 µM in 1 line (LOX-IMVI 0.0576×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SGK1]] (+0.67, fdr 7e-06), [[NEDD9]] (+0.66, fdr 7e-06), [[PLK2]] (+0.58, fdr 9e-06); moves opposite to [[GPALPP1]] (-0.56, fdr 4e-05), [[C8orf44-SGK3]] (-0.49, fdr 5e-05), [[LAMTOR5-AS1]] (-0.49, fdr 3e-04).
> It is in [[Module 113]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TSPAN2]] → it (grade B ⚠); 4 go from it, the strongest it → [[VSIR]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9787.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **10.2×** | +21.9 | 0e+00 | 24/25 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **9.59×** | +21.3 | 0e+00 | 25/25 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **7.29×** | +18.7 | 0e+00 | 23/24 (PANC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **3.62×** | +17.1 | 0e+00 | 19/24 (SK-MEL-2, HOP62, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.69×** | +12.3 | 1e-32 | 18/25 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.11×** | +9.9 | 3e-21 | 8/20 (CFPAC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **2.54×** | +8.4 | 3e-15 | 2/8 (NCI-H1792, HOP62) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +8.0 | 8e-14 | 9/21 (A549, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.10×** | +7.0 | 2e-10 | 11/20 (SK-MEL-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **2.09×** | +6.4 | 9e-09 | 3/11 (AsPC-1, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.85×** | +5.1 | 1e-05 | 8/22 (PANC-1, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.68×** | +4.9 | 6e-05 | 6/21 (CFPAC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +4.0 | 0.003 | 4/25 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.54×** | +3.9 | 0.004 | 3/21 (C32, CFPAC-1, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **1.51×** | +3.9 | 0.004 | 5/11 (Panc 03.27, NCI-H2347, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.48×** | +3.7 | 0.008 | 6/22 (NCI-H2347, A549, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.48×** | +3.4 | 0.020 | 2/18 (Hs 766T, CFPAC-1) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.42×** | +3.3 | 0.029 | 6/24 (Panc 03.27, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.61×** | +3.2 | 0.037 | 3/12 (CFPAC-1, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | **1.27×** | +3.1 | 0.043 | 4/23 (PANC-1, Panc 03.27, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9787.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (SNU-423 0.125×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (NCI-H1792 0.104×; ⚠ cell-cycle shift, would explain all of this change); [[Auranofin (drug)]] 5 µM in 1 line (LOX-IMVI 0.0576×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.659×** | -4.0 | 0.039 | 8/24 (AsPC-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[Vortioxetine (drug)]] 0.5 µM |  | 0.707× | -3.3 | 0.17 | 2/23 (CFPAC-1, A549) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 0.5 µM |  | 0.712× | -3.2 | 0.17 | 7/21 (C32, AsPC-1, …) | inconsistent across doses | position effect removed |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.714× | -3.2 | 0.17 | 6/19 (LOX-IMVI, C32, …) | rises with dose |  |
| [[TAK-733 (drug)]] 0.05 µM |  | 0.705× | -3.2 | 0.18 | 1/24 (PANC-1) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.60 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9787. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 7.28 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.97× (z +11.1) | — |
| [[HOP62 (line)]] | alt | 3.42 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 16.8× (z +8.7) | — |
| [[LOX-IMVI (line)]] | wt | 2.90 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0576× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 16.2 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.104× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 12.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.20× (z +8.7) | — |
| [[SNU-423 (line)]] | alt | 14.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.125× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 3.14 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 20.7× (z +8.5) | — |
| [[A-172 (line)]] | wt | 0.733 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.303 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.549 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.322 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.290 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.326 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.657 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.314 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 80.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.767 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.501 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.653 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.700 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.473 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.864 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.762 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.288 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.268 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.420 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.678 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9787), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SGK1]] | +0.67 | +0.61 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[NEDD9]] | +0.66 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[PLK2]] | +0.58 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[LINC00540]] | +0.57 | +0.34 / +0.48 | both halves | 1e-04 |  |
| [[MYO1E]] | +0.56 | +0.36 / +0.52 | both halves | 1e-04 |  |
| [[SERPINB1]] | +0.54 | +0.38 / +0.52 | both halves | 6e-05 |  |
| [[PHLDB2]] | +0.54 | +0.46 / +0.58 | both halves | 2e-05 |  |
| [[TRIB1]] | +0.54 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[EPAS1]] | +0.53 | +0.44 / +0.48 | both halves | 3e-05 |  |
| [[TIPARP]] | +0.53 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[CCN1]] | +0.52 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[LMCD1]] | +0.52 | +0.54 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPALPP1]] | -0.56 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[C8orf44-SGK3]] | -0.49 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[LAMTOR5-AS1]] | -0.49 | -0.28 / -0.40 | both halves | 3e-04 |  |
| [[TRAPPC13]] | -0.47 | -0.41 / -0.37 | both halves | 8e-05 |  |
| [[VPS33A]] | -0.47 | -0.32 / -0.50 | both halves | 2e-04 |  |
| [[PAAF1]] | -0.47 | -0.31 / -0.43 | both halves | 2e-04 |  |
| [[PEX6]] | -0.46 | -0.29 / -0.41 | both halves | 3e-04 |  |
| [[BCL2L2-PABPN1]] | -0.46 | -0.38 / -0.41 | both halves | 7e-05 |  |
| [[TAS2R4]] | -0.46 | -0.23 / -0.34 | both halves | 5e-04 | pathway: GPCR ligand binding |
| [[VPS13B-DT]] | -0.46 | -0.37 / -0.34 | both halves | 1e-04 |  |
| [[GARS1-DT]] | -0.45 | -0.29 / -0.45 | both halves | 2e-04 |  |
| [[SSBP1]] | -0.44 | -0.30 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TSPAN2]] | B | TSPAN2 activity raises ADRB2's level | lines that do not express TSPAN2 (19) vs lines expressing it (31) | 1.86× lower at baseline in the lines without TSPAN2 | 0.025 | ⚠ within organs, on part of the lines; also absent: SAA1, STK32A, IFI44L |
| [[GPRC5A]] | B | GPRC5A activity raises ADRB2's level | lines that do not express GPRC5A (12) vs lines expressing it (38) | 2.22× lower at baseline in the lines without GPRC5A | 0.056 | ⚠ within organs, on part of the lines; also absent: TESMIN, PSORS1C1, ITGA3 |
| [[VSIR]] | B | VSIR activity raises ADRB2's level | lines that do not express VSIR (14) vs lines expressing it (36) | 2.07× lower at baseline in the lines without VSIR | 0.064 | ⚠ within organs, on part of the lines; also absent: PLAAT4, NEURL3, SEPTIN9-DT; maybe low, not absent |
| [[MET]] | B | MET activity raises ADRB2's level | lines that do not express MET (9) vs lines expressing it (41) | 1.88× lower at baseline in the lines without MET | 0.093 | ⚠ within organs, on part of the lines; also absent: TGFBR2, PHLDA2, VDR |
| [[NEDD9]] | B | NEDD9 activity raises ADRB2's level | lines that do not express NEDD9 (16) vs lines expressing it (34) | 1.67× lower at baseline in the lines without NEDD9 | 0.094 | ⚠ within organs, on part of the lines; also absent: ITGA1, LGALS3, DGKG |
| [[TGM2]] | C | TGM2 activity raises ADRB2's level | lines that do not express TGM2 (16) vs lines expressing it (34) | 2.64× lower at baseline in the lines without TGM2 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: CCL20, SAA2, ALDH1A3; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VSIR]] | B | ADRB2 activity raises VSIR's level | lines that do not express ADRB2 (23) vs lines expressing it (27) | 2.08× lower at baseline in the lines without ADRB2 | 0.008 | ⚠ within organs, on part of the lines; also absent: GBP5, ADAMTS16, ENSG00000271933 |
| [[DUSP5]] | B | ADRB2 activity raises DUSP5's level | lines that do not express ADRB2 (23) vs lines expressing it (27) | 1.46× lower at baseline in the lines without ADRB2 | 0.042 | ⚠ within organs, on part of the lines; also absent: GBP5, ADAMTS16, ENSG00000271933 |
| [[UGCG]] | B | ADRB2 activity raises UGCG's level | lines that do not express ADRB2 (23) vs lines expressing it (27) | 1.64× lower at baseline in the lines without ADRB2 | 0.052 | ⚠ within organs, on part of the lines; also absent: GBP5, ADAMTS16, ENSG00000271933 |
| [[DUSP1]] | B | ADRB2 activity raises DUSP1's level | lines that do not express ADRB2 (23) vs lines expressing it (27) | 1.92× lower at baseline in the lines without ADRB2 | 0.097 | ⚠ within organs, on part of the lines; also absent: GBP5, ADAMTS16, ENSG00000271933 |

## Where it sits

- **Module**: [[Module 113]] — hypoxia; 43 genes; every member is in the + arm (projection on the module's main direction 0.558). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.2, 8.4); signed map (1.8, 23.8). **Vector** length 48.4, 9.60% of its response variance represented; |z| ≥ 3 in 676 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +17.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.6 | +7.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.3 | +21.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.2 | +21.9 |
|  | [[Belinostat (drug)]] 5 µM |  | +1.7 | +18.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.2 | +2.1 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.1 | +0.8 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.0 | +1.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.9 | +3.2 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -2.7 | -2.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -1.6 | -2.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.4 | -4.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.3 | -2.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -1.3 | -2.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.2 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | adrenoceptor beta 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q32 — chr5:148,826,611-148,828,623 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ADRBR, BAR, B2AR, ARB2; previously ADRB2R |
| Gene groups (HGNC) | Adrenoceptors |
| Reactome | 13 pathways, smallest: Adrenoceptors; Amine ligand-binding receptors; G alpha (s) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [P07550](https://www.uniprot.org/uniprotkb/P07550) (Beta-2 adrenergic receptor):

> G protein-coupled receptor for catecholamines that couples to both G(s) and G(i) proteins, activating bifurcated signaling pathways. ADRB2 binds epinephrine (Epi) with an approximately 30-fold greater affinity than norepinephrine (NE). In the heart, Epi- and NE-activated ADRB2 induces rapid and slow cardiomyocyte contraction rate, respectively (By similarity). Both NE and Epi promote coupling to G(s)/PKA pathway to regulate myocyte contraction rate (By similarity). Epi also promotes ADRB2 …

**Summary**, from NCBI Gene [154](https://www.ncbi.nlm.nih.gov/gene/154):

> This gene encodes beta-2-adrenergic receptor which is a member of the G protein-coupled receptor superfamily. This receptor is directly associated with one of its ultimate effectors, the class C L-type calcium channel Ca(V)1.2. This receptor-channel complex also contains a G protein, an adenylyl cyclase, cAMP-dependent kinase, and the counterbalancing phosphatase, PP2A. The assembly of the signaling complex provides a mechanism that ensures specific and rapid signaling by this G protein-coupled …

**Accessions** — [HGNC:286](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:286) · Entrez [154](https://www.ncbi.nlm.nih.gov/gene/154) · UniProt [P07550](https://www.uniprot.org/uniprotkb/P07550) · Ensembl [ENSG00000169252](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169252)

## Data

Gene col 9787: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9787); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9787, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9787]; `tensor/DDL_lfc|DDL_z.npy` [9787]; `embed/gene_vectors.npy` [9787]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9787 or target_col == 9787). Every well: [[ADRB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADRB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
