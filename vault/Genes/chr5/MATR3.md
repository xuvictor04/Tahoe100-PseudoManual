---
symbol: "MATR3"
type: "gene"
col: 295
ensembl_id: "ENSG00000015479"
name: "matrin 3"
location: "5q31.2"
module: 3
arm: "-"
pooled_cpm: 382.36
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 7
n_dd_up_clean: 13
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# MATR3

*matrin 3* — 5q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.08× (z +19.7, q 0e+00, up in 45 of 48 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.00× (z +13.1, q 7e-37, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.715× (z -6.4, q 9e-08, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF326]] (+0.67, fdr 7e-06), [[U2SURP]] (+0.66, fdr 7e-06), [[EWSR1]] (+0.65, fdr 1e-05); moves opposite to [[PLIN3]] (-0.60, fdr 1e-05), [[GBA2]] (-0.59, fdr 1e-05), [[MYO9B]] (-0.58, fdr 4e-05).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 2 go from it, the strongest it → [[PLEKHM1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 295.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.08×** | +19.7 | 0e+00 | 45/48 (COLO 205, A-172, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.00×** | +13.1 | 7e-37 | 45/48 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.96×** | +10.8 | 8e-25 | 48/49 (COLO 205, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.75×** | +10.6 | 6e-24 | 46/48 (A-427, A-172, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.76×** | +10.3 | 1e-22 | 44/48 (NCI-H460, COLO 205, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +10.1 | 4e-22 | 45/47 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.72×** | +9.9 | 3e-21 | 36/44 (NCI-H23, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.70×** | +9.9 | 4e-21 | 47/48 (SW480, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.67×** | +9.6 | 4e-20 | 43/49 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.66×** | +9.6 | 4e-20 | 40/48 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.56×** | +7.4 | 8e-12 | 38/45 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.43×** | +6.7 | 8e-10 | 36/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.41×** | +6.5 | 3e-09 | 43/48 (PANC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.41×** | +6.5 | 3e-09 | 37/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.70×** | +5.3 | 5e-06 | 41/45 (Hs 766T, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +5.3 | 5e-06 | 38/48 (PANC-1, KATO III, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.25×** | +4.2 | 9e-04 | 25/48 (SW480, BT-474, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.42×** | +3.5 | 0.012 | 28/49 (Panc 03.27, C-33 A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.21×** | +3.4 | 0.018 | 22/48 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.27×** | +3.2 | 0.029 | 28/49 (PANC-1, Hs 766T, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.18× | +3.0 | 0.056 | 17/49 (NCI-H460, PANC-1, …) | top dose only | plate-row cell shift; position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.35×** | +2.9 | 0.072 | 24/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 295.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.715×** | -6.4 | 9e-08 | 40/48 (PANC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.736×** | -5.8 | 1e-06 | 37/48 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.760×** | -5.2 | 3e-05 | 31/48 (SW 900, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.940× | -4.0 | 0.008 | 0/50 | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.812×** | -4.0 | 0.008 | 33/48 (SW 900, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Demeclocycline (drug)]] 5 µM |  | 0.865× | -3.9 | 0.009 | 9/48 (NCI-H661, HS-578T, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.796×** | -3.7 | 0.017 | 30/48 (SW 900, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Adenosine (drug)]] 5 µM |  | 0.874× | -3.7 | 0.018 | 7/48 (COLO 205, AsPC-1, …) | top dose only | position effect removed |
| [[Posaconazole (drug)]] 5 µM |  | **0.827×** | -3.5 | 0.031 | 26/48 (AsPC-1, HEC-1-A, …) | top dose only | plate-row cell shift |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.845× | -3.2 | 0.075 | 21/48 (CHP-212, SNU-1, …) | inconsistent across doses | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.796×** | -3.1 | 0.096 | 24/48 (AN3 CA, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.851× | -3.1 | 0.099 | 14/48 (HEC-1-A, AsPC-1, …) | top dose only |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.853× | -3.0 | 0.11 | 14/48 (NCI-H1573, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 295. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 401 | 15 (9 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.77× (z +20.0) | — |
| [[PANC-1 (line)]] | alt | 385 | 13 (6 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.64× (z +19.3) | [[Panobinostat (drug)]] 0.5 µM 0.527× (z -9.6) |
| [[LoVo (line)]] | wt | 412 | 10 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +16.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +14.1) | — |
| [[SW480 (line)]] | alt | 433 | 10 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.42× (z +15.8) | — |
| [[NCI-H1792 (line)]] | alt | 257 | 9 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +15.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.96× (z +12.6) | — |
| [[NCI-H23 (line)]] | alt | 393 | 7 (5 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.45× (z +14.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.82× (z +9.8) | [[Panobinostat (drug)]] 5 µM 0.591× (z -8.7) |
| [[HOP62 (line)]] | alt | 364 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +16.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +12.6) | — |
| [[KATO III (line)]] | alt | 243 | 8 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.70× (z +20.5) | — |
| [[LOX-IMVI (line)]] | wt | 350 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +12.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.44× (z +11.6) | — |
| [[NCI-H1573 (line)]] | alt | 290 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +17.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.11× (z +15.7) | — |
| [[BT-474 (line)]] | alt | 320 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +13.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.15× (z +10.7) | — |
| [[COLO 205 (line)]] | alt | 298 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +23.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.34× (z +15.4) | — |
| [[HT-29 (line)]] | alt | 298 | 7 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +16.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.99× (z +10.5) | — |
| [[LS 180 (line)]] | wt | 340 | 7 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.90× (z +19.9) | — |
| [[A549 (line)]] | wt | 332 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +19.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.43× (z +10.9) | — |
| [[H4 (line)]] | wt | 291 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +13.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.74× (z +11.7) | — |
| [[A-172 (line)]] | wt | 261 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +19.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.53× (z +12.8) | — |
| [[A-427 (line)]] | wt | 414 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.15× (z +13.1) | — |
| [[A498 (line)]] | wt | 296 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +15.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.04× (z +9.2) | — |
| [[HEC-1-A (line)]] | alt | 509 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +17.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.41× (z +11.6) | — |
| [[Hs 766T (line)]] | wt | 331 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +14.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.63× (z +10.2) | — |
| [[J82 (line)]] | alt | 336 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +15.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.23× (z +11.0) | — |
| [[SW 900 (line)]] | alt | 318 | 3 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +12.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.29× (z +10.7) | [[Panobinostat (drug)]] 0.5 µM 0.484× (z -9.4) |
| [[RKO (line)]] | wt | 359 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +16.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.49× (z +9.1) | — |
| [[RPMI-7951 (line)]] | alt | 306 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +16.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.25× (z +10.0) | — |
| [[AsPC-1 (line)]] | alt | 390 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +18.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.99× (z +9.4) | — |
| [[C32 (line)]] | wt | 333 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +13.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 4.51× (z +9.5) | — |
| [[hTERT-HPNE (line)]] | wt | 280 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +13.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.36× (z +10.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 501 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +10.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.01× (z +9.5) | — |
| [[Panc 03.27 (line)]] | alt | 335 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +15.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.24× (z +10.2) | — |
| [[HS-578T (line)]] | alt | 342 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +11.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.50× (z +9.3) | — |
| [[NCI-H2030 (line)]] | alt | 458 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.71× (z +11.4) | — |
| [[SHP-77 (line)]] | alt | 536 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.13× (z +10.9) | — |
| [[SK-MEL-2 (line)]] | alt | 414 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +16.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.87× (z +9.1) | — |
| [[SNU-423 (line)]] | alt | 398 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +13.1) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[SW1417 (line)]] | alt | 543 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +13.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.27× (z +10.0) | — |
| [[SW48 (line)]] | wt | 390 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.72× (z +12.2) | — |
| [[AN3 CA (line)]] | alt | 703 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.02× (z +8.6) | — |
| [[CFPAC-1 (line)]] | alt | 428 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +12.1) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[HCT15 (line)]] | alt | 522 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +11.0) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H2347 (line)]] | alt | 431 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +9.1) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[SNU-1 (line)]] | wt | 507 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.10× (z +9.3) | — |
| [[C-33 A (line)]] | alt | 514 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 438 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 422 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 365 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 422 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 456 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 454 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 511 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 295), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF326]] | +0.67 | +0.62 / +0.65 | both halves | 7e-06 | STRING 765 |
| [[U2SURP]] | +0.66 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[EWSR1]] | +0.65 | +0.53 / +0.69 | both halves | 1e-05 | STRING 591 |
| [[TOP2B]] | +0.63 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[BCLAF1]] | +0.62 | +0.57 / +0.62 | both halves | 1e-05 | STRING 675 |
| [[HNRNPU]] | +0.62 | +0.51 / +0.63 | both halves | 1e-05 | STRING 823 |
| [[NPM1]] | +0.61 | +0.68 / +0.53 | both halves | 1e-05 | STRING 508 |
| [[EIF4B]] | +0.60 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[STAG2]] | +0.60 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[SMARCE1]] | +0.59 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[HDAC2]] | +0.59 | +0.50 / +0.67 | both halves | 1e-05 |  |
| [[ZFR]] | +0.59 | +0.62 / +0.53 | both halves | 1e-05 | same gene group; STRING 537 |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLIN3]] | -0.60 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[GBA2]] | -0.59 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[MYO9B]] | -0.58 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[SLC25A44]] | -0.57 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[TMEM184B]] | -0.57 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[RABIF]] | -0.56 | -0.35 / -0.67 | both halves | 1e-04 |  |
| [[ISG20L2]] | -0.56 | -0.45 / -0.65 | both halves | 3e-05 |  |
| [[TNFAIP1]] | -0.56 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[ORAI1]] | -0.55 | -0.38 / -0.56 | both halves | 6e-05 |  |
| [[DMPK]] | -0.55 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[B3GAT3]] | -0.54 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[CDC34]] | -0.54 | -0.44 / -0.56 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises MATR3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CHASERR]] | C | CHASERR's natural level weakens MATR3's drug response | CHASERR's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.63, reverse -0.12; direction not clear | 0.063 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEKHM1]] | C | MATR3's natural level weakens PLEKHM1's drug response | MATR3's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.63, reverse +0.29; direction not clear | 0.063 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[VPS26A]] | C | MATR3's natural level weakens VPS26A's drug response | MATR3's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.61, reverse -0.31; direction not clear | 0.095 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.508). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-35.4, -25.1); signed map (13.6, -36.8). **Vector** length 102, 46.0% of its response variance represented; |z| ≥ 3 in 1,324 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.1 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.0 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.7 | +7.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +5.1 | +19.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | -0.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.8 | -0.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.6 | -1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.3 | +0.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.3 | +2.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -6.4 | +6.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -6.0 | +6.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.8 | +9.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.4 | -4.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -5.2 | +13.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.5 | -3.1 |
|  | [[Thymol (drug)]] 0.5 µM |  | -3.5 | -3.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.3 | -0.3 |
|  | [[vincristine (drug)]] 0.5 µM |  | -3.3 | -1.1 |
|  | [[vincristine (drug)]] 5 µM |  | -3.0 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | matrin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.2 — chr5:139,293,674-139,331,677 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0723, MGC9105, VCPDM; previously MPD2 |
| Gene groups (HGNC) | Zinc fingers matrin-type; Small nucleolar RNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [P43243](https://www.uniprot.org/uniprotkb/P43243) (Matrin-3):

> May play a role in transcription or may interact with other nuclear matrix proteins to form the internal fibrogranular network. In association with the SFPQ-NONO heteromer may play a role in nuclear retention of defective RNAs. Plays a role in the regulation of DNA virus-mediated innate immune response by assembling into the HDP-RNP complex, a complex that serves as a platform for IRF3 phosphorylation and subsequent innate immune response activation through the cGAS-STING pathway. Binds to …

**Summary**, from NCBI Gene [9782](https://www.ncbi.nlm.nih.gov/gene/9782):

> This gene encodes a nuclear matrix protein, which is proposed to stabilize certain messenger RNA species. Mutations of this gene are associated with distal myopathy 2, which often includes vocal cord and pharyngeal weakness. Alternatively spliced transcript variants, including read-through transcripts composed of the upstream small nucleolar RNA host gene 4 (non-protein coding) and matrin 3 gene sequence, have been identified. Pseudogenes of this gene are located on chromosomes 1 and X. …

**Accessions** — [HGNC:6912](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6912) · Entrez [9782](https://www.ncbi.nlm.nih.gov/gene/9782) · UniProt [P43243](https://www.uniprot.org/uniprotkb/P43243) · Ensembl [ENSG00000015479](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000015479)

## Data

Gene col 295: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 295); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 295, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 295]; `tensor/DDL_lfc|DDL_z.npy` [295]; `embed/gene_vectors.npy` [295]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 295 or target_col == 295). Every well: [[MATR3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MATR3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
