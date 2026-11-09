---
symbol: "TFAM"
type: "gene"
col: 2915
ensembl_id: "ENSG00000108064"
name: "transcription factor A, mitochondrial"
location: "10q21.1"
module: 1
arm: "+"
pooled_cpm: 53.05
n_lines_expressing: 50
n_dd_up: 36
n_dd_down: 2
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# TFAM

*transcription factor A, mitochondrial* — 10q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (22 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.02× (z +13.6, q 2e-39, up in 44 of 48 measured lines) ⚠ cell-cycle shift, explains ~46% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.33× (z +11.6, q 6e-29, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.893× (z -5.1, q 2e-04, down in 6 of 49 measured lines) ⚠ position not correctable. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 0.757× (z -3.5, q 0.085, down in 25 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 2 lines (NCI-H23 0.737×, MIA PaCa-2 0.700×; ⚠ position not correctable); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (AN3 CA 0.135×); [[Dinaciclib (drug)]] 5 µM in 1 line (SK-MEL-2 0.288×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (CHP-212 0.100×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RIF1]] (+0.66, fdr 7e-06), [[UTP20]] (+0.64, fdr 3e-05), [[ITPRIPL2]] (+0.62, fdr 7e-05); moves opposite to [[CRY2]] (-0.64, fdr 2e-05), [[PLD3]] (-0.63, fdr 1e-05), [[SLC17A5]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 24 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 22 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2915.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **2.02×** | +13.6 | 2e-39 | 44/48 (A549, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **2.48×** | +12.0 | 1e-30 | 40/43 (SNU-423, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **2.34×** | +11.7 | 3e-29 | 42/47 (LoVo, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.33×** | +11.6 | 6e-29 | 43/48 (LOX-IMVI, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **2.48×** | +11.5 | 2e-28 | 43/46 (MIA PaCa-2, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **2.24×** | +11.1 | 2e-26 | 45/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **2.32×** | +10.7 | 1e-24 | 43/45 (SNU-423, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **2.17×** | +10.2 | 1e-22 | 43/48 (LOX-IMVI, A549, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.64×** | +9.6 | 3e-20 | 43/48 (A-172, NCI-H460, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.03×** | +9.3 | 7e-19 | 43/47 (NCI-H1573, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.93×** | +9.0 | 9e-18 | 45/48 (NCI-H1792, CFPAC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.02×** | +8.9 | 2e-17 | 44/48 (LOX-IMVI, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.83×** | +8.3 | 5e-15 | 41/48 (SNU-423, NCI-H1792, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.77×** | +7.8 | 2e-13 | 41/48 (CFPAC-1, NCI-H1792, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.73×** | +7.5 | 2e-12 | 42/48 (LoVo, PANC-1, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.72×** | +7.4 | 4e-12 | 41/48 (A-172, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.67×** | +7.1 | 5e-11 | 40/48 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.40×** | +6.5 | 3e-09 | 38/48 (HOP62, A549, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.33×** | +5.5 | 8e-07 | 30/48 (PANC-1, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **1.33×** | +3.8 | 0.003 | 23/48 (NCI-H460, LOX-IMVI, …) | top dose only | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.67×** | +3.7 | 0.005 | 21/48 (HEC-1-A, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.013 | 23/48 (SNU-423, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.28×** | +3.1 | 0.033 | 17/47 (NCI-H460, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | **1.26×** | +3.1 | 0.038 | 22/48 (HS-578T, SNU-423, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.23×** | +2.9 | 0.067 | 17/48 (SNU-423, HOP62, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.24×** | +2.8 | 0.082 | 15/47 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.47×** | +2.8 | 0.083 | 14/48 (HCT15, NCI-H1573, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2915.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 2 lines (NCI-H23 0.737×, MIA PaCa-2 0.700×; ⚠ position not correctable); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (AN3 CA 0.135×); [[Dinaciclib (drug)]] 5 µM in 1 line (SK-MEL-2 0.288×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (CHP-212 0.100×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.893× | -5.1 | 2e-04 | 6/49 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.740×** | -4.1 | 0.013 | 26/48 (A-427, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.757×** | -3.5 | 0.085 | 25/47 (NCI-H2030, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[Roxadustat (drug)]] 5 µM |  | 0.783× | -3.2 | 0.18 | 18/47 (SHP-77, C32, …) | top dose only | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | 0.786× | -3.2 | 0.18 | 21/47 (NCI-H2030, RPMI-7951, …) | rises with dose |  |
| [[Pentagastrin (drug)]] 5 µM |  | 0.853× | -3.1 | 0.20 | 11/48 (LOX-IMVI, SK-MEL-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.63 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2915. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 58.9 | 11 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +13.2) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.86× (z +11.8) | — |
| [[PANC-1 (line)]] | alt | 69.1 | 7 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.67× (z +11.4) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 2.17× (z +9.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 49.7 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.36× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.25× (z +8.7) | — |
| [[NCI-H1573 (line)]] | alt | 38.5 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.73× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.07× (z +9.5) | — |
| [[NCI-H1792 (line)]] | alt | 30.6 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +10.8) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.81× (z +9.0) | — |
| [[SNU-423 (line)]] | alt | 68.3 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.36× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.14× (z +10.3) | — |
| [[A549 (line)]] | wt | 51.0 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +13.8) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.91× (z +11.3) | — |
| [[LoVo (line)]] | wt | 36.7 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +13.4) ⚠ cell-cycle shift, explains ~46% of this change | — |
| [[A-172 (line)]] | wt | 39.2 | 4 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +11.1) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[CFPAC-1 (line)]] | alt | 48.2 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +12.5) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.30× (z +10.3) | — |
| [[HOP62 (line)]] | alt | 36.5 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +12.0) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.55× (z +10.5) | — |
| [[SW480 (line)]] | alt | 114 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.48× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | — |
| [[A498 (line)]] | wt | 49.1 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +12.9) ⚠ cell-cycle shift, explains ~46% of this change | — |
| [[NCI-H460 (line)]] | wt | 46.1 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +10.8) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 48.3 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +8.9) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.88× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.288× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[AsPC-1 (line)]] | alt | 30.8 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.78× (z +8.6) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[HEC-1-A (line)]] | alt | 49.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +11.6) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.55× (z +9.2) | — |
| [[HS-578T (line)]] | alt | 24.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.68× (z +11.2) | — |
| [[LS 180 (line)]] | wt | 33.1 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.30× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[AN3 CA (line)]] | alt | 75.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.135× (z -10.9) |
| [[C32 (line)]] | wt | 18.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +9.7) ⚠ cell-cycle shift, explains ~46% of this change | — |
| [[CHP-212 (line)]] | wt | 39.7 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.100× (z -9.7) |
| [[H4 (line)]] | wt | 30.8 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.34× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[Hs 766T (line)]] | wt | 32.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.02× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | — |
| [[KATO III (line)]] | alt | 42.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.73× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | — |
| [[NCI-H2347 (line)]] | alt | 47.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +9.3) ⚠ cell-cycle shift, explains ~46% of this change | — |
| [[Panc 03.27 (line)]] | alt | 52.3 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +8.6) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[RKO (line)]] | wt | 65.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.97× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | — |
| [[RPMI-7951 (line)]] | alt | 33.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +9.5) ⚠ cell-cycle shift, explains ~46% of this change | — |
| [[SW1417 (line)]] | alt | 68.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | — |
| [[A-427 (line)]] | wt | 101 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 66.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 89.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 76.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 62.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 54.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 62.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2915), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*33 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIF1]] | +0.66 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[UTP20]] | +0.64 | +0.75 / +0.45 | both halves | 3e-05 |  |
| [[ITPRIPL2]] | +0.62 | +0.68 / +0.38 | both halves | 7e-05 |  |
| [[NOL11]] | +0.62 | +0.71 / +0.57 | both halves | 1e-05 | STRING 781 |
| [[SMIM15]] | +0.61 | +0.55 / +0.46 | both halves | 3e-05 |  |
| [[KRR1]] | +0.60 | +0.67 / +0.38 | both halves | 7e-05 | STRING 563 |
| [[ABCE1]] | +0.60 | +0.67 / +0.46 | both halves | 2e-05 | STRING 423 |
| [[LINC01515]] | +0.60 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[TASOR]] | +0.59 | +0.69 / +0.43 | both halves | 3e-05 |  |
| [[UTP15]] | +0.59 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[GPATCH4]] | +0.59 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[SF3B3]] | +0.59 | +0.57 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*67 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRY2]] | -0.64 | -0.64 / -0.46 | both halves | 2e-05 |  |
| [[PLD3]] | -0.63 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[SLC17A5]] | -0.62 | -0.70 / -0.49 | both halves | 1e-05 |  |
| [[ANO8]] | -0.62 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[LIN7B]] | -0.62 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[SLC25A29]] | -0.62 | -0.61 / -0.55 | both halves | 1e-05 |  |
| [[MPND]] | -0.61 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[RAB6A]] | -0.61 | -0.71 / -0.58 | both halves | 7e-06 |  |
| [[GUK1]] | -0.61 | -0.66 / -0.49 | both halves | 1e-05 |  |
| [[PPP2R5B]] | -0.60 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[COX7A2L]] | -0.60 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[CARD19]] | -0.60 | -0.64 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TFAM's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RIMS3]] | B | RIMS3 activity raises TFAM's level | lines that do not express RIMS3 (9) vs lines expressing it (41) | 1.29× lower at baseline in the lines without RIMS3 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: STOX1, ZFP69B, LINC02456; maybe low, not absent |
| [[FAM102A]] | C | FAM102A activity lowers TFAM's level | lines that do not express FAM102A (3) vs lines expressing it (47) | 1.77× higher at baseline in the lines without FAM102A | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MBNL2, NINJ1, RPS6KA2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.551). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (3.4, -17.4); signed map (2.8, -41.2). **Vector** length 69.1, 19.9% of its response variance represented; |z| ≥ 3 in 1,281 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.8 | +5.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +6.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.3 | +7.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.7 | +8.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.2 | +11.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.1 | +3.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.9 | +2.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.3 | +0.5 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.1 | +0.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.4 | +3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | +2.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | -2.2 | +7.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | +2.3 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.0 | +0.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.8 | -1.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.7 | -0.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.6 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | transcription factor A, mitochondrial |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q21.1 — chr10:58,385,345-58,399,220 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously TCF6, TCF6L2 |
| Gene groups (HGNC) | Mitochondrial transcription initiation complex subunits |
| Reactome | 5 pathways, smallest: Mitochondrial transcription; Transcriptional activation of mitochondrial biogenesis; Mitochondrial biogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q00059](https://www.uniprot.org/uniprotkb/Q00059) (Transcription factor A, mitochondrial):

> Binds to the mitochondrial light strand promoter and functions in mitochondrial transcription regulation. Component of the mitochondrial transcription initiation complex, composed at least of TFB2M, TFAM and POLRMT that is required for basal transcription of mitochondrial DNA. In this complex, TFAM recruits POLRMT to a specific promoter whereas TFB2M induces structural changes in POLRMT to enable promoter opening and trapping of the DNA non-template strand. Required for accurate and efficient …

**Summary**, from NCBI Gene [7019](https://www.ncbi.nlm.nih.gov/gene/7019):

> This gene encodes a key mitochondrial transcription factor containing two high mobility group motifs. The encoded protein also functions in mitochondrial DNA replication and repair. Sequence polymorphisms in this gene are associated with Alzheimer's and Parkinson's diseases. There are pseudogenes for this gene on chromosomes 6, 7, and 11. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Aug 2012]

**Accessions** — [HGNC:11741](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11741) · Entrez [7019](https://www.ncbi.nlm.nih.gov/gene/7019) · UniProt [Q00059](https://www.uniprot.org/uniprotkb/Q00059) · Ensembl [ENSG00000108064](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108064)

## Data

Gene col 2915: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2915); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2915, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2915]; `tensor/DDL_lfc|DDL_z.npy` [2915]; `embed/gene_vectors.npy` [2915]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2915 or target_col == 2915). Every well: [[TFAM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TFAM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
