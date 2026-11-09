---
symbol: "GLRX3"
type: "gene"
col: 2909
ensembl_id: "ENSG00000108010"
name: "glutaredoxin 3"
location: "10q26.3"
module: 18
arm: "+"
pooled_cpm: 78.51
n_lines_expressing: 50
n_dd_up: 43
n_dd_down: 2
n_dd_up_clean: 25
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# GLRX3

*glutaredoxin 3* — 10q26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 43 drug-doses (18 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.63× (z +19.2, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.824× (z -5.5, q 2e-05, down in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (C-33 A 0.217×, NCI-H23 0.237×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-427 0.340×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.385×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[METTL3]] (+0.55, fdr 1e-05), [[IRAK1]] (+0.54, fdr 3e-05), [[ECPAS]] (+0.54, fdr 1e-05); moves opposite to [[HES1]] (-0.56, fdr 3e-05), [[KLHL15]] (-0.50, fdr 2e-05), [[NFKBIZ]] (-0.50, fdr 3e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[IKZF2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 20 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 43 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2909.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.63×** | +19.2 | 0e+00 | 48/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.25×** | +16.1 | 0e+00 | 45/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.13×** | +15.0 | 0e+00 | 46/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.67×** | +14.3 | 4e-44 | 37/48 (AsPC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.97×** | +13.5 | 3e-39 | 45/48 (LoVo, HT-29, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.97×** | +13.4 | 3e-39 | 46/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.04×** | +13.3 | 1e-38 | 46/48 (LoVo, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.97×** | +12.9 | 3e-36 | 43/47 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.92×** | +12.9 | 4e-36 | 45/48 (LoVo, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.88×** | +12.5 | 5e-34 | 44/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.75×** | +11.1 | 7e-27 | 41/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.63×** | +9.6 | 3e-20 | 41/48 (HT-29, CFPAC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.57×** | +8.9 | 2e-17 | 37/49 (NCI-H1792, SW480, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.52×** | +7.7 | 8e-13 | 32/45 (NCI-H1792, PANC-1, …) | all doses, flat | composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.31×** | +7.6 | 1e-12 | 34/49 (HT-29, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.40×** | +6.6 | 1e-09 | 34/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.59×** | +6.5 | 2e-09 | 39/49 (PANC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.84×** | +6.3 | 7e-09 | 31/49 (NCI-H1573, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.31×** | +5.4 | 2e-06 | 33/48 (HT-29, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.62×** | +5.0 | 2e-05 | 28/48 (CFPAC-1, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2909.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (C-33 A 0.217×, NCI-H23 0.237×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-427 0.340×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.385×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.824×** | -5.5 | 2e-05 | 25/48 (A498, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.764×** | -5.4 | 2e-05 | 28/49 (HOP62, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.936× | -4.7 | 6e-04 | 1/50 (NCI-H23) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.845× | -3.4 | 0.098 | 19/47 (LoVo, SW480, …) | two highest doses |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 0.847× | -3.2 | 0.15 | 14/49 (HEC-1-A, NCI-H1573, …) | top dose only | plate-row cell shift |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 0.849× | -3.1 | 0.18 | 18/48 (NCI-H23, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2909. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 95.0 | 14 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.56× (z +16.3) | — |
| [[SW480 (line)]] | alt | 86.5 | 13 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.33× (z +18.6) | — |
| [[PANC-1 (line)]] | alt | 104 | 11 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.66× (z +23.8) | — |
| [[COLO 205 (line)]] | alt | 58.2 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.57× (z +17.2) | — |
| [[HT-29 (line)]] | alt | 66.4 | 9 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.84× (z +13.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.67× (z +12.8) | — |
| [[NCI-H1573 (line)]] | alt | 71.1 | 8 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 8.14× (z +16.6) | — |
| [[LoVo (line)]] | wt | 65.0 | 7 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.97× (z +16.5) | — |
| [[CFPAC-1 (line)]] | alt | 62.6 | 6 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.59× (z +10.7) | — |
| [[HOP62 (line)]] | alt | 49.2 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.05× (z +12.2) | — |
| [[KATO III (line)]] | alt | 35.1 | 6 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.46× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.24× (z +9.9) | — |
| [[AsPC-1 (line)]] | alt | 69.4 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +17.6) | — |
| [[H4 (line)]] | wt | 68.5 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.25× (z +10.4) | — |
| [[LS 180 (line)]] | wt | 82.0 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.04× (z +12.2) | — |
| [[NCI-H23 (line)]] | alt | 62.8 | 4 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.29× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.237× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change |
| [[HEC-1-A (line)]] | alt | 85.7 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.57× (z +10.9) | — |
| [[HepG2_C3A (line)]] | wt | 138 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.45× (z +13.4) | — |
| [[NCI-H1792 (line)]] | alt | 44.0 | 4 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.63× (z +11.2) | — |
| [[NCI-H2030 (line)]] | alt | 72.7 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +13.4) | — |
| [[SNU-423 (line)]] | alt | 130 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +15.1) | — |
| [[SW 900 (line)]] | alt | 72.3 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +11.9) | — |
| [[BT-474 (line)]] | alt | 38.9 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.52× (z +9.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.48× (z +9.4) | — |
| [[C32 (line)]] | wt | 55.4 | 3 | 0 | [[Auranofin (drug)]] 5 µM 3.33× (z +10.8) | — |
| [[Hs 766T (line)]] | wt | 86.2 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.62× (z +13.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.52× (z +13.0) | — |
| [[RKO (line)]] | wt | 141 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.26× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.448× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[SW1417 (line)]] | alt | 88.3 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.01× (z +12.8) | — |
| [[A-172 (line)]] | wt | 54.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +13.9) | — |
| [[A-427 (line)]] | wt | 80.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.340× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.385× (z -11.7) |
| [[A549 (line)]] | wt | 106 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +9.7) | — |
| [[C-33 A (line)]] | alt | 64.5 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.14× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.217× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change |
| [[HCT15 (line)]] | alt | 72.3 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.75× (z +9.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.61× (z +8.8) | — |
| [[hTERT-HPNE (line)]] | wt | 58.3 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.88× (z +9.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.70× (z +8.6) | — |
| [[J82 (line)]] | alt | 54.2 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.64× (z +9.8) | — |
| [[LOX-IMVI (line)]] | wt | 87.8 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.43× (z +9.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 104 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.31× (z +9.4) | — |
| [[NCI-H2347 (line)]] | alt | 75.5 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +10.1) ⚠ cell-cycle shift, explains ~14% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.67× (z +8.7) | — |
| [[SK-MEL-2 (line)]] | alt | 92.8 | 2 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.23× (z +8.7) | — |
| [[A498 (line)]] | wt | 81.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +11.1) | — |
| [[Panc 03.27 (line)]] | alt | 66.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.56× (z +9.8) | — |
| [[SHP-77 (line)]] | alt | 106 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.26× (z +9.1) | — |
| [[SNU-1 (line)]] | wt | 88.9 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.83× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 108 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.94× (z +9.1) | — |
| [[AN3 CA (line)]] | alt | 121 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 73.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 73.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 77.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 87.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 54.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2909), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METTL3]] | +0.55 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[IRAK1]] | +0.54 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[ECPAS]] | +0.54 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[TTL]] | +0.54 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[MAPKAPK3]] | +0.53 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[TATDN1]] | +0.53 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[LIMK1]] | +0.53 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[GATD1]] | +0.53 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[SEL1L3]] | +0.52 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[ABCA15P]] | +0.52 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[KCTD13]] | +0.52 | +0.42 / +0.43 | both halves | 4e-05 |  |
| [[NCS1]] | +0.52 | +0.48 / +0.53 | both halves | 2e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HES1]] | -0.56 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[KLHL15]] | -0.50 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[NFKBIZ]] | -0.50 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[PTGER4]] | -0.50 | -0.34 / -0.55 | both halves | 1e-04 |  |
| [[MYLIP]] | -0.49 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[PER2]] | -0.48 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[NEDD9]] | -0.47 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[TXNIP]] | -0.47 | -0.36 / -0.50 | both halves | 1e-04 |  |
| [[MEIS1]] | -0.47 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[NR4A3]] | -0.47 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[RNASE4]] | -0.46 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[SLFN11]] | -0.46 | -0.32 / -0.51 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IKZF2]] | B | IKZF2 activity lowers GLRX3's level | lines that do not express IKZF2 (13) vs lines expressing it (37) | 1.42× higher at baseline in the lines without IKZF2 | 0.017 | ⚠ within organs, on part of the lines; also absent: ENSG00000273118, MECOM, SEMA3C; maybe low, not absent |
| [[NR4A2]] | B | NR4A2 activity lowers GLRX3's level | lines that do not express NR4A2 (7) vs lines expressing it (43) | 1.22× higher at baseline in the lines without NR4A2 | 0.038 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[NEDD9]] | B | NEDD9 activity lowers GLRX3's level | lines that do not express NEDD9 (16) vs lines expressing it (34) | 1.24× higher at baseline in the lines without NEDD9 | 0.059 | ⚠ within organs, on part of the lines; also absent: ITGA1, LGALS3, DGKG |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.461). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-11.7, -29.8); signed map (5.7, -54.6). **Vector** length 74.8, 21.6% of its response variance represented; |z| ≥ 3 in 1,375 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.3 | +13.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | +5.8 | +8.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | +5.4 | +4.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.1 | +13.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.0 | +15.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.7 | +12.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.8 | +1.8 |
|  | [[EX229 (drug)]] 5 µM |  | +3.3 | +4.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.2 | +7.6 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -4.1 | +6.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -5.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.1 | -5.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.1 | +4.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.7 | -4.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.7 | -2.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.5 | -0.3 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.2 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | glutaredoxin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.3 — chr10:130,136,391-130,184,521 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PICOT, bA500G10.4, GRX3, GLRX4, GRX4; previously TXNL2 |
| Gene groups (HGNC) | Glutaredoxin domain containing |
| Reactome | 2 pathways, smallest: Iron uptake and transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [O76003](https://www.uniprot.org/uniprotkb/O76003) (Glutaredoxin-3):

> Together with BOLA2, acts as a cytosolic iron-sulfur (Fe-S) cluster assembly factor that facilitates [2Fe-2S] cluster insertion into a subset of cytosolic proteins. Acts as a critical negative regulator of cardiac hypertrophy and a positive inotropic regulator (By similarity). Required for hemoglobin maturation. Does not possess any thioredoxin activity since it lacks the conserved motif that is essential for catalytic activity.

**Summary**, from NCBI Gene [10539](https://www.ncbi.nlm.nih.gov/gene/10539):

> This gene encodes a member of the glutaredoxin family. Glutaredoxins are oxidoreductase enzymes that reduce a variety of substrates using glutathione as a cofactor. The encoded protein binds to and modulates the function of protein kinase C theta. The encoded protein may also inhibit apoptosis and play a role in cellular growth, and the expression of this gene may be a marker for cancer. Pseudogenes of this gene are located on the short arm of chromosomes 6 and 9. Alternatively spliced …

**Accessions** — [HGNC:15987](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15987) · Entrez [10539](https://www.ncbi.nlm.nih.gov/gene/10539) · UniProt [O76003](https://www.uniprot.org/uniprotkb/O76003) · Ensembl [ENSG00000108010](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108010)

## Data

Gene col 2909: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2909); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2909, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2909]; `tensor/DDL_lfc|DDL_z.npy` [2909]; `embed/gene_vectors.npy` [2909]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2909 or target_col == 2909). Every well: [[GLRX3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GLRX3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
