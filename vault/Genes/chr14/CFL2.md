---
symbol: "CFL2"
type: "gene"
col: 9116
ensembl_id: "ENSG00000165410"
name: "cofilin 2"
location: "14q13.1"
module: 28
arm: "+"
pooled_cpm: 20.92
n_lines_expressing: 45
n_dd_up: 33
n_dd_down: 8
n_dd_up_clean: 23
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 6
direction_downstream: 28
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# CFL2

*cofilin 2* — 14q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.09× (z +17.9, q 0e+00, up in 33 of 42 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 2.40× (z +14.4, q 4e-45, up in 35 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Ipatasertib (drug)]] 0.5 µM: 0.669× (z -4.9, q 2e-04, down in 18 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NCOA4]] (+0.75, fdr 7e-06), [[COL12A1]] (+0.72, fdr 7e-06), [[CILK1]] (+0.68, fdr 8e-06); moves opposite to [[AXIN1]] (-0.68, fdr 7e-06), [[SENP5]] (-0.68, fdr 7e-06), [[ZMYND19]] (-0.67, fdr 1e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[CSF1]] → it (grade B ⚠); 28 go from it, the strongest it → [[FAM171B]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9116.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.09×** | +17.9 | 0e+00 | 33/42 (A549, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.84×** | +17.9 | 0e+00 | 31/38 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.87×** | +17.4 | 0e+00 | 24/29 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.40×** | +14.4 | 4e-45 | 35/43 (A549, LoVo, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.22×** | +12.7 | 8e-35 | 30/32 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.90×** | +11.0 | 5e-26 | 32/43 (A549, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.87×** | +10.0 | 1e-21 | 32/42 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.50×** | +9.9 | 2e-21 | 31/43 (HEC-1-A, A-427, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.61×** | +8.2 | 2e-14 | 28/43 (A549, A498, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.44×** | +6.0 | 1e-07 | 22/42 (MIA PaCa-2, HOP62, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.43×** | +5.7 | 8e-07 | 23/43 (A-427, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.37×** | +5.4 | 3e-06 | 21/43 (MIA PaCa-2, A549, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +5.3 | 6e-06 | 18/42 (A549, LoVo, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.29×** | +5.0 | 2e-05 | 15/43 (MIA PaCa-2, HOP62, …) | two highest doses | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.21×** | +4.7 | 9e-05 | 19/43 (NCI-H1792, RKO, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.26×** | +4.7 | 1e-04 | 13/43 (MIA PaCa-2, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.26×** | +4.4 | 3e-04 | 17/43 (MIA PaCa-2, C32, …) | two highest doses | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.31×** | +4.4 | 3e-04 | 19/42 (C32, LoVo, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.32×** | +4.4 | 3e-04 | 17/42 (MIA PaCa-2, NCI-H2347, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.30×** | +4.4 | 3e-04 | 16/42 (MIA PaCa-2, HOP62, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9116.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.669×** | -4.9 | 2e-04 | 18/41 (HEC-1-A, NCI-H661, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.751×** | -4.9 | 2e-04 | 18/43 (Panc 03.27, Hs 766T, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.752×** | -4.9 | 2e-04 | 17/42 (Panc 03.27, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.758×** | -4.8 | 3e-04 | 18/43 (Panc 03.27, A-427, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.645×** | -3.9 | 0.010 | 10/42 (SW48, A498, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.801×** | -3.8 | 0.013 | 14/42 (RKO, LOX-IMVI, …) | inconsistent across doses |  |
| [[Bergenin (drug)]] 0.5 µM |  | **0.795×** | -3.6 | 0.022 | 13/42 (SW48, H4, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 0.862× | -3.6 | 0.023 | 17/42 (SNU-1, RKO, …) | top dose only | position effect removed |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM |  | **0.811×** | -3.3 | 0.055 | 6/42 (Hs 766T, SHP-77, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.822× | -3.1 | 0.10 | 13/42 (SW48, RPMI-7951, …) | inconsistent across doses |  |
| [[BAY1125976 (drug)]] 0.5 µM |  | 0.781× | -3.0 | 0.13 | 10/42 (BT-474, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9116. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 30.9 | 9 (5 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 2.24× (z +19.1) ⚠ position not correctable · without an alert: [[Binimetinib (drug)]] 0.5 µM 3.00× (z +9.2) | — |
| [[A498 (line)]] | wt | 26.5 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +13.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.36× (z +11.1) | — |
| [[A549 (line)]] | wt | 29.6 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.69× (z +18.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 6.99× (z +14.2) | — |
| [[A-172 (line)]] | wt | 29.8 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +11.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.00× (z +8.5) | — |
| [[HEC-1-A (line)]] | alt | 19.6 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +13.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.14× (z +11.1) | — |
| [[J82 (line)]] | alt | 23.7 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +12.4) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[SNU-423 (line)]] | alt | 29.8 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.45× (z +12.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 3.44× (z +9.0) | — |
| [[HOP62 (line)]] | alt | 24.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.23× (z +10.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 38.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +10.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.98× (z +8.7) | — |
| [[PANC-1 (line)]] | alt | 20.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.84× (z +14.7) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 23.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.42× (z +16.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.93× (z +9.1) | — |
| [[NCI-H2030 (line)]] | alt | 27.3 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.73× (z +9.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 3.91× (z +9.8) | — |
| [[NCI-H460 (line)]] | wt | 17.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.63× (z +12.1) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 32.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.57× (z +15.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.55× (z +10.6) | — |
| [[RPMI-7951 (line)]] | alt | 26.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.51× (z +9.9) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 30.7 | 0 | 1 | — | [[Decitabine (drug)]] 0.5 µM 0.0896× (z -9.6) |
| [[H4 (line)]] | wt | 28.6 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.127× (z -11.0) |
| [[HepG2_C3A (line)]] | wt | 14.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.00× (z +11.1) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[HS-578T (line)]] | alt | 14.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.73× (z +9.3) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 35.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.47× (z +9.5) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 7.57 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 7.91× (z +11.5) | — |
| [[LOX-IMVI (line)]] | wt | 24.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.66× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 9.57 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 7.16× (z +9.7) | — |
| [[NCI-H1792 (line)]] | alt | 31.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.79× (z +8.8) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 24.5 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.392× (z -8.6) ⚠ cell-cycle shift, explains ~45% of this change |
| [[SNU-1 (line)]] | wt | 39.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.159× (z -16.6) ⚠ cell-cycle shift, explains ~45% of this change |
| [[A-427 (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.28 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.88 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.77 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.14 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.51 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.16 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 258 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.96 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9116), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCOA4]] | +0.75 | +0.73 / +0.73 | both halves | 7e-06 |  |
| [[COL12A1]] | +0.72 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[CILK1]] | +0.68 | +0.70 / +0.58 | both halves | 8e-06 |  |
| [[ZNF260]] | +0.67 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[ARMT1]] | +0.67 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[TAB2]] | +0.66 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[OGFRL1]] | +0.66 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[MBTPS2]] | +0.65 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[BMI1]] | +0.65 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[SCRN1]] | +0.64 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[SYNE1]] | +0.64 | +0.63 / +0.57 | both halves | 9e-06 |  |
| [[HINT3]] | +0.63 | +0.53 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AXIN1]] | -0.68 | -0.60 / -0.66 | both halves | 7e-06 |  |
| [[SENP5]] | -0.68 | -0.68 / -0.62 | both halves | 7e-06 |  |
| [[ZMYND19]] | -0.67 | -0.57 / -0.62 | both halves | 1e-05 |  |
| [[UQCRH]] | -0.65 | -0.59 / -0.65 | both halves | 7e-06 |  |
| [[QPCTL]] | -0.65 | -0.55 / -0.65 | both halves | 1e-05 |  |
| [[DRD4]] | -0.65 | -0.56 / -0.64 | both halves | 1e-05 |  |
| [[IL9RP3]] | -0.64 | -0.28 / -0.67 | both halves | 3e-04 |  |
| [[GBA2]] | -0.64 | -0.58 / -0.58 | both halves | 8e-06 |  |
| [[ANKRD13D]] | -0.64 | -0.54 / -0.65 | both halves | 1e-05 |  |
| [[ATG101]] | -0.63 | -0.49 / -0.65 | both halves | 1e-05 |  |
| [[PDCD6]] | -0.62 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[CSNK1G2]] | -0.61 | -0.55 / -0.64 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CSF1]] | B | CSF1 activity raises CFL2's level | lines that do not express CSF1 (21) vs lines expressing it (29) | 2.12× lower at baseline in the lines without CSF1 | 0.026 | ⚠ within organs, on part of the lines; also absent: SERPINE1, TNFRSF9, ROR1-AS1 |
| [[MYL9]] | B | MYL9 activity raises CFL2's level | lines that do not express MYL9 (22) vs lines expressing it (28) | 1.82× lower at baseline in the lines without MYL9 | 0.040 | ⚠ within organs, on part of the lines; also absent: CCBE1, EFEMP1, SEC14L4 |
| [[OGFRL1]] | B | OGFRL1 activity raises CFL2's level | lines that do not express OGFRL1 (10) vs lines expressing it (40) | 2.40× lower at baseline in the lines without OGFRL1 | 0.059 | ⚠ within organs, on part of the lines; also absent: AFAP1L1, HDGFL3, CYP46A1 |
| [[FAM171B]] | B | FAM171B activity raises CFL2's level | lines that do not express FAM171B (7) vs lines expressing it (43) | 2.37× lower at baseline in the lines without FAM171B | 0.064 | ⚠ within organs, on part of the lines; also absent: NXPE3, GXYLT2, TMOD2; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises CFL2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CYP2U1]] | C | CYP2U1 activity raises CFL2's level | lines that do not express CYP2U1 (4) vs lines expressing it (46) | 3.33× lower at baseline in the lines without CYP2U1 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: CCDC102A, SPDL1, ASIC1; maybe low, not absent; its own permutation p |

### Downstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 0, C 28. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM171B]] | C | CFL2 activity raises FAM171B's level | lines that do not express CFL2 (4) vs lines expressing it (45) | 4.88× lower at baseline in the lines without CFL2 | 0.060 | ⚠ few lines (4 vs 45); within organs, on part of the lines; also absent: TPST1, SLC35F1, ITGA2B; maybe low, not absent; its own permutation p |
| [[CYP2U1]] | C | CFL2 activity raises CYP2U1's level | lines that do not express CFL2 (4) vs lines expressing it (45) | 2.43× lower at baseline in the lines without CFL2 | 0.060 | ⚠ few lines (4 vs 45); within organs, on part of the lines; also absent: TPST1, SLC35F1, ITGA2B; maybe low, not absent; its own permutation p |
| [[ARL2BP]] | C | CFL2 activity raises ARL2BP's level | lines that do not express CFL2 (4) vs lines expressing it (45) | 2.16× lower at baseline in the lines without CFL2 | 0.060 | ⚠ few lines (4 vs 45); within organs, on part of the lines; also absent: TPST1, SLC35F1, ITGA2B; maybe low, not absent; its own permutation p |
| [[ACAT1]] | C | CFL2 activity raises ACAT1's level | lines that do not express CFL2 (4) vs lines expressing it (45) | 2.16× lower at baseline in the lines without CFL2 | 0.060 | ⚠ few lines (4 vs 45); within organs, on part of the lines; also absent: TPST1, SLC35F1, ITGA2B; maybe low, not absent; its own permutation p |
| [[FECH]] | C | CFL2 activity raises FECH's level | lines that do not express CFL2 (4) vs lines expressing it (45) | 2.09× lower at baseline in the lines without CFL2 | 0.060 | ⚠ few lines (4 vs 45); within organs, on part of the lines; also absent: TPST1, SLC35F1, ITGA2B; maybe low, not absent; its own permutation p |
| [[SH2B2]] | C | CFL2 activity raises SH2B2's level | lines that do not express CFL2 (4) vs lines expressing it (45) | 2.01× lower at baseline in the lines without CFL2 | 0.060 | ⚠ few lines (4 vs 45); within organs, on part of the lines; also absent: TPST1, SLC35F1, ITGA2B; maybe low, not absent; its own permutation p |
| [[ZKSCAN8]] | C | CFL2 activity raises ZKSCAN8's level | lines that do not express CFL2 (4) vs lines expressing it (45) | 1.97× lower at baseline in the lines without CFL2 | 0.060 | ⚠ few lines (4 vs 45); within organs, on part of the lines; also absent: TPST1, SLC35F1, ITGA2B; maybe low, not absent; its own permutation p |
| [[SCCPDH]] | C | CFL2 activity raises SCCPDH's level | lines that do not express CFL2 (4) vs lines expressing it (45) | 1.93× lower at baseline in the lines without CFL2 | 0.060 | ⚠ few lines (4 vs 45); within organs, on part of the lines; also absent: TPST1, SLC35F1, ITGA2B; maybe low, not absent; its own permutation p |
| [[MBTPS2]] | C | CFL2 activity raises MBTPS2's level | lines that do not express CFL2 (4) vs lines expressing it (45) | 1.87× lower at baseline in the lines without CFL2 | 0.060 | ⚠ few lines (4 vs 45); within organs, on part of the lines; also absent: TPST1, SLC35F1, ITGA2B; maybe low, not absent; its own permutation p |
| [[SMARCE1]] | C | CFL2 activity raises SMARCE1's level | lines that do not express CFL2 (4) vs lines expressing it (45) | 1.40× lower at baseline in the lines without CFL2 | 0.060 | ⚠ few lines (4 vs 45); within organs, on part of the lines; also absent: TPST1, SLC35F1, ITGA2B; maybe low, not absent; its own permutation p |
| [[LRRC58]] | C | CFL2 activity raises LRRC58's level | lines that do not express CFL2 (4) vs lines expressing it (45) | 1.32× lower at baseline in the lines without CFL2 | 0.060 | ⚠ few lines (4 vs 45); within organs, on part of the lines; also absent: TPST1, SLC35F1, ITGA2B; maybe low, not absent; its own permutation p |
| [[ATG2B]] | C | CFL2 activity raises ATG2B's level | lines that do not express CFL2 (4) vs lines expressing it (45) | 1.32× lower at baseline in the lines without CFL2 | 0.060 | ⚠ few lines (4 vs 45); within organs, on part of the lines; also absent: TPST1, SLC35F1, ITGA2B; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.621). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-15.0, 2.0); signed map (16.3, -31.0). **Vector** length 107, 26.4% of its response variance represented; |z| ≥ 3 in 929 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +8.2 | +14.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +7.4 | +9.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +17.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.5 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.3 | +17.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.6 | +6.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.3 | +4.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.3 | +4.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.2 | +3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +4.2 | +4.4 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -3.5 | -4.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -3.1 | -4.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.9 | -4.9 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -2.7 | -2.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.7 | -4.9 |
|  | [[EX229 (drug)]] 5 µM |  | -2.2 | -3.9 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | -2.0 | -3.0 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -2.0 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | cofilin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q13.1 — chr14:34,709,113-34,714,823 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NEM7 |
| Gene groups (HGNC) | Cofilin family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y281](https://www.uniprot.org/uniprotkb/Q9Y281) (Cofilin-2):

> Controls reversibly actin polymerization and depolymerization in a pH-sensitive manner. Its F-actin depolymerization activity is regulated by association with CSPR3. It has the ability to bind G- and F-actin in a 1:1 ratio of cofilin to actin. It is the major component of intranuclear and cytoplasmic actin rods. Required for muscle maintenance. May play a role during the exchange of alpha-actin forms during the early postnatal remodeling of the sarcomere (By similarity).

**Summary**, from NCBI Gene [1073](https://www.ncbi.nlm.nih.gov/gene/1073):

> This gene encodes an intracellular protein that is involved in the regulation of actin-filament dynamics. This protein is a major component of intranuclear and cytoplasmic actin rods. It can bind G- and F-actin in a 1:1 ratio of cofilin to actin, and it reversibly controls actin polymerization and depolymerization in a pH-dependent manner. Mutations in this gene cause nemaline myopathy type 7, a form of congenital myopathy. Alternative splicing results in multiple transcript variants. [provided …

**Accessions** — [HGNC:1875](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1875) · Entrez [1073](https://www.ncbi.nlm.nih.gov/gene/1073) · UniProt [Q9Y281](https://www.uniprot.org/uniprotkb/Q9Y281) · Ensembl [ENSG00000165410](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165410)

## Data

Gene col 9116: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9116); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9116, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9116]; `tensor/DDL_lfc|DDL_z.npy` [9116]; `embed/gene_vectors.npy` [9116]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9116 or target_col == 9116). Every well: [[CFL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CFL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
