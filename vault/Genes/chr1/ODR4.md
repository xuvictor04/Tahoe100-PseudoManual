---
symbol: "ODR4"
type: "gene"
col: 8047
ensembl_id: "ENSG00000157181"
name: "odr-4 GPCR localization factor homolog"
location: "1q31.1"
module: 41
arm: "+"
pooled_cpm: 123.45
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 2
n_dd_up_clean: 13
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# ODR4

*odr-4 GPCR localization factor homolog* — 1q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.74× (z +12.5, q 3e-33, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.657× (z -9.1, q 4e-17, down in 34 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.863× (z -4.7, q 6e-04, down in 17 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (CHP-212 0.247×, C32 0.387×, KATO III 0.409×, NCI-H23 0.453×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (A498 0.564×, CHP-212 0.413×, LoVo 0.671×, NCI-H460 0.641×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 0.05 µM in 1 line (AN3 CA 0.212×); [[Temsirolimus (drug)]] 0.5 µM in 1 line (SW 1088 0.137×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MON2]] (+0.65, fdr 1e-05), [[TRA2A]] (+0.63, fdr 7e-06), [[TMEM87A]] (+0.60, fdr 1e-05); moves opposite to [[JPT2]] (-0.61, fdr 1e-05), [[VANGL1]] (-0.53, fdr 3e-05), [[RANGAP1]] (-0.52, fdr 4e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → cells under [[Clofarabine (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8047.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.74×** | +12.5 | 3e-33 | 47/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.73×** | +12.3 | 3e-32 | 46/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.47×** | +12.2 | 5e-32 | 39/48 (A-172, SW480, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.37×** | +10.2 | 3e-22 | 45/49 (SW480, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.48×** | +8.8 | 2e-16 | 41/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.45×** | +8.4 | 4e-15 | 38/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.41×** | +7.7 | 8e-13 | 40/48 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +7.3 | 2e-11 | 35/48 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.34×** | +6.6 | 3e-09 | 35/48 (PANC-1, LS 180, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.74×** | +6.5 | 5e-09 | 34/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.34×** | +6.4 | 9e-09 | 30/48 (NCI-H460, SW480, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.32×** | +6.0 | 1e-07 | 32/48 (PANC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.27×** | +5.3 | 4e-06 | 28/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.36×** | +4.9 | 4e-05 | 32/49 (PANC-1, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.49×** | +4.7 | 1e-04 | 33/45 (PANC-1, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.37×** | +3.7 | 0.006 | 22/48 (Hs 766T, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.33×** | +3.3 | 0.025 | 18/48 (NCI-H460, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.22×** | +3.2 | 0.034 | 16/48 (NCI-H2030, NCI-H460, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8047.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (CHP-212 0.247×, C32 0.387×, KATO III 0.409×, NCI-H23 0.453×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (A498 0.564×, CHP-212 0.413×, LoVo 0.671×, NCI-H460 0.641×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 0.05 µM in 1 line (AN3 CA 0.212×); [[Temsirolimus (drug)]] 0.5 µM in 1 line (SW 1088 0.137×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.657×** | -9.1 | 4e-17 | 34/44 (CHP-212, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.863× | -4.7 | 6e-04 | 17/48 (SW480, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.815×** | -4.6 | 6e-04 | 25/48 (SW480, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | 0.901× | -3.3 | 0.14 | 6/48 (SW 1088, A549, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.869× | -3.2 | 0.16 | 17/48 (SW 900, HS-578T, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8047. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 160 | 10 (6 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.33× (z +20.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.641× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 106 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +16.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.46× (z +15.9) | — |
| [[PANC-1 (line)]] | alt | 98.3 | 7 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.40× (z +13.6) | — |
| [[BT-474 (line)]] | alt | 88.3 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +11.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.87× (z +11.0) | — |
| [[NCI-H1792 (line)]] | alt | 138 | 5 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.69× (z +13.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.63× (z +13.3) | — |
| [[NCI-H23 (line)]] | alt | 87.0 | 4 (2 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.34× (z +10.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.19× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.453× (z -9.2) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 119 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.62× (z +14.7) | — |
| [[LS 180 (line)]] | wt | 108 | 4 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.38× (z +16.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 110 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +13.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.05× (z +9.1) | — |
| [[NCI-H1573 (line)]] | alt | 146 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.86× (z +13.8) | — |
| [[SNU-1 (line)]] | wt | 123 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.68× (z +12.1) | — |
| [[HT-29 (line)]] | alt | 105 | 3 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.55× (z +12.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.55× (z +12.0) | — |
| [[KATO III (line)]] | alt | 79.2 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.48× (z +15.9) | [[Dinaciclib (drug)]] 5 µM 0.409× (z -11.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 124 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +12.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.14× (z +9.0) | — |
| [[SW1417 (line)]] | alt | 93.1 | 3 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.35× (z +10.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +10.2) | — |
| [[SW48 (line)]] | wt | 141 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.18× (z +12.1) | — |
| [[A-172 (line)]] | wt | 110 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +16.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.01× (z +9.9) | — |
| [[A498 (line)]] | wt | 170 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +10.6) ⚠ cell-cycle shift, explains ~25% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.564× (z -12.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 168 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.82× (z +14.0) | — |
| [[CHP-212 (line)]] | wt | 206 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.247× (z -11.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 100.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +14.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.12× (z +9.7) | — |
| [[HepG2_C3A (line)]] | wt | 84.2 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.65× (z +9.4) | — |
| [[A-427 (line)]] | wt | 120 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.38× (z +11.6) | — |
| [[A549 (line)]] | wt | 111 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +13.9) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[AN3 CA (line)]] | alt | 116 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.212× (z -10.2) |
| [[C32 (line)]] | wt | 281 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.387× (z -11.3) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 133 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.361× (z -9.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 96.0 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.05× (z +9.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 131 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.55× (z +10.3) | — |
| [[NCI-H2347 (line)]] | alt | 167 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.519× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[SK-MEL-2 (line)]] | alt | 113 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +12.5) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[SW 1088 (line)]] | alt | 99.6 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.137× (z -8.7) |
| [[SW 900 (line)]] | alt | 260 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.457× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 96.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 127 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 96.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 111 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 93.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 95.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 86.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 95.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8047), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MON2]] | +0.65 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[TRA2A]] | +0.63 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[TMEM87A]] | +0.60 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[USP8]] | +0.59 | +0.62 / +0.44 | both halves | 3e-05 |  |
| [[CWC25]] | +0.59 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[GOLGA8N]] | +0.57 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[ECD]] | +0.57 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[TVP23B]] | +0.56 | +0.57 / +0.41 | both halves | 4e-05 |  |
| [[RINT1]] | +0.56 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[CNPY2]] | +0.55 | +0.39 / +0.54 | both halves | 6e-05 |  |
| [[COG7]] | +0.55 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[MED4]] | +0.55 | +0.48 / +0.51 | both halves | 2e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JPT2]] | -0.61 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[VANGL1]] | -0.53 | -0.63 / -0.43 | both halves | 3e-05 |  |
| [[RANGAP1]] | -0.52 | -0.43 / -0.50 | both halves | 4e-05 |  |
| [[SGPL1]] | -0.51 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[RIPOR1]] | -0.51 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[CDYL]] | -0.51 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[DBN1]] | -0.51 | -0.45 / -0.43 | both halves | 4e-05 |  |
| [[KIAA0930]] | -0.50 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[ACTB]] | -0.50 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[GNG12]] | -0.50 | -0.49 / -0.37 | both halves | 9e-05 |  |
| [[ANKRD52]] | -0.49 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[PSEN2]] | -0.49 | -0.45 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Clofarabine (drug)]] 0.5 µM | C | ODR4's natural level raises the cells' numbers under Clofarabine 0.5 µM (protects the cells) | ODR4's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.59 | 0.476 over the table, 0.076 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.548). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-35.6, -34.1); signed map (-6.7, -2.1). **Vector** length 80.8, 21.9% of its response variance represented; |z| ≥ 3 in 1,034 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.0 | +1.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +1.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +2.1 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +2.2 | +1.4 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.0 | +2.8 |
|  | [[Vilanterol (drug)]] 5 µM |  | +2.0 | +2.2 |
|  | [[EX229 (drug)]] 0.5 µM |  | +2.0 | +2.5 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.9 | +1.2 |
| fall | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -3.9 | -0.5 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -3.3 | -0.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.3 | +0.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.2 | +1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.2 | -0.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -4.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.6 | -0.1 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -2.4 | -0.0 |

## What is on record

|  |  |
|---|---|
| Name | odr-4 GPCR localization factor homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q31.1 — chr1:186,375,838-186,421,378 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20505, odr-4, TTG1; previously C1orf27 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5SWX8](https://www.uniprot.org/uniprotkb/Q5SWX8) (Protein odr-4 homolog):

> May play a role in the trafficking of a subset of G protein coupled receptors.

**Summary**, from NCBI Gene [54953](https://www.ncbi.nlm.nih.gov/gene/54953):

> Predicted to be involved in intracellular protein localization. Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24299](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24299) · Entrez [54953](https://www.ncbi.nlm.nih.gov/gene/54953) · UniProt [Q5SWX8](https://www.uniprot.org/uniprotkb/Q5SWX8) · Ensembl [ENSG00000157181](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157181)

## Data

Gene col 8047: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8047); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8047, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8047]; `tensor/DDL_lfc|DDL_z.npy` [8047]; `embed/gene_vectors.npy` [8047]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8047 or target_col == 8047). Every well: [[ODR4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ODR4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
