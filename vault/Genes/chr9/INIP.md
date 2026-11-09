---
symbol: "INIP"
type: "gene"
col: 7245
ensembl_id: "ENSG00000148153"
name: "INTS3 and NABP interacting protein"
location: "9q32"
module: 17
arm: "+"
pooled_cpm: 37.23
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 7
n_dd_up_clean: 12
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# INIP

*INTS3 and NABP interacting protein* — 9q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.85× (z +26.3, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.695× (z -8.8, q 9e-16, down in 21 of 36 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.788× (z -8.4, q 9e-15, down in 30 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (NCI-H460 0.315×, AsPC-1 0.274×, KATO III 0.351×, C32 0.296×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (COLO 205 0.145×, H4 0.0914×, NCI-H23 0.202×, RKO 0.262×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (KATO III 0.185×, hTERT-HPNE 0.0762×, SW480 0.501×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A498 0.599×); [[Belumosudil (mesylate) (drug)]] 5 µM in 1 line (H4 0.0775×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPATCH11]] (+0.75, fdr 9e-06), [[SNAP29]] (+0.70, fdr 7e-06), [[RAD17]] (+0.67, fdr 2e-05); moves opposite to [[ATP11C]] (-0.64, fdr 1e-05), [[C2orf88]] (-0.63, fdr 2e-04), [[EPM2A]] (-0.63, fdr 3e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7245.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.85×** | +26.3 | 0e+00 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.63×** | +24.3 | 0e+00 | 47/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.94×** | +23.5 | 0e+00 | 45/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.45×** | +22.4 | 0e+00 | 46/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.82×** | +15.0 | 0e+00 | 36/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.99×** | +14.3 | 1e-44 | 40/49 (SW480, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.78×** | +13.8 | 1e-41 | 41/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.42×** | +8.8 | 1e-16 | 36/48 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +8.4 | 3e-15 | 35/47 (RKO, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.68×** | +6.8 | 8e-10 | 26/48 (SW480, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.30×** | +6.5 | 3e-09 | 25/48 (HEC-1-A, SW1417, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.29×** | +6.4 | 6e-09 | 23/47 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.23×** | +5.1 | 2e-05 | 22/48 (PANC-1, NCI-H1573, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.47×** | +5.0 | 2e-05 | 17/48 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.16× | +3.7 | 0.008 | 10/48 (MIA PaCa-2, C32, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | 1.17× | +3.7 | 0.009 | 8/47 (A-427, SNU-423, …) | inconsistent across doses | low cells (technical?) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.31×** | +3.5 | 0.014 | 5/48 (PANC-1, A-172, …) | inconsistent across doses | noisy plate (z scaled) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 1.10× | +3.4 | 0.020 | 2/48 (AN3 CA, H4) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7245.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (NCI-H460 0.315×, AsPC-1 0.274×, KATO III 0.351×, C32 0.296×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (COLO 205 0.145×, H4 0.0914×, NCI-H23 0.202×, RKO 0.262×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (KATO III 0.185×, hTERT-HPNE 0.0762×, SW480 0.501×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A498 0.599×); [[Belumosudil (mesylate) (drug)]] 5 µM in 1 line (H4 0.0775×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.695×** | -8.8 | 9e-16 | 21/36 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.788×** | -8.4 | 9e-15 | 30/48 (A498, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.719×** | -7.6 | 4e-12 | 23/42 (KATO III, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.819×** | -5.0 | 8e-05 | 14/48 (HS-578T, NCI-H460, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.823×** | -4.9 | 1e-04 | 17/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.805×** | -4.2 | 0.002 | 20/47 (COLO 205, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.857× | -3.7 | 0.016 | 16/48 (SK-MEL-2, HEC-1-A, …) | top dose only |  |
| [[Rapamycin (drug)]] 0.5 µM |  | 0.877× | -3.3 | 0.073 | 11/48 (RPMI-7951, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.782×** | -3.2 | 0.077 | 10/35 (HT-29, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.878× | -3.1 | 0.093 | 17/48 (HEC-1-A, hTERT-HPNE, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7245. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 38.3 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +21.8) | [[Dinaciclib (drug)]] 5 µM 0.315× (z -13.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 34.3 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +22.2) | — |
| [[RKO (line)]] | wt | 45.7 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -9.2) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 49.3 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.63× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.185× (z -16.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 30.9 | 6 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.21× (z +13.1) | — |
| [[SW480 (line)]] | alt | 50.1 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.48× (z +17.0) | [[Dinaciclib (drug)]] 0.05 µM 0.501× (z -8.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 36.8 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.346× (z -8.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 45.4 | 5 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.78× (z +12.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 34.3 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +12.7) | — |
| [[A498 (line)]] | wt | 60.1 | 3 | 1 | [[Panobinostat (drug)]] 0.5 µM 2.61× (z +13.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.599× (z -10.0) |
| [[HOP62 (line)]] | alt | 37.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +12.2) | — |
| [[Hs 766T (line)]] | wt | 51.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +11.4) | — |
| [[J82 (line)]] | alt | 46.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +12.0) | — |
| [[LoVo (line)]] | wt | 27.8 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.15× (z +13.1) | — |
| [[NCI-H1573 (line)]] | alt | 27.8 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +14.4) | — |
| [[A-172 (line)]] | wt | 25.9 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.12× (z +9.8) | — |
| [[SNU-423 (line)]] | alt | 37.0 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.07× (z +9.6) | — |
| [[COLO 205 (line)]] | alt | 57.5 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.14× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -13.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 43.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0914× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Belumosudil (mesylate) (drug)]] 5 µM 0.0775× (z -8.7) |
| [[HT-29 (line)]] | alt | 33.7 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.80× (z +9.1) | — |
| [[NCI-H1792 (line)]] | alt | 27.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +10.1) | — |
| [[NCI-H2030 (line)]] | alt | 19.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +14.6) | — |
| [[NCI-H23 (line)]] | alt | 42.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +13.0) | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -10.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 37.9 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.87× (z +9.2) | — |
| [[SK-MEL-2 (line)]] | alt | 37.8 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.65× (z +8.5) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.275× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 30.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.46× (z +12.1) | — |
| [[AsPC-1 (line)]] | alt | 33.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.274× (z -10.6) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 28.3 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.33× (z +9.7) | — |
| [[C32 (line)]] | wt | 33.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.296× (z -8.6) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 37.2 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.61× (z +8.5) | — |
| [[hTERT-HPNE (line)]] | wt | 32.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0762× (z -15.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 29.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.74× (z +9.0) | — |
| [[NCI-H2347 (line)]] | alt | 33.6 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.32× (z +9.4) | — |
| [[SNU-1 (line)]] | wt | 20.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +9.1) | — |
| [[SW1417 (line)]] | alt | 36.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.47× (z +8.5) | — |
| [[A-427 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 37.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 35.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7245), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPATCH11]] | +0.75 | +0.57 / +0.73 | both halves | 9e-06 |  |
| [[SNAP29]] | +0.70 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[RAD17]] | +0.67 | +0.67 / +0.47 | both halves | 2e-05 |  |
| [[ZMYM6]] | +0.66 | +0.66 / +0.42 | both halves | 4e-05 |  |
| [[ZNF184]] | +0.65 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[FRA10AC1]] | +0.64 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[POLM]] | +0.64 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[SENP2]] | +0.63 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[ISCA2]] | +0.62 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[MTRES1]] | +0.62 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[TTC26]] | +0.61 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[ZCCHC9]] | +0.60 | +0.61 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP11C]] | -0.64 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[C2orf88]] | -0.63 | -0.32 / -0.42 | both halves | 2e-04 |  |
| [[EPM2A]] | -0.63 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[ARSB]] | -0.62 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[CERS2]] | -0.61 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[PRRC2B]] | -0.61 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[POU6F1]] | -0.60 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[EME2]] | -0.60 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[CRPPA]] | -0.60 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[HCFC1]] | -0.58 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[SUMO3]] | -0.58 | -0.52 / -0.38 | both halves | 7e-05 |  |
| [[MKRN5P]] | -0.58 | -0.38 / -0.45 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.538). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-28.7, -2.1); signed map (-19.5, -9.7). **Vector** length 95.9, 22.8% of its response variance represented; |z| ≥ 3 in 1,028 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +5.0 | +26.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.6 | +22.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.2 | +14.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.8 | +24.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.8 | +23.5 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +1.6 | +1.5 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.5 | +1.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | +6.8 |
|  | [[Altretamine (drug)]] 5 µM |  | +1.5 | +1.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.5 | +5.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.9 | -8.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.3 | -3.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -6.3 | -4.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.3 | -7.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.2 | -3.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.5 | -5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.1 | +2.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.8 | -0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | -1.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.3 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | INTS3 and NABP interacting protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q32 — chr9:112,683,926-112,718,149 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC043, hSSBIP1, SOSS-C, MISE; previously C9orf80 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRY2](https://www.uniprot.org/uniprotkb/Q9NRY2) (SOSS complex subunit C):

> Component of the SOSS complex, a multiprotein complex that functions downstream of the MRN complex to promote DNA repair and G2/M checkpoint. The SOSS complex associates with single-stranded DNA at DNA lesions and influences diverse endpoints in the cellular DNA damage response including cell-cycle checkpoint activation, recombinational repair and maintenance of genomic stability. Required for efficient homologous recombination-dependent repair of double-strand breaks (DSBs) and ATM-dependent …

**Summary**, from NCBI Gene [58493](https://www.ncbi.nlm.nih.gov/gene/58493):

> The protein encoded by this gene is a subunit of single-stranded DNA binding complexes that are important for maintaining genome stability. These complexes are involved in G2/M checkpoint control and homologous recombination repair. [provided by RefSeq, Jul 2016]

**Accessions** — [HGNC:24994](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24994) · Entrez [58493](https://www.ncbi.nlm.nih.gov/gene/58493) · UniProt [Q9NRY2](https://www.uniprot.org/uniprotkb/Q9NRY2) · Ensembl [ENSG00000148153](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148153)

## Data

Gene col 7245: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7245); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7245, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7245]; `tensor/DDL_lfc|DDL_z.npy` [7245]; `embed/gene_vectors.npy` [7245]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7245 or target_col == 7245). Every well: [[INIP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/INIP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
