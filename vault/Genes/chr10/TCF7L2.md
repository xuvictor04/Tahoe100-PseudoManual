---
symbol: "TCF7L2"
type: "gene"
col: 7312
ensembl_id: "ENSG00000148737"
name: "transcription factor 7 like 2"
location: "10q25.2-q25.3"
module: 97
arm: "+"
pooled_cpm: 321.26
n_lines_expressing: 48
n_dd_up: 9
n_dd_down: 24
n_dd_up_clean: 8
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 17
direction_downstream: 0
tags: ["gene", "module/097"]
generated_by: "tahoemap"
---

# TCF7L2

*transcription factor 7 like 2* — 10q25.2-q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.53× (z +10.4, q 1e-22, up in 36 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.400× (z -21.6, q 0e+00, down in 37 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.680× (z -9.4, q 4e-19, down in 32 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FOXO1]] (+0.65, fdr 2e-05), [[PPP3CA]] (+0.61, fdr 1e-05), [[HES1]] (+0.61, fdr 3e-05); moves opposite to [[PAAF1]] (-0.53, fdr 2e-05), [[CLCC1]] (-0.52, fdr 5e-05), [[ZNF25]] (-0.52, fdr 5e-05).
> It is in [[Module 097]], a single-armed module (estrogen response early).
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[KLF5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠; shown: the 15 strongest. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7312.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.53×** | +10.4 | 1e-22 | 36/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.54×** | +10.2 | 9e-22 | 32/46 (HEC-1-A, NCI-H460, …) | top dose only | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.30×** | +9.1 | 1e-17 | 28/46 (A498, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.42×** | +8.5 | 2e-15 | 36/46 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.42×** | +8.5 | 2e-15 | 33/46 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.41×** | +8.3 | 9e-15 | 32/46 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +8.0 | 1e-13 | 25/46 (HepG2/C3A, SW1417, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.18× | +3.9 | 0.008 | 20/45 (NCI-H460, HOP62, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.19× | +3.8 | 0.010 | 20/45 (LoVo, AsPC-1, …) | rises with dose | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **1.34×** | +3.7 | 0.010 | 23/46 (NCI-H2030, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.17× | +3.6 | 0.014 | 17/45 (NCI-H460, AsPC-1, …) | rises with dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.30×** | +3.3 | 0.039 | 19/46 (Hs 766T, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.3 | 0.047 | 12/45 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 1.14× | +3.1 | 0.068 | 18/47 (SW480, SW1417, …) | rises with dose |  |
| [[PH-797804 (drug)]] 0.05 µM |  | 1.14× | +3.1 | 0.076 | 6/46 (CFPAC-1, COLO 205, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 17 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7312.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.400×** | -21.6 | 0e+00 | 37/42 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.424×** | -19.0 | 0e+00 | 42/47 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.478×** | -16.7 | 0e+00 | 40/43 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.599×** | -12.5 | 8e-34 | 44/46 (SW48, AsPC-1, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.605×** | -11.8 | 4e-30 | 38/45 (HepG2/C3A, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.680×** | -9.4 | 4e-19 | 32/46 (A-427, AsPC-1, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.508×** | -8.7 | 4e-16 | 42/46 (SW48, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.537×** | -7.9 | 2e-13 | 36/46 (SW48, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.547×** | -7.7 | 8e-13 | 42/46 (AsPC-1, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.557×** | -7.5 | 5e-12 | 40/46 (HEC-1-A, SW48, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.819×** | -6.9 | 3e-10 | 27/47 (SW 900, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.604×** | -6.4 | 5e-09 | 35/46 (SW48, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 0.836× | -6.2 | 3e-08 | 22/47 (SW480, AsPC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.797×** | -5.6 | 1e-06 | 30/46 (SW 900, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.655×** | -5.4 | 3e-06 | 24/36 (BT-474, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.807×** | -4.9 | 3e-05 | 26/46 (A-427, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 0.5 µM |  | **0.766×** | -4.6 | 1e-04 | 30/47 (SW48, A498, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.816×** | -4.5 | 2e-04 | 25/45 (BT-474, NCI-H1573, …) | all doses, flat |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.775×** | -4.4 | 2e-04 | 27/46 (SW48, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.835× | -4.4 | 3e-04 | 23/46 (NCI-H1573, NCI-H23, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.793×** | -4.1 | 0.001 | 25/46 (SW48, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | 0.854× | -3.7 | 0.004 | 20/45 (NCI-H460, NCI-H1573, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7312. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 198 | 11 (6 ⚠) | 3 (3 ⚠) | [[Digitoxin (drug)]] 5 µM 3.76× (z +26.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.73× (z +26.3) | [[Dinaciclib (drug)]] 5 µM 0.296× (z -23.4) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 548 | 6 (4 ⚠) | 7 (6 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.85× (z +13.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.296× (z -18.6) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.495× (z -11.2) |
| [[SW480 (line)]] | alt | 519 | 3 (2 ⚠) | 10 (8 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.66× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.210× (z -25.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.568× (z -9.4) |
| [[HEC-1-A (line)]] | alt | 347 | 5 (2 ⚠) | 7 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +26.2) | [[Dinaciclib (drug)]] 0.05 µM 0.409× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.552× (z -10.7) |
| [[LOX-IMVI (line)]] | wt | 220 | 6 (1 ⚠) | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.48× (z +13.8) | [[Dinaciclib (drug)]] 5 µM 0.411× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.525× (z -9.8) |
| [[SNU-423 (line)]] | alt | 283 | 6 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +14.8) | [[Dinaciclib (drug)]] 5 µM 0.418× (z -14.3) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 738 | 1 | 9 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.58× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.183× (z -21.5) ⚠ toxic; transcription drop · without an alert: [[venetoclax (drug)]] 5 µM 0.203× (z -11.0) |
| [[A498 (line)]] | wt | 225 | 4 (2 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +28.9) | [[Dinaciclib (drug)]] 5 µM 0.405× (z -14.3) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 542 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.214× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.494× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 571 | 2 (1 ⚠) | 6 (5 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.07× (z +14.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.220× (z -20.2) ⚠ toxic · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.512× (z -8.8) |
| [[HOP62 (line)]] | alt | 117 | 7 (2 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.96× (z +15.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.542× (z -9.0) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 316 | 1 | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.58× (z +9.0) | [[Auranofin (drug)]] 5 µM 0.311× (z -16.3) |
| [[AsPC-1 (line)]] | alt | 690 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.191× (z -19.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.355× (z -13.4) |
| [[KATO III (line)]] | alt | 655 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.225× (z -17.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 592 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.158× (z -22.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.464× (z -14.5) |
| [[NCI-H1792 (line)]] | alt | 360 | 0 | 7 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -14.9) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.612× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 227 | 1 | 6 (6 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.74× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.389× (z -13.5) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 482 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -22.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.462× (z -12.0) |
| [[PANC-1 (line)]] | alt | 278 | 4 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +15.3) | [[Dinaciclib (drug)]] 0.5 µM 0.376× (z -14.8) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 737 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.362× (z -9.7) |
| [[HT-29 (line)]] | alt | 616 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -15.5) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.373× (z -11.2) |
| [[LS 180 (line)]] | wt | 722 | 2 (1 ⚠) | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.67× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.235× (z -17.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 287 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.207× (z -23.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.466× (z -11.6) |
| [[NCI-H2030 (line)]] | alt | 303 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.323× (z -16.2) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 352 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.389× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.616× (z -9.3) |
| [[A549 (line)]] | wt | 319 | 2 | 3 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.68× (z +12.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -13.8) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.459× (z -9.4) |
| [[H4 (line)]] | wt | 179 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.48× (z +10.7) | — |
| [[HS-578T (line)]] | alt | 102 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +13.5) | — |
| [[AN3 CA (line)]] | alt | 371 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.281× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.428× (z -8.7) |
| [[CHP-212 (line)]] | wt | 264 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.55× (z +8.7) | [[Dinaciclib (drug)]] 0.05 µM 0.286× (z -10.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 219 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +13.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.254× (z -20.0) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 174 | 1 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.54× (z +8.8) ⚠ cell-cycle shift, explains ~15% of this change | [[Dinaciclib (drug)]] 5 µM 0.355× (z -14.3) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 157 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +9.5) | — |
| [[C32 (line)]] | wt | 140 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 2.69× (z +11.1) | — |
| [[HCT15 (line)]] | alt | 315 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.243× (z -14.1) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 147 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 2.79× (z +11.4) | — |
| [[NCI-H23 (line)]] | alt | 121 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.399× (z -11.4) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 147 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.424× (z -12.6) ⚠ unreliable plate only |
| [[BT-474 (line)]] | alt | 115 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.116× (z -13.5) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 219 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.437× (z -9.9) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 146 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 2.31× (z +9.8) | — |
| [[NCI-H661 (line)]] | alt | 258 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.208× (z -10.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 101 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +10.7) ⚠ cell-cycle shift, explains ~15% of this change | — |
| [[SW 1271 (line)]] | alt | 161 | 0 | 1 | — | [[Decitabine (drug)]] 0.05 µM 0.168× (z -9.0) |
| [[J82 (line)]] | alt | 64.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 364 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 330 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.3 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 250 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 182 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7312), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FOXO1]] | +0.65 | +0.47 / +0.66 | both halves | 2e-05 | STRING 589 |
| [[PPP3CA]] | +0.61 | +0.57 / +0.54 | both halves | 1e-05 | pathway: Beta-catenin independent WNT signaling |
| [[HES1]] | +0.61 | +0.45 / +0.59 | both halves | 3e-05 | pathway: HALLMARK_NOTCH_SIGNALING |
| [[TJP2]] | +0.60 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[MAGI1]] | +0.60 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[KIF13B]] | +0.59 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[USP6NL]] | +0.58 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[BAIAP2L1]] | +0.57 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[NFAT5]] | +0.56 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[LRP6]] | +0.56 | +0.44 / +0.49 | both halves | 3e-05 | pathway: Signaling by WNT; STRING 509 |
| [[LIPH]] | +0.56 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[CTNNB1]] | +0.55 | +0.40 / +0.61 | both halves | 4e-05 | same gene group; pathway: Beta-catenin independent WNT signaling; STRING 999 |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAAF1]] | -0.53 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[CLCC1]] | -0.52 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[ZNF25]] | -0.52 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[ZNF343]] | -0.52 | -0.58 / -0.37 | both halves | 7e-05 |  |
| [[CHFR]] | -0.52 | -0.26 / -0.58 | both halves | 3e-04 |  |
| [[SLC30A6]] | -0.51 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[XPNPEP3]] | -0.51 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[SZT2]] | -0.50 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[RUSF1]] | -0.49 | -0.52 / -0.39 | both halves | 5e-05 |  |
| [[KLRA1P]] | -0.49 | -0.38 / -0.51 | both halves | 7e-05 |  |
| [[XPOT]] | -0.49 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[APTX]] | -0.49 | -0.44 / -0.52 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 17, C 0. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLF5]] | B | KLF5 activity raises TCF7L2's level | lines that do not express KLF5 (18) vs lines expressing it (32) | 1.96× lower at baseline in the lines without KLF5 | 0.001 | ⚠ within organs, on part of the lines; also absent: LAMA3, IFNLR1, NCMAP; maybe low, not absent |
| [[PPARG]] | B | PPARG activity raises TCF7L2's level | lines that do not express PPARG (20) vs lines expressing it (30) | 1.80× lower at baseline in the lines without PPARG | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000271933, LINC01589, NUP62CL |
| [[SDR16C5]] | B | SDR16C5 activity raises TCF7L2's level | lines that do not express SDR16C5 (28) vs lines expressing it (22) | 2.10× lower at baseline in the lines without SDR16C5 | 0.009 | ⚠ within organs, on part of the lines; also absent: CATSPERB, FA2H, LIPH |
| [[SH2D3A]] | B | SH2D3A activity raises TCF7L2's level | lines that do not express SH2D3A (24) vs lines expressing it (26) | 2.13× lower at baseline in the lines without SH2D3A | 0.009 | ⚠ within organs, on part of the lines; also absent: GRB7, MYO5B, CRB3 |
| [[LIPH]] | B | LIPH activity raises TCF7L2's level | lines that do not express LIPH (27) vs lines expressing it (23) | 2.09× lower at baseline in the lines without LIPH | 0.011 | ⚠ within organs, on part of the lines; also absent: CATSPERB, TC2N, SDR16C5 |
| [[JUP]] | B | JUP activity raises TCF7L2's level | lines that do not express JUP (16) vs lines expressing it (34) | 2.20× lower at baseline in the lines without JUP | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |
| [[MAML2]] | B | MAML2 activity raises TCF7L2's level | lines that do not express MAML2 (8) vs lines expressing it (42) | 1.79× lower at baseline in the lines without MAML2 | 0.017 | ⚠ within organs, on part of the lines; also absent: TNS3, SMOX, ALDH3B1 |
| [[SLC52A3]] | B | SLC52A3 activity raises TCF7L2's level | lines that do not express SLC52A3 (26) vs lines expressing it (24) | 2.14× lower at baseline in the lines without SLC52A3 | 0.017 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, CLDN7 |
| [[PDE9A]] | B | PDE9A activity raises TCF7L2's level | lines that do not express PDE9A (16) vs lines expressing it (34) | 1.97× lower at baseline in the lines without PDE9A | 0.017 | ⚠ within organs, on part of the lines; also absent: NRARP, FBXO2, ENSG00000267748 |
| [[CYP3A5]] | B | CYP3A5 activity raises TCF7L2's level | lines that do not express CYP3A5 (32) vs lines expressing it (18) | 2.34× lower at baseline in the lines without CYP3A5 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HHLA2, GCNT3, HNF4A |
| [[ITGB4]] | B | ITGB4 activity raises TCF7L2's level | lines that do not express ITGB4 (25) vs lines expressing it (25) | 2.26× lower at baseline in the lines without ITGB4 | 0.024 | ⚠ within organs, on part of the lines; also absent: SCNN1A, AREG, GJB3 |
| [[TNFRSF6B]] | B | TNFRSF6B activity raises TCF7L2's level | lines that do not express TNFRSF6B (33) vs lines expressing it (17) | 1.69× lower at baseline in the lines without TNFRSF6B | 0.026 | ⚠ within organs, on part of the lines; also absent: WFDC2, GABRP, FGF19 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 097]] — estrogen response early; 48 genes; every member is in the + arm (projection on the module's main direction 0.396). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (11.3, 47.2); signed map (10.6, 32.2). **Vector** length 133, 45.9% of its response variance represented; |z| ≥ 3 in 1,768 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.0 | +8.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.6 | +10.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | +6.6 | +3.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.6 | +8.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | +5.5 | +3.9 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.7 | +0.9 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.5 | +0.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.5 | +0.8 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +2.3 | +2.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -10.8 | -12.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -7.3 | -8.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -7.0 | -7.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -6.8 | -7.7 |
|  | [[EX229 (drug)]] 5 µM |  | -6.7 | -6.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.6 | -9.4 |

## What is on record

|  |  |
|---|---|
| Name | transcription factor 7 like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q25.2-q25.3 — chr10:112,950,247-113,167,678 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TCF-4; previously TCF4 |
| Gene groups (HGNC) | TCF/LEF transcription factor family; Wnt enhanceosome complex |
| Hallmark sets | NOTCH_SIGNALING |
| Reactome | 28 pathways, smallest: Signaling by TCF7L2 mutants; RUNX3 regulates WNT signaling; Binding of TCF/LEF:CTNNB1 to target gene promoters |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQB0](https://www.uniprot.org/uniprotkb/Q9NQB0) (Transcription factor 7-like 2):

> Participates in the Wnt signaling pathway and modulates MYC expression by binding to its promoter in a sequence-specific manner. Acts as a repressor in the absence of CTNNB1, and as activator in its presence. Activates transcription from promoters with several copies of the Tcf motif 5'-CCTTTGATC-3' in the presence of CTNNB1. TLE1, TLE2, TLE3 and TLE4 repress transactivation mediated by TCF7L2/TCF4 and CTNNB1. Expression of dominant-negative mutants results in cell-cycle arrest in G1. Necessary …

**Summary**, from NCBI Gene [6934](https://www.ncbi.nlm.nih.gov/gene/6934):

> This gene encodes a high mobility group (HMG) box-containing transcription factor that plays a key role in the Wnt signaling pathway. The protein has been implicated in blood glucose homeostasis. Genetic variants of this gene are associated with increased risk of type 2 diabetes. Several transcript variants encoding multiple different isoforms have been found for this gene.[provided by RefSeq, Oct 2010]

**Accessions** — [HGNC:11641](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11641) · Entrez [6934](https://www.ncbi.nlm.nih.gov/gene/6934) · UniProt [Q9NQB0](https://www.uniprot.org/uniprotkb/Q9NQB0) · Ensembl [ENSG00000148737](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148737)

## Data

Gene col 7312: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7312); `tables/drug_effects.parquet` (62 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7312, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7312]; `tensor/DDL_lfc|DDL_z.npy` [7312]; `embed/gene_vectors.npy` [7312]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7312 or target_col == 7312). Every well: [[TCF7L2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TCF7L2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
