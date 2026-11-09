---
symbol: "EPS15"
type: "gene"
col: 1442
ensembl_id: "ENSG00000085832"
name: "epidermal growth factor receptor pathway substrate 15"
location: "1p32.3"
module: 159
arm: "+"
pooled_cpm: 132.94
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 22
n_dd_up_clean: 3
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/159"]
generated_by: "tahoemap"
---

# EPS15

*epidermal growth factor receptor pathway substrate 15* — 1p32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.28× (z +5.9, q 2e-06, up in 30 of 47 measured lines) ⚠ cell-cycle shift, explains ~20% of this change. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.22× (z +4.9, q 2e-04, up in 27 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.475× (z -26.2, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INPP4A]] (+0.71, fdr 1e-05), [[CRLF3]] (+0.68, fdr 1e-05), [[STX2]] (+0.67, fdr 7e-06); moves opposite to [[RBM23]] (-0.65, fdr 3e-05), [[PAN2]] (-0.61, fdr 1e-04), [[YME1L1]] (-0.60, fdr 2e-04).
> It is in [[Module 159]], a single-armed module (High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PALS2]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1442.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.28×** | +5.9 | 2e-06 | 30/47 (A-172, HOP62, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.22×** | +4.9 | 2e-04 | 27/47 (HOP62, SNU-423, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.13× | +4.4 | 0.002 | 12/48 (NCI-H2347, LS 180, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.13× | +4.3 | 0.003 | 7/48 (MIA PaCa-2, CFPAC-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 1.17× | +3.9 | 0.013 | 19/49 (NCI-H2347, C32, …) | rises with dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.35×** | +3.6 | 0.030 | 20/48 (MIA PaCa-2, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.34×** | +3.5 | 0.034 | 18/49 (A-427, C32, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.5 | 0.034 | 19/48 (CFPAC-1, H4, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.10× | +3.3 | 0.051 | 2/48 (AN3 CA, SW 1088) | rises with dose |  |
| [[Neratinib (drug)]] 5 µM |  | 1.14× | +3.2 | 0.087 | 10/48 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 16 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1442.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.475×** | -26.2 | 0e+00 | 46/48 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.510×** | -16.8 | 0e+00 | 45/48 (HS-578T, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.568×** | -14.1 | 9e-43 | 42/48 (A-172, HEC-1-A, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.673×** | -13.9 | 5e-42 | 40/49 (A549, HS-578T, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.614×** | -11.7 | 2e-29 | 41/48 (NCI-H1573, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **0.692×** | -9.2 | 5e-18 | 33/49 (A-172, PANC-1, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.690×** | -8.9 | 6e-17 | 35/47 (RKO, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.504×** | -8.2 | 2e-14 | 34/49 (HOP62, LOX-IMVI, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.729×** | -7.3 | 2e-11 | 32/45 (A-172, PANC-1, …) | all doses, flat | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.769×** | -6.5 | 4e-09 | 28/48 (LOX-IMVI, COLO 205, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~52% of this change | **0.789×** | -5.9 | 2e-07 | 30/48 (SW1417, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change | **0.788×** | -5.7 | 5e-07 | 25/44 (SK-MEL-2, A-172, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.807×** | -5.3 | 4e-06 | 26/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.643×** | -5.3 | 5e-06 | 28/48 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.646×** | -5.2 | 6e-06 | 32/48 (Hs 766T, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.698×** | -4.3 | 5e-04 | 28/48 (SW480, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.846× | -4.2 | 9e-04 | 20/48 (SNU-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.712×** | -4.1 | 0.001 | 24/48 (MIA PaCa-2, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.802×** | -3.8 | 0.004 | 21/49 (MIA PaCa-2, LOX-IMVI, …) | two highest doses | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.803×** | -3.8 | 0.004 | 22/48 (LoVo, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | 0.887× | -3.0 | 0.059 | 9/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | 0.843× | -2.9 | 0.068 | 9/48 (MIA PaCa-2, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Vilanterol (drug)]] 5 µM |  | 0.920× | -2.9 | 0.068 | 2/49 (NCI-H2347, SNU-1) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1442. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 136 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -23.0) |
| [[LOX-IMVI (line)]] | wt | 173 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -30.0) |
| [[HEC-1-A (line)]] | alt | 141 | 0 | 7 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.406× (z -14.2) |
| [[HOP62 (line)]] | alt | 148 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -29.6) |
| [[HS-578T (line)]] | alt | 174 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -27.1) |
| [[MIA PaCa-2 (line)]] | alt | 273 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -20.4) |
| [[PANC-1 (line)]] | alt | 184 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.464× (z -19.9) |
| [[NCI-H1573 (line)]] | alt | 117 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -23.2) |
| [[SK-MEL-2 (line)]] | alt | 188 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -22.1) |
| [[SW48 (line)]] | wt | 135 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.301× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.335× (z -10.5) |
| [[A549 (line)]] | wt | 145 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -22.3) |
| [[NCI-H460 (line)]] | wt | 109 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -21.2) |
| [[A498 (line)]] | wt | 113 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.506× (z -13.8) |
| [[C32 (line)]] | wt | 130 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.289× (z -14.7) |
| [[J82 (line)]] | alt | 173 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -25.7) |
| [[LoVo (line)]] | wt | 106 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -18.1) |
| [[LS 180 (line)]] | wt | 113 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.481× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.620× (z -8.6) |
| [[NCI-H1792 (line)]] | alt | 131 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -30.8) |
| [[SNU-423 (line)]] | alt | 130 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -24.7) |
| [[NCI-H2030 (line)]] | alt | 157 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -15.6) |
| [[RKO (line)]] | wt | 160 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.294× (z -15.3) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.413× (z -11.5) |
| [[RPMI-7951 (line)]] | alt | 113 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -24.0) |
| [[SW 900 (line)]] | alt | 78.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -15.1) |
| [[AsPC-1 (line)]] | alt | 114 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.514× (z -12.7) |
| [[C-33 A (line)]] | alt | 129 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.398× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.576× (z -8.6) |
| [[Hs 766T (line)]] | wt | 181 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -24.4) |
| [[HT-29 (line)]] | alt | 117 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.524× (z -11.0) |
| [[hTERT-HPNE (line)]] | wt | 101 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -17.9) |
| [[KATO III (line)]] | alt | 83.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.568× (z -9.9) |
| [[SHP-77 (line)]] | alt | 120 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -13.4) |
| [[SNU-1 (line)]] | wt | 144 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.410× (z -9.7) |
| [[SW480 (line)]] | alt | 118 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.509× (z -10.9) |
| [[A-427 (line)]] | wt | 133 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.371× (z -14.0) |
| [[AN3 CA (line)]] | alt | 155 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -8.6) |
| [[BT-474 (line)]] | alt | 85.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.460× (z -11.5) |
| [[CFPAC-1 (line)]] | alt | 96.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -13.9) |
| [[COLO 205 (line)]] | alt | 78.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -13.5) |
| [[HCT15 (line)]] | alt | 119 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.492× (z -10.2) |
| [[HepG2_C3A (line)]] | wt | 120 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.398× (z -9.9) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 139 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -23.9) |
| [[NCI-H661 (line)]] | alt | 155 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.241× (z -8.7) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 147 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.586× (z -9.9) |
| [[SW 1088 (line)]] | alt | 112 | 0 | 1 | — | [[Decitabine (drug)]] 0.5 µM 0.140× (z -8.6) |
| [[SW 1271 (line)]] | alt | 112 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0978× (z -11.7) |
| [[SW1417 (line)]] | alt | 100.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.500× (z -9.6) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 75.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 130 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 78.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 123 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1442), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INPP4A]] | +0.71 | +0.69 / +0.50 | both halves | 1e-05 |  |
| [[CRLF3]] | +0.68 | +0.73 / +0.50 | both halves | 1e-05 |  |
| [[STX2]] | +0.67 | +0.72 / +0.58 | both halves | 7e-06 |  |
| [[SERAC1]] | +0.65 | +0.70 / +0.41 | both halves | 4e-05 |  |
| [[SGPP1]] | +0.65 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[EXOC2]] | +0.61 | +0.67 / +0.45 | both halves | 3e-05 |  |
| [[LYPLA1]] | +0.61 | +0.68 / +0.46 | both halves | 2e-05 |  |
| [[UNC13B]] | +0.61 | +0.61 / +0.46 | both halves | 3e-05 |  |
| [[CYTH3]] | +0.61 | +0.66 / +0.41 | both halves | 4e-05 |  |
| [[MAST2]] | +0.61 | +0.74 / +0.41 | both halves | 4e-05 |  |
| [[SLC23A2]] | +0.61 | +0.65 / +0.41 | both halves | 4e-05 |  |
| [[XPR1]] | +0.60 | +0.64 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM23]] | -0.65 | -0.72 / -0.43 | both halves | 3e-05 |  |
| [[PAN2]] | -0.61 | -0.67 / -0.34 | both halves | 1e-04 |  |
| [[YME1L1]] | -0.60 | -0.60 / -0.29 | both halves | 2e-04 |  |
| [[TRMO]] | -0.59 | -0.59 / -0.35 | both halves | 1e-04 |  |
| [[GOSR1]] | -0.59 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[C19orf54]] | -0.57 | -0.60 / -0.34 | both halves | 1e-04 |  |
| [[LPXN]] | -0.57 | -0.65 / -0.27 | both halves | 3e-04 |  |
| [[USP11]] | -0.56 | -0.65 / -0.25 | both halves | 4e-04 |  |
| [[MAGOHB]] | -0.56 | -0.61 / -0.33 | both halves | 1e-04 |  |
| [[ITFG2-AS1]] | -0.55 | -0.59 / -0.28 | both halves | 3e-04 |  |
| [[C2orf49-DT]] | -0.55 | -0.59 / -0.35 | both halves | 1e-04 |  |
| [[COQ7]] | -0.55 | -0.54 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PALS2]] | C | PALS2 activity raises EPS15's level | lines that do not express PALS2 (3) vs lines expressing it (47) | 1.56× lower at baseline in the lines without PALS2 | 0.074 | ⚠ few lines (3 vs 47); across organs; also absent: TMCC2, SACS, ANKRD44; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 159]] — High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells; 27 genes; every member is in the + arm (projection on the module's main direction 0.738). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.43; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (0.7, 1.6); signed map (-43.5, -7.1). **Vector** length 118, 37.9% of its response variance represented; |z| ≥ 3 in 1,232 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +6.1 | +2.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.9 | +2.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.1 | +1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +5.1 | +3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +4.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.4 | +2.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +4.1 | +4.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.7 | +1.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -9.1 | -26.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.2 | -14.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.0 | -16.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -5.1 | -11.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.1 | -8.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.6 | -2.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.5 | -4.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.6 | -4.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.5 | -5.2 |

## What is on record

|  |  |
|---|---|
| Name | epidermal growth factor receptor pathway substrate 15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p32.3 — chr1:51,354,263-51,519,328 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AF-1P, MLLT5 |
| Gene groups (HGNC) | EF-hand domain containing |
| Reactome | 21 pathways, smallest: InlB-mediated entry of Listeria monocytogenes into host cell; Listeria monocytogenes entry into host cells; Negative regulation of MET activity |
| Matched by | ensembl_id |

**Function**, from UniProt [P42566](https://www.uniprot.org/uniprotkb/P42566) (Epidermal growth factor receptor substrate 15):

> Involved in cell growth regulation. May be involved in the regulation of mitogenic signals and control of cell proliferation. Involved in the internalization of ligand-inducible receptors of the receptor tyrosine kinase (RTK) type, in particular EGFR. Plays a role in the assembly of clathrin-coated pits (CCPs). Acts as a clathrin adapter required for post-Golgi trafficking. Seems to be involved in CCPs maturation including invagination or budding. Involved in endocytosis of integrin beta-1 …

**Summary**, from NCBI Gene [2060](https://www.ncbi.nlm.nih.gov/gene/2060):

> This gene encodes a protein that is part of the EGFR pathway. The protein is present at clatherin-coated pits and is involved in receptor-mediated endocytosis of EGF. Notably, this gene is rearranged with the HRX/ALL/MLL gene in acute myelogeneous leukemias. Alternative splicing results in multiple transcript variants encoding distinct isoforms. [provided by RefSeq, May 2009]

**Accessions** — [HGNC:3419](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3419) · Entrez [2060](https://www.ncbi.nlm.nih.gov/gene/2060) · UniProt [P42566](https://www.uniprot.org/uniprotkb/P42566) · Ensembl [ENSG00000085832](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000085832)

## Data

Gene col 1442: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1442); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1442, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1442]; `tensor/DDL_lfc|DDL_z.npy` [1442]; `embed/gene_vectors.npy` [1442]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1442 or target_col == 1442). Every well: [[EPS15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EPS15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
