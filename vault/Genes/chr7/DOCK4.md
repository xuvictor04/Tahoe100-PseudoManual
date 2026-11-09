---
symbol: "DOCK4"
type: "gene"
col: 4886
ensembl_id: "ENSG00000128512"
name: "dedicator of cytokinesis 4"
location: "7q31.1"
module: 193
arm: "+"
pooled_cpm: 220.87
n_lines_expressing: 36
n_dd_up: 21
n_dd_down: 20
n_dd_up_clean: 18
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 6
direction_downstream: 5
tags: ["gene", "module/193"]
generated_by: "tahoemap"
---

# DOCK4

*dedicator of cytokinesis 4* — 7q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.72× (z +28.2, q 0e+00, up in 28 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.767× (z -6.3, q 2e-07, down in 19 of 36 measured lines) ⚠ cell-cycle shift, explains ~17% of this change. The strongest without an alert is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.745× (z -5.9, q 1e-06, down in 14 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SERPIND1]] (+0.71, fdr 7e-06), [[KIFC3]] (+0.67, fdr 7e-06), [[BMP6]] (+0.66, fdr 7e-06); moves opposite to [[MTO1]] (-0.50, fdr 4e-05), [[ZNF675]] (-0.50, fdr 6e-05), [[ALG12]] (-0.50, fdr 4e-05).
> It is in [[Module 193]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[ESM1]] → it (grade B ⚠); 5 go from it, the strongest it → cells under [[Bortezomib (drug)]] 0.05 µM (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4886.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.72×** | +28.2 | 0e+00 | 28/34 (HT-29, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.59×** | +27.5 | 0e+00 | 28/34 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.32×** | +25.7 | 0e+00 | 28/34 (HT-29, LS 180, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.73×** | +21.6 | 0e+00 | 31/34 (LS 180, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.00×** | +21.1 | 0e+00 | 28/34 (LS 180, SW1417, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.96×** | +14.5 | 1e-45 | 24/34 (LS 180, PANC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.50×** | +12.3 | 1e-32 | 17/34 (BT-474, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.76×** | +12.2 | 3e-32 | 27/35 (LS 180, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +11.4 | 3e-28 | 14/35 (LS 180, C-33 A, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.61×** | +10.8 | 2e-25 | 22/35 (Panc 03.27, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.33×** | +5.9 | 1e-07 | 17/34 (BT-474, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.32×** | +5.9 | 2e-07 | 17/34 (BT-474, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.29×** | +5.5 | 1e-06 | 17/34 (BT-474, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.31×** | +5.5 | 1e-06 | 11/36 (LS 180, C-33 A, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.28×** | +5.3 | 4e-06 | 17/34 (BT-474, CFPAC-1, …) | two highest doses |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.57×** | +5.1 | 1e-05 | 22/34 (HEC-1-A, Hs 766T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.23×** | +4.3 | 7e-04 | 12/34 (NCI-H1792, hTERT-HPNE, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4886.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.767×** | -6.3 | 2e-07 | 19/36 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.745×** | -5.9 | 1e-06 | 14/34 (NCI-H460, NCI-H1573, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.740×** | -5.6 | 5e-06 | 22/35 (NCI-H460, NCI-H1573, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.788×** | -5.5 | 6e-06 | 19/35 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.784×** | -5.2 | 2e-05 | 19/34 (NCI-H1573, A549, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.770×** | -5.2 | 2e-05 | 22/33 (SW 900, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **0.825×** | -5.1 | 3e-05 | 18/34 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.791×** | -4.8 | 9e-05 | 18/34 (NCI-H460, NCI-H23, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.830×** | -4.5 | 3e-04 | 13/34 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~8% of this change | **0.810×** | -4.5 | 3e-04 | 23/34 (SW 900, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[NG25 (drug)]] 5 µM |  | **0.668×** | -4.5 | 3e-04 | 18/33 (LOX-IMVI, A498, …) | top dose only | cell-cycle shift (explains ~25% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.804×** | -4.5 | 3e-04 | 21/32 (SW480, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.679×** | -4.3 | 6e-04 | 17/34 (NCI-H460, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.873× | -4.1 | 0.001 | 15/34 (LOX-IMVI, NCI-H23, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.829×** | -4.0 | 0.002 | 19/34 (NCI-H460, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.05 µM |  | **0.829×** | -3.7 | 0.007 | 12/34 (NCI-H460, CHP-212, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.888× | -3.6 | 0.010 | 10/34 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.823×** | -3.6 | 0.010 | 12/34 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.885× | -3.6 | 0.010 | 12/35 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4886. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 996 | 0 | 21 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -19.2) |
| [[BT-474 (line)]] | alt | 56.6 | 13 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.65× (z +21.5) | — |
| [[LS 180 (line)]] | wt | 57.1 | 12 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +14.7) | — |
| [[NCI-H2030 (line)]] | alt | 1,347 | 0 | 10 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.181× (z -23.0) |
| [[HepG2_C3A (line)]] | wt | 838 | 0 | 9 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.204× (z -22.8) |
| [[A498 (line)]] | wt | 148 | 5 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +15.3) | [[Dinaciclib (drug)]] 5 µM 0.398× (z -10.4) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 383 | 6 | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.14× (z +13.1) | [[Dinaciclib (drug)]] 0.5 µM 0.317× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 295 | 4 | 4 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.65× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.235× (z -20.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 97.1 | 6 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.58× (z +14.1) | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.359× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 238 | 2 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.235× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.426× (z -9.8) |
| [[SW48 (line)]] | wt | 59.8 | 7 | 0 | [[Panobinostat (drug)]] 5 µM 7.67× (z +12.9) | — |
| [[CFPAC-1 (line)]] | alt | 144 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.87× (z +10.0) | — |
| [[HT-29 (line)]] | alt | 66.9 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 5.96× (z +15.9) | — |
| [[NCI-H23 (line)]] | alt | 69.1 | 4 | 2 (2 ⚠) | [[Belinostat (drug)]] 5 µM 5.58× (z +12.6) | [[Adagrasib (drug)]] 0.05 µM 0.571× (z -14.5) ⚠ position not correctable |
| [[Panc 03.27 (line)]] | alt | 77.2 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +15.7) | — |
| [[PANC-1 (line)]] | alt | 58.8 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 4.19× (z +15.5) | — |
| [[C-33 A (line)]] | alt | 127 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 3.19× (z +12.0) | — |
| [[HS-578T (line)]] | alt | 57.4 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 4.60× (z +12.9) | — |
| [[SNU-423 (line)]] | alt | 56.4 | 5 | 0 | [[Belinostat (drug)]] 5 µM 3.87× (z +11.4) | — |
| [[NCI-H1573 (line)]] | alt | 174 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -10.0) |
| [[RKO (line)]] | wt | 195 | 4 | 0 | [[Belinostat (drug)]] 5 µM 3.32× (z +10.5) | — |
| [[A549 (line)]] | wt | 323 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -12.7) |
| [[H4 (line)]] | wt | 65.6 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.55× (z +9.5) | — |
| [[RPMI-7951 (line)]] | alt | 77.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.75× (z +10.3) | — |
| [[Hs 766T (line)]] | wt | 369 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.250× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 162 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +13.4) | — |
| [[LOX-IMVI (line)]] | wt | 382 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -13.1) |
| [[SHP-77 (line)]] | alt | 197 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -14.7) |
| [[C32 (line)]] | wt | 390 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.358× (z -8.9) |
| [[CHP-212 (line)]] | wt | 78.6 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0628× (z -13.4) |
| [[NCI-H1792 (line)]] | alt | 369 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.359× (z -10.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 30.3 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 25.6 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 118 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 31.7 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 23.6 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 29.1 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 197 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 50.6 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 28.8 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 21.1 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 43.5 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 17.0 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 367 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 28.7 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 254 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.9 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 24.6 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 54.9 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 289 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4886), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SERPIND1]] | +0.71 | +0.70 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[KIFC3]] | +0.67 | +0.69 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[BMP6]] | +0.66 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[UNC5D]] | +0.65 | +0.59 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[RAB3B]] | +0.65 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[NR2E3]] | +0.64 | +0.59 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[MCTP1]] | +0.63 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[ITGB5]] | +0.62 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[STC1]] | +0.60 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[ESM1]] | +0.60 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[AMOTL1]] | +0.60 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[TFPI2]] | +0.59 | +0.56 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_COMPLEMENT |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTO1]] | -0.50 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[ZNF675]] | -0.50 | -0.42 / -0.38 | both halves | 6e-05 |  |
| [[ALG12]] | -0.50 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[SUPV3L1]] | -0.49 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[MAIP1]] | -0.48 | -0.42 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ESM1]] | B | ESM1 activity raises DOCK4's level | lines that do not express ESM1 (37) vs lines expressing it (13) | 2.28× lower at baseline in the lines without ESM1 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, DIRAS3, ENSG00000224865 |
| [[MAP2K1]] | B | MAP2K1 activity raises DOCK4's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 3.6% of all compounds | 0.009 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SERPINE2]] | B | SERPINE2 activity raises DOCK4's level | lines that do not express SERPINE2 (21) vs lines expressing it (29) | 2.29× lower at baseline in the lines without SERPINE2 | 0.040 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ZNF365, ADAM12 |
| [[BCAR3]] | B | BCAR3 activity raises DOCK4's level | lines that do not express BCAR3 (9) vs lines expressing it (41) | 2.58× lower at baseline in the lines without BCAR3 | 0.059 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, CD59, C11orf91; maybe low, not absent |
| [[DUSP5]] | B | DUSP5 activity raises DOCK4's level | lines that do not express DUSP5 (7) vs lines expressing it (43) | 3.32× lower at baseline in the lines without DUSP5 | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000236213, CA13, SLC2A1; maybe low, not absent |
| [[SERPIND1]] | B | SERPIND1 activity raises DOCK4's level | lines that do not express SERPIND1 (16) vs lines expressing it (34) | 2.31× lower at baseline in the lines without SERPIND1 | 0.084 | ⚠ within organs, on part of the lines; also absent: ENSG00000254303, ENSG00000287390, LANCL3; maybe low, not absent |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Bortezomib (drug)]] 0.05 µM | B | DOCK4 activity lowers the cells' numbers under Bortezomib 0.05 µM (makes them more sensitive) | lines that do not express DOCK4 (14) vs lines expressing it (34) | the lines without DOCK4: 1.33× the cells of the other lines | 0.036 | ⚠ within organs, on part of the lines; also absent: STC2 |
| [[MAML3]] | B | DOCK4 activity raises MAML3's level | lines that do not express DOCK4 (14) vs lines expressing it (36) | 2.36× lower at baseline in the lines without DOCK4 | 0.044 | ⚠ within organs, on part of the lines; also absent: STC2 |
| [[NEDD4L]] | B | DOCK4 activity raises NEDD4L's level | lines that do not express DOCK4 (14) vs lines expressing it (36) | 1.69× lower at baseline in the lines without DOCK4 | 0.063 | ⚠ within organs, on part of the lines; also absent: STC2 |
| [[NRG1]] | B | DOCK4 activity raises NRG1's level | lines that do not express DOCK4 (14) vs lines expressing it (36) | 2.39× lower at baseline in the lines without DOCK4 | 0.088 | ⚠ within organs, on part of the lines; also absent: STC2 |
| [[SMOC1]] | B | DOCK4 activity raises SMOC1's level | lines that do not express DOCK4 (14) vs lines expressing it (36) | 2.31× lower at baseline in the lines without DOCK4 | 0.099 | ⚠ within organs, on part of the lines; also absent: STC2 |

## Where it sits

- **Module**: [[Module 193]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.753). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (41.9, 9.1); signed map (8.9, 44.3). **Vector** length 123, 34.9% of its response variance represented; |z| ≥ 3 in 1,343 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.6 | +21.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.6 | +12.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.7 | +21.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | +3.8 | +3.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +2.9 | -2.3 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +2.4 | +1.7 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +2.1 | +5.1 |
|  | [[4EGI-1 (drug)]] 5 µM |  | +2.0 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +2.5 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -6.3 | -6.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -5.7 | -5.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.8 | -5.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.6 | -5.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.6 | -5.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -4.6 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | dedicator of cytokinesis 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q31.1 — chr7:111,726,110-112,206,407 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ34238, KIAA0716 |
| Gene groups (HGNC) | DOCK family Rho GEFs; SH3 domain containing |
| Hallmark sets | COMPLEMENT, MITOTIC_SPINDLE |
| Reactome | 8 pathways, smallest: RHOG GTPase cycle; RAC2 GTPase cycle; Factors involved in megakaryocyte development and platelet production |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N1I0](https://www.uniprot.org/uniprotkb/Q8N1I0) (Dedicator of cytokinesis protein 4):

> Functions as a guanine nucleotide exchange factor (GEF) that promotes the exchange of GDP to GTP, converting inactive GDP-bound small GTPases into their active GTP-bound form. Involved in regulation of adherens junction between cells. Plays a role in cell migration.; [Isoform 2]: Has a higher guanine nucleotide exchange factor activity compared to other isoforms.

**Summary**, from NCBI Gene [9732](https://www.ncbi.nlm.nih.gov/gene/9732):

> This gene is a member of the dedicator of cytokinesis (DOCK) family and encodes a protein with a DHR-1 (CZH-1) domain, a DHR-2 (CZH-2) domain and an SH3 domain. This membrane-associated, cytoplasmic protein functions as a guanine nucleotide exchange factor and is involved in regulation of adherens junctions between cells. Mutations in this gene have been associated with ovarian, prostate, glioma, and colorectal cancers. Alternatively spliced variants which encode different protein isoforms have …

**Accessions** — [HGNC:19192](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19192) · Entrez [9732](https://www.ncbi.nlm.nih.gov/gene/9732) · UniProt [Q8N1I0](https://www.uniprot.org/uniprotkb/Q8N1I0) · Ensembl [ENSG00000128512](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128512)

## Data

Gene col 4886: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4886); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4886, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4886]; `tensor/DDL_lfc|DDL_z.npy` [4886]; `embed/gene_vectors.npy` [4886]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4886 or target_col == 4886). Every well: [[DOCK4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DOCK4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
