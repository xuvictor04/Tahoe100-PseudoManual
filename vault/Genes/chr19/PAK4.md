---
symbol: "PAK4"
type: "gene"
col: 5094
ensembl_id: "ENSG00000130669"
name: "p21 (RAC1) activated kinase 4"
location: "19q13.2"
module: 85
arm: "+"
pooled_cpm: 66.51
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 13
n_dd_up_clean: 5
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/085"]
generated_by: "tahoemap"
---

# PAK4

*p21 (RAC1) activated kinase 4* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.11× (z +7.5, q 4e-11, up in 34 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.359× (z -27.9, q 0e+00, down in 48 of 49 measured lines).
> Its strongest partners by |cos| (82 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 18 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FZR1]] (+0.70, fdr 8e-06), [[TNFAIP8L1]] (+0.68, fdr 2e-05), [[CEP131]] (+0.66, fdr 7e-05); moves opposite to [[MCTS1]] (-0.64, fdr 7e-05), [[DGKH]] (-0.63, fdr 2e-05), [[ZNF337-AS1]] (-0.62, fdr 2e-04).
> It sits in the **+** arm of [[Module 085]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5094.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.11×** | +7.5 | 4e-11 | 34/49 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.36×** | +5.9 | 8e-07 | 28/48 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.70×** | +5.3 | 2e-05 | 29/48 (HEC-1-A, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.25×** | +4.3 | 0.002 | 21/48 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.23×** | +3.9 | 0.011 | 22/48 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.22×** | +3.8 | 0.013 | 18/48 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.3 | 0.074 | 14/48 (C32, LS 180, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠; shown: the 15 strongest. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5094.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.359×** | -27.9 | 0e+00 | 48/49 (A549, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.434×** | -15.5 | 0e+00 | 44/48 (HOP62, A549, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.467×** | -14.1 | 6e-43 | 35/41 (BT-474, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.472×** | -13.9 | 7e-42 | 44/49 (HOP62, LS 180, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.512×** | -12.9 | 5e-36 | 39/48 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.563×** | -11.1 | 2e-26 | 38/48 (HT-29, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.557×** | -10.4 | 2e-23 | 34/44 (A549, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.614×** | -9.4 | 4e-19 | 39/48 (HOP62, MIA PaCa-2, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.779×** | -6.8 | 5e-10 | 31/48 (A-427, A549, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.740×** | -5.8 | 3e-07 | 30/48 (NCI-H23, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.743×** | -5.7 | 5e-07 | 27/48 (HOP62, A549, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.799×** | -4.3 | 7e-04 | 25/48 (MIA PaCa-2, LS 180, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.832×** | -3.6 | 0.016 | 19/48 (SW 1271, HS-578T, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 0.834× | -3.5 | 0.017 | 17/48 (CFPAC-1, A549, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~47% of this change | 0.844× | -3.2 | 0.060 | 14/47 (RKO, HT-29, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5094. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 204 | 5 (3 ⚠) | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +17.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.67× (z +14.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -20.5) |
| [[HOP62 (line)]] | alt | 109 | 0 | 9 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.226× (z -24.3) |
| [[A549 (line)]] | wt | 183 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.187× (z -29.2) |
| [[C32 (line)]] | wt | 76.2 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -15.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -15.0) |
| [[SW480 (line)]] | alt | 55.1 | 1 | 6 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.70× (z +9.1) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -13.1) |
| [[HEC-1-A (line)]] | alt | 84.4 | 1 | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.55× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -16.1) |
| [[A-172 (line)]] | wt | 45.4 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -13.8) |
| [[A-427 (line)]] | wt | 51.1 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.173× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.396× (z -13.0) |
| [[HT-29 (line)]] | alt | 73.0 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.267× (z -14.5) |
| [[AsPC-1 (line)]] | alt | 51.3 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.226× (z -20.5) |
| [[H4 (line)]] | wt | 99.9 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -14.3) |
| [[MIA PaCa-2 (line)]] | alt | 64.7 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -14.0) |
| [[SW1417 (line)]] | alt | 53.0 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -11.2) |
| [[CFPAC-1 (line)]] | alt | 57.8 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -17.7) |
| [[COLO 205 (line)]] | alt | 59.8 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -10.6) |
| [[HS-578T (line)]] | alt | 59.3 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.323× (z -14.3) |
| [[LoVo (line)]] | wt | 40.4 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -15.1) |
| [[LS 180 (line)]] | wt | 59.6 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -21.4) |
| [[NCI-H23 (line)]] | alt | 53.9 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -17.3) |
| [[NCI-H2347 (line)]] | alt | 51.1 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -15.8) |
| [[NCI-H460 (line)]] | wt | 39.0 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.243× (z -20.9) |
| [[Panc 03.27 (line)]] | alt | 59.4 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -14.2) |
| [[RKO (line)]] | wt | 38.1 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.162× (z -13.4) ⚠ toxic; cell-cycle shift, explains ~47% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -12.9) |
| [[RPMI-7951 (line)]] | alt | 45.3 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.199× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.335× (z -12.0) |
| [[SNU-423 (line)]] | alt | 33.3 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -11.8) |
| [[SW48 (line)]] | wt | 55.1 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -12.6) |
| [[A498 (line)]] | wt | 62.2 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -14.6) |
| [[AN3 CA (line)]] | alt | 54.6 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.100× (z -11.3) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -9.9) |
| [[HCT15 (line)]] | alt | 62.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.114× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -9.9) |
| [[Hs 766T (line)]] | wt | 36.2 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -12.1) |
| [[hTERT-HPNE (line)]] | wt | 36.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -13.3) |
| [[LOX-IMVI (line)]] | wt | 44.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -12.2) |
| [[NCI-H1792 (line)]] | alt | 40.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.276× (z -11.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 75.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -16.0) |
| [[SW 900 (line)]] | alt | 53.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.216× (z -19.2) |
| [[BT-474 (line)]] | alt | 66.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0359× (z -28.9) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 51.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -13.1) |
| [[HepG2_C3A (line)]] | wt | 29.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -8.7) |
| [[NCI-H1573 (line)]] | alt | 35.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -14.1) |
| [[SHP-77 (line)]] | alt | 66.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -12.4) |
| [[SK-MEL-2 (line)]] | alt | 43.4 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.218× (z -11.9) |
| [[SNU-1 (line)]] | wt | 45.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.234× (z -9.2) |
| [[CHP-212 (line)]] | wt | 43.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 65.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 198 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 46.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5094), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FZR1]] | +0.70 | +0.73 / +0.58 | both halves | 8e-06 |  |
| [[TNFAIP8L1]] | +0.68 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[CEP131]] | +0.66 | +0.72 / +0.38 | both halves | 7e-05 |  |
| [[SUFU]] | +0.66 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[MAST3]] | +0.65 | +0.70 / +0.28 | both halves | 3e-04 |  |
| [[BRAT1]] | +0.65 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[GUSBP18]] | +0.65 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[HDGFL2]] | +0.64 | +0.62 / +0.41 | both halves | 4e-05 |  |
| [[SLC27A1]] | +0.64 | +0.69 / +0.29 | both halves | 2e-04 |  |
| [[MPND]] | +0.61 | +0.51 / +0.30 | both halves | 2e-04 |  |
| [[ALAD]] | +0.60 | +0.36 / +0.40 | both halves | 9e-05 |  |
| [[DOK4]] | +0.59 | +0.51 / +0.36 | both halves | 9e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 16 of them with an alert (⚠; 16 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCTS1]] | -0.64 | -0.67 / -0.38 | both halves | 7e-05 |  |
| [[DGKH]] | -0.63 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[ZNF337-AS1]] | -0.62 | -0.69 / -0.32 | both halves | 2e-04 |  |
| [[EFCAB2]] | -0.58 | -0.60 / -0.25 | both halves | 4e-04 |  |
| [[PKN2-AS1]] | -0.57 | -0.63 / -0.24 | both halves | 5e-04 |  |
| [[MMADHC-DT]] | -0.57 | -0.65 / -0.13 | ⚠ one half (not replicated) | 0.002 |  |
| [[PCBP1-AS1]] | -0.57 | -0.61 / -0.23 | both halves | 5e-04 |  |
| [[CPSF2]] | -0.56 | -0.64 / -0.29 | both halves | 2e-04 |  |
| [[PTPRG]] | -0.56 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[ARRDC3-AS1]] | -0.56 | -0.67 / -0.16 | ⚠ one half (not replicated) | 0.001 |  |
| [[MCPH1]] | -0.56 | -0.57 / -0.24 | both halves | 5e-04 |  |
| [[SLC2A9]] | -0.56 | -0.60 / -0.28 | both halves | 3e-04 |  |
| [[MZF1-AS1]] | -0.56 | -0.63 / -0.24 | both halves | 5e-04 |  |
| [[AVEN]] | -0.55 | -0.53 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PAK4's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.5% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 085]]; 52 genes; this gene is in the **+** arm (projection on the module's main direction 0.698). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (4.0, -2.6); signed map (-33.3, -1.1). **Vector** length 104, 28.8% of its response variance represented; |z| ≥ 3 in 1,141 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +6.4 | -0.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.3 | -0.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.7 | +0.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +4.4 | +1.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~47% of this change | +3.8 | -3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.4 | +1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | -1.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.7 | +1.6 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +2.0 | +0.9 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +2.0 | +1.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.6 | -11.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -7.1 | -15.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.3 | -9.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.2 | -13.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.5 | -5.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.0 | -4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.0 | -6.8 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.4 | -2.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.3 | -5.7 |

## What is on record

|  |  |
|---|---|
| Name | p21 (RAC1) activated kinase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:39,125,770-39,182,816 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | p21 (RAC1) activated kinase family |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING |
| Reactome | 17 pathways, smallest: Activation of RAC1; RHOH GTPase cycle; RHOV GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [O96013](https://www.uniprot.org/uniprotkb/O96013) (Serine/threonine-protein kinase PAK 4):

> Serine/threonine-protein kinase that plays a role in a variety of different signaling pathways including cytoskeleton regulation, cell adhesion turnover, cell migration, growth, proliferation or cell survival. Activation by various effectors including growth factor receptors or active CDC42 and RAC1 results in a conformational change and a subsequent autophosphorylation on several serine and/or threonine residues. Phosphorylates and inactivates the protein phosphatase SSH1, leading to increased …

**Summary**, from NCBI Gene [10298](https://www.ncbi.nlm.nih.gov/gene/10298):

> PAK proteins, a family of serine/threonine p21-activating kinases, include PAK1, PAK2, PAK3 and PAK4. PAK proteins are critical effectors that link Rho GTPases to cytoskeleton reorganization and nuclear signaling. They serve as targets for the small GTP binding proteins Cdc42 and Rac and have been implicated in a wide range of biological activities. PAK4 interacts specifically with the GTP-bound form of Cdc42Hs and weakly activates the JNK family of MAP kinases. PAK4 is a mediator of filopodia …

**Accessions** — [HGNC:16059](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16059) · Entrez [10298](https://www.ncbi.nlm.nih.gov/gene/10298) · UniProt [O96013](https://www.uniprot.org/uniprotkb/O96013) · Ensembl [ENSG00000130669](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130669)

## Data

Gene col 5094: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5094); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5094, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5094]; `tensor/DDL_lfc|DDL_z.npy` [5094]; `embed/gene_vectors.npy` [5094]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5094 or target_col == 5094). Every well: [[PAK4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PAK4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
