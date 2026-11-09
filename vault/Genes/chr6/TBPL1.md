---
symbol: "TBPL1"
type: "gene"
col: 387
ensembl_id: "ENSG00000028839"
name: "TATA-box binding protein like 1"
location: "6q23.2"
module: 4
arm: "-"
pooled_cpm: 26.48
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 3
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# TBPL1

*TATA-box binding protein like 1* — 6q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.89× (z +16.3, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.560× (z -10.5, q 5e-23, down in 25 of 43 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (SW480 0.160×, KATO III 0.0750×, hTERT-HPNE 0.0896×, SW1417 0.240×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (COLO 205 0.0424×, Panc 03.27 0.115×, SHP-77 0.221×, SW 900 0.186×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SHP-77 0.293×, NCI-H2347 0.295×; ⚠ toxic; transcription drop); [[Cepharanthine (drug)]] 5 µM in 1 line (Hs 766T 0.304×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACVR2A]] (+0.56, fdr 3e-05), [[NKIRAS1]] (+0.54, fdr 2e-05), [[PAPOLG]] (+0.50, fdr 5e-05); moves opposite to [[SMARCA4]] (-0.51, fdr 7e-05), [[DNAAF5]] (-0.50, fdr 3e-05), [[LAS1L]] (-0.50, fdr 1e-04).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 387.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.89×** | +16.3 | 0e+00 | 45/48 (HEC-1-A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.69×** | +13.5 | 5e-39 | 36/47 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.69×** | +13.5 | 5e-39 | 43/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.89×** | +11.5 | 1e-28 | 45/48 (COLO 205, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.87×** | +11.3 | 1e-27 | 42/48 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.78×** | +10.4 | 2e-23 | 41/48 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.44×** | +9.4 | 7e-19 | 35/48 (COLO 205, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.57×** | +8.2 | 2e-14 | 34/48 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.52×** | +7.6 | 2e-12 | 34/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.46×** | +6.9 | 4e-10 | 28/47 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +6.6 | 2e-09 | 24/47 (MIA PaCa-2, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.39×** | +6.0 | 9e-08 | 24/48 (BT-474, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.38×** | +5.6 | 1e-06 | 23/48 (MIA PaCa-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.30×** | +4.7 | 1e-04 | 19/48 (MIA PaCa-2, HOP62, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.29×** | +4.6 | 1e-04 | 20/48 (NCI-H460, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.62×** | +4.6 | 2e-04 | 14/48 (SW480, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 387.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (SW480 0.160×, KATO III 0.0750×, hTERT-HPNE 0.0896×, SW1417 0.240×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (COLO 205 0.0424×, Panc 03.27 0.115×, SHP-77 0.221×, SW 900 0.186×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SHP-77 0.293×, NCI-H2347 0.295×; ⚠ toxic; transcription drop); [[Cepharanthine (drug)]] 5 µM in 1 line (Hs 766T 0.304×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.560×** | -10.5 | 5e-23 | 25/43 (COLO 205, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.691×** | -6.4 | 3e-08 | 22/35 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.790×** | -3.9 | 0.015 | 18/38 (SHP-77, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | 0.826× | -3.3 | 0.15 | 12/48 (H4, SNU-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 387. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 18.5 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 2.72× (z +11.1) | — |
| [[COLO 205 (line)]] | alt | 197 | 3 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 0.5 µM 2.58× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.0424× (z -32.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 23.7 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.98× (z +14.0) | — |
| [[NCI-H460 (line)]] | wt | 22.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +12.0) | — |
| [[SW480 (line)]] | alt | 41.0 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.160× (z -22.0) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 29.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.0896× (z -13.7) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 20.2 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0986× (z -10.0) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 22.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.373× (z -9.1) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 41.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.221× (z -12.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 19.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +9.0) | — |
| [[BT-474 (line)]] | alt | 16.7 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.87× (z +9.1) | — |
| [[C32 (line)]] | wt | 15.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +9.9) | — |
| [[CFPAC-1 (line)]] | alt | 11.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +8.9) | — |
| [[HEC-1-A (line)]] | alt | 17.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.02× (z +14.8) | — |
| [[HOP62 (line)]] | alt | 18.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.64× (z +11.1) | — |
| [[Hs 766T (line)]] | wt | 14.0 | 0 | 1 | — | [[Cepharanthine (drug)]] 5 µM 0.304× (z -9.2) |
| [[HS-578T (line)]] | alt | 26.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +9.9) | — |
| [[HT-29 (line)]] | alt | 23.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +8.5) | — |
| [[J82 (line)]] | alt | 16.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +9.7) | — |
| [[KATO III (line)]] | alt | 44.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0750× (z -19.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 35.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +8.5) | — |
| [[LS 180 (line)]] | wt | 27.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +9.6) | — |
| [[Panc 03.27 (line)]] | alt | 18.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.115× (z -13.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 36.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +9.0) | — |
| [[SW 900 (line)]] | alt | 28.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.186× (z -11.4) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 35.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.240× (z -11.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 387), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACVR2A]] | +0.56 | +0.44 / +0.63 | both halves | 3e-05 |  |
| [[NKIRAS1]] | +0.54 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[PAPOLG]] | +0.50 | +0.39 / +0.46 | both halves | 5e-05 |  |
| [[PITX2]] | +0.48 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[TSPAN12]] | +0.48 | +0.31 / +0.58 | both halves | 2e-04 |  |
| [[RTCA-AS1]] | +0.47 | +0.35 / +0.54 | both halves | 1e-04 |  |
| [[SATB2-AS1]] | +0.47 | +0.29 / +0.48 | both halves | 2e-04 |  |
| [[TSC22D4]] | +0.47 | +0.40 / +0.32 | both halves | 2e-04 |  |
| [[ENY2]] | +0.47 | +0.39 / +0.44 | both halves | 5e-05 | STRING 503 |
| [[ZNF280C]] | +0.47 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[WASL-DT]] | +0.47 | +0.24 / +0.56 | both halves | 5e-04 |  |
| [[SCAMP5]] | +0.46 | +0.20 / +0.53 | both halves | 7e-04 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMARCA4]] | -0.51 | -0.38 / -0.48 | both halves | 7e-05 |  |
| [[DNAAF5]] | -0.50 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[LAS1L]] | -0.50 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[CCDC57]] | -0.49 | -0.28 / -0.35 | both halves | 3e-04 |  |
| [[PBRM1]] | -0.49 | -0.32 / -0.51 | both halves | 1e-04 |  |
| [[ARHGAP39]] | -0.49 | -0.21 / -0.50 | both halves | 7e-04 |  |
| [[TOMM40]] | -0.47 | -0.36 / -0.50 | both halves | 1e-04 |  |
| [[MTOR]] | -0.47 | -0.23 / -0.50 | both halves | 5e-04 |  |
| [[CDK11B]] | -0.46 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[POLR1A]] | -0.46 | -0.38 / -0.40 | both halves | 7e-05 |  |
| [[LRRC14]] | -0.46 | -0.27 / -0.51 | both halves | 3e-04 |  |
| [[DDX46]] | -0.46 | -0.29 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.362). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-2.6, -38.7); signed map (38.7, -3.2). **Vector** length 67.2, 11.8% of its response variance represented; |z| ≥ 3 in 1,050 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.0 | +13.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.6 | +11.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.7 | +9.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +16.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.8 | +3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +1.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.4 | -0.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +1.4 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -1.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | +1.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.0 | +10.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.9 | -0.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | +0.3 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -1.4 | -2.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.2 | -0.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | TATA-box binding protein like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q23.2 — chr6:133,952,170-133,990,432 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TLP, STUD, TRF2, TLF |
| Gene groups (HGNC) | TATA-box binding protein family |
| Matched by | ensembl_id |

**Function**, from UniProt [P62380](https://www.uniprot.org/uniprotkb/P62380) (TATA box-binding protein-like 1):

> Part of a specialized transcription system that mediates the transcription of most ribosomal proteins through the 5'-TCT-3' motif which is a core promoter element at these genes. Seems to also mediate the transcription of NF1. Does not bind the TATA box.

**Summary**, from NCBI Gene [9519](https://www.ncbi.nlm.nih.gov/gene/9519):

> This gene encodes a member of the TATA box-binding protein family. TATA box-binding proteins play a critical role in transcription by RNA polymerase II as components of the transcription factor IID (TFIID) complex. The encoded protein does not bind to the TATA box and initiates transcription from TATA-less promoters. This gene plays a critical role in spermatogenesis, and single nucleotide polymorphisms in this gene may be associated with male infertility. Alternatively spliced transcript …

**Accessions** — [HGNC:11589](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11589) · Entrez [9519](https://www.ncbi.nlm.nih.gov/gene/9519) · UniProt [P62380](https://www.uniprot.org/uniprotkb/P62380) · Ensembl [ENSG00000028839](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000028839)

## Data

Gene col 387: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 387); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 387, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 387]; `tensor/DDL_lfc|DDL_z.npy` [387]; `embed/gene_vectors.npy` [387]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 387 or target_col == 387). Every well: [[TBPL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBPL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
