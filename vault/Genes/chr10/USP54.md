---
symbol: "USP54"
type: "gene"
col: 9291
ensembl_id: "ENSG00000166348"
name: "ubiquitin specific peptidase 54"
location: "10q22.2"
module: 44
arm: "+"
pooled_cpm: 64.65
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 17
n_dd_up_clean: 8
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 11
direction_downstream: 0
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# USP54

*ubiquitin specific peptidase 54* — 10q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.50× (z +7.1, q 9e-10, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.365× (z -17.7, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBM47]] (+0.60, fdr 1e-05), [[SLC40A1]] (+0.57, fdr 1e-05), [[GALM]] (+0.56, fdr 3e-05); moves opposite to [[TICAM2]] (-0.56, fdr 4e-05), [[CRYGS]] (-0.54, fdr 6e-05), [[CDC20-DT]] (-0.52, fdr 3e-05).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[ELF3-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9291.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.50×** | +7.1 | 9e-10 | 30/48 (RKO, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.30×** | +4.6 | 0.001 | 27/48 (HEC-1-A, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.29×** | +4.4 | 0.002 | 21/49 (LoVo, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.60×** | +4.3 | 0.003 | 24/49 (BT-474, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.56×** | +4.1 | 0.005 | 22/49 (HEC-1-A, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +4.0 | 0.007 | 20/48 (NCI-H1792, A498, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.25×** | +3.9 | 0.008 | 23/48 (RKO, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.26×** | +3.6 | 0.019 | 22/50 (LS 180, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.22×** | +3.5 | 0.031 | 17/48 (J82, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.036 | 16/49 (LS 180, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.16× | +3.3 | 0.050 | 17/48 (LS 180, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9291.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.365×** | -17.7 | 0e+00 | 47/48 (SW480, C-33 A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.473×** | -12.1 | 2e-31 | 35/42 (NCI-H460, SW480, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.521×** | -11.4 | 5e-28 | 35/45 (NCI-H1792, SW480, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.600×** | -8.6 | 1e-15 | 31/41 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.616×** | -8.5 | 2e-15 | 34/48 (COLO 205, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.702×** | -6.0 | 2e-07 | 29/47 (NCI-H460, COLO 205, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.740×** | -5.1 | 3e-05 | 26/50 (HT-29, NCI-H23, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.749×** | -5.1 | 3e-05 | 29/48 (C32, MIA PaCa-2, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.816×** | -5.0 | 3e-05 | 26/49 (COLO 205, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.803×** | -3.8 | 0.007 | 23/48 (COLO 205, LOX-IMVI, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.805×** | -3.7 | 0.013 | 19/47 (A-172, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.822×** | -3.4 | 0.025 | 23/48 (C32, SW 1088, …) | two highest doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.816×** | -3.4 | 0.025 | 19/48 (NCI-H1792, C32, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~49% of this change | **0.823×** | -3.4 | 0.025 | 19/46 (HT-29, SNU-423, …) | inconsistent across doses | low cells (technical?) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.697×** | -3.3 | 0.035 | 13/34 (HepG2/C3A, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.785×** | -3.0 | 0.082 | 18/46 (H4, C32, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9291. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 366 | 0 | 13 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0886× (z -30.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0565× (z -25.9) |
| [[HT-29 (line)]] | alt | 258 | 0 | 8 (6 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.148× (z -15.2) |
| [[NCI-H460 (line)]] | wt | 51.7 | 0 | 7 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.316× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.484× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 121 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.392× (z -13.2) |
| [[LS 180 (line)]] | wt | 88.1 | 4 (1 ⚠) | 2 (1 ⚠) | [[Trametinib (drug)]] 5 µM 3.19× (z +11.0) ⚠ cell-cycle shift, explains ~14% of this change · without an alert: [[Binimetinib (drug)]] 5 µM 2.89× (z +10.1) | [[Auranofin (drug)]] 5 µM 0.319× (z -10.3) |
| [[NCI-H1792 (line)]] | alt | 110 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -19.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.353× (z -8.9) |
| [[PANC-1 (line)]] | alt | 73.2 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.288× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.460× (z -8.7) |
| [[SW480 (line)]] | alt | 76.4 | 0 | 6 (5 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.242× (z -19.4) |
| [[C32 (line)]] | wt | 65.0 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.268× (z -10.4) |
| [[MIA PaCa-2 (line)]] | alt | 89.0 | 0 | 4 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.150× (z -15.2) |
| [[A-172 (line)]] | wt | 62.1 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.218× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -10.1) |
| [[A-427 (line)]] | wt | 38.0 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.240× (z -12.6) |
| [[SNU-423 (line)]] | alt | 88.5 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.254× (z -13.1) |
| [[SW 900 (line)]] | alt | 83.0 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.236× (z -13.9) |
| [[A498 (line)]] | wt | 47.3 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.355× (z -10.3) |
| [[C-33 A (line)]] | alt | 82.1 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.140× (z -17.6) |
| [[HEC-1-A (line)]] | alt | 42.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.343× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.443× (z -8.8) |
| [[HOP62 (line)]] | alt | 45.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.313× (z -11.2) |
| [[HS-578T (line)]] | alt | 41.0 | 1 | 1 | [[Dexamethasone (drug)]] 0.5 µM 2.92× (z +9.0) | [[Auranofin (drug)]] 5 µM 0.247× (z -11.7) |
| [[LoVo (line)]] | wt | 51.7 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.331× (z -11.4) |
| [[NCI-H1573 (line)]] | alt | 40.4 | 2 (1 ⚠) | 0 | [[Trametinib (drug)]] 5 µM 3.20× (z +9.8) ⚠ cell-cycle shift, explains ~14% of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 3.23× (z +9.0) | — |
| [[SW1417 (line)]] | alt | 65.3 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.290× (z -12.5) |
| [[SW48 (line)]] | wt | 43.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.144× (z -10.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 50.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.289× (z -8.5) |
| [[BT-474 (line)]] | alt | 50.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.98× (z +13.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HepG2_C3A (line)]] | wt | 51.3 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.107× (z -8.9) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 26.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +10.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[KATO III (line)]] | alt | 44.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.196× (z -14.4) |
| [[NCI-H2347 (line)]] | alt | 44.2 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.281× (z -11.4) |
| [[Panc 03.27 (line)]] | alt | 48.5 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.308× (z -9.6) |
| [[RKO (line)]] | wt | 24.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.70× (z +8.7) | — |
| [[SK-MEL-2 (line)]] | alt | 81.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.241× (z -12.2) |
| [[A549 (line)]] | wt | 51.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 68.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 43.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 63.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 39.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 75.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9291), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM47]] | +0.60 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[SLC40A1]] | +0.57 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[GALM]] | +0.56 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[FSBP]] | +0.55 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[CGN]] | +0.55 | +0.39 / +0.56 | both halves | 6e-05 |  |
| [[CTNND1]] | +0.54 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[MAP2K6]] | +0.54 | +0.51 / +0.36 | both halves | 1e-04 |  |
| [[FRK]] | +0.54 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[SSH2]] | +0.54 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[PLEKHG6]] | +0.53 | +0.50 / +0.46 | both halves | 2e-05 |  |
| [[EPS8]] | +0.53 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[MPP7]] | +0.52 | +0.49 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TICAM2]] | -0.56 | -0.42 / -0.59 | both halves | 4e-05 |  |
| [[CRYGS]] | -0.54 | -0.55 / -0.38 | both halves | 6e-05 |  |
| [[CDC20-DT]] | -0.52 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[TRAPPC12]] | -0.52 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[GPC5]] | -0.51 | -0.49 / -0.39 | both halves | 6e-05 |  |
| [[LINC00862]] | -0.50 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[ZNF621]] | -0.50 | -0.51 / -0.37 | both halves | 8e-05 |  |
| [[CFAP53]] | -0.50 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[LRP2BP-AS1]] | -0.49 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[CCDC92]] | -0.49 | -0.49 / -0.38 | both halves | 6e-05 |  |
| [[IDI2-AS1]] | -0.49 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[EOGT]] | -0.49 | -0.42 / -0.44 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ELF3-AS1]] | B | ELF3-AS1 activity raises USP54's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 1.52× lower at baseline in the lines without ELF3-AS1 | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[FRMD4B]] | B | FRMD4B activity raises USP54's level | lines that do not express FRMD4B (20) vs lines expressing it (30) | 1.62× lower at baseline in the lines without FRMD4B | 0.024 | ⚠ within organs, on part of the lines; also absent: LINC01589, ENSG00000290729, FRK; maybe low, not absent |
| [[HNMT]] | B | HNMT activity raises USP54's level | lines that do not express HNMT (17) vs lines expressing it (33) | 1.45× lower at baseline in the lines without HNMT | 0.042 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TNFSF10, VSIR |
| [[MTUS1]] | B | MTUS1 activity raises USP54's level | lines that do not express MTUS1 (17) vs lines expressing it (33) | 1.51× lower at baseline in the lines without MTUS1 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, SHROOM3, ELF3 |
| [[EFNA1]] | B | EFNA1 activity raises USP54's level | lines that do not express EFNA1 (13) vs lines expressing it (37) | 1.50× lower at baseline in the lines without EFNA1 | 0.074 | ⚠ within organs, on part of the lines; also absent: ELF3-AS1, ANO9, GPRC5A; maybe low, not absent |
| [[RASSF6]] | B | RASSF6 activity raises USP54's level | lines that do not express RASSF6 (28) vs lines expressing it (22) | 1.53× lower at baseline in the lines without RASSF6 | 0.076 | ⚠ within organs, on part of the lines; also absent: TOX3, ELF3, ITGB6 |
| [[SLC40A1]] | B | SLC40A1 activity raises USP54's level | lines that do not express SLC40A1 (28) vs lines expressing it (22) | 1.41× lower at baseline in the lines without SLC40A1 | 0.089 | ⚠ within organs, on part of the lines; also absent: RASSF6, WFDC2, TOX3 |
| [[TRIM31]] | B | TRIM31 activity raises USP54's level | lines that do not express TRIM31 (39) vs lines expressing it (11) | 1.80× lower at baseline in the lines without TRIM31 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, GCNT3, NPSR1 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers USP54's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers USP54's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MAP2K2]] | B | MAP2K2 activity lowers USP54's level | compounds that target MAP2K2: 2 of 2 raise it (Binimetinib, Trametinib) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.486). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.6, 43.1); signed map (52.5, 4.1). **Vector** length 97.4, 24.8% of its response variance represented; |z| ≥ 3 in 1,327 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.8 | +4.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.3 | +2.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +0.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.3 | +2.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change | +3.1 | -1.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.6 | +2.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.3 | +3.4 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.1 | +2.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.0 | +3.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.8 | -17.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.7 | -8.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.6 | -3.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.1 | -2.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.0 | -12.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -5.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.4 | -1.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.2 | -2.0 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -1.9 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin specific peptidase 54 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.2 — chr10:73,497,538-73,626,117 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ37318, bA137L10.3, bA137L10.4; previously C10orf29 |
| Gene groups (HGNC) | Ubiquitin specific peptidases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q70EL1](https://www.uniprot.org/uniprotkb/Q70EL1) (Ubiquitin carboxyl-terminal hydrolase 54):

> Deubiquitinase that specifically mediates 'Lys-63'-linked deubiquitination of substrates with a polyubiquitin chain composed of at least 3 ubiquitins. Specifically recognizes ubiquitin chain in position S2 and catalyzes cleavage of polyubiquitin within 'Lys-63'-linked chains. Not able to deubiquitinate substrates with shorter ubiquitin chains. Mediates deubiquitination of PLK4, maintaining PLK4 stability by reducing its ubiquitination-mediated degradation.

**Summary**, from NCBI Gene [159195](https://www.ncbi.nlm.nih.gov/gene/159195):

> Enables K63-linked deubiquitinase activity and cysteine-type deubiquitinase activity. Predicted to be involved in protein deubiquitination and proteolysis. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23513](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23513) · Entrez [159195](https://www.ncbi.nlm.nih.gov/gene/159195) · UniProt [Q70EL1](https://www.uniprot.org/uniprotkb/Q70EL1) · Ensembl [ENSG00000166348](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166348)

## Data

Gene col 9291: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9291); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9291, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9291]; `tensor/DDL_lfc|DDL_z.npy` [9291]; `embed/gene_vectors.npy` [9291]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9291 or target_col == 9291). Every well: [[USP54 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USP54.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
