---
symbol: "SZRD1"
type: "gene"
col: 620
ensembl_id: "ENSG00000055070"
name: "SUZ RNA binding domain containing 1"
location: "1p36.13"
module: 25
arm: "+"
pooled_cpm: 84.34
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# SZRD1

*SUZ RNA binding domain containing 1* — 1p36.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.12× (z +16.9, q 0e+00, up in 44 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 3.62× (z +15.2, q 0e+00, up in 47 of 49 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (HCT15 0.421×, RKO 0.552×, MIA PaCa-2 0.580×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (RKO 0.114×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 0.342×; ⚠ toxic; transcription drop); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM in 1 line (SW 1088 0.111×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SF3B4]] (+0.72, fdr 7e-06), [[EMC1]] (+0.69, fdr 7e-06), [[RAB1B]] (+0.68, fdr 7e-06); moves opposite to [[CROCCP2-1]] (-0.64, fdr 1e-05), [[SMIM26]] (-0.62, fdr 3e-05, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[ING2]] (-0.58, fdr 4e-05), [[TMEM191A-1]] (-0.58, fdr 2e-04).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 620.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.12×** | +16.9 | 0e+00 | 44/49 (LoVo, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.62×** | +15.2 | 0e+00 | 47/49 (PANC-1, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.90×** | +13.9 | 2e-41 | 37/44 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.72×** | +11.3 | 2e-27 | 35/45 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.63×** | +11.0 | 3e-26 | 46/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.51×** | +9.3 | 2e-18 | 44/48 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.09×** | +8.7 | 3e-16 | 38/48 (C32, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.41×** | +7.8 | 4e-13 | 39/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.39×** | +7.4 | 7e-12 | 40/48 (PANC-1, LS 180, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~21% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.37×** | +7.1 | 6e-11 | 38/48 (A498, NCI-H460, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.36×** | +6.9 | 2e-10 | 32/48 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.31×** | +6.0 | 7e-08 | 30/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.23×** | +4.7 | 1e-04 | 27/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.24×** | +4.6 | 1e-04 | 25/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.22×** | +4.4 | 4e-04 | 25/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.17× | +3.2 | 0.040 | 18/47 (SNU-1, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Folic acid (drug)]] 5 µM |  | 1.11× | +3.1 | 0.051 | 4/48 (NCI-H460, NCI-H1573, …) | rises with dose | position effect removed |
| [[Cyclosporin A (drug)]] 0.5 µM |  | 1.15× | +3.1 | 0.062 | 11/48 (HepG2/C3A, LOX-IMVI, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 620.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (HCT15 0.421×, RKO 0.552×, MIA PaCa-2 0.580×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (RKO 0.114×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 0.342×; ⚠ toxic; transcription drop); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM in 1 line (SW 1088 0.111×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.839× | -4.0 | 0.035 | 19/48 (HCT15, RPMI-7951, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.836× | -3.8 | 0.036 | 16/48 (NCI-H2030, LOX-IMVI, …) | inconsistent across doses |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 0.897× | -3.5 | 0.073 | 4/49 (SHP-77, NCI-H1792, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | 0.854× | -3.5 | 0.073 | 17/49 (J82, HS-578T, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.867× | -3.3 | 0.12 | 10/48 (hTERT-HPNE, BT-474, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | 0.872× | -3.1 | 0.16 | 13/48 (CHP-212, C32, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | 0.866× | -3.1 | 0.16 | 11/48 (C32, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 620. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 111 | 8 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.42× (z +14.8) | — |
| [[NCI-H460 (line)]] | wt | 68.4 | 7 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.41× (z +12.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.26× (z +11.7) | — |
| [[LoVo (line)]] | wt | 59.8 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +15.8) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 4.93× (z +10.9) | — |
| [[SW480 (line)]] | alt | 83.5 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.49× (z +13.2) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 5.34× (z +12.7) | — |
| [[NCI-H1573 (line)]] | alt | 72.5 | 5 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.00× (z +12.7) | — |
| [[A498 (line)]] | wt | 63.4 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +11.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.01× (z +9.0) | — |
| [[RKO (line)]] | wt | 100 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.00× (z +11.1) | [[Dinaciclib (drug)]] 0.05 µM 0.114× (z -23.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 56.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +12.3) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 85.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.93× (z +13.7) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 124 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.43× (z +10.1) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 107 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.53× (z +12.6) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 94.7 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.25× (z +11.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.92× (z +9.0) | — |
| [[LS 180 (line)]] | wt | 82.1 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.48× (z +10.0) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 5.19× (z +9.5) | — |
| [[NCI-H23 (line)]] | alt | 114 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 4.67× (z +10.7) | — |
| [[SNU-423 (line)]] | alt | 71.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +13.9) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 56.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.04× (z +11.0) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 75.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.46× (z +11.4) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 71.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.98× (z +12.5) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 173 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.32× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.580× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 79.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +10.9) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 85.1 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.05× (z +10.7) | — |
| [[Panc 03.27 (line)]] | alt | 56.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +11.4) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 86.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.63× (z +10.9) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 96.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.57× (z +10.9) | — |
| [[A549 (line)]] | wt | 62.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.69× (z +9.2) | — |
| [[AsPC-1 (line)]] | alt | 76.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.91× (z +8.7) | — |
| [[BT-474 (line)]] | alt | 67.5 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.177× (z -8.6) ⚠ toxic |
| [[C32 (line)]] | wt | 77.2 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 7.47× (z +10.3) | — |
| [[CFPAC-1 (line)]] | alt | 97.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.06× (z +9.9) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 63.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.52× (z +9.4) | — |
| [[HCT15 (line)]] | alt | 92.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -10.9) ⚠ cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 63.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.94× (z +8.5) | — |
| [[SNU-1 (line)]] | wt | 92.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.18× (z +9.9) | — |
| [[SW 1088 (line)]] | alt | 104 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.111× (z -8.7) |
| [[SW48 (line)]] | wt | 83.1 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 3.46× (z +10.4) | — |
| [[AN3 CA (line)]] | alt | 92.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 46.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 91.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 124 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 115 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 89.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 60.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 72.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 72.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 87.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 93.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 73.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 66.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 72.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 620), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SF3B4]] | +0.72 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[EMC1]] | +0.69 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[RAB1B]] | +0.68 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[LIN7C]] | +0.67 | +0.51 / +0.71 | both halves | 1e-05 |  |
| [[DHFR]] | +0.67 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[PRPF8]] | +0.66 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[CDC42]] | +0.66 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[PPP2R1A]] | +0.65 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[MAPRE1]] | +0.65 | +0.47 / +0.67 | both halves | 2e-05 |  |
| [[DCTN1]] | +0.65 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[NRAS]] | +0.64 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[TARDBP]] | +0.64 | +0.60 / +0.58 | both halves | 8e-06 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CROCCP2-1]] | -0.64 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[SMIM26]] ⚠ | -0.62 | -0.45 / -0.65 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ING2]] | -0.58 | -0.41 / -0.62 | both halves | 4e-05 |  |
| [[TMEM191A-1]] | -0.58 | -0.32 / -0.65 | both halves | 2e-04 |  |
| [[NACA4P]] ⚠ | -0.58 | -0.43 / -0.63 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NKAP]] | -0.58 | -0.46 / -0.62 | both halves | 3e-05 |  |
| [[GGNBP2]] | -0.57 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[SNHG32]] | -0.56 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[INAFM1]] | -0.56 | -0.40 / -0.59 | both halves | 5e-05 |  |
| [[CAMLG]] | -0.55 | -0.35 / -0.61 | both halves | 1e-04 |  |
| [[SNHG7]] | -0.55 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[SNHG6]] | -0.55 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[RPAIN]] | -0.55 | -0.40 / -0.58 | both halves | 5e-05 |  |
| [[MRPL23]] | -0.54 | -0.37 / -0.57 | both halves | 9e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.642). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-25.3, -24.0); signed map (-15.3, -35.1). **Vector** length 92.4, 23.4% of its response variance represented; |z| ≥ 3 in 979 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.3 | +13.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.5 | +16.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.3 | +11.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.3 | +15.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.3 | +2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.3 | +8.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +7.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.6 | +2.1 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.4 | -4.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.7 | +1.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.3 | +0.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.3 | -0.0 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.1 | -0.9 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.0 | -3.5 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -2.0 | -0.8 |
|  | [[Azithromycin (hydrate) (drug)]] 5 µM |  | -1.8 | -0.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.8 | +2.4 |

## What is on record

|  |  |
|---|---|
| Name | SUZ RNA binding domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.13 — chr1:16,352,575-16,398,145 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp566C0424; previously C1orf144 |
| Matched by | ensembl_id |

UniProt [Q7Z422](https://www.uniprot.org/uniprotkb/Q7Z422) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:30232](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30232) · Entrez [26099](https://www.ncbi.nlm.nih.gov/gene/26099) · UniProt [Q7Z422](https://www.uniprot.org/uniprotkb/Q7Z422) · Ensembl [ENSG00000055070](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000055070)

## Data

Gene col 620: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 620); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 620, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 620]; `tensor/DDL_lfc|DDL_z.npy` [620]; `embed/gene_vectors.npy` [620]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 620 or target_col == 620). Every well: [[SZRD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SZRD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
