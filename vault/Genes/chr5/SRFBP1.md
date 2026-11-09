---
symbol: "SRFBP1"
type: "gene"
col: 7504
ensembl_id: "ENSG00000151304"
name: "serum response factor binding protein 1"
location: "5q23.1"
module: 1
arm: "+"
pooled_cpm: 82.05
n_lines_expressing: 50
n_dd_up: 41
n_dd_down: 2
n_dd_up_clean: 25
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# SRFBP1

*serum response factor binding protein 1* — 5q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 41 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.25× (z +40.8, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[NG25 (drug)]] 5 µM: 0.677× (z -5.0, q 3e-04, down in 24 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.332×; ⚠ cell-cycle shift, explains ~28% of this change); [[Apalutamide (drug)]] 5 µM in 1 line (SW 1088 0.0718×); [[NG25 (drug)]] 5 µM in 1 line (RKO 0.193×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATIC]] (+0.71, fdr 7e-06), [[UTP15]] (+0.70, fdr 7e-06), [[NOC3L]] (+0.68, fdr 7e-06); moves opposite to [[PHF1]] (-0.68, fdr 7e-06), [[TESK2]] (-0.63, fdr 4e-05), [[CCS]] (-0.63, fdr 4e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 19 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 41 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7504.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.25×** | +40.8 | 0e+00 | 47/48 (SNU-423, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.33×** | +28.3 | 0e+00 | 48/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.06×** | +27.3 | 0e+00 | 47/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **6.98×** | +24.9 | 0e+00 | 48/49 (LoVo, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.15×** | +18.7 | 0e+00 | 46/48 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.12×** | +18.3 | 0e+00 | 45/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **2.02×** | +17.2 | 0e+00 | 44/48 (NCI-H1792, HS-578T, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **3.39×** | +15.6 | 0e+00 | 44/48 (HEC-1-A, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.87×** | +15.3 | 0e+00 | 45/48 (SNU-423, HS-578T, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.27×** | +15.2 | 0e+00 | 40/45 (NCI-H1792, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.84×** | +14.8 | 0e+00 | 46/48 (HS-578T, SNU-423, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.79×** | +14.2 | 6e-44 | 41/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.76×** | +13.8 | 2e-41 | 41/48 (PANC-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.71×** | +13.1 | 1e-37 | 41/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.41×** | +11.9 | 4e-31 | 35/49 (HS-578T, MIA PaCa-2, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.57×** | +10.9 | 2e-26 | 39/48 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +9.1 | 2e-18 | 31/48 (HOP62, HEC-1-A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.40×** | +8.2 | 5e-15 | 39/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.34×** | +6.8 | 2e-10 | 33/48 (NCI-H1792, LoVo, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.30×** | +6.4 | 3e-09 | 30/48 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.31×** | +6.2 | 1e-08 | 29/48 (KATO III, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7504.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.332×; ⚠ cell-cycle shift, explains ~28% of this change); [[Apalutamide (drug)]] 5 µM in 1 line (SW 1088 0.0718×); [[NG25 (drug)]] 5 µM in 1 line (RKO 0.193×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM |  | **0.677×** | -5.0 | 3e-04 | 24/47 (RKO, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | 0.856× | -3.9 | 0.026 | 11/48 (HEC-1-A, SK-MEL-2, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.807×** | -3.8 | 0.026 | 20/48 (A498, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.861× | -3.7 | 0.026 | 11/47 (LS 180, HOP62, …) | two highest doses | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.839× | -3.1 | 0.20 | 20/48 (SNU-1, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib (drug)]] 5 µM |  | 0.793× | -3.0 | 0.23 | 5/48 (HS-578T, A-427, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7504. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 83.1 | 16 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +22.5) | — |
| [[HS-578T (line)]] | alt | 106 | 15 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +28.5) | — |
| [[LoVo (line)]] | wt | 73.9 | 14 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +26.3) | — |
| [[PANC-1 (line)]] | alt | 102 | 13 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +28.2) | — |
| [[H4 (line)]] | wt | 88.4 | 11 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +16.4) | — |
| [[HEC-1-A (line)]] | alt | 85.5 | 11 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +24.6) | — |
| [[NCI-H460 (line)]] | wt | 96.7 | 11 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +22.5) | — |
| [[NCI-H1573 (line)]] | alt | 96.0 | 10 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +16.5) | — |
| [[NCI-H1792 (line)]] | alt | 109 | 10 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +16.8) | — |
| [[SW480 (line)]] | alt | 67.0 | 10 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +13.7) | — |
| [[A549 (line)]] | wt | 76.7 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.27× (z +25.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 63.3 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.02× (z +24.1) | — |
| [[NCI-H2030 (line)]] | alt | 62.8 | 8 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +17.7) | [[Dinaciclib (drug)]] 5 µM 0.439× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 54.0 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.70× (z +24.7) | — |
| [[SNU-423 (line)]] | alt | 75.9 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.95× (z +31.7) | — |
| [[A498 (line)]] | wt | 79.0 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.62× (z +28.4) | — |
| [[CFPAC-1 (line)]] | alt | 42.0 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.71× (z +20.2) | — |
| [[hTERT-HPNE (line)]] | wt | 65.8 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.22× (z +23.6) | — |
| [[LS 180 (line)]] | wt | 41.9 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +15.3) | — |
| [[A-172 (line)]] | wt | 97.5 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +27.3) | — |
| [[BT-474 (line)]] | alt | 49.6 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +16.3) | — |
| [[Hs 766T (line)]] | wt | 90.2 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +15.9) | — |
| [[HT-29 (line)]] | alt | 49.4 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +20.9) | — |
| [[Panc 03.27 (line)]] | alt | 72.6 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +20.4) | — |
| [[RPMI-7951 (line)]] | alt | 63.1 | 6 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 4.95× (z +13.7) | — |
| [[LOX-IMVI (line)]] | wt | 132 | 5 | 0 | [[Harringtonine (drug)]] 0.5 µM 2.56× (z +10.0) | — |
| [[SK-MEL-2 (line)]] | alt | 125 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +16.5) | — |
| [[SW 900 (line)]] | alt | 61.2 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +13.7) | — |
| [[AsPC-1 (line)]] | alt | 32.7 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +13.0) | — |
| [[C32 (line)]] | wt | 77.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +13.9) | — |
| [[COLO 205 (line)]] | alt | 41.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.00× (z +13.9) | — |
| [[J82 (line)]] | alt | 102 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +24.5) | — |
| [[NCI-H23 (line)]] | alt | 103 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.60× (z +12.4) | — |
| [[A-427 (line)]] | wt | 92.8 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 5.67× (z +11.0) | — |
| [[HCT15 (line)]] | alt | 47.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.01× (z +16.5) | — |
| [[RKO (line)]] | wt | 359 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.06× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -16.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[NG25 (drug)]] 5 µM 0.193× (z -9.3) |
| [[SW48 (line)]] | wt | 44.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +13.5) | — |
| [[KATO III (line)]] | alt | 40.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +10.8) | — |
| [[CHP-212 (line)]] | wt | 87.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +9.7) | — |
| [[HepG2_C3A (line)]] | wt | 76.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +14.8) | — |
| [[SNU-1 (line)]] | wt | 82.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.82× (z +8.7) | — |
| [[SW 1088 (line)]] | alt | 102 | 0 | 1 | — | [[Apalutamide (drug)]] 5 µM 0.0718× (z -9.4) |
| [[AN3 CA (line)]] | alt | 128 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 85.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 66.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 82.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 82.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 43.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7504), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATIC]] | +0.71 | +0.70 / +0.75 | both halves | 7e-06 |  |
| [[UTP15]] | +0.70 | +0.70 / +0.68 | both halves | 7e-06 | STRING 603 |
| [[NOC3L]] | +0.68 | +0.75 / +0.66 | both halves | 7e-06 | STRING 485 |
| [[UTP20]] | +0.68 | +0.65 / +0.73 | both halves | 7e-06 | STRING 798 |
| [[ABCE1]] | +0.68 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[TRIM44]] | +0.67 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[PNO1]] | +0.67 | +0.68 / +0.67 | both halves | 7e-06 | STRING 489 |
| [[DDX10]] | +0.66 | +0.70 / +0.68 | both halves | 7e-06 | STRING 843 |
| [[SCO1]] | +0.66 | +0.71 / +0.57 | both halves | 1e-05 |  |
| [[NAA15]] | +0.65 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[FARSB]] | +0.65 | +0.69 / +0.73 | both halves | 7e-06 |  |
| [[RRP15]] | +0.64 | +0.67 / +0.69 | both halves | 7e-06 | STRING 501 |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHF1]] | -0.68 | -0.68 / -0.66 | both halves | 7e-06 |  |
| [[TESK2]] | -0.63 | -0.42 / -0.69 | both halves | 4e-05 |  |
| [[CCS]] | -0.63 | -0.42 / -0.66 | both halves | 4e-05 |  |
| [[CNNM4]] | -0.63 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[ULK1]] | -0.62 | -0.60 / -0.65 | both halves | 7e-06 |  |
| [[TULP3]] | -0.62 | -0.57 / -0.68 | both halves | 1e-05 |  |
| [[ABHD3]] | -0.61 | -0.50 / -0.63 | both halves | 1e-05 |  |
| [[AHDC1]] | -0.60 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[LMBR1L]] | -0.59 | -0.56 / -0.66 | both halves | 1e-05 |  |
| [[AAMDC]] | -0.58 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[DEDD2]] | -0.58 | -0.53 / -0.66 | both halves | 1e-05 |  |
| [[CBFA2T2]] | -0.58 | -0.58 / -0.63 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SRFBP1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ZNF474]] | C | ZNF474's natural level weakens SRFBP1's drug response | ZNF474's natural level across 43 lines (lineage-adjusted; a glimpse) | r -0.68, reverse -0.41; direction clear | 0.063 | ⚠ tissue can mimic it; precision caveat |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.670). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-17.5, -36.7); signed map (1.7, -41.6). **Vector** length 84.8, 25.9% of its response variance represented; |z| ≥ 3 in 1,596 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +6.9 | +18.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.9 | +24.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.9 | +10.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.4 | +15.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.6 | +27.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.6 | +15.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.3 | +6.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +9.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.8 | +0.7 |
| fall | [[NG25 (drug)]] 5 µM |  | -3.7 | -5.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.1 | -1.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.7 | +0.4 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.1 | -3.9 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.1 | -2.9 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.9 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | serum response factor binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q23.1 — chr5:121,961,975-122,075,570 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ25286, p49, STRAP, BUD22, Rlb1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NEF9](https://www.uniprot.org/uniprotkb/Q8NEF9) (Serum response factor-binding protein 1):

> May be involved in regulating transcriptional activation of cardiac genes during the aging process. May play a role in biosynthesis and/or processing of SLC2A4 in adipose cells (By similarity).

**Summary**, from NCBI Gene [153443](https://www.ncbi.nlm.nih.gov/gene/153443):

> Enables RNA binding activity. Predicted to be involved in maturation of SSU-rRNA. Predicted to be located in perinuclear region of cytoplasm. Predicted to be part of 90S preribosome. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26333](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26333) · Entrez [153443](https://www.ncbi.nlm.nih.gov/gene/153443) · UniProt [Q8NEF9](https://www.uniprot.org/uniprotkb/Q8NEF9) · Ensembl [ENSG00000151304](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151304)

## Data

Gene col 7504: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7504); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7504, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7504]; `tensor/DDL_lfc|DDL_z.npy` [7504]; `embed/gene_vectors.npy` [7504]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7504 or target_col == 7504). Every well: [[SRFBP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SRFBP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
