---
symbol: "EYA3"
type: "gene"
col: 8138
ensembl_id: "ENSG00000158161"
name: "EYA transcriptional coactivator and phosphatase 3"
location: "1p35.3"
module: 178
arm: "+"
pooled_cpm: 69.0
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 5
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/178"]
generated_by: "tahoemap"
---

# EYA3

*EYA transcriptional coactivator and phosphatase 3* — 1p35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 1.58× (z +11.5, q 7e-28, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.473× (z -20.0, q 0e+00, down in 43 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[9-ING-41 (drug)]] 0.5 µM: 0.814× (z -3.6, q 0.031, down in 18 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (NCI-H23 0.108×, RKO 0.127×, NCI-H460 0.253×, CFPAC-1 0.230×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A-427 0.124×, RKO 0.147×, RPMI-7951 0.177×; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.191×; ⚠ toxic; cell-cycle shift, explains ~23% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLHDC10]] (+0.68, fdr 7e-06), [[NDUFB7]] (+0.68, fdr 7e-06), [[DHX57]] (+0.66, fdr 1e-05); moves opposite to [[HNRNPK]] (-0.54, fdr 4e-05), [[KDM6B]] (-0.54, fdr 1e-05), [[SEPTIN11]] (-0.53, fdr 3e-05).
> It is in [[Module 178]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠; shown: the 15 strongest. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8138.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **1.58×** | +11.5 | 7e-28 | 41/48 (PANC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.76×** | +11.0 | 6e-26 | 40/49 (SW480, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.46×** | +10.1 | 9e-22 | 35/48 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.45×** | +9.9 | 5e-21 | 38/48 (LoVo, A-172, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.43×** | +9.5 | 2e-19 | 42/48 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.22×** | +8.7 | 4e-16 | 35/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.35×** | +7.9 | 2e-13 | 39/48 (J82, BT-474, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.34×** | +7.8 | 3e-13 | 31/48 (PANC-1, HT-29, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.29×** | +6.4 | 8e-09 | 29/48 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~23% of this change | **1.28×** | +6.4 | 9e-09 | 23/47 (HT-29, MIA PaCa-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.7 | 1e-04 | 19/48 (PANC-1, LoVo, …) | rises with dose | composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 1.12× | +4.3 | 7e-04 | 14/48 (HT-29, LoVo, …) | rises with dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.26×** | +4.1 | 0.002 | 17/49 (PANC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.44×** | +4.0 | 0.003 | 16/45 (PANC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 1.13× | +3.2 | 0.052 | 16/48 (NCI-H460, A-427, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8138.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (NCI-H23 0.108×, RKO 0.127×, NCI-H460 0.253×, CFPAC-1 0.230×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A-427 0.124×, RKO 0.147×, RPMI-7951 0.177×; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.191×; ⚠ toxic; cell-cycle shift, explains ~23% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.473×** | -20.0 | 0e+00 | 43/49 (NCI-H23, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.442×** | -18.1 | 0e+00 | 43/45 (A-427, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.506×** | -17.5 | 0e+00 | 33/42 (PANC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~19% of this change | **0.777×** | -6.8 | 2e-09 | 26/47 (RPMI-7951, J82, …) | inconsistent across doses | low cells (technical?) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.814×** | -3.6 | 0.031 | 18/48 (NCI-H1792, AN3 CA, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | 0.875× | -3.6 | 0.034 | 11/48 (NCI-H1573, A498, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | 0.839× | -3.1 | 0.15 | 9/48 (SW 1271, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.894× | -3.0 | 0.18 | 7/48 (HS-578T, COLO 205, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8138. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 72.1 | 3 | 3 (3 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.06× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.319× (z -18.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 85.6 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.64× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.427× (z -14.3) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 74.4 | 1 | 3 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.81× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.303× (z -17.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 84.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.230× (z -19.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 74.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.378× (z -11.8) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 105 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -16.0) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 69.1 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.88× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.346× (z -12.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 65.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.290× (z -17.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 88.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.127× (z -23.3) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 87.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -18.5) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 104 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.244× (z -15.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 77.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.356× (z -9.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 53.9 | 2 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.48× (z +8.7) | — |
| [[J82 (line)]] | alt | 64.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.409× (z -11.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 59.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.440× (z -10.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 53.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.274× (z -13.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 62.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.329× (z -12.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 78.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.124× (z -21.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 52.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.362× (z -10.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 84.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.134× (z -10.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 65.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.431× (z -8.8) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 37.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.131× (z -9.0) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 67.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.395× (z -8.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 57.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.206× (z -11.4) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 56.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.344× (z -8.8) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 80.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.613× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 74.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.462× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 78.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.283× (z -14.3) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 84.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.108× (z -26.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 52.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.253× (z -20.5) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 59.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.109× (z -9.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 87.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.491× (z -8.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 64.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.189× (z -11.9) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 61.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.387× (z -10.2) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 56.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.267× (z -13.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 56.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -11.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 56.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 59.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 93.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 82.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 76.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 72.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 90.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 95.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 58.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8138), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHDC10]] | +0.68 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[NDUFB7]] | +0.68 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[DHX57]] | +0.66 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[PPIL2]] | +0.65 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[CDK5RAP1]] | +0.65 | +0.66 / +0.57 | both halves | 8e-06 |  |
| [[MED23]] | +0.65 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[AP3S2]] | +0.64 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[EIF4E2]] | +0.64 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[GTF3C2]] | +0.63 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[TRIP4]] | +0.63 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[TENT2]] | +0.63 | +0.68 / +0.49 | both halves | 1e-05 |  |
| [[TEFM]] | +0.63 | +0.51 / +0.69 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPK]] | -0.54 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[KDM6B]] | -0.54 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[SEPTIN11]] | -0.53 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[JUNB]] | -0.52 | -0.50 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 178]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.614). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-34.3, -7.9); signed map (-17.8, -18.8). **Vector** length 87.0, 20.3% of its response variance represented; |z| ≥ 3 in 999 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +5.0 | +11.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.9 | +10.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.7 | +11.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.5 | +7.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.0 | +8.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.9 | +4.1 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +1.6 | +2.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.4 | +1.5 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.5 | -18.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.7 | -17.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.4 | -20.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.7 | -2.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | +2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -1.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.8 | -1.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.7 | -2.5 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -1.5 | -1.3 |
|  | [[Roxadustat (drug)]] 5 µM |  | -1.5 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | EYA transcriptional coactivator and phosphatase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.3 — chr1:27,970,344-28,088,637 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp686C132 |
| Gene groups (HGNC) | EYA transcriptional coactivator and phosphatases |
| Reactome | 4 pathways, smallest: Recruitment and ATM-mediated phosphorylation of repair and signaling proteins at DNA double strand breaks; DNA Double Strand Break Response; DNA Double-Strand Break Repair |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99504](https://www.uniprot.org/uniprotkb/Q99504) (Protein phosphatase EYA3):

> Tyrosine phosphatase that specifically dephosphorylates 'Tyr-142' of histone H2AX (H2AXY142ph). 'Tyr-142' phosphorylation of histone H2AX plays a central role in DNA repair and acts as a mark that distinguishes between apoptotic and repair responses to genotoxic stress. Promotes efficient DNA repair by dephosphorylating H2AX, promoting the recruitment of DNA repair complexes containing MDC1. Its function as histone phosphatase probably explains its role in transcription regulation during …

**Summary**, from NCBI Gene [2140](https://www.ncbi.nlm.nih.gov/gene/2140):

> This gene encodes a member of the eyes absent (EYA) family of proteins. The encoded protein may act as a transcriptional activator and have a role during development. It can act as a mediator of chemoresistance and cell survival in Ewing sarcoma cells, where this gene is up-regulated via a micro-RNA that binds to the 3' UTR of the transcript. A similar protein in mice acts as a transcriptional activator. Alternative splicing of this gene results in multiple transcript variants. [provided by …

**Accessions** — [HGNC:3521](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3521) · Entrez [2140](https://www.ncbi.nlm.nih.gov/gene/2140) · UniProt [Q99504](https://www.uniprot.org/uniprotkb/Q99504) · Ensembl [ENSG00000158161](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158161)

## Data

Gene col 8138: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8138); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8138, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8138]; `tensor/DDL_lfc|DDL_z.npy` [8138]; `embed/gene_vectors.npy` [8138]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8138 or target_col == 8138). Every well: [[EYA3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EYA3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
