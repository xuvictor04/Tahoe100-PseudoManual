---
symbol: "BCL2L12"
type: "gene"
col: 4734
ensembl_id: "ENSG00000126453"
name: "BCL2 like 12"
location: "19q13.33"
module: 109
arm: "+"
pooled_cpm: 13.31
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 17
n_dd_up_clean: 3
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/109"]
generated_by: "tahoemap"
---

# BCL2L12

*BCL2 like 12* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.14× (z +20.9, q 0e+00, up in 43 of 47 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.20× (z +14.5, q 6e-45, up in 39 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.605× (z -5.6, q 1e-05, down in 25 of 48 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.642× (z -5.3, q 4e-05, down in 27 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EGR2]] (+0.71, fdr 7e-06), [[EGR3]] (+0.70, fdr 7e-06), [[TRIOBP]] (+0.64, fdr 1e-05); moves opposite to [[DUBR]] (-0.62, fdr 2e-05), [[WWP1]] (-0.60, fdr 3e-05), [[MRPS35]] (-0.58, fdr 1e-05).
> It is in [[Module 109]], a single-armed module (immediate early).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 15 with an alert ⚠; shown: the 15 strongest. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4734.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **3.14×** | +20.9 | 0e+00 | 43/47 (LoVo, NCI-H460, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.20×** | +14.5 | 6e-45 | 39/46 (A549, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **2.14×** | +9.8 | 1e-20 | 41/47 (SW480, SW1417, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **2.08×** | +9.5 | 3e-19 | 38/47 (A549, SW1417, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **2.13×** | +9.4 | 6e-19 | 34/47 (NCI-H460, A549, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.99×** | +8.9 | 5e-17 | 40/47 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.85×** | +8.0 | 1e-13 | 26/45 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **1.80×** | +7.6 | 2e-12 | 33/45 (NCI-H460, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.50×** | +5.3 | 7e-06 | 23/44 (RKO, H4, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.50×** | +5.3 | 7e-06 | 23/47 (NCI-H460, AsPC-1, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~66% of this change | **1.46×** | +4.9 | 5e-05 | 20/41 (NCI-H2030, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.43×** | +4.6 | 2e-04 | 21/39 (NCI-H460, SW1417, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +4.4 | 4e-04 | 17/46 (LoVo, SW480, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **1.36×** | +3.8 | 0.006 | 11/40 (J82, NCI-H2030, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.35×** | +3.6 | 0.012 | 13/33 (LS 180, SW480, …) | all doses, flat | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4734.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.605×** | -5.6 | 1e-05 | 25/48 (C-33 A, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.642×** | -5.3 | 4e-05 | 27/47 (NCI-H23, SNU-1, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.692×** | -4.7 | 4e-04 | 18/47 (SW1417, A498, …) | two highest doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.684×** | -4.7 | 4e-04 | 21/48 (A-427, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.726×** | -4.6 | 4e-04 | 21/48 (HT-29, A-427, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.777×** | -4.5 | 6e-04 | 23/48 (NCI-H1792, HT-29, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.699×** | -4.4 | 7e-04 | 20/46 (NCI-H23, AsPC-1, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.711×** | -4.2 | 0.002 | 23/45 (LOX-IMVI, hTERT-HPNE, …) | two highest doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.739×** | -3.9 | 0.006 | 18/47 (NCI-H23, HEC-1-A, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.738×** | -3.7 | 0.013 | 14/45 (SK-MEL-2, J82, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.530×** | -3.6 | 0.015 | 10/44 (Panc 03.27, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.793×** | -3.4 | 0.037 | 13/48 (A-427, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.763×** | -3.3 | 0.043 | 9/45 (HepG2/C3A, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Pemetrexed (drug)]] 0.5 µM |  | **0.779×** | -3.2 | 0.052 | 11/47 (NCI-H661, C32, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.838× | -3.2 | 0.052 | 17/48 (HT-29, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.574×** | -3.2 | 0.053 | 7/47 (A-427, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ciclopirox (drug)]] 0.5 µM |  | **0.786×** | -3.1 | 0.063 | 6/47 (CHP-212, HS-578T, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.844× | -3.1 | 0.064 | 9/48 (C-33 A, J82, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.51 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4734. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 7.57 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.26× (z +14.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.98× (z +10.2) | — |
| [[A549 (line)]] | wt | 11.4 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.77× (z +12.3) | — |
| [[AsPC-1 (line)]] | alt | 10.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.43× (z +10.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.25× (z +10.2) | — |
| [[C32 (line)]] | wt | 10.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.19× (z +10.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.50× (z +8.5) | — |
| [[CFPAC-1 (line)]] | alt | 9.03 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +9.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.61× (z +9.2) | — |
| [[HepG2_C3A (line)]] | wt | 13.9 | 0 | 2 | — | [[Glycyrrhizic acid (drug)]] 5 µM 0.111× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 12.7 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.84× (z +11.6) | — |
| [[PANC-1 (line)]] | alt | 11.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +10.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +9.2) | — |
| [[SK-MEL-2 (line)]] | alt | 10.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +8.5) ⚠ cell-cycle shift, explains ~28% of this change | [[Bortezomib (drug)]] 0.05 µM 0.0824× (z -10.5) ⚠ cell-cycle shift, explains ~75% of this change |
| [[A-172 (line)]] | wt | 9.88 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +8.6) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[A-427 (line)]] | wt | 20.7 | 0 | 1 | — | [[GSK1059615 (drug)]] 5 µM 0.0487× (z -8.6) |
| [[A498 (line)]] | wt | 11.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +8.7) | — |
| [[AN3 CA (line)]] | alt | 32.1 | 0 | 1 | — | [[Acetazolamide (drug)]] 0.5 µM 0.0736× (z -9.9) |
| [[HOP62 (line)]] | alt | 8.87 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.06× (z +10.6) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[HS-578T (line)]] | alt | 12.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +12.0) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 8.38 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0837× (z -9.1) |
| [[J82 (line)]] | alt | 12.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +8.7) | — |
| [[LoVo (line)]] | wt | 12.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.18× (z +14.8) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[LOX-IMVI (line)]] | wt | 13.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.90× (z +13.7) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[LS 180 (line)]] | wt | 11.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +10.0) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 17.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +9.8) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H2030 (line)]] | alt | 18.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +9.8) | — |
| [[NCI-H23 (line)]] | alt | 17.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +8.8) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[RKO (line)]] | wt | 17.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +8.5) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[RPMI-7951 (line)]] | alt | 15.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.65× (z +10.3) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[SNU-1 (line)]] | wt | 11.4 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0978× (z -8.5) |
| [[SW 900 (line)]] | alt | 15.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +8.7) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[SW480 (line)]] | alt | 14.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +8.9) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[BT-474 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.61 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.60 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.42 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.55 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4734), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EGR2]] | +0.71 | +0.77 / +0.65 | both halves | 7e-06 |  |
| [[EGR3]] | +0.70 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[TRIOBP]] | +0.64 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[STX10]] | +0.62 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[ING1]] | +0.61 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[GCAT]] | +0.60 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[ESPL1]] | +0.59 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[EGR1]] | +0.59 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[ASTL]] | +0.59 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[LSR]] | +0.58 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[THSD8]] ⚠ | +0.58 | +0.58 / +0.57 | both halves | 9e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[MYLK2]] | +0.57 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[SPATA32]] | +0.57 | +0.61 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DUBR]] | -0.62 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[WWP1]] | -0.60 | -0.70 / -0.46 | both halves | 3e-05 |  |
| [[MRPS35]] | -0.58 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[RAD23B]] | -0.56 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[RFXAP]] | -0.53 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[OSBPL1A]] | -0.52 | -0.46 / -0.48 | both halves | 2e-05 |  |
| [[SNX4]] | -0.52 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[RBM41]] | -0.52 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[NTPCR]] | -0.51 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[NXPE3]] | -0.51 | -0.54 / -0.40 | both halves | 5e-05 |  |
| [[ATP5F1C]] | -0.50 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[GNPDA2]] | -0.50 | -0.52 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises BCL2L12's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 109]] — immediate early; 43 genes; every member is in the + arm (projection on the module's main direction 0.627). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.7, -1.6); signed map (4.5, 29.5). **Vector** length 80.2, 16.5% of its response variance represented; |z| ≥ 3 in 1,008 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +5.9 | +20.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +14.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +2.7 | +9.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +1.8 | +5.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~66% of this change | +1.5 | +4.9 |
|  | [[SBI-0640756 (drug)]] 5 µM |  | +1.5 | +1.0 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.4 | +1.6 |
|  | [[Pimitespib (drug)]] 5 µM |  | +1.4 | +1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +0.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.2 | +0.6 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~75% of this change | -4.8 | -3.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | -1.7 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -3.6 | -5.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.6 | -0.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.6 | -3.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.2 | -4.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.2 | -5.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.1 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | BCL2 like 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:49,665,142-49,673,916 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | BCL2 family |
| Matched by | ensembl_id |

UniProt [Q9HB09](https://www.uniprot.org/uniprotkb/Q9HB09) carries no function annotation.

**Summary**, from NCBI Gene [83596](https://www.ncbi.nlm.nih.gov/gene/83596):

> This gene encodes a member of a family of proteins containing a Bcl-2 homology domain 2 (BH2). The encoded protein is an anti-apoptotic factor that acts as an inhibitor of caspases 3 and 7 in the cytoplasm. In the nucleus, it binds to the p53 tumor suppressor protein, preventing its association with target genes. Overexpression of this gene has been detected in a number of different cancers. There is a pseudogene for this gene on chromosome 3. Alternative splicing results in multiple transcript …

**Accessions** — [HGNC:13787](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13787) · Entrez [83596](https://www.ncbi.nlm.nih.gov/gene/83596) · UniProt [Q9HB09](https://www.uniprot.org/uniprotkb/Q9HB09) · Ensembl [ENSG00000126453](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126453)

## Data

Gene col 4734: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4734); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4734, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4734]; `tensor/DDL_lfc|DDL_z.npy` [4734]; `embed/gene_vectors.npy` [4734]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4734 or target_col == 4734). Every well: [[BCL2L12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BCL2L12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
