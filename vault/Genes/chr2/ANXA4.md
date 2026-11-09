---
symbol: "ANXA4"
type: "gene"
col: 12314
ensembl_id: "ENSG00000196975"
name: "annexin A4"
location: "2p13.3"
module: 15
arm: "+"
pooled_cpm: 142.14
n_lines_expressing: 49
n_dd_up: 21
n_dd_down: 21
n_dd_up_clean: 16
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# ANXA4

*annexin A4* — 2p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.98× (z +21.9, q 0e+00, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.367× (z -22.7, q 0e+00, down in 46 of 47 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACTA2]] (+0.65, fdr 2e-05), [[DERA]] (+0.64, fdr 3e-05), [[RAB21]] (+0.63, fdr 3e-05); moves opposite to [[SLC39A3]] (-0.63, fdr 3e-05), [[ETV5]] (-0.61, fdr 3e-05), [[GPRIN1]] (-0.58, fdr 1e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12314.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.98×** | +21.9 | 0e+00 | 38/48 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.11×** | +16.9 | 0e+00 | 44/48 (AsPC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.07×** | +15.9 | 0e+00 | 38/43 (HT-29, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.58×** | +9.6 | 1e-19 | 29/44 (A-427, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +9.0 | 3e-17 | 32/47 (C32, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +8.8 | 2e-16 | 36/49 (NCI-H460, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +6.4 | 1e-08 | 27/47 (A-427, A-172, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.22×** | +6.1 | 9e-08 | 25/48 (AsPC-1, CFPAC-1, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.25×** | +5.6 | 2e-06 | 26/47 (AsPC-1, HepG2/C3A, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.18× | +5.2 | 9e-06 | 17/47 (AsPC-1, A549, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.27×** | +5.2 | 9e-06 | 24/46 (AsPC-1, A549, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.25×** | +5.1 | 2e-05 | 23/49 (AsPC-1, SW48, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.25×** | +5.1 | 2e-05 | 23/48 (AsPC-1, HepG2/C3A, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.21×** | +5.1 | 2e-05 | 19/47 (AsPC-1, HepG2/C3A, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.25×** | +4.9 | 4e-05 | 24/48 (AsPC-1, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.24×** | +4.8 | 5e-05 | 25/47 (AsPC-1, RKO, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.16× | +4.8 | 5e-05 | 17/47 (A-172, NCI-H2347, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.23×** | +4.4 | 2e-04 | 23/47 (AsPC-1, HepG2/C3A, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.21×** | +4.0 | 0.002 | 18/47 (AsPC-1, HepG2/C3A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12314.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.367×** | -22.7 | 0e+00 | 46/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.568×** | -18.1 | 0e+00 | 39/47 (A549, CFPAC-1, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.452×** | -18.0 | 0e+00 | 42/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.437×** | -16.9 | 0e+00 | 46/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.498×** | -15.8 | 0e+00 | 46/47 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.506×** | -15.4 | 0e+00 | 41/47 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.553×** | -12.1 | 8e-32 | 41/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.612×** | -11.1 | 7e-27 | 44/47 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.599×** | -10.5 | 6e-24 | 40/47 (LoVo, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.672×** | -8.5 | 1e-15 | 33/47 (COLO 205, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.683×** | -8.3 | 4e-15 | 32/47 (MIA PaCa-2, NCI-H460, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.697×** | -7.4 | 7e-12 | 36/47 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.702×** | -7.2 | 2e-11 | 38/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.727×** | -7.2 | 2e-11 | 30/47 (A549, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.744×** | -6.7 | 7e-10 | 32/47 (SW480, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.506×** | -6.5 | 3e-09 | 33/47 (SW480, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.506×** | -6.5 | 3e-09 | 32/48 (SW480, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.783×** | -5.5 | 1e-06 | 28/47 (COLO 205, CFPAC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.828×** | -3.1 | 0.057 | 13/48 (COLO 205, LS 180, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12314. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 164 | 14 (3 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.10× (z +18.1) ⚠ toxic; transcription drop · without an alert: [[Trametinib (drug)]] 0.5 µM 2.42× (z +11.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.319× (z -12.7) |
| [[NCI-H460 (line)]] | wt | 92.4 | 4 (1 ⚠) | 11 (7 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.28× (z +20.9) | [[Panobinostat (drug)]] 5 µM 0.346× (z -13.1) |
| [[LS 180 (line)]] | wt | 166 | 5 (2 ⚠) | 8 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +17.5) | [[Panobinostat (drug)]] 5 µM 0.315× (z -17.0) |
| [[HT-29 (line)]] | alt | 265 | 3 (3 ⚠) | 8 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +15.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -13.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.354× (z -13.0) |
| [[LOX-IMVI (line)]] | wt | 85.3 | 5 (1 ⚠) | 6 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +17.4) | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -15.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.295× (z -13.4) |
| [[PANC-1 (line)]] | alt | 132 | 3 (3 ⚠) | 8 (4 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.15× (z +13.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.405× (z -15.3) |
| [[SW480 (line)]] | alt | 148 | 0 | 11 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.160× (z -28.8) |
| [[A498 (line)]] | wt | 293 | 7 (4 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +13.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +12.3) | [[Ixazomib citrate (drug)]] 5 µM 0.433× (z -10.5) |
| [[A549 (line)]] | wt | 383 | 2 (2 ⚠) | 8 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.55× (z +11.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -23.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.223× (z -19.1) |
| [[LoVo (line)]] | wt | 224 | 0 | 10 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.207× (z -20.5) |
| [[HepG2_C3A (line)]] | wt | 134 | 1 | 8 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +11.4) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.287× (z -12.4) |
| [[A-427 (line)]] | wt | 116 | 5 (3 ⚠) | 3 (1 ⚠) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 1.85× (z +11.2) | [[Panobinostat (drug)]] 0.5 µM 0.443× (z -9.4) |
| [[CFPAC-1 (line)]] | alt | 335 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -17.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.309× (z -10.9) |
| [[HOP62 (line)]] | alt | 59.2 | 5 (2 ⚠) | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.52× (z +19.8) | [[Belinostat (drug)]] 5 µM 0.320× (z -10.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.324× (z -10.4) |
| [[KATO III (line)]] | alt | 210 | 2 (2 ⚠) | 6 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.43× (z +11.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.285× (z -16.5) |
| [[SNU-423 (line)]] | alt | 86.3 | 1 | 7 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +11.9) | [[Panobinostat (drug)]] 5 µM 0.225× (z -16.1) |
| [[A-172 (line)]] | wt | 190 | 7 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.85× (z +18.2) | — |
| [[COLO 205 (line)]] | alt | 358 | 0 | 7 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.238× (z -15.5) |
| [[HS-578T (line)]] | alt | 78.5 | 2 | 5 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +15.3) | [[Panobinostat (drug)]] 5 µM 0.269× (z -13.4) |
| [[RKO (line)]] | wt | 82.7 | 3 (1 ⚠) | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +14.4) | [[Belinostat (drug)]] 5 µM 0.275× (z -12.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.281× (z -12.4) |
| [[SW48 (line)]] | wt | 158 | 2 | 5 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.37× (z +12.1) | [[Panobinostat (drug)]] 5 µM 0.236× (z -15.0) |
| [[C32 (line)]] | wt | 88.7 | 5 (2 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.13× (z +21.5) | [[Homoharringtonine (drug)]] 5 µM 0.526× (z -9.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[H4 (line)]] | wt | 89.6 | 3 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.66× (z +14.0) | [[Panobinostat (drug)]] 0.5 µM 0.252× (z -9.4) |
| [[HEC-1-A (line)]] | alt | 149 | 2 (2 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.43× (z +11.6) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.414× (z -11.4) |
| [[NCI-H1573 (line)]] | alt | 80.0 | 2 (2 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.19× (z +13.4) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.383× (z -11.5) |
| [[MIA PaCa-2 (line)]] | alt | 136 | 1 | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.63× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.255× (z -17.1) |
| [[NCI-H23 (line)]] | alt | 107 | 1 | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +14.3) | [[Homoharringtonine (drug)]] 5 µM 0.527× (z -11.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.388× (z -10.5) |
| [[SNU-1 (line)]] | wt | 107 | 3 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.03× (z +13.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +11.2) | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -12.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.366× (z -9.4) |
| [[SW1417 (line)]] | alt | 182 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.383× (z -13.7) |
| [[BT-474 (line)]] | alt | 73.7 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +11.0) | [[Digitoxin (drug)]] 5 µM 0.296× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.421× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 74.5 | 3 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.10× (z +16.3) | [[Panobinostat (drug)]] 5 µM 0.334× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 160 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -16.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.336× (z -12.9) |
| [[NCI-H2030 (line)]] | alt | 134 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.12× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.551× (z -10.6) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SK-MEL-2 (line)]] | alt | 68.7 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -14.2) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW 900 (line)]] | alt | 43.4 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +11.6) | — |
| [[C-33 A (line)]] | alt | 68.8 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.07× (z +9.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +8.8) | — |
| [[HCT15 (line)]] | alt | 105 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.290× (z -11.6) |
| [[NCI-H1792 (line)]] | alt | 87.0 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +12.2) | — |
| [[NCI-H2347 (line)]] | alt | 81.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.529× (z -10.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.480× (z -8.8) |
| [[CHP-212 (line)]] | wt | 54.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.60× (z +8.9) | — |
| [[Hs 766T (line)]] | wt | 142 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.346× (z -10.8) |
| [[J82 (line)]] | alt | 47.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +11.0) | — |
| [[RPMI-7951 (line)]] | alt | 112 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +12.1) | — |
| [[SW 1088 (line)]] | alt | 125 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.130× (z -8.7) ⚠ cell-cycle shift, explains ~26% of this change |
| [[AN3 CA (line)]] | alt | 70.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.3 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 111 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12314), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACTA2]] | +0.65 | +0.53 / +0.46 | both halves | 2e-05 |  |
| [[DERA]] | +0.64 | +0.57 / +0.43 | both halves | 3e-05 |  |
| [[RAB21]] | +0.63 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[HOXB7]] | +0.63 | +0.53 / +0.33 | both halves | 1e-04 |  |
| [[MR1]] | +0.62 | +0.51 / +0.38 | both halves | 6e-05 |  |
| [[FAS]] | +0.62 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[KLF3-AS1]] | +0.60 | +0.50 / +0.38 | both halves | 7e-05 |  |
| [[C2orf76]] | +0.60 | +0.58 / +0.34 | both halves | 1e-04 |  |
| [[SPATA18]] | +0.60 | +0.49 / +0.42 | both halves | 4e-05 |  |
| [[DRAM1]] | +0.59 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[TCAIM]] | +0.59 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[TSTD3]] | +0.59 | +0.50 / +0.33 | both halves | 1e-04 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC39A3]] | -0.63 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[ETV5]] | -0.61 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[GPRIN1]] | -0.58 | -0.52 / -0.33 | both halves | 1e-04 |  |
| [[CCNE1]] | -0.56 | -0.54 / -0.40 | both halves | 4e-05 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[SMYD3]] | -0.56 | -0.38 / -0.32 | both halves | 1e-04 |  |
| [[C13orf46]] | -0.55 | -0.56 / -0.39 | both halves | 5e-05 |  |
| [[MIER2]] | -0.53 | -0.59 / -0.36 | both halves | 1e-04 |  |
| [[DGKD]] | -0.52 | -0.42 / -0.33 | both halves | 1e-04 |  |
| [[CBR1]] | -0.52 | -0.27 / -0.44 | both halves | 3e-04 |  |
| [[PHC2]] | -0.51 | -0.49 / -0.36 | both halves | 1e-04 |  |
| [[RASA3]] | -0.51 | -0.46 / -0.29 | both halves | 3e-04 |  |
| [[ENTPD7]] | -0.51 | -0.51 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ANXA4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[POU5F1]] | B | POU5F1 activity raises ANXA4's level | lines that do not express POU5F1 (27) vs lines expressing it (23) | 1.70× lower at baseline in the lines without POU5F1 | 0.042 | ⚠ within organs, on part of the lines; also absent: P2RY2, C4BPB, UGT1A6 |
| [[MAP2K1]] | B | MAP2K1 activity lowers ANXA4's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.465). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-0.4, 19.2); signed map (37.4, -23.1). **Vector** length 120, 42.9% of its response variance represented; |z| ≥ 3 in 1,651 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +10.6 | +9.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +9.9 | +8.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.5 | +21.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.8 | +6.4 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +5.3 | +5.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.6 | +5.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.5 | +5.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.4 | +4.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +4.3 | +5.1 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -8.7 | -16.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -8.6 | -22.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -7.7 | -15.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.0 | -7.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | -4.0 | -6.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.8 | -10.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -5.5 |
|  | [[vincristine (drug)]] 0.5 µM |  | -2.2 | -0.9 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | -2.0 | -0.1 |
|  | [[Raltitrexed (drug)]] 0.5 µM |  | -1.9 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | annexin A4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.3 — chr2:69,644,425-69,827,112 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ANX4 |
| Gene groups (HGNC) | Annexins |
| Hallmark sets | UV_RESPONSE_DN, IL2_STAT5_SIGNALING |
| Matched by | ensembl_id |

**Function**, from UniProt [P09525](https://www.uniprot.org/uniprotkb/P09525) (Annexin A4):

> Calcium/phospholipid-binding protein which promotes membrane fusion and is involved in exocytosis.

**Summary**, from NCBI Gene [307](https://www.ncbi.nlm.nih.gov/gene/307):

> Annexin IV (ANX4) belongs to the annexin family of calcium-dependent phospholipid binding proteins. Although their functions are still not clearly defined, several members of the annexin family have been implicated in membrane-related events along exocytotic and endocytotic pathways. ANX4 has 45 to 59% identity with other members of its family and shares a similar size and exon-intron organization. Isolated from human placenta, ANX4 encodes a protein that has possible interactions with ATP, and …

**Accessions** — [HGNC:542](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:542) · Entrez [307](https://www.ncbi.nlm.nih.gov/gene/307) · UniProt [P09525](https://www.uniprot.org/uniprotkb/P09525) · Ensembl [ENSG00000196975](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196975)

## Data

Gene col 12314: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12314); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12314, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12314]; `tensor/DDL_lfc|DDL_z.npy` [12314]; `embed/gene_vectors.npy` [12314]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12314 or target_col == 12314). Every well: [[ANXA4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANXA4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
