---
symbol: "MED29"
type: "gene"
col: 727
ensembl_id: "ENSG00000063322"
name: "mediator complex subunit 29"
location: "19q13.2"
module: 77
arm: "-"
pooled_cpm: 52.02
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 8
n_dd_up_clean: 18
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# MED29

*mediator complex subunit 29* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.57× (z +34.5, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.590× (z -8.5, q 1e-14, down in 32 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.641× (z -7.2, q 2e-10, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C6orf62]] (+0.71, fdr 1e-05), [[USP11]] (+0.68, fdr 7e-06), [[HEXIM1]] (+0.67, fdr 1e-05); moves opposite to [[FAM24B]] (-0.63, fdr 1e-05), [[EEF1E1]] (-0.61, fdr 1e-05), [[NUP93]] (-0.61, fdr 3e-05).
> It sits in the **-** arm of [[Module 077]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 727.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.57×** | +34.5 | 0e+00 | 48/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.75×** | +23.0 | 0e+00 | 46/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.75×** | +15.6 | 0e+00 | 46/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.58×** | +15.2 | 0e+00 | 46/48 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.51×** | +14.8 | 0e+00 | 46/48 (A549, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.26×** | +12.6 | 3e-34 | 44/48 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~12% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.11×** | +12.0 | 2e-31 | 42/43 (HEC-1-A, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.06×** | +11.6 | 4e-29 | 37/47 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.97×** | +10.9 | 1e-25 | 42/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.01×** | +10.8 | 3e-25 | 40/47 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.81×** | +9.5 | 7e-20 | 41/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.84×** | +9.5 | 2e-19 | 28/35 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.45×** | +8.4 | 1e-15 | 34/48 (PANC-1, A-172, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.56×** | +7.1 | 4e-11 | 35/48 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.43×** | +5.7 | 4e-07 | 31/48 (A-172, BT-474, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.41×** | +5.5 | 1e-06 | 31/48 (LS 180, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.41×** | +5.5 | 2e-06 | 29/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 727.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.590×** | -8.5 | 1e-14 | 32/46 (SW48, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.641×** | -7.2 | 2e-10 | 28/48 (SHP-77, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.649×** | -7.0 | 6e-10 | 30/47 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.453×** | -6.7 | 4e-09 | 33/48 (PANC-1, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.460×** | -6.5 | 7e-09 | 30/47 (A-427, NCI-H460, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.709×** | -5.5 | 3e-06 | 32/48 (PANC-1, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.717×** | -5.4 | 7e-06 | 27/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.739×** | -4.9 | 8e-05 | 25/47 (SNU-423, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.933× | -3.7 | 0.012 | 2/48 (SW 1088, CHP-212) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 0.874× | -3.1 | 0.11 | 8/48 (Panc 03.27, SNU-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 727. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 425 | 11 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.01× (z +33.1) | [[Digitoxin (drug)]] 5 µM 0.433× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.493× (z -10.3) |
| [[MIA PaCa-2 (line)]] | alt | 32.7 | 10 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.96× (z +22.4) | — |
| [[NCI-H460 (line)]] | wt | 27.5 | 9 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.77× (z +21.2) | — |
| [[SW480 (line)]] | alt | 26.2 | 8 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.51× (z +22.4) | — |
| [[A549 (line)]] | wt | 53.2 | 7 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.52× (z +21.6) | — |
| [[HEC-1-A (line)]] | alt | 44.5 | 7 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.95× (z +22.2) | — |
| [[HS-578T (line)]] | alt | 29.5 | 7 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.68× (z +18.4) | — |
| [[KATO III (line)]] | alt | 40.3 | 7 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.85× (z +21.1) | — |
| [[HOP62 (line)]] | alt | 36.0 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +17.0) | — |
| [[J82 (line)]] | alt | 34.1 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.40× (z +16.7) | — |
| [[LoVo (line)]] | wt | 22.1 | 6 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.40× (z +19.2) | — |
| [[LS 180 (line)]] | wt | 20.5 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.60× (z +16.7) | — |
| [[A-172 (line)]] | wt | 26.4 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.79× (z +17.6) | — |
| [[A498 (line)]] | wt | 31.5 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +13.5) | — |
| [[SW1417 (line)]] | alt | 43.8 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +13.6) | — |
| [[AsPC-1 (line)]] | alt | 23.6 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.51× (z +17.9) | — |
| [[HT-29 (line)]] | alt | 51.6 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.91× (z +17.5) | — |
| [[Panc 03.27 (line)]] | alt | 35.9 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.93× (z +17.8) | — |
| [[A-427 (line)]] | wt | 28.7 | 2 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 3.38× (z +10.2) | [[PH-797804 (drug)]] 5 µM 0.0592× (z -12.4) |
| [[Hs 766T (line)]] | wt | 28.0 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.16× (z +18.0) | — |
| [[LOX-IMVI (line)]] | wt | 21.1 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.62× (z +14.0) | — |
| [[NCI-H1573 (line)]] | alt | 25.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.57× (z +17.8) | — |
| [[NCI-H1792 (line)]] | alt | 29.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.23× (z +16.7) | — |
| [[NCI-H2030 (line)]] | alt | 28.4 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.84× (z +11.8) | — |
| [[BT-474 (line)]] | alt | 28.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.83× (z +18.1) | — |
| [[CFPAC-1 (line)]] | alt | 29.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.78× (z +17.5) | — |
| [[hTERT-HPNE (line)]] | wt | 27.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.85× (z +15.0) | — |
| [[NCI-H2347 (line)]] | alt | 18.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.57× (z +15.9) | — |
| [[RPMI-7951 (line)]] | alt | 38.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.19× (z +14.5) | — |
| [[SK-MEL-2 (line)]] | alt | 21.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.82× (z +11.2) | — |
| [[SW48 (line)]] | wt | 28.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.83× (z +10.1) | [[Digitoxin (drug)]] 5 µM 0.0968× (z -12.4) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 33.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +10.4) | — |
| [[C32 (line)]] | wt | 24.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.70× (z +11.4) | — |
| [[COLO 205 (line)]] | alt | 28.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.90× (z +13.6) | — |
| [[H4 (line)]] | wt | 31.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.06× (z +12.8) | — |
| [[HCT15 (line)]] | alt | 38.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.48× (z +13.9) | — |
| [[HepG2_C3A (line)]] | wt | 22.5 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.188× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 22.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +10.2) | — |
| [[RKO (line)]] | wt | 21.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.89× (z +11.8) | — |
| [[SHP-77 (line)]] | alt | 41.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +9.8) | — |
| [[SNU-1 (line)]] | wt | 21.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.85× (z +8.8) | — |
| [[SNU-423 (line)]] | alt | 24.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.36× (z +11.2) | — |
| [[SW 900 (line)]] | alt | 30.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.90× (z +15.5) | — |
| [[AN3 CA (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 727), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C6orf62]] | +0.71 | +0.77 / +0.55 | both halves | 1e-05 |  |
| [[USP11]] | +0.68 | +0.75 / +0.59 | both halves | 7e-06 |  |
| [[HEXIM1]] | +0.67 | +0.76 / +0.54 | both halves | 1e-05 |  |
| [[TSPAN31]] | +0.64 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[C21orf91]] | +0.64 | +0.74 / +0.56 | both halves | 1e-05 |  |
| [[OFD1]] | +0.63 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[H3-3B]] | +0.62 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[CHCHD7]] | +0.62 | +0.79 / +0.45 | both halves | 3e-05 |  |
| [[BOLA1]] | +0.62 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[ABCA10]] | +0.61 | +0.79 / +0.44 | both halves | 3e-05 |  |
| [[THAP9]] | +0.61 | +0.72 / +0.45 | both halves | 3e-05 |  |
| [[GOLGB1]] | +0.61 | +0.65 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM24B]] | -0.63 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[EEF1E1]] | -0.61 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[NUP93]] | -0.61 | -0.65 / -0.46 | both halves | 3e-05 |  |
| [[NDUFS6]] | -0.61 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[CPSF4]] | -0.60 | -0.68 / -0.51 | both halves | 1e-05 |  |
| [[CASP2]] | -0.60 | -0.66 / -0.46 | both halves | 3e-05 |  |
| [[FAR1]] | -0.59 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[MFSD14CP]] | -0.58 | -0.64 / -0.56 | both halves | 1e-05 |  |
| [[NME2]] | -0.58 | -0.70 / -0.43 | both halves | 3e-05 |  |
| [[WDR5]] | -0.57 | -0.63 / -0.52 | both halves | 1e-05 |  |
| [[HACD3]] | -0.57 | -0.61 / -0.43 | both halves | 4e-05 |  |
| [[UCK2]] | -0.57 | -0.53 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MED29's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **-** arm (projection on the module's main direction -0.497). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (27.3, -27.3); signed map (15.0, -4.2). **Vector** length 86.5, 22.7% of its response variance represented; |z| ≥ 3 in 1,140 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +7.0 | +15.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.7 | +9.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.8 | +23.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.3 | +11.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +5.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.5 | +0.2 |
|  | [[Glycyrrhizic acid (drug)]] 5 µM |  | +1.7 | +1.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.6 | +0.7 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | +1.6 | -0.5 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.5 | -8.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -5.1 | -7.0 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -5.0 | -2.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.2 | -5.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | +2.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.4 | -6.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.1 | -0.3 |
|  | [[EX229 (drug)]] 5 µM |  | -3.0 | -2.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.9 | -2.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.6 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | mediator complex subunit 29 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:39,391,303-39,400,641 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp434H247, MED2; previously IXL |
| Gene groups (HGNC) | Mediator complex |
| Reactome | 8 pathways, smallest: Transcriptional regulation of white adipocyte differentiation; RSV-host interactions; Adipogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NX70](https://www.uniprot.org/uniprotkb/Q9NX70) (Mediator of RNA polymerase II transcription subunit 29):

> Component of the Mediator complex, a coactivator involved in the regulated transcription of nearly all RNA polymerase II-dependent genes. Mediator functions as a bridge to convey information from gene-specific regulatory proteins to the basal RNA polymerase II transcription machinery. Mediator is recruited to promoters by direct interactions with regulatory proteins and serves as a scaffold for the assembly of a functional pre-initiation complex with RNA polymerase II and the general …

**Summary**, from NCBI Gene [55588](https://www.ncbi.nlm.nih.gov/gene/55588):

> MED29 is a subunit of the Mediator complex, a multiprotein coactivator of RNA transcription that interacts with DNA-bound transcriptional activators, RNA polymerase II (see MIM 180660), and general initiation factors (Sato et al., 2003 [PubMed 14576168]).[supplied by OMIM, Aug 2009]

**Accessions** — [HGNC:23074](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23074) · Entrez [55588](https://www.ncbi.nlm.nih.gov/gene/55588) · UniProt [Q9NX70](https://www.uniprot.org/uniprotkb/Q9NX70) · Ensembl [ENSG00000063322](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000063322)

## Data

Gene col 727: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 727); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 727, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 727]; `tensor/DDL_lfc|DDL_z.npy` [727]; `embed/gene_vectors.npy` [727]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 727 or target_col == 727). Every well: [[MED29 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MED29.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
