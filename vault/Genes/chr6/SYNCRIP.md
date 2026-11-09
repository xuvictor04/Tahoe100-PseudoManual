---
symbol: "SYNCRIP"
type: "gene"
col: 5680
ensembl_id: "ENSG00000135316"
name: "synaptotagmin binding cytoplasmic RNA interacting protein"
location: "6q14.3"
module: 3
arm: "-"
pooled_cpm: 239.36
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 10
n_dd_up_clean: 5
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# SYNCRIP

*synaptotagmin binding cytoplasmic RNA interacting protein* — 6q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.78× (z +14.7, q 0e+00, up in 45 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.78× (z +13.6, q 8e-40, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.581× (z -13.8, q 9e-41, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EIF4G1]] (+0.73, fdr 7e-06), [[HNRNPD]] (+0.71, fdr 7e-06), [[NCL]] (+0.67, fdr 1e-05); moves opposite to [[BLVRB]] (-0.66, fdr 7e-06), [[RNF181]] (-0.66, fdr 2e-05), [[ATP6V1F]] (-0.64, fdr 1e-05).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5680.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.78×** | +14.7 | 0e+00 | 45/49 (SW480, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.78×** | +13.6 | 8e-40 | 47/49 (PANC-1, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.50×** | +12.2 | 5e-32 | 44/48 (PANC-1, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.45×** | +9.4 | 8e-19 | 42/48 (PANC-1, LS 180, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.46×** | +9.3 | 2e-18 | 33/44 (NCI-H1792, SNU-423, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **1.29×** | +9.1 | 9e-18 | 31/48 (A498, C32, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.43×** | +8.4 | 3e-15 | 39/45 (SW480, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.39×** | +8.3 | 6e-15 | 37/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.38×** | +8.3 | 9e-15 | 34/48 (HOP62, HT-29, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.36×** | +7.8 | 5e-13 | 36/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.35×** | +7.7 | 6e-13 | 40/48 (NCI-H1792, HT-29, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.34×** | +7.5 | 4e-12 | 33/48 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.48×** | +5.3 | 6e-06 | 27/38 (NCI-H1573, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **1.22×** | +4.9 | 3e-05 | 24/47 (NCI-H1792, COLO 205, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.19× | +4.4 | 4e-04 | 21/48 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.37×** | +4.2 | 1e-03 | 29/48 (CFPAC-1, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.32×** | +3.7 | 0.009 | 25/48 (Hs 766T, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.09× | +3.2 | 0.043 | 2/49 (MIA PaCa-2, NCI-H460) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.27×** | +3.2 | 0.045 | 20/48 (NCI-H1792, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | 1.14× | +3.1 | 0.050 | 10/48 (PANC-1, LoVo, …) | all doses, flat |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.052 | 16/48 (NCI-H460, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Mifepristone (drug)]] 0.05 µM |  | 1.14× | +3.1 | 0.053 | 9/47 (KATO III, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5680.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.581×** | -13.8 | 9e-41 | 46/48 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.614×** | -12.4 | 5e-33 | 44/48 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.676×** | -10.0 | 4e-21 | 40/48 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.807×** | -7.7 | 2e-12 | 27/48 (J82, LS 180, …) | rises with dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.759×** | -7.0 | 2e-10 | 40/48 (HEC-1-A, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.796×** | -5.8 | 5e-07 | 30/48 (KATO III, LoVo, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.799×** | -5.7 | 9e-07 | 34/48 (BT-474, A549, …) | two highest doses | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.815×** | -5.0 | 4e-05 | 25/47 (SK-MEL-2, C32, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.709×** | -4.6 | 3e-04 | 30/49 (PANC-1, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.847× | -4.2 | 0.001 | 18/48 (KATO III, J82, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.887× | -4.2 | 0.002 | 9/48 (NCI-H23, SW480, …) | all doses, flat |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.850× | -4.1 | 0.002 | 8/49 (A-427, HT-29, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.863× | -3.8 | 0.008 | 13/49 (LoVo, SW480, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.902× | -3.6 | 0.012 | 6/49 (NCI-H23, MIA PaCa-2, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.905× | -3.6 | 0.012 | 7/48 (SK-MEL-2, SW1417, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.891× | -3.4 | 0.023 | 13/48 (NCI-H23, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.885× | -3.1 | 0.051 | 13/47 (C32, SW480, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.884× | -3.0 | 0.071 | 18/48 (LoVo, Hs 766T, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5680. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 288 | 10 (8 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +19.2) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 3.06× (z +10.2) | [[Panobinostat (drug)]] 5 µM 0.559× (z -10.2) |
| [[PANC-1 (line)]] | alt | 286 | 9 (7 ⚠) | 3 | [[Digitoxin (drug)]] 0.5 µM 2.04× (z +14.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 3.51× (z +13.6) | [[Panobinostat (drug)]] 5 µM 0.485× (z -14.9) |
| [[NCI-H1573 (line)]] | alt | 147 | 7 (5 ⚠) | 3 | [[Digitoxin (drug)]] 5 µM 1.98× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.57× (z +10.6) | [[Panobinostat (drug)]] 5 µM 0.521× (z -10.4) |
| [[NCI-H1792 (line)]] | alt | 211 | 10 (9 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +17.6) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.46× (z +9.2) | — |
| [[LS 180 (line)]] | wt | 293 | 5 (3 ⚠) | 4 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.48× (z +13.9) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 3.21× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.512× (z -10.4) |
| [[HOP62 (line)]] | alt | 214 | 6 (4 ⚠) | 2 | [[Homoharringtonine (drug)]] 0.5 µM 2.06× (z +12.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 2.83× (z +9.7) | [[Panobinostat (drug)]] 5 µM 0.546× (z -10.8) |
| [[KATO III (line)]] | alt | 287 | 5 (5 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.45× (z +15.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.540× (z -10.5) |
| [[NCI-H460 (line)]] | wt | 192 | 8 (8 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.68× (z +15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[AsPC-1 (line)]] | alt | 207 | 5 (4 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.26× (z +12.1) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.91× (z +10.5) | [[Panobinostat (drug)]] 5 µM 0.498× (z -10.3) |
| [[SK-MEL-2 (line)]] | alt | 227 | 3 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.12× (z +11.3) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.19× (z +9.1) | [[Panobinostat (drug)]] 0.5 µM 0.436× (z -12.5) |
| [[HEC-1-A (line)]] | alt | 298 | 2 | 4 | [[PH-797804 (drug)]] 5 µM 3.20× (z +10.5) | [[Panobinostat (drug)]] 0.5 µM 0.422× (z -15.0) |
| [[HT-29 (line)]] | alt | 239 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.46× (z +14.3) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 2.78× (z +8.5) | — |
| [[LOX-IMVI (line)]] | wt | 257 | 6 (4 ⚠) | 0 | [[PH-797804 (drug)]] 5 µM 4.11× (z +10.6) | — |
| [[A498 (line)]] | wt | 164 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.42× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Panobinostat (drug)]] 5 µM 0.595× (z -8.6) |
| [[J82 (line)]] | alt | 269 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.95× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Selinexor (drug)]] 5 µM 0.618× (z -12.1) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.523× (z -11.5) |
| [[LoVo (line)]] | wt | 254 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.33× (z +14.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.564× (z -9.9) |
| [[NCI-H23 (line)]] | alt | 352 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.05× (z +10.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.424× (z -12.9) |
| [[Panc 03.27 (line)]] | alt | 172 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.51× (z +13.8) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 3.64× (z +10.1) | — |
| [[SW48 (line)]] | wt | 259 | 2 | 3 | [[TAK-901 (drug)]] 0.05 µM 3.80× (z +14.2) | [[Panobinostat (drug)]] 5 µM 0.324× (z -12.7) |
| [[A-427 (line)]] | wt | 264 | 2 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 1.78× (z +9.3) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 2.94× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.525× (z -10.5) |
| [[BT-474 (line)]] | alt | 263 | 1 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 2.78× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.479× (z -12.4) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.481× (z -12.4) |
| [[Hs 766T (line)]] | wt | 165 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.17× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.14× (z +9.6) | — |
| [[SNU-423 (line)]] | alt | 276 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +16.8) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 2.88× (z +9.2) | — |
| [[A549 (line)]] | wt | 171 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.27× (z +11.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.641× (z -8.9) ⚠ cell-cycle shift, explains ~12% of this change |
| [[HS-578T (line)]] | alt | 240 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.08× (z +10.7) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 421 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.05× (z +10.0) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 3.73× (z +9.6) | — |
| [[A-172 (line)]] | wt | 186 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 1.87× (z +10.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.613× (z -8.5) |
| [[C32 (line)]] | wt | 210 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +11.3) ⚠ cell-cycle shift, explains ~81% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 5.05× (z +10.8) | — |
| [[COLO 205 (line)]] | alt | 117 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +13.2) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 6.88× (z +10.6) | — |
| [[RKO (line)]] | wt | 193 | 2 (1 ⚠) | 0 | [[PH-797804 (drug)]] 5 µM 4.26× (z +10.7) | — |
| [[RPMI-7951 (line)]] | alt | 293 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 3.44× (z +9.2) | — |
| [[SW1417 (line)]] | alt | 201 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 2.85× (z +9.5) | — |
| [[C-33 A (line)]] | alt | 327 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.516× (z -9.9) |
| [[CFPAC-1 (line)]] | alt | 160 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.04× (z +9.0) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[H4 (line)]] | wt | 161 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 2.30× (z +8.7) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[HCT15 (line)]] | alt | 346 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.511× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 320 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.36× (z +9.1) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[SHP-77 (line)]] | alt | 214 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.82× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 317 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.20× (z +10.2) | — |
| [[SW 1088 (line)]] | alt | 189 | 0 | 1 | — | [[5-Azacytidine (drug)]] 5 µM 0.212× (z -8.7) |
| [[SW 900 (line)]] | alt | 195 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.16× (z +8.6) | — |
| [[AN3 CA (line)]] | alt | 277 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 288 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 142 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 219 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 199 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 204 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 224 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 273 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 254 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5680), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*50 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4G1]] | +0.73 | +0.68 / +0.75 | both halves | 7e-06 | STRING 758 |
| [[HNRNPD]] | +0.71 | +0.70 / +0.69 | both halves | 7e-06 | same gene group; pathway: HALLMARK_E2F_TARGETS; STRING 980 |
| [[NCL]] | +0.67 | +0.53 / +0.65 | both halves | 1e-05 | same gene group; pathway: HALLMARK_G2M_CHECKPOINT; STRING 587 |
| [[NCBP1]] | +0.65 | +0.63 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 473 |
| [[NOLC1]] | +0.65 | +0.61 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 478 |
| [[FAM120A]] | +0.64 | +0.48 / +0.72 | both halves | 2e-05 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 749 |
| [[IPO4]] | +0.63 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[SRSF1]] | +0.62 | +0.51 / +0.63 | both halves | 1e-05 | same gene group; pathway: HALLMARK_E2F_TARGETS; STRING 917 |
| [[HNRNPM]] | +0.62 | +0.49 / +0.67 | both halves | 1e-05 | same gene group; STRING 876 |
| [[DHX15]] | +0.62 | +0.51 / +0.69 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 819 |
| [[GSPT1]] | +0.62 | +0.49 / +0.69 | both halves | 1e-05 | pathway: HALLMARK_E2F_TARGETS |
| [[HNRNPR]] | +0.61 | +0.51 / +0.69 | both halves | 1e-05 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 956 |

## Genes that move opposite

*50 of its nearest partners move opposite, 7 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BLVRB]] | -0.66 | -0.64 / -0.65 | both halves | 7e-06 |  |
| [[RNF181]] | -0.66 | -0.48 / -0.66 | both halves | 2e-05 |  |
| [[ATP6V1F]] | -0.64 | -0.49 / -0.66 | both halves | 1e-05 |  |
| [[POLR2J]] ⚠ | -0.63 | -0.55 / -0.63 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[BSDC1]] | -0.63 | -0.60 / -0.58 | both halves | 7e-06 |  |
| [[IFI27L2]] | -0.61 | -0.46 / -0.64 | both halves | 2e-05 |  |
| [[FTL]] | -0.61 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[MIEN1]] | -0.61 | -0.49 / -0.66 | both halves | 1e-05 |  |
| [[JOSD2]] | -0.60 | -0.37 / -0.65 | both halves | 8e-05 |  |
| [[LSM10]] | -0.59 | -0.34 / -0.66 | both halves | 1e-04 |  |
| [[ATP6V0B]] | -0.59 | -0.43 / -0.60 | both halves | 4e-05 |  |
| [[RPP21]] | -0.59 | -0.32 / -0.67 | both halves | 2e-04 |  |
| [[GABARAPL2]] | -0.58 | -0.48 / -0.63 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.551). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-38.0, -25.5); signed map (-6.5, -43.9). **Vector** length 104, 38.1% of its response variance represented; |z| ≥ 3 in 1,469 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *mRNA 3'-end processing* (reactome, mean cos +0.53 to 12); *mRNA Polyadenylation* (reactome, mean cos +0.54 to 11); *mRNA Splicing - Major Pathway* (reactome, mean cos +0.54 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.6 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.5 | +14.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +6.3 | +9.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.4 | +7.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.8 | +12.2 |
|  | [[EX229 (drug)]] 5 µM |  | +3.4 | +3.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.9 | +4.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +2.8 | +1.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.6 | +0.0 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~78% of this change | -7.2 | -3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.5 | -0.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -5.9 | +0.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | -0.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | -4.0 | +7.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | -0.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.4 | -3.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.3 | -2.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.1 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | synaptotagmin binding cytoplasmic RNA interacting protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q14.3 — chr6:85,607,779-85,644,063 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NSAP1, GRY-RBP, dJ3J17.2, HNRPQ1, hnRNP-Q, HNRNPQ |
| Gene groups (HGNC) | RNA binding motif containing; Heterogeneous nuclear ribonucleoproteins |
| Hallmark sets | G2M_CHECKPOINT, E2F_TARGETS, MYC_TARGETS_V1 |
| Matched by | ensembl_id |

**Function**, from UniProt [O60506](https://www.uniprot.org/uniprotkb/O60506) (Heterogeneous nuclear ribonucleoprotein Q):

> Heterogeneous nuclear ribonucleoprotein (hnRNP) implicated in mRNA processing mechanisms. Component of the CRD-mediated complex that promotes MYC mRNA stability. Isoform 1, isoform 2 and isoform 3 are associated in vitro with pre-mRNA, splicing intermediates and mature mRNA protein complexes. Isoform 1 binds to apoB mRNA AU-rich sequences. Isoform 1 is part of the APOB mRNA editosome complex and may modulate the postranscriptional C to U RNA-editing of the APOB mRNA through either by binding to …

**Summary**, from NCBI Gene [10492](https://www.ncbi.nlm.nih.gov/gene/10492):

> This gene encodes a member of the cellular heterogeneous nuclear ribonucleoprotein (hnRNP) family. hnRNPs are RNA binding proteins that complex with heterogeneous nuclear RNA (hnRNA) and regulate alternative splicing, polyadenylation, and other aspects of mRNA metabolism and transport. The encoded protein plays a role in multiple aspects of mRNA maturation and is associated with several multiprotein complexes including the apoB RNA editing-complex and survival of motor neurons (SMN) complex. …

**Accessions** — [HGNC:16918](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16918) · Entrez [10492](https://www.ncbi.nlm.nih.gov/gene/10492) · UniProt [O60506](https://www.uniprot.org/uniprotkb/O60506) · Ensembl [ENSG00000135316](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135316)

## Data

Gene col 5680: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5680); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5680, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5680]; `tensor/DDL_lfc|DDL_z.npy` [5680]; `embed/gene_vectors.npy` [5680]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5680 or target_col == 5680). Every well: [[SYNCRIP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SYNCRIP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
