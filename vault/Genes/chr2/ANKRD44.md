---
symbol: "ANKRD44"
type: "gene"
col: 785
ensembl_id: "ENSG00000065413"
name: "ankyrin repeat domain 44"
location: "2q33.1"
module: 193
arm: "+"
pooled_cpm: 43.08
n_lines_expressing: 44
n_dd_up: 14
n_dd_down: 27
n_dd_up_clean: 13
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/193"]
generated_by: "tahoemap"
---

# ANKRD44

*ankyrin repeat domain 44* — 2q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.54× (z +11.3, q 7e-27, up in 31 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.543× (z -11.3, q 6e-27, down in 35 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDH4]] (+0.57, fdr 1e-05), [[FHOD3]] (+0.53, fdr 4e-05), [[CHN1]] (+0.53, fdr 2e-05); moves opposite to [[NADSYN1]] (-0.52, fdr 4e-05), [[SYNRG]] (-0.50, fdr 3e-05), [[FANK1]] (-0.46, fdr 1e-04).
> It is in [[Module 193]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[BNC2]] → it (grade B ⚠); 3 go from it, the strongest it → [[CEP78]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 785.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.54×** | +11.3 | 7e-27 | 31/42 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.61×** | +8.9 | 1e-16 | 30/42 (NCI-H1573, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.59×** | +8.7 | 7e-16 | 31/42 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.87×** | +6.1 | 2e-07 | 20/42 (LoVo, RKO, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.38×** | +5.5 | 5e-06 | 16/41 (SW480, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.23×** | +3.9 | 0.008 | 15/42 (C32, SW48, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.23×** | +3.9 | 0.008 | 14/41 (A498, NCI-H1573, …) | all doses, flat |  |
| [[Bentamapimod (drug)]] 0.05 µM |  | **1.24×** | +3.9 | 0.008 | 6/41 (NCI-H1573, SNU-423, …) | inconsistent across doses |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.21×** | +3.6 | 0.020 | 7/42 (HCT15, A549, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.020 | 12/41 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.21×** | +3.3 | 0.051 | 14/38 (Hs 766T, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Bentamapimod (drug)]] 5 µM |  | **1.40×** | +3.2 | 0.055 | 7/42 (PANC-1, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.18× | +3.2 | 0.065 | 4/42 (A549, C-33 A, …) | two highest doses |  |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.1 | 0.065 | 8/42 (SK-MEL-2, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 0.5 µM |  | **1.26×** | +3.1 | 0.065 | 4/42 (RPMI-7951, Panc 03.27, …) | rises with dose | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | 1.18× | +3.1 | 0.065 | 10/42 (C32, NCI-H1573, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.37×** | +3.1 | 0.065 | 7/42 (HS-578T, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.065 | 10/42 (NCI-H1573, A498, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 785.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.543×** | -11.3 | 6e-27 | 35/42 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.645×** | -8.1 | 1e-13 | 29/42 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.648×** | -8.0 | 2e-13 | 27/42 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.445×** | -7.8 | 7e-13 | 26/43 (A498, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.685×** | -7.0 | 3e-10 | 25/41 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.690×** | -6.6 | 4e-09 | 23/41 (A-427, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.704×** | -6.5 | 8e-09 | 22/42 (NCI-H460, HEC-1-A, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.703×** | -6.1 | 6e-08 | 23/42 (NCI-H460, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.721×** | -6.0 | 9e-08 | 20/42 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.732×** | -5.8 | 5e-07 | 19/41 (HEC-1-A, LOX-IMVI, …) | two highest doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.556×** | -5.7 | 7e-07 | 18/42 (NCI-H460, A498, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.745×** | -5.4 | 3e-06 | 21/42 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **0.752×** | -5.3 | 6e-06 | 20/40 (PANC-1, SK-MEL-2, …) | inconsistent across doses | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **0.581×** | -5.3 | 6e-06 | 22/41 (SK-MEL-2, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.590×** | -5.1 | 1e-05 | 18/41 (HEC-1-A, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.759×** | -4.9 | 4e-05 | 21/42 (HEC-1-A, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.641×** | -4.3 | 5e-04 | 13/42 (NCI-H1792, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.794×** | -4.3 | 6e-04 | 21/42 (SHP-77, RKO, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.654×** | -4.1 | 0.001 | 16/42 (Panc 03.27, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 785. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 121 | 0 | 14 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.238× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.294× (z -11.8) |
| [[HEC-1-A (line)]] | alt | 51.9 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -16.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.245× (z -13.0) |
| [[NCI-H2030 (line)]] | alt | 125 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -20.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.359× (z -10.5) |
| [[A498 (line)]] | wt | 102 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -16.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.163× (z -10.5) |
| [[NCI-H1792 (line)]] | alt | 41.2 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.179× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.331× (z -8.7) |
| [[PANC-1 (line)]] | alt | 68.7 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -12.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.410× (z -9.6) |
| [[SK-MEL-2 (line)]] | alt | 70.4 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -11.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -9.1) |
| [[C-33 A (line)]] | alt | 95.0 | 0 | 3 (3 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.172× (z -11.4) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 37.8 | 1 | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.22× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -12.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 74.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -11.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.362× (z -9.4) |
| [[C32 (line)]] | wt | 137 | 2 | 0 | [[Tofacitinib (drug)]] 5 µM 2.19× (z +8.9) | — |
| [[SHP-77 (line)]] | alt | 112 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.312× (z -10.0) |
| [[A-172 (line)]] | wt | 35.5 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.322× (z -8.9) |
| [[A-427 (line)]] | wt | 34.3 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.207× (z -11.9) |
| [[A549 (line)]] | wt | 42.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -14.7) ⚠ cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 30.9 | 0 | 1 | — | [[Pemetrexed (drug)]] 5 µM 0.0976× (z -8.7) |
| [[H4 (line)]] | wt | 18.7 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0968× (z -9.1) |
| [[HS-578T (line)]] | alt | 40.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 47.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.324× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 25.3 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.07× (z +8.5) | — |
| [[LOX-IMVI (line)]] | wt | 27.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.230× (z -10.9) ⚠ cell-cycle shift, explains ~24% of this change |
| [[NCI-H2347 (line)]] | alt | 12.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +9.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SNU-1 (line)]] | wt | 41.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.236× (z -8.5) |
| [[SW 1271 (line)]] | alt | 52.7 | 0 | 1 | — | [[Esmolol (hydrochloride) (drug)]] 0.5 µM 0.0769× (z -8.5) |
| [[SW48 (line)]] | wt | 33.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.201× (z -8.8) ⚠ cell-cycle shift, explains ~24% of this change |
| [[SW480 (line)]] | alt | 16.6 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.24× (z +8.7) | — |
| [[AsPC-1 (line)]] | alt | 5.58 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 10.4 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 40.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.58 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.18 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.81 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.73 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 785), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDH4]] | +0.57 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[FHOD3]] | +0.53 | +0.64 / +0.41 | both halves | 4e-05 |  |
| [[CHN1]] | +0.53 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[DOCK4]] | +0.51 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[CNKSR2]] | +0.50 | +0.40 / +0.50 | both halves | 5e-05 |  |
| [[FAM124A]] | +0.50 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[NIN]] | +0.48 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[LYPD6]] | +0.48 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[COL4A4]] | +0.48 | +0.41 / +0.44 | both halves | 4e-05 |  |
| [[NRG2]] | +0.48 | +0.52 / +0.43 | both halves | 3e-05 |  |
| [[RADIL]] | +0.48 | +0.41 / +0.45 | both halves | 4e-05 |  |
| [[DDAH1]] | +0.47 | +0.42 / +0.44 | both halves | 4e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NADSYN1]] | -0.52 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[SYNRG]] | -0.50 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[FANK1]] | -0.46 | -0.33 / -0.48 | both halves | 1e-04 | same gene group |
| [[GPALPP1]] | -0.45 | -0.36 / -0.45 | both halves | 1e-04 |  |
| [[RC3H1]] | -0.44 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[EMC3]] | -0.43 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[RBKS]] | -0.43 | -0.33 / -0.43 | both halves | 1e-04 |  |
| [[TTC9C]] | -0.42 | -0.36 / -0.41 | both halves | 1e-04 |  |
| [[LMAN2]] | -0.42 | -0.39 / -0.40 | both halves | 5e-05 |  |
| [[PPP4R3B]] | -0.41 | -0.32 / -0.45 | both halves | 2e-04 |  |
| [[ACOX3]] | -0.41 | -0.40 / -0.41 | both halves | 4e-05 |  |
| [[RABGAP1]] | -0.41 | -0.41 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BNC2]] | B | BNC2 activity raises ANKRD44's level | lines that do not express BNC2 (21) vs lines expressing it (29) | 2.00× lower at baseline in the lines without BNC2 | 0.085 | ⚠ within organs, on part of the lines; also absent: LINC03041, DPY19L2, RNF182 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CEP78]] | B | ANKRD44 activity raises CEP78's level | lines that do not express ANKRD44 (6) vs lines expressing it (44) | 1.76× lower at baseline in the lines without ANKRD44 | 0.030 | ⚠ within organs, on part of the lines; also absent: ENSG00000236230, TBC1D19, SSBP2; maybe low, not absent |
| [[AKT3]] | B | ANKRD44 activity raises AKT3's level | lines that do not express ANKRD44 (6) vs lines expressing it (44) | 8.26× lower at baseline in the lines without ANKRD44 | 0.053 | ⚠ within organs, on part of the lines; also absent: ENSG00000236230, TBC1D19, SSBP2; maybe low, not absent |
| [[SSX2IP]] | B | ANKRD44 activity raises SSX2IP's level | lines that do not express ANKRD44 (6) vs lines expressing it (44) | 1.89× lower at baseline in the lines without ANKRD44 | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000236230, TBC1D19, SSBP2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 193]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.607). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (41.0, 9.2); signed map (1.7, 56.3). **Vector** length 102, 25.0% of its response variance represented; |z| ≥ 3 in 1,252 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.5 | +11.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.2 | +8.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.3 | +8.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.4 | +6.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | +3.1 | -3.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.5 | +2.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.3 | +2.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.0 | +3.6 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -2.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | -2.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.6 | -5.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.6 | -5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | -1.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.1 | -1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat domain 44 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.1 — chr2:196,967,017-197,311,173 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PP6-ARS-B |
| Gene groups (HGNC) | Ankyrin repeat domain containing; Protein phosphatase 6 regulatory subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N8A2](https://www.uniprot.org/uniprotkb/Q8N8A2) (Serine/threonine-protein phosphatase 6 regulatory ankyrin repeat subunit B):

> Putative regulatory subunit of protein phosphatase 6 (PP6) that may be involved in the recognition of phosphoprotein substrates.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:25259](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25259) · Entrez [91526](https://www.ncbi.nlm.nih.gov/gene/91526) · UniProt [Q8N8A2](https://www.uniprot.org/uniprotkb/Q8N8A2) · Ensembl [ENSG00000065413](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000065413)

## Data

Gene col 785: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 785); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 785, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 785]; `tensor/DDL_lfc|DDL_z.npy` [785]; `embed/gene_vectors.npy` [785]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 785 or target_col == 785). Every well: [[ANKRD44 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKRD44.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
