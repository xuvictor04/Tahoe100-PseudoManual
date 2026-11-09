---
symbol: "TSPAN13"
type: "gene"
col: 2772
ensembl_id: "ENSG00000106537"
name: "tetraspanin 13"
location: "7p21.1"
module: 42
arm: "+"
pooled_cpm: 50.75
n_lines_expressing: 37
n_dd_up: 29
n_dd_down: 11
n_dd_up_clean: 19
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 5
direction_downstream: 8
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# TSPAN13

*tetraspanin 13* — 7p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.63× (z +22.5, q 0e+00, up in 35 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.05 µM: 0.655× (z -7.4, q 8e-11, down in 22 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LMAN1]] (+0.66, fdr 1e-05), [[SEPTIN6]] (+0.66, fdr 1e-05), [[GGCX]] (+0.63, fdr 2e-05); moves opposite to [[INO80D]] (-0.65, fdr 1e-05), [[RPP38]] (-0.64, fdr 1e-05), [[CREBBP]] (-0.61, fdr 3e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[HNF4G]] → it (grade B ⚠); 8 go from it, the strongest it → [[F11R]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2772.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.63×** | +22.5 | 0e+00 | 35/35 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.27×** | +20.7 | 0e+00 | 35/35 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.19×** | +20.2 | 0e+00 | 35/35 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.87×** | +15.0 | 0e+00 | 33/35 (SW480, SW1417, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.32×** | +14.7 | 0e+00 | 34/35 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.99×** | +12.0 | 4e-31 | 27/35 (PANC-1, NCI-H1573, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.96×** | +11.7 | 6e-30 | 30/34 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.72×** | +9.5 | 2e-19 | 30/36 (SW1417, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.66×** | +8.8 | 6e-17 | 29/35 (HT-29, KATO III, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.72×** | +8.7 | 2e-16 | 19/30 (PANC-1, NCI-H1573, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **1.67×** | +8.6 | 6e-16 | 17/29 (PANC-1, KATO III, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.57×** | +7.9 | 2e-13 | 22/35 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.60×** | +7.7 | 4e-13 | 23/34 (HT-29, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.33×** | +7.7 | 5e-13 | 24/36 (PANC-1, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.36×** | +7.3 | 1e-11 | 17/34 (NCI-H1792, SW480, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.36×** | +5.3 | 3e-06 | 16/35 (HT-29, PANC-1, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.37×** | +3.9 | 0.002 | 14/35 (NCI-H1792, LoVo, …) | two highest doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **1.27×** | +3.9 | 0.002 | 14/35 (LoVo, A498, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.36×** | +3.8 | 0.003 | 9/36 (PANC-1, HT-29, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2772.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.655×** | -7.4 | 8e-11 | 22/35 (NCI-H2347, LoVo, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.748×** | -5.1 | 1e-04 | 19/34 (NCI-H2347, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.627×** | -4.3 | 0.004 | 15/36 (A498, NCI-H1792, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.774×** | -4.1 | 0.005 | 12/32 (HepG2/C3A, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | **0.791×** | -3.9 | 0.009 | 15/35 (NCI-H2347, LoVo, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.804×** | -3.8 | 0.013 | 17/36 (CFPAC-1, LoVo, …) | all doses, flat |  |
| [[AZD-8055 (drug)]] 5 µM |  | **0.672×** | -3.6 | 0.023 | 11/36 (NCI-H1792, A498, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.778×** | -3.6 | 0.026 | 10/36 (C32, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.822×** | -3.4 | 0.037 | 12/35 (NCI-H2030, HS-578T, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.863× | -3.4 | 0.038 | 7/35 (LoVo, PANC-1, …) | rises with dose |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.832×** | -3.2 | 0.061 | 11/34 (HepG2/C3A, A498, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.823×** | -3.2 | 0.061 | 13/35 (BT-474, NCI-H1573, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 5 µM |  | 0.879× | -3.1 | 0.082 | 7/36 (A498, Panc 03.27, …) | all doses, flat |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 0.838× | -3.1 | 0.082 | 9/35 (AsPC-1, COLO 205, …) | top dose only |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 0.842× | -3.0 | 0.099 | 9/35 (LoVo, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2772. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 47.4 | 1 (1 ⚠) | 8 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +8.9) ⚠ cell-cycle shift, explains ~29% of this change | [[Binimetinib (drug)]] 5 µM 0.152× (z -12.2) |
| [[PANC-1 (line)]] | alt | 44.4 | 9 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.62× (z +18.1) | — |
| [[HT-29 (line)]] | alt | 82.1 | 8 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.09× (z +12.6) | — |
| [[A498 (line)]] | wt | 229 | 2 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.14× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.11× (z +8.6) | [[Triamcinolone (drug)]] 5 µM 0.498× (z -11.1) |
| [[NCI-H460 (line)]] | wt | 45.3 | 6 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.44× (z +14.8) | — |
| [[SW480 (line)]] | alt | 32.4 | 6 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.35× (z +12.0) | — |
| [[A-427 (line)]] | wt | 23.5 | 4 (1 ⚠) | 1 | [[Belinostat (drug)]] 5 µM 4.70× (z +10.2) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.372× (z -9.1) |
| [[H4 (line)]] | wt | 41.1 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 7.49× (z +12.8) | — |
| [[KATO III (line)]] | alt | 143 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.81× (z +12.9) | — |
| [[NCI-H1573 (line)]] | alt | 18.6 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 7.01× (z +13.3) | — |
| [[NCI-H1792 (line)]] | alt | 36.4 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +12.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 4.18× (z +10.4) | — |
| [[SW1417 (line)]] | alt | 56.8 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 4.26× (z +11.6) | — |
| [[AsPC-1 (line)]] | alt | 72.7 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 5.34× (z +16.0) | — |
| [[HepG2_C3A (line)]] | wt | 26.3 | 3 | 1 | [[Tucidinostat (drug)]] 5 µM 3.66× (z +10.1) | [[Harringtonine (drug)]] 0.05 µM 0.153× (z -9.8) |
| [[HS-578T (line)]] | alt | 15.1 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 6.24× (z +10.5) | — |
| [[NCI-H2030 (line)]] | alt | 39.1 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 5.64× (z +14.9) | — |
| [[BT-474 (line)]] | alt | 162 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.75× (z +10.8) | — |
| [[CFPAC-1 (line)]] | alt | 50.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.43× (z +10.8) | — |
| [[NCI-H2347 (line)]] | alt | 137 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.438× (z -10.2) |
| [[HEC-1-A (line)]] | alt | 14.7 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.11× (z +9.6) | — |
| [[Panc 03.27 (line)]] | alt | 43.2 | 2 | 0 | [[Belinostat (drug)]] 5 µM 3.23× (z +9.0) | — |
| [[SNU-1 (line)]] | wt | 77.8 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.236× (z -14.0) ⚠ cell-cycle shift, explains ~40% of this change |
| [[NCI-H661 (line)]] | alt | 37.5 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.5 µM 0.0710× (z -8.7) |
| [[SHP-77 (line)]] | alt | 71.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.50× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[A-172 (line)]] | wt | 6.65 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 12.6 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.49 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 12.0 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 64.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.29 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.98 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 11.7 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 95.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.61 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 79.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.41 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 67.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.50 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.74 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.79 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.18 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 54.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2772), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LMAN1]] | +0.66 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[SEPTIN6]] | +0.66 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[GGCX]] | +0.63 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[RIMS3]] | +0.62 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[HSPA5]] | +0.61 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[CALU]] | +0.61 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[ANXA6]] | +0.60 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[PDIA4]] | +0.59 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[SAR1A]] | +0.59 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[FKBP14]] | +0.58 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[P3H1]] | +0.58 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[TTC3]] | +0.58 | +0.40 / +0.56 | both halves | 5e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INO80D]] | -0.65 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[RPP38]] | -0.64 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[CREBBP]] | -0.61 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[ITPA]] | -0.61 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[HSPBAP1]] | -0.60 | -0.48 / -0.39 | both halves | 6e-05 |  |
| [[ZFX]] | -0.58 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[LATS1]] | -0.58 | -0.37 / -0.50 | both halves | 7e-05 |  |
| [[RNF146]] | -0.58 | -0.40 / -0.47 | both halves | 4e-05 |  |
| [[CCAR1]] | -0.57 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[NOL8]] | -0.55 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[CCDC137]] | -0.55 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[MED13]] | -0.54 | -0.39 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HNF4G]] | B | HNF4G activity raises TSPAN13's level | lines that do not express HNF4G (16) vs lines expressing it (34) | 3.60× lower at baseline in the lines without HNF4G | 0.004 | ⚠ within organs, on part of the lines; also absent: MPZL3, ELF3, ARHGEF5 |
| [[F11R]] | B | F11R activity raises TSPAN13's level | lines that do not express F11R (10) vs lines expressing it (40) | 3.20× lower at baseline in the lines without F11R | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000287306, LONRF3, TUBA4A |
| [[MTOR]] | B | MTOR activity raises TSPAN13's level | compounds that target MTOR: 5 of 8 lower it (AZD-8055, Bimiralisib, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 2.8% of all compounds | 0.006 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[FHL1]] | B | FHL1 activity lowers TSPAN13's level | lines that do not express FHL1 (19) vs lines expressing it (31) | 2.07× higher at baseline in the lines without FHL1 | 0.059 | ⚠ within organs, on part of the lines; also absent: ADAMTS7, ANTXR1, MSRB3 |
| [[ACTR3C]] | B | ACTR3C activity raises TSPAN13's level | lines that do not express ACTR3C (15) vs lines expressing it (35) | 2.16× lower at baseline in the lines without ACTR3C | 0.071 | ⚠ within organs, on part of the lines; also absent: LRRC61, ENPP4, ENSG00000263325 |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[F11R]] | B | TSPAN13 activity raises F11R's level | lines that do not express TSPAN13 (13) vs lines expressing it (37) | 2.87× lower at baseline in the lines without TSPAN13 | 0.026 | ⚠ within organs, on part of the lines; also absent: JUP, MPZL3, MYO5C |
| cells under [[Doxorubicin (hydrochloride) (drug)]] 5 µM | B | TSPAN13 activity raises the cells' numbers under Doxorubicin (hydrochloride) 5 µM (protects the cells) | lines that do not express TSPAN13 (13) vs lines expressing it (35) | the lines without TSPAN13: 0.59× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; also absent: JUP, MPZL3, MYO5C |
| [[CMTR2]] | B | TSPAN13 activity lowers CMTR2's level | lines that do not express TSPAN13 (13) vs lines expressing it (37) | 1.30× higher at baseline in the lines without TSPAN13 | 0.053 | ⚠ within organs, on part of the lines; also absent: JUP, MPZL3, MYO5C |
| [[RGS10]] | B | TSPAN13 activity lowers RGS10's level | lines that do not express TSPAN13 (13) vs lines expressing it (37) | 1.64× higher at baseline in the lines without TSPAN13 | 0.066 | ⚠ within organs, on part of the lines; also absent: JUP, MPZL3, MYO5C |
| cells under [[Docetaxel (drug)]] 5 µM | B | TSPAN13 activity raises the cells' numbers under Docetaxel 5 µM (protects the cells) | lines that do not express TSPAN13 (13) vs lines expressing it (35) | the lines without TSPAN13: 0.88× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: JUP, MPZL3, MYO5C |
| cells under [[Gallic acid (hydrate) (drug)]] 0.05 µM | B | TSPAN13 activity lowers the cells' numbers under Gallic acid (hydrate) 0.05 µM (makes them more sensitive) | lines that do not express TSPAN13 (13) vs lines expressing it (35) | the lines without TSPAN13: 1.16× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: JUP, MPZL3, MYO5C |
| [[TM9SF2]] | B | TSPAN13 activity raises TM9SF2's level | lines that do not express TSPAN13 (13) vs lines expressing it (37) | 1.42× lower at baseline in the lines without TSPAN13 | 0.074 | ⚠ within organs, on part of the lines; also absent: JUP, MPZL3, MYO5C |
| cells under [[Docetaxel (drug)]] 0.5 µM | B | TSPAN13 activity raises the cells' numbers under Docetaxel 0.5 µM (protects the cells) | lines that do not express TSPAN13 (13) vs lines expressing it (35) | the lines without TSPAN13: 0.87× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: JUP, MPZL3, MYO5C |

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.589). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (7.0, -6.1); signed map (-53.2, 6.2). **Vector** length 94.7, 22.8% of its response variance represented; |z| ≥ 3 in 1,053 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.4 | +15.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.2 | +9.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.0 | +14.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.1 | +11.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.6 | +7.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.6 | +1.5 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +1.5 | +2.3 |
|  | [[Lopinavir (drug)]] 5 µM |  | +1.3 | +1.1 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -6.5 | -5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.5 | -7.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | +1.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.0 | +1.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.7 | -3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | +0.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.4 | -4.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.2 | +0.6 |

## What is on record

|  |  |
|---|---|
| Name | tetraspanin 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p21.1 — chr7:16,753,755-16,784,536 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NET-6; previously TM4SF13 |
| Gene groups (HGNC) | Tetraspanin family |
| Hallmark sets | KRAS_SIGNALING_UP, ESTROGEN_RESPONSE_LATE |
| Matched by | ensembl_id |

UniProt [O95857](https://www.uniprot.org/uniprotkb/O95857) carries no function annotation.

**Summary**, from NCBI Gene [27075](https://www.ncbi.nlm.nih.gov/gene/27075):

> The protein encoded by this gene is a member of the transmembrane 4 superfamily, also known as the tetraspanin family. Most of these members are cell-surface proteins that are characterized by the presence of four hydrophobic domains. The proteins mediate signal transduction events that play a role in the regulation of cell development, activation, growth and motility. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:21643](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21643) · Entrez [27075](https://www.ncbi.nlm.nih.gov/gene/27075) · UniProt [O95857](https://www.uniprot.org/uniprotkb/O95857) · Ensembl [ENSG00000106537](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106537)

## Data

Gene col 2772: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2772); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2772, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2772]; `tensor/DDL_lfc|DDL_z.npy` [2772]; `embed/gene_vectors.npy` [2772]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2772 or target_col == 2772). Every well: [[TSPAN13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TSPAN13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
