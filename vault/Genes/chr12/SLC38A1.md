---
symbol: "SLC38A1"
type: "gene"
col: 3229
ensembl_id: "ENSG00000111371"
name: "solute carrier family 38 member 1"
location: "12q13.11"
module: 133
arm: "+"
pooled_cpm: 284.63
n_lines_expressing: 47
n_dd_up: 34
n_dd_down: 12
n_dd_up_clean: 26
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 4
tags: ["gene", "module/133"]
generated_by: "tahoemap"
---

# SLC38A1

*solute carrier family 38 member 1* — 12q13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (8 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.87× (z +14.4, q 5e-44, up in 42 of 45 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.81× (z +13.6, q 6e-40, up in 41 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.268× (z -30.4, q 0e+00, down in 43 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC7A1]] (+0.67, fdr 7e-06), [[YARS1]] (+0.66, fdr 7e-06), [[MOCOS]] (+0.65, fdr 7e-06); moves opposite to [[IL10RB]] (-0.58, fdr 1e-05), [[RNF114]] (-0.57, fdr 3e-05), [[SSBP3]] (-0.56, fdr 2e-05).
> It is in [[Module 133]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 4 go from it, the strongest it → [[NCR3LG1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 53 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3229.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.87×** | +14.4 | 5e-44 | 42/45 (NCI-H460, PANC-1, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **1.81×** | +13.6 | 6e-40 | 41/45 (NCI-H460, A-172, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +12.9 | 7e-36 | 41/44 (COLO 205, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.56×** | +10.1 | 5e-22 | 33/46 (NCI-H1792, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.50×** | +8.6 | 8e-16 | 26/42 (LOX-IMVI, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.44×** | +8.4 | 4e-15 | 32/45 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.30×** | +8.4 | 4e-15 | 29/45 (NCI-H460, NCI-H2030, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.44×** | +8.4 | 5e-15 | 37/45 (NCI-H2030, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +7.6 | 2e-12 | 26/41 (NCI-H1573, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.38×** | +7.4 | 7e-12 | 36/45 (Panc 03.27, C-33 A, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.25×** | +7.2 | 3e-11 | 29/45 (HEC-1-A, KATO III, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.24×** | +6.9 | 2e-10 | 24/46 (NCI-H23, COLO 205, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.34×** | +6.8 | 6e-10 | 28/45 (COLO 205, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.78×** | +6.2 | 3e-08 | 34/45 (NCI-H460, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.31×** | +6.1 | 3e-08 | 33/44 (Hs 766T, HS-578T, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.29×** | +5.8 | 2e-07 | 25/45 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.70×** | +5.7 | 4e-07 | 33/45 (NCI-H460, SW 900, …) | all doses, flat | noisy plate (z scaled) |
| [[Artesunate (drug)]] 0.5 µM |  | **1.28×** | +5.6 | 5e-07 | 31/45 (HEC-1-A, SW48, …) | rises with dose |  |
| [[Neratinib (drug)]] 5 µM |  | **1.27×** | +5.4 | 2e-06 | 23/45 (NCI-H460, NCI-H23, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.65×** | +5.4 | 2e-06 | 30/45 (SW480, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 1.17× | +5.2 | 5e-06 | 21/46 (Hs 766T, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3229.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.268×** | -30.4 | 0e+00 | 43/45 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.270×** | -30.2 | 0e+00 | 45/45 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.343×** | -24.7 | 0e+00 | 44/45 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.595×** | -17.0 | 0e+00 | 38/45 (PANC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.678×** | -9.0 | 3e-17 | 38/45 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.700×** | -8.0 | 2e-13 | 31/45 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.790×** | -5.5 | 3e-06 | 29/45 (HEC-1-A, SW1417, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~18% of this change | **0.784×** | -5.4 | 4e-06 | 28/44 (HT-29, HEC-1-A, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.811×** | -4.9 | 7e-05 | 23/46 (AsPC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.650×** | -4.7 | 2e-04 | 27/46 (PANC-1, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.817×** | -4.5 | 3e-04 | 23/45 (AsPC-1, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.883× | -4.1 | 0.002 | 20/45 (HEC-1-A, KATO III, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.835× | -4.0 | 0.002 | 21/44 (AsPC-1, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.871× | -3.9 | 0.004 | 19/45 (AsPC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.892× | -3.7 | 0.008 | 16/45 (SK-MEL-2, AsPC-1, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.856× | -3.6 | 0.011 | 20/46 (MIA PaCa-2, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.860× | -3.5 | 0.015 | 18/44 (AsPC-1, SK-MEL-2, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3229. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 323 | 1 (1 ⚠) | 10 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.20× (z +8.7) ⚠ unreliable plate only | [[Panobinostat (drug)]] 5 µM 0.152× (z -20.8) |
| [[HEC-1-A (line)]] | alt | 398 | 2 (2 ⚠) | 9 (3 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.06× (z +10.8) ⚠ toxic | [[Panobinostat (drug)]] 0.5 µM 0.164× (z -28.4) |
| [[NCI-H460 (line)]] | wt | 262 | 8 (4 ⚠) | 3 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.10× (z +15.9) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 2.84× (z +14.7) | [[Panobinostat (drug)]] 5 µM 0.237× (z -20.3) |
| [[Panc 03.27 (line)]] | alt | 285 | 7 (5 ⚠) | 4 | [[Niclosamide (olamine) (drug)]] 5 µM 2.22× (z +10.9) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 2.13× (z +10.8) | [[Panobinostat (drug)]] 5 µM 0.204× (z -22.7) |
| [[SW1417 (line)]] | alt | 301 | 3 (2 ⚠) | 7 | [[Dinaciclib (drug)]] 0.5 µM 1.93× (z +9.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 1.75× (z +8.5) | [[Panobinostat (drug)]] 0.5 µM 0.239× (z -21.8) |
| [[HT-29 (line)]] | alt | 367 | 2 (1 ⚠) | 7 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.31× (z +11.7) | [[Panobinostat (drug)]] 5 µM 0.173× (z -24.5) |
| [[KATO III (line)]] | alt | 418 | 0 | 9 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.139× (z -29.5) |
| [[COLO 205 (line)]] | alt | 231 | 4 (3 ⚠) | 4 | [[Niclosamide (olamine) (drug)]] 5 µM 3.71× (z +13.9) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.27× (z +9.0) | [[Panobinostat (drug)]] 5 µM 0.268× (z -14.6) |
| [[Hs 766T (line)]] | wt | 200 | 5 (3 ⚠) | 3 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.05× (z +12.0) | [[Panobinostat (drug)]] 5 µM 0.225× (z -17.8) |
| [[MIA PaCa-2 (line)]] | alt | 271 | 2 (1 ⚠) | 6 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.14× (z +9.9) | [[Panobinostat (drug)]] 5 µM 0.165× (z -23.7) |
| [[PANC-1 (line)]] | alt | 329 | 1 (1 ⚠) | 7 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.11× (z +12.0) ⚠ unreliable plate only | [[Panobinostat (drug)]] 5 µM 0.155× (z -30.3) |
| [[SW480 (line)]] | alt | 476 | 3 (2 ⚠) | 5 | [[Niclosamide (olamine) (drug)]] 5 µM 2.22× (z +12.8) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 2.07× (z +12.1) | [[Panobinostat (drug)]] 5 µM 0.135× (z -33.7) |
| [[A498 (line)]] | wt | 358 | 2 (1 ⚠) | 5 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.05× (z +10.2) | [[Panobinostat (drug)]] 5 µM 0.268× (z -19.0) |
| [[LoVo (line)]] | wt | 492 | 1 | 6 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.14× (z +10.1) | [[Panobinostat (drug)]] 5 µM 0.132× (z -26.9) |
| [[NCI-H1573 (line)]] | alt | 135 | 4 (4 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.88× (z +11.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -15.9) |
| [[NCI-H23 (line)]] | alt | 224 | 1 (1 ⚠) | 6 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.59× (z +11.0) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -23.5) |
| [[A549 (line)]] | wt | 191 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.28× (z +10.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.202× (z -19.5) |
| [[C-33 A (line)]] | alt | 141 | 3 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.04× (z +10.7) ⚠ toxic; transcription drop · without an alert: [[5-Azacytidine (drug)]] 5 µM 2.37× (z +8.7) | [[Panobinostat (drug)]] 5 µM 0.275× (z -13.0) |
| [[H4 (line)]] | wt | 385 | 3 | 3 | [[Auranofin (drug)]] 5 µM 2.25× (z +9.9) | [[Panobinostat (drug)]] 5 µM 0.290× (z -15.0) |
| [[HS-578T (line)]] | alt | 252 | 2 (1 ⚠) | 4 | [[Niclosamide (olamine) (drug)]] 5 µM 2.57× (z +12.0) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 2.00× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -17.4) |
| [[NCI-H1792 (line)]] | alt | 131 | 5 (5 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.54× (z +13.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.424× (z -9.1) |
| [[RKO (line)]] | wt | 589 | 2 (1 ⚠) | 4 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 1.85× (z +9.5) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 1.74× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.262× (z -21.6) |
| [[SNU-423 (line)]] | alt | 247 | 2 (1 ⚠) | 4 | [[Auranofin (drug)]] 5 µM 2.16× (z +10.3) | [[Panobinostat (drug)]] 5 µM 0.213× (z -20.9) |
| [[SW 900 (line)]] | alt | 248 | 3 (2 ⚠) | 3 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.56× (z +11.1) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 2.25× (z +9.6) | [[Panobinostat (drug)]] 0.5 µM 0.326× (z -13.4) |
| [[SW48 (line)]] | wt | 373 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.169× (z -20.1) |
| [[HepG2_C3A (line)]] | wt | 279 | 1 | 4 | [[Auranofin (drug)]] 5 µM 2.44× (z +10.8) | [[Panobinostat (drug)]] 0.5 µM 0.235× (z -17.5) |
| [[J82 (line)]] | alt | 372 | 2 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 0.5 µM 1.75× (z +9.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.66× (z +8.7) | [[Panobinostat (drug)]] 5 µM 0.284× (z -21.6) |
| [[LOX-IMVI (line)]] | wt | 83.3 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +9.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.364× (z -10.2) |
| [[LS 180 (line)]] | wt | 337 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.174× (z -23.0) |
| [[NCI-H2347 (line)]] | alt | 250 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.304× (z -14.6) |
| [[A-172 (line)]] | wt | 260 | 1 | 3 | [[Auranofin (drug)]] 5 µM 2.75× (z +13.1) | [[Panobinostat (drug)]] 5 µM 0.204× (z -20.7) |
| [[A-427 (line)]] | wt | 431 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.185× (z -23.7) |
| [[BT-474 (line)]] | alt | 339 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.270× (z -18.5) |
| [[CFPAC-1 (line)]] | alt | 229 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.245× (z -17.7) |
| [[HCT15 (line)]] | alt | 338 | 1 (1 ⚠) | 3 | [[Niclosamide (olamine) (drug)]] 5 µM 2.53× (z +11.1) ⚠ toxic | [[Panobinostat (drug)]] 5 µM 0.279× (z -15.9) |
| [[NCI-H2030 (line)]] | alt | 256 | 1 (1 ⚠) | 3 | [[c-Kit-IN-1 (drug)]] 0.05 µM 1.88× (z +8.8) ⚠ unreliable plate only | [[Panobinostat (drug)]] 5 µM 0.384× (z -13.4) |
| [[SHP-77 (line)]] | alt | 347 | 1 (1 ⚠) | 3 | [[Niclosamide (olamine) (drug)]] 5 µM 2.05× (z +11.1) ⚠ toxic | [[Panobinostat (drug)]] 5 µM 0.180× (z -27.5) |
| [[AN3 CA (line)]] | alt | 277 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.259× (z -11.9) |
| [[CHP-212 (line)]] | wt | 455 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.151× (z -17.6) |
| [[SK-MEL-2 (line)]] | alt | 75.7 | 0 | 2 | — | [[Trametinib (drug)]] 0.05 µM 0.408× (z -8.9) |
| [[SW 1271 (line)]] | alt | 350 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.226× (z -10.0) |
| [[C32 (line)]] | wt | 66.3 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 66.7 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 74.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 207 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 260 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 265 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 85.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.4 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 120 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3229), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC7A1]] | +0.67 | +0.66 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 566 |
| [[YARS1]] | +0.66 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[MOCOS]] | +0.65 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[NARS1]] | +0.65 | +0.57 / +0.68 | both halves | 9e-06 |  |
| [[PRNP]] | +0.64 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[IARS1]] | +0.64 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[PSAT1]] | +0.62 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[LARS1]] | +0.61 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[KCTD15]] | +0.61 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[KLHDC4]] | +0.61 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[GART]] | +0.60 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[TARS1]] | +0.60 | +0.54 / +0.65 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IL10RB]] | -0.58 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[RNF114]] | -0.57 | -0.43 / -0.61 | both halves | 3e-05 |  |
| [[SSBP3]] | -0.56 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[IFI27L2]] | -0.55 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[MIEN1]] | -0.54 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[LCA5]] | -0.54 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[HCFC1R1]] | -0.53 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[CRY2]] | -0.53 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[RANBP10]] | -0.52 | -0.40 / -0.51 | both halves | 4e-05 |  |
| [[TMEM205]] | -0.52 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[DBP]] | -0.51 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[CCDC24]] | -0.51 | -0.31 / -0.59 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NCR3LG1]] | C | SLC38A1 activity raises NCR3LG1's level | lines that do not express SLC38A1 (3) vs lines expressing it (47) | 2.68× lower at baseline in the lines without SLC38A1 | 0.081 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ALPK3, TRIB3, SAMHD1; maybe low, not absent; its own permutation p |
| [[AP1AR]] | C | SLC38A1 activity raises AP1AR's level | lines that do not express SLC38A1 (3) vs lines expressing it (47) | 1.74× lower at baseline in the lines without SLC38A1 | 0.081 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ALPK3, TRIB3, SAMHD1; maybe low, not absent |
| [[NARS1]] | C | SLC38A1 activity raises NARS1's level | lines that do not express SLC38A1 (3) vs lines expressing it (47) | 1.49× lower at baseline in the lines without SLC38A1 | 0.081 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ALPK3, TRIB3, SAMHD1; maybe low, not absent; its own permutation p |
| [[RSL24D1]] | C | SLC38A1 activity raises RSL24D1's level | lines that do not express SLC38A1 (3) vs lines expressing it (47) | 1.25× lower at baseline in the lines without SLC38A1 | 0.081 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ALPK3, TRIB3, SAMHD1; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 133]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.604). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-17.0, 46.1); signed map (-14.4, 23.0). **Vector** length 152, 56.6% of its response variance represented; |z| ≥ 3 in 1,928 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +12.9 | +14.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +12.3 | +13.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +10.2 | +12.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +9.0 | +8.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +8.7 | +7.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +6.7 | +4.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +6.7 | +6.2 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -8.4 | -8.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.0 | -17.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.4 | -3.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -4.3 | -3.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.9 | -30.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.8 | -4.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.6 | -4.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.2 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 38 member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.11 — chr12:46,183,063-46,270,017 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ATA1, NAT2, SAT1, SNAT1 |
| Gene groups (HGNC) | Solute carrier family 38 |
| Hallmark sets | G2M_CHECKPOINT |
| Reactome | 8 pathways, smallest: Astrocytic Glutamate-Glutamine Uptake And Metabolism; Neurotransmitter uptake and metabolism In glial cells; Amino acid transport across the plasma membrane |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H2H9](https://www.uniprot.org/uniprotkb/Q9H2H9) (Sodium-coupled neutral amino acid symporter 1):

> Symporter that cotransports short-chain neutral amino acids and sodium ions from the extracellular to the intracellular side of the cell membrane. The transport is elctrogenic, pH dependent and driven by the Na(+) electrochemical gradient. Participates in the astroglia-derived glutamine transport into GABAergic interneurons for neurotransmitter GABA de novo synthesis (By similarity). May also contributes to amino acid transport in placental trophoblasts. Also regulates synaptic plasticity.

**Summary**, from NCBI Gene [81539](https://www.ncbi.nlm.nih.gov/gene/81539):

> Amino acid transporters play essential roles in the uptake of nutrients, production of energy, chemical metabolism, detoxification, and neurotransmitter cycling. SLC38A1 is an important transporter of glutamine, an intermediate in the detoxification of ammonia and the production of urea. Glutamine serves as a precursor for the synaptic transmitter, glutamate (Gu et al., 2001 [PubMed 11325958]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:13447](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13447) · Entrez [81539](https://www.ncbi.nlm.nih.gov/gene/81539) · UniProt [Q9H2H9](https://www.uniprot.org/uniprotkb/Q9H2H9) · Ensembl [ENSG00000111371](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111371)

## Data

Gene col 3229: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3229); `tables/drug_effects.parquet` (73 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3229, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3229]; `tensor/DDL_lfc|DDL_z.npy` [3229]; `embed/gene_vectors.npy` [3229]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3229 or target_col == 3229). Every well: [[SLC38A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC38A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
