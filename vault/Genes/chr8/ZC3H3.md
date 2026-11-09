---
symbol: "ZC3H3"
type: "gene"
col: 285
ensembl_id: "ENSG00000014164"
name: "zinc finger CCCH-type containing 3"
location: "8q24.3"
module: 21
arm: "+"
pooled_cpm: 39.22
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# ZC3H3

*zinc finger CCCH-type containing 3* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 16.9× (z +39.9, q 0e+00, up in 46 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.95× (z +9.4, q 5e-19, up in 40 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ritonavir (drug)]] 0.5 µM in 1 line (H4 0.124×).
> Its strongest partners by |cos| (82 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 18 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ECI1]] (+0.67, fdr 1e-05), [[SARM1]] (+0.67, fdr 1e-05), [[MSTO1]] (+0.64, fdr 4e-05); moves opposite to [[MSH6]] (-0.54, fdr 3e-04), [[FOXA2]] (-0.53, fdr 4e-04), [[ISCA2]] (-0.53, fdr 4e-04).
> It is in [[Module 021]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 11 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 285.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **16.9×** | +39.9 | 0e+00 | 46/46 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **17.2×** | +38.6 | 0e+00 | 37/37 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **14.2×** | +33.3 | 0e+00 | 41/41 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **4.52×** | +11.1 | 2e-26 | 29/31 (HOP62, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.95×** | +9.4 | 5e-19 | 40/48 (HEC-1-A, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.92×** | +9.2 | 5e-18 | 40/48 (LOX-IMVI, KATO III, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.58×** | +9.1 | 6e-18 | 31/47 (NCI-H1792, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.82×** | +8.4 | 2e-15 | 34/46 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +7.0 | 1e-10 | 34/45 (NCI-H2030, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.57×** | +7.0 | 2e-10 | 33/49 (RKO, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +6.1 | 4e-08 | 31/47 (NCI-H460, H4, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.55×** | +5.8 | 3e-07 | 31/48 (CFPAC-1, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.65×** | +5.0 | 2e-05 | 27/49 (HEC-1-A, SW1417, …) | all doses, flat | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.43×** | +5.0 | 2e-05 | 25/48 (HOP62, HEC-1-A, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.93×** | +4.8 | 5e-05 | 25/42 (HEC-1-A, RKO, …) | all doses, flat | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +4.7 | 8e-05 | 23/47 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.39×** | +4.6 | 1e-04 | 30/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.81×** | +4.4 | 4e-04 | 21/47 (CFPAC-1, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.36×** | +4.4 | 4e-04 | 19/47 (HS-578T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **1.75×** | +4.1 | 0.001 | 25/46 (Panc 03.27, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.29×** | +3.6 | 0.008 | 16/48 (HOP62, NCI-H460, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.28×** | +3.5 | 0.012 | 19/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.51×** | +3.0 | 0.054 | 19/47 (LOX-IMVI, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 285.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ritonavir (drug)]] 0.5 µM in 1 line (H4 0.124×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Thymol (drug)]] 5 µM |  | 0.847× | -3.3 | 0.38 | 14/48 (CHP-212, LOX-IMVI, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.852× | -3.2 | 0.38 | 15/48 (MIA PaCa-2, BT-474, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 285. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 27.2 | 13 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 43.3× (z +27.0) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 10.4× (z +16.8) | — |
| [[HOP62 (line)]] | alt | 44.8 | 10 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 65.2× (z +33.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.13× (z +13.1) | — |
| [[SW 900 (line)]] | alt | 54.5 | 9 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 50.3× (z +22.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 5.61× (z +14.2) | — |
| [[HEC-1-A (line)]] | alt | 22.8 | 7 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.6× (z +20.0) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.77× (z +10.5) | — |
| [[CFPAC-1 (line)]] | alt | 44.5 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 16.0× (z +13.7) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 5.67× (z +9.0) | — |
| [[HS-578T (line)]] | alt | 53.2 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 29.8× (z +27.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 4.04× (z +16.2) | — |
| [[LOX-IMVI (line)]] | wt | 41.4 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 30.7× (z +31.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 4.57× (z +19.7) | — |
| [[NCI-H2030 (line)]] | alt | 53.7 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 20.4× (z +28.0) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 106 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 23.9× (z +17.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.62× (z +9.8) | — |
| [[C32 (line)]] | wt | 34.3 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.89× (z +13.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.55× (z +11.7) | — |
| [[H4 (line)]] | wt | 23.2 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 61.1× (z +19.1) ⚠ toxic; transcription drop | [[Ritonavir (drug)]] 0.5 µM 0.124× (z -10.1) |
| [[LoVo (line)]] | wt | 25.8 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 29.2× (z +28.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 4.12× (z +17.1) | — |
| [[NCI-H1792 (line)]] | alt | 32.1 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 16.9× (z +20.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 7.25× (z +19.8) | — |
| [[SNU-423 (line)]] | alt | 29.7 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 20.9× (z +22.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.34× (z +8.7) | — |
| [[SW480 (line)]] | alt | 20.2 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.7× (z +22.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +9.0) | — |
| [[A549 (line)]] | wt | 56.1 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 26.0× (z +26.1) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 25.3 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 20.1× (z +15.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.47× (z +9.6) | — |
| [[hTERT-HPNE (line)]] | wt | 21.9 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 22.9× (z +16.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 4.49× (z +10.9) | — |
| [[J82 (line)]] | alt | 40.8 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 25.8× (z +21.9) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 29.1 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 11.9× (z +17.2) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.40× (z +9.5) | — |
| [[NCI-H2347 (line)]] | alt | 85.0 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.74× (z +16.3) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 45.0 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 27.6× (z +16.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.18× (z +8.6) | — |
| [[SHP-77 (line)]] | alt | 40.1 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 30.5× (z +20.2) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 28.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 17.7× (z +20.0) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 62.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 25.1× (z +32.4) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 30.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 50.2× (z +14.7) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 48.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.1× (z +14.0) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 39.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 17.0× (z +19.3) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 33.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 5.63× (z +12.2) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 22.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 17.4× (z +18.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 34.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.8× (z +17.4) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 41.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 16.4× (z +23.0) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 33.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.0× (z +23.4) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 23.4 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.3× (z +14.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.44× (z +10.5) | — |
| [[SW1417 (line)]] | alt | 50.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.93× (z +13.6) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 36.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.44× (z +13.1) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 27.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 14.5× (z +11.3) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 27.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.4× (z +17.4) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 39.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.64× (z +9.4) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 23.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 13.1× (z +14.5) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 22.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 22.4× (z +10.3) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 23.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.67× (z +9.6) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 71.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.80× (z +16.0) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 285), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 12 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ECI1]] | +0.67 | +0.51 / +0.66 | both halves | 1e-05 | **novel candidate** |
| [[SARM1]] | +0.67 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[MSTO1]] | +0.64 | +0.42 / +0.68 | both halves | 4e-05 |  |
| [[CTC1]] | +0.62 | +0.31 / +0.72 | both halves | 2e-04 |  |
| [[SNHG22]] | +0.61 | +0.39 / +0.68 | both halves | 5e-05 |  |
| [[C8orf44-SGK3]] | +0.60 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[RAD51-AS1]] | +0.60 | +0.31 / +0.66 | both halves | 2e-04 |  |
| [[KCTD2]] | +0.57 | +0.39 / +0.63 | both halves | 6e-05 |  |
| [[DNAJC27-AS1]] | +0.55 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[TCEA2]] | +0.55 | +0.46 / +0.60 | both halves | 3e-05 |  |
| [[CCDC183]] | +0.55 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[NPEPPSP1]] | +0.55 | +0.33 / +0.62 | both halves | 1e-04 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSH6]] | -0.54 | -0.29 / -0.60 | both halves | 3e-04 |  |
| [[FOXA2]] | -0.53 | -0.25 / -0.63 | both halves | 4e-04 |  |
| [[ISCA2]] | -0.53 | -0.26 / -0.62 | both halves | 4e-04 |  |
| [[CSTF1]] | -0.52 | -0.41 / -0.61 | both halves | 4e-05 | STRING 774 |
| [[MPLKIP]] | -0.52 | -0.14 / -0.69 | ⚠ one half (not replicated) | 0.002 |  |
| [[CYC1]] | -0.51 | -0.29 / -0.58 | both halves | 2e-04 |  |
| [[ZNF184]] | -0.51 | -0.30 / -0.56 | both halves | 2e-04 |  |
| [[DEPDC7]] | -0.51 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[SIX1]] | -0.50 | -0.24 / -0.59 | both halves | 5e-04 |  |
| [[METTL23]] | -0.50 | -0.24 / -0.58 | both halves | 4e-04 |  |
| [[TRMT1L]] | -0.50 | -0.29 / -0.64 | both halves | 2e-04 |  |
| [[NPAT]] | -0.50 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[MAP3K1]] | -0.50 | -0.37 / -0.51 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.375). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-4.6, 27.1); signed map (31.1, -16.2). **Vector** length 94.7, 23.0% of its response variance represented; |z| ≥ 3 in 1,108 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +11.2 | +33.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.9 | +38.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.9 | +39.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.7 | +9.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.3 | +5.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.5 | +9.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.8 | +5.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.4 | +1.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +1.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.1 | +0.8 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.3 | -2.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | -0.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.8 | -3.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -1.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.2 | -1.7 |
|  | [[Carbamazepine (drug)]] 5 µM |  | -2.1 | -1.8 |
|  | [[Lumateperone (tosylate) (drug)]] 0.5 µM |  | -1.9 | -1.4 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -1.9 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger CCCH-type containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:143,437,659-143,541,447 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0150; previously ZC3HDC3 |
| Gene groups (HGNC) | Zinc fingers CCCH-type |
| Reactome | 2 pathways, smallest: Nuclear RNA decay; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IXZ2](https://www.uniprot.org/uniprotkb/Q8IXZ2) (Zinc finger CCCH domain-containing protein 3):

> Required for the export of polyadenylated mRNAs from the nucleus. Enhances ACVR1B-induced SMAD-dependent transcription. Binds to single-stranded DNA but not to double-stranded DNA in vitro. Involved in RNA cleavage (By similarity).

**Summary**, from NCBI Gene [23144](https://www.ncbi.nlm.nih.gov/gene/23144):

> Predicted to enable DNA binding activity; R-SMAD binding activity; and zinc ion binding activity. Predicted to be involved in RNA catabolic process. Predicted to act upstream of or within mRNA 3'-end processing and positive regulation of activin receptor signaling pathway. Located in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28972](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28972) · Entrez [23144](https://www.ncbi.nlm.nih.gov/gene/23144) · UniProt [Q8IXZ2](https://www.uniprot.org/uniprotkb/Q8IXZ2) · Ensembl [ENSG00000014164](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000014164)

## Data

Gene col 285: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 285); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 285, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 285]; `tensor/DDL_lfc|DDL_z.npy` [285]; `embed/gene_vectors.npy` [285]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 285 or target_col == 285). Every well: [[ZC3H3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZC3H3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
