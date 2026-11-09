---
symbol: "CEMIP2"
type: "gene"
col: 5641
ensembl_id: "ENSG00000135048"
name: "cell migration inducing hyaluronidase 2"
location: "9q21.13"
module: 38
arm: "+"
pooled_cpm: 154.53
n_lines_expressing: 46
n_dd_up: 17
n_dd_down: 7
n_dd_up_clean: 14
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 9
direction_downstream: 5
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# CEMIP2

*cell migration inducing hyaluronidase 2* — 9q21.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.27× (z +19.4, q 0e+00, up in 36 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.648× (z -7.3, q 2e-10, down in 29 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 0.797× (z -3.8, q 0.015, down in 21 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (SW480 0.209×, BT-474 0.126×, LS 180 0.247×, COLO 205 0.236×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (SW480 0.198×, LS 180 0.181×, BT-474 0.134×, KATO III 0.269×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SW480 0.283×, LS 180 0.267×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (HepG2/C3A 0.514×); [[AZD-7648 (drug)]] 5 µM in 1 line (CHP-212 0.0594×); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM in 1 line (SK-MEL-2 0.382×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INTS6]] (+0.58, fdr 1e-05), [[SLC12A2]] (+0.56, fdr 1e-05), [[STPG4]] (+0.55, fdr 3e-05); moves opposite to [[CNEP1R1]] (-0.58, fdr 2e-05), [[PSMD9]] (-0.54, fdr 3e-05), [[STX2]] (-0.49, fdr 2e-04).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[MROH3P]] → it (grade B ⚠); 5 go from it, the strongest it → [[THRB]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5641.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.27×** | +19.4 | 0e+00 | 36/45 (AsPC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.00×** | +16.4 | 0e+00 | 35/44 (AsPC-1, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +7.7 | 3e-12 | 28/44 (LOX-IMVI, HS-578T, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.56×** | +7.4 | 2e-11 | 33/44 (AsPC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +6.9 | 4e-10 | 28/46 (LOX-IMVI, HOP62, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.47×** | +6.1 | 8e-08 | 27/44 (A498, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.02×** | +6.1 | 8e-08 | 32/45 (AsPC-1, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.94×** | +5.8 | 5e-07 | 29/44 (SW48, BT-474, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.78×** | +5.0 | 3e-05 | 27/42 (PANC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.32×** | +4.3 | 8e-04 | 24/44 (LoVo, SW48, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.20×** | +4.3 | 9e-04 | 21/44 (NCI-H460, BT-474, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.27×** | +4.0 | 0.004 | 25/44 (AsPC-1, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.27×** | +3.7 | 0.008 | 20/44 (SNU-423, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.23×** | +3.5 | 0.021 | 21/44 (A-172, PANC-1, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.45×** | +3.2 | 0.046 | 17/44 (J82, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.31×** | +3.2 | 0.051 | 12/45 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 1.20× | +3.0 | 0.092 | 19/44 (HOP62, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5641.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (SW480 0.209×, BT-474 0.126×, LS 180 0.247×, COLO 205 0.236×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (SW480 0.198×, LS 180 0.181×, BT-474 0.134×, KATO III 0.269×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SW480 0.283×, LS 180 0.267×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (HepG2/C3A 0.514×); [[AZD-7648 (drug)]] 5 µM in 1 line (CHP-212 0.0594×); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM in 1 line (SK-MEL-2 0.382×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.648×** | -7.3 | 2e-10 | 29/45 (SW480, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.642×** | -6.9 | 2e-09 | 25/41 (SW480, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.670×** | -6.5 | 2e-08 | 23/38 (SW480, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.720×** | -5.5 | 5e-06 | 28/44 (KATO III, SW 1088, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.797×** | -3.8 | 0.015 | 21/44 (J82, H4, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.860× | -3.6 | 0.029 | 17/44 (Hs 766T, C32, …) | top dose only |  |
| [[Neratinib (drug)]] 5 µM |  | **0.817×** | -3.4 | 0.055 | 18/44 (SW48, SW 1088, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **0.826×** | -3.2 | 0.086 | 18/44 (A-172, C32, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5641. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 91.0 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.44× (z +25.3) | — |
| [[HepG2_C3A (line)]] | wt | 460 | 0 | 7 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.272× (z -13.5) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.514× (z -10.2) |
| [[SW480 (line)]] | alt | 439 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.209× (z -18.4) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 60.0 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.48× (z +21.2) | — |
| [[COLO 205 (line)]] | alt | 381 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -14.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 237 | 2 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +12.4) | [[Dinaciclib (drug)]] 0.5 µM 0.342× (z -12.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 80.2 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.52× (z +20.5) | — |
| [[LS 180 (line)]] | wt | 372 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -17.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 111 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.45× (z +25.1) | — |
| [[BT-474 (line)]] | alt | 224 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.126× (z -17.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 300 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.272× (z -12.2) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 75.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.44× (z +19.9) | — |
| [[KATO III (line)]] | alt | 438 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.269× (z -13.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 203 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.232× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.382× (z -9.0) |
| [[SW1417 (line)]] | alt | 217 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.277× (z -12.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 55.3 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.98× (z +15.9) | — |
| [[C32 (line)]] | wt | 271 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.359× (z -9.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 147 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.399× (z -9.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 69.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +14.0) | — |
| [[J82 (line)]] | alt | 189 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +16.2) | [[Dinaciclib (drug)]] 0.5 µM 0.407× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 72.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.85× (z +17.2) | — |
| [[NCI-H460 (line)]] | wt | 116 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.85× (z +15.4) | — |
| [[SNU-423 (line)]] | alt | 146 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +10.9) | [[Dinaciclib (drug)]] 0.05 µM 0.402× (z -8.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 158 | 2 | 0 | [[Cobimetinib (drug)]] 5 µM 3.00× (z +9.7) | — |
| [[CFPAC-1 (line)]] | alt | 139 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +13.2) | — |
| [[CHP-212 (line)]] | wt | 247 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[AZD-7648 (drug)]] 5 µM 0.0594× (z -9.6) |
| [[H4 (line)]] | wt | 98.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +10.6) | — |
| [[NCI-H1573 (line)]] | alt | 70.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +15.3) | — |
| [[NCI-H2347 (line)]] | alt | 97.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +12.6) | — |
| [[Panc 03.27 (line)]] | alt | 144 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.53× (z +15.0) | — |
| [[PANC-1 (line)]] | alt | 40.3 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +13.0) | — |
| [[SNU-1 (line)]] | wt | 63.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.29× (z +12.1) | — |
| [[AN3 CA (line)]] | alt | 74.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +8.8) | — |
| [[HCT15 (line)]] | alt | 185 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +10.9) | — |
| [[Hs 766T (line)]] | wt | 102 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.43× (z +15.4) | — |
| [[NCI-H2030 (line)]] | alt | 126 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +9.3) | — |
| [[NCI-H23 (line)]] | alt | 40.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +9.5) | — |
| [[RKO (line)]] | wt | 62.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.81× (z +15.5) | — |
| [[RPMI-7951 (line)]] | alt | 81.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.43× (z +12.6) | — |
| [[SW 1088 (line)]] | alt | 107 | 0 | 1 | — | [[Meloxicam (drug)]] 0.5 µM 0.0618× (z -9.0) |
| [[A-427 (line)]] | wt | 28.1 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 30.8 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 29.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.7 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 76.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 206 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 167 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5641), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INTS6]] | +0.58 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[SLC12A2]] | +0.56 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[STPG4]] | +0.55 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[MPDU1]] | +0.55 | +0.54 / +0.37 | both halves | 8e-05 |  |
| [[BCAR3-AS1]] | +0.54 | +0.55 / +0.41 | both halves | 4e-05 |  |
| [[THUMPD3-AS1]] | +0.54 | +0.48 / +0.40 | both halves | 5e-05 |  |
| [[FAM222A]] | +0.54 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[PCSK5]] | +0.53 | +0.43 / +0.63 | both halves | 3e-05 |  |
| [[TLE4]] | +0.53 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[EPHA4]] | +0.52 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[TRIM72]] | +0.52 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[ZNF703]] | +0.51 | +0.52 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNEP1R1]] | -0.58 | -0.58 / -0.46 | both halves | 2e-05 |  |
| [[PSMD9]] | -0.54 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[STX2]] | -0.49 | -0.48 / -0.30 | both halves | 2e-04 |  |
| [[STX7]] | -0.48 | -0.46 / -0.31 | both halves | 2e-04 |  |
| [[CASC3]] | -0.48 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[LINC01518]] | -0.47 | -0.42 / -0.36 | both halves | 9e-05 |  |
| [[DENND6A]] | -0.47 | -0.48 / -0.33 | both halves | 1e-04 |  |
| [[COMMD2]] | -0.47 | -0.45 / -0.27 | both halves | 3e-04 |  |
| [[ACTR10]] | -0.47 | -0.50 / -0.36 | both halves | 1e-04 |  |
| [[SLC15A4]] | -0.46 | -0.55 / -0.35 | both halves | 1e-04 |  |
| [[TBC1D13]] | -0.46 | -0.41 / -0.35 | both halves | 1e-04 |  |
| [[RNF216P1]] | -0.46 | -0.47 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MROH3P]] | B | MROH3P activity raises CEMIP2's level | lines that do not express MROH3P (29) vs lines expressing it (21) | 2.19× lower at baseline in the lines without MROH3P | 0.019 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[THRB]] | B | THRB activity raises CEMIP2's level | lines that do not express THRB (21) vs lines expressing it (29) | 1.90× lower at baseline in the lines without THRB | 0.025 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SIDT1, P2RY2 |
| [[GRHL2]] | B | GRHL2 activity raises CEMIP2's level | lines that do not express GRHL2 (34) vs lines expressing it (16) | 2.08× lower at baseline in the lines without GRHL2 | 0.040 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4 |
| [[ZNF341-AS1]] | B | ZNF341-AS1 activity raises CEMIP2's level | lines that do not express ZNF341-AS1 (7) vs lines expressing it (43) | 2.48× lower at baseline in the lines without ZNF341-AS1 | 0.041 | ⚠ within organs, on part of the lines; also absent: ABTB2, CD59, CLCF1; maybe low, not absent |
| [[KITLG]] | B | KITLG activity raises CEMIP2's level | lines that do not express KITLG (10) vs lines expressing it (40) | 2.41× lower at baseline in the lines without KITLG | 0.049 | ⚠ within organs, on part of the lines; also absent: ETS2, CDA, LMO7; maybe low, not absent |
| [[TLE4]] | B | TLE4 activity raises CEMIP2's level | lines that do not express TLE4 (10) vs lines expressing it (40) | 2.58× lower at baseline in the lines without TLE4 | 0.049 | ⚠ within organs, on part of the lines; also absent: LMO7, CA13, KITLG |
| [[C21orf91-OT1]] | B | C21orf91-OT1 activity raises CEMIP2's level | lines that do not express C21orf91-OT1 (5) vs lines expressing it (45) | 2.61× lower at baseline in the lines without C21orf91-OT1 | 0.053 | ⚠ within organs, on part of the lines; co-absent genes; also absent: USP25, GSDMD, RALGPS2 |
| [[CDHR2]] | B | CDHR2 activity raises CEMIP2's level | lines that do not express CDHR2 (30) vs lines expressing it (20) | 1.72× lower at baseline in the lines without CDHR2 | 0.062 | ⚠ within organs, on part of the lines; also absent: VIL1, NPSR1-AS1, EPS8L3; maybe low, not absent |
| [[PLSCR2]] | C | PLSCR2 activity raises CEMIP2's level | lines that do not express PLSCR2 (6) vs lines expressing it (44) | 2.58× lower at baseline in the lines without PLSCR2 | 0.073 | ⚠ within organs, on part of the lines; also absent: TRIB1, SLC2A1, CEMIP2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[THRB]] | C | CEMIP2 activity raises THRB's level | lines that do not express CEMIP2 (4) vs lines expressing it (46) | 5.22× lower at baseline in the lines without CEMIP2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: KIFC3, SMARCA2, PLSCR2; maybe low, not absent; its own permutation p |
| [[PLSCR2]] | C | CEMIP2 activity raises PLSCR2's level | lines that do not express CEMIP2 (4) vs lines expressing it (46) | 3.73× lower at baseline in the lines without CEMIP2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: KIFC3, SMARCA2, PLSCR2; maybe low, not absent; co-absent with the target; its own permutation p |
| [[KLHL15]] | C | CEMIP2 activity lowers KLHL15's level | lines that do not express CEMIP2 (4) vs lines expressing it (46) | 2.17× higher at baseline in the lines without CEMIP2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: KIFC3, SMARCA2, PLSCR2; maybe low, not absent; its own permutation p |
| [[LNCRNA-IUR]] | C | CEMIP2 activity raises LNCRNA-IUR's level | lines that do not express CEMIP2 (4) vs lines expressing it (46) | 1.97× lower at baseline in the lines without CEMIP2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: KIFC3, SMARCA2, PLSCR2; maybe low, not absent; its own permutation p |
| [[MCUR1]] | C | CEMIP2 activity lowers MCUR1's level | lines that do not express CEMIP2 (4) vs lines expressing it (46) | 1.59× higher at baseline in the lines without CEMIP2 | 0.094 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: KIFC3, SMARCA2, PLSCR2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.399). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.1, -25.5); signed map (55.3, 12.6). **Vector** length 130, 41.0% of its response variance represented; |z| ≥ 3 in 1,210 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.9 | +19.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +6.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +7.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.9 | +16.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +1.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.6 | +1.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.6 | +4.3 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.5 | -0.4 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.6 | -1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.4 | -1.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | +0.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.2 | -3.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.9 | +0.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.6 | -3.8 |
|  | [[Neratinib (drug)]] 5 µM |  | -3.1 | -3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.1 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | cell migration inducing hyaluronidase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.13 — chr9:71,683,366-71,816,690 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously TMEM2 |
| Gene groups (HGNC) | Hyaluronidases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UHN6](https://www.uniprot.org/uniprotkb/Q9UHN6) (Cell surface hyaluronidase CEMIP2):

> Cell surface hyaluronidase that mediates the initial cleavage of extracellular high-molecular-weight hyaluronan into intermediate-size hyaluronan of approximately 10-5 kDa fragments. Very specific to hyaluronan; not able to cleave chondroitin sulfate or dermatan sulfate. Has an essential function in systemic hyaluronan catabolism and turnover and regulates cell adhesion and migration via hyaluronan degradation at focal adhesion sites (By similarity). Acts as a regulator of angiogenesis and …

**Summary**, from NCBI Gene [23670](https://www.ncbi.nlm.nih.gov/gene/23670):

> This gene encodes a type II transmembrane protein that belongs to the interferon-induced transmembrane (IFITM) protein superfamily. The encoded protein functions as a cell surface hyaluronidase that cleaves extracellular high molecular weight hyaluronan into intermediate size fragments before internalization and degradation in the lysosome. It also has an interferon-mediated antiviral function in humans through activation of the JAK STAT signaling pathway. The activation of this gene by …

**Accessions** — [HGNC:11869](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11869) · Entrez [23670](https://www.ncbi.nlm.nih.gov/gene/23670) · UniProt [Q9UHN6](https://www.uniprot.org/uniprotkb/Q9UHN6) · Ensembl [ENSG00000135048](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135048)

## Data

Gene col 5641: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5641); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5641, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5641]; `tensor/DDL_lfc|DDL_z.npy` [5641]; `embed/gene_vectors.npy` [5641]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5641 or target_col == 5641). Every well: [[CEMIP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CEMIP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
