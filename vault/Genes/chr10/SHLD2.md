---
symbol: "SHLD2"
type: "gene"
col: 4330
ensembl_id: "ENSG00000122376"
name: "shieldin complex subunit 2"
location: "10q23.2"
module: 5
arm: "+"
pooled_cpm: 91.05
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 19
n_dd_up_clean: 1
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# SHLD2

*shieldin complex subunit 2* — 10q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.45× (z +10.0, q 1e-20, up in 28 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[EX229 (drug)]] 5 µM: 1.27× (z +3.5, q 0.083, up in 9 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 6 lines (CFPAC-1 2.91×, NCI-H1792 2.69×, NCI-H1573 3.27×, SW48 2.81×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H1573 2.93×, SW 900 3.13×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.598× (z -14.2, q 8e-43, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MPP3]] (+0.69, fdr 7e-06), [[NLN]] (+0.64, fdr 7e-06), [[EIF2B3]] (+0.62, fdr 1e-05); moves opposite to [[EFNA1]] (-0.61, fdr 1e-05), [[ITM2B]] (-0.53, fdr 3e-05), [[SLC2A12]] (-0.51, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ADCY3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4330.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 6 lines (CFPAC-1 2.91×, NCI-H1792 2.69×, NCI-H1573 3.27×, SW48 2.81×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H1573 2.93×, SW 900 3.13×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +10.0 | 1e-20 | 28/43 (CFPAC-1, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.20×** | +5.2 | 6e-05 | 21/48 (SW480, RKO, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **1.27×** | +3.5 | 0.083 | 9/48 (HEC-1-A, C32, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~55% of this change | 1.12× | +3.1 | 0.26 | 6/49 (PANC-1, LOX-IMVI, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 17 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4330.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.598×** | -14.2 | 8e-43 | 40/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.395×** | -13.4 | 1e-38 | 41/49 (NCI-H460, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.678×** | -10.7 | 2e-24 | 39/48 (HOP62, A498, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.669×** | -10.7 | 2e-24 | 31/50 (A-172, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.694×** | -10.1 | 8e-22 | 35/48 (HOP62, NCI-H460, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.694×** | -10.1 | 8e-22 | 32/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.701×** | -9.8 | 1e-20 | 27/48 (LS 180, HOP62, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.814×** | -8.0 | 9e-14 | 27/49 (A-172, A549, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.757×** | -7.7 | 1e-12 | 32/48 (A-172, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.824×** | -7.5 | 3e-12 | 24/48 (A498, C32, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.754×** | -7.5 | 4e-12 | 27/48 (NCI-H2030, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.755×** | -7.4 | 5e-12 | 24/47 (PANC-1, A-172, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **0.773×** | -7.1 | 6e-11 | 27/48 (RPMI-7951, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.770×** | -6.9 | 2e-10 | 27/47 (AsPC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.773×** | -6.8 | 4e-10 | 28/48 (SW48, MIA PaCa-2, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **0.674×** | -5.7 | 4e-07 | 30/47 (SW48, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.841× | -4.8 | 6e-05 | 21/49 (AsPC-1, MIA PaCa-2, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.844× | -4.7 | 9e-05 | 19/47 (AsPC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.881× | -3.9 | 0.003 | 16/49 (AsPC-1, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.885× | -3.6 | 0.006 | 15/48 (AsPC-1, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.785×** | -3.5 | 0.010 | 19/48 (A-427, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.05 µM |  | 0.881× | -3.2 | 0.026 | 11/47 (AN3 CA, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.800×** | -3.2 | 0.026 | 19/49 (A498, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4330. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 138 | 0 | 11 (5 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.284× (z -18.6) |
| [[HOP62 (line)]] | alt | 140 | 0 | 11 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.326× (z -15.9) |
| [[MIA PaCa-2 (line)]] | alt | 102 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.282× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.318× (z -14.5) |
| [[NCI-H460 (line)]] | wt | 108 | 1 (1 ⚠) | 7 (5 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.78× (z +8.8) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 0.05 µM 0.369× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.270× (z -10.7) |
| [[A549 (line)]] | wt | 115 | 1 (1 ⚠) | 6 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.00× (z +9.8) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 0.05 µM 0.371× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.432× (z -12.3) |
| [[HS-578T (line)]] | alt | 74.9 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.371× (z -11.6) |
| [[PANC-1 (line)]] | alt | 111 | 0 | 5 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.544× (z -11.6) ⚠ cell-cycle shift, explains ~29% of this change |
| [[RKO (line)]] | wt | 105 | 0 | 5 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.426× (z -10.9) |
| [[SW480 (line)]] | alt | 136 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.473× (z -13.3) |
| [[A498 (line)]] | wt | 93.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.507× (z -15.8) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.460× (z -12.8) |
| [[AsPC-1 (line)]] | alt | 95.7 | 0 | 3 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.462× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Trametinib (drug)]] 0.5 µM 0.520× (z -8.9) |
| [[C32 (line)]] | wt | 79.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -14.9) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.332× (z -11.9) |
| [[CFPAC-1 (line)]] | alt | 73.6 | 1 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.91× (z +12.1) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.558× (z -9.7) ⚠ cell-cycle shift, explains ~13% of this change |
| [[NCI-H1573 (line)]] | alt | 59.9 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.27× (z +10.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.490× (z -9.0) ⚠ cell-cycle shift, explains ~53% of this change |
| [[SNU-1 (line)]] | wt | 123 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -13.3) ⚠ cell-cycle shift, explains ~53% of this change |
| [[A-427 (line)]] | wt | 100 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -14.2) ⚠ cell-cycle shift, explains ~19% of this change |
| [[BT-474 (line)]] | alt | 73.2 | 0 | 2 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.178× (z -9.6) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.449× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 105 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -11.9) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.529× (z -9.4) |
| [[J82 (line)]] | alt | 74.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.545× (z -10.5) ⚠ cell-cycle shift, explains ~13% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.468× (z -9.3) |
| [[LoVo (line)]] | wt | 88.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.593× (z -10.9) ⚠ cell-cycle shift, explains ~53% of this change |
| [[LOX-IMVI (line)]] | wt | 68.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.553× (z -9.9) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.228× (z -9.2) |
| [[LS 180 (line)]] | wt | 86.5 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.352× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[NCI-H2030 (line)]] | alt | 56.4 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.315× (z -12.8) ⚠ cell-cycle shift, explains ~33% of this change |
| [[NCI-H23 (line)]] | alt | 69.1 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.289× (z -13.3) |
| [[RPMI-7951 (line)]] | alt | 77.0 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.301× (z -11.4) ⚠ transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.391× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 74.2 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.337× (z -11.9) |
| [[SW48 (line)]] | wt | 111 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.81× (z +10.0) ⚠ toxic; transcription drop | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.166× (z -17.3) ⚠ cell-cycle shift, explains ~19% of this change |
| [[C-33 A (line)]] | alt | 97.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.417× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 73.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.148× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[hTERT-HPNE (line)]] | wt | 75.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -12.9) ⚠ cell-cycle shift, explains ~53% of this change |
| [[NCI-H1792 (line)]] | alt | 81.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.69× (z +11.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 62.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.533× (z -10.8) ⚠ cell-cycle shift, explains ~13% of this change |
| [[Panc 03.27 (line)]] | alt | 74.6 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -8.7) |
| [[SNU-423 (line)]] | alt | 93.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.392× (z -11.0) |
| [[SW 1088 (line)]] | alt | 96.0 | 0 | 1 | — | [[Bestatin (hydrochloride) (drug)]] 0.05 µM 0.0690× (z -10.4) |
| [[SW 900 (line)]] | alt | 31.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[AN3 CA (line)]] | alt | 105 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 80.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 78.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 105 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 94.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 83.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 90.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 70.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 61.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 85.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4330), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPP3]] | +0.69 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[NLN]] | +0.64 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[EIF2B3]] | +0.62 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[PUS1]] | +0.60 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[DDX31]] | +0.60 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[WDR4]] | +0.60 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[NDUFAF2]] | +0.57 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[PDCD11]] | +0.57 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[RABEPK]] | +0.57 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[PUM3]] | +0.56 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[EIF3J]] | +0.55 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[MON1A]] | +0.55 | +0.58 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFNA1]] | -0.61 | -0.62 / -0.57 | both halves | 1e-05 |  |
| [[ITM2B]] | -0.53 | -0.63 / -0.44 | both halves | 3e-05 |  |
| [[SLC2A12]] | -0.51 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[CDKN1B]] | -0.50 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[CTDSPL2]] | -0.50 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[CASP10]] | -0.49 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[MINDY1]] | -0.48 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[SATB1]] | -0.48 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[TMEM59]] | -0.48 | -0.55 / -0.36 | both halves | 1e-04 |  |
| [[SP1]] | -0.48 | -0.43 / -0.36 | both halves | 1e-04 |  |
| [[BRWD3]] | -0.48 | -0.29 / -0.48 | both halves | 2e-04 |  |
| [[KDM3A]] | -0.47 | -0.30 / -0.53 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADCY3]] | B | ADCY3 activity raises SHLD2's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 1.32× lower at baseline in the lines without ADCY3 | 0.048 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |
| [[PRELID3A]] | C | PRELID3A activity raises SHLD2's level | lines that do not express PRELID3A (3) vs lines expressing it (47) | 1.21× lower at baseline in the lines without PRELID3A | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SLC4A7, HCN2, USP31 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.517). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-6.6, -36.0); signed map (-2.0, -50.5). **Vector** length 110, 30.0% of its response variance represented; |z| ≥ 3 in 1,334 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.4 | +5.2 |
|  | [[EX229 (drug)]] 5 µM |  | +3.9 | +3.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | -0.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | -1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.1 | +2.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.9 | +2.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.7 | +2.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.7 | +1.5 |
| fall | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | -6.3 | -7.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -5.5 | -6.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.6 | -2.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.5 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.3 | -4.8 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -4.3 | -4.7 |

## What is on record

|  |  |
|---|---|
| Name | shieldin complex subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q23.2 — chr10:87,094,161-87,191,465 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC5560, bA163M19.1, FAM35A1, RINN2; previously FAM35A |
| Gene groups (HGNC) | Shieldin complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86V20](https://www.uniprot.org/uniprotkb/Q86V20) (Shieldin complex subunit 2):

> Component of the shieldin complex, which plays an important role in repair of DNA double-stranded breaks (DSBs). During G1 and S phase of the cell cycle, the complex functions downstream of TP53BP1 to promote non-homologous end joining (NHEJ) and suppress DNA end resection. Mediates various NHEJ-dependent processes including immunoglobulin class-switch recombination, and fusion of unprotected telomeres.

**Summary**, from NCBI Gene [54537](https://www.ncbi.nlm.nih.gov/gene/54537):

> Involved in negative regulation of double-strand break repair via homologous recombination; positive regulation of double-strand break repair via nonhomologous end joining; and positive regulation of isotype switching. Located in nucleoplasm and site of double-strand break. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28773](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28773) · Entrez [54537](https://www.ncbi.nlm.nih.gov/gene/54537) · UniProt [Q86V20](https://www.uniprot.org/uniprotkb/Q86V20) · Ensembl [ENSG00000122376](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122376)

## Data

Gene col 4330: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4330); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4330, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4330]; `tensor/DDL_lfc|DDL_z.npy` [4330]; `embed/gene_vectors.npy` [4330]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4330 or target_col == 4330). Every well: [[SHLD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SHLD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
