---
symbol: "NAMPT"
type: "gene"
col: 2673
ensembl_id: "ENSG00000105835"
name: "nicotinamide phosphoribosyltransferase"
location: "7q22.3"
module: 139
arm: "+"
pooled_cpm: 591.73
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 19
n_dd_up_clean: 16
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/139"]
generated_by: "tahoemap"
---

# NAMPT

*nicotinamide phosphoribosyltransferase* — 7q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.16× (z +9.5, q 8e-19, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.533× (z -9.6, q 4e-19, down in 37 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tofacitinib (drug)]] 5 µM: 0.671× (z -9.0, q 1e-16, down in 40 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NFIL3]] (+0.72, fdr 7e-06), [[BCL6]] (+0.67, fdr 7e-06), [[NAMPTP1]] (+0.66, fdr 1e-05); moves opposite to [[SH3D19]] (-0.43, fdr 4e-05), [[IQCK]] (-0.41, fdr 5e-05).
> It is in [[Module 139]], a single-armed module (Interleukin-4 and Interleukin-13 signaling).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TREM1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2673.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.16×** | +9.5 | 8e-19 | 47/49 (Hs 766T, C32, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.59×** | +7.4 | 4e-11 | 35/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.32×** | +6.2 | 1e-07 | 34/48 (HT-29, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.00×** | +5.8 | 1e-06 | 37/48 (SW48, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.42×** | +5.6 | 2e-06 | 36/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.28×** | +5.6 | 2e-06 | 26/48 (AsPC-1, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.41×** | +5.4 | 5e-06 | 34/49 (HT-29, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +5.0 | 4e-05 | 31/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +4.9 | 7e-05 | 27/47 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.37×** | +4.8 | 1e-04 | 38/49 (PANC-1, HCT15, …) | top dose only | plate-row cell shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.32×** | +4.5 | 4e-04 | 29/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.31×** | +4.3 | 7e-04 | 30/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.32×** | +4.2 | 9e-04 | 28/48 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.30×** | +4.2 | 0.001 | 27/48 (LoVo, HT-29, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM |  | **1.20×** | +4.2 | 0.001 | 23/48 (HT-29, LoVo, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.28×** | +3.9 | 0.004 | 24/48 (LoVo, LS 180, …) | two highest doses |  |
| [[Selinexor (drug)]] 0.05 µM |  | **1.24×** | +3.5 | 0.017 | 23/49 (HT-29, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tomivosertib (drug)]] 5 µM |  | **1.51×** | +3.4 | 0.020 | 23/48 (AsPC-1, Hs 766T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2673.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.533×** | -9.6 | 4e-19 | 37/44 (CFPAC-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Tofacitinib (drug)]] 5 µM |  | **0.671×** | -9.0 | 1e-16 | 40/49 (SHP-77, CFPAC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.619×** | -7.6 | 5e-12 | 30/49 (CFPAC-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.632×** | -7.3 | 5e-11 | 38/48 (NCI-H1792, HT-29, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.627×** | -7.1 | 1e-10 | 38/47 (NCI-H460, SW 900, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.756×** | -6.3 | 3e-08 | 34/49 (CFPAC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.681×** | -6.1 | 9e-08 | 39/48 (LoVo, J82, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.703×** | -5.6 | 2e-06 | 33/48 (NCI-H460, SW 900, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.909× | -5.5 | 3e-06 | 0/50 | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.551×** | -4.9 | 4e-05 | 29/47 (SW 900, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib (drug)]] 5 µM |  | **0.566×** | -4.7 | 1e-04 | 35/48 (NCI-H23, J82, …) | top dose only | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **0.745×** | -4.7 | 1e-04 | 34/48 (J82, LoVo, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.757×** | -4.4 | 4e-04 | 28/49 (NCI-H1792, SW 900, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.763×** | -4.3 | 7e-04 | 30/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.831×** | -4.2 | 0.001 | 21/48 (NCI-H23, NCI-H1573, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.778×** | -4.0 | 0.002 | 31/48 (NCI-H661, C32, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.783×** | -3.9 | 0.003 | 27/48 (NCI-H1792, J82, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.788×** | -3.8 | 0.005 | 29/49 (NCI-H1573, SNU-423, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.803×** | -3.5 | 0.015 | 27/48 (SW 900, NCI-H1792, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2673. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 1,583 | 8 (3 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 3.79× (z +16.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.211× (z -18.3) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.408× (z -11.0) |
| [[J82 (line)]] | alt | 698 | 1 | 7 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.91× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.319× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.443× (z -10.2) |
| [[LoVo (line)]] | wt | 221 | 7 (5 ⚠) | 1 | [[Bortezomib (drug)]] 0.05 µM 3.47× (z +15.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.74× (z +13.7) | [[Tofacitinib (drug)]] 5 µM 0.610× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 1,674 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.275× (z -21.8) ⚠ cell-cycle shift, explains ~5% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.331× (z -13.2) |
| [[NCI-H1573 (line)]] | alt | 981 | 2 (1 ⚠) | 5 (3 ⚠) | [[Digitoxin (drug)]] 5 µM 4.04× (z +13.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.56× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.232× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.363× (z -10.0) |
| [[PANC-1 (line)]] | alt | 208 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.40× (z +18.2) | — |
| [[SW 900 (line)]] | alt | 1,602 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.221× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.358× (z -11.6) |
| [[HT-29 (line)]] | alt | 450 | 4 (2 ⚠) | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.33× (z +12.8) | [[Ponatinib (drug)]] 5 µM 0.387× (z -10.1) |
| [[SNU-423 (line)]] | alt | 1,132 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -15.0) ⚠ cell-cycle shift, explains ~5% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.342× (z -9.2) |
| [[A-427 (line)]] | wt | 184 | 4 (3 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +9.5) ⚠ cell-cycle shift, explains ~14% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.28× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.417× (z -9.5) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 323 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +16.6) | — |
| [[A-172 (line)]] | wt | 203 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +14.6) | — |
| [[C32 (line)]] | wt | 1,320 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.371× (z -8.8) ⚠ toxic; transcription drop · without an alert: [[Tofacitinib (drug)]] 5 µM 0.522× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 1,313 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.164× (z -20.0) ⚠ toxic; transcription drop · without an alert: [[Tofacitinib (drug)]] 5 µM 0.520× (z -10.7) |
| [[Hs 766T (line)]] | wt | 888 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.11× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.379× (z -11.3) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 517 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.563× (z -9.5) |
| [[LS 180 (line)]] | wt | 207 | 3 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 2.18× (z +11.2) | — |
| [[NCI-H23 (line)]] | alt | 279 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.320× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Tofacitinib (drug)]] 5 µM 0.597× (z -9.5) |
| [[NCI-H2347 (line)]] | alt | 885 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.08× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.426× (z -9.4) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 403 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 2.13× (z +12.0) | — |
| [[SHP-77 (line)]] | alt | 333 | 0 | 3 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.443× (z -10.8) |
| [[SK-MEL-2 (line)]] | alt | 391 | 1 (1 ⚠) | 2 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.65× (z +9.1) ⚠ toxic | [[Dinaciclib (drug)]] 0.5 µM 0.406× (z -8.8) ⚠ toxic; transcription drop · without an alert: [[Tofacitinib (drug)]] 5 µM 0.536× (z -8.6) |
| [[BT-474 (line)]] | alt | 530 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.202× (z -15.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 644 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.342× (z -10.0) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 208 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.77× (z +15.7) | — |
| [[RPMI-7951 (line)]] | alt | 734 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.04× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.339× (z -9.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 1,244 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -14.7) ⚠ cell-cycle shift, explains ~5% of this change |
| [[A549 (line)]] | wt | 466 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.482× (z -10.0) ⚠ cell-cycle shift, explains ~5% of this change |
| [[C-33 A (line)]] | alt | 238 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -10.9) |
| [[CHP-212 (line)]] | wt | 579 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.228× (z -11.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 153 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +10.0) | — |
| [[HepG2_C3A (line)]] | wt | 203 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +9.3) ⚠ cell-cycle shift, explains ~5% of this change | — |
| [[RKO (line)]] | wt | 262 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +8.6) ⚠ cell-cycle shift, explains ~14% of this change | — |
| [[SW 1088 (line)]] | alt | 1,150 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -9.4) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 388 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +13.4) | — |
| [[SW48 (line)]] | wt | 283 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 8.64× (z +9.1) | — |
| [[AN3 CA (line)]] | alt | 420 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 263 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 254 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 364 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 603 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 472 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 509 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 328 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 705 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 660 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 298 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 380 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 424 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 177 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2673), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NFIL3]] | +0.72 | +0.72 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 475 |
| [[BCL6]] | +0.67 | +0.60 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[NAMPTP1]] | +0.66 | +0.54 / +0.71 | both halves | 1e-05 | **novel candidate** |
| [[SAA2-SAA4]] | +0.65 | +0.45 / +0.69 | both halves | 3e-05 |  |
| [[SAA2]] | +0.64 | +0.46 / +0.67 | both halves | 2e-05 |  |
| [[SAA4]] | +0.63 | +0.45 / +0.65 | both halves | 3e-05 |  |
| [[HIF1A]] | +0.62 | +0.52 / +0.67 | both halves | 1e-05 | pathway: HALLMARK_INFLAMMATORY_RESPONSE; STRING 554 |
| [[CCNL1]] | +0.59 | +0.47 / +0.65 | both halves | 2e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[SOD2]] | +0.57 | +0.53 / +0.65 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 613 |
| [[CEBPB]] | +0.57 | +0.51 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 408 |
| [[SAA1]] | +0.56 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[STAT3]] | +0.54 | +0.50 / +0.58 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 493 |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH3D19]] | -0.43 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[IQCK]] | -0.41 | -0.40 / -0.42 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TREM1]] | B | TREM1 activity raises NAMPT's level | lines that do not express TREM1 (25) vs lines expressing it (25) | 2.20× lower at baseline in the lines without TREM1 | 0.005 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, DTNA, MAF |
| [[PTGES]] | B | PTGES activity raises NAMPT's level | lines that do not express PTGES (17) vs lines expressing it (33) | 2.01× lower at baseline in the lines without PTGES | 0.012 | ⚠ within organs, on part of the lines; also absent: C1R, GPX3, CFAP300 |
| [[CP]] | B | CP activity raises NAMPT's level | lines that do not express CP (39) vs lines expressing it (11) | 2.29× lower at baseline in the lines without CP | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ITIH2, BHMT2, APOB |
| [[JAK2]] | B | JAK2 activity raises NAMPT's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 3.6% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[GLRX]] | B | GLRX activity raises NAMPT's level | lines that do not express GLRX (10) vs lines expressing it (40) | 1.83× lower at baseline in the lines without GLRX | 0.063 | ⚠ within organs, on part of the lines; also absent: DUSP10, FES, DGKG; maybe low, not absent |
| [[PID1]] | B | PID1 activity raises NAMPT's level | lines that do not express PID1 (22) vs lines expressing it (28) | 2.02× lower at baseline in the lines without PID1 | 0.063 | ⚠ within organs, on part of the lines; also absent: TRPA1, DOCK10, ENSG00000289600 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 139]] — Interleukin-4 and Interleukin-13 signaling; 34 genes; every member is in the + arm (projection on the module's main direction 0.745). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.9, 16.3); signed map (16.8, 28.3). **Vector** length 142, 54.4% of its response variance represented; |z| ≥ 3 in 1,836 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Interleukin-4 and Interleukin-13 signaling* (reactome, mean cos +0.54 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +10.3 | +6.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.8 | +5.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +5.9 | +2.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.7 | +1.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.5 | -0.2 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +4.2 | +2.4 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +4.1 | +1.3 |
|  | [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | +4.0 | +1.5 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -7.5 | -9.0 |
|  | [[NG25 (drug)]] 5 µM |  | -6.1 | -4.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.7 | -7.1 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -5.5 | -3.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.9 | +0.2 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -4.8 | -6.3 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -4.7 | -6.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.1 | -7.3 |

## What is on record

|  |  |
|---|---|
| Name | nicotinamide phosphoribosyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.3 — chr7:106,248,298-106,285,966 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PBEF; previously PBEF1 |
| Gene groups (HGNC) | Phosphoribosyltransferases |
| Hallmark sets | INFLAMMATORY_RESPONSE, INTERFERON_GAMMA_RESPONSE, TNFA_SIGNALING_VIA_NFKB, MTORC1_SIGNALING |
| Reactome | 9 pathways, smallest: NPAS4 regulates expression of target genes; BMAL1:CLOCK,NPAS2 activates circadian expression; Nicotinate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P43490](https://www.uniprot.org/uniprotkb/P43490) (Nicotinamide phosphoribosyltransferase):

> Catalyzes the condensation of nicotinamide with 5-phosphoribosyl-1-pyrophosphate to yield nicotinamide mononucleotide, an intermediate in the biosynthesis of NAD. It is the rate limiting component in the mammalian NAD biosynthesis pathway. The secreted form behaves both as a cytokine with immunomodulating properties and an adipokine with anti-diabetic properties, it has no enzymatic activity, partly because of lack of activation by ATP, which has a low level in extracellular space and plasma. …

**Summary**, from NCBI Gene [10135](https://www.ncbi.nlm.nih.gov/gene/10135):

> This gene encodes a protein that catalyzes the condensation of nicotinamide with 5-phosphoribosyl-1-pyrophosphate to yield nicotinamide mononucleotide, one step in the biosynthesis of nicotinamide adenine dinucleotide. The protein belongs to the nicotinic acid phosphoribosyltransferase (NAPRTase) family and is thought to be involved in many important biological processes, including metabolism, stress response and aging. This gene has a pseudogene on chromosome 10. [provided by RefSeq, Feb 2011]

**Accessions** — [HGNC:30092](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30092) · Entrez [10135](https://www.ncbi.nlm.nih.gov/gene/10135) · UniProt [P43490](https://www.uniprot.org/uniprotkb/P43490) · Ensembl [ENSG00000105835](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105835)

## Data

Gene col 2673: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2673); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2673, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2673]; `tensor/DDL_lfc|DDL_z.npy` [2673]; `embed/gene_vectors.npy` [2673]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2673 or target_col == 2673). Every well: [[NAMPT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NAMPT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
