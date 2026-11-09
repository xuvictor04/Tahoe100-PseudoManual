---
symbol: "ZC3H11A"
type: "gene"
col: 665
ensembl_id: "ENSG00000058673"
name: "zinc finger CCCH-type containing 11A"
location: "1q32.1"
module: 168
arm: "-"
pooled_cpm: 307.63
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 19
n_dd_up_clean: 11
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/168"]
generated_by: "tahoemap"
---

# ZC3H11A

*zinc finger CCCH-type containing 11A* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.20× (z +21.9, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.463× (z -15.1, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARCN1]] (+0.73, fdr 7e-06), [[SKIL]] (+0.69, fdr 1e-05), [[LIG4]] (+0.69, fdr 2e-05); moves opposite to [[MFSD14CP]] (-0.76, fdr 7e-06), [[SEC11A]] (-0.71, fdr 1e-05), [[SDHAP2]] (-0.67, fdr 3e-05).
> It sits in the **-** arm of [[Module 168]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 665.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.20×** | +21.9 | 0e+00 | 48/48 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.44×** | +17.5 | 0e+00 | 48/48 (LoVo, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.16×** | +11.8 | 5e-30 | 47/49 (SK-MEL-2, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.82×** | +11.8 | 7e-30 | 47/48 (BT-474, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.84×** | +11.5 | 9e-29 | 47/48 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.79×** | +11.5 | 2e-28 | 46/48 (BT-474, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.76×** | +11.2 | 5e-27 | 47/48 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.75×** | +11.0 | 3e-26 | 46/48 (LoVo, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.45×** | +7.3 | 2e-11 | 38/48 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.97×** | +7.0 | 2e-10 | 45/48 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.33×** | +5.7 | 8e-07 | 36/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +5.4 | 4e-06 | 31/47 (NCI-H23, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.30×** | +5.2 | 7e-06 | 34/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.17× | +3.2 | 0.059 | 22/48 (A549, NCI-H460, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 665.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.463×** | -15.1 | 0e+00 | 48/48 (LOX-IMVI, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.468×** | -14.9 | 0e+00 | 48/48 (LOX-IMVI, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.474×** | -14.6 | 0e+00 | 48/48 (LOX-IMVI, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.606×** | -9.8 | 1e-20 | 46/48 (Panc 03.27, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.708×** | -9.6 | 1e-19 | 42/49 (A549, A498, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.652×** | -8.4 | 5e-15 | 45/48 (LOX-IMVI, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.664×** | -7.7 | 9e-13 | 37/44 (SNU-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.678×** | -7.6 | 2e-12 | 41/49 (SK-MEL-2, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.672×** | -7.5 | 4e-12 | 44/47 (RKO, HT-29, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.708×** | -6.5 | 4e-09 | 41/48 (H4, A498, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.750×** | -5.4 | 3e-06 | 29/50 (C32, SW 900, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.758×** | -5.0 | 3e-05 | 28/45 (NCI-H1792, A549, …) | all doses, stronger at high dose | composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.719×** | -4.6 | 2e-04 | 40/48 (CHP-212, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.662×** | -4.2 | 1e-03 | 40/49 (A549, HT-29, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.824×** | -3.8 | 0.006 | 28/48 (A-427, SNU-1, …) | two highest doses |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **0.775×** | -3.6 | 0.012 | 38/49 (SK-MEL-2, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.781×** | -3.4 | 0.018 | 31/48 (RPMI-7951, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | 0.853× | -3.1 | 0.053 | 13/48 (SW 1088, A549, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.895× | -3.1 | 0.060 | 4/48 (LOX-IMVI, NCI-H1792, …) | top dose only |  |
| [[Belinostat (drug)]] 0.05 µM |  | 0.856× | -3.0 | 0.062 | 18/48 (SK-MEL-2, SW1417, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.851× | -3.0 | 0.063 | 20/48 (NCI-H1573, LoVo, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 665. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 434 | 12 (1 ⚠) | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +24.1) | [[Panobinostat (drug)]] 5 µM 0.362× (z -14.7) |
| [[LOX-IMVI (line)]] | wt | 310 | 10 (1 ⚠) | 6 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +24.6) | [[Panobinostat (drug)]] 5 µM 0.358× (z -17.3) |
| [[SNU-1 (line)]] | wt | 313 | 10 (1 ⚠) | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +19.0) | [[Dinaciclib (drug)]] 5 µM 0.229× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.426× (z -10.8) |
| [[A549 (line)]] | wt | 306 | 7 | 8 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +30.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -20.4) |
| [[LoVo (line)]] | wt | 299 | 7 (2 ⚠) | 7 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.03× (z +19.4) | [[Belinostat (drug)]] 5 µM 0.396× (z -12.9) |
| [[A-172 (line)]] | wt | 355 | 9 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +26.9) | [[Panobinostat (drug)]] 5 µM 0.430× (z -13.1) |
| [[HT-29 (line)]] | alt | 315 | 6 (1 ⚠) | 7 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.51× (z +14.4) | [[Panobinostat (drug)]] 0.5 µM 0.379× (z -15.1) |
| [[NCI-H1792 (line)]] | alt | 325 | 6 | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +16.6) | [[Panobinostat (drug)]] 5 µM 0.353× (z -14.8) |
| [[A498 (line)]] | wt | 313 | 5 | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +30.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -16.9) |
| [[HOP62 (line)]] | alt | 294 | 8 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +15.8) | [[Panobinostat (drug)]] 5 µM 0.370× (z -14.6) |
| [[MIA PaCa-2 (line)]] | alt | 287 | 9 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +14.9) | [[Belinostat (drug)]] 5 µM 0.480× (z -11.5) |
| [[RKO (line)]] | wt | 279 | 8 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +20.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.333× (z -14.9) ⚠ toxic; cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.460× (z -10.9) |
| [[C32 (line)]] | wt | 421 | 6 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +22.2) | [[Dinaciclib (drug)]] 0.5 µM 0.433× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.479× (z -10.4) |
| [[J82 (line)]] | alt | 247 | 7 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +19.6) | [[Belinostat (drug)]] 5 µM 0.563× (z -9.6) |
| [[SW 900 (line)]] | alt | 483 | 5 | 6 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.51× (z +13.1) | [[Panobinostat (drug)]] 0.5 µM 0.383× (z -13.7) |
| [[SW480 (line)]] | alt | 249 | 8 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +15.3) | [[Belinostat (drug)]] 5 µM 0.481× (z -12.0) |
| [[AsPC-1 (line)]] | alt | 328 | 6 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +18.7) | [[Panobinostat (drug)]] 5 µM 0.400× (z -13.5) |
| [[HEC-1-A (line)]] | alt | 318 | 5 (1 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +16.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.554× (z -13.2) |
| [[HS-578T (line)]] | alt | 184 | 7 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +23.9) | [[Belinostat (drug)]] 5 µM 0.539× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 527 | 4 | 6 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.73× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.317× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.403× (z -11.1) |
| [[NCI-H23 (line)]] | alt | 222 | 6 (2 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +18.1) | [[Panobinostat (drug)]] 5 µM 0.485× (z -11.9) |
| [[NCI-H2347 (line)]] | alt | 401 | 7 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +21.5) | [[Panobinostat (drug)]] 0.5 µM 0.468× (z -12.5) |
| [[CFPAC-1 (line)]] | alt | 278 | 6 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +17.6) | [[Panobinostat (drug)]] 5 µM 0.476× (z -10.6) |
| [[hTERT-HPNE (line)]] | wt | 314 | 4 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +13.1) | [[Panobinostat (drug)]] 5 µM 0.376× (z -12.7) |
| [[NCI-H2030 (line)]] | alt | 287 | 5 | 4 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +21.2) | [[Belinostat (drug)]] 5 µM 0.347× (z -13.1) |
| [[PANC-1 (line)]] | alt | 312 | 6 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +27.7) | [[Panobinostat (drug)]] 5 µM 0.492× (z -11.8) |
| [[SK-MEL-2 (line)]] | alt | 243 | 4 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +23.6) | [[Dinaciclib (drug)]] 0.5 µM 0.446× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.499× (z -10.7) |
| [[BT-474 (line)]] | alt | 495 | 7 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.40× (z +17.8) | [[Panobinostat (drug)]] 0.5 µM 0.506× (z -9.8) |
| [[COLO 205 (line)]] | alt | 312 | 5 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +16.6) | [[Panobinostat (drug)]] 5 µM 0.391× (z -12.2) |
| [[RPMI-7951 (line)]] | alt | 304 | 5 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +15.3) | [[Panobinostat (drug)]] 5 µM 0.468× (z -10.5) |
| [[A-427 (line)]] | wt | 205 | 4 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +16.9) | [[Belinostat (drug)]] 5 µM 0.550× (z -9.0) |
| [[H4 (line)]] | wt | 317 | 1 | 6 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.16× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.342× (z -13.0) |
| [[KATO III (line)]] | alt | 225 | 4 | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.97× (z +14.4) | [[Panobinostat (drug)]] 0.5 µM 0.385× (z -12.6) |
| [[Panc 03.27 (line)]] | alt | 241 | 4 | 3 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +14.5) | [[Belinostat (drug)]] 5 µM 0.504× (z -10.3) |
| [[SW1417 (line)]] | alt | 202 | 4 | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.50× (z +14.6) | [[Belinostat (drug)]] 5 µM 0.516× (z -10.5) |
| [[SNU-423 (line)]] | alt | 239 | 3 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +22.5) | [[Panobinostat (drug)]] 5 µM 0.478× (z -11.0) |
| [[HepG2_C3A (line)]] | wt | 196 | 3 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +13.8) | [[Panobinostat (drug)]] 0.5 µM 0.393× (z -11.5) |
| [[Hs 766T (line)]] | wt | 291 | 3 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +18.4) | [[Panobinostat (drug)]] 5 µM 0.483× (z -10.5) |
| [[LS 180 (line)]] | wt | 302 | 3 (1 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.73× (z +11.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -10.9) |
| [[C-33 A (line)]] | alt | 221 | 3 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.29× (z +10.2) | [[Panobinostat (drug)]] 5 µM 0.478× (z -9.2) |
| [[CHP-212 (line)]] | wt | 477 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -10.4) |
| [[SW48 (line)]] | wt | 313 | 2 | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.19× (z +11.8) | [[Panobinostat (drug)]] 5 µM 0.411× (z -9.0) |
| [[HCT15 (line)]] | alt | 449 | 1 | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.67× (z +11.2) | [[Panobinostat (drug)]] 5 µM 0.426× (z -9.7) |
| [[AN3 CA (line)]] | alt | 208 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +10.7) | — |
| [[SHP-77 (line)]] | alt | 157 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.496× (z -8.5) |
| [[NCI-H2122 (line)]] | alt | 335 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 308 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 254 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 269 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 321 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 665), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARCN1]] | +0.73 | +0.65 / +0.74 | both halves | 7e-06 |  |
| [[SKIL]] | +0.69 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[LIG4]] | +0.69 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[VEZF1]] | +0.68 | +0.54 / +0.72 | both halves | 1e-05 |  |
| [[ZNF776]] | +0.67 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[ZNF24]] | +0.67 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[DDX6]] | +0.67 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[DCAF8]] | +0.67 | +0.43 / +0.63 | both halves | 3e-05 |  |
| [[ZFP91]] | +0.67 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[CPNE1]] | +0.66 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[UBQLN2]] | +0.66 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[NEK9]] | +0.66 | +0.44 / +0.57 | both halves | 3e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MFSD14CP]] | -0.76 | -0.65 / -0.77 | both halves | 7e-06 |  |
| [[SEC11A]] | -0.71 | -0.54 / -0.70 | both halves | 1e-05 |  |
| [[SDHAP2]] | -0.67 | -0.43 / -0.69 | both halves | 3e-05 |  |
| [[GFOD2]] | -0.66 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[CCT6P3-1]] | -0.66 | -0.53 / -0.69 | both halves | 1e-05 |  |
| [[SLC15A4]] | -0.65 | -0.50 / -0.67 | both halves | 1e-05 |  |
| [[TMEM120B]] | -0.65 | -0.43 / -0.63 | both halves | 3e-05 |  |
| [[SMG1P5]] | -0.65 | -0.43 / -0.69 | both halves | 3e-05 |  |
| [[SDHAP1]] | -0.63 | -0.40 / -0.62 | both halves | 5e-05 |  |
| [[CORO7]] | -0.63 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[SDHAP4-1]] | -0.63 | -0.46 / -0.63 | both halves | 3e-05 |  |
| [[MMS19]] | -0.63 | -0.47 / -0.54 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 168]]; 25 genes; this gene is in the **-** arm (projection on the module's main direction -0.698). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-10.5, -5.3); signed map (13.3, -28.2). **Vector** length 97.8, 42.9% of its response variance represented; |z| ≥ 3 in 1,562 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +9.4 | -7.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +8.2 | -7.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +8.0 | +7.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.9 | +11.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.8 | +21.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.0 | -0.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.8 | +3.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.3 | +2.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.8 | +0.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | -3.0 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -8.0 | -9.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.5 | -14.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | +1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.5 | -4.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.4 | +0.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | +1.0 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -2.5 | -3.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.4 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger CCCH-type containing 11A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:203,795,623-203,854,999 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0663; previously ZC3HDC11A |
| Gene groups (HGNC) | Zinc fingers CCCH-type; Transcription and export complex 1 subunits |
| Reactome | 5 pathways, smallest: Transport of Mature mRNA derived from an Intron-Containing Transcript; Transport of Mature Transcript to Cytoplasm; mRNA 3'-end processing |
| Matched by | ensembl_id |

**Function**, from UniProt [O75152](https://www.uniprot.org/uniprotkb/O75152) (Zinc finger CCCH domain-containing protein 11A):

> Through its association with TREX complex components, may participate in the export and post-transcriptional coordination of selected mRNA transcripts, including those required to maintain the metabolic processes in embryonic cells. Binds RNA.; (Microbial infection) Plays a role in efficient growth of several nuclear-replicating viruses such as HIV-1, influenza virus or herpes simplex virus 1/HHV-1. Required for efficient viral mRNA export. May be required for proper polyadenylation of …

**Summary**, from NCBI Gene [9877](https://www.ncbi.nlm.nih.gov/gene/9877):

> Enables RNA binding activity. Involved in poly(A)+ mRNA export from nucleus. Located in transcription export complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29093](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29093) · Entrez [9877](https://www.ncbi.nlm.nih.gov/gene/9877) · UniProt [O75152](https://www.uniprot.org/uniprotkb/O75152) · Ensembl [ENSG00000058673](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000058673)

## Data

Gene col 665: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 665); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 665, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 665]; `tensor/DDL_lfc|DDL_z.npy` [665]; `embed/gene_vectors.npy` [665]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 665 or target_col == 665). Every well: [[ZC3H11A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZC3H11A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
