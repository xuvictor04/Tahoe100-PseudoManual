---
symbol: "ARIH2"
type: "gene"
col: 10826
ensembl_id: "ENSG00000177479"
name: "ariadne RBR E3 ubiquitin protein ligase 2"
location: "3p21.31"
module: 36
arm: "+"
pooled_cpm: 78.07
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# ARIH2

*ariadne RBR E3 ubiquitin protein ligase 2* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (14 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.59× (z +17.8, q 0e+00, up in 40 of 49 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (C-33 A 0.231×, RKO 0.493×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.532×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TIMM23B-AGAP6]] (+0.67, fdr 7e-06), [[TIMM23B]] (+0.63, fdr 1e-05), [[TRAPPC10]] (+0.62, fdr 1e-05); moves opposite to [[RYBP]] (-0.60, fdr 1e-05), [[ARL4D]] (-0.57, fdr 1e-05), [[HPF1]] (-0.57, fdr 2e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[RYBP]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 50 in all, 25 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10826.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +17.8 | 0e+00 | 40/49 (NCI-H2347, LS 180, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.74×** | +15.1 | 0e+00 | 46/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.68×** | +13.6 | 7e-40 | 42/48 (LS 180, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.64×** | +13.4 | 1e-38 | 44/48 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.63×** | +13.2 | 1e-37 | 44/48 (HOP62, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **1.64×** | +13.0 | 8e-37 | 36/49 (SW480, NCI-H1792, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +12.6 | 2e-34 | 41/47 (NCI-H23, LoVo, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.59×** | +11.6 | 5e-29 | 37/45 (SW480, RPMI-7951, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.52×** | +11.4 | 3e-28 | 36/48 (LS 180, HOP62, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.51×** | +11.3 | 1e-27 | 45/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.53×** | +11.0 | 1e-26 | 38/50 (LS 180, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **1.50×** | +10.6 | 9e-25 | 28/44 (SW480, NCI-H460, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.47×** | +10.5 | 3e-24 | 37/48 (HOP62, HEC-1-A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.46×** | +10.3 | 2e-23 | 42/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.44×** | +10.0 | 6e-22 | 36/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.00×** | +9.8 | 3e-21 | 34/48 (RKO, LoVo, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +9.2 | 2e-18 | 34/48 (SW480, NCI-H2347, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.39×** | +8.5 | 6e-16 | 34/48 (PANC-1, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.77×** | +8.1 | 1e-14 | 38/49 (LoVo, A498, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.33×** | +7.7 | 3e-13 | 35/48 (PANC-1, HOP62, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.18× | +4.4 | 2e-04 | 18/48 (HOP62, BT-474, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.12× | +4.2 | 4e-04 | 8/49 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.11× | +4.1 | 8e-04 | 12/48 (NCI-H2347, SNU-423, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.13× | +3.3 | 0.014 | 14/47 (NCI-H23, HOP62, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 1.14× | +3.2 | 0.022 | 12/47 (BT-474, LOX-IMVI, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10826.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (C-33 A 0.231×, RKO 0.493×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.532×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.905× | -3.9 | 0.041 | 5/48 (NCI-H2030, NCI-H661, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.865× | -3.8 | 0.041 | 18/47 (NCI-H23, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.870× | -3.7 | 0.047 | 11/48 (C-33 A, SK-MEL-2, …) | rises with dose |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 0.883× | -3.4 | 0.089 | 9/48 (NCI-H2030, SW1417, …) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.884× | -3.4 | 0.089 | 10/48 (hTERT-HPNE, A-427, …) | inconsistent across doses |  |
| [[Balsalazide (sodium hydrate) (drug)]] 5 µM |  | 0.920× | -3.2 | 0.13 | 2/48 (SW 1271, COLO 205) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~51% of this change | 0.892× | -3.1 | 0.15 | 9/49 (NCI-H1792, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10826. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 88.8 | 9 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.76× (z +11.8) | — |
| [[HOP62 (line)]] | alt | 69.9 | 8 (5 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.33× (z +11.3) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +10.3) | — |
| [[SW480 (line)]] | alt | 97.4 | 7 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.69× (z +16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.92× (z +11.3) | — |
| [[LS 180 (line)]] | wt | 67.1 | 6 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +16.3) | — |
| [[NCI-H1792 (line)]] | alt | 61.7 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.07× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +9.6) | — |
| [[LOX-IMVI (line)]] | wt | 75.0 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +14.4) | — |
| [[NCI-H23 (line)]] | alt | 94.0 | 4 (4 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.83× (z +12.4) ⚠ toxic | — |
| [[NCI-H460 (line)]] | wt | 57.0 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +13.9) | — |
| [[NCI-H2347 (line)]] | alt | 77.3 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +16.5) | — |
| [[A-427 (line)]] | wt | 95.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.04× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -8.7) |
| [[A498 (line)]] | wt | 65.4 | 2 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +9.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.56× (z +8.5) | — |
| [[A549 (line)]] | wt | 59.0 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +10.1) | — |
| [[C32 (line)]] | wt | 82.5 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +12.0) | — |
| [[CFPAC-1 (line)]] | alt | 29.3 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +9.9) | — |
| [[HEC-1-A (line)]] | alt | 103 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 1.92× (z +10.6) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 66.8 | 2 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.26× (z +10.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +8.8) | — |
| [[NCI-H1573 (line)]] | alt | 42.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.46× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | — |
| [[Panc 03.27 (line)]] | alt | 66.0 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +10.7) | — |
| [[RKO (line)]] | wt | 124 | 1 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 3.19× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.493× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[SW48 (line)]] | wt | 93.9 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +9.5) | — |
| [[A-172 (line)]] | wt | 59.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.44× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[AsPC-1 (line)]] | alt | 60.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +10.7) | — |
| [[C-33 A (line)]] | alt | 114 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.231× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[COLO 205 (line)]] | alt | 40.8 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.78× (z +9.9) | — |
| [[Hs 766T (line)]] | wt | 51.4 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.61× (z +8.6) | — |
| [[J82 (line)]] | alt | 97.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.62× (z +9.1) | — |
| [[KATO III (line)]] | alt | 78.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.01× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[PANC-1 (line)]] | alt | 86.9 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.74× (z +8.7) | — |
| [[RPMI-7951 (line)]] | alt | 97.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.56× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[SNU-423 (line)]] | alt | 62.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +9.9) | — |
| [[SW 900 (line)]] | alt | 63.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +9.2) | — |
| [[SW1417 (line)]] | alt | 119 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.53× (z +9.6) | — |
| [[AN3 CA (line)]] | alt | 115 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 103 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 42.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 83.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 73.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 79.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 62.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 76.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 88.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 77.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 95.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 85.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 71.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10826), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIMM23B-AGAP6]] | +0.67 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[TIMM23B]] | +0.63 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[TRAPPC10]] | +0.62 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[POLR3E]] | +0.61 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[FOXK2]] | +0.61 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[ZNF767P-1]] | +0.60 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[FBXW11]] | +0.60 | +0.54 / +0.61 | both halves | 1e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[FUBP3]] | +0.60 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[TMEM11-DT]] | +0.59 | +0.68 / +0.46 | both halves | 3e-05 |  |
| [[NR2C2]] | +0.59 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[GART]] | +0.59 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[NIPA2]] | +0.58 | +0.55 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RYBP]] | -0.60 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[ARL4D]] | -0.57 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[HPF1]] | -0.57 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[TRMT1L]] | -0.56 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[TUBB2A]] | -0.56 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[NET1]] | -0.56 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[RAB30]] | -0.55 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[BTN2A2]] | -0.55 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[SFR1]] | -0.54 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[NUDT12]] | -0.54 | -0.43 / -0.54 | both halves | 4e-05 |  |
| [[SNAPIN]] | -0.54 | -0.46 / -0.51 | both halves | 2e-05 |  |
| [[ZNF184]] | -0.53 | -0.52 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RYBP]] | C | ARIH2's natural level strengthens RYBP's drug response | ARIH2's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.00; direction clear | 0.046 | ⚠ tissue can mimic it; precision caveat |

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.606). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-12.3, -17.6); signed map (-46.0, -20.5). **Vector** length 83.7, 21.9% of its response variance represented; |z| ≥ 3 in 1,355 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +5.5 | +13.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | +4.6 | +13.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +4.5 | +11.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | +4.3 | +10.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +17.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +4.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +9.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.5 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +9.2 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -8.0 | +1.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -6.6 | +6.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.3 | -1.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | -1.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.2 | +4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -2.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.3 | -1.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.9 | -1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.7 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | ariadne RBR E3 ubiquitin protein ligase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:48,918,821-48,986,382 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TRIAD1 |
| Gene groups (HGNC) | Ring finger proteins; RBR E3 ubiquitin ligases |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [O95376](https://www.uniprot.org/uniprotkb/O95376) (E3 ubiquitin-protein ligase ARIH2):

> E3 ubiquitin-protein ligase, which catalyzes ubiquitination of target proteins together with ubiquitin-conjugating enzyme E2 UBE2L3. Acts as an atypical E3 ubiquitin-protein ligase by working together with cullin-5-RING ubiquitin ligase complex (ECS complex, also named CRL5 complex) and initiating ubiquitination of ECS substrates: associates with ECS complex and specifically mediates addition of the first ubiquitin on ECS targets. The initial ubiquitin is then elongated. E3 ubiquitin-protein …

**Summary**, from NCBI Gene [10425](https://www.ncbi.nlm.nih.gov/gene/10425):

> The protein encoded by this gene is an E3 ubiquitin-protein ligase that polyubiquitinates some proteins, tagging them for degradation. The encoded protein upregulates p53 in some cancer cells and may inhibit myelopoiesis. Several transcript variants encoding different isoforms have been found for this gene, although the full-length nature of some of them have not been determined yet. [provided by RefSeq, Nov 2015]

**Accessions** — [HGNC:690](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:690) · Entrez [10425](https://www.ncbi.nlm.nih.gov/gene/10425) · UniProt [O95376](https://www.uniprot.org/uniprotkb/O95376) · Ensembl [ENSG00000177479](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177479)

## Data

Gene col 10826: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10826); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10826, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10826]; `tensor/DDL_lfc|DDL_z.npy` [10826]; `embed/gene_vectors.npy` [10826]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10826 or target_col == 10826). Every well: [[ARIH2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARIH2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
