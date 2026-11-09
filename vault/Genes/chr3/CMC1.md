---
symbol: "CMC1"
type: "gene"
col: 11889
ensembl_id: "ENSG00000187118"
name: "C-X9-C motif containing 1"
location: "3p24.1"
module: 65
arm: "+"
pooled_cpm: 58.93
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 23
n_dd_up_clean: 1
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# CMC1

*C-X9-C motif containing 1* — 3p24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.37× (z +12.3, q 5e-32, up in 34 of 48 measured lines) ⚠ cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.23× (z +5.7, q 4e-06, up in 23 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 2.27×; ⚠ cell-cycle shift, explains ~8% of this change).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.442× (z -31.5, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTX2]] (+0.84, fdr 7e-06), [[ANAPC4]] (+0.64, fdr 7e-06), [[FBXL4]] (+0.63, fdr 7e-06); moves opposite to [[CCDC144CP]] (-0.55, fdr 3e-05), [[MYO1C]] (-0.54, fdr 3e-05), [[NID1]] (-0.54, fdr 3e-05).
> It sits in the **+** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 9 with an alert ⚠; shown: the 15 strongest. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11889.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 2.27×; ⚠ cell-cycle shift, explains ~8% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.37×** | +12.3 | 5e-32 | 34/48 (PANC-1, HS-578T, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.23×** | +5.7 | 4e-06 | 23/48 (A498, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **1.22×** | +5.4 | 2e-05 | 21/48 (A-427, NCI-H2030, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +5.0 | 9e-05 | 10/48 (NCI-H23, hTERT-HPNE, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.13× | +4.6 | 4e-04 | 6/48 (SW 900, hTERT-HPNE, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~89% of this change | 1.18× | +4.2 | 0.002 | 12/48 (SW 900, C32, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 1.18× | +4.2 | 0.003 | 14/49 (SW1417, HOP62, …) | rises with dose |  |
| [[Afatinib (drug)]] 5 µM |  | 1.18× | +4.1 | 0.003 | 16/49 (NCI-H2347, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 1.16× | +4.1 | 0.003 | 15/48 (AsPC-1, HOP62, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.11× | +3.9 | 0.005 | 10/48 (A-427, HS-578T, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~3% of this change | 1.17× | +3.9 | 0.005 | 8/48 (SW1417, NCI-H2347, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.15× | +3.7 | 0.009 | 12/48 (J82, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.6 | 0.013 | 15/48 (A498, hTERT-HPNE, …) | all doses, flat |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | 1.09× | +3.5 | 0.019 | 2/48 (Panc 03.27, NCI-H1573) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | 1.14× | +3.4 | 0.028 | 6/48 (Panc 03.27, AsPC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 15 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11889.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.442×** | -31.5 | 0e+00 | 45/48 (SK-MEL-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.461×** | -21.1 | 0e+00 | 42/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.318×** | -16.4 | 0e+00 | 43/49 (MIA PaCa-2, LS 180, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.578×** | -14.9 | 0e+00 | 42/48 (SW480, LoVo, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.567×** | -14.9 | 0e+00 | 39/48 (NCI-H460, SW480, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.582×** | -14.8 | 0e+00 | 39/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.589×** | -14.4 | 3e-45 | 39/48 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.591×** | -13.3 | 3e-38 | 38/45 (A-427, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.621×** | -13.0 | 8e-37 | 35/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.640×** | -12.2 | 3e-32 | 39/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.453×** | -11.3 | 7e-28 | 36/48 (LS 180, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.651×** | -11.3 | 1e-27 | 31/43 (SHP-77, SW480, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.662×** | -10.8 | 1e-25 | 33/47 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.666×** | -10.1 | 2e-22 | 33/48 (NCI-H460, RPMI-7951, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.693×** | -10.0 | 6e-22 | 31/49 (Panc 03.27, SHP-77, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.754×** | -7.7 | 5e-13 | 29/48 (LS 180, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.812×** | -5.3 | 3e-06 | 23/48 (AN3 CA, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.766×** | -3.8 | 0.004 | 13/48 (HOP62, HCT15, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.769×** | -3.7 | 0.005 | 10/48 (NCI-H1792, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.827×** | -3.7 | 0.006 | 16/49 (Hs 766T, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.5 µM |  | 0.836× | -3.5 | 0.011 | 10/48 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Isocorydine (drug)]] 0.5 µM |  | 0.870× | -3.4 | 0.013 | 7/48 (KATO III, C-33 A, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11889. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 50.9 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -24.9) |
| [[SW480 (line)]] | alt | 85.2 | 0 | 12 (5 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.335× (z -19.8) |
| [[NCI-H2347 (line)]] | alt | 90.6 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -18.0) |
| [[HOP62 (line)]] | alt | 71.3 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -17.5) |
| [[KATO III (line)]] | alt | 66.9 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -17.6) |
| [[LS 180 (line)]] | wt | 111 | 0 | 7 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.236× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.263× (z -17.6) |
| [[SW1417 (line)]] | alt | 79.5 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -16.5) |
| [[C32 (line)]] | wt | 45.5 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -14.5) |
| [[HCT15 (line)]] | alt | 85.5 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.261× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.386× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 63.3 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -14.0) |
| [[COLO 205 (line)]] | alt | 59.8 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.141× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.333× (z -13.4) |
| [[HEC-1-A (line)]] | alt | 92.6 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -19.7) |
| [[J82 (line)]] | alt | 45.6 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -13.5) |
| [[LoVo (line)]] | wt | 59.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -20.5) |
| [[Panc 03.27 (line)]] | alt | 68.8 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0903× (z -26.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.388× (z -14.6) |
| [[RPMI-7951 (line)]] | alt | 62.3 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -14.0) |
| [[SNU-1 (line)]] | wt | 63.4 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.169× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.210× (z -11.3) |
| [[SNU-423 (line)]] | alt | 53.6 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -21.6) |
| [[A498 (line)]] | wt | 34.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -18.9) |
| [[AN3 CA (line)]] | alt | 55.3 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.117× (z -11.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.150× (z -9.6) |
| [[AsPC-1 (line)]] | alt | 40.8 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.275× (z -11.5) |
| [[HepG2_C3A (line)]] | wt | 54.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.195× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.462× (z -9.3) |
| [[HS-578T (line)]] | alt | 40.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -16.8) |
| [[MIA PaCa-2 (line)]] | alt | 61.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -12.0) |
| [[PANC-1 (line)]] | alt | 41.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -15.0) |
| [[SK-MEL-2 (line)]] | alt | 91.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -32.5) |
| [[A-172 (line)]] | wt | 49.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -12.3) |
| [[A-427 (line)]] | wt | 61.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +9.3) ⚠ cell-cycle shift, explains ~8% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.148× (z -20.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 43.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -13.1) |
| [[NCI-H1792 (line)]] | alt | 32.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -18.2) |
| [[RKO (line)]] | wt | 63.3 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.408× (z -8.5) |
| [[SHP-77 (line)]] | alt | 89.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0989× (z -23.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 42.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -11.7) |
| [[SW48 (line)]] | wt | 48.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.0603× (z -10.0) |
| [[A549 (line)]] | wt | 66.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -16.5) |
| [[BT-474 (line)]] | alt | 41.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.221× (z -12.2) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 62.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.149× (z -15.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 34.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -11.6) |
| [[H4 (line)]] | wt | 39.5 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.231× (z -8.8) |
| [[HT-29 (line)]] | alt | 34.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -10.2) |
| [[CHP-212 (line)]] | wt | 49.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 43.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 38.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 66.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 63.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 87.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11889), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTX2]] | +0.84 | +0.82 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[ANAPC4]] | +0.64 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[FBXL4]] | +0.63 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[FIG4]] | +0.63 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[CNIH4]] | +0.62 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[MRPL39]] | +0.62 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[LRIG2]] | +0.61 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[TMED8]] | +0.61 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[SDHAF4]] | +0.61 | +0.62 / +0.72 | both halves | 7e-06 | same gene group; pathway: Aerobic respiration and respiratory electron transport |
| [[SNRPA1]] | +0.60 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[LTA4H]] | +0.60 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[MINDY3]] | +0.59 | +0.54 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC144CP]] | -0.55 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[MYO1C]] | -0.54 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[NID1]] | -0.54 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[CELSR3]] | -0.53 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[MC1R]] | -0.52 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[THOC6]] | -0.52 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[AKT1S1]] | -0.51 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[SUPT6H]] | -0.51 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[DMPK]] | -0.51 | -0.58 / -0.37 | both halves | 7e-05 |  |
| [[SLC8A2]] | -0.51 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[ZBTB4]] | -0.51 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[KDM6B]] | -0.51 | -0.56 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **+** arm (projection on the module's main direction 0.671). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-4.7, -9.9); signed map (-31.0, -13.1). **Vector** length 88.7, 22.0% of its response variance represented; |z| ≥ 3 in 1,148 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +7.8 | +12.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~89% of this change | +3.7 | +4.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | +3.0 | +5.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +1.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.5 | +2.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.1 | +3.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.1 | +2.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.9 | +2.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | -0.0 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +1.8 | -1.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.8 | -14.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.8 | -31.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.1 | -13.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.9 | -11.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | -4.9 | -10.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | -11.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.4 | -0.4 |
|  | [[Lactate (calcium) (drug)]] 0.5 µM |  | -2.0 | -0.2 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | -2.0 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | C-X9-C motif containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p24.1 — chr3:28,241,584-28,325,142 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC61571; previously C3orf68 |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors |
| Reactome | 3 pathways, smallest: Complex IV assembly; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z7K0](https://www.uniprot.org/uniprotkb/Q7Z7K0) (COX assembly mitochondrial protein homolog):

> Component of the MITRAC (mitochondrial translation regulation assembly intermediate of cytochrome c oxidase complex) complex, that regulates cytochrome c oxidase assembly.

**Summary**, from NCBI Gene [152100](https://www.ncbi.nlm.nih.gov/gene/152100):

> Enables protein folding chaperone. Involved in mitochondrial respiratory chain complex IV assembly. Located in mitochondrion. Is active in mitochondrial intermembrane space. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28783](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28783) · Entrez [152100](https://www.ncbi.nlm.nih.gov/gene/152100) · UniProt [Q7Z7K0](https://www.uniprot.org/uniprotkb/Q7Z7K0) · Ensembl [ENSG00000187118](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187118)

## Data

Gene col 11889: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11889); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11889, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11889]; `tensor/DDL_lfc|DDL_z.npy` [11889]; `embed/gene_vectors.npy` [11889]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11889 or target_col == 11889). Every well: [[CMC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CMC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
