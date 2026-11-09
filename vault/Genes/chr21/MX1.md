---
symbol: "MX1"
type: "gene"
col: 8088
ensembl_id: "ENSG00000157601"
name: "MX dynamin like GTPase 1"
location: "21q22.3"
module: 32
arm: "+"
pooled_cpm: 133.37
n_lines_expressing: 31
n_dd_up: 31
n_dd_down: 70
n_dd_up_clean: 29
n_dd_down_clean: 56
in_vector_space: true
direction_upstream: 52
direction_downstream: 120
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# MX1

*MX dynamin like GTPase 1* — 21q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (2 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.92× (z +6.7, q 2e-08, up in 26 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 70 drug-doses (14 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.106× (z -23.6, q 0e+00, down in 28 of 29 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CMPK2]] (+0.96, fdr 7e-06), [[OAS2]] (+0.96, fdr 7e-06), [[PARP9]] (+0.95, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 52 arrows point to it, the strongest [[RASGRP3]] → it (grade B ⚠); 120 go from it, the strongest it → [[DDX60L]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8088.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.92×** | +6.7 | 2e-08 | 26/28 (HS-578T, Hs 766T, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.74×** | +5.9 | 1e-06 | 18/29 (NCI-H2347, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.47×** | +5.3 | 2e-05 | 26/29 (Hs 766T, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.67×** | +5.3 | 2e-05 | 24/29 (Hs 766T, HS-578T, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.59×** | +5.2 | 2e-05 | 24/30 (Hs 766T, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.61×** | +5.1 | 3e-05 | 24/28 (Hs 766T, RKO, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.47×** | +5.0 | 4e-05 | 24/29 (Hs 766T, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.36×** | +4.5 | 4e-04 | 26/30 (Hs 766T, CFPAC-1, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.41×** | +4.3 | 0.001 | 22/31 (CFPAC-1, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.46×** | +4.1 | 0.002 | 25/30 (LOX-IMVI, BT-474, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.45×** | +4.0 | 0.003 | 24/30 (Hs 766T, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[venetoclax (drug)]] 0.05 µM |  | **1.48×** | +3.9 | 0.004 | 26/30 (Panc 03.27, CFPAC-1, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 5 µM |  | **1.29×** | +3.9 | 0.004 | 20/29 (NCI-H2347, HS-578T, …) | rises with dose |  |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.43×** | +3.8 | 0.005 | 22/29 (SK-MEL-2, AsPC-1, …) | inconsistent across doses |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.45×** | +3.8 | 0.006 | 21/29 (Hs 766T, CFPAC-1, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.28×** | +3.8 | 0.006 | 20/29 (Hs 766T, CFPAC-1, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 70 in all, 14 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 70 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8088.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.106×** | -23.6 | 0e+00 | 28/29 (LoVo, SNU-423, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.222×** | -22.4 | 0e+00 | 29/30 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.121×** | -22.2 | 0e+00 | 29/29 (LoVo, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.124×** | -22.0 | 0e+00 | 29/29 (LoVo, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.268×** | -19.6 | 0e+00 | 28/30 (CFPAC-1, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.200×** | -16.9 | 0e+00 | 27/30 (SNU-423, A549, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.259×** | -14.2 | 5e-44 | 27/29 (LoVo, AsPC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.264×** | -14.0 | 7e-43 | 29/29 (SNU-423, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.392×** | -13.9 | 3e-42 | 27/29 (SNU-423, A549, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.271×** | -13.8 | 3e-41 | 27/29 (RKO, BT-474, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.282×** | -13.3 | 9e-39 | 27/30 (BT-474, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.300×** | -12.7 | 5e-35 | 28/29 (C-33 A, SNU-423, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.376×** | -10.3 | 4e-23 | 25/29 (LoVo, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.381×** | -10.1 | 1e-22 | 26/29 (A549, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.389×** | -9.5 | 6e-20 | 26/28 (LoVo, A549, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.529×** | -9.4 | 1e-19 | 25/30 (SNU-423, A549, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.412×** | -9.3 | 4e-19 | 25/29 (LoVo, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8088. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 242 | 0 | 28 (7 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0311× (z -25.4) |
| [[BT-474 (line)]] | alt | 116 | 0 | 27 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0309× (z -23.1) |
| [[A549 (line)]] | wt | 179 | 0 | 25 (7 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0269× (z -26.7) |
| [[LoVo (line)]] | wt | 558 | 0 | 24 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0243× (z -31.5) |
| [[SNU-423 (line)]] | alt | 289 | 0 | 23 (7 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0252× (z -27.9) |
| [[NCI-H1792 (line)]] | alt | 190 | 0 | 22 (5 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0487× (z -21.5) |
| [[RPMI-7951 (line)]] | alt | 281 | 3 (1 ⚠) | 19 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 10.1× (z +10.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.00× (z +9.5) | [[Belinostat (drug)]] 5 µM 0.0391× (z -27.7) |
| [[A498 (line)]] | wt | 412 | 0 | 21 (6 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0579× (z -22.8) |
| [[AsPC-1 (line)]] | alt | 151 | 0 | 20 (5 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0475× (z -18.8) |
| [[CFPAC-1 (line)]] | alt | 478 | 2 (1 ⚠) | 18 (5 ⚠) | [[Harringtonine (drug)]] 5 µM 3.21× (z +9.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.68× (z +8.5) | [[Tofacitinib (drug)]] 5 µM 0.116× (z -25.9) |
| [[NCI-H2347 (line)]] | alt | 324 | 3 (1 ⚠) | 17 (4 ⚠) | [[Harringtonine (drug)]] 5 µM 3.32× (z +11.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.08× (z +11.1) | [[Tofacitinib (drug)]] 5 µM 0.169× (z -24.6) |
| [[NCI-H1573 (line)]] | alt | 170 | 0 | 19 (4 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.133× (z -19.5) |
| [[NCI-H23 (line)]] | alt | 81.9 | 0 | 19 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0446× (z -17.0) |
| [[HepG2_C3A (line)]] | wt | 90.9 | 0 | 17 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0662× (z -15.9) ⚠ toxic · without an alert: [[Tofacitinib (drug)]] 5 µM 0.173× (z -15.1) |
| [[HS-578T (line)]] | alt | 84.6 | 3 | 14 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 5.76× (z +11.9) | [[Belinostat (drug)]] 5 µM 0.0768× (z -17.3) |
| [[CHP-212 (line)]] | wt | 118 | 0 | 14 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0380× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0444× (z -13.4) |
| [[COLO 205 (line)]] | alt | 681 | 0 | 13 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0400× (z -21.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0470× (z -20.6) |
| [[KATO III (line)]] | alt | 171 | 0 | 13 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0634× (z -19.5) |
| [[SW1417 (line)]] | alt | 96.5 | 0 | 13 | — | [[Belinostat (drug)]] 5 µM 0.136× (z -14.1) |
| [[Hs 766T (line)]] | wt | 124 | 0 | 12 | — | [[Tofacitinib (drug)]] 5 µM 0.178× (z -15.9) |
| [[Panc 03.27 (line)]] | alt | 320 | 0 | 11 | — | [[Tofacitinib (drug)]] 5 µM 0.211× (z -16.7) |
| [[SW 900 (line)]] | alt | 122 | 0 | 7 | — | [[Belinostat (drug)]] 5 µM 0.0824× (z -13.6) |
| [[C-33 A (line)]] | alt | 52.3 | 0 | 6 | — | [[Belinostat (drug)]] 0.5 µM 0.0263× (z -15.6) |
| [[SK-MEL-2 (line)]] | alt | 55.0 | 0 | 6 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.224× (z -11.0) |
| [[J82 (line)]] | alt | 71.3 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 11.8× (z +15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | [[Tofacitinib (drug)]] 5 µM 0.305× (z -10.6) |
| [[LOX-IMVI (line)]] | wt | 43.3 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0848× (z -11.7) |
| [[LS 180 (line)]] | wt | 33.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.62× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | [[Belinostat (drug)]] 5 µM 0.275× (z -8.9) |
| [[A-172 (line)]] | wt | 28.5 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 8.97 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 19.0 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 11.9 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 15.4 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.9 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 18.9 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 25.0 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.7 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.0 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 18.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 90.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.1 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 84.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.1 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 33.3 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 13.0 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 13.2 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.0 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 22.8 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 15.3 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8088), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CMPK2]] | +0.96 | +0.92 / +0.97 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 811 |
| [[OAS2]] | +0.96 | +0.94 / +0.96 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 978 |
| [[PARP9]] | +0.95 | +0.90 / +0.96 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 847 |
| [[OAS1]] | +0.94 | +0.90 / +0.95 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 985 |
| [[IFIT1]] | +0.93 | +0.90 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 989 |
| [[IFI44]] | +0.93 | +0.89 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 967 |
| [[XAF1]] | +0.93 | +0.84 / +0.95 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 925 |
| [[PLSCR1]] | +0.93 | +0.86 / +0.95 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 661 |
| [[IFIT3]] | +0.92 | +0.90 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 972 |
| [[OAS3]] | +0.92 | +0.89 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 967 |
| [[IFI44L]] | +0.92 | +0.85 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 965 |
| [[STAT1]] | +0.92 | +0.88 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 942 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*52 arrows, 52 of them with an alert ⚠; grade A 0, B 41, C 11. Shown: the 12 strongest; 40 more arrows (40 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RASGRP3]] | B | RASGRP3 activity raises MX1's level | lines that do not express RASGRP3 (16) vs lines expressing it (34) | 4.11× lower at baseline in the lines without RASGRP3 | 0.003 | ⚠ within organs, on part of the lines; also absent: IFI6, SLC15A3, GBP4; maybe low, not absent |
| [[GBP4]] | B | GBP4 activity raises MX1's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 3.44× lower at baseline in the lines without GBP4 | 0.004 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[SAMD9L]] | B | SAMD9L activity raises MX1's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 3.07× lower at baseline in the lines without SAMD9L | 0.005 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |
| [[SLC15A3]] | B | SLC15A3 activity raises MX1's level | lines that do not express SLC15A3 (16) vs lines expressing it (34) | 3.57× lower at baseline in the lines without SLC15A3 | 0.006 | ⚠ within organs, on part of the lines; also absent: XAF1, MX2, GBP4 |
| [[IFI44]] | B | IFI44 activity raises MX1's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 3.60× lower at baseline in the lines without IFI44 | 0.007 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |
| [[ETV7]] | B | ETV7 activity raises MX1's level | lines that do not express ETV7 (13) vs lines expressing it (37) | 3.15× lower at baseline in the lines without ETV7 | 0.007 | ⚠ within organs, on part of the lines; also absent: TUBA4A, AGMAT, ANO9; maybe low, not absent |
| [[CD5L]] | B | CD5L activity raises MX1's level | lines that do not express CD5L (23) vs lines expressing it (27) | 3.15× lower at baseline in the lines without CD5L | 0.009 | ⚠ within organs, on part of the lines; also absent: GBP4, TRIM22, GBP5; maybe low, not absent |
| [[CMPK2]] | B | CMPK2 activity raises MX1's level | lines that do not express CMPK2 (11) vs lines expressing it (39) | 3.35× lower at baseline in the lines without CMPK2 | 0.013 | ⚠ within organs, on part of the lines; also absent: OAS2, NRIR, OAS1 |
| [[GBP1]] | B | GBP1 activity raises MX1's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 3.02× lower at baseline in the lines without GBP1 | 0.016 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[CYP2J2]] | B | CYP2J2 activity raises MX1's level | lines that do not express CYP2J2 (12) vs lines expressing it (38) | 4.45× lower at baseline in the lines without CYP2J2 | 0.019 | ⚠ within organs, on part of the lines; also absent: CDK18 |
| [[PLSCR1]] | B | PLSCR1 activity raises MX1's level | lines that do not express PLSCR1 (8) vs lines expressing it (42) | 3.98× lower at baseline in the lines without PLSCR1 | 0.020 | ⚠ within organs, on part of the lines; also absent: PARP9, ENSG00000279320, IFI6; maybe low, not absent |
| [[MMP13]] | B | MMP13 activity raises MX1's level | lines that do not express MMP13 (30) vs lines expressing it (20) | 2.37× lower at baseline in the lines without MMP13 | 0.021 | ⚠ within organs, on part of the lines; also absent: SOX11, AGT, STEAP4 |

### Downstream of this gene

*120 arrows, 120 of them with an alert ⚠; grade A 0, B 108, C 12. Shown: the 12 strongest; 108 more arrows (108 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DDX60L]] | B | MX1 activity raises DDX60L's level | lines that do not express MX1 (19) vs lines expressing it (31) | 2.89× lower at baseline in the lines without MX1 | 6e-04 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[PML]] | B | MX1 activity raises PML's level | lines that do not express MX1 (19) vs lines expressing it (31) | 1.88× lower at baseline in the lines without MX1 | 7e-04 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[PARP14]] | B | MX1 activity raises PARP14's level | lines that do not express MX1 (19) vs lines expressing it (31) | 2.34× lower at baseline in the lines without MX1 | 7e-04 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[HERC6]] | B | MX1 activity raises HERC6's level | lines that do not express MX1 (19) vs lines expressing it (31) | 2.37× lower at baseline in the lines without MX1 | 0.001 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[PARP12]] | B | MX1 activity raises PARP12's level | lines that do not express MX1 (19) vs lines expressing it (31) | 2.32× lower at baseline in the lines without MX1 | 0.001 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[GBP3]] | B | MX1 activity raises GBP3's level | lines that do not express MX1 (19) vs lines expressing it (31) | 2.95× lower at baseline in the lines without MX1 | 0.001 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[STAT2]] | B | MX1 activity raises STAT2's level | lines that do not express MX1 (19) vs lines expressing it (31) | 1.70× lower at baseline in the lines without MX1 | 0.001 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[CMPK2]] | B | MX1 activity raises CMPK2's level | lines that do not express MX1 (19) vs lines expressing it (31) | 3.04× lower at baseline in the lines without MX1 | 0.001 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[PLSCR1]] | B | MX1 activity raises PLSCR1's level | lines that do not express MX1 (19) vs lines expressing it (31) | 2.77× lower at baseline in the lines without MX1 | 0.002 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[HELZ2]] | B | MX1 activity raises HELZ2's level | lines that do not express MX1 (19) vs lines expressing it (31) | 2.34× lower at baseline in the lines without MX1 | 0.002 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[SAMD9L]] | B | MX1 activity raises SAMD9L's level | lines that do not express MX1 (19) vs lines expressing it (31) | 2.86× lower at baseline in the lines without MX1 | 0.003 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[ODF3B]] | B | MX1 activity raises ODF3B's level | lines that do not express MX1 (19) vs lines expressing it (31) | 2.06× lower at baseline in the lines without MX1 | 0.003 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.957). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.6, 53.8); signed map (64.9, 31.7). **Vector** length 156, 61.6% of its response variance represented; |z| ≥ 3 in 1,647 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Interferon gamma signaling* (reactome, mean cos +0.80 to 17); *Modulation of host responses by IFN-stimulated genes* (reactome, mean cos +0.84 to 10); *IFIT antiviral response* (reactome, mean cos +0.91 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +9.2 | +5.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.5 | +3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +6.0 | +6.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +5.3 | -3.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +5.0 | +3.1 |
|  | [[Docetaxel (drug)]] 5 µM |  | +4.2 | +3.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.2 | +0.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.1 | +5.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.0 | +5.2 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -11.4 | -22.4 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -10.1 | -19.6 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -9.6 | -13.8 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -9.0 | -13.3 |
|  | [[Selinexor (drug)]] 5 µM |  | -8.5 | -13.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -8.0 | -16.9 |

## What is on record

|  |  |
|---|---|
| Name | MX dynamin like GTPase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.3 — chr21:41,420,020-41,470,071 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IFI-78K, MxA, lncMX1-215 |
| Gene groups (HGNC) | MX dynamin like GTPase family |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, KRAS_SIGNALING_DN, INTERFERON_GAMMA_RESPONSE |
| Reactome | 5 pathways, smallest: Interferon alpha/beta signaling; ISG15 antiviral mechanism; Antimicrobial mechanism of IFN-stimulated genes |
| Matched by | ensembl_id |

**Function**, from UniProt [P20591](https://www.uniprot.org/uniprotkb/P20591) (Interferon-induced GTP-binding protein Mx1):

> Interferon-induced dynamin-like GTPase with antiviral activity against a wide range of RNA viruses and some DNA viruses. Its target viruses include negative-stranded RNA viruses and HBV through binding and inactivation of their ribonucleocapsid. May also antagonize reoviridae and asfarviridae replication. Inhibits thogoto virus (THOV) replication by preventing the nuclear import of viral nucleocapsids. Inhibits La Crosse virus (LACV) replication by sequestering viral nucleoprotein in …

**Summary**, from NCBI Gene [4599](https://www.ncbi.nlm.nih.gov/gene/4599):

> This gene encodes a guanosine triphosphate (GTP)-metabolizing protein that participates in the cellular antiviral response. The encoded protein is induced by type I and type II interferons and antagonizes the replication process of several different RNA and DNA viruses. There is a related gene located adjacent to this gene on chromosome 21, and there are multiple pseudogenes located in a cluster on chromosome 4. Alternative splicing results in multiple transcript variants. [provided by RefSeq, …

**Accessions** — [HGNC:7532](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7532) · Entrez [4599](https://www.ncbi.nlm.nih.gov/gene/4599) · UniProt [P20591](https://www.uniprot.org/uniprotkb/P20591) · Ensembl [ENSG00000157601](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157601)

## Data

Gene col 8088: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8088); `tables/drug_effects.parquet` (101 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8088, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8088]; `tensor/DDL_lfc|DDL_z.npy` [8088]; `embed/gene_vectors.npy` [8088]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8088 or target_col == 8088). Every well: [[MX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
