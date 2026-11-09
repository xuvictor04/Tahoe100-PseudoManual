---
symbol: "CTNNAL1"
type: "gene"
col: 4053
ensembl_id: "ENSG00000119326"
name: "catenin alpha like 1"
location: "9q31.3"
module: 120
arm: "+"
pooled_cpm: 98.74
n_lines_expressing: 49
n_dd_up: 38
n_dd_down: 3
n_dd_up_clean: 15
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/120"]
generated_by: "tahoemap"
---

# CTNNAL1

*catenin alpha like 1* — 9q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (23 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.65× (z +32.2, q 0e+00, up in 47 of 47 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 3.18× (z +20.3, q 0e+00, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Neratinib (maleate) (drug)]] 5 µM: 0.850× (z -4.1, q 0.016, down in 19 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TEAD1]] (+0.68, fdr 7e-06), [[TPM4]] (+0.62, fdr 2e-05), [[MYBL1]] (+0.60, fdr 1e-05); moves opposite to [[NGDN]] (-0.52, fdr 2e-05), [[ZNF581]] (-0.51, fdr 1e-05), [[CCDC12]] (-0.51, fdr 2e-05).
> It is in [[Module 120]], a single-armed module (RHOA GTPase cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 26 with an alert ⚠; shown: the 15 strongest and the 13 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 23 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4053.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **3.65×** | +32.2 | 0e+00 | 47/47 (AsPC-1, RKO, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.18×** | +20.3 | 0e+00 | 44/47 (MIA PaCa-2, RKO, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **2.69×** | +17.4 | 0e+00 | 43/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.69×** | +16.7 | 0e+00 | 46/47 (RKO, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **2.49×** | +16.0 | 0e+00 | 44/47 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +16.0 | 0e+00 | 38/48 (SNU-423, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **2.25×** | +13.7 | 1e-40 | 36/42 (SNU-423, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **2.04×** | +12.5 | 3e-34 | 43/47 (LS 180, SNU-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.89×** | +11.1 | 7e-27 | 44/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.87×** | +11.0 | 3e-26 | 41/47 (SW480, SNU-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.85×** | +10.7 | 3e-25 | 42/47 (LoVo, SW1417, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **1.79×** | +9.5 | 1e-19 | 38/44 (SNU-423, C-33 A, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.71×** | +9.4 | 3e-19 | 37/47 (LoVo, SW1417, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.64×** | +8.7 | 2e-16 | 38/47 (LoVo, SW1417, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~53% of this change | **1.65×** | +8.5 | 9e-16 | 41/46 (LoVo, HOP62, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.41×** | +8.5 | 9e-16 | 31/47 (SNU-1, HOP62, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.58×** | +8.0 | 6e-14 | 38/47 (BT-474, SNU-1, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.35×** | +7.4 | 3e-12 | 34/48 (HT-29, H4, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.46×** | +6.4 | 4e-09 | 35/46 (HT-29, H4, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.44×** | +6.3 | 5e-09 | 33/46 (H4, LS 180, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.39×** | +5.8 | 2e-07 | 34/47 (LS 180, HT-29, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.53×** | +5.3 | 2e-06 | 28/47 (KATO III, RKO, …) | all doses, flat | low cells (technical?); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +4.8 | 3e-05 | 22/47 (HS-578T, SW48, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.28×** | +4.2 | 5e-04 | 23/47 (MIA PaCa-2, SNU-423, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.56×** | +4.0 | 9e-04 | 26/48 (SW1417, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.05 µM |  | **1.27×** | +4.0 | 0.001 | 24/47 (RKO, MIA PaCa-2, …) | all doses, flat |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | **1.22×** | +3.4 | 0.010 | 16/47 (HOP62, KATO III, …) | rises with dose |  |
| [[vincristine (drug)]] 5 µM |  | **1.43×** | +3.3 | 0.015 | 22/45 (HT-29, KATO III, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4053.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.850× | -4.1 | 0.016 | 19/47 (NCI-H460, A-172, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.797×** | -4.0 | 0.016 | 22/47 (NCI-H23, KATO III, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.674×** | -3.7 | 0.047 | 20/48 (SK-MEL-2, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.822×** | -3.5 | 0.066 | 21/47 (KATO III, SW 1088, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 5 µM | ⚠ toxic | 0.704× | -3.2 | 0.13 | 19/44 (KATO III, Panc 03.27, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.48 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4053. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 39.2 | 15 (13 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.24× (z +26.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.99× (z +14.2) | — |
| [[LS 180 (line)]] | wt | 48.7 | 12 (11 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.74× (z +21.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.73× (z +15.5) | — |
| [[HOP62 (line)]] | alt | 82.6 | 11 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.28× (z +28.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.73× (z +13.6) | — |
| [[KATO III (line)]] | alt | 125 | 9 (8 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.19× (z +13.4) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.09× (z +8.5) | [[Ponatinib (drug)]] 0.5 µM 0.460× (z -9.0) |
| [[SNU-1 (line)]] | wt | 120 | 11 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +16.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.37× (z +14.4) | — |
| [[SW480 (line)]] | alt | 127 | 11 (10 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +16.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.21× (z +9.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 102 | 10 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +29.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 11.3× (z +21.2) | — |
| [[NCI-H460 (line)]] | wt | 146 | 10 (8 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.49× (z +14.2) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.55× (z +12.0) | — |
| [[HT-29 (line)]] | alt | 56.5 | 9 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.82× (z +24.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.24× (z +13.2) | — |
| [[SNU-423 (line)]] | alt | 137 | 9 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +19.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.25× (z +15.6) | — |
| [[SW1417 (line)]] | alt | 90.8 | 9 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +18.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.13× (z +12.7) | — |
| [[COLO 205 (line)]] | alt | 30.7 | 8 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 26.5× (z +27.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.88× (z +11.3) | — |
| [[hTERT-HPNE (line)]] | wt | 50.3 | 8 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.84× (z +19.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.07× (z +14.4) | — |
| [[A-172 (line)]] | wt | 92.1 | 7 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +22.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.21× (z +15.2) | — |
| [[A549 (line)]] | wt | 98.2 | 7 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.05× (z +26.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.79× (z +16.0) | — |
| [[BT-474 (line)]] | alt | 45.7 | 7 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.44× (z +15.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.53× (z +9.1) | — |
| [[NCI-H1792 (line)]] | alt | 45.1 | 7 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.25× (z +19.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.60× (z +12.3) | — |
| [[NCI-H23 (line)]] | alt | 103 | 4 (3 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +20.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.25× (z +11.3) | [[Adagrasib (drug)]] 0.05 µM 0.615× (z -16.8) ⚠ position not correctable · without an alert: [[Binimetinib (drug)]] 5 µM 0.449× (z -8.5) |
| [[A-427 (line)]] | wt | 43.3 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.94× (z +15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.73× (z +11.6) | — |
| [[AsPC-1 (line)]] | alt | 101 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.75× (z +31.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.75× (z +11.7) | — |
| [[PANC-1 (line)]] | alt | 94.6 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +18.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.56× (z +13.5) | — |
| [[RKO (line)]] | wt | 146 | 5 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.51× (z +30.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.48× (z +17.4) | [[Selinexor (drug)]] 0.5 µM 0.485× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 185 | 5 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.01× (z +12.0) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[HS-578T (line)]] | alt | 47.1 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +14.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +10.3) | — |
| [[J82 (line)]] | alt | 133 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +17.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +12.1) | — |
| [[NCI-H1573 (line)]] | alt | 25.0 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.72× (z +19.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 8.68× (z +13.5) | — |
| [[RPMI-7951 (line)]] | alt | 67.2 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.71× (z +19.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.66× (z +13.4) | — |
| [[SW 900 (line)]] | alt | 65.1 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.74× (z +21.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.06× (z +12.4) | — |
| [[A498 (line)]] | wt | 160 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +17.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.58× (z +11.7) | [[Selinexor (drug)]] 5 µM 0.551× (z -10.6) ⚠ cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 49.3 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 6.02× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +9.5) | — |
| [[CFPAC-1 (line)]] | alt | 64.6 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +18.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +9.0) | — |
| [[H4 (line)]] | wt | 101 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.91× (z +18.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.26× (z +11.8) | — |
| [[NCI-H2030 (line)]] | alt | 143 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +22.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.18× (z +14.8) | — |
| [[NCI-H2347 (line)]] | alt | 80.1 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +15.4) | — |
| [[LOX-IMVI (line)]] | wt | 120 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +20.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.67× (z +9.9) | — |
| [[Panc 03.27 (line)]] | alt | 127 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +18.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +11.2) | — |
| [[CHP-212 (line)]] | wt | 47.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.25× (z +8.6) | [[Docetaxel (drug)]] 0.05 µM 0.123× (z -8.8) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 156 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +17.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +9.2) | — |
| [[SK-MEL-2 (line)]] | alt | 108 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +10.5) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[SW48 (line)]] | wt | 40.6 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +9.8) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[HCT15 (line)]] | alt | 130 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.56× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | — |
| [[SHP-77 (line)]] | alt | 121 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +9.0) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[SW 1088 (line)]] | alt | 70.9 | 0 | 1 | — | [[Ponatinib (drug)]] 0.5 µM 0.0579× (z -8.9) |
| [[AN3 CA (line)]] | alt | 152 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.8 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 172 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 73.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 85.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 257 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4053), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TEAD1]] | +0.68 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[TPM4]] | +0.62 | +0.46 / +0.60 | both halves | 2e-05 |  |
| [[MYBL1]] | +0.60 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[DDAH1]] | +0.60 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[CALM2]] | +0.59 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[AXL]] | +0.59 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[CRIM1]] | +0.57 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[EPB41L2]] | +0.55 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[ANXA5]] | +0.53 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[DIAPH3]] | +0.53 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[CYTOR]] | +0.53 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[PGM5P2-1]] | +0.53 | +0.45 / +0.54 | both halves | 3e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NGDN]] | -0.52 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[ZNF581]] | -0.51 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[CCDC12]] | -0.51 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[MAPKAPK5-AS1]] | -0.50 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[METTL22]] | -0.50 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[SLC25A38]] | -0.49 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[MRPL44]] | -0.48 | -0.27 / -0.52 | both halves | 3e-04 |  |
| [[COX16]] | -0.48 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[TFIP11]] | -0.48 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[TMEM208]] | -0.47 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[ARMH3]] | -0.47 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[MRPL54]] | -0.47 | -0.32 / -0.48 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CTNNAL1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[AXL]] | B | AXL activity raises CTNNAL1's level | lines that do not express AXL (14) vs lines expressing it (36) | 1.51× lower at baseline in the lines without AXL | 0.055 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: LGALS1, ENSG00000289526, LTBP2 |
| [[MYBL1]] | B | MYBL1 activity raises CTNNAL1's level | lines that do not express MYBL1 (8) vs lines expressing it (42) | 1.46× lower at baseline in the lines without MYBL1 | 0.083 | ⚠ within organs, on part of the lines; also absent: NCS1, KCNC4, JAZF1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 120]] — RHOA GTPase cycle; 41 genes; every member is in the + arm (projection on the module's main direction 0.629). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (38.5, 13.6); signed map (-5.6, 35.2). **Vector** length 98.2, 32.0% of its response variance represented; |z| ≥ 3 in 1,755 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | +6.0 | +17.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | +5.9 | +13.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +5.1 | +6.4 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +5.0 | +6.0 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +5.0 | +7.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +4.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.5 | +7.4 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +3.2 | +6.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.2 | +5.8 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -6.1 | +0.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.9 | +3.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.4 | -1.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~47% of this change | -4.0 | +2.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.0 | +2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.6 | +1.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.0 | +0.1 |
|  | [[EX229 (drug)]] 5 µM |  | -2.6 | -1.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.5 | +0.9 |

## What is on record

|  |  |
|---|---|
| Name | catenin alpha like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q31.3 — chr9:108,942,569-109,013,522 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CLLP, alpha-CATU |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBT7](https://www.uniprot.org/uniprotkb/Q9UBT7) (Alpha-catulin):

> May modulate the Rho pathway signaling by providing a scaffold for the Lbc Rho guanine nucleotide exchange factor (ARHGEF1).

**Summary**, from NCBI Gene [8727](https://www.ncbi.nlm.nih.gov/gene/8727):

> Predicted to enable actin filament binding activity and cadherin binding activity. Acts upstream of or within Rho protein signal transduction. Located in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:2512](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2512) · Entrez [8727](https://www.ncbi.nlm.nih.gov/gene/8727) · UniProt [Q9UBT7](https://www.uniprot.org/uniprotkb/Q9UBT7) · Ensembl [ENSG00000119326](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119326)

## Data

Gene col 4053: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4053); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4053, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4053]; `tensor/DDL_lfc|DDL_z.npy` [4053]; `embed/gene_vectors.npy` [4053]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4053 or target_col == 4053). Every well: [[CTNNAL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CTNNAL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
