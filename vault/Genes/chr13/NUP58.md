---
symbol: "NUP58"
type: "gene"
col: 6309
ensembl_id: "ENSG00000139496"
name: "nucleoporin 58"
location: "13q12.13"
module: 105
arm: "+"
pooled_cpm: 245.44
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 25
n_dd_up_clean: 14
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/105"]
generated_by: "tahoemap"
---

# NUP58

*nucleoporin 58* — 13q12.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 3.47× (z +12.9, q 3e-35, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.518× (z -6.5, q 3e-08, down in 40 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Trametinib (drug)]] 0.5 µM: 0.715× (z -4.0, q 0.009, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM210A]] (+0.68, fdr 7e-06), [[BTAF1]] (+0.65, fdr 7e-06), [[PDXP]] (+0.65, fdr 1e-05); moves opposite to [[C11orf58]] (-0.53, fdr 2e-05), [[TACC2]] (-0.51, fdr 5e-05), [[RNF115]] (-0.50, fdr 3e-05).
> It is in [[Module 105]], a single-armed module (Late Phase of HIV Life Cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6309.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.47×** | +12.9 | 3e-35 | 48/48 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.01×** | +11.4 | 1e-27 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.66×** | +10.1 | 8e-22 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.98×** | +10.0 | 2e-21 | 42/48 (COLO 205, HT-29, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **5.32×** | +9.0 | 2e-17 | 49/49 (COLO 205, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.27×** | +8.5 | 2e-15 | 45/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **3.04×** | +6.0 | 1e-07 | 43/48 (COLO 205, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.71×** | +5.5 | 2e-06 | 38/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.58×** | +4.7 | 1e-04 | 35/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | **2.37×** | +4.7 | 2e-04 | 44/48 (SHP-77, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.82×** | +4.4 | 5e-04 | 46/48 (HT-29, LoVo, …) | two highest doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.49×** | +4.1 | 0.002 | 38/48 (HT-29, Hs 766T, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.49×** | +4.1 | 0.002 | 33/48 (NCI-H460, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.44×** | +3.8 | 0.006 | 31/48 (COLO 205, LoVo, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.93×** | +3.6 | 0.013 | 24/38 (A-172, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Tomivosertib (drug)]] 5 µM |  | **1.82×** | +3.2 | 0.040 | 35/48 (NCI-H1573, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +3.2 | 0.040 | 28/48 (LoVo, HT-29, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.24×** | +3.2 | 0.049 | 28/49 (CFPAC-1, CHP-212, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.78×** | +3.1 | 0.054 | 36/48 (HT-29, LoVo, …) | two highest doses | noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.35×** | +3.0 | 0.070 | 30/49 (NCI-H460, SK-MEL-2, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6309.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.518×** | -6.5 | 3e-08 | 40/44 (SK-MEL-2, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.880× | -4.7 | 6e-04 | 5/50 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.637×** | -4.6 | 6e-04 | 39/49 (NCI-H2347, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.753×** | -4.1 | 0.005 | 29/48 (A-427, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.715×** | -4.0 | 0.009 | 37/48 (A-427, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.700×** | -3.7 | 0.021 | 38/47 (SW480, C32, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.702×** | -3.6 | 0.021 | 35/48 (KATO III, PANC-1, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.779×** | -3.5 | 0.025 | 29/49 (C32, HCT15, …) | all doses, flat | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.785×** | -3.5 | 0.025 | 34/48 (HEC-1-A, HepG2/C3A, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.702×** | -3.5 | 0.025 | 32/48 (NCI-H2347, RKO, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.715×** | -3.5 | 0.027 | 33/48 (KATO III, BT-474, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.716×** | -3.4 | 0.027 | 36/48 (SW 1271, HOP62, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.708×** | -3.4 | 0.027 | 31/47 (NCI-H2347, SW480, …) | all doses, stronger at high dose |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.722×** | -3.4 | 0.032 | 33/49 (NCI-H2347, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Apalutamide (drug)]] 0.5 µM |  | **0.727×** | -3.3 | 0.037 | 33/48 (NCI-H1792, NCI-H1573, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.642×** | -3.3 | 0.039 | 35/48 (A-427, HEC-1-A, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | **0.801×** | -3.2 | 0.040 | 33/48 (KATO III, SW1417, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.799×** | -3.2 | 0.044 | 30/48 (NCI-H2347, SW480, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.730×** | -3.1 | 0.051 | 27/48 (NCI-H2347, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6309. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 183 | 11 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.26× (z +23.4) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 8.20× (z +18.9) | — |
| [[NCI-H460 (line)]] | wt | 272 | 9 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 8.99× (z +18.2) | — |
| [[SW480 (line)]] | alt | 213 | 8 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.14× (z +18.9) | — |
| [[BT-474 (line)]] | alt | 174 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +11.2) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.31× (z +10.4) | — |
| [[HT-29 (line)]] | alt | 253 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +15.5) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.00× (z +10.9) | — |
| [[LoVo (line)]] | wt | 166 | 7 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.18× (z +17.5) | — |
| [[NCI-H1573 (line)]] | alt | 182 | 6 (2 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 10.1× (z +16.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 10.1× (z +16.6) | [[Dinaciclib (drug)]] 5 µM 0.221× (z -10.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 215 | 7 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.01× (z +16.4) | — |
| [[SW 900 (line)]] | alt | 285 | 6 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +13.6) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.78× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.300× (z -8.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 371 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.24× (z +11.8) | — |
| [[HOP62 (line)]] | alt | 263 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.00× (z +13.0) | — |
| [[Hs 766T (line)]] | wt | 209 | 5 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.69× (z +13.2) | — |
| [[J82 (line)]] | alt | 433 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.52× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.297× (z -10.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 248 | 5 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 7.36× (z +10.7) | — |
| [[AsPC-1 (line)]] | alt | 259 | 4 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.80× (z +12.9) | — |
| [[HepG2_C3A (line)]] | wt | 204 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.02× (z +13.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.79× (z +12.8) | — |
| [[NCI-H1792 (line)]] | alt | 154 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.54× (z +14.7) | — |
| [[Panc 03.27 (line)]] | alt | 191 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +13.7) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.79× (z +9.6) | — |
| [[SNU-423 (line)]] | alt | 147 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +14.4) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.97× (z +10.6) | — |
| [[KATO III (line)]] | alt | 183 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.78× (z +13.2) | — |
| [[NCI-H2347 (line)]] | alt | 240 | 1 | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.94× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.334× (z -9.4) ⚠ toxic; transcription drop · without an alert: [[Belumosudil (drug)]] 5 µM 0.339× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 251 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +13.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.93× (z +9.0) | — |
| [[C-33 A (line)]] | alt | 384 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -13.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 438 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.357× (z -9.8) ⚠ cell-cycle shift, explains ~66% of this change |
| [[H4 (line)]] | wt | 214 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.26× (z +9.2) | — |
| [[hTERT-HPNE (line)]] | wt | 265 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +10.0) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.40× (z +9.5) | — |
| [[LS 180 (line)]] | wt | 185 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.56× (z +13.5) | — |
| [[NCI-H2030 (line)]] | alt | 258 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.67× (z +9.2) | — |
| [[SK-MEL-2 (line)]] | alt | 156 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.164× (z -15.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 145 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.77× (z +9.9) | — |
| [[A-172 (line)]] | wt | 177 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +12.0) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[A-427 (line)]] | wt | 257 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.514× (z -11.2) ⚠ cell-cycle shift, explains ~66% of this change |
| [[A498 (line)]] | wt | 205 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +10.4) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[A549 (line)]] | wt | 227 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +9.1) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[HS-578T (line)]] | alt | 167 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +9.4) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[SW 1088 (line)]] | alt | 179 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.0664× (z -10.5) |
| [[SW48 (line)]] | wt | 306 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.59× (z +10.1) | — |
| [[AN3 CA (line)]] | alt | 242 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 244 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 242 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 351 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 253 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 513 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 308 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 235 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 285 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 239 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 420 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 297 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 400 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6309), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM210A]] | +0.68 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[BTAF1]] | +0.65 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[PDXP]] | +0.65 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[WDR45B]] | +0.65 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[UBA6]] | +0.63 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[INSIG2]] | +0.63 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[USP37]] | +0.62 | +0.63 / +0.58 | both halves | 8e-06 |  |
| [[ANKRD37]] | +0.62 | +0.68 / +0.45 | both halves | 3e-05 |  |
| [[CHSY1]] | +0.61 | +0.63 / +0.58 | both halves | 7e-06 | pathway: Metabolism of carbohydrates and carbohydrate derivatives |
| [[PDK3]] | +0.61 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[POM121C]] | +0.61 | +0.66 / +0.58 | both halves | 7e-06 | pathway: Antimicrobial mechanism of IFN-stimulated genes; STRING 804 |
| [[HK2]] | +0.60 | +0.57 / +0.53 | both halves | 1e-05 | pathway: Glucose metabolism |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C11orf58]] | -0.53 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[TACC2]] | -0.51 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[RNF115]] | -0.50 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[POLR3C]] | -0.50 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[UBQLN2]] | -0.49 | -0.52 / -0.38 | both halves | 7e-05 |  |
| [[ELF1]] | -0.48 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[CPLANE1]] | -0.48 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[USP47]] | -0.48 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[EXOSC10]] | -0.47 | -0.41 / -0.33 | both halves | 1e-04 |  |
| [[ZFTA]] | -0.47 | -0.57 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises NUP58's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 105]] — Late Phase of HIV Life Cycle; 44 genes; every member is in the + arm (projection on the module's main direction 0.704). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.3, -17.3); signed map (-38.7, 23.9). **Vector** length 102, 49.8% of its response variance represented; |z| ≥ 3 in 1,506 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +1.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.7 | +0.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.2 | +0.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.9 | +1.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | +2.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.3 | +4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +3.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.5 | +1.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.5 | +3.1 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -7.9 | +1.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -7.1 | -0.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.6 | +2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.9 | +1.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | -5.0 | -4.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.8 | +6.0 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -3.1 | -2.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.1 | -0.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.9 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | nucleoporin 58 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q12.13 — chr13:25,301,524-25,365,390 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0410, NUP45; previously NUPL1 |
| Gene groups (HGNC) | Nucleoporins |
| Hallmark sets | UV_RESPONSE_UP |
| Reactome | 73 pathways, smallest: Postmitotic nuclear pore complex (NPC) reformation; IP3 and IP4 transport between cytosol and nucleus; IP6 and IP7 transport between cytosol and nucleus |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BVL2](https://www.uniprot.org/uniprotkb/Q9BVL2) (Nucleoporin p58/p45):

> Component of the nuclear pore complex, a complex required for the trafficking across the nuclear membrane.

**Summary**, from NCBI Gene [9818](https://www.ncbi.nlm.nih.gov/gene/9818):

> This gene encodes a member of the nucleoporin family that shares 87% sequence identity with rat nucleoporin p58. The protein is localized to the nuclear rim and is a component of the nuclear pore complex (NPC). All molecules entering or leaving the nucleus either diffuse through or are actively transported by the NPC. Alternate transcriptional splice variants, encoding different isoforms, have been characterized. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:20261](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20261) · Entrez [9818](https://www.ncbi.nlm.nih.gov/gene/9818) · UniProt [Q9BVL2](https://www.uniprot.org/uniprotkb/Q9BVL2) · Ensembl [ENSG00000139496](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139496)

## Data

Gene col 6309: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6309); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6309, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6309]; `tensor/DDL_lfc|DDL_z.npy` [6309]; `embed/gene_vectors.npy` [6309]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6309 or target_col == 6309). Every well: [[NUP58 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUP58.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
