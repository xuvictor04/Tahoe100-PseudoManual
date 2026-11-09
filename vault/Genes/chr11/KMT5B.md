---
symbol: "KMT5B"
type: "gene"
col: 3110
ensembl_id: "ENSG00000110066"
name: "lysine methyltransferase 5B"
location: "11q13.2"
module: 51
arm: "+"
pooled_cpm: 153.27
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 27
n_dd_up_clean: 4
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# KMT5B

*lysine methyltransferase 5B* — 11q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.46× (z +16.8, q 0e+00, up in 35 of 48 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.32× (z +8.7, q 1e-15, up in 25 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (13 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.344× (z -33.3, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPC1]] (+0.76, fdr 7e-06), [[POGZ]] (+0.67, fdr 7e-06), [[TCEANC]] (+0.66, fdr 2e-05); moves opposite to [[AHSA1]] (-0.63, fdr 8e-06), [[SNHG30]] (-0.55, fdr 3e-05), [[ATP2C1]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3110.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.46×** | +16.8 | 0e+00 | 35/48 (A-427, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.32×** | +8.7 | 1e-15 | 25/48 (KATO III, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.58×** | +7.5 | 9e-12 | 31/48 (NCI-H1573, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.27×** | +7.5 | 1e-11 | 29/48 (HEC-1-A, A-427, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.28×** | +7.4 | 2e-11 | 26/48 (KATO III, A-427, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.20×** | +5.8 | 5e-07 | 24/48 (NCI-H1573, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +5.7 | 1e-06 | 21/48 (KATO III, NCI-H460, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.39×** | +5.4 | 5e-06 | 27/49 (SW480, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.18× | +5.2 | 1e-05 | 22/48 (KATO III, NCI-H1573, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.14× | +4.2 | 0.002 | 14/48 (A-427, HEC-1-A, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 21 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3110.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.344×** | -33.3 | 0e+00 | 48/48 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.354×** | -32.5 | 0e+00 | 48/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.400×** | -28.6 | 0e+00 | 48/48 (BT-474, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.529×** | -19.9 | 0e+00 | 48/48 (BT-474, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.548×** | -18.8 | 0e+00 | 48/48 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.572×** | -16.8 | 0e+00 | 45/50 (Panc 03.27, NCI-H23, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.586×** | -16.7 | 0e+00 | 43/49 (NCI-H1573, AsPC-1, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.561×** | -16.7 | 0e+00 | 38/45 (PANC-1, SW1417, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.690×** | -16.4 | 0e+00 | 36/49 (NCI-H2347, HS-578T, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.583×** | -16.2 | 0e+00 | 43/48 (NCI-H23, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **0.639×** | -13.4 | 2e-39 | 38/44 (SNU-1, C-33 A, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.670×** | -12.5 | 4e-34 | 41/48 (SNU-1, NCI-H23, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.715×** | -10.4 | 8e-24 | 35/48 (LoVo, SW480, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.542×** | -10.0 | 7e-22 | 44/49 (SW480, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.731×** | -9.2 | 1e-18 | 34/48 (BT-474, SW1417, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.816×** | -8.9 | 2e-17 | 29/48 (PANC-1, NCI-H2347, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.801×** | -6.9 | 2e-10 | 28/48 (BT-474, SW 900, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.862× | -6.5 | 2e-09 | 22/48 (SW480, BT-474, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.767×** | -4.3 | 3e-04 | 23/48 (Panc 03.27, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[OTS514 (drug)]] 5 µM |  | **0.780×** | -4.0 | 0.001 | 20/46 (MIA PaCa-2, NCI-H661, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.785×** | -3.9 | 0.002 | 16/48 (NCI-H23, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.05 µM |  | 0.882× | -3.9 | 0.002 | 11/48 (LoVo, NCI-H661, …) | all doses, stronger at high dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.790×** | -3.8 | 0.002 | 21/48 (PANC-1, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.886× | -3.7 | 0.003 | 7/48 (NCI-H2030, SW 900, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.53 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3110. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 164 | 1 (1 ⚠) | 14 (10 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +11.0) ⚠ cell-cycle shift, explains ~29% of this change | [[Panobinostat (drug)]] 0.5 µM 0.298× (z -21.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.299× (z -20.9) |
| [[BT-474 (line)]] | alt | 353 | 1 (1 ⚠) | 13 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +12.3) ⚠ cell-cycle shift, explains ~29% of this change | [[Panobinostat (drug)]] 0.5 µM 0.200× (z -28.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.323× (z -20.0) |
| [[HS-578T (line)]] | alt | 169 | 0 | 13 (9 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.313× (z -19.6) |
| [[PANC-1 (line)]] | alt | 211 | 1 (1 ⚠) | 12 (8 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.52× (z +13.0) ⚠ cell-cycle shift, explains ~29% of this change | [[Panobinostat (drug)]] 5 µM 0.412× (z -19.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.449× (z -17.6) |
| [[A-427 (line)]] | wt | 144 | 4 (2 ⚠) | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +17.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 2.88× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.390× (z -15.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.469× (z -12.3) |
| [[AsPC-1 (line)]] | alt | 169 | 1 | 10 (7 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.84× (z +9.6) | [[Panobinostat (drug)]] 0.5 µM 0.258× (z -20.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.277× (z -19.9) |
| [[HEC-1-A (line)]] | alt | 135 | 2 (2 ⚠) | 9 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +16.1) ⚠ cell-cycle shift, explains ~29% of this change | [[Dinaciclib (drug)]] 5 µM 0.298× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.385× (z -13.9) |
| [[SW1417 (line)]] | alt | 208 | 1 (1 ⚠) | 10 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +14.1) ⚠ cell-cycle shift, explains ~29% of this change | [[Panobinostat (drug)]] 0.5 µM 0.336× (z -19.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.384× (z -17.2) |
| [[SW480 (line)]] | alt | 185 | 1 | 10 (6 ⚠) | [[TAK-901 (drug)]] 5 µM 2.40× (z +8.9) | [[Belinostat (drug)]] 5 µM 0.281× (z -24.4) |
| [[NCI-H1573 (line)]] | alt | 311 | 1 | 9 (6 ⚠) | [[PH-797804 (drug)]] 5 µM 3.06× (z +9.9) | [[Panobinostat (drug)]] 5 µM 0.281× (z -21.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.296× (z -20.6) |
| [[NCI-H23 (line)]] | alt | 340 | 1 (1 ⚠) | 9 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +17.2) ⚠ cell-cycle shift, explains ~29% of this change | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.325× (z -19.3) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.361× (z -18.2) |
| [[Panc 03.27 (line)]] | alt | 160 | 1 (1 ⚠) | 9 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +10.2) ⚠ cell-cycle shift, explains ~29% of this change | [[Belinostat (drug)]] 5 µM 0.326× (z -17.0) |
| [[CFPAC-1 (line)]] | alt | 115 | 1 (1 ⚠) | 8 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +9.9) ⚠ cell-cycle shift, explains ~29% of this change | [[Belinostat (drug)]] 5 µM 0.343× (z -16.6) |
| [[HOP62 (line)]] | alt | 107 | 0 | 9 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.294× (z -17.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.316× (z -16.7) |
| [[LOX-IMVI (line)]] | wt | 151 | 0 | 9 (7 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.291× (z -19.3) |
| [[NCI-H2030 (line)]] | alt | 134 | 1 (1 ⚠) | 8 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +14.2) ⚠ cell-cycle shift, explains ~29% of this change | [[Panobinostat (drug)]] 5 µM 0.353× (z -15.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.404× (z -13.6) |
| [[A-172 (line)]] | wt | 108 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.318× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.433× (z -11.8) |
| [[C-33 A (line)]] | alt | 169 | 1 (1 ⚠) | 7 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +8.8) ⚠ cell-cycle shift, explains ~29% of this change | [[Dinaciclib (drug)]] 5 µM 0.216× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.430× (z -10.7) |
| [[KATO III (line)]] | alt | 173 | 4 (3 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +17.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.92× (z +10.9) | [[Belinostat (drug)]] 5 µM 0.397× (z -15.2) |
| [[LoVo (line)]] | wt | 148 | 2 (1 ⚠) | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +11.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.60× (z +8.8) | [[Belinostat (drug)]] 5 µM 0.392× (z -17.1) |
| [[NCI-H1792 (line)]] | alt | 115 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.285× (z -17.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.290× (z -17.1) |
| [[NCI-H460 (line)]] | wt | 99.0 | 1 (1 ⚠) | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +11.0) ⚠ cell-cycle shift, explains ~29% of this change | [[Belinostat (drug)]] 5 µM 0.355× (z -16.4) |
| [[RPMI-7951 (line)]] | alt | 127 | 0 | 8 (5 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.314× (z -13.4) |
| [[SNU-1 (line)]] | wt | 202 | 2 (2 ⚠) | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +10.4) ⚠ cell-cycle shift, explains ~29% of this change | [[Dinaciclib (drug)]] 5 µM 0.225× (z -19.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.296× (z -16.4) |
| [[SW 900 (line)]] | alt | 138 | 0 | 8 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.295× (z -15.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.321× (z -14.6) |
| [[A549 (line)]] | wt | 138 | 1 (1 ⚠) | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +12.8) ⚠ cell-cycle shift, explains ~29% of this change | [[Dinaciclib (drug)]] 5 µM 0.324× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.383× (z -14.5) |
| [[C32 (line)]] | wt | 131 | 0 | 7 (5 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.362× (z -12.7) |
| [[HepG2_C3A (line)]] | wt | 139 | 0 | 7 (5 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.287× (z -15.8) |
| [[HT-29 (line)]] | alt | 187 | 0 | 7 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.295× (z -19.3) |
| [[MIA PaCa-2 (line)]] | alt | 112 | 0 | 7 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.268× (z -17.8) |
| [[A498 (line)]] | wt | 61.9 | 2 (2 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +12.5) ⚠ cell-cycle shift, explains ~29% of this change | [[Belinostat (drug)]] 5 µM 0.440× (z -11.8) |
| [[Hs 766T (line)]] | wt | 112 | 1 (1 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +10.2) ⚠ cell-cycle shift, explains ~29% of this change | [[Panobinostat (drug)]] 5 µM 0.388× (z -11.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.400× (z -11.2) |
| [[SNU-423 (line)]] | alt | 138 | 0 | 6 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.279× (z -16.4) |
| [[hTERT-HPNE (line)]] | wt | 115 | 0 | 5 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.361× (z -10.8) |
| [[J82 (line)]] | alt | 114 | 0 | 5 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.442× (z -13.0) |
| [[LS 180 (line)]] | wt | 176 | 1 | 3 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 2.99× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.369× (z -14.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.401× (z -13.5) |
| [[RKO (line)]] | wt | 110 | 1 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +14.4) ⚠ cell-cycle shift, explains ~29% of this change | [[Belinostat (drug)]] 5 µM 0.327× (z -12.3) |
| [[COLO 205 (line)]] | alt | 141 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.258× (z -15.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.259× (z -14.9) |
| [[H4 (line)]] | wt | 114 | 0 | 3 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.353× (z -10.7) |
| [[NCI-H661 (line)]] | alt | 149 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.248× (z -9.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.382× (z -8.9) |
| [[SW48 (line)]] | wt | 139 | 0 | 3 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.326× (z -11.4) |
| [[AN3 CA (line)]] | alt | 187 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.495× (z -8.7) ⚠ cell-cycle shift, explains ~35% of this change |
| [[HCT15 (line)]] | alt | 156 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +13.5) ⚠ cell-cycle shift, explains ~29% of this change | [[Belinostat (drug)]] 5 µM 0.432× (z -9.7) |
| [[SK-MEL-2 (line)]] | alt | 68.5 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +12.1) ⚠ cell-cycle shift, explains ~29% of this change | [[Belinostat (drug)]] 5 µM 0.377× (z -10.3) |
| [[SW 1088 (line)]] | alt | 130 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0651× (z -12.6) ⚠ transcription drop · without an alert: [[Naproxen (drug)]] 0.05 µM 0.103× (z -9.7) |
| [[SHP-77 (line)]] | alt | 141 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.505× (z -12.7) ⚠ cell-cycle shift, explains ~35% of this change |
| [[CHP-212 (line)]] | wt | 137 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 169 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 184 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3110), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPC1]] | +0.76 | +0.79 / +0.62 | both halves | 7e-06 | pathway: Chromatin modifying enzymes |
| [[POGZ]] | +0.67 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[TCEANC]] | +0.66 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[LIPT1]] | +0.65 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[ING3]] | +0.64 | +0.58 / +0.56 | both halves | 1e-05 | pathway: Chromatin modifying enzymes |
| [[BRAF]] | +0.64 | +0.62 / +0.58 | both halves | 8e-06 |  |
| [[SENP6]] | +0.64 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[SCAF8]] | +0.63 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[THAP1]] | +0.63 | +0.67 / +0.46 | both halves | 3e-05 |  |
| [[HARBI1]] | +0.62 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[ADNP]] | +0.62 | +0.64 / +0.54 | both halves | 1e-05 | STRING 713 |
| [[MED19]] | +0.61 | +0.69 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AHSA1]] | -0.63 | -0.61 / -0.57 | both halves | 8e-06 |  |
| [[SNHG30]] | -0.55 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[ATP2C1]] | -0.55 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[USB1]] | -0.55 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[CRYBB2P1]] | -0.55 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[PRIM2]] | -0.55 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[ZNF731P]] | -0.54 | -0.52 / -0.40 | both halves | 4e-05 |  |
| [[ZDHHC16]] | -0.54 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[METTL3]] | -0.53 | -0.53 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises KMT5B's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.705). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-25.5, 12.8); signed map (7.5, -18.3). **Vector** length 116, 40.2% of its response variance represented; |z| ≥ 3 in 1,525 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +13.7 | +16.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +10.2 | +7.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | +9.3 | +7.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, would explain all of this change | +6.2 | -4.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.6 | +4.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +4.2 | -2.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.2 | +0.7 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +3.1 | +1.5 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +3.0 | +2.0 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -7.5 | -6.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -7.2 | -10.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.0 | -5.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.9 | -18.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -5.8 | -9.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.9 | -12.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.2 | -3.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -3.1 | -2.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | -3.1 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | lysine methyltransferase 5B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.2 — chr11:68,154,863-68,213,852 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-85; previously SUV420H1 |
| Gene groups (HGNC) | Histone lysine methyltransferases; SET domain containing |
| Reactome | 3 pathways, smallest: PKMTs methylate histone lysines; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q4FZB7](https://www.uniprot.org/uniprotkb/Q4FZB7) (Histone-lysine N-methyltransferase KMT5B):

> Histone methyltransferase that specifically methylates monomethylated 'Lys-20' (H4K20me1) and dimethylated 'Lys-20' (H4K20me2) of histone H4 to produce respectively dimethylated 'Lys-20' (H4K20me2) and trimethylated 'Lys-20' (H4K20me3) and thus regulates transcription and maintenance of genome integrity. In vitro also methylates unmodified 'Lys-20' (H4K20me0) of histone H4 and nucleosomes. H4 'Lys-20' trimethylation represents a specific tag for epigenetic transcriptional repression. Mainly …

**Summary**, from NCBI Gene [51111](https://www.ncbi.nlm.nih.gov/gene/51111):

> This gene encodes a protein that contains a SET domain. SET domains appear to be protein-protein interaction domains that mediate interactions with a family of proteins that display similarity with dual-specificity phosphatases (dsPTPases). The function of this gene has not been determined. Several alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2014]

**Accessions** — [HGNC:24283](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24283) · Entrez [51111](https://www.ncbi.nlm.nih.gov/gene/51111) · UniProt [Q4FZB7](https://www.uniprot.org/uniprotkb/Q4FZB7) · Ensembl [ENSG00000110066](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110066)

## Data

Gene col 3110: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3110); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3110, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3110]; `tensor/DDL_lfc|DDL_z.npy` [3110]; `embed/gene_vectors.npy` [3110]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3110 or target_col == 3110). Every well: [[KMT5B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KMT5B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
