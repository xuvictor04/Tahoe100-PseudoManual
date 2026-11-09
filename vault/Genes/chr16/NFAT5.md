---
symbol: "NFAT5"
type: "gene"
col: 2289
ensembl_id: "ENSG00000102908"
name: "nuclear factor of activated T cells 5"
location: "16q22.1"
module: 51
arm: "+"
pooled_cpm: 637.29
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 19
n_dd_up_clean: 9
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# NFAT5

*nuclear factor of activated T cells 5* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.65× (z +38.6, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.551× (z -16.7, q 0e+00, down in 46 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.720× (z -13.0, q 1e-36, down in 33 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZSWIM4]] (+0.61, fdr 1e-05), [[BRAF]] (+0.60, fdr 2e-05), [[TCF7L2]] (+0.56, fdr 1e-05); moves opposite to [[ABCB10]] (-0.60, fdr 1e-05), [[IMPDH1]] (-0.56, fdr 2e-05), [[DCUN1D2]] (-0.56, fdr 4e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ALDH1L2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2289.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.65×** | +38.6 | 0e+00 | 46/48 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.66×** | +26.4 | 0e+00 | 48/48 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.23×** | +22.5 | 0e+00 | 47/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.93×** | +18.5 | 0e+00 | 47/48 (NCI-H1573, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.37×** | +16.6 | 0e+00 | 48/49 (NCI-H1573, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.77×** | +16.1 | 0e+00 | 45/48 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.72×** | +15.1 | 0e+00 | 46/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.57×** | +12.7 | 4e-35 | 34/48 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.20×** | +10.8 | 2e-25 | 46/48 (NCI-H1573, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.32×** | +7.8 | 4e-13 | 27/48 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.24×** | +5.8 | 3e-07 | 25/47 (PANC-1, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~7% of this change | **1.22×** | +5.6 | 1e-06 | 27/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.6 | 2e-04 | 20/48 (RPMI-7951, A498, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.17× | +4.4 | 5e-04 | 23/48 (NCI-H1573, RPMI-7951, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~8% of this change | 1.16× | +4.2 | 0.001 | 21/47 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.14× | +3.0 | 0.095 | 12/47 (SW48, C32, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 16 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2289.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.551×** | -16.7 | 0e+00 | 46/49 (SNU-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.539×** | -16.7 | 0e+00 | 43/44 (SNU-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.720×** | -13.0 | 1e-36 | 33/49 (A549, SW1417, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.709×** | -9.7 | 7e-20 | 33/48 (AsPC-1, SNU-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.700×** | -9.2 | 3e-18 | 31/45 (CFPAC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.726×** | -9.0 | 2e-17 | 37/48 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.742×** | -8.4 | 5e-15 | 31/48 (AsPC-1, CFPAC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.748×** | -7.8 | 3e-13 | 31/47 (MIA PaCa-2, SNU-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.764×** | -7.6 | 3e-12 | 34/48 (NCI-H1792, SNU-1, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.774×** | -7.2 | 4e-11 | 35/48 (SW1417, SW480, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.932× | -7.1 | 6e-11 | 2/50 (NCI-H23, MIA PaCa-2) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.815×** | -5.7 | 4e-07 | 26/48 (MIA PaCa-2, AsPC-1, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 0.866× | -5.7 | 5e-07 | 14/48 (NCI-H1792, NCI-H2347, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.817×** | -5.7 | 6e-07 | 26/48 (SNU-1, SW1417, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.829×** | -5.3 | 5e-06 | 25/48 (NCI-H1792, SW480, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.736×** | -4.2 | 9e-04 | 31/48 (SW1417, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.750×** | -3.9 | 0.003 | 28/48 (SW1417, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.762×** | -3.7 | 0.006 | 28/48 (MIA PaCa-2, SNU-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.874× | -3.6 | 0.007 | 16/48 (NCI-H2347, NCI-H1792, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.896× | -3.6 | 0.007 | 12/48 (SNU-1, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.915× | -3.5 | 0.010 | 2/48 (LoVo, NCI-H460) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.773×** | -3.5 | 0.010 | 24/48 (MIA PaCa-2, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.883× | -3.5 | 0.011 | 21/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.779×** | -3.4 | 0.014 | 21/49 (AsPC-1, SNU-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | 0.918× | -3.4 | 0.016 | 6/48 (NCI-H1792, NCI-H460, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.888× | -3.3 | 0.017 | 13/49 (SNU-1, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2289. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 2,117 | 7 (1 ⚠) | 10 (7 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.63× (z +14.7) | [[Dinaciclib (drug)]] 5 µM 0.187× (z -24.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -22.2) |
| [[MIA PaCa-2 (line)]] | alt | 1,576 | 5 | 11 (9 ⚠) | [[Harringtonine (drug)]] 5 µM 2.87× (z +14.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -19.0) |
| [[SW480 (line)]] | alt | 1,271 | 6 (1 ⚠) | 8 (7 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.15× (z +11.9) | [[Dinaciclib (drug)]] 0.5 µM 0.365× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.495× (z -15.6) |
| [[HEC-1-A (line)]] | alt | 598 | 7 | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +32.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.524× (z -18.8) |
| [[NCI-H1573 (line)]] | alt | 484 | 12 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +35.6) | [[Dinaciclib (drug)]] 5 µM 0.248× (z -22.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 742 | 7 (1 ⚠) | 6 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 2.63× (z +15.5) | [[Dinaciclib (drug)]] 5 µM 0.227× (z -23.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -20.2) |
| [[NCI-H2030 (line)]] | alt | 1,059 | 9 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +23.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.538× (z -14.4) |
| [[NCI-H460 (line)]] | wt | 488 | 11 (3 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.44× (z +23.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.565× (z -12.8) |
| [[AsPC-1 (line)]] | alt | 925 | 5 (1 ⚠) | 7 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +19.4) | [[Panobinostat (drug)]] 5 µM 0.370× (z -16.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.657× (z -9.6) |
| [[NCI-H2347 (line)]] | alt | 347 | 8 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +30.9) | [[Dinaciclib (drug)]] 0.5 µM 0.520× (z -12.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 480 | 9 (2 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +21.5) | [[Dinaciclib (drug)]] 5 µM 0.562× (z -9.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 1,276 | 1 | 10 (9 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.83× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.394× (z -22.4) |
| [[A549 (line)]] | wt | 647 | 5 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +31.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.335× (z -25.7) |
| [[BT-474 (line)]] | alt | 304 | 10 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +25.5) | — |
| [[HepG2_C3A (line)]] | wt | 658 | 7 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.15× (z +18.5) | [[Dinaciclib (drug)]] 0.05 µM 0.506× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 571 | 8 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +30.1) | [[Dinaciclib (drug)]] 5 µM 0.280× (z -20.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 346 | 10 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +38.0) | — |
| [[RKO (line)]] | wt | 782 | 8 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +20.2) | [[Dinaciclib (drug)]] 0.5 µM 0.360× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.657× (z -10.2) |
| [[RPMI-7951 (line)]] | alt | 458 | 8 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +28.2) | [[Dinaciclib (drug)]] 5 µM 0.446× (z -14.0) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 455 | 9 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +13.6) | — |
| [[CFPAC-1 (line)]] | alt | 779 | 1 | 8 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +21.1) | [[Dinaciclib (drug)]] 5 µM 0.278× (z -18.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.466× (z -16.3) |
| [[HOP62 (line)]] | alt | 483 | 8 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +33.0) | [[Dinaciclib (drug)]] 0.5 µM 0.517× (z -11.6) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 304 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +27.0) | — |
| [[LoVo (line)]] | wt | 489 | 7 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.25× (z +15.1) | [[Dinaciclib (drug)]] 5 µM 0.510× (z -12.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 441 | 3 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +25.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.609× (z -12.9) |
| [[A-427 (line)]] | wt | 791 | 7 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +21.1) | [[Dinaciclib (drug)]] 0.5 µM 0.473× (z -11.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 429 | 6 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.43× (z +37.2) | [[Dinaciclib (drug)]] 0.5 µM 0.454× (z -12.3) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 432 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +31.9) | — |
| [[KATO III (line)]] | alt | 435 | 6 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.66× (z +21.5) | [[Dinaciclib (drug)]] 5 µM 0.464× (z -12.3) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 550 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +18.3) | — |
| [[LS 180 (line)]] | wt | 629 | 3 (2 ⚠) | 5 (2 ⚠) | [[Selinexor (drug)]] 5 µM 1.66× (z +11.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.99× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.428× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.585× (z -12.1) |
| [[SW48 (line)]] | wt | 396 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +19.5) | — |
| [[C32 (line)]] | wt | 441 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +23.6) | — |
| [[Hs 766T (line)]] | wt | 734 | 6 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +26.3) | [[Dinaciclib (drug)]] 5 µM 0.536× (z -9.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 346 | 5 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +35.8) | [[Dinaciclib (drug)]] 5 µM 0.539× (z -10.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 444 | 4 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +30.6) | [[Dinaciclib (drug)]] 0.5 µM 0.538× (z -11.1) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 582 | 4 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +18.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.544× (z -10.4) |
| [[Panc 03.27 (line)]] | alt | 430 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +33.8) | — |
| [[AN3 CA (line)]] | alt | 599 | 4 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.50× (z +14.1) | [[Dinaciclib (drug)]] 0.5 µM 0.424× (z -10.0) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 449 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +20.3) | [[Dinaciclib (drug)]] 0.5 µM 0.549× (z -9.1) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 1,170 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.265× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -13.4) |
| [[H4 (line)]] | wt | 430 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +23.0) | — |
| [[HCT15 (line)]] | alt | 868 | 1 | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.91× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -17.1) |
| [[SHP-77 (line)]] | alt | 269 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.06× (z +11.1) | — |
| [[SW 1271 (line)]] | alt | 688 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +11.1) | — |
| [[COLO 205 (line)]] | alt | 817 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -12.6) |
| [[SW 1088 (line)]] | alt | 553 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +10.7) | — |
| [[NCI-H2122 (line)]] | alt | 614 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 680 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 596 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2289), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*42 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZSWIM4]] | +0.61 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[BRAF]] | +0.60 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[TCF7L2]] | +0.56 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[HES1]] | +0.56 | +0.53 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[GPATCH8]] | +0.54 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[TGIF2]] | +0.53 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[ERBIN]] | +0.53 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[KLRC2]] | +0.53 | +0.34 / +0.55 | both halves | 1e-04 |  |
| [[CCDC148]] | +0.52 | +0.34 / +0.37 | both halves | 1e-04 |  |
| [[IER3]] | +0.51 | +0.50 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[ZFHX2]] | +0.51 | +0.31 / +0.45 | both halves | 2e-04 |  |
| [[IER5]] | +0.51 | +0.46 / +0.45 | both halves | 3e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |

## Genes that move opposite

*58 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCB10]] | -0.60 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[IMPDH1]] | -0.56 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[DCUN1D2]] | -0.56 | -0.41 / -0.63 | both halves | 4e-05 |  |
| [[XPOT]] | -0.55 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[STIMATE]] | -0.54 | -0.41 / -0.58 | both halves | 4e-05 |  |
| [[SEPTIN7P13]] | -0.54 | -0.33 / -0.55 | both halves | 1e-04 |  |
| [[GK5]] | -0.54 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[SRD5A1]] | -0.53 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[MSTO2P]] | -0.53 | -0.33 / -0.52 | both halves | 1e-04 |  |
| [[LONP1]] | -0.53 | -0.37 / -0.51 | both halves | 8e-05 |  |
| [[NOMO2]] | -0.52 | -0.27 / -0.50 | both halves | 3e-04 |  |
| [[GPD1L]] | -0.52 | -0.40 / -0.49 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ALDH1L2]] | B | ALDH1L2 activity lowers NFAT5's level | lines that do not express ALDH1L2 (23) vs lines expressing it (27) | 1.31× higher at baseline in the lines without ALDH1L2 | 0.083 | ⚠ within organs, on part of the lines; also absent: SLC8A1, ENSG00000230490, GPR173 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.393). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-25.0, 14.2); signed map (5.9, 25.8). **Vector** length 108, 40.5% of its response variance represented; |z| ≥ 3 in 1,933 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +9.2 | +26.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.9 | +3.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.9 | +38.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | -3.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.1 | +12.7 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +3.8 | +1.3 |
|  | [[Entrectinib (drug)]] 5 µM |  | +3.2 | -0.0 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | +3.0 | -0.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.0 | -0.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.7 | -5.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.2 | -3.9 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.2 | -3.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.1 | -4.2 |
|  | [[Budesonide (drug)]] 5 µM |  | -4.0 | -1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.7 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | nuclear factor of activated T cells 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:69,565,094-69,704,666 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TONEBP, KIAA0827, NFATL1, OREBP, NFATZ, NF-AT5 |
| Gene groups (HGNC) | Nuclear factors of activated T-cells; IPT domain containing |
| Hallmark sets | TNFA_SIGNALING_VIA_NFKB |
| Matched by | ensembl_id |

**Function**, from UniProt [O94916](https://www.uniprot.org/uniprotkb/O94916) (Nuclear factor of activated T-cells 5):

> Transcription factor involved, among others, in the transcriptional regulation of osmoprotective and inflammatory genes. Binds the DNA consensus sequence 5'-[ACT][AG]TGGAAA[CAT]A[TA][ATC][CA][ATG][GT][GAC][CG][CT]-3'. Mediates the transcriptional response to hypertonicity. Positively regulates the transcription of LCN2 and S100A4 genes; optimal transactivation of these genes requires the presence of DDX5/DDX17. Also involved in the DNA damage response by preventing formation of R-loops; R-loops …

**Summary**, from NCBI Gene [10725](https://www.ncbi.nlm.nih.gov/gene/10725):

> The product of this gene is a member of the nuclear factors of activated T cells family of transcription factors. Proteins belonging to this family play a central role in inducible gene transcription during the immune response. This protein regulates gene expression induced by osmotic stress in mammalian cells. Unlike monomeric members of this protein family, this protein exists as a homodimer and forms stable dimers with DNA elements. Multiple transcript variants encoding different isoforms …

**Accessions** — [HGNC:7774](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7774) · Entrez [10725](https://www.ncbi.nlm.nih.gov/gene/10725) · UniProt [O94916](https://www.uniprot.org/uniprotkb/O94916) · Ensembl [ENSG00000102908](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102908)

## Data

Gene col 2289: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2289); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2289, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2289]; `tensor/DDL_lfc|DDL_z.npy` [2289]; `embed/gene_vectors.npy` [2289]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2289 or target_col == 2289). Every well: [[NFAT5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NFAT5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
