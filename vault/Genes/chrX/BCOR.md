---
symbol: "BCOR"
type: "gene"
col: 11394
ensembl_id: "ENSG00000183337"
name: "BCL6 corepressor"
location: "Xp11.4"
module: 14
arm: "+"
pooled_cpm: 71.31
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 16
n_dd_up_clean: 9
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# BCOR

*BCL6 corepressor* — Xp11.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.41× (z +23.1, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.399× (z -17.1, q 0e+00, down in 41 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.511× (z -13.0, q 5e-36, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BHLHE41]] (+0.74, fdr 7e-06), [[NFIX]] (+0.71, fdr 7e-06), [[KLF10]] (+0.68, fdr 7e-06); moves opposite to [[ZNF731P]] (-0.64, fdr 7e-06), [[DIP2A]] (-0.57, fdr 2e-05), [[TPD52L2]] (-0.56, fdr 2e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[DPY19L2P2-1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11394.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.41×** | +23.1 | 0e+00 | 44/48 (KATO III, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **4.10×** | +14.3 | 1e-43 | 47/49 (PANC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **2.11×** | +13.9 | 2e-41 | 41/48 (RPMI-7951, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.79×** | +11.2 | 4e-27 | 38/48 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.67×** | +9.9 | 4e-21 | 34/48 (MIA PaCa-2, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.46×** | +7.3 | 3e-11 | 31/48 (NCI-H2347, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.33×** | +5.6 | 2e-06 | 30/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.66×** | +5.1 | 2e-05 | 25/48 (HEC-1-A, NCI-H2347, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +5.0 | 4e-05 | 4/50 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.27×** | +4.5 | 3e-04 | 23/48 (NCI-H460, SW480, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.25×** | +4.3 | 1e-03 | 23/49 (RPMI-7951, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +4.2 | 0.001 | 21/48 (Panc 03.27, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.25×** | +4.0 | 0.003 | 23/47 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.20×** | +3.4 | 0.023 | 20/47 (NCI-H2030, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~80% of this change | 1.18× | +3.1 | 0.071 | 19/47 (SW 900, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Radotinib (drug)]] 5 µM |  | 1.13× | +3.0 | 0.095 | 9/48 (CHP-212, AsPC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11394.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.399×** | -17.1 | 0e+00 | 41/43 (AN3 CA, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.511×** | -13.0 | 5e-36 | 43/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.535×** | -12.1 | 2e-31 | 39/48 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.593×** | -10.1 | 8e-22 | 37/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.712×** | -6.3 | 3e-08 | 29/48 (MIA PaCa-2, HOP62, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.737×** | -5.9 | 3e-07 | 30/48 (A-427, SW480, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.733×** | -5.8 | 6e-07 | 28/50 (AN3 CA, A-427, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.737×** | -5.6 | 2e-06 | 29/48 (C32, A-427, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.733×** | -5.6 | 2e-06 | 28/45 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.790×** | -4.6 | 3e-04 | 23/48 (HOP62, LS 180, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~64% of this change | **0.790×** | -4.4 | 6e-04 | 23/47 (AN3 CA, C-33 A, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.809×** | -4.1 | 0.002 | 23/48 (HOP62, C32, …) | rises with dose |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **0.826×** | -3.7 | 0.009 | 19/48 (HS-578T, HOP62, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.828×** | -3.7 | 0.010 | 21/48 (A-427, PANC-1, …) | all doses, flat |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.778×** | -3.5 | 0.020 | 16/48 (SNU-1, PANC-1, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | 0.849× | -3.2 | 0.053 | 16/49 (AsPC-1, SNU-423, …) | all doses, flat |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.853× | -3.1 | 0.070 | 10/49 (NCI-H460, MIA PaCa-2, …) | top dose only |  |
| [[vincristine (drug)]] 5 µM |  | **0.741×** | -3.0 | 0.074 | 16/46 (SHP-77, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11394. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 60.4 | 11 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +15.9) | — |
| [[AN3 CA (line)]] | alt | 600 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0163× (z -32.9) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.387× (z -11.1) |
| [[HEC-1-A (line)]] | alt | 81.5 | 7 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +15.2) | [[Panobinostat (drug)]] 5 µM 0.449× (z -9.3) |
| [[SW480 (line)]] | alt | 106 | 2 | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +10.3) | [[Panobinostat (drug)]] 5 µM 0.324× (z -17.6) |
| [[NCI-H2347 (line)]] | alt | 52.8 | 5 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +18.7) | [[Dinaciclib (drug)]] 5 µM 0.340× (z -11.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 104 | 4 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 10.4× (z +14.5) | [[Panobinostat (drug)]] 5 µM 0.312× (z -13.8) |
| [[A-427 (line)]] | wt | 80.6 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0656× (z -32.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.376× (z -11.5) |
| [[HOP62 (line)]] | alt | 72.7 | 1 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.311× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.392× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 85.4 | 3 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +17.4) | [[Panobinostat (drug)]] 5 µM 0.402× (z -10.2) |
| [[A-172 (line)]] | wt | 73.1 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -8.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 43.6 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +16.1) | [[Dinaciclib (drug)]] 5 µM 0.268× (z -12.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 61.2 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.422× (z -9.7) |
| [[NCI-H23 (line)]] | alt | 63.6 | 1 | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.17× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.220× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.325× (z -11.5) |
| [[A549 (line)]] | wt | 45.5 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +15.7) | [[Dinaciclib (drug)]] 5 µM 0.232× (z -11.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 115 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.277× (z -11.2) |
| [[HS-578T (line)]] | alt | 75.4 | 2 | 2 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 3.48× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -11.7) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 99.3 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +18.7) | [[Panobinostat (drug)]] 5 µM 0.427× (z -8.9) |
| [[KATO III (line)]] | alt | 63.6 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.82× (z +26.2) | — |
| [[LS 180 (line)]] | wt | 61.4 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.322× (z -11.5) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 83.3 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +18.3) | — |
| [[SNU-423 (line)]] | alt | 73.7 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.10× (z +19.8) | [[Dinaciclib (drug)]] 5 µM 0.255× (z -10.6) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 75.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.167× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.253× (z -11.5) |
| [[CFPAC-1 (line)]] | alt | 53.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.55× (z +23.8) | — |
| [[NCI-H1573 (line)]] | alt | 45.1 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.31× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.168× (z -16.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 37.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.32× (z +20.0) | [[Dinaciclib (drug)]] 5 µM 0.139× (z -15.2) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 155 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.115× (z -19.7) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 79.5 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +17.4) | — |
| [[COLO 205 (line)]] | alt | 36.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +12.7) | [[Dinaciclib (drug)]] 0.5 µM 0.211× (z -10.7) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 65.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +13.5) | — |
| [[Hs 766T (line)]] | wt | 59.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +12.6) | [[Dinaciclib (drug)]] 0.5 µM 0.211× (z -13.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 72.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.310× (z -9.5) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 117 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.148× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.153× (z -9.0) |
| [[SW 900 (line)]] | alt | 62.2 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +9.0) | [[Panobinostat (drug)]] 5 µM 0.380× (z -9.1) |
| [[AsPC-1 (line)]] | alt | 36.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +12.7) | — |
| [[CHP-212 (line)]] | wt | 63.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +10.3) | — |
| [[HepG2_C3A (line)]] | wt | 70.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +8.7) | — |
| [[hTERT-HPNE (line)]] | wt | 56.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +12.8) | — |
| [[LoVo (line)]] | wt | 91.5 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.14× (z +9.4) | — |
| [[LOX-IMVI (line)]] | wt | 38.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.243× (z -11.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 68.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.393× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 35.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +11.7) | — |
| [[SW48 (line)]] | wt | 62.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.279× (z -9.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 78.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 85.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 78.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 64.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11394), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BHLHE41]] | +0.74 | +0.68 / +0.75 | both halves | 7e-06 |  |
| [[NFIX]] | +0.71 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[KLF10]] | +0.68 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[ZIC2]] | +0.67 | +0.66 / +0.57 | both halves | 9e-06 |  |
| [[NR1D1]] | +0.66 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[ZNF318]] | +0.66 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[SMAD7]] | +0.64 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[GLIS2]] | +0.64 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[BCL3]] | +0.63 | +0.60 / +0.61 | both halves | 7e-06 | same gene group |
| [[ATP23]] | +0.63 | +0.57 / +0.58 | both halves | 8e-06 |  |
| [[TIFA]] | +0.62 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[MIDEAS]] | +0.61 | +0.67 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF731P]] | -0.64 | -0.65 / -0.59 | both halves | 7e-06 |  |
| [[DIP2A]] | -0.57 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[TPD52L2]] | -0.56 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[UFD1]] | -0.55 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[NAPG]] | -0.55 | -0.46 / -0.55 | both halves | 2e-05 |  |
| [[VPS53]] | -0.54 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[PPHLN1]] | -0.52 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[SENP5]] | -0.51 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[HERC2P3]] | -0.51 | -0.40 / -0.50 | both halves | 4e-05 |  |
| [[SLC30A6]] | -0.51 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[DEPDC5]] | -0.50 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[TANGO2]] | -0.50 | -0.49 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DPY19L2P2-1]] | B | DPY19L2P2-1 activity raises BCOR's level | lines that do not express DPY19L2P2-1 (17) vs lines expressing it (33) | 1.04× lower at baseline in the lines without DPY19L2P2-1 | 0.024 | ⚠ within organs, on part of the lines; also absent: RNF182, ENSG00000234405, FGF2 |
| [[DLX2]] | B | DLX2 activity raises BCOR's level | lines that do not express DLX2 (8) vs lines expressing it (42) | 1.15× lower at baseline in the lines without DLX2 | 0.086 | ⚠ within organs, on part of the lines; also absent: LINC01145-1, SCHIP1, NPHS1; maybe low, not absent |
| [[SOBP]] | B | SOBP activity raises BCOR's level | lines that do not express SOBP (19) vs lines expressing it (31) | 1.31× lower at baseline in the lines without SOBP | 0.098 | ⚠ within organs, on part of the lines; also absent: ANK2, TMEM145, SYT11 |
| [[MEX3B]] | C | MEX3B activity raises BCOR's level | lines that do not express MEX3B (4) vs lines expressing it (46) | 1.69× lower at baseline in the lines without MEX3B | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: KIF17, DPF1, CNTNAP1; its own permutation p |
| [[CNTNAP1]] | C | CNTNAP1 activity raises BCOR's level | lines that do not express CNTNAP1 (4) vs lines expressing it (46) | 1.61× lower at baseline in the lines without CNTNAP1 | 0.093 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZCCHC24, KIF17, SLC29A4 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.666). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.7, -3.0); signed map (-2.7, 12.8). **Vector** length 125, 37.6% of its response variance represented; |z| ≥ 3 in 1,182 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.7 | +23.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.0 | +13.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.4 | +11.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.4 | +4.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | +6.2 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.1 | +5.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.3 | +3.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.9 | +3.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.4 | +4.0 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | -7.5 | -5.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | -7.2 | -4.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -7.0 | -12.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.9 | -17.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.7 | -4.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.5 | -2.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.6 | -2.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.5 | -1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.3 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | BCL6 corepressor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.4 — chrX:40,049,815-40,177,329 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20285, KIAA1575 |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6W2J9](https://www.uniprot.org/uniprotkb/Q6W2J9) (BCL-6 corepressor):

> Transcriptional corepressor. May specifically inhibit gene expression when recruited to promoter regions by sequence-specific DNA-binding proteins such as BCL6 and MLLT3. This repression may be mediated at least in part by histone deacetylase activities which can associate with this corepressor. Involved in the repression of TFAP2A; impairs binding of BCL6 and KDM2B to TFAP2A promoter regions. Via repression of TFAP2A acts as a negative regulator of osteo-dentiogenic capacity in adult stem …

**Summary**, from NCBI Gene [54880](https://www.ncbi.nlm.nih.gov/gene/54880):

> The protein encoded by this gene was identified as an interacting corepressor of BCL6, a POZ/zinc finger transcription repressor that is required for germinal center formation and may influence apoptosis. This protein selectively interacts with the POZ domain of BCL6, but not with eight other POZ proteins. Specific class I and II histone deacetylases (HDACs) have been shown to interact with this protein, which suggests a possible link between the two classes of HDACs. Several transcript …

**Accessions** — [HGNC:20893](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20893) · Entrez [54880](https://www.ncbi.nlm.nih.gov/gene/54880) · UniProt [Q6W2J9](https://www.uniprot.org/uniprotkb/Q6W2J9) · Ensembl [ENSG00000183337](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183337)

## Data

Gene col 11394: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11394); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11394, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11394]; `tensor/DDL_lfc|DDL_z.npy` [11394]; `embed/gene_vectors.npy` [11394]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11394 or target_col == 11394). Every well: [[BCOR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BCOR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
