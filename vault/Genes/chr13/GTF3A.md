---
symbol: "GTF3A"
type: "gene"
col: 4317
ensembl_id: "ENSG00000122034"
name: "general transcription factor IIIA"
location: "13q12.2"
module: 28
arm: "+"
pooled_cpm: 31.76
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/028", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# GTF3A

*general transcription factor IIIA* — 13q12.2

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.12× (z +15.3, q 0e+00, up in 45 of 45 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (SW480 6.22×, HT-29 6.98×, NCI-H460 7.18×, LoVo 6.45×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (SW480 5.48×, NCI-H460 7.86×, HCT15 10.6×, LoVo 5.87×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW480 3.99×; ⚠ toxic; transcription drop).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (MIA PaCa-2 0.225×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CFAP97]] (+0.60, fdr 8e-06), [[DCAF17]] (+0.59, fdr 3e-05), [[NELFCD]] (+0.58, fdr 1e-05); moves opposite to [[FBXL19]] (-0.56, fdr 1e-05), [[POLR2J3-1]] (-0.54, fdr 4e-05), [[FRMD8]] (-0.53, fdr 1e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 8 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4317.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (SW480 6.22×, HT-29 6.98×, NCI-H460 7.18×, LoVo 6.45×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (SW480 5.48×, NCI-H460 7.86×, HCT15 10.6×, LoVo 5.87×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW480 3.99×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.12×** | +15.3 | 0e+00 | 45/45 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.14×** | +12.4 | 4e-33 | 37/37 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.03×** | +9.8 | 2e-20 | 42/43 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | **1.62×** | +4.2 | 0.003 | 27/47 (SW480, COLO 205, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +4.2 | 0.003 | 30/47 (C32, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~71% of this change | **1.51×** | +3.9 | 0.007 | 29/46 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.57×** | +3.9 | 0.007 | 24/48 (SW480, KATO III, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.47×** | +3.6 | 0.021 | 26/48 (SW480, SW48, …) | rises with dose |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (MIA PaCa-2 0.225×; ⚠ cell-cycle shift, would explain all of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.60 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4317. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HCT15 (line)]] | alt | 34.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 10.6× (z +11.5) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 20.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.53× (z +9.9) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 61.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.98× (z +13.6) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 51.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.03× (z +10.1) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 35.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.47× (z +12.4) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 64.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.22× (z +15.7) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 28.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.23× (z +9.0) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 34.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.12× (z +11.1) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 22.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.94× (z +10.6) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 42.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[Hs 766T (line)]] | wt | 38.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.32× (z +9.9) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 21.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.67× (z +9.0) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 25.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.45× (z +12.4) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 34.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.02× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -13.4) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 11.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.6× (z +10.6) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 27.4 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H460 (line)]] | wt | 20.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.18× (z +12.5) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 36.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.99× (z +11.0) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 59.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.70× (z +11.0) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 33.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.88× (z +10.5) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 10.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.19× (z +9.6) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 10.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.98× (z +9.0) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 24.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.57× (z +12.3) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 31.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.48× (z +10.4) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 18.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.87× (z +11.3) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 45.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.89× (z +10.2) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 17.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.57× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 19.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.41× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 21.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.73× (z +10.3) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 40.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.87× (z +9.9) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 55.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +10.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[AN3 CA (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 37.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 62.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 41.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 39.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4317), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFAP97]] | +0.60 | +0.59 / +0.58 | both halves | 8e-06 |  |
| [[DCAF17]] | +0.59 | +0.61 / +0.46 | both halves | 3e-05 |  |
| [[NELFCD]] | +0.58 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[TRUB1]] | +0.57 | +0.66 / +0.43 | both halves | 3e-05 |  |
| [[ACAT1]] | +0.57 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[COX11]] | +0.57 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[PEX1]] | +0.57 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[CEP63]] | +0.56 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[DMXL2]] | +0.56 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[LCOR]] | +0.54 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[LARS1]] | +0.54 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[IMPACT]] | +0.54 | +0.62 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXL19]] | -0.56 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[POLR2J3-1]] | -0.54 | -0.46 / -0.40 | both halves | 4e-05 |  |
| [[FRMD8]] | -0.53 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[POLR2J4]] | -0.53 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[ASB16-AS1]] | -0.51 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[ATG2A]] | -0.51 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[CHMP1A]] | -0.51 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[RAD9A]] | -0.51 | -0.51 / -0.46 | both halves | 2e-05 |  |
| [[GRIN2D]] | -0.51 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[TRIR]] ⚠ | -0.49 | -0.48 / -0.36 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[MED31]] | -0.49 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[MTCH1]] | -0.49 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[ADGRL1-AS1]] | -0.49 | -0.41 / -0.52 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.540). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-30.3, -15.4); signed map (-1.6, -37.4). **Vector** length 69.9, 17.9% of its response variance represented; |z| ≥ 3 in 544 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +12.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +3.1 | +3.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | +3.1 | +3.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +15.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +1.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | +1.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +2.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.4 | +2.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +1.9 | -0.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +2.0 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | -1.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | -1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | -0.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.6 | -0.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.7 | +0.1 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.5 | -0.5 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -1.4 | +0.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | +0.7 |

## What is on record

|  |  |
|---|---|
| Name | general transcription factor IIIA |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q12.2 — chr13:27,424,619-27,435,823 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TFIIIA, AP2 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; General transcription factors |
| Reactome | 4 pathways, smallest: RNA Polymerase III Transcription Initiation From Type 1 Promoter; RNA Polymerase III Transcription Initiation; RNA Polymerase III Abortive And Retractive Initiation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92664](https://www.uniprot.org/uniprotkb/Q92664) (Transcription factor IIIA):

> Involved in ribosomal large subunit biogenesis. Binds the approximately 50 base pairs internal control region (ICR) of 5S ribosomal RNA genes. It is required for their RNA polymerase III-dependent transcription and may also maintain the transcription of other genes. Also binds the transcribed 5S RNA's (By similarity).

**Summary**, from NCBI Gene [2971](https://www.ncbi.nlm.nih.gov/gene/2971):

> The product of this gene is a zinc finger protein with nine Cis[2]-His[2] zinc finger domains. It functions as an RNA polymerase III transcription factor to induce transcription of the 5S rRNA genes. The protein binds to a 50 bp internal promoter in the 5S genes called the internal control region (ICR), and nucleates formation of a stable preinitiation complex. This complex recruits the TFIIIC and TFIIIB transcription factors and RNA polymerase III to form the complete transcription complex. …

**Accessions** — [HGNC:4662](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4662) · Entrez [2971](https://www.ncbi.nlm.nih.gov/gene/2971) · UniProt [Q92664](https://www.uniprot.org/uniprotkb/Q92664) · Ensembl [ENSG00000122034](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122034)

## Data

Gene col 4317: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4317); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4317, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4317]; `tensor/DDL_lfc|DDL_z.npy` [4317]; `embed/gene_vectors.npy` [4317]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4317 or target_col == 4317). Every well: [[GTF3A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GTF3A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
