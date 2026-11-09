---
symbol: "KPNB1"
type: "gene"
col: 2945
ensembl_id: "ENSG00000108424"
name: "karyopherin subunit beta 1"
location: "17q21.32"
module: 6
arm: "+"
pooled_cpm: 369.98
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 13
n_dd_up_clean: 8
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# KPNB1

*karyopherin subunit beta 1* — 17q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.73× (z +17.6, q 0e+00, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.33× (z +5.1, q 5e-05, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.580× (z -13.6, q 4e-39, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDS5A]] (+0.61, fdr 1e-05), [[PTGES3]] (+0.60, fdr 1e-05), [[TCOF1]] (+0.60, fdr 1e-05); moves opposite to [[NR1D1]] (-0.61, fdr 2e-05), [[POLR1H]] (-0.57, fdr 1e-05), [[CLBA1]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TNK1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2945.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.73×** | +17.6 | 0e+00 | 49/49 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.59×** | +16.1 | 0e+00 | 44/44 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.71×** | +8.7 | 7e-16 | 42/45 (SNU-423, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **1.41×** | +5.8 | 9e-07 | 41/47 (LoVo, C32, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.33×** | +5.1 | 5e-05 | 32/48 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **1.64×** | +4.5 | 5e-04 | 40/48 (CFPAC-1, Panc 03.27, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.29×** | +4.2 | 0.002 | 32/48 (SW 900, NCI-H1792, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +4.1 | 0.003 | 35/48 (PANC-1, CFPAC-1, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.26×** | +4.1 | 0.003 | 27/48 (C32, RPMI-7951, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.25×** | +3.9 | 0.006 | 26/48 (KATO III, NCI-H460, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change | **1.24×** | +3.8 | 0.007 | 30/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.47×** | +3.5 | 0.019 | 35/48 (MIA PaCa-2, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **1.31×** | +3.4 | 0.029 | 38/49 (MIA PaCa-2, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.44×** | +3.4 | 0.029 | 33/48 (SW 900, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.41×** | +3.2 | 0.057 | 34/48 (NCI-H460, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠; shown: the 15 strongest. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2945.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.580×** | -13.6 | 4e-39 | 40/48 (MIA PaCa-2, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.575×** | -9.8 | 4e-20 | 48/48 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.575×** | -9.7 | 4e-20 | 47/48 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.701×** | -8.8 | 1e-16 | 44/48 (LS 180, RKO, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM |  | **0.671×** | -7.0 | 2e-10 | 43/48 (SK-MEL-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.681×** | -6.5 | 7e-09 | 32/48 (A-172, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.772×** | -6.5 | 8e-09 | 37/49 (CHP-212, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.903× | -6.2 | 4e-08 | 1/50 (MIA PaCa-2) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.744×** | -5.2 | 1e-05 | 38/48 (LS 180, A-172, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.782×** | -4.3 | 8e-04 | 34/48 (A498, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.660×** | -3.8 | 0.007 | 33/49 (PANC-1, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | **0.819×** | -3.5 | 0.020 | 30/48 (SW 1271, SW1417, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.823×** | -3.4 | 0.026 | 27/49 (COLO 205, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.878× | -3.2 | 0.046 | 13/48 (A498, SK-MEL-2, …) | top dose only |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | **0.832×** | -3.2 | 0.046 | 24/48 (SW 1271, HCT15, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2945. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 297 | 3 (3 ⚠) | 5 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +14.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.461× (z -15.8) |
| [[A498 (line)]] | wt | 441 | 2 (2 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +15.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.415× (z -13.9) |
| [[NCI-H460 (line)]] | wt | 379 | 3 (3 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +13.7) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.553× (z -11.2) |
| [[A-427 (line)]] | wt | 536 | 2 (2 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.43× (z +12.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.500× (z -13.9) |
| [[J82 (line)]] | alt | 516 | 2 (2 ⚠) | 5 | [[Dinaciclib (drug)]] 5 µM 2.35× (z +13.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.516× (z -15.2) |
| [[LS 180 (line)]] | wt | 244 | 3 (3 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.93× (z +13.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -18.0) |
| [[SK-MEL-2 (line)]] | alt | 454 | 2 (2 ⚠) | 5 | [[Dinaciclib (drug)]] 5 µM 2.05× (z +10.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.371× (z -14.2) |
| [[AsPC-1 (line)]] | alt | 213 | 2 (2 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.07× (z +14.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.428× (z -11.7) |
| [[NCI-H2030 (line)]] | alt | 384 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.32× (z +12.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.428× (z -12.2) |
| [[NCI-H23 (line)]] | alt | 469 | 1 (1 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +14.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.475× (z -15.1) |
| [[PANC-1 (line)]] | alt | 525 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 2.75× (z +15.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.392× (z -15.0) |
| [[SW1417 (line)]] | alt | 332 | 3 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.39× (z +13.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.620× (z -10.6) |
| [[CFPAC-1 (line)]] | alt | 361 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.43× (z +14.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.456× (z -17.9) |
| [[HEC-1-A (line)]] | alt | 331 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 1.79× (z +9.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.505× (z -10.8) |
| [[hTERT-HPNE (line)]] | wt | 349 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +13.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -15.0) |
| [[KATO III (line)]] | alt | 337 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.29× (z +17.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.584× (z -10.9) |
| [[MIA PaCa-2 (line)]] | alt | 471 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.27× (z +14.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -19.1) |
| [[SW 900 (line)]] | alt | 327 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +14.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.461× (z -10.9) |
| [[SW48 (line)]] | wt | 345 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.59× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -14.5) |
| [[C-33 A (line)]] | alt | 386 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.45× (z +10.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.559× (z -9.6) |
| [[H4 (line)]] | wt | 394 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.34× (z +14.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.469× (z -9.0) |
| [[HCT15 (line)]] | alt | 467 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +11.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -13.8) |
| [[HepG2_C3A (line)]] | wt | 287 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.48× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -15.4) |
| [[HOP62 (line)]] | alt | 415 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.48× (z +15.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.458× (z -14.2) |
| [[Hs 766T (line)]] | wt | 242 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.31× (z +14.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.531× (z -10.9) |
| [[HS-578T (line)]] | alt | 360 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.01× (z +15.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.503× (z -9.8) |
| [[LoVo (line)]] | wt | 212 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.97× (z +19.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 408 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +12.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.604× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 425 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.24× (z +17.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.452× (z -16.3) |
| [[RKO (line)]] | wt | 385 | 1 (1 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.80× (z +12.7) ⚠ toxic; transcription drop | [[Selinexor (drug)]] 5 µM 0.463× (z -13.5) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.489× (z -12.6) |
| [[SNU-423 (line)]] | alt | 357 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.55× (z +17.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.638× (z -8.7) |
| [[SW480 (line)]] | alt | 395 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.64× (z +17.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.546× (z -12.0) |
| [[A549 (line)]] | wt | 416 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +15.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.540× (z -8.5) |
| [[BT-474 (line)]] | alt | 217 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.374× (z -11.2) |
| [[C32 (line)]] | wt | 227 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +14.3) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 252 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +13.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.485× (z -11.9) |
| [[LOX-IMVI (line)]] | wt | 445 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.59× (z +13.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.602× (z -10.0) |
| [[NCI-H1573 (line)]] | alt | 258 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.58× (z +11.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -15.2) |
| [[SHP-77 (line)]] | alt | 372 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.56× (z +12.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.457× (z -10.6) |
| [[CHP-212 (line)]] | wt | 452 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -13.5) |
| [[HT-29 (line)]] | alt | 300 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.21× (z +14.2) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 295 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.44× (z +14.0) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 253 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +12.1) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 404 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.14× (z +10.9) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 387 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.572× (z -8.7) |
| [[NCI-H2122 (line)]] | alt | 279 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 314 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 433 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 225 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 310 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2945), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDS5A]] | +0.61 | +0.67 / +0.54 | both halves | 1e-05 | pathway: Mitotic Anaphase |
| [[PTGES3]] | +0.60 | +0.63 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[TCOF1]] | +0.60 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[SNRPA]] | +0.60 | +0.58 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[CCDC150]] | +0.58 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[GMPS]] | +0.58 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[PRKDC]] | +0.56 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[IMMT]] | +0.55 | +0.59 / +0.46 | both halves | 2e-05 |  |
| [[CEP78]] | +0.55 | +0.58 / +0.38 | both halves | 7e-05 |  |
| [[NUP107]] | +0.55 | +0.51 / +0.58 | both halves | 1e-05 | pathway: Antimicrobial mechanism of IFN-stimulated genes; STRING 934 |
| [[NSD2]] | +0.55 | +0.62 / +0.51 | both halves | 1e-05 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[HSPD1]] | +0.54 | +0.52 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NR1D1]] | -0.61 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[POLR1H]] | -0.57 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[CLBA1]] | -0.55 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[CLN5]] | -0.54 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[COMMD3]] | -0.54 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[NATD1]] | -0.53 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[NFKBIE]] | -0.52 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[DLX2]] | -0.52 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[FAM200B]] | -0.52 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[ETFRF1]] | -0.52 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[NINJ1]] | -0.51 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[TRIM8]] | -0.51 | -0.38 / -0.45 | both halves | 7e-05 | pathway: Interferon Signaling |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNK1]] | B | TNK1 activity lowers KPNB1's level | lines that do not express TNK1 (13) vs lines expressing it (37) | 1.18× higher at baseline in the lines without TNK1 | 0.037 | ⚠ within organs, on part of the lines; also absent: TUBA4A, CDCP1, CHMP4C; maybe low, not absent |
| [[MPZL3]] | B | MPZL3 activity lowers KPNB1's level | lines that do not express MPZL3 (25) vs lines expressing it (25) | 1.25× higher at baseline in the lines without MPZL3 | 0.050 | ⚠ within organs, on part of the lines; also absent: RNF39, MYO5B, CDH1 |
| [[MELK]] | C | MELK activity raises KPNB1's level | lines that do not express MELK (3) vs lines expressing it (47) | 1.41× lower at baseline in the lines without MELK | 0.080 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.488). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-28.7, -41.7); signed map (-33.8, -41.0). **Vector** length 94.7, 37.7% of its response variance represented; |z| ≥ 3 in 1,229 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.5 | +4.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.1 | +5.1 |
|  | [[EX229 (drug)]] 5 µM |  | +4.0 | +4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +4.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.5 | +3.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.5 | +3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.2 | +4.1 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -10.2 | -8.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.1 | -13.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.1 | -6.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -5.0 | -2.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | -4.8 | -5.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -3.6 | +1.4 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -3.0 | +1.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.8 | -1.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.6 | -0.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.5 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | karyopherin subunit beta 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.32 — chr17:47,649,476-47,685,505 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NTF97, IPOB, MGC2155, MGC2156, MGC2157, IMB1, Impnb, IPO1 |
| Gene groups (HGNC) | Armadillo repeat containing; Importins |
| Hallmark sets | G2M_CHECKPOINT, MYC_TARGETS_V1 |
| Reactome | 48 pathways, smallest: Suppression of phagosomal maturation; Apoptosis induced DNA fragmentation; Maturation of hRSV A proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14974](https://www.uniprot.org/uniprotkb/Q14974) (Importin subunit beta-1):

> Functions in nuclear protein import, either in association with an adapter protein, like an importin-alpha subunit, which binds to nuclear localization signals (NLS) in cargo substrates, or by acting as autonomous nuclear transport receptor. Acting autonomously, serves itself as NLS receptor. Docking of the importin/substrate complex to the nuclear pore complex (NPC) is mediated by KPNB1 through binding to nucleoporin FxFG repeats and the complex is subsequently translocated through the pore by …

**Summary**, from NCBI Gene [3837](https://www.ncbi.nlm.nih.gov/gene/3837):

> Nucleocytoplasmic transport, a signal- and energy-dependent process, takes place through nuclear pore complexes embedded in the nuclear envelope. The import of proteins containing a nuclear localization signal (NLS) requires the NLS import receptor, a heterodimer of importin alpha and beta subunits also known as karyopherins. Importin alpha binds the NLS-containing cargo in the cytoplasm and importin beta docks the complex at the cytoplasmic side of the nuclear pore complex. In the presence of …

**Accessions** — [HGNC:6400](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6400) · Entrez [3837](https://www.ncbi.nlm.nih.gov/gene/3837) · UniProt [Q14974](https://www.uniprot.org/uniprotkb/Q14974) · Ensembl [ENSG00000108424](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108424)

## Data

Gene col 2945: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2945); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2945, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2945]; `tensor/DDL_lfc|DDL_z.npy` [2945]; `embed/gene_vectors.npy` [2945]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2945 or target_col == 2945). Every well: [[KPNB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KPNB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
