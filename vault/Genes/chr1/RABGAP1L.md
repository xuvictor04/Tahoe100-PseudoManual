---
symbol: "RABGAP1L"
type: "gene"
col: 7587
ensembl_id: "ENSG00000152061"
name: "RAB GTPase activating protein 1 like"
location: "1q25.1"
module: 211
arm: "+"
pooled_cpm: 294.86
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 27
n_dd_up_clean: 8
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/211"]
generated_by: "tahoemap"
---

# RABGAP1L

*RAB GTPase activating protein 1 like* — 1q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.29× (z +6.3, q 2e-07, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (18 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.428× (z -14.7, q 0e+00, down in 47 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.618× (z -11.8, q 5e-30, down in 46 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STK3]] (+0.69, fdr 7e-06), [[UBE2E2]] (+0.66, fdr 1e-05), [[ERC1]] (+0.65, fdr 1e-05); moves opposite to [[HOXA3]] (-0.61, fdr 2e-05), [[VDAC1P8]] (-0.59, fdr 2e-05), [[ANKRA2]] (-0.55, fdr 3e-05).
> It is in [[Module 211]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[APLN]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7587.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +6.3 | 2e-07 | 35/48 (SW1417, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.36×** | +5.4 | 2e-05 | 31/48 (NCI-H460, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.32×** | +4.7 | 5e-04 | 37/47 (CFPAC-1, NCI-H460, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.32×** | +4.6 | 6e-04 | 35/47 (A-172, NCI-H460, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.28×** | +4.3 | 0.002 | 29/49 (NCI-H2347, SW1417, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.34×** | +4.2 | 0.003 | 34/48 (SW1417, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.26×** | +3.7 | 0.016 | 28/47 (A-172, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM |  | **1.20×** | +3.2 | 0.080 | 25/48 (SW1417, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.42×** | +3.2 | 0.080 | 27/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.41×** | +3.1 | 0.096 | 26/49 (NCI-H2347, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | 1.40× | +3.1 | 0.10 | 25/50 (NCI-H460, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 18 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7587.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.428×** | -14.7 | 0e+00 | 47/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.458×** | -13.5 | 2e-39 | 45/48 (SW480, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.470×** | -12.6 | 3e-34 | 45/47 (NCI-H1573, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.618×** | -11.8 | 5e-30 | 46/49 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.321×** | -10.3 | 6e-23 | 46/49 (SNU-1, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.556×** | -9.8 | 1e-20 | 37/44 (NCI-H23, A-172, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.580×** | -9.5 | 3e-19 | 45/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.582×** | -9.4 | 4e-19 | 44/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.561×** | -9.3 | 1e-18 | 38/45 (C-33 A, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.577×** | -8.7 | 2e-16 | 44/49 (SW 1271, NCI-H23, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~48% of this change | **0.669×** | -7.0 | 1e-10 | 42/48 (PANC-1, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.516×** | -6.0 | 9e-08 | 29/38 (Panc 03.27, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.702×** | -5.9 | 2e-07 | 35/50 (SK-MEL-2, A-427, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.529×** | -5.8 | 3e-07 | 32/48 (HOP62, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.672×** | -5.6 | 8e-07 | 33/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.773×** | -4.3 | 5e-04 | 27/48 (NCI-H23, A-427, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.782×** | -4.3 | 6e-04 | 30/48 (A549, NCI-H460, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.779×** | -3.9 | 0.002 | 31/48 (HepG2/C3A, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.801×** | -3.5 | 0.011 | 28/48 (NCI-H2030, A-427, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.820×** | -3.4 | 0.013 | 26/48 (C-33 A, Panc 03.27, …) | top dose only |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.881× | -3.1 | 0.041 | 7/49 (LOX-IMVI, AsPC-1, …) | top dose only |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.884× | -3.0 | 0.056 | 7/49 (hTERT-HPNE, HS-578T, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 0.886× | -2.9 | 0.061 | 12/48 (LoVo, RKO, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7587. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 316 | 2 | 17 (14 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.80× (z +10.8) | [[Digitoxin (drug)]] 5 µM 0.238× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.211× (z -10.5) |
| [[NCI-H23 (line)]] | alt | 394 | 0 | 13 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -22.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -13.4) |
| [[A-427 (line)]] | wt | 541 | 0 | 12 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -15.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -12.3) |
| [[SW480 (line)]] | alt | 347 | 0 | 12 (9 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.305× (z -18.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.514× (z -14.7) |
| [[LoVo (line)]] | wt | 402 | 0 | 11 (9 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.270× (z -17.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.186× (z -11.9) |
| [[LOX-IMVI (line)]] | wt | 312 | 0 | 11 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -15.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.545× (z -11.3) |
| [[NCI-H1573 (line)]] | alt | 290 | 0 | 10 (9 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.246× (z -17.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -15.4) |
| [[PANC-1 (line)]] | alt | 371 | 0 | 10 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -19.3) |
| [[A549 (line)]] | wt | 273 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -15.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -13.9) |
| [[HT-29 (line)]] | alt | 263 | 2 | 6 (5 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.69× (z +10.0) | [[Digitoxin (drug)]] 5 µM 0.403× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.288× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 362 | 0 | 8 (7 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.120× (z -14.8) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -14.6) |
| [[HEC-1-A (line)]] | alt | 254 | 1 | 6 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.67× (z +10.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.470× (z -10.1) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.613× (z -9.6) |
| [[LS 180 (line)]] | wt | 263 | 1 | 6 (5 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.64× (z +8.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.306× (z -14.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.236× (z -9.2) |
| [[HepG2_C3A (line)]] | wt | 303 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.554× (z -11.0) |
| [[HOP62 (line)]] | alt | 213 | 0 | 6 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.327× (z -12.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.192× (z -9.7) |
| [[Hs 766T (line)]] | wt | 460 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -14.6) |
| [[KATO III (line)]] | alt | 267 | 0 | 6 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.304× (z -15.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.479× (z -13.5) |
| [[SNU-1 (line)]] | wt | 277 | 0 | 6 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.309× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.125× (z -12.0) |
| [[SW 900 (line)]] | alt | 340 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -14.4) |
| [[SW1417 (line)]] | alt | 219 | 4 (1 ⚠) | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.01× (z +12.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.589× (z -9.6) |
| [[A-172 (line)]] | wt | 314 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.327× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.259× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 560 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -14.6) |
| [[BT-474 (line)]] | alt | 251 | 0 | 5 (4 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.150× (z -12.4) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 0.05 µM 0.453× (z -9.4) |
| [[C-33 A (line)]] | alt | 422 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.159× (z -21.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.537× (z -10.9) |
| [[COLO 205 (line)]] | alt | 587 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -11.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -9.5) |
| [[NCI-H1792 (line)]] | alt | 221 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.336× (z -13.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 127 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +15.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.05× (z +12.4) | — |
| [[SK-MEL-2 (line)]] | alt | 345 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.269× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -13.1) |
| [[SW48 (line)]] | wt | 225 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -10.3) |
| [[hTERT-HPNE (line)]] | wt | 196 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +10.4) ⚠ cell-cycle shift, would explain all of this change | [[Digitoxin (drug)]] 5 µM 0.319× (z -12.3) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 283 | 0 | 4 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.348× (z -12.5) ⚠ toxic |
| [[RKO (line)]] | wt | 277 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.356× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.197× (z -9.5) |
| [[SNU-423 (line)]] | alt | 238 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.413× (z -11.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.595× (z -9.8) |
| [[A498 (line)]] | wt | 209 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.460× (z -8.6) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 225 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.500× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 192 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.319× (z -12.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 224 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -15.9) |
| [[SHP-77 (line)]] | alt | 311 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.480× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.614× (z -8.9) |
| [[C32 (line)]] | wt | 206 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +11.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.72× (z +9.0) | — |
| [[CFPAC-1 (line)]] | alt | 251 | 1 | 1 (1 ⚠) | [[Cobimetinib (drug)]] 5 µM 2.31× (z +8.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.394× (z -9.5) ⚠ toxic |
| [[H4 (line)]] | wt | 237 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.390× (z -8.8) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 130 | 0 | 2 | — | [[crizotinib (drug)]] 0.05 µM 0.0712× (z -9.6) |
| [[HS-578T (line)]] | alt | 159 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -11.4) |
| [[SW 1271 (line)]] | alt | 255 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0640× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[AN3 CA (line)]] | alt | 263 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 276 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 236 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 286 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 314 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 181 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7587), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STK3]] | +0.69 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[UBE2E2]] | +0.66 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[ERC1]] | +0.65 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[SPIDR]] | +0.62 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[EXOC6B]] | +0.61 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[LRBA]] | +0.61 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[PITPNB]] | +0.60 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[MIPOL1]] | +0.57 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[SUPT3H]] | +0.57 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[ATP9B]] | +0.57 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[TMEM241]] | +0.57 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[DIAPH2]] | +0.56 | +0.50 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOXA3]] | -0.61 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[VDAC1P8]] | -0.59 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[ANKRA2]] | -0.55 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[NUP133]] | -0.55 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[EMC1-AS1]] | -0.55 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[BCKDHA]] | -0.55 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[TMEM94]] | -0.54 | -0.43 / -0.50 | both halves | 4e-05 |  |
| [[LINC00938]] | -0.54 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[GOT1-DT]] | -0.54 | -0.47 / -0.32 | both halves | 2e-04 |  |
| [[VPS13B-DT]] | -0.53 | -0.44 / -0.38 | both halves | 7e-05 |  |
| [[PRPSAP2]] | -0.53 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[DDB2]] | -0.52 | -0.50 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APLN]] | B | APLN activity lowers RABGAP1L's level | lines that do not express APLN (13) vs lines expressing it (37) | 1.43× higher at baseline in the lines without APLN | 0.015 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TUSC3]] | B | TUSC3 activity lowers RABGAP1L's level | lines that do not express TUSC3 (17) vs lines expressing it (33) | 1.27× higher at baseline in the lines without TUSC3 | 0.089 | ⚠ within organs, on part of the lines; also absent: MAP9, BVES-AS1, RNF150; its own permutation p |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers RABGAP1L's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers RABGAP1L's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[APLN]] | B | APLN activity weakens RABGAP1L's drug response | lines that do not express APLN (13) vs lines expressing it (36) | the lines without APLN respond 1.22× as strongly (z diff -1.41); strongest at Dinaciclib 0.5 µM: 0.39x vs 0.61x (z diff -3.1) | 0.0996 | ⚠ within organs, on part of the lines; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 211]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.800). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-2.0, -34.2); signed map (-12.9, -53.2). **Vector** length 110, 44.6% of its response variance represented; |z| ≥ 3 in 1,524 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~63% of this change | +6.4 | -3.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.2 | -4.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.1 | +1.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.7 | +4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.6 | -1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +6.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.4 | +2.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.2 | -0.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.1 | +3.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -12.1 | -11.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -9.5 | -12.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | -5.3 | -9.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.3 | -4.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.0 | -9.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.8 | -0.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.1 | -2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | -1.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.0 | -5.8 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -2.9 | +1.3 |

## What is on record

|  |  |
|---|---|
| Name | RAB GTPase activating protein 1 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q25.1 — chr1:174,159,410-174,995,308 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HHL, TBC1D18, KIAA0471, FLJ38519 |
| Gene groups (HGNC) | TBC1 domain family members |
| Hallmark sets | KRAS_SIGNALING_UP, IL2_STAT5_SIGNALING |
| Matched by | ensembl_id |

UniProt [B7ZAP0](https://www.uniprot.org/uniprotkb/B7ZAP0) carries no function annotation.

**Summary**, from NCBI Gene [9910](https://www.ncbi.nlm.nih.gov/gene/9910):

> Enables GTPase activator activity and small GTPase binding activity. Acts upstream of or within regulation of protein localization. Located in several cellular components, including Golgi apparatus; cilium; and early endosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24663](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24663) · Entrez [9910](https://www.ncbi.nlm.nih.gov/gene/9910) · UniProt [B7ZAP0](https://www.uniprot.org/uniprotkb/B7ZAP0) · Ensembl [ENSG00000152061](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152061)

## Data

Gene col 7587: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7587); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7587, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7587]; `tensor/DDL_lfc|DDL_z.npy` [7587]; `embed/gene_vectors.npy` [7587]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7587 or target_col == 7587). Every well: [[RABGAP1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RABGAP1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
