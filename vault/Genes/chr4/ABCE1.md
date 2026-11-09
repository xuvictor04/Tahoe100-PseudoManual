---
symbol: "ABCE1"
type: "gene"
col: 8886
ensembl_id: "ENSG00000164163"
name: "ATP binding cassette subfamily E member 1"
location: "4q31.21"
module: 1
arm: "+"
pooled_cpm: 70.6
n_lines_expressing: 50
n_dd_up: 40
n_dd_down: 19
n_dd_up_clean: 24
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# ABCE1

*ATP binding cassette subfamily E member 1* — 4q31.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 40 drug-doses (16 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.85× (z +20.8, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.633× (z -9.1, q 6e-17, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UTP20]] (+0.84, fdr 7e-06), [[TCERG1]] (+0.79, fdr 7e-06), [[PPIL1]] (+0.79, fdr 7e-06); moves opposite to [[MXD1]] (-0.72, fdr 7e-06), [[LMBR1L]] (-0.71, fdr 7e-06), [[ULK1]] (-0.70, fdr 7e-06).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[NDRG1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 18 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 40 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8886.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.85×** | +20.8 | 0e+00 | 47/48 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **2.06×** | +20.3 | 0e+00 | 43/48 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.61×** | +19.1 | 0e+00 | 44/49 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.63×** | +18.5 | 0e+00 | 42/44 (NCI-H1792, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.28×** | +16.4 | 0e+00 | 43/48 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.17×** | +15.4 | 0e+00 | 42/48 (NCI-H1573, HOP62, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.07×** | +14.5 | 1e-45 | 44/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.07×** | +13.4 | 5e-39 | 40/45 (NCI-H1792, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.87×** | +12.5 | 6e-34 | 45/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.97×** | +11.3 | 7e-28 | 43/49 (LoVo, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.72×** | +10.8 | 1e-25 | 42/48 (NCI-H1792, HT-29, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.74×** | +10.6 | 9e-25 | 35/48 (NCI-H1573, NCI-H1792, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.74×** | +10.6 | 2e-24 | 38/47 (NCI-H1573, NCI-H1792, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.54×** | +8.6 | 3e-16 | 36/48 (A-172, MIA PaCa-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.49×** | +8.0 | 5e-14 | 34/48 (NCI-H1792, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.48×** | +7.9 | 1e-13 | 39/48 (A-172, NCI-H460, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.10×** | +7.7 | 3e-13 | 29/48 (HEC-1-A, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.73×** | +5.7 | 3e-07 | 34/48 (NCI-H2347, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.30×** | +5.3 | 3e-06 | 29/48 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.29×** | +5.1 | 1e-05 | 24/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.62×** | +5.0 | 1e-05 | 31/48 (KATO III, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.30×** | +5.0 | 2e-05 | 29/48 (NCI-H1792, LoVo, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.59×** | +4.8 | 3e-05 | 29/48 (CFPAC-1, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.26×** | +4.4 | 2e-04 | 21/47 (NCI-H460, HOP62, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8886.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.633×** | -9.1 | 6e-17 | 31/48 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.642×** | -8.8 | 4e-16 | 34/48 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.785×** | -6.8 | 2e-09 | 27/48 (RKO, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.751×** | -5.7 | 2e-06 | 28/48 (SW480, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.831×** | -4.5 | 9e-04 | 21/48 (SW480, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.829×** | -4.4 | 1e-03 | 21/48 (SW480, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.809×** | -4.3 | 0.002 | 24/50 (LoVo, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.801×** | -4.2 | 0.002 | 23/47 (NCI-H2030, LoVo, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.810×** | -4.2 | 0.002 | 23/48 (LoVo, KATO III, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.671×** | -4.1 | 0.002 | 22/49 (LoVo, NCI-H2030, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.806×** | -4.1 | 0.002 | 22/47 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.807×** | -4.1 | 0.002 | 19/48 (LoVo, SW480, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.810×** | -4.1 | 0.002 | 26/49 (LoVo, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.818×** | -4.0 | 0.003 | 21/47 (C32, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | 0.864× | -4.0 | 0.003 | 17/48 (LoVo, SW480, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.862× | -4.0 | 0.003 | 16/48 (SW480, MIA PaCa-2, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.694×** | -3.8 | 0.005 | 18/50 (LoVo, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8886. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 60.7 | 12 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +13.2) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.86× (z +12.8) | — |
| [[SW480 (line)]] | alt | 113 | 9 (6 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.83× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.53× (z +11.9) | [[Panobinostat (drug)]] 0.5 µM 0.360× (z -13.2) |
| [[NCI-H1792 (line)]] | alt | 70.5 | 11 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 7.86× (z +20.5) | — |
| [[NCI-H460 (line)]] | wt | 65.8 | 10 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.10× (z +13.7) | — |
| [[A498 (line)]] | wt | 87.0 | 5 (4 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.26× (z +10.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.570× (z -10.4) |
| [[KATO III (line)]] | alt | 83.9 | 7 (4 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.70× (z +14.2) | [[Panobinostat (drug)]] 0.5 µM 0.365× (z -11.0) |
| [[NCI-H1573 (line)]] | alt | 59.7 | 9 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.87× (z +19.6) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 10.7× (z +18.6) | — |
| [[PANC-1 (line)]] | alt | 87.3 | 6 (3 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.60× (z +13.1) | [[Panobinostat (drug)]] 0.5 µM 0.440× (z -11.3) |
| [[HOP62 (line)]] | alt | 55.3 | 8 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +17.1) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.02× (z +15.0) | — |
| [[HT-29 (line)]] | alt | 54.8 | 8 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +15.4) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.29× (z +12.5) | — |
| [[LoVo (line)]] | wt | 82.3 | 6 (2 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +10.7) | [[Trametinib (drug)]] 5 µM 0.423× (z -10.1) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.548× (z -9.2) |
| [[SW 900 (line)]] | alt | 31.7 | 8 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.67× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.88× (z +11.0) | — |
| [[A-172 (line)]] | wt | 48.7 | 7 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.20× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.08× (z +11.3) | — |
| [[NCI-H2347 (line)]] | alt | 56.0 | 7 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +13.3) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.70× (z +12.2) | — |
| [[RPMI-7951 (line)]] | alt | 64.1 | 7 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.34× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.09× (z +9.5) | — |
| [[CFPAC-1 (line)]] | alt | 29.9 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.34× (z +15.8) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.40× (z +14.1) | — |
| [[HS-578T (line)]] | alt | 51.5 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.43× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.49× (z +11.6) | — |
| [[RKO (line)]] | wt | 163 | 1 | 5 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.13× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -21.5) |
| [[COLO 205 (line)]] | alt | 31.0 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.39× (z +14.2) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 7.72× (z +11.1) | — |
| [[HEC-1-A (line)]] | alt | 92.9 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +11.3) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 4.51× (z +9.7) | — |
| [[Panc 03.27 (line)]] | alt | 50.1 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.60× (z +11.0) | — |
| [[A549 (line)]] | wt | 58.2 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.15× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.58× (z +8.8) | — |
| [[Hs 766T (line)]] | wt | 50.1 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.94× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.57× (z +9.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 65.9 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.11× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | [[Panobinostat (drug)]] 5 µM 0.334× (z -10.8) |
| [[SK-MEL-2 (line)]] | alt | 78.2 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +11.1) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.51× (z +9.0) | — |
| [[SNU-1 (line)]] | wt | 130 | 2 | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.91× (z +10.6) | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0726× (z -13.6) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.466× (z -10.6) |
| [[SNU-423 (line)]] | alt | 35.5 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.85× (z +15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SW48 (line)]] | wt | 133 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -14.2) |
| [[AsPC-1 (line)]] | alt | 40.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +14.0) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.98× (z +10.0) | — |
| [[H4 (line)]] | wt | 64.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.95× (z +11.2) | — |
| [[HepG2_C3A (line)]] | wt | 73.4 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +10.8) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.04× (z +10.1) | — |
| [[LS 180 (line)]] | wt | 47.6 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +11.0) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.84× (z +10.5) | — |
| [[NCI-H2030 (line)]] | alt | 43.9 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +15.2) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H23 (line)]] | alt | 62.0 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.38× (z +11.2) | — |
| [[BT-474 (line)]] | alt | 74.9 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.13× (z +10.2) | — |
| [[C32 (line)]] | wt | 43.7 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.97× (z +9.0) | [[Cobimetinib (drug)]] 0.5 µM 0.350× (z -8.7) |
| [[HCT15 (line)]] | alt | 90.8 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.25× (z +9.0) | — |
| [[C-33 A (line)]] | alt | 147 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.380× (z -9.6) |
| [[hTERT-HPNE (line)]] | wt | 51.4 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.28× (z +8.6) | — |
| [[SHP-77 (line)]] | alt | 57.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.42× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SW1417 (line)]] | alt | 61.9 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.48× (z +10.4) | — |
| [[A-427 (line)]] | wt | 119 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 83.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 108 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 77.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 95.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 66.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 59.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8886), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UTP20]] | +0.84 | +0.82 / +0.84 | both halves | 7e-06 | STRING 427 |
| [[TCERG1]] | +0.79 | +0.71 / +0.79 | both halves | 7e-06 |  |
| [[PPIL1]] | +0.79 | +0.80 / +0.76 | both halves | 7e-06 |  |
| [[GNL3L]] | +0.78 | +0.73 / +0.79 | both halves | 7e-06 |  |
| [[ANAPC7]] | +0.77 | +0.78 / +0.73 | both halves | 7e-06 |  |
| [[NAA15]] | +0.77 | +0.74 / +0.83 | both halves | 7e-06 | STRING 602 |
| [[DNAJC11]] | +0.77 | +0.78 / +0.73 | both halves | 7e-06 |  |
| [[ZNF507]] | +0.76 | +0.72 / +0.73 | both halves | 7e-06 |  |
| [[ATIC]] | +0.76 | +0.72 / +0.85 | both halves | 7e-06 |  |
| [[COA7]] | +0.76 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[GPATCH4]] | +0.76 | +0.78 / +0.71 | both halves | 7e-06 |  |
| [[MAK16]] | +0.75 | +0.72 / +0.80 | both halves | 7e-06 | STRING 586 |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MXD1]] | -0.72 | -0.66 / -0.67 | both halves | 7e-06 |  |
| [[LMBR1L]] | -0.71 | -0.66 / -0.68 | both halves | 7e-06 |  |
| [[ULK1]] | -0.70 | -0.66 / -0.68 | both halves | 7e-06 |  |
| [[CBFA2T2]] | -0.68 | -0.66 / -0.65 | both halves | 7e-06 |  |
| [[VPS37D]] | -0.68 | -0.58 / -0.68 | both halves | 8e-06 |  |
| [[CARD19]] | -0.67 | -0.55 / -0.67 | both halves | 1e-05 |  |
| [[PLEKHH3]] | -0.66 | -0.61 / -0.61 | both halves | 7e-06 |  |
| [[ANG]] | -0.65 | -0.59 / -0.65 | both halves | 7e-06 |  |
| [[APAF1]] | -0.65 | -0.62 / -0.61 | both halves | 7e-06 |  |
| [[AHDC1]] | -0.65 | -0.64 / -0.58 | both halves | 7e-06 |  |
| [[ANKRD37]] | -0.65 | -0.59 / -0.62 | both halves | 7e-06 |  |
| [[KMT5C]] | -0.65 | -0.62 / -0.60 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 5, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NDRG1]] | B | NDRG1 activity lowers ABCE1's level | lines that do not express NDRG1 (6) vs lines expressing it (44) | 1.64× higher at baseline in the lines without NDRG1 | 0.016 | ⚠ within organs, on part of the lines; also absent: SMOX, DELEC1, SLC2A1 |
| [[MAP2K1]] | B | MAP2K1 activity raises ABCE1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[ME3]] | B | ME3 activity lowers ABCE1's level | lines that do not express ME3 (13) vs lines expressing it (37) | 1.23× higher at baseline in the lines without ME3 | 0.075 | ⚠ within organs, on part of the lines; also absent: PLAAT3 |
| [[NR3C2]] | B | NR3C2 activity lowers ABCE1's level | lines that do not express NR3C2 (15) vs lines expressing it (35) | 1.32× higher at baseline in the lines without NR3C2 | 0.084 | ⚠ within organs, on part of the lines; also absent: ENSG00000249631, ENSG00000287292, SATB1; maybe low, not absent |
| [[SLC17A7]] | B | SLC17A7 activity raises ABCE1's level | lines that do not express SLC17A7 (9) vs lines expressing it (41) | 1.36× lower at baseline in the lines without SLC17A7 | 0.084 | ⚠ within organs, on part of the lines; also absent: GXYLT2, ITGA10, NT5M; maybe low, not absent |
| [[TSEN2]] | C | TSEN2 activity raises ABCE1's level | lines that do not express TSEN2 (3) vs lines expressing it (47) | 2.02× lower at baseline in the lines without TSEN2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TMEM9B-AS1, NDC80, CSPG5; maybe low, not absent; its own permutation p |
| [[HSF2BP]] | C | HSF2BP activity raises ABCE1's level | lines that do not express HSF2BP (4) vs lines expressing it (46) | 1.32× lower at baseline in the lines without HSF2BP | 0.084 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; co-occurs with CTNNB1; also absent: TPST1, CPLANE1, SOAT1; maybe low, not absent |
| [[SLC35F2]] | C | SLC35F2 activity raises ABCE1's level | lines that do not express SLC35F2 (3) vs lines expressing it (47) | 1.67× lower at baseline in the lines without SLC35F2 | 0.086 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: BOK, TMEM132A, POLR3G; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.830). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-18.2, -36.2); signed map (1.5, -42.6). **Vector** length 117, 43.3% of its response variance represented; |z| ≥ 3 in 1,682 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA processing* (reactome, mean cos +0.51 to 28); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.52 to 24); *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.53 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +8.6 | +18.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | +7.9 | +19.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.3 | +16.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +7.1 | +13.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.6 | +10.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.8 | +2.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.0 | +5.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.0 | +5.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.7 | +4.1 |
|  | [[EX229 (drug)]] 5 µM |  | +3.4 | +4.8 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -5.1 | -8.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.9 | -9.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.6 | -5.7 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -2.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -3.2 | -0.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.9 | -1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.8 | -2.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.7 | -3.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.6 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | ATP binding cassette subfamily E member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q31.21 — chr4:145,098,288-145,129,524 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RLI, OABP, RLI1; previously RNASEL1, RNASELI, RNS4I |
| Gene groups (HGNC) | ATP binding cassette subfamily E |
| Hallmark sets | ALLOGRAFT_REJECTION, MYC_TARGETS_V1 |
| Reactome | 8 pathways, smallest: OAS antiviral response; Interferon alpha/beta signaling; PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [P61221](https://www.uniprot.org/uniprotkb/P61221) (ATP-binding cassette sub-family E member 1):

> Nucleoside-triphosphatase (NTPase) involved in ribosome recycling by mediating ribosome disassembly. Able to hydrolyze ATP, GTP, UTP and CTP. Splits ribosomes into free 60S subunits and tRNA- and mRNA-bound 40S subunits. Acts either after canonical termination facilitated by release factors (ETF1/eRF1) or after recognition of stalled and vacant ribosomes by mRNA surveillance factors (PELO/Pelota). Involved in the No-Go Decay (NGD) pathway: recruited to stalled ribosomes by the Pelota-HBS1L …

**Summary**, from NCBI Gene [6059](https://www.ncbi.nlm.nih.gov/gene/6059):

> The protein encoded by this gene is a member of the superfamily of ATP-binding cassette (ABC) transporters. ABC proteins transport various molecules across extra- and intra-cellular membranes. ABC genes are divided into seven distinct subfamilies (ABC1, MDR/TAP, MRP, ALD, OABP, GCN20, White). This protein is a member of the OABP subfamily. Alternatively referred to as the RNase L inhibitor, this protein functions to block the activity of ribonuclease L. Activation of ribonuclease L leads to …

**Accessions** — [HGNC:69](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:69) · Entrez [6059](https://www.ncbi.nlm.nih.gov/gene/6059) · UniProt [P61221](https://www.uniprot.org/uniprotkb/P61221) · Ensembl [ENSG00000164163](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164163)

## Data

Gene col 8886: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8886); `tables/drug_effects.parquet` (73 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8886, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8886]; `tensor/DDL_lfc|DDL_z.npy` [8886]; `embed/gene_vectors.npy` [8886]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8886 or target_col == 8886). Every well: [[ABCE1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABCE1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
