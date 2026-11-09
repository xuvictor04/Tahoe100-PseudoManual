---
symbol: "RICTOR"
type: "gene"
col: 8929
ensembl_id: "ENSG00000164327"
name: "RPTOR independent companion of MTOR complex 2"
location: "5p13.1"
module: 69
arm: "+"
pooled_cpm: 441.13
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 23
n_dd_up_clean: 8
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# RICTOR

*RPTOR independent companion of MTOR complex 2* — 5p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.99× (z +14.3, q 2e-43, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (13 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.383× (z -20.0, q 0e+00, down in 48 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.543× (z -12.7, q 8e-35, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (84 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 16 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM50A]] (+0.68, fdr 1e-05), [[WDR48]] (+0.65, fdr 3e-04), [[UBXN7]] (+0.62, fdr 6e-05); moves opposite to [[ZNF587]] (-0.53, fdr 3e-04), [[LRRC59]] (-0.52, fdr 2e-04), [[ZNF202]] (-0.50, fdr 3e-05).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SMAD3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8929.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.99×** | +14.3 | 2e-43 | 47/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.90×** | +13.4 | 3e-38 | 45/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.59×** | +9.7 | 7e-20 | 41/48 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.54×** | +9.0 | 2e-17 | 39/48 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.24×** | +8.1 | 4e-14 | 46/48 (COLO 205, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.82×** | +6.0 | 2e-07 | 37/49 (HT-29, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.25×** | +4.4 | 8e-04 | 29/48 (BT-474, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.24×** | +4.3 | 0.001 | 28/47 (NCI-H460, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.52×** | +4.2 | 0.002 | 35/48 (Panc 03.27, BT-474, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.7 | 0.013 | 23/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.3 | 0.043 | 20/47 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.17× | +3.1 | 0.078 | 19/47 (SW480, C32, …) | inconsistent across doses |  |
| [[crizotinib (drug)]] 5 µM |  | 1.17× | +3.1 | 0.091 | 15/48 (NCI-H1573, Hs 766T, …) | top dose only |  |
| [[Sapanisertib (drug)]] 5 µM |  | **1.35×** | +3.1 | 0.091 | 25/49 (NCI-H23, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 16 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8929.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.383×** | -20.0 | 0e+00 | 48/48 (MIA PaCa-2, NCI-H2347, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.379×** | -19.9 | 0e+00 | 46/49 (NCI-H2347, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.395×** | -18.6 | 0e+00 | 42/44 (A-427, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.543×** | -12.7 | 8e-35 | 44/48 (SNU-423, LoVo, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.550×** | -12.0 | 6e-31 | 45/47 (CFPAC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.547×** | -11.6 | 4e-29 | 39/45 (NCI-H2347, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.323×** | -11.4 | 4e-28 | 48/48 (Panc 03.27, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.610×** | -10.3 | 5e-23 | 42/48 (A549, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.382×** | -9.7 | 2e-20 | 46/48 (MIA PaCa-2, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.632×** | -9.6 | 7e-20 | 43/48 (A549, AsPC-1, …) | all doses, stronger at high dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.390×** | -9.5 | 1e-19 | 45/48 (AsPC-1, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.394×** | -9.4 | 3e-19 | 46/48 (NCI-H2347, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.457×** | -7.9 | 1e-13 | 45/48 (NCI-H2347, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.775×** | -7.5 | 2e-12 | 30/49 (A549, NCI-H1792, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.715×** | -7.0 | 1e-10 | 35/48 (A549, AsPC-1, …) | rises with dose |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.691×** | -5.5 | 1e-06 | 41/49 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.721×** | -4.9 | 4e-05 | 33/48 (MIA PaCa-2, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.724×** | -4.8 | 5e-05 | 37/48 (MIA PaCa-2, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.888× | -3.4 | 0.016 | 12/49 (AsPC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.876× | -3.3 | 0.019 | 16/48 (NCI-H1573, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | 0.848× | -3.2 | 0.025 | 18/48 (LoVo, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.729×** | -3.2 | 0.030 | 24/47 (MIA PaCa-2, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.869× | -2.9 | 0.071 | 21/48 (NCI-H1573, HS-578T, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | 0.872× | -2.8 | 0.091 | 19/48 (NCI-H1573, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8929. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 882 | 4 (1 ⚠) | 16 (9 ⚠) | [[Digitoxin (drug)]] 5 µM 4.99× (z +19.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.27× (z +17.2) | [[Dinaciclib (drug)]] 5 µM 0.109× (z -25.5) ⚠ toxic; transcription drop · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.400× (z -10.6) |
| [[NCI-H460 (line)]] | wt | 364 | 8 (4 ⚠) | 9 (5 ⚠) | [[Digitoxin (drug)]] 5 µM 3.10× (z +16.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.81× (z +15.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.225× (z -22.4) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.475× (z -11.2) |
| [[NCI-H2347 (line)]] | alt | 589 | 1 | 15 (9 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.96× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.212× (z -24.1) ⚠ toxic; transcription drop · without an alert: [[Abemaciclib (drug)]] 5 µM 0.249× (z -10.9) |
| [[SW480 (line)]] | alt | 399 | 7 (2 ⚠) | 8 (7 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.79× (z +15.2) | [[Dinaciclib (drug)]] 0.5 µM 0.367× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.516× (z -9.8) |
| [[AsPC-1 (line)]] | alt | 878 | 0 | 14 (8 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.244× (z -20.0) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.210× (z -10.7) |
| [[NCI-H1792 (line)]] | alt | 1,174 | 2 (1 ⚠) | 12 (9 ⚠) | [[Digitoxin (drug)]] 5 µM 2.27× (z +10.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.21× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.126× (z -24.5) ⚠ toxic; transcription drop · without an alert: [[c-Kit-IN-1 (drug)]] 5 µM 0.213× (z -9.2) |
| [[SW1417 (line)]] | alt | 362 | 2 (1 ⚠) | 11 (8 ⚠) | [[Digitoxin (drug)]] 5 µM 2.23× (z +12.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +12.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.267× (z -20.9) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.277× (z -9.8) |
| [[HOP62 (line)]] | alt | 438 | 4 (1 ⚠) | 8 (7 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.69× (z +12.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.274× (z -16.1) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.348× (z -13.2) |
| [[Panc 03.27 (line)]] | alt | 569 | 1 | 11 (8 ⚠) | [[TAK-901 (drug)]] 0.05 µM 1.87× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.283× (z -18.5) ⚠ toxic; transcription drop · without an alert: [[TAK-733 (drug)]] 5 µM 0.207× (z -11.3) |
| [[PANC-1 (line)]] | alt | 289 | 4 (1 ⚠) | 8 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.16× (z +18.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.339× (z -17.7) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.258× (z -10.7) |
| [[SW 900 (line)]] | alt | 778 | 2 (1 ⚠) | 10 (9 ⚠) | [[Digitoxin (drug)]] 5 µM 1.93× (z +8.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.91× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.216× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.399× (z -12.0) |
| [[A549 (line)]] | wt | 658 | 0 | 11 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.187× (z -33.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Abemaciclib (drug)]] 5 µM 0.288× (z -8.5) |
| [[SNU-423 (line)]] | alt | 439 | 2 (1 ⚠) | 8 (7 ⚠) | [[Digitoxin (drug)]] 5 µM 2.02× (z +9.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.87× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.251× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.321× (z -15.7) |
| [[BT-474 (line)]] | alt | 385 | 7 (4 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 0.5 µM 3.60× (z +14.9) | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -13.2) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 862 | 1 | 8 (8 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.13× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.209× (z -19.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 349 | 3 (1 ⚠) | 6 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 5.00× (z +11.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.413× (z -13.4) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.492× (z -10.7) |
| [[J82 (line)]] | alt | 477 | 3 (1 ⚠) | 6 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.50× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.310× (z -15.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 463 | 1 (1 ⚠) | 7 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.297× (z -17.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 462 | 0 | 8 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.275× (z -19.2) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 330 | 4 (1 ⚠) | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.52× (z +12.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.313× (z -15.4) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.426× (z -11.3) |
| [[hTERT-HPNE (line)]] | wt | 432 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.260× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.392× (z -10.7) |
| [[LoVo (line)]] | wt | 287 | 3 (2 ⚠) | 5 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.12× (z +12.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.386× (z -16.2) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.446× (z -13.7) |
| [[A-172 (line)]] | wt | 313 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.379× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.467× (z -10.7) |
| [[HS-578T (line)]] | alt | 585 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.276× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.395× (z -13.2) |
| [[LOX-IMVI (line)]] | wt | 365 | 1 | 6 (6 ⚠) | [[TAK-901 (drug)]] 0.05 µM 1.96× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.330× (z -14.4) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 693 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[TAK-733 (drug)]] 5 µM 0.225× (z -8.8) |
| [[SHP-77 (line)]] | alt | 407 | 2 (1 ⚠) | 5 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.12× (z +11.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.362× (z -15.2) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.277× (z -9.3) |
| [[RPMI-7951 (line)]] | alt | 387 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.392× (z -12.4) |
| [[C32 (line)]] | wt | 324 | 2 | 3 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.23× (z +9.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.329× (z -13.7) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.407× (z -11.1) |
| [[COLO 205 (line)]] | alt | 294 | 4 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.94× (z +15.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.531× (z -9.1) ⚠ unreliable plate only |
| [[KATO III (line)]] | alt | 190 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.81× (z +14.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.415× (z -12.6) ⚠ unreliable plate only |
| [[MIA PaCa-2 (line)]] | alt | 202 | 0 | 5 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.220× (z -24.1) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.428× (z -13.5) |
| [[NCI-H23 (line)]] | alt | 670 | 1 (1 ⚠) | 4 (3 ⚠) | [[Digitoxin (drug)]] 5 µM 1.88× (z +8.8) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 5 µM 0.277× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.439× (z -11.5) |
| [[A-427 (line)]] | wt | 284 | 1 (1 ⚠) | 3 (3 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +8.9) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.149× (z -27.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 218 | 0 | 4 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.292× (z -18.4) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.478× (z -11.0) |
| [[HepG2_C3A (line)]] | wt | 325 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.342× (z -12.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 340 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.352× (z -14.7) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.498× (z -9.8) |
| [[SK-MEL-2 (line)]] | alt | 173 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.476× (z -9.7) |
| [[SW 1088 (line)]] | alt | 527 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0973× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[TAK-733 (drug)]] 5 µM 0.0537× (z -9.4) |
| [[HCT15 (line)]] | alt | 264 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.399× (z -11.4) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.503× (z -8.5) |
| [[LS 180 (line)]] | wt | 220 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.65× (z +11.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.65× (z +11.7) | — |
| [[SNU-1 (line)]] | wt | 244 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.391× (z -9.7) ⚠ toxic |
| [[SW48 (line)]] | wt | 269 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.59× (z +9.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.162× (z -17.7) ⚠ unreliable plate only |
| [[C-33 A (line)]] | alt | 182 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.465× (z -8.8) ⚠ unreliable plate only |
| [[CHP-212 (line)]] | wt | 192 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.310× (z -8.9) ⚠ unreliable plate only |
| [[SW 1271 (line)]] | alt | 372 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.173× (z -13.1) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 303 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 582 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 476 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 292 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8929), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 15 of them with an alert (⚠; 15 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM50A]] | +0.68 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[WDR48]] | +0.65 | +0.27 / +0.75 | both halves | 3e-04 |  |
| [[UBXN7]] | +0.62 | +0.38 / +0.68 | both halves | 6e-05 |  |
| [[FBXL20]] | +0.62 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[HBP1]] | +0.62 | +0.44 / +0.73 | both halves | 3e-05 |  |
| [[PABIR3]] | +0.61 | +0.37 / +0.64 | both halves | 8e-05 |  |
| [[CREBRF]] | +0.59 | +0.17 / +0.73 | ⚠ one half (not replicated) | 0.001 |  |
| [[RB1CC1]] | +0.59 | +0.32 / +0.62 | both halves | 2e-04 | STRING 509 |
| [[SERINC1]] | +0.57 | +0.37 / +0.66 | both halves | 9e-05 |  |
| [[KDM6A]] | +0.57 | +0.32 / +0.70 | both halves | 2e-04 |  |
| [[TMEM59]] | +0.56 | +0.41 / +0.63 | both halves | 4e-05 |  |
| [[CCDC28A]] | +0.56 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[NEK7]] | +0.56 | +0.39 / +0.67 | both halves | 5e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF587]] | -0.53 | -0.27 / -0.52 | both halves | 3e-04 |  |
| [[LRRC59]] | -0.52 | -0.30 / -0.46 | both halves | 2e-04 |  |
| [[ZNF202]] | -0.50 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[GCN1]] | -0.50 | -0.32 / -0.41 | both halves | 2e-04 |  |
| [[TXLNA]] | -0.49 | -0.29 / -0.46 | both halves | 2e-04 |  |
| [[CLUH]] | -0.46 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[ZNG1E]] | -0.46 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[ZNF587B]] | -0.46 | -0.19 / -0.40 | ⚠ not reproduced | 8e-04 |  |
| [[TSR1]] | -0.46 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[TCERG1]] | -0.46 | -0.37 / -0.35 | both halves | 1e-04 |  |
| [[AFG3L2]] | -0.46 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[GTPBP4]] | -0.45 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[DHX37]] | -0.45 | -0.51 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMAD3]] | B | SMAD3 activity raises RICTOR's level | lines that do not express SMAD3 (6) vs lines expressing it (44) | 1.33× lower at baseline in the lines without SMAD3 | 0.054 | ⚠ within organs, on part of the lines; also absent: ITGA3, NIBAN2, IER3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.632). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (0.5, -44.0); signed map (-14.9, 10.6). **Vector** length 109, 47.8% of its response variance represented; |z| ≥ 3 in 1,950 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.0 | -1.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.4 | -2.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | +5.2 | -2.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.1 | -19.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | -18.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | -2.0 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.9 | +1.2 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +2.7 | +1.0 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.6 | +1.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -18.1 | -20.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -11.3 | -11.4 |
|  | [[venetoclax (drug)]] 5 µM |  | -10.6 | -9.5 |
|  | [[EX229 (drug)]] 5 µM |  | -10.3 | -7.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -10.3 | -9.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -10.1 | -9.4 |

## What is on record

|  |  |
|---|---|
| Name | RPTOR independent companion of MTOR complex 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p13.1 — chr5:38,937,920-39,074,402 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC39830, AVO3, PIA, KIAA1999 |
| Gene groups (HGNC) | MTOR complex 2; Armadillo like helical domain containing |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 25 pathways, smallest: Dengue virus modulates apoptosis; CD28 dependent PI3K/Akt signaling; Constitutive Signaling by AKT1 E17K in Cancer |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6R327](https://www.uniprot.org/uniprotkb/Q6R327) (Rapamycin-insensitive companion of mTOR):

> Component of the mechanistic target of rapamycin complex 2 (mTORC2), which transduces signals from growth factors to pathways involved in proliferation, cytoskeletal organization, lipogenesis and anabolic output. In response to growth factors, mTORC2 phosphorylates and activates AGC protein kinase family members, including AKT (AKT1, AKT2 and AKT3), PKC (PRKCA, PRKCB and PRKCE) and SGK1. In contrast to mTORC1, mTORC2 is nutrient-insensitive. Within the mTORC2 complex, RICTOR probably acts as a …

**Summary**, from NCBI Gene [253260](https://www.ncbi.nlm.nih.gov/gene/253260):

> RICTOR and MTOR (FRAP1; MIM 601231) are components of a protein complex that integrates nutrient- and growth factor-derived signals to regulate cell growth (Sarbassov et al., 2004 [PubMed 15268862]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:28611](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28611) · Entrez [253260](https://www.ncbi.nlm.nih.gov/gene/253260) · UniProt [Q6R327](https://www.uniprot.org/uniprotkb/Q6R327) · Ensembl [ENSG00000164327](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164327)

## Data

Gene col 8929: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8929); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8929, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8929]; `tensor/DDL_lfc|DDL_z.npy` [8929]; `embed/gene_vectors.npy` [8929]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8929 or target_col == 8929). Every well: [[RICTOR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RICTOR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
