---
symbol: "MSL2"
type: "gene"
col: 10506
ensembl_id: "ENSG00000174579"
name: "MSL complex subunit 2"
location: "3q22.3"
module: 1
arm: "+"
pooled_cpm: 67.82
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 2
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# MSL2

*MSL complex subunit 2* — 3q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 7.34× (z +16.7, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.435× (z -13.5, q 1e-38, down in 37 of 44 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 9 lines (NCI-H23 0.128×, RPMI-7951 0.117×, A-427 0.218×, SW48 0.111×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H2347 0.293×, PANC-1 0.348×, NCI-H1573 0.273×, SW1417 0.293×; ⚠ toxic; transcription drop); [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM in 1 line (CHP-212 0.0760×; ⚠ cell-cycle shift, explains ~0% of this change); [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (CHP-212 0.0879×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (SW 1271 0.0973×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM120C]] (+0.65, fdr 1e-05), [[SOCS5]] (+0.59, fdr 8e-06), [[THAP12]] (+0.59, fdr 1e-05); moves opposite to [[KCTD5]] (-0.51, fdr 2e-05), [[SLC9A1]] (-0.51, fdr 1e-05), [[POR]] (-0.49, fdr 2e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10506.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **7.34×** | +16.7 | 0e+00 | 48/49 (SW480, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **4.73×** | +13.0 | 4e-36 | 44/48 (SW480, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.75×** | +9.4 | 1e-18 | 44/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.57×** | +7.6 | 5e-12 | 41/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.50×** | +6.9 | 8e-10 | 37/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.44×** | +6.2 | 7e-08 | 41/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.30×** | +4.3 | 0.002 | 24/47 (LoVo, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.1 | 0.003 | 20/48 (CFPAC-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.29×** | +4.1 | 0.003 | 27/48 (NCI-H23, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **1.53×** | +3.5 | 0.022 | 22/49 (A498, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.23×** | +3.5 | 0.027 | 20/48 (CFPAC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.23×** | +3.4 | 0.028 | 21/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.23×** | +3.4 | 0.028 | 23/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10506.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 9 lines (NCI-H23 0.128×, RPMI-7951 0.117×, A-427 0.218×, SW48 0.111×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H2347 0.293×, PANC-1 0.348×, NCI-H1573 0.273×, SW1417 0.293×; ⚠ toxic; transcription drop); [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM in 1 line (CHP-212 0.0760×; ⚠ cell-cycle shift, explains ~0% of this change); [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (CHP-212 0.0879×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (SW 1271 0.0973×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.435×** | -13.5 | 1e-38 | 37/44 (NCI-H23, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.469×** | -12.8 | 8e-35 | 45/49 (NCI-H2347, PANC-1, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.818× | -3.3 | 0.15 | 20/50 (A-172, SNU-423, …) | top dose only |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.827× | -3.2 | 0.15 | 18/47 (KATO III, NCI-H2030, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 0.827× | -3.2 | 0.15 | 19/48 (A498, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10506. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 92.7 | 6 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.94× (z +13.3) | [[Dinaciclib (drug)]] 0.5 µM 0.348× (z -13.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 81.9 | 7 (2 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 10.9× (z +16.6) | [[Dinaciclib (drug)]] 0.5 µM 0.469× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 44.5 | 5 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.39× (z +14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 8.70× (z +11.5) | — |
| [[SW48 (line)]] | wt | 66.5 | 3 | 2 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 5.37× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.111× (z -16.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 102 | 3 (1 ⚠) | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 8.81× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.351× (z -11.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 57.0 | 2 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 12.5× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.308× (z -11.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 55.4 | 4 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 12.3× (z +12.0) | — |
| [[NCI-H1573 (line)]] | alt | 61.1 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 10.3× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.273× (z -13.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 96.2 | 2 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 2.94× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.48× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.128× (z -21.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 111 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 11.6× (z +13.8) | [[Dinaciclib (drug)]] 5 µM 0.218× (z -16.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 61.3 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.65× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.347× (z -10.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 49.8 | 2 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 24.9× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.327× (z -8.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 62.7 | 1 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 5.38× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.377× (z -10.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 88.4 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 9.07× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.318× (z -12.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 74.6 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 8.34× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.284× (z -12.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 58.8 | 2 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 8.64× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.166× (z -15.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 73.1 | 2 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 9.01× (z +11.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.376× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~37% of this change |
| [[SNU-423 (line)]] | alt | 46.8 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.00× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.264× (z -12.4) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 106 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.17× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -12.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 47.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.366× (z -9.0) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 87.4 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 7.88× (z +10.0) | — |
| [[CFPAC-1 (line)]] | alt | 58.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +11.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.55× (z +8.6) | — |
| [[CHP-212 (line)]] | wt | 68.1 | 0 | 2 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.0760× (z -13.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0879× (z -12.6) |
| [[HepG2_C3A (line)]] | wt | 49.3 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 11.4× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.165× (z -12.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 41.0 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.35× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.308× (z -10.2) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 76.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.376× (z -9.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 49.0 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 8.53× (z +12.0) | — |
| [[NCI-H2347 (line)]] | alt | 66.6 | 1 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 6.41× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -14.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 82.9 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 9.36× (z +11.2) | — |
| [[SK-MEL-2 (line)]] | alt | 67.3 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 12.0× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.346× (z -10.4) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 88.0 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 11.3× (z +10.1) | — |
| [[A-172 (line)]] | wt | 59.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.330× (z -10.9) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 82.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.167× (z -10.1) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 70.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 20.2× (z +12.6) | — |
| [[HT-29 (line)]] | alt | 63.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.69× (z +11.2) | — |
| [[J82 (line)]] | alt | 61.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.423× (z -9.3) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 117 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.119× (z -9.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 62.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.117× (z -17.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 68.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.373× (z -9.3) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 75.0 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0973× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 67.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 71.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 77.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 44.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 61.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 54.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10506), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM120C]] | +0.65 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[SOCS5]] | +0.59 | +0.59 / +0.58 | both halves | 8e-06 |  |
| [[THAP12]] | +0.59 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[MIRLET7BHG]] | +0.56 | +0.64 / +0.46 | both halves | 2e-05 |  |
| [[COPS8-DT]] | +0.56 | +0.57 / +0.36 | both halves | 1e-04 |  |
| [[ABHD13]] | +0.55 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[NDUFAF5]] | +0.55 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[SCAP]] | +0.55 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[ZNF410]] | +0.54 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[RBM33]] | +0.54 | +0.46 / +0.60 | both halves | 2e-05 |  |
| [[SP3]] | +0.53 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[PCMTD1-DT]] | +0.53 | +0.30 / +0.44 | both halves | 2e-04 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCTD5]] | -0.51 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[SLC9A1]] | -0.51 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[POR]] | -0.49 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[GAN]] | -0.49 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[PPFIA1]] | -0.49 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[LRRFIP1]] | -0.48 | -0.26 / -0.47 | both halves | 4e-04 |  |
| [[PITRM1]] | -0.47 | -0.56 / -0.38 | both halves | 7e-05 |  |
| [[UBR4]] | -0.45 | -0.42 / -0.29 | both halves | 2e-04 |  |
| [[SCFD1]] | -0.45 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[ARG2]] | -0.45 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[ACAP2]] | -0.45 | -0.28 / -0.44 | both halves | 3e-04 |  |
| [[FAM53C]] | -0.45 | -0.49 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.189). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (19.0, -3.1); signed map (30.4, -36.9). **Vector** length 72.7, 16.6% of its response variance represented; |z| ≥ 3 in 864 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.6 | +16.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.0 | +13.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.1 | +0.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.3 | -2.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +2.8 | +1.5 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.7 | +1.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.3 | -1.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +1.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.0 | +4.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.9 | +1.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | +1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | +0.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.1 | -0.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.0 | -1.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.8 | +0.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.7 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | MSL complex subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q22.3 — chr3:136,148,917-136,197,241 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10546, KIAA1585, msl-2; previously RNF184, MSL2L1 |
| Gene groups (HGNC) | Ring finger proteins; MSL histone acetyltransferase complex; RING finger E3 ubiquitin protein ligases |
| Reactome | 3 pathways, smallest: HATs acetylate histones; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HCI7](https://www.uniprot.org/uniprotkb/Q9HCI7) (E3 ubiquitin-protein ligase MSL2):

> Non-catalytic component of the MSL histone acetyltransferase complex, a multiprotein complex that mediates the majority of histone H4 acetylation at 'Lys-16' (H4K16ac), an epigenetic mark that prevents chromatin compaction. The MSL complex is required for chromosome stability and genome integrity by maintaining homeostatic levels of H4K16ac. The MSL complex is also involved in gene dosage by promoting up-regulation of genes expressed by the X chromosome (By similarity). X up-regulation is …

**Summary**, from NCBI Gene [55167](https://www.ncbi.nlm.nih.gov/gene/55167):

> Enables histone H2B ubiquitin ligase activity. Involved in DNA damage response and protein monoubiquitination. Located in nucleus. Part of MSL complex. Is active in chromatin. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25544](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25544) · Entrez [55167](https://www.ncbi.nlm.nih.gov/gene/55167) · UniProt [Q9HCI7](https://www.uniprot.org/uniprotkb/Q9HCI7) · Ensembl [ENSG00000174579](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174579)

## Data

Gene col 10506: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10506); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10506, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10506]; `tensor/DDL_lfc|DDL_z.npy` [10506]; `embed/gene_vectors.npy` [10506]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10506 or target_col == 10506). Every well: [[MSL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MSL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
