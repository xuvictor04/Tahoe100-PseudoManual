---
symbol: "C7orf50"
type: "gene"
col: 7103
ensembl_id: "ENSG00000146540"
name: "cholesin"
location: "7p22.3"
module: 4
arm: "+"
pooled_cpm: 67.59
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 2
n_dd_up_clean: 14
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# C7orf50

*cholesin* — 7p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.92× (z +17.3, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.819× (z -7.4, q 5e-11, down in 24 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (AN3 CA 0.194×, BT-474 0.387×, A498 0.531×, MIA PaCa-2 0.538×; ⚠ cell-cycle shift, explains ~67% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (A-427 0.176×, SK-MEL-2 0.185×, SHP-77 0.439×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (MIA PaCa-2 0.250×, A-427 0.293×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.413×, KATO III 0.514×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.587×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EIPR1]] (+0.65, fdr 7e-06), [[CHCHD6]] (+0.65, fdr 1e-05), [[NUDCD3]] (+0.64, fdr 1e-05); moves opposite to [[TAPT1]] (-0.58, fdr 7e-05), [[RSRP1]] (-0.52, fdr 3e-05), [[TXNDC16]] (-0.51, fdr 1e-04).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7103.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.92×** | +17.3 | 0e+00 | 47/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.80×** | +15.5 | 0e+00 | 45/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.78×** | +15.1 | 0e+00 | 46/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.61×** | +12.6 | 5e-34 | 38/48 (HEC-1-A, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.53×** | +11.2 | 4e-27 | 33/49 (PANC-1, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.41×** | +9.1 | 8e-18 | 38/48 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM |  | **1.40×** | +8.9 | 6e-17 | 41/48 (NCI-H1792, HT-29, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.26×** | +8.6 | 6e-16 | 28/48 (NCI-H1792, NCI-H1573, …) | all doses, flat | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.37×** | +8.3 | 5e-15 | 32/48 (NCI-H1792, A549, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.30×** | +6.9 | 3e-10 | 33/48 (HT-29, NCI-H1792, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | **1.29×** | +6.3 | 2e-08 | 24/45 (Hs 766T, HEC-1-A, …) | all doses, flat | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.28×** | +6.2 | 3e-08 | 27/48 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.23×** | +5.5 | 1e-06 | 23/48 (LoVo, NCI-H1792, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~13% of this change | 1.20× | +4.8 | 8e-05 | 20/48 (KATO III, SW480, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.20× | +4.4 | 5e-04 | 14/47 (A-427, SNU-423, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-733 (drug)]] 5 µM |  | **1.30×** | +3.6 | 0.009 | 8/48 (NCI-H1792, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.018 | 15/48 (NCI-H1792, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.027 | 9/48 (NCI-H1792, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.028 | 12/49 (KATO III, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 0.5 µM |  | 1.13× | +3.1 | 0.039 | 4/48 (Panc 03.27, HS-578T, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7103.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (AN3 CA 0.194×, BT-474 0.387×, A498 0.531×, MIA PaCa-2 0.538×; ⚠ cell-cycle shift, explains ~67% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (A-427 0.176×, SK-MEL-2 0.185×, SHP-77 0.439×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (MIA PaCa-2 0.250×, A-427 0.293×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.413×, KATO III 0.514×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.587×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.819×** | -7.4 | 5e-11 | 24/48 (MIA PaCa-2, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | 0.869× | -5.2 | 4e-05 | 20/48 (AN3 CA, BT-474, …) | top dose only | composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **0.706×** | -4.8 | 3e-04 | 19/49 (LoVo, HT-29, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 0.875× | -3.5 | 0.058 | 17/48 (KATO III, SW48, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.962× | -3.4 | 0.086 | 2/49 (NCI-H661, NCI-H2122) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.919× | -3.1 | 0.16 | 6/48 (LS 180, NCI-H2030, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7103. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 79.9 | 9 (5 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.03× (z +10.3) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.59× (z +9.8) | — |
| [[A-427 (line)]] | wt | 67.9 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.176× (z -20.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.587× (z -9.2) |
| [[HT-29 (line)]] | alt | 60.6 | 4 | 0 | [[Auranofin (drug)]] 5 µM 2.97× (z +11.4) | — |
| [[KATO III (line)]] | alt | 101 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 2.85× (z +13.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.514× (z -12.4) |
| [[MIA PaCa-2 (line)]] | alt | 91.4 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.250× (z -18.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -16.7) |
| [[SW480 (line)]] | alt | 74.6 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.10× (z +17.1) | — |
| [[BT-474 (line)]] | alt | 109 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.73× (z +11.5) | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -15.2) ⚠ cell-cycle shift, explains ~67% of this change |
| [[H4 (line)]] | wt | 105 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.73× (z +9.4) | — |
| [[SHP-77 (line)]] | alt | 152 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.92× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.297× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[SK-MEL-2 (line)]] | alt | 72.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[AN3 CA (line)]] | alt | 97.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -15.4) ⚠ cell-cycle shift, explains ~67% of this change |
| [[AsPC-1 (line)]] | alt | 41.5 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.16× (z +9.8) | — |
| [[COLO 205 (line)]] | alt | 51.1 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.43× (z +9.6) | — |
| [[HEC-1-A (line)]] | alt | 70.4 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.05× (z +14.5) | — |
| [[NCI-H23 (line)]] | alt | 111 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.03× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.438× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[NCI-H460 (line)]] | wt | 67.1 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.10× (z +10.0) | — |
| [[SNU-423 (line)]] | alt | 52.7 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.48× (z +9.4) | — |
| [[A-172 (line)]] | wt | 67.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.44× (z +13.6) | — |
| [[A498 (line)]] | wt | 96.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.531× (z -12.9) ⚠ cell-cycle shift, explains ~67% of this change |
| [[C32 (line)]] | wt | 40.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.25× (z +9.9) | — |
| [[HOP62 (line)]] | alt | 47.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.17× (z +8.5) | — |
| [[LoVo (line)]] | wt | 76.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.24× (z +10.4) | — |
| [[NCI-H2030 (line)]] | alt | 56.1 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.195× (z -10.0) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 89.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.81× (z +9.0) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 57.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +8.5) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 56.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 76.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 67.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 70.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 48.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 46.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 76.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 34.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 44.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 73.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 53.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 70.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 74.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 72.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 93.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7103), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIPR1]] | +0.65 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[CHCHD6]] | +0.65 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[NUDCD3]] | +0.64 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[MYBBP1A]] | +0.62 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[RBM28]] | +0.62 | +0.46 / +0.64 | both halves | 2e-05 | STRING 468 |
| [[POLR1A]] | +0.60 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[DIS3L2]] | +0.60 | +0.56 / +0.58 | both halves | 1e-05 | same gene group |
| [[NOL10]] | +0.60 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[POLR3H]] | +0.60 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[RAD54L2]] | +0.58 | +0.36 / +0.65 | both halves | 1e-04 |  |
| [[LSG1]] | +0.58 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[RRP1B]] | +0.58 | +0.49 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAPT1]] | -0.58 | -0.37 / -0.52 | both halves | 7e-05 |  |
| [[RSRP1]] | -0.52 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[TXNDC16]] | -0.51 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[CDKN2C]] | -0.51 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[PRDM2]] | -0.50 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[FOXC1]] | -0.48 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[SYNJ1]] | -0.48 | -0.32 / -0.49 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.542). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-9.7, -34.7); signed map (-12.1, -50.6). **Vector** length 101, 24.0% of its response variance represented; |z| ≥ 3 in 1,045 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | +6.9 | +8.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.5 | +9.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.9 | +12.6 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +5.9 | +8.3 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +4.9 | +8.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.1 | +6.2 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.5 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +5.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.4 | +3.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.6 | -7.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.3 | -2.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.8 | -1.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -5.1 | -3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.0 | -3.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.0 | -2.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.7 | -2.0 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -1.5 | -1.8 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.5 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | cholesin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p22.3 — chr7:996,986-1,138,260 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC11257, YCR016W; previously C7orf50 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BRJ6](https://www.uniprot.org/uniprotkb/Q9BRJ6) (Protein cholesin):

> Hormone secreted from the intestine in response to cholesterol, where it acts to inhibit cholesterol synthesis in the liver and VLDL secretion,leading to a reduction in circulating cholesterol levels. Acts through binding to its receptor, GPR146.

**Summary**, from NCBI Gene [84310](https://www.ncbi.nlm.nih.gov/gene/84310):

> Enables hormone activity. Involved in negative regulation of cholesterol biosynthetic process. Is active in obsolete extracellular space. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:22421](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22421) · Entrez [84310](https://www.ncbi.nlm.nih.gov/gene/84310) · UniProt [Q9BRJ6](https://www.uniprot.org/uniprotkb/Q9BRJ6) · Ensembl [ENSG00000146540](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146540)

## Data

Gene col 7103: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7103); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7103, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7103]; `tensor/DDL_lfc|DDL_z.npy` [7103]; `embed/gene_vectors.npy` [7103]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7103 or target_col == 7103). Every well: [[C7orf50 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C7orf50.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
