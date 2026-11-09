---
symbol: "CHD1"
type: "gene"
col: 7750
ensembl_id: "ENSG00000153922"
name: "chromodomain helicase DNA binding protein 1"
location: "5q15-q21.1"
module: 58
arm: "+"
pooled_cpm: 291.5
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 8
n_dd_up_clean: 17
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# CHD1

*chromodomain helicase DNA binding protein 1* — 5q15-q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.50× (z +28.4, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.384× (z -20.2, q 0e+00, down in 44 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 0.843× (z -5.3, q 1e-05, down in 22 of 48 measured lines).
> Its strongest partners by |cos| (71 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 32 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP5F1D]] (+0.55, fdr 6e-04, ⚠ ATP5F1D in the vector space only through flagged drug-doses), [[PAXX]] (+0.54, fdr 0.002, ⚠ one half only (not replicated); PAXX in the vector space only through flagged drug-doses), [[ID1]] (+0.53, fdr 3e-04), [[GCHFR]] (+0.53, fdr 7e-05), [[ZC3H15]] (+0.53, fdr 1e-04); moves opposite to [[CTTN]] (-0.60, fdr 4e-04), [[DCTN5]] (-0.56, fdr 4e-05), [[EAF1]] (-0.54, fdr 2e-04).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7750.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.50×** | +28.4 | 0e+00 | 46/48 (A549, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.56×** | +20.6 | 0e+00 | 47/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.34×** | +18.7 | 0e+00 | 46/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.23×** | +16.9 | 0e+00 | 45/48 (NCI-H1573, A549, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.13×** | +16.5 | 0e+00 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.06×** | +15.8 | 0e+00 | 47/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.85×** | +13.0 | 7e-37 | 46/47 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.64×** | +11.1 | 7e-27 | 44/49 (COLO 205, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.59×** | +10.2 | 2e-22 | 37/48 (HEC-1-A, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.26×** | +9.4 | 4e-19 | 43/48 (SW480, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.42×** | +7.7 | 5e-13 | 38/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.39×** | +7.3 | 2e-11 | 33/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.33×** | +6.3 | 1e-08 | 30/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.29×** | +5.5 | 1e-06 | 33/48 (PANC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **1.23×** | +4.5 | 3e-04 | 29/48 (SW 900, C-33 A, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.22×** | +4.4 | 4e-04 | 26/48 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.23×** | +4.4 | 4e-04 | 28/48 (HT-29, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7750.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.384×** | -20.2 | 0e+00 | 44/44 (Panc 03.27, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.466×** | -16.7 | 0e+00 | 48/49 (NCI-H2347, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.500×** | -14.0 | 2e-42 | 41/45 (SW48, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.807×** | -6.6 | 6e-09 | 27/48 (AsPC-1, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.767×** | -5.6 | 3e-06 | 37/47 (HT-29, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.843× | -5.3 | 1e-05 | 22/48 (A-172, HOP62, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.789×** | -5.2 | 2e-05 | 32/48 (KATO III, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.847× | -5.1 | 2e-05 | 22/49 (A498, NCI-H460, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.945× | -4.3 | 1e-03 | 0/50 | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.837× | -3.9 | 0.006 | 22/48 (SK-MEL-2, BT-474, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 0.844× | -3.7 | 0.010 | 20/48 (A-427, NCI-H2030, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 0.844× | -3.7 | 0.010 | 21/48 (NCI-H23, SW480, …) | top dose only |  |
| [[Ixazomib (drug)]] 5 µM |  | **0.748×** | -3.3 | 0.040 | 22/48 (A-427, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | 0.866× | -3.1 | 0.063 | 14/48 (HOP62, AsPC-1, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.866× | -3.1 | 0.063 | 12/48 (C-33 A, RPMI-7951, …) | top dose only |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.866× | -3.1 | 0.063 | 9/47 (Panc 03.27, hTERT-HPNE, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.867× | -3.1 | 0.064 | 12/48 (LOX-IMVI, NCI-H2030, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.773×** | -2.9 | 0.100 | 23/47 (NCI-H2347, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.875× | -2.9 | 0.100 | 14/47 (SW480, LS 180, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7750. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 273 | 13 (2 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.29× (z +23.6) | [[Dinaciclib (drug)]] 0.5 µM 0.486× (z -14.3) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 292 | 13 (3 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +18.0) | [[Dinaciclib (drug)]] 5 µM 0.385× (z -11.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 480 | 11 (2 ⚠) | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.77× (z +21.0) | [[Dinaciclib (drug)]] 5 µM 0.154× (z -24.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 271 | 13 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +27.2) | [[Dinaciclib (drug)]] 5 µM 0.326× (z -17.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 382 | 7 (2 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +23.5) | [[Dinaciclib (drug)]] 0.5 µM 0.283× (z -19.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 211 | 6 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +22.5) | [[Dinaciclib (drug)]] 5 µM 0.314× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.655× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 410 | 7 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +18.2) | [[Dinaciclib (drug)]] 0.5 µM 0.302× (z -17.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 273 | 8 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +21.4) | [[Dinaciclib (drug)]] 5 µM 0.383× (z -11.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 255 | 7 (2 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +21.8) | [[Dinaciclib (drug)]] 0.5 µM 0.411× (z -11.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 374 | 8 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.57× (z +22.1) | [[Dinaciclib (drug)]] 0.5 µM 0.418× (z -15.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 379 | 7 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +27.4) | [[Dinaciclib (drug)]] 0.5 µM 0.315× (z -19.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 242 | 7 (2 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +23.9) | [[Dinaciclib (drug)]] 0.5 µM 0.353× (z -13.1) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 155 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +19.3) | — |
| [[COLO 205 (line)]] | alt | 256 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +18.9) | — |
| [[HOP62 (line)]] | alt | 304 | 6 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +14.0) | [[Dinaciclib (drug)]] 0.5 µM 0.323× (z -13.5) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 196 | 7 (3 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.381× (z -12.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 285 | 6 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.80× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.338× (z -11.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 263 | 8 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +27.4) | [[Dinaciclib (drug)]] 0.5 µM 0.545× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 284 | 7 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +14.0) | [[Dinaciclib (drug)]] 5 µM 0.308× (z -14.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 273 | 8 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +22.1) | [[Dinaciclib (drug)]] 5 µM 0.128× (z -29.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 201 | 7 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +23.2) | [[Dinaciclib (drug)]] 5 µM 0.376× (z -15.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 297 | 4 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.94× (z +28.7) | [[Dinaciclib (drug)]] 5 µM 0.376× (z -11.9) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 244 | 6 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +18.6) | [[Dinaciclib (drug)]] 5 µM 0.494× (z -10.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 267 | 8 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.50× (z +20.0) | — |
| [[NCI-H23 (line)]] | alt | 255 | 5 (1 ⚠) | 3 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.16× (z +12.6) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.09× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.377× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.554× (z -9.7) |
| [[A498 (line)]] | wt | 324 | 3 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +26.4) | [[Dinaciclib (drug)]] 0.05 µM 0.313× (z -16.8) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 303 | 4 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.04× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.418× (z -12.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 302 | 3 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +20.0) | [[Dinaciclib (drug)]] 0.5 µM 0.474× (z -9.9) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 313 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +16.7) | — |
| [[hTERT-HPNE (line)]] | wt | 320 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.314× (z -12.0) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 165 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +21.8) | — |
| [[SW 900 (line)]] | alt | 265 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.425× (z -11.4) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 238 | 5 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.56× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.531× (z -8.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 126 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.43× (z +25.9) | [[Dinaciclib (drug)]] 5 µM 0.339× (z -12.8) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 222 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.49× (z +16.1) | [[Dinaciclib (drug)]] 0.05 µM 0.452× (z -9.4) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 315 | 3 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +13.0) | [[Dinaciclib (drug)]] 0.05 µM 0.136× (z -19.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 331 | 2 | 3 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 3.47× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.328× (z -18.4) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 298 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +15.8) | [[Dinaciclib (drug)]] 0.5 µM 0.364× (z -12.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 203 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +19.6) | — |
| [[SK-MEL-2 (line)]] | alt | 422 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +19.1) | [[Dinaciclib (drug)]] 5 µM 0.162× (z -20.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 314 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.55× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.349× (z -12.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 302 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.298× (z -12.9) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 389 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -16.3) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 265 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.194× (z -13.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 328 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.29× (z +9.7) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.65× (z +8.7) | — |
| [[SW 1271 (line)]] | alt | 516 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.96× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.356× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 533 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.326× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H2122 (line)]] | alt | 307 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 319 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 225 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7750), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 17 of them with an alert (⚠; 14 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP5F1D]] ⚠ | +0.55 | +0.22 / +0.54 | both halves | 6e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[PAXX]] ⚠ | +0.54 | +0.13 / +0.54 | ⚠ one half (not replicated) | 0.002 | ⚠ in the vector space only through flagged drug-doses |
| [[ID1]] | +0.53 | +0.27 / +0.47 | both halves | 3e-04 |  |
| [[GCHFR]] | +0.53 | +0.38 / +0.39 | both halves | 7e-05 |  |
| [[ZC3H15]] | +0.53 | +0.34 / +0.51 | both halves | 1e-04 |  |
| [[NUDT8]] | +0.52 | +0.34 / +0.38 | both halves | 1e-04 |  |
| [[ANTKMT]] | +0.52 | +0.25 / +0.41 | both halves | 4e-04 |  |
| [[SMCHD1]] | +0.51 | +0.27 / +0.57 | both halves | 3e-04 |  |
| [[ARL13B]] | +0.50 | +0.22 / +0.52 | both halves | 6e-04 |  |
| [[PPP1R35]] ⚠ | +0.50 | +0.22 / +0.46 | both halves | 6e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[TPR]] | +0.50 | +0.29 / +0.52 | both halves | 2e-04 |  |
| [[TCAF1]] | +0.50 | +0.18 / +0.45 | ⚠ not reproduced | 9e-04 |  |
| [[LSM2]] | +0.49 | +0.36 / +0.38 | both halves | 1e-04 |  |
| [[PHIP]] | +0.48 | +0.27 / +0.56 | both halves | 3e-04 | STRING 519 |
| [[MFSD3]] | +0.47 | +0.30 / +0.37 | both halves | 2e-04 |  |
| [[MIER1]] | +0.46 | +0.27 / +0.56 | both halves | 3e-04 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 15 of them with an alert (⚠; 15 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTTN]] | -0.60 | -0.26 / -0.60 | both halves | 4e-04 |  |
| [[DCTN5]] | -0.56 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[EAF1]] | -0.54 | -0.32 / -0.57 | both halves | 2e-04 |  |
| [[UHMK1]] | -0.53 | -0.24 / -0.48 | both halves | 5e-04 | pathway: ESR-mediated signaling |
| [[LY6G5B]] | -0.51 | -0.16 / -0.43 | ⚠ not reproduced | 0.001 |  |
| [[NRAS]] | -0.50 | -0.26 / -0.43 | both halves | 3e-04 | pathway: ESR-mediated signaling |
| [[AP2B1]] | -0.49 | -0.28 / -0.40 | both halves | 3e-04 |  |
| [[MFN2]] | -0.48 | -0.31 / -0.38 | both halves | 2e-04 |  |
| [[HEXA]] | -0.48 | -0.24 / -0.56 | both halves | 4e-04 |  |
| [[DAZAP2]] | -0.48 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[VAMP3]] | -0.47 | -0.27 / -0.48 | both halves | 3e-04 |  |
| [[PEX19]] | -0.47 | -0.39 / -0.33 | both halves | 1e-04 |  |
| [[TPP1]] | -0.47 | -0.34 / -0.43 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.483). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-48.4, -15.8); signed map (-31.6, 4.7). **Vector** length 78.9, 30.2% of its response variance represented; |z| ≥ 3 in 1,506 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +6.3 | +13.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.2 | +0.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.8 | -0.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.2 | +0.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | +1.8 |
|  | [[AZD-7648 (drug)]] 0.5 µM |  | +2.5 | -0.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.5 | -1.6 |
|  | [[Saquinavir (drug)]] 5 µM |  | +2.4 | -0.2 |
|  | [[Bendamustine (drug)]] 5 µM |  | +2.4 | +0.1 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -7.1 | -6.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.0 | -3.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.2 | +11.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | -4.1 | -3.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.9 | +20.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.2 | +9.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -5.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.2 | +0.6 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.1 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | chromodomain helicase DNA binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q15-q21.1 — chr5:98,853,985-98,929,007 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | SNF2 related family |
| Reactome | 7 pathways, smallest: CHD1 and CHD2 subfamily; Estrogen-dependent gene expression; CHD chromatin remodelers |
| Matched by | ensembl_id |

**Function**, from UniProt [O14646](https://www.uniprot.org/uniprotkb/O14646) (ATP-dependent chromatin remodeler CHD1):

> ATP-dependent chromatin-remodeling factor which functions as substrate recognition component of the transcription regulatory histone acetylation (HAT) complex SAGA. Regulates polymerase II transcription. Also required for efficient transcription by RNA polymerase I, and more specifically the polymerase I transcription termination step. Regulates negatively DNA replication. Not only involved in transcription-related chromatin-remodeling, but also required to maintain a specific chromatin …

**Summary**, from NCBI Gene [1105](https://www.ncbi.nlm.nih.gov/gene/1105):

> The CHD family of proteins is characterized by the presence of chromo (chromatin organization modifier) domains and SNF2-related helicase/ATPase domains. CHD genes alter gene expression possibly by modification of chromatin structure thus altering access of the transcriptional apparatus to its chromosomal DNA template. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:1915](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1915) · Entrez [1105](https://www.ncbi.nlm.nih.gov/gene/1105) · UniProt [O14646](https://www.uniprot.org/uniprotkb/O14646) · Ensembl [ENSG00000153922](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153922)

## Data

Gene col 7750: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7750); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7750, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7750]; `tensor/DDL_lfc|DDL_z.npy` [7750]; `embed/gene_vectors.npy` [7750]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7750 or target_col == 7750). Every well: [[CHD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
