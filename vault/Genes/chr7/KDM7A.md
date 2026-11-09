---
symbol: "KDM7A"
type: "gene"
col: 112
ensembl_id: "ENSG00000006459"
name: "lysine demethylase 7A"
location: "7q34"
module: 184
arm: "+"
pooled_cpm: 181.71
n_lines_expressing: 49
n_dd_up: 7
n_dd_down: 29
n_dd_up_clean: 5
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/184"]
generated_by: "tahoemap"
---

# KDM7A

*lysine demethylase 7A* — 7q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 1.99× (z +5.4, q 4e-05, up in 28 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.331× (z -15.9, q 0e+00, down in 42 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 0.706× (z -7.4, q 1e-11, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KDM7A-DT]] (+0.68, fdr 7e-06, ⚠ same locus), [[HOMER1]] (+0.57, fdr 5e-05), [[PDGFA]] (+0.54, fdr 1e-05), [[CDCP1]] (+0.54, fdr 7e-06); moves opposite to [[LUC7L2]] (-0.60, fdr 3e-05), [[FUBP1]] (-0.54, fdr 3e-05), [[EXOSC10]] (-0.52, fdr 4e-05).
> It sits in the **+** arm of [[Module 184]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 112.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.99×** | +5.4 | 4e-05 | 28/48 (COLO 205, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +4.8 | 4e-04 | 25/47 (SHP-77, A-427, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.37×** | +4.7 | 4e-04 | 31/47 (NCI-H1792, Panc 03.27, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.65×** | +3.9 | 0.011 | 29/47 (SW480, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.43×** | +3.8 | 0.015 | 29/47 (PANC-1, SW480, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | **1.57×** | +3.5 | 0.036 | 23/47 (C32, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 1.18× | +3.5 | 0.036 | 16/47 (RKO, SHP-77, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.18× | +3.5 | 0.038 | 19/48 (SHP-77, NCI-H460, …) | top dose only |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.54×** | +3.4 | 0.047 | 27/47 (HEC-1-A, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 14 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 112.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.331×** | -15.9 | 0e+00 | 42/43 (A549, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.356×** | -14.3 | 5e-44 | 39/44 (C32, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.393×** | -14.0 | 2e-42 | 45/48 (A549, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.464×** | -11.1 | 2e-26 | 41/46 (HepG2/C3A, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.527×** | -9.6 | 8e-20 | 42/47 (A549, HepG2/C3A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.569×** | -8.5 | 2e-15 | 40/47 (A549, HepG2/C3A, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.706×** | -7.4 | 1e-11 | 33/47 (AsPC-1, A549, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.447×** | -6.3 | 2e-08 | 39/47 (SW480, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.651×** | -6.2 | 4e-08 | 35/46 (C32, HCT15, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.713×** | -5.1 | 2e-05 | 34/47 (A549, HepG2/C3A, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **0.546×** | -4.7 | 1e-04 | 31/47 (SW480, SW48, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.797×** | -4.7 | 2e-04 | 28/48 (NCI-H23, HCT15, …) | all doses, flat |  |
| [[NG25 (drug)]] 5 µM |  | **0.576×** | -4.3 | 7e-04 | 30/47 (A549, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.756×** | -4.2 | 0.001 | 32/47 (NCI-H1792, SHP-77, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.761×** | -4.1 | 0.002 | 31/47 (SW480, HCT15, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.826×** | -4.1 | 0.002 | 22/47 (LoVo, AN3 CA, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **0.806×** | -4.0 | 0.002 | 21/47 (SW480, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.777×** | -3.8 | 0.005 | 26/47 (A549, KATO III, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.779×** | -3.8 | 0.005 | 27/47 (MIA PaCa-2, A-172, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.791×** | -3.4 | 0.018 | 25/47 (SW480, NCI-H23, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.658×** | -3.3 | 0.025 | 21/47 (C32, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.739×** | -3.2 | 0.027 | 26/47 (SW480, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.858× | -3.2 | 0.029 | 17/47 (SW480, NCI-H23, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.851× | -3.1 | 0.042 | 20/47 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 112. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 249 | 1 | 18 (10 ⚠) | [[PH-797804 (drug)]] 5 µM 4.71× (z +9.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.240× (z -15.4) ⚠ toxic · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.349× (z -11.8) |
| [[LoVo (line)]] | wt | 349 | 0 | 10 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -20.3) |
| [[HS-578T (line)]] | alt | 326 | 1 | 8 (7 ⚠) | [[PH-797804 (drug)]] 5 µM 5.62× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.464× (z -10.6) |
| [[A549 (line)]] | wt | 424 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0617× (z -22.8) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.373× (z -11.9) |
| [[LS 180 (line)]] | wt | 366 | 0 | 8 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.291× (z -13.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.481× (z -10.9) |
| [[BT-474 (line)]] | alt | 290 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.220× (z -12.6) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 319 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.149× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.339× (z -12.7) |
| [[HepG2_C3A (line)]] | wt | 317 | 0 | 7 (7 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.118× (z -19.0) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 314 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[LOX-IMVI (line)]] | wt | 176 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.225× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.391× (z -12.9) |
| [[NCI-H2347 (line)]] | alt | 133 | 0 | 6 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.217× (z -12.3) ⚠ toxic · without an alert: [[Selinexor (drug)]] 5 µM 0.368× (z -11.9) |
| [[PANC-1 (line)]] | alt | 138 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.321× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.542× (z -10.2) |
| [[C32 (line)]] | wt | 234 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.150× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.406× (z -11.7) |
| [[KATO III (line)]] | alt | 165 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.341× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 192 | 0 | 4 (3 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.618× (z -14.4) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.364× (z -11.9) |
| [[COLO 205 (line)]] | alt | 109 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 13.2× (z +11.9) | — |
| [[HOP62 (line)]] | alt | 168 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.240× (z -9.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 118 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.312× (z -12.3) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 153 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.251× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 153 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.81× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.203× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.382× (z -10.5) |
| [[NCI-H23 (line)]] | alt | 220 | 0 | 3 (3 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.577× (z -19.8) ⚠ position not correctable |
| [[NCI-H460 (line)]] | wt | 195 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.237× (z -11.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 371 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.296× (z -11.2) ⚠ toxic |
| [[A-172 (line)]] | wt | 109 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.260× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[A-427 (line)]] | wt | 85.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.277× (z -13.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 99.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.302× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.502× (z -8.7) |
| [[J82 (line)]] | alt | 85.8 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.274× (z -10.6) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 99.4 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.334× (z -10.0) ⚠ toxic |
| [[NCI-H596 (line)]] | alt | 205 | 0 | 2 (1 ⚠) | — | [[Methylthiouracil (drug)]] 5 µM 0.181× (z -13.2) |
| [[Panc 03.27 (line)]] | alt | 115 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.324× (z -10.2) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 94.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.271× (z -10.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 180 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.162× (z -15.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 109 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +9.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.319× (z -8.8) ⚠ toxic |
| [[SW 900 (line)]] | alt | 122 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.282× (z -12.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 179 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -14.6) |
| [[AsPC-1 (line)]] | alt | 135 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.333× (z -13.3) |
| [[H4 (line)]] | wt | 135 | 1 (1 ⚠) | 0 | [[Pitavastatin (Calcium) (drug)]] 5 µM 2.99× (z +8.7) ⚠ cell-cycle shift, explains ~85% of this change | — |
| [[HEC-1-A (line)]] | alt | 48.7 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +10.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[hTERT-HPNE (line)]] | wt | 128 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.300× (z -9.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 200 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.123× (z -16.6) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 90.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.329× (z -10.7) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 249 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[A498 (line)]] | wt | 106 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 165 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 40.0 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 262 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 93.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 173 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 83.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 112), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KDM7A-DT]] | +0.68 | +0.60 / +0.66 | both halves | 7e-06 | ⚠ same locus (0.2 kb: neighbours can correlate without regulation) |
| [[HOMER1]] | +0.57 | +0.39 / +0.57 | both halves | 5e-05 |  |
| [[PDGFA]] | +0.54 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[CDCP1]] | +0.54 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[STC1]] | +0.53 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[KCTD5]] | +0.52 | +0.31 / +0.54 | both halves | 2e-04 |  |
| [[TIMP1]] | +0.52 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[SH3GL3]] | +0.52 | +0.63 / +0.38 | both halves | 6e-05 |  |
| [[CSGALNACT2]] | +0.52 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[LUCAT1]] | +0.52 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[BACE2]] | +0.51 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[RELL2]] | +0.51 | +0.28 / +0.51 | both halves | 3e-04 |  |
| [[SEPTIN10]] | +0.51 | +0.60 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LUC7L2]] | -0.60 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[FUBP1]] | -0.54 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[EXOSC10]] | -0.52 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[CC2D2A]] | -0.52 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[CDC23]] | -0.50 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[ZZZ3]] | -0.48 | -0.31 / -0.48 | both halves | 2e-04 | pathway: Chromatin modifying enzymes |
| [[RPRD1B]] | -0.47 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[TNS3]] | -0.46 | -0.42 / -0.31 | both halves | 2e-04 |  |
| [[INTS7]] | -0.46 | -0.38 / -0.46 | both halves | 6e-05 |  |
| [[SMIM7]] | -0.45 | -0.26 / -0.37 | both halves | 4e-04 |  |
| [[CUL5]] | -0.45 | -0.36 / -0.48 | both halves | 1e-04 |  |
| [[EWSR1]] | -0.45 | -0.50 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises KDM7A's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 6.4% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds |
| [[TNS3]] | B | TNS3 activity strengthens KDM7A's drug response | lines that do not express TNS3 (8) vs lines expressing it (40) | the lines without TNS3 respond 0.68× as strongly (z diff +1.34); strongest at Dinaciclib 0.05 µM: 0.72x vs 0.34x (z diff +4.6) | 0.076 | ⚠ within organs, on part of the lines; also absent: LGALS3, MAML2, SMOX; target measured in part of the lines; artifact flags |
| [[KDM7A-DT]] | C | KDM7A-DT activity raises KDM7A's level | lines that do not express KDM7A-DT (4) vs lines expressing it (46) | 2.32× lower at baseline in the lines without KDM7A-DT | 0.028 | ⚠ few lines (4 vs 46); across organs; also absent: FBXO6, MCF2L2, KIAA1522; maybe low, not absent |
| [[KDM7A-DT]] | C | KDM7A-DT activity strengthens KDM7A's drug response | lines that do not express KDM7A-DT (3) vs lines expressing it (45) | the lines without KDM7A-DT respond 0.41× as strongly (z diff +3.28); strongest at Dinaciclib 0.5 µM: 0.68x vs 0.37x (z diff +5.0) | 0.047 | ⚠ few lines (4 vs 46); across organs; also absent: FBXO6, MCF2L2, KIAA1522; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 184]]; 20 genes; this gene is in the **+** arm (projection on the module's main direction 0.568). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.39).
- **Nodal map** (x, y) = (40.4, -4.2); signed map (-0.1, 32.3). **Vector** length 118, 42.9% of its response variance represented; |z| ≥ 3 in 1,736 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.0 | +4.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +6.6 | -0.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.3 | +0.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.5 | +2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.4 | +1.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.2 | +3.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.7 | +0.8 |
|  | [[Infigratinib (drug)]] 5 µM |  | +3.5 | +1.9 |
| fall | [[Selinexor (drug)]] 5 µM |  | -4.8 | -7.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.7 | -3.8 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -4.3 | -4.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.3 | -6.2 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -4.3 | -3.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.0 | -6.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.8 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | lysine demethylase 7A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q34 — chr7:140,084,746-140,176,983 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1718; previously JHDM1D |
| Gene groups (HGNC) | PHD finger proteins; Lysine demethylase 7 family |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 6 pathways, smallest: HDMs demethylate histones; Signaling by BRAF and RAF1 fusions; Oncogenic MAPK signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZMT4](https://www.uniprot.org/uniprotkb/Q6ZMT4) (Lysine-specific demethylase 7A):

> Histone demethylase required for brain development. Specifically demethylates dimethylated 'Lys-9', 'Lys-27' and 'Lys-36' (H3K9me2, H3K27me2, H3K36me2, respectively) of histone H3 and monomethylated histone H4 'Lys-20' residue (H4K20Me1), thereby playing a central role in histone code. Specifically binds trimethylated 'Lys-4' of histone H3 (H3K4me3), affecting histone demethylase specificity: in presence of H3K4me3, it has no demethylase activity toward H3K9me2, while it has high activity …

**Summary**, from NCBI Gene [80853](https://www.ncbi.nlm.nih.gov/gene/80853):

> Enables histone demethylase activity and transition metal ion binding activity. Predicted to be involved in chromatin remodeling; midbrain development; and regulation of transcription by RNA polymerase II. Predicted to be located in nucleoplasm. Implicated in melanoma. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:22224](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22224) · Entrez [80853](https://www.ncbi.nlm.nih.gov/gene/80853) · UniProt [Q6ZMT4](https://www.uniprot.org/uniprotkb/Q6ZMT4) · Ensembl [ENSG00000006459](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000006459)

## Data

Gene col 112: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 112); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 112, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 112]; `tensor/DDL_lfc|DDL_z.npy` [112]; `embed/gene_vectors.npy` [112]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 112 or target_col == 112). Every well: [[KDM7A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KDM7A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
