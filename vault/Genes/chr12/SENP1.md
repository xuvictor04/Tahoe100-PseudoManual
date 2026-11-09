---
symbol: "SENP1"
type: "gene"
col: 1255
ensembl_id: "ENSG00000079387"
name: "SUMO specific peptidase 1"
location: "12q13.11"
module: 16
arm: "+"
pooled_cpm: 50.96
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 10
n_dd_up_clean: 10
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# SENP1

*SUMO specific peptidase 1* — 12q13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.08× (z +44.9, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.546× (z -17.1, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NHLRC2]] (+0.70, fdr 7e-06), [[FAM111A]] (+0.69, fdr 7e-06), [[TIA1]] (+0.68, fdr 7e-06); moves opposite to [[QSOX1]] (-0.63, fdr 1e-05), [[GIT1]] (-0.62, fdr 1e-05), [[ZDHHC9]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[NDRG1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1255.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.08×** | +44.9 | 0e+00 | 48/48 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.10×** | +30.8 | 0e+00 | 48/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **4.64×** | +22.7 | 0e+00 | 45/49 (SW480, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.00×** | +19.7 | 0e+00 | 46/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.66×** | +14.4 | 6e-45 | 43/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.54×** | +12.2 | 3e-32 | 36/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.03×** | +10.4 | 1e-23 | 35/48 (SW480, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.41×** | +9.7 | 3e-20 | 34/47 (KATO III, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.41×** | +9.7 | 3e-20 | 36/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.33×** | +8.0 | 7e-14 | 31/48 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +7.0 | 9e-11 | 24/48 (LoVo, BT-474, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.21×** | +5.3 | 5e-06 | 20/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | 1.17× | +4.5 | 3e-04 | 14/48 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | 1.15× | +3.8 | 0.005 | 15/47 (HepG2/C3A, NCI-H1573, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | 1.13× | +3.4 | 0.022 | 15/47 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[Terfenadine (drug)]] 0.5 µM |  | 1.12× | +3.1 | 0.058 | 6/48 (Hs 766T, SHP-77, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.11× | +3.0 | 0.067 | 2/47 (LoVo, hTERT-HPNE) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1255.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.546×** | -17.1 | 0e+00 | 44/48 (NCI-H23, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.585×** | -15.1 | 0e+00 | 41/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.713×** | -13.5 | 3e-39 | 34/48 (NCI-H23, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.732×** | -12.4 | 2e-33 | 41/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.698×** | -10.1 | 4e-22 | 38/48 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.755×** | -7.9 | 2e-13 | 25/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.795×** | -6.5 | 7e-09 | 26/48 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.822×** | -5.3 | 7e-06 | 22/47 (LOX-IMVI, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.784×** | -4.9 | 6e-05 | 18/48 (LoVo, C32, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.744×** | -4.4 | 8e-04 | 15/48 (RKO, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.866× | -3.9 | 0.005 | 18/48 (C-33 A, A-427, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~95% of this change | 0.916× | -3.5 | 0.024 | 13/48 (H4, SW 1088, …) | top dose only | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.965× | -3.2 | 0.051 | 0/49 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1255. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 96.6 | 6 (2 ⚠) | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.64× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.136× (z -24.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -15.9) |
| [[SW480 (line)]] | alt | 74.6 | 5 | 5 | [[TAK-901 (drug)]] 5 µM 5.71× (z +15.4) | [[Panobinostat (drug)]] 0.5 µM 0.476× (z -12.5) |
| [[NCI-H460 (line)]] | wt | 58.1 | 7 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +29.2) | [[Panobinostat (drug)]] 5 µM 0.533× (z -9.7) |
| [[PANC-1 (line)]] | alt | 73.2 | 6 | 3 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +34.7) | [[Panobinostat (drug)]] 5 µM 0.445× (z -12.8) |
| [[NCI-H1573 (line)]] | alt | 66.6 | 6 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +18.5) | [[Panobinostat (drug)]] 0.5 µM 0.407× (z -11.2) |
| [[A-427 (line)]] | wt | 99.9 | 3 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.13× (z +9.6) | [[Panobinostat (drug)]] 0.5 µM 0.393× (z -12.0) |
| [[A498 (line)]] | wt | 52.3 | 4 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +26.2) | [[Panobinostat (drug)]] 0.5 µM 0.463× (z -10.5) |
| [[NCI-H2030 (line)]] | alt | 57.4 | 4 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +22.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.557× (z -10.3) |
| [[KATO III (line)]] | alt | 44.2 | 5 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +12.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.564× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 53.9 | 4 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +20.8) | [[Dinaciclib (drug)]] 0.5 µM 0.405× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.448× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 45.4 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +23.1) | — |
| [[LOX-IMVI (line)]] | wt | 56.1 | 3 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +13.4) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -14.4) |
| [[NCI-H2347 (line)]] | alt | 40.3 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.73× (z +29.7) | — |
| [[A-172 (line)]] | wt | 38.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +21.0) | — |
| [[A549 (line)]] | wt | 53.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.92× (z +28.6) | — |
| [[HS-578T (line)]] | alt | 34.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +16.5) | — |
| [[J82 (line)]] | alt | 59.4 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +24.4) | [[Panobinostat (drug)]] 5 µM 0.369× (z -12.9) |
| [[LoVo (line)]] | wt | 52.0 | 4 | 0 | [[Harringtonine (drug)]] 5 µM 3.21× (z +13.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 33.0 | 4 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 4.09× (z +11.4) | — |
| [[RKO (line)]] | wt | 70.3 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +14.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.551× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 42.6 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +14.6) | [[Lonafarnib (drug)]] 5 µM 0.105× (z -10.2) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 63.3 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.473× (z -11.2) |
| [[SK-MEL-2 (line)]] | alt | 51.5 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.296× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 41.9 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +12.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -11.5) |
| [[CFPAC-1 (line)]] | alt | 26.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.04× (z +21.4) | — |
| [[H4 (line)]] | wt | 37.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +9.8) | [[Selinexor (drug)]] 5 µM 0.323× (z -9.9) ⚠ cell-cycle shift, explains ~95% of this change |
| [[HCT15 (line)]] | alt | 37.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +10.4) | — |
| [[HOP62 (line)]] | alt | 32.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +15.0) | — |
| [[Hs 766T (line)]] | wt | 29.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +13.7) | — |
| [[HT-29 (line)]] | alt | 35.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +16.3) | — |
| [[hTERT-HPNE (line)]] | wt | 29.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.87× (z +14.9) | — |
| [[NCI-H1792 (line)]] | alt | 36.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +14.1) | — |
| [[RPMI-7951 (line)]] | alt | 40.3 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 5.01× (z +12.3) | — |
| [[SNU-1 (line)]] | wt | 69.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +13.3) | — |
| [[SNU-423 (line)]] | alt | 36.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.37× (z +21.9) | — |
| [[SW 900 (line)]] | alt | 44.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +18.2) | — |
| [[BT-474 (line)]] | alt | 32.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +12.4) | — |
| [[C32 (line)]] | wt | 39.7 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 3.00× (z +9.7) | — |
| [[HepG2_C3A (line)]] | wt | 48.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +14.9) | — |
| [[SW1417 (line)]] | alt | 45.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +12.3) | — |
| [[AN3 CA (line)]] | alt | 68.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 66.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 38.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 72.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 83.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1255), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NHLRC2]] | +0.70 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[FAM111A]] | +0.69 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[TIA1]] | +0.68 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[ZFP91]] | +0.68 | +0.65 / +0.58 | both halves | 8e-06 |  |
| [[VEZF1]] | +0.68 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[ST7L]] | +0.66 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[ZNF678]] | +0.66 | +0.56 / +0.72 | both halves | 1e-05 |  |
| [[DCLRE1A]] | +0.66 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[ZNF764]] | +0.66 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[LZIC]] | +0.66 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[ZNF507]] | +0.65 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[ZNF620]] | +0.65 | +0.63 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[QSOX1]] | -0.63 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[GIT1]] | -0.62 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[ZDHHC9]] | -0.62 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[RAB6A]] | -0.62 | -0.59 / -0.58 | both halves | 7e-06 |  |
| [[AZIN2]] | -0.61 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[CARD19]] | -0.61 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[CD81]] | -0.61 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[SPTLC2]] | -0.61 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[TMEM120B]] | -0.60 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[IGSF8]] | -0.60 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[RNF149]] | -0.60 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[PI4KAP2]] | -0.60 | -0.56 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NDRG1]] | B | NDRG1 activity lowers SENP1's level | lines that do not express NDRG1 (6) vs lines expressing it (44) | 1.77× higher at baseline in the lines without NDRG1 | 0.007 | ⚠ within organs, on part of the lines; also absent: SMOX, DELEC1, SLC2A1 |
| [[MICE]] | B | MICE activity lowers SENP1's level | lines that do not express MICE (14) vs lines expressing it (36) | 1.28× higher at baseline in the lines without MICE | 0.066 | ⚠ within organs, on part of the lines; also absent: TRIM2, ACSL5, TNFRSF14-AS1; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises SENP1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises SENP1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.643). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-17.9, 4.6); signed map (14.9, -29.3). **Vector** length 104, 27.1% of its response variance represented; |z| ≥ 3 in 1,183 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +9.1 | +30.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.8 | +44.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.9 | +19.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.7 | +22.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.8 | +12.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | +0.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +5.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | -0.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.3 | +0.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +7.0 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -5.8 | -17.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.4 | -12.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.3 | -15.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.9 | -10.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -1.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.3 | -1.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.0 | +1.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -3.0 | -4.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.6 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | SUMO specific peptidase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.11 — chr12:48,039,784-48,106,079 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | SUMO specific peptidases |
| Reactome | 7 pathways, smallest: SUMO is proteolytically processed; Processing and activation of SUMO; RHOF GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P0U3](https://www.uniprot.org/uniprotkb/Q9P0U3) (Sentrin-specific protease 1):

> Protease that catalyzes two essential functions in the SUMO pathway. The first is the hydrolysis of an alpha-linked peptide bond at the C-terminal end of the small ubiquitin-like modifier (SUMO) propeptides, SUMO1, SUMO2 and SUMO3 leading to the mature form of the proteins. The second is the deconjugation of SUMO1, SUMO2 and SUMO3 from targeted proteins, by cleaving an epsilon-linked peptide bond between the C-terminal glycine of the mature SUMO and the lysine epsilon-amino group of the target …

**Summary**, from NCBI Gene [29843](https://www.ncbi.nlm.nih.gov/gene/29843):

> This gene encodes a cysteine protease that specifically targets members of the small ubiquitin-like modifier (SUMO) protein family. This protease regulates SUMO pathways by deconjugating sumoylated proteins. This protease also functions to process the precursor SUMO proteins into their mature form. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Jun 2012]

**Accessions** — [HGNC:17927](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17927) · Entrez [29843](https://www.ncbi.nlm.nih.gov/gene/29843) · UniProt [Q9P0U3](https://www.uniprot.org/uniprotkb/Q9P0U3) · Ensembl [ENSG00000079387](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000079387)

## Data

Gene col 1255: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1255); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1255, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1255]; `tensor/DDL_lfc|DDL_z.npy` [1255]; `embed/gene_vectors.npy` [1255]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1255 or target_col == 1255). Every well: [[SENP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SENP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
