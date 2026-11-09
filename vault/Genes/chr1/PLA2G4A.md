---
symbol: "PLA2G4A"
type: "gene"
col: 3827
ensembl_id: "ENSG00000116711"
name: "phospholipase A2 group IVA"
location: "1q31.1"
module: 152
arm: "+"
pooled_cpm: 28.99
n_lines_expressing: 28
n_dd_up: 19
n_dd_down: 23
n_dd_up_clean: 16
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 12
direction_downstream: 13
tags: ["gene", "module/152"]
generated_by: "tahoemap"
---

# PLA2G4A

*phospholipase A2 group IVA* — 1q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.22× (z +19.8, q 0e+00, up in 23 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (4 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.563× (z -10.1, q 3e-21, down in 20 of 26 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTGS2]] (+0.59, fdr 2e-05), [[PLD1]] (+0.53, fdr 3e-05), [[ZMAT4]] (+0.52, fdr 7e-05); moves opposite to [[AHNAK]] (-0.48, fdr 5e-05), [[SOGA1]] (-0.39, fdr 2e-04), [[FLII]] (-0.39, fdr 3e-04).
> It is in [[Module 152]], a single-armed module (Retinoid metabolism and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[SERPINE2]] → it (grade B ⚠); 13 go from it, the strongest it → cells under [[Procainamide (hydrochloride) (drug)]] 5 µM (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3827.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.22×** | +19.8 | 0e+00 | 23/26 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.10×** | +13.0 | 3e-36 | 21/26 (NCI-H2347, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.86×** | +10.9 | 2e-25 | 19/26 (NCI-H2347, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~5% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.77×** | +10.0 | 2e-21 | 14/26 (A498, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~24% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.67×** | +9.0 | 2e-17 | 12/26 (NCI-H2347, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.65×** | +8.8 | 1e-16 | 11/26 (NCI-H2347, A498, …) | all doses, flat | cell-cycle shift (explains ~23% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.26×** | +5.7 | 8e-07 | 9/26 (HEC-1-A, LS 180, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.35×** | +5.2 | 1e-05 | 10/26 (LoVo, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.73×** | +5.1 | 3e-05 | 11/27 (NCI-H2030, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.31×** | +4.8 | 1e-04 | 13/26 (SW 900, BT-474, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.27×** | +4.2 | 0.001 | 6/26 (NCI-H2347, C32, …) | all doses, stronger at high dose |  |
| [[Gemcitabine (drug)]] 5 µM |  | **1.38×** | +4.2 | 0.001 | 2/26 (NCI-H1792, SW 900) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.24×** | +3.8 | 0.006 | 11/26 (BT-474, NCI-H460, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.17× | +3.7 | 0.008 | 4/27 (C32, NCI-H1792, …) | all doses, flat |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.34×** | +3.6 | 0.010 | 7/26 (NCI-H2030, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.034 | 3/27 (SNU-423, RPMI-7951, …) | top dose only |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.22×** | +3.3 | 0.034 | 4/25 (NCI-H2347, LOX-IMVI, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 0.5 µM |  | **1.29×** | +3.2 | 0.048 | 1/27 (LOX-IMVI) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3827.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.563×** | -10.1 | 3e-21 | 20/26 (C32, SW 900, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.683×** | -9.5 | 8e-19 | 20/27 (LS 180, HT-29, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.651×** | -7.5 | 9e-12 | 13/26 (C32, A549, …) | all doses, flat |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.742×** | -7.4 | 2e-11 | 14/26 (NCI-H1792, NCI-H460, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.660×** | -7.3 | 3e-11 | 16/26 (LS 180, KATO III, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.699×** | -6.3 | 3e-08 | 16/25 (HT-29, LS 180, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.704×** | -6.1 | 6e-08 | 13/26 (KATO III, LoVo, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **0.721×** | -5.7 | 7e-07 | 14/26 (NCI-H460, H4, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.713×** | -5.7 | 7e-07 | 14/25 (HT-29, A549, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.728×** | -5.6 | 2e-06 | 16/26 (LS 180, KATO III, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.747×** | -5.1 | 2e-05 | 12/26 (C32, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.766×** | -4.5 | 3e-04 | 8/26 (A549, KATO III, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~22% of this change | **0.778×** | -4.4 | 4e-04 | 15/25 (SW 900, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?) |
| [[Neratinib (drug)]] 5 µM |  | **0.784×** | -4.3 | 8e-04 | 13/26 (hTERT-HPNE, NCI-H1792, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.714×** | -4.2 | 9e-04 | 12/26 (SK-MEL-2, HT-29, …) | all doses, stronger at high dose | low cells (technical?); noisy plate (z scaled) |
| [[Auranofin (drug)]] 0.5 µM |  | **0.790×** | -4.1 | 0.001 | 6/26 (A-427, HT-29, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.799×** | -3.9 | 0.003 | 12/25 (LS 180, BT-474, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.790×** | -3.8 | 0.004 | 7/25 (A549, NCI-H1792, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3827. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 681 | 0 | 18 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0626× (z -40.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.139× (z -20.5) |
| [[LS 180 (line)]] | wt | 44.4 | 0 | 7 (3 ⚠) | — | [[Vinblastine (sulfate) (drug)]] 5 µM 0.362× (z -10.8) |
| [[KATO III (line)]] | alt | 48.8 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -13.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.135× (z -11.7) |
| [[A549 (line)]] | wt | 49.7 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -11.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.225× (z -9.0) |
| [[HT-29 (line)]] | alt | 32.0 | 0 | 4 (1 ⚠) | — | [[Vinblastine (sulfate) (drug)]] 5 µM 0.366× (z -10.2) |
| [[hTERT-HPNE (line)]] | wt | 49.8 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -10.8) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 7.69 | 3 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 7.14× (z +12.8) | — |
| [[NCI-H460 (line)]] | wt | 40.7 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +11.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.24× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -9.1) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A498 (line)]] | wt | 13.9 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.78× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 96.1 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0792× (z -17.8) ⚠ transcription drop; cell-cycle shift, explains ~22% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.144× (z -13.6) |
| [[HEC-1-A (line)]] | alt | 14.5 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.32× (z +10.4) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H1792 (line)]] | alt | 138 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -18.2) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 22.6 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.30× (z +8.6) | — |
| [[SK-MEL-2 (line)]] | alt | 17.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0657× (z -19.2) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 9.82 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -10.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 3.79 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 8.64 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.46 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.54 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.17 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 7.09 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 33.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.70 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.67 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.85 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.24 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.87 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.18 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.46 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.24 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.84 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.10 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 9.35 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.22 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.81 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.72 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.91 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.89 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.32 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3827), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTGS2]] | +0.59 | +0.47 / +0.65 | both halves | 2e-05 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 962 |
| [[PLD1]] | +0.53 | +0.46 / +0.49 | both halves | 3e-05 | same gene group; pathway: Glycerophospholipid biosynthesis; STRING 743 |
| [[ZMAT4]] | +0.52 | +0.38 / +0.58 | both halves | 7e-05 |  |
| [[SNAP25]] | +0.51 | +0.41 / +0.46 | both halves | 4e-05 | STRING 410 |
| [[CFI]] | +0.51 | +0.40 / +0.54 | both halves | 5e-05 |  |
| [[TRPM8]] | +0.48 | +0.46 / +0.50 | both halves | 2e-05 |  |
| [[RNF128]] | +0.48 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[SOD3]] | +0.48 | +0.36 / +0.38 | both halves | 9e-05 |  |
| [[MEIS1]] | +0.48 | +0.23 / +0.53 | both halves | 5e-04 |  |
| [[ITPR1]] | +0.48 | +0.39 / +0.49 | both halves | 5e-05 | pathway: G alpha (i) signalling events |
| [[TESC]] | +0.47 | +0.42 / +0.44 | both halves | 4e-05 |  |
| [[LINC00511]] | +0.47 | +0.44 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AHNAK]] | -0.48 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[SOGA1]] | -0.39 | -0.30 / -0.41 | both halves | 2e-04 |  |
| [[FLII]] | -0.39 | -0.27 / -0.44 | both halves | 3e-04 |  |
| [[PIEZO1]] | -0.38 | -0.33 / -0.39 | both halves | 1e-04 |  |
| [[JPT2]] | -0.38 | -0.24 / -0.41 | both halves | 5e-04 |  |
| [[PDK1-AS1]] | -0.37 | -0.31 / -0.36 | both halves | 2e-04 |  |
| [[NUDT16-DT]] | -0.37 | -0.22 / -0.39 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 4, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SERPINE2]] | B | SERPINE2 activity raises PLA2G4A's level | lines that do not express SERPINE2 (21) vs lines expressing it (29) | 3.09× lower at baseline in the lines without SERPINE2 | 0.008 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ZNF365, ADAM12 |
| [[MEIS1]] | B | MEIS1 activity raises PLA2G4A's level | lines that do not express MEIS1 (11) vs lines expressing it (39) | 3.54× lower at baseline in the lines without MEIS1 | 0.057 | ⚠ within organs, on part of the lines; also absent: LINC01798, DYNC1I1, CAMK4 |
| [[SYTL5]] | B | SYTL5 activity raises PLA2G4A's level | lines that do not express SYTL5 (20) vs lines expressing it (30) | 2.30× lower at baseline in the lines without SYTL5 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: GBP4, LINC00589, ENSG00000227400 |
| [[PLEKHS1]] | B | PLEKHS1 activity raises PLA2G4A's level | lines that do not express PLEKHS1 (15) vs lines expressing it (35) | 1.93× lower at baseline in the lines without PLEKHS1 | 0.095 | ⚠ within organs, on part of the lines; also absent: ENSG00000261227, CYP4F3, CRYM; maybe low, not absent |
| [[PTGS2]] | C | PTGS2 activity raises PLA2G4A's level | lines that do not express PTGS2 (27) vs lines expressing it (23) | 3.69× lower at baseline in the lines without PTGS2 | 0.005 | ⚠ within organs, on part of the lines; also absent: ADAMTS9-AS2, CFH, ITGA4; co-absent with the target |
| [[GPRIN3]] | C | GPRIN3 activity raises PLA2G4A's level | lines that do not express GPRIN3 (35) vs lines expressing it (15) | 3.45× lower at baseline in the lines without GPRIN3 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AKR1B10, ENSG00000230975, ENSG00000237031; co-absent with the target |
| [[IL33]] | C | IL33 activity raises PLA2G4A's level | lines that do not express IL33 (35) vs lines expressing it (15) | 2.76× lower at baseline in the lines without IL33 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01133, MUC2, LINC01411; co-absent with the target |
| [[SNAP25]] | C | SNAP25 activity raises PLA2G4A's level | lines that do not express SNAP25 (26) vs lines expressing it (24) | 3.20× lower at baseline in the lines without SNAP25 | 0.042 | ⚠ within organs, on part of the lines; also absent: EYA4, SPOCK1, DPYSL3; co-absent with the target |
| [[AEBP1]] | C | AEBP1 activity raises PLA2G4A's level | lines that do not express AEBP1 (39) vs lines expressing it (11) | 4.34× lower at baseline in the lines without AEBP1 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TYR, FCRLA, LHFPL3-AS1; co-absent with the target |
| [[EDNRB]] | C | EDNRB activity raises PLA2G4A's level | lines that do not express EDNRB (34) vs lines expressing it (16) | 2.68× lower at baseline in the lines without EDNRB | 0.082 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL19A1, AEBP1, COL1A2; co-absent with the target |
| [[IL6]] | C | IL6 activity raises PLA2G4A's level | lines that do not express IL6 (32) vs lines expressing it (18) | 2.29× lower at baseline in the lines without IL6 | 0.092 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, G0S2; co-absent with the target |
| [[ZMAT4]] | C | ZMAT4 activity raises PLA2G4A's level | lines that do not express ZMAT4 (31) vs lines expressing it (19) | 3.04× lower at baseline in the lines without ZMAT4 | 0.094 | ⚠ within organs, on part of the lines; also absent: UBE2QL1, SHISAL1, SOX11; co-absent with the target |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 8, C 5. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Procainamide (hydrochloride) (drug)]] 5 µM | B | PLA2G4A activity raises the cells' numbers under Procainamide (hydrochloride) 5 µM (protects the cells) | lines that do not express PLA2G4A (22) vs lines expressing it (26) | the lines without PLA2G4A: 0.84× the cells of the other lines | 0.046 | ⚠ within organs, on part of the lines; also absent: PTGS2, ITGA4, EPB41L3 |
| cells under [[Arbutin (drug)]] 5 µM | B | PLA2G4A activity raises the cells' numbers under Arbutin 5 µM (protects the cells) | lines that do not express PLA2G4A (22) vs lines expressing it (26) | the lines without PLA2G4A: 0.85× the cells of the other lines | 0.068 | ⚠ within organs, on part of the lines; also absent: PTGS2, ITGA4, EPB41L3 |
| cells under [[Darolutamide (drug)]] 0.05 µM | B | PLA2G4A activity raises the cells' numbers under Darolutamide 0.05 µM (protects the cells) | lines that do not express PLA2G4A (22) vs lines expressing it (26) | the lines without PLA2G4A: 0.85× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: PTGS2, ITGA4, EPB41L3 |
| cells under [[Tucatinib (drug)]] 5 µM | B | PLA2G4A activity raises the cells' numbers under Tucatinib 5 µM (protects the cells) | lines that do not express PLA2G4A (22) vs lines expressing it (26) | the lines without PLA2G4A: 0.85× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: PTGS2, ITGA4, EPB41L3 |
| cells under [[Loperamide (hydrochloride) (drug)]] 0.5 µM | B | PLA2G4A activity lowers the cells' numbers under Loperamide (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express PLA2G4A (22) vs lines expressing it (26) | the lines without PLA2G4A: 1.11× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: PTGS2, ITGA4, EPB41L3 |
| cells under [[Malotilate (drug)]] 0.05 µM | B | PLA2G4A activity raises the cells' numbers under Malotilate 0.05 µM (protects the cells) | lines that do not express PLA2G4A (22) vs lines expressing it (26) | the lines without PLA2G4A: 0.87× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: PTGS2, ITGA4, EPB41L3 |
| cells under [[Hydroxyurea (drug)]] 0.5 µM | B | PLA2G4A activity lowers the cells' numbers under Hydroxyurea 0.5 µM (makes them more sensitive) | lines that do not express PLA2G4A (22) vs lines expressing it (26) | the lines without PLA2G4A: 1.17× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: PTGS2, ITGA4, EPB41L3 |
| [[CTTNBP2]] | B | PLA2G4A activity raises CTTNBP2's level | lines that do not express PLA2G4A (22) vs lines expressing it (28) | 2.17× lower at baseline in the lines without PLA2G4A | 0.098 | ⚠ within organs, on part of the lines; also absent: PTGS2, ITGA4, EPB41L3 |
| [[PTGS2]] | C | PLA2G4A activity raises PTGS2's level | lines that do not express PLA2G4A (22) vs lines expressing it (28) | 4.73× lower at baseline in the lines without PLA2G4A | 0.011 | ⚠ within organs, on part of the lines; also absent: PTGS2, ITGA4, EPB41L3; co-absent with the target |
| [[IL33]] | C | PLA2G4A activity raises IL33's level | lines that do not express PLA2G4A (22) vs lines expressing it (28) | 2.01× lower at baseline in the lines without PLA2G4A | 0.012 | ⚠ within organs, on part of the lines; also absent: PTGS2, ITGA4, EPB41L3; co-absent with the target |
| [[IL6]] | C | PLA2G4A activity raises IL6's level | lines that do not express PLA2G4A (22) vs lines expressing it (28) | 3.67× lower at baseline in the lines without PLA2G4A | 0.022 | ⚠ within organs, on part of the lines; also absent: PTGS2, ITGA4, EPB41L3; co-absent with the target |
| [[SOD3]] | C | PLA2G4A activity raises SOD3's level | lines that do not express PLA2G4A (22) vs lines expressing it (28) | 1.72× lower at baseline in the lines without PLA2G4A | 0.041 | ⚠ within organs, on part of the lines; also absent: PTGS2, ITGA4, EPB41L3; co-absent with the target |

## Where it sits

- **Module**: [[Module 152]] — Retinoid metabolism and transport; 29 genes; every member is in the + arm (projection on the module's main direction 0.494). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (33.7, 31.8); signed map (33.3, 34.6). **Vector** length 84.0, 21.7% of its response variance represented; |z| ≥ 3 in 814 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.2 | +19.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.1 | +13.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +5.4 | -1.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +5.2 | -0.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +4.6 | +0.1 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.7 | +0.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +0.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.6 | +4.2 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.5 | +2.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.0 | -10.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.9 | -9.5 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -3.6 | -7.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.4 | -5.7 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -3.3 | -6.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.3 | -5.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.2 | -6.1 |

## What is on record

|  |  |
|---|---|
| Name | phospholipase A2 group IVA |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q31.1 — chr1:186,828,949-186,988,981 (+) |
| Ensembl biotype | protein_coding |
| Also known as | cPLA2-alpha; previously PLA2G4 |
| Gene groups (HGNC) | Phospholipases; C2 domain containing phospholipases |
| Hallmark sets | COMPLEMENT, INTERFERON_GAMMA_RESPONSE |
| Reactome | 31 pathways, smallest: Acyl chain remodeling of CL; Hydrolysis of LPC; Acyl chain remodelling of PI |
| Matched by | ensembl_id |

**Function**, from UniProt [P47712](https://www.uniprot.org/uniprotkb/P47712) (Cytosolic phospholipase A2):

> Has primarily calcium-dependent phospholipase and lysophospholipase activities, with a major role in membrane lipid remodeling and biosynthesis of lipid mediators of the inflammatory response. Plays an important role in embryo implantation and parturition through its ability to trigger prostanoid production (By similarity). Preferentially hydrolyzes the ester bond of the fatty acyl group attached at sn-2 position of phospholipids (phospholipase A2 activity). Selectively hydrolyzes sn-2 …

**Summary**, from NCBI Gene [5321](https://www.ncbi.nlm.nih.gov/gene/5321):

> This gene encodes a member of the cytosolic phospholipase A2 group IV family. The enzyme catalyzes the hydrolysis of membrane phospholipids to release arachidonic acid which is subsequently metabolized into eicosanoids. Eicosanoids, including prostaglandins and leukotrienes, are lipid-based cellular hormones that regulate hemodynamics, inflammatory responses, and other intracellular pathways. The hydrolysis reaction also produces lysophospholipids that are converted into platelet-activating …

**Accessions** — [HGNC:9035](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9035) · Entrez [5321](https://www.ncbi.nlm.nih.gov/gene/5321) · UniProt [P47712](https://www.uniprot.org/uniprotkb/P47712) · Ensembl [ENSG00000116711](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116711)

## Data

Gene col 3827: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3827); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3827, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3827]; `tensor/DDL_lfc|DDL_z.npy` [3827]; `embed/gene_vectors.npy` [3827]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3827 or target_col == 3827). Every well: [[PLA2G4A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLA2G4A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
