---
symbol: "STAT5B"
type: "gene"
col: 10425
ensembl_id: "ENSG00000173757"
name: "signal transducer and activator of transcription 5B"
location: "17q21.2"
module: 42
arm: "+"
pooled_cpm: 64.01
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 24
n_dd_up_clean: 1
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# STAT5B

*signal transducer and activator of transcription 5B* — 17q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 1.25× (z +4.9, q 5e-04, up in 18 of 50 measured lines) ⚠ cell-cycle shift, explains ~47% of this change. The strongest without an alert is [[Trametinib (drug)]] 0.05 µM: 1.14× (z +4.7, q 7e-04, up in 11 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A-427 2.28×, NCI-H2347 1.77×, HS-578T 1.77×; ⚠ cell-cycle shift, explains ~0% of this change); [[Trametinib (drug)]] 0.5 µM in 1 line (NCI-H460 1.81×); [[Harringtonine (drug)]] 5 µM in 1 line (HOP62 2.42×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A498 2.19×); [[Trametinib (drug)]] 0.05 µM in 1 line (NCI-H460 1.59×).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (14 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.488× (z -18.3, q 0e+00, down in 44 of 48 measured lines) ⚠ cell-cycle shift, explains ~46% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.393× (z -10.2, q 3e-22, down in 39 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF115]] (+0.67, fdr 1e-05), [[UBXN2A]] (+0.60, fdr 1e-05), [[TLCD5]] (+0.60, fdr 3e-05); moves opposite to [[TPM3]] (-0.61, fdr 2e-05), [[GNAI3]] (-0.60, fdr 3e-05), [[MLF2]] (-0.60, fdr 2e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LINC02970]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10425.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A-427 2.28×, NCI-H2347 1.77×, HS-578T 1.77×; ⚠ cell-cycle shift, explains ~0% of this change); [[Trametinib (drug)]] 0.5 µM in 1 line (NCI-H460 1.81×); [[Harringtonine (drug)]] 5 µM in 1 line (HOP62 2.42×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A498 2.19×); [[Trametinib (drug)]] 0.05 µM in 1 line (NCI-H460 1.59×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.25×** | +4.9 | 5e-04 | 18/50 (NCI-H460, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.14× | +4.7 | 7e-04 | 11/48 (NCI-H460, PANC-1, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +4.4 | 0.002 | 20/48 (HOP62, HS-578T, …) | top dose only | composition shift |
| [[Bimiralisib (drug)]] 0.05 µM |  | 1.20× | +4.4 | 0.002 | 12/49 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.15× | +4.2 | 0.003 | 13/48 (NCI-H460, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.18× | +4.2 | 0.003 | 15/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.46×** | +4.1 | 0.003 | 14/50 (NCI-H460, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 5 µM |  | 1.12× | +4.0 | 0.004 | 7/49 (Hs 766T, AsPC-1, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.10× | +3.4 | 0.036 | 4/48 (NCI-H2030, NCI-H23, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.15× | +3.3 | 0.049 | 10/49 (NCI-H460, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.09× | +3.1 | 0.086 | 5/49 (PANC-1, NCI-H460, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.13× | +3.1 | 0.097 | 10/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | 1.13× | +3.0 | 0.11 | 8/47 (PANC-1, C32, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 20 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10425.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.488×** | -18.3 | 0e+00 | 44/48 (PANC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.526×** | -16.3 | 0e+00 | 43/48 (PANC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.553×** | -15.1 | 0e+00 | 42/48 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.557×** | -13.8 | 6e-41 | 34/45 (SNU-423, SW480, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.393×** | -10.2 | 3e-22 | 39/49 (A549, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.691×** | -9.0 | 2e-17 | 36/50 (HOP62, SW 1271, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.790×** | -8.4 | 3e-15 | 27/49 (NCI-H2030, NCI-H23, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.732×** | -7.9 | 2e-13 | 31/48 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.742×** | -7.6 | 2e-12 | 30/48 (NCI-H2030, CHP-212, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.742×** | -7.6 | 2e-12 | 31/48 (C32, RKO, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.740×** | -7.4 | 1e-11 | 28/48 (HEC-1-A, SW 1271, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.757×** | -7.1 | 8e-11 | 31/48 (Panc 03.27, C32, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **0.768×** | -6.7 | 9e-10 | 31/48 (SW 1271, NCI-H2347, …) | all doses, flat | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.774×** | -6.5 | 3e-09 | 27/48 (C32, PANC-1, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.796×** | -5.8 | 3e-07 | 22/48 (PANC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.872× | -4.9 | 3e-05 | 19/48 (HOP62, SNU-423, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.830×** | -4.7 | 8e-05 | 21/47 (HEC-1-A, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.674×** | -4.3 | 5e-04 | 14/48 (NCI-H460, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.711×** | -3.7 | 0.006 | 10/48 (PANC-1, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | 0.862× | -3.5 | 0.011 | 15/48 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.727×** | -3.5 | 0.014 | 10/48 (PANC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.728×** | -3.5 | 0.014 | 13/48 (PANC-1, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.760×** | -3.0 | 0.056 | 11/47 (PANC-1, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.05 µM |  | 0.890× | -2.9 | 0.060 | 4/48 (C-33 A, PANC-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.922× | -2.9 | 0.070 | 8/48 (PANC-1, NCI-H2030, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.771×** | -2.8 | 0.082 | 13/48 (HEC-1-A, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.50 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10425. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 87.9 | 3 (1 ⚠) | 8 (8 ⚠) | [[Trametinib (drug)]] 0.5 µM 1.81× (z +9.8) | [[Panobinostat (drug)]] 5 µM 0.405× (z -12.3) ⚠ cell-cycle shift, explains ~46% of this change |
| [[HOP62 (line)]] | alt | 89.3 | 1 (1 ⚠) | 5 (4 ⚠) | [[Harringtonine (drug)]] 5 µM 2.42× (z +9.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -11.1) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.513× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 53.9 | 0 | 6 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.273× (z -13.7) ⚠ cell-cycle shift, explains ~46% of this change |
| [[C32 (line)]] | wt | 57.3 | 0 | 5 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.326× (z -10.0) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 76.8 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.369× (z -12.1) ⚠ cell-cycle shift, explains ~43% of this change |
| [[PANC-1 (line)]] | alt | 124 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.195× (z -22.1) ⚠ cell-cycle shift, explains ~46% of this change |
| [[A549 (line)]] | wt | 82.3 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.352× (z -11.9) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.167× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 78.1 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.464× (z -14.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.463× (z -10.1) |
| [[LoVo (line)]] | wt | 41.2 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.252× (z -15.5) ⚠ cell-cycle shift, explains ~46% of this change |
| [[NCI-H2030 (line)]] | alt | 97.4 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -14.8) ⚠ cell-cycle shift, explains ~49% of this change |
| [[SW480 (line)]] | alt | 56.4 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.361× (z -13.4) ⚠ cell-cycle shift, explains ~46% of this change |
| [[SNU-423 (line)]] | alt | 63.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.263× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[SW 1271 (line)]] | alt | 71.0 | 0 | 3 (3 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0745× (z -10.2) ⚠ cell-cycle shift, explains ~49% of this change |
| [[C-33 A (line)]] | alt | 73.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 121 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.320× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 52.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Belinostat (drug)]] 5 µM 0.447× (z -9.1) ⚠ cell-cycle shift, explains ~48% of this change |
| [[NCI-H661 (line)]] | alt | 45.5 | 0 | 2 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0799× (z -10.1) |
| [[A-427 (line)]] | wt | 35.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A498 (line)]] | wt | 49.9 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.19× (z +9.1) | — |
| [[AsPC-1 (line)]] | alt | 49.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -10.7) ⚠ cell-cycle shift, explains ~49% of this change |
| [[HCT15 (line)]] | alt | 67.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0780× (z -21.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 44.8 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0953× (z -17.2) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 69.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[KATO III (line)]] | alt | 60.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.390× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[LS 180 (line)]] | wt | 52.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.344× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[NCI-H1573 (line)]] | alt | 31.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.370× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 49.5 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -12.2) ⚠ cell-cycle shift, explains ~49% of this change |
| [[RKO (line)]] | wt | 52.3 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.373× (z -8.8) ⚠ cell-cycle shift, explains ~48% of this change |
| [[SHP-77 (line)]] | alt | 84.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.303× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[SK-MEL-2 (line)]] | alt | 71.8 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.382× (z -9.8) ⚠ cell-cycle shift, explains ~43% of this change |
| [[SW 1088 (line)]] | alt | 64.7 | 0 | 1 | — | [[Zileuton (drug)]] 5 µM 0.0592× (z -8.7) |
| [[SW1417 (line)]] | alt | 52.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.330× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[SW48 (line)]] | wt | 54.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.209× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 53.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 116 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 75.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 44.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 83.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 39.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 86.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 64.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 49.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 41.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10425), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF115]] | +0.67 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[UBXN2A]] | +0.60 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[TLCD5]] | +0.60 | +0.55 / +0.46 | both halves | 3e-05 |  |
| [[DSTYK]] | +0.59 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[LSM14A]] | +0.58 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[RUFY1]] | +0.58 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[HACD1]] | +0.57 | +0.47 / +0.41 | both halves | 4e-05 |  |
| [[ITSN2]] | +0.57 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[AGO4]] | +0.56 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[KDM3B]] | +0.55 | +0.57 / +0.37 | both halves | 7e-05 |  |
| [[THAP3]] | +0.55 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[RNF146]] | +0.55 | +0.48 / +0.49 | both halves | 2e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPM3]] | -0.61 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[GNAI3]] | -0.60 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[MLF2]] | -0.60 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[SAR1A]] | -0.59 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[DCUN1D3]] | -0.56 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[PMPCA]] | -0.56 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[LINC02458]] | -0.54 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[NAPG]] | -0.54 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[GDAP2]] | -0.53 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[ARPC2]] | -0.53 | -0.54 / -0.40 | both halves | 5e-05 |  |
| [[ATG16L1]] | -0.53 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[RNGTT]] | -0.52 | -0.47 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02970]] | B | LINC02970 activity raises STAT5B's level | lines that do not express LINC02970 (24) vs lines expressing it (26) | 1.16× lower at baseline in the lines without LINC02970 | 0.068 | ⚠ within organs, on part of the lines; also absent: TOX, MXRA5, ENSG00000255595 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction -0.456). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-13.4, 11.5); signed map (7.1, -7.0). **Vector** length 88.1, 19.9% of its response variance represented; |z| ≥ 3 in 1,218 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.2 | +4.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, would explain all of this change | +4.8 | -0.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.6 | +0.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.5 | -4.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.4 | +0.5 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +3.2 | +4.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | -1.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.9 | +4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.9 | +2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.8 | +2.9 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -4.0 | -10.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -2.9 | -16.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -2.9 | -8.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -2.8 | -18.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | -7.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | -4.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.4 | -3.5 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.1 | -3.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.0 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | signal transducer and activator of transcription 5B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.2 — chr17:42,199,176-42,288,633 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | SH2 domain containing; Signal transducer and activator of transcription family |
| Reactome | 36 pathways, smallest: Erythropoietin activates STAT5; STAT5 Activation; Interleukin-9 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P51692](https://www.uniprot.org/uniprotkb/P51692) (Signal transducer and activator of transcription 5B):

> Signal transducer and transcription activator that mediates cellular responses to cytokines, hormones and growth factors. Binds to the GAS element and activates PRL-induced transcription. Positively regulates hematopoietic/erythroid differentiation. Involved in the oncostatin-M-mediated signaling pathway through type II OSM receptor complex (heterodimers composed of OSMR and IL6ST).

**Summary**, from NCBI Gene [6777](https://www.ncbi.nlm.nih.gov/gene/6777):

> The protein encoded by this gene is a member of the STAT family of transcription factors. In response to cytokines and growth factors, STAT family members are phosphorylated by the receptor associated kinases, and then form homo- or heterodimers that translocate to the cell nucleus where they act as transcription activators. This protein mediates the signal transduction triggered by various cell ligands, such as IL2, IL4, CSF1, and different growth hormones. It has been shown to be involved in …

**Accessions** — [HGNC:11367](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11367) · Entrez [6777](https://www.ncbi.nlm.nih.gov/gene/6777) · UniProt [P51692](https://www.uniprot.org/uniprotkb/P51692) · Ensembl [ENSG00000173757](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173757)

## Data

Gene col 10425: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10425); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10425, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10425]; `tensor/DDL_lfc|DDL_z.npy` [10425]; `embed/gene_vectors.npy` [10425]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10425 or target_col == 10425). Every well: [[STAT5B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STAT5B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
