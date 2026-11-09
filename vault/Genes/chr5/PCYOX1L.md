---
symbol: "PCYOX1L"
type: "gene"
col: 7036
ensembl_id: "ENSG00000145882"
name: "prenylcysteine oxidase 1 like"
location: "5q32"
module: 6
arm: "+"
pooled_cpm: 4.04
n_lines_expressing: 49
n_dd_up: 19
n_dd_down: 21
n_dd_up_clean: 8
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# PCYOX1L

*prenylcysteine oxidase 1 like* — 5q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.39× (z +11.3, q 7e-27, up in 39 of 46 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 2.15× (z +7.1, q 1e-10, up in 25 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.248× (z -12.9, q 3e-35, down in 35 of 44 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRRC45]] (+0.63, fdr 1e-05), [[SLC37A4]] (+0.61, fdr 1e-05), [[MSH5]] (+0.59, fdr 2e-05); moves opposite to [[ATP6V1G1]] (-0.58, fdr 2e-04), [[FCF1]] (-0.56, fdr 6e-04), [[UBXN4]] (-0.54, fdr 2e-04).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7036.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **3.39×** | +11.3 | 7e-27 | 39/46 (HOP62, A498, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **3.29×** | +11.0 | 9e-26 | 35/44 (HOP62, A498, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.85×** | +9.7 | 7e-20 | 31/46 (HOP62, A498, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.79×** | +9.1 | 1e-17 | 2/5 (A498, HS-578T) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.66×** | +8.7 | 4e-16 | 22/30 (SW480, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.28×** | +7.6 | 3e-12 | 9/17 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.15×** | +7.1 | 1e-10 | 25/46 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.66×** | +6.7 | 2e-09 | 24/45 (HOP62, A-172, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.60×** | +6.1 | 5e-08 | 21/36 (SHP-77, NCI-H460, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | **1.89×** | +5.7 | 8e-07 | 9/19 (KATO III, NCI-H23, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.79×** | +5.4 | 4e-06 | 19/42 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.64×** | +4.7 | 1e-04 | 11/40 (HOP62, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.64×** | +4.6 | 2e-04 | 17/45 (CFPAC-1, HOP62, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.53×** | +4.0 | 0.003 | 10/36 (RPMI-7951, A-172, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.56×** | +4.0 | 0.003 | 10/37 (KATO III, SW480, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.39×** | +3.1 | 0.070 | 6/43 (LOX-IMVI, NCI-H460, …) | all doses, flat |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.86×** | +3.0 | 0.086 | 1/18 (NCI-H460) | top dose only | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.37×** | +2.9 | 0.099 | 2/46 (NCI-H460, SW 900) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7036.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.248×** | -12.9 | 3e-35 | 35/44 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.439×** | -10.8 | 1e-24 | 30/38 (PANC-1, A-172, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.314×** | -10.7 | 2e-24 | 34/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.351×** | -9.7 | 6e-20 | 21/28 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.401×** | -8.1 | 5e-14 | 27/42 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.459×** | -7.2 | 6e-11 | 27/43 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.481×** | -6.8 | 1e-09 | 24/45 (PANC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.540×** | -5.7 | 8e-07 | 21/43 (SK-MEL-2, NCI-H23, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.347×** | -5.1 | 2e-05 | 18/32 (HOP62, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.561×** | -5.0 | 3e-05 | 18/41 (A498, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.621×** | -4.4 | 6e-04 | 13/34 (PANC-1, HEC-1-A, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.411×** | -4.3 | 8e-04 | 15/42 (PANC-1, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.631×** | -4.2 | 9e-04 | 16/42 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.643×** | -4.1 | 0.002 | 16/46 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.756×** | -3.6 | 0.010 | 15/44 (hTERT-HPNE, NCI-H23, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.669×** | -3.6 | 0.013 | 11/45 (RPMI-7951, MIA PaCa-2, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.595×** | -3.4 | 0.020 | 7/44 (NCI-H460, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.698×** | -3.3 | 0.028 | 8/46 (AN3 CA, SW480, …) | two highest doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.74 per unit of S-phase module lfc, -0.55 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7036. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 9.29 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0779× (z -21.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0881× (z -14.1) |
| [[A-427 (line)]] | wt | 12.1 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.133× (z -10.6) |
| [[A498 (line)]] | wt | 3.18 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0943× (z -12.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.0868× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 8.14 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -10.7) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H460 (line)]] | wt | 4.02 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0833× (z -10.2) |
| [[SK-MEL-2 (line)]] | alt | 7.64 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0615× (z -10.4) |
| [[SW1417 (line)]] | alt | 4.15 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0462× (z -10.4) |
| [[SW480 (line)]] | alt | 4.35 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0490× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0541× (z -13.9) |
| [[A-172 (line)]] | wt | 6.28 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0444× (z -16.4) ⚠ cell-cycle shift, explains ~31% of this change |
| [[BT-474 (line)]] | alt | 3.82 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0559× (z -11.3) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HOP62 (line)]] | alt | 5.42 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -12.0) ⚠ cell-cycle shift, explains ~31% of this change |
| [[KATO III (line)]] | alt | 4.15 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0791× (z -8.8) |
| [[LS 180 (line)]] | wt | 5.14 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0640× (z -9.5) |
| [[A549 (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.687 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.38 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.07 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.82 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7036), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC45]] | +0.63 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[SLC37A4]] | +0.61 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[MSH5]] | +0.59 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[TKFC]] | +0.59 | +0.71 / +0.46 | both halves | 3e-05 |  |
| [[GVQW3]] | +0.58 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[GNAZ]] | +0.57 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[CELSR2]] | +0.57 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[HYAL2]] | +0.57 | +0.38 / +0.55 | both halves | 6e-05 |  |
| [[LRRC20]] | +0.57 | +0.38 / +0.59 | both halves | 6e-05 |  |
| [[TCF19]] | +0.57 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[GLB1L2]] | +0.56 | +0.40 / +0.53 | both halves | 5e-05 |  |
| [[PODXL2]] | +0.56 | +0.44 / +0.49 | both halves | 3e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP6V1G1]] | -0.58 | -0.29 / -0.59 | both halves | 2e-04 |  |
| [[FCF1]] | -0.56 | -0.22 / -0.57 | both halves | 6e-04 |  |
| [[UBXN4]] | -0.54 | -0.32 / -0.58 | both halves | 2e-04 |  |
| [[SNRNP27]] | -0.54 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[CXCL13]] | -0.53 | -0.29 / -0.42 | both halves | 3e-04 |  |
| [[CELF6]] | -0.52 | -0.19 / -0.43 | ⚠ not reproduced | 8e-04 |  |
| [[GRK7]] | -0.50 | -0.36 / -0.38 | both halves | 9e-05 |  |
| [[ARHGAP5]] | -0.50 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[N4BP2L2]] | -0.49 | -0.26 / -0.52 | both halves | 3e-04 |  |
| [[MAFG]] | -0.49 | -0.28 / -0.46 | both halves | 3e-04 |  |
| [[ZNF271P]] | -0.49 | -0.24 / -0.43 | both halves | 5e-04 |  |
| [[RNF103-CHMP3]] | -0.49 | -0.24 / -0.43 | both halves | 4e-04 |  |
| [[PIN4]] | -0.49 | -0.20 / -0.43 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PCYOX1L's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[PODXL2]] | B | PODXL2 activity raises PCYOX1L's level | lines that do not express PODXL2 (14) vs lines expressing it (36) | 1.55× lower at baseline in the lines without PODXL2 | 0.089 | ⚠ within organs, on part of the lines |
| [[JMJD8]] | C | JMJD8 activity lowers PCYOX1L's level | lines that do not express JMJD8 (3) vs lines expressing it (47) | 1.96× higher at baseline in the lines without JMJD8 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PIM2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.463). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-27.2, -43.6); signed map (-34.0, -38.4). **Vector** length 54.1, 7.45% of its response variance represented; |z| ≥ 3 in 1,239 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +2.3 | +11.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +6.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +2.1 | +9.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +2.1 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | +2.1 | +3.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +2.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.3 | +1.9 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.0 | +2.2 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.0 | +3.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -4.7 | -10.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.0 | -5.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.7 | -8.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -3.3 | -4.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.5 | -5.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -3.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -1.1 | -1.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.1 | -2.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 5 µM |  | -1.0 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | prenylcysteine oxidase 1 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q32 — chr5:149,358,037-149,369,653 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC3265 |
| Gene groups (HGNC) | Flavoproteins; Prenylcysteine oxidase family |
| Reactome | 4 pathways, smallest: Platelet degranulation; Response to elevated platelet cytosolic Ca2+; Platelet activation, signaling and aggregation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NBM8](https://www.uniprot.org/uniprotkb/Q8NBM8) (Prenylcysteine oxidase 1-like):

> Prenylcysteine oxidase that cleaves the thioether bond of prenyl-L-cysteines, such as farnesylcysteine and geranylgeranylcysteine. Does not metabolize shorter prenyl chain compounds (Probable). Required in the mevalonate pathway to regulate prenylation and enhances the bactericidal activity of neutrophils (By similarity). Promotes the assembly of the postsynaptic ion channel ASIC1a (By similarity).

**Summary**, from NCBI Gene [78991](https://www.ncbi.nlm.nih.gov/gene/78991):

> Enables prenylcysteine oxidase activity. Predicted to be involved in neutrophil-mediated killing of bacterium and prenylated protein catabolic process. Located in membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28477](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28477) · Entrez [78991](https://www.ncbi.nlm.nih.gov/gene/78991) · UniProt [Q8NBM8](https://www.uniprot.org/uniprotkb/Q8NBM8) · Ensembl [ENSG00000145882](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145882)

## Data

Gene col 7036: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7036); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7036, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7036]; `tensor/DDL_lfc|DDL_z.npy` [7036]; `embed/gene_vectors.npy` [7036]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7036 or target_col == 7036). Every well: [[PCYOX1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCYOX1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
