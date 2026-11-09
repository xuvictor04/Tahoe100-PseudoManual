---
symbol: "CD9"
type: "gene"
col: 204
ensembl_id: "ENSG00000010278"
name: "CD9 molecule"
location: "12p13.31"
module: 28
arm: "-"
pooled_cpm: 115.61
n_lines_expressing: 40
n_dd_up: 12
n_dd_down: 13
n_dd_up_clean: 5
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# CD9

*CD9 molecule* — 12p13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.96× (z +13.4, q 4e-38, up in 37 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.77× (z +10.0, q 3e-21, up in 27 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.279× (z -22.3, q 0e+00, down in 37 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITGA6]] (+0.60, fdr 1e-05), [[KLF13]] (+0.58, fdr 1e-05), [[TMBIM6]] (+0.55, fdr 1e-05); moves opposite to [[PSMD4]] (-0.58, fdr 2e-05), [[BRF2]] (-0.56, fdr 3e-05), [[ZFP37]] (-0.55, fdr 2e-05).
> It sits in the **-** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ITGB4]] → it (grade B ⚠); 1 goes from it, the strongest it → [[PSMC2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 204.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.96×** | +13.4 | 4e-38 | 37/39 (NCI-H1573, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.48×** | +10.8 | 9e-25 | 32/34 (C32, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +10.0 | 3e-21 | 27/39 (A549, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.31×** | +9.6 | 2e-19 | 31/35 (NCI-H1573, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.74×** | +6.9 | 7e-10 | 32/38 (C32, Hs 766T, …) | rises with dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +5.3 | 1e-05 | 21/40 (BT-474, SW 900, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.35×** | +3.7 | 0.016 | 21/38 (C32, AsPC-1, …) | all doses, flat | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.016 | 20/38 (BT-474, MIA PaCa-2, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **1.35×** | +3.6 | 0.022 | 21/37 (NCI-H1573, A-427, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.33×** | +3.5 | 0.025 | 21/38 (Hs 766T, COLO 205, …) | rises with dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.083 | 15/38 (SW 900, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.64×** | +3.1 | 0.090 | 17/38 (NCI-H2347, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 204.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.279×** | -22.3 | 0e+00 | 37/38 (SW48, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.379×** | -12.0 | 1e-30 | 33/38 (SW48, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.432×** | -10.0 | 4e-21 | 32/38 (AsPC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.556×** | -6.8 | 1e-09 | 32/38 (SW48, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~24% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.595×** | -6.4 | 2e-08 | 32/38 (COLO 205, SW48, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.668×** | -5.0 | 6e-05 | 28/38 (LS 180, LoVo, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.708×** | -4.3 | 0.002 | 23/38 (SW1417, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.529×** | -4.0 | 0.005 | 25/39 (LS 180, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.740×** | -3.7 | 0.012 | 21/38 (SW48, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.554×** | -3.7 | 0.012 | 25/34 (AsPC-1, COLO 205, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.743×** | -3.4 | 0.036 | 19/38 (SW48, LoVo, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.598×** | -3.2 | 0.061 | 18/39 (LS 180, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | **0.772×** | -3.2 | 0.063 | 18/38 (J82, PANC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 204. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 53.1 | 14 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 7.81× (z +14.7) ⚠ toxic; transcription drop · without an alert: [[Betamethasone dipropionate (drug)]] 0.5 µM 4.36× (z +10.6) | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -15.3) |
| [[SW48 (line)]] | wt | 592 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0928× (z -31.2) |
| [[Hs 766T (line)]] | wt | 348 | 1 (1 ⚠) | 6 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.29× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -25.4) |
| [[LoVo (line)]] | wt | 229 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0791× (z -28.8) |
| [[LS 180 (line)]] | wt | 259 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -28.1) |
| [[SW480 (line)]] | alt | 244 | 2 (2 ⚠) | 5 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +10.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -27.0) |
| [[AsPC-1 (line)]] | alt | 256 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -29.8) |
| [[SW1417 (line)]] | alt | 233 | 3 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.00× (z +11.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -14.5) |
| [[KATO III (line)]] | alt | 312 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.37× (z +10.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -26.5) |
| [[NCI-H2347 (line)]] | alt | 257 | 2 (1 ⚠) | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -21.9) |
| [[HOP62 (line)]] | alt | 49.1 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.81× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -13.2) |
| [[NCI-H2030 (line)]] | alt | 105 | 2 (1 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -21.1) |
| [[PANC-1 (line)]] | alt | 60.1 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.36× (z +10.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -16.4) |
| [[A-427 (line)]] | wt | 120 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.61× (z +11.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.175× (z -15.3) |
| [[A549 (line)]] | wt | 67.3 | 2 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +11.6) | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -14.7) |
| [[C32 (line)]] | wt | 90.2 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.33× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.435× (z -9.0) |
| [[COLO 205 (line)]] | alt | 150 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0631× (z -30.2) |
| [[HEC-1-A (line)]] | alt | 76.3 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.24× (z +10.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -14.2) |
| [[HT-29 (line)]] | alt | 146 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0906× (z -25.8) |
| [[Panc 03.27 (line)]] | alt | 256 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +10.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -19.3) |
| [[RKO (line)]] | wt | 87.8 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -20.4) |
| [[A-172 (line)]] | wt | 63.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -14.2) |
| [[BT-474 (line)]] | alt | 155 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -9.3) |
| [[CFPAC-1 (line)]] | alt | 54.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -14.6) |
| [[H4 (line)]] | wt | 38.2 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.35× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -9.1) |
| [[HS-578T (line)]] | alt | 33.2 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -12.0) |
| [[J82 (line)]] | alt | 53.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -10.3) |
| [[MIA PaCa-2 (line)]] | alt | 101 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.85× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -19.2) |
| [[NCI-H23 (line)]] | alt | 90.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -14.9) |
| [[RPMI-7951 (line)]] | alt | 40.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -11.1) |
| [[SW 1088 (line)]] | alt | 83.1 | 0 | 2 | — | [[Benproperine (phosphate) (drug)]] 0.5 µM 0.0633× (z -9.2) |
| [[SW 900 (line)]] | alt | 58.7 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.57× (z +10.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +8.8) | — |
| [[HCT15 (line)]] | alt | 158 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -17.4) |
| [[NCI-H1792 (line)]] | alt | 44.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -8.7) |
| [[NCI-H661 (line)]] | alt | 47.6 | 0 | 1 | — | [[Sinomenine (drug)]] 0.05 µM 0.0618× (z -9.3) |
| [[SW 1271 (line)]] | alt | 113 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -10.7) |
| [[A498 (line)]] | wt | 6.68 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.7 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 65.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.4 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.4 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 14.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 90.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 20.9 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.88 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.0 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 9.40 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 27.6 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 204), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*24 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGA6]] | +0.60 | +0.60 / +0.57 | both halves | 1e-05 | same gene group; STRING 871 |
| [[KLF13]] | +0.58 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[TMBIM6]] | +0.55 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[DIAPH1]] | +0.54 | +0.61 / +0.43 | both halves | 4e-05 |  |
| [[CST3]] | +0.53 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[MSLN]] | +0.52 | +0.54 / +0.42 | both halves | 4e-05 |  |
| [[PERP]] | +0.52 | +0.51 / +0.48 | both halves | 2e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE |
| [[ZBTB7C]] | +0.51 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[RASA1]] | +0.50 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[IGFBP2]] | +0.49 | +0.53 / +0.32 | both halves | 2e-04 |  |
| [[B4GALNT3]] | +0.49 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[ACTN4]] | +0.49 | +0.59 / +0.36 | both halves | 1e-04 | pathway: Platelet activation, signaling and aggregation |

## Genes that move opposite

*76 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD4]] | -0.58 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[BRF2]] | -0.56 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[ZFP37]] | -0.55 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[DDX1]] | -0.55 | -0.59 / -0.47 | both halves | 2e-05 | STRING 694 |
| [[PSMC5]] | -0.55 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[ZSCAN26]] | -0.55 | -0.62 / -0.46 | both halves | 3e-05 |  |
| [[AZI2]] | -0.54 | -0.64 / -0.41 | both halves | 4e-05 |  |
| [[ARMCX5]] | -0.54 | -0.43 / -0.61 | both halves | 3e-05 |  |
| [[TACO1]] | -0.54 | -0.60 / -0.36 | both halves | 1e-04 |  |
| [[NBN]] | -0.54 | -0.56 / -0.51 | both halves | 1e-05 | pathway: Reproduction |
| [[SMARCE1]] | -0.53 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[SPART]] | -0.53 | -0.54 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGB4]] | B | ITGB4 activity raises CD9's level | lines that do not express ITGB4 (25) vs lines expressing it (25) | 3.50× lower at baseline in the lines without ITGB4 | 0.021 | ⚠ within organs, on part of the lines; also absent: SCNN1A, AREG, GJB3 |
| [[B4GALNT3]] | B | B4GALNT3 activity raises CD9's level | lines that do not express B4GALNT3 (16) vs lines expressing it (34) | 3.06× lower at baseline in the lines without B4GALNT3 | 0.049 | ⚠ within organs, on part of the lines; also absent: MCF2L, EPHA1, PLEKHG6 |
| [[TOP2A]] | B | TOP2A activity lowers CD9's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MSLN]] | B | MSLN activity raises CD9's level | lines that do not express MSLN (33) vs lines expressing it (17) | 2.78× lower at baseline in the lines without MSLN | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C4BPB, EPS8L3, EDAR |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMC2]] | B | CD9 activity raises PSMC2's level | lines that do not express CD9 (10) vs lines expressing it (40) | 1.27× lower at baseline in the lines without CD9 | 0.099 | ⚠ within organs, on part of the lines; also absent: ALS2CL, CARD10, MSX2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **-** arm (projection on the module's main direction -0.520). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-30.2, 4.4); signed map (-11.8, 40.2). **Vector** length 109, 34.5% of its response variance represented; |z| ≥ 3 in 951 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.9 | +10.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +7.8 | +6.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.6 | +3.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +6.3 | +3.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.6 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.8 | +0.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.8 | +1.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.5 | -0.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +2.7 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.6 | -10.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.3 | -3.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.8 | -12.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.9 | -6.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.8 | -6.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.7 | -5.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.8 | -3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -2.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.2 | -0.9 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.7 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | CD9 molecule |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.31 — chr12:6,199,715-6,238,271 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BA2, P24, TSPAN29, MRP-1; previously MIC3 |
| Gene groups (HGNC) | CD molecules; Tetraspanin family; Gamete adhesion and fusion factors |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING, CHOLESTEROL_HOMEOSTASIS, COAGULATION, ESTROGEN_RESPONSE_LATE, MTORC1_SIGNALING |
| Reactome | 9 pathways, smallest: Uptake and function of diphtheria toxin; Fertilization; Uptake and actions of bacterial toxins |
| Matched by | ensembl_id |

**Function**, from UniProt [P21926](https://www.uniprot.org/uniprotkb/P21926) (CD9 antigen):

> Integral membrane protein associated with integrins, which regulates different processes, such as sperm-egg fusion, platelet activation and aggregation, and cell adhesion. Present at the cell surface of oocytes and plays a key role in sperm-egg fusion, possibly by organizing multiprotein complexes and the morphology of the membrane required for the fusion (By similarity). In myoblasts, associates with CD81 and PTGFRN and inhibits myotube fusion during muscle regeneration (By similarity). In …

**Summary**, from NCBI Gene [928](https://www.ncbi.nlm.nih.gov/gene/928):

> This gene encodes a member of the transmembrane 4 superfamily, also known as the tetraspanin family. Tetraspanins are cell surface glycoproteins with four transmembrane domains that form multimeric complexes with other cell surface proteins. The encoded protein functions in many cellular processes including differentiation, adhesion, and signal transduction, and expression of this gene plays a critical role in the suppression of cancer cell motility and metastasis. [provided by RefSeq, Jan 2011]

**Accessions** — [HGNC:1709](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1709) · Entrez [928](https://www.ncbi.nlm.nih.gov/gene/928) · UniProt [P21926](https://www.uniprot.org/uniprotkb/P21926) · Ensembl [ENSG00000010278](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000010278)

## Data

Gene col 204: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 204); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 204, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 204]; `tensor/DDL_lfc|DDL_z.npy` [204]; `embed/gene_vectors.npy` [204]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 204 or target_col == 204). Every well: [[CD9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CD9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
