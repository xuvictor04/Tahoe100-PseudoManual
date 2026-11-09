---
symbol: "ZHX1"
type: "gene"
col: 9077
ensembl_id: "ENSG00000165156"
name: "zinc fingers and homeoboxes 1"
location: "8q24.13"
module: 130
arm: "+"
pooled_cpm: 40.85
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 5
n_dd_up_clean: 14
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/130"]
generated_by: "tahoemap"
---

# ZHX1

*zinc fingers and homeoboxes 1* — 8q24.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (16 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.23× (z +24.8, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.816× (z -6.3, q 1e-07, down in 23 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CMC4]] (+0.60, fdr 2e-05), [[DECR1]] (+0.58, fdr 7e-06), [[NFYB]] (+0.58, fdr 1e-05); moves opposite to [[RRP7BP]] (-0.60, fdr 1e-05), [[ANKS6]] (-0.58, fdr 1e-05), [[ZNF544]] (-0.58, fdr 3e-05).
> It is in [[Module 130]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 17 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9077.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.23×** | +24.8 | 0e+00 | 47/48 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.92×** | +20.2 | 0e+00 | 44/47 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.87×** | +12.5 | 1e-33 | 37/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.81×** | +12.5 | 1e-33 | 37/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.61×** | +10.4 | 3e-23 | 35/44 (NCI-H2347, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.51×** | +9.0 | 2e-17 | 32/48 (RKO, PANC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +8.9 | 6e-17 | 33/48 (SW1417, HOP62, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.45×** | +8.2 | 2e-14 | 29/48 (SW480, KATO III, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.43×** | +7.8 | 6e-13 | 31/47 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.43×** | +7.5 | 4e-12 | 24/38 (PANC-1, H4, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.34×** | +6.3 | 1e-08 | 27/48 (LoVo, RKO, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.34×** | +6.2 | 2e-08 | 27/47 (SK-MEL-2, NCI-H2030, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.32×** | +6.1 | 4e-08 | 25/48 (RKO, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.33×** | +5.9 | 1e-07 | 27/48 (NCI-H23, PANC-1, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.31×** | +5.9 | 1e-07 | 22/47 (KATO III, SW480, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.60×** | +5.4 | 3e-06 | 20/48 (PANC-1, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.28×** | +5.2 | 6e-06 | 24/47 (C32, HS-578T, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.21×** | +5.1 | 1e-05 | 20/48 (C32, MIA PaCa-2, …) | two highest doses | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.49×** | +4.5 | 1e-04 | 14/46 (LOX-IMVI, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.25×** | +4.5 | 2e-04 | 19/48 (A498, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.18× | +4.2 | 7e-04 | 13/48 (C32, NCI-H460, …) | two highest doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.21×** | +4.1 | 9e-04 | 16/47 (C32, PANC-1, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 1.19× | +3.8 | 0.003 | 16/49 (C32, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[AZD-7648 (drug)]] 5 µM |  | **1.33×** | +3.3 | 0.019 | 8/46 (C32, NCI-H460, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9077.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.816×** | -6.3 | 1e-07 | 23/48 (HT-29, A498, …) | all doses, stronger at high dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.669×** | -6.3 | 1e-07 | 26/46 (HCT15, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.775×** | -5.1 | 6e-05 | 25/48 (HT-29, A498, …) | all doses, stronger at high dose |  |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | 0.837× | -3.9 | 0.015 | 17/47 (SW 1271, HCT15, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.855× | -3.4 | 0.069 | 18/48 (HT-29, HOP62, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.747×** | -3.3 | 0.081 | 10/48 (BT-474, AN3 CA, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **0.755×** | -3.2 | 0.089 | 7/48 (BT-474, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.864× | -3.2 | 0.089 | 12/47 (HT-29, RPMI-7951, …) | top dose only |  |
| [[Baicalin (drug)]] 5 µM |  | 0.904× | -3.1 | 0.089 | 2/48 (HCT15, MIA PaCa-2) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.867× | -3.1 | 0.089 | 15/48 (HT-29, PANC-1, …) | rises with dose |  |
| [[Hydroxyurea (drug)]] 0.05 µM |  | 0.857× | -3.1 | 0.089 | 15/47 (NCI-H661, LS 180, …) | inconsistent across doses |  |
| [[Pravastatin (sodium) (drug)]] 0.05 µM |  | 0.858× | -3.1 | 0.089 | 10/47 (SW 1271, A-427, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9077. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 151 | 2 | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +13.2) | [[Bortezomib (drug)]] 0.05 µM 0.350× (z -12.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.467× (z -9.3) |
| [[PANC-1 (line)]] | alt | 28.5 | 6 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.36× (z +18.0) | — |
| [[SW480 (line)]] | alt | 38.0 | 6 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +14.5) | — |
| [[KATO III (line)]] | alt | 42.5 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +12.8) | — |
| [[HEC-1-A (line)]] | alt | 41.8 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +13.4) | — |
| [[SW1417 (line)]] | alt | 66.6 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +14.9) | — |
| [[A498 (line)]] | wt | 61.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +14.5) | — |
| [[A549 (line)]] | wt | 35.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +11.4) | — |
| [[AsPC-1 (line)]] | alt | 64.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.340× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[C-33 A (line)]] | alt | 22.6 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +9.0) | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.109× (z -10.8) |
| [[C32 (line)]] | wt | 26.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +9.3) | — |
| [[HOP62 (line)]] | alt | 36.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +11.2) | — |
| [[LS 180 (line)]] | wt | 30.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +11.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 22.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.95× (z +10.6) | — |
| [[NCI-H1573 (line)]] | alt | 30.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +10.6) | — |
| [[NCI-H2030 (line)]] | alt | 36.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +15.1) | — |
| [[NCI-H2347 (line)]] | alt | 54.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +11.4) | — |
| [[NCI-H460 (line)]] | wt | 27.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +12.6) | — |
| [[BT-474 (line)]] | alt | 36.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +10.0) | — |
| [[CFPAC-1 (line)]] | alt | 30.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +8.9) | — |
| [[COLO 205 (line)]] | alt | 35.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.09× (z +10.9) | — |
| [[HCT15 (line)]] | alt | 39.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +9.6) | — |
| [[Hs 766T (line)]] | wt | 49.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +9.4) | — |
| [[HS-578T (line)]] | alt | 63.9 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.148× (z -9.8) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[J82 (line)]] | alt | 25.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +10.5) | — |
| [[LoVo (line)]] | wt | 20.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +10.6) | — |
| [[LOX-IMVI (line)]] | wt | 62.6 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0891× (z -14.7) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 20.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +8.9) | — |
| [[Panc 03.27 (line)]] | alt | 45.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +12.5) | — |
| [[RPMI-7951 (line)]] | alt | 42.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +10.6) | — |
| [[SHP-77 (line)]] | alt | 68.8 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.101× (z -12.4) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 21.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.21× (z +12.3) | — |
| [[SNU-423 (line)]] | alt | 19.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +9.4) | — |
| [[SW 900 (line)]] | alt | 37.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +8.5) | — |
| [[A-172 (line)]] | wt | 43.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 61.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 36.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 55.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 76.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 52.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9077), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CMC4]] | +0.60 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[DECR1]] | +0.58 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[NFYB]] | +0.58 | +0.62 / +0.49 | both halves | 1e-05 | STRING 619 |
| [[ACBD5]] | +0.57 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[EMC7]] | +0.57 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[LNPEP]] | +0.57 | +0.38 / +0.53 | both halves | 7e-05 |  |
| [[UBR5]] | +0.56 | +0.43 / +0.54 | both halves | 4e-05 |  |
| [[ARFGAP2]] | +0.55 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[LRRC57]] | +0.55 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[TET2]] | +0.54 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[BMI1]] | +0.54 | +0.62 / +0.43 | both halves | 3e-05 |  |
| [[NCOA4]] | +0.53 | +0.59 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRP7BP]] | -0.60 | -0.63 / -0.50 | both halves | 1e-05 |  |
| [[ANKS6]] | -0.58 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[ZNF544]] | -0.58 | -0.45 / -0.54 | both halves | 3e-05 | same gene group |
| [[PRR5-ARHGAP8]] | -0.55 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[SGSM1]] | -0.53 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[CUTC]] | -0.53 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[RRP7BP-1]] | -0.53 | -0.40 / -0.54 | both halves | 4e-05 |  |
| [[GP6-AS1]] | -0.52 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[WDR59]] | -0.52 | -0.57 / -0.39 | both halves | 6e-05 |  |
| [[TOMM5]] | -0.52 | -0.59 / -0.31 | both halves | 2e-04 |  |
| [[NEIL2]] | -0.51 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[ETV5]] | -0.51 | -0.47 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ZHX1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MCOLN2]] | B | MCOLN2 activity lowers ZHX1's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 1.33× higher at baseline in the lines without MCOLN2 | 0.085 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |
| [[AKT1]], [[AKT2]], [[AKT3]] | B | AKT1, AKT2, AKT3 activity raises ZHX1's level | compounds that target AKT1, AKT2, AKT3: 2 of 3 lower it (BAY1125976, Ipatasertib) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 130]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.612). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (3.1, -26.9); signed map (13.4, -14.0). **Vector** length 94.3, 21.6% of its response variance represented; |z| ≥ 3 in 1,059 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.1 | +24.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.7 | +20.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.5 | +12.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.6 | +5.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.5 | +5.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.4 | +4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.2 | +3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.1 | +3.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.0 | -6.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | -4.9 | -5.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -4.6 | +6.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -4.1 | +6.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.3 | -6.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.2 | +1.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.4 | -2.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.3 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | zinc fingers and homeoboxes 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.13 — chr8:123,248,451-123,275,541 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Zinc fingers C2H2-type; ZF class homeoboxes and pseudogenes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UKY1](https://www.uniprot.org/uniprotkb/Q9UKY1) (Zinc fingers and homeoboxes protein 1):

> Acts as a transcriptional repressor. Increases DNMT3B-mediated repressive transcriptional activity when DNMT3B is tethered to DNA. May link molecule between DNMT3B and other co-repressor proteins.

**Summary**, from NCBI Gene [11244](https://www.ncbi.nlm.nih.gov/gene/11244):

> The members of the zinc fingers and homeoboxes gene family are nuclear homodimeric transcriptional repressors that interact with the A subunit of nuclear factor-Y (NF-YA) and contain two C2H2-type zinc fingers and five homeobox DNA-binding domains. This gene encodes member 1 of this gene family. In addition to forming homodimers, this protein heterodimerizes with members 2 and 3 of the zinc fingers and homeoboxes family. Alternative splicing results in multiple transcript variants. Read-through …

**Accessions** — [HGNC:12871](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12871) · Entrez [11244](https://www.ncbi.nlm.nih.gov/gene/11244) · UniProt [Q9UKY1](https://www.uniprot.org/uniprotkb/Q9UKY1) · Ensembl [ENSG00000165156](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165156)

## Data

Gene col 9077: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9077); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9077, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9077]; `tensor/DDL_lfc|DDL_z.npy` [9077]; `embed/gene_vectors.npy` [9077]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9077 or target_col == 9077). Every well: [[ZHX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZHX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
