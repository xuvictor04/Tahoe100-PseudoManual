---
symbol: "MYO19"
type: "gene"
col: 15906
ensembl_id: "ENSG00000278259"
name: "myosin XIX"
location: "17q12"
module: 6
arm: "+"
pooled_cpm: 94.52
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 23
n_dd_up_clean: 3
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# MYO19

*myosin XIX* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.49× (z +9.3, q 7e-18, up in 39 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[c-Kit-IN-1 (drug)]] 5 µM: 1.54× (z +5.3, q 3e-05, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (5 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.526× (z -14.5, q 6e-45, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FANCA]] (+0.72, fdr 7e-06), [[FANCC]] (+0.71, fdr 7e-06), [[DNA2]] (+0.70, fdr 7e-06); moves opposite to [[BROX]] (-0.58, fdr 1e-05), [[VWA5A]] (-0.58, fdr 1e-05), [[WBP2]] (-0.58, fdr 2e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TERT]] → it (grade B ⚠); 1 goes from it, the strongest it → [[MPP3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15906.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.49×** | +9.3 | 7e-18 | 39/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.54×** | +5.3 | 3e-05 | 31/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.48×** | +4.8 | 2e-04 | 25/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.48×** | +4.8 | 2e-04 | 26/48 (MIA PaCa-2, SNU-1, …) | rises with dose | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +4.3 | 0.002 | 13/48 (NCI-H2347, CFPAC-1, …) | top dose only |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.20×** | +4.2 | 0.003 | 18/48 (SW480, LoVo, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | 1.13× | +4.0 | 0.005 | 21/49 (NCI-H1792, HT-29, …) | top dose only |  |
| [[TAK-733 (drug)]] 0.05 µM |  | 1.18× | +3.7 | 0.013 | 18/48 (PANC-1, NCI-H23, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.14× | +3.0 | 0.15 | 19/48 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15906.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.526×** | -14.5 | 6e-45 | 40/48 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.655×** | -14.1 | 1e-42 | 34/48 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.703×** | -11.7 | 2e-29 | 38/48 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.689×** | -8.8 | 3e-16 | 32/48 (A549, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.512×** | -8.2 | 2e-14 | 35/49 (MIA PaCa-2, SHP-77, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.707×** | -8.2 | 3e-14 | 32/48 (HEC-1-A, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.764×** | -6.3 | 2e-08 | 26/48 (SK-MEL-2, A-172, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.781×** | -5.8 | 5e-07 | 24/48 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.625×** | -5.8 | 5e-07 | 30/48 (C32, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.790×** | -5.5 | 2e-06 | 27/48 (LOX-IMVI, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~25% of this change | **0.811×** | -4.9 | 4e-05 | 20/48 (A-172, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.806×** | -4.8 | 8e-05 | 23/48 (LS 180, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.822×** | -4.6 | 2e-04 | 21/48 (A-427, C32, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.688×** | -4.6 | 2e-04 | 25/47 (H4, A-427, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.817×** | -4.6 | 2e-04 | 21/44 (hTERT-HPNE, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **0.818×** | -4.6 | 2e-04 | 20/47 (LOX-IMVI, NCI-H23, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.780×** | -4.2 | 1e-03 | 21/47 (Hs 766T, H4, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.844× | -4.0 | 0.002 | 18/48 (A549, J82, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.845× | -4.0 | 0.002 | 15/49 (HEC-1-A, AsPC-1, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15906. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 164 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.307× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.482× (z -13.9) |
| [[MIA PaCa-2 (line)]] | alt | 101 | 1 (1 ⚠) | 6 (3 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.35× (z +10.5) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 0.5 µM 0.351× (z -12.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.442× (z -9.6) |
| [[A-427 (line)]] | wt | 151 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -15.9) |
| [[HS-578T (line)]] | alt | 101 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.308× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.360× (z -11.2) |
| [[A549 (line)]] | wt | 110 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -19.3) |
| [[HEC-1-A (line)]] | alt | 148 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -18.4) |
| [[A498 (line)]] | wt | 115 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -21.0) |
| [[A-172 (line)]] | wt | 106 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.423× (z -10.5) |
| [[BT-474 (line)]] | alt | 146 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -15.3) |
| [[C32 (line)]] | wt | 59.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -12.2) |
| [[HOP62 (line)]] | alt | 97.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -12.8) |
| [[NCI-H460 (line)]] | wt | 95.2 | 1 (1 ⚠) | 2 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.27× (z +13.1) ⚠ unreliable plate only | [[Selinexor (drug)]] 5 µM 0.612× (z -11.0) |
| [[RKO (line)]] | wt | 93.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -12.5) |
| [[SW1417 (line)]] | alt | 73.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -15.9) |
| [[NCI-H2030 (line)]] | alt | 190 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.379× (z -11.5) |
| [[Panc 03.27 (line)]] | alt | 87.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -15.4) |
| [[SHP-77 (line)]] | alt | 128 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.380× (z -12.3) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 77.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -17.6) |
| [[AsPC-1 (line)]] | alt | 64.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -12.4) |
| [[C-33 A (line)]] | alt | 120 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.311× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 65.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.145× (z -15.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 83.1 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.566× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 93.5 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.529× (z -11.2) |
| [[LS 180 (line)]] | wt | 59.0 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.422× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 75.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.415× (z -10.4) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 53.7 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +9.7) ⚠ cell-cycle shift, explains ~81% of this change | — |
| [[NCI-H23 (line)]] | alt | 148 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.432× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 77.4 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.393× (z -12.9) |
| [[RPMI-7951 (line)]] | alt | 77.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.327× (z -10.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 126 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.397× (z -10.9) |
| [[SW 1271 (line)]] | alt | 94.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.142× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 90.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.486× (z -13.3) |
| [[AN3 CA (line)]] | alt | 62.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 47.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 76.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 89.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 94.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 62.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 51.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 85.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 78.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 72.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 71.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 75.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 78.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 67.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 73.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 97.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15906), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FANCA]] | +0.72 | +0.70 / +0.77 | both halves | 7e-06 |  |
| [[FANCC]] | +0.71 | +0.66 / +0.76 | both halves | 7e-06 |  |
| [[DNA2]] | +0.70 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[XRCC3]] | +0.69 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[TOMM40]] | +0.68 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[TOP3A]] | +0.67 | +0.60 / +0.74 | both halves | 7e-06 |  |
| [[UHRF1]] | +0.67 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[RAD51]] | +0.67 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[CDC45]] | +0.66 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[WDR4]] | +0.65 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[DGCR8]] | +0.65 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[ATAD3B]] | +0.65 | +0.68 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BROX]] | -0.58 | -0.52 / -0.64 | both halves | 1e-05 |  |
| [[VWA5A]] | -0.58 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[WBP2]] | -0.58 | -0.47 / -0.62 | both halves | 2e-05 |  |
| [[MAT2B]] | -0.57 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[ETFRF1]] | -0.57 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[SECISBP2L]] | -0.57 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[OAZ2]] | -0.56 | -0.54 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TERT]] | B | TERT activity raises MYO19's level | lines that do not express TERT (13) vs lines expressing it (37) | 1.34× lower at baseline in the lines without TERT | 0.022 | ⚠ within organs, on part of the lines; also absent: SAMD11, MIR1915HG, LNC-LBCS |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MPP3]] | C | MYO19's natural level strengthens MPP3's drug response | MYO19's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.36; direction not clear | 0.078 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.624). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-31.6, -47.1); signed map (-35.4, -44.5). **Vector** length 137, 42.2% of its response variance represented; |z| ≥ 3 in 1,297 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DNA strand elongation* (reactome, mean cos +0.51 to 28); *DNA Replication* (reactome, mean cos +0.52 to 40); *E2F G1/S* (control, mean cos +0.51 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +9.7 | +9.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | +6.7 | +4.0 |
|  | [[EX229 (drug)]] 5 µM |  | +6.0 | +4.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +5.9 | +5.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | +5.5 | +4.8 |
|  | [[venetoclax (drug)]] 5 µM |  | +4.4 | +2.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +3.9 | +2.9 |
| fall | [[Selinexor (drug)]] 5 µM |  | -9.5 | -11.7 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -6.0 | -5.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.8 | -14.5 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -5.1 | -4.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.0 | -8.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.1 | -4.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.8 | -3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.7 | -4.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.7 | -3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.6 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | myosin XIX |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q12 — chr17:36,495,636-36,543,435 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22865; previously MYOHD1 |
| Gene groups (HGNC) | Myosin heavy chains, class XIX |
| Reactome | 4 pathways, smallest: RHOT1 GTPase cycle; RHOT2 GTPase cycle; Miro GTPase Cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96H55](https://www.uniprot.org/uniprotkb/Q96H55) (Unconventional myosin-XIX):

> Actin-based motor molecule with ATPase activity that localizes to the mitochondrion outer membrane. Motor protein that moves towards the plus-end of actin filaments (By similarity). Required for mitochondrial inheritance during mitosis. May be involved in mitochondrial transport or positioning.

**Summary**, from NCBI Gene [80179](https://www.ncbi.nlm.nih.gov/gene/80179):

> Enables ATP hydrolysis activity and actin binding activity. Involved in regulation of cytokinesis and regulation of mitochondrial fission. Acts upstream of or within mitochondrion migration along actin filament. Located in cytosol and mitochondrial outer membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26234](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26234) · Entrez [80179](https://www.ncbi.nlm.nih.gov/gene/80179) · UniProt [Q96H55](https://www.uniprot.org/uniprotkb/Q96H55) · Ensembl [ENSG00000278259](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000278259)

## Data

Gene col 15906: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15906); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15906, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15906]; `tensor/DDL_lfc|DDL_z.npy` [15906]; `embed/gene_vectors.npy` [15906]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15906 or target_col == 15906). Every well: [[MYO19 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYO19.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
