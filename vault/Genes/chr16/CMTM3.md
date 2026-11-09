---
symbol: "CMTM3"
type: "gene"
col: 6462
ensembl_id: "ENSG00000140931"
name: "CKLF like MARVEL transmembrane domain containing 3"
location: "16q22.1"
module: 147
arm: "+"
pooled_cpm: 13.78
n_lines_expressing: 39
n_dd_up: 4
n_dd_down: 30
n_dd_up_clean: 2
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 9
direction_downstream: 4
tags: ["gene", "module/147"]
generated_by: "tahoemap"
---

# CMTM3

*CKLF like MARVEL transmembrane domain containing 3* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.67× (z +6.1, q 5e-07, up in 16 of 22 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.39× (z +4.1, q 0.008, up in 15 of 37 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (A498 3.65×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.244× (z -17.4, q 0e+00, down in 34 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SVIL]] (+0.57, fdr 5e-05), [[LIMD2]] (+0.57, fdr 2e-05), [[FOXL1]] (+0.56, fdr 1e-05); moves opposite to [[SIDT1]] (-0.48, fdr 1e-04), [[PIK3C2B]] (-0.47, fdr 5e-05), [[PPP1R1B]] (-0.45, fdr 7e-05).
> It is in [[Module 147]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[NPNT]] → it (grade B ⚠); 4 go from it, the strongest it → [[NPNT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6462.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (A498 3.65×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.67×** | +6.1 | 5e-07 | 16/22 (A498, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.61×** | +5.9 | 1e-06 | 17/29 (SNU-423, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.39×** | +4.1 | 0.008 | 15/37 (A498, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.34×** | +3.4 | 0.082 | 10/36 (NCI-H460, BT-474, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.28× | +3.1 | 0.23 | 13/37 (A498, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6462.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.244×** | -17.4 | 0e+00 | 34/37 (A-172, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.265×** | -16.4 | 0e+00 | 33/37 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.425×** | -15.0 | 0e+00 | 29/35 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.358×** | -12.7 | 9e-35 | 32/36 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.554×** | -10.3 | 7e-23 | 23/35 (HepG2/C3A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.237×** | -9.2 | 5e-18 | 31/37 (PANC-1, NCI-H2030, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.485×** | -8.9 | 3e-17 | 23/37 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.527×** | -7.6 | 2e-12 | 22/37 (SW 900, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.593×** | -6.1 | 7e-08 | 22/37 (SK-MEL-2, A549, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.405×** | -5.8 | 5e-07 | 24/37 (J82, HS-578T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.617×** | -5.7 | 5e-07 | 20/36 (J82, MIA PaCa-2, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.662×** | -5.6 | 1e-06 | 20/37 (CFPAC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.667×** | -5.0 | 2e-05 | 19/36 (HOP62, Hs 766T, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.666×** | -4.8 | 5e-05 | 18/36 (A498, NCI-H460, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.772×** | -4.3 | 6e-04 | 17/37 (SW480, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.708×** | -4.3 | 7e-04 | 15/35 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.714×** | -4.2 | 0.001 | 16/36 (CFPAC-1, SW 1271, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6462. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 28.9 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.138× (z -13.3) |
| [[J82 (line)]] | alt | 19.9 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.178× (z -11.6) |
| [[NCI-H460 (line)]] | wt | 12.4 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -14.4) |
| [[RKO (line)]] | wt | 27.4 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.153× (z -12.0) |
| [[SW 900 (line)]] | alt | 16.9 | 0 | 4 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0660× (z -12.6) |
| [[SW480 (line)]] | alt | 10.7 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.127× (z -13.5) |
| [[CFPAC-1 (line)]] | alt | 26.0 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.148× (z -12.8) |
| [[HepG2_C3A (line)]] | wt | 42.4 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.210× (z -12.9) |
| [[HOP62 (line)]] | alt | 20.0 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.181× (z -12.7) |
| [[A-172 (line)]] | wt | 28.9 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.192× (z -13.0) |
| [[A498 (line)]] | wt | 14.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.65× (z +8.5) ⚠ toxic; transcription drop | [[Cobimetinib (drug)]] 5 µM 0.188× (z -10.9) |
| [[AsPC-1 (line)]] | alt | 10.2 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.163× (z -8.5) |
| [[Hs 766T (line)]] | wt | 30.2 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.167× (z -12.1) |
| [[LOX-IMVI (line)]] | wt | 15.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -12.6) |
| [[NCI-H1792 (line)]] | alt | 20.4 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -9.3) |
| [[PANC-1 (line)]] | alt | 15.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -11.3) |
| [[SK-MEL-2 (line)]] | alt | 13.9 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.116× (z -11.1) |
| [[BT-474 (line)]] | alt | 9.16 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -9.4) |
| [[C32 (line)]] | wt | 7.97 | 0 | 1 | — | [[Monocrotaline (drug)]] 0.05 µM 0.0891× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 43.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -13.8) |
| [[NCI-H23 (line)]] | alt | 11.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -8.7) |
| [[NCI-H2347 (line)]] | alt | 8.58 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -10.7) |
| [[Panc 03.27 (line)]] | alt | 9.85 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0531× (z -12.4) |
| [[A-427 (line)]] | wt | 7.65 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.02 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.61 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.07 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6462), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SVIL]] | +0.57 | +0.40 / +0.63 | both halves | 5e-05 |  |
| [[LIMD2]] | +0.57 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[FOXL1]] | +0.56 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[ELK3]] | +0.56 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[SPRY4]] | +0.54 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[LINC02454]] | +0.53 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[WIPF1]] | +0.53 | +0.62 / +0.42 | both halves | 4e-05 |  |
| [[TSPAN4]] | +0.53 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[RGS17]] | +0.51 | +0.63 / +0.40 | both halves | 5e-05 |  |
| [[PXN]] | +0.51 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[SLC35G2]] | +0.51 | +0.43 / +0.48 | both halves | 3e-05 |  |
| [[SPRY2]] | +0.51 | +0.38 / +0.55 | both halves | 7e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIDT1]] | -0.48 | -0.49 / -0.33 | both halves | 1e-04 |  |
| [[PIK3C2B]] | -0.47 | -0.53 / -0.39 | both halves | 5e-05 |  |
| [[PPP1R1B]] | -0.45 | -0.39 / -0.38 | both halves | 7e-05 |  |
| [[UGT1A1]] | -0.45 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[GPX2]] | -0.44 | -0.48 / -0.29 | both halves | 3e-04 |  |
| [[CREB3L1]] | -0.44 | -0.35 / -0.34 | both halves | 1e-04 |  |
| [[TFG]] | -0.44 | -0.24 / -0.43 | both halves | 4e-04 |  |
| [[ST6GALNAC1]] | -0.44 | -0.40 / -0.37 | both halves | 9e-05 |  |
| [[PRR15L]] | -0.43 | -0.47 / -0.27 | both halves | 3e-04 |  |
| [[BCL2L14]] | -0.43 | -0.55 / -0.31 | both halves | 2e-04 |  |
| [[GPA33]] | -0.43 | -0.42 / -0.32 | both halves | 1e-04 |  |
| [[FXYD3]] | -0.43 | -0.45 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NPNT]] | B | NPNT activity lowers CMTM3's level | lines that do not express NPNT (33) vs lines expressing it (17) | 3.47× higher at baseline in the lines without NPNT | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4 |
| [[PRR15L]] | B | PRR15L activity lowers CMTM3's level | lines that do not express PRR15L (38) vs lines expressing it (12) | 4.19× higher at baseline in the lines without PRR15L | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: TMEM30B, CDH17, ENSG00000267881 |
| [[FXYD3]] | B | FXYD3 activity lowers CMTM3's level | lines that do not express FXYD3 (34) vs lines expressing it (16) | 2.83× higher at baseline in the lines without FXYD3 | 0.011 | ⚠ within organs, on part of the lines; also absent: CEACAM6, TMEM30B, TMPRSS2 |
| [[ADD3]] | B | ADD3 activity lowers CMTM3's level | lines that do not express ADD3 (5) vs lines expressing it (45) | 1.45× higher at baseline in the lines without ADD3 | 0.032 | ⚠ within organs, on part of the lines; also absent: LINC02842, ADD3-AS1, WWC3 |
| [[GPA33]] | B | GPA33 activity lowers CMTM3's level | lines that do not express GPA33 (41) vs lines expressing it (9) | 3.40× higher at baseline in the lines without GPA33 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17 |
| [[LINC02331]] | B | LINC02331 activity lowers CMTM3's level | lines that do not express LINC02331 (30) vs lines expressing it (20) | 2.85× higher at baseline in the lines without LINC02331 | 0.076 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPS8L3, LCN2 |
| [[PPP1R1B]] | B | PPP1R1B activity lowers CMTM3's level | lines that do not express PPP1R1B (37) vs lines expressing it (13) | 2.70× higher at baseline in the lines without PPP1R1B | 0.076 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CEACAM5, NPSR1, CDH17 |
| [[CFTR]] | B | CFTR activity lowers CMTM3's level | lines that do not express CFTR (39) vs lines expressing it (11) | 2.29× higher at baseline in the lines without CFTR | 0.098 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CTSE, ENSG00000224322, ATP10B; maybe low, not absent |
| [[TSPAN4]] | C | TSPAN4 activity raises CMTM3's level | lines that do not express TSPAN4 (7) vs lines expressing it (43) | 4.65× lower at baseline in the lines without TSPAN4 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: TRPC1, EMP3, PXDC1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NPNT]] | B | CMTM3 activity lowers NPNT's level | lines that do not express CMTM3 (11) vs lines expressing it (39) | 7.07× higher at baseline in the lines without CMTM3 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: ZNF605, C2orf74, MAP1B |
| [[SLC35B4]] | B | CMTM3 activity raises SLC35B4's level | lines that do not express CMTM3 (11) vs lines expressing it (39) | 1.40× lower at baseline in the lines without CMTM3 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: ZNF605, C2orf74, MAP1B |
| [[LIMD2]] | B | CMTM3 activity raises LIMD2's level | lines that do not express CMTM3 (11) vs lines expressing it (39) | 2.36× lower at baseline in the lines without CMTM3 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: ZNF605, C2orf74, MAP1B |
| [[FHL3]] | B | CMTM3 activity raises FHL3's level | lines that do not express CMTM3 (11) vs lines expressing it (39) | 1.46× lower at baseline in the lines without CMTM3 | 0.088 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: ZNF605, C2orf74, MAP1B |

## Where it sits

- **Module**: [[Module 147]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.622). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (53.4, -0.9); signed map (10.7, 55.6). **Vector** length 74.1, 16.7% of its response variance represented; |z| ≥ 3 in 877 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +3.8 | +4.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | -1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +3.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +0.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +0.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +2.5 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.8 | +2.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.7 | +3.4 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -3.4 | -9.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.1 | -4.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.1 | -3.9 |
|  | [[Trametinib (drug)]] 5 µM |  | -3.0 | -5.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.0 | -4.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.7 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.7 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | CKLF like MARVEL transmembrane domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:66,603,874-66,613,892 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ31762, BNAS2; previously CKLFSF3 |
| Gene groups (HGNC) | CKLF like MARVEL transmembrane domain containing |
| Matched by | ensembl_id |

UniProt [Q96MX0](https://www.uniprot.org/uniprotkb/Q96MX0) carries no function annotation.

**Summary**, from NCBI Gene [123920](https://www.ncbi.nlm.nih.gov/gene/123920):

> This gene belongs to the chemokine-like factor gene superfamily, a novel family that is similar to the chemokine and the transmembrane 4 superfamilies of signaling molecules. This gene is one of several chemokine-like factor genes located in a cluster on chromosome 16. Alternatively spliced transcript variants containing different 5' UTRs, but encoding the same protein, have been identified. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:19174](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19174) · Entrez [123920](https://www.ncbi.nlm.nih.gov/gene/123920) · UniProt [Q96MX0](https://www.uniprot.org/uniprotkb/Q96MX0) · Ensembl [ENSG00000140931](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140931)

## Data

Gene col 6462: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6462); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6462, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6462]; `tensor/DDL_lfc|DDL_z.npy` [6462]; `embed/gene_vectors.npy` [6462]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6462 or target_col == 6462). Every well: [[CMTM3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CMTM3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
