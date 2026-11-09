---
symbol: "ENC1"
type: "gene"
col: 10141
ensembl_id: "ENSG00000171617"
name: "ectodermal-neural cortex 1"
location: "5q13.3"
module: 120
arm: "+"
pooled_cpm: 37.41
n_lines_expressing: 45
n_dd_up: 18
n_dd_down: 23
n_dd_up_clean: 16
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/120"]
generated_by: "tahoemap"
---

# ENC1

*ectodermal-neural cortex 1* — 5q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 2.57× (z +9.2, q 2e-17, up in 27 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.387× (z -9.3, q 8e-18, down in 36 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDK6]] (+0.71, fdr 7e-06), [[DDAH1]] (+0.66, fdr 7e-06), [[AMIGO2]] (+0.65, fdr 7e-06); moves opposite to [[RAB6A]] (-0.67, fdr 7e-06), [[KCTD7]] (-0.64, fdr 7e-06), [[MAX]] (-0.60, fdr 1e-05).
> It is in [[Module 120]], a single-armed module (RHOA GTPase cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SOX9]] → it (grade B ⚠); 2 go from it, the strongest it → [[SRP54-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10141.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.57×** | +9.2 | 2e-17 | 27/41 (NCI-H23, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.60×** | +9.0 | 9e-17 | 31/42 (HS-578T, BT-474, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.31×** | +8.2 | 6e-14 | 32/43 (HS-578T, A498, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.86×** | +6.1 | 2e-07 | 26/43 (MIA PaCa-2, HOP62, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.52×** | +5.8 | 9e-07 | 24/42 (BT-474, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **1.69×** | +5.1 | 3e-05 | 30/43 (NCI-H2347, CFPAC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.51×** | +4.0 | 0.004 | 19/43 (SW48, A498, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +3.9 | 0.007 | 4/43 (KATO III, HT-29, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **1.47×** | +3.8 | 0.010 | 25/43 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.31×** | +3.7 | 0.012 | 18/43 (A498, PANC-1, …) | rises with dose |  |
| [[Omeprazole (drug)]] 5 µM |  | **1.45×** | +3.6 | 0.017 | 16/43 (HT-29, PANC-1, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | **1.43×** | +3.5 | 0.023 | 13/43 (PANC-1, A-172, …) | inconsistent across doses | position effect removed |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +3.5 | 0.023 | 16/43 (HT-29, A-172, …) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.96×** | +3.4 | 0.023 | 17/44 (MIA PaCa-2, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.055 | 19/43 (PANC-1, A498, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Busulfan (drug)]] 0.05 µM |  | **1.38×** | +3.1 | 0.068 | 14/43 (NCI-H2347, Panc 03.27, …) | inconsistent across doses | position effect removed |
| [[Tirabrutinib (drug)]] 0.5 µM |  | **1.37×** | +3.1 | 0.070 | 16/43 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10141.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.387×** | -9.3 | 8e-18 | 36/43 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.519×** | -9.1 | 3e-17 | 31/42 (AsPC-1, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.400×** | -9.0 | 6e-17 | 40/43 (COLO 205, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.451×** | -7.8 | 9e-13 | 32/43 (KATO III, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.486×** | -7.1 | 2e-10 | 25/43 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.552×** | -5.8 | 6e-07 | 30/43 (COLO 205, KATO III, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.561×** | -5.3 | 8e-06 | 24/43 (COLO 205, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~21% here); position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **0.637×** | -5.3 | 8e-06 | 25/43 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.583×** | -5.3 | 8e-06 | 27/43 (SK-MEL-2, SW 900, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.647×** | -4.8 | 9e-05 | 22/43 (LOX-IMVI, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.611×** | -4.6 | 2e-04 | 25/42 (SK-MEL-2, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.621×** | -4.5 | 3e-04 | 24/43 (RKO, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.669×** | -3.9 | 0.004 | 18/43 (A498, NCI-H1573, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 5 µM | ⚠ toxic | **0.490×** | -3.7 | 0.010 | 18/39 (NCI-H460, NCI-H1573, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Triamcinolone (drug)]] 5 µM |  | **0.771×** | -3.6 | 0.011 | 22/43 (SW 1088, Panc 03.27, …) | all doses, flat |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **0.692×** | -3.6 | 0.011 | 18/43 (COLO 205, KATO III, …) | two highest doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10141. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 105 | 0 | 12 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0524× (z -17.4) |
| [[KATO III (line)]] | alt | 106 | 0 | 10 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0694× (z -16.2) |
| [[NCI-H460 (line)]] | wt | 98.2 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -18.8) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0762× (z -17.4) |
| [[HT-29 (line)]] | alt | 110 | 0 | 7 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -12.3) |
| [[AsPC-1 (line)]] | alt | 73.1 | 2 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 0.5 µM 5.00× (z +10.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.180× (z -16.1) |
| [[Panc 03.27 (line)]] | alt | 92.8 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.0980× (z -12.6) |
| [[HS-578T (line)]] | alt | 16.5 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +16.5) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 17.7× (z +14.0) | — |
| [[LoVo (line)]] | wt | 52.0 | 0 | 4 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.165× (z -12.2) |
| [[SW1417 (line)]] | alt | 79.9 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.306× (z -12.7) |
| [[A-172 (line)]] | wt | 62.5 | 1 | 2 | [[Harringtonine (drug)]] 0.5 µM 5.14× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.154× (z -9.7) |
| [[A498 (line)]] | wt | 9.92 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.89× (z +12.5) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.14× (z +10.1) | — |
| [[BT-474 (line)]] | alt | 10.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 22.3× (z +16.8) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 20.7× (z +11.1) | — |
| [[HOP62 (line)]] | alt | 21.6 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.95× (z +13.5) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.74× (z +10.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 55.7 | 2 | 1 | [[Auranofin (drug)]] 5 µM 8.88× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.233× (z -10.3) |
| [[NCI-H23 (line)]] | alt | 24.9 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.5 µM 11.0× (z +13.3) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.105× (z -12.1) |
| [[CFPAC-1 (line)]] | alt | 45.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +11.2) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.71× (z +8.5) | — |
| [[HepG2_C3A (line)]] | wt | 67.0 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0321× (z -17.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.124× (z -11.0) |
| [[Hs 766T (line)]] | wt | 23.8 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.162× (z -9.3) |
| [[LOX-IMVI (line)]] | wt | 39.6 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.250× (z -8.8) |
| [[LS 180 (line)]] | wt | 51.4 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.139× (z -12.9) |
| [[NCI-H2030 (line)]] | alt | 31.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0820× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -10.9) |
| [[RKO (line)]] | wt | 19.3 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.123× (z -10.1) |
| [[SW48 (line)]] | wt | 29.5 | 1 | 1 | [[Homoharringtonine (drug)]] 0.05 µM 8.22× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.0628× (z -11.6) |
| [[C-33 A (line)]] | alt | 30.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0894× (z -9.1) |
| [[H4 (line)]] | wt | 13.7 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0429× (z -10.6) |
| [[J82 (line)]] | alt | 26.2 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 6.02× (z +8.9) | — |
| [[NCI-H1792 (line)]] | alt | 16.6 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.109× (z -8.7) |
| [[PANC-1 (line)]] | alt | 13.6 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.08× (z +8.6) | — |
| [[SNU-423 (line)]] | alt | 20.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +9.1) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[SW 900 (line)]] | alt | 20.8 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.44× (z +8.6) | — |
| [[A-427 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.65 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.14 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.19 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 8.70 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.55 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 24.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10141), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDK6]] | +0.71 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[DDAH1]] | +0.66 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[AMIGO2]] | +0.65 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[CCN2]] | +0.65 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[FJX1]] | +0.65 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[FAT1]] | +0.65 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[CCND1]] | +0.63 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[NCEH1]] | +0.62 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[ZNF462]] | +0.61 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[LTBP2]] | +0.59 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[PHLDA1]] | +0.59 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[SERTAD4]] | +0.59 | +0.58 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB6A]] | -0.67 | -0.63 / -0.62 | both halves | 7e-06 |  |
| [[KCTD7]] | -0.64 | -0.63 / -0.58 | both halves | 7e-06 | same gene group |
| [[MAX]] | -0.60 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[PLD3]] | -0.59 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[TULP3]] | -0.58 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[PIK3C2A]] | -0.58 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[NDUFAF7]] | -0.58 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[CAMLG]] | -0.57 | -0.64 / -0.46 | both halves | 3e-05 |  |
| [[ALKBH7]] | -0.57 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[RAB40C]] | -0.56 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[CBLB]] | -0.56 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[KDELR1]] | -0.56 | -0.49 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SOX9]] | B | SOX9 activity raises ENC1's level | lines that do not express SOX9 (8) vs lines expressing it (42) | 1.90× lower at baseline in the lines without SOX9 | 0.084 | ⚠ within organs, on part of the lines; also absent: CXCL3, SMOX, TRIM38 |
| [[MAP2K1]] | B | MAP2K1 activity raises ENC1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SRP54-AS1]] | B | ENC1 activity lowers SRP54-AS1's level | lines that do not express ENC1 (5) vs lines expressing it (45) | 1.59× higher at baseline in the lines without ENC1 | 0.074 | ⚠ within organs, on part of the lines; also absent: ENSG00000285868, NMI, NABP1 |
| [[PHLDA1]] | B | ENC1 activity raises PHLDA1's level | lines that do not express ENC1 (5) vs lines expressing it (45) | 2.14× lower at baseline in the lines without ENC1 | 0.080 | ⚠ within organs, on part of the lines; also absent: ENSG00000285868, NMI, NABP1 |

## Where it sits

- **Module**: [[Module 120]] — RHOA GTPase cycle; 41 genes; every member is in the + arm (projection on the module's main direction 0.723). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (40.2, 13.4); signed map (15.3, 41.3). **Vector** length 137, 41.7% of its response variance represented; |z| ≥ 3 in 1,325 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.1 | +9.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.1 | +9.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +7.5 | +5.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.4 | +8.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.0 | +3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.8 | +6.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.2 | +4.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +5.1 | +5.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +0.5 |
| fall | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -5.3 | -4.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.0 | -5.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.8 | -7.1 |
|  | [[Trametinib (drug)]] 5 µM |  | -4.8 | -4.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.4 | -5.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.0 | -5.3 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.8 | -3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.5 | -2.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.5 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | ectodermal-neural cortex 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q13.3 — chr5:74,627,406-74,641,424 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PIG10, ENC-1, TP53I10, KLHL37; previously NRPB |
| Gene groups (HGNC) | Kelch like; BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O14682](https://www.uniprot.org/uniprotkb/O14682) (Ectoderm-neural cortex protein 1):

> Actin-binding protein involved in the regulation of neuronal process formation and in differentiation of neural crest cells. Down-regulates transcription factor NF2L2/NRF2 by decreasing the rate of protein synthesis and not via a ubiquitin-mediated proteasomal degradation mechanism.

**Summary**, from NCBI Gene [8507](https://www.ncbi.nlm.nih.gov/gene/8507):

> This gene encodes a member of the kelch-related family of actin-binding proteins. The encoded protein plays a role in the oxidative stress response as a regulator of the transcription factor Nrf2, and expression of this gene may play a role in malignant transformation. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Feb 2012]

**Accessions** — [HGNC:3345](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3345) · Entrez [8507](https://www.ncbi.nlm.nih.gov/gene/8507) · UniProt [O14682](https://www.uniprot.org/uniprotkb/O14682) · Ensembl [ENSG00000171617](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171617)

## Data

Gene col 10141: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10141); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10141, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10141]; `tensor/DDL_lfc|DDL_z.npy` [10141]; `embed/gene_vectors.npy` [10141]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10141 or target_col == 10141). Every well: [[ENC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ENC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
