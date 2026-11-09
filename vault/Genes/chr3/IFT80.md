---
symbol: "IFT80"
type: "gene"
col: 903
ensembl_id: "ENSG00000068885"
name: "intraflagellar transport 80"
location: "3q25.33"
module: 3
arm: "-"
pooled_cpm: 54.46
n_lines_expressing: 50
n_dd_up: 35
n_dd_down: 23
n_dd_up_clean: 33
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# IFT80

*intraflagellar transport 80* — 3q25.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.78× (z +14.8, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.285× (z -18.1, q 0e+00, down in 46 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.325× (z -16.2, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DZIP3]] (+0.61, fdr 1e-05), [[IFT81]] (+0.56, fdr 5e-05), [[FH]] (+0.51, fdr 3e-05); moves opposite to [[CCNQ]] (-0.55, fdr 4e-05), [[RILPL1]] (-0.53, fdr 5e-05), [[PTDSS2]] (-0.53, fdr 3e-05).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 903.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.78×** | +14.8 | 0e+00 | 48/48 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.56×** | +13.5 | 3e-39 | 48/48 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.50×** | +13.2 | 2e-37 | 47/48 (KATO III, LoVo, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +11.4 | 8e-28 | 42/48 (SW1417, SW480, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.12×** | +8.5 | 2e-15 | 43/48 (KATO III, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +7.5 | 4e-12 | 36/48 (NCI-H2347, KATO III, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.65×** | +7.2 | 6e-11 | 40/48 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +6.9 | 3e-10 | 35/48 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.62×** | +6.7 | 2e-09 | 27/42 (NCI-H1573, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +6.2 | 4e-08 | 27/48 (SW480, C32, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.48×** | +5.7 | 7e-07 | 37/48 (HEC-1-A, SW1417, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.07×** | +5.5 | 2e-06 | 38/48 (KATO III, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +5.4 | 4e-06 | 32/48 (SW1417, PANC-1, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.42×** | +4.8 | 6e-05 | 32/47 (HEC-1-A, NCI-H1573, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.40×** | +4.6 | 2e-04 | 32/47 (NCI-H1573, HEC-1-A, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.33×** | +4.1 | 0.001 | 23/48 (LS 180, KATO III, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 903.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.285×** | -18.1 | 0e+00 | 46/48 (PANC-1, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.325×** | -16.2 | 0e+00 | 47/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.336×** | -15.7 | 0e+00 | 47/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.376×** | -14.1 | 8e-43 | 46/48 (PANC-1, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.526×** | -9.3 | 2e-18 | 41/48 (RPMI-7951, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.573×** | -7.7 | 1e-12 | 37/47 (J82, RKO, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.675×** | -5.3 | 8e-06 | 32/48 (KATO III, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.773×** | -5.2 | 1e-05 | 33/48 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.518×** | -4.9 | 5e-05 | 28/49 (A-427, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.648×** | -4.9 | 5e-05 | 25/47 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.536×** | -4.7 | 1e-04 | 27/48 (A-427, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.726×** | -4.6 | 2e-04 | 28/48 (KATO III, A-427, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.673×** | -4.5 | 3e-04 | 26/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.738×** | -4.4 | 5e-04 | 27/48 (CFPAC-1, H4, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.739×** | -4.3 | 5e-04 | 29/48 (SW480, J82, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.762×** | -3.9 | 0.003 | 29/48 (CFPAC-1, SK-MEL-2, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.767×** | -3.6 | 0.010 | 19/47 (MIA PaCa-2, A-427, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.706×** | -3.6 | 0.011 | 24/48 (A-427, HCT15, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 903. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 137 | 2 | 8 (3 ⚠) | [[Belinostat (drug)]] 5 µM 2.12× (z +9.7) | [[Digitoxin (drug)]] 5 µM 0.273× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.117× (z -14.6) |
| [[SW480 (line)]] | alt | 60.3 | 5 | 5 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +11.8) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.128× (z -20.5) |
| [[KATO III (line)]] | alt | 75.1 | 3 | 6 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.68× (z +12.8) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.218× (z -15.1) |
| [[LoVo (line)]] | wt | 28.3 | 5 (1 ⚠) | 4 (1 ⚠) | [[Belinostat (drug)]] 5 µM 4.21× (z +11.6) | [[Digitoxin (drug)]] 5 µM 0.244× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.282× (z -10.3) |
| [[NCI-H460 (line)]] | wt | 35.7 | 2 | 7 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.87× (z +8.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.250× (z -11.8) |
| [[PANC-1 (line)]] | alt | 90.1 | 3 | 5 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.51× (z +11.0) | [[Digitoxin (drug)]] 5 µM 0.119× (z -25.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.177× (z -20.9) |
| [[SW1417 (line)]] | alt | 41.8 | 5 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +12.4) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.264× (z -10.7) |
| [[HCT15 (line)]] | alt | 60.0 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.214× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.229× (z -9.6) |
| [[J82 (line)]] | alt | 96.6 | 0 | 6 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.121× (z -17.7) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.241× (z -12.4) |
| [[MIA PaCa-2 (line)]] | alt | 49.1 | 3 | 3 | [[Panobinostat (drug)]] 5 µM 4.67× (z +10.2) | [[Ixazomib citrate (drug)]] 5 µM 0.204× (z -10.6) |
| [[RKO (line)]] | wt | 39.4 | 4 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.01× (z +11.0) | [[Niclosamide (olamine) (drug)]] 5 µM 0.205× (z -10.5) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.228× (z -10.1) |
| [[COLO 205 (line)]] | alt | 79.2 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.134× (z -17.0) |
| [[HOP62 (line)]] | alt | 53.8 | 1 | 4 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.62× (z +9.1) | [[Digitoxin (drug)]] 5 µM 0.187× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.251× (z -10.3) |
| [[HS-578T (line)]] | alt | 89.4 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.142× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.217× (z -12.6) |
| [[HT-29 (line)]] | alt | 49.2 | 2 | 3 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.05× (z +8.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.244× (z -11.4) |
| [[LS 180 (line)]] | wt | 24.5 | 3 | 2 | [[Panobinostat (drug)]] 5 µM 5.49× (z +10.1) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.153× (z -11.2) |
| [[NCI-H2347 (line)]] | alt | 20.8 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 4.62× (z +11.1) | — |
| [[H4 (line)]] | wt | 81.9 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.175× (z -11.7) |
| [[HEC-1-A (line)]] | alt | 69.2 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.82× (z +9.8) | — |
| [[RPMI-7951 (line)]] | alt | 75.5 | 1 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Ixazomib citrate (drug)]] 5 µM 0.247× (z -11.3) |
| [[SHP-77 (line)]] | alt | 58.9 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0937× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.168× (z -14.8) |
| [[SNU-423 (line)]] | alt | 47.8 | 1 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.87× (z +10.2) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.230× (z -11.2) |
| [[A-172 (line)]] | wt | 53.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.89× (z +11.3) | — |
| [[A549 (line)]] | wt | 52.0 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.70× (z +10.6) | — |
| [[AsPC-1 (line)]] | alt | 14.4 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.09× (z +9.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 6.41× (z +9.5) | — |
| [[BT-474 (line)]] | alt | 17.8 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 7.66× (z +9.5) | — |
| [[C-33 A (line)]] | alt | 76.7 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.282× (z -8.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.285× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 109 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.237× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.371× (z -10.0) |
| [[Panc 03.27 (line)]] | alt | 54.7 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +8.5) | [[Digitoxin (drug)]] 5 µM 0.195× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.325× (z -8.8) |
| [[SW 900 (line)]] | alt | 54.3 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.277× (z -9.7) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.330× (z -8.7) |
| [[A498 (line)]] | wt | 48.0 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.90× (z +9.1) | [[Niclosamide (olamine) (drug)]] 5 µM 0.307× (z -9.9) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 33.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.01× (z +9.1) | — |
| [[LOX-IMVI (line)]] | wt | 40.3 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.231× (z -9.6) |
| [[NCI-H1792 (line)]] | alt | 48.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +13.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Digitoxin (drug)]] 5 µM 0.257× (z -11.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 39.4 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0600× (z -15.4) |
| [[AN3 CA (line)]] | alt | 53.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0852× (z -11.0) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 44.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.230× (z -10.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 47.4 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.317× (z -8.6) |
| [[hTERT-HPNE (line)]] | wt | 43.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.226× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 45.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.23× (z +10.2) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 37.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 60.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.98× (z +8.8) | — |
| [[CHP-212 (line)]] | wt | 50.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 82.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 65.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 903), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DZIP3]] | +0.61 | +0.75 / +0.51 | both halves | 1e-05 |  |
| [[IFT81]] | +0.56 | +0.56 / +0.40 | both halves | 5e-05 | pathway: Assembly of the 9+0 primary cilium; STRING 998 |
| [[FH]] | +0.51 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[SPDL1]] | +0.51 | +0.62 / +0.42 | both halves | 4e-05 |  |
| [[CCDC148]] | +0.51 | +0.71 / +0.47 | both halves | 2e-05 |  |
| [[SUB1]] | +0.50 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[CETN3]] | +0.50 | +0.62 / +0.30 | both halves | 2e-04 |  |
| [[ACAA2]] | +0.50 | +0.51 / +0.39 | both halves | 5e-05 |  |
| [[KIF11]] | +0.50 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[C2CD5]] | +0.50 | +0.52 / +0.42 | both halves | 4e-05 |  |
| [[YWHAE]] | +0.49 | +0.47 / +0.33 | both halves | 1e-04 | pathway: Assembly of the 9+0 primary cilium |
| [[COPS3]] | +0.49 | +0.41 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNQ]] | -0.55 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[RILPL1]] | -0.53 | -0.55 / -0.39 | both halves | 5e-05 |  |
| [[PTDSS2]] | -0.53 | -0.64 / -0.43 | both halves | 3e-05 |  |
| [[ARL8A]] | -0.53 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[FLYWCH1]] | -0.50 | -0.56 / -0.40 | both halves | 5e-05 |  |
| [[SLC35D2]] | -0.50 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[GPR89A]] | -0.50 | -0.58 / -0.30 | both halves | 2e-04 |  |
| [[ANKS6]] | -0.50 | -0.62 / -0.29 | both halves | 2e-04 |  |
| [[FAM89A]] | -0.49 | -0.52 / -0.26 | both halves | 4e-04 |  |
| [[GPR89B]] | -0.49 | -0.51 / -0.26 | both halves | 4e-04 |  |
| [[LSM10]] | -0.48 | -0.34 / -0.33 | both halves | 1e-04 |  |
| [[DENND10]] | -0.47 | -0.44 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers IFT80's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.413). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-15.8, 4.1); signed map (17.4, -36.0). **Vector** length 70.6, 21.1% of its response variance represented; |z| ≥ 3 in 1,400 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +4.1 | -4.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | -2.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.9 | -4.7 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +1.9 |
|  | [[Megestrol (drug)]] 0.05 µM |  | +1.8 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +5.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | +1.7 | +0.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.6 | +3.2 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +1.6 | +2.0 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -6.7 | -1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.1 | -4.6 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -4.3 | -3.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.7 | -5.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.5 | -7.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.4 | -0.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.4 | -5.2 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -2.3 | -0.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.2 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | intraflagellar transport 80 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q25.33 — chr3:160,256,986-160,399,880 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1374, FAP167, CFAP167; previously WDR56 |
| Gene groups (HGNC) | WD repeat domain containing; IFT-B2 complex |
| Reactome | 4 pathways, smallest: Intraflagellar transport; Assembly of the 9+0 primary cilium; Cilium Assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P2H3](https://www.uniprot.org/uniprotkb/Q9P2H3) (Intraflagellar transport protein 80 homolog):

> Component of the intraflagellar transport (IFT) complex B, which is essential for the development and maintenance of motile and sensory cilia.

**Summary**, from NCBI Gene [57560](https://www.ncbi.nlm.nih.gov/gene/57560):

> The protein encoded by this gene is part of the intraflagellar transport complex B and is necessary for the function of motile and sensory cilia. Defects in this gene are a cause of asphyxiating thoracic dystrophy 2 (ATD2). Three transcript variants encoding two different isoforms have been found for this gene.[provided by RefSeq, Jun 2010]

**Accessions** — [HGNC:29262](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29262) · Entrez [57560](https://www.ncbi.nlm.nih.gov/gene/57560) · UniProt [Q9P2H3](https://www.uniprot.org/uniprotkb/Q9P2H3) · Ensembl [ENSG00000068885](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000068885)

## Data

Gene col 903: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 903); `tables/drug_effects.parquet` (63 rows, flagged included); `relations/gene_relations.parquet` (col_a == 903, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 903]; `tensor/DDL_lfc|DDL_z.npy` [903]; `embed/gene_vectors.npy` [903]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 903 or target_col == 903). Every well: [[IFT80 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IFT80.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
