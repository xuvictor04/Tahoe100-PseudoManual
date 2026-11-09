---
symbol: "CAPN2"
type: "gene"
col: 8596
ensembl_id: "ENSG00000162909"
name: "calpain 2"
location: "1q41"
module: 110
arm: "+"
pooled_cpm: 230.07
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 20
n_dd_up_clean: 14
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/110"]
generated_by: "tahoemap"
---

# CAPN2

*calpain 2* — 1q41

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.27× (z +19.9, q 0e+00, up in 45 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Vinblastine (sulfate) (drug)]] 5 µM: 1.34× (z +10.1, q 8e-22, up in 32 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.500× (z -16.8, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PXN]] (+0.70, fdr 7e-06), [[CORO2B]] (+0.68, fdr 7e-06), [[MACF1]] (+0.68, fdr 7e-06); moves opposite to [[DPM3]] (-0.58, fdr 4e-05), [[RHOXF1]] (-0.57, fdr 1e-05), [[CNNM2]] (-0.56, fdr 1e-05).
> It is in [[Module 110]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[C6orf141]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8596.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.27×** | +19.9 | 0e+00 | 45/49 (NCI-H1792, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.07×** | +17.0 | 0e+00 | 39/44 (SNU-423, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.70×** | +11.8 | 6e-30 | 35/45 (SNU-423, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.56×** | +10.7 | 1e-24 | 40/48 (HT-29, COLO 205, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.34×** | +10.1 | 8e-22 | 32/49 (HT-29, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.47×** | +9.4 | 6e-19 | 35/48 (HT-29, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.48×** | +9.2 | 4e-18 | 35/47 (HT-29, COLO 205, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.44×** | +8.9 | 5e-17 | 38/47 (HT-29, COLO 205, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.36×** | +7.5 | 5e-12 | 26/47 (HT-29, COLO 205, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.44×** | +6.3 | 2e-08 | 30/48 (HT-29, C32, …) | all doses, flat | low cells (technical?); noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.29×** | +6.2 | 3e-08 | 25/47 (NCI-H460, SW48, …) | two highest doses | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.28×** | +6.1 | 6e-08 | 27/48 (HT-29, NCI-H1792, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +6.0 | 9e-08 | 26/48 (KATO III, COLO 205, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.27×** | +5.5 | 1e-06 | 27/48 (SHP-77, SW480, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.25×** | +5.3 | 5e-06 | 27/47 (NCI-H460, COLO 205, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.24×** | +5.2 | 9e-06 | 24/48 (A498, A-427, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +4.6 | 1e-04 | 23/48 (KATO III, LS 180, …) | two highest doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.12× | +4.0 | 0.002 | 15/48 (NCI-H460, SW 900, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.17× | +3.7 | 0.005 | 15/48 (SW480, PANC-1, …) | top dose only |  |
| [[vincristine (drug)]] 0.05 µM |  | **1.21×** | +3.6 | 0.007 | 17/48 (SK-MEL-2, COLO 205, …) | all doses, flat | noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **1.47×** | +3.4 | 0.016 | 17/46 (HT-29, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8596.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.500×** | -16.8 | 0e+00 | 44/48 (HEC-1-A, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.542×** | -14.8 | 0e+00 | 40/48 (RKO, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.632×** | -11.1 | 3e-26 | 39/48 (HEC-1-A, RKO, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.755×** | -9.6 | 1e-19 | 29/48 (NCI-H460, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.789×** | -8.1 | 8e-14 | 26/49 (RKO, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.795×** | -6.6 | 5e-09 | 27/48 (LoVo, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.755×** | -6.5 | 5e-09 | 24/48 (LoVo, AsPC-1, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.831×** | -6.3 | 2e-08 | 25/48 (J82, RKO, …) | rises with dose | low cells (technical?) |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.818×** | -6.2 | 3e-08 | 27/49 (SW480, LoVo, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.808×** | -6.2 | 4e-08 | 25/48 (LoVo, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.782×** | -5.9 | 2e-07 | 24/48 (LoVo, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.778×** | -5.6 | 1e-06 | 25/48 (LoVo, SW480, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **0.784×** | -5.6 | 1e-06 | 25/50 (LoVo, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.795×** | -5.3 | 4e-06 | 28/47 (AsPC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.849× | -5.2 | 9e-06 | 22/48 (LoVo, SW480, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.771×** | -4.9 | 3e-05 | 24/48 (AsPC-1, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.808×** | -4.9 | 3e-05 | 23/49 (LoVo, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8596. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 167 | 4 (2 ⚠) | 16 (2 ⚠) | [[Daptomycin (drug)]] 5 µM 2.08× (z +10.4) ⚠ unreliable plate only · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 1.54× (z +8.7) | [[Digitoxin (drug)]] 5 µM 0.404× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Trametinib (drug)]] 0.5 µM 0.507× (z -12.1) |
| [[HEC-1-A (line)]] | alt | 351 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -20.1) |
| [[SW480 (line)]] | alt | 169 | 3 (1 ⚠) | 9 | [[Vinblastine (sulfate) (drug)]] 5 µM 1.73× (z +9.6) | [[Binimetinib (drug)]] 0.5 µM 0.479× (z -11.3) |
| [[HT-29 (line)]] | alt | 134 | 11 (6 ⚠) | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 2.70× (z +15.8) | — |
| [[NCI-H460 (line)]] | wt | 213 | 7 (3 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.02× (z +10.2) ⚠ toxic; transcription drop · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 1.54× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -24.7) |
| [[AsPC-1 (line)]] | alt | 477 | 0 | 10 | — | [[Panobinostat (drug)]] 5 µM 0.361× (z -14.6) |
| [[CFPAC-1 (line)]] | alt | 369 | 5 (3 ⚠) | 5 | [[Vinblastine (sulfate) (drug)]] 5 µM 1.80× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.517× (z -12.1) |
| [[COLO 205 (line)]] | alt | 137 | 10 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.14× (z +16.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Peretinoin (drug)]] 5 µM 4.17× (z +12.8) | — |
| [[J82 (line)]] | alt | 270 | 0 | 9 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.346× (z -16.4) |
| [[KATO III (line)]] | alt | 102 | 8 (4 ⚠) | 1 | [[Ixazomib citrate (drug)]] 5 µM 4.00× (z +16.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.63× (z +15.2) | [[Panobinostat (drug)]] 5 µM 0.460× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 232 | 6 (3 ⚠) | 3 | [[Vinblastine (sulfate) (drug)]] 5 µM 2.22× (z +13.3) | [[Homoharringtonine (drug)]] 5 µM 0.449× (z -13.3) |
| [[RKO (line)]] | wt | 430 | 0 | 9 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.239× (z -20.6) |
| [[C32 (line)]] | wt | 133 | 7 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.48× (z +10.9) ⚠ toxic; transcription drop · without an alert: [[Peretinoin (drug)]] 5 µM 2.48× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.556× (z -9.9) |
| [[MIA PaCa-2 (line)]] | alt | 373 | 2 (2 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.29× (z +10.2) ⚠ toxic; transcription drop | [[Adagrasib (drug)]] 0.05 µM 0.632× (z -19.8) ⚠ position not correctable · without an alert: [[Panobinostat (drug)]] 5 µM 0.408× (z -11.4) |
| [[SNU-423 (line)]] | alt | 142 | 8 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.82× (z +18.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.11× (z +12.7) | — |
| [[A549 (line)]] | wt | 250 | 3 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 2.73× (z +14.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.341× (z -16.3) |
| [[HOP62 (line)]] | alt | 412 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.429× (z -14.0) |
| [[NCI-H2347 (line)]] | alt | 515 | 3 (3 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.50× (z +15.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -19.2) |
| [[SK-MEL-2 (line)]] | alt | 104 | 6 (3 ⚠) | 1 | [[Vinblastine (sulfate) (drug)]] 5 µM 1.87× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -15.4) |
| [[LS 180 (line)]] | wt | 128 | 5 (2 ⚠) | 1 | [[Daptomycin (drug)]] 5 µM 2.41× (z +9.6) ⚠ unreliable plate only · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 1.83× (z +9.3) | [[Panobinostat (drug)]] 5 µM 0.278× (z -13.8) |
| [[PANC-1 (line)]] | alt | 163 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +13.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.360× (z -13.1) |
| [[A-172 (line)]] | wt | 436 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.04× (z +11.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.458× (z -13.5) |
| [[C-33 A (line)]] | alt | 81.3 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 4.29× (z +13.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.355× (z -9.9) |
| [[NCI-H1792 (line)]] | alt | 187 | 4 (4 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.64× (z +19.7) ⚠ toxic; transcription drop | [[Adagrasib (drug)]] 0.05 µM 0.652× (z -16.3) ⚠ position not correctable |
| [[H4 (line)]] | wt | 190 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.280× (z -11.8) |
| [[Hs 766T (line)]] | wt | 376 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.29× (z +9.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.413× (z -10.2) |
| [[NCI-H2030 (line)]] | alt | 106 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.05× (z +13.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.591× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 318 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.425× (z -10.5) |
| [[RPMI-7951 (line)]] | alt | 223 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +12.9) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.607× (z -8.9) |
| [[A-427 (line)]] | wt | 79.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.27× (z +13.6) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 249 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.96× (z +17.7) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 127 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.337× (z -10.5) |
| [[HS-578T (line)]] | alt | 231 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.07× (z +10.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.526× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 200 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +12.5) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 83.8 | 3 (2 ⚠) | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 1.99× (z +9.9) | — |
| [[SW 900 (line)]] | alt | 305 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +14.3) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 95.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.27× (z +11.3) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 233 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.42× (z +12.4) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 77.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.42× (z +9.0) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 164 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.51× (z +9.3) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 117 | 1 (1 ⚠) | 0 | [[Daptomycin (drug)]] 5 µM 2.70× (z +8.8) ⚠ unreliable plate only | — |
| [[SNU-1 (line)]] | wt | 93.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.84× (z +12.7) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 102 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 310 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 187 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 237 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 125 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8596), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PXN]] | +0.70 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[CORO2B]] | +0.68 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[MACF1]] | +0.68 | +0.61 / +0.70 | both halves | 7e-06 | same gene group |
| [[TOMM34]] | +0.68 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[DCBLD2]] | +0.67 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[BMAL2]] | +0.65 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[LAMC1]] | +0.65 | +0.60 / +0.74 | both halves | 7e-06 | pathway: Degradation of the extracellular matrix |
| [[ITGA2]] | +0.65 | +0.70 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_COAGULATION |
| [[LAMC2]] | +0.65 | +0.68 / +0.62 | both halves | 7e-06 | pathway: Degradation of the extracellular matrix |
| [[S100A16]] | +0.65 | +0.74 / +0.62 | both halves | 7e-06 | same gene group |
| [[CD44]] | +0.65 | +0.65 / +0.64 | both halves | 7e-06 | pathway: Degradation of the extracellular matrix |
| [[RALB]] | +0.65 | +0.70 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPM3]] | -0.58 | -0.42 / -0.62 | both halves | 4e-05 |  |
| [[RHOXF1]] | -0.57 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[CNNM2]] | -0.56 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[COX14]] | -0.55 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[SAP30]] | -0.54 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[CEBPD]] | -0.54 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[PHF21A]] | -0.54 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[TNRC6B]] | -0.52 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[FMC1]] | -0.52 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[PDK4]] | -0.52 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[SAT2]] | -0.51 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[LCORL]] | -0.51 | -0.46 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C6orf141]] | B | C6orf141 activity raises CAPN2's level | lines that do not express C6orf141 (21) vs lines expressing it (29) | 1.44× lower at baseline in the lines without C6orf141 | 0.014 | ⚠ within organs, on part of the lines; also absent: ADAM8, ENSG00000251584, SAMD12-AS1 |
| [[MICAL2]] | B | MICAL2 activity raises CAPN2's level | lines that do not express MICAL2 (11) vs lines expressing it (39) | 1.88× lower at baseline in the lines without MICAL2 | 0.028 | ⚠ within organs, on part of the lines; also absent: UBA7, ENSG00000285906, SERPINB1 |
| [[ETS1]] | B | ETS1 activity raises CAPN2's level | lines that do not express ETS1 (11) vs lines expressing it (39) | 1.88× lower at baseline in the lines without ETS1 | 0.042 | ⚠ within organs, on part of the lines; also absent: AXL, ENSG00000289526, PRSS23 |
| [[PNMA2]] | B | PNMA2 activity raises CAPN2's level | lines that do not express PNMA2 (16) vs lines expressing it (34) | 1.60× lower at baseline in the lines without PNMA2 | 0.055 | ⚠ within organs, on part of the lines; also absent: MCOLN3, CACNG6, SELENOM |
| [[MGLL]] | B | MGLL activity raises CAPN2's level | lines that do not express MGLL (14) vs lines expressing it (36) | 1.73× lower at baseline in the lines without MGLL | 0.055 | ⚠ within organs, on part of the lines; also absent: CXCL3, MET, PSORS1C1; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises CAPN2's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.4% of all compounds | 0.067 | ⚠ off-target possible; 3 compounds |
| [[S100A16]] | B | S100A16 activity raises CAPN2's level | lines that do not express S100A16 (9) vs lines expressing it (41) | 1.87× lower at baseline in the lines without S100A16 | 0.068 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, MET, TGFBR2 |
| [[COTL1]] | B | COTL1 activity raises CAPN2's level | lines that do not express COTL1 (5) vs lines expressing it (45) | 1.91× lower at baseline in the lines without COTL1 | 0.089 | ⚠ within organs, on part of the lines; also absent: TIMP1, HOXA-AS2, ELK3; maybe low, not absent |
| [[CDCP1]] | B | CDCP1 activity raises CAPN2's level | lines that do not express CDCP1 (16) vs lines expressing it (34) | 1.51× lower at baseline in the lines without CDCP1 | 0.091 | ⚠ within organs, on part of the lines; also absent: PTK6, TNK1, CHMP4C |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 110]]; 43 genes; every member is in the + arm (projection on the module's main direction 0.615). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (40.0, 7.2); signed map (6.6, 43.7). **Vector** length 146, 54.9% of its response variance represented; |z| ≥ 3 in 1,913 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +9.9 | +10.7 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +9.4 | +8.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +8.8 | +9.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +8.7 | +10.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +7.8 | +9.4 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +6.2 | +7.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.7 | +5.2 |
| fall | [[Trametinib (drug)]] 0.5 µM |  | -6.3 | -6.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.0 | -5.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -5.5 | -6.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -5.3 | -4.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.3 | -3.7 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -5.0 | -6.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.9 | -6.5 |

## What is on record

|  |  |
|---|---|
| Name | calpain 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q41 — chr1:223,701,593-223,776,018 (+) |
| Ensembl biotype | protein_coding |
| Also known as | mCANP, CANPml, CANPL2 |
| Gene groups (HGNC) | EF-hand domain containing; Calpains |
| Hallmark sets | COAGULATION |
| Reactome | 11 pathways, smallest: Deregulated CDK5 triggers multiple neurodegenerative pathways in Alzheimer's disease models; Neurodegenerative Diseases; Defective Intrinsic Pathway for Apoptosis |
| Matched by | ensembl_id |

**Function**, from UniProt [P17655](https://www.uniprot.org/uniprotkb/P17655) (Calpain-2 catalytic subunit):

> Calcium-regulated non-lysosomal thiol-protease which catalyzes limited proteolysis of substrates involved in cytoskeletal remodeling and signal transduction. Proteolytically cleaves MYOC at 'Arg-226'. Proteolytically cleaves CPEB3 following neuronal stimulation which abolishes CPEB3 translational repressor activity, leading to translation of CPEB3 target mRNAs (By similarity).

**Summary**, from NCBI Gene [824](https://www.ncbi.nlm.nih.gov/gene/824):

> The calpains, calcium-activated neutral proteases, are nonlysosomal, intracellular cysteine proteases. The mammalian calpains include ubiquitous, stomach-specific, and muscle-specific proteins. The ubiquitous enzymes consist of heterodimers with distinct large, catalytic subunits associated with a common small, regulatory subunit. This gene encodes the large subunit of the ubiquitous enzyme, calpain 2. Multiple heterogeneous transcriptional start sites in the 5' UTR have been reported. Two …

**Accessions** — [HGNC:1479](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1479) · Entrez [824](https://www.ncbi.nlm.nih.gov/gene/824) · UniProt [P17655](https://www.uniprot.org/uniprotkb/P17655) · Ensembl [ENSG00000162909](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162909)

## Data

Gene col 8596: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8596); `tables/drug_effects.parquet` (70 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8596, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8596]; `tensor/DDL_lfc|DDL_z.npy` [8596]; `embed/gene_vectors.npy` [8596]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8596 or target_col == 8596). Every well: [[CAPN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CAPN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
