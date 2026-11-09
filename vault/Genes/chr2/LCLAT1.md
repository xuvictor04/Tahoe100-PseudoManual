---
symbol: "LCLAT1"
type: "gene"
col: 10322
ensembl_id: "ENSG00000172954"
name: "lysocardiolipin acyltransferase 1"
location: "2p23.1"
module: 4
arm: "+"
pooled_cpm: 91.33
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 13
n_dd_up_clean: 2
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# LCLAT1

*lysocardiolipin acyltransferase 1* — 2p23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.52× (z +9.4, q 5e-18, up in 41 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 6 lines (LoVo 4.69×, NCI-H1792 5.40×, MIA PaCa-2 4.22×, HEC-1-A 3.84×, …); [[Homoharringtonine (drug)]] 5 µM in 1 line (hTERT-HPNE 6.60×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (hTERT-HPNE 4.85×; ⚠ cell-cycle shift, explains ~54% of this change); [[PH-797804 (drug)]] 5 µM in 1 line (HEC-1-A 3.73×).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.526× (z -11.3, q 5e-27, down in 47 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.665× (z -11.2, q 7e-27, down in 39 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COA1]] (+0.74, fdr 7e-06), [[DIS3L2]] (+0.74, fdr 7e-06), [[SNRPE]] (+0.71, fdr 7e-06); moves opposite to [[ERO1B]] (-0.65, fdr 7e-06), [[YPEL5]] (-0.60, fdr 2e-05), [[RSRP1]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10322.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 6 lines (LoVo 4.69×, NCI-H1792 5.40×, MIA PaCa-2 4.22×, HEC-1-A 3.84×, …); [[Homoharringtonine (drug)]] 5 µM in 1 line (hTERT-HPNE 6.60×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (hTERT-HPNE 4.85×; ⚠ cell-cycle shift, explains ~54% of this change); [[PH-797804 (drug)]] 5 µM in 1 line (HEC-1-A 3.73×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.52×** | +9.4 | 5e-18 | 41/49 (LoVo, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.92×** | +6.6 | 1e-08 | 32/48 (HEC-1-A, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.38×** | +6.2 | 1e-07 | 33/48 (SW480, PANC-1, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | 1.18× | +4.5 | 0.001 | 21/48 (J82, SNU-423, …) | rises with dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10322.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.526×** | -11.3 | 5e-27 | 47/49 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.665×** | -11.2 | 7e-27 | 39/49 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.576×** | -10.3 | 1e-22 | 37/44 (NCI-H1573, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.601×** | -9.9 | 6e-21 | 44/48 (MIA PaCa-2, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.664×** | -7.4 | 2e-11 | 31/45 (HEC-1-A, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.704×** | -6.6 | 5e-09 | 29/48 (SK-MEL-2, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.707×** | -6.5 | 7e-09 | 32/50 (A-427, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.721×** | -6.4 | 1e-08 | 31/48 (NCI-H460, SW48, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.735×** | -5.8 | 5e-07 | 30/47 (NCI-H460, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.821×** | -5.4 | 3e-06 | 26/48 (A498, NCI-H661, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **0.779×** | -4.9 | 6e-05 | 29/48 (SW1417, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.797×** | -4.4 | 5e-04 | 26/49 (NCI-H2347, A498, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.882× | -3.5 | 0.023 | 19/48 (LoVo, COLO 205, …) | rises with dose | composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.844× | -3.3 | 0.038 | 14/49 (MIA PaCa-2, LS 180, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.736×** | -3.1 | 0.065 | 18/48 (HCT15, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.897× | -3.0 | 0.089 | 15/48 (A-172, SW 1271, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10322. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 99.9 | 0 | 9 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.299× (z -17.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -16.6) |
| [[C32 (line)]] | wt | 84.6 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.450× (z -12.9) |
| [[HEC-1-A (line)]] | alt | 109 | 2 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.84× (z +9.3) | [[Dinaciclib (drug)]] 0.05 µM 0.348× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.472× (z -9.9) |
| [[A-427 (line)]] | wt | 161 | 1 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.43× (z +8.5) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -12.1) |
| [[LoVo (line)]] | wt | 103 | 1 | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.69× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.481× (z -13.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.610× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 102 | 1 | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.22× (z +9.3) | [[Auranofin (drug)]] 5 µM 0.377× (z -12.2) |
| [[SW1417 (line)]] | alt | 130 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.533× (z -11.3) |
| [[A-172 (line)]] | wt | 75.4 | 0 | 3 | — | [[Auranofin (drug)]] 5 µM 0.359× (z -12.0) |
| [[HOP62 (line)]] | alt | 61.9 | 0 | 3 | — | [[Auranofin (drug)]] 5 µM 0.355× (z -10.8) |
| [[LS 180 (line)]] | wt | 83.2 | 0 | 3 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -9.7) |
| [[NCI-H1792 (line)]] | alt | 93.4 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.40× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.528× (z -10.2) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 147 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.165× (z -20.8) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -13.8) |
| [[RKO (line)]] | wt | 86.8 | 0 | 3 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -10.1) |
| [[SW480 (line)]] | alt | 129 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.05× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.462× (z -10.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 130 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.470× (z -13.5) |
| [[COLO 205 (line)]] | alt | 74.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -12.1) ⚠ cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 82.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.296× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.342× (z -9.3) |
| [[hTERT-HPNE (line)]] | wt | 45.2 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.60× (z +18.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[LOX-IMVI (line)]] | wt | 81.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -13.4) |
| [[NCI-H1573 (line)]] | alt | 97.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0790× (z -30.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 91.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.433× (z -12.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 94.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.166× (z -14.8) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 105 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.305× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.502× (z -8.9) |
| [[A498 (line)]] | wt | 106 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -13.8) |
| [[C-33 A (line)]] | alt | 117 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.328× (z -11.7) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 52.3 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0964× (z -8.6) ⚠ toxic |
| [[HT-29 (line)]] | alt | 71.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.362× (z -10.7) |
| [[KATO III (line)]] | alt | 90.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.377× (z -11.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 101 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.432× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 58.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.521× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 57.5 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.322× (z -9.8) |
| [[SK-MEL-2 (line)]] | alt | 75.8 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.146× (z -19.1) |
| [[SW 1271 (line)]] | alt | 97.9 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.251× (z -8.8) |
| [[AN3 CA (line)]] | alt | 101 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 64.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 69.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 75.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 71.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 58.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 88.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 60.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 87.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 86.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 89.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 85.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 85.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 93.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10322), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COA1]] | +0.74 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[DIS3L2]] | +0.74 | +0.65 / +0.75 | both halves | 7e-06 |  |
| [[SNRPE]] | +0.71 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[ORC5]] | +0.70 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[SNRPD1]] | +0.69 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[AGK]] | +0.68 | +0.61 / +0.65 | both halves | 7e-06 | pathway: Glycerophospholipid biosynthesis; STRING 921 |
| [[DLAT]] | +0.65 | +0.44 / +0.72 | both halves | 3e-05 |  |
| [[MCAT]] | +0.65 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[MRPS27]] | +0.65 | +0.51 / +0.71 | both halves | 1e-05 |  |
| [[VTA1]] | +0.64 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[CHCHD6]] | +0.64 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[XPO7]] | +0.63 | +0.65 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERO1B]] | -0.65 | -0.63 / -0.62 | both halves | 7e-06 |  |
| [[YPEL5]] | -0.60 | -0.48 / -0.56 | both halves | 2e-05 | STRING 466 |
| [[RSRP1]] | -0.58 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[ADCY10]] | -0.57 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[KLRD1]] | -0.56 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[UPP2]] | -0.56 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[ZNF846]] | -0.56 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[GNAS]] | -0.55 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[MAP1LC3B]] | -0.55 | -0.43 / -0.63 | both halves | 4e-05 |  |
| [[INTS6-AS1]] | -0.55 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[SNX31]] | -0.55 | -0.46 / -0.51 | both halves | 2e-05 |  |
| [[SMIM14]] | -0.55 | -0.46 / -0.58 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises LCLAT1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[WDR35]] | B | WDR35 activity strengthens LCLAT1's drug response | lines that do not express WDR35 (5) vs lines expressing it (45) | the lines without WDR35 respond 0.90× as strongly (z diff +0.47); rises at some drug-doses, falls at others (71% from rises): TAK-901 5 µM: 1.63x vs 2.65x (z diff +2.5); PH-797804 5 µM: 1.25x vs 1.88x (z diff +2.4); Dinaciclib 0.05 µM: 0.87x vs 0.66x (z diff +1.9) | 0.081 | ⚠ within organs, on part of the lines; also absent: AGK, DUSP19, ENTPD1-AS1; maybe low, not absent; both ways; rises at some drug-doses, falls at others; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.616). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-17.6, -42.4); signed map (-9.7, -48.5). **Vector** length 101, 27.6% of its response variance represented; |z| ≥ 3 in 922 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +9.6 | +9.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +7.1 | +6.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.4 | +6.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +5.1 | +4.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.4 | +1.9 |
|  | [[EX229 (drug)]] 5 µM |  | +3.3 | +2.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.0 | +1.8 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.6 | +1.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.9 | -9.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.5 | -5.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.3 | -11.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.2 | -6.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.8 | -6.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.3 | -3.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.2 | +0.1 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -2.2 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | lysocardiolipin acyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.1 — chr2:30,447,226-30,644,225 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ37965, ALCAT1, AGPAT8, LPLAT6; previously LYCAT |
| Gene groups (HGNC) | 1-acylglycerol-3-phosphate O-acyltransferases; Lysophospholipid acyltransferases |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Reactome | 5 pathways, smallest: Acyl chain remodeling of CL; Synthesis of PA; Glycerophospholipid biosynthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UWP7](https://www.uniprot.org/uniprotkb/Q6UWP7) (Lysocardiolipin acyltransferase 1):

> Exhibits acyl-CoA:lysocardiolipin acyltransferase (ALCAT) activity; catalyzes the reacylation of lyso-cardiolipin to cardiolipin (CL), a key step in CL remodeling (By similarity). Recognizes both monolysocardiolipin and dilysocardiolipin as substrates with a preference for linoleoyl-CoA and oleoyl-CoA as acyl donors (By similarity). Also exhibits 1-acyl-sn-glycerol-3-phosphate acyltransferase activity (AGPAT) activity; converts 1-acyl-sn-glycerol-3- phosphate (lysophosphatidic acid or LPA) into …

**Summary**, from NCBI Gene [253558](https://www.ncbi.nlm.nih.gov/gene/253558):

> Enables 1-acylglycerol-3-phosphate O-acyltransferase activity. Predicted to be involved in phosphatidylinositol acyl-chain remodeling. Located in endoplasmic reticulum. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26756](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26756) · Entrez [253558](https://www.ncbi.nlm.nih.gov/gene/253558) · UniProt [Q6UWP7](https://www.uniprot.org/uniprotkb/Q6UWP7) · Ensembl [ENSG00000172954](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172954)

## Data

Gene col 10322: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10322); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10322, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10322]; `tensor/DDL_lfc|DDL_z.npy` [10322]; `embed/gene_vectors.npy` [10322]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10322 or target_col == 10322). Every well: [[LCLAT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LCLAT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
