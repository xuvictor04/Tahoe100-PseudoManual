---
symbol: "AK6"
type: "gene"
col: 1419
ensembl_id: "ENSG00000085231"
name: "adenylate kinase 6"
location: "5q13.2"
module: 29
arm: "-"
pooled_cpm: 26.0
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# AK6

*adenylate kinase 6* — 5q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.47× (z +14.0, q 7e-42, up in 39 of 47 measured lines) ⚠ cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.32× (z +9.2, q 4e-18, up in 37 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SHP-77 0.156×, SW 900 0.196×; ⚠ toxic; transcription drop); [[Pimozide (drug)]] 0.05 µM in 1 line (AN3 CA 0.119×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRSAM1]] (+0.72, fdr 7e-06), [[RBX1]] (+0.72, fdr 7e-06), [[MRPS18C]] (+0.70, fdr 7e-06); moves opposite to [[ARF3]] (-0.69, fdr 7e-06), [[PABIR2]] (-0.66, fdr 7e-06), [[FKBP1A]] (-0.66, fdr 1e-05).
> It sits in the **-** arm of [[Module 029]] (Neutrophil degranulation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 12 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1419.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **2.47×** | +14.0 | 7e-42 | 39/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.49×** | +10.0 | 4e-21 | 46/47 (NCI-H460, SW480, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.36×** | +9.4 | 1e-18 | 45/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.32×** | +9.2 | 4e-18 | 37/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **2.39×** | +9.2 | 5e-18 | 38/48 (NCI-H460, A498, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.77×** | +6.3 | 4e-08 | 42/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.73×** | +6.0 | 1e-07 | 35/48 (NCI-H460, HT-29, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.72×** | +5.9 | 2e-07 | 40/48 (LS 180, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **1.72×** | +5.7 | 8e-07 | 36/47 (NCI-H460, LS 180, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.74×** | +5.5 | 2e-06 | 37/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.62×** | +5.3 | 5e-06 | 37/48 (NCI-H460, LoVo, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.61×** | +4.9 | 4e-05 | 27/48 (HEC-1-A, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.49×** | +4.4 | 5e-04 | 28/48 (NCI-H2347, SW480, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~67% of this change | **1.48×** | +4.3 | 7e-04 | 25/45 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.8 | 0.005 | 22/46 (NCI-H2347, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.34×** | +3.2 | 0.043 | 22/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1419.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SHP-77 0.156×, SW 900 0.196×; ⚠ toxic; transcription drop); [[Pimozide (drug)]] 0.05 µM in 1 line (AN3 CA 0.119×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Demeclocycline (drug)]] 5 µM |  | 0.809× | -3.3 | 0.57 | 19/48 (A498, NCI-H2347, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1419. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 25.6 | 12 (9 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.41× (z +19.5) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.99× (z +13.3) | — |
| [[LoVo (line)]] | wt | 26.2 | 4 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.32× (z +10.4) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.60× (z +9.1) | — |
| [[NCI-H1573 (line)]] | alt | 20.6 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +13.0) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.85× (z +9.1) | — |
| [[PANC-1 (line)]] | alt | 50.2 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +15.8) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.15× (z +10.5) | — |
| [[SW 900 (line)]] | alt | 26.8 | 3 (3 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 4.71× (z +9.5) ⚠ cell-cycle shift, explains ~38% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.196× (z -8.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 29.7 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +10.9) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[A498 (line)]] | wt | 40.2 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +15.3) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[A549 (line)]] | wt | 24.7 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +11.2) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[LS 180 (line)]] | wt | 31.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +10.0) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[A-172 (line)]] | wt | 28.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +12.3) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[AN3 CA (line)]] | alt | 36.8 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.119× (z -8.7) |
| [[C32 (line)]] | wt | 16.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +11.0) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[COLO 205 (line)]] | alt | 21.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.69× (z +10.8) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[HEC-1-A (line)]] | alt | 20.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +12.4) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 22.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.11× (z +10.3) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[J82 (line)]] | alt | 22.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +9.4) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[LOX-IMVI (line)]] | wt | 22.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +10.5) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[SHP-77 (line)]] | alt | 21.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.156× (z -9.2) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 26.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +12.3) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[A-427 (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1419), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRSAM1]] | +0.72 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[RBX1]] | +0.72 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[MRPS18C]] | +0.70 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[ERVK3-1]] | +0.70 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[ATF4]] | +0.70 | +0.64 / +0.76 | both halves | 7e-06 |  |
| [[NSRP1]] | +0.70 | +0.73 / +0.70 | both halves | 7e-06 |  |
| [[MTRFR]] | +0.68 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[N4BP2L2]] | +0.67 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[NKAP]] | +0.67 | +0.59 / +0.75 | both halves | 7e-06 |  |
| [[RSF1]] | +0.66 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[WASHC1]] | +0.66 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[LRCH3]] | +0.65 | +0.58 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARF3]] | -0.69 | -0.65 / -0.69 | both halves | 7e-06 |  |
| [[PABIR2]] | -0.66 | -0.62 / -0.64 | both halves | 7e-06 |  |
| [[FKBP1A]] | -0.66 | -0.57 / -0.66 | both halves | 1e-05 |  |
| [[TMEM30A]] | -0.65 | -0.58 / -0.70 | both halves | 7e-06 |  |
| [[ERMP1]] | -0.65 | -0.57 / -0.64 | both halves | 1e-05 |  |
| [[ATP5F1B]] | -0.62 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[TMEM106C]] | -0.62 | -0.64 / -0.46 | both halves | 3e-05 |  |
| [[SKP2]] | -0.62 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[TMED7]] | -0.61 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[AGO1]] | -0.61 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[PRPF8]] | -0.61 | -0.48 / -0.66 | both halves | 2e-05 |  |
| [[SUMO1]] | -0.60 | -0.61 / -0.62 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **-** arm (projection on the module's main direction -0.661). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-26.6, -24.4); signed map (-2.1, -8.3). **Vector** length 76.4, 17.9% of its response variance represented; |z| ≥ 3 in 832 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +5.4 | +14.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.2 | +9.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +3.8 | +9.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +2.9 | +4.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.8 | +5.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.8 | +6.0 |
|  | [[Adagrasib (drug)]] 5 µM |  | +1.7 | +1.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.5 | +2.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.5 | +2.4 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.4 | -1.9 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | +1.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.6 | -0.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | -2.6 | +3.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.5 | +2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.7 | -2.3 |
|  | [[Diphenhydramine (drug)]] 5 µM |  | -1.5 | -0.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.5 | -2.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.4 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | adenylate kinase 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q13.2 — chr5:69,350,984-69,370,013 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CINAP |
| Gene groups (HGNC) | Adenylate kinases; Ribosome biogenesis factors |
| Reactome | 2 pathways, smallest: Interconversion of nucleotide di- and triphosphates; Metabolism of nucleotides |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y3D8](https://www.uniprot.org/uniprotkb/Q9Y3D8) (Adenylate kinase isoenzyme 6):

> Broad-specificity nucleoside monophosphate (NMP) kinase that catalyzes the reversible transfer of the terminal phosphate group between nucleoside triphosphates and monophosphates. Also has ATPase activity. Involved in the late cytoplasmic maturation steps of the 40S ribosomal particles, specifically 18S rRNA maturation. While NMP activity is not required for ribosome maturation, ATPase activity is. Associates transiently with small ribosomal subunit protein uS11. ATP hydrolysis breaks the …

**Summary**, from NCBI Gene [102157402](https://www.ncbi.nlm.nih.gov/gene/102157402):

> This gene encodes a protein that belongs to the adenylate kinase family of enzymes. The protein has a nuclear localization and contains Walker A (P-loop) and Walker B motifs and a metal-coordinating residue. The protein may be involved in regulation of Cajal body formation. In human, AK6 and TAF9 (GeneID: 6880) are two distinct genes that share 5' exons. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Sep 2013]

**Accessions** — [HGNC:49151](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49151) · Entrez [102157402](https://www.ncbi.nlm.nih.gov/gene/102157402) · UniProt [Q9Y3D8](https://www.uniprot.org/uniprotkb/Q9Y3D8) · Ensembl [ENSG00000085231](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000085231)

## Data

Gene col 1419: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1419); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1419, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1419]; `tensor/DDL_lfc|DDL_z.npy` [1419]; `embed/gene_vectors.npy` [1419]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1419 or target_col == 1419). Every well: [[AK6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AK6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
