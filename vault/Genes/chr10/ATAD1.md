---
symbol: "ATAD1"
type: "gene"
col: 6132
ensembl_id: "ENSG00000138138"
name: "ATPase family AAA domain containing 1"
location: "10q23.31"
module: 1
arm: "+"
pooled_cpm: 107.38
n_lines_expressing: 46
n_dd_up: 15
n_dd_down: 1
n_dd_up_clean: 7
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 15
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# ATAD1

*ATPase family AAA domain containing 1* — 10q23.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.16× (z +13.2, q 5e-37, up in 35 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Temsirolimus (drug)]] 0.5 µM: 0.830× (z -6.2, q 4e-07, down in 22 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (A549 0.518×, NCI-H460 0.470×, NCI-H2030 0.600×, SK-MEL-2 0.617×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 0.408×, NCI-H460 0.473×; ⚠ cell-cycle shift, explains ~0% of this change); [[Auranofin (drug)]] 5 µM in 1 line (NCI-H460 0.409×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBLCP1]] (+0.58, fdr 2e-05), [[AAGAB]] (+0.58, fdr 1e-05), [[PGGT1B]] (+0.54, fdr 3e-05); moves opposite to [[CKS2]] (-0.55, fdr 7e-05), [[TUBB3]] (-0.55, fdr 6e-05), [[CSRP2]] (-0.54, fdr 2e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 15 go from it, the strongest it → cells under [[Topotecan (hydrochloride) (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6132.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.16×** | +13.2 | 5e-37 | 35/45 (LoVo, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.38×** | +10.5 | 3e-23 | 35/44 (CFPAC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.34×** | +9.5 | 4e-19 | 27/44 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.72×** | +9.3 | 1e-18 | 31/44 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.22×** | +9.1 | 1e-17 | 22/44 (LoVo, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.32×** | +9.0 | 2e-17 | 27/44 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.34×** | +8.9 | 5e-17 | 29/42 (HOP62, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change | **1.31×** | +8.8 | 9e-17 | 27/44 (LoVo, LS 180, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.30×** | +8.7 | 2e-16 | 28/44 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.27×** | +7.5 | 4e-12 | 25/44 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.25×** | +7.3 | 1e-11 | 23/45 (COLO 205, HT-29, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.24×** | +6.9 | 2e-10 | 22/44 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.46×** | +6.5 | 3e-09 | 24/36 (HOP62, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.21×** | +6.1 | 4e-08 | 20/41 (SW48, J82, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.20× | +5.9 | 2e-07 | 19/44 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.14× | +4.4 | 3e-04 | 13/44 (HOP62, KATO III, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.25×** | +3.9 | 0.003 | 14/44 (HepG2/C3A, A-427, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.13× | +3.6 | 0.009 | 9/44 (NCI-H460, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.12× | +3.6 | 0.009 | 18/43 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses |  |
| [[Gallic acid (drug)]] 0.05 µM |  | 1.10× | +3.2 | 0.029 | 2/44 (BT-474, hTERT-HPNE) | inconsistent across doses |  |
| [[NVP-BHG712 (drug)]] 0.05 µM |  | 1.10× | +2.9 | 0.073 | 3/44 (PANC-1, HEC-1-A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6132.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (A549 0.518×, NCI-H460 0.470×, NCI-H2030 0.600×, SK-MEL-2 0.617×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 0.408×, NCI-H460 0.473×; ⚠ cell-cycle shift, explains ~0% of this change); [[Auranofin (drug)]] 5 µM in 1 line (NCI-H460 0.409×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.830×** | -6.2 | 4e-07 | 22/44 (SK-MEL-2, J82, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.892× | -5.3 | 3e-05 | 18/45 (A549, NCI-H460, …) | rises with dose |  |
| [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | 0.896× | -3.7 | 0.048 | 3/44 (NCI-H23, AN3 CA, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.859× | -3.6 | 0.048 | 14/44 (A498, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.914× | -3.1 | 0.20 | 6/46 (A-427, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6132. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 349 | 8 (4 ⚠) | 5 (4 ⚠) | [[Digitoxin (drug)]] 0.05 µM 2.62× (z +12.3) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.46× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.470× (z -13.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.409× (z -11.4) |
| [[LoVo (line)]] | wt | 133 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +12.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.37× (z +12.6) | — |
| [[LS 180 (line)]] | wt | 141 | 6 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.41× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 4.65× (z +10.9) | — |
| [[SW480 (line)]] | alt | 121 | 4 (1 ⚠) | 0 | [[PH-797804 (drug)]] 5 µM 3.03× (z +10.9) | — |
| [[CFPAC-1 (line)]] | alt | 82.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.17× (z +10.2) | — |
| [[HEC-1-A (line)]] | alt | 87.3 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 3.28× (z +9.2) | — |
| [[NCI-H1573 (line)]] | alt | 144 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.20× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change | — |
| [[NCI-H2030 (line)]] | alt | 137 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.92× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.600× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 132 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -12.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 103 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 2.93× (z +9.3) | — |
| [[A549 (line)]] | wt | 130 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.518× (z -14.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 123 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +10.5) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[COLO 205 (line)]] | alt | 60.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.94× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HOP62 (line)]] | alt | 82.2 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 3.31× (z +8.9) | — |
| [[HT-29 (line)]] | alt | 75.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.85× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[J82 (line)]] | alt | 53.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.12× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[KATO III (line)]] | alt | 76.1 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 1.92× (z +8.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 71.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.09× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 110 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.617× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 116 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.384× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[SW48 (line)]] | wt | 107 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.74× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[A-172 (line)]] | wt | 83.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 86.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 127 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 65.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 88.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.89 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 115 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.84 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 82.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 109 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 78.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 72.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 94.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 72.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 92.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 89.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 75.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 99.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.67 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 66.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 79.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.9 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 76.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 97.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6132), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBLCP1]] | +0.58 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[AAGAB]] | +0.58 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[PGGT1B]] | +0.54 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[RBM45]] | +0.53 | +0.47 / +0.38 | both halves | 7e-05 |  |
| [[TMEM128]] | +0.52 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[AGK]] | +0.52 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[DMAC2L]] | +0.51 | +0.38 / +0.46 | both halves | 7e-05 |  |
| [[TMEM209]] | +0.51 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[MRPL42]] | +0.51 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[SCRN3]] | +0.51 | +0.35 / +0.54 | both halves | 1e-04 |  |
| [[ABHD13]] | +0.51 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[DCAF17]] | +0.50 | +0.39 / +0.49 | both halves | 5e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CKS2]] | -0.55 | -0.38 / -0.54 | both halves | 7e-05 |  |
| [[TUBB3]] | -0.55 | -0.38 / -0.55 | both halves | 6e-05 |  |
| [[CSRP2]] | -0.54 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[BAIAP2]] | -0.51 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[GATA2]] | -0.50 | -0.29 / -0.54 | both halves | 3e-04 |  |
| [[PDXK]] | -0.50 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[DEDD2]] | -0.49 | -0.27 / -0.51 | both halves | 3e-04 |  |
| [[FAM53C]] | -0.48 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[POR]] | -0.48 | -0.29 / -0.53 | both halves | 3e-04 |  |
| [[TESK2]] | -0.48 | -0.36 / -0.47 | both halves | 9e-05 |  |
| [[TSEN34]] | -0.48 | -0.40 / -0.48 | both halves | 4e-05 |  |
| [[SNAI1]] | -0.48 | -0.25 / -0.47 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 0, C 15. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Topotecan (hydrochloride) (drug)]] 0.5 µM | C | ATAD1, [[PTEN]] activity raises the cells' numbers under Topotecan (hydrochloride) 0.5 µM (protects the cells) | lines that do not express ATAD1, PTEN (4) vs lines expressing them (44) | the lines without ATAD1, PTEN: 0.68× the cells of the other lines | 0.012 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: CFL1P1-1, ZC3HAV1L, OSR2; co-absent genes |
| cells under [[Ixazomib citrate (drug)]] 5 µM | C | ATAD1, [[PTEN]] activity raises the cells' numbers under Ixazomib citrate 5 µM (protects the cells) | lines that do not express ATAD1, PTEN (4) vs lines expressing them (44) | the lines without ATAD1, PTEN: 0.54× the cells of the other lines | 0.014 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: CFL1P1-1, ZC3HAV1L, OSR2; co-absent genes |
| cells under [[Elimusertib hydrochloride (drug)]] 5 µM | C | ATAD1, [[PTEN]] activity raises the cells' numbers under Elimusertib hydrochloride 5 µM (protects the cells) | lines that do not express ATAD1, PTEN (4) vs lines expressing them (44) | the lines without ATAD1, PTEN: 0.61× the cells of the other lines | 0.021 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: CFL1P1-1, ZC3HAV1L, OSR2; co-absent genes |
| cells under [[Daptomycin (drug)]] 0.5 µM | C | ATAD1, [[PTEN]] activity raises the cells' numbers under Daptomycin 0.5 µM (protects the cells) | lines that do not express ATAD1, PTEN (4) vs lines expressing them (44) | the lines without ATAD1, PTEN: 0.62× the cells of the other lines | 0.021 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: CFL1P1-1, ZC3HAV1L, OSR2; cell counts less trustworthy; co-absent genes |
| cells under [[Cabozantinib (S-malate) (drug)]] 5 µM | C | ATAD1, [[PTEN]] activity raises the cells' numbers under Cabozantinib (S-malate) 5 µM (protects the cells) | lines that do not express ATAD1, PTEN (4) vs lines expressing them (44) | the lines without ATAD1, PTEN: 0.76× the cells of the other lines | 0.033 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: CFL1P1-1, ZC3HAV1L, OSR2; co-absent genes |
| cells under [[Carbamazepine (drug)]] 0.5 µM | C | ATAD1, [[PTEN]] activity raises the cells' numbers under Carbamazepine 0.5 µM (protects the cells) | lines that do not express ATAD1, PTEN (4) vs lines expressing them (44) | the lines without ATAD1, PTEN: 0.72× the cells of the other lines | 0.041 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: CFL1P1-1, ZC3HAV1L, OSR2; co-absent genes |
| cells under [[Vemurafenib (drug)]] 5 µM | C | ATAD1, [[PTEN]] activity lowers the cells' numbers under Vemurafenib 5 µM (makes them more sensitive) | lines that do not express ATAD1, PTEN (4) vs lines expressing them (44) | the lines without ATAD1, PTEN: 1.25× the cells of the other lines | 0.045 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: CFL1P1-1, ZC3HAV1L, OSR2; co-absent genes |
| cells under [[Peretinoin (drug)]] 5 µM | C | ATAD1, [[PTEN]] activity raises the cells' numbers under Peretinoin 5 µM (protects the cells) | lines that do not express ATAD1, PTEN (4) vs lines expressing them (44) | the lines without ATAD1, PTEN: 0.76× the cells of the other lines | 0.055 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: CFL1P1-1, ZC3HAV1L, OSR2; co-absent genes |
| cells under [[NG25 (drug)]] 5 µM | C | ATAD1, [[PTEN]] activity raises the cells' numbers under NG25 5 µM (protects the cells) | lines that do not express ATAD1, PTEN (4) vs lines expressing them (44) | the lines without ATAD1, PTEN: 0.56× the cells of the other lines | 0.059 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: CFL1P1-1, ZC3HAV1L, OSR2; co-absent genes |
| cells under [[Peretinoin (drug)]] 0.5 µM | C | ATAD1, [[PTEN]] activity raises the cells' numbers under Peretinoin 0.5 µM (protects the cells) | lines that do not express ATAD1, PTEN (4) vs lines expressing them (44) | the lines without ATAD1, PTEN: 0.62× the cells of the other lines | 0.076 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: CFL1P1-1, ZC3HAV1L, OSR2; co-absent genes |
| cells under [[vincristine (drug)]] 5 µM | C | ATAD1, [[PTEN]] activity raises the cells' numbers under vincristine 5 µM (protects the cells) | lines that do not express ATAD1, PTEN (4) vs lines expressing them (44) | the lines without ATAD1, PTEN: 0.55× the cells of the other lines | 0.092 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: CFL1P1-1, ZC3HAV1L, OSR2; co-absent genes |
| cells under [[Citalopram (hydrobromide) (drug)]] 0.05 µM | C | ATAD1, [[PTEN]] activity lowers the cells' numbers under Citalopram (hydrobromide) 0.05 µM (makes them more sensitive) | lines that do not express ATAD1, PTEN (4) vs lines expressing them (44) | the lines without ATAD1, PTEN: 1.32× the cells of the other lines | 0.093 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: CFL1P1-1, ZC3HAV1L, OSR2; co-absent genes |

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.438). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-26.4, -12.9); signed map (-20.4, -53.9). **Vector** length 83.3, 17.3% of its response variance represented; |z| ≥ 3 in 971 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.3 | +8.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +5.9 | +7.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +5.1 | +6.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.5 | +10.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.0 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +5.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | +9.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +2.4 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +1.8 | +0.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.8 | +3.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.4 | -2.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.6 | -5.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.9 | -1.6 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.8 | -0.5 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.6 | -0.8 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -1.5 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | ATPase family AAA domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q23.31 — chr10:87,751,512-87,841,361 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14600, Msp1 |
| Gene groups (HGNC) | AAA ATPases |
| Reactome | 2 pathways, smallest: Class I peroxisomal membrane protein import; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NBU5](https://www.uniprot.org/uniprotkb/Q8NBU5) (Outer mitochondrial transmembrane helix translocase):

> Outer mitochondrial translocase required to remove mislocalized tail-anchored transmembrane proteins on mitochondria. Specifically recognizes and binds tail-anchored transmembrane proteins: acts as a dislocase that mediates the ATP-dependent extraction of mistargeted tail-anchored transmembrane proteins from the mitochondrion outer membrane (By similarity). Also plays a critical role in regulating the surface expression of AMPA receptors (AMPAR), thereby regulating synaptic plasticity and …

**Summary**, from NCBI Gene [84896](https://www.ncbi.nlm.nih.gov/gene/84896):

> Predicted to enable ATP hydrolysis activity. Involved in extraction of mislocalized protein from mitochondrial outer membrane. Located in mitochondrial outer membrane and peroxisomal membrane. Implicated in hyperekplexia 4. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25903](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25903) · Entrez [84896](https://www.ncbi.nlm.nih.gov/gene/84896) · UniProt [Q8NBU5](https://www.uniprot.org/uniprotkb/Q8NBU5) · Ensembl [ENSG00000138138](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138138)

## Data

Gene col 6132: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6132); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6132, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6132]; `tensor/DDL_lfc|DDL_z.npy` [6132]; `embed/gene_vectors.npy` [6132]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6132 or target_col == 6132). Every well: [[ATAD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATAD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
