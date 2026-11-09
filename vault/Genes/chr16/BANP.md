---
symbol: "BANP"
type: "gene"
col: 10265
ensembl_id: "ENSG00000172530"
name: "BTG3 associated nuclear protein"
location: "16q24.2"
module: 17
arm: "-"
pooled_cpm: 39.8
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 3
n_dd_up_clean: 21
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# BANP

*BTG3 associated nuclear protein* — 16q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (6 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.34× (z +14.1, q 2e-42, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.527× (z -10.3, q 4e-22, down in 30 of 40 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (NCI-H1573 0.154×, SHP-77 0.114×, A498 0.227×, LOX-IMVI 0.158×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (C32 0.217×, J82 0.265×, NCI-H1573 0.308×, LS 180 0.257×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (C32 0.126×, A-427 0.247×, C-33 A 0.215×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 3 lines (Panc 03.27 0.311×, C32 0.368×, SHP-77 0.347×); [[Ponatinib (drug)]] 5 µM in 1 line (AN3 CA 0.136×); [[Saquinavir (drug)]] 0.5 µM in 1 line (SNU-1 0.177×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DENND6A-AS1]] (+0.62, fdr 1e-04), [[DCAF4L1]] (+0.62, fdr 2e-05), [[PPP2R2D]] (+0.62, fdr 3e-05); moves opposite to [[MRPS31P4]] (-0.63, fdr 3e-05), [[SUGT1P4-STRA6LP]] (-0.61, fdr 2e-05), [[STRA6LP]] (-0.59, fdr 5e-05).
> It sits in the **-** arm of [[Module 017]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10265.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.34×** | +14.1 | 2e-42 | 44/48 (MIA PaCa-2, A-172, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.14×** | +12.6 | 6e-34 | 45/48 (COLO 205, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +11.2 | 1e-26 | 36/48 (MIA PaCa-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.82×** | +10.0 | 3e-21 | 40/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.05×** | +9.7 | 4e-20 | 36/49 (NCI-H2030, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +8.8 | 9e-17 | 36/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.67×** | +8.5 | 1e-15 | 33/48 (NCI-H1573, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.38×** | +7.6 | 2e-12 | 28/48 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.57×** | +7.5 | 5e-12 | 35/48 (LS 180, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.54×** | +7.2 | 3e-11 | 28/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +7.0 | 1e-10 | 29/47 (BT-474, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.41×** | +5.7 | 6e-07 | 30/48 (Hs 766T, PANC-1, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.40×** | +5.6 | 1e-06 | 32/48 (MIA PaCa-2, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +4.8 | 7e-05 | 24/47 (A498, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.35×** | +4.7 | 1e-04 | 23/48 (CFPAC-1, HT-29, …) | inconsistent across doses |  |
| [[Infigratinib (drug)]] 5 µM |  | **1.70×** | +4.6 | 1e-04 | 25/48 (A-172, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.34×** | +4.6 | 2e-04 | 25/47 (SW480, SW48, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +4.4 | 4e-04 | 23/49 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.30×** | +4.3 | 5e-04 | 21/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10265.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (NCI-H1573 0.154×, SHP-77 0.114×, A498 0.227×, LOX-IMVI 0.158×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (C32 0.217×, J82 0.265×, NCI-H1573 0.308×, LS 180 0.257×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (C32 0.126×, A-427 0.247×, C-33 A 0.215×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 3 lines (Panc 03.27 0.311×, C32 0.368×, SHP-77 0.347×); [[Ponatinib (drug)]] 5 µM in 1 line (AN3 CA 0.136×); [[Saquinavir (drug)]] 0.5 µM in 1 line (SNU-1 0.177×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.527×** | -10.3 | 4e-22 | 30/40 (NCI-H1573, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.532×** | -9.7 | 6e-20 | 33/43 (C32, A-427, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.587×** | -8.9 | 1e-16 | 36/47 (C32, J82, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | 0.820× | -3.1 | 0.30 | 17/47 (H4, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10265. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 28.0 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.227× (z -12.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 36.8 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +13.2) | [[Dinaciclib (drug)]] 0.5 µM 0.409× (z -9.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 29.4 | 4 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.84× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.414× (z -8.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 40.7 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.08× (z +10.5) | — |
| [[C32 (line)]] | wt | 84.4 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.126× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.368× (z -11.2) |
| [[HT-29 (line)]] | alt | 29.2 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.17× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.289× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 76.4 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.16× (z +17.6) | [[Dinaciclib (drug)]] 5 µM 0.314× (z -9.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 28.2 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.13× (z +9.6) | — |
| [[Hs 766T (line)]] | wt | 31.4 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.52× (z +9.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 49.4 | 2 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 5.66× (z +14.6) | [[Dinaciclib (drug)]] 0.5 µM 0.338× (z -9.2) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 82.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.114× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.347× (z -9.4) |
| [[SNU-423 (line)]] | alt | 35.7 | 2 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.07× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.279× (z -9.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 35.1 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.61× (z +12.6) | [[Dinaciclib (drug)]] 0.05 µM 0.312× (z -8.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 44.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.259× (z -11.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 52.2 | 0 | 2 (1 ⚠) | — | [[Ponatinib (drug)]] 5 µM 0.136× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 30.4 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.75× (z +11.5) | [[Lonafarnib (drug)]] 5 µM 0.133× (z -9.3) ⚠ toxic |
| [[HOP62 (line)]] | alt | 37.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +11.3) | — |
| [[HS-578T (line)]] | alt | 27.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +12.7) | [[Dinaciclib (drug)]] 0.05 µM 0.263× (z -9.3) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 28.3 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.63× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 50.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.154× (z -15.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 53.2 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.08× (z +10.9) | — |
| [[A549 (line)]] | wt | 28.0 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.97× (z +8.5) | — |
| [[AsPC-1 (line)]] | alt | 32.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.55× (z +10.4) | — |
| [[C-33 A (line)]] | alt | 49.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.215× (z -10.1) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 32.2 | 0 | 1 | — | [[Allantoin (drug)]] 0.5 µM 0.105× (z -8.5) |
| [[COLO 205 (line)]] | alt | 24.1 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 9.68× (z +13.2) | — |
| [[HCT15 (line)]] | alt | 47.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -10.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 39.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.265× (z -11.2) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 36.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -9.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 46.7 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.78× (z +9.0) | — |
| [[LOX-IMVI (line)]] | wt | 49.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -11.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 31.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +8.9) | — |
| [[Panc 03.27 (line)]] | alt | 33.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -12.4) |
| [[SNU-1 (line)]] | wt | 30.4 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.177× (z -9.2) |
| [[SW 900 (line)]] | alt | 41.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.327× (z -8.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 35.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 52.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 41.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 63.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 62.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 38.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10265), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DENND6A-AS1]] | +0.62 | +0.35 / +0.59 | both halves | 1e-04 |  |
| [[DCAF4L1]] | +0.62 | +0.51 / +0.46 | both halves | 2e-05 |  |
| [[PPP2R2D]] | +0.62 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[PRDM15]] | +0.60 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[DARS1-AS1]] | +0.60 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[CASS4]] | +0.59 | +0.46 / +0.43 | both halves | 3e-05 |  |
| [[ZFHX2-AS1]] | +0.59 | +0.43 / +0.48 | both halves | 3e-05 |  |
| [[ZNF460-AS1]] | +0.59 | +0.38 / +0.49 | both halves | 6e-05 |  |
| [[LRRC41]] | +0.59 | +0.27 / +0.52 | both halves | 3e-04 |  |
| [[MIATNB]] | +0.58 | +0.40 / +0.54 | both halves | 4e-05 |  |
| [[PRDM10]] | +0.58 | +0.34 / +0.48 | both halves | 1e-04 |  |
| [[SLC25A53]] | +0.58 | +0.37 / +0.52 | both halves | 7e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS31P4]] | -0.63 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[SUGT1P4-STRA6LP]] | -0.61 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[STRA6LP]] | -0.59 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[SUGT1P4-STRA6LP-CCDC180]] | -0.54 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[NDFIP2]] | -0.53 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[MNS1]] | -0.52 | -0.35 / -0.37 | both halves | 1e-04 |  |
| [[HOOK1]] | -0.52 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[ALDH7A1]] | -0.52 | -0.32 / -0.45 | both halves | 2e-04 |  |
| [[BBS5]] | -0.51 | -0.36 / -0.39 | both halves | 9e-05 |  |
| [[SSX2IP]] | -0.51 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[MPP1]] | -0.50 | -0.43 / -0.25 | both halves | 4e-04 |  |
| [[DDX19B]] | -0.50 | -0.35 / -0.42 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **-** arm (projection on the module's main direction -0.516). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-10.4, 27.9); signed map (9.8, 1.2). **Vector** length 95.2, 23.0% of its response variance represented; |z| ≥ 3 in 1,105 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +11.7 | +14.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.4 | +11.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.3 | +3.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +8.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.1 | +4.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.4 | +4.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.7 | +2.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +8.5 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -1.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -0.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | +0.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -0.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.7 | -2.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.6 | -1.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | -0.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -2.2 | -1.4 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.9 | -2.1 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -1.8 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | BTG3 associated nuclear protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q24.2 — chr16:87,949,244-88,077,318 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SMARBP1, SMAR1, FLJ20538, DKFZp761H172, FLJ10177, BEND1 |
| Gene groups (HGNC) | BEN domain containing |
| Reactome | 12 pathways, smallest: Regulation of TP53 Activity through Association with Co-factors; Degradation of CDH1; Regulation of CDH1 Function |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N9N5](https://www.uniprot.org/uniprotkb/Q8N9N5) (Protein BANP):

> Controls V(D)J recombination during T-cell development by repressing T-cell receptor (TCR) beta enhancer function (By similarity). Binds to scaffold/matrix attachment region beta (S/MARbeta), an ATC-rich DNA sequence located upstream of the TCR beta enhancer (By similarity). Represses cyclin D1 transcription by recruiting HDAC1 to its promoter, thereby diminishing H3K9ac, H3S10ph and H4K8ac levels. Promotes TP53 activation, which causes cell cycle arrest (By similarity). Plays a role in the …

**Summary**, from NCBI Gene [54971](https://www.ncbi.nlm.nih.gov/gene/54971):

> This gene encodes a protein that binds to matrix attachment regions. The protein forms a complex with p53 and negatively regulates p53 transcription, and functions as a tumor suppressor and cell cycle regulator. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Mar 2010]

**Accessions** — [HGNC:13450](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13450) · Entrez [54971](https://www.ncbi.nlm.nih.gov/gene/54971) · UniProt [Q8N9N5](https://www.uniprot.org/uniprotkb/Q8N9N5) · Ensembl [ENSG00000172530](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172530)

## Data

Gene col 10265: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10265); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10265, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10265]; `tensor/DDL_lfc|DDL_z.npy` [10265]; `embed/gene_vectors.npy` [10265]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10265 or target_col == 10265). Every well: [[BANP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BANP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
