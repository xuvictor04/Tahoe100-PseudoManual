---
symbol: "SUV39H2"
type: "gene"
col: 7630
ensembl_id: "ENSG00000152455"
name: "SUV39H2 histone lysine methyltransferase"
location: "10p13"
module: 6
arm: "+"
pooled_cpm: 13.03
n_lines_expressing: 50
n_dd_up: 36
n_dd_down: 15
n_dd_up_clean: 14
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# SUV39H2

*SUV39H2 histone lysine methyltransferase* — 10p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (22 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.03× (z +22.0, q 0e+00, up in 44 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.770× (z -5.3, q 7e-05, down in 19 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MCM8]] (+0.75, fdr 7e-06), [[CENPO]] (+0.74, fdr 7e-06), [[UHRF1]] (+0.73, fdr 7e-06); moves opposite to [[UBE2B]] (-0.73, fdr 7e-06), [[SAT2]] (-0.64, fdr 7e-06), [[NOP53]] (-0.63, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 22 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 22 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7630.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.03×** | +22.0 | 0e+00 | 44/46 (AsPC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.05×** | +14.2 | 5e-43 | 32/46 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **2.16×** | +10.7 | 1e-24 | 41/47 (NCI-H1792, SNU-423, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **2.08×** | +10.2 | 2e-22 | 38/47 (PANC-1, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **2.08×** | +9.9 | 6e-21 | 33/46 (HOP62, SW480, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **3.63×** | +9.4 | 3e-19 | 33/46 (PANC-1, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.93×** | +9.2 | 3e-18 | 37/47 (PANC-1, A498, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **1.87×** | +8.7 | 2e-16 | 33/47 (AsPC-1, A549, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **1.82×** | +8.4 | 4e-15 | 32/47 (A498, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.79×** | +8.1 | 3e-14 | 32/45 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **3.00×** | +8.0 | 5e-14 | 27/43 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.80×** | +7.9 | 2e-13 | 30/46 (HOP62, SK-MEL-2, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.74×** | +7.7 | 5e-13 | 30/46 (HT-29, AsPC-1, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.71×** | +7.5 | 2e-12 | 34/47 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.70×** | +7.1 | 4e-11 | 30/47 (PANC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.53×** | +6.0 | 8e-08 | 26/45 (A549, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +5.2 | 6e-06 | 21/48 (PANC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.49×** | +3.7 | 0.004 | 6/48 (PANC-1, MIA PaCa-2, …) | two highest doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.64×** | +3.6 | 0.007 | 11/43 (PANC-1, Panc 03.27, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.60×** | +3.4 | 0.011 | 7/44 (MIA PaCa-2, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.54×** | +3.1 | 0.031 | 7/45 (MIA PaCa-2, NCI-H23, …) | two highest doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.24×** | +3.0 | 0.047 | 7/47 (A-172, NCI-H23, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **1.49×** | +2.9 | 0.064 | 6/42 (A498, NCI-H460, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7630.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.770×** | -5.3 | 7e-05 | 19/48 (SHP-77, LS 180, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.727×** | -4.5 | 0.002 | 18/45 (SW480, LS 180, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.740×** | -4.3 | 0.004 | 18/44 (LS 180, SNU-1, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.761×** | -4.2 | 0.004 | 21/48 (NCI-H23, SW48, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.759×** | -3.8 | 0.017 | 13/46 (HS-578T, LoVo, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.831×** | -3.7 | 0.017 | 15/48 (KATO III, RKO, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.764×** | -3.7 | 0.018 | 13/46 (SNU-1, hTERT-HPNE, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.775×** | -3.5 | 0.029 | 13/48 (HEC-1-A, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 5 µM |  | 0.844× | -3.5 | 0.034 | 9/48 (HEC-1-A, SW 900, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.699×** | -3.4 | 0.037 | 11/44 (Hs 766T, NCI-H2030, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.789×** | -3.4 | 0.038 | 10/47 (AN3 CA, KATO III, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.797×** | -3.2 | 0.057 | 7/47 (LoVo, SW480, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | **0.800×** | -3.2 | 0.063 | 7/47 (KATO III, LoVo, …) | top dose only |  |
| [[Alpelisib (drug)]] 5 µM |  | **0.658×** | -3.1 | 0.076 | 12/41 (NCI-H23, A549, …) | top dose only | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.855× | -3.1 | 0.076 | 8/48 (SW480, SK-MEL-2, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.861× | -3.0 | 0.096 | 13/47 (NCI-H661, C32, …) | all doses, flat |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.732×** | -3.0 | 0.096 | 8/43 (LoVo, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.813×** | -3.0 | 0.096 | 11/47 (KATO III, A-172, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.85 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7630. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 12.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +11.5) | — |
| [[A-172 (line)]] | wt | 14.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.192× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 11.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.25× (z +10.2) | — |
| [[A549 (line)]] | wt | 11.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +10.2) | — |
| [[AsPC-1 (line)]] | alt | 6.52 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.91× (z +13.2) | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0884× (z -9.3) |
| [[J82 (line)]] | alt | 19.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.90× (z +9.9) | [[Dinaciclib (drug)]] 0.05 µM 0.194× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 11.3 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.12× (z +10.4) | [[Pyridoxine (drug)]] 0.5 µM 0.212× (z -10.1) |
| [[RPMI-7951 (line)]] | alt | 12.1 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.67× (z +9.2) | [[Thymol (drug)]] 0.5 µM 0.130× (z -8.8) |
| [[SHP-77 (line)]] | alt | 27.6 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +10.0) | [[Acetohexamide (drug)]] 0.5 µM 0.280× (z -8.6) |
| [[C-33 A (line)]] | alt | 27.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.170× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 7.37 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.39× (z +10.3) | — |
| [[HEC-1-A (line)]] | alt | 17.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.157× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 13.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.23× (z +8.9) | — |
| [[HOP62 (line)]] | alt | 11.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +8.9) | — |
| [[HS-578T (line)]] | alt | 8.83 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.29× (z +9.9) | — |
| [[LOX-IMVI (line)]] | wt | 11.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.33× (z +11.5) | — |
| [[NCI-H1792 (line)]] | alt | 13.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.26× (z +11.9) | — |
| [[NCI-H2030 (line)]] | alt | 16.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.74× (z +11.6) | — |
| [[NCI-H2347 (line)]] | alt | 6.59 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.04× (z +10.2) | — |
| [[Panc 03.27 (line)]] | alt | 7.41 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.35× (z +8.6) | — |
| [[SNU-423 (line)]] | alt | 7.30 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.75× (z +9.7) | — |
| [[SW 900 (line)]] | alt | 8.34 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.40× (z +8.7) | — |
| [[SW1417 (line)]] | alt | 15.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +9.2) | — |
| [[A-427 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.51 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.43 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.49 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.92 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 21.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7630), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCM8]] | +0.75 | +0.77 / +0.75 | both halves | 7e-06 |  |
| [[CENPO]] | +0.74 | +0.70 / +0.76 | both halves | 7e-06 |  |
| [[UHRF1]] | +0.73 | +0.71 / +0.76 | both halves | 7e-06 | STRING 456 |
| [[VRK1]] | +0.73 | +0.74 / +0.73 | both halves | 7e-06 |  |
| [[CDC25A]] | +0.72 | +0.72 / +0.76 | both halves | 7e-06 |  |
| [[KNTC1]] | +0.72 | +0.69 / +0.72 | both halves | 7e-06 |  |
| [[XRCC2]] | +0.72 | +0.74 / +0.72 | both halves | 7e-06 |  |
| [[DDIAS]] | +0.71 | +0.74 / +0.71 | both halves | 7e-06 |  |
| [[XRCC3]] | +0.71 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[ESCO2]] | +0.71 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[GEN1]] | +0.71 | +0.68 / +0.72 | both halves | 7e-06 |  |
| [[HASPIN]] | +0.70 | +0.67 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2B]] | -0.73 | -0.66 / -0.73 | both halves | 7e-06 |  |
| [[SAT2]] | -0.64 | -0.60 / -0.63 | both halves | 7e-06 |  |
| [[NOP53]] | -0.63 | -0.58 / -0.58 | both halves | 7e-06 |  |
| [[OAZ1]] | -0.62 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[TBC1D17]] | -0.61 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[ATP5MC2]] | -0.60 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[SEC62]] | -0.60 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[JUND]] | -0.59 | -0.49 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SUV39H2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PIK3CA]] | B | PIK3CA activity raises SUV39H2's level | compounds that target PIK3CA: 3 of 4 lower it (Alpelisib, Bimiralisib, GSK1059615) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[GKAP1]] | C | GKAP1 activity raises SUV39H2's level | lines that do not express GKAP1 (3) vs lines expressing it (47) | 2.26× lower at baseline in the lines without GKAP1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SEMA3F, TMEM132A, SPDL1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.670). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-38.3, -43.9); signed map (-38.2, -48.6). **Vector** length 82.4, 17.4% of its response variance represented; |z| ≥ 3 in 1,230 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.52 to 65); *DNA strand elongation* (reactome, mean cos +0.54 to 28); *DNA Replication* (reactome, mean cos +0.53 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.2 | +22.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +4.8 | +9.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +4.3 | +7.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~50% of this change | +4.0 | +7.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.5 | +9.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +7.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.0 | +3.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.0 | +3.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.7 | +3.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | -5.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -3.3 | -4.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.7 | -4.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -0.8 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | -2.6 | -3.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.3 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.2 | -3.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.2 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | SUV39H2 histone lysine methyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p13 — chr10:14,878,820-14,904,315 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23414, KMT1B |
| Gene groups (HGNC) | Histone lysine methyltransferases; SET domain containing |
| Reactome | 3 pathways, smallest: PKMTs methylate histone lysines; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H5I1](https://www.uniprot.org/uniprotkb/Q9H5I1) (Histone-lysine N-methyltransferase SUV39H2):

> Histone methyltransferase that specifically mediates trimethylation of 'Lys-9' of histone H3 (H3K9me3) using monomethylated H3 'Lys-9' (H3K9me1) as substrate. H3 'Lys-9' trimethylation represents a specific tag for epigenetic transcriptional repression by recruiting HP1 (CBX1, CBX3 and/or CBX5) proteins to methylated histones. Mainly functions in heterochromatin regions, thereby playing a central role in the establishment of constitutive heterochromatin at pericentric and telomere regions. H3 …

**Summary**, from NCBI Gene [79723](https://www.ncbi.nlm.nih.gov/gene/79723):

> Enables cation binding activity; histone H3K14ub reader activity; and histone H3K9 trimethyltransferase activity. Involved in epigenetic programming in the zygotic pronuclei and pericentric heterochromatin formation. Acts upstream of or within cellular response to hypoxia and negative regulation of transcription by RNA polymerase II. Located in chromatin. Is active in nucleus and pericentric heterochromatin. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17287](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17287) · Entrez [79723](https://www.ncbi.nlm.nih.gov/gene/79723) · UniProt [Q9H5I1](https://www.uniprot.org/uniprotkb/Q9H5I1) · Ensembl [ENSG00000152455](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152455)

## Data

Gene col 7630: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7630); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7630, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7630]; `tensor/DDL_lfc|DDL_z.npy` [7630]; `embed/gene_vectors.npy` [7630]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7630 or target_col == 7630). Every well: [[SUV39H2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SUV39H2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
