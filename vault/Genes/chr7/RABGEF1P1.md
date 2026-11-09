---
symbol: "RABGEF1P1"
type: "gene"
col: 13696
ensembl_id: "ENSG00000229180"
name: "RABGEF1 pseudogene 1"
location: "7q11.21"
module: 3
arm: "+"
pooled_cpm: 53.24
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 21
n_dd_up_clean: 15
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# RABGEF1P1

*RABGEF1 pseudogene 1* — 7q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 10.7× (z +22.5, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.312× (z -20.5, q 0e+00, down in 44 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 0.724× (z -8.3, q 2e-14, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBE2R2]] (+0.68, fdr 7e-06), [[MARK4]] (+0.68, fdr 7e-06), [[MAP2K1]] (+0.67, fdr 1e-05); moves opposite to [[LIN7C]] (-0.68, fdr 1e-05), [[MCCC2]] (-0.62, fdr 8e-06), [[GMFB]] (-0.62, fdr 2e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13696.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **10.7×** | +22.5 | 0e+00 | 48/49 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **5.00×** | +15.3 | 0e+00 | 43/48 (HEC-1-A, SW480, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.27×** | +14.9 | 0e+00 | 44/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.13×** | +13.7 | 1e-40 | 42/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.84×** | +11.1 | 2e-26 | 39/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.82×** | +10.8 | 2e-25 | 41/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **2.15×** | +7.3 | 3e-11 | 38/48 (CFPAC-1, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.42×** | +6.3 | 2e-08 | 32/48 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.36×** | +5.5 | 2e-06 | 26/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.23×** | +5.2 | 9e-06 | 22/49 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.45×** | +4.8 | 8e-05 | 24/49 (LoVo, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.30×** | +4.5 | 3e-04 | 21/48 (CFPAC-1, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.25×** | +4.1 | 0.002 | 23/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +4.1 | 0.002 | 21/48 (LS 180, KATO III, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.49×** | +3.8 | 0.006 | 17/45 (PANC-1, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.5 µM |  | **1.33×** | +3.7 | 0.008 | 15/48 (HEC-1-A, PANC-1, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.21×** | +3.4 | 0.019 | 14/48 (CFPAC-1, LS 180, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.29×** | +3.3 | 0.032 | 10/48 (NCI-H1792, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13696.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.312×** | -20.5 | 0e+00 | 44/47 (A-427, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.306×** | -19.9 | 0e+00 | 40/45 (A498, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.326×** | -19.6 | 0e+00 | 39/42 (A549, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.724×** | -8.3 | 2e-14 | 37/48 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.644×** | -7.7 | 2e-12 | 36/48 (MIA PaCa-2, RKO, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.699×** | -6.5 | 8e-09 | 30/48 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.707×** | -6.3 | 3e-08 | 33/48 (AsPC-1, A-427, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.721×** | -5.9 | 2e-07 | 27/48 (LoVo, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.723×** | -5.7 | 9e-07 | 33/48 (AsPC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.783×** | -4.5 | 5e-04 | 26/48 (LOX-IMVI, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.785×** | -4.4 | 6e-04 | 24/47 (KATO III, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.787×** | -4.2 | 0.001 | 19/49 (AsPC-1, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.796×** | -4.0 | 0.003 | 22/48 (A-172, A498, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.799×** | -3.8 | 0.007 | 20/48 (AsPC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.865× | -3.7 | 0.007 | 14/48 (A-172, NCI-H661, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.866× | -3.7 | 0.008 | 20/48 (NCI-H2347, NCI-H1573, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.812×** | -3.7 | 0.008 | 20/47 (MIA PaCa-2, AsPC-1, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.851× | -3.5 | 0.014 | 18/48 (AsPC-1, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.827×** | -3.5 | 0.015 | 20/48 (AsPC-1, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13696. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 56.0 | 8 (2 ⚠) | 3 (3 ⚠) | [[Digitoxin (drug)]] 5 µM 3.57× (z +17.1) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 9.93× (z +16.1) | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -22.7) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 64.9 | 8 (2 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 7.49× (z +17.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.05 µM 6.09× (z +15.9) | [[Dinaciclib (drug)]] 0.05 µM 0.229× (z -12.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 51.3 | 6 (1 ⚠) | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 16.9× (z +12.2) | [[Dinaciclib (drug)]] 0.5 µM 0.196× (z -13.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 116 | 2 | 6 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.84× (z +12.0) | [[Selinexor (drug)]] 5 µM 0.384× (z -16.1) |
| [[KATO III (line)]] | alt | 42.8 | 4 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 11.9× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.300× (z -10.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 55.6 | 4 (1 ⚠) | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 10.1× (z +13.2) | [[Dinaciclib (drug)]] 0.05 µM 0.169× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.432× (z -9.1) |
| [[LS 180 (line)]] | wt | 31.5 | 5 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 5.75× (z +14.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 5.04× (z +13.3) | [[Dinaciclib (drug)]] 0.05 µM 0.194× (z -12.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 96.0 | 1 | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 17.4× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.0692× (z -21.8) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.481× (z -8.8) |
| [[PANC-1 (line)]] | alt | 40.0 | 5 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 13.0× (z +14.6) | [[Dinaciclib (drug)]] 0.5 µM 0.323× (z -11.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 51.9 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 10.2× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.196× (z -13.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 75.0 | 1 | 4 (4 ⚠) | [[PH-797804 (drug)]] 5 µM 14.2× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.0929× (z -14.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 64.7 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 12.9× (z +14.0) | [[Dinaciclib (drug)]] 5 µM 0.178× (z -17.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 52.7 | 1 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 11.2× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.198× (z -12.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 64.8 | 5 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.66× (z +14.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.83× (z +12.7) | — |
| [[SK-MEL-2 (line)]] | alt | 75.6 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 13.3× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.131× (z -18.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 59.0 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.124× (z -22.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 57.2 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 9.72× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.0662× (z -25.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 44.6 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 10.7× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.249× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.487× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 69.4 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 13.5× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -11.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 35.9 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 12.8× (z +11.5) | [[Dinaciclib (drug)]] 0.05 µM 0.0835× (z -19.7) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 48.5 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 7.45× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.276× (z -12.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 57.7 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.99× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.0872× (z -23.0) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 54.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0662× (z -18.9) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 59.2 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 14.6× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.194× (z -9.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 47.9 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 8.95× (z +10.9) | [[Dinaciclib (drug)]] 0.05 µM 0.274× (z -11.3) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 42.5 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.50× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.174× (z -15.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 60.0 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 12.8× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.104× (z -18.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 39.5 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 23.1× (z +12.9) | [[Dinaciclib (drug)]] 0.05 µM 0.306× (z -8.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 40.4 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 13.8× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.162× (z -11.3) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 49.2 | 2 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 20.6× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -11.9) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 43.9 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 12.2× (z +10.1) | [[Dinaciclib (drug)]] 0.05 µM 0.110× (z -15.7) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 71.7 | 2 (1 ⚠) | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 18.5× (z +8.9) | [[Dinaciclib (drug)]] 0.05 µM 0.0764× (z -13.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 53.9 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 15.8× (z +12.1) | — |
| [[SW 900 (line)]] | alt | 46.3 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 19.0× (z +10.9) | — |
| [[BT-474 (line)]] | alt | 47.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 9.48× (z +8.8) | — |
| [[COLO 205 (line)]] | alt | 19.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 24.7× (z +8.6) | — |
| [[HCT15 (line)]] | alt | 42.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0947× (z -13.9) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 39.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 10.1× (z +9.4) | — |
| [[hTERT-HPNE (line)]] | wt | 53.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 32.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.83× (z +9.1) | — |
| [[Panc 03.27 (line)]] | alt | 33.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 11.6× (z +10.2) | — |
| [[SHP-77 (line)]] | alt | 44.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.179× (z -13.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 79.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 51.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 37.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 60.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13696), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2R2]] | +0.68 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[MARK4]] | +0.68 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[MAP2K1]] | +0.67 | +0.74 / +0.55 | both halves | 1e-05 |  |
| [[PRKRIP1]] | +0.67 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[SLC35E1]] | +0.65 | +0.69 / +0.57 | both halves | 9e-06 |  |
| [[RABGEF1]] | +0.64 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[FAAP20]] | +0.64 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[CSNK1G2]] | +0.63 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[FOXK2]] | +0.63 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[TMEM38A]] | +0.63 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[SEC61G]] | +0.62 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[MICOS13]] | +0.62 | +0.60 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIN7C]] | -0.68 | -0.55 / -0.69 | both halves | 1e-05 |  |
| [[MCCC2]] | -0.62 | -0.60 / -0.57 | both halves | 8e-06 |  |
| [[GMFB]] | -0.62 | -0.47 / -0.64 | both halves | 2e-05 |  |
| [[SCRN1]] | -0.62 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[HACD2]] | -0.60 | -0.47 / -0.64 | both halves | 2e-05 |  |
| [[SF3A1]] | -0.60 | -0.40 / -0.66 | both halves | 5e-05 |  |
| [[CFL2]] | -0.60 | -0.51 / -0.61 | both halves | 1e-05 |  |
| [[GUF1]] | -0.60 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[SMARCE1]] | -0.60 | -0.61 / -0.58 | both halves | 7e-06 |  |
| [[MBTPS2]] | -0.60 | -0.47 / -0.62 | both halves | 2e-05 |  |
| [[STAG2]] | -0.60 | -0.34 / -0.54 | both halves | 1e-04 |  |
| [[HNRNPK]] | -0.60 | -0.45 / -0.57 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.643). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-11.5, -3.6); signed map (-42.1, 21.6). **Vector** length 103, 31.0% of its response variance represented; |z| ≥ 3 in 1,335 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +7.4 | +0.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.6 | +2.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.2 | -1.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.7 | -0.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.1 | +22.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.0 | +1.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.3 | +7.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | -0.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | +15.3 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.6 | +3.3 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.8 | -1.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.7 | -5.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.9 | -2.1 |
|  | [[Selinexor (drug)]] 5 µM |  | -5.8 | -8.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.7 | -3.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.5 | -7.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.3 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.0 | -3.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.7 | -1.6 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -2.4 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | RABGEF1 pseudogene 1 |
| Locus type | pseudogene |
| Location | 7q11.21 — chr7:66,554,588-66,576,923 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55751](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55751) · Entrez [493754](https://www.ncbi.nlm.nih.gov/gene/493754) · Ensembl [ENSG00000229180](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000229180)

## Data

Gene col 13696: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13696); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13696, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13696]; `tensor/DDL_lfc|DDL_z.npy` [13696]; `embed/gene_vectors.npy` [13696]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13696 or target_col == 13696). Every well: [[RABGEF1P1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RABGEF1P1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
