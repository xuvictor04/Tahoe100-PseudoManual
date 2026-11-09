---
symbol: "ATP6V1H"
type: "gene"
col: 511
ensembl_id: "ENSG00000047249"
name: "ATPase H+ transporting V1 subunit H"
location: "8q11.23"
module: 122
arm: "+"
pooled_cpm: 74.23
n_lines_expressing: 50
n_dd_up: 38
n_dd_down: 4
n_dd_up_clean: 32
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/122"]
generated_by: "tahoemap"
---

# ATP6V1H

*ATPase H+ transporting V1 subunit H* — 8q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.22× (z +28.1, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.556× (z -9.6, q 3e-19, down in 31 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.709× (z -8.3, q 2e-14, down in 41 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (A-427 0.173×, LoVo 0.259×, SNU-1 0.132×, HEC-1-A 0.368×, …; ⚠ toxic; transcription drop); [[Tucidinostat (drug)]] 5 µM in 5 lines (C32 0.490×, SW480 0.632×, HOP62 0.515×, LS 180 0.494×, …); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (COLO 205 0.0963×, NCI-H2347 0.285×, SW1417 0.295×, SNU-1 0.255×; ⚠ toxic; transcription drop); [[Tucidinostat (drug)]] 0.5 µM in 2 lines (SW480 0.550×, C32 0.409×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HEXA]] (+0.71, fdr 7e-06), [[FAM204A]] (+0.65, fdr 7e-06), [[ATP6V1A]] (+0.65, fdr 7e-06); moves opposite to [[ADARB1]] (-0.57, fdr 4e-05), [[DOT1L]] (-0.57, fdr 1e-05), [[NUP98]] (-0.53, fdr 3e-05).
> It is in [[Module 122]], a single-armed module (Transferrin endocytosis and recycling).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 511.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.22×** | +28.1 | 0e+00 | 48/48 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **10.3×** | +18.8 | 0e+00 | 48/49 (SW480, PANC-1, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.34×** | +14.4 | 6e-45 | 44/48 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.81×** | +14.2 | 6e-44 | 44/48 (PANC-1, HT-29, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[PH-797804 (drug)]] 5 µM |  | **5.23×** | +13.3 | 2e-38 | 45/48 (SW480, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.15×** | +13.0 | 9e-37 | 42/48 (KATO III, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.81×** | +10.1 | 4e-22 | 44/48 (KATO III, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.83×** | +9.9 | 3e-21 | 43/48 (J82, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **1.78×** | +9.8 | 5e-21 | 44/48 (LS 180, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.80×** | +9.4 | 3e-19 | 42/48 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +9.4 | 3e-19 | 38/49 (LS 180, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.72×** | +9.2 | 2e-18 | 34/47 (KATO III, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.70×** | +9.0 | 1e-17 | 43/49 (LS 180, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +8.2 | 7e-15 | 37/48 (SK-MEL-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.57×** | +7.7 | 6e-13 | 40/48 (KATO III, LS 180, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.56×** | +7.6 | 1e-12 | 40/48 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~11% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 511.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (A-427 0.173×, LoVo 0.259×, SNU-1 0.132×, HEC-1-A 0.368×, …; ⚠ toxic; transcription drop); [[Tucidinostat (drug)]] 5 µM in 5 lines (C32 0.490×, SW480 0.632×, HOP62 0.515×, LS 180 0.494×, …); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (COLO 205 0.0963×, NCI-H2347 0.285×, SW1417 0.295×, SNU-1 0.255×; ⚠ toxic; transcription drop); [[Tucidinostat (drug)]] 0.5 µM in 2 lines (SW480 0.550×, C32 0.409×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.556×** | -9.6 | 3e-19 | 31/42 (A-427, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.709×** | -8.3 | 2e-14 | 41/48 (C32, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.680×** | -6.6 | 7e-09 | 37/49 (SW480, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.814×** | -3.5 | 0.056 | 24/49 (COLO 205, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Carbamazepine (drug)]] 5 µM |  | 0.829× | -3.2 | 0.14 | 19/47 (A498, hTERT-HPNE, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 511. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 84.3 | 12 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.32× (z +18.6) | [[Dinaciclib (drug)]] 5 µM 0.388× (z -10.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 70.4 | 11 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +18.9) | [[Tucidinostat (drug)]] 5 µM 0.632× (z -9.7) |
| [[NCI-H460 (line)]] | wt | 49.6 | 12 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.74× (z +30.3) | — |
| [[PANC-1 (line)]] | alt | 52.6 | 12 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +15.5) | — |
| [[LS 180 (line)]] | wt | 83.9 | 9 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +12.2) | [[Tucidinostat (drug)]] 5 µM 0.494× (z -9.4) |
| [[LoVo (line)]] | wt | 73.2 | 5 | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.75× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.259× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 0.584× (z -8.8) |
| [[A-427 (line)]] | wt | 54.6 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +19.3) | [[Dinaciclib (drug)]] 5 µM 0.173× (z -15.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 49.8 | 6 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +18.9) | [[Tucidinostat (drug)]] 5 µM 0.515× (z -9.5) |
| [[HT-29 (line)]] | alt | 76.6 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +17.9) | — |
| [[HEC-1-A (line)]] | alt | 84.0 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +15.8) | [[Dinaciclib (drug)]] 5 µM 0.368× (z -10.4) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 66.0 | 6 | 0 | [[TAK-901 (drug)]] 0.05 µM 3.75× (z +13.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 85.4 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +16.6) | [[Dinaciclib (drug)]] 5 µM 0.347× (z -10.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 55.3 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +19.4) | [[Dinaciclib (drug)]] 5 µM 0.383× (z -9.0) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 84.6 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +14.6) | [[Dinaciclib (drug)]] 0.5 µM 0.0963× (z -20.4) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 90.4 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.04× (z +23.8) | — |
| [[NCI-H1573 (line)]] | alt | 36.4 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +17.2) | — |
| [[NCI-H23 (line)]] | alt | 52.2 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.42× (z +22.5) | — |
| [[NCI-H2347 (line)]] | alt | 107 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +20.3) | [[Dinaciclib (drug)]] 0.5 µM 0.285× (z -13.4) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 87.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +11.0) | — |
| [[Hs 766T (line)]] | wt | 76.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.71× (z +20.3) | — |
| [[Panc 03.27 (line)]] | alt | 83.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.38× (z +21.0) | — |
| [[RKO (line)]] | wt | 121 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +16.7) | — |
| [[A498 (line)]] | wt | 118 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +15.4) | — |
| [[A549 (line)]] | wt | 43.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +16.0) | — |
| [[HS-578T (line)]] | alt | 61.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.46× (z +17.8) | — |
| [[hTERT-HPNE (line)]] | wt | 47.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.04× (z +15.3) | — |
| [[SK-MEL-2 (line)]] | alt | 50.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.69× (z +16.7) | — |
| [[SNU-1 (line)]] | wt | 104 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.132× (z -13.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 86.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +16.6) | — |
| [[SW1417 (line)]] | alt | 88.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +16.4) | [[Dinaciclib (drug)]] 0.5 µM 0.295× (z -11.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 117 | 0 | 2 | — | [[Tucidinostat (drug)]] 5 µM 0.490× (z -9.7) |
| [[CFPAC-1 (line)]] | alt | 57.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +13.0) | — |
| [[H4 (line)]] | wt | 41.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +10.0) | — |
| [[NCI-H1792 (line)]] | alt | 42.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +12.8) | — |
| [[SW 900 (line)]] | alt | 110 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +12.7) | — |
| [[SW48 (line)]] | wt | 85.4 | 2 | 0 | [[TAK-901 (drug)]] 0.05 µM 4.34× (z +9.9) | — |
| [[AsPC-1 (line)]] | alt | 59.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +13.6) | — |
| [[HCT15 (line)]] | alt | 79.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +10.6) | — |
| [[NCI-H2030 (line)]] | alt | 111 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +9.7) | — |
| [[RPMI-7951 (line)]] | alt | 72.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +11.7) | — |
| [[SHP-77 (line)]] | alt | 103 | 1 | 0 | [[Selinexor (drug)]] 5 µM 1.86× (z +9.4) | — |
| [[AN3 CA (line)]] | alt | 182 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 71.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 53.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 97.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 85.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 93.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 59.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 511), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HEXA]] | +0.71 | +0.59 / +0.72 | both halves | 7e-06 |  |
| [[FAM204A]] | +0.65 | +0.74 / +0.58 | both halves | 7e-06 |  |
| [[ATP6V1A]] | +0.65 | +0.72 / +0.62 | both halves | 7e-06 | same gene group; pathway: Amino acids regulate mTORC1; STRING 999 |
| [[RAB21]] | +0.62 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[WASHC2C]] | +0.62 | +0.47 / +0.67 | both halves | 2e-05 |  |
| [[EAF1]] | +0.60 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[HPS1]] | +0.60 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[WASHC2A]] | +0.59 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[SUPV3L1]] | +0.59 | +0.50 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |
| [[ATP6V0E1]] | +0.59 | +0.59 / +0.58 | both halves | 7e-06 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 997 |
| [[SPNS1]] | +0.59 | +0.44 / +0.64 | both halves | 3e-05 |  |
| [[RRAGB]] | +0.59 | +0.60 / +0.57 | both halves | 1e-05 | pathway: Amino acids regulate mTORC1; STRING 623 |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADARB1]] | -0.57 | -0.60 / -0.41 | both halves | 4e-05 |  |
| [[DOT1L]] | -0.57 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[NUP98]] | -0.53 | -0.49 / -0.45 | both halves | 3e-05 | pathway: HIV Infection |
| [[DGKD]] | -0.52 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[R3HDM4]] | -0.51 | -0.52 / -0.39 | both halves | 6e-05 |  |
| [[SEPTIN10]] | -0.51 | -0.60 / -0.41 | both halves | 4e-05 |  |
| [[EDEM3]] | -0.51 | -0.37 / -0.51 | both halves | 9e-05 |  |
| [[ODF2]] | -0.51 | -0.67 / -0.35 | both halves | 1e-04 |  |
| [[SLC4A7]] | -0.51 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[CEP85]] | -0.50 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[AREG]] | -0.49 | -0.54 / -0.33 | both halves | 1e-04 |  |
| [[EHD4]] | -0.49 | -0.48 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 122]] — Transferrin endocytosis and recycling; 40 genes; every member is in the + arm (projection on the module's main direction 0.697). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-19.7, 14.1); signed map (-9.7, -19.1). **Vector** length 102, 35.7% of its response variance represented; |z| ≥ 3 in 1,395 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +14.9 | +14.2 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +9.7 | +9.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | +7.2 | +18.8 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +6.6 | +9.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.9 | +2.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +4.6 | +5.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.3 | +13.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.1 | +2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.5 | +7.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -10.5 | -8.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -7.8 | -6.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.9 | +5.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.2 | +6.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.7 | +3.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.2 | -1.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.9 | -2.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.8 | +0.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | ATPase H+ transporting V1 subunit H |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q11.23 — chr8:53,715,543-53,843,558 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-11, SFD, VMA13, SFDalpha, SFDbeta |
| Gene groups (HGNC) | V-type ATPase subunits; Armadillo like helical domain containing |
| Hallmark sets | PROTEIN_SECRETION, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 27 pathways, smallest: Nef Mediated CD8 Down-regulation; Nef Mediated CD4 Down-regulation; Suppression of phagosomal maturation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UI12](https://www.uniprot.org/uniprotkb/Q9UI12) (V-type proton ATPase subunit H):

> Subunit of the V1 complex of vacuolar(H+)-ATPase (V-ATPase), a multisubunit enzyme composed of a peripheral complex (V1) that hydrolyzes ATP and a membrane integral complex (V0) that translocates protons. V-ATPase is responsible for acidifying and maintaining the pH of intracellular compartments and in some cell types, is targeted to the plasma membrane, where it promotes acidification of the extracellular environment (By similarity). The V-ATPase complex also acts as an activator for mTORC1 on …

**Summary**, from NCBI Gene [51606](https://www.ncbi.nlm.nih.gov/gene/51606):

> This gene encodes a component of vacuolar ATPase (V-ATPase), a multisubunit enzyme that mediates acidification of intracellular organelles. V-ATPase-dependent organelle acidification is necessary for multiple processes including protein sorting, zymogen activation, receptor-mediated endocytosis, and synaptic vesicle proton gradient generation. The encoded protein is the regulatory H subunit of the V1 domain of V-ATPase, which is required for catalysis of ATP but not the assembly of V-ATPase. …

**Accessions** — [HGNC:18303](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18303) · Entrez [51606](https://www.ncbi.nlm.nih.gov/gene/51606) · UniProt [Q9UI12](https://www.uniprot.org/uniprotkb/Q9UI12) · Ensembl [ENSG00000047249](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000047249)

## Data

Gene col 511: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 511); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 511, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 511]; `tensor/DDL_lfc|DDL_z.npy` [511]; `embed/gene_vectors.npy` [511]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 511 or target_col == 511). Every well: [[ATP6V1H — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP6V1H.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
