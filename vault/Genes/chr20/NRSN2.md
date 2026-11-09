---
symbol: "NRSN2"
type: "gene"
col: 4673
ensembl_id: "ENSG00000125841"
name: "neurensin 2"
location: "20p13"
module: 2
arm: "+"
pooled_cpm: 7.95
n_lines_expressing: 41
n_dd_up: 2
n_dd_down: 27
n_dd_up_clean: 2
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# NRSN2

*neurensin 2* — 20p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.61× (z +5.7, q 9e-06, up in 16 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.268× (z -21.8, q 0e+00, down in 34 of 37 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXL8]] (+0.55, fdr 2e-05), [[CERCAM]] (+0.55, fdr 2e-05), [[ARHGEF6]] (+0.54, fdr 2e-05); moves opposite to [[ATXN7L1]] (-0.55, fdr 1e-05), [[CRADD]] (-0.54, fdr 3e-05), [[ARHGEF28]] (-0.51, fdr 2e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MAP1B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4673.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.61×** | +5.7 | 9e-06 | 16/37 (SNU-423, hTERT-HPNE, …) | rises with dose | low cells (technical?); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.58×** | +5.2 | 5e-05 | 18/35 (SW480, H4, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Entrectinib (drug)]] 5 µM |  | 1.32× | +3.3 | 0.18 | 5/36 (HT-29, A498, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.31× | +3.2 | 0.18 | 10/38 (NCI-H2030, NCI-H460, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4673.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.268×** | -21.8 | 0e+00 | 34/37 (RPMI-7951, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.306×** | -13.8 | 5e-41 | 32/35 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.397×** | -10.8 | 7e-25 | 31/39 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.487×** | -8.1 | 1e-13 | 27/37 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.503×** | -8.0 | 1e-13 | 30/37 (LOX-IMVI, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.515×** | -7.7 | 1e-12 | 23/34 (PANC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.826×** | -7.7 | 1e-12 | 23/39 (SW480, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.570×** | -6.6 | 4e-09 | 25/37 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.589×** | -6.2 | 5e-08 | 23/37 (LOX-IMVI, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.590×** | -5.9 | 2e-07 | 16/31 (SNU-423, SK-MEL-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.636×** | -5.3 | 7e-06 | 18/38 (RPMI-7951, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.643×** | -5.1 | 1e-05 | 17/39 (PANC-1, BT-474, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.657×** | -4.9 | 5e-05 | 18/36 (NCI-H460, SNU-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.687×** | -4.4 | 5e-04 | 15/38 (SNU-423, A-172, …) | two highest doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.677×** | -4.4 | 5e-04 | 12/29 (LOX-IMVI, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.518×** | -4.0 | 0.002 | 13/34 (NCI-H1792, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **0.712×** | -3.8 | 0.005 | 8/38 (LOX-IMVI, CFPAC-1, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.740×** | -3.3 | 0.025 | 9/37 (A-172, RPMI-7951, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.758×** | -3.2 | 0.033 | 10/37 (RPMI-7951, LOX-IMVI, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.766×** | -2.9 | 0.083 | 11/36 (A-172, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.783×** | -2.8 | 0.100 | 2/39 (BT-474, SNU-1) | rises with dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.783×** | -2.8 | 0.100 | 8/37 (SK-MEL-2, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4673. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 11.0 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.135× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.263× (z -13.2) |
| [[A549 (line)]] | wt | 13.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0359× (z -18.0) |
| [[LOX-IMVI (line)]] | wt | 11.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -15.3) |
| [[BT-474 (line)]] | alt | 11.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0817× (z -15.6) |
| [[HOP62 (line)]] | alt | 16.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -18.0) |
| [[HT-29 (line)]] | alt | 5.70 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0726× (z -9.7) |
| [[NCI-H1792 (line)]] | alt | 5.72 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0562× (z -11.4) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H23 (line)]] | alt | 8.50 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -9.7) |
| [[NCI-H460 (line)]] | wt | 6.13 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.117× (z -10.6) |
| [[SW 900 (line)]] | alt | 10.7 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0761× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.177× (z -11.0) |
| [[A-172 (line)]] | wt | 20.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -14.9) |
| [[A498 (line)]] | wt | 8.71 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -9.2) |
| [[CFPAC-1 (line)]] | alt | 9.85 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -14.1) |
| [[COLO 205 (line)]] | alt | 6.58 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -8.5) |
| [[HS-578T (line)]] | alt | 10.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.121× (z -10.0) |
| [[RPMI-7951 (line)]] | alt | 16.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0315× (z -22.0) |
| [[SK-MEL-2 (line)]] | alt | 14.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -14.2) |
| [[SNU-1 (line)]] | wt | 16.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0781× (z -10.1) |
| [[SNU-423 (line)]] | alt | 10.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.119× (z -9.9) ⚠ toxic; cell-cycle shift, explains ~28% of this change |
| [[SW480 (line)]] | alt | 7.14 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -9.4) |
| [[A-427 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.738 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.18 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.947 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.722 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 9.25 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.11 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.708 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.765 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.01 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.667 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.900 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.58 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4673), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXL8]] | +0.55 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[CERCAM]] | +0.55 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[ARHGEF6]] | +0.54 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[TESK1]] | +0.53 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[MAPK7]] | +0.52 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[TSHZ3-AS1]] | +0.52 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[ACLY]] | +0.52 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[B4GALNT1]] | +0.52 | +0.49 / +0.46 | both halves | 2e-05 |  |
| [[ESYT1]] | +0.51 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[CSPG4]] | +0.50 | +0.52 / +0.42 | both halves | 4e-05 |  |
| [[L1CAM]] | +0.50 | +0.57 / +0.43 | both halves | 3e-05 |  |
| [[CDR2L]] | +0.49 | +0.47 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATXN7L1]] | -0.55 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[CRADD]] | -0.54 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[ARHGEF28]] | -0.51 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[ANK3]] | -0.48 | -0.51 / -0.34 | both halves | 1e-04 |  |
| [[SH3D19]] | -0.45 | -0.51 / -0.29 | both halves | 3e-04 |  |
| [[RAMP1]] | -0.45 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[ABO]] | -0.44 | -0.47 / -0.30 | both halves | 2e-04 |  |
| [[SYK]] | -0.43 | -0.46 / -0.28 | both halves | 3e-04 |  |
| [[SEC62]] | -0.43 | -0.32 / -0.43 | both halves | 2e-04 |  |
| [[RAD50]] | -0.42 | -0.47 / -0.32 | both halves | 2e-04 |  |
| [[SPG11]] | -0.41 | -0.47 / -0.20 | ⚠ not reproduced | 8e-04 |  |
| [[AKAP9]] | -0.41 | -0.30 / -0.43 | both halves | 2e-04 |  |
| [[GATAD1]] | -0.41 | -0.46 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP1B]] | B | MAP1B activity raises NRSN2's level | lines that do not express MAP1B (16) vs lines expressing it (34) | 2.78× lower at baseline in the lines without MAP1B | 0.012 | ⚠ within organs, on part of the lines; also absent: MPDZ, GNB4, EVL |
| [[NAV1]] | B | NAV1 activity raises NRSN2's level | lines that do not express NAV1 (22) vs lines expressing it (28) | 2.03× lower at baseline in the lines without NAV1 | 0.019 | ⚠ within organs, on part of the lines; also absent: NAV2, ENSG00000287622, CDK15; maybe low, not absent |
| [[SYK]] | B | SYK activity lowers NRSN2's level | lines that do not express SYK (30) vs lines expressing it (20) | 2.57× higher at baseline in the lines without SYK | 0.044 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ITGB6, ST14 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.345). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (57.4, 17.9); signed map (52.4, -17.5). **Vector** length 55.7, 9.11% of its response variance represented; |z| ≥ 3 in 846 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.6 | +1.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.4 | -0.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.9 | +2.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +1.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.3 | +0.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.1 | +5.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.7 | -3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | -1.4 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.3 | -0.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.2 | -4.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.4 | -13.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.0 | -21.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -1.8 | -8.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.8 | -6.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -4.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.2 | -0.1 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.2 | -1.0 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.2 | -0.6 |
|  | [[Rucaparib (phosphate) (drug)]] 5 µM |  | -1.0 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | neurensin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p13 — chr20:346,782-359,660 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ1103G7.6; previously C20orf98 |
| Gene groups (HGNC) | Neurensin family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9GZP1](https://www.uniprot.org/uniprotkb/Q9GZP1) (Neurensin-2):

> May play a role in maintenance and/or transport of vesicles.

**Summary**, from NCBI Gene [80023](https://www.ncbi.nlm.nih.gov/gene/80023):

> Predicted to be involved in nervous system development. Located in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16229](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16229) · Entrez [80023](https://www.ncbi.nlm.nih.gov/gene/80023) · UniProt [Q9GZP1](https://www.uniprot.org/uniprotkb/Q9GZP1) · Ensembl [ENSG00000125841](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125841)

## Data

Gene col 4673: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4673); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4673, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4673]; `tensor/DDL_lfc|DDL_z.npy` [4673]; `embed/gene_vectors.npy` [4673]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4673 or target_col == 4673). Every well: [[NRSN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NRSN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
