---
symbol: "UFD1"
type: "gene"
col: 934
ensembl_id: "ENSG00000070010"
name: "ubiquitin recognition factor in ER associated degradation 1"
location: "22q11.21"
module: 72
arm: "+"
pooled_cpm: 42.3
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 2
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# UFD1

*ubiquitin recognition factor in ER associated degradation 1* — 22q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (20 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 4.96× (z +31.3, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.727× (z -8.8, q 9e-16, down in 35 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-427 0.272×, AN3 CA 0.159×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (H4 0.260×, A-427 0.487×; ⚠ cell-cycle shift, would explain all of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.365×); [[Tucidinostat (drug)]] 5 µM in 1 line (C32 0.485×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MBOAT7]] (+0.74, fdr 7e-06), [[TANGO2]] (+0.73, fdr 7e-06), [[BABAM1]] (+0.72, fdr 7e-06); moves opposite to [[PPP4R2]] (-0.66, fdr 1e-05), [[EBAG9]] (-0.62, fdr 7e-06), [[TIGD2]] (-0.61, fdr 1e-05).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 21 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 934.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **4.96×** | +31.3 | 0e+00 | 48/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **4.29×** | +28.5 | 0e+00 | 48/48 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **3.84×** | +24.9 | 0e+00 | 48/48 (SW480, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.53×** | +18.2 | 0e+00 | 48/48 (C32, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.11×** | +14.6 | 0e+00 | 46/48 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **2.04×** | +13.9 | 3e-42 | 37/46 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.65×** | +13.6 | 4e-40 | 45/48 (SW480, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.99×** | +13.5 | 1e-39 | 44/48 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.96×** | +13.2 | 4e-38 | 46/48 (SW480, HOP62, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.85×** | +12.0 | 2e-31 | 43/48 (PANC-1, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.74×** | +10.8 | 2e-25 | 40/47 (PANC-1, LS 180, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **1.77×** | +10.7 | 3e-25 | 32/41 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.73×** | +10.0 | 9e-22 | 42/43 (SW480, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.68×** | +9.4 | 1e-19 | 31/44 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.40×** | +9.4 | 2e-19 | 33/48 (SNU-423, A498, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.18×** | +7.8 | 3e-13 | 41/49 (PANC-1, KATO III, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.43×** | +7.0 | 7e-11 | 37/48 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.39×** | +3.3 | 0.023 | 17/48 (KATO III, LS 180, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.05 µM |  | 1.17× | +3.1 | 0.034 | 15/48 (KATO III, SW 900, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.11× | +2.8 | 0.093 | 10/48 (HT-29, CFPAC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 934.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-427 0.272×, AN3 CA 0.159×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (H4 0.260×, A-427 0.487×; ⚠ cell-cycle shift, would explain all of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.365×); [[Tucidinostat (drug)]] 5 µM in 1 line (C32 0.485×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.727×** | -8.8 | 9e-16 | 35/48 (C32, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.651×** | -8.4 | 2e-14 | 37/48 (LoVo, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | 0.838× | -3.4 | 0.11 | 18/48 (hTERT-HPNE, H4, …) | all doses, stronger at high dose |  |
| [[Omeprazole (drug)]] 0.05 µM |  | 0.851× | -3.1 | 0.25 | 11/48 (RPMI-7951, NCI-H2347, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 934. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 43.7 | 12 (7 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.20× (z +20.1) | — |
| [[LoVo (line)]] | wt | 37.9 | 10 (6 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.95× (z +18.7) | — |
| [[PANC-1 (line)]] | alt | 38.5 | 10 (6 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.08× (z +15.9) | — |
| [[HOP62 (line)]] | alt | 38.9 | 9 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 6.80× (z +18.7) | — |
| [[KATO III (line)]] | alt | 43.0 | 7 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.53× (z +16.4) | — |
| [[HEC-1-A (line)]] | alt | 35.4 | 6 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.84× (z +17.2) | — |
| [[LS 180 (line)]] | wt | 76.7 | 6 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.02× (z +16.7) | — |
| [[SNU-423 (line)]] | alt | 40.1 | 6 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.03× (z +13.8) | — |
| [[A-427 (line)]] | wt | 44.0 | 3 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.79× (z +12.4) | [[Homoharringtonine (drug)]] 0.5 µM 0.272× (z -12.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 41.8 | 4 | 1 | [[Ixazomib citrate (drug)]] 5 µM 5.77× (z +15.7) | [[Tucidinostat (drug)]] 5 µM 0.485× (z -9.1) |
| [[NCI-H1792 (line)]] | alt | 32.6 | 5 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.27× (z +15.1) | — |
| [[NCI-H23 (line)]] | alt | 44.3 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.17× (z +13.8) | — |
| [[NCI-H460 (line)]] | wt | 32.4 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.36× (z +18.3) | — |
| [[Panc 03.27 (line)]] | alt | 70.1 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.89× (z +15.6) | — |
| [[A498 (line)]] | wt | 22.6 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.51× (z +11.2) | — |
| [[CFPAC-1 (line)]] | alt | 27.1 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.72× (z +13.0) | — |
| [[COLO 205 (line)]] | alt | 20.5 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 13.2× (z +12.9) | — |
| [[H4 (line)]] | wt | 24.5 | 3 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 6.04× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 45.5 | 3 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 6.00× (z +14.6) | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.108× (z -9.2) ⚠ toxic |
| [[HT-29 (line)]] | alt | 51.7 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.15× (z +16.8) | — |
| [[NCI-H2030 (line)]] | alt | 58.5 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.12× (z +16.3) | — |
| [[RKO (line)]] | wt | 49.4 | 4 (1 ⚠) | 0 | [[Bortezomib (drug)]] 0.05 µM 3.96× (z +10.6) | — |
| [[SNU-1 (line)]] | wt | 45.8 | 3 | 1 | [[Ixazomib citrate (drug)]] 5 µM 5.73× (z +12.0) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.365× (z -9.8) |
| [[SW 900 (line)]] | alt | 31.7 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.47× (z +11.1) | — |
| [[A549 (line)]] | wt | 28.4 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.30× (z +11.2) | — |
| [[AsPC-1 (line)]] | alt | 46.7 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.31× (z +10.6) | — |
| [[BT-474 (line)]] | alt | 33.0 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.06× (z +10.4) | — |
| [[C-33 A (line)]] | alt | 52.3 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.60× (z +10.3) | — |
| [[HCT15 (line)]] | alt | 39.6 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 7.08× (z +12.7) | — |
| [[HepG2_C3A (line)]] | wt | 34.0 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.67× (z +10.3) | — |
| [[HS-578T (line)]] | alt | 77.7 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.28× (z +10.9) | — |
| [[hTERT-HPNE (line)]] | wt | 33.7 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.44× (z +12.9) | — |
| [[LOX-IMVI (line)]] | wt | 23.1 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.65× (z +13.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 40.1 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.64× (z +14.3) | — |
| [[NCI-H1573 (line)]] | alt | 50.3 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.70× (z +18.7) | — |
| [[NCI-H2347 (line)]] | alt | 49.6 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.33× (z +13.8) | — |
| [[RPMI-7951 (line)]] | alt | 34.7 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.46× (z +12.2) | — |
| [[SK-MEL-2 (line)]] | alt | 68.9 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.70× (z +13.2) | — |
| [[SW1417 (line)]] | alt | 63.7 | 3 | 0 | [[Bortezomib (drug)]] 0.05 µM 3.57× (z +12.9) | — |
| [[SW48 (line)]] | wt | 51.8 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.25× (z +12.4) | — |
| [[A-172 (line)]] | wt | 30.9 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.88× (z +9.0) | — |
| [[SHP-77 (line)]] | alt | 55.4 | 2 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.95× (z +9.1) | — |
| [[AN3 CA (line)]] | alt | 76.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.159× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 30.5 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.74× (z +8.7) | — |
| [[CHP-212 (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 934), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MBOAT7]] | +0.74 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[TANGO2]] | +0.73 | +0.75 / +0.68 | both halves | 7e-06 | STRING 536 |
| [[BABAM1]] | +0.72 | +0.79 / +0.68 | both halves | 7e-06 | pathway: Deubiquitination |
| [[GDAP2]] | +0.70 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[ZNF731P]] | +0.68 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[MAN2B2]] | +0.68 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[PSMB3]] | +0.68 | +0.79 / +0.56 | both halves | 1e-05 | pathway: Cellular response to chemical stress; STRING 664 |
| [[ANKRD39]] | +0.66 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[BCAP31]] | +0.66 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[NPLOC4]] | +0.65 | +0.67 / +0.70 | both halves | 7e-06 | same gene group; pathway: Cellular response to chemical stress; STRING 999 |
| [[PSMD13]] | +0.65 | +0.61 / +0.67 | both halves | 7e-06 | pathway: Cellular response to chemical stress; STRING 655 |
| [[ZCCHC17]] | +0.64 | +0.63 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP4R2]] | -0.66 | -0.49 / -0.65 | both halves | 1e-05 |  |
| [[EBAG9]] | -0.62 | -0.63 / -0.64 | both halves | 7e-06 |  |
| [[TIGD2]] | -0.61 | -0.59 / -0.57 | both halves | 1e-05 |  |
| [[NFKBIA]] | -0.60 | -0.55 / -0.55 | both halves | 1e-05 | pathway: Deubiquitination |
| [[RPP25L]] | -0.59 | -0.62 / -0.49 | both halves | 1e-05 |  |
| [[TGIF2]] | -0.59 | -0.65 / -0.53 | both halves | 1e-05 |  |
| [[CCDC148]] | -0.59 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[DMAC1]] | -0.59 | -0.66 / -0.53 | both halves | 1e-05 |  |
| [[TIFA]] | -0.58 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[NUDCD2]] | -0.58 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[TRMT1L]] | -0.58 | -0.64 / -0.51 | both halves | 1e-05 |  |
| [[PEX12]] | -0.58 | -0.56 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.753). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.3, -8.3); signed map (-27.6, -26.1). **Vector** length 98.4, 28.9% of its response variance represented; |z| ≥ 3 in 1,297 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +11.3 | +31.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +10.8 | +24.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +10.2 | +28.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.7 | +18.2 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +5.8 | +10.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +5.0 | +13.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.9 | -0.3 |
|  | [[Infigratinib (drug)]] 5 µM |  | +1.5 | +2.6 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -8.3 | +0.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -7.9 | -1.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.9 | -1.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -7.6 | +0.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -7.5 | -8.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.0 | -1.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.6 | -3.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.1 | -0.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.4 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin recognition factor in ER associated degradation 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.21 — chr22:19,449,911-19,479,202 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously UFD1L |
| Gene groups (HGNC) | VCP-Ufd1-Npl4 complex subunits |
| Reactome | 17 pathways, smallest: Translesion Synthesis by POLH; Translesion synthesis by Y family DNA polymerases bypasses lesions on DNA template; DNA Damage Bypass |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92890](https://www.uniprot.org/uniprotkb/Q92890) (Ubiquitin recognition factor in ER-associated degradation protein 1):

> Essential component of the ubiquitin-dependent proteolytic pathway which degrades ubiquitin fusion proteins. The ternary complex containing UFD1, VCP and NPLOC4 binds ubiquitinated proteins and is necessary for the export of misfolded proteins from the ER to the cytoplasm, where they are degraded by the proteasome. The NPLOC4-UFD1-VCP complex regulates spindle disassembly at the end of mitosis and is necessary for the formation of a closed nuclear envelope. It may be involved in the development …

**Summary**, from NCBI Gene [7353](https://www.ncbi.nlm.nih.gov/gene/7353):

> The protein encoded by this gene forms a complex with two other proteins, nuclear protein localization-4 and valosin-containing protein, and this complex is necessary for the degradation of ubiquitinated proteins. In addition, this complex controls the disassembly of the mitotic spindle and the formation of a closed nuclear envelope after mitosis. Mutations in this gene have been associated with Catch 22 syndrome as well as cardiac and craniofacial defects. Alternative splicing results in …

**Accessions** — [HGNC:12520](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12520) · Entrez [7353](https://www.ncbi.nlm.nih.gov/gene/7353) · UniProt [Q92890](https://www.uniprot.org/uniprotkb/Q92890) · Ensembl [ENSG00000070010](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000070010)

## Data

Gene col 934: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 934); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 934, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 934]; `tensor/DDL_lfc|DDL_z.npy` [934]; `embed/gene_vectors.npy` [934]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 934 or target_col == 934). Every well: [[UFD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UFD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
