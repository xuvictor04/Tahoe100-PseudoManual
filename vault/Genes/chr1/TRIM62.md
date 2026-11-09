---
symbol: "TRIM62"
type: "gene"
col: 3803
ensembl_id: "ENSG00000116525"
name: "tripartite motif containing 62"
location: "1p35.1"
module: 3
arm: "+"
pooled_cpm: 13.9
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 12
n_dd_up_clean: 11
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# TRIM62

*tripartite motif containing 62* — 1p35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.95× (z +16.6, q 0e+00, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.402× (z -12.9, q 3e-35, down in 28 of 32 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.536× (z -9.6, q 2e-19, down in 29 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAB40C]] (+0.71, fdr 1e-05), [[CARHSP1]] (+0.71, fdr 1e-05), [[CBFA2T2]] (+0.70, fdr 7e-06); moves opposite to [[TASOR]] (-0.69, fdr 7e-06), [[KICS2]] (-0.68, fdr 1e-05), [[HDHD2]] (-0.66, fdr 1e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3803.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.95×** | +16.6 | 0e+00 | 41/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.78×** | +15.7 | 0e+00 | 41/47 (PANC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.60×** | +14.6 | 0e+00 | 40/47 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +10.5 | 1e-23 | 27/46 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.92×** | +10.0 | 2e-21 | 36/45 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.78×** | +8.8 | 1e-16 | 32/47 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.12×** | +6.0 | 2e-07 | 24/38 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.41×** | +5.0 | 5e-05 | 17/46 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.84×** | +4.9 | 7e-05 | 18/47 (PANC-1, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.78×** | +4.6 | 2e-04 | 11/44 (SW480, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.33×** | +4.3 | 8e-04 | 18/47 (LoVo, H4, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.23×** | +3.1 | 0.084 | 5/47 (A-172, A-427, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.087 | 7/48 (LoVo, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3803.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.402×** | -12.9 | 3e-35 | 28/32 (SK-MEL-2, SW480, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.446×** | -12.3 | 2e-32 | 27/39 (SW1417, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.536×** | -9.6 | 2e-19 | 29/44 (LOX-IMVI, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.546×** | -8.9 | 8e-17 | 31/46 (C32, SNU-423, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.549×** | -8.8 | 1e-16 | 14/23 (C32, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.633×** | -7.0 | 3e-10 | 26/47 (C32, LoVo, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.501×** | -5.5 | 2e-06 | 24/46 (A498, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.807×** | -4.6 | 3e-04 | 21/46 (SK-MEL-2, C32, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **0.753×** | -4.3 | 9e-04 | 18/43 (Panc 03.27, HCT15, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.774×** | -3.9 | 0.005 | 15/47 (C32, Panc 03.27, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.631×** | -3.7 | 0.012 | 16/43 (Panc 03.27, SW1417, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.859× | -3.3 | 0.048 | 19/47 (C32, SK-MEL-2, …) | top dose only | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~19% of this change | **0.801×** | -3.3 | 0.048 | 17/42 (C32, SK-MEL-2, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.948× | -3.1 | 0.079 | 3/48 (A-172, SW 1088, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3803. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 45.9 | 0 | 10 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0689× (z -17.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.139× (z -13.5) |
| [[SK-MEL-2 (line)]] | alt | 49.2 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0835× (z -18.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 22.3 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.116× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.191× (z -11.1) |
| [[SW480 (line)]] | alt | 11.7 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.38× (z +9.7) | [[Dinaciclib (drug)]] 0.05 µM 0.0922× (z -17.5) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 18.7 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +8.9) | [[Ixazomib (drug)]] 0.05 µM 0.213× (z -9.1) |
| [[LoVo (line)]] | wt | 11.6 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 4.43× (z +9.0) | [[Harringtonine (drug)]] 5 µM 0.177× (z -10.0) |
| [[MIA PaCa-2 (line)]] | alt | 18.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.159× (z -12.4) |
| [[PANC-1 (line)]] | alt | 9.39 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.54× (z +10.9) | — |
| [[BT-474 (line)]] | alt | 19.5 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.200× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Peretinoin (drug)]] 5 µM 0.216× (z -8.9) |
| [[SW1417 (line)]] | alt | 21.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.113× (z -15.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 8.07 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0817× (z -11.1) |
| [[A498 (line)]] | wt | 7.00 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.170× (z -8.9) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 17.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -10.2) ⚠ cell-cycle shift, explains ~64% of this change |
| [[HOP62 (line)]] | alt | 10.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +9.2) | — |
| [[HS-578T (line)]] | alt | 20.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.109× (z -12.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 14.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.199× (z -8.7) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 12.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.156× (z -8.6) |
| [[J82 (line)]] | alt | 19.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -10.0) ⚠ cell-cycle shift, explains ~64% of this change |
| [[KATO III (line)]] | alt | 12.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -11.4) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 14.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.123× (z -12.5) |
| [[LS 180 (line)]] | wt | 12.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.146× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 7.29 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.104× (z -10.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 13.3 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.101× (z -13.0) ⚠ transcription drop; cell-cycle shift, explains ~31% of this change |
| [[SHP-77 (line)]] | alt | 23.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.132× (z -10.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 17.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0829× (z -10.8) |
| [[A-172 (line)]] | wt | 7.21 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.77 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.38 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.74 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.15 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3803), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB40C]] | +0.71 | +0.57 / +0.69 | both halves | 1e-05 |  |
| [[CARHSP1]] | +0.71 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[CBFA2T2]] | +0.70 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[UBTD1]] | +0.70 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[MAP3K9]] | +0.70 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[ANKRD9]] | +0.70 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[LIN7B]] | +0.69 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[NENF]] | +0.69 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[RALGDS]] | +0.69 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[STK32C]] | +0.68 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[SNTA1]] | +0.67 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[SAP130]] | +0.66 | +0.53 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TASOR]] | -0.69 | -0.61 / -0.59 | both halves | 7e-06 |  |
| [[KICS2]] | -0.68 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[HDHD2]] | -0.66 | -0.49 / -0.63 | both halves | 1e-05 |  |
| [[ZNF655]] | -0.66 | -0.46 / -0.65 | both halves | 3e-05 |  |
| [[ST7L]] | -0.66 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[YWHAE]] | -0.64 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[GUF1]] | -0.64 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[SRSF1]] | -0.63 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[CLHC1]] | -0.62 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[CPNE1]] | -0.62 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[ICE2]] | -0.62 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[NEK9]] | -0.62 | -0.47 / -0.51 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.773). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (3.8, -3.7); signed map (-31.6, 17.1). **Vector** length 98.8, 22.2% of its response variance represented; |z| ≥ 3 in 987 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +4.8 | +10.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.5 | +14.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.9 | +15.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.3 | +16.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.3 | +4.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +1.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.0 | +2.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.9 | +2.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.7 | +4.6 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.4 | -9.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.2 | -12.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.9 | -8.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.7 | -12.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | -5.4 | -4.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.9 | -2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.8 | +0.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -3.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.8 | -2.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.7 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | tripartite motif containing 62 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.1 — chr1:33,145,399-33,182,059 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10759, DEAR1 |
| Gene groups (HGNC) | Ring finger proteins; Tripartite motif family; RING finger E3 ubiquitin protein ligases |
| Reactome | 3 pathways, smallest: Interferon gamma signaling; Interferon Signaling; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BVG3](https://www.uniprot.org/uniprotkb/Q9BVG3) (E3 ubiquitin-protein ligase TRIM62):

> E3 ubiquitin ligase that plays a role in antifungal immunity by mediating 'Lys-27'-linked ubiquitination of CARD9 downstream of C-type lectin receptors; leading to CARD9 activation, followed by activation of NF-kappa-B and MAP kinase p38 pathways. E3 ubiquitin ligase activity is dependent on E2 ubiquitin-conjugating enzyme UBE2D2.

**Summary**, from NCBI Gene [55223](https://www.ncbi.nlm.nih.gov/gene/55223):

> Enables identical protein binding activity; transcription coactivator activity; and ubiquitin protein ligase activity. Involved in several processes, including negative regulation of viral transcription; positive regulation of antifungal innate immune response; and positive regulation of canonical NF-kappaB signal transduction. Is active in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25574](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25574) · Entrez [55223](https://www.ncbi.nlm.nih.gov/gene/55223) · UniProt [Q9BVG3](https://www.uniprot.org/uniprotkb/Q9BVG3) · Ensembl [ENSG00000116525](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116525)

## Data

Gene col 3803: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3803); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3803, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3803]; `tensor/DDL_lfc|DDL_z.npy` [3803]; `embed/gene_vectors.npy` [3803]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3803 or target_col == 3803). Every well: [[TRIM62 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIM62.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
