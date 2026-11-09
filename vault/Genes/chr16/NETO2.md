---
symbol: "NETO2"
type: "gene"
col: 10073
ensembl_id: "ENSG00000171208"
name: "neuropilin and tolloid like 2"
location: "16q12.1"
module: 18
arm: "+"
pooled_cpm: 53.54
n_lines_expressing: 39
n_dd_up: 36
n_dd_down: 10
n_dd_up_clean: 18
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# NETO2

*neuropilin and tolloid like 2* — 16q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (18 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.56× (z +26.0, q 0e+00, up in 35 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.566× (z -5.8, q 3e-06, down in 20 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPR63]] (+0.59, fdr 1e-05), [[STK26]] (+0.58, fdr 4e-05), [[SNX5]] (+0.57, fdr 4e-05); moves opposite to [[IK]] (-0.58, fdr 1e-04), [[UBXN1]] (-0.54, fdr 2e-04), [[ZER1]] (-0.54, fdr 3e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[GPR63]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 21 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10073.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.56×** | +26.0 | 0e+00 | 35/37 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.83×** | +16.7 | 0e+00 | 22/37 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.38×** | +16.3 | 0e+00 | 33/36 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.92×** | +12.7 | 7e-35 | 33/36 (J82, SW480, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.86×** | +11.3 | 1e-27 | 31/37 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.82×** | +11.3 | 2e-27 | 25/36 (NCI-H460, HOP62, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.50×** | +11.3 | 2e-27 | 31/37 (NCI-H2030, SW1417, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.70×** | +9.9 | 2e-21 | 23/37 (NCI-H1573, A549, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **1.60×** | +8.9 | 5e-17 | 26/36 (HOP62, LoVo, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.57×** | +8.7 | 1e-16 | 23/37 (LoVo, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.56×** | +8.7 | 1e-16 | 25/37 (NCI-H2030, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.52×** | +8.1 | 2e-14 | 25/37 (J82, BT-474, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.52×** | +8.1 | 2e-14 | 21/37 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.52×** | +7.8 | 2e-13 | 21/33 (SNU-423, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **1.97×** | +6.9 | 2e-10 | 24/37 (NCI-H460, A498, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.89×** | +6.5 | 3e-09 | 23/36 (NCI-H460, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +6.1 | 2e-08 | 19/37 (HOP62, J82, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.78×** | +5.9 | 1e-07 | 18/36 (NCI-H460, J82, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.30×** | +5.1 | 6e-06 | 19/36 (HOP62, SNU-423, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.35×** | +4.2 | 6e-04 | 15/37 (NCI-H460, J82, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.47×** | +3.9 | 0.002 | 18/36 (NCI-H460, A498, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.46×** | +3.9 | 0.002 | 13/36 (NCI-H460, A498, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **1.23×** | +3.5 | 0.008 | 12/37 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10073.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.566×** | -5.8 | 3e-06 | 20/38 (RKO, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.733×** | -5.6 | 5e-06 | 21/37 (SW480, A-427, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.762×** | -5.1 | 6e-05 | 16/36 (A549, J82, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.639×** | -4.6 | 7e-04 | 15/38 (A-427, A549, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.797×** | -4.4 | 0.001 | 16/36 (SK-MEL-2, LoVo, …) | rises with dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.806×** | -4.2 | 0.002 | 16/37 (A498, BT-474, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.811×** | -3.9 | 0.006 | 12/36 (SW480, A549, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.828×** | -3.9 | 0.006 | 12/37 (A-427, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.824×** | -3.8 | 0.009 | 12/38 (SW480, SW 900, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.818×** | -3.8 | 0.009 | 18/36 (NCI-H23, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.860× | -3.8 | 0.009 | 9/37 (SW480, HepG2/C3A, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.843× | -3.6 | 0.016 | 10/37 (SW480, SW 900, …) | all doses, flat | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | 0.834× | -3.5 | 0.017 | 13/36 (NCI-H1573, CFPAC-1, …) | two highest doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | 0.889× | -3.3 | 0.045 | 12/37 (A-427, HOP62, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.857× | -3.0 | 0.096 | 13/35 (PANC-1, A498, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.61 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10073. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 90.4 | 7 (5 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +15.6) | [[Dinaciclib (drug)]] 0.05 µM 0.382× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 35.8 | 7 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.15× (z +16.9) | — |
| [[J82 (line)]] | alt | 84.0 | 6 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +15.1) | — |
| [[NCI-H460 (line)]] | wt | 85.1 | 6 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.38× (z +21.9) | — |
| [[SW480 (line)]] | alt | 81.0 | 5 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +14.0) | — |
| [[A-427 (line)]] | wt | 117 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.435× (z -14.7) |
| [[CFPAC-1 (line)]] | alt | 27.8 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.24× (z +18.5) | — |
| [[NCI-H1792 (line)]] | alt | 67.8 | 4 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.22× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.27× (z +9.8) | — |
| [[PANC-1 (line)]] | alt | 76.6 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.458× (z -11.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.326× (z -8.6) |
| [[SNU-423 (line)]] | alt | 33.0 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.79× (z +14.2) | — |
| [[C-33 A (line)]] | alt | 132 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0602× (z -28.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.403× (z -14.2) |
| [[SW1417 (line)]] | alt | 56.3 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +13.1) | — |
| [[A498 (line)]] | wt | 69.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.09× (z +17.0) | — |
| [[A549 (line)]] | wt | 96.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +11.1) | — |
| [[C32 (line)]] | wt | 33.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +10.7) | — |
| [[HS-578T (line)]] | alt | 26.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +10.4) | — |
| [[hTERT-HPNE (line)]] | wt | 28.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.32× (z +10.1) | — |
| [[NCI-H1573 (line)]] | alt | 47.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +10.6) | — |
| [[NCI-H23 (line)]] | alt | 50.4 | 1 (1 ⚠) | 1 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.76× (z +8.7) ⚠ toxic | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -10.4) |
| [[NCI-H2347 (line)]] | alt | 35.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +11.8) | — |
| [[Panc 03.27 (line)]] | alt | 23.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.63× (z +11.2) | — |
| [[RKO (line)]] | wt | 98.0 | 0 | 2 | — | [[TAK-901 (drug)]] 5 µM 0.113× (z -11.7) |
| [[BT-474 (line)]] | alt | 36.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.69× (z +11.4) | — |
| [[H4 (line)]] | wt | 49.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.48× (z +9.2) | — |
| [[HCT15 (line)]] | alt | 53.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.62× (z +11.0) | — |
| [[NCI-H2030 (line)]] | alt | 66.3 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.09× (z +9.5) | — |
| [[SHP-77 (line)]] | alt | 106 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.52× (z +9.1) ⚠ toxic | — |
| [[A-172 (line)]] | wt | 12.2 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 9.84 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.98 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 69.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.9 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.11 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 12.3 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.61 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 6.22 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 73.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.62 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 77.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 74.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 94.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 70.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.06 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10073), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPR63]] | +0.59 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[STK26]] | +0.58 | +0.59 / +0.42 | both halves | 4e-05 |  |
| [[SNX5]] | +0.57 | +0.60 / +0.41 | both halves | 4e-05 |  |
| [[SLC25A15]] | +0.57 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[ZNF124]] | +0.56 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[KCTD12]] | +0.56 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[NHSL1]] | +0.56 | +0.41 / +0.46 | both halves | 4e-05 |  |
| [[SLC35F2]] | +0.55 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[GALNT14]] | +0.55 | +0.36 / +0.59 | both halves | 1e-04 |  |
| [[TBC1D4]] | +0.55 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[PRPS2]] | +0.54 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[NCR3LG1]] | +0.54 | +0.54 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IK]] | -0.58 | -0.35 / -0.50 | both halves | 1e-04 |  |
| [[UBXN1]] | -0.54 | -0.30 / -0.48 | both halves | 2e-04 |  |
| [[ZER1]] | -0.54 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[CALCOCO1]] | -0.54 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[DCTN3]] | -0.52 | -0.38 / -0.39 | both halves | 6e-05 |  |
| [[BAD]] | -0.52 | -0.55 / -0.34 | both halves | 1e-04 |  |
| [[ZSCAN16]] | -0.52 | -0.23 / -0.41 | both halves | 5e-04 |  |
| [[ACOT8]] | -0.51 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[SYF2]] | -0.50 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[CIR1]] | -0.50 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[UBXN6]] | -0.49 | -0.41 / -0.60 | both halves | 4e-05 |  |
| [[DAPK3]] | -0.49 | -0.48 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NETO2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TOP1]] | B | TOP1 activity lowers NETO2's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 6.7% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[GPR63]] | C | GPR63 activity raises NETO2's level | lines that do not express GPR63 (10) vs lines expressing it (40) | 4.00× lower at baseline in the lines without GPR63 | 0.037 | ⚠ within organs, on part of the lines; also absent: ZNF618, BEX3, OLFM2; co-absent with the target |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPR63]] | C | NETO2 activity raises GPR63's level | lines that do not express NETO2 (11) vs lines expressing it (39) | 2.34× lower at baseline in the lines without NETO2 | 0.079 | ⚠ within organs, on part of the lines; also absent: BEND6, ZDBF2, CPQ; co-absent with the target |

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.458). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-7.1, 6.9); signed map (22.3, -35.7). **Vector** length 115, 31.5% of its response variance represented; |z| ≥ 3 in 1,137 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.0 | +11.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +8.0 | +12.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.4 | +11.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.2 | +16.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.8 | +8.7 |
|  | [[EX229 (drug)]] 5 µM |  | +3.8 | +5.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.6 | +6.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.4 | +6.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.9 | +3.9 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -5.0 | -5.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | +1.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.5 | +0.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.4 | -3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.9 | -3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.5 | -3.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.4 | -3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.3 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | neuropilin and tolloid like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q12.1 — chr16:47,077,703-47,143,945 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10430, NEOT2 |
| Gene groups (HGNC) | Neuropilin and tolloid like family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NC67](https://www.uniprot.org/uniprotkb/Q8NC67) (Neuropilin and tolloid-like protein 2):

> Accessory subunit of neuronal kainate-sensitive glutamate receptors, GRIK2 and GRIK3. Increases kainate-receptor channel activity, slowing the decay kinetics of the receptors, without affecting their expression at the cell surface, and increasing the open probability of the receptor channels. Modulates the agonist sensitivity of kainate receptors. Slows the decay of kainate receptor-mediated excitatory postsynaptic currents (EPSCs), thus directly influencing synaptic transmission (By …

**Summary**, from NCBI Gene [81831](https://www.ncbi.nlm.nih.gov/gene/81831):

> This gene encodes a predicted transmembrane protein containing two extracellular CUB domains followed by a low-density lipoprotein class A (LDLa) domain. A similar gene in rats encodes a protein that modulates glutamate signaling in the brain by regulating kainate receptor function. Expression of this gene may be a biomarker for proliferating infantile hemangiomas. A pseudogene of this gene is located on the long arm of chromosome 8. Alternatively spliced transcript variants encoding multiple …

**Accessions** — [HGNC:14644](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14644) · Entrez [81831](https://www.ncbi.nlm.nih.gov/gene/81831) · UniProt [Q8NC67](https://www.uniprot.org/uniprotkb/Q8NC67) · Ensembl [ENSG00000171208](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171208)

## Data

Gene col 10073: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10073); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10073, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10073]; `tensor/DDL_lfc|DDL_z.npy` [10073]; `embed/gene_vectors.npy` [10073]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10073 or target_col == 10073). Every well: [[NETO2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NETO2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
