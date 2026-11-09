---
symbol: "SRSF10"
type: "gene"
col: 12020
ensembl_id: "ENSG00000188529"
name: "serine and arginine rich splicing factor 10"
location: "1p36.11"
module: 3
arm: "-"
pooled_cpm: 102.62
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# SRSF10

*serine and arginine rich splicing factor 10* — 1p36.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.98× (z +42.3, q 0e+00, up in 47 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (LS 180 0.404×, LoVo 0.527×, SW480 0.643×, HT-29 0.575×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Binimetinib (drug)]] 0.05 µM in 1 line (SW480 0.715×); [[Trametinib (drug)]] 5 µM in 1 line (SW480 0.651×; ⚠ cell-cycle shift, explains ~50% of this change); [[Binimetinib (drug)]] 0.5 µM in 1 line (SW480 0.686×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HNRNPD]] (+0.72, fdr 7e-06), [[BCLAF1]] (+0.68, fdr 7e-06), [[SRSF1]] (+0.64, fdr 1e-05); moves opposite to [[RPL28]] (-0.66, fdr 7e-06), [[MTM1]] (-0.65, fdr 1e-05), [[MPG]] (-0.65, fdr 1e-05).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[FAM111A]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 17 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12020.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.98×** | +42.3 | 0e+00 | 47/48 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.62×** | +26.3 | 0e+00 | 48/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.44×** | +23.5 | 0e+00 | 48/48 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.33×** | +21.5 | 0e+00 | 45/45 (PANC-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.14×** | +20.8 | 0e+00 | 46/49 (NCI-H1573, KATO III, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.97×** | +17.8 | 0e+00 | 43/44 (PANC-1, HT-29, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.89×** | +17.4 | 0e+00 | 44/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.89×** | +17.4 | 0e+00 | 45/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.51×** | +11.2 | 2e-27 | 42/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.50×** | +11.0 | 2e-26 | 40/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.46×** | +10.2 | 6e-23 | 39/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.39×** | +9.0 | 8e-18 | 36/48 (HS-578T, MIA PaCa-2, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.83×** | +8.6 | 3e-16 | 37/49 (PANC-1, HS-578T, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **1.37×** | +8.3 | 4e-15 | 35/47 (COLO 205, PANC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.31×** | +7.0 | 1e-10 | 32/47 (HepG2/C3A, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.25×** | +6.1 | 3e-08 | 32/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.24×** | +5.9 | 1e-07 | 25/48 (SNU-423, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.45×** | +5.3 | 4e-06 | 24/48 (HEC-1-A, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.19× | +4.7 | 7e-05 | 18/48 (PANC-1, LOX-IMVI, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.018 | 13/48 (SHP-77, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[AZD-7648 (drug)]] 0.5 µM |  | 1.17× | +3.0 | 0.060 | 5/48 (HT-29, SW48, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | 1.16× | +2.9 | 0.067 | 12/48 (HOP62, SW480, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12020.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (LS 180 0.404×, LoVo 0.527×, SW480 0.643×, HT-29 0.575×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Binimetinib (drug)]] 0.05 µM in 1 line (SW480 0.715×); [[Trametinib (drug)]] 5 µM in 1 line (SW480 0.651×; ⚠ cell-cycle shift, explains ~50% of this change); [[Binimetinib (drug)]] 0.5 µM in 1 line (SW480 0.686×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.886× | -4.7 | 0.001 | 21/49 (LS 180, LoVo, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.867× | -3.9 | 0.016 | 15/47 (LS 180, SK-MEL-2, …) | two highest doses | low cells (technical?) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | 0.860× | -3.9 | 0.016 | 16/50 (SW480, LS 180, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 0.894× | -3.1 | 0.28 | 13/48 (LoVo, LS 180, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12020. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 84.5 | 14 (9 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +21.1) | — |
| [[PANC-1 (line)]] | alt | 110 | 11 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +33.8) | — |
| [[LoVo (line)]] | wt | 106 | 8 (5 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.00× (z +29.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.527× (z -13.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 63.1 | 8 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.41× (z +25.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.527× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 190 | 7 (4 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +15.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.643× (z -13.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 108 | 8 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +28.4) | — |
| [[HT-29 (line)]] | alt | 144 | 7 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +23.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.575× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 108 | 8 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +17.5) | — |
| [[LS 180 (line)]] | wt | 108 | 6 (3 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +15.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.404× (z -16.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 100 | 8 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +16.3) | — |
| [[AsPC-1 (line)]] | alt | 84.7 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +25.4) | — |
| [[HEC-1-A (line)]] | alt | 117 | 6 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +22.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.630× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 136 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.17× (z +27.7) | — |
| [[HS-578T (line)]] | alt | 132 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +21.3) | — |
| [[NCI-H1792 (line)]] | alt | 73.1 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +21.4) | — |
| [[SNU-423 (line)]] | alt | 69.9 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.01× (z +26.0) | — |
| [[A498 (line)]] | wt | 87.6 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +19.9) | — |
| [[A549 (line)]] | wt | 61.1 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +21.0) | — |
| [[C32 (line)]] | wt | 69.4 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.95× (z +22.0) | — |
| [[J82 (line)]] | alt | 128 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +29.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 72.5 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +13.3) | — |
| [[A-172 (line)]] | wt | 59.7 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +17.3) | — |
| [[BT-474 (line)]] | alt | 74.9 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +15.1) | — |
| [[CFPAC-1 (line)]] | alt | 104 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +23.2) | — |
| [[LOX-IMVI (line)]] | wt | 79.1 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +21.4) | — |
| [[NCI-H2030 (line)]] | alt | 108 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +22.9) | — |
| [[Panc 03.27 (line)]] | alt | 59.4 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +15.5) | — |
| [[RPMI-7951 (line)]] | alt | 102 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +19.5) | — |
| [[SW1417 (line)]] | alt | 97.9 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +19.0) | — |
| [[C-33 A (line)]] | alt | 185 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +16.9) | — |
| [[COLO 205 (line)]] | alt | 95.9 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +21.3) | — |
| [[Hs 766T (line)]] | wt | 93.6 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +17.0) | — |
| [[hTERT-HPNE (line)]] | wt | 79.9 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +19.4) | — |
| [[RKO (line)]] | wt | 102 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +10.8) | — |
| [[SK-MEL-2 (line)]] | alt | 84.1 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +22.2) | — |
| [[H4 (line)]] | wt | 92.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +15.5) | — |
| [[NCI-H23 (line)]] | alt | 146 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +15.2) | — |
| [[NCI-H2347 (line)]] | alt | 87.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +19.2) | — |
| [[SHP-77 (line)]] | alt | 110 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.85× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.98× (z +12.3) | — |
| [[SW48 (line)]] | wt | 108 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +9.9) | — |
| [[A-427 (line)]] | wt | 106 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.05× (z +11.7) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 130 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +18.8) | — |
| [[SNU-1 (line)]] | wt | 106 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +9.7) | — |
| [[AN3 CA (line)]] | alt | 105 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +10.8) | — |
| [[CHP-212 (line)]] | wt | 64.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 87.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 85.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12020), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*33 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPD]] | +0.72 | +0.62 / +0.69 | both halves | 7e-06 | same gene group; pathway: HALLMARK_G2M_CHECKPOINT; STRING 606 |
| [[BCLAF1]] | +0.68 | +0.60 / +0.68 | both halves | 7e-06 | STRING 732 |
| [[SRSF1]] | +0.64 | +0.54 / +0.60 | both halves | 1e-05 | same gene group; pathway: HALLMARK_G2M_CHECKPOINT; STRING 999 |
| [[SFPQ]] | +0.64 | +0.52 / +0.64 | both halves | 1e-05 | same gene group; pathway: HALLMARK_G2M_CHECKPOINT; STRING 652 |
| [[SRSF6]] | +0.63 | +0.53 / +0.62 | both halves | 1e-05 | same gene group; pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 754 |
| [[HNRNPL]] | +0.60 | +0.42 / +0.56 | both halves | 4e-05 | same gene group; pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 845 |
| [[SREK1]] | +0.59 | +0.56 / +0.52 | both halves | 1e-05 | same gene group; STRING 850 |
| [[ANKRD18A]] | +0.59 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[ABCE1]] | +0.59 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[FUBP1]] | +0.58 | +0.39 / +0.55 | both halves | 6e-05 |  |
| [[EWSR1]] | +0.58 | +0.36 / +0.59 | both halves | 1e-04 | same gene group; pathway: HALLMARK_G2M_CHECKPOINT; STRING 752 |
| [[TIA1]] | +0.58 | +0.55 / +0.52 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*67 of its nearest partners move opposite, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL28]] | -0.66 | -0.64 / -0.61 | both halves | 7e-06 |  |
| [[MTM1]] | -0.65 | -0.50 / -0.65 | both halves | 1e-05 |  |
| [[MPG]] | -0.65 | -0.53 / -0.67 | both halves | 1e-05 |  |
| [[RABAC1]] | -0.64 | -0.49 / -0.70 | both halves | 1e-05 |  |
| [[TRPT1]] | -0.64 | -0.49 / -0.64 | both halves | 1e-05 |  |
| [[KLHL7]] | -0.63 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[UBA52]] | -0.63 | -0.54 / -0.62 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[GUK1]] | -0.63 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[RPL12]] | -0.63 | -0.63 / -0.58 | both halves | 7e-06 |  |
| [[RAB6A]] | -0.62 | -0.61 / -0.58 | both halves | 7e-06 |  |
| [[TUSC2]] | -0.61 | -0.44 / -0.61 | both halves | 3e-05 |  |
| [[COMMD6]] | -0.61 | -0.46 / -0.61 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM111A]] | C | FAM111A activity weakens SRSF10's drug response | lines that do not express FAM111A (3) vs lines expressing it (46) | the lines without FAM111A respond 1.07× as strongly (z diff -1.85); strongest at Harringtonine 5 µM: 2.64x vs 2.52x (z diff -4.1) | 5e-04 | ⚠ few lines (3 vs 47); across organs; also absent: FXYD5, ACCS, TFAP2A; maybe low, not absent; target measured in part of the lines; rests on the correction; artifact flags |
| [[FAM219A]] | C | FAM219A activity lowers SRSF10's level | lines that do not express FAM219A (3) vs lines expressing it (47) | 1.28× higher at baseline in the lines without FAM219A | 0.096 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SH3PXD2A, METRNL; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.646). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-38.3, -25.4); signed map (14.1, -38.1). **Vector** length 94.0, 28.1% of its response variance represented; |z| ≥ 3 in 1,248 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Dengue Virus-Host Interactions* (reactome, mean cos +0.51 to 12); *MYC targets v1* (hallmark, mean cos +0.51 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.5 | +21.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.9 | +26.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +5.7 | +20.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +5.5 | +17.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.8 | +42.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.0 | +1.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +6.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.2 | -0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +9.0 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | +2.0 | +1.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.9 | -4.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.3 | +0.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.0 | -2.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.8 | -1.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | -2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.6 | +0.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.0 | -0.1 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -2.7 | +1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | +4.7 |

## What is on record

|  |  |
|---|---|
| Name | serine and arginine rich splicing factor 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:23,964,347-23,980,927 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TASR1, TASR2, SRp38, SRrp40, SFRS13, PPP1R149; previously FUSIP2, FUSIP1, SFRS13A |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; RNA binding motif containing; Serine and arginine rich splicing factors |
| Hallmark sets | G2M_CHECKPOINT |
| Reactome | 6 pathways, smallest: mRNA Polyadenylation; mRNA 3'-end processing; mRNA Splicing - Major Pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [O75494](https://www.uniprot.org/uniprotkb/O75494) (Serine/arginine-rich splicing factor 10):

> Splicing factor that in its dephosphorylated form acts as a general repressor of pre-mRNA splicing. Seems to interfere with the U1 snRNP 5'-splice recognition of SNRNP70. Required for splicing repression in M-phase cells and after heat shock. Also acts as a splicing factor that specifically promotes exon skipping during alternative splicing. Interaction with YTHDC1, a RNA-binding protein that recognizes and binds N6-methyladenosine (m6A)-containing RNAs, prevents SRSF10 from binding to its …

**Summary**, from NCBI Gene [10772](https://www.ncbi.nlm.nih.gov/gene/10772):

> This gene product is a member of the serine-arginine (SR) family of proteins, which are involved in constitutive and regulated RNA splicing. Members of this family are characterized by N-terminal RNP1 and RNP2 motifs, which are required for binding to RNA, and multiple C-terminal SR/RS repeats, which are important in mediating association with other cellular proteins. This protein interacts with the oncoprotein TLS, and abrogates the influence of TLS on adenovirus E1A pre-mRNA splicing. This …

**Accessions** — [HGNC:16713](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16713) · Entrez [10772](https://www.ncbi.nlm.nih.gov/gene/10772) · UniProt [O75494](https://www.uniprot.org/uniprotkb/O75494) · Ensembl [ENSG00000188529](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188529)

## Data

Gene col 12020: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12020); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12020, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12020]; `tensor/DDL_lfc|DDL_z.npy` [12020]; `embed/gene_vectors.npy` [12020]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12020 or target_col == 12020). Every well: [[SRSF10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SRSF10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
