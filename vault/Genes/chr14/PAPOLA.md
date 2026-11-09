---
symbol: "PAPOLA"
type: "gene"
col: 1610
ensembl_id: "ENSG00000090060"
name: "poly(A) polymerase alpha"
location: "14q32.2"
module: 25
arm: "+"
pooled_cpm: 247.84
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 7
n_dd_up_clean: 11
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# PAPOLA

*poly(A) polymerase alpha* — 14q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.47× (z +19.8, q 0e+00, up in 48 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.85× (z +13.4, q 8e-39, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.723× (z -7.1, q 7e-10, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBQLN1]] (+0.74, fdr 7e-06), [[EEF1A1]] (+0.70, fdr 9e-06), [[CSDE1]] (+0.70, fdr 7e-06); moves opposite to [[VPS37C]] (-0.74, fdr 1e-05), [[PPP1R35]] (-0.64, fdr 1e-05, ⚠ PPP1R35 in the vector space only through flagged drug-doses), [[IMP3]] (-0.64, fdr 4e-05), [[KRI1]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 15 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1610.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.47×** | +19.8 | 0e+00 | 48/49 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.17×** | +16.3 | 0e+00 | 43/44 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.85×** | +13.4 | 8e-39 | 43/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.93×** | +13.3 | 3e-38 | 45/45 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.77×** | +11.9 | 8e-31 | 43/47 (COLO 205, LoVo, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.70×** | +11.6 | 3e-29 | 46/48 (C32, LoVo, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.62×** | +10.6 | 3e-24 | 46/48 (RKO, LS 180, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.61×** | +10.4 | 2e-23 | 45/48 (HEC-1-A, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.34×** | +9.7 | 1e-20 | 46/49 (PANC-1, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.37×** | +9.7 | 2e-20 | 31/48 (PANC-1, NCI-H460, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.46×** | +8.3 | 5e-15 | 33/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.49×** | +8.2 | 2e-14 | 41/48 (MIA PaCa-2, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.44×** | +8.0 | 5e-14 | 35/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.75×** | +6.4 | 7e-09 | 39/48 (SW48, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.32×** | +6.0 | 9e-08 | 30/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.26×** | +3.6 | 0.008 | 26/49 (MIA PaCa-2, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Aliskiren (drug)]] 0.5 µM |  | 1.16× | +3.2 | 0.033 | 12/49 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.31×** | +3.1 | 0.045 | 21/48 (MIA PaCa-2, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.11× | +3.1 | 0.046 | 6/49 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | 1.15× | +3.0 | 0.060 | 17/48 (HOP62, SW 900, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1610.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.723×** | -7.1 | 7e-10 | 38/48 (KATO III, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.757×** | -6.1 | 3e-07 | 34/48 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.762×** | -6.0 | 5e-07 | 36/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.767×** | -5.8 | 8e-07 | 35/48 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.726×** | -5.0 | 6e-05 | 43/48 (COLO 205, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.812×** | -4.6 | 4e-04 | 26/48 (SHP-77, SW480, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~19% of this change | **0.813×** | -4.4 | 1e-03 | 26/47 (KATO III, SW480, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 0.885× | -3.8 | 0.010 | 11/48 (SHP-77, SW1417, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.851× | -3.5 | 0.024 | 19/48 (SW 900, KATO III, …) | rises with dose |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.871× | -3.0 | 0.13 | 13/48 (SW48, NCI-H23, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1610. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 205 | 16 (11 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.82× (z +23.1) | — |
| [[LoVo (line)]] | wt | 286 | 13 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.74× (z +24.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 267 | 11 (8 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +18.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.33× (z +12.6) | — |
| [[SW480 (line)]] | alt | 268 | 10 (5 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +26.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.00× (z +14.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.650× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~19% of this change |
| [[C32 (line)]] | wt | 165 | 10 (6 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.25× (z +17.8) | — |
| [[PANC-1 (line)]] | alt | 186 | 10 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.00× (z +20.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +15.2) | — |
| [[C-33 A (line)]] | alt | 253 | 9 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +16.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.44× (z +13.9) | — |
| [[HEC-1-A (line)]] | alt | 239 | 9 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.30× (z +12.7) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.13× (z +11.5) | — |
| [[HT-29 (line)]] | alt | 201 | 6 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.29× (z +14.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.23× (z +13.8) | [[Panobinostat (drug)]] 5 µM 0.543× (z -10.5) |
| [[KATO III (line)]] | alt | 274 | 5 (4 ⚠) | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.62× (z +15.5) | [[Panobinostat (drug)]] 5 µM 0.517× (z -10.6) |
| [[LS 180 (line)]] | wt | 287 | 8 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.21× (z +18.2) | — |
| [[NCI-H1792 (line)]] | alt | 227 | 8 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.15× (z +19.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.81× (z +14.0) | — |
| [[SW48 (line)]] | wt | 308 | 8 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.06× (z +15.0) | — |
| [[HOP62 (line)]] | alt | 218 | 7 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +17.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.07× (z +10.7) | — |
| [[Hs 766T (line)]] | wt | 163 | 7 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.15× (z +14.1) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 1.99× (z +9.1) | — |
| [[Panc 03.27 (line)]] | alt | 252 | 7 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.56× (z +14.8) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 1.90× (z +10.1) | — |
| [[SK-MEL-2 (line)]] | alt | 211 | 7 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.69× (z +18.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.22× (z +11.6) | — |
| [[A-172 (line)]] | wt | 132 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.44× (z +17.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.00× (z +9.8) | — |
| [[A549 (line)]] | wt | 217 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.98× (z +20.4) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.51× (z +9.7) | — |
| [[COLO 205 (line)]] | alt | 260 | 6 (4 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 4.41× (z +20.6) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.96× (z +15.7) | — |
| [[RKO (line)]] | wt | 309 | 6 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.94× (z +15.8) | — |
| [[SHP-77 (line)]] | alt | 286 | 2 (2 ⚠) | 4 (4 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.52× (z +13.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.605× (z -10.7) ⚠ cell-cycle shift, explains ~34% of this change |
| [[SNU-1 (line)]] | wt | 225 | 6 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.01× (z +12.8) | — |
| [[SW 900 (line)]] | alt | 332 | 6 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.52× (z +13.6) | — |
| [[A-427 (line)]] | wt | 205 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.05× (z +16.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.01× (z +10.0) | — |
| [[LOX-IMVI (line)]] | wt | 268 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.47× (z +11.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.36× (z +10.9) | — |
| [[NCI-H1573 (line)]] | alt | 432 | 3 (2 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.41× (z +12.4) | [[Panobinostat (drug)]] 0.5 µM 0.522× (z -9.3) |
| [[NCI-H2030 (line)]] | alt | 331 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.64× (z +12.1) | — |
| [[RPMI-7951 (line)]] | alt | 213 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.82× (z +12.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.25× (z +10.4) | — |
| [[SNU-423 (line)]] | alt | 174 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.59× (z +18.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 1.97× (z +9.6) | — |
| [[A498 (line)]] | wt | 172 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +15.1) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 227 | 2 (1 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.10× (z +9.6) | [[Panobinostat (drug)]] 0.5 µM 0.485× (z -9.3) |
| [[J82 (line)]] | alt | 203 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.69× (z +14.4) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 1.80× (z +8.6) | — |
| [[BT-474 (line)]] | alt | 228 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.34× (z +12.8) | — |
| [[HS-578T (line)]] | alt | 169 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.97× (z +13.5) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 241 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.32× (z +9.7) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 203 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.62× (z +13.5) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 313 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.05× (z +11.1) | — |
| [[CFPAC-1 (line)]] | alt | 332 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 1.89× (z +8.5) | — |
| [[HCT15 (line)]] | alt | 385 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.01× (z +8.9) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 270 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.08× (z +8.9) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 216 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.03× (z +8.9) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 267 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.83× (z +9.5) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 278 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 255 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 430 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 255 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 269 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 216 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 289 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1610), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBQLN1]] | +0.74 | +0.64 / +0.82 | both halves | 7e-06 |  |
| [[EEF1A1]] | +0.70 | +0.57 / +0.72 | both halves | 9e-06 |  |
| [[CSDE1]] | +0.70 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[PDIA3P1]] | +0.68 | +0.46 / +0.60 | both halves | 3e-05 |  |
| [[MOB1A]] | +0.67 | +0.41 / +0.75 | both halves | 4e-05 |  |
| [[CNOT1]] | +0.66 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[DDX3X]] | +0.65 | +0.46 / +0.66 | both halves | 2e-05 | pathway: Dengue Virus-Host Interactions |
| [[HNRNPA1L3]] | +0.65 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[TWF1]] | +0.65 | +0.51 / +0.68 | both halves | 1e-05 |  |
| [[SPAG16]] | +0.64 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[EIF4H]] | +0.64 | +0.50 / +0.70 | both halves | 1e-05 |  |
| [[EIF4G2]] | +0.63 | +0.44 / +0.61 | both halves | 3e-05 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 6 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS37C]] | -0.74 | -0.55 / -0.70 | both halves | 1e-05 |  |
| [[PPP1R35]] ⚠ | -0.64 | -0.53 / -0.64 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[IMP3]] | -0.64 | -0.41 / -0.71 | both halves | 4e-05 |  |
| [[MRPL41]] ⚠ | -0.64 | -0.34 / -0.68 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[KRI1]] | -0.64 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[ZNF593]] | -0.64 | -0.41 / -0.79 | both halves | 4e-05 |  |
| [[MAP1S]] | -0.64 | -0.35 / -0.65 | both halves | 1e-04 |  |
| [[ARID3A]] | -0.63 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[CCDC85B]] | -0.63 | -0.42 / -0.63 | both halves | 4e-05 |  |
| [[TRAPPC4]] | -0.62 | -0.35 / -0.67 | both halves | 1e-04 |  |
| [[CDKN2D]] | -0.62 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[PUSL1]] | -0.61 | -0.39 / -0.55 | both halves | 5e-05 |  |
| [[ORAI1]] | -0.61 | -0.34 / -0.67 | both halves | 1e-04 |  |
| [[FBXO45]] | -0.60 | -0.39 / -0.70 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises PAPOLA's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.663). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-33.1, -23.6); signed map (-21.2, -32.6). **Vector** length 117, 44.3% of its response variance represented; |z| ≥ 3 in 1,417 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +13.7 | +16.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +13.2 | +19.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +12.7 | +13.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.8 | +11.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.6 | +3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +0.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.0 | -0.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.8 | +10.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.5 | +1.2 |
| fall | [[Belinostat (drug)]] 5 µM |  | -5.9 | -6.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.6 | -5.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.6 | +0.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.6 | -7.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.4 | -5.0 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -3.4 | -0.7 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -2.8 | -1.8 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | -2.7 | -2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | poly(A) polymerase alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.2 — chr14:96,501,433-96,567,116 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PAP |
| Reactome | 10 pathways, smallest: Processing of Intronless Pre-mRNAs; Processing of Capped Intronless Pre-mRNA; RNA Polymerase II Transcription Termination |
| Matched by | ensembl_id |

**Function**, from UniProt [P51003](https://www.uniprot.org/uniprotkb/P51003) (Poly(A) polymerase alpha):

> Polymerase that creates the 3'-poly(A) tail of mRNA's. Also required for the endoribonucleolytic cleavage reaction at some polyadenylation sites. May acquire specificity through interaction with a cleavage and polyadenylation specificity factor (CPSF) at its C-terminus.

**Summary**, from NCBI Gene [10914](https://www.ncbi.nlm.nih.gov/gene/10914):

> The protein encoded by this gene belongs to the poly(A) polymerase family. It is required for the addition of adenosine residues for the creation of the 3'-poly(A) tail of mRNAs. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Oct 2011]

**Accessions** — [HGNC:14981](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14981) · Entrez [10914](https://www.ncbi.nlm.nih.gov/gene/10914) · UniProt [P51003](https://www.uniprot.org/uniprotkb/P51003) · Ensembl [ENSG00000090060](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000090060)

## Data

Gene col 1610: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1610); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1610, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1610]; `tensor/DDL_lfc|DDL_z.npy` [1610]; `embed/gene_vectors.npy` [1610]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1610 or target_col == 1610). Every well: [[PAPOLA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PAPOLA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
