---
symbol: "EGR1"
type: "gene"
col: 4217
ensembl_id: "ENSG00000120738"
name: "early growth response 1"
location: "5q31.2"
module: 109
arm: "+"
pooled_cpm: 274.25
n_lines_expressing: 48
n_dd_up: 13
n_dd_down: 52
n_dd_up_clean: 8
n_dd_down_clean: 43
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/109"]
generated_by: "tahoemap"
---

# EGR1

*early growth response 1* — 5q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 16.1× (z +30.2, q 0e+00, up in 46 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 52 drug-doses (9 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.0643× (z -20.5, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EGR2]] (+0.90, fdr 7e-06), [[EGR3]] (+0.90, fdr 7e-06), [[IER2]] (+0.90, fdr 7e-06); moves opposite to [[FHIP2A]] (-0.69, fdr 7e-06), [[HINT1]] (-0.61, fdr 1e-05), [[SNX4]] (-0.60, fdr 1e-05).
> It is in [[Module 109]], a single-armed module (immediate early).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4217.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **16.1×** | +30.2 | 0e+00 | 46/46 (C32, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **13.4×** | +19.2 | 0e+00 | 46/46 (NCI-H1573, C32, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **5.13×** | +12.6 | 5e-34 | 46/46 (C32, SW48, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **4.83×** | +12.1 | 1e-31 | 46/47 (SK-MEL-2, HS-578T, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **5.03×** | +12.0 | 6e-31 | 39/42 (HS-578T, C32, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.38×** | +6.7 | 2e-09 | 41/46 (AsPC-1, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~25% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.25×** | +6.3 | 3e-08 | 33/46 (C32, NCI-H460, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.13×** | +5.8 | 4e-07 | 38/46 (SK-MEL-2, AsPC-1, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **2.23×** | +5.7 | 7e-07 | 34/43 (SK-MEL-2, HS-578T, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **5.52×** | +5.6 | 1e-06 | 41/47 (BT-474, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.51×** | +4.5 | 3e-04 | 38/46 (HEC-1-A, SW 900, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.49×** | +3.1 | 0.098 | 25/46 (SK-MEL-2, HEC-1-A, …) | top dose only |  |
| [[Hesperidin (drug)]] 0.05 µM |  | **1.53×** | +3.1 | 0.098 | 28/46 (NCI-H1573, SHP-77, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 52 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 52 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4217.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.0643×** | -20.5 | 0e+00 | 48/48 (SW48, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); noisy plate (z scaled); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.0754×** | -19.1 | 0e+00 | 45/45 (NCI-H23, SHP-77, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.106×** | -17.2 | 0e+00 | 47/47 (SW48, C32, …) | all doses, flat | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **0.173×** | -16.9 | 0e+00 | 46/46 (SW48, SHP-77, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.103×** | -16.8 | 0e+00 | 46/46 (SW48, NCI-H23, …) | all doses, flat | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.0979×** | -16.5 | 0e+00 | 46/46 (NCI-H23, SHP-77, …) | all doses, flat | position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **0.217×** | -16.5 | 0e+00 | 46/46 (NCI-H23, SHP-77, …) | all doses, stronger at high dose | position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.179×** | -13.2 | 6e-38 | 44/45 (C32, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.271×** | -10.6 | 3e-24 | 46/47 (C32, SHP-77, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.370×** | -7.6 | 1e-12 | 41/46 (LOX-IMVI, A-427, …) | rises with dose | position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.453×** | -7.3 | 1e-11 | 44/46 (MIA PaCa-2, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.369×** | -7.2 | 2e-11 | 43/46 (C32, MIA PaCa-2, …) | all doses, flat |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.112×** | -7.2 | 3e-11 | 46/46 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.133×** | -6.6 | 1e-09 | 45/48 (NCI-H23, SW48, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **0.555×** | -6.4 | 6e-09 | 36/46 (C32, SW48, …) | rises with dose | low cells (technical?) |
| [[BI-3406 (drug)]] 5 µM |  | **0.167×** | -5.9 | 1e-07 | 37/46 (NCI-H23, SHP-77, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.93 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4217. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 427 | 7 (3 ⚠) | 19 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 35.3× (z +34.9) | [[Cobimetinib (drug)]] 0.5 µM 0.0251× (z -25.5) |
| [[MIA PaCa-2 (line)]] | alt | 330 | 6 (3 ⚠) | 17 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 12.2× (z +25.7) | [[Adagrasib (drug)]] 0.05 µM 0.295× (z -30.9) ⚠ position not correctable · without an alert: [[Cobimetinib (drug)]] 5 µM 0.0398× (z -22.7) |
| [[SW48 (line)]] | wt | 820 | 8 (4 ⚠) | 14 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 11.8× (z +28.0) | [[Trametinib (drug)]] 5 µM 0.0225× (z -30.0) |
| [[AsPC-1 (line)]] | alt | 371 | 12 (8 ⚠) | 9 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 21.6× (z +31.2) | [[Cobimetinib (drug)]] 5 µM 0.0345× (z -23.2) |
| [[A-427 (line)]] | wt | 277 | 4 (1 ⚠) | 16 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.07× (z +16.3) | [[Cobimetinib (drug)]] 5 µM 0.0416× (z -21.8) |
| [[NCI-H23 (line)]] | alt | 580 | 2 | 17 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.60× (z +18.3) | [[Cobimetinib (drug)]] 5 µM 0.0202× (z -28.5) |
| [[NCI-H460 (line)]] | wt | 186 | 11 (7 ⚠) | 7 | [[Homoharringtonine (drug)]] 5 µM 52.5× (z +27.8) | [[Cobimetinib (drug)]] 5 µM 0.0886× (z -11.5) |
| [[SK-MEL-2 (line)]] | alt | 96.4 | 12 (6 ⚠) | 6 | [[Homoharringtonine (drug)]] 5 µM 50.7× (z +28.0) | [[Trametinib (drug)]] 0.5 µM 0.118× (z -13.3) |
| [[NCI-H1573 (line)]] | alt | 517 | 6 (3 ⚠) | 11 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 27.5× (z +29.5) | [[Cobimetinib (drug)]] 5 µM 0.0218× (z -23.2) |
| [[HOP62 (line)]] | alt | 556 | 4 (1 ⚠) | 12 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 21.5× (z +23.0) | [[Cobimetinib (drug)]] 5 µM 0.0230× (z -19.2) |
| [[HS-578T (line)]] | alt | 231 | 7 (4 ⚠) | 9 | [[Homoharringtonine (drug)]] 5 µM 24.1× (z +25.1) | [[Trametinib (drug)]] 5 µM 0.0390× (z -17.9) |
| [[NCI-H2347 (line)]] | alt | 185 | 5 (2 ⚠) | 11 | [[Homoharringtonine (drug)]] 5 µM 29.3× (z +26.8) | [[Cobimetinib (drug)]] 5 µM 0.0727× (z -14.2) |
| [[SW480 (line)]] | alt | 349 | 5 (2 ⚠) | 11 | [[Homoharringtonine (drug)]] 5 µM 15.9× (z +23.8) | [[Trametinib (drug)]] 5 µM 0.0386× (z -19.6) |
| [[SHP-77 (line)]] | alt | 334 | 1 | 14 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +9.8) | [[Trametinib (drug)]] 5 µM 0.0190× (z -25.2) |
| [[HEC-1-A (line)]] | alt | 245 | 7 (3 ⚠) | 7 | [[Homoharringtonine (drug)]] 5 µM 26.2× (z +25.2) | [[Cobimetinib (drug)]] 5 µM 0.0497× (z -15.6) |
| [[LOX-IMVI (line)]] | wt | 324 | 4 (1 ⚠) | 10 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +17.9) | [[Trametinib (drug)]] 5 µM 0.0286× (z -17.8) |
| [[NCI-H2030 (line)]] | alt | 282 | 3 | 11 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 18.0× (z +21.0) | [[Adagrasib (drug)]] 0.05 µM 0.432× (z -14.9) ⚠ position not correctable · without an alert: [[Cobimetinib (drug)]] 5 µM 0.0526× (z -14.6) |
| [[PANC-1 (line)]] | alt | 248 | 3 | 11 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 32.2× (z +24.5) | [[Trametinib (drug)]] 5 µM 0.0370× (z -16.5) |
| [[RPMI-7951 (line)]] | alt | 272 | 6 (3 ⚠) | 8 | [[Homoharringtonine (drug)]] 5 µM 21.6× (z +19.3) | [[Trametinib (drug)]] 5 µM 0.0434× (z -13.3) |
| [[SW 900 (line)]] | alt | 179 | 6 (3 ⚠) | 8 | [[Homoharringtonine (drug)]] 5 µM 19.2× (z +21.9) | [[Trametinib (drug)]] 0.05 µM 0.173× (z -12.8) |
| [[A549 (line)]] | wt | 260 | 4 (1 ⚠) | 9 | [[Homoharringtonine (drug)]] 5 µM 20.1× (z +20.8) | [[Trametinib (drug)]] 5 µM 0.0438× (z -15.5) |
| [[BT-474 (line)]] | alt | 222 | 5 (1 ⚠) | 8 | [[Homoharringtonine (drug)]] 5 µM 12.4× (z +22.1) | [[Cobimetinib (drug)]] 5 µM 0.0825× (z -15.0) |
| [[HCT15 (line)]] | alt | 335 | 5 (2 ⚠) | 8 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.12× (z +15.9) | [[Trametinib (drug)]] 5 µM 0.0945× (z -15.4) |
| [[hTERT-HPNE (line)]] | wt | 235 | 5 (2 ⚠) | 8 | [[Homoharringtonine (drug)]] 5 µM 25.6× (z +23.6) | [[Trametinib (drug)]] 5 µM 0.0620× (z -13.9) |
| [[CFPAC-1 (line)]] | alt | 275 | 4 (2 ⚠) | 8 | [[Homoharringtonine (drug)]] 5 µM 27.4× (z +27.4) | [[Cobimetinib (drug)]] 5 µM 0.0631× (z -15.5) |
| [[H4 (line)]] | wt | 313 | 3 (2 ⚠) | 9 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.17× (z +14.3) | [[Trametinib (drug)]] 5 µM 0.0187× (z -18.4) |
| [[J82 (line)]] | alt | 121 | 3 (1 ⚠) | 9 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +17.3) | [[Trametinib (drug)]] 0.05 µM 0.185× (z -12.1) |
| [[LoVo (line)]] | wt | 189 | 3 (2 ⚠) | 9 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 14.2× (z +22.7) | [[Cobimetinib (drug)]] 5 µM 0.0625× (z -16.1) |
| [[LS 180 (line)]] | wt | 158 | 4 (1 ⚠) | 8 | [[Homoharringtonine (drug)]] 5 µM 11.2× (z +18.4) | [[Cobimetinib (drug)]] 5 µM 0.0643× (z -14.1) |
| [[NCI-H1792 (line)]] | alt | 237 | 4 (2 ⚠) | 8 | [[Homoharringtonine (drug)]] 5 µM 13.7× (z +16.6) | [[Cobimetinib (drug)]] 5 µM 0.0384× (z -14.0) |
| [[C-33 A (line)]] | alt | 215 | 2 (1 ⚠) | 9 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.44× (z +14.3) | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.105× (z -14.6) |
| [[HT-29 (line)]] | alt | 422 | 2 (1 ⚠) | 9 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +15.4) | [[Trametinib (drug)]] 5 µM 0.150× (z -12.5) |
| [[A-172 (line)]] | wt | 118 | 6 (3 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 57.9× (z +25.2) | [[Trametinib (drug)]] 5 µM 0.0808× (z -10.6) |
| [[Hs 766T (line)]] | wt | 203 | 2 | 8 | [[Homoharringtonine (drug)]] 5 µM 22.7× (z +21.2) | [[Trametinib (drug)]] 0.5 µM 0.100× (z -13.7) |
| [[Panc 03.27 (line)]] | alt | 289 | 2 | 8 | [[Homoharringtonine (drug)]] 5 µM 15.4× (z +22.2) | [[Cobimetinib (drug)]] 5 µM 0.0505× (z -16.3) |
| [[SNU-423 (line)]] | alt | 318 | 2 | 8 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 26.7× (z +25.7) | [[Cobimetinib (drug)]] 5 µM 0.0768× (z -13.6) |
| [[SW1417 (line)]] | alt | 296 | 1 | 9 | [[Homoharringtonine (drug)]] 5 µM 5.95× (z +15.2) | [[Trametinib (drug)]] 5 µM 0.0964× (z -14.2) |
| [[A498 (line)]] | wt | 105 | 2 | 7 | [[Homoharringtonine (drug)]] 5 µM 9.59× (z +15.9) | [[Trametinib (drug)]] 5 µM 0.0803× (z -12.0) |
| [[HepG2_C3A (line)]] | wt | 303 | 2 | 7 | [[Homoharringtonine (drug)]] 5 µM 5.98× (z +16.9) | [[Cobimetinib (drug)]] 5 µM 0.0828× (z -15.9) |
| [[KATO III (line)]] | alt | 135 | 2 | 7 | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +18.4) | [[Trametinib (drug)]] 5 µM 0.0840× (z -13.0) |
| [[RKO (line)]] | wt | 275 | 1 | 8 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +10.3) | [[Trametinib (drug)]] 5 µM 0.0533× (z -19.8) |
| [[AN3 CA (line)]] | alt | 173 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 20.2× (z +18.6) | — |
| [[COLO 205 (line)]] | alt | 438 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 32.7× (z +18.2) | [[Cobimetinib (drug)]] 5 µM 0.0531× (z -10.3) |
| [[SW 1088 (line)]] | alt | 221 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 9.64× (z +10.5) | [[Trametinib (drug)]] 0.5 µM 0.0906× (z -9.7) |
| [[CHP-212 (line)]] | wt | 214 | 0 | 3 | — | [[Trametinib (drug)]] 5 µM 0.0552× (z -13.8) |
| [[SW 1271 (line)]] | alt | 237 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 30.8× (z +13.9) | — |
| [[NCI-H2122 (line)]] | alt | 273 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 275 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.7 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 40.9 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4217), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EGR2]] | +0.90 | +0.90 / +0.88 | both halves | 7e-06 | same gene group; pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 980 |
| [[EGR3]] | +0.90 | +0.89 / +0.89 | both halves | 7e-06 | same gene group; pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 876 |
| [[IER2]] | +0.90 | +0.90 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 908 |
| [[ERCC1]] | +0.83 | +0.85 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[MCL1]] | +0.82 | +0.85 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 414 |
| [[FOS]] | +0.79 | +0.75 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 995 |
| [[PHLDA1]] | +0.75 | +0.74 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[DUSP6]] | +0.74 | +0.75 / +0.70 | both halves | 7e-06 | pathway: Nuclear Events (kinase and transcription factor activation); STRING 729 |
| [[ASTL]] | +0.73 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[FOSL1]] | +0.72 | +0.72 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 862 |
| [[JUNB]] | +0.72 | +0.70 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 970 |
| [[SYAP1]] | +0.71 | +0.63 / +0.73 | both halves | 7e-06 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FHIP2A]] | -0.69 | -0.64 / -0.64 | both halves | 7e-06 |  |
| [[HINT1]] | -0.61 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[SNX4]] | -0.60 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[ZNF148]] | -0.60 | -0.55 / -0.55 | both halves | 1e-05 | same gene group |
| [[CIAO2A]] | -0.59 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[NAPB]] | -0.59 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[ASB7]] | -0.59 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[C8orf76]] | -0.58 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[BMPR1A]] | -0.58 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[LRRFIP2]] | -0.58 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[RWDD3]] | -0.57 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[SOS1]] | -0.57 | -0.57 / -0.47 | both halves | 2e-05 | pathway: Signaling by NTRK1 (TRKA); STRING 426 |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises EGR1's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 8.4% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC00659]] | B | LINC00659 activity raises EGR1's level | lines that do not express LINC00659 (26) vs lines expressing it (24) | 1.66× lower at baseline in the lines without LINC00659 | 0.044 | ⚠ within organs, on part of the lines; also absent: KLK6, TRIM15, ENSG00000225680 |
| [[EGR2]] | B | EGR2 activity raises EGR1's level | lines that do not express EGR2 (7) vs lines expressing it (43) | 2.34× lower at baseline in the lines without EGR2 | 0.047 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[PMEPA1]] | B | PMEPA1 activity raises EGR1's level | lines that do not express PMEPA1 (6) vs lines expressing it (44) | 1.74× lower at baseline in the lines without PMEPA1 | 0.074 | ⚠ within organs, on part of the lines; also absent: SOX4, SLC2A1-DT, ENSG00000285253 |
| [[MAML3]] | B | MAML3 activity raises EGR1's level | lines that do not express MAML3 (9) vs lines expressing it (41) | 1.75× lower at baseline in the lines without MAML3 | 0.083 | ⚠ within organs, on part of the lines; also absent: SOX4, GOLGA7B-DT, STEAP2-AS1 |
| [[TOP2A]] | B | TOP2A activity raises EGR1's level | compounds that target TOP2A: 4 of 5 lower it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin) | 80% of the class's compounds vs 8.4% of all compounds | 0.084 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PLEKHG2]] | B | PLEKHG2 activity raises EGR1's level | lines that do not express PLEKHG2 (10) vs lines expressing it (40) | 1.85× lower at baseline in the lines without PLEKHG2 | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000225689; maybe low, not absent |
| [[NAA16]] | C | NAA16's natural level strengthens EGR1's drug response | NAA16's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse -0.01; direction not clear | 0.071 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 109]] — immediate early; 43 genes; every member is in the + arm (projection on the module's main direction 0.932). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.3, -0.3); signed map (6.0, 29.5). **Vector** length 174, 69.4% of its response variance represented; |z| ≥ 3 in 2,288 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +10.4 | +30.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +9.6 | +19.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.5 | +12.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +7.0 | +6.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +6.4 | +5.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +4.5 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | +4.6 | +2.2 |
|  | [[Tirabrutinib (drug)]] 0.5 µM |  | +4.4 | +2.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.1 | +1.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +4.1 | +1.2 |
| fall | [[Trametinib (drug)]] 0.5 µM |  | -13.2 | -16.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -12.8 | -17.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -12.6 | -16.8 |
|  | [[Trametinib (drug)]] 5 µM |  | -12.5 | -20.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -12.1 | -19.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -11.5 | -16.5 |

## What is on record

|  |  |
|---|---|
| Name | early growth response 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.2 — chr5:138,465,479-138,469,303 (+) |
| Ensembl biotype | protein_coding |
| Also known as | 225, TIS8, AT225, G0S30, NGFI-A, ZIF268, KROX-24, ZIF-268 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; Early growth response family |
| Hallmark sets | TNFA_SIGNALING_VIA_NFKB |
| Reactome | 12 pathways, smallest: NGF-stimulated transcription; Nuclear Events (kinase and transcription factor activation); Interferon alpha/beta signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P18146](https://www.uniprot.org/uniprotkb/P18146) (Early growth response protein 1):

> Transcriptional regulator. Recognizes and binds to the DNA sequence 5'-GCG(T/G)GGGCG-3'(EGR-site) in the promoter region of target genes (By similarity). Binds double-stranded target DNA, irrespective of the cytosine methylation status. Regulates the transcription of numerous target genes, and thereby plays an important role in regulating the response to growth factors, DNA damage, and ischemia. Plays a role in the regulation of cell survival, proliferation and cell death. Activates expression …

**Summary**, from NCBI Gene [1958](https://www.ncbi.nlm.nih.gov/gene/1958):

> The protein encoded by this gene belongs to the EGR family of C2H2-type zinc-finger proteins. It is a nuclear protein and functions as a transcriptional regulator. The products of target genes it activates are required for differentitation and mitogenesis. Studies suggest this is a cancer suppressor gene. [provided by RefSeq, Dec 2014]

**Accessions** — [HGNC:3238](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3238) · Entrez [1958](https://www.ncbi.nlm.nih.gov/gene/1958) · UniProt [P18146](https://www.uniprot.org/uniprotkb/P18146) · Ensembl [ENSG00000120738](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120738)

## Data

Gene col 4217: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4217); `tables/drug_effects.parquet` (65 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4217, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4217]; `tensor/DDL_lfc|DDL_z.npy` [4217]; `embed/gene_vectors.npy` [4217]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4217 or target_col == 4217). Every well: [[EGR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EGR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
