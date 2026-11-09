---
symbol: "STIM2"
type: "gene"
col: 3074
ensembl_id: "ENSG00000109689"
name: "stromal interaction molecule 2"
location: "4p15.2"
module: 197
arm: "+"
pooled_cpm: 40.88
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 7
n_dd_up_clean: 11
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/197"]
generated_by: "tahoemap"
---

# STIM2

*stromal interaction molecule 2* — 4p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.68× (z +24.5, q 0e+00, up in 47 of 48 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.71× (z +18.9, q 0e+00, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Vinblastine (sulfate) (drug)]] 5 µM: 0.803× (z -7.8, q 5e-12, down in 26 of 49 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAGI1]] (+0.59, fdr 1e-05), [[NEO1]] (+0.57, fdr 1e-05), [[LRP6]] (+0.55, fdr 1e-05); moves opposite to [[VIPAS39]] (-0.59, fdr 1e-05), [[SLC30A6]] (-0.58, fdr 3e-05), [[ACOX3]] (-0.58, fdr 1e-05).
> It is in [[Module 197]], a single-armed module (Nervous system development).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 21 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3074.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.68×** | +24.5 | 0e+00 | 47/48 (A498, J82, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.52×** | +23.0 | 0e+00 | 47/47 (A498, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.40×** | +21.7 | 0e+00 | 47/48 (A498, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.71×** | +18.9 | 0e+00 | 37/48 (hTERT-HPNE, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.12×** | +18.7 | 0e+00 | 46/48 (LoVo, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.55×** | +15.3 | 0e+00 | 45/48 (SW480, LoVo, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.54×** | +15.1 | 0e+00 | 34/48 (LS 180, LoVo, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.70×** | +13.1 | 2e-37 | 43/47 (LoVo, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.65×** | +12.4 | 2e-33 | 36/48 (NCI-H460, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.62×** | +11.5 | 1e-28 | 31/48 (NCI-H460, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +10.5 | 6e-24 | 35/48 (SW480, LoVo, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.19×** | +10.2 | 9e-23 | 40/49 (LoVo, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **2.08×** | +9.5 | 8e-20 | 37/47 (A498, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.45×** | +9.2 | 1e-18 | 30/47 (J82, HOP62, …) | two highest doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.39×** | +8.2 | 6e-15 | 32/49 (LoVo, RKO, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.38×** | +8.0 | 4e-14 | 29/47 (SK-MEL-2, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | 1.16× | +3.7 | 0.004 | 13/48 (NCI-H1573, A-172, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.05 µM |  | 1.14× | +3.3 | 0.018 | 7/47 (HEC-1-A, LoVo, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.14× | +3.1 | 0.034 | 7/47 (C32, BT-474, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.14× | +3.1 | 0.036 | 13/47 (NCI-H1573, AsPC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3074.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.803×** | -7.8 | 5e-12 | 26/49 (HT-29, LS 180, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.766×** | -6.7 | 7e-09 | 23/47 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.780×** | -6.2 | 1e-07 | 24/47 (NCI-H1573, HepG2/C3A, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.785×** | -5.7 | 2e-06 | 22/48 (HT-29, SW48, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.940× | -5.1 | 4e-05 | 2/49 (NCI-H23, SW 1271) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.826×** | -4.8 | 2e-04 | 18/47 (A498, HT-29, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.828×** | -4.7 | 2e-04 | 22/47 (HT-29, LoVo, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.828×** | -4.5 | 4e-04 | 16/47 (AN3 CA, RKO, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | 0.884× | -4.4 | 7e-04 | 15/48 (HT-29, LS 180, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.862× | -3.6 | 0.020 | 15/47 (HT-29, LS 180, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.905× | -3.5 | 0.020 | 11/48 (NCI-H2030, H4, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.875× | -3.3 | 0.039 | 13/47 (HT-29, C32, …) | rises with dose |  |
| [[Neratinib (drug)]] 5 µM |  | 0.876× | -3.3 | 0.039 | 10/47 (RKO, HT-29, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.47 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3074. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 29.7 | 7 (4 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +12.8) | [[Ixazomib citrate (drug)]] 5 µM 0.409× (z -9.0) |
| [[HOP62 (line)]] | alt | 19.3 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +11.9) | — |
| [[NCI-H1573 (line)]] | alt | 42.4 | 6 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.81× (z +12.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.19× (z +10.1) | — |
| [[NCI-H2347 (line)]] | alt | 32.0 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +11.0) | — |
| [[CFPAC-1 (line)]] | alt | 26.9 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +14.4) | — |
| [[SK-MEL-2 (line)]] | alt | 39.1 | 5 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.36× (z +9.8) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.11× (z +8.5) | — |
| [[SNU-423 (line)]] | alt | 18.1 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +12.1) | — |
| [[J82 (line)]] | alt | 29.7 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.95× (z +12.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 2.57× (z +8.6) | — |
| [[LoVo (line)]] | wt | 59.0 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +11.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 2.74× (z +10.9) | — |
| [[NCI-H1792 (line)]] | alt | 25.5 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +11.9) | — |
| [[RKO (line)]] | wt | 34.7 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.89× (z +9.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 3.70× (z +9.4) | — |
| [[SW480 (line)]] | alt | 44.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +9.6) | — |
| [[A-172 (line)]] | wt | 17.1 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 5.32× (z +10.1) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[A-427 (line)]] | wt | 83.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -21.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 41.3 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.17× (z +14.1) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[C-33 A (line)]] | alt | 117 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.107× (z -20.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 25.7 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.96× (z +10.6) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[HT-29 (line)]] | alt | 106 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.340× (z -11.8) |
| [[hTERT-HPNE (line)]] | wt | 23.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.60× (z +14.5) | — |
| [[PANC-1 (line)]] | alt | 32.8 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.53× (z +11.8) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[AsPC-1 (line)]] | alt | 22.0 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.86× (z +9.4) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[COLO 205 (line)]] | alt | 39.4 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +10.4) | [[Sonidegib (drug)]] 5 µM 0.0642× (z -10.3) |
| [[LS 180 (line)]] | wt | 78.1 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +12.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.71× (z +8.6) | — |
| [[NCI-H23 (line)]] | alt | 45.8 | 2 (2 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.57× (z +8.6) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[RPMI-7951 (line)]] | alt | 24.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +12.4) | — |
| [[SW48 (line)]] | wt | 73.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.110× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 19.2 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.46× (z +8.6) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[AN3 CA (line)]] | alt | 48.9 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.136× (z -9.0) ⚠ cell-cycle shift, explains ~42% of this change |
| [[CHP-212 (line)]] | wt | 69.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0726× (z -13.2) ⚠ cell-cycle shift, explains ~22% of this change |
| [[HEC-1-A (line)]] | alt | 49.0 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0812× (z -13.0) ⚠ toxic |
| [[KATO III (line)]] | alt | 31.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 12.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +9.9) | — |
| [[SNU-1 (line)]] | wt | 46.0 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.37× (z +8.8) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[SW 900 (line)]] | alt | 85.1 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.47× (z +9.0) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[BT-474 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 113 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 52.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 40.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 37.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3074), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAGI1]] | +0.59 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[NEO1]] | +0.57 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[LRP6]] | +0.55 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[DPY19L1]] | +0.54 | +0.27 / +0.51 | both halves | 3e-04 |  |
| [[ARHGEF12]] | +0.54 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[EML4]] | +0.54 | +0.37 / +0.61 | both halves | 8e-05 |  |
| [[H2AZ2]] | +0.53 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[TCF7L2]] | +0.52 | +0.39 / +0.48 | both halves | 6e-05 |  |
| [[PCDH7]] | +0.52 | +0.65 / +0.46 | both halves | 2e-05 | STRING 700 |
| [[OSBPL10]] | +0.52 | +0.36 / +0.50 | both halves | 1e-04 |  |
| [[MED14]] | +0.52 | +0.21 / +0.51 | both halves | 7e-04 |  |
| [[ABCD3]] | +0.52 | +0.46 / +0.61 | both halves | 3e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VIPAS39]] | -0.59 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[SLC30A6]] | -0.58 | -0.67 / -0.45 | both halves | 3e-05 |  |
| [[ACOX3]] | -0.58 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[METTL22]] | -0.55 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[NOXRED1]] | -0.52 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[ZBTB49]] | -0.52 | -0.54 / -0.40 | both halves | 5e-05 |  |
| [[KRBOX4]] | -0.52 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[PCYT1A]] | -0.51 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[ZFAND2A]] | -0.50 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[CCDC32]] | -0.50 | -0.56 / -0.34 | both halves | 1e-04 |  |
| [[ZBTB43]] | -0.50 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[RUFY2]] | -0.49 | -0.56 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers STIM2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises STIM2's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 197]] — Nervous system development; 16 genes; every member is in the + arm (projection on the module's main direction 0.621). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.45; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-6.2, 37.7); signed map (5.0, 12.9). **Vector** length 88.7, 21.5% of its response variance represented; |z| ≥ 3 in 1,312 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.8 | +15.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.5 | +18.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.8 | +8.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.5 | +13.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | +3.0 | +4.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.7 | +10.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +10.5 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +1.9 | +1.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.8 | +3.1 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | -6.9 | -5.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -6.6 | -6.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.9 | -6.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.7 | -1.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | -1.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.3 | -7.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.0 | -0.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.6 | -4.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.7 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | stromal interaction molecule 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p15.2 — chr4:26,857,601-27,025,381 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Sterile alpha motif domain containing; Stromal interaction molecule family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P246](https://www.uniprot.org/uniprotkb/Q9P246) (Stromal interaction molecule 2):

> Plays a role in mediating store-operated Ca(2+) entry (SOCE), a Ca(2+) influx following depletion of intracellular Ca(2+) stores. Functions as a highly sensitive Ca(2+) sensor in the endoplasmic reticulum which activates both store-operated and store-independent Ca(2+)-influx. Regulates basal cytosolic and endoplasmic reticulum Ca(2+) concentrations. Upon mild variations of the endoplasmic reticulum Ca(2+) concentration, translocates from the endoplasmic reticulum to the plasma membrane where …

**Summary**, from NCBI Gene [57620](https://www.ncbi.nlm.nih.gov/gene/57620):

> This gene is a member of the stromal interaction molecule (STIM) family and likely arose, along with related family member STIM1, from a common ancestral gene. The encoded protein functions to regulate calcium concentrations in the cytosol and endoplasmic reticulum, and is involved in the activation of plasma membrane Orai Ca(2+) entry channels. This gene initiates translation from a non-AUG (UUG) start site. A signal peptide is cleaved from the resulting protein. Multiple transcript variants …

**Accessions** — [HGNC:19205](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19205) · Entrez [57620](https://www.ncbi.nlm.nih.gov/gene/57620) · UniProt [Q9P246](https://www.uniprot.org/uniprotkb/Q9P246) · Ensembl [ENSG00000109689](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109689)

## Data

Gene col 3074: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3074); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3074, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3074]; `tensor/DDL_lfc|DDL_z.npy` [3074]; `embed/gene_vectors.npy` [3074]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3074 or target_col == 3074). Every well: [[STIM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STIM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
