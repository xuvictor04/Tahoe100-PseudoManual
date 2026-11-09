---
symbol: "EREG"
type: "gene"
col: 4580
ensembl_id: "ENSG00000124882"
name: "epiregulin"
location: "4q13.3"
module: 113
arm: "+"
pooled_cpm: 110.61
n_lines_expressing: 24
n_dd_up: 23
n_dd_down: 23
n_dd_up_clean: 10
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 11
direction_downstream: 11
tags: ["gene", "module/113"]
generated_by: "tahoemap"
---

# EREG

*epiregulin* — 4q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.96× (z +18.3, q 0e+00, up in 19 of 23 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.18× (z +10.3, q 5e-23, up in 17 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.603× (z -6.7, q 1e-08, down in 16 of 22 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CXCL1]] (+0.54, fdr 7e-05), [[TIPARP]] (+0.53, fdr 2e-05), [[SIPA1L2]] (+0.51, fdr 6e-05); moves opposite to [[MIEF2]] (-0.49, fdr 1e-04), [[FZR1]] (-0.49, fdr 1e-04), [[GTF3C5]] (-0.48, fdr 7e-05).
> It is in [[Module 113]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[CXCL2]] → it (grade B ⚠); 11 go from it, the strongest it → [[EXTL2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4580.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.96×** | +18.3 | 0e+00 | 19/23 (LOX-IMVI, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.71×** | +16.7 | 0e+00 | 14/19 (NCI-H2347, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.08×** | +13.8 | 5e-41 | 14/20 (NCI-H2347, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.47×** | +12.0 | 4e-31 | 14/22 (MIA PaCa-2, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.82×** | +11.3 | 1e-27 | 14/22 (AsPC-1, CFPAC-1, …) | rises with dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.18×** | +10.3 | 5e-23 | 17/22 (AsPC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.20×** | +10.1 | 7e-22 | 20/21 (AsPC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.73×** | +7.3 | 2e-11 | 17/23 (RPMI-7951, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.77×** | +7.1 | 9e-11 | 18/23 (AsPC-1, CFPAC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.70×** | +7.0 | 1e-10 | 20/22 (MIA PaCa-2, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +6.8 | 4e-10 | 16/22 (RPMI-7951, HOP62, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.70×** | +6.8 | 4e-10 | 16/22 (A549, AsPC-1, …) | rises with dose | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.32×** | +5.8 | 2e-07 | 8/16 (NCI-H2347, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.51×** | +5.5 | 2e-06 | 16/22 (AsPC-1, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.48×** | +5.2 | 6e-06 | 20/22 (MIA PaCa-2, AsPC-1, …) | rises with dose |  |
| [[Gemcitabine (drug)]] 0.5 µM |  | **1.35×** | +4.1 | 0.002 | 9/22 (CFPAC-1, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.05 µM |  | **1.33×** | +3.8 | 0.005 | 6/22 (AsPC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 5 µM |  | **1.29×** | +3.4 | 0.018 | 10/22 (HCT15, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.37×** | +3.0 | 0.069 | 1/22 (NCI-H1792) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.25×** | +3.0 | 0.072 | 9/22 (RPMI-7951, LS 180, …) | all doses, stronger at high dose |  |
| [[Gemcitabine (drug)]] 0.05 µM |  | **1.24×** | +3.0 | 0.075 | 12/22 (CFPAC-1, HOP62, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4580.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.603×** | -6.7 | 1e-08 | 16/22 (LS 180, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **0.715×** | -5.7 | 4e-06 | 12/22 (SW48, NCI-H23, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.654×** | -5.6 | 5e-06 | 16/22 (LS 180, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **0.669×** | -5.3 | 1e-05 | 16/24 (SW48, SW 900, …) | all doses, flat | cell-cycle shift (explains ~23% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.659×** | -5.3 | 1e-05 | 14/21 (SW48, HOP62, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.675×** | -5.2 | 2e-05 | 11/21 (NCI-H23, SW48, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.670×** | -4.9 | 9e-05 | 11/22 (NCI-H23, SW48, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.692×** | -4.8 | 9e-05 | 12/22 (LS 180, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **0.503×** | -4.7 | 1e-04 | 19/22 (LoVo, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.754×** | -4.5 | 3e-04 | 15/22 (SW 900, SW48, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.760×** | -4.4 | 5e-04 | 12/22 (SW48, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.527×** | -4.4 | 5e-04 | 14/24 (SW 900, SW48, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.915× | -4.1 | 0.002 | 4/24 (NCI-H23, HOP62, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | **0.808×** | -3.9 | 0.003 | 14/22 (SW 900, NCI-H23, …) | rises with dose |  |
| [[Afatinib (drug)]] 5 µM |  | **0.718×** | -3.6 | 0.013 | 16/23 (SW 900, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.763×** | -3.5 | 0.014 | 5/22 (LS 180, LOX-IMVI, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4580. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 372 | 0 | 13 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.186× (z -15.4) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Trametinib (drug)]] 5 µM 0.161× (z -11.6) |
| [[A549 (line)]] | wt | 283 | 6 (5 ⚠) | 3 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 5.43× (z +12.9) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.56× (z +10.0) | [[Panobinostat (drug)]] 0.5 µM 0.172× (z -14.0) |
| [[LoVo (line)]] | wt | 336 | 4 (2 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.55× (z +12.2) | [[Panobinostat (drug)]] 5 µM 0.109× (z -21.2) |
| [[LOX-IMVI (line)]] | wt | 56.0 | 9 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.55× (z +14.3) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.81× (z +11.8) | — |
| [[AsPC-1 (line)]] | alt | 78.7 | 8 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.76× (z +23.9) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 11.1× (z +18.7) | — |
| [[HOP62 (line)]] | alt | 75.4 | 6 (5 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.11× (z +12.4) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 7.50× (z +10.8) | [[Adagrasib (drug)]] 0.05 µM 0.472× (z -13.3) ⚠ position not correctable |
| [[LS 180 (line)]] | wt | 604 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0589× (z -26.6) |
| [[MIA PaCa-2 (line)]] | alt | 579 | 6 (5 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.71× (z +12.5) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 7.87× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.233× (z -19.6) ⚠ cell-cycle shift, explains ~15% of this change |
| [[SW 900 (line)]] | alt | 379 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.174× (z -13.2) |
| [[HEC-1-A (line)]] | alt | 258 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +9.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.169× (z -16.2) |
| [[CFPAC-1 (line)]] | alt | 357 | 3 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +17.9) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 9.26× (z +10.4) | [[Panobinostat (drug)]] 0.5 µM 0.281× (z -11.3) |
| [[NCI-H23 (line)]] | alt | 50.0 | 1 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +9.2) ⚠ cell-cycle shift, explains ~47% of this change | [[Adagrasib (drug)]] 0.05 µM 0.299× (z -20.2) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 5 µM 0.132× (z -10.4) |
| [[Hs 766T (line)]] | wt | 71.3 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +10.6) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[HT-29 (line)]] | alt | 188 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.237× (z -11.0) |
| [[NCI-H2347 (line)]] | alt | 141 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.32× (z +11.6) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 153 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.251× (z -10.1) |
| [[RPMI-7951 (line)]] | alt | 126 | 3 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.11× (z +9.7) | — |
| [[NCI-H1792 (line)]] | alt | 248 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -14.8) ⚠ cell-cycle shift, explains ~15% of this change |
| [[COLO 205 (line)]] | alt | 200 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -9.7) ⚠ cell-cycle shift, explains ~15% of this change |
| [[SW1417 (line)]] | alt | 42.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +8.5) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[A-172 (line)]] | wt | 6.84 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 26.4 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 6.21 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 14.2 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 8.19 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 9.60 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 6.94 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 15.9 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 8.28 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.1 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 7.10 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.1 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 7.10 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 11.7 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 22.2 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 7.68 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 83.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.2 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 95.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.84 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 9.82 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 7.33 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 6.80 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.60 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 8.71 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 8.39 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 93.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.46 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 18.6 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4580), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CXCL1]] | +0.54 | +0.38 / +0.55 | both halves | 7e-05 | STRING 461 |
| [[TIPARP]] | +0.53 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[SIPA1L2]] | +0.51 | +0.38 / +0.45 | both halves | 6e-05 |  |
| [[TARID]] | +0.50 | +0.40 / +0.54 | both halves | 5e-05 |  |
| [[ODC1]] | +0.50 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[ABCC3]] | +0.49 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[TGFBR2]] | +0.48 | +0.48 / +0.40 | both halves | 5e-05 |  |
| [[QPCT]] | +0.48 | +0.31 / +0.57 | both halves | 2e-04 |  |
| [[BIRC3]] | +0.48 | +0.42 / +0.50 | both halves | 4e-05 | pathway: HALLMARK_APOPTOSIS |
| [[CCL20]] | +0.47 | +0.40 / +0.47 | both halves | 5e-05 | pathway: HALLMARK_INFLAMMATORY_RESPONSE; STRING 405 |
| [[CPT1A]] | +0.47 | +0.38 / +0.37 | both halves | 8e-05 |  |
| [[CASC19]] | +0.47 | +0.53 / +0.39 | both halves | 6e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIEF2]] | -0.49 | -0.33 / -0.53 | both halves | 1e-04 |  |
| [[FZR1]] | -0.49 | -0.36 / -0.52 | both halves | 1e-04 |  |
| [[GTF3C5]] | -0.48 | -0.37 / -0.44 | both halves | 7e-05 |  |
| [[TRADD]] | -0.46 | -0.37 / -0.41 | both halves | 7e-05 |  |
| [[LSP1P4]] | -0.46 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[PRMT2]] | -0.45 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[BTRC]] | -0.45 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[RAB11FIP5]] | -0.44 | -0.27 / -0.48 | both halves | 3e-04 |  |
| [[KCTD7]] | -0.43 | -0.38 / -0.37 | both halves | 8e-05 |  |
| [[TULP3]] | -0.43 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[ZFPL1]] | -0.43 | -0.30 / -0.40 | both halves | 2e-04 |  |
| [[KLHDC10]] | -0.43 | -0.36 / -0.41 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 4, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CXCL2]] | B | CXCL2 activity raises EREG's level | lines that do not express CXCL2 (14) vs lines expressing it (36) | 2.90× lower at baseline in the lines without CXCL2 | 0.015 | ⚠ within organs, on part of the lines; also absent: TENT5A, GPR39, CXCL3 |
| [[CXCL8]] | B | CXCL8 activity raises EREG's level | lines that do not express CXCL8 (20) vs lines expressing it (30) | 1.97× lower at baseline in the lines without CXCL8 | 0.060 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, IL1R1, C15orf48 |
| [[MAP2K1]] | B | MAP2K1 activity raises EREG's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[BIRC3]] | B | BIRC3 activity raises EREG's level | lines that do not express BIRC3 (5) vs lines expressing it (45) | 4.00× lower at baseline in the lines without BIRC3 | 0.094 | ⚠ within organs, on part of the lines; also absent: LRRC8E, TRIM34, IFI35 |
| [[ABCC3]] | C | ABCC3 activity raises EREG's level | lines that do not express ABCC3 (16) vs lines expressing it (34) | 4.26× lower at baseline in the lines without ABCC3 | 0.021 | ⚠ within organs, on part of the lines; also absent: AQP3, CDC42BPG, NUP62CL; co-absent with the target |
| [[AREG]] | C | AREG activity raises EREG's level | lines that do not express AREG (26) vs lines expressing it (24) | 5.09× lower at baseline in the lines without AREG | 0.025 | ⚠ within organs, on part of the lines; also absent: TC2N, ESRP1, CRB3; co-absent with the target |
| [[SGPP2]] | C | SGPP2 activity raises EREG's level | lines that do not express SGPP2 (32) vs lines expressing it (18) | 4.99× lower at baseline in the lines without SGPP2 | 0.026 | ⚠ within organs, on part of the lines; also absent: ST14, CATSPERB, TMPRSS4; co-absent with the target |
| [[QPCT]] | C | QPCT activity raises EREG's level | lines that do not express QPCT (25) vs lines expressing it (25) | 3.02× lower at baseline in the lines without QPCT | 0.042 | ⚠ within organs, on part of the lines; also absent: WFDC10B, LRRN1, KRT81; co-absent with the target |
| [[SHH]] | C | SHH activity raises EREG's level | lines that do not express SHH (29) vs lines expressing it (21) | 4.42× lower at baseline in the lines without SHH | 0.057 | ⚠ within organs, on part of the lines; also absent: KLK6, HSD17B2, EPS8L3; co-absent with the target |
| [[ACSL5]] | C | ACSL5 activity raises EREG's level | lines that do not express ACSL5 (24) vs lines expressing it (26) | 3.48× lower at baseline in the lines without ACSL5 | 0.059 | ⚠ within organs, on part of the lines; also absent: TNFRSF14-AS1, IL20RA, TINAGL1; co-absent with the target |
| [[CASC19]] | C | CASC19 activity raises EREG's level | lines that do not express CASC19 (28) vs lines expressing it (22) | 4.19× lower at baseline in the lines without CASC19 | 0.081 | ⚠ within organs, on part of the lines; also absent: KLK10, KLK6, TNS4; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 7, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EXTL2]] | B | EREG activity lowers EXTL2's level | lines that do not express EREG (26) vs lines expressing it (24) | 1.41× higher at baseline in the lines without EREG | 0.008 | ⚠ within organs, on part of the lines; also absent: DPP4, IL20RA, HS3ST1 |
| [[ZC3H12A]] | B | EREG activity raises ZC3H12A's level | lines that do not express EREG (26) vs lines expressing it (24) | 1.66× lower at baseline in the lines without EREG | 0.009 | ⚠ within organs, on part of the lines; also absent: DPP4, IL20RA, HS3ST1 |
| [[SDHAP2]] | B | EREG activity raises SDHAP2's level | lines that do not express EREG (26) vs lines expressing it (24) | 1.35× lower at baseline in the lines without EREG | 0.022 | ⚠ within organs, on part of the lines; also absent: DPP4, IL20RA, HS3ST1 |
| [[CXCL2]] | B | EREG activity raises CXCL2's level | lines that do not express EREG (26) vs lines expressing it (24) | 1.71× lower at baseline in the lines without EREG | 0.033 | ⚠ within organs, on part of the lines; also absent: DPP4, IL20RA, HS3ST1 |
| [[MTHFD2L]] | B | EREG activity strengthens MTHFD2L's drug response | lines that do not express EREG (25) vs lines expressing it (22) | the lines without EREG respond 0.59× as strongly (z diff +1.60); strongest at Homoharringtonine 5 µM: 1.18x vs 1.64x (z diff +3.2) | 0.056 | ⚠ within organs, on part of the lines; also absent: DPP4, IL20RA, HS3ST1; target measured in part of the lines; artifact flags |
| [[TCIM]] | B | EREG activity raises TCIM's level | lines that do not express EREG (26) vs lines expressing it (24) | 1.47× lower at baseline in the lines without EREG | 0.083 | ⚠ within organs, on part of the lines; also absent: DPP4, IL20RA, HS3ST1 |
| [[TGFBR2]] | B | EREG activity raises TGFBR2's level | lines that do not express EREG (26) vs lines expressing it (24) | 2.16× lower at baseline in the lines without EREG | 0.091 | ⚠ within organs, on part of the lines; also absent: DPP4, IL20RA, HS3ST1 |
| [[ACSL5]] | C | EREG activity raises ACSL5's level | lines that do not express EREG (26) vs lines expressing it (24) | 3.42× lower at baseline in the lines without EREG | 0.002 | ⚠ within organs, on part of the lines; also absent: DPP4, IL20RA, HS3ST1; co-absent with the target |
| [[ABCC3]] | C | EREG activity raises ABCC3's level | lines that do not express EREG (26) vs lines expressing it (24) | 2.55× lower at baseline in the lines without EREG | 0.006 | ⚠ within organs, on part of the lines; also absent: DPP4, IL20RA, HS3ST1; co-absent with the target |
| [[SGPP2]] | C | EREG activity raises SGPP2's level | lines that do not express EREG (26) vs lines expressing it (24) | 4.39× lower at baseline in the lines without EREG | 0.014 | ⚠ within organs, on part of the lines; also absent: DPP4, IL20RA, HS3ST1; co-absent with the target |
| [[SHH]] | C | EREG activity raises SHH's level | lines that do not express EREG (26) vs lines expressing it (24) | 2.14× lower at baseline in the lines without EREG | 0.022 | ⚠ within organs, on part of the lines; also absent: DPP4, IL20RA, HS3ST1; co-absent with the target |

## Where it sits

- **Module**: [[Module 113]] — hypoxia; 43 genes; every member is in the + arm (projection on the module's main direction 0.348). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (27.8, 10.3); signed map (11.5, 29.4). **Vector** length 90.1, 24.2% of its response variance represented; |z| ≥ 3 in 1,009 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.9 | +6.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.1 | +18.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.0 | +13.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.5 | +7.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.4 | +16.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.3 | +1.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.4 | +1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +1.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.8 | +3.0 |
| fall | [[NG25 (drug)]] 5 µM |  | -3.6 | -4.7 |
|  | [[Trametinib (drug)]] 5 µM |  | -3.1 | -5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | +0.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.6 | -3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.6 | -4.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.3 | -3.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.3 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | epiregulin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q13.3 — chr4:74,365,145-74,388,749 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ER |
| Gene groups (HGNC) | EGF ligand family |
| Hallmark sets | ALLOGRAFT_REJECTION, INFLAMMATORY_RESPONSE, APOPTOSIS, KRAS_SIGNALING_UP |
| Reactome | 44 pathways, smallest: Inhibition of Signaling by Overexpressed EGFR; Signaling by Overexpressed Wild-Type EGFR in Cancer; EGFR interacts with phospholipase C-gamma |
| Matched by | ensembl_id |

**Function**, from UniProt [O14944](https://www.uniprot.org/uniprotkb/O14944) (Proepiregulin):

> Ligand of the EGF receptor/EGFR and ERBB4. Stimulates EGFR and ERBB4 tyrosine phosphorylation. Contributes to inflammation, wound healing, tissue repair, and oocyte maturation by regulating angiogenesis and vascular remodeling and by stimulating cell proliferation.

**Summary**, from NCBI Gene [2069](https://www.ncbi.nlm.nih.gov/gene/2069):

> This gene encodes a secreted peptide hormone and member of the epidermal growth factor (EGF) family of proteins. The encoded protein is a ligand of the epidermal growth factor receptor (EGFR) and the structurally related erb-b2 receptor tyrosine kinase 4 (ERBB4). The encoded protein may be involved in a wide range of biological processes including inflammation, wound healing, oocyte maturation, and cell proliferation. Additionally, the encoded protein may promote the progression of cancers of …

**Accessions** — [HGNC:3443](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3443) · Entrez [2069](https://www.ncbi.nlm.nih.gov/gene/2069) · UniProt [O14944](https://www.uniprot.org/uniprotkb/O14944) · Ensembl [ENSG00000124882](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124882)

## Data

Gene col 4580: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4580); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4580, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4580]; `tensor/DDL_lfc|DDL_z.npy` [4580]; `embed/gene_vectors.npy` [4580]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4580 or target_col == 4580). Every well: [[EREG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EREG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
