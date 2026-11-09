---
symbol: "EIPR1"
type: "gene"
col: 405
ensembl_id: "ENSG00000032389"
name: "EARP complex and GARP complex interacting protein 1"
location: "2p25.3"
module: 4
arm: "+"
pooled_cpm: 46.57
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 7
n_dd_up_clean: 12
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# EIPR1

*EARP complex and GARP complex interacting protein 1* — 2p25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.89× (z +10.4, q 1e-22, up in 41 of 48 measured lines) ⚠ cell-cycle shift, explains ~51% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.64× (z +8.1, q 9e-14, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.772× (z -6.0, q 1e-06, down in 28 of 47 measured lines) ⚠ cell-cycle shift, explains ~64% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.818× (z -4.6, q 6e-04, down in 22 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (A498 0.368×, PANC-1 0.477×, J82 0.325×, SK-MEL-2 0.382×, …; ⚠ cell-cycle shift, explains ~64% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H23 0.312×, SNU-1 0.183×, SHP-77 0.374×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Lonafarnib (drug)]] 5 µM in 2 lines (HEC-1-A 0.100×, AsPC-1 0.114×; ⚠ toxic); [[XRK3F2 (drug)]] 0.5 µM in 1 line (C32 0.0815×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNGTT]] (+0.79, fdr 7e-06), [[POLR1A]] (+0.74, fdr 7e-06), [[SPATA5]] (+0.74, fdr 7e-06); moves opposite to [[ABCA5]] (-0.75, fdr 7e-06), [[TXNDC16]] (-0.70, fdr 8e-06), [[RSRP1]] (-0.69, fdr 7e-06).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 405.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.89×** | +10.4 | 1e-22 | 41/48 (A498, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.77×** | +9.3 | 4e-18 | 40/48 (A498, A549, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.74×** | +9.1 | 2e-17 | 40/48 (A549, SW480, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.64×** | +8.1 | 8e-14 | 34/48 (NCI-H1573, A549, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.64×** | +8.1 | 9e-14 | 40/48 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.62×** | +7.9 | 2e-13 | 38/48 (A498, PANC-1, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.62×** | +7.9 | 3e-13 | 38/48 (A498, Panc 03.27, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.47×** | +5.9 | 2e-07 | 34/48 (A549, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.35×** | +4.9 | 6e-05 | 32/48 (PANC-1, HepG2/C3A, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.32×** | +4.3 | 9e-04 | 21/47 (SW480, A-172, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.20×** | +4.2 | 0.001 | 20/48 (NCI-H1792, SNU-423, …) | rises with dose | low cells (technical?) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.29×** | +4.2 | 0.001 | 25/47 (PANC-1, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.63×** | +4.2 | 0.001 | 25/48 (PANC-1, A549, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.29×** | +4.0 | 0.003 | 20/48 (NCI-H2347, COLO 205, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.55×** | +3.7 | 0.007 | 20/48 (A498, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.49×** | +3.4 | 0.021 | 13/47 (A498, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.49×** | +3.4 | 0.021 | 15/48 (NCI-H2347, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.47×** | +3.3 | 0.028 | 15/49 (A498, SHP-77, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **1.46×** | +3.2 | 0.034 | 18/46 (A498, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Acetohexamide (drug)]] 5 µM |  | 1.14× | +2.9 | 0.088 | 2/48 (MIA PaCa-2, NCI-H2347) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 405.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (A498 0.368×, PANC-1 0.477×, J82 0.325×, SK-MEL-2 0.382×, …; ⚠ cell-cycle shift, explains ~64% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H23 0.312×, SNU-1 0.183×, SHP-77 0.374×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Lonafarnib (drug)]] 5 µM in 2 lines (HEC-1-A 0.100×, AsPC-1 0.114×; ⚠ toxic); [[XRK3F2 (drug)]] 0.5 µM in 1 line (C32 0.0815×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.772×** | -6.0 | 1e-06 | 28/47 (A498, PANC-1, …) | top dose only | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.717×** | -5.2 | 5e-05 | 26/48 (PANC-1, NCI-H460, …) | top dose only | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.818×** | -4.6 | 6e-04 | 22/48 (CHP-212, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.759×** | -4.4 | 0.002 | 24/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.848× | -3.8 | 0.015 | 17/48 (J82, SNU-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.827×** | -3.7 | 0.023 | 18/48 (LoVo, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.809×** | -3.5 | 0.041 | 21/48 (Panc 03.27, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.825×** | -3.4 | 0.041 | 18/49 (LoVo, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.823× | -3.1 | 0.11 | 15/49 (LoVo, NCI-H23, …) | two highest doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.838× | -3.1 | 0.11 | 15/48 (SK-MEL-2, SNU-1, …) | two highest doses | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.876× | -3.1 | 0.11 | 20/48 (AsPC-1, NCI-H2030, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.57 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 405. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 68.9 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.377× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 82.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.180× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 26.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.68× (z +9.0) ⚠ cell-cycle shift, explains ~51% of this change | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -13.1) ⚠ cell-cycle shift, explains ~64% of this change |
| [[AsPC-1 (line)]] | alt | 41.8 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.429× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 42.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.477× (z -12.2) ⚠ cell-cycle shift, explains ~64% of this change |
| [[A549 (line)]] | wt | 50.9 | 1 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.55× (z +8.7) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[C32 (line)]] | wt | 15.4 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.0815× (z -9.9) |
| [[HEC-1-A (line)]] | alt | 48.2 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.100× (z -11.6) ⚠ toxic |
| [[J82 (line)]] | alt | 29.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -12.0) ⚠ cell-cycle shift, explains ~64% of this change |
| [[LoVo (line)]] | wt | 53.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.486× (z -9.5) ⚠ cell-cycle shift, explains ~64% of this change |
| [[NCI-H1573 (line)]] | alt | 46.6 | 1 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.94× (z +9.0) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[SHP-77 (line)]] | alt | 130 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.374× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 49.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -11.5) ⚠ cell-cycle shift, explains ~64% of this change |
| [[SNU-1 (line)]] | wt | 50.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 37.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 82.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 58.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 81.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 41.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 70.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 57.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 57.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 67.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 405), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNGTT]] | +0.79 | +0.74 / +0.78 | both halves | 7e-06 |  |
| [[POLR1A]] | +0.74 | +0.74 / +0.73 | both halves | 7e-06 |  |
| [[SPATA5]] | +0.74 | +0.77 / +0.69 | both halves | 7e-06 |  |
| [[MRPS27]] | +0.72 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[EBNA1BP2]] | +0.71 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[LSG1]] | +0.71 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[CHCHD6]] | +0.71 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[LARS2]] | +0.70 | +0.74 / +0.74 | both halves | 7e-06 |  |
| [[PRIM2]] | +0.70 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[POP1]] | +0.70 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[CHCHD3]] | +0.69 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[NUDC]] | +0.69 | +0.68 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCA5]] | -0.75 | -0.72 / -0.68 | both halves | 7e-06 |  |
| [[TXNDC16]] | -0.70 | -0.70 / -0.58 | both halves | 8e-06 |  |
| [[RSRP1]] | -0.69 | -0.70 / -0.67 | both halves | 7e-06 |  |
| [[PIK3IP1]] | -0.67 | -0.63 / -0.67 | both halves | 7e-06 |  |
| [[ZMYM5]] | -0.66 | -0.61 / -0.69 | both halves | 7e-06 |  |
| [[TAPT1]] | -0.65 | -0.63 / -0.59 | both halves | 7e-06 |  |
| [[KLHL24]] | -0.64 | -0.71 / -0.61 | both halves | 7e-06 |  |
| [[ZBTB10]] | -0.64 | -0.56 / -0.62 | both halves | 1e-05 |  |
| [[CREBRF]] | -0.64 | -0.72 / -0.60 | both halves | 7e-06 |  |
| [[OPTN]] | -0.63 | -0.67 / -0.61 | both halves | 7e-06 |  |
| [[TERF2IP]] | -0.62 | -0.61 / -0.60 | both halves | 7e-06 |  |
| [[ZNF821]] | -0.62 | -0.61 / -0.62 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.764). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-10.1, -33.6); signed map (-12.3, -47.9). **Vector** length 125, 35.0% of its response variance represented; |z| ≥ 3 in 1,087 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *tRNA processing in the nucleus* (reactome, mean cos +0.54 to 8); *tRNA processing* (reactome, mean cos +0.51 to 10); *Metabolism of non-coding RNA* (reactome, mean cos +0.50 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.0 | +9.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.2 | +7.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +7.0 | +8.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.8 | +8.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.2 | +5.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.2 | +2.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.4 | +4.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.3 | +3.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | -6.8 | -6.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -6.1 | -3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.7 | -4.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -5.4 | -5.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.0 | -3.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.5 | -3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.7 | -3.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.6 | -3.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.4 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | EARP complex and GARP complex interacting protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p25.3 — chr2:3,188,925-3,377,830 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EIPR-1; previously TSSC1 |
| Gene groups (HGNC) | WD repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q53HC9](https://www.uniprot.org/uniprotkb/Q53HC9) (EARP and GARP complex-interacting protein 1):

> Acts as a component of endosomal retrieval machinery that is involved in protein transport from early endosomes to either recycling endosomes or the trans-Golgi network. Mediates the recruitment of Golgi-associated retrograde protein (GARP) complex to the trans-Golgi network and controls early endosome-to-Golgi transport of internalized protein. Promotes the recycling of internalized transferrin receptor (TFRC) to the plasma membrane through interaction with endosome-associated recycling …

**Summary**, from NCBI Gene [7260](https://www.ncbi.nlm.nih.gov/gene/7260):

> This gene has been reported in PMID 9403053 as one of several tumor-suppressing subtransferable fragments located in the imprinted gene domain of 11p15.5, an important tumor-suppressor gene region. Alterations in this region have been associated with the Beckwith-Wiedemann syndrome, Wilms tumor, rhabdomyosarcoma, adrenocortical carcinoma, and lung, ovarian, and breast cancer. Alignment of this gene to genomic sequence data suggests that this gene resides on chromosome 2 rather than chromosome …

**Accessions** — [HGNC:12383](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12383) · Entrez [7260](https://www.ncbi.nlm.nih.gov/gene/7260) · UniProt [Q53HC9](https://www.uniprot.org/uniprotkb/Q53HC9) · Ensembl [ENSG00000032389](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000032389)

## Data

Gene col 405: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 405); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 405, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 405]; `tensor/DDL_lfc|DDL_z.npy` [405]; `embed/gene_vectors.npy` [405]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 405 or target_col == 405). Every well: [[EIPR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIPR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
