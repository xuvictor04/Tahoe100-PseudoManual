---
symbol: "NCBP3"
type: "gene"
col: 1077
ensembl_id: "ENSG00000074356"
name: "nuclear cap binding subunit 3"
location: "17p13.2"
module: 172
arm: "+"
pooled_cpm: 66.55
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 3
n_dd_up_clean: 8
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/172"]
generated_by: "tahoemap"
---

# NCBP3

*nuclear cap binding subunit 3* — 17p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.77× (z +20.5, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.774× (z -13.0, q 4e-36, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NCOA6]] (+0.60, fdr 2e-05), [[ZNF346]] (+0.59, fdr 1e-05), [[GUSBP11]] (+0.58, fdr 2e-05); moves opposite to [[RARA]] (-0.54, fdr 1e-05), [[CXCR4]] (-0.51, fdr 3e-05), [[SEC24A]] (-0.48, fdr 4e-05).
> It is in [[Module 172]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1077.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.77×** | +20.5 | 0e+00 | 44/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.55×** | +15.7 | 0e+00 | 41/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.49×** | +14.3 | 4e-44 | 41/48 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.48×** | +14.1 | 4e-43 | 41/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.47×** | +13.9 | 1e-41 | 40/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.40×** | +12.0 | 2e-31 | 37/48 (SW480, C32, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.34×** | +10.0 | 9e-22 | 32/48 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.21×** | +9.6 | 9e-20 | 21/48 (PANC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.29×** | +8.3 | 9e-15 | 30/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.22×** | +6.8 | 6e-10 | 22/47 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~8% of this change | **1.21×** | +6.7 | 1e-09 | 23/47 (LoVo, NCI-H23, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.36×** | +5.8 | 3e-07 | 18/44 (MIA PaCa-2, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.17× | +5.7 | 4e-07 | 18/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 1.18× | +5.7 | 6e-07 | 21/48 (SW480, A498, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~11% of this change | 1.17× | +5.5 | 1e-06 | 19/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.20×** | +4.7 | 8e-05 | 17/49 (SW480, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.14× | +4.2 | 6e-04 | 16/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.12× | +4.0 | 0.002 | 7/48 (A498, LS 180, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.08× | +3.9 | 0.003 | 3/49 (AsPC-1, H4, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | 1.20× | +3.4 | 0.015 | 14/48 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.09× | +3.0 | 0.066 | 8/47 (HEC-1-A, LOX-IMVI, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1077.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.774×** | -13.0 | 4e-36 | 34/48 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.753×** | -9.3 | 6e-18 | 32/49 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | 0.860× | -7.7 | 3e-12 | 23/49 (A-172, A-427, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.830×** | -6.7 | 3e-09 | 23/48 (J82, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.850× | -5.8 | 6e-07 | 19/49 (SNU-1, SW480, …) | all doses, flat | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.955× | -5.5 | 3e-06 | 0/50 | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | 0.882× | -4.5 | 6e-04 | 9/49 (HEC-1-A, KATO III, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.897× | -3.9 | 0.007 | 13/48 (HepG2/C3A, J82, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.897× | -3.8 | 0.011 | 15/43 (NCI-H1573, C-33 A, …) | all doses, flat | composition shift |
| [[Entrectinib (drug)]] 5 µM |  | 0.910× | -3.4 | 0.040 | 9/48 (SNU-423, SW 1088, …) | top dose only |  |
| [[Terfenadine (drug)]] 0.5 µM |  | 0.906× | -3.2 | 0.062 | 6/48 (A498, LOX-IMVI, …) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.916× | -3.1 | 0.077 | 3/48 (COLO 205, HS-578T, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.913× | -3.0 | 0.11 | 17/45 (NCI-H1792, SHP-77, …) | all doses, flat | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1077. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 116 | 7 (2 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.23× (z +18.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.16× (z +17.4) | [[Dinaciclib (drug)]] 0.5 µM 0.654× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 80.9 | 6 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.24× (z +14.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.10× (z +13.4) | — |
| [[AsPC-1 (line)]] | alt | 54.9 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.72× (z +13.5) | — |
| [[PANC-1 (line)]] | alt | 48.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +12.4) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.15× (z +11.8) | — |
| [[SHP-77 (line)]] | alt | 96.5 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +9.6) ⚠ cell-cycle shift, explains ~22% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.619× (z -8.7) ⚠ cell-cycle shift, explains ~3% of this change |
| [[A-172 (line)]] | wt | 70.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.582× (z -10.7) ⚠ cell-cycle shift, explains ~3% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.644× (z -8.7) |
| [[KATO III (line)]] | alt | 74.2 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.73× (z +14.1) | — |
| [[LoVo (line)]] | wt | 65.1 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.34× (z +12.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.28× (z +12.0) | — |
| [[LS 180 (line)]] | wt | 67.5 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.12× (z +10.5) | — |
| [[NCI-H1792 (line)]] | alt | 64.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.09× (z +8.8) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 0.05 µM 0.449× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 105 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.00× (z +10.1) | — |
| [[A-427 (line)]] | wt | 61.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.460× (z -9.1) ⚠ cell-cycle shift, explains ~3% of this change |
| [[A498 (line)]] | wt | 80.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +11.7) ⚠ cell-cycle shift, explains ~22% of this change | — |
| [[HOP62 (line)]] | alt | 53.3 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.01× (z +9.0) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 69.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.623× (z -9.6) ⚠ cell-cycle shift, explains ~22% of this change |
| [[LOX-IMVI (line)]] | wt | 66.6 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.99× (z +9.0) | — |
| [[NCI-H1573 (line)]] | alt | 45.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.177× (z -19.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H596 (line)]] | alt | 68.5 | 0 | 1 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.05 µM 0.203× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 28.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +8.9) ⚠ cell-cycle shift, explains ~22% of this change | — |
| [[SNU-1 (line)]] | wt | 81.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.322× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 1271 (line)]] | alt | 89.8 | 0 | 1 | — | [[Decitabine (drug)]] 0.05 µM 0.0699× (z -10.8) |
| [[SW 900 (line)]] | alt | 51.7 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.40× (z +8.8) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 82.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 100 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 90.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 58.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 67.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 84.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 94.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 40.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 57.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 81.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 88.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 72.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 85.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 83.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 63.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 86.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1077), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCOA6]] | +0.60 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[ZNF346]] | +0.59 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[GUSBP11]] | +0.58 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[TRAF3IP1]] | +0.56 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[PPP6R2]] | +0.56 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[SPOUT1]] | +0.56 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[MAU2]] | +0.55 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[YLPM1]] | +0.55 | +0.52 / +0.54 | both halves | 1e-05 | STRING 429 |
| [[TRAPPC8]] | +0.55 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[QRSL1]] | +0.55 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[GPATCH3]] | +0.55 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[ELMOD3]] | +0.54 | +0.57 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RARA]] | -0.54 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[CXCR4]] | -0.51 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[SEC24A]] | -0.48 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[RYBP]] | -0.48 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[RGS16]] | -0.48 | -0.33 / -0.54 | both halves | 1e-04 |  |
| [[LINC02036]] | -0.47 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[RAB11A]] | -0.47 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[ARL5B]] | -0.47 | -0.51 / -0.39 | both halves | 6e-05 |  |
| [[SERTAD2]] | -0.47 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[ICAM1]] | -0.47 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[PKM]] | -0.47 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[BZW2]] | -0.46 | -0.32 / -0.48 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises NCBP3's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[CPLANE1]] | B | CPLANE1 activity raises NCBP3's level | lines that do not express CPLANE1 (5) vs lines expressing it (45) | 1.26× lower at baseline in the lines without CPLANE1 | 0.089 | ⚠ within organs, on part of the lines; also absent: NKAIN1, SIX4, TPST1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 172]]; 24 genes; every member is in the + arm (projection on the module's main direction 0.630). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-47.2, 12.6); signed map (-2.4, -11.3). **Vector** length 76.6, 14.9% of its response variance represented; |z| ≥ 3 in 1,097 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +4.9 | +14.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.4 | +6.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.9 | +12.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.8 | +10.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.5 | +3.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.9 | +4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +5.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.7 | -0.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +1.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.8 | -13.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.8 | -9.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | -4.1 | +4.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.1 | -6.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | -3.1 | -7.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.7 | +3.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.9 | -2.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.5 | -1.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.3 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | nuclear cap binding subunit 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.2 — chr17:3,802,158-3,846,246 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HSA277841, ELG; previously C17orf85 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q53F19](https://www.uniprot.org/uniprotkb/Q53F19) (Nuclear cap-binding protein subunit 3):

> Associates with NCBP1/CBP80 to form an alternative cap-binding complex (CBC) which plays a key role in mRNA export. NCBP3 serves as adapter protein linking the capped RNAs (m7GpppG-capped RNA) to NCBP1/CBP80. Unlike the conventional CBC with NCBP2 which binds both small nuclear RNA (snRNA) and messenger (mRNA) and is involved in their export from the nucleus, the alternative CBC with NCBP3 does not bind snRNA and associates only with mRNA thereby playing a role in only mRNA export. The …

**Summary**, from NCBI Gene [55421](https://www.ncbi.nlm.nih.gov/gene/55421):

> Enables RNA 7-methylguanosine cap binding activity and mRNA binding activity. Involved in defense response to virus; mRNA export from nucleus; and snRNA export from nucleus. Located in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24612](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24612) · Entrez [55421](https://www.ncbi.nlm.nih.gov/gene/55421) · UniProt [Q53F19](https://www.uniprot.org/uniprotkb/Q53F19) · Ensembl [ENSG00000074356](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000074356)

## Data

Gene col 1077: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1077); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1077, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1077]; `tensor/DDL_lfc|DDL_z.npy` [1077]; `embed/gene_vectors.npy` [1077]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1077 or target_col == 1077). Every well: [[NCBP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NCBP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
