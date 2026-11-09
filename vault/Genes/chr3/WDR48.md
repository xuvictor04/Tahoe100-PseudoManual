---
symbol: "WDR48"
type: "gene"
col: 3580
ensembl_id: "ENSG00000114742"
name: "WD repeat domain 48"
location: "3p22.2"
module: 74
arm: "+"
pooled_cpm: 74.66
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 20
n_dd_up_clean: 11
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# WDR48

*WD repeat domain 48* — 3p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.20× (z +20.8, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.313× (z -21.6, q 0e+00, down in 47 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.308× (z -11.4, q 7e-28, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RB1CC1]] (+0.74, fdr 7e-06), [[CREBRF]] (+0.74, fdr 7e-06), [[CRBN]] (+0.74, fdr 7e-06); moves opposite to [[UBE2N]] (-0.54, fdr 3e-05), [[LRRC59]] (-0.53, fdr 5e-05).
> It is in [[Module 074]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CRBN]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠; shown: the 15 strongest. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3580.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.20×** | +20.8 | 0e+00 | 46/48 (A549, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.22×** | +14.9 | 0e+00 | 42/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.93×** | +12.3 | 3e-32 | 40/48 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.69×** | +9.4 | 8e-19 | 42/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.62×** | +9.0 | 2e-17 | 40/48 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.57×** | +8.4 | 5e-15 | 36/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.18×** | +7.6 | 2e-12 | 39/49 (LoVo, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.11×** | +7.3 | 2e-11 | 36/48 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +6.2 | 3e-08 | 35/47 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.37×** | +5.8 | 3e-07 | 32/48 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.33×** | +5.3 | 5e-06 | 30/48 (HS-578T, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.28×** | +4.5 | 3e-04 | 25/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.32×** | +3.7 | 0.009 | 19/49 (HS-578T, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.22×** | +3.7 | 0.010 | 21/48 (HS-578T, A498, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 1.20× | +3.4 | 0.025 | 19/48 (BT-474, NCI-H2030, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3580.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.313×** | -21.6 | 0e+00 | 47/48 (HEC-1-A, SW480, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.308×** | -11.4 | 7e-28 | 47/48 (SW1417, SW48, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.322×** | -11.0 | 6e-26 | 46/48 (SW1417, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.338×** | -10.6 | 6e-24 | 47/48 (HCT15, SW1417, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.366×** | -9.8 | 2e-20 | 45/48 (SW480, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.376×** | -9.5 | 2e-19 | 43/48 (SW1417, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.557×** | -7.8 | 7e-13 | 43/48 (SW480, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.715×** | -6.2 | 3e-08 | 30/49 (SK-MEL-2, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[EX229 (drug)]] 0.05 µM |  | **0.701×** | -6.2 | 3e-08 | 34/48 (Hs 766T, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.724×** | -5.5 | 2e-06 | 28/45 (A-172, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | **0.735×** | -5.5 | 2e-06 | 27/44 (C-33 A, A549, …) | all doses, flat | composition shift |
| [[Belzutifan (drug)]] 5 µM |  | **0.579×** | -5.3 | 5e-06 | 36/47 (CFPAC-1, NCI-H661, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.676×** | -5.2 | 1e-05 | 39/49 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.823×** | -5.1 | 1e-05 | 26/49 (A-172, A549, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.760×** | -5.1 | 1e-05 | 28/48 (MIA PaCa-2, AsPC-1, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.704×** | -4.6 | 1e-04 | 31/48 (NCI-H1792, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.851× | -4.2 | 9e-04 | 22/48 (A498, NCI-H2347, …) | rises with dose |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **0.823×** | -3.6 | 0.009 | 18/48 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.833×** | -3.4 | 0.021 | 17/49 (RPMI-7951, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.833×** | -3.2 | 0.036 | 17/48 (NCI-H1792, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3580. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 55.7 | 10 (4 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.80× (z +17.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.339× (z -11.9) ⚠ unreliable plate only |
| [[SW1417 (line)]] | alt | 113 | 3 | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +16.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.238× (z -19.4) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.154× (z -13.2) |
| [[LoVo (line)]] | wt | 55.1 | 7 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.14× (z +17.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.316× (z -12.4) ⚠ unreliable plate only |
| [[SW480 (line)]] | alt | 83.9 | 5 (1 ⚠) | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.87× (z +15.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.254× (z -19.6) ⚠ unreliable plate only · without an alert: [[c-Kit-IN-1 (drug)]] 5 µM 0.266× (z -9.9) |
| [[NCI-H2347 (line)]] | alt | 95.7 | 4 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +20.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.306× (z -17.5) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.289× (z -9.6) |
| [[A-172 (line)]] | wt | 79.8 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +19.2) | [[Dinaciclib (drug)]] 0.05 µM 0.199× (z -16.3) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 97.0 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +23.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.277× (z -14.8) ⚠ unreliable plate only |
| [[HEC-1-A (line)]] | alt | 108 | 3 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +18.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.227× (z -19.7) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.233× (z -10.1) |
| [[NCI-H1792 (line)]] | alt | 166 | 3 (1 ⚠) | 3 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.46× (z +11.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.41× (z +11.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.310× (z -15.2) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.245× (z -9.5) |
| [[BT-474 (line)]] | alt | 47.5 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +16.5) | — |
| [[HOP62 (line)]] | alt | 71.4 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +15.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.260× (z -15.8) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.240× (z -8.8) |
| [[HS-578T (line)]] | alt | 121 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +10.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.254× (z -14.4) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.206× (z -8.7) |
| [[PANC-1 (line)]] | alt | 52.4 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.53× (z +14.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.342× (z -12.1) ⚠ unreliable plate only |
| [[SNU-423 (line)]] | alt | 81.9 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +14.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.338× (z -12.4) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.243× (z -8.5) |
| [[A498 (line)]] | wt | 65.6 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +19.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.413× (z -8.6) ⚠ unreliable plate only |
| [[SK-MEL-2 (line)]] | alt | 116 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +11.3) | [[Dinaciclib (drug)]] 0.05 µM 0.260× (z -13.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 82.9 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.362× (z -8.6) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 71.5 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.63× (z +10.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.180× (z -17.5) ⚠ unreliable plate only |
| [[HCT15 (line)]] | alt | 69.8 | 0 | 3 (1 ⚠) | — | [[EX229 (drug)]] 5 µM 0.0770× (z -10.7) |
| [[hTERT-HPNE (line)]] | wt | 81.9 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +11.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.255× (z -11.3) ⚠ unreliable plate only |
| [[J82 (line)]] | alt | 60.4 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +13.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.404× (z -9.0) ⚠ unreliable plate only |
| [[KATO III (line)]] | alt | 55.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +12.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.247× (z -13.1) ⚠ unreliable plate only |
| [[LOX-IMVI (line)]] | wt | 77.6 | 0 | 3 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.247× (z -16.0) ⚠ unreliable plate only |
| [[LS 180 (line)]] | wt | 78.5 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.95× (z +12.9) | — |
| [[NCI-H1573 (line)]] | alt | 48.0 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +13.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.362× (z -8.9) ⚠ unreliable plate only |
| [[NCI-H2030 (line)]] | alt | 66.2 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +12.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.321× (z -12.5) ⚠ unreliable plate only |
| [[NCI-H23 (line)]] | alt | 61.7 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +9.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.398× (z -9.6) ⚠ unreliable plate only |
| [[RKO (line)]] | wt | 77.3 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +16.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.240× (z -12.8) ⚠ unreliable plate only |
| [[SNU-1 (line)]] | wt | 82.5 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +8.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.267× (z -10.2) ⚠ unreliable plate only |
| [[SW48 (line)]] | wt | 93.9 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +13.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.153× (z -14.3) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.0623× (z -11.1) |
| [[C-33 A (line)]] | alt | 62.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.128× (z -14.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 66.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +8.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.339× (z -10.2) ⚠ unreliable plate only |
| [[CFPAC-1 (line)]] | alt | 44.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +10.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.386× (z -9.3) ⚠ unreliable plate only |
| [[Hs 766T (line)]] | wt | 59.0 | 0 | 2 (1 ⚠) | — | [[EX229 (drug)]] 0.05 µM 0.260× (z -11.1) |
| [[HT-29 (line)]] | alt | 45.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +12.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.270× (z -11.9) ⚠ unreliable plate only |
| [[Panc 03.27 (line)]] | alt | 75.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +11.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.293× (z -13.4) ⚠ unreliable plate only |
| [[RPMI-7951 (line)]] | alt | 101 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +9.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.267× (z -14.0) ⚠ unreliable plate only |
| [[SHP-77 (line)]] | alt | 105 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.16× (z +8.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.352× (z -11.7) ⚠ unreliable plate only |
| [[H4 (line)]] | wt | 48.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +10.0) | — |
| [[HepG2_C3A (line)]] | wt | 98.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.266× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[MIA PaCa-2 (line)]] | alt | 52.4 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.212× (z -14.9) ⚠ unreliable plate only |
| [[SW 1271 (line)]] | alt | 128 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.196× (z -8.5) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 59.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 89.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 102 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 72.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 81.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 67.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 60.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3580), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RB1CC1]] | +0.74 | +0.58 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[CREBRF]] | +0.74 | +0.62 / +0.87 | both halves | 7e-06 |  |
| [[CRBN]] | +0.74 | +0.66 / +0.78 | both halves | 7e-06 |  |
| [[IKZF5]] | +0.73 | +0.62 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[UBXN7]] | +0.72 | +0.55 / +0.76 | both halves | 1e-05 |  |
| [[KLHL24]] | +0.71 | +0.56 / +0.76 | both halves | 1e-05 |  |
| [[SLU7]] | +0.71 | +0.49 / +0.79 | both halves | 1e-05 |  |
| [[CIR1]] | +0.71 | +0.62 / +0.75 | both halves | 7e-06 |  |
| [[HDAC5]] | +0.69 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[CCDC28A]] | +0.68 | +0.46 / +0.79 | both halves | 3e-05 |  |
| [[KMT2A]] | +0.68 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[HBP1]] | +0.68 | +0.45 / +0.80 | both halves | 3e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2N]] | -0.54 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[LRRC59]] | -0.53 | -0.40 / -0.50 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CRBN]] | C | CRBN's natural level strengthens WDR48's drug response | CRBN's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.68, reverse +0.35; direction not clear | 0.024 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.821). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (0.4, -45.3); signed map (-15.4, 8.9). **Vector** length 116, 38.1% of its response variance represented; |z| ≥ 3 in 1,296 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.2 | +20.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +4.1 | +1.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.8 | +9.4 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +3.6 | +2.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +3.3 | +1.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.3 | +2.2 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +3.3 | +0.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -20.2 | -21.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -11.6 | -11.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -11.4 | -11.0 |
|  | [[EX229 (drug)]] 5 µM |  | -11.4 | -10.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -10.8 | -9.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -9.2 | -7.8 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat domain 48 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p22.2 — chr3:39,052,013-39,096,671 (+) |
| Ensembl biotype | protein_coding |
| Also known as | UAF1, KIAA1449, P80, SPG60, Bun62 |
| Gene groups (HGNC) | WD repeat domain containing |
| Reactome | 9 pathways, smallest: Signaling by cytosolic PDGFRA and PDGFRB fusion proteins; Signaling by PDGFR in disease; Recognition of DNA damage by PCNA-containing replication complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TAF3](https://www.uniprot.org/uniprotkb/Q8TAF3) (WD repeat-containing protein 48):

> Regulator of deubiquitinating complexes, which acts as a strong activator of USP1, USP12 and USP46. Enhances the USP1-mediated deubiquitination of FANCD2; USP1 being almost inactive by itself. Activates deubiquitination by increasing the catalytic turnover without increasing the affinity of deubiquitinating enzymes for the substrate. Also activates deubiquitinating activity of complexes containing USP12. In complex with USP12, acts as a potential tumor suppressor by positively regulating PHLPP1 …

**Summary**, from NCBI Gene [57599](https://www.ncbi.nlm.nih.gov/gene/57599):

> The protein encoded by this gene has been shown to interact with ubiquitin specific peptidase 1 (USP1), activating the deubiquitinating activity of USP1 and allowing it to remove the ubiquitin moiety from monoubiquitinated FANCD2. FANCD2 is ubiquitinated in response to DNA damage. [provided by RefSeq, Sep 2016]

**Accessions** — [HGNC:30914](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30914) · Entrez [57599](https://www.ncbi.nlm.nih.gov/gene/57599) · UniProt [Q8TAF3](https://www.uniprot.org/uniprotkb/Q8TAF3) · Ensembl [ENSG00000114742](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114742)

## Data

Gene col 3580: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3580); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3580, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3580]; `tensor/DDL_lfc|DDL_z.npy` [3580]; `embed/gene_vectors.npy` [3580]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3580 or target_col == 3580). Every well: [[WDR48 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDR48.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
