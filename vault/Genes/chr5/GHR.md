---
symbol: "GHR"
type: "gene"
col: 3419
ensembl_id: "ENSG00000112964"
name: "growth hormone receptor"
location: "5p13.1-p12"
module: 104
arm: "+"
pooled_cpm: 25.23
n_lines_expressing: 26
n_dd_up: 24
n_dd_down: 29
n_dd_up_clean: 19
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 6
direction_downstream: 3
tags: ["gene", "module/104"]
generated_by: "tahoemap"
---

# GHR

*growth hormone receptor* — 5p13.1-p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (5 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.26× (z +17.5, q 0e+00, up in 17 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (10 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.512× (z -10.2, q 2e-21, down in 19 of 23 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF175]] (+0.65, fdr 1e-05), [[DAAM2]] (+0.62, fdr 1e-05), [[TMEM108]] (+0.62, fdr 7e-06); moves opposite to [[ZBTB22]] (-0.43, fdr 9e-05), [[LINC02086]] (-0.43, fdr 1e-04), [[SHISAL1]] (-0.42, fdr 2e-04).
> It is in [[Module 104]], a single-armed module (Molecules associated with elastic fibres).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[KDM2B-DT]] → it (grade B ⚠); 3 go from it, the strongest it → [[RORA]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3419.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.26×** | +17.5 | 0e+00 | 17/24 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.03×** | +16.8 | 0e+00 | 19/23 (NCI-H460, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.18×** | +16.7 | 0e+00 | 5/24 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.61×** | +14.6 | 0e+00 | 16/23 (SHP-77, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.08×** | +11.1 | 9e-27 | 15/23 (NCI-H460, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.06×** | +11.0 | 4e-26 | 15/23 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.85×** | +9.3 | 7e-19 | 18/23 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.83×** | +9.2 | 4e-18 | 14/23 (NCI-H1573, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.55×** | +7.4 | 6e-12 | 15/24 (NCI-H23, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.57×** | +6.4 | 1e-08 | 3/19 (NCI-H460, LoVo, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.41×** | +5.3 | 7e-06 | 11/23 (HS-578T, SW 900, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +5.0 | 3e-05 | 0/14 | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Budesonide (drug)]] 0.5 µM |  | **1.37×** | +4.8 | 7e-05 | 7/23 (HS-578T, SW 900, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.33×** | +4.4 | 5e-04 | 3/21 (NCI-H460, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.32×** | +4.2 | 9e-04 | 9/23 (HS-578T, NCI-H1792, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.29×** | +3.9 | 0.004 | 6/23 (A498, CHP-212, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 0.5 µM |  | **1.43×** | +3.9 | 0.004 | 5/23 (SHP-77, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.27×** | +3.6 | 0.009 | 6/23 (HS-578T, SW 900, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3419.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.512×** | -10.2 | 2e-21 | 19/23 (LOX-IMVI, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.545×** | -9.2 | 9e-18 | 18/23 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.598×** | -7.8 | 1e-12 | 19/23 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.605×** | -7.6 | 3e-12 | 14/23 (C32, A498, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.739×** | -6.5 | 1e-08 | 18/23 (C32, LOX-IMVI, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.659×** | -6.3 | 2e-08 | 10/23 (C32, A498, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.666×** | -6.2 | 6e-08 | 18/23 (C32, A-172, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.673×** | -6.0 | 1e-07 | 10/23 (H4, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.678×** | -5.9 | 2e-07 | 18/23 (A498, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.718×** | -5.0 | 3e-05 | 14/23 (C32, LOX-IMVI, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.724×** | -4.9 | 5e-05 | 12/23 (C32, BT-474, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.729×** | -4.8 | 7e-05 | 18/23 (C32, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.754×** | -4.3 | 8e-04 | 15/23 (H4, SW 900, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.759×** | -4.2 | 0.001 | 7/23 (LOX-IMVI, A498, …) | top dose only |  |
| [[crizotinib (drug)]] 5 µM |  | **0.752×** | -4.2 | 0.001 | 6/23 (A498, NCI-H23, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.635×** | -3.6 | 0.009 | 12/23 (LOX-IMVI, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Vilanterol (drug)]] 5 µM |  | 0.851× | -3.5 | 0.014 | 2/23 (LOX-IMVI, SW 900) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.851× | -3.4 | 0.014 | 11/23 (BT-474, CHP-212, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.651×** | -3.4 | 0.016 | 7/23 (HEC-1-A, AN3 CA, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.671×** | -3.2 | 0.034 | 7/23 (BT-474, C32, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3419. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 421 | 0 | 18 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -25.2) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -15.3) |
| [[LOX-IMVI (line)]] | wt | 56.9 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -15.8) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.250× (z -11.0) |
| [[HS-578T (line)]] | alt | 45.2 | 6 | 2 (2 ⚠) | [[Clobetasol propionate (drug)]] 0.5 µM 3.88× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -13.5) ⚠ cell-cycle shift, explains ~71% of this change |
| [[NCI-H460 (line)]] | wt | 7.17 | 7 | 0 | [[Panobinostat (drug)]] 0.05 µM 13.0× (z +12.7) | — |
| [[A498 (line)]] | wt | 26.6 | 0 | 6 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.151× (z -13.4) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.263× (z -9.8) |
| [[NCI-H1573 (line)]] | alt | 10.3 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 14.9× (z +11.2) | [[Selinexor (drug)]] 5 µM 0.217× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 33.3 | 3 (1 ⚠) | 3 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 4.24× (z +11.6) | [[Digitoxin (drug)]] 5 µM 0.158× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.171× (z -10.0) |
| [[SW 900 (line)]] | alt | 68.6 | 1 | 5 (2 ⚠) | [[Clobetasol propionate (drug)]] 0.5 µM 3.59× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.0820× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.276× (z -9.2) |
| [[LoVo (line)]] | wt | 9.01 | 3 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 7.37× (z +13.4) | [[Digitoxin (drug)]] 5 µM 0.0487× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.164× (z -8.6) |
| [[NCI-H1792 (line)]] | alt | 23.6 | 1 | 4 (2 ⚠) | [[Clobetasol propionate (drug)]] 0.05 µM 4.92× (z +8.6) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.124× (z -11.3) |
| [[A-427 (line)]] | wt | 112 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0890× (z -21.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 95.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +12.8) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 17.6× (z +9.6) | — |
| [[CHP-212 (line)]] | wt | 73.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0620× (z -12.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 74.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.279× (z -11.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 17.9 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 5.49× (z +11.8) | — |
| [[AN3 CA (line)]] | alt | 79.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -9.0) ⚠ cell-cycle shift, explains ~71% of this change |
| [[NCI-H2030 (line)]] | alt | 36.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -9.0) ⚠ cell-cycle shift, explains ~71% of this change |
| [[SK-MEL-2 (line)]] | alt | 11.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -12.5) ⚠ cell-cycle shift, explains ~71% of this change |
| [[SW 1271 (line)]] | alt | 54.0 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.0485× (z -10.2) |
| [[A-172 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.52 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.74 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.30 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.53 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.74 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.79 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.85 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.10 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.49 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.89 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.96 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.72 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.87 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.70 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.32 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.70 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.74 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.60 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 8.23 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.21 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.75 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.65 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.17 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.01 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3419), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF175]] | +0.65 | +0.56 / +0.62 | both halves | 1e-05 | **novel candidate** |
| [[DAAM2]] | +0.62 | +0.54 / +0.61 | both halves | 1e-05 | **novel candidate** |
| [[TMEM108]] | +0.62 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[ST6GALNAC3]] | +0.58 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[GAS7]] | +0.56 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[PANTR1]] | +0.55 | +0.55 / +0.54 | both halves | 1e-05 | **novel candidate** |
| [[GNAO1]] | +0.55 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[ELMO1]] | +0.53 | +0.34 / +0.57 | both halves | 1e-04 |  |
| [[SRPX]] | +0.52 | +0.40 / +0.45 | both halves | 5e-05 |  |
| [[EPHA3]] | +0.52 | +0.53 / +0.46 | both halves | 2e-05 |  |
| [[KC6]] | +0.51 | +0.40 / +0.47 | both halves | 4e-05 |  |
| [[JAKMIP2]] | +0.50 | +0.52 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBTB22]] | -0.43 | -0.37 / -0.36 | both halves | 9e-05 |  |
| [[LINC02086]] | -0.43 | -0.38 / -0.35 | both halves | 1e-04 |  |
| [[SHISAL1]] | -0.42 | -0.30 / -0.37 | both halves | 2e-04 |  |
| [[PATJ]] | -0.41 | -0.37 / -0.41 | both halves | 8e-05 |  |
| [[MIR4713HG]] | -0.41 | -0.36 / -0.42 | both halves | 1e-04 |  |
| [[SERPINB9P1]] | -0.40 | -0.39 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 1, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KDM2B-DT]] | B | KDM2B-DT activity raises GHR's level | lines that do not express KDM2B-DT (8) vs lines expressing it (42) | 4.05× lower at baseline in the lines without KDM2B-DT | 0.066 | ⚠ within organs, on part of the lines; also absent: KATNAL2, TMEM170B, LHFPL6; maybe low, not absent |
| [[POU3F3]] | C | POU3F3 activity raises GHR's level | lines that do not express POU3F3 (34) vs lines expressing it (16) | 4.93× lower at baseline in the lines without POU3F3 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PANTR1, EPGN, ENSG00000244468; co-absent with the target |
| [[ATRNL1]] | C | ATRNL1 activity raises GHR's level | lines that do not express ATRNL1 (21) vs lines expressing it (29) | 3.12× lower at baseline in the lines without ATRNL1 | 0.046 | ⚠ within organs, on part of the lines; also absent: CAMK4, BVES, NEGR1; maybe low, not absent; co-absent with the target |
| [[ST6GALNAC3]] | C | ST6GALNAC3 activity raises GHR's level | lines that do not express ST6GALNAC3 (18) vs lines expressing it (32) | 3.88× lower at baseline in the lines without ST6GALNAC3 | 0.068 | ⚠ within organs, on part of the lines; also absent: TRIM9, GHR, OSBPL6; maybe low, not absent; co-absent with the target |
| [[CAMK4]] | C | CAMK4 activity raises GHR's level | lines that do not express CAMK4 (21) vs lines expressing it (29) | 3.57× lower at baseline in the lines without CAMK4 | 0.069 | ⚠ within organs, on part of the lines; also absent: SNAP25, PRR16, ADAM12; co-absent with the target |
| [[PANTR1]] | C | PANTR1 activity raises GHR's level | lines that do not express PANTR1 (37) vs lines expressing it (13) | 3.36× lower at baseline in the lines without PANTR1 | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: POU3F3, LINC01508, TIMD4; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RORA]] | B | GHR activity raises RORA's level | lines that do not express GHR (24) vs lines expressing it (26) | 1.97× lower at baseline in the lines without GHR | 0.058 | ⚠ within organs, on part of the lines; also absent: FAP, LHX2, ADCY1 |
| [[ATRNL1]] | C | GHR activity raises ATRNL1's level | lines that do not express GHR (24) vs lines expressing it (26) | 2.98× lower at baseline in the lines without GHR | 0.057 | ⚠ within organs, on part of the lines; also absent: FAP, LHX2, ADCY1; co-absent with the target |
| [[ST6GALNAC3]] | C | GHR activity raises ST6GALNAC3's level | lines that do not express GHR (24) vs lines expressing it (26) | 3.11× lower at baseline in the lines without GHR | 0.084 | ⚠ within organs, on part of the lines; also absent: FAP, LHX2, ADCY1; co-absent with the target |

## Where it sits

- **Module**: [[Module 104]] — Molecules associated with elastic fibres; 44 genes; every member is in the + arm (projection on the module's main direction 0.487). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (52.9, 25.0); signed map (25.7, 38.9). **Vector** length 89.0, 26.0% of its response variance represented; |z| ≥ 3 in 828 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.4 | +17.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.2 | +14.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.7 | +16.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +4.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +3.4 | +3.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.0 | +7.4 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +2.4 | +2.7 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +2.3 | +4.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.0 | +4.2 |
| fall | [[Digitoxin (drug)]] 0.05 µM |  | -2.9 | -6.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.4 | -1.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -2.4 | -3.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.0 | -4.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.9 | -0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | +0.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.7 | -6.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.4 | +1.7 |

## What is on record

|  |  |
|---|---|
| Name | growth hormone receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p13.1-p12 — chr5:42,423,439-42,721,878 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GHBP |
| Gene groups (HGNC) | Fibronectin type III domain containing |
| Reactome | 3 pathways, smallest: Prolactin receptor signaling; Growth hormone receptor signaling; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

**Function**, from UniProt [P10912](https://www.uniprot.org/uniprotkb/P10912) (Growth hormone receptor):

> Receptor for pituitary gland growth hormone (GH1) involved in regulating postnatal body growth. On ligand binding, couples to the JAK2/STAT5 pathway.; [Growth hormone-binding protein]: The soluble form (GHBP) acts as a reservoir of growth hormone in plasma and may be a modulator/inhibitor of GH signaling.; [Isoform 2]: Up-regulates the production of the soluble Growth hormone-binding protein form (GHBP) and acts as a negative inhibitor of growth hormone signaling.

**Summary**, from NCBI Gene [2690](https://www.ncbi.nlm.nih.gov/gene/2690):

> This gene encodes a member of the type I cytokine receptor family, which is a transmembrane receptor for growth hormone. Binding of growth hormone to the receptor leads to receptor dimerization and the activation of an intra- and intercellular signal transduction pathway leading to growth. Mutations in this gene have been associated with Laron syndrome, also known as the growth hormone insensitivity syndrome (GHIS), a disorder characterized by short stature. In humans and rabbits, but not …

**Accessions** — [HGNC:4263](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4263) · Entrez [2690](https://www.ncbi.nlm.nih.gov/gene/2690) · UniProt [P10912](https://www.uniprot.org/uniprotkb/P10912) · Ensembl [ENSG00000112964](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112964)

## Data

Gene col 3419: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3419); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3419, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3419]; `tensor/DDL_lfc|DDL_z.npy` [3419]; `embed/gene_vectors.npy` [3419]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3419 or target_col == 3419). Every well: [[GHR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GHR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
