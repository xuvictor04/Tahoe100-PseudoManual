---
symbol: "BLMH"
type: "gene"
col: 2968
ensembl_id: "ENSG00000108578"
name: "bleomycin hydrolase"
location: "17q11.2"
module: 57
arm: "+"
pooled_cpm: 26.75
n_lines_expressing: 48
n_dd_up: 27
n_dd_down: 1
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# BLMH

*bleomycin hydrolase* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (17 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 2.70× (z +20.2, q 0e+00, up in 45 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.785× (z -6.9, q 2e-09, down in 25 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (SK-MEL-2 0.157×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (PANC-1 0.588×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HSD17B4]] (+0.74, fdr 7e-06), [[GNPDA2]] (+0.71, fdr 7e-06), [[VWA8]] (+0.70, fdr 7e-06); moves opposite to [[THUMPD3-AS1]] (-0.62, fdr 1e-05), [[EP300]] (-0.61, fdr 3e-05), [[RSPRY1]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LRP3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 20 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2968.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.70×** | +20.2 | 0e+00 | 45/45 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.46×** | +18.3 | 0e+00 | 45/46 (PANC-1, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.34×** | +16.3 | 0e+00 | 43/46 (PANC-1, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.91×** | +12.6 | 3e-34 | 35/45 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.53×** | +8.6 | 9e-16 | 31/45 (HEC-1-A, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.51×** | +8.4 | 4e-15 | 33/46 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **1.49×** | +7.8 | 6e-13 | 18/34 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.46×** | +7.7 | 8e-13 | 33/46 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.98×** | +7.3 | 2e-11 | 29/41 (PANC-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.45×** | +7.3 | 2e-11 | 26/46 (PANC-1, LoVo, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.62×** | +7.0 | 2e-10 | 33/46 (PANC-1, COLO 205, …) | all doses, flat | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.35×** | +6.1 | 4e-08 | 20/46 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.35×** | +6.1 | 4e-08 | 23/46 (BT-474, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change | **1.32×** | +5.7 | 5e-07 | 19/42 (A-172, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.22×** | +5.6 | 6e-07 | 18/46 (PANC-1, NCI-H2030, …) | rises with dose | composition shift |
| [[venetoclax (drug)]] 5 µM |  | **1.67×** | +5.4 | 2e-06 | 20/44 (HEC-1-A, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.24×** | +4.4 | 3e-04 | 17/46 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.49×** | +4.2 | 5e-04 | 13/45 (NCI-H460, NCI-H2030, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.49×** | +4.2 | 6e-04 | 8/46 (HEC-1-A, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.13× | +3.6 | 0.007 | 12/46 (NCI-H2030, NCI-H1573, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.19× | +3.5 | 0.011 | 7/46 (LOX-IMVI, C32, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.26×** | +3.4 | 0.015 | 6/46 (HEC-1-A, NCI-H2347, …) | two highest doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.36×** | +3.2 | 0.023 | 13/45 (NCI-H460, J82, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2968.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (SK-MEL-2 0.157×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (PANC-1 0.588×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.785×** | -6.9 | 2e-09 | 25/46 (PANC-1, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.907× | -6.8 | 2e-09 | 5/46 (SNU-423, HCT15, …) | inconsistent across doses |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 0.836× | -3.5 | 0.080 | 11/46 (A549, NCI-H1792, …) | top dose only | plate-row cell shift |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 0.844× | -3.4 | 0.080 | 7/45 (A549, A498, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.846× | -3.4 | 0.080 | 14/45 (AsPC-1, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.853× | -3.1 | 0.18 | 12/45 (SW 1271, A549, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2968. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 33.8 | 6 (2 ⚠) | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 3.73× (z +15.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.588× (z -9.0) |
| [[A-427 (line)]] | wt | 45.7 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.69× (z +9.6) | — |
| [[SW480 (line)]] | alt | 23.0 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.24× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.07× (z +10.7) | — |
| [[HOP62 (line)]] | alt | 29.0 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.06× (z +10.0) | — |
| [[LOX-IMVI (line)]] | wt | 41.1 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.85× (z +9.8) | — |
| [[A549 (line)]] | wt | 37.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +9.0) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[COLO 205 (line)]] | alt | 8.81 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 11.9× (z +9.2) | — |
| [[LoVo (line)]] | wt | 12.9 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 4.02× (z +9.0) ⚠ toxic | — |
| [[NCI-H1792 (line)]] | alt | 25.0 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.73× (z +8.5) ⚠ toxic | — |
| [[NCI-H2030 (line)]] | alt | 18.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +11.2) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[NCI-H460 (line)]] | wt | 31.6 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.17× (z +11.0) ⚠ toxic | — |
| [[SK-MEL-2 (line)]] | alt | 27.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.157× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change |
| [[A-172 (line)]] | wt | 43.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 52.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.49 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 40.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.25 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 39.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 39.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2968), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSD17B4]] | +0.74 | +0.72 / +0.69 | both halves | 7e-06 |  |
| [[GNPDA2]] | +0.71 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[VWA8]] | +0.70 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[NXPE3]] | +0.67 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[GRHPR]] | +0.67 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[PPP5C]] | +0.67 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[NAA16]] | +0.65 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[HSF2]] | +0.65 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[NSFL1C]] | +0.65 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[RAD23B]] | +0.65 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[PHKB]] | +0.64 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[GSR]] | +0.63 | +0.66 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THUMPD3-AS1]] | -0.62 | -0.50 / -0.62 | both halves | 1e-05 |  |
| [[EP300]] | -0.61 | -0.66 / -0.46 | both halves | 3e-05 |  |
| [[RSPRY1]] | -0.59 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[CATSPERG]] | -0.58 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[LINC01004]] | -0.58 | -0.46 / -0.63 | both halves | 2e-05 |  |
| [[HERPUD2]] | -0.57 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[C21orf91-OT1]] | -0.57 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[TOB2]] | -0.57 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[RSL1D1-DT]] | -0.56 | -0.60 / -0.34 | both halves | 1e-04 |  |
| [[TNRC6C]] | -0.56 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[BOLA1]] | -0.56 | -0.36 / -0.55 | both halves | 1e-04 |  |
| [[PLA2G12B]] | -0.55 | -0.45 / -0.53 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRP3]] | B | LRP3 activity raises BLMH's level | lines that do not express LRP3 (7) vs lines expressing it (43) | 2.72× lower at baseline in the lines without LRP3 | 0.033 | ⚠ within organs, on part of the lines; also absent: ACBD7, SNTA1, TMCC2; maybe low, not absent |
| [[SYTL4]] | B | SYTL4 activity lowers BLMH's level | lines that do not express SYTL4 (10) vs lines expressing it (40) | 1.69× higher at baseline in the lines without SYTL4 | 0.041 | ⚠ within organs, on part of the lines; also absent: PTPRE, PLEKHA6 |
| [[ANXA6]] | B | ANXA6 activity raises BLMH's level | lines that do not express ANXA6 (8) vs lines expressing it (42) | 2.37× lower at baseline in the lines without ANXA6 | 0.057 | ⚠ within organs, on part of the lines; also absent: KATNAL1, PHC1, FAM171A1 |
| [[SOAT1]] | C | SOAT1 activity raises BLMH's level | lines that do not express SOAT1 (3) vs lines expressing it (47) | 3.04× lower at baseline in the lines without SOAT1 | 0.046 | ⚠ few lines (3 vs 47); across organs; also absent: NKAIN1, CEP85L, CFL2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.547). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-20.4, -7.6); signed map (-27.8, -21.5). **Vector** length 84.1, 17.3% of its response variance represented; |z| ≥ 3 in 941 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +7.8 | +20.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.0 | +18.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.8 | +16.3 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +4.4 | +7.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.2 | +12.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.1 | +7.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | +3.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.9 | +2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.6 | +4.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.8 | -6.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -0.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -0.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -2.4 | +6.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.6 | -1.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -2.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.2 | -2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.2 | +2.4 |

## What is on record

|  |  |
|---|---|
| Name | bleomycin hydrolase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:30,248,203-30,292,056 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BH |
| Gene groups (HGNC) | Peptidase family C1; Cysteine endopeptidases |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13867](https://www.uniprot.org/uniprotkb/Q13867) (Bleomycin hydrolase):

> The normal physiological role of BLM hydrolase is unknown, but it catalyzes the inactivation of the antitumor drug BLM (a glycopeptide) by hydrolyzing the carboxamide bond of its B-aminoalaninamide moiety thus protecting normal and malignant cells from BLM toxicity.

**Summary**, from NCBI Gene [642](https://www.ncbi.nlm.nih.gov/gene/642):

> Bleomycin hydrolase (BMH) is a cytoplasmic cysteine peptidase that is highly conserved through evolution; however, the only known activity of the enzyme is metabolic inactivation of the glycopeptide bleomycin (BLM), an essential component of combination chemotherapy regimens for cancer. The protein contains the signature active site residues of the cysteine protease papain superfamily. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:1059](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1059) · Entrez [642](https://www.ncbi.nlm.nih.gov/gene/642) · UniProt [Q13867](https://www.uniprot.org/uniprotkb/Q13867) · Ensembl [ENSG00000108578](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108578)

## Data

Gene col 2968: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2968); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2968, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2968]; `tensor/DDL_lfc|DDL_z.npy` [2968]; `embed/gene_vectors.npy` [2968]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2968 or target_col == 2968). Every well: [[BLMH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BLMH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
