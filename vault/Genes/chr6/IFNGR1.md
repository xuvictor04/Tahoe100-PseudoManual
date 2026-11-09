---
symbol: "IFNGR1"
type: "gene"
col: 378
ensembl_id: "ENSG00000027697"
name: "interferon gamma receptor 1"
location: "6q23.3"
module: 106
arm: "+"
pooled_cpm: 68.21
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 14
n_dd_up_clean: 7
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/106"]
generated_by: "tahoemap"
---

# IFNGR1

*interferon gamma receptor 1* — 6q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.79× (z +10.4, q 1e-22, up in 43 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.527× (z -17.6, q 0e+00, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[B4GALT1]] (+0.64, fdr 7e-06), [[PDLIM1]] (+0.58, fdr 7e-06), [[CPD]] (+0.56, fdr 1e-05); moves opposite to [[HOMER3]] (-0.56, fdr 1e-05), [[MSANTD3]] (-0.54, fdr 3e-05), [[SBF2-AS1]] (-0.54, fdr 4e-05).
> It is in [[Module 106]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[MMP7]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 378.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.79×** | +10.4 | 1e-22 | 43/49 (LoVo, BT-474, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.70×** | +10.4 | 1e-22 | 40/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +8.6 | 2e-15 | 40/48 (SW480, RKO, …) | rises with dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.12×** | +7.6 | 3e-12 | 35/48 (SW480, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.41×** | +6.6 | 4e-09 | 30/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.32×** | +5.4 | 5e-06 | 23/48 (SW480, NCI-H460, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.31×** | +5.2 | 1e-05 | 24/49 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.61×** | +4.8 | 1e-04 | 18/36 (LoVo, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.22×** | +3.6 | 0.023 | 19/47 (HOP62, J82, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.5 | 0.031 | 17/48 (BT-474, C-33 A, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 1.19× | +3.4 | 0.031 | 21/48 (HOP62, SNU-423, …) | two highest doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | 1.19× | +3.4 | 0.037 | 13/49 (HS-578T, HepG2/C3A, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.38×** | +3.2 | 0.053 | 12/49 (SW480, HepG2/C3A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.19× | +3.1 | 0.088 | 10/48 (AsPC-1, HepG2/C3A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 378.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.527×** | -17.6 | 0e+00 | 42/48 (COLO 205, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.457×** | -15.2 | 0e+00 | 39/48 (COLO 205, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.625×** | -9.2 | 9e-18 | 31/48 (COLO 205, SW48, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.630×** | -8.6 | 7e-16 | 26/40 (AsPC-1, HCT15, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.698×** | -7.0 | 3e-10 | 33/48 (LoVo, HT-29, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.753×** | -5.5 | 3e-06 | 23/48 (A549, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.773×** | -5.0 | 4e-05 | 25/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.783×** | -4.6 | 3e-04 | 24/48 (COLO 205, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[vincristine (drug)]] 0.5 µM |  | **0.732×** | -4.3 | 9e-04 | 23/48 (SW 1271, A-427, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.817×** | -4.0 | 0.004 | 24/48 (COLO 205, A498, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **0.833×** | -3.6 | 0.018 | 20/47 (NCI-H1792, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.778×** | -3.5 | 0.022 | 15/48 (SHP-77, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.786×** | -3.3 | 0.036 | 18/48 (COLO 205, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | 0.843× | -3.3 | 0.036 | 14/48 (HS-578T, KATO III, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.844× | -3.3 | 0.036 | 19/48 (LoVo, HepG2/C3A, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.846× | -3.1 | 0.061 | 17/47 (SW 900, A498, …) | rises with dose |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **0.805×** | -3.0 | 0.082 | 11/49 (SW 900, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 378. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 481 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0739× (z -31.9) |
| [[LoVo (line)]] | wt | 126 | 1 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.66× (z +11.7) | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -17.2) |
| [[SW480 (line)]] | alt | 45.4 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.89× (z +13.6) | — |
| [[AsPC-1 (line)]] | alt | 96.2 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.167× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.402× (z -11.9) |
| [[A549 (line)]] | wt | 79.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -13.4) |
| [[BT-474 (line)]] | alt | 108 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.71× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.280× (z -11.1) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 183 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.257× (z -15.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.378× (z -11.4) |
| [[NCI-H1792 (line)]] | alt | 63.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -18.7) |
| [[A-172 (line)]] | wt | 53.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.373× (z -9.2) |
| [[A498 (line)]] | wt | 101 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.335× (z -11.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 90.3 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.366× (z -9.3) |
| [[LOX-IMVI (line)]] | wt | 49.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -16.7) |
| [[LS 180 (line)]] | wt | 111 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -14.1) |
| [[NCI-H1573 (line)]] | alt | 29.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -12.9) |
| [[NCI-H2030 (line)]] | alt | 57.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -19.4) |
| [[NCI-H460 (line)]] | wt | 32.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -16.5) |
| [[RPMI-7951 (line)]] | alt | 60.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -13.0) |
| [[SW48 (line)]] | wt | 92.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.244× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.275× (z -10.2) |
| [[HCT15 (line)]] | alt | 53.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.119× (z -14.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 34.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.321× (z -9.9) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 136 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -9.2) |
| [[HOP62 (line)]] | alt | 35.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -9.9) |
| [[J82 (line)]] | alt | 54.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.25× (z +9.1) | — |
| [[KATO III (line)]] | alt | 83.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.481× (z -11.2) |
| [[NCI-H23 (line)]] | alt | 35.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -9.6) |
| [[NCI-H596 (line)]] | alt | 68.5 | 1 | 0 | [[Oxaprozin (drug)]] 5 µM 2.91× (z +11.2) | — |
| [[PANC-1 (line)]] | alt | 50.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.546× (z -10.2) |
| [[SNU-423 (line)]] | alt | 74.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -16.0) |
| [[SW 900 (line)]] | alt | 63.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -11.6) |
| [[SW1417 (line)]] | alt | 88.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.378× (z -10.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 34.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 44.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 52.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 39.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 93.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 49.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 68.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 57.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 41.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 52.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 378), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[B4GALT1]] | +0.64 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[PDLIM1]] | +0.58 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[CPD]] | +0.56 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[AGFG1]] | +0.56 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[XPR1]] | +0.55 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[PLSCR4]] | +0.55 | +0.46 / +0.64 | both halves | 2e-05 |  |
| [[LPCAT3]] | +0.54 | +0.44 / +0.52 | both halves | 3e-05 | pathway: HALLMARK_ADIPOGENESIS |
| [[LMTK2]] | +0.54 | +0.59 / +0.40 | both halves | 5e-05 |  |
| [[ADAM15]] | +0.53 | +0.62 / +0.38 | both halves | 6e-05 |  |
| [[GAREM1]] | +0.53 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[CDC42SE2]] | +0.53 | +0.57 / +0.45 | both halves | 3e-05 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[PACSIN2]] | +0.53 | +0.55 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOMER3]] | -0.56 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[MSANTD3]] | -0.54 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[SBF2-AS1]] | -0.54 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[MSANTD3-TMEFF1]] | -0.53 | -0.56 / -0.39 | both halves | 5e-05 |  |
| [[LZIC]] | -0.52 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[SPHK1]] | -0.52 | -0.60 / -0.38 | both halves | 6e-05 | pathway: Interferon Signaling |
| [[ADTRP]] | -0.51 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[NSRP1]] | -0.50 | -0.61 / -0.37 | both halves | 9e-05 |  |
| [[GOLGA1]] | -0.50 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[LINC00973]] | -0.49 | -0.52 / -0.39 | both halves | 6e-05 |  |
| [[FMNL1-DT]] | -0.49 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[NEPRO-AS1]] | -0.49 | -0.57 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MMP7]] | B | MMP7 activity raises IFNGR1's level | lines that do not express MMP7 (39) vs lines expressing it (11) | 1.49× lower at baseline in the lines without MMP7 | 0.053 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC5B, SFTPA2, GABRP |
| [[PLSCR4]] | B | PLSCR4 activity raises IFNGR1's level | lines that do not express PLSCR4 (11) vs lines expressing it (39) | 1.42× lower at baseline in the lines without PLSCR4 | 0.054 | ⚠ within organs, on part of the lines; also absent: IRF7, KLF12, GSDMD |
| [[STOM]] | B | STOM activity lowers IFNGR1's level | lines that do not express STOM (16) vs lines expressing it (34) | 1.00× higher at baseline in the lines without STOM | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000227355, TRIM6, AOX1 |
| [[DUBR]] | B | DUBR activity lowers IFNGR1's level | lines that do not express DUBR (8) vs lines expressing it (42) | 1.97× higher at baseline in the lines without DUBR | 0.073 | ⚠ within organs, on part of the lines; also absent: ATP10D, LRP12, CYP46A1 |
| [[PDLIM1]] | B | PDLIM1 activity raises IFNGR1's level | lines that do not express PDLIM1 (11) vs lines expressing it (39) | 1.58× lower at baseline in the lines without PDLIM1 | 0.091 | ⚠ within organs, on part of the lines; also absent: PCED1B, GPR39, ATP8B1 |
| [[HOMER3]] | C | HOMER3 activity lowers IFNGR1's level | lines that do not express HOMER3 (3) vs lines expressing it (47) | 3.00× higher at baseline in the lines without HOMER3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CHST3, RGS10, ENSG00000290876; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 106]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.638). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.7, 18.3); signed map (18.8, 28.0). **Vector** length 130, 37.9% of its response variance represented; |z| ≥ 3 in 1,256 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.7 | +8.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.3 | +5.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.8 | +10.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.6 | +10.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.7 | +1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.6 | +7.6 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +3.2 | +2.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.2 | +2.2 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | +3.2 | +3.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -11.3 | -17.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.8 | -15.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.1 | -7.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -5.8 | -4.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.0 | -3.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.5 | -3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.4 | -5.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | interferon gamma receptor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q23.3 — chr6:137,197,483-137,219,449 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CD119; previously IFNGR |
| Gene groups (HGNC) | CD molecules; Interferon receptors |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING, ALLOGRAFT_REJECTION, APOPTOSIS, IL2_STAT5_SIGNALING, ADIPOGENESIS |
| Reactome | 8 pathways, smallest: IFNG signaling activates MAPKs; Regulation of IFNG signaling; Interferon gamma signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P15260](https://www.uniprot.org/uniprotkb/P15260) (Interferon gamma receptor 1):

> Receptor subunit for interferon gamma/INFG that plays crucial roles in antimicrobial, antiviral, and antitumor responses by activating effector immune cells and enhancing antigen presentation. Associates with transmembrane accessory factor IFNGR2 to form a functional receptor. Upon ligand binding, the intracellular domain of IFNGR1 opens out to allow association of downstream signaling components JAK1 and JAK2. In turn, activated JAK1 phosphorylates IFNGR1 to form a docking site for STAT1. …

**Summary**, from NCBI Gene [3459](https://www.ncbi.nlm.nih.gov/gene/3459):

> This gene (IFNGR1) encodes the ligand-binding chain (alpha) of the gamma interferon receptor. Human interferon-gamma receptor is a heterodimer of IFNGR1 and IFNGR2. A genetic variation in IFNGR1 is associated with susceptibility to Helicobacter pylori infection. In addition, defects in IFNGR1 are a cause of mendelian susceptibility to mycobacterial disease, also known as familial disseminated atypical mycobacterial infection. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:5439](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5439) · Entrez [3459](https://www.ncbi.nlm.nih.gov/gene/3459) · UniProt [P15260](https://www.uniprot.org/uniprotkb/P15260) · Ensembl [ENSG00000027697](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000027697)

## Data

Gene col 378: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 378); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 378, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 378]; `tensor/DDL_lfc|DDL_z.npy` [378]; `embed/gene_vectors.npy` [378]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 378 or target_col == 378). Every well: [[IFNGR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IFNGR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
