---
symbol: "HIBCH"
type: "gene"
col: 12535
ensembl_id: "ENSG00000198130"
name: "3-hydroxyisobutyryl-CoA hydrolase"
location: "2q32.2"
module: 60
arm: "+"
pooled_cpm: 120.69
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 23
n_dd_up_clean: 14
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# HIBCH

*3-hydroxyisobutyryl-CoA hydrolase* — 2q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 3.04× (z +29.3, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.628× (z -18.3, q 0e+00, down in 33 of 48 measured lines) ⚠ cell-cycle shift, explains ~62% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.618× (z -13.4, q 1e-38, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKRD39]] (+0.76, fdr 7e-06), [[CACYBP]] (+0.75, fdr 7e-06), [[TMEM161A]] (+0.66, fdr 7e-06); moves opposite to [[HIVEP2]] (-0.62, fdr 1e-05), [[HIVEP1]] (-0.60, fdr 1e-05), [[CGGBP1]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 060]] (heat shock).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12535.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **3.04×** | +29.3 | 0e+00 | 48/48 (HEC-1-A, A498, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.54×** | +26.0 | 0e+00 | 44/48 (HOP62, C32, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.47×** | +25.2 | 0e+00 | 47/48 (HEC-1-A, HT-29, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.06×** | +20.2 | 0e+00 | 45/48 (A498, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.93×** | +18.3 | 0e+00 | 44/48 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.74×** | +15.5 | 0e+00 | 45/48 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.96×** | +15.4 | 0e+00 | 43/45 (HEC-1-A, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.73×** | +15.2 | 0e+00 | 47/48 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.04×** | +14.2 | 7e-44 | 45/49 (HOP62, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.35×** | +12.0 | 2e-31 | 39/48 (LOX-IMVI, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.38×** | +8.9 | 2e-17 | 38/48 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.35×** | +8.4 | 2e-15 | 38/48 (SW1417, LS 180, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.33×** | +8.0 | 8e-14 | 42/49 (SW1417, LS 180, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.73×** | +7.8 | 3e-13 | 40/49 (AsPC-1, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.65×** | +7.1 | 5e-11 | 36/47 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Infigratinib (drug)]] 5 µM |  | **1.58×** | +6.5 | 3e-09 | 32/48 (HEC-1-A, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.25×** | +6.1 | 3e-08 | 25/48 (NCI-H2347, SW 900, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.23×** | +5.8 | 2e-07 | 24/48 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.15× | +5.6 | 7e-07 | 18/48 (KATO III, NCI-H2347, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 19 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12535.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.628×** | -18.3 | 0e+00 | 33/48 (A498, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.596×** | -14.4 | 8e-45 | 38/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.615×** | -13.5 | 2e-39 | 41/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.618×** | -13.4 | 1e-38 | 40/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.656×** | -11.8 | 7e-30 | 36/48 (A498, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.696×** | -10.1 | 5e-22 | 36/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.710×** | -9.5 | 1e-19 | 31/49 (HEC-1-A, RPMI-7951, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.701×** | -9.5 | 1e-19 | 34/48 (A498, PANC-1, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.732×** | -8.7 | 2e-16 | 30/48 (A498, NCI-H460, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~67% of this change | **0.760×** | -7.6 | 1e-12 | 33/48 (PANC-1, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.774×** | -7.1 | 6e-11 | 35/48 (LS 180, LoVo, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.802×** | -6.1 | 4e-08 | 25/47 (SW 900, LS 180, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **0.800×** | -6.0 | 1e-07 | 25/47 (AN3 CA, RPMI-7951, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.810×** | -5.8 | 2e-07 | 26/47 (LoVo, NCI-H23, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.865× | -5.7 | 5e-07 | 18/49 (HT-29, LoVo, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.866× | -5.6 | 6e-07 | 19/48 (SW1417, NCI-H2347, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.821×** | -5.3 | 4e-06 | 26/47 (LS 180, HT-29, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.857× | -4.3 | 4e-04 | 16/48 (SW 900, HT-29, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.857× | -4.1 | 9e-04 | 17/48 (Hs 766T, CFPAC-1, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.752×** | -4.0 | 0.001 | 22/48 (Hs 766T, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.757×** | -3.9 | 0.002 | 18/48 (A498, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.870× | -3.9 | 0.002 | 23/48 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.808×** | -3.0 | 0.052 | 13/48 (A498, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **0.815×** | -2.9 | 0.074 | 13/46 (SHP-77, BT-474, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12535. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 128 | 6 (1 ⚠) | 12 (10 ⚠) | [[Panobinostat (drug)]] 5 µM 2.37× (z +14.9) | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -21.8) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.441× (z -14.1) |
| [[SW1417 (line)]] | alt | 151 | 11 (4 ⚠) | 7 (6 ⚠) | [[Bortezomib (drug)]] 0.05 µM 3.18× (z +17.3) | [[Dinaciclib (drug)]] 0.5 µM 0.484× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.528× (z -10.1) |
| [[PANC-1 (line)]] | alt | 110 | 9 (1 ⚠) | 8 (7 ⚠) | [[Bortezomib (drug)]] 0.05 µM 3.37× (z +20.2) | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -23.9) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.513× (z -11.8) |
| [[A-172 (line)]] | wt | 103 | 10 (2 ⚠) | 5 (4 ⚠) | [[Bortezomib (drug)]] 0.05 µM 4.97× (z +20.2) | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -19.4) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.498× (z -9.4) |
| [[HOP62 (line)]] | alt | 71.8 | 9 (1 ⚠) | 6 (5 ⚠) | [[Auranofin (drug)]] 5 µM 7.29× (z +24.0) | [[Homoharringtonine (drug)]] 5 µM 0.446× (z -13.8) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.417× (z -10.5) |
| [[A498 (line)]] | wt | 145 | 6 (1 ⚠) | 8 (7 ⚠) | [[Bortezomib (drug)]] 0.05 µM 4.88× (z +21.9) | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -27.9) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.537× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 177 | 4 (1 ⚠) | 9 (8 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.90× (z +15.1) | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -20.5) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.515× (z -10.0) |
| [[LOX-IMVI (line)]] | wt | 99.3 | 10 (2 ⚠) | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 4.82× (z +21.0) | [[Homoharringtonine (drug)]] 5 µM 0.601× (z -9.7) ⚠ cell-cycle shift, explains ~62% of this change |
| [[SW480 (line)]] | alt | 137 | 3 | 9 (8 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 1.83× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.279× (z -24.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.357× (z -20.3) |
| [[HEC-1-A (line)]] | alt | 147 | 10 (2 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 4.12× (z +23.2) | [[Dinaciclib (drug)]] 0.5 µM 0.408× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HS-578T (line)]] | alt | 91.2 | 7 (1 ⚠) | 4 (4 ⚠) | [[Auranofin (drug)]] 5 µM 4.83× (z +19.4) | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -18.4) ⚠ cell-cycle shift, explains ~62% of this change |
| [[LoVo (line)]] | wt | 161 | 9 (1 ⚠) | 2 (2 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.83× (z +16.0) | [[Homoharringtonine (drug)]] 0.5 µM 0.572× (z -9.0) ⚠ cell-cycle shift, explains ~37% of this change |
| [[SW 900 (line)]] | alt | 99.0 | 7 | 3 (3 ⚠) | [[Auranofin (drug)]] 5 µM 4.17× (z +17.1) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.445× (z -9.8) ⚠ cell-cycle shift, explains ~32% of this change |
| [[C32 (line)]] | wt | 75.6 | 7 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 10.1× (z +22.8) | [[Harringtonine (drug)]] 0.5 µM 0.395× (z -9.2) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HT-29 (line)]] | alt | 87.2 | 9 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.77× (z +20.4) | — |
| [[hTERT-HPNE (line)]] | wt | 75.6 | 8 (1 ⚠) | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 4.56× (z +12.9) | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -11.5) ⚠ cell-cycle shift, explains ~62% of this change |
| [[RPMI-7951 (line)]] | alt | 128 | 5 (1 ⚠) | 4 (4 ⚠) | [[Auranofin (drug)]] 5 µM 4.29× (z +17.1) | [[Dinaciclib (drug)]] 0.5 µM 0.327× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[AsPC-1 (line)]] | alt | 149 | 7 (1 ⚠) | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 3.82× (z +16.9) | [[Homoharringtonine (drug)]] 5 µM 0.631× (z -8.8) ⚠ cell-cycle shift, explains ~62% of this change |
| [[BT-474 (line)]] | alt | 80.2 | 8 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 6.24× (z +18.2) | — |
| [[Hs 766T (line)]] | wt | 165 | 2 | 6 (5 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.77× (z +11.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.347× (z -12.1) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.466× (z -8.7) |
| [[J82 (line)]] | alt | 64.3 | 7 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 3.77× (z +15.0) | [[Homoharringtonine (drug)]] 5 µM 0.552× (z -9.5) ⚠ cell-cycle shift, explains ~62% of this change |
| [[MIA PaCa-2 (line)]] | alt | 111 | 5 | 3 (2 ⚠) | [[Auranofin (drug)]] 5 µM 4.24× (z +16.1) | [[Digitoxin (drug)]] 5 µM 0.427× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.433× (z -9.3) |
| [[NCI-H2030 (line)]] | alt | 162 | 4 | 4 (4 ⚠) | [[Auranofin (drug)]] 5 µM 2.31× (z +13.1) | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -20.4) ⚠ cell-cycle shift, explains ~62% of this change |
| [[SK-MEL-2 (line)]] | alt | 76.9 | 7 | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 3.89× (z +13.5) | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -13.3) ⚠ cell-cycle shift, explains ~62% of this change |
| [[SNU-423 (line)]] | alt | 60.8 | 4 | 4 (3 ⚠) | [[Auranofin (drug)]] 5 µM 3.43× (z +12.5) | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -12.4) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.400× (z -9.3) |
| [[A549 (line)]] | wt | 113 | 3 | 4 (4 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.32× (z +11.3) | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -17.0) ⚠ cell-cycle shift, explains ~62% of this change |
| [[LS 180 (line)]] | wt | 190 | 7 (4 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 1.74× (z +12.1) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 1.83× (z +9.4) | — |
| [[NCI-H1792 (line)]] | alt | 90.7 | 2 | 5 (5 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.43× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.543× (z -11.3) ⚠ cell-cycle shift, explains ~62% of this change |
| [[NCI-H23 (line)]] | alt | 184 | 3 (1 ⚠) | 4 (4 ⚠) | [[Auranofin (drug)]] 5 µM 2.52× (z +14.5) | [[Homoharringtonine (drug)]] 5 µM 0.585× (z -12.0) ⚠ cell-cycle shift, explains ~62% of this change |
| [[NCI-H2347 (line)]] | alt | 73.6 | 6 | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 3.98× (z +16.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.612× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 95.8 | 7 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.79× (z +18.7) | — |
| [[A-427 (line)]] | wt | 143 | 4 (1 ⚠) | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 3.11× (z +16.1) | [[Dinaciclib (drug)]] 0.5 µM 0.420× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[CFPAC-1 (line)]] | alt | 108 | 3 | 2 (2 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.46× (z +11.8) | [[Homoharringtonine (drug)]] 5 µM 0.452× (z -15.7) ⚠ cell-cycle shift, explains ~62% of this change |
| [[H4 (line)]] | wt | 114 | 2 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 3.34× (z +11.3) | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -10.9) ⚠ cell-cycle shift, explains ~62% of this change |
| [[KATO III (line)]] | alt | 94.7 | 2 (1 ⚠) | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.41× (z +10.6) | [[Dinaciclib (drug)]] 0.05 µM 0.323× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.489× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 103 | 4 (1 ⚠) | 0 | [[Bortezomib (drug)]] 0.05 µM 2.98× (z +13.5) | — |
| [[CHP-212 (line)]] | wt | 149 | 2 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.19× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 93.3 | 1 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.63× (z +9.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.527× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 114 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.71× (z +14.1) | — |
| [[SHP-77 (line)]] | alt | 156 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.32× (z +12.1) | [[Digitoxin (drug)]] 5 µM 0.539× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SW 1088 (line)]] | alt | 147 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0789× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Simotinib (drug)]] 0.05 µM 0.0998× (z -10.5) |
| [[AN3 CA (line)]] | alt | 147 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.267× (z -9.9) ⚠ toxic; cell-cycle shift, explains ~37% of this change |
| [[HepG2_C3A (line)]] | wt | 99.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.63× (z +9.2) | — |
| [[SW 1271 (line)]] | alt | 160 | 0 | 1 | — | [[Vilanterol (drug)]] 0.5 µM 0.122× (z -11.8) |
| [[C-33 A (line)]] | alt | 138 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 220 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 232 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12535), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD39]] | +0.76 | +0.75 / +0.62 | both halves | 7e-06 |  |
| [[CACYBP]] | +0.75 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[TMEM161A]] | +0.66 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[HSPE1]] | +0.64 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[MINDY4]] | +0.64 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[PWWP3A]] | +0.64 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[FAM241B]] | +0.64 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[GNPDA2]] | +0.64 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[HSP90AB3P]] | +0.63 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[CAMK2G]] | +0.63 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[ANKRD23]] | +0.62 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[HSP90AA2P]] | +0.62 | +0.64 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HIVEP2]] | -0.62 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[HIVEP1]] | -0.60 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[CGGBP1]] | -0.58 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[ERF]] | -0.54 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[PHF19]] | -0.53 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[APLF]] | -0.53 | -0.45 / -0.38 | both halves | 6e-05 |  |
| [[SMIM19]] | -0.52 | -0.47 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.677). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-17.8, -9.2); signed map (-26.5, -27.1). **Vector** length 127, 43.8% of its response variance represented; |z| ≥ 3 in 1,811 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Mitochondrial unfolded protein response (UPRmt)* (reactome, mean cos +0.51 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +16.3 | +25.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +16.1 | +29.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +13.5 | +20.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +11.3 | +26.0 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +11.1 | +15.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +8.8 | +14.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.8 | +2.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.2 | +4.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | -11.4 | -18.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -9.5 | -11.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -9.4 | -5.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -6.9 | -8.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | -6.5 | -9.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.5 | -3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.3 | -5.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.7 | -5.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.5 | -2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.1 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | 3-hydroxyisobutyryl-CoA hydrolase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q32.2 — chr2:190,189,735-190,344,193 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Thioester hydrolases |
| Hallmark sets | FATTY_ACID_METABOLISM, ADIPOGENESIS |
| Reactome | 4 pathways, smallest: Diseases of branched-chain amino acid catabolism; Branched-chain amino acid catabolism; Diseases of metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6NVY1](https://www.uniprot.org/uniprotkb/Q6NVY1) (3-hydroxyisobutyryl-CoA hydrolase, mitochondrial):

> Hydrolyzes 3-hydroxyisobutyryl-CoA (HIBYL-CoA), a saline catabolite. Has high activity toward isobutyryl-CoA. Could be an isobutyryl-CoA dehydrogenase that functions in valine catabolism. Also hydrolyzes 3-hydroxypropanoyl-CoA.

**Summary**, from NCBI Gene [26275](https://www.ncbi.nlm.nih.gov/gene/26275):

> This gene encodes the enzyme responsible for hydrolysis of both HIBYL-CoA and beta-hydroxypropionyl-CoA. Mutations in this gene have been associated with 3-hyroxyisobutyryl-CoA hydrolase deficiency. Alternative splicing results in multiple transcript variants.[provided by RefSeq, May 2010]

**Accessions** — [HGNC:4908](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4908) · Entrez [26275](https://www.ncbi.nlm.nih.gov/gene/26275) · UniProt [Q6NVY1](https://www.uniprot.org/uniprotkb/Q6NVY1) · Ensembl [ENSG00000198130](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198130)

## Data

Gene col 12535: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12535); `tables/drug_effects.parquet` (63 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12535, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12535]; `tensor/DDL_lfc|DDL_z.npy` [12535]; `embed/gene_vectors.npy` [12535]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12535 or target_col == 12535). Every well: [[HIBCH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HIBCH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
