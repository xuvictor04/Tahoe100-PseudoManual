---
symbol: "NUPR1"
type: "gene"
col: 10674
ensembl_id: "ENSG00000176046"
name: "nuclear protein 1, transcriptional regulator"
location: "16p11.2"
module: 63
arm: "+"
pooled_cpm: 24.39
n_lines_expressing: 26
n_dd_up: 21
n_dd_down: 12
n_dd_up_clean: 16
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 5
direction_downstream: 11
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# NUPR1

*nuclear protein 1, transcriptional regulator* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.70× (z +6.3, q 2e-07, up in 7 of 20 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 2.08× (z +4.7, q 5e-04, up in 18 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.240× (z -9.0, q 9e-17, down in 23 of 24 measured lines) ⚠ cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 0.416× (z -5.5, q 4e-06, down in 22 of 22 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LMO4]] (+0.66, fdr 1e-05), [[SLC3A2]] (+0.66, fdr 1e-05), [[DMGDH]] (+0.66, fdr 1e-05); moves opposite to [[DCBLD2]] (-0.54, fdr 3e-05), [[DOCK5]] (-0.54, fdr 2e-05), [[BZW1]] (-0.51, fdr 3e-05).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 11 go from it, the strongest it → [[PHGDH]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10674.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.70×** | +6.3 | 2e-07 | 7/20 (HS-578T, HepG2/C3A, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.77×** | +5.1 | 8e-05 | 20/24 (SNU-1, BT-474, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **2.08×** | +4.7 | 5e-04 | 18/24 (C32, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.14×** | +4.6 | 5e-04 | 3/14 (HS-578T, hTERT-HPNE, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.99×** | +4.4 | 0.001 | 16/22 (BT-474, SK-MEL-2, …) | two highest doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.94×** | +4.0 | 0.005 | 16/24 (HepG2/C3A, COLO 205, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.88×** | +4.0 | 0.005 | 12/22 (RPMI-7951, H4, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.36×** | +3.9 | 0.007 | 12/22 (A-172, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **1.52×** | +3.7 | 0.011 | 14/24 (SNU-1, PANC-1, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **2.19×** | +3.6 | 0.021 | 12/22 (LS 180, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 5 µM |  | **1.75×** | +3.4 | 0.030 | 19/24 (BT-474, MIA PaCa-2, …) | top dose only |  |
| [[Neratinib (drug)]] 5 µM |  | **1.70×** | +3.4 | 0.030 | 15/24 (BT-474, hTERT-HPNE, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.61×** | +3.4 | 0.030 | 17/23 (BT-474, LoVo, …) | two highest doses | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.45×** | +3.4 | 0.030 | 11/24 (BT-474, C32, …) | two highest doses |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **2.09×** | +3.3 | 0.031 | 13/22 (PANC-1, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | **1.65×** | +3.2 | 0.053 | 11/23 (KATO III, HT-29, …) | top dose only | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.66×** | +3.1 | 0.057 | 12/22 (BT-474, LoVo, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.43×** | +3.1 | 0.057 | 15/24 (LoVo, BT-474, …) | all doses, flat |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.62×** | +3.1 | 0.064 | 14/24 (hTERT-HPNE, BT-474, …) | rises with dose |  |
| [[Almonertinib (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +3.0 | 0.087 | 11/24 (BT-474, HT-29, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10674.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.240×** | -9.0 | 9e-17 | 23/24 (H4, PANC-1, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.349×** | -6.7 | 8e-09 | 23/24 (KATO III, H4, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.412×** | -5.6 | 4e-06 | 22/24 (KATO III, H4, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.416×** | -5.5 | 4e-06 | 22/22 (RPMI-7951, H4, …) | rises with dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.441×** | -5.2 | 2e-05 | 20/24 (H4, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.620×** | -4.3 | 0.002 | 19/24 (HT-29, SNU-423, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.505×** | -4.1 | 0.003 | 17/24 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.527×** | -4.0 | 0.004 | 17/23 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.336×** | -3.6 | 0.020 | 15/23 (KATO III, HT-29, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.582×** | -3.4 | 0.035 | 13/24 (KATO III, HT-29, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.587×** | -3.4 | 0.040 | 13/23 (PANC-1, HepG2/C3A, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.390×** | -3.1 | 0.088 | 16/24 (HT-29, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -1.04 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10674. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 38.9 | 0 | 17 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0473× (z -17.0) |
| [[KATO III (line)]] | alt | 156 | 1 | 13 (9 ⚠) | [[Entrectinib (drug)]] 5 µM 6.92× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.0238× (z -17.1) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 0.0812× (z -11.5) |
| [[H4 (line)]] | wt | 65.7 | 0 | 7 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0287× (z -17.7) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 0.0550× (z -14.4) |
| [[SNU-423 (line)]] | alt | 60.0 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0794× (z -11.6) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.206× (z -10.3) |
| [[A-172 (line)]] | wt | 112 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.113× (z -12.8) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.326× (z -9.3) |
| [[HS-578T (line)]] | alt | 59.4 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.136× (z -10.6) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.317× (z -8.7) |
| [[LS 180 (line)]] | wt | 125 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0385× (z -13.9) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.219× (z -9.2) |
| [[PANC-1 (line)]] | alt | 40.7 | 0 | 4 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0705× (z -13.8) ⚠ cell-cycle shift, explains ~40% of this change |
| [[A498 (line)]] | wt | 82.7 | 0 | 3 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.203× (z -9.1) ⚠ cell-cycle shift, explains ~40% of this change |
| [[BT-474 (line)]] | alt | 47.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Neratinib (maleate) (drug)]] 0.5 µM 6.24× (z +8.7) ⚠ cell-cycle shift, explains ~26% of this change | [[Panobinostat (drug)]] 0.5 µM 0.120× (z -10.1) ⚠ cell-cycle shift, explains ~64% of this change |
| [[RPMI-7951 (line)]] | alt | 42.3 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.140× (z -9.0) |
| [[LoVo (line)]] | wt | 9.46 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0626× (z -10.5) ⚠ cell-cycle shift, explains ~40% of this change |
| [[A-427 (line)]] | wt | 2.28 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.94 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.71 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.98 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.56 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 7.51 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.07 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.53 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.81 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.08 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 8.41 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.44 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.71 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.77 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.26 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.64 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.92 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.22 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.39 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.97 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.45 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 9.14 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.78 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.69 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.29 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.79 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.32 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10674), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LMO4]] | +0.66 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[SLC3A2]] | +0.66 | +0.57 / +0.67 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[DMGDH]] | +0.66 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[SARS1]] | +0.65 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[BEX2]] | +0.64 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[NBR2]] | +0.63 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[PCK2]] | +0.63 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[DDIT3]] | +0.62 | +0.54 / +0.64 | both halves | 1e-05 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 421 |
| [[EIF2S2]] | +0.61 | +0.49 / +0.63 | both halves | 1e-05 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[GARS1]] | +0.61 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[AARS1]] | +0.61 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[SESN2]] | +0.61 | +0.56 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCBLD2]] | -0.54 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[DOCK5]] | -0.54 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[BZW1]] | -0.51 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[TEAD1]] | -0.50 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[CD59]] | -0.49 | -0.38 / -0.44 | both halves | 7e-05 |  |
| [[UHRF1]] | -0.49 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[MTAP]] | -0.49 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[ITGB5]] | -0.48 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[SRPK1]] | -0.48 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[SUV39H2]] | -0.48 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[NUP188]] | -0.47 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[BANF1]] | -0.47 | -0.38 / -0.48 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises NUPR1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MAP2K1]] | B | MAP2K1 activity lowers NUPR1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds |
| [[SLC1A4]] | C | SLC1A4 activity raises NUPR1's level | lines that do not express SLC1A4 (4) vs lines expressing it (46) | 3.40× lower at baseline in the lines without SLC1A4 | 0.074 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CCNP, PSAT1, KAZN; maybe low, not absent; its own permutation p |
| [[LINC01133]] | C | LINC01133 activity raises NUPR1's level | lines that do not express LINC01133 (34) vs lines expressing it (16) | 3.41× lower at baseline in the lines without LINC01133 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HEPH, IL33, UGT1A1; co-absent with the target |
| [[ASNSP1]] | C | ASNSP1 activity raises NUPR1's level | lines that do not express ASNSP1 (35) vs lines expressing it (15) | 2.04× lower at baseline in the lines without ASNSP1 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF208, GCG, GPR15; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 10, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PHGDH]] | B | NUPR1 activity raises PHGDH's level | lines that do not express NUPR1 (24) vs lines expressing it (26) | 2.01× lower at baseline in the lines without NUPR1 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TTTY14, SPARC, PCDH18 |
| [[TTC39B]] | B | NUPR1 activity raises TTC39B's level | lines that do not express NUPR1 (24) vs lines expressing it (26) | 1.61× lower at baseline in the lines without NUPR1 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TTTY14, SPARC, PCDH18 |
| [[TEAD1]] | B | NUPR1 activity lowers TEAD1's level | lines that do not express NUPR1 (24) vs lines expressing it (26) | 1.33× higher at baseline in the lines without NUPR1 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TTTY14, SPARC, PCDH18 |
| [[NBR2]] | B | NUPR1 activity raises NBR2's level | lines that do not express NUPR1 (24) vs lines expressing it (26) | 1.38× lower at baseline in the lines without NUPR1 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TTTY14, SPARC, PCDH18 |
| [[CBX4]] | B | NUPR1 activity raises CBX4's level | lines that do not express NUPR1 (24) vs lines expressing it (26) | 1.28× lower at baseline in the lines without NUPR1 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TTTY14, SPARC, PCDH18 |
| [[GDF15]] | B | NUPR1 activity raises GDF15's level | lines that do not express NUPR1 (24) vs lines expressing it (26) | 2.91× lower at baseline in the lines without NUPR1 | 0.059 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TTTY14, SPARC, PCDH18 |
| [[SLC1A4]] | B | NUPR1 activity raises SLC1A4's level | lines that do not express NUPR1 (24) vs lines expressing it (26) | 1.72× lower at baseline in the lines without NUPR1 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TTTY14, SPARC, PCDH18 |
| [[EIF1]] | B | NUPR1 activity lowers EIF1's level | lines that do not express NUPR1 (24) vs lines expressing it (26) | 1.13× higher at baseline in the lines without NUPR1 | 0.072 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TTTY14, SPARC, PCDH18 |
| [[NRSN2-AS1]] | B | NUPR1 activity raises NRSN2-AS1's level | lines that do not express NUPR1 (24) vs lines expressing it (26) | 1.40× lower at baseline in the lines without NUPR1 | 0.082 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TTTY14, SPARC, PCDH18 |
| [[DMGDH]] | B | NUPR1 activity raises DMGDH's level | lines that do not express NUPR1 (24) vs lines expressing it (26) | 1.19× lower at baseline in the lines without NUPR1 | 0.087 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TTTY14, SPARC, PCDH18 |
| [[UGT1A8]] | C | NUPR1 activity raises UGT1A8's level | lines that do not express NUPR1 (24) vs lines expressing it (26) | 2.23× lower at baseline in the lines without NUPR1 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TTTY14, SPARC, PCDH18; co-absent with the target |

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.630). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.3, 48.3); signed map (-11.8, 22.9). **Vector** length 88.1, 28.0% of its response variance represented; |z| ≥ 3 in 768 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *ISR ATF4* (control, mean cos +0.56 to 16); *Cytosolic tRNA aminoacylation* (reactome, mean cos +0.52 to 9); *tRNA Aminoacylation* (reactome, mean cos +0.52 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +4.7 | +4.7 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +4.6 | +5.1 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +3.6 | +4.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.4 | +3.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.1 | +3.4 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | +3.0 | +3.7 |
|  | [[Adagrasib (drug)]] 5 µM |  | +2.9 | +3.4 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.1 | -3.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.0 | -5.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.8 | -1.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.8 | -2.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.7 | -2.0 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.6 | -1.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.6 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | nuclear protein 1, transcriptional regulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:28,532,708-28,539,008 (-) |
| Ensembl biotype | protein_coding |
| Also known as | COM1, p8 |
| Hallmark sets | P53_PATHWAY, MTORC1_SIGNALING |
| Matched by | ensembl_id |

**Function**, from UniProt [O60356](https://www.uniprot.org/uniprotkb/O60356) (Nuclear protein 1):

> Transcription regulator that converts stress signals into a program of gene expression that empowers cells with resistance to the stress induced by a change in their microenvironment. Thereby participates in the regulation of many processes namely cell-cycle, apoptosis, autophagy and DNA repair responses. Controls cell cycle progression and protects cells from genotoxic stress induced by doxorubicin through the complex formation with TP53 and EP300 that binds CDKN1A promoter leading to …

**Summary**, from NCBI Gene [26471](https://www.ncbi.nlm.nih.gov/gene/26471):

> Enables DNA binding activity and transcription coactivator activity. Involved in several processes, including negative regulation of autophagosome assembly; negative regulation of programmed cell death; and regulation of generation of precursor metabolites and energy. Acts upstream of or within negative regulation of cell cycle. Located in nucleoplasm and perinuclear region of cytoplasm. Part of protein-DNA complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29990](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29990) · Entrez [26471](https://www.ncbi.nlm.nih.gov/gene/26471) · UniProt [O60356](https://www.uniprot.org/uniprotkb/O60356) · Ensembl [ENSG00000176046](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176046)

## Data

Gene col 10674: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10674); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10674, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10674]; `tensor/DDL_lfc|DDL_z.npy` [10674]; `embed/gene_vectors.npy` [10674]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10674 or target_col == 10674). Every well: [[NUPR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUPR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
