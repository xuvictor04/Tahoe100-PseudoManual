---
symbol: "GTF2I"
type: "gene"
col: 15399
ensembl_id: "ENSG00000263001"
name: "general transcription factor IIi"
location: "7q11.23"
module: 29
arm: "+"
pooled_cpm: 104.02
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 19
n_dd_up_clean: 2
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# GTF2I

*general transcription factor IIi* — 7q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.27× (z +5.7, q 7e-06, up in 26 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 2.14×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.214× (z -36.4, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PAXBP1]] (+0.67, fdr 1e-05), [[LUC7L2]] (+0.64, fdr 1e-05), [[CASD1]] (+0.62, fdr 1e-05); moves opposite to [[CSGALNACT2]] (-0.62, fdr 1e-05), [[N4BP3]] (-0.60, fdr 1e-05), [[ARG2]] (-0.59, fdr 2e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[UPP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15399.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 2.14×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.27×** | +5.7 | 7e-06 | 26/48 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.13× | +4.2 | 0.007 | 7/48 (HS-578T, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.1 | 0.008 | 19/48 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 1.17× | +3.8 | 0.017 | 17/48 (Hs 766T, Panc 03.27, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.19× | +3.8 | 0.017 | 18/48 (NCI-H1573, AsPC-1, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.18× | +3.7 | 0.017 | 19/47 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.12× | +3.7 | 0.017 | 10/48 (PANC-1, HEC-1-A, …) | all doses, flat |  |
| [[NG25 (drug)]] 5 µM |  | **1.31×** | +3.3 | 0.064 | 15/47 (HepG2/C3A, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.3 | 0.064 | 18/48 (SW480, HOP62, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 1.15× | +3.0 | 0.13 | 17/48 (PANC-1, A549, …) | inconsistent across doses |  |
| [[Ixazomib (drug)]] 5 µM |  | 1.27× | +3.0 | 0.13 | 12/48 (A-172, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15399.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.214×** | -36.4 | 0e+00 | 48/48 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.218×** | -36.0 | 0e+00 | 48/48 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.268×** | -31.1 | 0e+00 | 48/48 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.541×** | -20.5 | 0e+00 | 40/48 (C32, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.454×** | -18.7 | 0e+00 | 48/48 (A498, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.569×** | -13.3 | 1e-38 | 43/48 (SW48, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.615×** | -11.5 | 2e-28 | 42/48 (SNU-1, SW48, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.717×** | -11.1 | 1e-26 | 39/48 (PANC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.626×** | -11.1 | 1e-26 | 40/48 (C32, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.660×** | -9.4 | 2e-19 | 36/48 (C32, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.511×** | -8.3 | 6e-15 | 43/49 (MIA PaCa-2, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.722×** | -7.7 | 8e-13 | 37/49 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.762×** | -6.4 | 6e-09 | 30/48 (NCI-H1573, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.796×** | -5.4 | 3e-06 | 27/48 (NCI-H23, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.726×** | -4.0 | 0.003 | 21/45 (SK-MEL-2, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.861× | -3.5 | 0.013 | 16/47 (COLO 205, PANC-1, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15399. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 248 | 0 | 15 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -28.0) |
| [[MIA PaCa-2 (line)]] | alt | 206 | 0 | 14 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0782× (z -39.4) |
| [[LOX-IMVI (line)]] | wt | 78.9 | 0 | 9 | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -23.8) |
| [[SW48 (line)]] | wt | 252 | 0 | 9 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.113× (z -24.6) |
| [[C-33 A (line)]] | alt | 165 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.210× (z -18.5) |
| [[HT-29 (line)]] | alt | 97.3 | 0 | 8 | — | [[Panobinostat (drug)]] 5 µM 0.208× (z -20.1) |
| [[PANC-1 (line)]] | alt | 113 | 0 | 8 | — | [[Panobinostat (drug)]] 5 µM 0.159× (z -29.1) |
| [[SW480 (line)]] | alt | 132 | 0 | 8 | — | [[Panobinostat (drug)]] 5 µM 0.138× (z -27.6) |
| [[A498 (line)]] | wt | 115 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.192× (z -25.2) |
| [[Panc 03.27 (line)]] | alt | 122 | 0 | 7 | — | [[Panobinostat (drug)]] 0.5 µM 0.201× (z -20.9) |
| [[SK-MEL-2 (line)]] | alt | 109 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.187× (z -20.3) |
| [[SW 900 (line)]] | alt | 125 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.162× (z -19.8) |
| [[SW1417 (line)]] | alt | 129 | 0 | 7 | — | [[Panobinostat (drug)]] 0.5 µM 0.180× (z -24.5) |
| [[AN3 CA (line)]] | alt | 290 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.175× (z -14.7) |
| [[COLO 205 (line)]] | alt | 73.3 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -16.3) |
| [[HEC-1-A (line)]] | alt | 170 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.178× (z -26.4) |
| [[J82 (line)]] | alt | 81.8 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.240× (z -19.0) |
| [[NCI-H2030 (line)]] | alt | 96.0 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -18.4) |
| [[NCI-H23 (line)]] | alt | 79.5 | 0 | 6 | — | [[Belinostat (drug)]] 5 µM 0.236× (z -16.4) |
| [[NCI-H2347 (line)]] | alt | 101 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.222× (z -20.7) |
| [[RKO (line)]] | wt | 89.5 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -17.9) |
| [[A-427 (line)]] | wt | 74.7 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.14× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.240× (z -17.5) |
| [[NCI-H1792 (line)]] | alt | 127 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.210× (z -19.3) |
| [[NCI-H460 (line)]] | wt | 81.4 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.190× (z -18.9) |
| [[A-172 (line)]] | wt | 80.9 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.181× (z -19.9) |
| [[AsPC-1 (line)]] | alt | 64.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -11.8) |
| [[CFPAC-1 (line)]] | alt | 71.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -15.5) |
| [[H4 (line)]] | wt | 101 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.139× (z -16.3) |
| [[HOP62 (line)]] | alt | 68.2 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.226× (z -17.8) |
| [[HS-578T (line)]] | alt | 59.6 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.208× (z -16.2) |
| [[LoVo (line)]] | wt | 85.9 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.340× (z -14.6) |
| [[NCI-H1573 (line)]] | alt | 77.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -13.9) |
| [[RPMI-7951 (line)]] | alt | 80.5 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.270× (z -12.9) |
| [[SNU-1 (line)]] | wt | 130 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.125× (z -19.8) |
| [[SNU-423 (line)]] | alt | 68.0 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.209× (z -17.1) |
| [[A549 (line)]] | wt | 61.7 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.213× (z -17.3) |
| [[BT-474 (line)]] | alt | 139 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.207× (z -17.5) |
| [[CHP-212 (line)]] | wt | 110 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.234× (z -9.3) |
| [[HCT15 (line)]] | alt | 63.3 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.163× (z -13.8) |
| [[HepG2_C3A (line)]] | wt | 70.1 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.168× (z -15.5) |
| [[Hs 766T (line)]] | wt | 80.2 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.219× (z -16.0) |
| [[hTERT-HPNE (line)]] | wt | 49.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -10.8) |
| [[KATO III (line)]] | alt | 135 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.171× (z -20.9) |
| [[LS 180 (line)]] | wt | 85.9 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.322× (z -14.2) |
| [[SHP-77 (line)]] | alt | 53.4 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.207× (z -14.7) |
| [[SW 1088 (line)]] | alt | 99.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0361× (z -12.5) |
| [[SW 1271 (line)]] | alt | 96.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.135× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2122 (line)]] | alt | 94.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 105 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15399), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*47 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAXBP1]] | +0.67 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[LUC7L2]] | +0.64 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[CASD1]] | +0.62 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[MFSD14A]] | +0.60 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[RAF1]] | +0.60 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[ARID1B]] | +0.59 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[TDRD3]] | +0.58 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[FUCA2]] | +0.58 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[PLBD1]] | +0.58 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[ANP32A]] | +0.58 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[ZNF362]] | +0.58 | +0.40 / +0.51 | both halves | 5e-05 |  |
| [[ZZZ3]] | +0.58 | +0.53 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*53 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSGALNACT2]] | -0.62 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[N4BP3]] | -0.60 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[ARG2]] | -0.59 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[ARID3B]] | -0.59 | -0.36 / -0.51 | both halves | 9e-05 |  |
| [[SMIM29]] | -0.58 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[BCL10]] | -0.57 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[ATOSB]] | -0.56 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[GIPR]] | -0.55 | -0.31 / -0.50 | both halves | 2e-04 |  |
| [[PDE2A]] | -0.55 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[PTPRH]] | -0.55 | -0.36 / -0.45 | both halves | 1e-04 |  |
| [[KBTBD11-OT1-1]] | -0.55 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[MEAK7]] | -0.54 | -0.47 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UPP1]] | B | UPP1 activity raises GTF2I's level | lines that do not express UPP1 (9) vs lines expressing it (41) | 1.17× lower at baseline in the lines without UPP1 | 0.076 | ⚠ within organs, on part of the lines; also absent: ENSG00000230479, PPP1R18, EBI3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.551). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (18.2, -6.1); signed map (29.1, -25.6). **Vector** length 122, 38.5% of its response variance represented; |z| ≥ 3 in 1,367 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.2 | +2.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | +6.0 | -3.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +5.5 | +5.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.3 | +4.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.3 | +3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.6 | +2.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.5 | +3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +4.4 | +3.8 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +4.1 | +3.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.4 | -11.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -7.0 | -7.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.8 | -11.5 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -4.8 | -2.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.4 | -18.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.3 | -6.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -4.3 | -3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.2 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | general transcription factor IIi |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.23 — chr7:74,650,231-74,760,692 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TFII-I, BAP-135, SPIN, BTKAP1, DIWS, IB291; previously WBSCR6 |
| Gene groups (HGNC) | General transcription factors |
| Matched by | ensembl_id |

**Function**, from UniProt [P78347](https://www.uniprot.org/uniprotkb/P78347) (General transcription factor II-I):

> Interacts with the basal transcription machinery by coordinating the formation of a multiprotein complex at the C-FOS promoter, and linking specific signal responsive activator complexes. Promotes the formation of stable high-order complexes of SRF and PHOX1 and interacts cooperatively with PHOX1 to promote serum-inducible transcription of a reporter gene deriven by the C-FOS serum response element (SRE). Acts as a coregulator for USF1 by binding independently two promoter elements, a …

**Summary**, from NCBI Gene [2969](https://www.ncbi.nlm.nih.gov/gene/2969):

> This gene encodes a phosphoprotein containing six characteristic repeat motifs. The encoded protein binds to the initiator element (Inr) and E-box element in promoters and functions as a regulator of transcription. This locus, along with several other neighboring genes, is deleted in Williams-Beuren syndrome. There are many closely related genes and pseudogenes for this gene on chromosome 7. This gene also has pseudogenes on chromosomes 9, 13, and 21. Alternatively spliced transcript variants …

**Accessions** — [HGNC:4659](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4659) · Entrez [2969](https://www.ncbi.nlm.nih.gov/gene/2969) · UniProt [P78347](https://www.uniprot.org/uniprotkb/P78347) · Ensembl [ENSG00000263001](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000263001)

## Data

Gene col 15399: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15399); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15399, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15399]; `tensor/DDL_lfc|DDL_z.npy` [15399]; `embed/gene_vectors.npy` [15399]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15399 or target_col == 15399). Every well: [[GTF2I — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GTF2I.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
