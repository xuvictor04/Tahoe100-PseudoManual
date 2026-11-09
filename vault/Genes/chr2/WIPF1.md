---
symbol: "WIPF1"
type: "gene"
col: 3738
ensembl_id: "ENSG00000115935"
name: "WAS/WASL interacting protein family member 1"
location: "2q31.1"
module: 13
arm: "+"
pooled_cpm: 49.94
n_lines_expressing: 34
n_dd_up: 0
n_dd_down: 31
n_dd_up_clean: 0
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 26
direction_downstream: 9
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# WIPF1

*WAS/WASL interacting protein family member 1* — 2q31.1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.212× (z -43.0, q 0e+00, down in 31 of 32 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CNRIP1]] (+0.55, fdr 4e-05), [[CMTM3]] (+0.53, fdr 4e-05), [[TSHZ3-AS1]] (+0.52, fdr 4e-05); moves opposite to [[DLEU1]] (-0.59, fdr 9e-06), [[PRR15L]] (-0.54, fdr 3e-05), [[UGT1A9]] (-0.51, fdr 4e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 26 arrows point to it, the strongest [[FLI1]] → it (grade B ⚠); 9 go from it, the strongest it → [[SLC35G2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3738.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Rapamycin (drug)]] 5 µM |  | 1.16× | +4.2 | 0.012 | 13/32 (NCI-H460, J82, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.5 | 0.089 | 12/32 (A-427, NCI-H1792, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 0.5 µM |  | 1.19× | +3.5 | 0.089 | 12/32 (NCI-H460, H4, …) | rises with dose |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 1.18× | +3.2 | 0.19 | 4/32 (A549, SK-MEL-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3738.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.212×** | -43.0 | 0e+00 | 31/32 (J82, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.385×** | -18.7 | 0e+00 | 31/32 (A-172, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.386×** | -18.6 | 0e+00 | 31/32 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.409×** | -17.5 | 0e+00 | 30/32 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.416×** | -17.2 | 0e+00 | 30/32 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.393×** | -15.4 | 0e+00 | 26/32 (NCI-H460, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.249×** | -14.3 | 3e-44 | 26/32 (A-427, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.272×** | -13.3 | 9e-39 | 28/33 (HOP62, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.699×** | -9.9 | 3e-21 | 20/32 (HS-578T, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.620×** | -9.3 | 5e-19 | 22/32 (NCI-H23, J82, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.602×** | -8.4 | 3e-15 | 24/31 (J82, NCI-H23, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.661×** | -8.1 | 2e-14 | 20/32 (J82, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.714×** | -6.6 | 2e-09 | 20/32 (NCI-H460, A549, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.717×** | -6.5 | 4e-09 | 17/32 (NCI-H23, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.727×** | -6.2 | 2e-08 | 18/32 (A549, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.728×** | -6.2 | 2e-08 | 22/32 (NCI-H460, SK-MEL-2, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.768×** | -5.1 | 9e-06 | 18/32 (A-172, C32, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.787×** | -4.7 | 9e-05 | 16/32 (A-172, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.655×** | -4.3 | 4e-04 | 13/33 (J82, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.809×** | -4.1 | 9e-04 | 13/32 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.825×** | -3.5 | 0.009 | 14/32 (C32, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3738. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 63.5 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0955× (z -37.4) |
| [[A-172 (line)]] | wt | 145 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -32.5) |
| [[C32 (line)]] | wt | 119 | 0 | 10 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.177× (z -14.6) |
| [[SK-MEL-2 (line)]] | alt | 149 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -26.9) |
| [[HOP62 (line)]] | alt | 124 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -36.6) |
| [[NCI-H23 (line)]] | alt | 49.6 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -19.7) |
| [[NCI-H460 (line)]] | wt | 57.2 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -30.5) |
| [[Panc 03.27 (line)]] | alt | 57.8 | 0 | 9 | — | [[Homoharringtonine (drug)]] 5 µM 0.0727× (z -37.1) |
| [[A549 (line)]] | wt | 86.0 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -27.6) |
| [[LOX-IMVI (line)]] | wt | 136 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -23.0) |
| [[NCI-H2030 (line)]] | alt | 145 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -19.8) |
| [[PANC-1 (line)]] | alt | 40.7 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -22.5) |
| [[HS-578T (line)]] | alt | 83.7 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -19.9) |
| [[RPMI-7951 (line)]] | alt | 156 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -29.0) |
| [[A-427 (line)]] | wt | 37.8 | 0 | 4 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0421× (z -15.0) |
| [[NCI-H1792 (line)]] | alt | 98.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -21.3) |
| [[SW480 (line)]] | alt | 50.9 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.158× (z -18.7) |
| [[hTERT-HPNE (line)]] | wt | 109 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -21.5) |
| [[NCI-H2347 (line)]] | alt | 29.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -15.2) |
| [[SW 1271 (line)]] | alt | 108 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -13.5) |
| [[SW 900 (line)]] | alt | 98.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -12.7) |
| [[NCI-H1573 (line)]] | alt | 13.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -11.5) |
| [[SNU-423 (line)]] | alt | 25.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -20.2) |
| [[SW1417 (line)]] | alt | 22.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -14.7) |
| [[C-33 A (line)]] | alt | 26.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.146× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[CFPAC-1 (line)]] | alt | 25.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -15.9) |
| [[H4 (line)]] | wt | 81.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -13.6) |
| [[SW 1088 (line)]] | alt | 83.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -9.1) |
| [[A498 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.05 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.38 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.45 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 51.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.05 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.40 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.20 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.55 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.52 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.97 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.92 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.83 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.77 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.36 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.33 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.98 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3738), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNRIP1]] | +0.55 | +0.60 / +0.42 | both halves | 4e-05 |  |
| [[CMTM3]] | +0.53 | +0.62 / +0.42 | both halves | 4e-05 |  |
| [[TSHZ3-AS1]] | +0.52 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[NAV1]] | +0.51 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[DNAAF9]] | +0.51 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[FLI1]] | +0.51 | +0.58 / +0.40 | both halves | 5e-05 | STRING 429 |
| [[WNT5B]] | +0.51 | +0.46 / +0.52 | both halves | 2e-05 |  |
| [[NINL]] | +0.51 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[ARHGAP22]] | +0.51 | +0.57 / +0.50 | both halves | 1e-05 | pathway: CDC42 GTPase cycle |
| [[TSHZ3]] | +0.50 | +0.58 / +0.46 | both halves | 3e-05 |  |
| [[KHDC1-AS1]] | +0.50 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[HS3ST3A1]] | +0.50 | +0.49 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DLEU1]] | -0.59 | -0.57 / -0.58 | both halves | 9e-06 |  |
| [[PRR15L]] | -0.54 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[UGT1A9]] | -0.51 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[RORC]] | -0.50 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[UGT1A8]] | -0.50 | -0.51 / -0.38 | both halves | 6e-05 |  |
| [[PRR15]] | -0.49 | -0.56 / -0.38 | both halves | 6e-05 |  |
| [[PRR15-DT]] | -0.49 | -0.49 / -0.39 | both halves | 6e-05 |  |
| [[PIK3C2B]] | -0.48 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[FAAH2]] | -0.47 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[SORL1]] | -0.47 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[TMEM125]] | -0.46 | -0.50 / -0.34 | both halves | 1e-04 |  |
| [[MGC32805]] | -0.46 | -0.49 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 9, C 17. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FLI1]] | B | FLI1 activity raises WIPF1's level | lines that do not express FLI1 (31) vs lines expressing it (19) | 4.32× lower at baseline in the lines without FLI1 | 0.019 | ⚠ within organs, on part of the lines; also absent: GYPC, PLPP4, LINC01615 |
| [[C4BPB]] | B | C4BPB activity lowers WIPF1's level | lines that do not express C4BPB (37) vs lines expressing it (13) | 4.72× higher at baseline in the lines without C4BPB | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, LINC02964, REG4 |
| [[ITGB3]] | B | ITGB3 activity raises WIPF1's level | lines that do not express ITGB3 (25) vs lines expressing it (25) | 3.43× lower at baseline in the lines without ITGB3 | 0.030 | ⚠ within organs, on part of the lines; also absent: ENSG00000259753, BICC1, ENSG00000291130 |
| [[HS3ST3A1]] | B | HS3ST3A1 activity raises WIPF1's level | lines that do not express HS3ST3A1 (33) vs lines expressing it (17) | 4.61× lower at baseline in the lines without HS3ST3A1 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000224865, CDH13, COL19A1 |
| [[PRR15L]] | B | PRR15L activity lowers WIPF1's level | lines that do not express PRR15L (38) vs lines expressing it (12) | 4.14× higher at baseline in the lines without PRR15L | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: TMEM30B, CDH17, ENSG00000267881 |
| [[TTC7B]] | B | TTC7B activity raises WIPF1's level | lines that do not express TTC7B (9) vs lines expressing it (41) | 6.07× lower at baseline in the lines without TTC7B | 0.068 | ⚠ within organs, on part of the lines; also absent: SYNGR1, HDGFL3, HLTF |
| [[PAPPA]] | B | PAPPA activity raises WIPF1's level | lines that do not express PAPPA (33) vs lines expressing it (17) | 4.64× lower at baseline in the lines without PAPPA | 0.070 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HTRA3, MSC-AS1, PDGFRB |
| [[FAM20C]] | B | FAM20C activity raises WIPF1's level | lines that do not express FAM20C (19) vs lines expressing it (31) | 3.14× lower at baseline in the lines without FAM20C | 0.079 | ⚠ within organs, on part of the lines; also absent: TUB, S1PR3, FHL1 |
| [[RORC]] | B | RORC activity weakens WIPF1's drug response | lines that do not express RORC (23) vs lines expressing it (10) | the lines without RORC respond 1.49× as strongly (z diff -1.59); strongest at PH-797804 5 µM: 0.25x vs 0.47x (z diff -3.0) | 0.096 | ⚠ within organs, on part of the lines; also absent: LRG1, LINC03040, ATP2C2; target measured in part of the lines; artifact flags |
| [[BVES]] | C | BVES activity raises WIPF1's level | lines that do not express BVES (19) vs lines expressing it (31) | 8.59× lower at baseline in the lines without BVES | 0.002 | ⚠ within organs, on part of the lines; also absent: MPDZ, BVES-AS1, DPY19L2; co-absent with the target |
| [[GNB4]] | C | GNB4 activity raises WIPF1's level | lines that do not express GNB4 (18) vs lines expressing it (32) | 8.27× lower at baseline in the lines without GNB4 | 0.004 | ⚠ within organs, on part of the lines; also absent: MPDZ, BVES, BVES-AS1; co-absent with the target |
| [[MRC2]] | C | MRC2 activity raises WIPF1's level | lines that do not express MRC2 (17) vs lines expressing it (33) | 6.01× lower at baseline in the lines without MRC2 | 0.009 | ⚠ within organs, on part of the lines; also absent: FBXO17, ENSG00000269547, FSD1; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 3, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC35G2]] | B | WIPF1 activity raises SLC35G2's level | lines that do not express WIPF1 (16) vs lines expressing it (34) | 3.49× lower at baseline in the lines without WIPF1 | 0.018 | ⚠ within organs, on part of the lines; also absent: BVES-AS1, GNB4, POPDC3 |
| [[UBASH3B]] | B | WIPF1 activity raises UBASH3B's level | lines that do not express WIPF1 (16) vs lines expressing it (34) | 1.52× lower at baseline in the lines without WIPF1 | 0.082 | ⚠ within organs, on part of the lines; also absent: BVES-AS1, GNB4, POPDC3 |
| [[C4BPB]] | B | WIPF1 activity lowers C4BPB's level | lines that do not express WIPF1 (16) vs lines expressing it (34) | 3.95× higher at baseline in the lines without WIPF1 | 0.088 | ⚠ within organs, on part of the lines; also absent: BVES-AS1, GNB4, POPDC3 |
| [[GNB4]] | C | WIPF1 activity raises GNB4's level | lines that do not express WIPF1 (16) vs lines expressing it (34) | 10.43× lower at baseline in the lines without WIPF1 | 0.026 | ⚠ within organs, on part of the lines; also absent: BVES-AS1, GNB4, POPDC3; co-absent with the target |
| [[LOXL1-AS1]] | C | WIPF1 activity raises LOXL1-AS1's level | lines that do not express WIPF1 (16) vs lines expressing it (34) | 2.27× lower at baseline in the lines without WIPF1 | 0.029 | ⚠ within organs, on part of the lines; also absent: BVES-AS1, GNB4, POPDC3; co-absent with the target |
| [[BVES]] | C | WIPF1 activity raises BVES's level | lines that do not express WIPF1 (16) vs lines expressing it (34) | 4.42× lower at baseline in the lines without WIPF1 | 0.049 | ⚠ within organs, on part of the lines; also absent: BVES-AS1, GNB4, POPDC3; co-absent with the target |
| [[KHDC1-AS1]] | C | WIPF1 activity raises KHDC1-AS1's level | lines that do not express WIPF1 (16) vs lines expressing it (34) | 2.47× lower at baseline in the lines without WIPF1 | 0.057 | ⚠ within organs, on part of the lines; also absent: BVES-AS1, GNB4, POPDC3; co-absent with the target |
| [[ZNF354C]] | C | WIPF1 activity raises ZNF354C's level | lines that do not express WIPF1 (16) vs lines expressing it (34) | 3.15× lower at baseline in the lines without WIPF1 | 0.071 | ⚠ within organs, on part of the lines; also absent: BVES-AS1, GNB4, POPDC3; co-absent with the target |
| [[NAV1]] | C | WIPF1 activity raises NAV1's level | lines that do not express WIPF1 (16) vs lines expressing it (34) | 3.97× lower at baseline in the lines without WIPF1 | 0.097 | ⚠ within organs, on part of the lines; also absent: BVES-AS1, GNB4, POPDC3; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.451). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (55.3, 15.0); signed map (25.8, 49.8). **Vector** length 84.9, 22.3% of its response variance represented; |z| ≥ 3 in 871 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.8 | -0.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.4 | +0.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | -0.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.0 | +3.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +0.5 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.9 | +4.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.8 | +2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | -5.1 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -4.7 | -13.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.5 | -14.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.9 | -43.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.4 | -15.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.4 | -18.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.8 | -2.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.8 | -0.9 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -1.7 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | WAS/WASL interacting protein family member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.1 — chr2:174,559,572-174,682,916 (-) |
| Ensembl biotype | protein_coding |
| Also known as | WIP; previously WASPIP |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 15 pathways, smallest: RHO GTPases Activate WASPs and WAVEs; FCGR3A-mediated phagocytosis; Leishmania phagocytosis |
| Matched by | ensembl_id |

**Function**, from UniProt [O43516](https://www.uniprot.org/uniprotkb/O43516) (WAS/WASL-interacting protein family member 1):

> Plays a role in the reorganization of the actin cytoskeleton. Contributes with NCK1 and GRB2 in the recruitment and activation of WASL. May participate in regulating the subcellular localization of WASL, resulting in the disassembly of stress fibers in favor of filopodia formation. Plays a role in the formation of cell ruffles (By similarity). Plays an important role in the intracellular motility of vaccinia virus by functioning as an adapter for recruiting WASL to vaccinia virus.

**Summary**, from NCBI Gene [7456](https://www.ncbi.nlm.nih.gov/gene/7456):

> This gene encodes a protein that plays an important role in the organization of the actin cytoskeleton. The encoded protein binds to a region of Wiskott-Aldrich syndrome protein that is frequently mutated in Wiskott-Aldrich syndrome, an X-linked recessive disorder. Impairment of the interaction between these two proteins may contribute to the disease. Two transcript variants encoding the same protein have been identified for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:12736](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12736) · Entrez [7456](https://www.ncbi.nlm.nih.gov/gene/7456) · UniProt [O43516](https://www.uniprot.org/uniprotkb/O43516) · Ensembl [ENSG00000115935](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115935)

## Data

Gene col 3738: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3738); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3738, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3738]; `tensor/DDL_lfc|DDL_z.npy` [3738]; `embed/gene_vectors.npy` [3738]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3738 or target_col == 3738). Every well: [[WIPF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WIPF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
