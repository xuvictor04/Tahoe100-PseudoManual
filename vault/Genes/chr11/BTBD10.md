---
symbol: "BTBD10"
type: "gene"
col: 7326
ensembl_id: "ENSG00000148925"
name: "BTB domain containing 10"
location: "11p15.3"
module: 101
arm: "+"
pooled_cpm: 107.91
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 15
n_dd_up_clean: 3
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/101"]
generated_by: "tahoemap"
---

# BTBD10

*BTB domain containing 10* — 11p15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 1.87× (z +5.6, q 2e-05, up in 27 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (12 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.415× (z -15.0, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PFDN1]] (+0.57, fdr 2e-05), [[TECPR2]] (+0.55, fdr 2e-04), [[RMND5B]] (+0.54, fdr 4e-05); moves opposite to [[C1QTNF3-AMACR]] (-0.47, fdr 3e-05), [[DVL2]] (-0.45, fdr 3e-05), [[NFIC]] (-0.45, fdr 5e-05).
> It is in [[Module 101]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CXCL13]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7326.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.87×** | +5.6 | 2e-05 | 27/49 (SW480, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.18× | +4.0 | 0.016 | 19/49 (NCI-H1573, HT-29, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.26×** | +3.9 | 0.020 | 24/48 (A498, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.50×** | +3.6 | 0.046 | 27/48 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[NVP-BHG712 (drug)]] 0.05 µM |  | 1.21× | +3.1 | 0.23 | 20/48 (A549, LOX-IMVI, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 1.20× | +3.0 | 0.24 | 17/47 (NCI-H2030, HS-578T, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 12 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7326.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.415×** | -15.0 | 0e+00 | 45/48 (A-427, LoVo, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.489×** | -11.3 | 6e-27 | 36/44 (HEC-1-A, LS 180, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.639×** | -10.8 | 1e-24 | 39/48 (HEC-1-A, LoVo, …) | top dose only | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.539×** | -10.5 | 1e-23 | 43/49 (SNU-1, A549, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.618×** | -7.9 | 4e-13 | 35/43 (NCI-H23, A549, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.632×** | -7.8 | 5e-13 | 34/48 (LS 180, SW1417, …) | rises with dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.622×** | -7.8 | 7e-13 | 36/47 (LoVo, COLO 205, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.690×** | -6.3 | 2e-08 | 29/48 (LS 180, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **0.759×** | -4.7 | 2e-04 | 31/48 (SW 1271, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.787×** | -4.1 | 0.002 | 23/48 (LS 180, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **0.813×** | -3.5 | 0.022 | 25/48 (A498, LOX-IMVI, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.808×** | -3.5 | 0.023 | 23/48 (HEC-1-A, LoVo, …) | top dose only | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.829×** | -3.2 | 0.062 | 21/48 (RKO, NCI-H2347, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.702×** | -3.2 | 0.066 | 17/48 (SW1417, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.833×** | -3.1 | 0.069 | 19/48 (AsPC-1, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7326. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 109 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -14.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.241× (z -14.8) |
| [[RKO (line)]] | wt | 184 | 1 | 6 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 5.75× (z +9.9) | [[Dinaciclib (drug)]] 0.05 µM 0.339× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.453× (z -8.6) |
| [[SW480 (line)]] | alt | 109 | 2 | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 6.19× (z +13.3) | [[Auranofin (drug)]] 5 µM 0.378× (z -13.4) |
| [[A549 (line)]] | wt | 216 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.205× (z -16.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 138 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.171× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.359× (z -10.6) |
| [[LOX-IMVI (line)]] | wt | 161 | 3 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.44× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.397× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.430× (z -9.7) |
| [[LS 180 (line)]] | wt | 138 | 2 | 4 (4 ⚠) | [[PH-797804 (drug)]] 5 µM 6.29× (z +11.2) | [[Digitoxin (drug)]] 5 µM 0.254× (z -16.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 122 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.282× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.457× (z -8.9) |
| [[A-427 (line)]] | wt | 99.7 | 1 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.57× (z +9.8) | [[Auranofin (drug)]] 5 µM 0.246× (z -15.3) |
| [[A498 (line)]] | wt | 131 | 3 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.59× (z +13.2) | [[Dinaciclib (drug)]] 0.5 µM 0.542× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 108 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.373× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.378× (z -10.8) |
| [[SW48 (line)]] | wt | 91.8 | 0 | 4 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.224× (z -10.8) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.268× (z -9.9) |
| [[A-172 (line)]] | wt | 157 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.322× (z -13.1) |
| [[AsPC-1 (line)]] | alt | 229 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.232× (z -15.9) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 166 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.269× (z -11.0) |
| [[Hs 766T (line)]] | wt | 163 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -13.0) ⚠ cell-cycle shift, explains ~33% of this change |
| [[HS-578T (line)]] | alt | 82.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -14.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.462× (z -9.0) |
| [[J82 (line)]] | alt | 131 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -10.9) ⚠ cell-cycle shift, explains ~33% of this change |
| [[NCI-H23 (line)]] | alt | 105 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.133× (z -19.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.259× (z -13.9) |
| [[C32 (line)]] | wt | 71.1 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.198× (z -14.1) |
| [[COLO 205 (line)]] | alt | 93.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -12.3) ⚠ cell-cycle shift, explains ~33% of this change |
| [[HOP62 (line)]] | alt | 80.1 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.263× (z -13.8) |
| [[HT-29 (line)]] | alt | 110 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.311× (z -13.1) |
| [[hTERT-HPNE (line)]] | wt | 65.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.201× (z -12.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 91.2 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 5.24× (z +9.0) | [[Auranofin (drug)]] 5 µM 0.386× (z -9.9) |
| [[NCI-H1792 (line)]] | alt | 94.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.503× (z -10.0) ⚠ cell-cycle shift, explains ~33% of this change |
| [[NCI-H2347 (line)]] | alt | 89.0 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -9.6) ⚠ cell-cycle shift, explains ~4% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.339× (z -9.5) |
| [[Panc 03.27 (line)]] | alt | 126 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.374× (z -10.9) |
| [[SK-MEL-2 (line)]] | alt | 75.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.326× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.359× (z -10.0) |
| [[SNU-1 (line)]] | wt | 112 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0792× (z -21.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 91.6 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.236× (z -13.8) |
| [[AN3 CA (line)]] | alt | 72.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.116× (z -12.1) |
| [[BT-474 (line)]] | alt | 79.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.230× (z -13.0) |
| [[C-33 A (line)]] | alt | 68.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.286× (z -11.6) |
| [[HCT15 (line)]] | alt | 101 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.258× (z -11.8) |
| [[KATO III (line)]] | alt | 55.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.359× (z -10.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 59.8 | 1 | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 2.00× (z +9.8) | — |
| [[NCI-H2030 (line)]] | alt | 69.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.405× (z -9.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 111 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.637× (z -8.5) ⚠ cell-cycle shift, explains ~33% of this change |
| [[SHP-77 (line)]] | alt | 40.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.228× (z -12.7) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 152 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0863× (z -13.0) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 47.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -8.5) ⚠ cell-cycle shift, explains ~33% of this change |
| [[CFPAC-1 (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 67.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 92.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 95.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 61.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 90.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7326), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PFDN1]] | +0.57 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[TECPR2]] | +0.55 | +0.31 / +0.58 | both halves | 2e-04 |  |
| [[RMND5B]] | +0.54 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[TEP1]] | +0.53 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[ZNF7]] | +0.53 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[RALGAPB]] | +0.52 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[RNF34]] | +0.51 | +0.39 / +0.52 | both halves | 5e-05 |  |
| [[TNFAIP1]] | +0.51 | +0.50 / +0.50 | both halves | 1e-05 | same gene group; STRING 650 |
| [[MAST4]] | +0.49 | +0.39 / +0.54 | both halves | 5e-05 |  |
| [[BCLAF3]] | +0.49 | +0.49 / +0.49 | both halves | 2e-05 |  |
| [[ARHGAP29]] | +0.49 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[ITGA2-AS1]] | +0.49 | +0.36 / +0.51 | both halves | 9e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C1QTNF3-AMACR]] | -0.47 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[DVL2]] | -0.45 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[NFIC]] | -0.45 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[MTSS2]] | -0.44 | -0.46 / -0.32 | both halves | 1e-04 |  |
| [[NFIX]] | -0.44 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[RHOBTB3]] | -0.44 | -0.46 / -0.39 | both halves | 6e-05 | same gene group |
| [[KLRG1]] | -0.43 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[MIR23AHG]] | -0.42 | -0.41 / -0.37 | both halves | 9e-05 |  |
| [[MLLT6]] | -0.42 | -0.51 / -0.28 | both halves | 3e-04 |  |
| [[BCO2]] | -0.41 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[OSR2]] | -0.41 | -0.51 / -0.32 | both halves | 2e-04 |  |
| [[RHOXF1]] | -0.41 | -0.31 / -0.40 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CXCL13]] | B | CXCL13 activity lowers BTBD10's level | lines that do not express CXCL13 (8) vs lines expressing it (42) | 1.76× higher at baseline in the lines without CXCL13 | 0.004 | ⚠ within organs, on part of the lines; also absent: DNAH2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 101]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.390). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-21.7, 35.1); signed map (-3.0, 31.9). **Vector** length 125, 40.6% of its response variance represented; |z| ≥ 3 in 1,218 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +6.5 | +3.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.8 | +4.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.4 | +2.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.4 | +1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.2 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.2 | +1.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.5 | +2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +4.4 | +2.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -9.3 | -15.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.8 | -7.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -5.7 | -10.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.1 | -7.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -4.7 | -6.3 |
|  | [[Afatinib (drug)]] 5 µM |  | -3.3 | -2.2 |
|  | [[Gefitinib (drug)]] 5 µM |  | -3.1 | -2.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.8 | -3.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.8 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | BTB domain containing 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.3 — chr11:13,388,008-13,463,297 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GMRP1, GMRP-1, MGC13007 |
| Gene groups (HGNC) | BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BSF8](https://www.uniprot.org/uniprotkb/Q9BSF8) (BTB/POZ domain-containing protein 10):

> Plays a major role as an activator of AKT family members by inhibiting PPP2CA-mediated dephosphorylation, thereby keeping AKTs activated. Plays a role in preventing motor neuronal death and accelerating the growth of pancreatic beta cells.

**Summary**, from NCBI Gene [84280](https://www.ncbi.nlm.nih.gov/gene/84280):

> Predicted to be involved in positive regulation of phosphatidylinositol 3-kinase/protein kinase B signal transduction and type B pancreatic cell proliferation. Located in fibrillar center and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21445](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21445) · Entrez [84280](https://www.ncbi.nlm.nih.gov/gene/84280) · UniProt [Q9BSF8](https://www.uniprot.org/uniprotkb/Q9BSF8) · Ensembl [ENSG00000148925](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148925)

## Data

Gene col 7326: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7326); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7326, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7326]; `tensor/DDL_lfc|DDL_z.npy` [7326]; `embed/gene_vectors.npy` [7326]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7326 or target_col == 7326). Every well: [[BTBD10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BTBD10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
