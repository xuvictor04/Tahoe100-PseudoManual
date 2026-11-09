---
symbol: "AREG"
type: "gene"
col: 3043
ensembl_id: "ENSG00000109321"
name: "amphiregulin"
location: "4q13.3"
module: 162
arm: "+"
pooled_cpm: 249.18
n_lines_expressing: 24
n_dd_up: 19
n_dd_down: 16
n_dd_up_clean: 4
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 11
direction_downstream: 35
tags: ["gene", "module/162"]
generated_by: "tahoemap"
---

# AREG

*amphiregulin* — 4q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (15 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 4.45× (z +12.4, q 1e-32, up in 18 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (drug)]] 0.05 µM: 0.582× (z -6.2, q 3e-07, down in 16 of 22 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MIDN]] (+0.63, fdr 1e-05), [[BAIAP2L1]] (+0.62, fdr 1e-05), [[LINC00659]] (+0.60, fdr 1e-05); moves opposite to [[CTPS2]] (-0.57, fdr 3e-05), [[NNT]] (-0.55, fdr 6e-05), [[SUPV3L1]] (-0.54, fdr 2e-05).
> It is in [[Module 162]], a single-armed module (estrogen response late).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 35 go from it, the strongest it → [[RDH13]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 15 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3043.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **4.45×** | +12.4 | 1e-32 | 18/22 (AsPC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.45×** | +10.5 | 1e-23 | 22/22 (SW 900, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **3.46×** | +10.3 | 8e-23 | 16/22 (AsPC-1, A549, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **3.17×** | +9.6 | 1e-19 | 13/23 (A549, NCI-H2347, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **3.09×** | +9.4 | 6e-19 | 19/22 (A549, AsPC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.99×** | +9.1 | 7e-18 | 18/22 (AsPC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.26×** | +6.8 | 9e-10 | 20/23 (SW 900, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **2.25×** | +6.2 | 3e-08 | 7/20 (A549, NCI-H2347, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **2.15×** | +6.1 | 6e-08 | 10/20 (A549, NCI-H2347, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.86×** | +5.2 | 1e-05 | 15/22 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.81×** | +4.9 | 4e-05 | 17/22 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.84×** | +4.9 | 5e-05 | 15/22 (AsPC-1, NCI-H1573, …) | rises with dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.72×** | +4.5 | 3e-04 | 17/22 (SW 900, A549, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.63×** | +4.1 | 0.002 | 15/22 (AsPC-1, A549, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~64% of this change | **1.59×** | +3.7 | 0.007 | 11/22 (AsPC-1, NCI-H1573, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.44×** | +3.0 | 0.073 | 2/22 (HEC-1-A, A549) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 1 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3043.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 0.05 µM |  | **0.582×** | -6.2 | 3e-07 | 16/22 (BT-474, SW480, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **0.453×** | -6.0 | 5e-07 | 18/24 (SW48, BT-474, …) | all doses, flat | cell-cycle shift (explains ~23% here); noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.631×** | -5.4 | 1e-05 | 21/23 (SW48, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.536×** | -4.8 | 3e-04 | 15/22 (BT-474, SW480, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.573×** | -4.6 | 4e-04 | 11/22 (BT-474, SW480, …) | two highest doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.633×** | -4.0 | 0.007 | 15/22 (BT-474, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Folic acid (drug)]] 5 µM |  | **0.728×** | -3.7 | 0.016 | 17/22 (HEC-1-A, LoVo, …) | top dose only | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.643×** | -3.5 | 0.031 | 14/22 (BT-474, SW48, …) | two highest doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.665×** | -3.4 | 0.033 | 13/23 (BT-474, SW 900, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.661×** | -3.4 | 0.033 | 18/22 (BT-474, HT-29, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.662×** | -3.4 | 0.033 | 12/23 (BT-474, SW480, …) | all doses, flat |  |
| [[Radotinib (drug)]] 5 µM |  | **0.755×** | -3.3 | 0.048 | 18/22 (COLO 205, SW 900, …) | top dose only |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.757×** | -3.3 | 0.050 | 12/22 (HT-29, SW480, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.722×** | -3.1 | 0.073 | 13/22 (BT-474, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.454×** | -3.0 | 0.084 | 15/24 (SW48, SW 900, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.455×** | -3.0 | 0.084 | 15/23 (LS 180, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, +0.60 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3043. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 325 | 0 | 23 | — | [[Cobimetinib (drug)]] 5 µM 0.0399× (z -12.1) |
| [[A549 (line)]] | wt | 64.8 | 11 (10 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 12.3× (z +13.9) | — |
| [[AsPC-1 (line)]] | alt | 212 | 10 (9 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.70× (z +17.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 12.7× (z +15.3) | — |
| [[NCI-H1573 (line)]] | alt | 634 | 7 (6 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 7.84× (z +11.6) | [[Selinexor (drug)]] 5 µM 0.341× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 145 | 6 (3 ⚠) | 2 | [[Tucidinostat (drug)]] 5 µM 7.59× (z +15.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.238× (z -10.6) |
| [[MIA PaCa-2 (line)]] | alt | 246 | 4 (3 ⚠) | 2 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 5.96× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 5.54× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.109× (z -19.1) |
| [[SW48 (line)]] | wt | 1,274 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0945× (z -19.8) |
| [[SW480 (line)]] | alt | 84.1 | 4 (2 ⚠) | 2 | [[Tucidinostat (drug)]] 5 µM 4.72× (z +10.9) | [[Trametinib (drug)]] 0.05 µM 0.262× (z -9.3) |
| [[NCI-H2030 (line)]] | alt | 202 | 4 (2 ⚠) | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 4.94× (z +10.7) | [[Adagrasib (drug)]] 0.05 µM 0.542× (z -9.6) ⚠ position not correctable |
| [[HT-29 (line)]] | alt | 533 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.168× (z -18.5) |
| [[LoVo (line)]] | wt | 481 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.203× (z -16.7) |
| [[KATO III (line)]] | alt | 578 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.271× (z -13.3) |
| [[LS 180 (line)]] | wt | 716 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.196× (z -16.3) |
| [[NCI-H2347 (line)]] | alt | 605 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.89× (z +9.5) | — |
| [[Panc 03.27 (line)]] | alt | 467 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.161× (z -16.8) |
| [[SW1417 (line)]] | alt | 187 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +8.5) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -11.8) |
| [[A-427 (line)]] | wt | 3,085 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.319× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 357 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -9.5) |
| [[COLO 205 (line)]] | alt | 499 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.171× (z -11.5) |
| [[SW 1271 (line)]] | alt | 96.5 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0498× (z -9.0) |
| [[A-172 (line)]] | wt | 19.3 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 23.1 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 38.3 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 22.9 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 19.0 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 35.2 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 25.5 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 81.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 74.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 49.6 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 45.7 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 31.6 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 19.1 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 53.4 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 17.8 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 24.7 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 40.1 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 37.2 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 40.0 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 207 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.3 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 17.7 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 20.3 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 26.0 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 16.5 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.4 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 21.3 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 26.0 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 35.8 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3043), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIDN]] | +0.63 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[BAIAP2L1]] | +0.62 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[LINC00659]] | +0.60 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[DUSP6]] | +0.60 | +0.57 / +0.52 | both halves | 1e-05 | pathway: MAPK family signaling cascades |
| [[SH2D3A]] | +0.59 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[R3HDM4]] | +0.57 | +0.52 / +0.43 | both halves | 3e-05 |  |
| [[SYP]] | +0.57 | +0.43 / +0.42 | both halves | 4e-05 |  |
| [[DUSP2]] | +0.57 | +0.49 / +0.47 | both halves | 2e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE |
| [[TIAM1]] | +0.56 | +0.50 / +0.45 | both halves | 3e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[TRIM15]] | +0.55 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[S100A11]] | +0.55 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[ARC]] | +0.55 | +0.47 / +0.58 | both halves | 2e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTPS2]] | -0.57 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[NNT]] | -0.55 | -0.39 / -0.47 | both halves | 6e-05 |  |
| [[SUPV3L1]] | -0.54 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[ZNF362]] | -0.54 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[TMEM94]] | -0.54 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[MED24]] | -0.52 | -0.39 / -0.42 | both halves | 6e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[PSMC2]] | -0.52 | -0.43 / -0.35 | both halves | 1e-04 | pathway: Cellular response to chemical stress |
| [[C5orf15]] | -0.51 | -0.37 / -0.36 | both halves | 1e-04 |  |
| [[LAMTOR5-AS1]] | -0.50 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[NADK2]] | -0.50 | -0.41 / -0.37 | both halves | 9e-05 |  |
| [[NAXD]] | -0.50 | -0.38 / -0.36 | both halves | 9e-05 |  |
| [[RBBP4]] | -0.50 | -0.30 / -0.54 | both halves | 2e-04 | pathway: Intracellular signaling by second messengers |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 1, C 10.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises AREG's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[CBLC]] | C | CBLC activity raises AREG's level | lines that do not express CBLC (31) vs lines expressing it (19) | 7.38× lower at baseline in the lines without CBLC | 0.001 | ⚠ within organs, on part of the lines; also absent: KDF1, CLDN7, PRSS8; co-absent with the target |
| [[S100A14]] | C | S100A14 activity raises AREG's level | lines that do not express S100A14 (33) vs lines expressing it (17) | 6.54× lower at baseline in the lines without S100A14 | 0.003 | ⚠ within organs, on part of the lines; also absent: PRSS8, RAB25, TMPRSS4; co-absent with the target |
| [[SH2D3A]] | C | SH2D3A activity raises AREG's level | lines that do not express SH2D3A (24) vs lines expressing it (26) | 6.13× lower at baseline in the lines without SH2D3A | 0.004 | ⚠ within organs, on part of the lines; also absent: GRB7, MYO5B, CRB3; co-absent with the target |
| [[C19orf33]] | C | C19orf33 activity raises AREG's level | lines that do not express C19orf33 (19) vs lines expressing it (31) | 5.91× lower at baseline in the lines without C19orf33 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: KRT80, MISP, AREG; co-absent with the target |
| [[KLF5]] | C | KLF5 activity raises AREG's level | lines that do not express KLF5 (18) vs lines expressing it (32) | 4.65× lower at baseline in the lines without KLF5 | 0.009 | ⚠ within organs, on part of the lines; also absent: LAMA3, IFNLR1, NCMAP; maybe low, not absent; co-absent with the target |
| [[TRIM15]] | C | TRIM15 activity raises AREG's level | lines that do not express TRIM15 (34) vs lines expressing it (16) | 6.10× lower at baseline in the lines without TRIM15 | 0.016 | ⚠ within organs, on part of the lines; also absent: TMEM45B, EPS8L3, ENSG00000225680; co-absent with the target |
| [[GOLT1A]] | C | GOLT1A activity raises AREG's level | lines that do not express GOLT1A (24) vs lines expressing it (26) | 4.93× lower at baseline in the lines without GOLT1A | 0.018 | ⚠ within organs, on part of the lines; also absent: GRB7, RHOV, ELF3; maybe low, not absent; co-absent with the target |
| [[SULT2B1]] | C | SULT2B1 activity raises AREG's level | lines that do not express SULT2B1 (28) vs lines expressing it (22) | 5.91× lower at baseline in the lines without SULT2B1 | 0.028 | ⚠ within organs, on part of the lines; also absent: ATP2C2, ST14, SGPP2; maybe low, not absent; co-absent with the target |
| [[LINC00659]] | C | LINC00659 activity raises AREG's level | lines that do not express LINC00659 (26) vs lines expressing it (24) | 4.30× lower at baseline in the lines without LINC00659 | 0.029 | ⚠ within organs, on part of the lines; also absent: KLK6, TRIM15, ENSG00000225680; co-absent with the target |
| [[KRT18]] | C | KRT18 activity raises AREG's level | lines that do not express KRT18 (19) vs lines expressing it (31) | 4.65× lower at baseline in the lines without KRT18 | 0.065 | ⚠ within organs, on part of the lines; also absent: MISP, SFN, GRB7; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*35 arrows, 35 of them with an alert ⚠; grade A 0, B 21, C 14. Shown: the 12 strongest; 23 more arrows (23 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RDH13]] | B | AREG activity raises RDH13's level | lines that do not express AREG (26) vs lines expressing it (24) | 2.27× lower at baseline in the lines without AREG | 0.007 | ⚠ within organs, on part of the lines; also absent: TC2N, ESRP1, CRB3 |
| [[KRT15]] | B | AREG activity raises KRT15's level | lines that do not express AREG (26) vs lines expressing it (24) | 2.75× lower at baseline in the lines without AREG | 0.008 | ⚠ within organs, on part of the lines; also absent: TC2N, ESRP1, CRB3 |
| [[BAIAP2L1]] | B | AREG activity raises BAIAP2L1's level | lines that do not express AREG (26) vs lines expressing it (24) | 2.87× lower at baseline in the lines without AREG | 0.011 | ⚠ within organs, on part of the lines; also absent: TC2N, ESRP1, CRB3 |
| [[SDC4]] | B | AREG activity raises SDC4's level | lines that do not express AREG (26) vs lines expressing it (24) | 1.94× lower at baseline in the lines without AREG | 0.014 | ⚠ within organs, on part of the lines; also absent: TC2N, ESRP1, CRB3 |
| [[ABCC3]] | B | AREG activity raises ABCC3's level | lines that do not express AREG (26) vs lines expressing it (24) | 3.82× lower at baseline in the lines without AREG | 0.020 | ⚠ within organs, on part of the lines; also absent: TC2N, ESRP1, CRB3 |
| [[SAT1]] | B | AREG activity raises SAT1's level | lines that do not express AREG (26) vs lines expressing it (24) | 2.01× lower at baseline in the lines without AREG | 0.024 | ⚠ within organs, on part of the lines; also absent: TC2N, ESRP1, CRB3 |
| [[EPHA2]] | B | AREG activity raises EPHA2's level | lines that do not express AREG (26) vs lines expressing it (24) | 3.11× lower at baseline in the lines without AREG | 0.025 | ⚠ within organs, on part of the lines; also absent: TC2N, ESRP1, CRB3 |
| [[CYSTM1]] | B | AREG activity raises CYSTM1's level | lines that do not express AREG (26) vs lines expressing it (24) | 2.07× lower at baseline in the lines without AREG | 0.026 | ⚠ within organs, on part of the lines; also absent: TC2N, ESRP1, CRB3 |
| [[GALE]] | B | AREG activity raises GALE's level | lines that do not express AREG (26) vs lines expressing it (24) | 1.56× lower at baseline in the lines without AREG | 0.027 | ⚠ within organs, on part of the lines; also absent: TC2N, ESRP1, CRB3 |
| cells under [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM | B | AREG activity raises the cells' numbers under 18β-Glycyrrhetinic acid 0.5 µM (protects the cells) | lines that do not express AREG (26) vs lines expressing it (22) | the lines without AREG: 0.84× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: TC2N, ESRP1, CRB3 |
| [[STON2]] | B | AREG activity raises STON2's level | lines that do not express AREG (26) vs lines expressing it (24) | 2.40× lower at baseline in the lines without AREG | 0.057 | ⚠ within organs, on part of the lines; also absent: TC2N, ESRP1, CRB3 |
| [[ANGEL2]] | B | AREG activity lowers ANGEL2's level | lines that do not express AREG (26) vs lines expressing it (24) | 1.20× higher at baseline in the lines without AREG | 0.066 | ⚠ within organs, on part of the lines; also absent: TC2N, ESRP1, CRB3 |

## Where it sits

- **Module**: [[Module 162]] — estrogen response late; 26 genes; every member is in the + arm (projection on the module's main direction 0.642). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.1, 48.4); signed map (-0.1, 36.9). **Vector** length 106, 36.7% of its response variance represented; |z| ≥ 3 in 802 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.8 | +10.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.3 | +6.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | +5.7 | +9.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | +5.2 | +4.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.2 | +12.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +2.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.9 | +1.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.8 | +1.3 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.8 | +2.1 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.8 | -4.8 |
|  | [[Trametinib (drug)]] 5 µM |  | -4.0 | -6.0 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -3.5 | -6.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -1.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.9 | -3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.9 | -3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.8 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | amphiregulin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q13.3 — chr4:74,445,136-74,455,005 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AR, CRDGF; previously SDGF, AREGB |
| Gene groups (HGNC) | EGF ligand family |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, EPITHELIAL_MESENCHYMAL_TRANSITION, ESTROGEN_RESPONSE_EARLY, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 44 pathways, smallest: Developmental Cell Lineages of the Integumentary System; Developmental Lineage of Mammary Gland Luminal Epithelial Cells; Developmental Lineage of Mammary Gland Myoepithelial Cells |
| Matched by | ensembl_id |

**Function**, from UniProt [P15514](https://www.uniprot.org/uniprotkb/P15514) (Amphiregulin):

> Ligand of the EGF receptor/EGFR. Autocrine growth factor as well as a mitogen for a broad range of target cells including astrocytes, Schwann cells and fibroblasts.

**Summary**, from NCBI Gene [374](https://www.ncbi.nlm.nih.gov/gene/374):

> The protein encoded by this gene is a member of the epidermal growth factor family. It is an autocrine growth factor as well as a mitogen for astrocytes, Schwann cells and fibroblasts. It is related to epidermal growth factor (EGF) and transforming growth factor alpha (TGF-alpha). The protein interacts with the EGF/TGF-alpha receptor to promote the growth of normal epithelial cells, and it inhibits the growth of certain aggressive carcinoma cell lines. It also functions in mammary gland, oocyte …

**Accessions** — [HGNC:651](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:651) · Entrez [374](https://www.ncbi.nlm.nih.gov/gene/374) · UniProt [P15514](https://www.uniprot.org/uniprotkb/P15514) · Ensembl [ENSG00000109321](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109321)

## Data

Gene col 3043: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3043); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3043, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3043]; `tensor/DDL_lfc|DDL_z.npy` [3043]; `embed/gene_vectors.npy` [3043]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3043 or target_col == 3043). Every well: [[AREG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AREG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
