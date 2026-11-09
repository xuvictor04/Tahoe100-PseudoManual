---
symbol: "OGDH"
type: "gene"
col: 2692
ensembl_id: "ENSG00000105953"
name: "oxoglutarate dehydrogenase"
location: "7p13"
module: 39
arm: "+"
pooled_cpm: 122.21
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 21
n_dd_up_clean: 6
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# OGDH

*oxoglutarate dehydrogenase* — 7p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.40× (z +11.6, q 2e-28, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (10 with an alert ⚠); the strongest is [[Belinostat (drug)]] 0.5 µM: 0.634× (z -11.1, q 1e-25, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPRC5D-AS1]] (+0.56, fdr 1e-05), [[ADCY10P1]] (+0.55, fdr 2e-05), [[INO80C]] (+0.54, fdr 2e-05); moves opposite to [[TERF1]] (-0.56, fdr 1e-05), [[ACVR1B]] (-0.54, fdr 5e-05), [[TMEM218]] (-0.53, fdr 4e-05).
> It is in [[Module 039]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2692.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +11.6 | 2e-28 | 43/48 (MIA PaCa-2, SW1417, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.41×** | +8.3 | 3e-14 | 34/49 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.29×** | +6.2 | 8e-08 | 27/47 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.30×** | +6.2 | 1e-07 | 33/47 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +5.8 | 9e-07 | 23/48 (C32, SK-MEL-2, …) | top dose only | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +5.7 | 1e-06 | 17/48 (KATO III, Hs 766T, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.47×** | +4.9 | 8e-05 | 26/48 (BT-474, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | 1.19× | +4.2 | 0.002 | 19/48 (NCI-H1792, AsPC-1, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.38×** | +4.0 | 0.003 | 22/48 (SW1417, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Omeprazole (drug)]] 0.05 µM |  | 1.16× | +3.6 | 0.019 | 13/48 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 0.05 µM |  | 1.16× | +3.5 | 0.026 | 15/48 (PANC-1, Hs 766T, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 1.14× | +3.1 | 0.098 | 8/49 (A498, BT-474, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 1.13× | +3.0 | 0.10 | 12/48 (CHP-212, BT-474, …) | inconsistent across doses |  |
| [[Cepharanthine (drug)]] 5 µM |  | 1.09× | +3.0 | 0.10 | 5/48 (NCI-H23, A549, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2692.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 0.5 µM |  | **0.634×** | -11.1 | 1e-25 | 43/48 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.662×** | -9.6 | 2e-19 | 33/48 (PANC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.678×** | -9.4 | 7e-19 | 35/48 (RPMI-7951, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.767×** | -9.1 | 1e-17 | 28/49 (HEC-1-A, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.700×** | -8.7 | 6e-16 | 31/48 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.710×** | -8.3 | 8e-15 | 30/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.571×** | -7.1 | 9e-11 | 30/49 (LS 180, KATO III, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.584×** | -6.8 | 7e-10 | 36/47 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~24% here); noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **0.761×** | -6.6 | 2e-09 | 33/48 (PANC-1, SW 1088, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.761×** | -6.6 | 2e-09 | 29/48 (PANC-1, RPMI-7951, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.776×** | -6.2 | 4e-08 | 24/48 (A498, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.616×** | -6.1 | 4e-08 | 29/45 (SW 900, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.619×** | -6.1 | 5e-08 | 36/48 (LS 180, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.770×** | -6.0 | 8e-08 | 30/48 (LoVo, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.787×** | -5.8 | 2e-07 | 29/48 (MIA PaCa-2, PANC-1, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 0.848× | -5.7 | 5e-07 | 14/48 (LoVo, AsPC-1, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **0.792×** | -5.6 | 5e-07 | 23/48 (COLO 205, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.896× | -3.8 | 0.004 | 10/49 (Panc 03.27, SHP-77, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.868× | -3.4 | 0.013 | 19/48 (Panc 03.27, A549, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.879× | -3.1 | 0.037 | 14/48 (KATO III, LoVo, …) | top dose only |  |
| [[Mebendazole (drug)]] 0.5 µM |  | 0.879× | -3.1 | 0.038 | 6/48 (NCI-H2347, NCI-H23, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2692. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 137 | 0 | 12 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.315× (z -22.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.560× (z -11.1) |
| [[NCI-H460 (line)]] | wt | 180 | 3 | 6 (5 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 2.49× (z +12.8) | [[Harringtonine (drug)]] 5 µM 0.412× (z -12.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.638× (z -9.3) |
| [[H4 (line)]] | wt | 172 | 0 | 6 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.258× (z -13.8) ⚠ cell-cycle shift, explains ~27% of this change |
| [[RPMI-7951 (line)]] | alt | 136 | 1 | 5 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.74× (z +8.8) | [[Ixazomib citrate (drug)]] 5 µM 0.317× (z -12.9) |
| [[SW480 (line)]] | alt | 155 | 2 | 3 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.57× (z +10.2) | [[Digitoxin (drug)]] 5 µM 0.529× (z -10.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 103 | 1 | 3 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.63× (z +10.7) | [[Harringtonine (drug)]] 5 µM 0.390× (z -14.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.659× (z -9.3) |
| [[AsPC-1 (line)]] | alt | 235 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.363× (z -11.4) ⚠ cell-cycle shift, explains ~27% of this change |
| [[HEC-1-A (line)]] | alt | 169 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.50× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -12.7) |
| [[KATO III (line)]] | alt | 216 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.283× (z -18.1) ⚠ cell-cycle shift, explains ~27% of this change |
| [[LS 180 (line)]] | wt | 153 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.384× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.615× (z -9.0) |
| [[SW1417 (line)]] | alt | 134 | 1 | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.82× (z +11.6) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.517× (z -9.1) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A-427 (line)]] | wt | 66.8 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.417× (z -9.5) ⚠ cell-cycle shift, explains ~28% of this change |
| [[C32 (line)]] | wt | 56.3 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +15.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[COLO 205 (line)]] | alt | 143 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.543× (z -9.3) |
| [[Hs 766T (line)]] | wt | 160 | 2 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 1.80× (z +9.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 171 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 1.82× (z +11.7) | [[Auranofin (drug)]] 5 µM 0.403× (z -12.6) |
| [[NCI-H1573 (line)]] | alt | 76.9 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.368× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 88.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.17× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Harringtonine (drug)]] 5 µM 0.449× (z -9.0) ⚠ cell-cycle shift, explains ~28% of this change |
| [[RKO (line)]] | wt | 47.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.337× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 61.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +14.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Lonafarnib (drug)]] 5 µM 0.119× (z -10.7) ⚠ toxic |
| [[A-172 (line)]] | wt | 136 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.573× (z -9.3) |
| [[A549 (line)]] | wt | 88.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.38× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[AN3 CA (line)]] | alt | 78.2 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0947× (z -12.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HCT15 (line)]] | alt | 150 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.474× (z -8.9) |
| [[HT-29 (line)]] | alt | 143 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.377× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 90.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.615× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 114 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.118× (z -12.2) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 96.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.546× (z -9.6) |
| [[SW 900 (line)]] | alt | 108 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.368× (z -9.8) ⚠ cell-cycle shift, explains ~28% of this change |
| [[BT-474 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 75.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 83.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 65.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 64.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 77.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 91.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 84.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 89.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 239 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 54.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 86.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 50.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 87.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 237 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 124 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2692), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPRC5D-AS1]] | +0.56 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[ADCY10P1]] | +0.55 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[INO80C]] | +0.54 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[LAT2]] | +0.53 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[PILRA]] | +0.52 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[ALDH8A1]] | +0.52 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[SSUH2]] | +0.52 | +0.61 / +0.42 | both halves | 4e-05 |  |
| [[UBAP2]] | +0.51 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[LINC00910]] | +0.51 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[RIPK1]] | +0.50 | +0.50 / +0.46 | both halves | 2e-05 |  |
| [[PPIEL-1]] | +0.50 | +0.59 / +0.41 | both halves | 4e-05 |  |
| [[SPTBN5]] | +0.49 | +0.52 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TERF1]] | -0.56 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[ACVR1B]] | -0.54 | -0.64 / -0.40 | both halves | 5e-05 |  |
| [[TMEM218]] | -0.53 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[USP30]] | -0.53 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[FHIP2A]] | -0.50 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[CHPT1]] | -0.49 | -0.62 / -0.36 | both halves | 1e-04 |  |
| [[HSF2]] | -0.49 | -0.58 / -0.31 | both halves | 2e-04 |  |
| [[ZSCAN2]] | -0.48 | -0.52 / -0.27 | both halves | 3e-04 |  |
| [[CIPC]] | -0.48 | -0.57 / -0.40 | both halves | 5e-05 |  |
| [[SLC25A38]] | -0.48 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[NAGPA]] | -0.46 | -0.46 / -0.37 | both halves | 8e-05 |  |
| [[RPP30]] | -0.45 | -0.58 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.459). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.9, -14.8); signed map (14.4, 9.9). **Vector** length 117, 34.4% of its response variance represented; |z| ≥ 3 in 1,297 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.0 | +11.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +4.9 | +6.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +4.7 | +6.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.7 | +8.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.1 | +4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +5.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.9 | +4.0 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -8.4 | -11.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.1 | -9.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -5.7 | -5.7 |
|  | [[NG25 (drug)]] 5 µM |  | -5.1 | -6.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.1 | -3.1 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -3.2 | -2.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.0 | -2.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.9 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | oxoglutarate dehydrogenase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p13 — chr7:44,606,572-44,709,066 (+) |
| Ensembl biotype | protein_coding |
| Also known as | E1k, OGDC-E1, OGDH2, KGD1 |
| Gene groups (HGNC) | Oxoglutarate dehydrogenase family; Oxoglutarate dehydrogenase complex subunits |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 7 pathways, smallest: OGDH complex synthesizes succinyl-CoA from 2-OG; Glycine degradation; Glyoxylate metabolism and glycine degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q02218](https://www.uniprot.org/uniprotkb/Q02218) (2-oxoglutarate dehydrogenase complex component E1):

> 2-oxoglutarate dehydrogenase (E1o) component of the 2-oxoglutarate dehydrogenase complex (OGDHC). Participates in the first step, rate limiting for the overall conversion of 2-oxoglutarate to succinyl-CoA and CO(2) catalyzed by the whole OGDHC. Catalyzes the irreversible decarboxylation of 2-oxoglutarate (alpha-ketoglutarate) via the thiamine diphosphate (ThDP) cofactor and subsequent transfer of the decarboxylated acyl intermediate on an oxidized dihydrolipoyl group that is covalently amidated …

**Summary**, from NCBI Gene [4967](https://www.ncbi.nlm.nih.gov/gene/4967):

> This gene encodes one subunit of the 2-oxoglutarate dehydrogenase complex. This complex catalyzes the overall conversion of 2-oxoglutarate (alpha-ketoglutarate) to succinyl-CoA and CO(2) during the Krebs cycle. The protein is located in the mitochondrial matrix and uses thiamine pyrophosphate as a cofactor. A congenital deficiency in 2-oxoglutarate dehydrogenase activity is believed to lead to hypotonia, metabolic acidosis, and hyperlactatemia. Alternative splicing results in multiple …

**Accessions** — [HGNC:8124](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8124) · Entrez [4967](https://www.ncbi.nlm.nih.gov/gene/4967) · UniProt [Q02218](https://www.uniprot.org/uniprotkb/Q02218) · Ensembl [ENSG00000105953](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105953)

## Data

Gene col 2692: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2692); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2692, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2692]; `tensor/DDL_lfc|DDL_z.npy` [2692]; `embed/gene_vectors.npy` [2692]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2692 or target_col == 2692). Every well: [[OGDH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OGDH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
