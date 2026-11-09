---
symbol: "KIF20B"
type: "gene"
col: 6140
ensembl_id: "ENSG00000138182"
name: "kinesin family member 20B"
location: "10q23.31"
module: 22
arm: "+"
pooled_cpm: 132.45
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 11
n_dd_up_clean: 10
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# KIF20B

*kinesin family member 20B* — 10q23.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (20 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.08× (z +30.0, q 0e+00, up in 46 of 48 measured lines) ⚠ cell-cycle shift, explains ~49% of this change. The strongest without an alert is [[Docetaxel (drug)]] 5 µM: 1.18× (z +3.5, q 0.015, up in 20 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (9 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.625× (z -10.0, q 8e-21, down in 38 of 48 measured lines) ⚠ cell-cycle shift, explains ~99% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.690× (z -7.9, q 8e-13, down in 39 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 11 lines (HEC-1-A 0.491×, HOP62 0.425×, HCT15 0.352×, MIA PaCa-2 0.386×, …); [[Selinexor (drug)]] 5 µM in 5 lines (A498 0.238×, A-427 0.291×, LS 180 0.281×, A-172 0.352×, …; ⚠ cell-cycle shift, explains ~99% of this change); [[Selinexor (drug)]] 0.5 µM in 2 lines (H4 0.145×, A498 0.302×; ⚠ cell-cycle shift, would explain all of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 2 lines (A-427 0.428×, H4 0.369×); [[Amsacrine (drug)]] 5 µM in 1 line (A498 0.496×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDC80]] (+0.87, fdr 7e-06), [[SGO1]] (+0.85, fdr 7e-06), [[CENPE]] (+0.85, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[ANKRD20A4P]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 20 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6140.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **4.08×** | +30.0 | 0e+00 | 46/48 (PANC-1, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **3.49×** | +18.1 | 0e+00 | 47/48 (PANC-1, RKO, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.74×** | +15.2 | 0e+00 | 44/48 (RKO, HS-578T, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **2.36×** | +13.0 | 2e-36 | 47/48 (KATO III, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **2.32×** | +12.7 | 7e-35 | 47/48 (KATO III, LS 180, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.74×** | +8.3 | 7e-15 | 45/48 (KATO III, LoVo, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.70×** | +8.0 | 8e-14 | 36/48 (A-172, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.70×** | +8.0 | 9e-14 | 43/48 (KATO III, LoVo, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~90% of this change | **1.67×** | +7.7 | 8e-13 | 39/48 (HT-29, SW1417, …) | all doses, flat | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.59×** | +7.0 | 1e-10 | 41/48 (A549, NCI-H460, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **2.15×** | +6.0 | 8e-08 | 40/49 (HEC-1-A, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.47×** | +5.8 | 2e-07 | 30/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.46×** | +5.7 | 6e-07 | 35/48 (A549, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.43×** | +5.4 | 2e-06 | 35/48 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.27×** | +5.2 | 8e-06 | 35/48 (NCI-H23, HT-29, …) | top dose only |  |
| [[Docetaxel (drug)]] 5 µM |  | 1.18× | +3.5 | 0.015 | 20/48 (HT-29, PANC-1, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.55×** | +3.5 | 0.015 | 22/48 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.015 | 22/48 (HT-29, H4, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.25×** | +3.4 | 0.017 | 22/48 (HT-29, SW 900, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.53×** | +3.3 | 0.020 | 21/48 (PANC-1, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.27×** | +3.3 | 0.020 | 25/48 (HT-29, NCI-H460, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.24×** | +3.3 | 0.022 | 22/47 (HOP62, NCI-H23, …) | all doses, flat |  |
| [[HI-TOPK-032 (drug)]] 0.5 µM |  | **1.33×** | +3.1 | 0.041 | 16/49 (PANC-1, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.23×** | +3.0 | 0.049 | 19/47 (HOP62, H4, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.21×** | +2.9 | 0.068 | 21/48 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **1.20×** | +2.8 | 0.088 | 20/49 (HT-29, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 9 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6140.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 11 lines (HEC-1-A 0.491×, HOP62 0.425×, HCT15 0.352×, MIA PaCa-2 0.386×, …); [[Selinexor (drug)]] 5 µM in 5 lines (A498 0.238×, A-427 0.291×, LS 180 0.281×, A-172 0.352×, …; ⚠ cell-cycle shift, explains ~99% of this change); [[Selinexor (drug)]] 0.5 µM in 2 lines (H4 0.145×, A498 0.302×; ⚠ cell-cycle shift, would explain all of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 2 lines (A-427 0.428×, H4 0.369×); [[Amsacrine (drug)]] 5 µM in 1 line (A498 0.496×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | **0.625×** | -10.0 | 8e-21 | 38/48 (A498, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.690×** | -7.9 | 8e-13 | 39/49 (HEC-1-A, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.613×** | -7.4 | 3e-11 | 37/48 (H4, A498, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.706×** | -5.0 | 7e-05 | 28/44 (HEC-1-A, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | **0.751×** | -4.3 | 0.002 | 31/49 (A498, SNU-1, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.823×** | -4.1 | 0.003 | 26/48 (MIA PaCa-2, HCT15, …) | rises with dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~93% of this change | **0.681×** | -4.1 | 0.003 | 27/48 (KATO III, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.765×** | -4.0 | 0.004 | 28/48 (A498, H4, …) | rises with dose |  |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **0.693×** | -3.9 | 0.006 | 27/48 (MIA PaCa-2, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~98% of this change | **0.657×** | -3.3 | 0.054 | 21/45 (LS 180, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | **0.798×** | -3.2 | 0.069 | 20/48 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.90 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6140. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 219 | 8 (7 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +23.7) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 3.62× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -16.0) |
| [[LS 180 (line)]] | wt | 115 | 6 (6 ⚠) | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.84× (z +15.1) ⚠ cell-cycle shift, explains ~62% of this change | [[Selinexor (drug)]] 5 µM 0.281× (z -15.3) ⚠ cell-cycle shift, explains ~99% of this change |
| [[A498 (line)]] | wt | 123 | 3 (3 ⚠) | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +17.7) ⚠ cell-cycle shift, explains ~49% of this change | [[Selinexor (drug)]] 5 µM 0.238× (z -22.0) ⚠ cell-cycle shift, explains ~99% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.496× (z -10.8) |
| [[NCI-H460 (line)]] | wt | 122 | 8 (7 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.80× (z +22.1) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 2.79× (z +9.1) | [[Selinexor (drug)]] 5 µM 0.513× (z -8.5) ⚠ cell-cycle shift, explains ~99% of this change |
| [[HOP62 (line)]] | alt | 219 | 5 (5 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.24× (z +26.0) ⚠ cell-cycle shift, explains ~49% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.425× (z -12.3) |
| [[KATO III (line)]] | alt | 114 | 7 (7 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +16.8) ⚠ cell-cycle shift, explains ~49% of this change | [[Selinexor (drug)]] 5 µM 0.551× (z -8.6) ⚠ cell-cycle shift, explains ~99% of this change |
| [[A-172 (line)]] | wt | 145 | 4 (4 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.66× (z +23.6) ⚠ cell-cycle shift, explains ~49% of this change | [[Selinexor (drug)]] 5 µM 0.352× (z -14.2) ⚠ cell-cycle shift, explains ~99% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.520× (z -8.9) |
| [[H4 (line)]] | wt | 168 | 1 (1 ⚠) | 6 (4 ⚠) | [[Digitoxin (drug)]] 5 µM 3.64× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | [[Selinexor (drug)]] 0.5 µM 0.145× (z -13.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.369× (z -9.5) |
| [[HT-29 (line)]] | alt | 114 | 6 (5 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.97× (z +16.3) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Docetaxel (drug)]] 5 µM 2.04× (z +8.5) | [[Selinexor (drug)]] 5 µM 0.449× (z -9.5) ⚠ cell-cycle shift, explains ~99% of this change |
| [[LoVo (line)]] | wt | 103 | 7 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.33× (z +21.2) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[C32 (line)]] | wt | 107 | 5 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.92× (z +20.2) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 3.02× (z +8.8) | [[Selinexor (drug)]] 5 µM 0.418× (z -9.9) ⚠ cell-cycle shift, explains ~99% of this change |
| [[LOX-IMVI (line)]] | wt | 105 | 5 (5 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.73× (z +24.7) ⚠ cell-cycle shift, explains ~49% of this change | [[Selinexor (drug)]] 5 µM 0.463× (z -9.9) ⚠ cell-cycle shift, explains ~99% of this change |
| [[PANC-1 (line)]] | alt | 156 | 5 (5 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 6.34× (z +32.5) ⚠ cell-cycle shift, explains ~49% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.612× (z -8.6) |
| [[RKO (line)]] | wt | 144 | 6 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.91× (z +29.7) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[SW480 (line)]] | alt | 244 | 5 (5 ⚠) | 1 | [[Harringtonine (drug)]] 5 µM 3.26× (z +13.0) ⚠ cell-cycle shift, explains ~47% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -11.1) |
| [[A-427 (line)]] | wt | 173 | 2 (2 ⚠) | 3 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 3.05× (z +11.0) ⚠ cell-cycle shift, explains ~47% of this change | [[Selinexor (drug)]] 5 µM 0.291× (z -18.1) ⚠ cell-cycle shift, explains ~99% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.428× (z -12.4) |
| [[A549 (line)]] | wt | 134 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.10× (z +28.4) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 2.62× (z +8.8) | — |
| [[hTERT-HPNE (line)]] | wt | 71.6 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.92× (z +15.5) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[NCI-H1792 (line)]] | alt | 71.4 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.19× (z +20.9) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[NCI-H23 (line)]] | alt | 118 | 4 (4 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +18.9) ⚠ cell-cycle shift, explains ~49% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.455× (z -10.2) |
| [[NCI-H2347 (line)]] | alt | 141 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.39× (z +29.2) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[SW48 (line)]] | wt | 160 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.02× (z +19.5) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[Panc 03.27 (line)]] | alt | 159 | 3 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.57× (z +25.6) ⚠ cell-cycle shift, explains ~49% of this change | [[Selinexor (drug)]] 5 µM 0.451× (z -11.9) ⚠ cell-cycle shift, explains ~99% of this change |
| [[SW1417 (line)]] | alt | 157 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +23.2) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[CFPAC-1 (line)]] | alt | 117 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.77× (z +22.8) ⚠ cell-cycle shift, explains ~49% of this change | [[Selinexor (drug)]] 5 µM 0.513× (z -9.8) ⚠ cell-cycle shift, explains ~99% of this change |
| [[HCT15 (line)]] | alt | 251 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +10.1) ⚠ cell-cycle shift, explains ~49% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -12.1) |
| [[HS-578T (line)]] | alt | 68.9 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +27.3) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[J82 (line)]] | alt | 110 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.18× (z +25.5) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[NCI-H1573 (line)]] | alt | 64.7 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.43× (z +16.0) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[RPMI-7951 (line)]] | alt | 143 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +17.0) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[SW 900 (line)]] | alt | 68.0 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +14.6) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[AsPC-1 (line)]] | alt | 57.8 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.62× (z +17.5) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[C-33 A (line)]] | alt | 109 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +9.1) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[Hs 766T (line)]] | wt | 131 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.446× (z -9.4) ⚠ cell-cycle shift, explains ~99% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 162 | 1 (1 ⚠) | 1 | [[Harringtonine (drug)]] 5 µM 4.22× (z +12.1) ⚠ cell-cycle shift, explains ~47% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -11.8) |
| [[NCI-H2030 (line)]] | alt | 94.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.94× (z +25.3) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 117 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +15.0) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[SNU-423 (line)]] | alt | 134 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.85× (z +21.3) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[AN3 CA (line)]] | alt | 278 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.270× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 69.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +13.8) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[COLO 205 (line)]] | alt | 72.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +11.5) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[HepG2_C3A (line)]] | wt | 47.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +10.5) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[SHP-77 (line)]] | alt | 71.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +11.1) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[SNU-1 (line)]] | wt | 99.3 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 4.40× (z +9.0) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[SW 1271 (line)]] | alt | 167 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +9.8) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[CHP-212 (line)]] | wt | 102 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 73.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 85.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 102 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6140), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDC80]] | +0.87 | +0.86 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 594 |
| [[SGO1]] | +0.85 | +0.88 / +0.83 | both halves | 7e-06 | STRING 525 |
| [[CENPE]] | +0.85 | +0.87 / +0.82 | both halves | 7e-06 | same gene group; pathway: HALLMARK_G2M_CHECKPOINT; STRING 950 |
| [[CKAP2L]] | +0.85 | +0.82 / +0.84 | both halves | 7e-06 |  |
| [[SMC4]] | +0.84 | +0.89 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 674 |
| [[CKAP2]] | +0.84 | +0.79 / +0.84 | both halves | 7e-06 | STRING 669 |
| [[CENPF]] | +0.83 | +0.81 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 694 |
| [[KNL1]] | +0.82 | +0.82 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[CDCA8]] | +0.81 | +0.77 / +0.82 | both halves | 7e-06 | STRING 714 |
| [[CDK1]] | +0.81 | +0.79 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 538 |
| [[DBF4]] | +0.79 | +0.73 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 475 |
| [[GTSE1]] | +0.79 | +0.80 / +0.77 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANKRD20A4P]] | B | ANKRD20A4P activity raises KIF20B's level | lines that do not express ANKRD20A4P (24) vs lines expressing it (26) | 1.32× lower at baseline in the lines without ANKRD20A4P | 0.042 | ⚠ within organs, on part of the lines; also absent: ENSG00000253503, ENSG00000253500, ADGRF5 |
| [[RNF17]] | B | RNF17 activity lowers KIF20B's level | lines that do not express RNF17 (42) vs lines expressing it (8) | 1.52× higher at baseline in the lines without RNF17 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SSX1, LINC00879, APOD |
| [[PBK]] | C | PBK activity raises KIF20B's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.06× lower at baseline in the lines without PBK | 0.050 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises KIF20B's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.07× lower at baseline in the lines without AURKB | 0.076 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[CDCA3]] | C | CDCA3 activity raises KIF20B's level | lines that do not express CDCA3 (3) vs lines expressing it (47) | 2.09× lower at baseline in the lines without CDCA3 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TBC1D19, PBK, SNPH; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.804). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-38.5, -56.2); signed map (-49.6, -44.6). **Vector** length 148, 61.6% of its response variance represented; |z| ≥ 3 in 1,462 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DREAM G2/M down* (control, mean cos +0.71 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.63 to 48); *E2F targets* (hallmark, mean cos +0.60 to 46).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +6.6 | +5.2 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | +5.6 | +5.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +5.5 | +30.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +4.9 | +18.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +4.0 | +1.2 |
|  | [[Docetaxel (drug)]] 5 µM |  | +3.5 | +3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.5 | +0.8 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | +3.0 | +1.9 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +2.8 | +2.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.7 | -7.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | -8.7 | -10.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -7.6 | -1.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -7.5 | -7.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.9 | -1.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.8 | -4.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.5 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | -2.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.1 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | kinesin family member 20B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q23.31 — chr10:89,701,590-89,774,939 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MPP1, KRMP1, CT90; previously MPHOSPH1 |
| Gene groups (HGNC) | Kinesins |
| Hallmark sets | G2M_CHECKPOINT, MITOTIC_SPINDLE |
| Reactome | 8 pathways, smallest: Kinesins; COPI-dependent Golgi-to-ER retrograde traffic; Golgi-to-ER retrograde transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96Q89](https://www.uniprot.org/uniprotkb/Q96Q89) (Kinesin-like protein KIF20B):

> Plus-end-directed motor enzyme that is required for completion of cytokinesis. Required for proper midbody organization and abscission in polarized cortical stem cells. Plays a role in the regulation of neuronal polarization by mediating the transport of specific cargos. Participates in the mobilization of SHTN1 and in the accumulation of PIP3 in the growth cone of primary hippocampal neurons in a tubulin and actin-dependent manner. In the developing telencephalon, cooperates with SHTN1 to …

**Summary**, from NCBI Gene [9585](https://www.ncbi.nlm.nih.gov/gene/9585):

> Enables several functions, including ATP hydrolysis activity; WW domain binding activity; and plus-end-directed microtubule motor activity. Involved in positive regulation of cell population proliferation and positive regulation of cytokinesis. Located in several cellular components, including microtubule cytoskeleton; midbody; and nuclear lumen. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:7212](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7212) · Entrez [9585](https://www.ncbi.nlm.nih.gov/gene/9585) · UniProt [Q96Q89](https://www.uniprot.org/uniprotkb/Q96Q89) · Ensembl [ENSG00000138182](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138182)

## Data

Gene col 6140: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6140); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6140, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6140]; `tensor/DDL_lfc|DDL_z.npy` [6140]; `embed/gene_vectors.npy` [6140]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6140 or target_col == 6140). Every well: [[KIF20B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KIF20B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
