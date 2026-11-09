---
symbol: "SHPRH"
type: "gene"
col: 7092
ensembl_id: "ENSG00000146414"
name: "SNF2 histone linker PHD RING helicase"
location: "6q24.3"
module: 213
arm: "+"
pooled_cpm: 84.9
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 21
n_dd_up_clean: 1
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/213"]
generated_by: "tahoemap"
---

# SHPRH

*SNF2 histone linker PHD RING helicase* — 6q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[NG25 (drug)]] 5 µM: 1.47× (z +5.1, q 2e-04, up in 28 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (hTERT-HPNE 2.33×; ⚠ cell-cycle shift, explains ~57% of this change).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (15 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.530× (z -16.0, q 0e+00, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACBD6]] (+0.64, fdr 7e-06), [[TUT4]] (+0.63, fdr 8e-06), [[RBM26]] (+0.62, fdr 7e-06); moves opposite to [[IRGQ]] (-0.54, fdr 3e-05), [[NOP14-AS1]] (-0.52, fdr 4e-05), [[CFL1]] (-0.52, fdr 6e-05).
> It is in [[Module 213]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7092.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (hTERT-HPNE 2.33×; ⚠ cell-cycle shift, explains ~57% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM |  | **1.47×** | +5.1 | 2e-04 | 28/47 (HEC-1-A, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 1.18× | +4.3 | 0.006 | 18/48 (LS 180, HS-578T, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.18× | +4.1 | 0.009 | 18/47 (A498, C32, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +4.0 | 0.010 | 18/48 (J82, LS 180, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.16× | +3.8 | 0.014 | 17/48 (HOP62, LS 180, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.14× | +3.2 | 0.14 | 5/48 (C32, LS 180, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | 1.13× | +3.1 | 0.14 | 7/50 (C32, NCI-H1792, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.09× | +3.0 | 0.16 | 5/48 (C32, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 21 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7092.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.530×** | -16.0 | 0e+00 | 40/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.555×** | -14.8 | 0e+00 | 39/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.611×** | -12.4 | 5e-33 | 41/48 (A-427, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.614×** | -11.3 | 1e-27 | 30/45 (RKO, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.660×** | -10.5 | 1e-23 | 35/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.766×** | -9.5 | 3e-19 | 30/49 (LOX-IMVI, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.790×** | -8.4 | 5e-15 | 28/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.722×** | -8.2 | 2e-14 | 29/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **0.729×** | -7.9 | 1e-13 | 30/49 (NCI-H23, A-427, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.744×** | -7.1 | 5e-11 | 28/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.758×** | -7.0 | 2e-10 | 29/48 (NCI-H460, RKO, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **0.765×** | -6.7 | 8e-10 | 28/48 (PANC-1, NCI-H661, …) | inconsistent across doses | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.780×** | -6.0 | 9e-08 | 25/48 (LOX-IMVI, SK-MEL-2, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.795×** | -5.5 | 1e-06 | 25/50 (SNU-1, HEC-1-A, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.805×** | -5.4 | 2e-06 | 24/48 (AN3 CA, NCI-H460, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.717×** | -4.4 | 4e-04 | 22/48 (hTERT-HPNE, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.842× | -4.0 | 0.002 | 20/47 (SNU-1, NCI-H1573, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.896× | -3.9 | 0.002 | 8/49 (MIA PaCa-2, HT-29, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.900× | -3.7 | 0.004 | 12/48 (SNU-423, CHP-212, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.869× | -3.5 | 0.010 | 17/48 (NCI-H460, RKO, …) | all doses, stronger at high dose |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | 0.865× | -3.4 | 0.016 | 15/47 (Hs 766T, COLO 205, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.774×** | -3.4 | 0.016 | 13/48 (HOP62, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | 0.874× | -3.2 | 0.022 | 14/48 (SW480, A498, …) | rises with dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.880× | -3.2 | 0.025 | 14/48 (SW480, CHP-212, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.881× | -3.2 | 0.026 | 12/47 (LS 180, Panc 03.27, …) | two highest doses |  |
| [[Piroxicam (drug)]] 0.05 µM |  | 0.884× | -2.9 | 0.063 | 8/48 (NCI-H2030, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7092. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 117 | 0 | 11 (9 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.426× (z -17.0) |
| [[SW480 (line)]] | alt | 176 | 0 | 11 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.222× (z -27.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.271× (z -23.4) |
| [[NCI-H460 (line)]] | wt | 81.0 | 0 | 10 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.298× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.389× (z -14.3) |
| [[SNU-423 (line)]] | alt | 126 | 0 | 7 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.318× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.337× (z -13.7) |
| [[LOX-IMVI (line)]] | wt | 113 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -15.3) |
| [[RKO (line)]] | wt | 120 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.101× (z -25.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.443× (z -9.5) |
| [[AN3 CA (line)]] | alt | 169 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0760× (z -20.6) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.292× (z -9.9) |
| [[HCT15 (line)]] | alt | 129 | 0 | 4 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.249× (z -14.2) |
| [[HepG2_C3A (line)]] | wt | 68.1 | 0 | 4 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0683× (z -22.2) ⚠ toxic; cell-cycle shift, explains ~8% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.305× (z -10.2) |
| [[J82 (line)]] | alt | 59.4 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.324× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.350× (z -11.0) |
| [[NCI-H1573 (line)]] | alt | 59.8 | 0 | 4 (3 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.174× (z -11.0) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.419× (z -10.4) |
| [[NCI-H23 (line)]] | alt | 91.4 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0972× (z -29.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.436× (z -10.3) |
| [[SNU-1 (line)]] | wt | 123 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -19.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.421× (z -9.1) |
| [[A-427 (line)]] | wt | 89.0 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.276× (z -18.3) |
| [[C-33 A (line)]] | alt | 165 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.324× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[CHP-212 (line)]] | wt | 132 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.335× (z -10.5) |
| [[HEC-1-A (line)]] | alt | 111 | 0 | 3 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.541× (z -9.0) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.563× (z -8.7) |
| [[HOP62 (line)]] | alt | 73.0 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.337× (z -12.3) |
| [[SK-MEL-2 (line)]] | alt | 74.9 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.183× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.363× (z -11.3) |
| [[SW48 (line)]] | wt | 59.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.315× (z -8.5) |
| [[A-172 (line)]] | wt | 64.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.279× (z -12.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 85.7 | 0 | 2 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0777× (z -14.3) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.383× (z -10.3) |
| [[hTERT-HPNE (line)]] | wt | 63.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +9.2) ⚠ cell-cycle shift, explains ~57% of this change | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -8.6) ⚠ cell-cycle shift, explains ~19% of this change |
| [[LoVo (line)]] | wt | 95.0 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.472× (z -11.7) |
| [[MIA PaCa-2 (line)]] | alt | 115 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.306× (z -15.8) |
| [[SHP-77 (line)]] | alt | 106 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.463× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.464× (z -9.5) |
| [[SW1417 (line)]] | alt | 85.8 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.489× (z -9.3) |
| [[C32 (line)]] | wt | 69.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.374× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 90.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.417× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 74.8 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.375× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~8% of this change |
| [[NCI-H661 (line)]] | alt | 153 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.153× (z -11.3) ⚠ transcription drop; cell-cycle shift, explains ~37% of this change |
| [[Panc 03.27 (line)]] | alt | 61.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.314× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change |
| [[SW 1088 (line)]] | alt | 81.2 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0849× (z -9.1) |
| [[A498 (line)]] | wt | 57.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 58.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 57.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 70.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 70.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 65.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 94.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 70.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 94.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 88.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 60.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7092), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACBD6]] | +0.64 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[TUT4]] | +0.63 | +0.59 / +0.58 | both halves | 8e-06 |  |
| [[RBM26]] | +0.62 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[PPA2]] | +0.61 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[TMLHE]] | +0.59 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[MRPS9]] | +0.59 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[IRAK1BP1]] | +0.58 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[INTU]] | +0.58 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[NARS2]] | +0.57 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[CWC27]] | +0.56 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[PTPN4]] | +0.56 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[MRPL1]] | +0.56 | +0.47 / +0.59 | both halves | 2e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IRGQ]] | -0.54 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[NOP14-AS1]] | -0.52 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[CFL1]] | -0.52 | -0.39 / -0.51 | both halves | 6e-05 |  |
| [[LINC01128]] | -0.51 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[CCNYL1]] | -0.51 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[VPS37B]] | -0.51 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[RHBDF1]] | -0.50 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[CDC42EP2]] | -0.49 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[AGRN]] | -0.49 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[PPP1CA]] | -0.49 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[RELT]] | -0.48 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[WNT9A]] | -0.48 | -0.42 / -0.44 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 213]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.795). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-22.7, -0.6); signed map (-10.3, -40.4). **Vector** length 96.0, 25.8% of its response variance represented; |z| ≥ 3 in 1,132 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.1 | +3.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +4.6 | -2.4 |
|  | [[NG25 (drug)]] 5 µM |  | +4.5 | +5.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.6 | -1.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.6 | +4.0 |
|  | [[EX229 (drug)]] 5 µM |  | +2.3 | +0.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.2 | -0.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +4.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.8 | +0.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.7 | -12.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.7 | -3.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.7 | -9.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.4 | -11.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.1 | -2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -2.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.3 | -1.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.6 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | SNF2 histone linker PHD RING helicase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q24.3 — chr6:145,864,245-145,964,423 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ90837, KIAA2023, bA545I5.2 |
| Gene groups (HGNC) | Ring finger proteins; PHD finger proteins; SNF2 related family; RING finger E3 ubiquitin protein ligases |
| Reactome | 2 pathways, smallest: E3 ubiquitin ligases ubiquitinate target proteins; Protein ubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q149N8](https://www.uniprot.org/uniprotkb/Q149N8) (E3 ubiquitin-protein ligase SHPRH):

> E3 ubiquitin-protein ligase involved in DNA repair. Upon genotoxic stress, accepts ubiquitin from the UBE2N-UBE2V2 E2 complex and transfers it to 'Lys-164' of PCNA which had been monoubiquitinated by UBE2A/B-RAD18, promoting the formation of non-canonical poly-ubiquitin chains linked through 'Lys-63'.

**Summary**, from NCBI Gene [257218](https://www.ncbi.nlm.nih.gov/gene/257218):

> SHPRH is a ubiquitously expressed protein that contains motifs characteristics of several DNA repair proteins, transcription factors, and helicases. SHPRH is a functional homolog of S. cerevisiae RAD5 (Unk et al., 2006 [PubMed 17108083]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:19336](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19336) · Entrez [257218](https://www.ncbi.nlm.nih.gov/gene/257218) · UniProt [Q149N8](https://www.uniprot.org/uniprotkb/Q149N8) · Ensembl [ENSG00000146414](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146414)

## Data

Gene col 7092: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7092); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7092, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7092]; `tensor/DDL_lfc|DDL_z.npy` [7092]; `embed/gene_vectors.npy` [7092]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7092 or target_col == 7092). Every well: [[SHPRH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SHPRH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
