---
symbol: "BZW1"
type: "gene"
col: 1337
ensembl_id: "ENSG00000082153"
name: "basic leucine zipper and W2 domains 1"
location: "2q33.1"
module: 78
arm: "+"
pooled_cpm: 246.76
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 21
n_dd_up_clean: 7
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# BZW1

*basic leucine zipper and W2 domains 1* — 2q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (16 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.47× (z +12.3, q 8e-32, up in 46 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.83× (z +8.2, q 4e-14, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (3 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.637× (z -5.8, q 2e-06, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARPC2]] (+0.67, fdr 7e-06), [[SEPTIN10]] (+0.65, fdr 7e-06), [[NT5E]] (+0.63, fdr 7e-06); moves opposite to [[SPIN2B]] (-0.58, fdr 5e-05), [[NELFA]] (-0.58, fdr 1e-05), [[PKDCC]] (-0.57, fdr 3e-05).
> It is in [[Module 078]], a single-armed module (apical junction).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[EMP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 17 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1337.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **2.47×** | +12.3 | 8e-32 | 46/49 (SW480, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **2.32×** | +11.0 | 1e-25 | 41/44 (SW480, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.83×** | +8.2 | 4e-14 | 48/48 (SW480, AsPC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.83×** | +8.2 | 4e-14 | 43/48 (SW480, HT-29, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.81×** | +8.1 | 7e-14 | 46/48 (SW480, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.83×** | +7.6 | 4e-12 | 43/45 (SW480, SW48, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.74×** | +7.5 | 4e-12 | 43/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.46×** | +7.2 | 3e-11 | 34/48 (SNU-423, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **1.69×** | +7.2 | 5e-11 | 46/48 (SW480, HT-29, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.62×** | +6.6 | 3e-09 | 46/48 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.34×** | +6.0 | 9e-08 | 43/49 (RPMI-7951, AsPC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.13×** | +5.4 | 4e-06 | 40/48 (HS-578T, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.47×** | +5.2 | 8e-06 | 34/48 (COLO 205, C32, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **1.45×** | +4.8 | 5e-05 | 31/48 (COLO 205, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Mebendazole (drug)]] 5 µM |  | **1.43×** | +4.7 | 1e-04 | 44/48 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.32×** | +3.8 | 0.004 | 32/48 (C32, A549, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.54×** | +3.1 | 0.055 | 27/48 (MIA PaCa-2, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.23×** | +2.9 | 0.090 | 23/48 (MIA PaCa-2, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1337.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.637×** | -5.8 | 2e-06 | 39/47 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **0.737×** | -5.8 | 2e-06 | 37/48 (RKO, SW 900, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.665×** | -5.6 | 5e-06 | 41/50 (NCI-H23, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.749×** | -5.3 | 1e-05 | 42/48 (NCI-H23, MIA PaCa-2, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.740×** | -5.0 | 5e-05 | 37/48 (NCI-H23, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.760×** | -5.0 | 5e-05 | 38/49 (MIA PaCa-2, SW480, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.696×** | -4.9 | 7e-05 | 39/49 (NCI-H23, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.704×** | -4.7 | 2e-04 | 37/48 (RKO, NCI-H23, …) | rises with dose | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.712×** | -4.5 | 4e-04 | 36/48 (KATO III, NCI-H23, …) | rises with dose | position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.739×** | -4.0 | 0.003 | 36/47 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.733×** | -4.0 | 0.004 | 34/48 (SW 1088, NCI-H23, …) | all doses, flat |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.664×** | -3.9 | 0.004 | 36/48 (SK-MEL-2, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.05 µM |  | **0.737×** | -3.8 | 0.005 | 40/49 (HEC-1-A, PANC-1, …) | inconsistent across doses |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.739×** | -3.8 | 0.006 | 33/48 (MIA PaCa-2, RKO, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.765×** | -3.6 | 0.014 | 29/49 (NCI-H23, MIA PaCa-2, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.811×** | -3.5 | 0.014 | 29/48 (MIA PaCa-2, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.763×** | -3.3 | 0.029 | 27/48 (NCI-H23, MIA PaCa-2, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, +0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1337. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 306 | 2 (1 ⚠) | 10 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.33× (z +9.1) | [[Adagrasib (drug)]] 0.05 µM 0.497× (z -26.3) ⚠ position not correctable · without an alert: [[Binimetinib (drug)]] 0.05 µM 0.438× (z -12.3) |
| [[NCI-H23 (line)]] | alt | 276 | 2 (2 ⚠) | 10 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.82× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | [[Adagrasib (drug)]] 0.05 µM 0.554× (z -21.9) ⚠ position not correctable · without an alert: [[Binimetinib (drug)]] 5 µM 0.369× (z -11.1) |
| [[SW480 (line)]] | alt | 181 | 11 (9 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 4.27× (z +15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.25× (z +12.9) | [[Binimetinib (drug)]] 0.05 µM 0.552× (z -8.9) |
| [[HT-29 (line)]] | alt | 113 | 9 (8 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.93× (z +13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.30× (z +12.1) | — |
| [[LoVo (line)]] | wt | 125 | 9 (8 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.89× (z +11.2) | — |
| [[COLO 205 (line)]] | alt | 88.1 | 8 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +14.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.40× (z +9.8) | — |
| [[C32 (line)]] | wt | 217 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +13.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.91× (z +10.8) | — |
| [[NCI-H1792 (line)]] | alt | 254 | 6 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +12.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[AsPC-1 (line)]] | alt | 504 | 4 (4 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.59× (z +13.2) ⚠ cell-cycle shift, explains ~55% of this change | [[Trametinib (drug)]] 0.5 µM 0.478× (z -9.5) |
| [[PANC-1 (line)]] | alt | 172 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[RKO (line)]] | wt | 211 | 1 (1 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.67× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | [[Trametinib (drug)]] 5 µM 0.347× (z -10.2) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Binimetinib (drug)]] 5 µM 0.415× (z -8.7) |
| [[SNU-1 (line)]] | wt | 144 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.02× (z +10.0) | — |
| [[SNU-423 (line)]] | alt | 152 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +14.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.35× (z +9.1) | — |
| [[A498 (line)]] | wt | 181 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +12.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A-172 (line)]] | wt | 195 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.74× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.21× (z +8.9) | — |
| [[A-427 (line)]] | wt | 133 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.72× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[HOP62 (line)]] | alt | 252 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.66× (z +9.6) | — |
| [[KATO III (line)]] | alt | 114 | 3 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.27× (z +11.1) ⚠ cell-cycle shift, explains ~55% of this change | — |
| [[RPMI-7951 (line)]] | alt | 212 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +12.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SK-MEL-2 (line)]] | alt | 147 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +14.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.52× (z +9.5) | — |
| [[SW48 (line)]] | wt | 86.0 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +12.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A549 (line)]] | wt | 308 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.50× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.26× (z +9.3) | — |
| [[H4 (line)]] | wt | 158 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[HEC-1-A (line)]] | alt | 142 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.54× (z +9.5) | — |
| [[Hs 766T (line)]] | wt | 327 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.63× (z +10.4) ⚠ cell-cycle shift, explains ~55% of this change | — |
| [[LOX-IMVI (line)]] | wt | 272 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.33× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[NCI-H2030 (line)]] | alt | 233 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.47× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[NCI-H460 (line)]] | wt | 518 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 2.38× (z +8.8) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[AN3 CA (line)]] | alt | 121 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.51× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[BT-474 (line)]] | alt | 354 | 0 | 1 | — | [[Afatinib (drug)]] 5 µM 0.366× (z -8.7) |
| [[C-33 A (line)]] | alt | 130 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.18× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[HCT15 (line)]] | alt | 219 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.48× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[HS-578T (line)]] | alt | 259 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 4.59× (z +9.0) | — |
| [[hTERT-HPNE (line)]] | wt | 227 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.33× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[LS 180 (line)]] | wt | 212 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[SW 1088 (line)]] | alt | 242 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.148× (z -10.0) |
| [[SW1417 (line)]] | alt | 188 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +10.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[CFPAC-1 (line)]] | alt | 386 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 107 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 217 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 380 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 380 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 503 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 386 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 242 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 258 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 231 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 343 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 319 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1337), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARPC2]] | +0.67 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[SEPTIN10]] | +0.65 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[NT5E]] | +0.63 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[KPNA4]] | +0.63 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[ITGB1]] | +0.63 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[ACTR2]] | +0.62 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[ANXA5]] | +0.62 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[ITGA2]] | +0.62 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[CD59]] | +0.62 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[TPM3]] | +0.60 | +0.57 / +0.62 | both halves | 9e-06 |  |
| [[RALB]] | +0.60 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[ASPH]] | +0.60 | +0.55 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPIN2B]] | -0.58 | -0.40 / -0.62 | both halves | 5e-05 |  |
| [[NELFA]] | -0.58 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[PKDCC]] | -0.57 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[SAT2]] | -0.57 | -0.47 / -0.65 | both halves | 2e-05 |  |
| [[ATP5MC2]] | -0.55 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[CLN3]] | -0.55 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[SLC11A2]] | -0.55 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[THAP3]] | -0.55 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[EGFL8]] | -0.54 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[RPAIN]] | -0.54 | -0.51 / -0.61 | both halves | 1e-05 |  |
| [[MRPS24]] | -0.53 | -0.36 / -0.59 | both halves | 9e-05 |  |
| [[MORN4]] | -0.53 | -0.38 / -0.60 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EMP1]] | B | EMP1 activity raises BZW1's level | lines that do not express EMP1 (10) vs lines expressing it (40) | 1.23× lower at baseline in the lines without EMP1 | 0.051 | ⚠ within organs, on part of the lines |
| [[MAP2K1]] | B | MAP2K1 activity raises BZW1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CD59]] | B | CD59 activity raises BZW1's level | lines that do not express CD59 (7) vs lines expressing it (43) | 1.45× lower at baseline in the lines without CD59 | 0.061 | ⚠ within organs, on part of the lines; also absent: C11orf91, ENSG00000284969, MET; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.714). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (39.5, 6.4); signed map (-6.9, 37.9). **Vector** length 127, 51.6% of its response variance represented; |z| ≥ 3 in 1,716 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *apical junction* (hallmark, mean cos +0.53 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.5 | +8.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.6 | +2.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~76% of this change | +4.0 | +3.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.7 | +7.5 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +3.6 | +0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +3.8 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +2.8 | +0.9 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -7.1 | -0.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -6.6 | -3.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | -6.4 | -5.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -6.2 | -5.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -6.0 | -4.7 |
|  | [[venetoclax (drug)]] 5 µM |  | -5.9 | -1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -5.4 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | basic leucine zipper and W2 domains 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.1 — chr2:200,810,594-200,827,338 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BZAP45, KIAA0005, 5MP2 |
| Gene groups (HGNC) | Basic leucine zipper and W2 domains family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7L1Q6](https://www.uniprot.org/uniprotkb/Q7L1Q6) (eIF5-mimic protein 2):

> Translation initiation regulator which represses repeat-associated non-AUG (RAN) initiated translation probably by acting as a competitive inhibitor of eukaryotic translation initiation factor 5 (EIF5) function. Enhances histone H4 gene transcription but does not seem to bind DNA directly.

**Summary**, from NCBI Gene [9689](https://www.ncbi.nlm.nih.gov/gene/9689):

> Enables RNA binding activity and cadherin binding activity. Involved in regulation of translational initiation. Located in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18380](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18380) · Entrez [9689](https://www.ncbi.nlm.nih.gov/gene/9689) · UniProt [Q7L1Q6](https://www.uniprot.org/uniprotkb/Q7L1Q6) · Ensembl [ENSG00000082153](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000082153)

## Data

Gene col 1337: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1337); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1337, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1337]; `tensor/DDL_lfc|DDL_z.npy` [1337]; `embed/gene_vectors.npy` [1337]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1337 or target_col == 1337). Every well: [[BZW1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BZW1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
