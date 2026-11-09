---
symbol: "TRAPPC8"
type: "gene"
col: 7716
ensembl_id: "ENSG00000153339"
name: "trafficking protein particle complex subunit 8"
location: "18q12.1"
module: 194
arm: "+"
pooled_cpm: 82.32
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 4
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/194"]
generated_by: "tahoemap"
---

# TRAPPC8

*trafficking protein particle complex subunit 8* — 18q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.92× (z +17.6, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.639× (z -8.6, q 4e-15, down in 33 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 0.5 µM: 0.812× (z -4.0, q 0.008, down in 23 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (NCI-H23 0.0997×, SNU-1 0.167×, SHP-77 0.237×, KATO III 0.311×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (RKO 0.109×, NCI-H1573 0.299×, A-427 0.356×, LoVo 0.388×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SW48 0.0859×, NCI-H460 0.362×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ASXL2]] (+0.72, fdr 7e-06), [[ATE1]] (+0.67, fdr 1e-05), [[NUTM2B-AS1]] (+0.65, fdr 3e-05); moves opposite to [[GPR160]] (-0.62, fdr 1e-05), [[GIPR]] (-0.59, fdr 1e-05), [[RAB3A]] (-0.58, fdr 5e-05).
> It sits in the **+** arm of [[Module 194]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7716.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.92×** | +17.6 | 0e+00 | 46/48 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.46×** | +17.2 | 0e+00 | 48/48 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.02×** | +13.4 | 7e-39 | 47/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.85×** | +11.8 | 6e-30 | 46/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.80×** | +11.2 | 4e-27 | 44/47 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.74×** | +8.5 | 2e-15 | 42/49 (NCI-H460, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.55×** | +8.1 | 6e-14 | 39/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.48×** | +7.5 | 5e-12 | 38/48 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.39×** | +6.3 | 2e-08 | 37/48 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.09×** | +6.2 | 4e-08 | 36/48 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.37×** | +6.0 | 1e-07 | 35/48 (HOP62, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.34×** | +5.6 | 1e-06 | 37/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +5.3 | 5e-06 | 32/48 (NCI-H23, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.38×** | +4.6 | 1e-04 | 31/48 (PANC-1, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.27×** | +4.5 | 2e-04 | 27/48 (NCI-H460, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +4.3 | 7e-04 | 17/48 (NCI-H2347, HOP62, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7716.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (NCI-H23 0.0997×, SNU-1 0.167×, SHP-77 0.237×, KATO III 0.311×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (RKO 0.109×, NCI-H1573 0.299×, A-427 0.356×, LoVo 0.388×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SW48 0.0859×, NCI-H460 0.362×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.639×** | -8.6 | 4e-15 | 33/49 (RKO, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.677×** | -7.2 | 1e-10 | 33/44 (NCI-H23, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.667×** | -6.5 | 1e-08 | 31/45 (SW48, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.812×** | -4.0 | 0.008 | 23/49 (SW 1271, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | 0.836× | -3.5 | 0.058 | 20/48 (RPMI-7951, COLO 205, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.884× | -3.4 | 0.066 | 12/48 (NCI-H1792, NCI-H2030, …) | two highest doses |  |
| [[Decitabine (drug)]] 0.5 µM |  | 0.851× | -3.1 | 0.14 | 15/48 (AN3 CA, SW48, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7716. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 78.2 | 9 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +20.6) | [[Dinaciclib (drug)]] 0.05 µM 0.362× (z -10.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 84.2 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.311× (z -13.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 84.9 | 4 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.21× (z +13.4) | [[Dinaciclib (drug)]] 0.5 µM 0.388× (z -10.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 102 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.13× (z +12.0) | — |
| [[HOP62 (line)]] | alt | 53.6 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.96× (z +12.4) | — |
| [[NCI-H23 (line)]] | alt | 148 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +15.1) | [[Dinaciclib (drug)]] 5 µM 0.0997× (z -28.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 81.3 | 4 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.58× (z +12.6) | — |
| [[RKO (line)]] | wt | 105 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +15.8) | [[Dinaciclib (drug)]] 0.5 µM 0.109× (z -21.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 77.2 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.413× (z -10.2) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 67.1 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.35× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.217× (z -11.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 84.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.469× (z -8.7) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 65.2 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.74× (z +13.4) | — |
| [[LOX-IMVI (line)]] | wt | 105 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +12.8) | — |
| [[NCI-H1792 (line)]] | alt | 126 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.16× (z +13.1) | — |
| [[Panc 03.27 (line)]] | alt | 192 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.98× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.415× (z -10.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 51.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +11.4) | — |
| [[SW480 (line)]] | alt | 44.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +10.3) | — |
| [[A-427 (line)]] | wt | 144 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.356× (z -12.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 73.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -10.5) ⚠ cell-cycle shift, explains ~6% of this change |
| [[CFPAC-1 (line)]] | alt | 51.2 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.77× (z +9.4) | — |
| [[COLO 205 (line)]] | alt | 57.7 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.12× (z +11.2) | — |
| [[HCT15 (line)]] | alt | 77.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +10.1) | — |
| [[HepG2_C3A (line)]] | wt | 74.6 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.77× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.365× (z -8.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 80.2 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +10.4) | — |
| [[J82 (line)]] | alt | 85.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +11.1) | — |
| [[LS 180 (line)]] | wt | 105 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.68× (z +13.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 96.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +14.5) | — |
| [[NCI-H1573 (line)]] | alt | 127 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +14.1) | [[Dinaciclib (drug)]] 0.5 µM 0.299× (z -15.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 100 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.77× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.167× (z -15.3) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 101 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0859× (z -17.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 64.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +12.1) | — |
| [[AsPC-1 (line)]] | alt | 92.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +10.9) | — |
| [[C32 (line)]] | wt | 78.8 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0864× (z -10.3) ⚠ toxic |
| [[HS-578T (line)]] | alt | 68.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +8.7) | — |
| [[hTERT-HPNE (line)]] | wt | 65.3 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.11× (z +9.8) | — |
| [[NCI-H2030 (line)]] | alt | 38.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +10.6) | — |
| [[NCI-H2347 (line)]] | alt | 58.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +14.2) | — |
| [[RPMI-7951 (line)]] | alt | 61.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +9.3) | — |
| [[SHP-77 (line)]] | alt | 112 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -14.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 79.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +10.7) | — |
| [[SW 900 (line)]] | alt | 39.5 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.68× (z +8.6) | — |
| [[AN3 CA (line)]] | alt | 112 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 90.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 96.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 83.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 81.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 94.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 80.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7716), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASXL2]] | +0.72 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[ATE1]] | +0.67 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[NUTM2B-AS1]] | +0.65 | +0.70 / +0.44 | both halves | 3e-05 |  |
| [[ATAD2B]] | +0.63 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[CREBBP]] | +0.63 | +0.51 / +0.46 | both halves | 2e-05 |  |
| [[CPSF2]] | +0.62 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[MED13]] | +0.60 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[ZMYND11]] | +0.60 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[NSD1]] | +0.60 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[RAB28]] | +0.59 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[ARID1B]] | +0.59 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[MED1]] | +0.58 | +0.56 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPR160]] | -0.62 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[GIPR]] | -0.59 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[RAB3A]] | -0.58 | -0.52 / -0.39 | both halves | 5e-05 | pathway: RAB GEFs exchange GTP for GDP on RABs |
| [[FCHO1]] | -0.58 | -0.50 / -0.39 | both halves | 6e-05 |  |
| [[ABCB9]] | -0.58 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[GNAI3]] | -0.57 | -0.54 / -0.31 | both halves | 2e-04 |  |
| [[FSCN1]] | -0.56 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[PLCD1]] | -0.56 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[AHDC1]] | -0.55 | -0.51 / -0.39 | both halves | 6e-05 |  |
| [[RADX]] | -0.54 | -0.42 / -0.37 | both halves | 8e-05 |  |
| [[TSPAN13]] | -0.54 | -0.43 / -0.36 | both halves | 1e-04 |  |
| [[SNAI1]] | -0.54 | -0.37 / -0.54 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 194]]; 17 genes; this gene is in the **+** arm (projection on the module's main direction 0.728). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-6.8, 3.7); signed map (19.3, -29.1). **Vector** length 78.0, 20.8% of its response variance represented; |z| ≥ 3 in 1,010 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +4.4 | +17.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +4.2 | +11.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +4.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +5.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +11.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.0 | -0.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +1.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.8 | +1.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.8 | +1.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.5 | -3.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.5 | -4.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | +0.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | +1.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -0.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | -2.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.2 | -1.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.1 | +0.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.0 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | trafficking protein particle complex subunit 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q12.1 — chr18:31,829,197-31,953,136 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HsT2706, TRS85, GSG1; previously KIAA1012 |
| Gene groups (HGNC) | Trafficking protein particle complex subunits |
| Reactome | 4 pathways, smallest: RAB GEFs exchange GTP for GDP on RABs; Rab regulation of trafficking; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2L5](https://www.uniprot.org/uniprotkb/Q9Y2L5) (Trafficking protein particle complex subunit 8):

> Plays a role in endoplasmic reticulum to Golgi apparatus trafficking at a very early stage. Maintains together with TBC1D14 the cycling pool of ATG9 required for initiation of autophagy. Involved in collagen secretion.

**Summary**, from NCBI Gene [22878](https://www.ncbi.nlm.nih.gov/gene/22878):

> Involved in Golgi organization and collagen biosynthetic process. Part of TRAPP complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29169](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29169) · Entrez [22878](https://www.ncbi.nlm.nih.gov/gene/22878) · UniProt [Q9Y2L5](https://www.uniprot.org/uniprotkb/Q9Y2L5) · Ensembl [ENSG00000153339](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153339)

## Data

Gene col 7716: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7716); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7716, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7716]; `tensor/DDL_lfc|DDL_z.npy` [7716]; `embed/gene_vectors.npy` [7716]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7716 or target_col == 7716). Every well: [[TRAPPC8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRAPPC8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
