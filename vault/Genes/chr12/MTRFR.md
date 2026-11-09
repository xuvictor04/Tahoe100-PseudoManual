---
symbol: "MTRFR"
type: "gene"
col: 5144
ensembl_id: "ENSG00000130921"
name: "mitochondrial translation release factor in rescue"
location: "12q24.31"
module: 149
arm: "+"
pooled_cpm: 25.27
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 4
n_dd_up_clean: 5
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/149"]
generated_by: "tahoemap"
---

# MTRFR

*mitochondrial translation release factor in rescue* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.73× (z +13.3, q 1e-37, up in 36 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.620× (z -7.6, q 2e-11, down in 24 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Pyridoxine (hydrochloride) (drug)]] 5 µM: 0.846× (z -4.1, q 0.005, down in 21 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 5 lines (HEC-1-A 0.0553×, LS 180 0.134×, A-427 0.259×, PANC-1 0.342×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (PANC-1 0.261×, HEC-1-A 0.309×, MIA PaCa-2 0.262×; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SK-MEL-2 0.135×, A-427 0.294×; ⚠ cell-cycle shift, explains ~7% of this change); [[Roxadustat (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0833×); [[Arbutin (drug)]] 5 µM in 1 line (SW48 0.0605×); [[Bendamustine (drug)]] 5 µM in 1 line (SW48 0.105×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AK6]] (+0.68, fdr 7e-06), [[TMEM79]] (+0.67, fdr 7e-06), [[DCP1A]] (+0.64, fdr 1e-05); moves opposite to [[SH3GLB2]] (-0.59, fdr 1e-05), [[ACTR3]] (-0.59, fdr 7e-06), [[PABIR2]] (-0.59, fdr 1e-05).
> It is in [[Module 149]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5144.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +13.3 | 1e-37 | 36/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.57×** | +11.0 | 1e-25 | 32/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.28×** | +4.0 | 0.014 | 17/45 (J82, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.25×** | +3.6 | 0.045 | 15/47 (PANC-1, NCI-H1573, …) | top dose only | composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.22×** | +3.4 | 0.074 | 8/48 (LS 180, C-33 A, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.15× | +3.3 | 0.074 | 4/48 (SW 900, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.074 | 6/48 (C-33 A, HOP62, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.074 | 11/48 (C-33 A, hTERT-HPNE, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5144.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 5 lines (HEC-1-A 0.0553×, LS 180 0.134×, A-427 0.259×, PANC-1 0.342×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (PANC-1 0.261×, HEC-1-A 0.309×, MIA PaCa-2 0.262×; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SK-MEL-2 0.135×, A-427 0.294×; ⚠ cell-cycle shift, explains ~7% of this change); [[Roxadustat (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0833×); [[Arbutin (drug)]] 5 µM in 1 line (SW48 0.0605×); [[Bendamustine (drug)]] 5 µM in 1 line (SW48 0.105×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.620×** | -7.6 | 2e-11 | 24/39 (HEC-1-A, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.625×** | -7.5 | 2e-11 | 22/33 (SW480, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.682×** | -6.6 | 8e-09 | 23/43 (PANC-1, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.846× | -4.1 | 0.005 | 21/48 (SW 1271, PANC-1, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.790×** | -4.1 | 0.005 | 15/48 (PANC-1, COLO 205, …) | inconsistent across doses |  |
| [[Folic acid (drug)]] 5 µM |  | 0.869× | -3.4 | 0.061 | 11/48 (HS-578T, NCI-H661, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5144. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 37.2 | 0 | 5 (5 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.238× (z -12.6) ⚠ cell-cycle shift, explains ~51% of this change |
| [[PANC-1 (line)]] | alt | 43.0 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +16.0) | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -15.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 21.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.244× (z -9.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 36.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0553× (z -26.2) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 31.5 | 0 | 2 (1 ⚠) | — | [[Roxadustat (drug)]] 0.05 µM 0.0833× (z -13.1) |
| [[LS 180 (line)]] | wt | 17.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +9.6) | [[Dinaciclib (drug)]] 0.05 µM 0.134× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 15.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +10.9) | — |
| [[NCI-H460 (line)]] | wt | 22.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +14.4) | — |
| [[SW48 (line)]] | wt | 18.3 | 0 | 2 | — | [[Arbutin (drug)]] 5 µM 0.0605× (z -11.7) |
| [[SW480 (line)]] | alt | 24.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.337× (z -9.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 31.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.270× (z -9.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 18.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +9.6) | — |
| [[CFPAC-1 (line)]] | alt | 22.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +8.9) | — |
| [[HOP62 (line)]] | alt | 24.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +9.4) | — |
| [[HT-29 (line)]] | alt | 23.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.254× (z -9.3) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 34.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +9.0) | — |
| [[LoVo (line)]] | wt | 31.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +11.6) | — |
| [[LOX-IMVI (line)]] | wt | 14.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +11.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 34.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -10.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 15.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +13.8) | — |
| [[NCI-H2030 (line)]] | alt | 19.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +9.5) | — |
| [[RPMI-7951 (line)]] | alt | 18.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.156× (z -9.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 17.7 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.135× (z -10.9) ⚠ cell-cycle shift, explains ~7% of this change |
| [[SNU-1 (line)]] | wt | 21.5 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.134× (z -8.9) ⚠ cell-cycle shift, explains ~7% of this change |
| [[SNU-423 (line)]] | alt | 32.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.270× (z -9.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5144), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AK6]] | +0.68 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[TMEM79]] | +0.67 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[DCP1A]] | +0.64 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[ZNF766]] | +0.63 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[LRSAM1]] | +0.63 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[N4BP2L2]] | +0.63 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[TRAPPC2B]] | +0.63 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[CCDC174]] | +0.62 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[CCDC59]] | +0.62 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[ZMYM5]] | +0.62 | +0.57 / +0.60 | both halves | 9e-06 |  |
| [[RBBP6]] | +0.62 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[TRIP11]] | +0.61 | +0.65 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH3GLB2]] | -0.59 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[ACTR3]] | -0.59 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[PABIR2]] | -0.59 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[POMGNT1]] | -0.59 | -0.65 / -0.50 | both halves | 1e-05 |  |
| [[APEH]] | -0.58 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[FKBP1A]] | -0.58 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[ZDHHC21]] | -0.58 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[CORO1C]] | -0.57 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[FAM199X]] | -0.57 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[LINC03009]] | -0.57 | -0.59 / -0.58 | both halves | 8e-06 |  |
| [[ITGB1]] | -0.56 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[ARHGAP4]] | -0.56 | -0.46 / -0.50 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 149]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.690). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-47.5, -3.6); signed map (-7.4, -10.8). **Vector** length 95.0, 20.3% of its response variance represented; |z| ≥ 3 in 756 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.3 | +11.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +3.6 | +2.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +13.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.9 | +4.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | +2.8 | +3.6 |
|  | [[Adagrasib (drug)]] 5 µM |  | +2.6 | +2.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.1 | +0.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.8 | +0.6 |
|  | [[γ-Oryzanol (drug)]] 0.05 µM |  | +1.7 | +2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +3.3 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.6 | -7.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -7.1 | -6.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.1 | -7.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.3 | -2.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -1.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.8 | -1.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.1 | -4.1 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.7 | -2.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.6 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial translation release factor in rescue |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:123,233,385-123,258,079 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ38663, SPG55, COXPD7, mtRF-R; previously C12orf65 |
| Gene groups (HGNC) | Mitochondrial translation release factor family |
| Reactome | 3 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation; Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H3J6](https://www.uniprot.org/uniprotkb/Q9H3J6) (Mitochondrial translation release factor in rescue):

> Part of a mitoribosome-associated quality control pathway that prevents aberrant translation by responding to interruptions during elongation. As heterodimer with MTRES1, ejects the unfinished nascent chain and peptidyl transfer RNA (tRNA), respectively, from stalled ribosomes. Recruitment of mitoribosome biogenesis factors to these quality control intermediates suggests additional roles for MTRES1 and MTRF during mitoribosome rescue.

**Summary**, from NCBI Gene [91574](https://www.ncbi.nlm.nih.gov/gene/91574):

> This nuclear gene encodes a mitochondrial matrix protein that appears to contribute to peptide chain termination in the mitochondrial translation machinery. Two different 1 bp deletions (resulting in the same premature stop codon)result in decreased mitochondrial translation, decreased levels of oxidative phosphorylation complexes and encepthalomyopathy. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Aug 2010]

**Accessions** — [HGNC:26784](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26784) · Entrez [91574](https://www.ncbi.nlm.nih.gov/gene/91574) · UniProt [Q9H3J6](https://www.uniprot.org/uniprotkb/Q9H3J6) · Ensembl [ENSG00000130921](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130921)

## Data

Gene col 5144: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5144); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5144, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5144]; `tensor/DDL_lfc|DDL_z.npy` [5144]; `embed/gene_vectors.npy` [5144]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5144 or target_col == 5144). Every well: [[MTRFR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTRFR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
