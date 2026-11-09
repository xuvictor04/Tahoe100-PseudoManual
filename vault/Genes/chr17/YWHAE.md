---
symbol: "YWHAE"
type: "gene"
col: 3012
ensembl_id: "ENSG00000108953"
name: "tyrosine 3-monooxygenase/tryptophan 5-monooxygenase activation protein epsilon"
location: "17p13.3"
module: 3
arm: "-"
pooled_cpm: 371.6
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 7
n_dd_up_clean: 4
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# YWHAE

*tyrosine 3-monooxygenase/tryptophan 5-monooxygenase activation protein epsilon* — 17p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (15 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.35× (z +18.8, q 0e+00, up in 48 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 4.55× (z +17.5, q 0e+00, up in 49 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.682× (z -8.5, q 9e-15, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HNRNPK]] (+0.82, fdr 7e-06), [[SRSF3]] (+0.78, fdr 7e-06), [[HNRNPM]] (+0.72, fdr 7e-06); moves opposite to [[MPG]] (-0.71, fdr 4e-05), [[COMMD6]] (-0.70, fdr 7e-06), [[CIAO2B]] (-0.69, fdr 1e-05).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 18 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3012.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.35×** | +18.8 | 0e+00 | 48/49 (A549, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **4.55×** | +17.5 | 0e+00 | 49/49 (NCI-H1573, LoVo, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.18×** | +16.5 | 0e+00 | 43/44 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.59×** | +14.5 | 1e-45 | 43/48 (A549, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.01×** | +14.2 | 1e-43 | 45/45 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.89×** | +14.0 | 2e-42 | 47/48 (KATO III, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.41×** | +10.2 | 2e-22 | 46/48 (C32, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.56×** | +9.8 | 6e-21 | 45/48 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.48×** | +8.6 | 5e-16 | 43/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.48×** | +8.4 | 3e-15 | 42/48 (A498, A549, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.43×** | +7.9 | 2e-13 | 37/48 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **1.42×** | +7.3 | 1e-11 | 38/47 (COLO 205, C32, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.36×** | +6.8 | 5e-10 | 36/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.35×** | +6.5 | 2e-09 | 35/48 (A549, NCI-H1573, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +6.0 | 9e-08 | 0/50 | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.24×** | +4.7 | 6e-05 | 27/48 (HT-29, SW480, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.22×** | +4.3 | 5e-04 | 27/48 (HT-29, SW 900, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.20× | +3.9 | 0.002 | 22/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | 1.15× | +2.9 | 0.092 | 12/48 (A549, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3012.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.682×** | -8.5 | 9e-15 | 37/48 (LoVo, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.686×** | -8.4 | 1e-14 | 40/48 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.694×** | -8.1 | 9e-14 | 39/48 (LoVo, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.739×** | -6.7 | 2e-09 | 36/48 (SK-MEL-2, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | **0.822×** | -6.2 | 8e-08 | 27/49 (HCT15, SW480, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.682×** | -4.5 | 8e-04 | 36/49 (LoVo, Panc 03.27, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.824×** | -4.3 | 0.001 | 25/48 (NCI-H23, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 0.844× | -3.8 | 0.011 | 21/48 (NCI-H2347, MIA PaCa-2, …) | two highest doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.849× | -3.5 | 0.028 | 20/47 (RKO, LoVo, …) | rises with dose |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.856× | -3.5 | 0.028 | 10/49 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.857× | -3.5 | 0.028 | 19/48 (LOX-IMVI, RKO, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.903× | -3.3 | 0.052 | 4/48 (NCI-H23, A549, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~47% of this change | 0.866× | -3.1 | 0.085 | 21/47 (NCI-H23, HEC-1-A, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3012. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 378 | 16 (14 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +19.9) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.75× (z +13.2) | — |
| [[NCI-H1573 (line)]] | alt | 200 | 13 (12 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +17.3) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 8.62× (z +17.3) | [[Panobinostat (drug)]] 5 µM 0.564× (z -8.8) |
| [[PANC-1 (line)]] | alt | 356 | 12 (11 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.25× (z +21.2) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 4.48× (z +14.6) | [[Belinostat (drug)]] 5 µM 0.592× (z -9.9) |
| [[LoVo (line)]] | wt | 300 | 10 (9 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +18.7) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.90× (z +16.8) | [[Panobinostat (drug)]] 5 µM 0.483× (z -14.7) |
| [[NCI-H1792 (line)]] | alt | 246 | 13 (12 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +18.0) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.93× (z +10.8) | — |
| [[SW 900 (line)]] | alt | 447 | 13 (11 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +15.5) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.10× (z +13.7) | — |
| [[LOX-IMVI (line)]] | wt | 422 | 9 (7 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.28× (z +14.6) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 4.69× (z +14.3) | [[Panobinostat (drug)]] 5 µM 0.533× (z -11.1) |
| [[C32 (line)]] | wt | 254 | 10 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +16.7) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 7.88× (z +14.5) | — |
| [[SW480 (line)]] | alt | 584 | 9 (7 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.62× (z +16.3) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 5.43× (z +15.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.625× (z -11.4) ⚠ cell-cycle shift, explains ~7% of this change |
| [[A-172 (line)]] | wt | 420 | 9 (8 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +17.4) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 2.95× (z +9.9) | — |
| [[hTERT-HPNE (line)]] | wt | 330 | 9 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +15.1) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 5.14× (z +12.6) | — |
| [[SNU-423 (line)]] | alt | 325 | 9 (8 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +16.6) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.98× (z +10.3) | — |
| [[A549 (line)]] | wt | 487 | 8 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +21.0) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 4.55× (z +13.1) | — |
| [[COLO 205 (line)]] | alt | 296 | 8 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +16.4) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 8.75× (z +16.3) | — |
| [[HOP62 (line)]] | alt | 328 | 8 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +15.9) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 6.19× (z +14.1) | — |
| [[HS-578T (line)]] | alt | 352 | 8 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +16.2) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 5.22× (z +12.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 482 | 4 (3 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +20.6) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 5.14× (z +14.2) | [[Panobinostat (drug)]] 0.5 µM 0.549× (z -9.9) |
| [[NCI-H23 (line)]] | alt | 495 | 5 (4 ⚠) | 3 | [[TAK-901 (drug)]] 5 µM 3.60× (z +13.2) | [[Belinostat (drug)]] 5 µM 0.589× (z -10.5) |
| [[Panc 03.27 (line)]] | alt | 272 | 5 (3 ⚠) | 3 | [[TAK-901 (drug)]] 5 µM 5.15× (z +13.9) | [[Belinostat (drug)]] 5 µM 0.531× (z -10.3) |
| [[SK-MEL-2 (line)]] | alt | 189 | 4 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +14.4) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.53× (z +9.7) | [[Belinostat (drug)]] 5 µM 0.479× (z -10.8) |
| [[SW48 (line)]] | wt | 392 | 7 (4 ⚠) | 1 | [[PH-797804 (drug)]] 5 µM 7.21× (z +14.1) | [[Belinostat (drug)]] 5 µM 0.533× (z -8.6) |
| [[A498 (line)]] | wt | 451 | 7 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +19.2) ⚠ cell-cycle shift, explains ~63% of this change | — |
| [[AsPC-1 (line)]] | alt | 286 | 7 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.78× (z +15.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.17× (z +13.0) | — |
| [[Hs 766T (line)]] | wt | 271 | 7 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.92× (z +15.4) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 5.57× (z +12.9) | — |
| [[KATO III (line)]] | alt | 494 | 7 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.09× (z +19.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.09× (z +10.3) | — |
| [[LS 180 (line)]] | wt | 329 | 7 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.53× (z +12.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.45× (z +10.4) | — |
| [[RPMI-7951 (line)]] | alt | 336 | 7 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +14.8) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.65× (z +13.6) | — |
| [[HT-29 (line)]] | alt | 263 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.17× (z +17.6) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 5.03× (z +12.9) | — |
| [[J82 (line)]] | alt | 437 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.41× (z +15.2) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.79× (z +12.1) | — |
| [[BT-474 (line)]] | alt | 312 | 5 (3 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.04× (z +13.7) | — |
| [[CFPAC-1 (line)]] | alt | 263 | 3 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +11.6) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.84× (z +10.8) | [[Panobinostat (drug)]] 0.5 µM 0.501× (z -10.6) |
| [[H4 (line)]] | wt | 468 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.39× (z +12.3) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.39× (z +9.0) | — |
| [[HCT15 (line)]] | alt | 466 | 4 (3 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.48× (z +12.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.570× (z -12.6) ⚠ cell-cycle shift, explains ~7% of this change |
| [[HEC-1-A (line)]] | alt | 429 | 5 (3 ⚠) | 0 | [[PH-797804 (drug)]] 5 µM 4.39× (z +12.7) | — |
| [[SNU-1 (line)]] | wt | 363 | 5 (3 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 9.66× (z +16.5) | — |
| [[A-427 (line)]] | wt | 270 | 3 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.50× (z +15.3) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 2.99× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.592× (z -8.8) ⚠ cell-cycle shift, explains ~7% of this change |
| [[HepG2_C3A (line)]] | wt | 275 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.96× (z +10.3) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.49× (z +10.0) | — |
| [[NCI-H2030 (line)]] | alt | 410 | 4 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.17× (z +11.3) | — |
| [[SW1417 (line)]] | alt | 298 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.97× (z +11.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.48× (z +10.7) | — |
| [[RKO (line)]] | wt | 463 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.27× (z +13.6) | — |
| [[SHP-77 (line)]] | alt | 521 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.45× (z +15.2) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 340 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.34× (z +12.8) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 4.19× (z +11.2) | — |
| [[CHP-212 (line)]] | wt | 367 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.77× (z +9.3) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 301 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 3.55× (z +11.2) | [[Panobinostat (drug)]] 0.5 µM 0.607× (z -8.6) |
| [[SW 1271 (line)]] | alt | 406 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.90× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[AN3 CA (line)]] | alt | 448 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.24× (z +9.3) ⚠ toxic; transcription drop | — |
| [[NCI-H2122 (line)]] | alt | 343 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 372 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 570 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 361 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3012), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPK]] | +0.82 | +0.72 / +0.83 | both halves | 7e-06 | STRING 403 |
| [[SRSF3]] | +0.78 | +0.75 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[HNRNPM]] | +0.72 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[DDX3X]] | +0.71 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[EWSR1]] | +0.70 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[CPNE1]] | +0.70 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[HNRNPA2B1]] | +0.69 | +0.62 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[HNRNPL]] | +0.69 | +0.59 / +0.68 | both halves | 7e-06 | STRING 507 |
| [[HUWE1]] | +0.69 | +0.54 / +0.73 | both halves | 1e-05 |  |
| [[EIF4G2]] | +0.69 | +0.72 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 404 |
| [[SFPQ]] | +0.68 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[TASOR]] | +0.68 | +0.65 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*54 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPG]] | -0.71 | -0.42 / -0.74 | both halves | 4e-05 |  |
| [[COMMD6]] | -0.70 | -0.59 / -0.69 | both halves | 7e-06 |  |
| [[CIAO2B]] | -0.69 | -0.53 / -0.67 | both halves | 1e-05 |  |
| [[CAMLG]] | -0.68 | -0.60 / -0.66 | both halves | 7e-06 |  |
| [[ATP5MK]] | -0.68 | -0.56 / -0.64 | both halves | 1e-05 | pathway: Organelle biogenesis and maintenance |
| [[MIR4458HG]] | -0.67 | -0.59 / -0.70 | both halves | 7e-06 |  |
| [[TULP3]] | -0.67 | -0.60 / -0.66 | both halves | 7e-06 |  |
| [[ATP5MJ]] | -0.66 | -0.54 / -0.67 | both halves | 1e-05 | pathway: Organelle biogenesis and maintenance |
| [[SLC37A3]] | -0.66 | -0.57 / -0.63 | both halves | 1e-05 |  |
| [[LAMTOR5]] | -0.66 | -0.57 / -0.69 | both halves | 1e-05 | pathway: TP53 Regulates Metabolic Genes |
| [[SDHAP2]] | -0.66 | -0.57 / -0.62 | both halves | 9e-06 |  |
| [[ATOX1]] | -0.65 | -0.55 / -0.64 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises YWHAE's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.799). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-37.4, -24.1); signed map (15.1, -38.4). **Vector** length 99.3, 42.2% of its response variance represented; |z| ≥ 3 in 1,422 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *mRNA 3'-end processing* (reactome, mean cos +0.65 to 12); *mRNA Polyadenylation* (reactome, mean cos +0.66 to 11); *mRNA Splicing - Major Pathway* (reactome, mean cos +0.65 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.2 | +14.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.1 | +16.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | +7.1 | +14.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.0 | +18.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +5.3 | +7.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | -0.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.4 | +1.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.8 | +10.2 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | +3.0 | +0.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.9 | +1.1 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~47% of this change | -5.4 | -3.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.7 | +3.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.6 | -4.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.2 | -0.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.7 | -8.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.5 | +0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.3 | +4.3 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -2.8 | -0.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.5 | -0.8 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -2.4 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | tyrosine 3-monooxygenase/tryptophan 5-monooxygenase activation protein epsilon |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.3 — chr17:1,344,275-1,400,222 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ45465 |
| Gene groups (HGNC) | 14-3-3 phospho-serine/phospho-threonine binding proteins |
| Hallmark sets | MITOTIC_SPINDLE, MYC_TARGETS_V1 |
| Reactome | 61 pathways, smallest: NADE modulates death signalling; SARS-CoV-2 targets host intracellular signalling and regulatory pathways; Chk1/Chk2(Cds1) mediated inactivation of Cyclin B:Cdk1 complex |
| Matched by | ensembl_id |

**Function**, from UniProt [P62258](https://www.uniprot.org/uniprotkb/P62258) (14-3-3 protein epsilon):

> Adapter protein implicated in the regulation of a large spectrum of both general and specialized signaling pathways. Binds to a large number of partners, usually by recognition of a phosphoserine or phosphothreonine motif. Binding generally results in the modulation of the activity of the binding partner (By similarity). Positively regulates phosphorylated protein HSF1 nuclear export to the cytoplasm. Plays a positive role in the antiviral signaling pathway upstream of TBK1 via interaction with …

**Summary**, from NCBI Gene [7531](https://www.ncbi.nlm.nih.gov/gene/7531):

> This gene product belongs to the 14-3-3 family of proteins which mediate signal transduction by binding to phosphoserine-containing proteins. This highly conserved protein family is found in both plants and mammals, and this protein is 100% identical to the mouse ortholog. It interacts with CDC25 phosphatases, RAF1 and IRS1 proteins, suggesting its role in diverse biochemical activities related to signal transduction, such as cell division and regulation of insulin sensitivity. It has also been …

**Accessions** — [HGNC:12851](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12851) · Entrez [7531](https://www.ncbi.nlm.nih.gov/gene/7531) · UniProt [P62258](https://www.uniprot.org/uniprotkb/P62258) · Ensembl [ENSG00000108953](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108953)

## Data

Gene col 3012: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3012); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3012, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3012]; `tensor/DDL_lfc|DDL_z.npy` [3012]; `embed/gene_vectors.npy` [3012]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3012 or target_col == 3012). Every well: [[YWHAE — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/YWHAE.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
