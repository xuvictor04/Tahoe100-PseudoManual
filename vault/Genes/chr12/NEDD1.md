---
symbol: "NEDD1"
type: "gene"
col: 6296
ensembl_id: "ENSG00000139350"
name: "NEDD1 gamma-tubulin ring complex targeting factor"
location: "12q23.1"
module: 6
arm: "+"
pooled_cpm: 53.91
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 5
n_dd_up_clean: 2
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# NEDD1

*NEDD1 gamma-tubulin ring complex targeting factor* — 12q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.42× (z +13.1, q 3e-36, up in 34 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (MIA PaCa-2 2.32×, CFPAC-1 2.31×, SNU-423 2.01×, RPMI-7951 2.40×, …); [[Homoharringtonine (drug)]] 5 µM in 2 lines (Hs 766T 2.20×, LS 180 1.83×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW480 2.05×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.632× (z -12.1, q 3e-31, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACTL6A]] (+0.69, fdr 7e-06), [[ZWILCH]] (+0.69, fdr 7e-06), [[CEP78]] (+0.61, fdr 1e-05); moves opposite to [[CELF6]] (-0.62, fdr 1e-05), [[CLDN15]] (-0.52, fdr 3e-05), [[ATP6V0C]] (-0.50, fdr 3e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 12 with an alert ⚠; shown: the 15 strongest. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6296.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (MIA PaCa-2 2.32×, CFPAC-1 2.31×, SNU-423 2.01×, RPMI-7951 2.40×, …); [[Homoharringtonine (drug)]] 5 µM in 2 lines (Hs 766T 2.20×, LS 180 1.83×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW480 2.05×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +13.1 | 3e-36 | 34/48 (MIA PaCa-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.48×** | +10.4 | 1e-22 | 37/48 (RKO, NCI-H1792, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.44×** | +9.6 | 2e-19 | 34/48 (LOX-IMVI, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **1.40×** | +8.6 | 8e-16 | 30/41 (PANC-1, A498, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.38×** | +8.4 | 4e-15 | 30/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change | **1.30×** | +6.9 | 4e-10 | 27/48 (SW480, J82, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.27×** | +6.3 | 2e-08 | 27/48 (SW480, RKO, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.21×** | +4.8 | 9e-05 | 21/48 (MIA PaCa-2, HEC-1-A, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | 1.19× | +4.5 | 5e-04 | 14/48 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.37×** | +4.4 | 6e-04 | 17/49 (HT-29, RKO, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.19× | +4.3 | 1e-03 | 18/47 (A549, LoVo, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.17× | +4.2 | 0.001 | 15/48 (LS 180, NCI-H460, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | 1.17× | +4.0 | 0.003 | 18/49 (SW480, RPMI-7951, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 1.16× | +4.0 | 0.003 | 16/48 (NCI-H460, LS 180, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 1.16× | +3.8 | 0.005 | 15/48 (RKO, HT-29, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6296.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.632×** | -12.1 | 3e-31 | 34/48 (NCI-H460, SW480, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.697×** | -9.6 | 3e-19 | 25/47 (SW480, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.587×** | -7.4 | 3e-11 | 27/49 (AsPC-1, NCI-H1792, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.629×** | -6.4 | 2e-08 | 26/48 (MIA PaCa-2, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.801×** | -5.9 | 5e-07 | 24/48 (SW480, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | 0.857× | -3.9 | 0.011 | 14/48 (SW480, J82, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.867× | -3.8 | 0.012 | 17/48 (SW480, LoVo, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | 0.876× | -3.5 | 0.031 | 8/49 (PANC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.877× | -3.5 | 0.031 | 14/48 (SW480, SNU-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | 0.912× | -3.4 | 0.032 | 10/48 (A-427, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.883× | -3.3 | 0.050 | 13/49 (A-172, HCT15, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 5 µM |  | 0.919× | -3.2 | 0.070 | 5/49 (NCI-H460, J82, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | 0.887× | -3.1 | 0.072 | 9/47 (RPMI-7951, NCI-H460, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.889× | -3.1 | 0.072 | 10/48 (SW1417, Panc 03.27, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.921× | -3.1 | 0.073 | 17/48 (LoVo, COLO 205, …) | top dose only | composition shift |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 0.887× | -3.1 | 0.073 | 6/49 (NCI-H1792, AsPC-1, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6296. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 49.1 | 1 (1 ⚠) | 5 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.05× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change | [[Digitoxin (drug)]] 5 µM 0.348× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.491× (z -10.2) |
| [[NCI-H460 (line)]] | wt | 183 | 0 | 4 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.269× (z -11.5) |
| [[A-427 (line)]] | wt | 74.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.352× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[AsPC-1 (line)]] | alt | 48.8 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.323× (z -10.8) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 38.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +8.5) | — |
| [[C32 (line)]] | wt | 25.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.115× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 38.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +11.1) | — |
| [[HOP62 (line)]] | alt | 36.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.383× (z -9.1) |
| [[LS 180 (line)]] | wt | 48.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +9.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 47.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +11.7) | — |
| [[NCI-H2347 (line)]] | alt | 46.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.468× (z -9.4) |
| [[RPMI-7951 (line)]] | alt | 34.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +9.4) | — |
| [[SHP-77 (line)]] | alt | 65.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.411× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 43.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.340× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change |
| [[SNU-423 (line)]] | alt | 41.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +9.6) | — |
| [[SW 1271 (line)]] | alt | 68.1 | 0 | 1 | — | [[Allantoin (drug)]] 0.5 µM 0.0754× (z -10.1) |
| [[SW48 (line)]] | wt | 49.3 | 0 | 1 | — | [[OTS514 (drug)]] 5 µM 0.0694× (z -10.0) |
| [[A-172 (line)]] | wt | 62.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 49.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 58.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 70.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 76.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 36.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 46.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 35.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 44.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 54.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 53.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 46.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 43.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6296), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACTL6A]] | +0.69 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[ZWILCH]] | +0.69 | +0.68 / +0.66 | both halves | 7e-06 | pathway: Mitotic Prometaphase |
| [[CEP78]] | +0.61 | +0.55 / +0.62 | both halves | 1e-05 | pathway: AURKA Activation by TPX2 |
| [[CENPU]] | +0.59 | +0.57 / +0.55 | both halves | 1e-05 | pathway: Mitotic Prometaphase |
| [[DDIAS]] | +0.59 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[CEP57L1]] | +0.59 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[CENPH]] | +0.59 | +0.48 / +0.62 | both halves | 2e-05 | pathway: Mitotic Prometaphase |
| [[VRK1]] | +0.58 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[C18orf54]] | +0.58 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[PBK]] | +0.58 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[ARMC1]] | +0.58 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[WDHD1]] | +0.58 | +0.54 / +0.56 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CELF6]] | -0.62 | -0.51 / -0.66 | both halves | 1e-05 |  |
| [[CLDN15]] | -0.52 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[ATP6V0C]] | -0.50 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[GRK7]] | -0.50 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[LINC01618]] | -0.49 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[AP5Z1]] | -0.48 | -0.39 / -0.51 | both halves | 6e-05 |  |
| [[LINC02646]] | -0.48 | -0.44 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers NEDD1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.534). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-39.7, -45.5); signed map (-40.2, -49.2). **Vector** length 103, 23.4% of its response variance represented; |z| ≥ 3 in 1,005 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change | +4.4 | +6.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | +3.4 | +8.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | +3.3 | +4.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | +3.0 | +4.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.9 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +4.2 |
|  | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | +1.9 | +1.6 |
|  | [[Raltitrexed (drug)]] 0.5 µM |  | +1.8 | +2.2 |
|  | [[Asciminib (drug)]] 0.05 µM |  | +1.8 | +1.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -9.0 | -12.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.8 | -7.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.6 | -3.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.5 | -6.4 |
|  | [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | -3.2 | -3.9 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.5 | -2.1 |
|  | [[Temsirolimus (drug)]] 5 µM |  | -2.5 | -3.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.5 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | NEDD1 gamma-tubulin ring complex targeting factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.1 — chr12:96,907,224-96,953,780 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GCP-WD, TUBGCP7 |
| Gene groups (HGNC) | WD repeat domain containing |
| Reactome | 17 pathways, smallest: Loss of Nlp from mitotic centrosomes; Loss of proteins required for interphase microtubule organization from the centrosome; AURKA Activation by TPX2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NHV4](https://www.uniprot.org/uniprotkb/Q8NHV4) (Protein NEDD1):

> Required for mitosis progression. Promotes the nucleation of microtubules from the spindle.

**Summary**, from NCBI Gene [121441](https://www.ncbi.nlm.nih.gov/gene/121441):

> Predicted to enable gamma-tubulin binding activity. Predicted to be involved in microtubule nucleation and mitotic cell cycle. Located in centrosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:7723](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7723) · Entrez [121441](https://www.ncbi.nlm.nih.gov/gene/121441) · UniProt [Q8NHV4](https://www.uniprot.org/uniprotkb/Q8NHV4) · Ensembl [ENSG00000139350](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139350)

## Data

Gene col 6296: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6296); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6296, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6296]; `tensor/DDL_lfc|DDL_z.npy` [6296]; `embed/gene_vectors.npy` [6296]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6296 or target_col == 6296). Every well: [[NEDD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NEDD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
