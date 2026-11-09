---
symbol: "TAF1B"
type: "gene"
col: 3714
ensembl_id: "ENSG00000115750"
name: "TATA-box binding protein associated factor, RNA polymerase I subunit B"
location: "2p25.1"
module: 1
arm: "+"
pooled_cpm: 59.1
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 6
n_dd_up_clean: 1
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# TAF1B

*TATA-box binding protein associated factor, RNA polymerase I subunit B* — 2p25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.55× (z +10.7, q 7e-24, up in 36 of 48 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.14× (z +4.4, q 0.001, up in 15 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A-172 2.75×, A498 2.25×, SNU-423 1.99×; ⚠ cell-cycle shift, explains ~55% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-172 2.50×, A498 2.56×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (A-172 2.59×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.591× (z -18.1, q 0e+00, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MPHOSPH6]] (+0.66, fdr 1e-05), [[TMEM185B]] (+0.66, fdr 1e-05), [[SERBP1]] (+0.65, fdr 7e-06); moves opposite to [[GNAS]] (-0.67, fdr 1e-05), [[TMEM59]] (-0.66, fdr 7e-06), [[APTR]] (-0.65, fdr 7e-06).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[STON2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3714.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A-172 2.75×, A498 2.25×, SNU-423 1.99×; ⚠ cell-cycle shift, explains ~55% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-172 2.50×, A498 2.56×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (A-172 2.59×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.55×** | +10.7 | 7e-24 | 36/48 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.48×** | +9.5 | 6e-19 | 35/48 (A-172, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.29×** | +6.3 | 6e-08 | 30/48 (A-172, LoVo, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +4.4 | 0.001 | 15/48 (KATO III, LS 180, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.19× | +4.3 | 0.002 | 19/48 (LOX-IMVI, A549, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.2 | 0.002 | 19/48 (A-172, A498, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.18× | +3.9 | 0.009 | 16/48 (SNU-423, NCI-H1792, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.18× | +3.8 | 0.012 | 18/47 (A-172, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | 1.16× | +3.7 | 0.013 | 15/48 (KATO III, LS 180, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.033 | 11/48 (A-172, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | 1.14× | +3.2 | 0.064 | 9/48 (A-172, LoVo, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.2 | 0.072 | 13/48 (KATO III, SW48, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.13× | +3.0 | 0.11 | 13/48 (A-172, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3714.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.591×** | -18.1 | 0e+00 | 41/48 (NCI-H23, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.759×** | -6.7 | 5e-09 | 26/48 (NCI-H460, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.785×** | -5.9 | 7e-07 | 25/48 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.802×** | -5.2 | 3e-05 | 23/48 (A-427, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.805×** | -5.1 | 4e-05 | 24/49 (HEC-1-A, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~12% of this change | 0.835× | -4.4 | 1e-03 | 23/48 (MIA PaCa-2, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.785×** | -4.2 | 0.002 | 17/48 (PANC-1, SNU-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 0.847× | -4.0 | 0.004 | 22/48 (HEC-1-A, NCI-H23, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.856× | -3.6 | 0.022 | 16/48 (A-427, PANC-1, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.864× | -3.4 | 0.035 | 19/47 (C-33 A, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | 0.912× | -3.2 | 0.079 | 16/48 (NCI-H1792, A-427, …) | top dose only | composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.880× | -3.1 | 0.084 | 14/49 (A-427, A549, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.902× | -3.1 | 0.086 | 11/48 (A-427, NCI-H23, …) | two highest doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3714. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 59.2 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.206× (z -17.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -13.9) |
| [[A-172 (line)]] | wt | 63.9 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +17.4) ⚠ cell-cycle shift, explains ~55% of this change | — |
| [[A-427 (line)]] | wt | 130 | 0 | 4 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -19.5) |
| [[HEC-1-A (line)]] | alt | 64.8 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.533× (z -11.0) |
| [[NCI-H460 (line)]] | wt | 38.6 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -14.4) |
| [[NCI-H23 (line)]] | alt | 113 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -17.7) |
| [[SNU-1 (line)]] | wt | 101 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.124× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -10.0) |
| [[A498 (line)]] | wt | 32.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +11.9) ⚠ cell-cycle shift, explains ~55% of this change | — |
| [[NCI-H1573 (line)]] | alt | 54.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -12.8) |
| [[SNU-423 (line)]] | alt | 58.1 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +11.1) ⚠ cell-cycle shift, explains ~55% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.518× (z -10.6) |
| [[A549 (line)]] | wt | 102 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.514× (z -11.9) |
| [[AsPC-1 (line)]] | alt | 37.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.468× (z -9.2) ⚠ cell-cycle shift, explains ~55% of this change |
| [[BT-474 (line)]] | alt | 38.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -12.1) |
| [[C-33 A (line)]] | alt | 99.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.389× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 52.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -13.5) |
| [[COLO 205 (line)]] | alt | 39.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -8.9) |
| [[HCT15 (line)]] | alt | 83.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.470× (z -9.8) |
| [[HOP62 (line)]] | alt | 56.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -15.9) |
| [[J82 (line)]] | alt | 56.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.399× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 39.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.572× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 77.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -16.9) |
| [[NCI-H1792 (line)]] | alt | 36.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -12.3) ⚠ cell-cycle shift, explains ~55% of this change |
| [[NCI-H2030 (line)]] | alt | 62.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -12.1) |
| [[Panc 03.27 (line)]] | alt | 41.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -11.1) |
| [[PANC-1 (line)]] | alt | 107 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.592× (z -12.7) |
| [[SHP-77 (line)]] | alt | 95.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.318× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 1088 (line)]] | alt | 62.6 | 0 | 1 | — | [[Clotrimazole (drug)]] 0.5 µM 0.0735× (z -8.8) |
| [[SW 1271 (line)]] | alt | 75.7 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.101× (z -8.9) |
| [[SW48 (line)]] | wt | 61.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.160× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 51.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 41.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 60.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 53.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 40.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 66.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 82.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 79.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 63.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3714), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*45 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPHOSPH6]] | +0.66 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[TMEM185B]] | +0.66 | +0.57 / +0.71 | both halves | 1e-05 |  |
| [[SERBP1]] | +0.65 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[EIF2B3]] | +0.63 | +0.46 / +0.60 | both halves | 3e-05 |  |
| [[NOC3L]] | +0.63 | +0.53 / +0.72 | both halves | 1e-05 |  |
| [[MGA]] | +0.62 | +0.53 / +0.69 | both halves | 1e-05 |  |
| [[ZKSCAN2]] | +0.62 | +0.47 / +0.68 | both halves | 2e-05 |  |
| [[RUVBL1]] | +0.62 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[CEP83]] | +0.61 | +0.43 / +0.66 | both halves | 3e-05 |  |
| [[AGK]] | +0.60 | +0.44 / +0.61 | both halves | 3e-05 |  |
| [[SACS]] | +0.60 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[DDX10]] | +0.60 | +0.47 / +0.65 | both halves | 2e-05 |  |

## Genes that move opposite

*55 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAS]] | -0.67 | -0.53 / -0.67 | both halves | 1e-05 |  |
| [[TMEM59]] | -0.66 | -0.63 / -0.64 | both halves | 7e-06 |  |
| [[APTR]] | -0.65 | -0.58 / -0.61 | both halves | 7e-06 |  |
| [[SMPDL3A]] | -0.61 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[KLC4]] | -0.61 | -0.41 / -0.68 | both halves | 4e-05 |  |
| [[MKRN1]] | -0.60 | -0.50 / -0.64 | both halves | 1e-05 |  |
| [[C12orf73]] | -0.59 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[PCMTD1]] | -0.59 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[IFT20]] | -0.59 | -0.53 / -0.65 | both halves | 1e-05 |  |
| [[COPZ2]] | -0.58 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[TSC22D4]] | -0.57 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[SOS1]] | -0.57 | -0.43 / -0.58 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STON2]] | B | STON2 activity lowers TAF1B's level | lines that do not express STON2 (19) vs lines expressing it (31) | 1.52× higher at baseline in the lines without STON2 | 0.004 | ⚠ within organs, on part of the lines; also absent: FRK, RASSF6, AQP3 |
| [[TOP2A]] | B | TOP2A activity raises TAF1B's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CADPS2]] | B | CADPS2 activity lowers TAF1B's level | lines that do not express CADPS2 (14) vs lines expressing it (36) | 1.60× higher at baseline in the lines without CADPS2 | 0.037 | ⚠ within organs, on part of the lines; also absent: DGKG, RBPMS, FAM3B |
| [[HDAC6]] | B | HDAC6 activity lowers TAF1B's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[STON2]] | B | STON2 activity strengthens TAF1B's drug response | lines that do not express STON2 (19) vs lines expressing it (30) | the lines without STON2 respond 0.91× as strongly (z diff +0.08); strongest at Panobinostat 5 µM: 1.16x vs 1.57x (z diff +2.8) | 0.080 | ⚠ within organs, on part of the lines; also absent: FRK, RASSF6, AQP3; target measured in part of the lines; both ways; artifact flags |
| [[HOXB3]] | B | HOXB3 activity lowers TAF1B's level | lines that do not express HOXB3 (9) vs lines expressing it (41) | 1.27× higher at baseline in the lines without HOXB3 | 0.090 | ⚠ within organs, on part of the lines; also absent: HOXB6 |
| [[CADPS2]] | B | CADPS2 activity strengthens TAF1B's drug response | lines that do not express CADPS2 (14) vs lines expressing it (35) | the lines without CADPS2 respond 0.88× as strongly (z diff +0.25); strongest at Belinostat 5 µM: 0.92x vs 1.41x (z diff +4.0) | 0.096 | ⚠ within organs, on part of the lines; also absent: DGKG, RBPMS, FAM3B; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.503). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-10.4, -42.6); signed map (-6.5, -48.0). **Vector** length 105, 24.6% of its response variance represented; |z| ≥ 3 in 1,010 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.5 | +2.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.0 | +3.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.8 | +4.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +4.8 | +10.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.4 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +4.4 |
|  | [[EX229 (drug)]] 5 µM |  | +2.9 | +2.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +3.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.7 | +3.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.9 | -18.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.1 | -5.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -5.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.3 | -3.1 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.7 | -1.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.7 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.6 | -3.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.6 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | TATA-box binding protein associated factor, RNA polymerase I subunit B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p25.1 — chr2:9,843,443-9,934,416 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TAFI63, SL1, RAF1B, RAFI63 |
| Reactome | 10 pathways, smallest: SIRT1 negatively regulates rRNA expression; RNA Polymerase I Transcription Termination; B-WICH complex positively regulates rRNA expression |
| Matched by | ensembl_id |

**Function**, from UniProt [Q53T94](https://www.uniprot.org/uniprotkb/Q53T94) (TATA box-binding protein-associated factor RNA polymerase I subunit B):

> Component of RNA polymerase I core factor complex that acts as a GTF2B/TFIIB-like factor and plays a key role in multiple steps during transcription initiation such as pre-initiation complex (PIC) assembly and postpolymerase recruitment events in polymerase I (Pol I) transcription. Binds rDNA promoters and plays a role in Pol I recruitment as a component of the SL1/TIF-IB complex and, possibly, directly through its interaction with RRN3.

**Summary**, from NCBI Gene [9014](https://www.ncbi.nlm.nih.gov/gene/9014):

> Initiation of transcription by RNA polymerase I requires the formation of a complex composed of the TATA-binding protein (TBP) and three TBP-associated factors (TAFs) specific for RNA polymerase I. This complex, known as SL1, binds to the core promoter of ribosomal RNA genes to position the polymerase properly and acts as a channel for regulatory signals. This gene encodes one of the SL1-specific TAFs. Multiple transcript variants encoding different isoforms have been found for this gene. …

**Accessions** — [HGNC:11533](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11533) · Entrez [9014](https://www.ncbi.nlm.nih.gov/gene/9014) · UniProt [Q53T94](https://www.uniprot.org/uniprotkb/Q53T94) · Ensembl [ENSG00000115750](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115750)

## Data

Gene col 3714: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3714); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3714, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3714]; `tensor/DDL_lfc|DDL_z.npy` [3714]; `embed/gene_vectors.npy` [3714]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3714 or target_col == 3714). Every well: [[TAF1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TAF1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
