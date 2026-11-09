---
symbol: "ZSWIM8"
type: "gene"
col: 13213
ensembl_id: "ENSG00000214655"
name: "zinc finger SWIM-type containing 8"
location: "10q22.2"
module: 41
arm: "+"
pooled_cpm: 37.14
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 14
n_dd_up_clean: 10
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# ZSWIM8

*zinc finger SWIM-type containing 8* — 10q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 5.17× (z +12.9, q 1e-35, up in 46 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.407× (z -13.0, q 7e-36, down in 31 of 36 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.705× (z -6.4, q 2e-08, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WBP1L]] (+0.67, fdr 8e-06), [[FBXL12]] (+0.67, fdr 1e-05), [[ZFYVE1]] (+0.65, fdr 7e-06); moves opposite to [[G3BP1]] (-0.64, fdr 7e-06), [[CCT5]] (-0.58, fdr 1e-05), [[ADGRA3]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13213.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **5.17×** | +12.9 | 1e-35 | 46/49 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **4.47×** | +11.8 | 1e-29 | 40/48 (SW480, SNU-423, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.85×** | +11.2 | 6e-27 | 39/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.83×** | +9.1 | 1e-17 | 38/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **2.03×** | +5.6 | 3e-06 | 34/48 (SW480, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.40×** | +5.1 | 4e-05 | 27/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +5.0 | 5e-05 | 24/48 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.34×** | +4.5 | 5e-04 | 24/48 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.32×** | +4.3 | 0.001 | 22/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.28×** | +3.7 | 0.010 | 21/48 (HEC-1-A, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 0.5 µM |  | 1.33× | +3.1 | 0.12 | 11/48 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13213.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.407×** | -13.0 | 7e-36 | 31/36 (RPMI-7951, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.419×** | -12.1 | 3e-31 | 30/39 (Panc 03.27, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.463×** | -11.5 | 4e-28 | 38/46 (AsPC-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.705×** | -6.4 | 2e-08 | 34/48 (NCI-H2347, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.725×** | -4.5 | 9e-04 | 24/47 (SW480, C-33 A, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.770×** | -3.9 | 0.010 | 20/48 (NCI-H2347, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~6% here); position effect removed |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.777×** | -3.8 | 0.013 | 22/48 (H4, A498, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.772×** | -3.7 | 0.014 | 22/48 (NCI-H2347, LS 180, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.786×** | -3.6 | 0.020 | 21/48 (LoVo, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.800×** | -3.3 | 0.044 | 20/48 (NCI-H460, RPMI-7951, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.941× | -3.3 | 0.044 | 2/49 (COLO 205, NCI-H2122) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.802×** | -3.3 | 0.044 | 20/48 (NCI-H2030, A498, …) | inconsistent across doses |  |
| [[Ralimetinib dimesylate (drug)]] 5 µM |  | **0.664×** | -3.2 | 0.058 | 7/48 (J82, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Busulfan (drug)]] 0.05 µM |  | **0.812×** | -3.1 | 0.075 | 14/48 (MIA PaCa-2, A498, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.816×** | -3.0 | 0.089 | 12/48 (PANC-1, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13213. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 43.5 | 7 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.15× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.234× (z -11.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 66.5 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -15.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 35.2 | 5 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.21× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.164× (z -17.4) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 44.1 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.201× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 0.512× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 29.8 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +15.1) | — |
| [[CFPAC-1 (line)]] | alt | 41.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.120× (z -17.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 28.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +10.4) | — |
| [[A549 (line)]] | wt | 38.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.0946× (z -15.6) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 56.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.123× (z -17.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 50.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.108× (z -15.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 26.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.165× (z -12.4) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 34.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0802× (z -18.4) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 73.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.139× (z -17.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 50.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +9.9) | — |
| [[A498 (line)]] | wt | 52.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -13.1) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 21.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.200× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 53.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0643× (z -14.6) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 50.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.209× (z -9.8) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 39.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +8.8) | — |
| [[HOP62 (line)]] | alt | 32.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.34× (z +8.5) | — |
| [[Hs 766T (line)]] | wt | 42.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.220× (z -10.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 46.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.233× (z -10.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 28.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.115× (z -13.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 33.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0681× (z -17.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 30.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.247× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 40.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.169× (z -14.3) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 56.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.158× (z -12.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 32.6 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.74× (z +9.9) | — |
| [[RPMI-7951 (line)]] | alt | 49.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0534× (z -19.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 30.2 | 0 | 1 | — | [[PH-797804 (drug)]] 0.5 µM 0.0597× (z -9.9) |
| [[A-427 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13213), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WBP1L]] | +0.67 | +0.58 / +0.70 | both halves | 8e-06 |  |
| [[FBXL12]] | +0.67 | +0.54 / +0.72 | both halves | 1e-05 |  |
| [[ZFYVE1]] | +0.65 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[SRP54]] | +0.64 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[AKAP17A]] | +0.64 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[YIPF2]] | +0.63 | +0.57 / +0.70 | both halves | 1e-05 |  |
| [[MMUT]] | +0.63 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[PMM1]] | +0.61 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[TMEM208]] | +0.61 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[STX5-DT]] | +0.61 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[DERL2]] | +0.60 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[YIPF5]] | +0.60 | +0.60 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[G3BP1]] | -0.64 | -0.58 / -0.67 | both halves | 7e-06 |  |
| [[CCT5]] | -0.58 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[ADGRA3]] | -0.58 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[VWA8]] | -0.57 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[UBE2E3]] | -0.56 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[TMX3]] | -0.56 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[NAA15]] | -0.56 | -0.48 / -0.63 | both halves | 2e-05 |  |
| [[CTPS1]] | -0.55 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[GLO1]] | -0.55 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[ZDHHC21]] | -0.54 | -0.41 / -0.59 | both halves | 4e-05 |  |
| [[ATIC]] | -0.54 | -0.43 / -0.60 | both halves | 3e-05 |  |
| [[MTHFD2L]] | -0.54 | -0.52 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.667). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-24.5, -32.7); signed map (-17.4, 1.6). **Vector** length 106, 29.1% of its response variance represented; |z| ≥ 3 in 985 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.4 | +12.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +5.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.3 | +11.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.3 | +11.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.8 | +2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +2.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.7 | +1.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.4 | +1.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.6 | -6.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.0 | -12.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.0 | -13.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.0 | -11.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.9 | -3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.5 | +0.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -2.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.6 | -4.5 |
|  | [[Ralimetinib dimesylate (drug)]] 5 µM |  | -2.2 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger SWIM-type containing 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.2 — chr10:73,785,606-73,801,797 (+) |
| Ensembl biotype | protein_coding |
| Also known as | 4832404P21Rik; previously KIAA0913 |
| Gene groups (HGNC) | Zinc fingers SWIM-type |
| Reactome | 4 pathways, smallest: Regulation of expression of SLITs and ROBOs; Signaling by ROBO receptors; Axon guidance |
| Matched by | ensembl_id |

**Function**, from UniProt [A7E2V4](https://www.uniprot.org/uniprotkb/A7E2V4) (Zinc finger SWIM domain-containing protein 8):

> Substrate recognition component of a SCF-like E3 ubiquitin-protein ligase complex that promotes target-directed microRNA degradation (TDMD), a process that mediates degradation of microRNAs (miRNAs). The SCF-like E3 ubiquitin-protein ligase complex acts by catalyzing ubiquitination and subsequent degradation of AGO proteins (AGO1, AGO2, AGO3 and/or AGO4), thereby exposing miRNAs for degradation. Specifically recognizes and binds AGO proteins when they are engaged with a TDMD target. May also …

**Summary**, from NCBI Gene [23053](https://www.ncbi.nlm.nih.gov/gene/23053):

> Enables ubiquitin-like ligase-substrate adaptor activity. Involved in several processes, including positive regulation of miRNA catabolic process; protein catabolic process; and target-directed miRNA degradation. Part of Cul3-RING ubiquitin ligase complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23528](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23528) · Entrez [23053](https://www.ncbi.nlm.nih.gov/gene/23053) · UniProt [A7E2V4](https://www.uniprot.org/uniprotkb/A7E2V4) · Ensembl [ENSG00000214655](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214655)

## Data

Gene col 13213: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13213); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13213, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13213]; `tensor/DDL_lfc|DDL_z.npy` [13213]; `embed/gene_vectors.npy` [13213]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13213 or target_col == 13213). Every well: [[ZSWIM8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZSWIM8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
