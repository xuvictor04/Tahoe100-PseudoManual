---
symbol: "NBL1"
type: "gene"
col: 8187
ensembl_id: "ENSG00000158747"
name: "NBL1, DAN family BMP antagonist"
location: "1p36.13"
module: 28
arm: "-"
pooled_cpm: 54.78
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 5
n_dd_up_clean: 11
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# NBL1

*NBL1, DAN family BMP antagonist* — 1p36.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 2.04× (z +13.0, q 8e-36, up in 39 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 1.52× (z +8.3, q 2e-14, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.638× (z -8.9, q 3e-16, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MFSD14CP]] (+0.63, fdr 7e-06), [[SENP3]] (+0.60, fdr 3e-05), [[CTC-338M12.4]] (+0.57, fdr 1e-05); moves opposite to [[GOLGB1]] (-0.62, fdr 1e-05), [[SNAPIN]] (-0.60, fdr 1e-05), [[CREB3]] (-0.57, fdr 1e-05).
> It sits in the **-** arm of [[Module 028]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8187.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.04×** | +13.0 | 8e-36 | 39/44 (NCI-H460, SW480, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.96×** | +12.7 | 1e-34 | 45/47 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.69×** | +10.3 | 8e-23 | 38/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.65×** | +9.8 | 2e-20 | 32/48 (LoVo, LS 180, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.52×** | +8.3 | 2e-14 | 32/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +7.8 | 7e-13 | 28/48 (NCI-H460, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.45×** | +7.3 | 2e-11 | 33/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.99×** | +7.1 | 9e-11 | 35/49 (PANC-1, A498, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +7.0 | 2e-10 | 24/41 (LoVo, KATO III, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.38×** | +6.3 | 2e-08 | 29/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +6.2 | 4e-08 | 28/47 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.78×** | +5.9 | 2e-07 | 24/35 (SW480, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.32×** | +5.5 | 2e-06 | 29/48 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.29×** | +5.1 | 2e-05 | 26/47 (NCI-H2347, A498, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.59×** | +4.8 | 7e-05 | 21/48 (PANC-1, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +4.5 | 2e-04 | 21/48 (HT-29, SW480, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.38×** | +4.5 | 2e-04 | 25/47 (LoVo, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.27×** | +3.4 | 0.021 | 16/48 (KATO III, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8187.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.638×** | -8.9 | 3e-16 | 33/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.780×** | -7.0 | 8e-10 | 26/48 (LoVo, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.717×** | -6.6 | 8e-09 | 31/48 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.756×** | -5.6 | 4e-06 | 26/48 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.830×** | -3.7 | 0.023 | 21/48 (RKO, HS-578T, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.839× | -3.5 | 0.045 | 16/48 (SW480, KATO III, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.844× | -3.3 | 0.085 | 15/47 (SK-MEL-2, SW480, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.845× | -3.2 | 0.085 | 15/47 (HOP62, A498, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.859× | -3.0 | 0.14 | 11/47 (SK-MEL-2, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.860× | -3.0 | 0.14 | 14/48 (H4, LS 180, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8187. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 39.5 | 10 (7 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.43× (z +13.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.34× (z +13.2) | — |
| [[SW480 (line)]] | alt | 51.6 | 6 (3 ⚠) | 2 | [[Digitoxin (drug)]] 5 µM 3.01× (z +14.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.95× (z +14.4) | [[Homoharringtonine (drug)]] 5 µM 0.574× (z -10.5) |
| [[LoVo (line)]] | wt | 76.4 | 4 (4 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.43× (z +13.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -16.7) |
| [[LS 180 (line)]] | wt | 121 | 3 (2 ⚠) | 2 | [[Digitoxin (drug)]] 5 µM 2.63× (z +10.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.46× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.558× (z -9.0) |
| [[PANC-1 (line)]] | alt | 55.2 | 5 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.37× (z +11.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.01× (z +9.1) | — |
| [[KATO III (line)]] | alt | 87.3 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.70× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -9.9) |
| [[RPMI-7951 (line)]] | alt | 157 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -11.3) |
| [[A-427 (line)]] | wt | 50.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.23× (z +8.5) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 33.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -10.0) |
| [[CFPAC-1 (line)]] | alt | 54.8 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.54× (z +8.6) ⚠ toxic | — |
| [[HepG2_C3A (line)]] | wt | 82.6 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.88× (z +9.6) ⚠ toxic | — |
| [[HT-29 (line)]] | alt | 42.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.523× (z -8.8) |
| [[NCI-H1573 (line)]] | alt | 35.4 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.68× (z +10.3) ⚠ toxic | — |
| [[NCI-H1792 (line)]] | alt | 50.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.486× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 52.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.76× (z +8.7) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 65.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.523× (z -9.2) |
| [[SNU-1 (line)]] | wt | 45.6 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.57× (z +8.9) ⚠ toxic | — |
| [[A-172 (line)]] | wt | 32.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 59.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 39.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 60.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 81.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 68.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 39.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 79.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 74.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 54.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 72.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 60.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8187), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MFSD14CP]] | +0.63 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[SENP3]] | +0.60 | +0.66 / +0.45 | both halves | 3e-05 |  |
| [[CTC-338M12.4]] | +0.57 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[ADAT3]] | +0.57 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[NUP42]] | +0.56 | +0.43 / +0.52 | both halves | 4e-05 |  |
| [[AMFR]] | +0.56 | +0.67 / +0.44 | both halves | 3e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[CMAHP]] | +0.56 | +0.38 / +0.42 | both halves | 7e-05 |  |
| [[SMPD4BP]] | +0.54 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[ATPAF2]] | +0.54 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[NADK]] | +0.54 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[TIMM23B]] | +0.54 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[ECI1]] | +0.54 | +0.40 / +0.54 | both halves | 4e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GOLGB1]] | -0.62 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[SNAPIN]] | -0.60 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[CREB3]] | -0.57 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[TRMT1L]] | -0.56 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[DARS1]] | -0.55 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[CEP350]] | -0.54 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[ZRANB1]] | -0.53 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[LYSMD3]] | -0.53 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[TRIP11]] | -0.53 | -0.63 / -0.60 | both halves | 7e-06 |  |
| [[THAP5]] | -0.52 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[ASF1A]] | -0.52 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[ARCN1]] | -0.51 | -0.59 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **-** arm (projection on the module's main direction -0.424). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-31.4, 0.8); signed map (-41.9, -26.2). **Vector** length 103, 25.8% of its response variance represented; |z| ≥ 3 in 972 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +8.9 | +12.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.9 | +13.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +7.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +10.3 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +5.7 | +5.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.9 | +4.5 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +3.6 | +5.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.9 | +4.8 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.9 | +2.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.6 | +1.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.4 | -8.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.4 | -3.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.2 | -2.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.9 | -7.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.8 | -3.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.3 | -1.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.2 | -0.9 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.8 | -1.4 |
|  | [[Methylthiouracil (drug)]] 5 µM |  | -1.8 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | NBL1, DAN family BMP antagonist |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.13 — chr1:19,596,979-19,658,456 (+) |
| Ensembl biotype | protein_coding |
| Also known as | D1S1733E, NB, DAN, NO3, DAND1 |
| Gene groups (HGNC) | DAN family |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Matched by | ensembl_id |

**Function**, from UniProt [P41271](https://www.uniprot.org/uniprotkb/P41271) (Neuroblastoma suppressor of tumorigenicity 1):

> Possible candidate as a tumor suppressor gene of neuroblastoma. May play an important role in preventing cells from entering the final stage (G1/S) of the transformation process.

**Summary**, from NCBI Gene [4681](https://www.ncbi.nlm.nih.gov/gene/4681):

> This gene product is the founding member of the evolutionarily conserved CAN (Cerberus and DAN) family of proteins, which contain a domain resembling the CTCK (C-terminal cystine knot-like) motif found in a number of signaling molecules. These proteins are secreted, and act as BMP (bone morphogenetic protein) antagonists by binding to BMPs and preventing them from interacting with their receptors. They may thus play an important role during growth and development. Alternatively spliced …

**Accessions** — [HGNC:7650](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7650) · Entrez [4681](https://www.ncbi.nlm.nih.gov/gene/4681) · UniProt [P41271](https://www.uniprot.org/uniprotkb/P41271) · Ensembl [ENSG00000158747](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158747)

## Data

Gene col 8187: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8187); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8187, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8187]; `tensor/DDL_lfc|DDL_z.npy` [8187]; `embed/gene_vectors.npy` [8187]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8187 or target_col == 8187). Every well: [[NBL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NBL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
