---
symbol: "DYNLL2"
type: "gene"
col: 15439
ensembl_id: "ENSG00000264364"
name: "dynein light chain LC8-type 2"
location: "17q22"
module: 96
arm: "+"
pooled_cpm: 36.16
n_lines_expressing: 50
n_dd_up: 36
n_dd_down: 3
n_dd_up_clean: 24
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/096"]
generated_by: "tahoemap"
---

# DYNLL2

*dynein light chain LC8-type 2* — 17q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.62× (z +24.1, q 0e+00, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.536× (z -6.2, q 4e-07, down in 26 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H1573 0.251×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SFPQ]] (+0.62, fdr 1e-05), [[SRSF6]] (+0.61, fdr 1e-05), [[TFE3]] (+0.55, fdr 3e-05); moves opposite to [[NUP54]] (-0.58, fdr 3e-05), [[COX5B]] (-0.57, fdr 2e-05), [[NDUFA7]] (-0.54, fdr 2e-04).
> It is in [[Module 096]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15439.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.62×** | +24.1 | 0e+00 | 44/47 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.86×** | +19.9 | 0e+00 | 43/46 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.89×** | +19.3 | 0e+00 | 37/38 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.62×** | +18.2 | 0e+00 | 47/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.27×** | +15.5 | 0e+00 | 43/47 (HOP62, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.19×** | +14.8 | 0e+00 | 46/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.08×** | +13.9 | 6e-42 | 45/48 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.90×** | +12.1 | 5e-32 | 39/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.91×** | +11.8 | 4e-30 | 38/46 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.92×** | +11.4 | 3e-28 | 37/43 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.78×** | +10.9 | 6e-26 | 43/48 (MIA PaCa-2, NCI-H460, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +10.2 | 1e-22 | 37/47 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.58×** | +8.6 | 3e-16 | 38/48 (HEC-1-A, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.55×** | +8.3 | 4e-15 | 32/48 (HEC-1-A, C32, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.54×** | +7.9 | 1e-13 | 33/48 (C32, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.47×** | +7.2 | 2e-11 | 29/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.45×** | +7.1 | 5e-11 | 32/48 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.29×** | +6.3 | 7e-09 | 27/48 (J82, HEC-1-A, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +5.9 | 1e-07 | 30/48 (HT-29, NCI-H2347, …) | rises with dose | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.76×** | +5.6 | 5e-07 | 24/48 (PANC-1, SW1417, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15439.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H1573 0.251×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.536×** | -6.2 | 4e-07 | 26/48 (LS 180, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 0.848× | -4.2 | 0.007 | 14/48 (A498, A549, …) | inconsistent across doses | position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.807×** | -4.1 | 0.009 | 15/48 (A-172, SW1417, …) | inconsistent across doses |  |
| [[Naproxen (drug)]] 5 µM |  | **0.829×** | -3.4 | 0.084 | 9/47 (C-33 A, KATO III, …) | top dose only |  |
| [[Pravastatin (sodium) (drug)]] 0.05 µM |  | 0.834× | -3.2 | 0.16 | 14/47 (HEC-1-A, C32, …) | inconsistent across doses | position effect removed |
| [[Lumateperone (tosylate) (drug)]] 0.5 µM |  | 0.848× | -3.1 | 0.16 | 4/48 (Panc 03.27, A498, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | 0.848× | -3.0 | 0.21 | 14/47 (NCI-H23, A498, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15439. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 18.3 | 12 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +13.9) | — |
| [[SW480 (line)]] | alt | 47.0 | 11 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.88× (z +18.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.27× (z +12.5) | — |
| [[HEC-1-A (line)]] | alt | 58.5 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +14.3) | — |
| [[HOP62 (line)]] | alt | 37.2 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.84× (z +21.6) | — |
| [[KATO III (line)]] | alt | 62.9 | 7 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.86× (z +14.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.18× (z +10.9) | — |
| [[PANC-1 (line)]] | alt | 24.8 | 7 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.49× (z +12.9) | — |
| [[A-172 (line)]] | wt | 31.1 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +11.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.04× (z +9.1) | — |
| [[HT-29 (line)]] | alt | 46.5 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +11.5) | — |
| [[C32 (line)]] | wt | 29.5 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.72× (z +18.1) | — |
| [[LOX-IMVI (line)]] | wt | 17.9 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.98× (z +14.2) | — |
| [[NCI-H1792 (line)]] | alt | 21.7 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.36× (z +16.2) | — |
| [[Panc 03.27 (line)]] | alt | 50.5 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.59× (z +14.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.79× (z +13.3) | — |
| [[A549 (line)]] | wt | 20.2 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +10.1) | — |
| [[J82 (line)]] | alt | 41.0 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +13.3) | — |
| [[LoVo (line)]] | wt | 28.5 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +14.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 29.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +11.4) | — |
| [[NCI-H2030 (line)]] | alt | 26.2 | 4 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 7.58× (z +15.4) | — |
| [[NCI-H2347 (line)]] | alt | 45.2 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.59× (z +9.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.42× (z +8.9) | — |
| [[CFPAC-1 (line)]] | alt | 37.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.22× (z +19.3) | — |
| [[hTERT-HPNE (line)]] | wt | 40.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.90× (z +15.8) | — |
| [[NCI-H1573 (line)]] | alt | 23.4 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.02× (z +15.4) | [[Digitoxin (drug)]] 5 µM 0.251× (z -10.1) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 23.3 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.71× (z +9.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.88× (z +8.5) | — |
| [[SK-MEL-2 (line)]] | alt | 49.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +11.5) | — |
| [[SW 900 (line)]] | alt | 38.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +11.8) | — |
| [[SW1417 (line)]] | alt | 95.9 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +12.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.81× (z +9.3) | — |
| [[LS 180 (line)]] | wt | 40.4 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +11.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.42× (z +10.9) | — |
| [[SNU-423 (line)]] | alt | 26.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +10.6) | — |
| [[A498 (line)]] | wt | 38.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +9.8) | — |
| [[AsPC-1 (line)]] | alt | 17.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +8.5) | — |
| [[BT-474 (line)]] | alt | 89.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.70× (z +8.8) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 32.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.61× (z +8.6) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 31.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +11.4) | — |
| [[HepG2_C3A (line)]] | wt | 48.8 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.23× (z +8.6) | — |
| [[SHP-77 (line)]] | alt | 29.9 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.12× (z +9.4) | — |
| [[SNU-1 (line)]] | wt | 29.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +9.9) | — |
| [[A-427 (line)]] | wt | 34.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 51.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 39.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 33.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15439), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SFPQ]] | +0.62 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[SRSF6]] | +0.61 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[TFE3]] | +0.55 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[PIEZO1]] | +0.53 | +0.61 / +0.39 | both halves | 5e-05 |  |
| [[RMRP]] | +0.53 | +0.26 / +0.55 | both halves | 4e-04 |  |
| [[TAOK2]] | +0.53 | +0.56 / +0.42 | both halves | 4e-05 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[MTSS2]] | +0.52 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[SCRIB]] | +0.52 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[DLG5]] | +0.52 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[UBE2A]] | +0.52 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[MAFK]] | +0.51 | +0.35 / +0.48 | both halves | 1e-04 | pathway: Affinity selection of immunoglobulins |
| [[NCDN]] | +0.51 | +0.48 / +0.52 | both halves | 2e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP54]] | -0.58 | -0.56 / -0.43 | both halves | 3e-05 | pathway: HCMV Early Events; STRING 487 |
| [[COX5B]] | -0.57 | -0.64 / -0.47 | both halves | 2e-05 |  |
| [[NDUFA7]] | -0.54 | -0.32 / -0.53 | both halves | 2e-04 |  |
| [[BFAR]] | -0.49 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[SPATA7]] | -0.49 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[USP37]] | -0.48 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[TTC9C]] | -0.48 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[ORC2]] | -0.48 | -0.42 / -0.41 | both halves | 4e-05 | pathway: Cell Cycle Checkpoints |
| [[BMT2]] | -0.48 | -0.60 / -0.31 | both halves | 2e-04 |  |
| [[NUDT22]] | -0.47 | -0.23 / -0.51 | both halves | 5e-04 |  |
| [[RPL12]] | -0.47 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[NOA1]] | -0.47 | -0.27 / -0.46 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 096]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.550). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-3.5, -20.6); signed map (8.9, -36.0). **Vector** length 81.9, 19.7% of its response variance represented; |z| ≥ 3 in 1,260 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +3.9 | +12.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +19.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +19.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +10.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +3.3 | +5.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.1 | +8.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +5.9 |
|  | [[crizotinib (drug)]] 5 µM |  | +1.9 | +0.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.7 | +1.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | -9.3 | +2.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -6.2 | -6.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.4 | +1.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | +1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.0 | -2.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.9 | -3.0 |
|  | [[Ixazomib (drug)]] 0.05 µM |  | -1.8 | -0.1 |
|  | [[TAK-901 (drug)]] 0.5 µM |  | -1.6 | -0.2 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -1.5 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | dynein light chain LC8-type 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q22 — chr17:58,083,419-58,095,542 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC17810, Dlc2, DNCL1B, RSPH22 |
| Gene groups (HGNC) | Dynein 1 complex subunits; Dynein 2 complex subunits; Dyneins, axonemal outer arm complex subunits; Dyneins, axonemal inner arm I1/f complex subunits; Dynein light chain LC8-type family |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 50 pathways, smallest: Activation of BMF and translocation to mitochondria; Activation of BH3-only proteins; Aggrephagy |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96FJ2](https://www.uniprot.org/uniprotkb/Q96FJ2) (Dynein light chain 2, cytoplasmic):

> Acts as one of several non-catalytic accessory components of the cytoplasmic dynein 1 complex that are thought to be involved in linking dynein to cargos and to adapter proteins that regulate dynein function. Cytoplasmic dynein 1 acts as a motor for the intracellular retrograde motility of vesicles and organelles along microtubules. May play a role in changing or maintaining the spatial distribution of cytoskeletal structures (By similarity).

**Summary**, from NCBI Gene [140735](https://www.ncbi.nlm.nih.gov/gene/140735):

> Predicted to enable dynein intermediate chain binding activity. Predicted to be involved in several processes, including flagellated sperm motility; intraciliary retrograde transport; and positive regulation of mitotic cell cycle spindle assembly checkpoint. Located in 9+0 non-motile cilium and centrosome. Is active in glutamatergic synapse and postsynapse. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24596](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24596) · Entrez [140735](https://www.ncbi.nlm.nih.gov/gene/140735) · UniProt [Q96FJ2](https://www.uniprot.org/uniprotkb/Q96FJ2) · Ensembl [ENSG00000264364](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000264364)

## Data

Gene col 15439: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15439); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15439, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15439]; `tensor/DDL_lfc|DDL_z.npy` [15439]; `embed/gene_vectors.npy` [15439]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15439 or target_col == 15439). Every well: [[DYNLL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DYNLL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
