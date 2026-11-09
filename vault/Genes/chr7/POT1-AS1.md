---
symbol: "POT1-AS1"
type: "gene"
col: 13428
ensembl_id: "ENSG00000224897"
name: "POT1 antisense RNA 1"
location: "7q31.33"
module: 92
arm: "+"
pooled_cpm: 9.77
n_lines_expressing: 49
n_dd_up: 44
n_dd_down: 13
n_dd_up_clean: 39
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/092"]
generated_by: "tahoemap"
---

# POT1-AS1

*POT1 antisense RNA 1* — 7q31.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 44 drug-doses (5 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.12× (z +11.3, q 1e-26, up in 39 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.412× (z -9.5, q 2e-18, down in 32 of 46 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 0.600× (z -5.5, q 5e-06, down in 20 of 42 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DIO2]] (+0.52, fdr 1e-05), [[CLIC2]] (+0.52, fdr 1e-05), [[FILIP1L]] (+0.49, fdr 2e-05); moves opposite to [[NHSL1]] (-0.53, fdr 1e-05), [[ETV4]] (-0.49, fdr 4e-05), [[POC1B]] (-0.48, fdr 3e-05).
> It is in [[Module 092]], a single-armed module (MAPK output).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LINC01170]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 5 with an alert ⚠; shown: the 15 strongest. 44 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13428.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.12×** | +11.3 | 1e-26 | 39/45 (KATO III, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **2.54×** | +9.5 | 5e-19 | 31/43 (HOP62, KATO III, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **2.23×** | +8.5 | 4e-15 | 31/47 (NCI-H23, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **2.18×** | +8.0 | 2e-13 | 29/43 (HOP62, A498, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.83×** | +7.7 | 2e-12 | 28/44 (NCI-H23, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.03×** | +7.5 | 5e-12 | 32/44 (KATO III, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.01×** | +7.4 | 1e-11 | 24/43 (C32, HT-29, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.01×** | +7.4 | 1e-11 | 28/47 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.98×** | +7.3 | 2e-11 | 25/44 (A498, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.86×** | +6.6 | 2e-09 | 27/44 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.86×** | +6.6 | 2e-09 | 30/46 (NCI-H23, A498, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.78×** | +6.5 | 3e-09 | 25/47 (HOP62, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.68×** | +6.4 | 6e-09 | 22/45 (HOP62, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.77×** | +5.7 | 5e-07 | 20/44 (SW480, SW 900, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.58×** | +5.7 | 5e-07 | 20/45 (Panc 03.27, SW480, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13428.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.412×** | -9.5 | 2e-18 | 32/46 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.546×** | -6.5 | 3e-08 | 23/40 (PANC-1, CHP-212, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.558×** | -6.2 | 9e-08 | 24/43 (SW480, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.594×** | -5.6 | 4e-06 | 25/44 (SW480, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.600×** | -5.5 | 5e-06 | 20/42 (BT-474, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.440×** | -4.6 | 5e-04 | 18/42 (CHP-212, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | **0.754×** | -4.3 | 0.002 | 14/45 (NCI-H23, Panc 03.27, …) | top dose only | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.487×** | -4.0 | 0.004 | 14/40 (HEC-1-A, HepG2/C3A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.704×** | -3.8 | 0.010 | 12/44 (PANC-1, NCI-H23, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.512×** | -3.7 | 0.010 | 12/44 (HEC-1-A, RPMI-7951, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.783×** | -3.7 | 0.010 | 16/45 (CFPAC-1, Hs 766T, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **0.700×** | -3.7 | 0.011 | 17/45 (SW 900, SW480, …) | top dose only | composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.727×** | -3.4 | 0.028 | 9/47 (PANC-1, HepG2/C3A, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13428. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 10.7 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.130× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.152× (z -10.7) |
| [[CHP-212 (line)]] | wt | 40.2 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0769× (z -13.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 0.05 µM 0.0592× (z -10.4) |
| [[SW480 (line)]] | alt | 12.0 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0964× (z -13.6) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A-172 (line)]] | wt | 6.68 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 13.0× (z +13.0) ⚠ cell-cycle shift, would explain all of this change | [[Belinostat (drug)]] 0.5 µM 0.0906× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 14.4 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.188× (z -8.6) |
| [[HS-578T (line)]] | alt | 25.6 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +14.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HT-29 (line)]] | alt | 8.13 | 1 | 1 | [[Auranofin (drug)]] 5 µM 14.9× (z +11.1) | [[Fluvoxamine (drug)]] 5 µM 0.0438× (z -12.4) |
| [[KATO III (line)]] | alt | 15.0 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 5.15× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.143× (z -9.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 3.15 | 2 | 0 | [[Auranofin (drug)]] 5 µM 11.5× (z +8.9) | — |
| [[NCI-H23 (line)]] | alt | 20.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.90× (z +10.8) ⚠ position not correctable | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.182× (z -8.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[BT-474 (line)]] | alt | 11.4 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0812× (z -9.3) |
| [[C32 (line)]] | wt | 11.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 26.7× (z +13.0) | — |
| [[CFPAC-1 (line)]] | alt | 13.4 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.69× (z +8.5) | — |
| [[HCT15 (line)]] | alt | 9.36 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0333× (z -10.3) |
| [[HOP62 (line)]] | alt | 13.8 | 1 | 0 | [[Cobimetinib (drug)]] 5 µM 10.5× (z +10.3) | — |
| [[hTERT-HPNE (line)]] | wt | 39.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +8.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H1573 (line)]] | alt | 4.51 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -10.1) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 4.94 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.95× (z +8.9) | — |
| [[SK-MEL-2 (line)]] | alt | 10.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 8.15× (z +8.8) | — |
| [[SW 900 (line)]] | alt | 15.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.102× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.69 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.34 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.60 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.84 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.01 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.04 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.93 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.72 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13428), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DIO2]] | +0.52 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[CLIC2]] | +0.52 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[FILIP1L]] | +0.49 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[HIF1A-AS3]] | +0.49 | +0.35 / +0.54 | both halves | 1e-04 | same gene group |
| [[ROS1]] | +0.49 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[ZSCAN31]] | +0.48 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[TRMT10A]] | +0.48 | +0.56 / +0.39 | both halves | 5e-05 |  |
| [[LINC00871]] | +0.48 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[AKR1C1]] | +0.47 | +0.43 / +0.45 | both halves | 3e-05 |  |
| [[LINC00298]] | +0.47 | +0.40 / +0.52 | both halves | 5e-05 |  |
| [[LINC03002]] | +0.47 | +0.33 / +0.60 | both halves | 1e-04 |  |
| [[SYNPO2]] | +0.46 | +0.52 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NHSL1]] | -0.53 | -0.53 / -0.65 | both halves | 1e-05 |  |
| [[ETV4]] | -0.49 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[POC1B]] | -0.48 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[TMEM158]] | -0.48 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[DPY19L3]] | -0.48 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[ICAM3]] | -0.47 | -0.37 / -0.44 | both halves | 9e-05 |  |
| [[SPRY4-AS1]] | -0.46 | -0.47 / -0.45 | both halves | 3e-05 | same gene group |
| [[SPRY4]] | -0.46 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[ITGB5]] | -0.46 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[SPRED2]] | -0.46 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[PITPNC1]] | -0.45 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[CFAP298]] | -0.44 | -0.33 / -0.38 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01170]] | B | LINC01170 activity raises POT1-AS1's level | lines that do not express LINC01170 (13) vs lines expressing it (37) | 1.74× lower at baseline in the lines without LINC01170 | 0.007 | ⚠ within organs, on part of the lines; also absent: ZNF608, ENSG00000249526; maybe low, not absent |
| [[DSEL]] | B | DSEL activity raises POT1-AS1's level | lines that do not express DSEL (16) vs lines expressing it (34) | 1.71× lower at baseline in the lines without DSEL | 0.042 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: HDX, GLRB, AFAP1L1 |
| [[NREP]] | B | NREP activity raises POT1-AS1's level | lines that do not express NREP (13) vs lines expressing it (37) | 1.82× lower at baseline in the lines without NREP | 0.086 | ⚠ within organs, on part of the lines; also absent: DMD, MAP1B, KCTD16 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 092]] — MAPK output; 49 genes; every member is in the + arm (projection on the module's main direction -0.415). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.8, 25.4); signed map (40.9, 19.8). **Vector** length 80.6, 16.4% of its response variance represented; |z| ≥ 3 in 1,150 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.5 | +11.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.4 | +7.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.6 | +7.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.2 | +9.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.1 | +2.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.7 | +7.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.5 | +8.0 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -5.2 | -5.5 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -2.1 | -1.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -1.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -0.9 |
|  | [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | -1.7 | -2.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.6 | -2.8 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.5 | -0.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | POT1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 7q31.33 — chr7:124,929,873-125,482,966 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:49459](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49459) · Entrez [401398](https://www.ncbi.nlm.nih.gov/gene/401398) · Ensembl [ENSG00000224897](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000224897)

## Data

Gene col 13428: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13428); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13428, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13428]; `tensor/DDL_lfc|DDL_z.npy` [13428]; `embed/gene_vectors.npy` [13428]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13428 or target_col == 13428). Every well: [[POT1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POT1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
