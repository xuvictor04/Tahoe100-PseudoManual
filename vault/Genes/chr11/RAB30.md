---
symbol: "RAB30"
type: "gene"
col: 6027
ensembl_id: "ENSG00000137502"
name: "RAB30, member RAS oncogene family"
location: "11q14.1"
module: 59
arm: "+"
pooled_cpm: 50.57
n_lines_expressing: 50
n_dd_up: 38
n_dd_down: 6
n_dd_up_clean: 35
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# RAB30

*RAB30, member RAS oncogene family* — 11q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.75× (z +37.0, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.458× (z -13.1, q 1e-36, down in 34 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.724× (z -5.5, q 7e-06, down in 26 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DBP]] (+0.64, fdr 1e-05), [[MEF2C]] (+0.64, fdr 7e-06), [[ZNF292]] (+0.64, fdr 1e-05); moves opposite to [[TIMM23B-AGAP6]] (-0.67, fdr 1e-05), [[ZNF731P]] (-0.63, fdr 1e-05), [[SMG1P6]] (-0.63, fdr 3e-05).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PCDH18]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 4 with an alert ⚠; shown: the 15 strongest. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6027.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.75×** | +37.0 | 0e+00 | 45/48 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.52×** | +20.3 | 0e+00 | 45/48 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.21×** | +19.6 | 0e+00 | 41/48 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.94×** | +11.1 | 1e-26 | 35/48 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.82×** | +10.0 | 1e-21 | 38/48 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.52×** | +10.0 | 2e-21 | 36/48 (KATO III, LoVo, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **3.07×** | +9.8 | 6e-21 | 37/49 (PANC-1, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.78×** | +9.6 | 4e-20 | 36/48 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.75×** | +9.4 | 4e-19 | 36/48 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.61×** | +7.9 | 1e-13 | 35/48 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.57×** | +7.5 | 3e-12 | 30/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.25×** | +7.1 | 5e-11 | 35/49 (PANC-1, AsPC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.32×** | +6.6 | 2e-09 | 32/48 (PANC-1, RPMI-7951, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.42×** | +5.8 | 2e-07 | 24/48 (SW480, C-33 A, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.39×** | +5.5 | 1e-06 | 29/48 (KATO III, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6027.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.458×** | -13.1 | 1e-36 | 34/47 (C32, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.463×** | -12.4 | 4e-33 | 31/41 (C32, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.462×** | -12.0 | 6e-31 | 34/44 (SW1417, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.724×** | -5.5 | 7e-06 | 26/48 (H4, BT-474, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM |  | **0.819×** | -4.8 | 2e-04 | 17/48 (MIA PaCa-2, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.794×** | -3.8 | 0.017 | 21/48 (NCI-H2347, A549, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.948× | -3.3 | 0.080 | 0/50 | inconsistent across doses |  |
| [[Lapatinib ditosylate (drug)]] 5 µM |  | 0.708× | -3.0 | 0.17 | 4/48 (COLO 205, SW480, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6027. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 47.0 | 9 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +35.7) | [[Dinaciclib (drug)]] 5 µM 0.421× (z -9.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 21.4 | 9 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +24.5) | — |
| [[NCI-H460 (line)]] | wt | 25.6 | 9 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.92× (z +22.0) | — |
| [[SW480 (line)]] | alt | 111 | 6 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +17.2) | [[Dinaciclib (drug)]] 5 µM 0.260× (z -13.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 65.0 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +17.9) | [[Dinaciclib (drug)]] 5 µM 0.139× (z -17.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 22.5 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +23.6) | — |
| [[NCI-H1573 (line)]] | alt | 35.7 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.54× (z +23.3) | [[Dinaciclib (drug)]] 5 µM 0.197× (z -12.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 152 | 2 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.0836× (z -23.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 41.9 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.8× (z +27.1) | — |
| [[J82 (line)]] | alt | 31.6 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.4× (z +24.4) | — |
| [[LS 180 (line)]] | wt | 91.4 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.87× (z +17.9) | [[Dinaciclib (drug)]] 0.5 µM 0.159× (z -14.7) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 89.5 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +18.0) | [[Dinaciclib (drug)]] 0.05 µM 0.113× (z -18.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 47.9 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.57× (z +22.4) | — |
| [[KATO III (line)]] | alt | 21.2 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.96× (z +18.0) | [[Dinaciclib (drug)]] 5 µM 0.162× (z -10.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 26.2 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.59× (z +16.7) | — |
| [[NCI-H2030 (line)]] | alt | 51.7 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +12.0) | [[Dinaciclib (drug)]] 0.05 µM 0.169× (z -12.7) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 69.6 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.136× (z -15.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 21.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.71× (z +19.7) | — |
| [[CHP-212 (line)]] | wt | 258 | 0 | 4 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0969× (z -16.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 65.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.28× (z +23.8) | — |
| [[SHP-77 (line)]] | alt | 188 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 0.384× (z -8.9) |
| [[SW48 (line)]] | wt | 41.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.14× (z +15.1) | — |
| [[AsPC-1 (line)]] | alt | 17.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.8× (z +18.1) | — |
| [[C-33 A (line)]] | alt | 78.0 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +12.5) | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -12.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 22.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.66× (z +16.5) | — |
| [[HepG2_C3A (line)]] | wt | 63.0 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +11.0) | [[Dinaciclib (drug)]] 0.05 µM 0.177× (z -11.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 32.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.03× (z +18.0) | — |
| [[NCI-H1792 (line)]] | alt | 58.7 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.235× (z -12.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 26.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.35× (z +17.8) | — |
| [[RPMI-7951 (line)]] | alt | 56.4 | 2 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.83× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.173× (z -13.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 53.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.33× (z +13.8) | — |
| [[BT-474 (line)]] | alt | 78.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.190× (z -10.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 28.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.88× (z +17.2) | [[Dinaciclib (drug)]] 0.05 µM 0.226× (z -10.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 73.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.14× (z +15.7) | — |
| [[hTERT-HPNE (line)]] | wt | 34.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.71× (z +13.6) | — |
| [[NCI-H23 (line)]] | alt | 27.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.84× (z +20.0) | — |
| [[NCI-H2347 (line)]] | alt | 42.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +17.2) | — |
| [[Panc 03.27 (line)]] | alt | 30.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +15.0) | — |
| [[H4 (line)]] | wt | 56.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +11.7) | — |
| [[HOP62 (line)]] | alt | 16.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.20× (z +14.8) | — |
| [[NCI-H596 (line)]] | alt | 75.5 | 0 | 1 | — | [[Methylthiouracil (drug)]] 5 µM 0.0980× (z -9.0) |
| [[NCI-H661 (line)]] | alt | 146 | 0 | 1 | — | [[Budesonide (drug)]] 0.5 µM 0.0748× (z -12.2) |
| [[SNU-423 (line)]] | alt | 47.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +10.5) | — |
| [[SW 1271 (line)]] | alt | 75.5 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0950× (z -9.6) |
| [[AN3 CA (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 54.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 59.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 82.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6027), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DBP]] | +0.64 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[MEF2C]] | +0.64 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[ZNF292]] | +0.64 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[MIER1]] | +0.63 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[SNX2]] | +0.63 | +0.66 / +0.58 | both halves | 8e-06 |  |
| [[COMMD3]] | +0.62 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[ZNF608]] | +0.61 | +0.57 / +0.65 | both halves | 8e-06 |  |
| [[KMT2E]] | +0.61 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[LCA5]] | +0.60 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[MYLIP]] | +0.59 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[CXADR]] | +0.59 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[GBP2]] | +0.58 | +0.56 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIMM23B-AGAP6]] | -0.67 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[ZNF731P]] | -0.63 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[SMG1P6]] | -0.63 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[NPIPB11]] | -0.62 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[GHRLOS]] | -0.60 | -0.38 / -0.64 | both halves | 7e-05 |  |
| [[NIPA2]] | -0.58 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[TTL]] | -0.58 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[POC1B]] | -0.58 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[RBM19]] | -0.57 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[BCAP31]] | -0.57 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[SENP5]] | -0.56 | -0.50 / -0.66 | both halves | 1e-05 |  |
| [[HERC2P9-1]] | -0.56 | -0.52 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCDH18]] | B | PCDH18 activity raises RAB30's level | lines that do not express PCDH18 (34) vs lines expressing it (16) | 1.92× lower at baseline in the lines without PCDH18 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZIC1, DCN, ZNF677 |
| [[POU3F2]] | B | POU3F2 activity raises RAB30's level | lines that do not express POU3F2 (32) vs lines expressing it (18) | 1.37× lower at baseline in the lines without POU3F2 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MSR1, AMPH, SPARC |
| [[DUSP8]] | C | DUSP8 activity lowers RAB30's level | lines that do not express DUSP8 (4) vs lines expressing it (46) | 1.84× higher at baseline in the lines without DUSP8 | 0.066 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FAM241B, BTG3-AS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.715). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (21.2, -6.6); signed map (-6.9, 14.4). **Vector** length 103, 29.4% of its response variance represented; |z| ≥ 3 in 1,459 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.7 | +10.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.2 | +5.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.0 | +20.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +5.4 | +3.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.3 | +11.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.9 | +3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.7 | +3.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.7 | +4.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.6 | -5.5 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.2 | -1.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.2 | -0.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | +0.4 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -3.4 | -2.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.3 | +0.0 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -3.3 | -1.0 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -2.7 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | RAB30, member RAS oncogene family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q14.1 — chr11:82,973,133-83,071,923 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | RAB, member RAS oncogene GTPases; Small nucleolar RNA protein coding host genes |
| Reactome | 5 pathways, smallest: Intra-Golgi traffic; RAB geranylgeranylation; Intra-Golgi and retrograde Golgi-to-ER traffic |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15771](https://www.uniprot.org/uniprotkb/Q15771) (Ras-related protein Rab-30):

> The small GTPases Rab are key regulators of intracellular membrane trafficking, from the formation of transport vesicles to their fusion with membranes. Rabs cycle between an inactive GDP-bound form and an active GTP-bound form that is able to recruit to membranes different sets of downstream effectors directly responsible for vesicle formation, movement, tethering and fusion. RAB30 is required for maintaining the structural integrity of the Golgi apparatus, possibly by mediating interactions …

**Summary**, from NCBI Gene [27314](https://www.ncbi.nlm.nih.gov/gene/27314):

> Enables G protein activity. Involved in Golgi organization. Located in Golgi apparatus and vacuolar membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:9770](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9770) · Entrez [27314](https://www.ncbi.nlm.nih.gov/gene/27314) · UniProt [Q15771](https://www.uniprot.org/uniprotkb/Q15771) · Ensembl [ENSG00000137502](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137502)

## Data

Gene col 6027: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6027); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6027, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6027]; `tensor/DDL_lfc|DDL_z.npy` [6027]; `embed/gene_vectors.npy` [6027]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6027 or target_col == 6027). Every well: [[RAB30 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB30.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
