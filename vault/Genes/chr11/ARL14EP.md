---
symbol: "ARL14EP"
type: "gene"
col: 7603
ensembl_id: "ENSG00000152219"
name: "ARF like GTPase 14 effector protein"
location: "11p14.1"
module: 11
arm: "+"
pooled_cpm: 22.76
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 5
n_dd_up_clean: 13
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# ARL14EP

*ARF like GTPase 14 effector protein* — 11p14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.13× (z +40.5, q 0e+00, up in 47 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.720× (z -6.7, q 1e-08, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPP38]] (+0.84, fdr 7e-06), [[METTL18]] (+0.83, fdr 7e-06), [[ABRAXAS2]] (+0.82, fdr 7e-06); moves opposite to [[CD81]] (-0.67, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[SOCS2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7603.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.13×** | +40.5 | 0e+00 | 47/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.23×** | +29.5 | 0e+00 | 47/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **4.28×** | +28.6 | 0e+00 | 48/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.58×** | +19.4 | 0e+00 | 45/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.76×** | +11.6 | 4e-29 | 38/48 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +8.9 | 4e-17 | 30/45 (AsPC-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.33×** | +8.2 | 2e-14 | 27/48 (A-172, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.30×** | +5.4 | 4e-06 | 18/48 (A-172, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.32×** | +5.2 | 1e-05 | 20/47 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.28×** | +5.0 | 3e-05 | 13/47 (J82, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.27×** | +4.8 | 8e-05 | 16/48 (NCI-H2347, PANC-1, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.53×** | +4.5 | 3e-04 | 14/48 (A498, A-427, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **1.20×** | +3.8 | 0.006 | 16/44 (HOP62, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-733 (drug)]] 5 µM |  | **1.41×** | +3.7 | 0.009 | 6/47 (PANC-1, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 1.19× | +3.6 | 0.011 | 17/48 (NCI-H1573, BT-474, …) | top dose only | composition shift |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.37×** | +3.3 | 0.029 | 11/46 (A-427, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.32×** | +3.0 | 0.090 | 5/47 (NCI-H460, SNU-423, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7603.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.720×** | -6.7 | 1e-08 | 25/48 (PANC-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.724×** | -6.6 | 1e-08 | 24/43 (A-427, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.764×** | -5.5 | 6e-06 | 20/47 (RKO, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.783×** | -5.0 | 8e-05 | 19/48 (A498, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.814×** | -4.0 | 0.006 | 15/31 (NCI-H1792, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.846× | -3.4 | 0.055 | 14/48 (A498, J82, …) | all doses, stronger at high dose |  |
| [[Bergenin (drug)]] 0.5 µM |  | 0.854× | -3.2 | 0.10 | 7/48 (MIA PaCa-2, LoVo, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~1% of this change | 0.848× | -3.1 | 0.13 | 13/36 (A-172, BT-474, …) | all doses, flat | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7603. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 27.6 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 5.15× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.190× (z -13.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 29.4 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.33× (z +22.6) | [[Dinaciclib (drug)]] 0.05 µM 0.262× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~1% of this change |
| [[A498 (line)]] | wt | 29.5 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +19.9) | [[Dinaciclib (drug)]] 5 µM 0.343× (z -10.5) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 19.6 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.74× (z +24.3) | [[Digitoxin (drug)]] 5 µM 0.371× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 17.2 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.234× (z -11.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 33.7 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.20× (z +29.0) | [[Dinaciclib (drug)]] 5 µM 0.368× (z -12.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 30.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +15.8) | — |
| [[C32 (line)]] | wt | 21.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +19.8) | — |
| [[Hs 766T (line)]] | wt | 29.2 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.16× (z +19.2) | [[Dinaciclib (drug)]] 5 µM 0.309× (z -8.6) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 20.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.53× (z +15.2) | — |
| [[LOX-IMVI (line)]] | wt | 24.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +14.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 25.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +13.9) | — |
| [[NCI-H1573 (line)]] | alt | 17.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.39× (z +20.8) | — |
| [[NCI-H1792 (line)]] | alt | 22.9 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.79× (z +17.8) | [[Dinaciclib (drug)]] 5 µM 0.0986× (z -16.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 24.8 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +13.4) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.218× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 25.1 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.38× (z +18.3) | [[Dinaciclib (drug)]] 5 µM 0.302× (z -9.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 17.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.14× (z +16.6) | — |
| [[BT-474 (line)]] | alt | 15.4 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.57× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.144× (z -10.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 11.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.83× (z +16.0) | — |
| [[HOP62 (line)]] | alt | 18.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +14.0) | — |
| [[HT-29 (line)]] | alt | 23.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.84× (z +20.3) | — |
| [[hTERT-HPNE (line)]] | wt | 21.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.01× (z +15.3) | — |
| [[J82 (line)]] | alt | 28.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.53× (z +17.9) | — |
| [[KATO III (line)]] | alt | 14.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.00× (z +12.0) | — |
| [[NCI-H2347 (line)]] | alt | 20.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +18.8) | — |
| [[Panc 03.27 (line)]] | alt | 31.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +16.0) | — |
| [[SW480 (line)]] | alt | 29.4 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.70× (z +10.9) | — |
| [[H4 (line)]] | wt | 31.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +11.3) | — |
| [[LoVo (line)]] | wt | 19.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +8.6) | — |
| [[LS 180 (line)]] | wt | 16.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +13.6) | — |
| [[NCI-H2030 (line)]] | alt | 12.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +9.7) | — |
| [[C-33 A (line)]] | alt | 26.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -9.8) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 11.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.51× (z +11.2) | — |
| [[HepG2_C3A (line)]] | wt | 16.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +10.4) | — |
| [[SNU-1 (line)]] | wt | 32.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +9.2) | — |
| [[SW 900 (line)]] | alt | 9.00 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.97× (z +10.2) | — |
| [[SW1417 (line)]] | alt | 29.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +9.0) | — |
| [[SW48 (line)]] | wt | 18.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.69× (z +9.9) | — |
| [[AN3 CA (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7603), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPP38]] | +0.84 | +0.83 / +0.79 | both halves | 7e-06 |  |
| [[METTL18]] | +0.83 | +0.81 / +0.75 | both halves | 7e-06 |  |
| [[ABRAXAS2]] | +0.82 | +0.81 / +0.79 | both halves | 7e-06 |  |
| [[ZNF197]] | +0.81 | +0.84 / +0.70 | both halves | 7e-06 |  |
| [[NME6]] | +0.80 | +0.80 / +0.69 | both halves | 7e-06 |  |
| [[FAM200A]] | +0.80 | +0.82 / +0.70 | both halves | 7e-06 |  |
| [[ZNF181]] | +0.79 | +0.82 / +0.64 | both halves | 7e-06 |  |
| [[MRPL58]] | +0.77 | +0.86 / +0.75 | both halves | 7e-06 |  |
| [[ERCC4]] | +0.77 | +0.83 / +0.71 | both halves | 7e-06 |  |
| [[C1orf131]] | +0.77 | +0.81 / +0.68 | both halves | 7e-06 |  |
| [[NAIF1]] | +0.76 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[RPP25L]] | +0.76 | +0.77 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CD81]] | -0.67 | -0.69 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SOCS2]] | B | SOCS2 activity raises ARL14EP's level | lines that do not express SOCS2 (10) vs lines expressing it (40) | 1.48× lower at baseline in the lines without SOCS2 | 0.014 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, HOXC9, TMEM45A |
| [[HDAC6]] | B | HDAC6 activity raises ARL14EP's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SRGAP2C]] | B | SRGAP2C activity raises ARL14EP's level | lines that do not express SRGAP2C (5) vs lines expressing it (45) | 1.32× lower at baseline in the lines without SRGAP2C | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TGFBR2, PRDM2, APC; also absent: FAM72B, LINC02798, DNAJB5 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.860). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-32.5, 7.1); signed map (3.7, -21.5). **Vector** length 108, 26.1% of its response variance represented; |z| ≥ 3 in 883 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +12.0 | +29.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +10.4 | +19.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +9.5 | +28.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +9.4 | +40.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +8.2 | +11.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.8 | +5.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.2 | +2.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.5 | +3.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +2.3 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -5.7 | -6.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.3 | -5.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.8 | -6.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.6 | -5.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.3 | -4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.2 | -1.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.0 | -0.8 |
|  | [[crizotinib (drug)]] 5 µM |  | -2.0 | -2.3 |
|  | [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | -1.6 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | ARF like GTPase 14 effector protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p14.1 — chr11:30,323,104-30,338,223 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ38968, ARF7EP; previously C11orf46 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N8R7](https://www.uniprot.org/uniprotkb/Q8N8R7) (ARL14 effector protein):

> Through its interaction with ARL14 and MYO1E, may connect MHC class II-containing cytoplasmic vesicles to the actin network and hence controls the movement of these vesicles along the actin cytoskeleton in dendritic cells.

**Summary**, from NCBI Gene [120534](https://www.ncbi.nlm.nih.gov/gene/120534):

> The protein encoded by this gene is an effector protein. It interacts with ADP-ribosylation factor-like 14 [ARL14, also known as ADP-ribosylation factor 7 (ARF7)], beta-actin (ACTB) and actin-based motor protein myosin 1E (MYO1E). ARL14 is a small GTPase; it controls the export of major histocompatibility class II molecules by connecting to the actin network via this effector protein. [provided by RefSeq, Sep 2014]

**Accessions** — [HGNC:26798](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26798) · Entrez [120534](https://www.ncbi.nlm.nih.gov/gene/120534) · UniProt [Q8N8R7](https://www.uniprot.org/uniprotkb/Q8N8R7) · Ensembl [ENSG00000152219](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152219)

## Data

Gene col 7603: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7603); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7603, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7603]; `tensor/DDL_lfc|DDL_z.npy` [7603]; `embed/gene_vectors.npy` [7603]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7603 or target_col == 7603). Every well: [[ARL14EP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARL14EP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
