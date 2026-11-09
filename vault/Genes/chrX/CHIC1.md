---
symbol: "CHIC1"
type: "gene"
col: 12813
ensembl_id: "ENSG00000204116"
name: "cysteine rich hydrophobic domain 1"
location: "Xq13.2"
module: 51
arm: "+"
pooled_cpm: 36.63
n_lines_expressing: 44
n_dd_up: 10
n_dd_down: 22
n_dd_up_clean: 7
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# CHIC1

*cysteine rich hydrophobic domain 1* — Xq13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.43× (z +8.6, q 5e-15, up in 29 of 42 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.41× (z +5.8, q 9e-07, up in 27 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.340× (z -25.8, q 0e+00, down in 40 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABCB7]] (+0.68, fdr 1e-05), [[CC2D2A]] (+0.63, fdr 3e-05), [[THUMPD2]] (+0.63, fdr 1e-05); moves opposite to [[SENP5]] (-0.65, fdr 7e-06), [[FBH1]] (-0.64, fdr 1e-05), [[LRRC8A]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LIN28B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12813.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.43×** | +8.6 | 5e-15 | 29/42 (A-427, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.41×** | +5.8 | 9e-07 | 27/42 (NCI-H460, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.41×** | +5.8 | 9e-07 | 23/42 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.28×** | +5.8 | 9e-07 | 22/42 (A-427, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.38×** | +5.3 | 2e-05 | 25/42 (A-427, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.33×** | +4.8 | 2e-04 | 22/42 (HOP62, LoVo, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.26×** | +3.8 | 0.010 | 16/42 (NCI-H1573, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.25×** | +3.7 | 0.014 | 19/42 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.48×** | +3.4 | 0.038 | 10/42 (SW480, SW1417, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Roxadustat (drug)]] 5 µM |  | **1.23×** | +3.3 | 0.056 | 9/42 (Panc 03.27, A-427, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12813.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.340×** | -25.8 | 0e+00 | 40/42 (NCI-H460, A-172, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.408×** | -14.0 | 5e-42 | 30/39 (NCI-H1573, SW 900, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.455×** | -13.3 | 5e-38 | 41/42 (SW480, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.473×** | -12.6 | 2e-34 | 38/42 (SW480, HT-29, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.506×** | -11.1 | 2e-26 | 35/42 (NCI-H460, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.523×** | -10.9 | 7e-26 | 31/41 (SW480, NCI-H460, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.539×** | -10.0 | 9e-22 | 26/36 (Hs 766T, H4, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.565×** | -9.6 | 4e-20 | 41/42 (SW480, PANC-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.565×** | -9.3 | 1e-18 | 32/41 (NCI-H460, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~23% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.592×** | -8.9 | 5e-17 | 32/42 (SW480, HCT15, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **0.766×** | -4.3 | 8e-04 | 19/40 (A-427, RKO, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.793×** | -3.9 | 0.004 | 17/42 (NCI-H460, HT-29, …) | two highest doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.797×** | -3.8 | 0.005 | 19/41 (RKO, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.797×** | -3.7 | 0.009 | 20/41 (LoVo, H4, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.804×** | -3.7 | 0.009 | 15/42 (LOX-IMVI, RPMI-7951, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.663×** | -3.6 | 0.010 | 16/41 (HCT15, C32, …) | top dose only | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.812×** | -3.4 | 0.022 | 11/42 (COLO 205, CFPAC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.870× | -3.3 | 0.025 | 13/42 (HT-29, H4, …) | two highest doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.727×** | -3.3 | 0.025 | 14/42 (HOP62, HT-29, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.871× | -3.3 | 0.025 | 14/42 (A-172, NCI-H2347, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12813. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 64.1 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.248× (z -16.6) |
| [[NCI-H460 (line)]] | wt | 46.7 | 2 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -20.9) |
| [[SW480 (line)]] | alt | 79.7 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.167× (z -21.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -15.0) |
| [[A-172 (line)]] | wt | 29.2 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +13.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.211× (z -17.4) |
| [[HT-29 (line)]] | alt | 56.3 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.276× (z -14.4) |
| [[SW48 (line)]] | wt | 54.1 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.187× (z -15.8) |
| [[A-427 (line)]] | wt | 45.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +13.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.350× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~35% of this change |
| [[Panc 03.27 (line)]] | alt | 28.7 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.191× (z -17.2) |
| [[PANC-1 (line)]] | alt | 52.3 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -14.6) |
| [[RPMI-7951 (line)]] | alt | 74.9 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.325× (z -13.3) |
| [[COLO 205 (line)]] | alt | 39.1 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.228× (z -10.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -9.5) |
| [[H4 (line)]] | wt | 49.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0978× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.256× (z -8.5) |
| [[HOP62 (line)]] | alt | 32.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.286× (z -15.6) |
| [[Hs 766T (line)]] | wt | 35.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0769× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.336× (z -11.0) |
| [[HS-578T (line)]] | alt | 26.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -13.0) |
| [[NCI-H1573 (line)]] | alt | 44.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0512× (z -25.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -10.9) |
| [[NCI-H23 (line)]] | alt | 53.3 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +11.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -14.0) |
| [[NCI-H2347 (line)]] | alt | 25.6 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +10.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -9.9) |
| [[RKO (line)]] | wt | 58.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.223× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -10.7) |
| [[SHP-77 (line)]] | alt | 46.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.322× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -8.6) |
| [[SNU-423 (line)]] | alt | 67.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.269× (z -16.1) |
| [[SW 900 (line)]] | alt | 27.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0759× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -10.4) |
| [[SW1417 (line)]] | alt | 51.4 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.283× (z -16.4) |
| [[A549 (line)]] | wt | 36.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -14.9) |
| [[AsPC-1 (line)]] | alt | 31.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +10.6) | — |
| [[C-33 A (line)]] | alt | 41.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.223× (z -9.3) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 28.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -13.1) |
| [[CFPAC-1 (line)]] | alt | 33.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -15.3) |
| [[CHP-212 (line)]] | wt | 63.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.112× (z -14.9) |
| [[HCT15 (line)]] | alt | 46.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.294× (z -8.6) |
| [[hTERT-HPNE (line)]] | wt | 29.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -10.0) |
| [[LoVo (line)]] | wt | 19.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -10.7) |
| [[LS 180 (line)]] | wt | 28.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -12.5) |
| [[NCI-H2030 (line)]] | alt | 11.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.195× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 52.4 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0780× (z -9.7) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 69.1 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.150× (z -8.7) ⚠ toxic |
| [[A498 (line)]] | wt | 3.70 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.36 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.70 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.80 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.42 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.12 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12813), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCB7]] | +0.68 | +0.53 / +0.71 | both halves | 1e-05 | STRING 472 |
| [[CC2D2A]] | +0.63 | +0.43 / +0.64 | both halves | 3e-05 |  |
| [[THUMPD2]] | +0.63 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[INTU]] | +0.62 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[ZDHHC17]] | +0.62 | +0.48 / +0.67 | both halves | 2e-05 |  |
| [[KPNA5]] | +0.61 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[ZNF780A]] | +0.61 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[ZNF260]] | +0.60 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[MTPAP]] | +0.60 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[TMEM126B]] | +0.60 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[ZNF280D]] | +0.59 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[ZMYM4]] | +0.59 | +0.46 / +0.61 | both halves | 2e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SENP5]] | -0.65 | -0.60 / -0.64 | both halves | 7e-06 |  |
| [[FBH1]] | -0.64 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[LRRC8A]] | -0.63 | -0.50 / -0.62 | both halves | 1e-05 |  |
| [[MAPKAPK2]] | -0.63 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[DPP9]] | -0.61 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[TPTEP2-CSNK1E]] | -0.60 | -0.47 / -0.67 | both halves | 2e-05 |  |
| [[MYO9B]] | -0.60 | -0.47 / -0.60 | both halves | 2e-05 |  |
| [[RUBCN]] | -0.60 | -0.37 / -0.65 | both halves | 8e-05 |  |
| [[RECQL]] | -0.59 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[EHBP1L1]] | -0.59 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[ARPC5L]] | -0.57 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[RABGEF1]] | -0.57 | -0.48 / -0.61 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LIN28B]] | B | LIN28B activity raises CHIC1's level | lines that do not express LIN28B (31) vs lines expressing it (19) | 1.59× lower at baseline in the lines without LIN28B | 0.042 | ⚠ within organs, on part of the lines; also absent: LRFN5, BARX1, KCNH7 |
| [[ZC3H12B]] | B | ZC3H12B activity raises CHIC1's level | lines that do not express ZC3H12B (21) vs lines expressing it (29) | 1.86× lower at baseline in the lines without ZC3H12B | 0.072 | ⚠ within organs, on part of the lines; also absent: RUNX3, TMEM132D, LINC01876 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.580). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-14.7, 0.2); signed map (9.1, -25.7). **Vector** length 92.1, 22.0% of its response variance represented; |z| ≥ 3 in 952 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +9.7 | +8.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.4 | +5.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +5.8 | +4.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.3 | +5.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.2 | +5.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | -1.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.1 | -0.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.1 | -0.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.1 | -25.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.6 | -3.3 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -3.5 | -2.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.5 | -9.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.3 | -11.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.3 | -3.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.9 | -3.7 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -2.7 | -3.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.4 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | cysteine rich hydrophobic domain 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq13.2 — chrX:73,563,197-73,687,111 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BRX |
| Gene groups (HGNC) | Armadillo like helical domain containing; Cysteine rich hydrophobic domain family |
| Matched by | ensembl_id |

UniProt [Q5VXU3](https://www.uniprot.org/uniprotkb/Q5VXU3) carries no function annotation.

**Summary**, from NCBI Gene [53344](https://www.ncbi.nlm.nih.gov/gene/53344):

> This gene encodes a cysteine-rich hydrophobic (CHIC) domain-containing protein, and is one of the few protein-coding genes found near the X-inactivation center. Studies in mouse indicate that the mouse ortholog of this gene is subject to X-inactivation in mouse. Experiments with other CHIC domain-containing family members show that the cysteine residues are palmitoylated post-translationally, resulting in membrane association. Alternative splicing results in multiple transcript variants …

**Accessions** — [HGNC:1934](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1934) · Entrez [53344](https://www.ncbi.nlm.nih.gov/gene/53344) · UniProt [Q5VXU3](https://www.uniprot.org/uniprotkb/Q5VXU3) · Ensembl [ENSG00000204116](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204116)

## Data

Gene col 12813: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12813); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12813, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12813]; `tensor/DDL_lfc|DDL_z.npy` [12813]; `embed/gene_vectors.npy` [12813]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12813 or target_col == 12813). Every well: [[CHIC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHIC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
