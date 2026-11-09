---
symbol: "TSC22D2"
type: "gene"
col: 12204
ensembl_id: "ENSG00000196428"
name: "TSC22 domain family member 2"
location: "3q25.1"
module: 31
arm: "+"
pooled_cpm: 323.71
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 12
n_dd_up_clean: 21
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 12
direction_downstream: 1
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# TSC22D2

*TSC22 domain family member 2* — 3q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.41× (z +17.9, q 0e+00, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.398× (z -12.8, q 2e-34, down in 42 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 0.5 µM: 0.709× (z -5.0, q 8e-05, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PICALM]] (+0.60, fdr 9e-06), [[FA2H]] (+0.57, fdr 4e-05), [[UGCG]] (+0.56, fdr 1e-05); moves opposite to [[MCM3AP]] (-0.63, fdr 2e-05), [[RCC1L]] (-0.51, fdr 5e-05), [[MAPKAPK5]] (-0.51, fdr 4e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[S100A14]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Tofacitinib (drug)]] 0.05 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12204.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.41×** | +17.9 | 0e+00 | 42/48 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.43×** | +17.7 | 0e+00 | 48/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.84×** | +15.0 | 0e+00 | 47/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.54×** | +13.4 | 1e-38 | 46/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.38×** | +12.5 | 1e-33 | 46/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.12×** | +10.4 | 3e-23 | 40/48 (A-427, A498, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.01×** | +10.0 | 1e-21 | 40/48 (C32, A-427, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.91×** | +8.9 | 3e-17 | 32/47 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.04×** | +8.4 | 4e-15 | 40/49 (PANC-1, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.71×** | +7.5 | 4e-12 | 41/48 (A-427, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.68×** | +7.5 | 5e-12 | 38/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.39×** | +6.6 | 2e-09 | 41/49 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.52×** | +6.0 | 7e-08 | 34/48 (HS-578T, A-172, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.49×** | +5.7 | 5e-07 | 32/48 (A-427, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.47×** | +5.5 | 1e-06 | 37/48 (HT-29, LS 180, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.44×** | +5.3 | 5e-06 | 29/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.42×** | +5.0 | 2e-05 | 32/48 (Hs 766T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.39×** | +4.7 | 7e-05 | 33/48 (KATO III, HCT15, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12204.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.398×** | -12.8 | 2e-34 | 42/44 (NCI-H2347, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.465×** | -11.0 | 7e-26 | 41/49 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.657×** | -5.6 | 4e-06 | 30/45 (NCI-H2347, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.709×** | -5.0 | 8e-05 | 37/48 (NCI-H1573, KATO III, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.911× | -5.0 | 8e-05 | 0/50 | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.719×** | -4.6 | 4e-04 | 29/48 (NCI-H2347, HS-578T, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.740×** | -4.4 | 0.001 | 32/48 (BT-474, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.755×** | -4.1 | 0.003 | 32/48 (NCI-H1573, NCI-H2347, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.757×** | -4.0 | 0.003 | 34/48 (NCI-H2347, HT-29, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.831×** | -3.8 | 0.008 | 23/48 (NCI-H2347, BT-474, …) | rises with dose | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.844× | -3.5 | 0.024 | 20/48 (COLO 205, NCI-H2347, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.787×** | -3.5 | 0.025 | 27/48 (NCI-H1573, HOP62, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.789×** | -3.3 | 0.042 | 27/47 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.853× | -3.3 | 0.044 | 22/48 (NCI-H2347, BT-474, …) | top dose only | position effect removed |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.812×** | -3.0 | 0.095 | 23/49 (RPMI-7951, SW48, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12204. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 271 | 13 (3 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 8.78× (z +28.2) | [[Dinaciclib (drug)]] 5 µM 0.375× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 182 | 14 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 12.1× (z +22.0) | — |
| [[SW480 (line)]] | alt | 137 | 13 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.78× (z +21.8) | — |
| [[NCI-H2347 (line)]] | alt | 1,121 | 0 | 12 (10 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0763× (z -28.1) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.456× (z -12.2) |
| [[HT-29 (line)]] | alt | 340 | 9 (3 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.02× (z +14.8) | [[Dinaciclib (drug)]] 5 µM 0.336× (z -11.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 214 | 9 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +16.2) | [[Dinaciclib (drug)]] 0.05 µM 0.384× (z -9.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 326 | 8 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +18.5) | [[Dinaciclib (drug)]] 5 µM 0.288× (z -15.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 228 | 8 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +22.7) | [[Dinaciclib (drug)]] 0.5 µM 0.365× (z -11.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 545 | 7 (2 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.53× (z +16.2) | [[Dinaciclib (drug)]] 5 µM 0.103× (z -23.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 189 | 9 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +19.7) | [[Dinaciclib (drug)]] 5 µM 0.321× (z -13.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 199 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +15.7) | — |
| [[SW1417 (line)]] | alt | 397 | 6 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +20.6) | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -15.2) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 238 | 8 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 3.74× (z +12.3) | — |
| [[HepG2_C3A (line)]] | wt | 202 | 7 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.01× (z +14.5) | [[Dinaciclib (drug)]] 0.05 µM 0.309× (z -11.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 122 | 8 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.33× (z +15.8) | — |
| [[J82 (line)]] | alt | 415 | 5 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.43× (z +13.2) | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -12.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 256 | 8 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.95× (z +20.1) | — |
| [[CFPAC-1 (line)]] | alt | 729 | 2 | 5 (5 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 2.59× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.124× (z -16.4) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 172 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +14.8) | — |
| [[RPMI-7951 (line)]] | alt | 225 | 5 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +15.0) | [[Dinaciclib (drug)]] 0.5 µM 0.332× (z -11.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 208 | 7 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.49× (z +15.3) | — |
| [[A498 (line)]] | wt | 289 | 4 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.18× (z +25.7) | [[Dinaciclib (drug)]] 0.5 µM 0.364× (z -10.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 162 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.99× (z +21.8) | — |
| [[HOP62 (line)]] | alt | 238 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.43× (z +12.6) | [[Dinaciclib (drug)]] 0.5 µM 0.403× (z -9.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 305 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.48× (z +16.5) | — |
| [[LS 180 (line)]] | wt | 240 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.55× (z +14.9) | [[Dinaciclib (drug)]] 5 µM 0.301× (z -10.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 305 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.00× (z +18.0) | — |
| [[NCI-H1792 (line)]] | alt | 173 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.80× (z +12.7) | — |
| [[RKO (line)]] | wt | 354 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +18.0) | [[Dinaciclib (drug)]] 0.5 µM 0.390× (z -9.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 232 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.199× (z -16.3) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 696 | 3 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.76× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.159× (z -17.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 426 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.241× (z -11.9) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 155 | 5 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.66× (z +14.7) | — |
| [[Panc 03.27 (line)]] | alt | 586 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.122× (z -20.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 370 | 2 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.40× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.182× (z -14.4) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 301 | 3 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.27× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.326× (z -10.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 280 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.261× (z -15.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 378 | 2 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.53× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.268× (z -9.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 136 | 3 (2 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.99× (z +11.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.85× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.406× (z -9.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 337 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +11.8) | [[Dinaciclib (drug)]] 0.05 µM 0.350× (z -8.8) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 269 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.273× (z -11.1) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 1,012 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.113× (z -11.4) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 165 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.76× (z +8.5) | — |
| [[HCT15 (line)]] | alt | 173 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.71× (z +9.2) | — |
| [[SW 1271 (line)]] | alt | 243 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.32× (z +9.9) | — |
| [[SW48 (line)]] | wt | 400 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.212× (z -9.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 253 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 405 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 310 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 191 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12204), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PICALM]] | +0.60 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[FA2H]] | +0.57 | +0.54 / +0.41 | both halves | 4e-05 |  |
| [[UGCG]] | +0.56 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[CRYBG2]] | +0.55 | +0.54 / +0.41 | both halves | 4e-05 |  |
| [[PPP2R2A]] | +0.55 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[ARHGAP29]] | +0.55 | +0.52 / +0.43 | both halves | 3e-05 |  |
| [[KRT19]] | +0.54 | +0.46 / +0.41 | both halves | 4e-05 |  |
| [[JPT1]] | +0.54 | +0.33 / +0.48 | both halves | 1e-04 |  |
| [[TTC9]] | +0.54 | +0.53 / +0.40 | both halves | 5e-05 |  |
| [[OXSR1]] | +0.54 | +0.54 / +0.46 | both halves | 2e-05 |  |
| [[PRSS8]] | +0.54 | +0.50 / +0.30 | both halves | 2e-04 |  |
| [[CLDN4]] | +0.53 | +0.48 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCM3AP]] | -0.63 | -0.64 / -0.46 | both halves | 2e-05 |  |
| [[RCC1L]] | -0.51 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[MAPKAPK5]] | -0.51 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[DUS3L]] | -0.50 | -0.44 / -0.37 | both halves | 7e-05 |  |
| [[KIAA0753]] | -0.49 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[DNAAF5]] | -0.49 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[VPS52]] | -0.49 | -0.38 / -0.29 | both halves | 2e-04 |  |
| [[ECHDC1]] | -0.48 | -0.40 / -0.34 | both halves | 1e-04 |  |
| [[TRUB2]] | -0.48 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[FARS2]] | -0.48 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[ITPKB]] | -0.47 | -0.17 / -0.49 | ⚠ not reproduced | 0.001 |  |
| [[CEP20]] | -0.47 | -0.36 / -0.42 | both halves | 1e-04 |  |
| [[PPWD1]] | -0.47 | -0.35 / -0.44 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 12, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[S100A14]] | B | S100A14 activity raises TSC22D2's level | lines that do not express S100A14 (33) vs lines expressing it (17) | 1.62× lower at baseline in the lines without S100A14 | 0.013 | ⚠ within organs, on part of the lines; also absent: PRSS8, RAB25, TMPRSS4 |
| [[SULT2B1]] | B | SULT2B1 activity raises TSC22D2's level | lines that do not express SULT2B1 (28) vs lines expressing it (22) | 1.56× lower at baseline in the lines without SULT2B1 | 0.019 | ⚠ within organs, on part of the lines; also absent: ATP2C2, ST14, SGPP2; maybe low, not absent |
| [[CLDN7]] | B | CLDN7 activity raises TSC22D2's level | lines that do not express CLDN7 (30) vs lines expressing it (20) | 1.54× lower at baseline in the lines without CLDN7 | 0.027 | ⚠ within organs, on part of the lines; also absent: ESRP1, ENSG00000262302, ST14 |
| [[PRSS8]] | B | PRSS8 activity raises TSC22D2's level | lines that do not express PRSS8 (33) vs lines expressing it (17) | 1.61× lower at baseline in the lines without PRSS8 | 0.033 | ⚠ within organs, on part of the lines; also absent: RAB25, TMPRSS4, LCN2 |
| [[CDH1]] | B | CDH1 activity raises TSC22D2's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 1.49× lower at baseline in the lines without CDH1 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1 |
| [[CBLC]] | B | CBLC activity raises TSC22D2's level | lines that do not express CBLC (31) vs lines expressing it (19) | 1.55× lower at baseline in the lines without CBLC | 0.055 | ⚠ within organs, on part of the lines; also absent: KDF1, CLDN7, PRSS8 |
| [[CDH3]] | B | CDH3 activity raises TSC22D2's level | lines that do not express CDH3 (26) vs lines expressing it (24) | 1.43× lower at baseline in the lines without CDH3 | 0.060 | ⚠ within organs, on part of the lines; also absent: CKMT1A, ESRP1, GPR87; maybe low, not absent |
| [[CRYBG2]] | B | CRYBG2 activity raises TSC22D2's level | lines that do not express CRYBG2 (23) vs lines expressing it (27) | 1.39× lower at baseline in the lines without CRYBG2 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SPINT1-AS1, SMPDL3B, LAD1 |
| [[CDH1]] | B | CDH1 activity weakens TSC22D2's drug response | lines that do not express CDH1 (31) vs lines expressing it (18) | the lines without CDH1 respond 1.25× as strongly (z diff -1.63); strongest at Harringtonine 5 µM: 2.60x vs 1.40x (z diff -4.4) | 0.069 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1; target measured in part of the lines; artifact flags |
| [[S100A14]] | B | S100A14 activity weakens TSC22D2's drug response | lines that do not express S100A14 (33) vs lines expressing it (16) | the lines without S100A14 respond 1.29× as strongly (z diff -1.62); strongest at Harringtonine 5 µM: 2.57x vs 1.32x (z diff -5.0) | 0.070 | ⚠ within organs, on part of the lines; also absent: PRSS8, RAB25, TMPRSS4; target measured in part of the lines; artifact flags |
| [[LMTK3]] | B | LMTK3 activity raises TSC22D2's level | lines that do not express LMTK3 (15) vs lines expressing it (35) | 1.39× lower at baseline in the lines without LMTK3 | 0.092 | ⚠ within organs, on part of the lines; also absent: CRYBG2, CXADR, CCDC120; maybe low, not absent |
| [[FAM83A]] | B | FAM83A activity raises TSC22D2's level | lines that do not express FAM83A (37) vs lines expressing it (13) | 1.66× lower at baseline in the lines without FAM83A | 0.099 | ⚠ within organs, on part of the lines; also absent: GSDMC, DAPP1, S100A9 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Tofacitinib (drug)]] 0.05 µM | C | TSC22D2's natural level lowers the cells' numbers under Tofacitinib 0.05 µM (makes them more sensitive) | TSC22D2's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.68 | 0.285 over the table, 0.077 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.479). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.6, 29.6); signed map (-1.8, 38.1). **Vector** length 88.6, 36.4% of its response variance represented; |z| ≥ 3 in 1,714 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.3 | +4.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.8 | +2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.1 | +6.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.6 | +5.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.5 | +5.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.4 | +4.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +4.3 | +4.6 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +3.2 | +2.6 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -4.2 | +7.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.1 | +17.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.6 | +4.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.6 | +2.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.4 | +8.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.8 | -0.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.5 | +1.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -2.1 | -5.0 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.9 | +0.7 |

## What is on record

|  |  |
|---|---|
| Name | TSC22 domain family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q25.1 — chr3:150,408,298-150,466,422 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0669, TILZ4a, TILZ4b, TILZ4c |
| Gene groups (HGNC) | TSC22 domain family |
| Matched by | ensembl_id |

**Function**, from UniProt [O75157](https://www.uniprot.org/uniprotkb/O75157) (TSC22 domain family protein 2):

> Reduces the level of nuclear PKM isoform M2 which results in repression of cyclin CCND1 transcription and reduced cell growth.

**Summary**, from NCBI Gene [9819](https://www.ncbi.nlm.nih.gov/gene/9819):

> Involved in negative regulation of cell cycle. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29095](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29095) · Entrez [9819](https://www.ncbi.nlm.nih.gov/gene/9819) · UniProt [O75157](https://www.uniprot.org/uniprotkb/O75157) · Ensembl [ENSG00000196428](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196428)

## Data

Gene col 12204: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12204); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12204, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12204]; `tensor/DDL_lfc|DDL_z.npy` [12204]; `embed/gene_vectors.npy` [12204]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12204 or target_col == 12204). Every well: [[TSC22D2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TSC22D2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
