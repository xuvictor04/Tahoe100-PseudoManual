---
symbol: "GGA2"
type: "gene"
col: 2361
ensembl_id: "ENSG00000103365"
name: "golgi associated, gamma adaptin ear containing, ARF binding protein 2"
location: "16p12.2"
module: 164
arm: "+"
pooled_cpm: 74.53
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 3
n_dd_up_clean: 19
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/164"]
generated_by: "tahoemap"
---

# GGA2

*golgi associated, gamma adaptin ear containing, ARF binding protein 2* — 16p12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.96× (z +11.3, q 7e-27, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.495× (z -11.4, q 3e-27, down in 39 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Busulfan (drug)]] 0.05 µM: 0.794× (z -3.6, q 0.056, down in 27 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (SNU-1 0.200×, HCT15 0.226×, SK-MEL-2 0.251×, NCI-H23 0.308×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (C-33 A 0.320×, A-172 0.325×, NCI-H1573 0.308×, AN3 CA 0.193×, …; ⚠ toxic; transcription drop); [[Methylthiouracil (drug)]] 5 µM in 1 line (NCI-H596 0.0907×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (NCI-H661 0.0980×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SRP54-AS1]] (+0.70, fdr 7e-06), [[DHRS13]] (+0.70, fdr 7e-06), [[PDK3]] (+0.67, fdr 7e-06); moves opposite to [[PTPN21]] (-0.60, fdr 1e-05), [[TJP1]] (-0.59, fdr 1e-05), [[REEP3]] (-0.58, fdr 2e-05).
> It is in [[Module 164]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2361.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.96×** | +11.3 | 7e-27 | 41/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.80×** | +9.9 | 2e-20 | 39/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.75×** | +9.4 | 9e-19 | 41/48 (NCI-H1573, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.55×** | +8.2 | 3e-14 | 45/49 (COLO 205, AsPC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.53×** | +8.2 | 4e-14 | 41/48 (A-427, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +7.9 | 3e-13 | 31/49 (PANC-1, HOP62, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.58×** | +7.7 | 9e-13 | 39/48 (NCI-H1573, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.56×** | +7.5 | 5e-12 | 36/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.54×** | +7.2 | 4e-11 | 38/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.37×** | +7.1 | 6e-11 | 38/48 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.52×** | +7.1 | 8e-11 | 38/48 (NCI-H1573, LOX-IMVI, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.51×** | +6.9 | 2e-10 | 35/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.47×** | +6.1 | 6e-08 | 32/48 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.72×** | +4.7 | 8e-05 | 28/45 (NCI-H460, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.28×** | +4.1 | 0.002 | 23/48 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.27×** | +3.9 | 0.004 | 24/48 (A498, A-427, …) | top dose only | cell-cycle shift (explains ~6% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +3.8 | 0.005 | 25/48 (PANC-1, SK-MEL-2, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.23×** | +3.3 | 0.025 | 19/49 (NCI-H1792, SW 900, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2361.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (SNU-1 0.200×, HCT15 0.226×, SK-MEL-2 0.251×, NCI-H23 0.308×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (C-33 A 0.320×, A-172 0.325×, NCI-H1573 0.308×, AN3 CA 0.193×, …; ⚠ toxic; transcription drop); [[Methylthiouracil (drug)]] 5 µM in 1 line (NCI-H596 0.0907×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (NCI-H661 0.0980×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.495×** | -11.4 | 3e-27 | 39/44 (C-33 A, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.581×** | -9.1 | 2e-17 | 39/49 (SNU-1, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Busulfan (drug)]] 0.05 µM |  | **0.794×** | -3.6 | 0.056 | 27/49 (H4, SW1417, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.807× | -3.4 | 0.10 | 22/48 (HOP62, H4, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.812× | -3.3 | 0.10 | 20/49 (PANC-1, A-172, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | 0.813× | -3.2 | 0.10 | 21/48 (Panc 03.27, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Thymol (drug)]] 5 µM |  | 0.866× | -3.2 | 0.10 | 14/48 (NCI-H661, SNU-423, …) | top dose only |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | 0.816× | -3.2 | 0.10 | 13/49 (HOP62, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2361. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 63.1 | 9 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.32× (z +15.1) | — |
| [[NCI-H1573 (line)]] | alt | 60.4 | 5 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.35× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.308× (z -11.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 73.4 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.58× (z +16.9) | — |
| [[SW1417 (line)]] | alt | 70.2 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.93× (z +11.1) | — |
| [[SW480 (line)]] | alt | 65.7 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.53× (z +13.0) | — |
| [[AsPC-1 (line)]] | alt | 71.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +12.8) | — |
| [[KATO III (line)]] | alt | 66.9 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.86× (z +16.2) | — |
| [[A-172 (line)]] | wt | 69.2 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +19.0) | [[Dinaciclib (drug)]] 5 µM 0.325× (z -11.1) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 119 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.167× (z -11.2) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 66.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +12.3) | — |
| [[J82 (line)]] | alt | 90.3 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.36× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.326× (z -9.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 44.8 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.06× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.329× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 68.9 | 2 | 1 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.38× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -13.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 76.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.334× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 88.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +14.9) | — |
| [[HT-29 (line)]] | alt | 59.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +9.9) | — |
| [[NCI-H1792 (line)]] | alt | 75.5 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.80× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.70× (z +9.3) | — |
| [[SHP-77 (line)]] | alt | 49.4 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.86× (z +9.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.58× (z +8.5) | — |
| [[SNU-1 (line)]] | wt | 120 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -15.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 68.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +8.9) | — |
| [[AN3 CA (line)]] | alt | 127 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -10.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 69.4 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.16× (z +10.1) | — |
| [[C-33 A (line)]] | alt | 106 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.320× (z -11.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 111 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.334× (z -9.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 75.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.360× (z -9.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 131 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -14.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 130 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.362× (z -10.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 56.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +8.9) | — |
| [[NCI-H596 (line)]] | alt | 83.0 | 0 | 1 | — | [[Methylthiouracil (drug)]] 5 µM 0.0907× (z -12.6) |
| [[NCI-H661 (line)]] | alt | 73.8 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0980× (z -10.0) |
| [[SK-MEL-2 (line)]] | alt | 87.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -14.4) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 110 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 93.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 81.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 75.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 63.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 48.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 88.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 75.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 77.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 76.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 66.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 79.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 92.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 79.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 87.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2361), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRP54-AS1]] | +0.70 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[DHRS13]] | +0.70 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[PDK3]] | +0.67 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[UBE2O]] | +0.65 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[TRIT1]] | +0.65 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[PEX3]] | +0.64 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[RNASET2]] | +0.64 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[ATPAF2]] | +0.63 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[POM121]] | +0.63 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[SAP30-DT]] | +0.63 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[MMS19]] | +0.63 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[HDHD5]] | +0.63 | +0.61 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPN21]] | -0.60 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[TJP1]] | -0.59 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[REEP3]] | -0.58 | -0.46 / -0.56 | both halves | 2e-05 |  |
| [[ZBTB38]] | -0.56 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[ROCK2]] | -0.56 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[C3orf62]] | -0.54 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[SKIL]] | -0.54 | -0.53 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 164]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.736). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.37; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (9.5, -18.9); signed map (-38.5, 22.1). **Vector** length 89.9, 26.3% of its response variance represented; |z| ≥ 3 in 1,037 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +7.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.9 | +3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.6 | +1.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.5 | -0.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +0.7 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +2.4 | +2.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.6 | +2.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.3 | -1.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.8 | +3.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.6 | +7.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | +0.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.8 | +0.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.4 | -1.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.3 | -0.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.2 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | golgi associated, gamma adaptin ear containing, ARF binding protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p12.2 — chr16:23,463,542-23,521,995 (-) |
| Ensembl biotype | protein_coding |
| Also known as | VEAR, KIAA1080 |
| Gene groups (HGNC) | Golgi associated, gamma adaptin ear containing, ARF binding proteins |
| Hallmark sets | MTORC1_SIGNALING |
| Reactome | 5 pathways, smallest: TBC/RABGAPs; Amyloid fiber formation; Rab regulation of trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UJY4](https://www.uniprot.org/uniprotkb/Q9UJY4) (ADP-ribosylation factor-binding protein GGA2):

> Plays a role in protein sorting and trafficking between the trans-Golgi network (TGN) and endosomes. Mediates the ARF-dependent recruitment of clathrin to the TGN and binds ubiquitinated proteins and membrane cargo molecules with a cytosolic acidic cluster-dileucine (DXXLL) motif. Mediates export of the GPCR receptor ADRA2B to the cell surface. Regulates retrograde transport of phosphorylated form of BACE1 from endosomes to the trans-Golgi network.

**Summary**, from NCBI Gene [23062](https://www.ncbi.nlm.nih.gov/gene/23062):

> This gene encodes a member of the Golgi-localized, gamma adaptin ear-containing, ARF-binding (GGA) family. This family includes ubiquitous coat proteins that regulate the trafficking of proteins between the trans-Golgi network and the lysosome. These proteins share an amino-terminal VHS domain which mediates sorting of the mannose 6-phosphate receptors at the trans-Golgi network. They also contain a carboxy-terminal region with homology to the ear domain of gamma-adaptins. This family member …

**Accessions** — [HGNC:16064](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16064) · Entrez [23062](https://www.ncbi.nlm.nih.gov/gene/23062) · UniProt [Q9UJY4](https://www.uniprot.org/uniprotkb/Q9UJY4) · Ensembl [ENSG00000103365](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103365)

## Data

Gene col 2361: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2361); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2361, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2361]; `tensor/DDL_lfc|DDL_z.npy` [2361]; `embed/gene_vectors.npy` [2361]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2361 or target_col == 2361). Every well: [[GGA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GGA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
