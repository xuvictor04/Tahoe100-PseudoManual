---
symbol: "ANAPC16"
type: "gene"
col: 9279
ensembl_id: "ENSG00000166295"
name: "anaphase promoting complex subunit 16"
location: "10q22.1"
module: 28
arm: "+"
pooled_cpm: 74.32
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 20
n_dd_up_clean: 0
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# ANAPC16

*anaphase promoting complex subunit 16* — 10q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.00× (z +8.2, q 1e-13, up in 45 of 49 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (A498 3.63×, HEC-1-A 2.85×, Panc 03.27 2.95×, CFPAC-1 2.73×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (HEC-1-A 2.56×, CFPAC-1 2.86×, A498 2.93×, A-427 2.80×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.372× (z -11.8, q 3e-29, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRMT10B]] (+0.68, fdr 7e-06), [[C1orf43]] (+0.65, fdr 7e-06), [[RAD52]] (+0.65, fdr 8e-06); moves opposite to [[GATAD2A]] (-0.64, fdr 7e-06), [[CDC42EP2]] (-0.63, fdr 7e-06), [[TPM3]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9279.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (A498 3.63×, HEC-1-A 2.85×, Panc 03.27 2.95×, CFPAC-1 2.73×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (HEC-1-A 2.56×, CFPAC-1 2.86×, A498 2.93×, A-427 2.80×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.00×** | +8.2 | 1e-13 | 45/49 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.72×** | +6.2 | 2e-07 | 30/42 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | 1.32× | +3.3 | 0.12 | 31/48 (A-172, NCI-H23, …) | all doses, flat |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.32× | +3.3 | 0.12 | 27/49 (A-172, HOP62, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | 1.30× | +3.2 | 0.17 | 23/47 (SW 900, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Sulfatinib (drug)]] 5 µM |  | 1.31× | +3.1 | 0.18 | 27/49 (A-172, A549, …) | top dose only |  |
| [[Adagrasib (drug)]] 5 µM |  | 1.30× | +3.0 | 0.21 | 25/48 (hTERT-HPNE, NCI-H1573, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9279.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.372×** | -11.8 | 3e-29 | 48/48 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.395×** | -11.0 | 7e-26 | 48/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.449×** | -9.5 | 3e-19 | 47/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.642×** | -7.4 | 2e-11 | 42/49 (HEC-1-A, NCI-H460, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.569×** | -6.7 | 3e-09 | 43/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.582×** | -6.4 | 1e-08 | 42/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.598×** | -6.1 | 8e-08 | 43/48 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.620×** | -5.7 | 1e-06 | 40/48 (RKO, HT-29, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.732×** | -5.2 | 1e-05 | 30/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.638×** | -5.1 | 2e-05 | 32/48 (SW480, LS 180, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.658×** | -5.0 | 3e-05 | 33/48 (HCT15, PANC-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.466×** | -4.7 | 1e-04 | 38/48 (C32, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.677×** | -4.6 | 2e-04 | 32/48 (LoVo, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.710×** | -4.1 | 0.002 | 31/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.739×** | -3.6 | 0.013 | 25/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.739×** | -3.5 | 0.014 | 32/48 (J82, NCI-H1792, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.743×** | -3.5 | 0.015 | 29/48 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.574×** | -3.4 | 0.018 | 29/49 (A-427, SNU-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Fluvoxamine (drug)]] 0.5 µM |  | **0.774×** | -3.0 | 0.078 | 22/48 (SNU-423, LOX-IMVI, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.45 per unit of S-phase module lfc, +0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9279. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 105 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.253× (z -14.5) |
| [[NCI-H460 (line)]] | wt | 94.3 | 1 (1 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.46× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -16.3) |
| [[HEC-1-A (line)]] | alt | 124 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.85× (z +10.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -11.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.394× (z -9.5) |
| [[LoVo (line)]] | wt | 65.9 | 0 | 5 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.316× (z -11.6) |
| [[LS 180 (line)]] | wt | 118 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.301× (z -11.9) |
| [[NCI-H1573 (line)]] | alt | 111 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -15.9) |
| [[A-427 (line)]] | wt | 68.8 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.80× (z +8.5) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.303× (z -10.1) |
| [[MIA PaCa-2 (line)]] | alt | 72.5 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.246× (z -12.0) |
| [[SW48 (line)]] | wt | 100 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.239× (z -10.6) |
| [[C32 (line)]] | wt | 80.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -14.8) |
| [[HCT15 (line)]] | alt | 135 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.250× (z -12.7) |
| [[LOX-IMVI (line)]] | wt | 50.8 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.329× (z -9.2) |
| [[SNU-1 (line)]] | wt | 81.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.227× (z -10.9) |
| [[A498 (line)]] | wt | 49.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.63× (z +10.9) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 71.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.86× (z +9.2) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 89.5 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.219× (z -14.3) |
| [[KATO III (line)]] | alt | 104 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.42× (z +8.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.422× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 70.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +9.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.301× (z -10.0) |
| [[PANC-1 (line)]] | alt | 109 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.372× (z -9.8) |
| [[RKO (line)]] | wt | 43.6 | 0 | 2 | — | [[Belinostat (drug)]] 0.5 µM 0.304× (z -8.6) |
| [[A549 (line)]] | wt | 76.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.346× (z -8.9) |
| [[HepG2_C3A (line)]] | wt | 75.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.251× (z -10.1) |
| [[HOP62 (line)]] | alt | 76.2 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.326× (z -10.1) |
| [[HS-578T (line)]] | alt | 42.7 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.296× (z -9.3) |
| [[hTERT-HPNE (line)]] | wt | 49.4 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.276× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 57.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.328× (z -8.7) |
| [[SHP-77 (line)]] | alt | 21.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.182× (z -9.2) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 57.6 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.299× (z -9.1) |
| [[SW1417 (line)]] | alt | 83.4 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.382× (z -8.7) |
| [[A-172 (line)]] | wt | 49.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 67.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 63.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 62.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 87.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 55.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 59.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 71.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 59.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 77.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 55.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 75.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 69.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 51.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9279), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRMT10B]] | +0.68 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[C1orf43]] | +0.65 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[RAD52]] | +0.65 | +0.64 / +0.57 | both halves | 8e-06 |  |
| [[C15orf40]] | +0.62 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[ZC3H6]] | +0.60 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[TRPM7]] | +0.60 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[SUMO4]] | +0.59 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[COMMD3]] | +0.59 | +0.58 / +0.57 | both halves | 9e-06 |  |
| [[CLK4]] | +0.59 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[ZNF428]] | +0.59 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[HEIH]] | +0.59 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[AKAP10]] | +0.58 | +0.54 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GATAD2A]] | -0.64 | -0.62 / -0.60 | both halves | 7e-06 |  |
| [[CDC42EP2]] | -0.63 | -0.59 / -0.61 | both halves | 7e-06 |  |
| [[TPM3]] | -0.62 | -0.56 / -0.64 | both halves | 1e-05 |  |
| [[EIF5A]] | -0.59 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[PYCR3]] | -0.59 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[KCNC4]] | -0.58 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[CDK2]] | -0.56 | -0.57 / -0.57 | both halves | 1e-05 | pathway: APC/C-mediated degradation of cell cycle proteins; STRING 555 |
| [[ABHD17A]] | -0.56 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[SLC35C1]] | -0.56 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[BCAP31]] | -0.56 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[PLXNA1]] | -0.55 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[ZNF731P]] | -0.55 | -0.52 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.625). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-20.2, 15.9); signed map (8.5, -21.7). **Vector** length 91.8, 30.7% of its response variance represented; |z| ≥ 3 in 974 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +5.8 | -0.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.6 | -5.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.3 | +3.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.2 | -3.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.9 | +0.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.4 | +3.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.8 | +1.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.6 | +2.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.5 | +3.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -6.8 | -7.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.0 | -5.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.8 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -2.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.4 | -2.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.0 | -1.7 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.9 | -0.3 |
|  | [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | -1.8 | -0.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.7 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | anaphase promoting complex subunit 16 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.1 — chr10:72,216,000-72,235,860 (+) |
| Ensembl biotype | protein_coding |
| Also known as | bA570G20.3, FLJ33728, APC16, CENP-27; previously C10orf104 |
| Gene groups (HGNC) | Anaphase promoting complex |
| Reactome | 39 pathways, smallest: Aberrant regulation of mitotic exit in cancer due to RB1 defects; Conversion from APC/C:Cdc20 to APC/C:Cdh1 in late anaphase; Phosphorylation of the APC/C |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96DE5](https://www.uniprot.org/uniprotkb/Q96DE5) (Anaphase-promoting complex subunit 16):

> Component of the anaphase promoting complex/cyclosome (APC/C), a cell cycle-regulated E3 ubiquitin ligase that controls progression through the cell cycle. APC/C acts by mediating ubiquitination and subsequent degradation of target proteins: it mainly mediates the formation of 'Lys-11'-linked polyubiquitin chains and, to a lower extent, the formation of 'Lys-48'- and 'Lys-63'-linked polyubiquitin chains. APC/C catalyzes assembly of branched 'Lys-11'-/'Lys-48'-linked branched ubiquitin chains on …

**Summary**, from NCBI Gene [119504](https://www.ncbi.nlm.nih.gov/gene/119504):

> Involved in anaphase-promoting complex-dependent catabolic process and protein polyubiquitination. Located in cytosol and kinetochore. Part of anaphase-promoting complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26976](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26976) · Entrez [119504](https://www.ncbi.nlm.nih.gov/gene/119504) · UniProt [Q96DE5](https://www.uniprot.org/uniprotkb/Q96DE5) · Ensembl [ENSG00000166295](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166295)

## Data

Gene col 9279: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9279); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9279, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9279]; `tensor/DDL_lfc|DDL_z.npy` [9279]; `embed/gene_vectors.npy` [9279]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9279 or target_col == 9279). Every well: [[ANAPC16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANAPC16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
