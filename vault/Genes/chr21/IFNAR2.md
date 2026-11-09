---
symbol: "IFNAR2"
type: "gene"
col: 8216
ensembl_id: "ENSG00000159110"
name: "interferon alpha and beta receptor subunit 2"
location: "21q22.11"
module: 14
arm: "+"
pooled_cpm: 73.82
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 26
n_dd_up_clean: 7
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# IFNAR2

*interferon alpha and beta receptor subunit 2* — 21q22.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.35× (z +10.5, q 5e-23, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.468× (z -18.7, q 0e+00, down in 41 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.513× (z -16.5, q 0e+00, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TNFRSF1B]] (+0.58, fdr 4e-05), [[C15orf48]] (+0.57, fdr 1e-05), [[PPP4R4]] (+0.56, fdr 1e-05); moves opposite to [[WDR13]] (-0.51, fdr 4e-05), [[EXOC7]] (-0.48, fdr 6e-05), [[MCM3AP]] (-0.46, fdr 5e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8216.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +10.5 | 5e-23 | 36/48 (HEC-1-A, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.41×** | +8.5 | 7e-15 | 33/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.41×** | +8.3 | 3e-14 | 31/47 (CFPAC-1, AsPC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.25×** | +5.5 | 6e-06 | 23/48 (SW480, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.24×** | +5.2 | 2e-05 | 22/49 (CFPAC-1, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 1.19× | +5.1 | 3e-05 | 19/50 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.17× | +4.6 | 4e-04 | 15/48 (CFPAC-1, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Gemcitabine (drug)]] 0.5 µM |  | 1.18× | +4.2 | 0.002 | 11/48 (PANC-1, J82, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 1.18× | +4.1 | 0.002 | 15/49 (CFPAC-1, LOX-IMVI, …) | two highest doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.18× | +4.1 | 0.003 | 14/47 (CFPAC-1, AsPC-1, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 1.18× | +3.9 | 0.004 | 10/48 (CFPAC-1, A-172, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.36×** | +3.9 | 0.005 | 15/49 (SW480, A-172, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.8 | 0.006 | 19/48 (SW480, A-172, …) | inconsistent across doses |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 1.17× | +3.8 | 0.006 | 15/48 (HOP62, J82, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.34×** | +3.7 | 0.007 | 22/49 (LoVo, BT-474, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.11× | +3.7 | 0.008 | 6/48 (AsPC-1, HS-578T, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.12× | +3.5 | 0.013 | 12/48 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Cyclosporin A (drug)]] 5 µM |  | 1.15× | +3.5 | 0.016 | 8/48 (AsPC-1, LoVo, …) | top dose only | position effect removed |
| [[Ferulic acid (drug)]] 0.5 µM |  | 1.15× | +3.4 | 0.017 | 8/47 (J82, H4, …) | two highest doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8216.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.468×** | -18.7 | 0e+00 | 41/48 (NCI-H23, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.513×** | -16.5 | 0e+00 | 41/48 (A498, HT-29, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.508×** | -16.1 | 0e+00 | 34/42 (A498, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.578×** | -13.5 | 2e-39 | 39/48 (MIA PaCa-2, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.704×** | -12.2 | 3e-32 | 39/48 (NCI-H2347, NCI-H1792, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.611×** | -12.1 | 8e-32 | 40/48 (A498, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.618×** | -11.0 | 5e-26 | 32/44 (A549, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.673×** | -9.8 | 1e-20 | 30/48 (LOX-IMVI, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.658×** | -9.7 | 2e-20 | 34/48 (A498, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.784×** | -8.5 | 1e-15 | 34/48 (A549, A-172, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.716×** | -8.2 | 1e-14 | 27/48 (LS 180, RKO, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.757×** | -6.9 | 3e-10 | 27/48 (RKO, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.760×** | -6.7 | 7e-10 | 27/48 (LS 180, J82, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.759×** | -6.5 | 3e-09 | 29/47 (NCI-H23, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.739×** | -6.5 | 4e-09 | 31/48 (NCI-H2030, Panc 03.27, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.772×** | -6.4 | 8e-09 | 28/48 (LOX-IMVI, SNU-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.804×** | -5.3 | 3e-06 | 22/48 (A549, LOX-IMVI, …) | all doses, flat |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.720×** | -4.1 | 1e-03 | 19/48 (A498, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | 0.846× | -4.1 | 1e-03 | 10/48 (CFPAC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.851× | -4.0 | 0.002 | 16/48 (PANC-1, A-172, …) | top dose only |  |
| [[Ixazomib (drug)]] 5 µM |  | **0.753×** | -3.6 | 0.009 | 9/48 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8216. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 165 | 0 | 14 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.249× (z -21.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.362× (z -10.6) |
| [[NCI-H23 (line)]] | alt | 104 | 0 | 10 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.212× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.436× (z -9.7) |
| [[NCI-H2030 (line)]] | alt | 120 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -17.0) ⚠ cell-cycle shift, explains ~79% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.395× (z -11.2) |
| [[PANC-1 (line)]] | alt | 74.9 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.276× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.428× (z -9.4) |
| [[A498 (line)]] | wt | 146 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.258× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.348× (z -13.8) |
| [[LOX-IMVI (line)]] | wt | 60.2 | 1 | 5 (1 ⚠) | [[Cobimetinib (drug)]] 5 µM 2.43× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -18.0) ⚠ cell-cycle shift, explains ~79% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.259× (z -14.0) |
| [[LoVo (line)]] | wt | 95.7 | 2 (1 ⚠) | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 12.0× (z +14.9) | [[Dinaciclib (drug)]] 0.5 µM 0.445× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.572× (z -9.3) |
| [[RKO (line)]] | wt | 64.4 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.306× (z -11.1) |
| [[HEC-1-A (line)]] | alt | 59.0 | 1 | 3 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.71× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.571× (z -9.8) ⚠ cell-cycle shift, explains ~79% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.502× (z -8.5) |
| [[HT-29 (line)]] | alt | 49.1 | 0 | 4 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.345× (z -10.5) |
| [[LS 180 (line)]] | wt | 51.0 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.267× (z -13.5) |
| [[NCI-H460 (line)]] | wt | 31.2 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.452× (z -11.7) ⚠ cell-cycle shift, explains ~79% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.390× (z -9.8) |
| [[Panc 03.27 (line)]] | alt | 97.5 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -16.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.405× (z -9.5) |
| [[SW480 (line)]] | alt | 46.7 | 2 | 2 | [[Panobinostat (drug)]] 0.05 µM 2.01× (z +9.3) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.459× (z -10.3) |
| [[A-172 (line)]] | wt | 69.3 | 2 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.78× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.444× (z -9.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 88.0 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +12.1) ⚠ cell-cycle shift, explains ~79% of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 2.60× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.233× (z -13.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 61.8 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +13.8) ⚠ cell-cycle shift, explains ~79% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 12.7× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.244× (z -9.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 60.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -13.0) ⚠ cell-cycle shift, explains ~79% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.273× (z -10.6) |
| [[CFPAC-1 (line)]] | alt | 71.5 | 2 | 1 | [[Cobimetinib (drug)]] 5 µM 2.82× (z +9.8) | [[Selinexor (drug)]] 5 µM 0.540× (z -8.5) |
| [[HS-578T (line)]] | alt | 74.6 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +19.8) ⚠ cell-cycle shift, explains ~79% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.76× (z +13.9) | — |
| [[J82 (line)]] | alt | 47.7 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.383× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.440× (z -8.7) |
| [[NCI-H1573 (line)]] | alt | 164 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 47.9 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.476× (z -11.6) |
| [[SW1417 (line)]] | alt | 52.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.269× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.415× (z -8.5) |
| [[COLO 205 (line)]] | alt | 83.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -10.8) ⚠ cell-cycle shift, explains ~79% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.367× (z -8.6) |
| [[HCT15 (line)]] | alt | 46.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.148× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.298× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 90.6 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.304× (z -11.0) |
| [[NCI-H1792 (line)]] | alt | 90.9 | 0 | 2 | — | [[Selinexor (drug)]] 5 µM 0.487× (z -10.4) |
| [[SK-MEL-2 (line)]] | alt | 71.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.172× (z -16.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 59.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.131× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.279× (z -9.2) |
| [[SNU-423 (line)]] | alt | 63.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +10.9) ⚠ cell-cycle shift, explains ~79% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -9.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 60.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.159× (z -13.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 70.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.389× (z -10.3) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 96.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.211× (z -15.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 55.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +12.8) ⚠ cell-cycle shift, explains ~79% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 82.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +13.9) ⚠ cell-cycle shift, explains ~79% of this change | — |
| [[KATO III (line)]] | alt | 44.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.411× (z -8.6) |
| [[SHP-77 (line)]] | alt | 55.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.240× (z -13.3) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 67.7 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.217× (z -12.0) ⚠ transcription drop; cell-cycle shift, explains ~34% of this change |
| [[AN3 CA (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 36.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 68.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 54.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 53.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 63.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8216), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNFRSF1B]] | +0.58 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[C15orf48]] | +0.57 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[PPP4R4]] | +0.56 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[SLC25A37]] | +0.55 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[TNFAIP6]] | +0.55 | +0.48 / +0.61 | both halves | 2e-05 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[DTX2]] | +0.55 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[RNF144B]] | +0.55 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[GBP2]] | +0.55 | +0.50 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_ALLOGRAFT_REJECTION |
| [[SLC11A2]] | +0.55 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[TNFAIP2]] | +0.54 | +0.53 / +0.61 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[ICAM1]] | +0.54 | +0.53 / +0.50 | both halves | 1e-05 | pathway: HALLMARK_ALLOGRAFT_REJECTION |
| [[TNFAIP8]] | +0.54 | +0.50 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR13]] | -0.51 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[EXOC7]] | -0.48 | -0.38 / -0.46 | both halves | 6e-05 |  |
| [[MCM3AP]] | -0.46 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[AVEN]] | -0.45 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[DVL3]] | -0.45 | -0.39 / -0.38 | both halves | 7e-05 |  |
| [[SUCLA2]] | -0.44 | -0.32 / -0.42 | both halves | 2e-04 |  |
| [[LY6G5B]] | -0.44 | -0.31 / -0.42 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers IFNAR2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[C15orf48]] | B | C15orf48 activity raises IFNAR2's level | lines that do not express C15orf48 (25) vs lines expressing it (25) | 1.33× lower at baseline in the lines without C15orf48 | 0.092 | ⚠ within organs, on part of the lines; also absent: ZNF229, HMGN2P46, RHCG |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.545). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.4, 1.9); signed map (43.3, 12.5). **Vector** length 127, 38.3% of its response variance represented; |z| ≥ 3 in 1,461 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.3 | +10.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.0 | +8.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.4 | +5.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.4 | +8.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.3 | +3.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.3 | +3.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.3 | +5.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -10.6 | -16.5 |
|  | [[Selinexor (drug)]] 5 µM |  | -8.8 | -12.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.0 | -16.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -6.7 | -13.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.6 | -12.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | -5.2 | -4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.2 | -8.5 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -3.3 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | interferon alpha and beta receptor subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.11 — chr21:33,205,282-33,265,675 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously IFNABR |
| Gene groups (HGNC) | Interferon receptors |
| Hallmark sets | ALLOGRAFT_REJECTION, INTERFERON_GAMMA_RESPONSE |
| Reactome | 13 pathways, smallest: Regulation of IFNA/IFNB signaling; Evasion by RSV of host interferon responses; Interferon alpha/beta signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P48551](https://www.uniprot.org/uniprotkb/P48551) (Interferon alpha/beta receptor 2):

> Together with IFNAR1, forms the heterodimeric receptor for type I interferons (including interferons alpha, beta, epsilon, omega and kappa). Type I interferon binding activates the JAK-STAT signaling cascade, resulting in transcriptional activation or repression of interferon-regulated genes that encode the effectors of the interferon response. Mechanistically, type I interferon-binding brings the IFNAR1 and IFNAR2 subunits into close proximity with one another, driving their associated Janus …

**Summary**, from NCBI Gene [3455](https://www.ncbi.nlm.nih.gov/gene/3455):

> The protein encoded by this gene is a type I membrane protein that forms one of the two chains of a receptor for interferons alpha and beta. Binding and activation of the receptor stimulates Janus protein kinases, which in turn phosphorylate several proteins, including STAT1 and STAT2. The protein belongs to the type II cytokine receptor family. Mutations in this gene are associated with Immunodeficiency 45. [provided by RefSeq, Jul 2020]

**Accessions** — [HGNC:5433](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5433) · Entrez [3455](https://www.ncbi.nlm.nih.gov/gene/3455) · UniProt [P48551](https://www.uniprot.org/uniprotkb/P48551) · Ensembl [ENSG00000159110](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159110)

## Data

Gene col 8216: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8216); `tables/drug_effects.parquet` (74 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8216, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8216]; `tensor/DDL_lfc|DDL_z.npy` [8216]; `embed/gene_vectors.npy` [8216]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8216 or target_col == 8216). Every well: [[IFNAR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IFNAR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
