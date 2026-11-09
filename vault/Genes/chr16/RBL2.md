---
symbol: "RBL2"
type: "gene"
col: 2369
ensembl_id: "ENSG00000103479"
name: "RB transcriptional corepressor like 2"
location: "16q12.2"
module: 57
arm: "+"
pooled_cpm: 76.74
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 45
n_dd_up_clean: 0
n_dd_down_clean: 34
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# RBL2

*RB transcriptional corepressor like 2* — 16q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.32× (z +7.1, q 8e-10, up in 29 of 49 measured lines) ⚠ toxic; transcription drop.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (HEC-1-A 1.89×, RKO 2.60×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (HEC-1-A 1.85×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 45 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.279× (z -46.0, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LANCL1]] (+0.65, fdr 1e-05), [[MBTPS1]] (+0.62, fdr 1e-05), [[NUDT21]] (+0.62, fdr 1e-05); moves opposite to [[NOP56]] (-0.57, fdr 1e-05), [[CCDC71L]] (-0.56, fdr 2e-05), [[IL12RB2]] (-0.55, fdr 5e-05).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2369.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (HEC-1-A 1.89×, RKO 2.60×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (HEC-1-A 1.85×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.32×** | +7.1 | 8e-10 | 29/49 (HEC-1-A, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.17× | +4.0 | 0.019 | 21/44 (HEC-1-A, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib (drug)]] 5 µM |  | 1.26× | +3.1 | 0.41 | 8/48 (H4, SNU-423, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 57 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 45 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2369.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.279×** | -46.0 | 0e+00 | 47/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.338×** | -27.7 | 0e+00 | 46/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.367×** | -24.5 | 0e+00 | 46/48 (COLO 205, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.442×** | -20.7 | 0e+00 | 47/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.457×** | -19.9 | 0e+00 | 46/48 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.601×** | -18.3 | 0e+00 | 44/49 (HOP62, A-172, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.528×** | -15.9 | 0e+00 | 47/48 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.541×** | -15.6 | 0e+00 | 44/48 (SW480, SNU-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.541×** | -15.6 | 0e+00 | 44/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.592×** | -13.3 | 1e-38 | 44/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.612×** | -12.0 | 2e-31 | 40/47 (NCI-H23, NCI-H460, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.409×** | -11.9 | 6e-31 | 45/49 (SW480, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.627×** | -11.9 | 8e-31 | 41/48 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.655×** | -10.7 | 3e-25 | 38/48 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.748×** | -10.4 | 1e-23 | 39/48 (MIA PaCa-2, LS 180, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.473×** | -10.0 | 8e-22 | 39/48 (SW480, NCI-H2030, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.688×** | -9.5 | 7e-20 | 36/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.674×** | -9.5 | 9e-20 | 37/48 (SK-MEL-2, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2369. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 79.4 | 0 | 17 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -37.7) |
| [[MIA PaCa-2 (line)]] | alt | 115 | 0 | 14 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -32.1) |
| [[SW480 (line)]] | alt | 110 | 0 | 13 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -23.5) |
| [[HOP62 (line)]] | alt | 89.2 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -33.3) |
| [[HS-578T (line)]] | alt | 68.1 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -21.1) |
| [[J82 (line)]] | alt | 62.7 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -24.4) |
| [[LoVo (line)]] | wt | 72.7 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -25.7) |
| [[HEC-1-A (line)]] | alt | 73.2 | 2 (2 ⚠) | 7 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.89× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -18.2) |
| [[hTERT-HPNE (line)]] | wt | 83.0 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -14.2) |
| [[SW 900 (line)]] | alt | 75.8 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -21.5) |
| [[A-172 (line)]] | wt | 78.7 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -17.1) |
| [[A498 (line)]] | wt | 106 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -29.4) |
| [[H4 (line)]] | wt | 107 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -25.0) |
| [[PANC-1 (line)]] | alt | 61.7 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -31.9) |
| [[SK-MEL-2 (line)]] | alt | 70.5 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -21.0) |
| [[SNU-1 (line)]] | wt | 80.5 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -17.2) |
| [[AsPC-1 (line)]] | alt | 60.0 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -27.8) |
| [[CFPAC-1 (line)]] | alt | 55.1 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -23.9) |
| [[LS 180 (line)]] | wt | 75.3 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -21.4) |
| [[SNU-423 (line)]] | alt | 74.2 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -20.5) |
| [[HCT15 (line)]] | alt | 95.7 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -17.0) |
| [[LOX-IMVI (line)]] | wt | 76.9 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -22.0) |
| [[NCI-H1573 (line)]] | alt | 62.6 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -33.7) |
| [[Panc 03.27 (line)]] | alt | 72.7 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -19.9) |
| [[SW1417 (line)]] | alt | 70.1 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.485× (z -12.0) |
| [[A549 (line)]] | wt | 77.2 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -26.8) |
| [[KATO III (line)]] | alt | 108 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -15.6) |
| [[NCI-H1792 (line)]] | alt | 64.7 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -16.6) |
| [[NCI-H23 (line)]] | alt | 73.0 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -20.3) |
| [[RKO (line)]] | wt | 53.7 | 1 (1 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -24.3) |
| [[C32 (line)]] | wt | 58.5 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -14.7) |
| [[COLO 205 (line)]] | alt | 85.2 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0784× (z -22.9) |
| [[NCI-H2030 (line)]] | alt | 88.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -20.5) |
| [[NCI-H2347 (line)]] | alt | 50.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -18.8) |
| [[RPMI-7951 (line)]] | alt | 69.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -21.6) |
| [[AN3 CA (line)]] | alt | 65.4 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0927× (z -13.1) |
| [[HepG2_C3A (line)]] | wt | 79.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -17.4) |
| [[HT-29 (line)]] | alt | 65.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -19.7) |
| [[SHP-77 (line)]] | alt | 89.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -11.7) |
| [[SW48 (line)]] | wt | 65.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -12.3) |
| [[BT-474 (line)]] | alt | 69.2 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.305× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.447× (z -10.5) |
| [[CHP-212 (line)]] | wt | 131 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -8.7) |
| [[Hs 766T (line)]] | wt | 39.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -15.4) |
| [[SW 1088 (line)]] | alt | 79.8 | 0 | 1 | — | [[Gallic acid (drug)]] 0.05 µM 0.0929× (z -8.6) |
| [[SW 1271 (line)]] | alt | 66.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -10.1) |
| [[A-427 (line)]] | wt | 76.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 76.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 66.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 70.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 47.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2369), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LANCL1]] | +0.65 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[MBTPS1]] | +0.62 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[NUDT21]] | +0.62 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[ALDH6A1]] | +0.62 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[ANAPC5]] | +0.62 | +0.57 / +0.51 | both halves | 1e-05 | pathway: S Phase |
| [[VAMP7]] | +0.61 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[MZT1]] | +0.61 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[MDH1]] | +0.59 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[RPA1]] | +0.59 | +0.61 / +0.47 | both halves | 2e-05 | pathway: G1/S Transition |
| [[CCDC28A]] | +0.59 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[SCAMP1]] | +0.59 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[CNPY3]] | +0.58 | +0.49 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOP56]] | -0.57 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[CCDC71L]] | -0.56 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[IL12RB2]] | -0.55 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[ANKHD1-EIF4EBP3]] | -0.55 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[CEACAM19]] | -0.54 | -0.60 / -0.42 | both halves | 4e-05 |  |
| [[ADNP2]] | -0.53 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[ABL2]] | -0.52 | -0.49 / -0.37 | both halves | 7e-05 |  |
| [[ARL14EPL]] | -0.52 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[RBBP6]] | -0.51 | -0.60 / -0.31 | both halves | 2e-04 |  |
| [[RCAN1]] | -0.51 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[ST8SIA5]] | -0.51 | -0.52 / -0.39 | both halves | 5e-05 |  |
| [[YTHDF2]] | -0.51 | -0.49 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.623). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-13.2, -18.9); signed map (-37.3, -15.5). **Vector** length 94.6, 28.6% of its response variance represented; |z| ≥ 3 in 1,625 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | +4.5 | -6.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +0.3 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +1.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +7.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.1 | +4.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.0 | +1.2 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +2.0 | +0.5 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +2.0 | +1.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +1.9 | +1.6 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +1.7 | +1.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -8.1 | -10.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.0 | -15.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.7 | -7.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.8 | -13.3 |
|  | [[EX229 (drug)]] 5 µM |  | -5.4 | -7.3 |
|  | [[venetoclax (drug)]] 5 µM |  | -5.0 | -7.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.0 | -6.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.5 | -6.8 |

## What is on record

|  |  |
|---|---|
| Name | RB transcriptional corepressor like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q12.2 — chr16:53,433,977-53,491,648 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Rb2, p130 |
| Gene groups (HGNC) | DREAM complex subunits |
| Reactome | 18 pathways, smallest: Transcription of E2F targets under negative control by p107 (RBL1) and p130 (RBL2) in complex with HDAC1; FOXO-mediated transcription of cell cycle genes; TP53 Regulates Transcription of Genes Involved in G2 Cell Cycle Arrest |
| Matched by | ensembl_id |

**Function**, from UniProt [Q08999](https://www.uniprot.org/uniprotkb/Q08999) (Retinoblastoma-like protein 2):

> Key regulator of entry into cell division. Directly involved in heterochromatin formation by maintaining overall chromatin structure and, in particular, that of constitutive heterochromatin by stabilizing histone methylation. Recruits and targets histone methyltransferases KMT5B and KMT5C, leading to epigenetic transcriptional repression. Controls histone H4 'Lys-20' trimethylation. Probably acts as a transcription repressor by recruiting chromatin-modifying enzymes to promoters. Potent …

**Summary**, from NCBI Gene [5934](https://www.ncbi.nlm.nih.gov/gene/5934):

> Enables promoter-specific chromatin binding activity. Involved in regulation of lipid kinase activity. Acts upstream of or within negative regulation of gene expression. Located in nucleolus and nucleoplasm. Implicated in Brunet-Wagner neurodevelopmental syndrome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:9894](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9894) · Entrez [5934](https://www.ncbi.nlm.nih.gov/gene/5934) · UniProt [Q08999](https://www.uniprot.org/uniprotkb/Q08999) · Ensembl [ENSG00000103479](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103479)

## Data

Gene col 2369: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2369); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2369, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2369]; `tensor/DDL_lfc|DDL_z.npy` [2369]; `embed/gene_vectors.npy` [2369]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2369 or target_col == 2369). Every well: [[RBL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
