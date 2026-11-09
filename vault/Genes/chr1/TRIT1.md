---
symbol: "TRIT1"
type: "gene"
col: 496
ensembl_id: "ENSG00000043514"
name: "tRNA isopentenyltransferase 1"
location: "1p34.2"
module: 17
arm: "+"
pooled_cpm: 50.49
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 9
n_dd_up_clean: 4
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# TRIT1

*tRNA isopentenyltransferase 1* — 1p34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.28× (z +6.0, q 9e-07, up in 36 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.414× (z -11.9, q 1e-29, down in 35 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.685× (z -7.3, q 6e-11, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALG9]] (+0.73, fdr 7e-06), [[FAM234B]] (+0.72, fdr 7e-06), [[PMS2P3-1]] (+0.72, fdr 7e-06); moves opposite to [[TJP1]] (-0.61, fdr 1e-05), [[DDX5]] (-0.60, fdr 1e-05), [[SKIL]] (-0.59, fdr 3e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 496.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.28×** | +6.0 | 9e-07 | 36/49 (RKO, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.08×** | +5.4 | 2e-05 | 32/48 (RKO, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.45×** | +5.2 | 5e-05 | 34/48 (A498, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.36×** | +4.3 | 0.002 | 23/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.33×** | +4.0 | 0.007 | 25/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.30×** | +3.6 | 0.027 | 22/48 (LoVo, SW480, …) | top dose only |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 1.19× | +3.3 | 0.083 | 12/48 (A498, NCI-H23, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | 1.55× | +3.2 | 0.10 | 22/48 (AsPC-1, RPMI-7951, …) | rises with dose | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | 1.25× | +3.1 | 0.12 | 19/48 (HT-29, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | 1.41× | +3.1 | 0.13 | 14/48 (HS-578T, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 496.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.414×** | -11.9 | 1e-29 | 35/43 (SW48, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.460×** | -10.9 | 5e-25 | 40/47 (NCI-H23, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.685×** | -7.3 | 6e-11 | 31/48 (SK-MEL-2, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.677×** | -5.3 | 2e-05 | 27/48 (PANC-1, C32, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.701×** | -4.6 | 5e-04 | 27/45 (RKO, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.723×** | -4.4 | 0.001 | 28/50 (C32, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.744×** | -4.0 | 0.006 | 25/48 (H4, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.770×** | -3.7 | 0.018 | 23/48 (A-172, LOX-IMVI, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~20% of this change | **0.785×** | -3.3 | 0.070 | 21/47 (C-33 A, C32, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | 0.848× | -3.1 | 0.095 | 19/48 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Apalutamide (drug)]] 0.5 µM |  | 0.802× | -3.1 | 0.10 | 20/48 (NCI-H1792, HOP62, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.804× | -3.1 | 0.10 | 15/48 (NCI-H2347, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 496. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 89.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.208× (z -11.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 64.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -10.4) ⚠ cell-cycle shift, explains ~98% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.336× (z -8.5) |
| [[J82 (line)]] | alt | 44.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -12.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 66.1 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.29× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.417× (z -9.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 68.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.291× (z -9.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 70.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.298× (z -9.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 60.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -10.0) |
| [[NCI-H2347 (line)]] | alt | 49.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.263× (z -10.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 51.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.36× (z +9.1) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 5 µM 0.360× (z -10.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SK-MEL-2 (line)]] | alt | 58.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.148× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -10.3) |
| [[SNU-423 (line)]] | alt | 50.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -12.4) ⚠ cell-cycle shift, explains ~98% of this change |
| [[SW48 (line)]] | wt | 76.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0850× (z -16.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 47.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -9.0) |
| [[A-427 (line)]] | wt | 42.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +9.4) ⚠ cell-cycle shift, explains ~98% of this change | — |
| [[COLO 205 (line)]] | alt | 33.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -10.4) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 75.1 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.176× (z -9.4) |
| [[HEC-1-A (line)]] | alt | 63.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.303× (z -10.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 26.6 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.227× (z -8.7) |
| [[Hs 766T (line)]] | wt | 45.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.273× (z -8.7) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 39.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -8.7) ⚠ cell-cycle shift, explains ~98% of this change |
| [[LoVo (line)]] | wt | 35.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.388× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 42.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.115× (z -16.1) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 55.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.179× (z -12.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 47.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.340× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 72.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0937× (z -23.7) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 43.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.529× (z -9.0) ⚠ cell-cycle shift, explains ~98% of this change |
| [[RKO (line)]] | wt | 49.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.204× (z -12.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 61.7 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.305× (z -11.3) |
| [[A498 (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 32.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 79.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 53.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 86.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 76.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 59.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 56.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 63.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 496), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALG9]] | +0.73 | +0.81 / +0.60 | both halves | 7e-06 |  |
| [[FAM234B]] | +0.72 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[PMS2P3-1]] | +0.72 | +0.76 / +0.64 | both halves | 7e-06 |  |
| [[ARL6]] | +0.72 | +0.76 / +0.66 | both halves | 7e-06 |  |
| [[PMS2P3]] | +0.71 | +0.75 / +0.61 | both halves | 7e-06 |  |
| [[SNAPC3]] | +0.69 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[HDHD5]] | +0.68 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[HEATR6]] | +0.68 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[MMS19]] | +0.67 | +0.77 / +0.51 | both halves | 1e-05 |  |
| [[ATPAF2]] | +0.67 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[PEX3]] | +0.67 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[SNRPA1]] | +0.67 | +0.71 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TJP1]] | -0.61 | -0.51 / -0.66 | both halves | 1e-05 |  |
| [[DDX5]] | -0.60 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[SKIL]] | -0.59 | -0.67 / -0.45 | both halves | 3e-05 |  |
| [[SVIL]] | -0.59 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[HIVEP2-DT]] | -0.59 | -0.65 / -0.48 | both halves | 2e-05 |  |
| [[MSRA]] | -0.59 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[C6orf62]] | -0.58 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[GARIN1A]] | -0.56 | -0.52 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises TRIT1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[GSTA4]] | B | GSTA4 activity raises TRIT1's level | lines that do not express GSTA4 (5) vs lines expressing it (45) | 1.39× lower at baseline in the lines without GSTA4 | 0.092 | ⚠ within organs, on part of the lines; also absent: PHGDH, P3H3; maybe low, not absent |
| [[HACE1]] | C | HACE1 activity raises TRIT1's level | lines that do not express HACE1 (3) vs lines expressing it (47) | 2.01× lower at baseline in the lines without HACE1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AXDND1, CFL2, ATP6V1E2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.554). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-3.9, -13.0); signed map (-33.3, -9.0). **Vector** length 109, 31.6% of its response variance represented; |z| ≥ 3 in 810 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +5.5 | +2.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.8 | +0.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.7 | +1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.5 | +3.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.3 | +2.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.5 | +3.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +3.1 | +2.6 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -7.8 | -5.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~98% of this change | -6.7 | -2.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.7 | -7.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~20% of this change | -3.2 | -3.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | +0.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.8 | -1.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.5 | -1.6 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.3 | -0.1 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.3 | -3.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.2 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | tRNA isopentenyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.2 — chr1:39,838,110-39,883,511 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20061, IPT |
| Gene groups (HGNC) | Zinc fingers matrin-type |
| Reactome | 4 pathways, smallest: tRNA modification in the mitochondrion; tRNA modification in the nucleus and cytosol; tRNA processing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H3H1](https://www.uniprot.org/uniprotkb/Q9H3H1) (tRNA dimethylallyltransferase):

> Catalyzes the transfer of a dimethylallyl group onto the adenine at position 37 of both cytosolic and mitochondrial tRNAs, leading to the formation of N6-(dimethylallyl)adenosine (i6A37). Mediates modification of a limited subset of tRNAs: tRNA(Ser)(AGA), tRNA(Ser)(CGA), tRNA(Ser)(UGA), as well as partial modification of the selenocysteine tRNA(Ser)(UCA). TRIT1 is therefore required for selenoprotein expression.

**Summary**, from NCBI Gene [54802](https://www.ncbi.nlm.nih.gov/gene/54802):

> This gene encodes a protein that that is targeted to the mitochondrion and modifies transfer RNAs (tRNAs) by adding a dimethylallyl group onto the adenine at position 37. This modification is important for maintaining the correct reading frame during protein translation. This gene is considered a tumor suppressor and its expression can decrease cell growth. Alternative splicing results in multiple transcripts variants, most of which are likely non-functional. [provided by RefSeq, Aug 2015]

**Accessions** — [HGNC:20286](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20286) · Entrez [54802](https://www.ncbi.nlm.nih.gov/gene/54802) · UniProt [Q9H3H1](https://www.uniprot.org/uniprotkb/Q9H3H1) · Ensembl [ENSG00000043514](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000043514)

## Data

Gene col 496: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 496); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 496, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 496]; `tensor/DDL_lfc|DDL_z.npy` [496]; `embed/gene_vectors.npy` [496]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 496 or target_col == 496). Every well: [[TRIT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
