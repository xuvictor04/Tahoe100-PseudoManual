---
symbol: "GRAMD1A"
type: "gene"
col: 1586
ensembl_id: "ENSG00000089351"
name: "GRAM domain containing 1A"
location: "19q13.11"
module: 54
arm: "+"
pooled_cpm: 48.22
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 25
n_dd_up_clean: 0
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# GRAMD1A

*GRAM domain containing 1A* — 19q13.11

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 6 lines (A-172 7.75×, J82 13.0×, HS-578T 13.0×, hTERT-HPNE 23.4×, …); [[Harringtonine (drug)]] 5 µM in 5 lines (J82 6.76×, HS-578T 4.05×, A-172 2.68×, RPMI-7951 5.13×, …; ⚠ cell-cycle shift, explains ~28% of this change); [[PH-797804 (drug)]] 5 µM in 3 lines (HS-578T 9.68×, A-172 4.25×, hTERT-HPNE 12.2×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (J82 3.09×, hTERT-HPNE 3.21×).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (16 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.552× (z -16.5, q 0e+00, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXO46]] (+0.59, fdr 1e-05), [[MRPL14]] (+0.58, fdr 1e-05), [[SCN1B]] (+0.58, fdr 1e-05, ⚠ read-through risk), [[DTX2]] (+0.57, fdr 1e-05); moves opposite to [[UBE2A]] (-0.49, fdr 4e-05), [[TMEM167A]] (-0.49, fdr 2e-04), [[PGRMC1]] (-0.48, fdr 2e-04).
> It sits in the **+** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ANKRD33B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1586.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 6 lines (A-172 7.75×, J82 13.0×, HS-578T 13.0×, hTERT-HPNE 23.4×, …); [[Harringtonine (drug)]] 5 µM in 5 lines (J82 6.76×, HS-578T 4.05×, A-172 2.68×, RPMI-7951 5.13×, …; ⚠ cell-cycle shift, explains ~28% of this change); [[PH-797804 (drug)]] 5 µM in 3 lines (HS-578T 9.68×, A-172 4.25×, hTERT-HPNE 12.2×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (J82 3.09×, hTERT-HPNE 3.21×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | 1.43× | +3.7 | 0.11 | 20/49 (A-172, J82, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | 1.39× | +3.4 | 0.16 | 18/48 (HS-578T, A-172, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.12× | +3.2 | 0.31 | 16/48 (HT-29, HepG2/C3A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 19 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1586.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.552×** | -16.5 | 0e+00 | 40/48 (LoVo, HOP62, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.594×** | -14.5 | 6e-45 | 33/48 (NCI-H23, LoVo, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.498×** | -13.7 | 2e-40 | 33/48 (SNU-1, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.566×** | -11.2 | 7e-27 | 35/48 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.566×** | -10.7 | 8e-25 | 25/39 (HepG2/C3A, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.591×** | -10.3 | 5e-23 | 37/48 (C32, SK-MEL-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.620×** | -9.4 | 6e-19 | 31/48 (A549, HOP62, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.631×** | -9.0 | 1e-17 | 31/47 (HepG2/C3A, SW480, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.631×** | -8.7 | 3e-16 | 32/47 (HOP62, SK-MEL-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.620×** | -8.7 | 3e-16 | 30/44 (NCI-H23, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **0.645×** | -8.6 | 5e-16 | 31/47 (HepG2/C3A, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.677×** | -7.6 | 1e-12 | 31/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.702×** | -6.9 | 2e-10 | 29/48 (HepG2/C3A, LoVo, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.709×** | -6.5 | 4e-09 | 30/47 (LoVo, NCI-H23, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.753×** | -5.5 | 1e-06 | 25/48 (HepG2/C3A, A498, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.810×** | -3.9 | 0.003 | 17/48 (LoVo, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.876× | -3.6 | 0.006 | 19/48 (HOP62, J82, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.859× | -2.9 | 0.061 | 13/47 (A498, NCI-H23, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1586. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 28.0 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -17.7) |
| [[A-172 (line)]] | wt | 69.7 | 5 (2 ⚠) | 2 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 3.69× (z +15.9) ⚠ cell-cycle shift, explains ~17% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.75× (z +13.0) | [[Dinaciclib (drug)]] 0.05 µM 0.363× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[SW480 (line)]] | alt | 43.6 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -16.3) |
| [[HepG2_C3A (line)]] | wt | 72.0 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.142× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.241× (z -13.2) |
| [[J82 (line)]] | alt | 39.5 | 4 (1 ⚠) | 2 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 6.76× (z +16.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.09× (z +14.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -12.8) |
| [[NCI-H23 (line)]] | alt | 40.4 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -18.0) |
| [[A549 (line)]] | wt | 153 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -10.6) |
| [[SK-MEL-2 (line)]] | alt | 35.2 | 0 | 5 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.190× (z -13.1) |
| [[A-427 (line)]] | wt | 35.9 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -14.1) |
| [[HEC-1-A (line)]] | alt | 61.3 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.269× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -12.2) |
| [[HOP62 (line)]] | alt | 61.8 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -16.6) |
| [[HS-578T (line)]] | alt | 69.0 | 4 (2 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 5.80× (z +15.1) ⚠ cell-cycle shift, explains ~17% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 13.0× (z +11.5) | — |
| [[hTERT-HPNE (line)]] | wt | 39.0 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +10.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 77.6 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.445× (z -10.9) |
| [[C32 (line)]] | wt | 42.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -16.9) |
| [[COLO 205 (line)]] | alt | 34.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -11.3) |
| [[NCI-H460 (line)]] | wt | 35.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.323× (z -12.2) |
| [[Panc 03.27 (line)]] | alt | 36.3 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.284× (z -14.3) |
| [[RKO (line)]] | wt | 51.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -17.5) |
| [[SW 900 (line)]] | alt | 52.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -10.9) |
| [[C-33 A (line)]] | alt | 50.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.241× (z -10.2) |
| [[HT-29 (line)]] | alt | 17.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -11.2) |
| [[KATO III (line)]] | alt | 48.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.292× (z -10.6) |
| [[LOX-IMVI (line)]] | wt | 32.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -15.0) |
| [[NCI-H1573 (line)]] | alt | 16.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.151× (z -12.2) |
| [[NCI-H1792 (line)]] | alt | 48.3 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 8.55× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.490× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 38.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -10.2) |
| [[RPMI-7951 (line)]] | alt | 45.9 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 5.13× (z +11.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 12.0× (z +9.1) | — |
| [[SNU-1 (line)]] | wt | 39.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0842× (z -15.3) |
| [[SNU-423 (line)]] | alt | 40.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -9.0) |
| [[SW1417 (line)]] | alt | 39.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -12.5) |
| [[SW48 (line)]] | wt | 49.4 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -9.0) |
| [[A498 (line)]] | wt | 140 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 2.14× (z +9.8) ⚠ cell-cycle shift, explains ~17% of this change | — |
| [[AN3 CA (line)]] | alt | 68.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -13.0) |
| [[AsPC-1 (line)]] | alt | 21.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -10.8) |
| [[CFPAC-1 (line)]] | alt | 29.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.317× (z -8.6) |
| [[H4 (line)]] | wt | 73.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.339× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[Hs 766T (line)]] | wt | 45.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.302× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[LS 180 (line)]] | wt | 31.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.321× (z -8.6) |
| [[BT-474 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 46.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1586), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 4 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO46]] | +0.59 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[MRPL14]] | +0.58 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[SCN1B]] | +0.58 | +0.52 / +0.52 | both halves | 1e-05 | STRING 624; ⚠ **readthrough risk**: SCN1B lies 4.0 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[DTX2]] | +0.57 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[B4GALT5]] | +0.53 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[KRI1]] | +0.51 | +0.27 / +0.59 | both halves | 3e-04 |  |
| [[PELO]] | +0.50 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[RHOG]] | +0.50 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[TRIP10]] | +0.50 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[SBNO2]] | +0.50 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[BTBD2]] | +0.49 | +0.38 / +0.46 | both halves | 7e-05 |  |
| [[ZGPAT]] | +0.49 | +0.51 / +0.41 | both halves | 4e-05 |  |
| [[RPS26]] | +0.49 | +0.40 / +0.42 | both halves | 5e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2A]] | -0.49 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[TMEM167A]] | -0.49 | -0.30 / -0.58 | both halves | 2e-04 |  |
| [[PGRMC1]] | -0.48 | -0.31 / -0.52 | both halves | 2e-04 |  |
| [[VBP1]] | -0.46 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[RAB22A]] | -0.43 | -0.33 / -0.36 | both halves | 1e-04 |  |
| [[PRDM2]] | -0.43 | -0.44 / -0.36 | both halves | 1e-04 |  |
| [[SLC35F5]] | -0.43 | -0.27 / -0.39 | both halves | 3e-04 |  |
| [[AP2B1]] | -0.43 | -0.24 / -0.43 | both halves | 5e-04 |  |
| [[N4BP2]] | -0.43 | -0.41 / -0.33 | both halves | 1e-04 |  |
| [[NEK11]] | -0.42 | -0.39 / -0.30 | both halves | 2e-04 |  |
| [[EIF4G2]] | -0.41 | -0.29 / -0.39 | both halves | 2e-04 |  |
| [[RPN1]] | -0.41 | -0.17 / -0.47 | ⚠ not reproduced | 0.001 |  |
| [[PAPOLA]] | -0.41 | -0.22 / -0.43 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANKRD33B]] | B | ANKRD33B activity raises GRAMD1A's level | lines that do not express ANKRD33B (15) vs lines expressing it (35) | 1.46× lower at baseline in the lines without ANKRD33B | 0.062 | ⚠ within organs, on part of the lines; also absent: JCAD, FAT4, ARHGAP22 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **+** arm (projection on the module's main direction 0.391). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (13.8, 41.5); signed map (49.8, 0.1). **Vector** length 105, 27.3% of its response variance represented; |z| ≥ 3 in 1,086 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.6 | +3.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.5 | +3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +3.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.7 | +2.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.0 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.5 | +2.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.4 | +1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | -0.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.4 | -10.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.9 | -3.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.8 | -16.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -3.4 | -5.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.4 | -8.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -5.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.1 | -0.9 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.0 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | GRAM domain containing 1A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.11 — chr19:34,994,784-35,026,471 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LAMa, FLJ90346; previously KIAA1533 |
| Gene groups (HGNC) | GRAM domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96CP6](https://www.uniprot.org/uniprotkb/Q96CP6) (Protein Aster-A):

> Cholesterol transporter that mediates non-vesicular transport of cholesterol from the plasma membrane (PM) to the endoplasmic reticulum (ER) (By similarity). Contains unique domains for binding cholesterol and the PM, thereby serving as a molecular bridge for the transfer of cholesterol from the PM to the ER (By similarity). Plays a crucial role in cholesterol homeostasis and has the unique ability to localize to the PM based on the level of membrane cholesterol (By similarity). In lipid-poor …

**Summary**, from NCBI Gene [57655](https://www.ncbi.nlm.nih.gov/gene/57655):

> Predicted to enable cholesterol binding activity and cholesterol transfer activity. Predicted to be involved in cellular response to cholesterol and intracellular cholesterol transport. Located in endoplasmic reticulum membrane; organelle membrane contact site; and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29305](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29305) · Entrez [57655](https://www.ncbi.nlm.nih.gov/gene/57655) · UniProt [Q96CP6](https://www.uniprot.org/uniprotkb/Q96CP6) · Ensembl [ENSG00000089351](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000089351)

## Data

Gene col 1586: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1586); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1586, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1586]; `tensor/DDL_lfc|DDL_z.npy` [1586]; `embed/gene_vectors.npy` [1586]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1586 or target_col == 1586). Every well: [[GRAMD1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GRAMD1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
