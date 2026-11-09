---
symbol: "RAB30-DT"
type: "gene"
col: 14452
ensembl_id: "ENSG00000246067"
name: "RAB30 divergent transcript"
location: "11q14.1"
module: 88
arm: "+"
pooled_cpm: 49.46
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 14
n_dd_up_clean: 14
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/088"]
generated_by: "tahoemap"
---

# RAB30-DT

*RAB30 divergent transcript* — 11q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.66× (z +17.0, q 0e+00, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (9 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.430× (z -10.4, q 1e-22, down in 40 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.415× (z -5.7, q 1e-06, down in 33 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ST7L]] (+0.84, fdr 7e-06), [[CLHC1]] (+0.82, fdr 1e-05), [[PPP3CB-AS1]] (+0.82, fdr 8e-06); moves opposite to [[GMCL1]] (-0.75, fdr 1e-05), [[LPCAT4]] (-0.74, fdr 1e-05), [[PIK3R2]] (-0.72, fdr 1e-05).
> It sits in the **+** arm of [[Module 088]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, none with an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14452.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.66×** | +17.0 | 0e+00 | 44/47 (LoVo, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.96×** | +11.7 | 3e-29 | 48/48 (PANC-1, SW1417, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.25×** | +10.0 | 2e-21 | 40/47 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.86×** | +7.7 | 2e-12 | 45/48 (A-172, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.63×** | +5.8 | 8e-07 | 34/48 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.45×** | +4.6 | 5e-04 | 26/48 (HT-29, SW 900, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.43×** | +4.4 | 1e-03 | 32/48 (LoVo, HOP62, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.35×** | +3.7 | 0.017 | 22/47 (LoVo, HOP62, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.21×** | +3.2 | 0.076 | 18/48 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.21×** | +3.2 | 0.076 | 20/48 (SW480, C32, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.30×** | +3.1 | 0.079 | 17/47 (SW480, A549, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.30×** | +3.1 | 0.079 | 23/47 (SW480, LoVo, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.29×** | +3.1 | 0.079 | 20/48 (KATO III, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.28×** | +3.1 | 0.079 | 17/48 (A-172, NCI-H460, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14452.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.430×** | -10.4 | 1e-22 | 40/47 (LS 180, NCI-H460, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.457×** | -9.3 | 4e-18 | 40/47 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.556×** | -7.2 | 9e-11 | 34/48 (PANC-1, BT-474, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.558×** | -7.2 | 9e-11 | 40/48 (SW1417, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.575×** | -6.8 | 1e-09 | 39/48 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.615×** | -6.0 | 2e-07 | 33/48 (NCI-H1573, NCI-H23, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.415×** | -5.7 | 1e-06 | 33/49 (SW480, BT-474, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.511×** | -4.3 | 0.001 | 30/47 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.515×** | -4.3 | 0.001 | 27/48 (MIA PaCa-2, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.716×** | -4.1 | 0.002 | 27/48 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.724×** | -4.0 | 0.003 | 26/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.762×** | -3.3 | 0.038 | 20/48 (BT-474, PANC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.767×** | -3.3 | 0.048 | 22/48 (BT-474, NCI-H460, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.618×** | -3.1 | 0.076 | 17/36 (AsPC-1, H4, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14452. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 67.8 | 2 | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +16.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.237× (z -13.7) ⚠ toxic |
| [[A-427 (line)]] | wt | 67.7 | 2 | 5 (4 ⚠) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 1.81× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.187× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -9.2) |
| [[LoVo (line)]] | wt | 54.3 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.97× (z +28.5) | [[Dinaciclib (drug)]] 0.5 µM 0.239× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 76.2 | 3 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +17.0) | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 62.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +12.5) | — |
| [[NCI-H1792 (line)]] | alt | 38.1 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +15.6) | [[Digitoxin (drug)]] 5 µM 0.221× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SW480 (line)]] | alt | 61.6 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +14.8) | [[Digitoxin (drug)]] 5 µM 0.301× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[BT-474 (line)]] | alt | 73.9 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.214× (z -13.1) ⚠ cell-cycle shift, explains ~41% of this change |
| [[COLO 205 (line)]] | alt | 75.1 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.132× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 67.4 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.24× (z +15.5) | [[Dinaciclib (drug)]] 0.05 µM 0.237× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 42.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.63× (z +13.0) | — |
| [[NCI-H460 (line)]] | wt | 41.4 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +12.6) | [[Digitoxin (drug)]] 5 µM 0.179× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[A-172 (line)]] | wt | 54.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +12.5) | — |
| [[HepG2_C3A (line)]] | wt | 48.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +8.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.246× (z -8.8) ⚠ toxic |
| [[HT-29 (line)]] | alt | 54.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +10.9) | [[Digitoxin (drug)]] 5 µM 0.266× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[LOX-IMVI (line)]] | wt | 58.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +13.3) | [[Niclosamide (olamine) (drug)]] 5 µM 0.251× (z -10.3) ⚠ toxic |
| [[LS 180 (line)]] | wt | 51.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +9.0) | [[Digitoxin (drug)]] 5 µM 0.149× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[Panc 03.27 (line)]] | alt | 50.8 | 1 | 1 (1 ⚠) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 2.43× (z +9.0) | [[Digitoxin (drug)]] 5 µM 0.229× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SNU-1 (line)]] | wt | 84.0 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.227× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SW1417 (line)]] | alt | 45.3 | 1 | 1 (1 ⚠) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 2.77× (z +12.0) | [[Panobinostat (drug)]] 0.5 µM 0.336× (z -9.0) ⚠ cell-cycle shift, explains ~36% of this change |
| [[SW48 (line)]] | wt | 38.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.95× (z +13.8) | — |
| [[A498 (line)]] | wt | 21.3 | 1 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 2.73× (z +8.9) | — |
| [[AsPC-1 (line)]] | alt | 24.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +11.3) | — |
| [[C-33 A (line)]] | alt | 82.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +10.9) | — |
| [[C32 (line)]] | wt | 31.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +8.9) | — |
| [[CFPAC-1 (line)]] | alt | 29.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +9.3) | — |
| [[H4 (line)]] | wt | 40.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +11.2) | — |
| [[HOP62 (line)]] | alt | 36.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +15.0) | — |
| [[Hs 766T (line)]] | wt | 33.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +8.8) | — |
| [[hTERT-HPNE (line)]] | wt | 31.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.63× (z +11.7) | — |
| [[J82 (line)]] | alt | 60.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +11.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 52.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.206× (z -10.9) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 35.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.27× (z +17.7) | — |
| [[NCI-H23 (line)]] | alt | 53.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +12.2) | — |
| [[RPMI-7951 (line)]] | alt | 47.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +10.2) | — |
| [[SHP-77 (line)]] | alt | 36.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.283× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 1271 (line)]] | alt | 85.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0985× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SW 900 (line)]] | alt | 35.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +9.5) | — |
| [[A549 (line)]] | wt | 49.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 52.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 63.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 62.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14452), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST7L]] | +0.84 | +0.86 / +0.63 | both halves | 7e-06 |  |
| [[CLHC1]] | +0.82 | +0.86 / +0.56 | both halves | 1e-05 |  |
| [[PPP3CB-AS1]] | +0.82 | +0.80 / +0.58 | both halves | 8e-06 |  |
| [[KRCC1]] | +0.81 | +0.84 / +0.63 | both halves | 7e-06 |  |
| [[RFX3-DT]] | +0.81 | +0.84 / +0.54 | both halves | 1e-05 | same gene group |
| [[BCDIN3D]] | +0.79 | +0.79 / +0.59 | both halves | 7e-06 |  |
| [[ATE1OSP]] | +0.78 | +0.82 / +0.49 | both halves | 1e-05 |  |
| [[MZF1-AS1]] | +0.78 | +0.81 / +0.49 | both halves | 1e-05 |  |
| [[PPP1R12A-AS2]] | +0.78 | +0.81 / +0.48 | both halves | 2e-05 |  |
| [[WARS2-AS1]] | +0.78 | +0.81 / +0.52 | both halves | 1e-05 |  |
| [[ZNF407-AS1]] | +0.78 | +0.85 / +0.44 | both halves | 3e-05 |  |
| [[GABPB2]] | +0.76 | +0.79 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GMCL1]] | -0.75 | -0.78 / -0.56 | both halves | 1e-05 |  |
| [[LPCAT4]] | -0.74 | -0.75 / -0.53 | both halves | 1e-05 |  |
| [[PIK3R2]] | -0.72 | -0.75 / -0.56 | both halves | 1e-05 |  |
| [[HACE1]] | -0.71 | -0.71 / -0.53 | both halves | 1e-05 |  |
| [[IGSF8]] | -0.71 | -0.64 / -0.48 | both halves | 2e-05 |  |
| [[RPA1]] | -0.70 | -0.78 / -0.52 | both halves | 1e-05 |  |
| [[POGLUT2]] | -0.69 | -0.59 / -0.60 | both halves | 7e-06 |  |
| [[MAST3]] | -0.69 | -0.64 / -0.33 | both halves | 1e-04 |  |
| [[SHQ1]] | -0.69 | -0.67 / -0.57 | both halves | 9e-06 |  |
| [[EFNA4]] | -0.69 | -0.60 / -0.40 | both halves | 5e-05 |  |
| [[SKP2]] | -0.68 | -0.67 / -0.57 | both halves | 1e-05 |  |
| [[PAPSS1]] | -0.68 | -0.59 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers RAB30-DT's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[PMP22]] | B | PMP22 activity lowers RAB30-DT's level | lines that do not express PMP22 (10) vs lines expressing it (40) | 1.26× higher at baseline in the lines without PMP22 | 0.072 | ⚠ within organs, on part of the lines; also absent: FKBP7, FAM216A, ARHGEF6; maybe low, not absent |
| [[RGS14]] | C | RGS14 activity lowers RAB30-DT's level | lines that do not express RGS14 (4) vs lines expressing it (46) | 1.61× higher at baseline in the lines without RGS14 | 0.068 | ⚠ few lines (4 vs 46); within organs, on part of the lines |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 088]]; 51 genes; this gene is in the **+** arm (projection on the module's main direction 0.888). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.46).
- **Nodal map** (x, y) = (5.0, 7.7); signed map (17.9, -25.0). **Vector** length 131, 43.3% of its response variance represented; |z| ≥ 3 in 1,177 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +13.8 | +10.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +13.0 | +17.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +9.2 | +5.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +8.2 | +2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +8.0 | +3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.6 | +4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.8 | +11.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.6 | +3.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.9 | +1.4 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -9.8 | -7.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -9.4 | -6.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -9.1 | -6.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -6.4 | -2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.9 | -1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.2 | -0.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.4 | -1.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.8 | -3.3 |
|  | [[Ipatasertib (drug)]] 0.05 µM |  | -2.5 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | RAB30 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 11q14.1 — chr11:83,072,052-83,107,789 (+) |
| Ensembl biotype | lncRNA |
| Also known as | LFPM; previously RAB30-AS1 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:48672](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48672) · Entrez [100506233](https://www.ncbi.nlm.nih.gov/gene/100506233) · Ensembl [ENSG00000246067](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000246067)

## Data

Gene col 14452: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14452); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14452, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14452]; `tensor/DDL_lfc|DDL_z.npy` [14452]; `embed/gene_vectors.npy` [14452]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14452 or target_col == 14452). Every well: [[RAB30-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB30-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
