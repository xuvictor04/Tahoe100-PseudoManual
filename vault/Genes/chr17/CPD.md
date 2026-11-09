---
symbol: "CPD"
type: "gene"
col: 2969
ensembl_id: "ENSG00000108582"
name: "carboxypeptidase D"
location: "17q11.2"
module: 106
arm: "+"
pooled_cpm: 152.5
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 7
n_dd_up_clean: 13
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/106"]
generated_by: "tahoemap"
---

# CPD

*carboxypeptidase D* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.70× (z +18.3, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.05 µM: 0.782× (z -4.5, q 0.003, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COPS8]] (+0.71, fdr 7e-06), [[ATP1A1]] (+0.70, fdr 7e-06), [[B4GALT1]] (+0.68, fdr 7e-06); moves opposite to [[HDAC9]] (-0.64, fdr 1e-05), [[SLC7A11-AS1]] (-0.60, fdr 1e-05), [[IL23A]] (-0.57, fdr 1e-05).
> It is in [[Module 106]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[SLAMF7]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2969.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.70×** | +18.3 | 0e+00 | 46/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.33×** | +15.6 | 0e+00 | 46/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.32×** | +15.5 | 0e+00 | 46/48 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +8.8 | 2e-16 | 32/49 (RKO, NCI-H460, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.52×** | +7.8 | 9e-13 | 42/48 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.47×** | +7.1 | 1e-10 | 40/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.09×** | +7.1 | 1e-10 | 39/49 (SW480, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.42×** | +6.5 | 6e-09 | 32/49 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.43×** | +6.3 | 1e-08 | 32/44 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.39×** | +6.1 | 5e-08 | 36/48 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +5.8 | 4e-07 | 32/47 (LoVo, C-33 A, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change | **1.36×** | +5.7 | 5e-07 | 33/48 (KATO III, SW480, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.79×** | +5.6 | 8e-07 | 41/49 (LoVo, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.35×** | +5.2 | 9e-06 | 28/45 (SK-MEL-2, SW48, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.61×** | +4.6 | 2e-04 | 28/48 (SW480, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.23×** | +3.8 | 0.004 | 24/48 (A498, H4, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.21×** | +3.4 | 0.020 | 21/49 (A498, NCI-H1573, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | 1.20× | +3.3 | 0.024 | 24/48 (A498, NCI-H2347, …) | all doses, flat |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.41×** | +3.3 | 0.025 | 23/48 (H4, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 5 µM |  | 1.19× | +3.3 | 0.025 | 23/48 (A498, H4, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2969.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.782×** | -4.5 | 0.003 | 30/48 (SW 900, PANC-1, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.714×** | -4.4 | 0.003 | 27/48 (SW 900, SW480, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.941× | -3.9 | 0.016 | 0/50 | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.805×** | -3.9 | 0.016 | 24/47 (SW 900, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.810×** | -3.6 | 0.035 | 25/47 (AN3 CA, CHP-212, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.826×** | -3.5 | 0.038 | 22/48 (CFPAC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.767×** | -3.5 | 0.038 | 25/48 (LS 180, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **0.773×** | -3.4 | 0.049 | 29/49 (PANC-1, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 0.835× | -3.3 | 0.054 | 23/47 (A-427, NCI-H1792, …) | inconsistent across doses | low cells (technical?) |
| [[9-ING-41 (drug)]] 0.5 µM |  | 0.789× | -3.1 | 0.10 | 24/48 (NCI-H460, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | 0.841× | -3.1 | 0.11 | 23/49 (NCI-H2030, C32, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2969. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 113 | 23 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 4.22× (z +13.6) | — |
| [[NCI-H2347 (line)]] | alt | 438 | 22 | 0 | [[Triamcinolone (drug)]] 5 µM 2.10× (z +15.3) | — |
| [[A498 (line)]] | wt | 327 | 20 | 0 | [[Triamcinolone (drug)]] 0.5 µM 5.67× (z +19.6) | — |
| [[SW 900 (line)]] | alt | 304 | 18 | 1 | [[Clobetasol propionate (drug)]] 5 µM 3.74× (z +13.0) | [[Auranofin (drug)]] 5 µM 0.420× (z -8.5) |
| [[H4 (line)]] | wt | 120 | 17 | 0 | [[Clobetasol propionate (drug)]] 5 µM 4.34× (z +13.7) | — |
| [[Panc 03.27 (line)]] | alt | 180 | 17 | 0 | [[Triamcinolone (drug)]] 5 µM 2.10× (z +12.5) | — |
| [[SNU-423 (line)]] | alt | 199 | 17 | 0 | [[Clobetasol propionate (drug)]] 5 µM 3.64× (z +13.7) | — |
| [[A549 (line)]] | wt | 141 | 12 | 0 | [[Panobinostat (drug)]] 5 µM 2.75× (z +13.2) | — |
| [[SW480 (line)]] | alt | 104 | 10 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.47× (z +19.8) | — |
| [[CFPAC-1 (line)]] | alt | 353 | 7 | 2 (2 ⚠) | [[Clobetasol propionate (drug)]] 0.05 µM 2.85× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.530× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 89.0 | 9 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.02× (z +13.7) | — |
| [[PANC-1 (line)]] | alt | 134 | 9 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.85× (z +14.7) | — |
| [[HOP62 (line)]] | alt | 135 | 7 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.06× (z +14.2) | — |
| [[NCI-H460 (line)]] | wt | 121 | 7 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.56× (z +13.8) | — |
| [[KATO III (line)]] | alt | 150 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.83× (z +13.0) | — |
| [[LS 180 (line)]] | wt | 111 | 6 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.92× (z +12.6) | — |
| [[NCI-H1792 (line)]] | alt | 171 | 6 | 0 | [[Clobetasol propionate (drug)]] 5 µM 2.58× (z +10.5) | — |
| [[HEC-1-A (line)]] | alt | 178 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.86× (z +14.2) | — |
| [[Hs 766T (line)]] | wt | 60.2 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 3.71× (z +11.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 72.7 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.19× (z +14.6) | — |
| [[RKO (line)]] | wt | 113 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.61× (z +14.0) | — |
| [[SW1417 (line)]] | alt | 106 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.20× (z +13.2) | — |
| [[A-427 (line)]] | wt | 109 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.95× (z +13.3) | — |
| [[HS-578T (line)]] | alt | 156 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.69× (z +11.1) | [[Homoharringtonine (drug)]] 5 µM 0.572× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 79.5 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.31× (z +12.9) | — |
| [[LOX-IMVI (line)]] | wt | 88.7 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 5.13× (z +18.1) | — |
| [[NCI-H23 (line)]] | alt | 71.6 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.62× (z +12.9) | — |
| [[RPMI-7951 (line)]] | alt | 88.6 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.25× (z +11.2) | — |
| [[AsPC-1 (line)]] | alt | 136 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.08× (z +9.9) | — |
| [[HT-29 (line)]] | alt | 129 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.33× (z +10.3) | — |
| [[hTERT-HPNE (line)]] | wt | 119 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.32× (z +11.5) | — |
| [[NCI-H2030 (line)]] | alt | 103 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.71× (z +12.4) | — |
| [[SK-MEL-2 (line)]] | alt | 85.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.75× (z +10.6) | — |
| [[A-172 (line)]] | wt | 157 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.80× (z +10.6) | — |
| [[C-33 A (line)]] | alt | 125 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.50× (z +9.9) | — |
| [[SW48 (line)]] | wt | 118 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.40× (z +11.6) | — |
| [[AN3 CA (line)]] | alt | 182 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.302× (z -8.9) |
| [[BT-474 (line)]] | alt | 124 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.51× (z +9.1) | — |
| [[HCT15 (line)]] | alt | 118 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.74× (z +9.5) | — |
| [[SHP-77 (line)]] | alt | 160 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.16× (z +8.8) | — |
| [[SNU-1 (line)]] | wt | 134 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +9.3) | — |
| [[SW 1271 (line)]] | alt | 129 | 1 | 0 | [[Triamcinolone (drug)]] 5 µM 3.39× (z +8.5) | — |
| [[C32 (line)]] | wt | 128 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 95.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 227 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 182 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 99.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2969), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPS8]] | +0.71 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[ATP1A1]] | +0.70 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[B4GALT1]] | +0.68 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[ACSL1]] | +0.65 | +0.58 / +0.70 | both halves | 8e-06 |  |
| [[STOM]] | +0.65 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[SORT1]] | +0.64 | +0.60 / +0.61 | both halves | 7e-06 | pathway: Golgi Associated Vesicle Biogenesis; STRING 675 |
| [[ADAM15]] | +0.64 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[MAOA]] | +0.61 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[FTH1]] | +0.61 | +0.68 / +0.56 | both halves | 1e-05 | pathway: Golgi Associated Vesicle Biogenesis; STRING 517 |
| [[LAMP2]] | +0.61 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[PACSIN2]] | +0.60 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[CCND3]] | +0.60 | +0.62 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HDAC9]] | -0.64 | -0.64 / -0.56 | both halves | 1e-05 |  |
| [[SLC7A11-AS1]] | -0.60 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[IL23A]] | -0.57 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[LINC00973]] | -0.54 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[TRAF1]] | -0.54 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[MSANTD3]] | -0.54 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[OSGIN1]] | -0.54 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[CLCF1]] | -0.53 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[LINC00944]] | -0.53 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[C11orf68]] | -0.53 | -0.33 / -0.55 | both halves | 1e-04 |  |
| [[PPIF]] | -0.52 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[LINC01060]] | -0.52 | -0.54 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLAMF7]] | B | SLAMF7 activity raises CPD's level | lines that do not express SLAMF7 (34) vs lines expressing it (16) | 1.31× lower at baseline in the lines without SLAMF7 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG4, AMPH, RNF17 |
| [[TSC22D3]] | B | TSC22D3 activity raises CPD's level | lines that do not express TSC22D3 (11) vs lines expressing it (39) | 1.36× lower at baseline in the lines without TSC22D3 | 0.030 | ⚠ within organs, on part of the lines; also absent: IL15, IGFBP3, PAG1; maybe low, not absent |
| [[ADGRG2]] | B | ADGRG2 activity lowers CPD's level | lines that do not express ADGRG2 (10) vs lines expressing it (40) | 1.21× higher at baseline in the lines without ADGRG2 | 0.071 | ⚠ within organs, on part of the lines; also absent: KCNN3, SLC17A7, STARD8; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 106]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.671). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.3, 17.5); signed map (18.1, 27.9). **Vector** length 141, 50.1% of its response variance represented; |z| ≥ 3 in 1,626 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dexamethasone (drug)]] 0.5 µM |  | +7.5 | +3.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +7.4 | +3.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +7.1 | +3.3 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | +6.8 | +2.7 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | +6.4 | +3.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | -11.5 | -3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.4 | -2.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.9 | -3.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.5 | +1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.9 | -4.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.9 | -3.5 |
|  | [[vincristine (drug)]] 0.5 µM |  | -3.9 | -4.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.7 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | carboxypeptidase D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:30,378,927-30,469,989 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GP180 |
| Gene groups (HGNC) | M14 carboxypeptidases |
| Reactome | 9 pathways, smallest: RND1 GTPase cycle; RND3 GTPase cycle; Golgi Associated Vesicle Biogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [O75976](https://www.uniprot.org/uniprotkb/O75976) (Carboxypeptidase D):

> Functions in the processing of proteins and peptides in the secretory pathway. Mechanistically, cleaves exclusively C-terminal basic residues. By removing terminal residues, can modulate the activity, stability, and receptor-binding properties of bioactive peptides.; (Microbial infection) Acts as an alternative entry receptor for adeno-associated virus (AAV).

**Summary**, from NCBI Gene [1362](https://www.ncbi.nlm.nih.gov/gene/1362):

> The metallocarboxypeptidase family of enzymes is divided into 2 subfamilies based on sequence similarities. The pancreatic carboxypeptidase-like and the regulatory B-type carboxypeptidase subfamilies. Carboxypeptidase D has been identified as a regulatory B-type carboxypeptidase. CPD is a homolog of duck gp180, a hepatitis B virus-binding protein. Transcript variants utilizing alternative polyadenylation signals exist for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:2301](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2301) · Entrez [1362](https://www.ncbi.nlm.nih.gov/gene/1362) · UniProt [O75976](https://www.uniprot.org/uniprotkb/O75976) · Ensembl [ENSG00000108582](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108582)

## Data

Gene col 2969: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2969); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2969, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2969]; `tensor/DDL_lfc|DDL_z.npy` [2969]; `embed/gene_vectors.npy` [2969]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2969 or target_col == 2969). Every well: [[CPD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CPD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
