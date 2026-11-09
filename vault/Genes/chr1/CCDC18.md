---
symbol: "CCDC18"
type: "gene"
col: 4342
ensembl_id: "ENSG00000122483"
name: "coiled-coil domain containing 18"
location: "1p22.1"
module: 22
arm: "+"
pooled_cpm: 73.72
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 9
n_dd_up_clean: 5
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# CCDC18

*coiled-coil domain containing 18* — 1p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.93× (z +20.5, q 0e+00, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.677× (z -12.1, q 4e-31, down in 39 of 48 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.655× (z -9.3, q 3e-18, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CIP2A]] (+0.72, fdr 7e-06), [[SCG5]] (+0.69, fdr 7e-06), [[GEN1]] (+0.68, fdr 7e-06); moves opposite to [[TP53TG1]] (-0.55, fdr 7e-05), [[ATP6V0E1]] (-0.52, fdr 4e-05), [[TRAPPC5]] (-0.50, fdr 5e-05).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Clofarabine (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4342.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.93×** | +20.5 | 0e+00 | 43/48 (NCI-H460, AsPC-1, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.83×** | +13.3 | 8e-38 | 41/48 (HEC-1-A, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.75×** | +11.9 | 3e-30 | 33/42 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.65×** | +10.2 | 2e-22 | 32/44 (HEC-1-A, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +10.1 | 7e-22 | 36/48 (C32, HS-578T, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +7.3 | 3e-11 | 30/48 (NCI-H1573, C32, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.25×** | +7.0 | 2e-10 | 25/48 (SK-MEL-2, LoVo, …) | rises with dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.39×** | +6.9 | 4e-10 | 30/48 (C32, SW480, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.32×** | +6.1 | 5e-08 | 26/48 (AsPC-1, C32, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.20×** | +5.6 | 9e-07 | 19/48 (Hs 766T, MIA PaCa-2, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | 1.19× | +5.3 | 5e-06 | 22/48 (NCI-H2347, MIA PaCa-2, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.22×** | +4.3 | 7e-04 | 20/48 (Hs 766T, A498, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~95% of this change | 1.19× | +3.8 | 0.007 | 21/48 (Hs 766T, A498, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~75% of this change | 1.17× | +3.4 | 0.027 | 16/48 (NCI-H460, SHP-77, …) | inconsistent across doses | low cells (technical?) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.16× | +3.2 | 0.061 | 16/48 (MIA PaCa-2, H4, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | 1.16× | +3.1 | 0.074 | 13/48 (MIA PaCa-2, HT-29, …) | rises with dose |  |
| [[Pralsetinib (drug)]] 0.05 µM |  | 1.16× | +3.0 | 0.085 | 3/48 (NCI-H460, H4, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 0.5 µM |  | 1.14× | +2.9 | 0.097 | 11/48 (PANC-1, NCI-H23, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4342.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.677×** | -12.1 | 4e-31 | 39/48 (LS 180, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.655×** | -9.3 | 3e-18 | 32/48 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.737×** | -6.7 | 3e-09 | 33/48 (H4, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.757×** | -6.1 | 1e-07 | 28/48 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.785×** | -5.3 | 1e-05 | 21/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.815×** | -4.5 | 6e-04 | 21/48 (C-33 A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.681×** | -4.4 | 8e-04 | 17/49 (A498, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.872× | -4.3 | 0.001 | 10/48 (NCI-H1792, NCI-H23, …) | all doses, stronger at high dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.765×** | -4.2 | 0.002 | 18/48 (SW480, A-427, …) | two highest doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 0.840× | -3.9 | 0.006 | 21/48 (HEC-1-A, J82, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 0.844× | -3.6 | 0.016 | 10/48 (NCI-H23, RPMI-7951, …) | top dose only | plate-row cell shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.846× | -3.6 | 0.017 | 17/47 (J82, PANC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~58% of this change | 0.855× | -3.5 | 0.022 | 19/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[palbociclib (drug)]] 5 µM |  | **0.741×** | -3.5 | 0.022 | 15/47 (RKO, A-427, …) | two highest doses | noisy plate (z scaled) |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.866× | -3.2 | 0.053 | 8/48 (CFPAC-1, COLO 205, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.895× | -3.0 | 0.084 | 14/48 (RKO, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4342. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 65.8 | 7 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.24× (z +15.3) | — |
| [[PANC-1 (line)]] | alt | 76.8 | 2 (1 ⚠) | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.55× (z +9.3) | [[Digitoxin (drug)]] 5 µM 0.353× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.363× (z -15.2) |
| [[AsPC-1 (line)]] | alt | 40.4 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.32× (z +18.4) | — |
| [[HS-578T (line)]] | alt | 96.9 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +11.8) | — |
| [[LoVo (line)]] | wt | 64.4 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.54× (z +15.3) | — |
| [[NCI-H1573 (line)]] | alt | 74.5 | 2 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.30× (z +12.7) | [[Digitoxin (drug)]] 5 µM 0.318× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.387× (z -10.1) |
| [[SW1417 (line)]] | alt | 45.9 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +13.1) | — |
| [[SW480 (line)]] | alt | 86.7 | 2 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +13.1) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.403× (z -12.7) |
| [[A-427 (line)]] | wt | 64.3 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.446× (z -11.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -10.4) |
| [[CFPAC-1 (line)]] | alt | 58.2 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +11.6) | — |
| [[HEC-1-A (line)]] | alt | 121 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.43× (z +15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[HOP62 (line)]] | alt | 103 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.435× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.458× (z -9.5) |
| [[J82 (line)]] | alt | 143 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.360× (z -13.1) |
| [[LOX-IMVI (line)]] | wt | 76.4 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +9.5) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.81× (z +8.5) | [[Selinexor (drug)]] 5 µM 0.494× (z -10.0) ⚠ cell-cycle shift, explains ~30% of this change |
| [[LS 180 (line)]] | wt | 51.6 | 2 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +8.5) | [[Selinexor (drug)]] 5 µM 0.269× (z -15.3) ⚠ cell-cycle shift, explains ~30% of this change |
| [[NCI-H2347 (line)]] | alt | 39.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +11.1) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +10.1) | — |
| [[NCI-H460 (line)]] | wt | 51.2 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +18.7) | [[Selinexor (drug)]] 5 µM 0.583× (z -9.1) ⚠ cell-cycle shift, explains ~30% of this change |
| [[Hs 766T (line)]] | wt | 83.1 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +11.1) | — |
| [[RKO (line)]] | wt | 125 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +10.1) | [[Selinexor (drug)]] 5 µM 0.460× (z -10.7) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SK-MEL-2 (line)]] | alt | 85.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +15.1) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.85× (z +8.5) | — |
| [[A-172 (line)]] | wt | 43.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.452× (z -9.7) ⚠ cell-cycle shift, explains ~30% of this change |
| [[A549 (line)]] | wt | 56.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.71× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[BT-474 (line)]] | alt | 38.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +9.8) | — |
| [[C-33 A (line)]] | alt | 80.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.318× (z -10.1) |
| [[HCT15 (line)]] | alt | 98.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +9.0) ⚠ cell-cycle shift, explains ~70% of this change | — |
| [[HepG2_C3A (line)]] | wt | 40.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.64× (z +11.0) | — |
| [[hTERT-HPNE (line)]] | wt | 69.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +10.8) | — |
| [[KATO III (line)]] | alt | 55.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +8.8) | — |
| [[NCI-H2030 (line)]] | alt | 57.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +11.0) ⚠ cell-cycle shift, explains ~70% of this change | — |
| [[NCI-H23 (line)]] | alt | 106 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +11.1) ⚠ cell-cycle shift, explains ~70% of this change | — |
| [[Panc 03.27 (line)]] | alt | 63.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +10.9) | — |
| [[RPMI-7951 (line)]] | alt | 99.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +10.2) | — |
| [[SHP-77 (line)]] | alt | 69.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.68× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[SNU-1 (line)]] | wt | 53.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.67× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[SNU-423 (line)]] | alt | 67.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +11.3) | — |
| [[SW 1271 (line)]] | alt | 90.7 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.109× (z -9.5) |
| [[A498 (line)]] | wt | 97.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 68.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 57.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 65.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 75.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 72.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 77.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 62.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 64.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4342), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CIP2A]] | +0.72 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[SCG5]] | +0.69 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[GEN1]] | +0.68 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[KIF14]] | +0.67 | +0.62 / +0.75 | both halves | 7e-06 |  |
| [[MYLK2]] | +0.65 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[SMC4]] | +0.65 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[TBC1D31]] | +0.64 | +0.58 / +0.67 | both halves | 8e-06 | same gene group |
| [[GTSE1]] | +0.64 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[ASPM]] | +0.63 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[MYH15]] | +0.63 | +0.65 / +0.58 | both halves | 8e-06 |  |
| [[PAK6]] | +0.61 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[DBF4B]] | +0.61 | +0.53 / +0.67 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TP53TG1]] | -0.55 | -0.37 / -0.52 | both halves | 7e-05 |  |
| [[ATP6V0E1]] | -0.52 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[TRAPPC5]] | -0.50 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[SNX2]] | -0.50 | -0.33 / -0.51 | both halves | 1e-04 |  |
| [[DOK4]] | -0.50 | -0.41 / -0.51 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CCDC18's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.2% of all compounds | 0.007 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SPDL1]] | C | SPDL1 activity raises CCDC18's level | lines that do not express SPDL1 (3) vs lines expressing it (47) | 1.70× lower at baseline in the lines without SPDL1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TBC1D19, PBK, SNPH; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Clofarabine (drug)]] 0.5 µM | C | CCDC18's natural level lowers the cells' numbers under Clofarabine 0.5 µM (makes them more sensitive) | CCDC18's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.68 | 0.287 over the table, 0.018 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.559). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-40.5, -56.0); signed map (-49.8, -46.8). **Vector** length 128, 38.5% of its response variance represented; |z| ≥ 3 in 1,180 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Processing of antigen in germinal center B cells* (reactome, mean cos +0.51 to 9); *MHC class II antigen presentation* (reactome, mean cos +0.51 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +10.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +4.4 | +6.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | +4.4 | +7.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +20.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.5 | +3.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.0 | +1.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | +2.7 | +3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +6.1 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +2.4 | +2.7 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -11.9 | -12.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -7.8 | -6.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.5 | +2.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.5 | -6.1 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~58% of this change | -4.5 | -3.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.9 | -3.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.7 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.6 | -2.9 |
|  | [[palbociclib (drug)]] 5 µM |  | -3.6 | -3.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -3.5 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 18 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p22.1 — chr1:93,179,919-93,278,730 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NY-SAR-41 |
| Gene groups (HGNC) | Centriolar satellite proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T9S5](https://www.uniprot.org/uniprotkb/Q5T9S5) (Coiled-coil domain-containing protein 18):

> May promote pre-adipocyte differentiation.

**Summary**, from NCBI Gene [343099](https://www.ncbi.nlm.nih.gov/gene/343099):

> Predicted to be involved in positive regulation of adipose tissue development. Located in centriolar satellite. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30370](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30370) · Entrez [343099](https://www.ncbi.nlm.nih.gov/gene/343099) · UniProt [Q5T9S5](https://www.uniprot.org/uniprotkb/Q5T9S5) · Ensembl [ENSG00000122483](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122483)

## Data

Gene col 4342: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4342); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4342, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4342]; `tensor/DDL_lfc|DDL_z.npy` [4342]; `embed/gene_vectors.npy` [4342]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4342 or target_col == 4342). Every well: [[CCDC18 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC18.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
