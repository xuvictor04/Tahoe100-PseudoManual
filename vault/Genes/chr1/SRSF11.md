---
symbol: "SRSF11"
type: "gene"
col: 3835
ensembl_id: "ENSG00000116754"
name: "serine and arginine rich splicing factor 11"
location: "1p31.1"
module: 12
arm: "+"
pooled_cpm: 295.88
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# SRSF11

*serine and arginine rich splicing factor 11* — 1p31.1

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (8 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.45× (z +7.6, q 2e-11, up in 46 of 48 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (AsPC-1 1.75×, NCI-H1573 1.82×, A549 1.75×, HEC-1-A 1.53×; ⚠ cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 4 lines (LS 180 2.02×, NCI-H460 2.06×, LoVo 1.86×, NCI-H1573 2.03×; ⚠ cell-cycle shift, explains ~33% of this change); [[Digitoxin (drug)]] 5 µM in 3 lines (LoVo 1.90×, NCI-H460 2.09×, LS 180 1.86×; ⚠ toxic; transcription drop); [[TAK-901 (drug)]] 0.05 µM in 1 line (LOX-IMVI 1.97×).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.821× (z -5.7, q 7e-06, down in 26 of 49 measured lines) ⚠ cell-cycle shift, explains ~22% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (LoVo 0.614×, NCI-H460 0.608×, A549 0.604×, SNU-423 0.647×; ⚠ cell-cycle shift, explains ~22% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (SNU-1 0.438×, SW48 0.480×, SK-MEL-2 0.517×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (H4 0.502×; ⚠ cell-cycle shift, explains ~65% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPIG]] (+0.78, fdr 7e-06), [[SEC62]] (+0.76, fdr 7e-06), [[ZC3H13]] (+0.71, fdr 7e-06); moves opposite to [[SLC25A39]] (-0.63, fdr 1e-05), [[FKBP1A]] (-0.62, fdr 7e-06), [[PTDSS1]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 10 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3835.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (AsPC-1 1.75×, NCI-H1573 1.82×, A549 1.75×, HEC-1-A 1.53×; ⚠ cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 4 lines (LS 180 2.02×, NCI-H460 2.06×, LoVo 1.86×, NCI-H1573 2.03×; ⚠ cell-cycle shift, explains ~33% of this change); [[Digitoxin (drug)]] 5 µM in 3 lines (LoVo 1.90×, NCI-H460 2.09×, LS 180 1.86×; ⚠ toxic; transcription drop); [[TAK-901 (drug)]] 0.05 µM in 1 line (LOX-IMVI 1.97×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +7.6 | 2e-11 | 46/48 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.39×** | +6.7 | 7e-09 | 40/48 (HEC-1-A, A549, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.35×** | +6.2 | 1e-07 | 35/48 (LS 180, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.22×** | +5.7 | 2e-06 | 25/48 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.26×** | +4.5 | 7e-04 | 30/48 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~20% of this change | **1.25×** | +4.4 | 8e-04 | 29/47 (LoVo, LS 180, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.24×** | +4.4 | 9e-04 | 32/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.46×** | +4.0 | 0.004 | 42/47 (LoVo, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | 1.20× | +3.7 | 0.016 | 23/49 (COLO 205, LS 180, …) | inconsistent across doses | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 1.19× | +3.6 | 0.016 | 22/48 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.18× | +3.4 | 0.030 | 18/48 (NCI-H1792, NCI-H23, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3835.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (LoVo 0.614×, NCI-H460 0.608×, A549 0.604×, SNU-423 0.647×; ⚠ cell-cycle shift, explains ~22% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (SNU-1 0.438×, SW48 0.480×, SK-MEL-2 0.517×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (H4 0.502×; ⚠ cell-cycle shift, explains ~65% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.821×** | -5.7 | 7e-06 | 26/49 (LoVo, NCI-H460, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 0.848× | -3.4 | 0.22 | 19/48 (Panc 03.27, HepG2/C3A, …) | all doses, flat |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.859× | -3.1 | 0.35 | 11/48 (NCI-H1573, NCI-H23, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3835. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 218 | 6 (6 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.18× (z +12.0) ⚠ cell-cycle shift, explains ~28% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.608× (z -10.9) ⚠ cell-cycle shift, explains ~22% of this change |
| [[LoVo (line)]] | wt | 323 | 3 (3 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 1.90× (z +11.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.614× (z -12.2) ⚠ cell-cycle shift, explains ~22% of this change |
| [[NCI-H1573 (line)]] | alt | 200 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +11.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A549 (line)]] | wt | 214 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +11.7) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.604× (z -10.5) ⚠ cell-cycle shift, explains ~22% of this change |
| [[COLO 205 (line)]] | alt | 176 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.54× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | — |
| [[HEC-1-A (line)]] | alt | 327 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.53× (z +10.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[LOX-IMVI (line)]] | wt | 266 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 1.91× (z +9.1) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[TAK-901 (drug)]] 0.05 µM 1.97× (z +9.0) | — |
| [[LS 180 (line)]] | wt | 318 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.02× (z +11.7) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H1792 (line)]] | alt | 242 | 2 (2 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 1.84× (z +9.5) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 218 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +9.3) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.517× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[AsPC-1 (line)]] | alt | 268 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +12.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[H4 (line)]] | wt | 353 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.502× (z -8.6) ⚠ cell-cycle shift, explains ~65% of this change |
| [[HT-29 (line)]] | alt | 306 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.55× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[KATO III (line)]] | alt | 245 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.52× (z +8.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H2030 (line)]] | alt | 358 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.73× (z +8.8) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[SNU-1 (line)]] | wt | 328 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.438× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[SNU-423 (line)]] | alt | 277 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.647× (z -9.5) ⚠ cell-cycle shift, explains ~22% of this change |
| [[SW48 (line)]] | wt | 356 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.480× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[A-172 (line)]] | wt | 270 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 276 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 383 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 338 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 253 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 356 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 245 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 291 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 199 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 421 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 285 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 187 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 339 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 341 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 288 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 356 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 411 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 252 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 354 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 215 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 290 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 377 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 290 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 329 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 388 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 323 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 255 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 422 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 278 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 277 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 336 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 330 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3835), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPIG]] | +0.78 | +0.76 / +0.73 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 611 |
| [[SEC62]] | +0.76 | +0.74 / +0.71 | both halves | 7e-06 |  |
| [[ZC3H13]] | +0.71 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[CROCCP2-1]] | +0.69 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[PRPF4B]] | +0.69 | +0.64 / +0.56 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 702 |
| [[SETDB1]] | +0.68 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[PNISR]] | +0.67 | +0.67 / +0.62 | both halves | 7e-06 | STRING 945 |
| [[AKAP9]] | +0.67 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[GGNBP2]] | +0.67 | +0.69 / +0.57 | both halves | 9e-06 |  |
| [[ANKRD49]] | +0.67 | +0.64 / +0.73 | both halves | 7e-06 |  |
| [[SREK1]] | +0.66 | +0.71 / +0.56 | both halves | 1e-05 | same gene group; STRING 933 |
| [[YTHDC1]] | +0.66 | +0.71 / +0.57 | both halves | 1e-05 | STRING 566 |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A39]] | -0.63 | -0.62 / -0.57 | both halves | 1e-05 |  |
| [[FKBP1A]] | -0.62 | -0.59 / -0.58 | both halves | 7e-06 |  |
| [[PTDSS1]] | -0.61 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[G6PD]] | -0.61 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[PSME3]] | -0.61 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[TUBG1]] | -0.60 | -0.65 / -0.47 | both halves | 2e-05 |  |
| [[NIPA2]] | -0.60 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[SIGMAR1]] | -0.59 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[TXNDC5]] | -0.59 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[ACLY]] | -0.59 | -0.50 / -0.60 | both halves | 1e-05 | STRING 411 |
| [[EDEM1]] | -0.58 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[SUV39H2]] | -0.58 | -0.50 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.645). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-36.7, 1.6); signed map (-11.4, -5.2). **Vector** length 112, 38.8% of its response variance represented; |z| ≥ 3 in 689 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +5.0 | +6.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.6 | +5.7 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +4.0 | +4.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +1.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.7 | +0.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.5 | +0.2 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +3.4 | +1.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.3 | +1.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.3 | +2.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -6.2 | -5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.2 | -1.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.3 | -1.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -1.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.7 | +0.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.6 | -1.9 |
|  | [[Lopinavir (drug)]] 5 µM |  | -2.5 | -2.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.4 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | serine and arginine rich splicing factor 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.1 — chr1:70,205,682-70,253,052 (+) |
| Ensembl biotype | protein_coding |
| Also known as | p54, NET2; previously SFRS11 |
| Gene groups (HGNC) | RNA binding motif containing; Serine and arginine rich splicing factors |
| Reactome | 11 pathways, smallest: Transport of Mature mRNA derived from an Intron-Containing Transcript; Transport of Mature Transcript to Cytoplasm; mRNA Polyadenylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q05519](https://www.uniprot.org/uniprotkb/Q05519) (Serine/arginine-rich splicing factor 11):

> May function in pre-mRNA splicing.

**Summary**, from NCBI Gene [9295](https://www.ncbi.nlm.nih.gov/gene/9295):

> This gene encodes 54-kD nuclear protein that contains an arginine/serine-rich region similar to segments found in pre-mRNA splicing factors. Although the function of this protein is not yet known, structure and immunolocalization data suggest that it may play a role in pre-mRNA processing. Alternative splicing results in multiple transcript variants encoding different proteins. In addition, a pseudogene of this gene has been found on chromosome 12.[provided by RefSeq, Sep 2010]

**Accessions** — [HGNC:10782](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10782) · Entrez [9295](https://www.ncbi.nlm.nih.gov/gene/9295) · UniProt [Q05519](https://www.uniprot.org/uniprotkb/Q05519) · Ensembl [ENSG00000116754](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116754)

## Data

Gene col 3835: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3835); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3835, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3835]; `tensor/DDL_lfc|DDL_z.npy` [3835]; `embed/gene_vectors.npy` [3835]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3835 or target_col == 3835). Every well: [[SRSF11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SRSF11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
