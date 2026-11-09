---
symbol: "NCBP2"
type: "gene"
col: 3560
ensembl_id: "ENSG00000114503"
name: "nuclear cap binding protein subunit 2"
location: "3q29"
module: 1
arm: "+"
pooled_cpm: 70.05
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 1
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# NCBP2

*nuclear cap binding protein subunit 2* — 3q29

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.43× (z +13.9, q 3e-41, up in 47 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.69× (z +8.2, q 3e-14, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.863× (z -7.9, q 2e-12, down in 9 of 49 measured lines) ⚠ position not correctable.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 2 lines (MIA PaCa-2 0.720×, HOP62 0.778×; ⚠ position not correctable); [[Thymol (drug)]] 0.5 µM in 1 line (SW 1271 0.0953×); [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.514×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDX18]] (+0.65, fdr 1e-05), [[PNO1]] (+0.64, fdr 1e-05), [[MYSM1]] (+0.61, fdr 1e-05); moves opposite to [[ELF2]] (-0.64, fdr 7e-06), [[MARCHF6]] (-0.61, fdr 1e-05), [[KDM6A]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TP53]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3560.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.43×** | +13.9 | 3e-41 | 47/49 (A-172, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.32×** | +12.7 | 3e-34 | 41/43 (A498, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.19×** | +11.8 | 8e-30 | 47/47 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.82×** | +8.6 | 1e-15 | 39/45 (NCI-H1573, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.69×** | +8.2 | 3e-14 | 38/48 (SK-MEL-2, RPMI-7951, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.60×** | +7.4 | 1e-11 | 42/48 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.52×** | +6.3 | 2e-08 | 32/48 (SK-MEL-2, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.47×** | +6.0 | 1e-07 | 36/48 (PANC-1, LOX-IMVI, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.46×** | +6.0 | 1e-07 | 37/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.43×** | +5.6 | 1e-06 | 32/48 (CFPAC-1, HOP62, …) | all doses, flat |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.93×** | +5.4 | 3e-06 | 39/48 (MIA PaCa-2, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~60% of this change | **1.36×** | +4.8 | 8e-05 | 34/48 (A-172, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.33×** | +4.5 | 3e-04 | 28/48 (A-172, SNU-423, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.28×** | +3.8 | 0.005 | 28/48 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.27×** | +3.7 | 0.007 | 26/48 (PANC-1, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.29×** | +3.7 | 0.008 | 25/47 (LOX-IMVI, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +3.6 | 0.009 | 18/48 (A-172, HOP62, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.55×** | +3.6 | 0.009 | 24/48 (PANC-1, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.38×** | +3.5 | 0.014 | 25/48 (MIA PaCa-2, HEC-1-A, …) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.34×** | +3.2 | 0.037 | 20/48 (NCI-H1792, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **1.23×** | +3.1 | 0.052 | 19/48 (MIA PaCa-2, PANC-1, …) | top dose only | position effect removed |
| [[Belzutifan (drug)]] 5 µM |  | **1.42×** | +2.9 | 0.090 | 18/46 (NCI-H2030, PANC-1, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3560.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 2 lines (MIA PaCa-2 0.720×, HOP62 0.778×; ⚠ position not correctable); [[Thymol (drug)]] 0.5 µM in 1 line (SW 1271 0.0953×); [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.514×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.863× | -7.9 | 2e-12 | 9/49 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.780×** | -3.7 | 0.053 | 24/47 (NCI-H2030, CHP-212, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.860× | -3.2 | 0.17 | 15/48 (C-33 A, A-427, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | 0.675× | -3.2 | 0.17 | 18/50 (NCI-H596, AsPC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 0.789× | -3.2 | 0.17 | 20/50 (A-427, C-33 A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Folic acid (drug)]] 5 µM |  | 0.870× | -3.1 | 0.19 | 12/48 (Hs 766T, Panc 03.27, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3560. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 51.8 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.60× (z +14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[PANC-1 (line)]] | alt | 119 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.47× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 2.20× (z +9.9) | — |
| [[LOX-IMVI (line)]] | wt | 60.1 | 4 (3 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.15× (z +12.3) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.05× (z +10.1) | — |
| [[A498 (line)]] | wt | 53.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[CFPAC-1 (line)]] | alt | 57.5 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.68× (z +10.2) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[HS-578T (line)]] | alt | 65.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.59× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H1573 (line)]] | alt | 60.8 | 3 (3 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 5.41× (z +15.4) ⚠ toxic | — |
| [[SW480 (line)]] | alt | 113 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[HOP62 (line)]] | alt | 54.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[HT-29 (line)]] | alt | 71.0 | 2 (2 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.95× (z +11.0) ⚠ toxic | — |
| [[MIA PaCa-2 (line)]] | alt | 97.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H1792 (line)]] | alt | 46.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H2347 (line)]] | alt | 85.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H460 (line)]] | wt | 48.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.81× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 99.5 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.41× (z +9.2) | — |
| [[SNU-423 (line)]] | alt | 51.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.00× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[A-427 (line)]] | wt | 64.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.89× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[A549 (line)]] | wt | 41.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.48× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[AsPC-1 (line)]] | alt | 45.9 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.27× (z +9.4) ⚠ toxic | — |
| [[C-33 A (line)]] | alt | 56.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.43× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[C32 (line)]] | wt | 44.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.77× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[HEC-1-A (line)]] | alt | 84.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.33× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[Hs 766T (line)]] | wt | 44.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.00× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[KATO III (line)]] | alt | 91.4 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.57× (z +14.0) ⚠ toxic | — |
| [[LoVo (line)]] | wt | 48.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.78× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[Panc 03.27 (line)]] | alt | 92.6 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.62× (z +9.3) ⚠ toxic | — |
| [[RKO (line)]] | wt | 89.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.514× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 77.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[SW 1271 (line)]] | alt | 70.8 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0953× (z -8.7) |
| [[SW1417 (line)]] | alt | 96.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.29× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[AN3 CA (line)]] | alt | 72.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 58.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 88.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 84.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 66.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 70.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 54.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 97.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 66.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 64.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 69.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 103 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3560), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX18]] | +0.65 | +0.69 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[PNO1]] | +0.64 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[MYSM1]] | +0.61 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[RBAK]] | +0.60 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[THUMPD3]] | +0.60 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[ZNF121]] | +0.59 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[RPL7L1]] | +0.59 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[MAK16]] | +0.58 | +0.58 / +0.55 | both halves | 1e-05 | same gene group |
| [[MGA]] | +0.56 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[ZNF770]] | +0.56 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[ZNF146]] | +0.56 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[UBE2V2]] | +0.56 | +0.61 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELF2]] | -0.64 | -0.63 / -0.59 | both halves | 7e-06 |  |
| [[MARCHF6]] | -0.61 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[KDM6A]] | -0.57 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[RHEB]] | -0.55 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[TBC1D12]] | -0.55 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[HSF2]] | -0.55 | -0.46 / -0.48 | both halves | 2e-05 |  |
| [[SNX1]] | -0.54 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[PIAS1]] | -0.54 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[SEC11A]] | -0.54 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[RHEBL1]] | -0.54 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[LRRFIP2]] | -0.54 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[USP33]] | -0.53 | -0.48 / -0.47 | both halves | 2e-05 | pathway: Regulation of expression of SLITs and ROBOs |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TP53]] | C | TP53 activity weakens NCBP2's drug response | recorded loss-of-function mutation of TP53 in 32 lines vs 17 not recorded | the TP53-altered lines respond 1.16× as strongly (z diff -1.03); strongest at Dinaciclib 0.05 µM: 1.92x vs 1.57x (z diff -1.9) | 0.709 over the table, 0.045 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.514). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-1.0, -40.7); signed map (1.4, -44.8). **Vector** length 76.4, 19.4% of its response variance represented; |z| ≥ 3 in 876 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +5.0 | +7.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.0 | +6.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.8 | +6.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +4.6 | +5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +8.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.3 | +5.4 |
|  | [[EX229 (drug)]] 5 µM |  | +2.6 | +2.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.4 | +3.7 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.0 | +0.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | +1.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.2 | -0.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.1 | -0.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | +2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | +2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.7 | -1.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.5 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | nuclear cap binding protein subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q29 — chr3:196,935,402-196,942,594 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NIP1, CBP20, Cbc2 |
| Gene groups (HGNC) | RNA binding motif containing |
| Hallmark sets | DNA_REPAIR, MYC_TARGETS_V1 |
| Reactome | 56 pathways, smallest: SLBP independent Processing of Histone Pre-mRNAs; SLBP Dependent Processing of Replication-Dependent Histone Pre-mRNAs; Signaling by FGFR2 IIIa TM |
| Matched by | ensembl_id |

**Function**, from UniProt [P52298](https://www.uniprot.org/uniprotkb/P52298) (Nuclear cap-binding protein subunit 2):

> Component of the cap-binding complex (CBC), which binds co-transcriptionally to the 5' cap of pre-mRNAs and is involved in various processes such as pre-mRNA splicing, translation regulation, nonsense-mediated mRNA decay, RNA-mediated gene silencing (RNAi) by microRNAs (miRNAs) and mRNA export. The CBC complex is involved in mRNA export from the nucleus via its interaction with ALYREF/THOC4/ALY, leading to the recruitment of the mRNA export machinery to the 5' end of mRNA and to mRNA export in …

**Summary**, from NCBI Gene [22916](https://www.ncbi.nlm.nih.gov/gene/22916):

> The product of this gene is a component of the nuclear cap-binding protein complex (CBC), which binds to the monomethylated 5' cap of nascent pre-mRNA in the nucleoplasm. The encoded protein has an RNP domain commonly found in RNA binding proteins, and contains the cap-binding activity. The CBC promotes pre-mRNA splicing, 3'-end processing, RNA nuclear export, and nonsense-mediated mRNA decay. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by …

**Accessions** — [HGNC:7659](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7659) · Entrez [22916](https://www.ncbi.nlm.nih.gov/gene/22916) · UniProt [P52298](https://www.uniprot.org/uniprotkb/P52298) · Ensembl [ENSG00000114503](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114503)

## Data

Gene col 3560: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3560); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3560, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3560]; `tensor/DDL_lfc|DDL_z.npy` [3560]; `embed/gene_vectors.npy` [3560]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3560 or target_col == 3560). Every well: [[NCBP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NCBP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
