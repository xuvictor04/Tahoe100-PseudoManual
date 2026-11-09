---
symbol: "PUM2"
type: "gene"
col: 631
ensembl_id: "ENSG00000055917"
name: "pumilio RNA binding family member 2"
location: "2p24.1"
module: 51
arm: "+"
pooled_cpm: 374.44
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 14
n_dd_up_clean: 10
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# PUM2

*pumilio RNA binding family member 2* — 2p24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.56× (z +16.5, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.379× (z -16.3, q 0e+00, down in 44 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.485× (z -12.7, q 1e-34, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (87 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBM33]] (+0.70, fdr 7e-06), [[SCAF8]] (+0.69, fdr 1e-05), [[ZZZ3]] (+0.67, fdr 7e-06); moves opposite to [[KCTD5]] (-0.63, fdr 1e-05), [[FAM219A]] (-0.59, fdr 1e-04), [[TAF13]] (-0.59, fdr 6e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 631.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.56×** | +16.5 | 0e+00 | 48/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.14×** | +13.3 | 4e-38 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **4.04×** | +12.8 | 3e-35 | 49/49 (SW480, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.61×** | +11.8 | 6e-30 | 48/48 (SW480, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.94×** | +11.7 | 2e-29 | 47/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.94×** | +11.6 | 3e-29 | 47/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.32×** | +6.9 | 6e-10 | 28/48 (A-172, COLO 205, …) | top dose only | cell-cycle shift (explains ~4% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.39×** | +5.8 | 4e-07 | 32/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.38×** | +5.7 | 7e-07 | 33/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +5.6 | 1e-06 | 40/47 (COLO 205, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.29×** | +4.3 | 8e-04 | 33/48 (A-172, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.21×** | +3.4 | 0.034 | 26/48 (Hs 766T, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.20× | +3.2 | 0.066 | 22/48 (SW1417, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.078 | 20/48 (KATO III, HT-29, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 631.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.379×** | -16.3 | 0e+00 | 44/44 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.399×** | -16.1 | 0e+00 | 48/49 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.485×** | -12.7 | 1e-34 | 48/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.492×** | -12.4 | 3e-33 | 48/48 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.626×** | -11.6 | 5e-29 | 47/49 (A549, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.568×** | -9.9 | 3e-21 | 47/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.620×** | -7.7 | 8e-13 | 37/45 (NCI-H2347, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.676×** | -6.9 | 5e-10 | 46/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.692×** | -6.2 | 4e-08 | 35/50 (A-172, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.718×** | -5.8 | 4e-07 | 41/48 (SW480, SK-MEL-2, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.740×** | -5.3 | 8e-06 | 43/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **0.774×** | -4.3 | 8e-04 | 35/47 (MIA PaCa-2, NCI-H2347, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.788×** | -4.2 | 0.001 | 36/48 (SW1417, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.830×** | -3.1 | 0.073 | 24/48 (SW480, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 631. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 401 | 11 (2 ⚠) | 6 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.14× (z +20.6) | [[Dinaciclib (drug)]] 5 µM 0.290× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.433× (z -12.1) |
| [[SW480 (line)]] | alt | 453 | 8 (1 ⚠) | 9 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.97× (z +21.8) | [[Dinaciclib (drug)]] 5 µM 0.329× (z -21.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.519× (z -18.5) |
| [[KATO III (line)]] | alt | 411 | 6 (1 ⚠) | 7 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.91× (z +20.7) | [[Dinaciclib (drug)]] 5 µM 0.346× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.456× (z -12.0) |
| [[LoVo (line)]] | wt | 323 | 7 (2 ⚠) | 6 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.38× (z +20.4) | [[Dinaciclib (drug)]] 5 µM 0.378× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.436× (z -13.9) |
| [[HOP62 (line)]] | alt | 369 | 6 (1 ⚠) | 6 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.29× (z +15.1) | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.406× (z -11.3) |
| [[HT-29 (line)]] | alt | 368 | 7 (1 ⚠) | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.89× (z +16.1) | [[Dinaciclib (drug)]] 0.5 µM 0.372× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.384× (z -14.5) |
| [[NCI-H1573 (line)]] | alt | 410 | 7 (2 ⚠) | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.40× (z +19.3) | [[Dinaciclib (drug)]] 0.5 µM 0.303× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.424× (z -11.3) |
| [[NCI-H23 (line)]] | alt | 463 | 7 (2 ⚠) | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.38× (z +13.6) | [[Dinaciclib (drug)]] 0.5 µM 0.459× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.612× (z -10.9) |
| [[SW 900 (line)]] | alt | 400 | 6 (1 ⚠) | 6 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.78× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.387× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.419× (z -10.9) |
| [[SW1417 (line)]] | alt | 579 | 4 (1 ⚠) | 8 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +14.4) | [[Panobinostat (drug)]] 0.5 µM 0.401× (z -14.4) |
| [[LS 180 (line)]] | wt | 422 | 6 (1 ⚠) | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.04× (z +17.5) | [[Dinaciclib (drug)]] 5 µM 0.325× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.441× (z -10.3) |
| [[PANC-1 (line)]] | alt | 375 | 6 (1 ⚠) | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.91× (z +21.5) | [[Dinaciclib (drug)]] 0.5 µM 0.374× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.451× (z -12.7) |
| [[A-172 (line)]] | wt | 268 | 5 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +15.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.450× (z -17.7) |
| [[LOX-IMVI (line)]] | wt | 430 | 3 | 7 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.95× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.207× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -12.1) |
| [[A549 (line)]] | wt | 436 | 3 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +11.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -20.2) |
| [[BT-474 (line)]] | alt | 338 | 8 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.81× (z +15.6) | [[Panobinostat (drug)]] 0.5 µM 0.554× (z -9.0) |
| [[COLO 205 (line)]] | alt | 311 | 6 (2 ⚠) | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.37× (z +18.9) | [[Dinaciclib (drug)]] 0.5 µM 0.429× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.490× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 411 | 2 | 7 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.45× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.280× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.439× (z -10.4) |
| [[SNU-423 (line)]] | alt | 277 | 6 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.70× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.402× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.593× (z -9.4) |
| [[HEC-1-A (line)]] | alt | 396 | 3 | 5 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 4.94× (z +11.9) | [[Dinaciclib (drug)]] 0.5 µM 0.294× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.557× (z -11.8) |
| [[HepG2_C3A (line)]] | wt | 429 | 3 (2 ⚠) | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.42× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.384× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.457× (z -9.1) |
| [[J82 (line)]] | alt | 226 | 5 (1 ⚠) | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.80× (z +13.6) | [[Dinaciclib (drug)]] 0.5 µM 0.400× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.422× (z -11.6) |
| [[NCI-H1792 (line)]] | alt | 248 | 6 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.80× (z +17.5) | [[Dinaciclib (drug)]] 5 µM 0.432× (z -10.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 304 | 2 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.319× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.533× (z -12.2) |
| [[H4 (line)]] | wt | 229 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.25× (z +14.1) | — |
| [[Hs 766T (line)]] | wt | 228 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.99× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.411× (z -11.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 335 | 1 | 6 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.06× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.276× (z -18.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.575× (z -11.1) |
| [[RPMI-7951 (line)]] | alt | 338 | 4 (1 ⚠) | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.48× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.327× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.562× (z -10.2) |
| [[SW48 (line)]] | wt | 465 | 3 (1 ⚠) | 4 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.23× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.216× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -10.0) |
| [[A-427 (line)]] | wt | 540 | 2 | 4 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 3.89× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.223× (z -20.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.504× (z -9.6) |
| [[AsPC-1 (line)]] | alt | 420 | 3 (1 ⚠) | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.37× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.274× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.444× (z -9.0) |
| [[CFPAC-1 (line)]] | alt | 319 | 1 | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.04× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.344× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.480× (z -9.4) |
| [[HCT15 (line)]] | alt | 395 | 3 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.40× (z +12.6) | [[Dinaciclib (drug)]] 0.5 µM 0.335× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.537× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 252 | 4 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.95× (z +12.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -11.0) |
| [[Panc 03.27 (line)]] | alt | 310 | 3 | 3 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 4.59× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.432× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.460× (z -10.5) |
| [[RKO (line)]] | wt | 424 | 4 | 2 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 6.42× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.206× (z -20.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.499× (z -13.0) |
| [[C-33 A (line)]] | alt | 434 | 2 | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.13× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.281× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.508× (z -8.6) |
| [[C32 (line)]] | wt | 379 | 2 | 3 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 5.31× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.400× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.485× (z -8.7) |
| [[HS-578T (line)]] | alt | 220 | 4 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.38× (z +10.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.512× (z -11.5) |
| [[SK-MEL-2 (line)]] | alt | 296 | 2 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.37× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.228× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.522× (z -11.8) |
| [[AN3 CA (line)]] | alt | 451 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.293× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.499× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 517 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.64× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.278× (z -12.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 359 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.30× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.463× (z -10.0) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 484 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.13× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.245× (z -15.6) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 378 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.48× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.298× (z -11.3) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 444 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.235× (z -9.9) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 380 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.69× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.273× (z -9.2) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 294 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.219× (z -9.7) ⚠ toxic; transcription drop |
| [[NCI-H2122 (line)]] | alt | 455 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 403 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 631), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 10 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM33]] | +0.70 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[SCAF8]] | +0.69 | +0.56 / +0.73 | both halves | 1e-05 | STRING 401 |
| [[ZZZ3]] | +0.67 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[WAC]] | +0.63 | +0.63 / +0.61 | both halves | 7e-06 | STRING 605 |
| [[PUM1]] | +0.63 | +0.53 / +0.58 | both halves | 1e-05 | same gene group; STRING 721 |
| [[RAF1]] | +0.62 | +0.66 / +0.57 | both halves | 9e-06 |  |
| [[LUC7L2]] | +0.62 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[USP24]] | +0.61 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[VAPA]] | +0.61 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[DYRK1A]] | +0.60 | +0.59 / +0.59 | both halves | 7e-06 | STRING 405 |
| [[PTBP2]] | +0.58 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[ZNF428]] | +0.58 | +0.26 / +0.50 | both halves | 4e-04 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCTD5]] | -0.63 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[FAM219A]] | -0.59 | -0.33 / -0.62 | both halves | 1e-04 |  |
| [[TAF13]] | -0.59 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[CDC37]] | -0.57 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[EHD4]] | -0.56 | -0.29 / -0.50 | both halves | 2e-04 |  |
| [[RP2]] | -0.55 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[STK10]] | -0.54 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[WNT9A]] | -0.53 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[LRRFIP1]] | -0.53 | -0.18 / -0.51 | ⚠ one half (not replicated) | 9e-04 |  |
| [[NPC1]] | -0.52 | -0.32 / -0.54 | both halves | 2e-04 |  |
| [[GPATCH2L]] | -0.52 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[PTPRH]] | -0.52 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[MIR22HG]] | -0.51 | -0.58 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PUM2's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.454). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-18.0, 1.9); signed map (12.9, -34.4). **Vector** length 77.4, 37.3% of its response variance represented; |z| ≥ 3 in 1,379 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.4 | -16.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.3 | -16.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.4 | -7.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.4 | +5.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.9 | -1.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.5 | +0.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | -3.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.4 | -2.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.0 | -2.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.5 | -5.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.5 | -5.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.4 | +0.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.1 | +3.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.7 | -1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | +3.1 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -2.1 | -1.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.1 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | pumilio RNA binding family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p24.1 — chr2:20,248,691-20,352,234 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PUMH2, KIAA0235 |
| Gene groups (HGNC) | Pumilio homology domain containing |
| Reactome | 1 pathways, smallest: Neddylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TB72](https://www.uniprot.org/uniprotkb/Q8TB72) (Pumilio homolog 2):

> Sequence-specific RNA-binding protein that acts as a post-transcriptional repressor by binding the 3'-UTR of mRNA targets. Binds to an RNA consensus sequence, the Pumilio Response Element (PRE), 5'-UGUANAUA-3', that is related to the Nanos Response Element (NRE) (, PubMed:21397187). Mediates post-transcriptional repression of transcripts via different mechanisms: acts via direct recruitment of the CCR4-POP2-NOT deadenylase leading to translational inhibition and mRNA degradation. Also mediates …

**Summary**, from NCBI Gene [23369](https://www.ncbi.nlm.nih.gov/gene/23369):

> This gene encodes a protein that belongs to a family of RNA-binding proteins. The encoded protein functions as a translational repressor during embryonic development and cell differentiation. This protein is also thought to be a positive regulator of cell proliferation in adipose-derived stem cells. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Sep 2013]

**Accessions** — [HGNC:14958](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14958) · Entrez [23369](https://www.ncbi.nlm.nih.gov/gene/23369) · UniProt [Q8TB72](https://www.uniprot.org/uniprotkb/Q8TB72) · Ensembl [ENSG00000055917](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000055917)

## Data

Gene col 631: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 631); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 631, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 631]; `tensor/DDL_lfc|DDL_z.npy` [631]; `embed/gene_vectors.npy` [631]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 631 or target_col == 631). Every well: [[PUM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PUM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
