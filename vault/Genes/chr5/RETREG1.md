---
symbol: "RETREG1"
type: "gene"
col: 7778
ensembl_id: "ENSG00000154153"
name: "reticulophagy regulator 1"
location: "5p15.1"
module: 132
arm: "+"
pooled_cpm: 17.7
n_lines_expressing: 38
n_dd_up: 47
n_dd_down: 18
n_dd_up_clean: 41
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 3
tags: ["gene", "module/132"]
generated_by: "tahoemap"
---

# RETREG1

*reticulophagy regulator 1* — 5p15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 47 drug-doses (6 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.60× (z +17.6, q 0e+00, up in 32 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (11 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.416× (z -11.5, q 1e-27, down in 30 of 36 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.438× (z -10.8, q 1e-24, down in 28 of 35 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DOCK3]] (+0.60, fdr 1e-05), [[TMOD2]] (+0.57, fdr 7e-06), [[MCAM]] (+0.57, fdr 4e-05); moves opposite to [[NRP1]] (-0.49, fdr 4e-05), [[ODF2]] (-0.48, fdr 2e-05), [[IKZF4]] (-0.48, fdr 7e-05).
> It is in [[Module 132]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ANKS1B]] → it (grade B ⚠); 3 go from it, the strongest it → [[KIAA0753]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 47 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7778.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.60×** | +17.6 | 0e+00 | 32/35 (SW480, A498, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.89×** | +13.9 | 3e-41 | 27/34 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.80×** | +7.0 | 5e-10 | 19/36 (SW 900, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.53×** | +6.6 | 8e-09 | 18/35 (NCI-H460, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.67×** | +6.5 | 1e-08 | 21/34 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.62×** | +6.0 | 2e-07 | 7/21 (HOP62, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.54×** | +5.6 | 1e-06 | 16/36 (LoVo, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.51×** | +5.4 | 4e-06 | 11/36 (SW 900, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.53×** | +5.4 | 5e-06 | 16/35 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.33×** | +5.3 | 8e-06 | 15/36 (A-172, C-33 A, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.49×** | +5.2 | 8e-06 | 15/34 (C-33 A, A-172, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.47×** | +5.0 | 2e-05 | 11/36 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.46×** | +5.0 | 2e-05 | 14/36 (NCI-H460, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.45×** | +4.9 | 4e-05 | 14/36 (NCI-H460, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.33×** | +4.8 | 5e-05 | 14/36 (LoVo, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **2.02×** | +4.6 | 2e-04 | 8/36 (SW480, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.46×** | +4.5 | 2e-04 | 14/34 (HS-578T, A498, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.40×** | +4.4 | 4e-04 | 12/34 (SW480, A-427, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7778.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.416×** | -11.5 | 1e-27 | 30/36 (LoVo, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.438×** | -10.8 | 1e-24 | 28/35 (NCI-H23, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.512×** | -8.8 | 4e-16 | 24/34 (LoVo, LS 180, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.640×** | -8.2 | 2e-14 | 26/35 (LoVo, NCI-H460, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.552×** | -7.8 | 8e-13 | 25/35 (LoVo, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.677×** | -7.2 | 5e-11 | 25/35 (A-427, LoVo, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.637×** | -5.9 | 3e-07 | 19/35 (C32, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.407×** | -5.8 | 4e-07 | 17/34 (A-427, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.659×** | -5.0 | 4e-05 | 14/36 (NCI-H23, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.697×** | -4.7 | 1e-04 | 15/35 (MIA PaCa-2, LoVo, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.680×** | -4.6 | 2e-04 | 16/35 (LOX-IMVI, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.699×** | -4.5 | 3e-04 | 16/36 (LoVo, MIA PaCa-2, …) | top dose only | composition shift |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.645×** | -4.1 | 0.002 | 11/36 (NCI-H460, LoVo, …) | two highest doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.563×** | -3.7 | 0.008 | 17/36 (A-427, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.751×** | -3.6 | 0.012 | 15/34 (A-427, HEC-1-A, …) | top dose only |  |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | **0.770×** | -3.4 | 0.022 | 4/35 (A549, LS 180, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.603×** | -3.3 | 0.034 | 10/35 (MIA PaCa-2, SK-MEL-2, …) | two highest doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7778. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 58.3 | 0 | 10 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -22.4) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -15.3) |
| [[NCI-H460 (line)]] | wt | 41.1 | 3 | 3 (2 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 5.40× (z +12.2) | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -18.3) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -10.9) |
| [[A-427 (line)]] | wt | 67.3 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0448× (z -27.1) |
| [[AN3 CA (line)]] | alt | 55.2 | 0 | 5 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0686× (z -12.3) ⚠ toxic; cell-cycle shift, explains ~60% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.0939× (z -11.3) |
| [[HEC-1-A (line)]] | alt | 33.5 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -11.9) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.494× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 12.7 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.117× (z -10.9) ⚠ cell-cycle shift, explains ~90% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 35.4 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -11.0) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.271× (z -10.8) |
| [[NCI-H23 (line)]] | alt | 13.8 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0189× (z -20.7) |
| [[C32 (line)]] | wt | 44.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -11.5) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -9.4) |
| [[LOX-IMVI (line)]] | wt | 12.3 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0345× (z -17.1) ⚠ cell-cycle shift, explains ~90% of this change |
| [[LS 180 (line)]] | wt | 37.1 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0978× (z -14.4) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A-172 (line)]] | wt | 66.9 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.218× (z -11.6) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -10.8) |
| [[A549 (line)]] | wt | 14.4 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.168× (z -9.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.186× (z -8.5) |
| [[HS-578T (line)]] | alt | 6.09 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.02× (z +9.2) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 5.88× (z +9.1) | — |
| [[SW480 (line)]] | alt | 11.8 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.57× (z +11.1) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.180× (z -10.7) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A498 (line)]] | wt | 7.04 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.43× (z +9.7) | — |
| [[HCT15 (line)]] | alt | 23.4 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.144× (z -9.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[RKO (line)]] | wt | 5.80 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0676× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 15.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -12.7) ⚠ cell-cycle shift, explains ~60% of this change |
| [[SHP-77 (line)]] | alt | 53.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.221× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.65 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.30 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.81 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.01 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.89 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.65 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.70 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.70 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.89 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.78 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 37.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7778), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DOCK3]] | +0.60 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[TMOD2]] | +0.57 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[MCAM]] | +0.57 | +0.41 / +0.63 | both halves | 4e-05 |  |
| [[NUDT11]] | +0.54 | +0.35 / +0.63 | both halves | 1e-04 |  |
| [[REEP1]] | +0.53 | +0.55 / +0.50 | both halves | 1e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY; STRING 420 |
| [[NFASC]] | +0.52 | +0.35 / +0.51 | both halves | 1e-04 |  |
| [[KRAS]] | +0.52 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[AKAP6]] | +0.52 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[EPHA10]] | +0.52 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[PRKAG2]] | +0.50 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[POU3F3]] | +0.50 | +0.44 / +0.44 | both halves | 3e-05 |  |
| [[KSR2]] | +0.50 | +0.55 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NRP1]] | -0.49 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[ODF2]] | -0.48 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[IKZF4]] | -0.48 | -0.38 / -0.43 | both halves | 7e-05 |  |
| [[PDCD6]] | -0.46 | -0.36 / -0.48 | both halves | 1e-04 |  |
| [[GLE1]] | -0.45 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[P3H1]] | -0.45 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[KIAA0753]] | -0.45 | -0.34 / -0.53 | both halves | 1e-04 |  |
| [[HSPA14]] | -0.45 | -0.32 / -0.43 | both halves | 2e-04 |  |
| [[SUV39H2]] | -0.44 | -0.25 / -0.48 | both halves | 4e-04 |  |
| [[POLE3]] | -0.44 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[NUP133]] | -0.44 | -0.29 / -0.44 | both halves | 2e-04 |  |
| [[SHPK]] | -0.42 | -0.40 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANKS1B]] | B | ANKS1B activity raises RETREG1's level | lines that do not express ANKS1B (18) vs lines expressing it (32) | 2.28× lower at baseline in the lines without ANKS1B | 0.042 | ⚠ within organs, on part of the lines; also absent: LHX2, CECR2, HS6ST3 |
| [[ELAPOR2]] | B | ELAPOR2 activity raises RETREG1's level | lines that do not express ELAPOR2 (17) vs lines expressing it (33) | 2.25× lower at baseline in the lines without ELAPOR2 | 0.079 | ⚠ within organs, on part of the lines; also absent: SCN2A, CACNB2, ENSG00000227681 |
| [[ROR2]] | B | ROR2 activity raises RETREG1's level | lines that do not express ROR2 (25) vs lines expressing it (25) | 1.83× lower at baseline in the lines without ROR2 | 0.099 | ⚠ within organs, on part of the lines; also absent: BEGAIN, OLFM1, HOXD11 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KIAA0753]] | B | RETREG1 activity raises KIAA0753's level | lines that do not express RETREG1 (12) vs lines expressing it (38) | 1.54× lower at baseline in the lines without RETREG1 | 0.005 | ⚠ within organs, on part of the lines; also absent: LINC02269, FILIP1, C19orf81 |
| [[GKAP1]] | B | RETREG1 activity raises GKAP1's level | lines that do not express RETREG1 (12) vs lines expressing it (38) | 1.56× lower at baseline in the lines without RETREG1 | 0.066 | ⚠ within organs, on part of the lines; also absent: LINC02269, FILIP1, C19orf81 |
| [[KIAA0753]] | B | RETREG1 activity strengthens KIAA0753's drug response | lines that do not express RETREG1 (12) vs lines expressing it (37) | the lines without RETREG1 respond 0.67× as strongly (z diff +1.70); strongest at Dinaciclib 0.05 µM: 0.73x vs 0.45x (z diff +3.8) | 0.099 | ⚠ within organs, on part of the lines; also absent: LINC02269, FILIP1, C19orf81; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 132]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.464). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (3.8, 35.2); signed map (29.5, 28.8). **Vector** length 91.6, 21.8% of its response variance represented; |z| ≥ 3 in 1,057 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.8 | +17.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +9.0 | +13.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.9 | +1.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +4.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +6.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.4 | +6.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.3 | +3.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.2 | +4.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.0 | +5.4 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | -3.1 | -4.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.8 | -0.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -1.7 | -3.0 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -1.5 | -1.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.5 | -4.1 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -1.4 | -0.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -0.6 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.4 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | reticulophagy regulator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p15.1 — chr5:16,473,038-16,617,101 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20152, JK1; previously FAM134B |
| Hallmark sets | ESTROGEN_RESPONSE_EARLY |
| Reactome | 4 pathways, smallest: Dengue virus modulates apoptosis; Dengue Virus-Host Interactions; Dengue Virus Infection |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H6L5](https://www.uniprot.org/uniprotkb/Q9H6L5) (Reticulophagy regulator 1):

> Endoplasmic reticulum (ER)-anchored autophagy regulator which mediates ER delivery into lysosomes through sequestration into autophagosomes. Promotes membrane remodeling and ER scission via its membrane bending capacity and targets the fragments into autophagosomes via interaction with ATG8 family proteins. Active under basal conditions. Required for collagen quality control in a LIR motif-dependent manner (By similarity). Required for long-term survival of nociceptive and autonomic ganglion …

**Summary**, from NCBI Gene [54463](https://www.ncbi.nlm.nih.gov/gene/54463):

> The protein encoded by this gene is a cis-Golgi transmembrane protein that may be necessary for the long-term survival of nociceptive and autonomic ganglion neurons. Mutations in this gene are a cause of hereditary sensory and autonomic neuropathy type IIB (HSAN IIB), and this gene may also play a role in susceptibility to vascular dementia. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Nov 2011]

**Accessions** — [HGNC:25964](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25964) · Entrez [54463](https://www.ncbi.nlm.nih.gov/gene/54463) · UniProt [Q9H6L5](https://www.uniprot.org/uniprotkb/Q9H6L5) · Ensembl [ENSG00000154153](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154153)

## Data

Gene col 7778: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7778); `tables/drug_effects.parquet` (65 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7778, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7778]; `tensor/DDL_lfc|DDL_z.npy` [7778]; `embed/gene_vectors.npy` [7778]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7778 or target_col == 7778). Every well: [[RETREG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RETREG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
