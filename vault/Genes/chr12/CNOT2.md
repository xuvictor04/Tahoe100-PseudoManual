---
symbol: "CNOT2"
type: "gene"
col: 3242
ensembl_id: "ENSG00000111596"
name: "CCR4-NOT transcription complex subunit 2"
location: "12q15"
module: 76
arm: "+"
pooled_cpm: 270.89
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 22
n_dd_up_clean: 7
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# CNOT2

*CCR4-NOT transcription complex subunit 2* — 12q15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.02× (z +14.6, q 1e-45, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.329× (z -22.2, q 0e+00, down in 44 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.396× (z -19.3, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (80 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 21 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIK3C3]] (+0.55, fdr 2e-05), [[PTRHD1]] (+0.55, fdr 4e-05, ⚠ PTRHD1 in the vector space only through flagged drug-doses), [[TNKS]] (+0.55, fdr 3e-05), [[HBP1]] (+0.55, fdr 1e-05); moves opposite to [[MAP7D1]] (-0.54, fdr 1e-05), [[MICALL1]] (-0.52, fdr 3e-05), [[MICAL1]] (-0.51, fdr 4e-04).
> It is in [[Module 076]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3242.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.02×** | +14.6 | 1e-45 | 46/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.81×** | +12.3 | 1e-32 | 43/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.82×** | +11.3 | 4e-27 | 48/49 (LoVo, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.65×** | +10.4 | 2e-23 | 41/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.65×** | +10.3 | 6e-23 | 43/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.52×** | +10.0 | 1e-21 | 47/48 (LoVo, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.39×** | +6.8 | 7e-10 | 34/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.54×** | +4.7 | 2e-04 | 27/38 (NCI-H2030, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.24×** | +4.5 | 5e-04 | 27/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.24×** | +4.3 | 8e-04 | 25/47 (LoVo, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +3.7 | 0.013 | 0/50 | inconsistent across doses |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.18× | +3.4 | 0.038 | 19/49 (PANC-1, A-172, …) | top dose only | plate-row cell shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | 1.12× | +3.3 | 0.050 | 16/48 (A498, A549, …) | top dose only | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 11 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3242.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.329×** | -22.2 | 0e+00 | 44/44 (NCI-H23, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.396×** | -19.3 | 0e+00 | 48/48 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.405×** | -18.8 | 0e+00 | 48/48 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.426×** | -17.8 | 0e+00 | 48/48 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.429×** | -17.6 | 0e+00 | 49/49 (SK-MEL-2, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.566×** | -11.9 | 2e-30 | 47/48 (NCI-H1792, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.731×** | -9.2 | 2e-18 | 39/49 (NCI-H460, CFPAC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.649×** | -9.0 | 1e-17 | 44/48 (NCI-H2347, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.640×** | -8.9 | 2e-17 | 44/47 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.683×** | -7.6 | 1e-12 | 38/48 (SNU-423, C32, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.736×** | -6.2 | 4e-08 | 39/50 (A-172, hTERT-HPNE, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.812×** | -6.1 | 4e-08 | 28/48 (C32, LOX-IMVI, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.746×** | -6.1 | 5e-08 | 40/48 (KATO III, SW 900, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.759×** | -5.3 | 4e-06 | 31/45 (NCI-H2347, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.780×** | -5.2 | 8e-06 | 29/48 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.634×** | -5.0 | 2e-05 | 42/49 (SK-MEL-2, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.794×** | -4.8 | 5e-05 | 25/48 (CFPAC-1, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.829×** | -3.9 | 0.003 | 23/48 (NCI-H1792, C32, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.856× | -3.3 | 0.030 | 21/48 (NCI-H1792, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.858× | -3.2 | 0.033 | 19/48 (NCI-H2347, C32, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.745×** | -3.2 | 0.033 | 29/48 (MIA PaCa-2, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.859× | -3.2 | 0.036 | 21/48 (NCI-H1573, NCI-H1792, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.863× | -3.1 | 0.045 | 14/48 (NCI-H1573, NCI-H1792, …) | rises with dose |  |
| [[Vitamin K4 (drug)]] 0.05 µM |  | 0.868× | -3.0 | 0.065 | 13/49 (NCI-H1792, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3242. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 221 | 8 (1 ⚠) | 7 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.82× (z +18.8) | [[Dinaciclib (drug)]] 5 µM 0.320× (z -19.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.379× (z -17.6) |
| [[NCI-H460 (line)]] | wt | 420 | 6 (1 ⚠) | 8 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 2.47× (z +11.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.363× (z -17.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.257× (z -16.5) |
| [[HT-29 (line)]] | alt | 243 | 7 (2 ⚠) | 6 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.71× (z +15.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.40× (z +13.9) | [[Panobinostat (drug)]] 0.5 µM 0.352× (z -16.6) |
| [[J82 (line)]] | alt | 247 | 5 (1 ⚠) | 7 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.35× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.267× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.383× (z -14.9) |
| [[LoVo (line)]] | wt | 296 | 7 (2 ⚠) | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.80× (z +23.2) | [[Panobinostat (drug)]] 5 µM 0.478× (z -12.9) |
| [[NCI-H1792 (line)]] | alt | 425 | 4 (1 ⚠) | 8 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.85× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.236× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.279× (z -16.5) |
| [[PANC-1 (line)]] | alt | 226 | 7 (1 ⚠) | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.59× (z +23.2) | [[Dinaciclib (drug)]] 5 µM 0.399× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.453× (z -14.4) |
| [[HOP62 (line)]] | alt | 231 | 5 (1 ⚠) | 6 (2 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.30× (z +10.6) | [[Panobinostat (drug)]] 0.5 µM 0.320× (z -14.5) |
| [[KATO III (line)]] | alt | 184 | 6 (1 ⚠) | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.06× (z +19.1) | [[Belinostat (drug)]] 5 µM 0.389× (z -16.2) |
| [[NCI-H1573 (line)]] | alt | 257 | 6 (2 ⚠) | 5 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.64× (z +13.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.45× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.314× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.463× (z -10.6) |
| [[NCI-H23 (line)]] | alt | 301 | 6 (2 ⚠) | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.03× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.237× (z -22.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.505× (z -11.3) |
| [[SW 900 (line)]] | alt | 335 | 4 (1 ⚠) | 7 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.39× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.263× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.307× (z -14.5) |
| [[A-172 (line)]] | wt | 192 | 1 | 9 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 2.00× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.339× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.371× (z -12.2) |
| [[C32 (line)]] | wt | 356 | 0 | 10 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.246× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.314× (z -13.4) |
| [[HepG2_C3A (line)]] | wt | 303 | 4 (1 ⚠) | 6 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.82× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.325× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.351× (z -13.3) |
| [[hTERT-HPNE (line)]] | wt | 245 | 0 | 10 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.267× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.293× (z -12.9) |
| [[LOX-IMVI (line)]] | wt | 382 | 1 | 9 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.35× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.241× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.266× (z -16.1) |
| [[NCI-H2347 (line)]] | alt | 322 | 0 | 10 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -22.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.327× (z -18.0) |
| [[A498 (line)]] | wt | 252 | 3 (3 ⚠) | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +12.5) ⚠ cell-cycle shift, explains ~83% of this change | [[Panobinostat (drug)]] 0.5 µM 0.363× (z -14.6) |
| [[CFPAC-1 (line)]] | alt | 279 | 0 | 9 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.234× (z -21.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.328× (z -17.3) |
| [[H4 (line)]] | wt | 382 | 0 | 9 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.194× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.214× (z -16.2) |
| [[A549 (line)]] | wt | 249 | 2 (1 ⚠) | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +12.3) ⚠ cell-cycle shift, explains ~83% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.17× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.274× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.339× (z -13.4) |
| [[AsPC-1 (line)]] | alt | 407 | 2 (1 ⚠) | 6 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.09× (z +14.1) | [[Panobinostat (drug)]] 5 µM 0.216× (z -19.2) |
| [[BT-474 (line)]] | alt | 292 | 5 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.13× (z +10.7) | [[Panobinostat (drug)]] 0.5 µM 0.477× (z -10.6) |
| [[COLO 205 (line)]] | alt | 233 | 5 (2 ⚠) | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.51× (z +11.3) | [[Panobinostat (drug)]] 0.5 µM 0.415× (z -12.7) |
| [[HEC-1-A (line)]] | alt | 240 | 4 (1 ⚠) | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.58× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.438× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.521× (z -10.3) |
| [[RKO (line)]] | wt | 386 | 4 (1 ⚠) | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.41× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -23.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.444× (z -11.3) |
| [[Hs 766T (line)]] | wt | 201 | 2 (1 ⚠) | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.40× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.313× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.359× (z -12.2) |
| [[LS 180 (line)]] | wt | 305 | 2 (1 ⚠) | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.89× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.255× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.403× (z -11.6) |
| [[MIA PaCa-2 (line)]] | alt | 250 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.267× (z -16.6) |
| [[Panc 03.27 (line)]] | alt | 181 | 2 | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.66× (z +9.7) | [[Panobinostat (drug)]] 0.5 µM 0.387× (z -13.6) |
| [[RPMI-7951 (line)]] | alt | 256 | 1 | 6 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.77× (z +8.7) | [[Panobinostat (drug)]] 0.5 µM 0.322× (z -14.3) |
| [[SNU-423 (line)]] | alt | 232 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.362× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.406× (z -12.2) |
| [[SW1417 (line)]] | alt | 240 | 2 (1 ⚠) | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.93× (z +9.8) | [[Panobinostat (drug)]] 5 µM 0.406× (z -13.4) |
| [[HS-578T (line)]] | alt | 171 | 5 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.64× (z +12.7) | [[Panobinostat (drug)]] 0.5 µM 0.457× (z -10.3) |
| [[SHP-77 (line)]] | alt | 248 | 2 (1 ⚠) | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.43× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.367× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.511× (z -8.5) |
| [[A-427 (line)]] | wt | 284 | 1 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.51× (z +9.4) ⚠ cell-cycle shift, explains ~83% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.438× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.507× (z -10.9) |
| [[HCT15 (line)]] | alt | 399 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.131× (z -20.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.334× (z -11.3) |
| [[NCI-H2030 (line)]] | alt | 175 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.00× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.502× (z -9.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 194 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.172× (z -24.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.423× (z -11.9) |
| [[AN3 CA (line)]] | alt | 273 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.337× (z -10.4) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 245 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.333× (z -12.9) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 294 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0909× (z -20.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.328× (z -10.0) |
| [[NCI-H2122 (line)]] | alt | 389 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0349× (z -12.4) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 169 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.231× (z -8.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 270 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.247× (z -15.2) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 354 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -8.9) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 223 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.58× (z +10.4) | — |
| [[NCI-H596 (line)]] | alt | 325 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 212 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3242), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 15 of them with an alert (⚠; 14 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIK3C3]] | +0.55 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[PTRHD1]] ⚠ | +0.55 | +0.42 / +0.42 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TNKS]] | +0.55 | +0.46 / +0.62 | both halves | 3e-05 |  |
| [[HBP1]] | +0.55 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[ZNF292]] | +0.55 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[MED6]] | +0.54 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[HELZ]] | +0.54 | +0.57 / +0.60 | both halves | 1e-05 | STRING 542 |
| [[RBPJ]] | +0.52 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[C11orf1]] | +0.51 | +0.14 / +0.41 | ⚠ not reproduced | 0.002 |  |
| [[PART1]] | +0.51 | +0.22 / +0.35 | both halves | 6e-04 |  |
| [[KMT2E]] | +0.50 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[TRA2A]] | +0.49 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[HOXA5]] | +0.48 | +0.33 / +0.30 | both halves | 2e-04 |  |
| [[PAN3]] | +0.48 | +0.57 / +0.60 | both halves | 1e-05 | pathway: Deadenylation of mRNA |

## Genes that move opposite

*27 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAP7D1]] | -0.54 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[MICALL1]] | -0.52 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[MICAL1]] | -0.51 | -0.26 / -0.44 | both halves | 4e-04 |  |
| [[ZBED4]] | -0.50 | -0.20 / -0.54 | ⚠ one half (not replicated) | 8e-04 |  |
| [[POGK]] | -0.49 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[CEP170B]] | -0.48 | -0.41 / -0.35 | both halves | 1e-04 |  |
| [[RUBCN]] | -0.48 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[KIF1C]] | -0.48 | -0.29 / -0.32 | both halves | 3e-04 |  |
| [[ABCC10]] | -0.48 | -0.19 / -0.66 | ⚠ one half (not replicated) | 8e-04 |  |
| [[RNF34]] | -0.47 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[CDV3]] | -0.47 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[PSEN2]] | -0.46 | -0.35 / -0.57 | both halves | 1e-04 |  |
| [[TTL]] | -0.46 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[PTPN21]] | -0.45 | -0.44 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.365). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (3.8, -23.4); signed map (-11.2, 5.0). **Vector** length 76.4, 29.2% of its response variance represented; |z| ≥ 3 in 1,648 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +7.4 | +1.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | +6.6 | -5.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.9 | -17.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | -22.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | -0.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | -2.6 |
|  | [[Arbutin (drug)]] 5 µM |  | +2.9 | +0.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.7 | -0.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.4 | -1.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.2 | -5.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.2 | -4.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.1 | -1.2 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -3.7 | -0.0 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -3.3 | -1.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.2 | -3.2 |
|  | [[EX229 (drug)]] 5 µM |  | -3.2 | -2.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -3.2 | +0.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.2 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | CCR4-NOT transcription complex subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q15 — chr12:70,243,002-70,354,993 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CDC36, NOT2H; previously NOT2 |
| Gene groups (HGNC) | CCR4-NOT transcription complex |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 8 pathways, smallest: TP53 regulates transcription of additional cell cycle genes whose exact role in the p53 pathway remain uncertain; Deadenylation of mRNA; M-decay: degradation of maternal mRNAs by maternally stored factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZN8](https://www.uniprot.org/uniprotkb/Q9NZN8) (CCR4-NOT transcription complex subunit 2):

> Component of the CCR4-NOT complex which is one of the major cellular mRNA deadenylases and is linked to various cellular processes including bulk mRNA degradation, miRNA-mediated repression, translational repression during translational initiation and general transcription regulation. Additional complex functions may be a consequence of its influence on mRNA expression. Required for the CCR4-NOT complex structural integrity. Can repress transcription and may link the CCR4-NOT complex to …

**Summary**, from NCBI Gene [4848](https://www.ncbi.nlm.nih.gov/gene/4848):

> This gene encodes a subunit of the multi-component CCR4-NOT complex. The CCR4-NOT complex regulates mRNA synthesis and degradation and is also thought to be involved in mRNA splicing, transport and localization. The encoded protein interacts with histone deacetylases and functions as a repressor of polymerase II transcription. Alternatively spliced transcript variants have been observed for this gene. [provided by RefSeq, Dec 2010]

**Accessions** — [HGNC:7878](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7878) · Entrez [4848](https://www.ncbi.nlm.nih.gov/gene/4848) · UniProt [Q9NZN8](https://www.uniprot.org/uniprotkb/Q9NZN8) · Ensembl [ENSG00000111596](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111596)

## Data

Gene col 3242: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3242); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3242, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3242]; `tensor/DDL_lfc|DDL_z.npy` [3242]; `embed/gene_vectors.npy` [3242]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3242 or target_col == 3242). Every well: [[CNOT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CNOT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
