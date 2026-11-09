---
symbol: "KIF5B"
type: "gene"
col: 10000
ensembl_id: "ENSG00000170759"
name: "kinesin family member 5B"
location: "10p11.22"
module: 3
arm: "-"
pooled_cpm: 357.25
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 6
n_dd_up_clean: 6
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# KIF5B

*kinesin family member 5B* — 10p11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.96× (z +19.1, q 0e+00, up in 45 of 48 measured lines) ⚠ cell-cycle shift, explains ~49% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.30× (z +5.3, q 5e-06, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.642× (z -8.8, q 5e-16, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAD21]] (+0.60, fdr 1e-05), [[HNRNPU]] (+0.59, fdr 1e-05), [[USP7]] (+0.57, fdr 2e-05); moves opposite to [[VPS37C]] (-0.56, fdr 3e-05), [[TMEM120B]] (-0.55, fdr 5e-05), [[TMEM63C]] (-0.54, fdr 3e-05).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 19 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10000.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.96×** | +19.1 | 0e+00 | 45/48 (A498, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.27×** | +16.4 | 0e+00 | 48/49 (HS-578T, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.20×** | +15.2 | 0e+00 | 42/44 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.66×** | +10.2 | 4e-22 | 46/48 (KATO III, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.64×** | +9.1 | 8e-18 | 42/45 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.56×** | +9.0 | 3e-17 | 39/48 (A498, SW480, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.47×** | +7.7 | 1e-12 | 40/48 (KATO III, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **1.42×** | +6.7 | 1e-09 | 34/47 (COLO 205, C32, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.38×** | +6.4 | 8e-09 | 37/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.37×** | +6.1 | 6e-08 | 35/48 (A498, COLO 205, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.33×** | +5.7 | 6e-07 | 36/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.30×** | +5.3 | 5e-06 | 30/48 (A498, RKO, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.63×** | +5.1 | 1e-05 | 39/49 (SW480, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.26×** | +4.6 | 1e-04 | 27/48 (RPMI-7951, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~95% of this change | **1.26×** | +4.6 | 2e-04 | 30/48 (HOP62, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.22×** | +4.0 | 0.002 | 24/48 (A498, RKO, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.21×** | +3.9 | 0.003 | 24/47 (HOP62, H4, …) | two highest doses | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +3.9 | 0.003 | 25/48 (CFPAC-1, RPMI-7951, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.38×** | +3.4 | 0.017 | 28/48 (SW48, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.12× | +3.4 | 0.019 | 9/49 (CFPAC-1, A498, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.17× | +3.2 | 0.027 | 19/48 (CFPAC-1, HOP62, …) | rises with dose |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 1.12× | +3.2 | 0.032 | 1/49 (CFPAC-1) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | 1.17× | +3.0 | 0.056 | 18/48 (Hs 766T, hTERT-HPNE, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10000.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.642×** | -8.8 | 5e-16 | 38/48 (Panc 03.27, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.686×** | -7.5 | 2e-11 | 43/48 (BT-474, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.715×** | -6.7 | 5e-09 | 34/48 (BT-474, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.815×** | -4.1 | 0.007 | 28/48 (Panc 03.27, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.762×** | -3.9 | 0.013 | 39/48 (AN3 CA, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~72% of this change | **0.827×** | -3.8 | 0.015 | 27/49 (Hs 766T, HEC-1-A, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.840× | -3.4 | 0.046 | 21/48 (HepG2/C3A, SK-MEL-2, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.951× | -3.4 | 0.053 | 0/50 | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.883× | -3.3 | 0.053 | 6/48 (NCI-H23, LS 180, …) | inconsistent across doses |  |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | 0.850× | -3.1 | 0.11 | 19/48 (RPMI-7951, KATO III, …) | rises with dose |  |
| [[Folic acid (drug)]] 5 µM |  | 0.896× | -3.1 | 0.11 | 4/48 (AsPC-1, SW48, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10000. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 316 | 8 (8 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +18.6) ⚠ cell-cycle shift, explains ~49% of this change | [[Panobinostat (drug)]] 5 µM 0.571× (z -9.1) |
| [[A498 (line)]] | wt | 239 | 9 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +23.0) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Auranofin (drug)]] 5 µM 1.90× (z +9.7) | — |
| [[NCI-H460 (line)]] | wt | 241 | 9 (9 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.03× (z +15.8) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 345 | 7 (7 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.36× (z +20.1) ⚠ cell-cycle shift, explains ~45% of this change | [[Panobinostat (drug)]] 5 µM 0.576× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 297 | 4 (4 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.50× (z +13.4) ⚠ cell-cycle shift, explains ~45% of this change | [[Panobinostat (drug)]] 5 µM 0.478× (z -10.7) |
| [[PANC-1 (line)]] | alt | 327 | 5 (5 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.03× (z +17.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.564× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 329 | 6 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +20.2) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[HS-578T (line)]] | alt | 274 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H1792 (line)]] | alt | 377 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.71× (z +17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[Panc 03.27 (line)]] | alt | 379 | 3 (3 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +14.3) ⚠ cell-cycle shift, explains ~49% of this change | [[Panobinostat (drug)]] 5 µM 0.510× (z -11.1) |
| [[COLO 205 (line)]] | alt | 169 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +19.4) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[HEC-1-A (line)]] | alt | 354 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +16.9) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[HepG2_C3A (line)]] | wt | 483 | 4 (4 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +15.7) ⚠ cell-cycle shift, explains ~49% of this change | [[Belinostat (drug)]] 5 µM 0.592× (z -8.5) |
| [[HOP62 (line)]] | alt | 306 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +19.2) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[NCI-H2347 (line)]] | alt | 312 | 4 (4 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +14.3) ⚠ cell-cycle shift, explains ~49% of this change | [[Panobinostat (drug)]] 5 µM 0.609× (z -8.9) |
| [[SW 900 (line)]] | alt | 303 | 4 (4 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +13.4) ⚠ cell-cycle shift, explains ~49% of this change | [[Panobinostat (drug)]] 5 µM 0.498× (z -9.9) |
| [[A-172 (line)]] | wt | 316 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.02× (z +16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[A549 (line)]] | wt | 371 | 3 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +18.2) ⚠ cell-cycle shift, explains ~49% of this change | [[Panobinostat (drug)]] 5 µM 0.587× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 425 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +22.1) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[BT-474 (line)]] | alt | 356 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +10.2) ⚠ cell-cycle shift, explains ~49% of this change | [[Panobinostat (drug)]] 0.5 µM 0.495× (z -10.2) |
| [[C32 (line)]] | wt | 167 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[HT-29 (line)]] | alt | 447 | 3 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +14.1) ⚠ cell-cycle shift, explains ~49% of this change | [[Panobinostat (drug)]] 5 µM 0.584× (z -8.6) |
| [[hTERT-HPNE (line)]] | wt | 316 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.41× (z +16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[LOX-IMVI (line)]] | wt | 420 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +15.5) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 352 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[RKO (line)]] | wt | 386 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +18.3) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Auranofin (drug)]] 5 µM 1.99× (z +8.9) | — |
| [[RPMI-7951 (line)]] | alt | 404 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.38× (z +14.5) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 394 | 3 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +16.7) ⚠ cell-cycle shift, explains ~49% of this change | [[Panobinostat (drug)]] 5 µM 0.571× (z -9.0) |
| [[SW48 (line)]] | wt | 379 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +10.6) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[H4 (line)]] | wt | 192 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.62× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[HCT15 (line)]] | alt | 472 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.51× (z +10.9) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 209 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[J82 (line)]] | alt | 353 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.52× (z +14.4) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 337 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +16.0) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[SNU-423 (line)]] | alt | 241 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +16.6) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[CHP-212 (line)]] | wt | 400 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +10.1) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[LoVo (line)]] | wt | 387 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.77× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[LS 180 (line)]] | wt | 624 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.07× (z +10.2) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[SHP-77 (line)]] | alt | 284 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.27× (z +11.5) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 411 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +14.0) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[A-427 (line)]] | wt | 698 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 338 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 379 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 747 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 322 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 300 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 377 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 419 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 242 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 511 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10000), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAD21]] | +0.60 | +0.54 / +0.60 | both halves | 1e-05 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[HNRNPU]] | +0.59 | +0.51 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[USP7]] | +0.57 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[TOP2B]] | +0.57 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[CPSF2]] | +0.56 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[HMMR]] | +0.55 | +0.62 / +0.45 | both halves | 3e-05 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[PSMD6-AS1]] | +0.55 | +0.42 / +0.44 | both halves | 4e-05 |  |
| [[ZFP91]] | +0.55 | +0.51 / +0.40 | both halves | 5e-05 |  |
| [[SPDL1]] | +0.54 | +0.64 / +0.40 | both halves | 5e-05 | pathway: RHO GTPase Effectors |
| [[HNRNPH3]] | +0.54 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[PAK2]] | +0.54 | +0.34 / +0.55 | both halves | 1e-04 | pathway: RHO GTPase Effectors |
| [[WNK1]] | +0.54 | +0.49 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS37C]] | -0.56 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[TMEM120B]] | -0.55 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[TMEM63C]] | -0.54 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[AP2S1]] | -0.52 | -0.46 / -0.32 | both halves | 2e-04 | pathway: MHC class II antigen presentation |
| [[CENPX]] | -0.51 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[SHQ1]] | -0.50 | -0.51 / -0.29 | both halves | 3e-04 |  |
| [[LCMT1]] | -0.50 | -0.45 / -0.31 | both halves | 2e-04 |  |
| [[UNC45A]] | -0.50 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[B3GAT3]] | -0.50 | -0.31 / -0.44 | both halves | 2e-04 |  |
| [[SDHAF1]] | -0.49 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[YIF1B]] | -0.48 | -0.36 / -0.33 | both halves | 1e-04 |  |
| [[PHAF1]] | -0.48 | -0.34 / -0.38 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises KIF5B's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.511). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-35.7, -24.7); signed map (14.6, -36.2). **Vector** length 102, 40.4% of its response variance represented; |z| ≥ 3 in 1,339 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +7.5 | +19.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +4.5 | +9.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +15.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.1 | +3.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +3.8 | +16.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.0 | +1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +2.5 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +2.3 | +0.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.0 | -0.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | -1.3 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -5.0 | -7.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.0 | -8.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.8 | -6.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.7 | -3.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.2 | -1.4 |
|  | [[Thymol (drug)]] 0.5 µM |  | -3.4 | -3.4 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -3.3 | +0.1 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -3.2 | -1.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.8 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | kinesin family member 5B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p11.22 — chr10:32,009,015-32,056,425 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KNS, uKHC; previously KNS1 |
| Gene groups (HGNC) | Kinesins |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE, G2M_CHECKPOINT, MITOTIC_SPINDLE |
| Reactome | 22 pathways, smallest: RHO GTPases activate KTN1; Insulin processing; Kinesins |
| Matched by | ensembl_id |

**Function**, from UniProt [P33176](https://www.uniprot.org/uniprotkb/P33176) (Kinesin-1 heavy chain):

> Microtubule-dependent motor required for normal distribution of mitochondria and lysosomes. Can induce formation of neurite-like membrane protrusions in non-neuronal cells in a ZFYVE27-dependent manner (By similarity). Regulates centrosome and nuclear positioning during mitotic entry. During the G2 phase of the cell cycle in a BICD2-dependent manner, antagonizes dynein function and drives the separation of nuclei and centrosomes. Required for anterograde axonal transportation of MAPK8IP3/JIP3 …

**Summary**, from NCBI Gene [3799](https://www.ncbi.nlm.nih.gov/gene/3799):

> Enables identical protein binding activity; microtubule binding activity; and microtubule motor activity. Involved in several processes, including natural killer cell mediated cytotoxicity; positive regulation of potassium ion transport; and positive regulation of protein localization to plasma membrane. Located in cytosol and vesicle. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:6324](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6324) · Entrez [3799](https://www.ncbi.nlm.nih.gov/gene/3799) · UniProt [P33176](https://www.uniprot.org/uniprotkb/P33176) · Ensembl [ENSG00000170759](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170759)

## Data

Gene col 10000: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10000); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10000, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10000]; `tensor/DDL_lfc|DDL_z.npy` [10000]; `embed/gene_vectors.npy` [10000]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10000 or target_col == 10000). Every well: [[KIF5B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KIF5B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
