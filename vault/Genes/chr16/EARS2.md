---
symbol: "EARS2"
type: "gene"
col: 2359
ensembl_id: "ENSG00000103356"
name: "glutamyl-tRNA synthetase 2, mitochondrial"
location: "16p12.2"
module: 33
arm: "+"
pooled_cpm: 23.3
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 6
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# EARS2

*glutamyl-tRNA synthetase 2, mitochondrial* — 16p12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.69× (z +11.0, q 2e-25, up in 38 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.56× (z +9.4, q 2e-18, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.563× (z -17.2, q 0e+00, down in 36 of 47 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM: 0.830× (z -4.0, q 0.007, down in 4 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 8 lines (RKO 0.132×, PANC-1 0.403×, LoVo 0.334×, hTERT-HPNE 0.196×, …; ⚠ cell-cycle shift, explains ~25% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (SW48 0.0822×, NCI-H460 0.312×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (PANC-1 0.305×; ⚠ cell-cycle shift, explains ~31% of this change); [[Afatinib (drug)]] 0.05 µM in 1 line (BT-474 0.337×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[URB1]] (+0.77, fdr 7e-06), [[RABEPK]] (+0.75, fdr 7e-06), [[PTRH2]] (+0.74, fdr 7e-06); moves opposite to [[TP53INP2]] (-0.58, fdr 1e-05), [[TXNDC16]] (-0.56, fdr 2e-05), [[FMR1]] (-0.55, fdr 2e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2359.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.69×** | +11.0 | 2e-25 | 38/48 (SW480, NCI-H2347, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +9.4 | 2e-18 | 34/48 (LoVo, C32, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.21×** | +8.8 | 3e-16 | 26/45 (PANC-1, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.37×** | +6.6 | 7e-09 | 18/43 (LS 180, SNU-1, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **1.71×** | +5.9 | 4e-07 | 17/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.67×** | +5.7 | 1e-06 | 19/46 (NCI-H460, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.66×** | +5.6 | 2e-06 | 18/46 (HEC-1-A, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.32×** | +5.6 | 2e-06 | 19/48 (A-172, HEC-1-A, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.29×** | +5.4 | 4e-06 | 22/48 (NCI-H1573, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[EX229 (drug)]] 5 µM |  | **1.58×** | +5.1 | 2e-05 | 19/47 (SW480, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **1.37×** | +4.8 | 1e-04 | 10/48 (HEC-1-A, SW480, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.36×** | +4.6 | 2e-04 | 10/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.48×** | +4.3 | 7e-04 | 8/27 (PANC-1, A549, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.23×** | +4.2 | 0.001 | 14/33 (LoVo, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.20× | +3.8 | 0.006 | 12/48 (HEC-1-A, A-172, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **1.38×** | +3.5 | 0.014 | 7/46 (KATO III, SW480, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.35×** | +3.3 | 0.025 | 17/48 (HEC-1-A, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.22×** | +3.0 | 0.076 | 1/48 (SW480) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.15× | +2.9 | 0.096 | 8/47 (NCI-H460, LOX-IMVI, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2359.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 8 lines (RKO 0.132×, PANC-1 0.403×, LoVo 0.334×, hTERT-HPNE 0.196×, …; ⚠ cell-cycle shift, explains ~25% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (SW48 0.0822×, NCI-H460 0.312×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (PANC-1 0.305×; ⚠ cell-cycle shift, explains ~31% of this change); [[Afatinib (drug)]] 0.05 µM in 1 line (BT-474 0.337×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.563×** | -17.2 | 0e+00 | 36/47 (RKO, PANC-1, …) | top dose only | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.693×** | -7.5 | 2e-11 | 26/47 (PANC-1, HS-578T, …) | rises with dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.792×** | -5.0 | 1e-04 | 18/48 (SW480, KATO III, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.821×** | -4.2 | 0.004 | 18/48 (NCI-H460, HS-578T, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.823×** | -4.1 | 0.004 | 18/46 (SW48, NCI-H460, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.830×** | -4.0 | 0.007 | 4/48 (MIA PaCa-2, LoVo, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.837× | -3.6 | 0.021 | 17/47 (MIA PaCa-2, C32, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~19% of this change | 0.838× | -3.6 | 0.021 | 13/46 (A498, PANC-1, …) | top dose only |  |
| [[Elagolix sodium (drug)]] 0.5 µM |  | 0.845× | -3.6 | 0.022 | 15/48 (HOP62, SNU-423, …) | two highest doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.842× | -3.5 | 0.024 | 9/47 (A-427, NCI-H460, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 0.05 µM |  | 0.837× | -3.5 | 0.024 | 10/47 (SNU-1, BT-474, …) | all doses, flat |  |
| [[Berbamine (drug)]] 5 µM |  | 0.894× | -3.4 | 0.032 | 7/48 (LoVo, NCI-H460, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.885× | -3.1 | 0.075 | 7/48 (LoVo, AN3 CA, …) | two highest doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 0.869× | -3.1 | 0.089 | 7/48 (MIA PaCa-2, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[crizotinib (drug)]] 5 µM |  | 0.862× | -3.0 | 0.089 | 13/48 (HOP62, hTERT-HPNE, …) | top dose only |  |
| [[Mozavaptan (drug)]] 0.05 µM |  | 0.859× | -3.0 | 0.094 | 3/47 (AsPC-1, RKO, …) | inconsistent across doses | position effect removed |
| [[Adagrasib (drug)]] 5 µM |  | 0.864× | -3.0 | 0.094 | 8/48 (SW 1088, MIA PaCa-2, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.907× | -3.0 | 0.097 | 10/48 (A498, LS 180, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2359. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 25.6 | 1 (1 ⚠) | 2 (2 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.12× (z +8.5) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.510× (z -10.7) ⚠ cell-cycle shift, explains ~25% of this change |
| [[HS-578T (line)]] | alt | 21.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -12.9) ⚠ cell-cycle shift, explains ~25% of this change |
| [[LoVo (line)]] | wt | 27.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.16× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -14.1) ⚠ cell-cycle shift, explains ~25% of this change |
| [[NCI-H460 (line)]] | wt | 22.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -12.8) ⚠ cell-cycle shift, explains ~25% of this change |
| [[PANC-1 (line)]] | alt | 43.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -16.4) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SW48 (line)]] | wt | 32.1 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0822× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[A498 (line)]] | wt | 29.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.385× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~19% of this change |
| [[A549 (line)]] | wt | 28.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.198× (z -12.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 24.3 | 0 | 1 | — | [[Afatinib (drug)]] 0.05 µM 0.337× (z -9.5) |
| [[CHP-212 (line)]] | wt | 39.6 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0884× (z -9.3) ⚠ toxic |
| [[HOP62 (line)]] | alt | 22.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -9.5) ⚠ cell-cycle shift, explains ~25% of this change |
| [[hTERT-HPNE (line)]] | wt | 19.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -13.1) ⚠ cell-cycle shift, explains ~25% of this change |
| [[J82 (line)]] | alt | 22.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -8.6) ⚠ cell-cycle shift, explains ~25% of this change |
| [[MIA PaCa-2 (line)]] | alt | 28.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.288× (z -9.8) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 29.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.253× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~5% of this change |
| [[RKO (line)]] | wt | 23.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -16.8) ⚠ cell-cycle shift, explains ~25% of this change |
| [[RPMI-7951 (line)]] | alt | 24.4 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.103× (z -14.2) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 21.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -10.6) ⚠ cell-cycle shift, explains ~25% of this change |
| [[A-172 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 40.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.89 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.94 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2359), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[URB1]] | +0.77 | +0.76 / +0.72 | both halves | 7e-06 | STRING 480 |
| [[RABEPK]] | +0.75 | +0.77 / +0.70 | both halves | 7e-06 |  |
| [[PTRH2]] | +0.74 | +0.76 / +0.69 | both halves | 7e-06 |  |
| [[PUM3]] | +0.69 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[NAA20]] | +0.69 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[NOL10]] | +0.68 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[TSR1]] | +0.68 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[PDCD11]] | +0.67 | +0.63 / +0.65 | both halves | 7e-06 | STRING 536 |
| [[DDX31]] | +0.67 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[FUBP3]] | +0.66 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[ZNF551]] | +0.66 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[WDR3]] | +0.66 | +0.67 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TP53INP2]] | -0.58 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[TXNDC16]] | -0.56 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[FMR1]] | -0.55 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[GPR137C]] | -0.55 | -0.60 / -0.40 | both halves | 5e-05 |  |
| [[ABI1]] | -0.54 | -0.37 / -0.62 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.641). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-10.4, -30.9); signed map (-14.3, -56.4). **Vector** length 101, 21.9% of its response variance represented; |z| ≥ 3 in 913 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA modification in the nucleus and cytosol* (reactome, mean cos +0.53 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.1 | +11.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.9 | +9.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.3 | +8.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.2 | +5.7 |
|  | [[EX229 (drug)]] 5 µM |  | +4.0 | +5.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.9 | +5.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -6.7 | -17.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -4.9 | -7.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.1 | -3.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~19% of this change | -2.7 | -3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.7 | -3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.6 | -4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | -3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.3 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | glutamyl-tRNA synthetase 2, mitochondrial |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p12.2 — chr16:23,520,754-23,557,731 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1970, MSE1, mtGlnRS |
| Gene groups (HGNC) | Aminoacyl tRNA synthetases, Class I |
| Reactome | 3 pathways, smallest: Mitochondrial tRNA aminoacylation; tRNA Aminoacylation; Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5JPH6](https://www.uniprot.org/uniprotkb/Q5JPH6) (Nondiscriminating glutamyl-tRNA synthetase EARS2, mitochondrial):

> Non-discriminating glutamyl-tRNA synthetase that catalyzes aminoacylation of both mitochondrial tRNA(Glu) and tRNA(Gln) and participates in RNA aminoacylation for mitochondrial protein translation. Attachs glutamate to tRNA(Glu) or tRNA(Gln) in a two-step reaction: glutamate is first activated by ATP to form Glu-AMP and then transferred to the acceptor end of tRNA(Glu) or tRNA(Gln). In vitro, cytoplasmic tRNA(Gln) is slightly glutamylated, but with low activity.

**Summary**, from NCBI Gene [124454](https://www.ncbi.nlm.nih.gov/gene/124454):

> This gene encodes a member of the class I family of aminoacyl-tRNA synthetases. These enzymes play a critical role in protein biosynthesis by charging tRNAs with their cognate amino acids. This protein is encoded by the nuclear genome but is likely to be imported to the mitochondrion where it is thought to catalyze the ligation of glutamate to tRNA molecules. Mutations in this gene have been associated with combined oxidative phosphorylation deficiency 12 (COXPD12). Alternative splicing results …

**Accessions** — [HGNC:29419](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29419) · Entrez [124454](https://www.ncbi.nlm.nih.gov/gene/124454) · UniProt [Q5JPH6](https://www.uniprot.org/uniprotkb/Q5JPH6) · Ensembl [ENSG00000103356](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103356)

## Data

Gene col 2359: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2359); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2359, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2359]; `tensor/DDL_lfc|DDL_z.npy` [2359]; `embed/gene_vectors.npy` [2359]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2359 or target_col == 2359). Every well: [[EARS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EARS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
