---
symbol: "AKIRIN1"
type: "gene"
col: 10505
ensembl_id: "ENSG00000174574"
name: "akirin 1"
location: "1p34.3"
module: 178
arm: "+"
pooled_cpm: 57.59
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 5
n_dd_up_clean: 13
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/178"]
generated_by: "tahoemap"
---

# AKIRIN1

*akirin 1* — 1p34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.77× (z +25.8, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.05 µM: 0.738× (z -5.5, q 2e-05, down in 33 of 48 measured lines) ⚠ cell-cycle shift, explains ~21% of this change. The strongest without an alert is [[Osimertinib (mesylate) (drug)]] 5 µM: 0.793× (z -4.2, q 0.004, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TNFRSF12A]] (+0.60, fdr 1e-05), [[ANAPC7]] (+0.59, fdr 1e-05), [[ACTR2]] (+0.59, fdr 1e-05); moves opposite to [[NSA2]] (-0.62, fdr 1e-05), [[ELP2]] (-0.60, fdr 9e-06), [[FAM185BP]] (-0.59, fdr 1e-05).
> It is in [[Module 178]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 17 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10505.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.77×** | +25.8 | 0e+00 | 48/48 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.05×** | +19.2 | 0e+00 | 48/48 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.56×** | +16.8 | 0e+00 | 47/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.45×** | +16.1 | 0e+00 | 46/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.12×** | +13.5 | 2e-39 | 46/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.11×** | +13.4 | 9e-39 | 47/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.06×** | +12.9 | 3e-36 | 43/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.05×** | +12.9 | 6e-36 | 42/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.70×** | +9.5 | 2e-19 | 37/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.66×** | +9.0 | 9e-18 | 38/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.59×** | +7.9 | 1e-13 | 37/47 (PANC-1, J82, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.54×** | +7.7 | 6e-13 | 36/48 (SW480, SNU-423, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.49×** | +7.1 | 4e-11 | 34/48 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.41×** | +6.1 | 3e-08 | 35/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.32×** | +5.0 | 2e-05 | 29/48 (RPMI-7951, HT-29, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.68×** | +4.5 | 3e-04 | 27/49 (SW480, AsPC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.65×** | +4.3 | 4e-04 | 21/48 (NCI-H1573, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.27×** | +4.2 | 7e-04 | 21/48 (LS 180, hTERT-HPNE, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +4.1 | 9e-04 | 21/48 (MIA PaCa-2, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.25×** | +3.7 | 0.004 | 23/48 (KATO III, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10505.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.738×** | -5.5 | 2e-05 | 33/48 (RPMI-7951, HT-29, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.753×** | -5.1 | 8e-05 | 30/48 (SW 1088, AsPC-1, …) | all doses, flat |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.793×** | -4.2 | 0.004 | 25/48 (AsPC-1, SNU-423, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.650×** | -3.8 | 0.021 | 22/47 (KATO III, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.682×** | -3.4 | 0.083 | 10/48 (A498, A-427, …) | rises with dose | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Temsirolimus (drug)]] 0.5 µM |  | 0.834× | -3.3 | 0.083 | 17/47 (NCI-H2347, SNU-423, …) | two highest doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.835× | -3.3 | 0.083 | 13/48 (KATO III, NCI-H23, …) | two highest doses |  |
| [[Cabozantinib (S-malate) (drug)]] 0.5 µM |  | 0.838× | -3.2 | 0.089 | 17/48 (SW480, hTERT-HPNE, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | 0.886× | -3.1 | 0.10 | 15/48 (NCI-H1792, AsPC-1, …) | all doses, flat | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10505. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 45.3 | 11 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +18.8) | — |
| [[SW480 (line)]] | alt | 56.5 | 10 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.29× (z +17.3) | — |
| [[HOP62 (line)]] | alt | 49.7 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.70× (z +19.8) | — |
| [[PANC-1 (line)]] | alt | 66.0 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +23.0) | — |
| [[NCI-H1573 (line)]] | alt | 77.4 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +16.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 72.3 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +15.8) | — |
| [[NCI-H1792 (line)]] | alt | 35.3 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +12.3) | [[Selinexor (drug)]] 5 µM 0.432× (z -9.8) ⚠ cell-cycle shift, explains ~50% of this change |
| [[AsPC-1 (line)]] | alt | 56.7 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.97× (z +18.6) | [[Selinexor (drug)]] 5 µM 0.500× (z -9.4) ⚠ cell-cycle shift, explains ~50% of this change |
| [[CFPAC-1 (line)]] | alt | 34.0 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.75× (z +20.1) | — |
| [[HEC-1-A (line)]] | alt | 66.8 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +18.0) | — |
| [[HS-578T (line)]] | alt | 55.8 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +12.0) | — |
| [[LOX-IMVI (line)]] | wt | 61.1 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +13.6) | — |
| [[A-427 (line)]] | wt | 96.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +16.0) | — |
| [[A498 (line)]] | wt | 58.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +15.3) | — |
| [[A549 (line)]] | wt | 47.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +15.6) | — |
| [[LoVo (line)]] | wt | 42.0 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.51× (z +12.2) | — |
| [[NCI-H2347 (line)]] | alt | 42.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +14.7) | — |
| [[BT-474 (line)]] | alt | 50.6 | 3 | 0 | [[Digitoxin (drug)]] 0.5 µM 3.67× (z +10.0) | — |
| [[Hs 766T (line)]] | wt | 40.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +14.0) | — |
| [[KATO III (line)]] | alt | 27.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +13.7) | — |
| [[LS 180 (line)]] | wt | 48.6 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.40× (z +12.3) | — |
| [[NCI-H23 (line)]] | alt | 154 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.45× (z +10.5) | — |
| [[SNU-1 (line)]] | wt | 62.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +10.8) | — |
| [[SW48 (line)]] | wt | 68.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +12.8) | — |
| [[COLO 205 (line)]] | alt | 29.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +12.9) | — |
| [[HT-29 (line)]] | alt | 80.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +13.6) | — |
| [[hTERT-HPNE (line)]] | wt | 40.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +12.8) | — |
| [[NCI-H2030 (line)]] | alt | 60.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +13.7) | — |
| [[Panc 03.27 (line)]] | alt | 84.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +13.1) | — |
| [[RPMI-7951 (line)]] | alt | 42.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +12.6) | — |
| [[SK-MEL-2 (line)]] | alt | 79.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +14.7) | — |
| [[SNU-423 (line)]] | alt | 25.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +13.4) | — |
| [[SW 900 (line)]] | alt | 57.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +9.7) | — |
| [[SW1417 (line)]] | alt | 58.8 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.54× (z +9.9) | — |
| [[A-172 (line)]] | wt | 50.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +8.5) | — |
| [[C32 (line)]] | wt | 50.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +11.0) | — |
| [[H4 (line)]] | wt | 24.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.70× (z +11.7) | — |
| [[HCT15 (line)]] | alt | 42.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +11.2) | — |
| [[HepG2_C3A (line)]] | wt | 59.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +10.6) | — |
| [[J82 (line)]] | alt | 66.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +10.6) | — |
| [[AN3 CA (line)]] | alt | 73.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 91.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 66.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10505), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*36 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNFRSF12A]] | +0.60 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[ANAPC7]] | +0.59 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[ACTR2]] | +0.59 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[KPNA4]] | +0.57 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[CRK]] | +0.56 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[ZNF518B]] | +0.56 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[VEZF1]] | +0.56 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[SOCS4]] | +0.56 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[SKIL]] | +0.56 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[PSME3]] | +0.55 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[WDR82]] | +0.55 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[LIG4]] | +0.55 | +0.45 / +0.57 | both halves | 3e-05 |  |

## Genes that move opposite

*64 of its nearest partners move opposite, 7 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NSA2]] | -0.62 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[ELP2]] | -0.60 | -0.57 / -0.59 | both halves | 9e-06 |  |
| [[FAM185BP]] | -0.59 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[CDK7]] | -0.58 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[CWC15]] | -0.57 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[NDUFAF7]] | -0.57 | -0.46 / -0.64 | both halves | 2e-05 |  |
| [[PPOX]] | -0.57 | -0.47 / -0.60 | both halves | 2e-05 |  |
| [[NACA]] ⚠ | -0.57 | -0.53 / -0.53 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL21]] ⚠ | -0.57 | -0.49 / -0.57 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[EGFL8]] | -0.56 | -0.42 / -0.59 | both halves | 4e-05 |  |
| [[EPB41L4A-AS1]] | -0.56 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[RPL5]] | -0.56 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[ASB7]] | -0.56 | -0.50 / -0.62 | both halves | 1e-05 |  |
| [[FAM174A]] | -0.56 | -0.48 / -0.60 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 178]]; 22 genes; every member is in the + arm (projection on the module's main direction -0.580). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (0.6, -20.1); signed map (-5.9, 38.4). **Vector** length 87.6, 24.8% of its response variance represented; |z| ≥ 3 in 1,159 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +5.9 | +13.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.8 | +19.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +3.7 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.7 | +6.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | +3.5 | +7.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +7.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.4 | -0.1 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | +2.3 | +0.6 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +2.2 | +1.7 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -7.0 | -3.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -5.1 | -5.1 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | -4.6 | -5.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.9 | +4.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -3.3 | -4.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.3 | +4.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.8 | -2.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.5 | -3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.3 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | akirin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.3 — chr1:38,991,276-39,006,059 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12666; previously C1orf108 |
| Gene groups (HGNC) | Akirin family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H9L7](https://www.uniprot.org/uniprotkb/Q9H9L7) (Akirin-1):

> Molecular adapter that acts as a bridge between proteins, and which is involved skeletal muscle development (By similarity). Functions as a signal transducer for MSTN during skeletal muscle regeneration and myogenesis (By similarity). May regulate chemotaxis of both macrophages and myoblasts by reorganising actin cytoskeleton, leading to more efficient lamellipodia formation via a PI3 kinase dependent pathway (By similarity). In contrast to AKIRIN2, not involved in nuclear import of proteasomes.

**Summary**, from NCBI Gene [79647](https://www.ncbi.nlm.nih.gov/gene/79647):

> Predicted to enable transcription coregulator activity. Predicted to be involved in several processes, including myoblast migration involved in skeletal muscle regeneration; negative regulation of satellite cell differentiation; and positive regulation of lamellipodium assembly. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25744](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25744) · Entrez [79647](https://www.ncbi.nlm.nih.gov/gene/79647) · UniProt [Q9H9L7](https://www.uniprot.org/uniprotkb/Q9H9L7) · Ensembl [ENSG00000174574](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174574)

## Data

Gene col 10505: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10505); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10505, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10505]; `tensor/DDL_lfc|DDL_z.npy` [10505]; `embed/gene_vectors.npy` [10505]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10505 or target_col == 10505). Every well: [[AKIRIN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AKIRIN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
