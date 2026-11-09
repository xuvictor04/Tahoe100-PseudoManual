---
symbol: "NUDC"
type: "gene"
col: 1616
ensembl_id: "ENSG00000090273"
name: "nuclear distribution C, dynein complex regulator"
location: "1p36.11"
module: 4
arm: "+"
pooled_cpm: 66.29
n_lines_expressing: 50
n_dd_up: 40
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# NUDC

*nuclear distribution C, dynein complex regulator* — 1p36.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 40 drug-doses (22 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.54× (z +16.7, q 0e+00, up in 48 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 3.52× (z +16.6, q 0e+00, up in 48 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.218×; ⚠ cell-cycle shift, explains ~87% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.317×; ⚠ toxic); [[Isocorydine (drug)]] 0.5 µM in 1 line (SW 1271 0.0841×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STIP1]] (+0.75, fdr 7e-06), [[CCT3]] (+0.75, fdr 7e-06), [[CCT5]] (+0.75, fdr 7e-06); moves opposite to [[TNRC6C]] (-0.65, fdr 1e-05), [[CMC4]] (-0.63, fdr 1e-05), [[RSRP1]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 22 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 40 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 22 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1616.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **3.54×** | +16.7 | 0e+00 | 48/49 (A498, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **3.52×** | +16.6 | 0e+00 | 48/48 (HOP62, C32, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **3.65×** | +16.4 | 0e+00 | 42/42 (NCI-H460, A498, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.42×** | +11.6 | 4e-29 | 46/48 (SW1417, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.35×** | +11.2 | 3e-27 | 47/48 (HOP62, A498, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.57×** | +10.4 | 3e-23 | 42/44 (KATO III, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.29×** | +9.8 | 1e-20 | 47/48 (HOP62, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.94×** | +8.8 | 1e-16 | 46/48 (HOP62, COLO 205, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.89×** | +8.4 | 3e-15 | 44/48 (HOP62, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.68×** | +6.8 | 4e-10 | 41/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.58×** | +6.5 | 3e-09 | 41/44 (SW1417, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.63×** | +6.4 | 6e-09 | 39/48 (HOP62, AsPC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +6.4 | 8e-09 | 41/47 (CFPAC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~51% of this change | **1.62×** | +6.1 | 5e-08 | 41/47 (NCI-H1573, COLO 205, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.57×** | +5.7 | 4e-07 | 34/48 (HOP62, A549, …) | all doses, stronger at high dose | composition shift |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.39×** | +4.3 | 4e-04 | 30/47 (HOP62, SW 900, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.40×** | +4.3 | 6e-04 | 29/48 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.72×** | +4.2 | 6e-04 | 31/49 (SW1417, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.32×** | +3.6 | 0.006 | 25/48 (PANC-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.69×** | +3.6 | 0.006 | 26/48 (NCI-H1792, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Infigratinib (drug)]] 5 µM |  | **1.65×** | +3.5 | 0.011 | 21/48 (HOP62, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.59×** | +3.2 | 0.026 | 20/48 (NCI-H460, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.31×** | +3.0 | 0.056 | 19/48 (NCI-H460, SW 900, …) | all doses, flat |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.27×** | +2.9 | 0.056 | 17/48 (A549, NCI-H460, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.53×** | +2.9 | 0.060 | 16/48 (LS 180, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1616.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.218×; ⚠ cell-cycle shift, explains ~87% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.317×; ⚠ toxic); [[Isocorydine (drug)]] 0.5 µM in 1 line (SW 1271 0.0841×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 0.05 µM |  | 0.823× | -3.5 | 0.23 | 22/48 (RKO, Hs 766T, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 0.783× | -3.3 | 0.29 | 25/48 (RKO, HOP62, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.50 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1616. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 53.8 | 8 (4 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 6.49× (z +18.2) | — |
| [[A498 (line)]] | wt | 69.1 | 7 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.24× (z +16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.11× (z +11.2) | — |
| [[SW480 (line)]] | alt | 75.2 | 7 (5 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.76× (z +15.0) | — |
| [[KATO III (line)]] | alt | 40.7 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.55× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.33× (z +9.9) | — |
| [[SW1417 (line)]] | alt | 51.5 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.62× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.71× (z +11.9) | — |
| [[HEC-1-A (line)]] | alt | 73.3 | 5 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.91× (z +14.8) | — |
| [[HS-578T (line)]] | alt | 83.6 | 5 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.48× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.45× (z +11.4) | — |
| [[RKO (line)]] | wt | 249 | 1 | 4 (4 ⚠) | [[Auranofin (drug)]] 5 µM 2.78× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.218× (z -17.0) ⚠ cell-cycle shift, explains ~87% of this change |
| [[Hs 766T (line)]] | wt | 68.6 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.72× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.53× (z +9.8) | — |
| [[SK-MEL-2 (line)]] | alt | 91.5 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.07× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.81× (z +11.5) | — |
| [[SNU-423 (line)]] | alt | 50.3 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.27× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Auranofin (drug)]] 5 µM 4.68× (z +11.2) | — |
| [[A-172 (line)]] | wt | 53.9 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.57× (z +12.7) | — |
| [[AsPC-1 (line)]] | alt | 34.6 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.46× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.04× (z +8.5) | — |
| [[HT-29 (line)]] | alt | 63.8 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.62× (z +15.1) | — |
| [[hTERT-HPNE (line)]] | wt | 46.3 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.93× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.77× (z +8.8) | — |
| [[J82 (line)]] | alt | 98.6 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.55× (z +8.9) | — |
| [[LoVo (line)]] | wt | 54.1 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.49× (z +15.0) | — |
| [[LOX-IMVI (line)]] | wt | 76.0 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.37× (z +13.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 48.2 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.08× (z +12.1) | — |
| [[NCI-H1573 (line)]] | alt | 44.2 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.16× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.95× (z +9.1) | — |
| [[NCI-H1792 (line)]] | alt | 32.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.52× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[NCI-H2347 (line)]] | alt | 65.6 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.22× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.42× (z +8.7) | — |
| [[NCI-H460 (line)]] | wt | 46.0 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.92× (z +16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.14× (z +10.3) | — |
| [[Panc 03.27 (line)]] | alt | 45.4 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.09× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.29× (z +9.6) | — |
| [[PANC-1 (line)]] | alt | 91.4 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.98× (z +14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.68× (z +10.2) | — |
| [[SW 900 (line)]] | alt | 50.3 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.85× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Auranofin (drug)]] 5 µM 4.23× (z +11.8) | — |
| [[A-427 (line)]] | wt | 91.6 | 2 | 0 | [[Auranofin (drug)]] 5 µM 4.34× (z +13.6) | — |
| [[COLO 205 (line)]] | alt | 43.2 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.03× (z +9.0) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[H4 (line)]] | wt | 51.3 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.37× (z +10.2) | — |
| [[HCT15 (line)]] | alt | 58.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.14× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[HepG2_C3A (line)]] | wt | 69.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.70× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[LS 180 (line)]] | wt | 39.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.58× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H2030 (line)]] | alt | 85.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.31× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[NCI-H23 (line)]] | alt | 105 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.72× (z +11.9) | — |
| [[RPMI-7951 (line)]] | alt | 62.5 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.91× (z +10.6) | — |
| [[SHP-77 (line)]] | alt | 106 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.18× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[SNU-1 (line)]] | wt | 56.4 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.47× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Auranofin (drug)]] 5 µM 4.46× (z +9.4) | — |
| [[A549 (line)]] | wt | 40.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.74× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[AN3 CA (line)]] | alt | 85.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.06× (z +9.2) | — |
| [[BT-474 (line)]] | alt | 47.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 12.2× (z +16.7) | — |
| [[C-33 A (line)]] | alt | 122 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.35× (z +12.0) | — |
| [[C32 (line)]] | wt | 44.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 10.3× (z +16.9) | — |
| [[SW 1271 (line)]] | alt | 62.6 | 0 | 1 | — | [[Isocorydine (drug)]] 0.5 µM 0.0841× (z -9.0) |
| [[SW48 (line)]] | wt | 69.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.05× (z +10.3) | — |
| [[CFPAC-1 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 99.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 57.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1616), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STIP1]] | +0.75 | +0.70 / +0.74 | both halves | 7e-06 | STRING 553 |
| [[CCT3]] | +0.75 | +0.76 / +0.73 | both halves | 7e-06 | STRING 581 |
| [[CCT5]] | +0.75 | +0.76 / +0.74 | both halves | 7e-06 | STRING 715 |
| [[GPN1]] | +0.75 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[LSG1]] | +0.74 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[ELAC2]] | +0.74 | +0.79 / +0.63 | both halves | 7e-06 |  |
| [[CCT6A]] | +0.73 | +0.74 / +0.73 | both halves | 7e-06 | STRING 554 |
| [[CCT2]] | +0.73 | +0.73 / +0.72 | both halves | 7e-06 | STRING 704 |
| [[PSMD12]] | +0.72 | +0.70 / +0.72 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[LAS1L]] | +0.70 | +0.73 / +0.67 | both halves | 7e-06 |  |
| [[HERC2]] | +0.69 | +0.73 / +0.61 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[EIPR1]] | +0.69 | +0.68 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNRC6C]] | -0.65 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[CMC4]] | -0.63 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[RSRP1]] | -0.62 | -0.50 / -0.64 | both halves | 1e-05 |  |
| [[POLH]] | -0.62 | -0.61 / -0.55 | both halves | 1e-05 |  |
| [[ABCA5]] | -0.62 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[LNX2]] | -0.60 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[PPM1D]] | -0.60 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[TXNDC16]] | -0.60 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[PHPT1]] | -0.59 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[HLA-A]] | -0.59 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[ZNF821]] | -0.59 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[AAMDC]] | -0.58 | -0.63 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.717). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-20.4, -31.7); signed map (-11.9, -46.0). **Vector** length 83.6, 27.4% of its response variance represented; |z| ≥ 3 in 1,191 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *tRNA processing in the nucleus* (reactome, mean cos +0.50 to 8); *Folding of actin by CCT/TriC* (reactome, mean cos +0.62 to 4); *Prefoldin mediated transfer of substrate  to CCT/TriC* (reactome, mean cos +0.59 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +8.2 | +11.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +7.8 | +9.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.2 | +11.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.3 | +16.6 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +5.3 | +6.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.2 | +4.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | +2.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.7 | +4.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | -4.0 | +2.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~99% of this change | -3.6 | +4.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | +1.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | +1.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | -2.9 | +2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -2.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.6 | +1.3 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -1.6 | +1.5 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | -1.4 | -0.2 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -1.4 | +0.7 |

## What is on record

|  |  |
|---|---|
| Name | nuclear distribution C, dynein complex regulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:26,900,238-26,946,871 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | NudC family |
| Reactome | 19 pathways, smallest: RND2 GTPase cycle; Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; Amplification of signal from the kinetochores |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y266](https://www.uniprot.org/uniprotkb/Q9Y266) (Nuclear migration protein nudC):

> Plays a role in neurogenesis and neuronal migration (By similarity). Necessary for correct formation of mitotic spindles and chromosome separation during mitosis. Necessary for cytokinesis and cell proliferation.

**Summary**, from NCBI Gene [10726](https://www.ncbi.nlm.nih.gov/gene/10726):

> This gene encodes a nuclear distribution protein that plays an essential role in mitosis and cytokinesis. The encoded protein is involved in spindle formation during mitosis and in microtubule organization during cytokinesis. Pseudogenes of this gene are found on chromosome 2. [provided by RefSeq, Feb 2012]

**Accessions** — [HGNC:8045](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8045) · Entrez [10726](https://www.ncbi.nlm.nih.gov/gene/10726) · UniProt [Q9Y266](https://www.uniprot.org/uniprotkb/Q9Y266) · Ensembl [ENSG00000090273](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000090273)

## Data

Gene col 1616: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1616); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1616, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1616]; `tensor/DDL_lfc|DDL_z.npy` [1616]; `embed/gene_vectors.npy` [1616]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1616 or target_col == 1616). Every well: [[NUDC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUDC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
