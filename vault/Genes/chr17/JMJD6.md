---
symbol: "JMJD6"
type: "gene"
col: 953
ensembl_id: "ENSG00000070495"
name: "jumonji domain containing 6, arginine demethylase and lysine hydroxylase"
location: "17q25.1"
module: 41
arm: "+"
pooled_cpm: 46.57
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 20
n_dd_up_clean: 12
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# JMJD6

*jumonji domain containing 6, arginine demethylase and lysine hydroxylase* — 17q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.19× (z +13.4, q 5e-38, up in 40 of 47 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 4.02× (z +9.0, q 6e-17, up in 45 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.475× (z -8.9, q 3e-16, down in 33 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 0.649× (z -5.2, q 5e-05, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPTY2D1]] (+0.66, fdr 8e-06), [[YIPF5]] (+0.64, fdr 1e-05), [[LYSMD3]] (+0.62, fdr 1e-05); moves opposite to [[PON2]] (-0.58, fdr 1e-05), [[PAXBP1]] (-0.57, fdr 1e-05), [[KPNA1]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[EHD2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 953.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **2.19×** | +13.4 | 5e-38 | 40/47 (LoVo, A498, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **4.02×** | +9.0 | 6e-17 | 45/49 (PANC-1, NCI-H2030, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.90×** | +7.9 | 4e-13 | 36/47 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.69×** | +6.5 | 1e-08 | 40/48 (KATO III, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.65×** | +6.2 | 7e-08 | 37/48 (LoVo, HEC-1-A, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.66×** | +6.1 | 1e-07 | 35/48 (A-427, PANC-1, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.61×** | +5.9 | 3e-07 | 38/48 (A-427, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.59×** | +5.8 | 6e-07 | 39/48 (KATO III, PANC-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.40×** | +5.7 | 9e-07 | 34/48 (HOP62, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.53×** | +5.0 | 3e-05 | 31/48 (KATO III, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.49×** | +4.9 | 5e-05 | 33/48 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +4.5 | 3e-04 | 0/49 | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.84×** | +3.9 | 0.004 | 31/48 (HOP62, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.76×** | +3.6 | 0.011 | 23/48 (HEC-1-A, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.69×** | +3.4 | 0.026 | 21/43 (NCI-H2347, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.30×** | +3.2 | 0.045 | 18/48 (CHP-212, NCI-H23, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.28×** | +3.0 | 0.075 | 19/48 (MIA PaCa-2, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.19× | +3.0 | 0.081 | 22/49 (LOX-IMVI, CFPAC-1, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.28×** | +2.9 | 0.097 | 15/48 (SW480, NCI-H23, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 953.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.475×** | -8.9 | 3e-16 | 33/40 (KATO III, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.649×** | -5.2 | 5e-05 | 34/48 (SW 900, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.649×** | -5.2 | 5e-05 | 35/48 (NCI-H1573, NCI-H2030, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.673×** | -4.9 | 1e-04 | 26/48 (A-427, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.673×** | -4.9 | 1e-04 | 34/48 (SW 1088, HOP62, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.721×** | -4.1 | 0.004 | 25/48 (A498, SW 900, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.797×** | -3.9 | 0.007 | 25/48 (H4, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.737×** | -3.8 | 0.010 | 24/48 (A498, SW 900, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.742×** | -3.7 | 0.013 | 27/48 (HepG2/C3A, CFPAC-1, …) | rises with dose |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.761×** | -3.4 | 0.039 | 22/48 (C32, A-172, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.823×** | -3.3 | 0.043 | 19/48 (AsPC-1, NCI-H23, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.790×** | -3.3 | 0.044 | 20/48 (AsPC-1, BT-474, …) | all doses, flat | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.774×** | -3.2 | 0.060 | 23/48 (HOP62, SW 1088, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.775×** | -3.2 | 0.060 | 18/48 (Hs 766T, SW480, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.771×** | -3.1 | 0.070 | 20/47 (HEC-1-A, SW480, …) | inconsistent across doses | position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **0.753×** | -3.0 | 0.079 | 21/49 (AsPC-1, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.784×** | -3.0 | 0.079 | 20/47 (SW480, AsPC-1, …) | two highest doses | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.775×** | -2.9 | 0.095 | 17/48 (AsPC-1, SK-MEL-2, …) | inconsistent across doses | position effect removed |
| [[Amsacrine (drug)]] 5 µM |  | 0.845× | -2.9 | 0.095 | 16/48 (A549, HOP62, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, +0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 953. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 85.3 | 1 (1 ⚠) | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +15.1) ⚠ cell-cycle shift, explains ~38% of this change | [[Panobinostat (drug)]] 0.5 µM 0.371× (z -12.1) ⚠ cell-cycle shift, explains ~28% of this change |
| [[PANC-1 (line)]] | alt | 36.2 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +12.9) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.58× (z +9.1) | — |
| [[KATO III (line)]] | alt | 43.6 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +11.9) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.51× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.0663× (z -20.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 39.4 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +15.5) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.66× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.261× (z -11.3) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 40.8 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +14.7) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.09× (z +8.7) | — |
| [[SW480 (line)]] | alt | 35.3 | 2 (1 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.25× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.230× (z -11.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 30.8 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 3.47× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.173× (z -12.4) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 51.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.246× (z -11.1) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 46.8 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.56× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.406× (z -8.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 50.3 | 0 | 2 (1 ⚠) | — | [[OTS514 (drug)]] 5 µM 0.0620× (z -10.6) |
| [[A-172 (line)]] | wt | 54.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +9.3) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[C32 (line)]] | wt | 63.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +9.7) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[H4 (line)]] | wt | 82.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.229× (z -9.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 72.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +8.8) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[LOX-IMVI (line)]] | wt | 52.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.296× (z -10.1) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 27.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +9.5) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H1573 (line)]] | alt | 36.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +10.7) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H1792 (line)]] | alt | 66.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +13.1) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H2030 (line)]] | alt | 59.6 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 28.5 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H460 (line)]] | wt | 36.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +12.7) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[Panc 03.27 (line)]] | alt | 32.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +11.4) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[SHP-77 (line)]] | alt | 42.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.216× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change |
| [[SNU-423 (line)]] | alt | 63.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +9.9) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[SW 900 (line)]] | alt | 54.7 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.256× (z -11.1) |
| [[SW1417 (line)]] | alt | 29.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +9.0) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[A549 (line)]] | wt | 60.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 71.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 55.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 55.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 74.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 953), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPTY2D1]] | +0.66 | +0.64 / +0.58 | both halves | 8e-06 |  |
| [[YIPF5]] | +0.64 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[LYSMD3]] | +0.62 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[CLK3]] | +0.61 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[ARF4]] | +0.61 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[OSBP]] | +0.59 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[NOSIP]] | +0.58 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[PPFIA3]] | +0.58 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[CCDC28B]] | +0.58 | +0.43 / +0.45 | both halves | 3e-05 |  |
| [[DNAJB2]] | +0.58 | +0.60 / +0.42 | both halves | 4e-05 |  |
| [[RNF113A]] | +0.57 | +0.59 / +0.42 | both halves | 4e-05 |  |
| [[ARFIP2]] | +0.57 | +0.55 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PON2]] | -0.58 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[PAXBP1]] | -0.57 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[KPNA1]] | -0.56 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[CD99L2]] | -0.55 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[GTF2I]] | -0.54 | -0.52 / -0.43 | both halves | 4e-05 |  |
| [[HDAC2]] | -0.54 | -0.47 / -0.55 | both halves | 2e-05 | pathway: Chromatin modifying enzymes |
| [[SUMO2]] | -0.52 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[SMAD2]] | -0.52 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[PUM2]] | -0.51 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[ZNF236]] | -0.51 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[RNASEH2B]] | -0.51 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[RBBP4]] | -0.50 | -0.49 / -0.38 | both halves | 7e-05 | pathway: Chromatin modifying enzymes |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EHD2]] | B | EHD2 activity raises JMJD6's level | lines that do not express EHD2 (14) vs lines expressing it (36) | 1.42× lower at baseline in the lines without EHD2 | 0.079 | ⚠ within organs, on part of the lines; also absent: ITGA3, ENSG00000289526, ENSG00000230479 |
| [[GLRX]] | B | GLRX activity raises JMJD6's level | lines that do not express GLRX (10) vs lines expressing it (40) | 1.44× lower at baseline in the lines without GLRX | 0.084 | ⚠ within organs, on part of the lines; also absent: DUSP10, FES, DGKG; maybe low, not absent |
| [[NDRG1]] | B | NDRG1 activity raises JMJD6's level | lines that do not express NDRG1 (6) vs lines expressing it (44) | 1.48× lower at baseline in the lines without NDRG1 | 0.090 | ⚠ within organs, on part of the lines; also absent: SMOX, DELEC1, SLC2A1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.596). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (11.7, -37.9); signed map (-33.5, 34.1). **Vector** length 102, 30.8% of its response variance represented; |z| ≥ 3 in 1,171 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.4 | +6.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +6.7 | +13.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +5.2 | +7.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.5 | +1.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.8 | +2.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.1 | +3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | -1.0 |
|  | [[Fluvoxamine (maleate) (drug)]] 5 µM |  | +2.1 | +2.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.0 | +0.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -5.4 | +3.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.0 | -5.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | -5.0 | +3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -4.7 | +4.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.6 | +2.1 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.6 | -3.4 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.2 | -3.2 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -2.0 | -2.2 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -1.9 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | jumonji domain containing 6, arginine demethylase and lysine hydroxylase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.1 — chr17:76,712,832-76,726,799 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PTDSR1, KIAA0585; previously PTDSR |
| Gene groups (HGNC) | Iron (II) and 2-oxoglutarate dependent oxygenases |
| Hallmark sets | HYPOXIA |
| Reactome | 5 pathways, smallest: Protein hydroxylation; HDMs demethylate histones; Gamma carboxylation, hypusinylation, hydroxylation, and arylsulfatase activation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6NYC1](https://www.uniprot.org/uniprotkb/Q6NYC1) (Bifunctional arginine demethylase and lysyl-hydroxylase JMJD6):

> Dioxygenase that can both act as a arginine demethylase and a lysyl-hydroxylase. Acts as a lysyl-hydroxylase that catalyzes 5-hydroxylation on specific lysine residues of target proteins such as U2AF2/U2AF65 and LUC7L2. Regulates RNA splicing by mediating 5-hydroxylation of U2AF2/U2AF65, affecting the pre-mRNA splicing activity of U2AF2/U2AF65. Hydroxylates its own N-terminus, which is required for homooligomerization. Plays a role in the regulation of nucleolar liquid-liquid phase separation …

**Summary**, from NCBI Gene [23210](https://www.ncbi.nlm.nih.gov/gene/23210):

> This gene encodes a nuclear protein with a JmjC domain. JmjC domain-containing proteins are predicted to function as protein hydroxylases or histone demethylases. This protein was first identified as a putative phosphatidylserine receptor involved in phagocytosis of apoptotic cells; however, subsequent studies have indicated that it does not directly function in the clearance of apoptotic cells, and questioned whether it is a true phosphatidylserine receptor. Multiple transcript variants …

**Accessions** — [HGNC:19355](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19355) · Entrez [23210](https://www.ncbi.nlm.nih.gov/gene/23210) · UniProt [Q6NYC1](https://www.uniprot.org/uniprotkb/Q6NYC1) · Ensembl [ENSG00000070495](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000070495)

## Data

Gene col 953: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 953); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 953, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 953]; `tensor/DDL_lfc|DDL_z.npy` [953]; `embed/gene_vectors.npy` [953]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 953 or target_col == 953). Every well: [[JMJD6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/JMJD6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
