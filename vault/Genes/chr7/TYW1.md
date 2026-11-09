---
symbol: "TYW1"
type: "gene"
col: 12717
ensembl_id: "ENSG00000198874"
name: "tRNA-yW synthesizing protein 1 homolog"
location: "7q11.21"
module: 36
arm: "+"
pooled_cpm: 90.19
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 9
n_dd_up_clean: 15
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# TYW1

*tRNA-yW synthesizing protein 1 homolog* — 7q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.11× (z +18.3, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.605× (z -12.4, q 2e-32, down in 37 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.882× (z -4.4, q 7e-04, down in 15 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (SW480 0.366×, A498 0.332×, PANC-1 0.417×, NCI-H23 0.337×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (PANC-1 0.275×, HCT15 0.122×, SW480 0.431×, SNU-1 0.170×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SK-MEL-2 0.290×; ⚠ toxic; transcription drop); [[Harringtonine (drug)]] 0.05 µM in 1 line (A549 0.419×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HIRA]] (+0.75, fdr 7e-06), [[IPO11]] (+0.71, fdr 7e-06), [[GTF3C2]] (+0.67, fdr 7e-06); moves opposite to [[NOTCH2NLC]] (-0.66, fdr 1e-05), [[CGGBP1]] (-0.65, fdr 1e-05), [[CDC42EP1]] (-0.63, fdr 2e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LACC1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12717.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.11×** | +18.3 | 0e+00 | 48/48 (LoVo, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.96×** | +16.5 | 0e+00 | 48/48 (LoVo, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.86×** | +15.3 | 0e+00 | 48/48 (AsPC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.41×** | +12.9 | 1e-35 | 44/49 (SW480, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.44×** | +8.9 | 5e-17 | 41/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.11×** | +7.8 | 5e-13 | 35/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.36×** | +7.6 | 3e-12 | 33/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.36×** | +7.5 | 6e-12 | 37/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.35×** | +7.4 | 6e-12 | 36/48 (PANC-1, NCI-H1792, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.37×** | +7.3 | 1e-11 | 36/48 (PANC-1, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.30×** | +6.5 | 4e-09 | 29/48 (AsPC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.30×** | +6.3 | 1e-08 | 29/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.29×** | +6.3 | 1e-08 | 27/48 (AsPC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.28×** | +6.1 | 6e-08 | 27/48 (HOP62, SW480, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.22×** | +4.7 | 1e-04 | 22/48 (COLO 205, HS-578T, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.21×** | +4.4 | 3e-04 | 22/47 (HEC-1-A, BT-474, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.45×** | +3.9 | 0.004 | 15/49 (AsPC-1, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | 1.17× | +3.8 | 0.005 | 8/48 (NCI-H1792, A498, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12717.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (SW480 0.366×, A498 0.332×, PANC-1 0.417×, NCI-H23 0.337×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (PANC-1 0.275×, HCT15 0.122×, SW480 0.431×, SNU-1 0.170×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SK-MEL-2 0.290×; ⚠ toxic; transcription drop); [[Harringtonine (drug)]] 0.05 µM in 1 line (A549 0.419×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.605×** | -12.4 | 2e-32 | 37/49 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.631×** | -10.9 | 2e-25 | 32/44 (PANC-1, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.727×** | -7.3 | 5e-11 | 29/45 (SK-MEL-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **0.767×** | -6.6 | 8e-09 | 28/48 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.772×** | -6.1 | 9e-08 | 28/48 (A498, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.819×** | -4.9 | 9e-05 | 23/49 (SW 1271, KATO III, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.830×** | -4.6 | 3e-04 | 24/48 (C32, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.882× | -4.4 | 7e-04 | 15/48 (SHP-77, A498, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.761×** | -4.0 | 0.004 | 22/47 (CHP-212, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.770×** | -3.8 | 0.007 | 17/48 (PANC-1, LS 180, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.902× | -3.6 | 0.015 | 17/49 (SHP-77, A498, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.870× | -3.2 | 0.068 | 19/47 (A549, SW 900, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Carbamazepine (drug)]] 5 µM |  | 0.881× | -3.2 | 0.070 | 4/47 (Panc 03.27, LOX-IMVI, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12717. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 135 | 9 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +18.8) | [[Dinaciclib (drug)]] 0.5 µM 0.366× (z -19.3) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 124 | 2 (1 ⚠) | 5 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 3.84× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.275× (z -21.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 128 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.332× (z -16.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 87.6 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.83× (z +15.3) | [[Dinaciclib (drug)]] 5 µM 0.436× (z -11.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 102 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +11.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.23× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.373× (z -12.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 89.9 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.42× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.296× (z -14.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 64.6 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.68× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.376× (z -11.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 66.5 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.46× (z +11.3) | [[Harringtonine (drug)]] 0.05 µM 0.419× (z -10.1) |
| [[AsPC-1 (line)]] | alt | 76.5 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.84× (z +14.7) | — |
| [[HEC-1-A (line)]] | alt | 110 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.24× (z +10.4) | — |
| [[KATO III (line)]] | alt | 114 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.04× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.452× (z -10.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 80.1 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.42× (z +13.9) | — |
| [[NCI-H460 (line)]] | wt | 81.1 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.30× (z +13.9) | — |
| [[BT-474 (line)]] | alt | 102 | 3 | 0 | [[Belinostat (drug)]] 5 µM 2.10× (z +9.0) | — |
| [[CFPAC-1 (line)]] | alt | 49.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.90× (z +11.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 97.5 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 6.71× (z +9.6) | — |
| [[RKO (line)]] | wt | 85.0 | 3 | 0 | [[Belinostat (drug)]] 5 µM 2.24× (z +9.5) | — |
| [[SNU-423 (line)]] | alt | 57.6 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.49× (z +9.4) | [[Dinaciclib (drug)]] 0.05 µM 0.359× (z -9.7) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 130 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.81× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.409× (z -12.9) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 63.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.122× (z -16.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 60.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.25× (z +10.2) | — |
| [[HS-578T (line)]] | alt | 64.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.51× (z +10.3) | — |
| [[J82 (line)]] | alt | 60.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.34× (z +10.0) | — |
| [[NCI-H23 (line)]] | alt | 78.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 1.92× (z +8.9) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 0.5 µM 0.337× (z -14.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 67.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.397× (z -10.2) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 93.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.170× (z -15.6) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 86.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.415× (z -8.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 94.1 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.419× (z -8.6) ⚠ cell-cycle shift, explains ~17% of this change |
| [[COLO 205 (line)]] | alt | 67.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 15.8× (z +10.3) | — |
| [[H4 (line)]] | wt | 64.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.11× (z +9.0) | — |
| [[HepG2_C3A (line)]] | wt | 78.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.350× (z -9.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 71.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.51× (z +9.4) | — |
| [[NCI-H1573 (line)]] | alt | 82.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.09× (z +9.6) | — |
| [[NCI-H2030 (line)]] | alt | 95.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.386× (z -11.5) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 76.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.13× (z +8.8) | — |
| [[SHP-77 (line)]] | alt | 164 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.540× (z -10.6) ⚠ cell-cycle shift, would explain all of this change |
| [[SW 1088 (line)]] | alt | 92.9 | 0 | 1 (1 ⚠) | — | [[Plicamycin (drug)]] 5 µM 0.0924× (z -9.0) ⚠ unreliable plate only |
| [[SW48 (line)]] | wt | 123 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.336× (z -10.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 85.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 116 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 96.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 95.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 48.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 72.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 83.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 94.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 66.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 93.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 87.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12717), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HIRA]] | +0.75 | +0.75 / +0.67 | both halves | 7e-06 |  |
| [[IPO11]] | +0.71 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[GTF3C2]] | +0.67 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[HERC2P9]] | +0.66 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[NFATC3]] | +0.66 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[TUFM]] | +0.65 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[CDK5RAP1]] | +0.65 | +0.59 / +0.60 | both halves | 7e-06 | same gene group; STRING 533 |
| [[EIF3K]] | +0.64 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[PARGP1]] | +0.63 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[UBE3C]] | +0.62 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[RNF216]] | +0.62 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[KNOP1]] | +0.62 | +0.53 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOTCH2NLC]] | -0.66 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[CGGBP1]] | -0.65 | -0.57 / -0.61 | both halves | 1e-05 |  |
| [[CDC42EP1]] | -0.63 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[LACC1]] | -0.62 | -0.57 / -0.46 | both halves | 3e-05 |  |
| [[MMRN2]] | -0.62 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[NOTCH2NLB]] | -0.60 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[SYNGAP1]] | -0.60 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[SOCS2]] | -0.59 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[ENO3]] | -0.59 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[ARMT1]] | -0.58 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[THAP9]] | -0.58 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[SYNPO]] | -0.58 | -0.50 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LACC1]] | B | LACC1 activity lowers TYW1's level | lines that do not express LACC1 (6) vs lines expressing it (44) | 1.36× higher at baseline in the lines without LACC1 | 0.069 | ⚠ within organs, on part of the lines; also absent: CCDC122, IL1RAP, NABP1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.740). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-9.7, -17.7); signed map (-49.9, -19.5). **Vector** length 105, 30.0% of its response variance represented; |z| ≥ 3 in 1,177 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[PH-797804 (drug)]] 5 µM |  | +5.1 | +7.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.1 | +12.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.4 | +7.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +3.3 | +7.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.0 | +16.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.6 | +4.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.0 | +2.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.0 | +3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.9 | +6.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -11.1 | -1.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -9.2 | -6.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -8.5 | -1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -7.6 | -4.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -7.2 | -4.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.5 | -2.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.4 | -3.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.8 | -2.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.6 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | tRNA-yW synthesizing protein 1 homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.21 — chr7:66,995,173-67,239,514 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10900, MGC23001, MGC60291, YPL207W, TYW1A; previously RSAFD1 |
| Gene groups (HGNC) | Radical S-adenosylmethionine domain containing; tRNA-yW synthesizing protein 1 homologs |
| Reactome | 4 pathways, smallest: Synthesis of wybutosine at G37 of tRNA(Phe); tRNA modification in the nucleus and cytosol; tRNA processing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NV66](https://www.uniprot.org/uniprotkb/Q9NV66) (S-adenosyl-L-methionine-dependent tRNA 4-demethylwyosine synthase TYW1):

> Involved in the biosynthesis of wybutosine, a hyper modified guanosine with a tricyclic base located at position 37 of eukaryotic phenylalanine tRNA (tRNA(Phe)) that contributes to maintenance of the translational reading frame. Catalyzes the condensation of N-methylguanine with 2 carbon atoms from pyruvate to form the tricyclic 4-demethylwyosine, an intermediate in wybutosine biosynthesis.

**Summary**, from NCBI Gene [55253](https://www.ncbi.nlm.nih.gov/gene/55253):

> Wybutosine (yW) is a hypermodified guanosine found in phenylalanine tRNA adjacent to the anticodon that stabilizes codon-anticodon interactions in the ribosome. In yeast, the homolog of this gene is essential for the synthesis of wybutosine. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2015]

**Accessions** — [HGNC:25598](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25598) · Entrez [55253](https://www.ncbi.nlm.nih.gov/gene/55253) · UniProt [Q9NV66](https://www.uniprot.org/uniprotkb/Q9NV66) · Ensembl [ENSG00000198874](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198874)

## Data

Gene col 12717: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12717); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12717, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12717]; `tensor/DDL_lfc|DDL_z.npy` [12717]; `embed/gene_vectors.npy` [12717]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12717 or target_col == 12717). Every well: [[TYW1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TYW1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
