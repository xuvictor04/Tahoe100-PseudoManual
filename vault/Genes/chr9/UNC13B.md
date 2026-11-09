---
symbol: "UNC13B"
type: "gene"
col: 12654
ensembl_id: "ENSG00000198722"
name: "unc-13 homolog B"
location: "9p13.3"
module: 159
arm: "+"
pooled_cpm: 57.37
n_lines_expressing: 49
n_dd_up: 13
n_dd_down: 13
n_dd_up_clean: 11
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/159"]
generated_by: "tahoemap"
---

# UNC13B

*unc-13 homolog B* — 9p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.77× (z +21.4, q 0e+00, up in 47 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.571× (z -16.7, q 0e+00, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INPP4A]] (+0.73, fdr 7e-06), [[MAPK8]] (+0.66, fdr 1e-05), [[EPS15]] (+0.61, fdr 3e-05); moves opposite to [[PRR3]] (-0.63, fdr 6e-05), [[PNISR-AS1]] (-0.61, fdr 4e-05), [[METTL6]] (-0.59, fdr 4e-05).
> It is in [[Module 159]], a single-armed module (High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PLS3-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠; shown: the 15 strongest. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12654.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.77×** | +21.4 | 0e+00 | 47/47 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.52×** | +19.4 | 0e+00 | 45/47 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.44×** | +18.8 | 0e+00 | 46/47 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.75×** | +11.7 | 1e-29 | 40/47 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.65×** | +10.5 | 1e-23 | 35/47 (BT-474, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.45×** | +7.8 | 8e-13 | 28/46 (BT-474, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.39×** | +6.9 | 6e-10 | 26/47 (LoVo, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +6.8 | 8e-10 | 24/47 (HOP62, C32, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.84×** | +6.7 | 1e-09 | 28/48 (NCI-H23, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +6.7 | 2e-09 | 23/46 (KATO III, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.33×** | +6.0 | 1e-07 | 30/46 (SNU-423, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.31×** | +5.6 | 9e-07 | 22/46 (hTERT-HPNE, C32, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.42×** | +3.9 | 0.005 | 14/47 (RKO, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.5 | 0.018 | 12/47 (BT-474, SW 900, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.18× | +3.4 | 0.025 | 9/48 (LoVo, NCI-H2347, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12654.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.571×** | -16.7 | 0e+00 | 33/48 (PANC-1, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.664×** | -8.6 | 2e-15 | 32/47 (LoVo, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.741×** | -5.8 | 1e-06 | 25/44 (AN3 CA, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.768×** | -5.3 | 1e-05 | 22/49 (C-33 A, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.783×** | -5.1 | 3e-05 | 24/47 (A-427, AN3 CA, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **0.788×** | -5.0 | 5e-05 | 23/45 (PANC-1, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 0.846× | -5.0 | 5e-05 | 16/47 (SK-MEL-2, NCI-H2030, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.640×** | -4.9 | 7e-05 | 24/45 (A549, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | 0.855× | -4.6 | 2e-04 | 21/47 (HS-578T, A549, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.695×** | -4.0 | 0.004 | 18/48 (LoVo, NCI-H1792, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Sulfatinib (drug)]] 5 µM |  | **0.824×** | -3.9 | 0.005 | 19/48 (KATO III, HS-578T, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.709×** | -3.8 | 0.007 | 17/47 (HEC-1-A, J82, …) | top dose only | noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.851× | -3.4 | 0.031 | 11/46 (H4, J82, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.741×** | -3.3 | 0.040 | 13/46 (LoVo, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | 0.857× | -3.2 | 0.045 | 21/47 (AN3 CA, RPMI-7951, …) | rises with dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.750×** | -3.2 | 0.052 | 12/45 (AsPC-1, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.756×** | -3.1 | 0.065 | 10/47 (AsPC-1, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.866× | -3.0 | 0.073 | 8/47 (SW 1088, C-33 A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12654. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 69.9 | 4 (1 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.10× (z +14.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -13.1) |
| [[SW480 (line)]] | alt | 50.4 | 4 | 2 | [[Panobinostat (drug)]] 5 µM 3.25× (z +14.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -12.2) |
| [[HS-578T (line)]] | alt | 43.3 | 1 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.53× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.290× (z -16.4) |
| [[A549 (line)]] | wt | 98.5 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -14.4) ⚠ cell-cycle shift, explains ~93% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.585× (z -8.6) |
| [[AN3 CA (line)]] | alt | 112 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0716× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~4% of this change |
| [[CFPAC-1 (line)]] | alt | 20.9 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.95× (z +10.3) | — |
| [[HOP62 (line)]] | alt | 23.4 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 5.29× (z +13.4) | — |
| [[Hs 766T (line)]] | wt | 40.9 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 3.74× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -16.8) |
| [[NCI-H2347 (line)]] | alt | 19.7 | 3 | 1 | [[Panobinostat (drug)]] 0.5 µM 3.33× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -11.8) |
| [[PANC-1 (line)]] | alt | 80.8 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 2.93× (z +15.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -18.1) |
| [[SNU-423 (line)]] | alt | 29.8 | 4 | 0 | [[Belinostat (drug)]] 5 µM 3.71× (z +10.1) | — |
| [[A498 (line)]] | wt | 44.1 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.09× (z +10.1) | [[Dinaciclib (drug)]] 0.05 µM 0.355× (z -8.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 18.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 9.83× (z +9.6) | — |
| [[KATO III (line)]] | alt | 43.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.72× (z +13.7) | — |
| [[LoVo (line)]] | wt | 80.6 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.23× (z +9.3) | [[Auranofin (drug)]] 5 µM 0.291× (z -14.4) |
| [[MIA PaCa-2 (line)]] | alt | 36.0 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 3.96× (z +11.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.483× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 34.3 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -15.0) |
| [[NCI-H460 (line)]] | wt | 35.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.73× (z +10.0) | — |
| [[Panc 03.27 (line)]] | alt | 39.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.26× (z +9.5) | — |
| [[SK-MEL-2 (line)]] | alt | 63.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.226× (z -11.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 48.2 | 2 | 1 | [[Belinostat (drug)]] 5 µM 2.63× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -15.8) |
| [[A-427 (line)]] | wt | 45.4 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.36× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.322× (z -11.3) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 90.2 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.44× (z +9.3) | — |
| [[BT-474 (line)]] | alt | 326 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.67× (z +11.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -15.7) |
| [[C-33 A (line)]] | alt | 60.9 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.21× (z +9.6) | — |
| [[COLO 205 (line)]] | alt | 40.7 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.26× (z +9.2) | — |
| [[HEC-1-A (line)]] | alt | 59.8 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.417× (z -12.0) |
| [[HT-29 (line)]] | alt | 63.3 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 2.77× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -10.4) |
| [[hTERT-HPNE (line)]] | wt | 28.6 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.57× (z +9.9) | — |
| [[J82 (line)]] | alt | 63.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -12.9) ⚠ cell-cycle shift, explains ~93% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.520× (z -9.9) |
| [[NCI-H1792 (line)]] | alt | 59.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -12.1) ⚠ cell-cycle shift, explains ~93% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -10.5) |
| [[NCI-H2030 (line)]] | alt | 56.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.315× (z -17.5) |
| [[RKO (line)]] | wt | 68.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.79× (z +9.2) | — |
| [[SNU-1 (line)]] | wt | 83.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.169× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~4% of this change |
| [[HCT15 (line)]] | alt | 28.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.37× (z +8.6) | — |
| [[HepG2_C3A (line)]] | wt | 86.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.404× (z -10.4) |
| [[LS 180 (line)]] | wt | 155 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.74× (z +8.5) | — |
| [[RPMI-7951 (line)]] | alt | 32.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.185× (z -10.6) ⚠ cell-cycle shift, explains ~53% of this change |
| [[SHP-77 (line)]] | alt | 112 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.546× (z -8.5) |
| [[SW 900 (line)]] | alt | 49.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -10.6) |
| [[A-172 (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 49.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.10 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 70.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 75.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12654), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*44 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INPP4A]] | +0.73 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[MAPK8]] | +0.66 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[EPS15]] | +0.61 | +0.61 / +0.46 | both halves | 3e-05 |  |
| [[SGPP1]] | +0.60 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[TMOD2]] | +0.59 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[CRLF3]] | +0.59 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[PACS2]] | +0.58 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[DGKZ]] | +0.58 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[PSMD9]] | +0.58 | +0.56 / +0.31 | both halves | 2e-04 |  |
| [[RALGPS1]] | +0.57 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[STX2]] | +0.57 | +0.56 / +0.39 | both halves | 6e-05 | STRING 461 |
| [[BRF1]] | +0.56 | +0.53 / +0.33 | both halves | 1e-04 |  |

## Genes that move opposite

*56 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRR3]] | -0.63 | -0.53 / -0.39 | both halves | 6e-05 |  |
| [[PNISR-AS1]] | -0.61 | -0.40 / -0.55 | both halves | 4e-05 |  |
| [[METTL6]] | -0.59 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[MFF-DT]] | -0.56 | -0.33 / -0.46 | both halves | 1e-04 |  |
| [[AEBP2]] | -0.56 | -0.44 / -0.38 | both halves | 7e-05 |  |
| [[C1S]] | -0.56 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[THAP2]] | -0.56 | -0.49 / -0.29 | both halves | 2e-04 |  |
| [[TMEM79]] | -0.55 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[CCDC90B-AS1]] | -0.54 | -0.39 / -0.36 | both halves | 9e-05 |  |
| [[PLS3-AS1]] | -0.54 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[ZNF773]] | -0.54 | -0.49 / -0.25 | both halves | 4e-04 |  |
| [[LINC01340]] | -0.54 | -0.47 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLS3-AS1]] | B | PLS3-AS1 activity lowers UNC13B's level | lines that do not express PLS3-AS1 (10) vs lines expressing it (40) | 2.00× higher at baseline in the lines without PLS3-AS1 | 0.078 | ⚠ within organs, on part of the lines; also absent: COPZ2, CAV2, DNAI1 |
| [[ABCA3]] | B | ABCA3 activity raises UNC13B's level | lines that do not express ABCA3 (9) vs lines expressing it (41) | 2.00× lower at baseline in the lines without ABCA3 | 0.086 | ⚠ within organs, on part of the lines; also absent: SLC37A1, CCDC88C, GRTP1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 159]] — High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells; 27 genes; every member is in the + arm (projection on the module's main direction 0.712). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.43; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (0.6, 3.7); signed map (-43.6, -7.4). **Vector** length 119, 34.3% of its response variance represented; |z| ≥ 3 in 1,269 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +5.8 | +19.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.6 | +21.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.5 | +18.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.0 | +11.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.0 | +6.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +6.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.4 | +2.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.1 | +3.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.9 | +2.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.7 | -16.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | -9.8 | -4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -9.0 | -8.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -6.6 | -3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.5 | -2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.9 | +0.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.8 | -3.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.7 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | unc-13 homolog B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.3 — chr9:35,161,992-35,405,338 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hmunc13, Unc13h2, Munc13-2; previously UNC13 |
| Gene groups (HGNC) | UNC13 homologs |
| Hallmark sets | ESTROGEN_RESPONSE_LATE |
| Reactome | 8 pathways, smallest: Acetylcholine Neurotransmitter Release Cycle; Norepinephrine Neurotransmitter Release Cycle; Serotonin Neurotransmitter Release Cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [O14795](https://www.uniprot.org/uniprotkb/O14795) (Protein unc-13 homolog B):

> Plays a role in vesicle maturation during exocytosis as a target of the diacylglycerol second messenger pathway. Is involved in neurotransmitter release by acting in synaptic vesicle priming prior to vesicle fusion and participates in the activity-depending refilling of readily releasable vesicle pool (RRP) (By similarity). Essential for synaptic vesicle maturation in a subset of excitatory/glutamatergic but not inhibitory/GABA-mediated synapses (By similarity). In collaboration with UNC13A, …

**Summary**, from NCBI Gene [10497](https://www.ncbi.nlm.nih.gov/gene/10497):

> This gene is expressed in the kidney cortical epithelial cells and is upregulated by hyperglycemia. The encoded protein shares a high level of similarity to the rat homolog, and contains 3 C2 domains and a diacylglycerol-binding C1 domain. Hyperglycemia increases the levels of diacylglycerol, which has been shown to induce apoptosis in cells transfected with this gene and thus contribute to the renal cell complications of hyperglycemia. Studies in other species also indicate a role for this …

**Accessions** — [HGNC:12566](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12566) · Entrez [10497](https://www.ncbi.nlm.nih.gov/gene/10497) · UniProt [O14795](https://www.uniprot.org/uniprotkb/O14795) · Ensembl [ENSG00000198722](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198722)

## Data

Gene col 12654: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12654); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12654, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12654]; `tensor/DDL_lfc|DDL_z.npy` [12654]; `embed/gene_vectors.npy` [12654]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12654 or target_col == 12654). Every well: [[UNC13B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UNC13B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
