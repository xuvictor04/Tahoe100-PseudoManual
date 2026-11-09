---
symbol: "TMEM54"
type: "gene"
col: 4304
ensembl_id: "ENSG00000121900"
name: "transmembrane protein 54"
location: "1p35.1"
module: 44
arm: "+"
pooled_cpm: 9.69
n_lines_expressing: 44
n_dd_up: 4
n_dd_down: 12
n_dd_up_clean: 0
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# TMEM54

*transmembrane protein 54* — 1p35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.89× (z +9.5, q 2e-18, up in 13 of 15 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (KATO III 5.09×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.466× (z -10.0, q 8e-21, down in 29 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CYTH1]] (+0.56, fdr 1e-05), [[KLK7]] (+0.55, fdr 2e-05), [[RAB25]] (+0.55, fdr 4e-05); moves opposite to [[TRMT13]] (-0.55, fdr 2e-05), [[COG4]] (-0.51, fdr 2e-05), [[ERMARD]] (-0.48, fdr 4e-05).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LCN2]] → it (grade B ⚠); 1 goes from it, the strongest it → [[SPINT2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4304.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (KATO III 5.09×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.89×** | +9.5 | 2e-18 | 13/15 (LS 180, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.41×** | +8.2 | 9e-14 | 24/29 (KATO III, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.90×** | +5.5 | 6e-06 | 15/20 (HEC-1-A, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.74×** | +5.2 | 3e-05 | 19/32 (SW1417, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | 1.42× | +3.3 | 0.13 | 15/42 (HOP62, COLO 205, …) | inconsistent across doses | position effect removed |
| [[Canagliflozin (drug)]] 0.05 µM |  | 1.44× | +3.2 | 0.13 | 11/37 (J82, HT-29, …) | inconsistent across doses | position effect removed |
| [[Filgotinib (drug)]] 0.5 µM |  | 1.40× | +3.1 | 0.13 | 10/39 (HT-29, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.67× | +3.1 | 0.13 | 9/37 (COLO 205, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4304.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.466×** | -10.0 | 8e-21 | 29/37 (HT-29, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.370×** | -9.2 | 8e-18 | 31/37 (LS 180, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.507×** | -6.1 | 3e-07 | 22/39 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.610×** | -4.6 | 7e-04 | 21/40 (BT-474, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.659×** | -3.9 | 0.013 | 17/40 (NCI-H2030, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.666×** | -3.8 | 0.016 | 16/41 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.477×** | -3.6 | 0.027 | 18/38 (NCI-H1573, A-427, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Budesonide (drug)]] 5 µM |  | **0.700×** | -3.3 | 0.071 | 12/41 (NCI-H661, NCI-H1792, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.706×** | -3.2 | 0.082 | 17/41 (RKO, RPMI-7951, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.710×** | -3.2 | 0.082 | 13/40 (AsPC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.521×** | -3.2 | 0.082 | 12/39 (KATO III, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.715×** | -3.1 | 0.093 | 12/41 (COLO 205, HT-29, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4304. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 46.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -20.3) |
| [[KATO III (line)]] | alt | 19.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.09× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -10.4) |
| [[LoVo (line)]] | wt | 21.5 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.186× (z -9.6) |
| [[LS 180 (line)]] | wt | 26.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0972× (z -13.7) |
| [[NCI-H2030 (line)]] | alt | 16.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -15.1) |
| [[SW1417 (line)]] | alt | 15.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -13.7) |
| [[AsPC-1 (line)]] | alt | 7.24 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -11.2) |
| [[BT-474 (line)]] | alt | 9.69 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -10.5) |
| [[HOP62 (line)]] | alt | 11.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.320× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 4.33 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0762× (z -9.2) |
| [[NCI-H2347 (line)]] | alt | 16.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -12.6) |
| [[Panc 03.27 (line)]] | alt | 5.90 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -10.3) |
| [[A-172 (line)]] | wt | 6.26 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.49 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.14 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.848 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.45 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.76 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.82 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.49 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.97 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.65 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.55 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.704 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.18 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.14 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4304), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYTH1]] | +0.56 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[KLK7]] | +0.55 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[RAB25]] | +0.55 | +0.61 / +0.40 | both halves | 4e-05 |  |
| [[KRTCAP3]] | +0.54 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[TST]] | +0.53 | +0.35 / +0.50 | both halves | 1e-04 |  |
| [[CKMT1A]] | +0.53 | +0.52 / +0.37 | both halves | 8e-05 |  |
| [[CORO2A]] | +0.52 | +0.55 / +0.37 | both halves | 8e-05 |  |
| [[MUC3A]] | +0.52 | +0.56 / +0.31 | both halves | 2e-04 |  |
| [[MSLN]] | +0.51 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[EGFL7]] | +0.51 | +0.52 / +0.39 | both halves | 6e-05 |  |
| [[CCNE1]] | +0.51 | +0.40 / +0.48 | both halves | 5e-05 |  |
| [[HDHD3]] | +0.51 | +0.42 / +0.47 | both halves | 4e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRMT13]] | -0.55 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[COG4]] | -0.51 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[ERMARD]] | -0.48 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[THOC7]] | -0.46 | -0.42 / -0.37 | both halves | 8e-05 |  |
| [[UPF3A]] | -0.46 | -0.48 / -0.31 | both halves | 2e-04 |  |
| [[RAD52]] | -0.46 | -0.47 / -0.36 | both halves | 1e-04 |  |
| [[TXNRD2]] | -0.46 | -0.48 / -0.33 | both halves | 1e-04 |  |
| [[HNRNPH3]] | -0.45 | -0.34 / -0.38 | both halves | 1e-04 |  |
| [[COQ9]] | -0.45 | -0.48 / -0.33 | both halves | 1e-04 |  |
| [[CCAR1]] | -0.45 | -0.44 / -0.33 | both halves | 1e-04 |  |
| [[RAD50]] | -0.45 | -0.44 / -0.39 | both halves | 6e-05 |  |
| [[TCEAL4]] | -0.45 | -0.48 / -0.21 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LCN2]] | B | LCN2 activity raises TMEM54's level | lines that do not express LCN2 (33) vs lines expressing it (17) | 2.04× lower at baseline in the lines without LCN2 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4 |
| [[SULT2B1]] | B | SULT2B1 activity raises TMEM54's level | lines that do not express SULT2B1 (28) vs lines expressing it (22) | 2.14× lower at baseline in the lines without SULT2B1 | 0.087 | ⚠ within organs, on part of the lines; also absent: ATP2C2, ST14, SGPP2; maybe low, not absent |
| [[MUC3A]] | B | MUC3A activity raises TMEM54's level | lines that do not express MUC3A (25) vs lines expressing it (25) | 1.85× lower at baseline in the lines without MUC3A | 0.091 | ⚠ within organs, on part of the lines; also absent: HSH2D, ADGRF1, CKMT1B |
| [[TMEM171]] | B | TMEM171 activity raises TMEM54's level | lines that do not express TMEM171 (15) vs lines expressing it (35) | 1.52× lower at baseline in the lines without TMEM171 | 0.093 | ⚠ within organs, on part of the lines; also absent: CD274, GBP5, PTGER4; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPINT2]] | B | TMEM54 activity raises SPINT2's level | lines that do not express TMEM54 (6) vs lines expressing it (44) | 5.20× lower at baseline in the lines without TMEM54 | 0.072 | ⚠ within organs, on part of the lines; also absent: RNF135, PDP1, ENSG00000291063; maybe low, not absent |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.392). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.2, 60.4); signed map (68.3, 4.9). **Vector** length 53.7, 9.67% of its response variance represented; |z| ≥ 3 in 610 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +2.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +9.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.9 | +2.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +8.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +5.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +2.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +3.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.4 | +1.7 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.4 | +3.1 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.4 | -9.2 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -1.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.8 | -6.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.4 | -1.5 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.3 | -1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.3 | -3.6 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.3 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 54 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.1 — chr1:32,894,594-32,901,438 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CAC-1, BCLP |
| Matched by | ensembl_id |

UniProt [Q969K7](https://www.uniprot.org/uniprotkb/Q969K7) carries no function annotation.

**Summary**, from NCBI Gene [113452](https://www.ncbi.nlm.nih.gov/gene/113452):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24143](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24143) · Entrez [113452](https://www.ncbi.nlm.nih.gov/gene/113452) · UniProt [Q969K7](https://www.uniprot.org/uniprotkb/Q969K7) · Ensembl [ENSG00000121900](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121900)

## Data

Gene col 4304: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4304); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4304, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4304]; `tensor/DDL_lfc|DDL_z.npy` [4304]; `embed/gene_vectors.npy` [4304]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4304 or target_col == 4304). Every well: [[TMEM54 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM54.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
