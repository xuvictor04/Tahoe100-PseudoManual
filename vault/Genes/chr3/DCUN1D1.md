---
symbol: "DCUN1D1"
type: "gene"
col: 493
ensembl_id: "ENSG00000043093"
name: "defective in cullin neddylation 1 domain containing 1"
location: "3q26.33"
module: 28
arm: "+"
pooled_cpm: 62.04
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 1
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# DCUN1D1

*defective in cullin neddylation 1 domain containing 1* — 3q26.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.50× (z +36.9, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.880× (z -3.7, q 0.060, down in 14 of 48 measured lines) ⚠ cell-cycle shift, explains ~24% of this change. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.783× (z -3.7, q 0.060, down in 10 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SK-MEL-2 0.149×, NCI-H1573 0.503×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SK-MEL-2 0.187×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.659×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TBCEL]] (+0.69, fdr 7e-06), [[AASDHPPT]] (+0.67, fdr 7e-06), [[MIER3]] (+0.66, fdr 4e-05); moves opposite to [[DHDDS]] (-0.69, fdr 7e-06), [[DPM1]] (-0.61, fdr 1e-05), [[P4HB]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PMP22]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 493.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.50×** | +36.9 | 0e+00 | 44/48 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.27×** | +22.5 | 0e+00 | 44/48 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.92×** | +18.6 | 0e+00 | 42/48 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.47×** | +11.0 | 5e-26 | 36/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.47×** | +10.9 | 1e-25 | 38/48 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.93×** | +9.8 | 1e-20 | 41/49 (HT-29, RKO, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.29×** | +7.3 | 3e-11 | 26/47 (LoVo, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.26×** | +6.6 | 2e-09 | 27/48 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.26×** | +6.5 | 4e-09 | 22/48 (H4, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.26×** | +6.4 | 7e-09 | 25/47 (COLO 205, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.24×** | +6.2 | 3e-08 | 20/48 (H4, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.24×** | +6.2 | 3e-08 | 24/48 (RPMI-7951, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +6.1 | 5e-08 | 22/48 (A498, CFPAC-1, …) | rises with dose | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **1.49×** | +6.0 | 1e-07 | 25/48 (NCI-H1573, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.21×** | +5.1 | 1e-05 | 19/48 (HOP62, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.14× | +3.4 | 0.021 | 6/48 (SW480, HEC-1-A, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.08× | +3.0 | 0.076 | 4/48 (SNU-423, BT-474, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.11× | +2.9 | 0.095 | 10/47 (HEC-1-A, SW48, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 493.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SK-MEL-2 0.149×, NCI-H1573 0.503×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SK-MEL-2 0.187×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.659×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 0.880× | -3.7 | 0.060 | 14/48 (SW480, Panc 03.27, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.783×** | -3.7 | 0.060 | 10/47 (PANC-1, COLO 205, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.881× | -3.6 | 0.060 | 16/48 (HT-29, SW480, …) | rises with dose |  |
| [[EX229 (drug)]] 0.5 µM |  | 0.844× | -3.4 | 0.067 | 9/48 (SW480, MIA PaCa-2, …) | two highest doses | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | 0.845× | -3.4 | 0.067 | 11/48 (SW480, SNU-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Resveratrol (drug)]] 0.5 µM |  | 0.896× | -3.1 | 0.16 | 11/49 (SNU-1, SW48, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 493. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 47.9 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +22.3) | — |
| [[NCI-H1792 (line)]] | alt | 48.4 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +17.4) | — |
| [[NCI-H460 (line)]] | wt | 45.5 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +19.1) | — |
| [[A-172 (line)]] | wt | 57.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +21.3) | — |
| [[A549 (line)]] | wt | 45.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +20.3) | — |
| [[HEC-1-A (line)]] | alt | 97.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +21.5) | — |
| [[HS-578T (line)]] | alt | 56.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +23.2) | — |
| [[KATO III (line)]] | alt | 76.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +14.4) | — |
| [[LoVo (line)]] | wt | 47.1 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +16.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 81.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +13.9) | — |
| [[PANC-1 (line)]] | alt | 79.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +25.4) | — |
| [[SK-MEL-2 (line)]] | alt | 83.3 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +14.0) | [[Dinaciclib (drug)]] 5 µM 0.149× (z -21.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 43.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.99× (z +24.2) | — |
| [[HOP62 (line)]] | alt | 43.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +21.8) | — |
| [[hTERT-HPNE (line)]] | wt | 39.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.92× (z +20.4) | — |
| [[J82 (line)]] | alt | 78.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.55× (z +30.2) | — |
| [[NCI-H1573 (line)]] | alt | 73.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +15.8) | [[Dinaciclib (drug)]] 5 µM 0.503× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 64.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +19.5) | — |
| [[RPMI-7951 (line)]] | alt | 52.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +18.1) | — |
| [[SNU-423 (line)]] | alt | 47.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.43× (z +25.3) | — |
| [[C32 (line)]] | wt | 39.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +14.5) | — |
| [[H4 (line)]] | wt | 55.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +13.4) | — |
| [[LS 180 (line)]] | wt | 60.5 | 2 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +11.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.85× (z +10.5) | — |
| [[RKO (line)]] | wt | 72.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +12.9) | [[Dinaciclib (drug)]] 0.5 µM 0.427× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 41.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +12.8) | — |
| [[SW480 (line)]] | alt | 70.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +15.3) | — |
| [[A-427 (line)]] | wt | 142 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.659× (z -10.4) |
| [[BT-474 (line)]] | alt | 71.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +12.8) | — |
| [[HepG2_C3A (line)]] | wt | 39.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +11.1) | — |
| [[Hs 766T (line)]] | wt | 31.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +11.2) | — |
| [[HT-29 (line)]] | alt | 63.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +13.8) | — |
| [[NCI-H2030 (line)]] | alt | 46.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +9.9) | — |
| [[NCI-H23 (line)]] | alt | 35.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +9.1) | — |
| [[Panc 03.27 (line)]] | alt | 111 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +15.5) | — |
| [[SW1417 (line)]] | alt | 94.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +13.2) | — |
| [[SW48 (line)]] | wt | 57.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +9.5) | — |
| [[AN3 CA (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 84.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 51.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 62.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 73.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 74.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 493), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBCEL]] | +0.69 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[AASDHPPT]] | +0.67 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[MIER3]] | +0.66 | +0.76 / +0.40 | both halves | 4e-05 |  |
| [[UBXN2A]] | +0.65 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[TAB2]] | +0.65 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[NHLRC2]] | +0.64 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[THOC7]] | +0.62 | +0.63 / +0.42 | both halves | 4e-05 |  |
| [[ZFR]] | +0.62 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[C11orf58]] | +0.62 | +0.57 / +0.42 | both halves | 4e-05 |  |
| [[DDX6]] | +0.61 | +0.47 / +0.40 | both halves | 5e-05 |  |
| [[CILK1]] | +0.61 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[CFL2]] | +0.61 | +0.58 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHDDS]] | -0.69 | -0.67 / -0.63 | both halves | 7e-06 |  |
| [[DPM1]] | -0.61 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[P4HB]] | -0.61 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[NPHP4]] | -0.60 | -0.64 / -0.35 | both halves | 1e-04 |  |
| [[NDEL1]] | -0.60 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[SAR1A]] | -0.59 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[ENTPD7]] | -0.59 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[GP6-AS1]] | -0.59 | -0.61 / -0.41 | both halves | 4e-05 |  |
| [[QPCTL]] | -0.59 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[COPA]] | -0.58 | -0.66 / -0.48 | both halves | 2e-05 |  |
| [[TMEM104]] | -0.58 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[P3H1]] | -0.58 | -0.60 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PMP22]] | B | PMP22 activity lowers DCUN1D1's level | lines that do not express PMP22 (10) vs lines expressing it (40) | 1.38× higher at baseline in the lines without PMP22 | 0.017 | ⚠ within organs, on part of the lines; also absent: FKBP7, FAM216A, ARHGEF6; maybe low, not absent |
| [[MLPH]] | B | MLPH activity strengthens DCUN1D1's drug response | lines that do not express MLPH (13) vs lines expressing it (36) | the lines without MLPH respond 0.62× as strongly (z diff +1.37); strongest at Homoharringtonine 5 µM: 1.65x vs 2.84x (z diff +2.9) | 0.086 | ⚠ within organs, on part of the lines; also absent: GBP3, LGALS3, FBXO32; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.549). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-16.5, 6.3); signed map (15.3, -30.3). **Vector** length 96.5, 22.6% of its response variance represented; |z| ≥ 3 in 1,043 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +6.8 | +22.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.1 | +36.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.1 | +10.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.7 | +18.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.0 | +6.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.9 | +6.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.8 | +1.5 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.4 | +2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.4 | +3.4 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +2.3 | +1.5 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -6.0 | -3.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -5.3 | -3.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.7 | -2.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | -0.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.5 | -2.5 |
|  | [[EX229 (drug)]] 0.05 µM |  | -3.0 | -1.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -3.0 | -2.0 |
|  | [[EX229 (drug)]] 5 µM |  | -3.0 | -2.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.9 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | defective in cullin neddylation 1 domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q26.33 — chr3:182,938,074-182,985,953 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RP42, SCRO, DCUN1L1, Tes3, SCCRO |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 1 pathways, smallest: Neddylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96GG9](https://www.uniprot.org/uniprotkb/Q96GG9) (DCN1-like protein 1):

> Part of an E3 ubiquitin ligase complex for neddylation. Promotes neddylation of cullin components of E3 cullin-RING ubiquitin ligase complexes. Acts by binding to cullin-RBX1 complexes in the cytoplasm and promoting their nuclear translocation, enhancing recruitment of E2-NEDD8 (UBE2M-NEDD8) thioester to the complex, and optimizing the orientation of proteins in the complex to allow efficient transfer of NEDD8 from the E2 to the cullin substrates. Involved in the release of inhibitory effets of …

**Summary**, from NCBI Gene [54165](https://www.ncbi.nlm.nih.gov/gene/54165):

> Enables cullin family protein binding activity. Involved in positive regulation of protein neddylation and regulation of protein ubiquitination. Located in cytoplasm and nucleus. Part of ubiquitin ligase complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18184](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18184) · Entrez [54165](https://www.ncbi.nlm.nih.gov/gene/54165) · UniProt [Q96GG9](https://www.uniprot.org/uniprotkb/Q96GG9) · Ensembl [ENSG00000043093](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000043093)

## Data

Gene col 493: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 493); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 493, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 493]; `tensor/DDL_lfc|DDL_z.npy` [493]; `embed/gene_vectors.npy` [493]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 493 or target_col == 493). Every well: [[DCUN1D1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DCUN1D1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
