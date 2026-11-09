---
symbol: "LSG1"
type: "gene"
col: 477
ensembl_id: "ENSG00000041802"
name: "large 60S subunit nuclear export GTPase 1"
location: "3q29"
module: 4
arm: "+"
pooled_cpm: 53.64
n_lines_expressing: 50
n_dd_up: 44
n_dd_down: 2
n_dd_up_clean: 26
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# LSG1

*large 60S subunit nuclear export GTPase 1* — 3q29

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 44 drug-doses (18 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 10.2× (z +23.4, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.913× (z -5.8, q 3e-06, down in 4 of 49 measured lines) ⚠ position not correctable. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 2 lines (MIA PaCa-2 0.719×, HOP62 0.727×; ⚠ position not correctable); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.400×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SNU-1 0.217×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BYSL]] (+0.77, fdr 7e-06), [[POLR1A]] (+0.77, fdr 7e-06), [[TWNK]] (+0.75, fdr 7e-06); moves opposite to [[LNX2]] (-0.63, fdr 7e-06), [[ABCA5]] (-0.62, fdr 1e-05), [[TXNDC16]] (-0.62, fdr 3e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 21 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 44 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 477.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **10.2×** | +23.4 | 0e+00 | 48/49 (SW480, LoVo, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.78×** | +19.7 | 0e+00 | 48/48 (HOP62, SW480, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **5.98×** | +18.0 | 0e+00 | 47/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.45×** | +17.3 | 0e+00 | 47/48 (HOP62, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.78×** | +15.7 | 0e+00 | 38/48 (NCI-H2347, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **2.20×** | +15.1 | 0e+00 | 48/48 (HOP62, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.08×** | +14.1 | 5e-43 | 40/48 (NCI-H2347, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.06×** | +13.9 | 7e-42 | 46/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.94×** | +12.8 | 1e-35 | 45/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.89×** | +12.2 | 1e-32 | 43/48 (SK-MEL-2, SW480, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.86×** | +11.9 | 3e-31 | 42/48 (NCI-H1573, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.93×** | +11.9 | 3e-31 | 43/48 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.91×** | +11.9 | 3e-31 | 42/48 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.64×** | +9.5 | 9e-20 | 36/47 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.62×** | +9.3 | 8e-19 | 40/48 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.52×** | +8.1 | 2e-14 | 37/48 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +7.6 | 9e-13 | 32/48 (HS-578T, CFPAC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.48×** | +7.5 | 1e-12 | 39/48 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.50×** | +7.3 | 7e-12 | 33/47 (HEC-1-A, SW1417, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.54×** | +5.9 | 8e-08 | 33/48 (PANC-1, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.32×** | +5.1 | 7e-06 | 23/48 (NCI-H1792, MIA PaCa-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.28×** | +4.8 | 3e-05 | 25/48 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 477.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 2 lines (MIA PaCa-2 0.719×, HOP62 0.727×; ⚠ position not correctable); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.400×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SNU-1 0.217×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.913× | -5.8 | 3e-06 | 4/49 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.757×** | -5.4 | 2e-05 | 29/48 (A498, CHP-212, …) | all doses, flat |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.820×** | -3.9 | 0.020 | 15/48 (NCI-H2347, HS-578T, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.846× | -3.1 | 0.19 | 15/47 (SK-MEL-2, A498, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.870× | -3.1 | 0.19 | 11/48 (CHP-212, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 0.839× | -3.0 | 0.23 | 16/48 (SW48, A498, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.46 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 477. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 85.7 | 14 (6 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 12.1× (z +18.8) | — |
| [[HOP62 (line)]] | alt | 34.6 | 9 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.01× (z +14.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 16.1× (z +12.6) | — |
| [[LS 180 (line)]] | wt | 52.7 | 9 (5 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 16.3× (z +13.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 50.2 | 9 (4 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 22.3× (z +14.2) | — |
| [[NCI-H1573 (line)]] | alt | 41.2 | 9 (8 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.50× (z +11.9) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 10.1× (z +11.5) | — |
| [[PANC-1 (line)]] | alt | 103 | 9 (4 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 9.07× (z +13.7) | — |
| [[HS-578T (line)]] | alt | 65.0 | 8 (4 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 10.8× (z +12.5) | — |
| [[NCI-H2347 (line)]] | alt | 44.7 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +12.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 8.33× (z +12.0) | — |
| [[CFPAC-1 (line)]] | alt | 32.6 | 7 (5 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 19.7× (z +13.1) | — |
| [[LoVo (line)]] | wt | 51.6 | 7 (4 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 14.1× (z +16.3) | — |
| [[NCI-H1792 (line)]] | alt | 26.2 | 7 (5 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.93× (z +10.3) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 13.5× (z +10.2) | — |
| [[A-172 (line)]] | wt | 35.9 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +11.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 8.13× (z +9.8) | — |
| [[LOX-IMVI (line)]] | wt | 33.1 | 6 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.13× (z +10.6) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 15.0× (z +10.6) | — |
| [[NCI-H460 (line)]] | wt | 31.7 | 6 (4 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 8.93× (z +10.5) | — |
| [[Panc 03.27 (line)]] | alt | 69.6 | 6 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 16.8× (z +15.3) | — |
| [[SNU-423 (line)]] | alt | 29.7 | 6 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.07× (z +10.2) | — |
| [[COLO 205 (line)]] | alt | 45.1 | 5 (3 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 42.3× (z +14.3) | — |
| [[HEC-1-A (line)]] | alt | 47.9 | 5 (1 ⚠) | 0 | [[TAK-901 (drug)]] 0.05 µM 5.06× (z +14.5) | — |
| [[KATO III (line)]] | alt | 81.2 | 5 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 12.8× (z +14.6) | — |
| [[SK-MEL-2 (line)]] | alt | 105 | 5 | 0 | [[Auranofin (drug)]] 5 µM 3.89× (z +13.9) | — |
| [[AsPC-1 (line)]] | alt | 34.8 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.91× (z +10.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 9.75× (z +8.9) | — |
| [[BT-474 (line)]] | alt | 48.4 | 4 (2 ⚠) | 0 | [[TAK-901 (drug)]] 0.05 µM 4.86× (z +11.9) | — |
| [[H4 (line)]] | wt | 39.3 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +11.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 30.8× (z +10.2) | — |
| [[Hs 766T (line)]] | wt | 29.1 | 4 (3 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 24.0× (z +11.1) | — |
| [[A-427 (line)]] | wt | 58.1 | 2 | 1 | [[TAK-901 (drug)]] 5 µM 8.61× (z +11.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.400× (z -9.4) |
| [[HT-29 (line)]] | alt | 36.1 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 10.2× (z +10.3) | — |
| [[SW1417 (line)]] | alt | 94.6 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 8.22× (z +13.1) | — |
| [[A549 (line)]] | wt | 32.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +10.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 11.4× (z +10.1) | — |
| [[J82 (line)]] | alt | 73.8 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.50× (z +10.1) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H2030 (line)]] | alt | 46.9 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 8.22× (z +9.6) | — |
| [[RKO (line)]] | wt | 62.7 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 13.5× (z +13.1) | — |
| [[SNU-1 (line)]] | wt | 42.6 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 19.1× (z +9.5) | [[Dinaciclib (drug)]] 0.05 µM 0.217× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[A498 (line)]] | wt | 57.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.08× (z +8.9) | — |
| [[HCT15 (line)]] | alt | 45.7 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.30× (z +9.6) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H23 (line)]] | alt | 87.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.47× (z +9.7) | — |
| [[SW48 (line)]] | wt | 57.9 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 4.76× (z +10.3) | — |
| [[AN3 CA (line)]] | alt | 69.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 53.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 57.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 67.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 57.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 68.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 477), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BYSL]] | +0.77 | +0.83 / +0.71 | both halves | 7e-06 | STRING 908 |
| [[POLR1A]] | +0.77 | +0.76 / +0.74 | both halves | 7e-06 | STRING 647 |
| [[TWNK]] | +0.75 | +0.79 / +0.67 | both halves | 7e-06 |  |
| [[NUDC]] | +0.74 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[BCCIP]] | +0.74 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[DIS3L2]] | +0.74 | +0.78 / +0.70 | both halves | 7e-06 |  |
| [[NOM1]] | +0.74 | +0.73 / +0.74 | both halves | 7e-06 | STRING 419 |
| [[MAK16]] | +0.72 | +0.74 / +0.73 | both halves | 7e-06 | STRING 920 |
| [[GTPBP4]] | +0.72 | +0.78 / +0.68 | both halves | 7e-06 | STRING 969 |
| [[LTV1]] | +0.71 | +0.77 / +0.73 | both halves | 7e-06 | STRING 808 |
| [[MYBBP1A]] | +0.71 | +0.67 / +0.72 | both halves | 7e-06 | STRING 509 |
| [[EIPR1]] | +0.71 | +0.63 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LNX2]] | -0.63 | -0.61 / -0.62 | both halves | 7e-06 |  |
| [[ABCA5]] | -0.62 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[TXNDC16]] | -0.62 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[AAMDC]] | -0.60 | -0.58 / -0.61 | both halves | 7e-06 |  |
| [[ZNF706]] | -0.59 | -0.52 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.718). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-13.8, -35.6); signed map (-3.9, -47.1). **Vector** length 78.2, 21.9% of its response variance represented; |z| ≥ 3 in 1,536 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.5 | +23.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.4 | +18.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.6 | +13.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.9 | +11.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.2 | +12.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.0 | +12.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.8 | +5.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.2 | +7.3 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | +1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.1 | -2.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -3.8 | -5.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.8 | +15.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | +0.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.4 | -2.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.3 | +1.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.0 | -1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | large 60S subunit nuclear export GTPase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q29 — chr3:194,640,791-194,672,463 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11301 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H089](https://www.uniprot.org/uniprotkb/Q9H089) (Large subunit GTPase 1 homolog):

> Functions as a GTPase. May act by mediating the release of NMD3 from the 60S ribosomal subunit after export into the cytoplasm during the 60S ribosomal subunit maturation.

**Summary**, from NCBI Gene [55341](https://www.ncbi.nlm.nih.gov/gene/55341):

> This gene encodes a protein related to the yeast large subunit GTPase 1. The encoded protein is necessary for cell viability and may localize in the endoplasmic reticulum, nucleus and cytoplasm.[provided by RefSeq, Feb 2009]

**Accessions** — [HGNC:25652](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25652) · Entrez [55341](https://www.ncbi.nlm.nih.gov/gene/55341) · UniProt [Q9H089](https://www.uniprot.org/uniprotkb/Q9H089) · Ensembl [ENSG00000041802](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000041802)

## Data

Gene col 477: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 477); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 477, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 477]; `tensor/DDL_lfc|DDL_z.npy` [477]; `embed/gene_vectors.npy` [477]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 477 or target_col == 477). Every well: [[LSG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LSG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
