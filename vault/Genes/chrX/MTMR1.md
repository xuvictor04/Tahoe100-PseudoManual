---
symbol: "MTMR1"
type: "gene"
col: 730
ensembl_id: "ENSG00000063601"
name: "myotubularin related protein 1"
location: "Xq28"
module: 88
arm: "+"
pooled_cpm: 56.61
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 23
n_dd_up_clean: 2
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/088"]
generated_by: "tahoemap"
---

# MTMR1

*myotubularin related protein 1* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 2.03× (z +6.6, q 3e-08, up in 31 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (PANC-1 2.17×, BT-474 2.71×, HOP62 2.01×, CFPAC-1 1.84×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (BT-474 3.11×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.375× (z -17.3, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZC3H7B]] (+0.60, fdr 1e-05), [[UMPS]] (+0.54, fdr 3e-05), [[DDAH1]] (+0.53, fdr 2e-05); moves opposite to [[STRN]] (-0.56, fdr 6e-05), [[CARD19]] (-0.53, fdr 5e-05), [[MPZL1]] (-0.53, fdr 5e-05).
> It sits in the **+** arm of [[Module 088]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 730.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (PANC-1 2.17×, BT-474 2.71×, HOP62 2.01×, CFPAC-1 1.84×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (BT-474 3.11×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.03×** | +6.6 | 3e-08 | 31/49 (NCI-H1573, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.68×** | +4.8 | 4e-04 | 30/48 (NCI-H1573, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +4.5 | 0.001 | 24/48 (PANC-1, BT-474, …) | top dose only | composition shift |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 1.21× | +3.3 | 0.12 | 13/48 (SW480, KATO III, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.2 | 0.16 | 20/48 (BT-474, hTERT-HPNE, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 730.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.375×** | -17.3 | 0e+00 | 46/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.388×** | -16.7 | 0e+00 | 46/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.455×** | -13.9 | 1e-41 | 45/48 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.671×** | -9.9 | 4e-21 | 40/48 (LOX-IMVI, A-172, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.584×** | -9.5 | 3e-19 | 39/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.638×** | -7.6 | 2e-12 | 34/47 (NCI-H460, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.668×** | -6.6 | 4e-09 | 31/44 (LS 180, A549, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.693×** | -6.5 | 8e-09 | 33/48 (CFPAC-1, J82, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **0.695×** | -6.4 | 1e-08 | 33/49 (RKO, H4, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.706×** | -6.1 | 5e-08 | 29/48 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.523×** | -6.0 | 1e-07 | 28/43 (NCI-H1792, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.786×** | -6.0 | 1e-07 | 30/48 (SW480, SW1417, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.724×** | -5.7 | 6e-07 | 31/48 (HOP62, SNU-423, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.726×** | -5.6 | 7e-07 | 28/48 (HOP62, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.733×** | -5.5 | 2e-06 | 32/47 (SW 1271, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.782×** | -4.3 | 5e-04 | 24/48 (HEC-1-A, RPMI-7951, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.778×** | -4.2 | 9e-04 | 24/48 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.821×** | -3.5 | 0.014 | 21/48 (HEC-1-A, SNU-423, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.690×** | -3.4 | 0.017 | 19/49 (SHP-77, COLO 205, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.712×** | -3.1 | 0.044 | 15/48 (A549, SW480, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 730. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 71.7 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.320× (z -12.2) |
| [[A-172 (line)]] | wt | 53.5 | 0 | 5 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -15.0) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.304× (z -13.1) |
| [[HOP62 (line)]] | alt | 55.8 | 1 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +9.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Auranofin (drug)]] 5 µM 0.355× (z -10.4) |
| [[Hs 766T (line)]] | wt | 65.2 | 0 | 5 (1 ⚠) | — | [[Pimitespib (drug)]] 5 µM 0.0579× (z -13.1) |
| [[MIA PaCa-2 (line)]] | alt | 65.9 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.258× (z -13.3) |
| [[NCI-H460 (line)]] | wt | 52.6 | 0 | 5 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.329× (z -13.5) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.351× (z -13.2) |
| [[A549 (line)]] | wt | 60.3 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.356× (z -10.9) |
| [[CFPAC-1 (line)]] | alt | 69.9 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.305× (z -12.6) |
| [[KATO III (line)]] | alt | 72.6 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.272× (z -14.1) |
| [[RKO (line)]] | wt | 66.4 | 0 | 4 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.139× (z -16.9) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.256× (z -12.1) |
| [[SW480 (line)]] | alt | 72.5 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.256× (z -17.7) |
| [[BT-474 (line)]] | alt | 45.2 | 2 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +11.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.291× (z -9.6) |
| [[LoVo (line)]] | wt | 41.0 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.345× (z -10.8) |
| [[LOX-IMVI (line)]] | wt | 62.0 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.289× (z -12.4) |
| [[NCI-H1573 (line)]] | alt | 43.9 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.198× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.388× (z -8.7) |
| [[SHP-77 (line)]] | alt | 57.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.169× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.337× (z -9.0) |
| [[SW 900 (line)]] | alt | 65.2 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.363× (z -9.3) |
| [[SW1417 (line)]] | alt | 62.6 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.257× (z -14.1) |
| [[COLO 205 (line)]] | alt | 62.3 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.356× (z -8.9) |
| [[HT-29 (line)]] | alt | 80.5 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.355× (z -9.8) |
| [[NCI-H1792 (line)]] | alt | 47.5 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.313× (z -9.9) |
| [[PANC-1 (line)]] | alt | 81.9 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +13.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.454× (z -9.6) |
| [[SK-MEL-2 (line)]] | alt | 64.6 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.309× (z -10.7) |
| [[SW48 (line)]] | wt | 51.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.172× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.308× (z -8.6) |
| [[A498 (line)]] | wt | 31.9 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.379× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 52.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.507× (z -9.0) |
| [[CHP-212 (line)]] | wt | 44.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.120× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 39.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0984× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[HCT15 (line)]] | alt | 68.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.319× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change |
| [[HS-578T (line)]] | alt | 29.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -8.9) |
| [[J82 (line)]] | alt | 54.6 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.369× (z -9.6) |
| [[LS 180 (line)]] | wt | 39.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.301× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[NCI-H23 (line)]] | alt | 51.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.358× (z -9.6) |
| [[Panc 03.27 (line)]] | alt | 72.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.343× (z -9.6) |
| [[RPMI-7951 (line)]] | alt | 37.4 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.279× (z -9.7) |
| [[SNU-423 (line)]] | alt | 57.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.395× (z -9.1) |
| [[A-427 (line)]] | wt | 37.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 46.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 39.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 36.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 73.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 730), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZC3H7B]] | +0.60 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[UMPS]] | +0.54 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[DDAH1]] | +0.53 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[INTS14]] | +0.53 | +0.43 / +0.39 | both halves | 6e-05 |  |
| [[AMOTL2]] | +0.53 | +0.49 / +0.37 | both halves | 8e-05 |  |
| [[AXL]] | +0.53 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[TXNRD2]] | +0.52 | +0.34 / +0.43 | both halves | 1e-04 |  |
| [[C12orf4]] | +0.51 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[LGALSL-DT]] | +0.51 | +0.41 / +0.32 | both halves | 2e-04 |  |
| [[PYM1]] | +0.50 | +0.42 / +0.36 | both halves | 1e-04 |  |
| [[ERCC6L2]] | +0.49 | +0.36 / +0.31 | both halves | 2e-04 |  |
| [[LATS1]] | +0.49 | +0.42 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STRN]] | -0.56 | -0.48 / -0.38 | both halves | 6e-05 |  |
| [[CARD19]] | -0.53 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[MPZL1]] | -0.53 | -0.39 / -0.42 | both halves | 5e-05 |  |
| [[NEAT1]] | -0.53 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[EFNA4]] | -0.51 | -0.31 / -0.44 | both halves | 2e-04 |  |
| [[MKNK2]] | -0.51 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[NCOA3]] | -0.49 | -0.39 / -0.47 | both halves | 6e-05 |  |
| [[DDIT4]] | -0.48 | -0.29 / -0.54 | both halves | 2e-04 |  |
| [[FXR1]] | -0.48 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[YIPF1]] | -0.48 | -0.35 / -0.34 | both halves | 1e-04 |  |
| [[MIIP]] | -0.48 | -0.48 / -0.27 | both halves | 3e-04 |  |
| [[SS18L1]] | -0.46 | -0.39 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 088]]; 51 genes; this gene is in the **+** arm (projection on the module's main direction 0.488). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.46).
- **Nodal map** (x, y) = (-4.1, -0.3); signed map (22.5, -40.5). **Vector** length 88.9, 22.5% of its response variance represented; |z| ≥ 3 in 1,141 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +10.2 | +4.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +7.5 | +1.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.6 | +6.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.2 | -2.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.1 | -0.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | -1.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | +4.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.4 | +2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.1 | +1.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.0 | +1.6 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.3 | -6.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.3 | -7.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.6 | -5.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -1.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.8 | -4.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.6 | -1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | -5.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.9 | -2.3 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | -1.8 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | myotubularin related protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:150,692,971-150,765,108 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Myotubularins; Phosphoinositide phosphatases |
| Reactome | 8 pathways, smallest: RHOF GTPase cycle; Synthesis of PIPs at the plasma membrane; PI Metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13613](https://www.uniprot.org/uniprotkb/Q13613) (Phosphatidylinositol-3-phosphate phosphatase MTMR1):

> Lipid phosphatase that specifically dephosphorylates the D-3 position of phosphatidylinositol 3-phosphate, generating phosphatidylinositol. Could also dephosphorylate phosphatidylinositol 3,5-bisphosphate to produce phosphatidylinositol 5-phosphate.

**Summary**, from NCBI Gene [8776](https://www.ncbi.nlm.nih.gov/gene/8776):

> This gene encodes a member of the myotubularin related family of proteins. Members of this family contain the consensus sequence for the active site of protein tyrosine phosphatases. Alternatively spliced variants have been described but their biological validity has not been determined. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:7449](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7449) · Entrez [8776](https://www.ncbi.nlm.nih.gov/gene/8776) · UniProt [Q13613](https://www.uniprot.org/uniprotkb/Q13613) · Ensembl [ENSG00000063601](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000063601)

## Data

Gene col 730: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 730); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 730, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 730]; `tensor/DDL_lfc|DDL_z.npy` [730]; `embed/gene_vectors.npy` [730]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 730 or target_col == 730). Every well: [[MTMR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTMR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
