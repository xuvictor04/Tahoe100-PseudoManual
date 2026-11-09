---
symbol: "PPL"
type: "gene"
col: 4024
ensembl_id: "ENSG00000118898"
name: "periplakin"
location: "16p13.3"
module: 15
arm: "-"
pooled_cpm: 44.14
n_lines_expressing: 31
n_dd_up: 18
n_dd_down: 26
n_dd_up_clean: 14
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 24
direction_downstream: 23
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# PPL

*periplakin* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.86× (z +11.7, q 5e-29, up in 24 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (6 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.503× (z -9.1, q 7e-17, down in 22 of 29 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.541× (z -8.1, q 1e-13, down in 21 of 29 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPPK1]] (+0.69, fdr 7e-06), [[C1orf226]] (+0.61, fdr 1e-05), [[TPPP]] (+0.59, fdr 1e-05); moves opposite to [[TMEM11-DT]] (-0.55, fdr 3e-05), [[GLUD1P3]] (-0.52, fdr 3e-05), [[PSMB5]] (-0.51, fdr 6e-05).
> It sits in the **-** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 24 arrows point to it, the strongest [[KLF5]] → it (grade B ⚠); 23 go from it, the strongest it → [[AGFG2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4024.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.86×** | +11.7 | 5e-29 | 24/29 (J82, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.69×** | +10.0 | 6e-21 | 16/29 (SHP-77, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.94×** | +8.8 | 2e-16 | 21/29 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.97×** | +8.7 | 5e-16 | 9/22 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.85×** | +8.2 | 2e-14 | 16/28 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.83×** | +8.1 | 6e-14 | 21/29 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.80×** | +7.2 | 4e-11 | 12/23 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.58×** | +6.1 | 7e-08 | 21/30 (Hs 766T, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.53×** | +5.7 | 9e-07 | 15/29 (PANC-1, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.37×** | +4.3 | 0.001 | 14/29 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.29×** | +3.9 | 0.004 | 15/29 (J82, Hs 766T, …) | two highest doses | noisy plate (z scaled); position effect removed |
| [[Arbutin (drug)]] 0.05 µM |  | **1.35×** | +3.8 | 0.008 | 11/29 (NCI-H2347, SW480, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.31×** | +3.5 | 0.019 | 11/29 (A-427, NCI-H23, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.29×** | +3.4 | 0.027 | 11/29 (SHP-77, BT-474, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.029 | 12/29 (Hs 766T, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **1.25×** | +3.0 | 0.094 | 9/29 (HT-29, KATO III, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.36×** | +3.0 | 0.094 | 2/28 (SHP-77, LoVo) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.19× | +3.0 | 0.094 | 10/29 (Hs 766T, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4024.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.503×** | -9.1 | 7e-17 | 22/29 (NCI-H1573, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.536×** | -8.2 | 5e-14 | 23/29 (SW480, KATO III, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.541×** | -8.1 | 1e-13 | 21/29 (NCI-H1573, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.546×** | -8.0 | 2e-13 | 24/29 (NCI-H1573, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.661×** | -7.7 | 2e-12 | 27/30 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.571×** | -7.4 | 1e-11 | 24/29 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.627×** | -6.2 | 6e-08 | 20/29 (HT-29, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.649×** | -5.7 | 9e-07 | 19/29 (NCI-H1573, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.634×** | -5.0 | 3e-05 | 18/29 (HT-29, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.488×** | -5.0 | 4e-05 | 18/29 (KATO III, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.701×** | -4.7 | 2e-04 | 14/28 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.700×** | -4.5 | 3e-04 | 13/27 (SW480, Panc 03.27, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.716×** | -4.4 | 5e-04 | 18/29 (HT-29, HCT15, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.714×** | -4.3 | 8e-04 | 14/28 (NCI-H1792, J82, …) | rises with dose | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.560×** | -4.0 | 0.002 | 15/29 (SW480, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.585×** | -3.7 | 0.008 | 17/30 (A-427, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.751×** | -3.6 | 0.010 | 9/29 (Hs 766T, NCI-H1792, …) | top dose only | position effect removed |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.686×** | -3.5 | 0.012 | 11/29 (SW480, LoVo, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4024. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 153 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.250× (z -21.2) |
| [[HT-29 (line)]] | alt | 221 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.130× (z -18.5) |
| [[PANC-1 (line)]] | alt | 19.1 | 6 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.97× (z +11.9) | — |
| [[NCI-H1573 (line)]] | alt | 87.1 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.125× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.126× (z -13.3) |
| [[HEC-1-A (line)]] | alt | 117 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.76× (z +13.2) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -8.9) |
| [[LS 180 (line)]] | wt | 41.6 | 1 | 3 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.16× (z +8.6) | [[Digitoxin (drug)]] 5 µM 0.273× (z -9.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.276× (z -9.6) |
| [[Hs 766T (line)]] | wt | 62.1 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.16× (z +13.0) | [[Digitoxin (drug)]] 5 µM 0.217× (z -8.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 11.1 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 4.64× (z +10.0) | — |
| [[A-427 (line)]] | wt | 24.9 | 0 | 2 (1 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.0634× (z -9.5) |
| [[CFPAC-1 (line)]] | alt | 64.9 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +12.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -13.8) |
| [[COLO 205 (line)]] | alt | 35.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +11.1) | — |
| [[KATO III (line)]] | alt | 160 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -14.4) |
| [[LoVo (line)]] | wt | 26.2 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.39× (z +9.5) | — |
| [[Panc 03.27 (line)]] | alt | 84.4 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -10.4) |
| [[BT-474 (line)]] | alt | 69.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -9.4) |
| [[HCT15 (line)]] | alt | 128 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.275× (z -13.2) |
| [[HepG2_C3A (line)]] | wt | 32.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.94× (z +11.9) | — |
| [[SHP-77 (line)]] | alt | 12.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +13.9) | — |
| [[SNU-423 (line)]] | alt | 29.0 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.125× (z -10.2) |
| [[SW1417 (line)]] | alt | 143 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.296× (z -15.5) |
| [[A-172 (line)]] | wt | 5.36 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.52 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 11.0 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 8.47 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 10.3 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 9.62 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.95 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.98 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.80 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 8.12 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.61 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.85 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.54 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.42 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 69.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.23 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.61 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 10.7 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.55 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.07 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4024), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPPK1]] | +0.69 | +0.70 / +0.62 | both halves | 7e-06 | same gene group; STRING 692 |
| [[C1orf226]] | +0.61 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[TPPP]] | +0.59 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[EZR]] | +0.59 | +0.47 / +0.51 | both halves | 2e-05 | STRING 957 |
| [[MISP]] | +0.59 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[JUNB]] | +0.57 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[PNPLA2]] | +0.55 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[PLCD3]] | +0.54 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[SPTAN1]] | +0.54 | +0.37 / +0.52 | both halves | 9e-05 | same gene group |
| [[ZDHHC11B]] | +0.53 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[TNKS1BP1]] | +0.53 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[CGN]] | +0.53 | +0.49 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM11-DT]] | -0.55 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[GLUD1P3]] | -0.52 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[PSMB5]] | -0.51 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[SNHG30]] | -0.50 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[ELMOD3]] | -0.49 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[PRDM10]] | -0.49 | -0.38 / -0.43 | both halves | 7e-05 |  |
| [[METTL4]] | -0.48 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[DHX35]] | -0.48 | -0.37 / -0.41 | both halves | 9e-05 |  |
| [[TRAPPC13]] | -0.47 | -0.30 / -0.40 | both halves | 2e-04 |  |
| [[MCM9]] | -0.47 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[C8orf76]] | -0.47 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[APTX]] | -0.46 | -0.40 / -0.26 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 8, C 16. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLF5]] | B | KLF5 activity raises PPL's level | lines that do not express KLF5 (18) vs lines expressing it (32) | 3.63× lower at baseline in the lines without KLF5 | 0.014 | ⚠ within organs, on part of the lines; also absent: LAMA3, IFNLR1, NCMAP; maybe low, not absent |
| [[AQP3]] | B | AQP3 activity raises PPL's level | lines that do not express AQP3 (19) vs lines expressing it (31) | 3.12× lower at baseline in the lines without AQP3 | 0.027 | ⚠ within organs, on part of the lines; also absent: ABCC3, ELF3, CD24; maybe low, not absent |
| [[KRT23]] | B | KRT23 activity raises PPL's level | lines that do not express KRT23 (40) vs lines expressing it (10) | 4.33× lower at baseline in the lines without KRT23 | 0.032 | ⚠ within organs, on part of the lines; also absent: PROM1, HSD17B2, GABRP |
| [[GAREM1]] | B | GAREM1 activity raises PPL's level | lines that do not express GAREM1 (10) vs lines expressing it (40) | 2.91× lower at baseline in the lines without GAREM1 | 0.039 | ⚠ within organs, on part of the lines; also absent: TESMIN, GRTP1; maybe low, not absent |
| [[SH2D3A]] | B | SH2D3A activity raises PPL's level | lines that do not express SH2D3A (24) vs lines expressing it (26) | 3.25× lower at baseline in the lines without SH2D3A | 0.043 | ⚠ within organs, on part of the lines; also absent: GRB7, MYO5B, CRB3 |
| [[VAV1]] | B | VAV1 activity raises PPL's level | lines that do not express VAV1 (23) vs lines expressing it (27) | 2.28× lower at baseline in the lines without VAV1 | 0.047 | ⚠ within organs, on part of the lines; also absent: COL4A4, COL4A3, C3; maybe low, not absent |
| [[TMEM184A]] | B | TMEM184A activity raises PPL's level | lines that do not express TMEM184A (8) vs lines expressing it (42) | 4.09× lower at baseline in the lines without TMEM184A | 0.087 | ⚠ within organs, on part of the lines; also absent: ENSG00000267737, ENSG00000284716, GPRC5C; maybe low, not absent |
| [[ACOXL]] | B | ACOXL activity raises PPL's level | lines that do not express ACOXL (28) vs lines expressing it (22) | 2.06× lower at baseline in the lines without ACOXL | 0.092 | ⚠ within organs, on part of the lines; also absent: ILDR1, PRKCH-AS1, LRRN1; maybe low, not absent |
| [[CDC42BPG]] | C | CDC42BPG activity raises PPL's level | lines that do not express CDC42BPG (19) vs lines expressing it (31) | 5.05× lower at baseline in the lines without CDC42BPG | 7e-04 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, PLEKHG6; maybe low, not absent; co-absent with the target |
| [[EPPK1]] | C | EPPK1 activity raises PPL's level | lines that do not express EPPK1 (25) vs lines expressing it (25) | 4.73× lower at baseline in the lines without EPPK1 | 8e-04 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, CLDN3; co-absent with the target |
| [[TJP3]] | C | TJP3 activity raises PPL's level | lines that do not express TJP3 (29) vs lines expressing it (21) | 5.35× lower at baseline in the lines without TJP3 | 0.001 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1; co-absent with the target |
| [[TRIM29]] | C | TRIM29 activity raises PPL's level | lines that do not express TRIM29 (28) vs lines expressing it (22) | 5.12× lower at baseline in the lines without TRIM29 | 0.001 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, TNNT2; co-absent with the target |

### Downstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 9, C 14. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AGFG2]] | B | PPL activity raises AGFG2's level | lines that do not express PPL (19) vs lines expressing it (31) | 1.82× lower at baseline in the lines without PPL | 0.004 | ⚠ within organs, on part of the lines; also absent: EPPK1, SMPDL3B, PLEKHG6 |
| [[GAREM1]] | B | PPL activity raises GAREM1's level | lines that do not express PPL (19) vs lines expressing it (31) | 2.63× lower at baseline in the lines without PPL | 0.008 | ⚠ within organs, on part of the lines; also absent: EPPK1, SMPDL3B, PLEKHG6 |
| [[ABHD11]] | B | PPL activity raises ABHD11's level | lines that do not express PPL (19) vs lines expressing it (31) | 1.96× lower at baseline in the lines without PPL | 0.029 | ⚠ within organs, on part of the lines; also absent: EPPK1, SMPDL3B, PLEKHG6 |
| [[RAP1GAP]] | B | PPL activity raises RAP1GAP's level | lines that do not express PPL (19) vs lines expressing it (31) | 1.65× lower at baseline in the lines without PPL | 0.032 | ⚠ within organs, on part of the lines; also absent: EPPK1, SMPDL3B, PLEKHG6 |
| [[SH2D3A]] | B | PPL activity raises SH2D3A's level | lines that do not express PPL (19) vs lines expressing it (31) | 3.65× lower at baseline in the lines without PPL | 0.053 | ⚠ within organs, on part of the lines; also absent: EPPK1, SMPDL3B, PLEKHG6 |
| [[TMEM184A]] | B | PPL activity raises TMEM184A's level | lines that do not express PPL (19) vs lines expressing it (31) | 2.20× lower at baseline in the lines without PPL | 0.056 | ⚠ within organs, on part of the lines; also absent: EPPK1, SMPDL3B, PLEKHG6 |
| [[KLF5]] | B | PPL activity raises KLF5's level | lines that do not express PPL (19) vs lines expressing it (31) | 3.15× lower at baseline in the lines without PPL | 0.087 | ⚠ within organs, on part of the lines; also absent: EPPK1, SMPDL3B, PLEKHG6 |
| [[JUNB]] | B | PPL activity weakens JUNB's drug response | lines that do not express PPL (18) vs lines expressing it (31) | the lines without PPL respond 1.27× as strongly (z diff -0.78); strongest at Dinaciclib 5 µM: 4.74x vs 2.02x (z diff -3.2) | 0.093 | ⚠ within organs, on part of the lines; also absent: EPPK1, SMPDL3B, PLEKHG6; target measured in part of the lines; both ways; artifact flags |
| [[ELF3-AS1]] | B | PPL activity raises ELF3-AS1's level | lines that do not express PPL (19) vs lines expressing it (31) | 2.55× lower at baseline in the lines without PPL | 0.098 | ⚠ within organs, on part of the lines; also absent: EPPK1, SMPDL3B, PLEKHG6 |
| [[CDC42BPG]] | C | PPL activity raises CDC42BPG's level | lines that do not express PPL (19) vs lines expressing it (31) | 3.33× lower at baseline in the lines without PPL | 0.005 | ⚠ within organs, on part of the lines; also absent: EPPK1, SMPDL3B, PLEKHG6; co-absent with the target |
| [[CGN]] | C | PPL activity raises CGN's level | lines that do not express PPL (19) vs lines expressing it (31) | 3.98× lower at baseline in the lines without PPL | 0.007 | ⚠ within organs, on part of the lines; also absent: EPPK1, SMPDL3B, PLEKHG6; co-absent with the target |
| [[EPPK1]] | C | PPL activity raises EPPK1's level | lines that do not express PPL (19) vs lines expressing it (31) | 3.80× lower at baseline in the lines without PPL | 0.014 | ⚠ within organs, on part of the lines; also absent: EPPK1, SMPDL3B, PLEKHG6; co-absent with the target |

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **-** arm (projection on the module's main direction -0.480). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (10.5, 57.6); signed map (-0.8, 23.8). **Vector** length 93.3, 26.0% of its response variance represented; |z| ≥ 3 in 884 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.0 | +8.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.7 | +8.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.3 | +11.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.4 | +10.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.2 | +7.2 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +1.5 | +1.6 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | +1.5 | +2.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.4 | +0.8 |
|  | [[Infigratinib (drug)]] 0.05 µM |  | +1.4 | +2.7 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -3.9 | -3.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.8 | -7.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | -3.4 | -4.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.1 | -8.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.1 | -7.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | -6.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.2 | -3.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.2 | -3.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.9 | -4.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.8 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | periplakin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:4,882,507-4,960,741 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Plakins; Spectrin repeat containing; SH3 domain containing |
| Reactome | 4 pathways, smallest: Butyrophilin (BTN) family interactions; Formation of the cornified envelope; Keratinization |
| Matched by | ensembl_id |

**Function**, from UniProt [O60437](https://www.uniprot.org/uniprotkb/O60437) (Periplakin):

> Component of the cornified envelope of keratinocytes. May link the cornified envelope to desmosomes and intermediate filaments. May act as a localization signal in PKB/AKT-mediated signaling.

**Summary**, from NCBI Gene [5493](https://www.ncbi.nlm.nih.gov/gene/5493):

> The protein encoded by this gene is a component of desmosomes and of the epidermal cornified envelope in keratinocytes. The N-terminal domain of this protein interacts with the plasma membrane and its C-terminus interacts with intermediate filaments. Through its rod domain, this protein forms complexes with envoplakin. This protein may serve as a link between the cornified envelope and desmosomes as well as intermediate filaments. AKT1/PKB, a protein kinase mediating a variety of cell growth …

**Accessions** — [HGNC:9273](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9273) · Entrez [5493](https://www.ncbi.nlm.nih.gov/gene/5493) · UniProt [O60437](https://www.uniprot.org/uniprotkb/O60437) · Ensembl [ENSG00000118898](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118898)

## Data

Gene col 4024: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4024); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4024, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4024]; `tensor/DDL_lfc|DDL_z.npy` [4024]; `embed/gene_vectors.npy` [4024]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4024 or target_col == 4024). Every well: [[PPL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
