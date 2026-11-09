---
symbol: "MRFAP1"
type: "gene"
col: 10988
ensembl_id: "ENSG00000179010"
name: "Morf4 family associated protein 1"
location: "4p16.1"
module: 11
arm: "+"
pooled_cpm: 66.17
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 2
n_dd_up_clean: 7
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# MRFAP1

*Morf4 family associated protein 1* — 4p16.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (11 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 1.78× (z +6.8, q 6e-09, up in 40 of 48 measured lines) ⚠ cell-cycle shift, explains ~54% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.77× (z +6.1, q 2e-07, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.797× (z -4.0, q 0.027, down in 27 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A-427 0.338×, LoVo 0.526×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (COLO 205 0.155×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.529×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRFAP1L1]] (+0.72, fdr 7e-06), [[SRRD]] (+0.70, fdr 7e-06), [[PDRG1]] (+0.69, fdr 7e-06); moves opposite to [[SMG1P1]] (-0.62, fdr 8e-06), [[SEC61A2]] (-0.62, fdr 8e-06), [[LINC00115]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 12 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10988.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.78×** | +6.8 | 6e-09 | 40/48 (LS 180, AsPC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.45×** | +6.5 | 3e-08 | 38/48 (LS 180, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.77×** | +6.1 | 2e-07 | 39/48 (HOP62, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.62×** | +6.0 | 3e-07 | 41/48 (LS 180, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.58×** | +5.6 | 3e-06 | 38/48 (LOX-IMVI, LS 180, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +5.2 | 2e-05 | 41/48 (RKO, MIA PaCa-2, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +5.1 | 3e-05 | 36/47 (LS 180, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~60% of this change | **1.51×** | +5.0 | 3e-05 | 38/48 (RPMI-7951, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | **1.51×** | +4.9 | 8e-05 | 29/43 (NCI-H460, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change | **1.50×** | +4.4 | 8e-04 | 30/49 (A498, A549, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.39×** | +4.1 | 0.003 | 33/48 (LOX-IMVI, LS 180, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.38×** | +4.0 | 0.003 | 34/48 (NCI-H2347, HOP62, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.36×** | +3.5 | 0.024 | 26/47 (C32, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.31×** | +3.3 | 0.044 | 26/48 (C32, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.054 | 29/48 (NCI-H2347, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.27×** | +3.0 | 0.090 | 20/48 (BT-474, A549, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10988.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A-427 0.338×, LoVo 0.526×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (COLO 205 0.155×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.529×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.797×** | -4.0 | 0.027 | 27/48 (A-427, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.722×** | -3.9 | 0.027 | 32/48 (A498, LOX-IMVI, …) | top dose only | position effect removed |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.765× | -3.3 | 0.16 | 33/48 (A498, HS-578T, …) | all doses, stronger at high dose |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | 0.834× | -3.2 | 0.18 | 18/48 (LS 180, A498, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10988. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 47.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.60× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change | — |
| [[A-427 (line)]] | wt | 81.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -10.2) |
| [[A498 (line)]] | wt | 88.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change | — |
| [[COLO 205 (line)]] | alt | 57.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +8.5) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.155× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change |
| [[LS 180 (line)]] | wt | 57.3 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +11.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A-172 (line)]] | wt | 74.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.13× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | — |
| [[AsPC-1 (line)]] | alt | 37.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +11.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[LoVo (line)]] | wt | 73.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 31.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.64× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | — |
| [[AN3 CA (line)]] | alt | 82.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 60.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 77.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 48.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 99.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 76.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 105 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 94.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 85.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 55.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 76.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 45.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 64.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 71.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 87.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 90.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 67.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 85.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 62.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 65.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 95.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 75.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 65.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 64.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 64.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 65.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 82.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 67.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 59.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 74.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10988), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRFAP1L1]] | +0.72 | +0.71 / +0.81 | both halves | 7e-06 | STRING 721 |
| [[SRRD]] | +0.70 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[PDRG1]] | +0.69 | +0.62 / +0.75 | both halves | 7e-06 |  |
| [[GSPT2]] | +0.68 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[MMADHC]] | +0.67 | +0.51 / +0.69 | both halves | 1e-05 | STRING 498 |
| [[POP4]] | +0.66 | +0.63 / +0.72 | both halves | 7e-06 |  |
| [[KLHL9]] | +0.66 | +0.52 / +0.70 | both halves | 1e-05 |  |
| [[ASF1A]] | +0.65 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[CEBPZ]] | +0.64 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[PSMB1]] | +0.63 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[THUMPD1]] | +0.63 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[EXOC8]] | +0.63 | +0.68 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMG1P1]] | -0.62 | -0.66 / -0.58 | both halves | 8e-06 |  |
| [[SEC61A2]] | -0.62 | -0.58 / -0.60 | both halves | 8e-06 |  |
| [[LINC00115]] | -0.56 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[FAM81A]] | -0.56 | -0.37 / -0.52 | both halves | 8e-05 |  |
| [[NFKBID]] | -0.55 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[EIF2S3]] | -0.55 | -0.62 / -0.57 | both halves | 9e-06 |  |
| [[RPS3A]] | -0.54 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[PCGF2]] | -0.54 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[RPL6]] | -0.53 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[PDIA6]] | -0.53 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[IFI27L1]] | -0.52 | -0.54 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.602). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-35.4, -0.4); signed map (-0.3, -23.1). **Vector** length 85.3, 25.0% of its response variance represented; |z| ≥ 3 in 793 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +5.1 | +6.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +4.6 | +6.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | +4.5 | +6.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.5 | +3.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.5 | +6.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.1 | +3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.1 | +4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +5.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.7 | +3.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.5 | -4.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.5 | +2.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.2 | -2.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.6 | -0.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | -5.3 | +4.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.7 | -0.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.4 | -3.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -1.2 | -1.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.2 | -1.1 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -1.1 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | Morf4 family associated protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.1 — chr4:6,640,091-6,642,729 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PAM14, PGR1 |
| Matched by | ensembl_id |

UniProt [Q9Y605](https://www.uniprot.org/uniprotkb/Q9Y605) carries no function annotation.

**Summary**, from NCBI Gene [93621](https://www.ncbi.nlm.nih.gov/gene/93621):

> This gene encodes an intracellular protein that interacts with members of the MORF4/MRG (mortality factor on chromosome 4/MORF4 related gene) family and the tumor suppressor Rb (retinoblastoma protein.) The protein may play a role in senescence, cell growth and immortalization. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2013]

**Accessions** — [HGNC:24549](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24549) · Entrez [93621](https://www.ncbi.nlm.nih.gov/gene/93621) · UniProt [Q9Y605](https://www.uniprot.org/uniprotkb/Q9Y605) · Ensembl [ENSG00000179010](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179010)

## Data

Gene col 10988: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10988); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10988, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10988]; `tensor/DDL_lfc|DDL_z.npy` [10988]; `embed/gene_vectors.npy` [10988]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10988 or target_col == 10988). Every well: [[MRFAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRFAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
