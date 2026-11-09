---
symbol: "PLEKHM1"
type: "gene"
col: 13440
ensembl_id: "ENSG00000225190"
name: "pleckstrin homology and RUN domain containing M1"
location: "17q21.31"
module: 34
arm: "+"
pooled_cpm: 53.65
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 20
n_dd_up_clean: 15
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 24
direction_downstream: 0
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# PLEKHM1

*pleckstrin homology and RUN domain containing M1* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.42× (z +6.3, q 2e-07, up in 25 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.288× (z -21.8, q 0e+00, down in 34 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Epirubicin (hydrochloride) (drug)]] 5 µM: 0.721× (z -5.7, q 1e-06, down in 27 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLEKHM1P1]] (+0.83, fdr 7e-06), [[ARHGAP27P1-BPTFP1-KPNA2P3]] (+0.71, fdr 7e-06), [[ARHGAP27]] (+0.70, fdr 7e-06, ⚠ same locus), [[KPNA2P3]] (+0.66, fdr 7e-06); moves opposite to [[KCTD3]] (-0.56, fdr 1e-05), [[ANP32A]] (-0.54, fdr 3e-05), [[GTF2I]] (-0.54, fdr 3e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 24 arrows point to it, the strongest [[LINC02725]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13440.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.42×** | +6.3 | 2e-07 | 25/48 (NCI-H460, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.26×** | +6.0 | 7e-07 | 24/47 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.37×** | +5.7 | 2e-06 | 25/48 (SW480, NCI-H1573, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.36×** | +5.6 | 3e-06 | 26/48 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.78×** | +5.5 | 5e-06 | 28/49 (NCI-H460, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.35×** | +5.4 | 5e-06 | 24/47 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.72×** | +5.1 | 2e-05 | 27/48 (SNU-423, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.32×** | +5.0 | 3e-05 | 25/48 (NCI-H460, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.32×** | +5.0 | 3e-05 | 25/48 (A-427, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.30×** | +4.8 | 8e-05 | 23/48 (KATO III, A498, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.18× | +4.3 | 8e-04 | 21/49 (NCI-H1573, SW480, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.27×** | +4.3 | 8e-04 | 21/48 (COLO 205, KATO III, …) | rises with dose |  |
| [[TAK-733 (drug)]] 0.05 µM |  | **1.27×** | +4.0 | 0.002 | 19/48 (COLO 205, HT-29, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.24×** | +3.9 | 0.004 | 19/48 (KATO III, C32, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[ULK-101 (drug)]] 0.05 µM |  | **1.25×** | +3.9 | 0.004 | 16/49 (MIA PaCa-2, HOP62, …) | inconsistent across doses | position effect removed |
| [[BAY1125976 (drug)]] 5 µM |  | **1.49×** | +3.8 | 0.005 | 20/48 (SW480, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13440.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.288×** | -21.8 | 0e+00 | 34/38 (LOX-IMVI, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.342×** | -19.5 | 0e+00 | 41/47 (SNU-423, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.477×** | -12.5 | 3e-33 | 35/42 (SNU-423, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.800×** | -5.8 | 1e-06 | 24/49 (AsPC-1, Hs 766T, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.721×** | -5.7 | 1e-06 | 27/49 (SNU-423, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.805×** | -5.6 | 2e-06 | 24/48 (SNU-423, NCI-H1573, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **0.765×** | -4.9 | 9e-05 | 25/45 (H4, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.772×** | -4.5 | 4e-04 | 22/47 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.820×** | -4.4 | 5e-04 | 26/48 (AsPC-1, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.815×** | -4.2 | 0.001 | 20/48 (AsPC-1, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.798×** | -4.1 | 0.002 | 20/49 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[venetoclax (drug)]] 0.05 µM |  | **0.787×** | -4.1 | 0.002 | 16/49 (AsPC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.795×** | -4.1 | 0.002 | 23/49 (AsPC-1, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.797×** | -4.0 | 0.003 | 23/47 (AsPC-1, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.863× | -3.8 | 0.005 | 19/48 (AsPC-1, Hs 766T, …) | all doses, flat |  |
| [[Radotinib (drug)]] 5 µM |  | 0.866× | -3.7 | 0.007 | 15/48 (AsPC-1, COLO 205, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.819×** | -3.7 | 0.008 | 18/48 (AsPC-1, LS 180, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.872× | -3.4 | 0.016 | 14/49 (AsPC-1, CFPAC-1, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.824×** | -3.3 | 0.028 | 18/48 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Larotrectinib (drug)]] 5 µM |  | 0.885× | -3.2 | 0.037 | 9/48 (LOX-IMVI, BT-474, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13440. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 128 | 0 | 12 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.115× (z -20.8) ⚠ toxic; transcription drop · without an alert: [[Trametinib (drug)]] 0.5 µM 0.370× (z -12.2) |
| [[NCI-H460 (line)]] | wt | 35.1 | 11 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +17.5) | — |
| [[SNU-423 (line)]] | alt | 115 | 1 | 7 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +12.8) | [[Dinaciclib (drug)]] 0.05 µM 0.0988× (z -22.0) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -12.1) |
| [[A-172 (line)]] | wt | 73.0 | 4 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.80× (z +22.7) | [[Dinaciclib (drug)]] 5 µM 0.144× (z -15.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 73.7 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.153× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.498× (z -9.5) |
| [[A498 (line)]] | wt | 57.3 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -17.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 112 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.145× (z -16.3) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 110 | 2 (1 ⚠) | 2 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 4.46× (z +10.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.72× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.113× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Radotinib (drug)]] 5 µM 0.415× (z -9.0) |
| [[Hs 766T (line)]] | wt | 107 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -15.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 71.3 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.288× (z -9.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 49.6 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +15.0) | [[Dinaciclib (drug)]] 5 µM 0.0423× (z -28.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 40.4 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.0926× (z -14.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 56.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -12.5) |
| [[hTERT-HPNE (line)]] | wt | 71.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.117× (z -15.4) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 47.4 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.178× (z -15.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 72.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.141× (z -15.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 41.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.0617× (z -21.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 32.5 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.340× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 44.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.199× (z -13.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 28.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.08× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -12.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 37.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.282× (z -10.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 29.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.125× (z -14.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 56.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.343× (z -9.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 32.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.222× (z -10.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 58.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.248× (z -12.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 59.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.177× (z -13.2) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 36.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0961× (z -16.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 51.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -16.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 57.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.315× (z -11.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 61.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.269× (z -11.1) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 56.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.204× (z -11.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 48.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.150× (z -13.9) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 46.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0693× (z -18.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 51.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.238× (z -10.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 26.8 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.146× (z -9.6) |
| [[AN3 CA (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 39.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 76.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13440), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLEKHM1P1]] | +0.83 | +0.86 / +0.79 | both halves | 7e-06 |  |
| [[ARHGAP27P1-BPTFP1-KPNA2P3]] | +0.71 | +0.66 / +0.75 | both halves | 7e-06 |  |
| [[ARHGAP27]] | +0.70 | +0.61 / +0.78 | both halves | 7e-06 | same gene group; STRING 604; ⚠ same locus (1.5 kb, same strand: neighbours can correlate without regulation) |
| [[KPNA2P3]] | +0.66 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[RDH13]] | +0.64 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[PTK6]] | +0.63 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[LAT]] | +0.62 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[ZBTB43]] | +0.62 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[PRSS3]] | +0.60 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[NPC1]] | +0.60 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[PPARD]] | +0.59 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[TMC6]] | +0.59 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[PLEK2]] | +0.59 | +0.52 / +0.62 | both halves | 1e-05 | same gene group; STRING 709 |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCTD3]] | -0.56 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[ANP32A]] | -0.54 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[GTF2I]] | -0.54 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[PDS5B]] | -0.54 | -0.46 / -0.52 | both halves | 2e-05 |  |
| [[SH3BGRL]] | -0.53 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[MATR3]] | -0.53 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[SCARB2]] | -0.52 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[SEPHS1]] | -0.52 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[TOP2B]] | -0.51 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[TMPO]] | -0.51 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[AKAP7]] | -0.51 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[PON2]] | -0.50 | -0.43 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 23, C 1. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02725]] | B | LINC02725 activity raises PLEKHM1's level | lines that do not express LINC02725 (35) vs lines expressing it (15) | 1.57× lower at baseline in the lines without LINC02725 | 0.008 | ⚠ within organs, on part of the lines; also absent: DHRS9, ENSG00000203434, LINC01425 |
| [[TOR4A]] | B | TOR4A activity raises PLEKHM1's level | lines that do not express TOR4A (14) vs lines expressing it (36) | 1.77× lower at baseline in the lines without TOR4A | 0.015 | ⚠ within organs, on part of the lines; also absent: PLEKHA6, CDCP1, C19orf33 |
| [[S100A16]] | B | S100A16 activity raises PLEKHM1's level | lines that do not express S100A16 (9) vs lines expressing it (41) | 1.77× lower at baseline in the lines without S100A16 | 0.016 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, MET, TGFBR2 |
| [[PRSS3]] | B | PRSS3 activity raises PLEKHM1's level | lines that do not express PRSS3 (30) vs lines expressing it (20) | 1.57× lower at baseline in the lines without PRSS3 | 0.018 | ⚠ within organs, on part of the lines; also absent: IL20RA, ABO, EDAR |
| [[C6orf141]] | B | C6orf141 activity raises PLEKHM1's level | lines that do not express C6orf141 (21) vs lines expressing it (29) | 1.47× lower at baseline in the lines without C6orf141 | 0.019 | ⚠ within organs, on part of the lines; also absent: ADAM8, ENSG00000251584, SAMD12-AS1 |
| [[TINAGL1]] | B | TINAGL1 activity raises PLEKHM1's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 1.62× lower at baseline in the lines without TINAGL1 | 0.020 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19 |
| [[ST3GAL1]] | B | ST3GAL1 activity raises PLEKHM1's level | lines that do not express ST3GAL1 (11) vs lines expressing it (39) | 1.65× lower at baseline in the lines without ST3GAL1 | 0.026 | ⚠ within organs, on part of the lines; also absent: IL1RAP, FBXO32, PLSCR2 |
| [[LAMC2]] | B | LAMC2 activity raises PLEKHM1's level | lines that do not express LAMC2 (27) vs lines expressing it (23) | 1.47× lower at baseline in the lines without LAMC2 | 0.027 | ⚠ within organs, on part of the lines; also absent: ENSG00000287929, TNS4, HS3ST1 |
| [[TMCC3]] | B | TMCC3 activity raises PLEKHM1's level | lines that do not express TMCC3 (19) vs lines expressing it (31) | 1.41× lower at baseline in the lines without TMCC3 | 0.032 | ⚠ within organs, on part of the lines; also absent: PTPRB, KRT7, ADGRF4 |
| [[PEAR1]] | B | PEAR1 activity raises PLEKHM1's level | lines that do not express PEAR1 (24) vs lines expressing it (26) | 1.50× lower at baseline in the lines without PEAR1 | 0.035 | ⚠ within organs, on part of the lines; also absent: LY75, AFAP1L2, PRSS3 |
| [[PLEK2]] | B | PLEK2 activity raises PLEKHM1's level | lines that do not express PLEK2 (17) vs lines expressing it (33) | 1.43× lower at baseline in the lines without PLEK2 | 0.038 | ⚠ within organs, on part of the lines; also absent: CDCP1, SAMD12, SDR16C5 |
| [[LAMA3]] | B | LAMA3 activity weakens PLEKHM1's drug response | lines that do not express LAMA3 (22) vs lines expressing it (27) | the lines without LAMA3 respond 0.96× as strongly (z diff +0.01); strongest at Homoharringtonine 5 µM: 1.93x vs 1.01x (z diff -6.1) | 0.040 | ⚠ within organs, on part of the lines; also absent: P2RY2, ELF3, MYO5B; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.680). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (9.7, 54.0); signed map (0.8, 36.4). **Vector** length 124, 38.7% of its response variance represented; |z| ≥ 3 in 1,352 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.9 | +4.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.5 | +3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.2 | +1.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | +3.6 | +3.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.6 | +1.4 |
|  | [[Entrectinib (drug)]] 5 µM |  | +3.4 | +1.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.3 | +3.0 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -5.4 | -3.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -4.5 | -4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.3 | -4.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.2 | -4.0 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -4.2 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | pleckstrin homology and RUN domain containing M1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.31 — chr17:45,435,900-45,490,758 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0356 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; RUN domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y4G2](https://www.uniprot.org/uniprotkb/Q9Y4G2) (Pleckstrin homology domain-containing family M member 1):

> Acts as a multivalent adapter protein that regulates Rab7-dependent and HOPS complex-dependent fusion events in the endolysosomal system and couples autophagic and the endocytic trafficking pathways. Acts as a dual effector of RAB7A and ARL8B that simultaneously binds these GTPases, bringing about clustering and fusion of late endosomes and lysosomes. Required for late stages of endolysosomal maturation, facilitating both endocytosis-mediated degradation of growth factor receptors and …

**Summary**, from NCBI Gene [9842](https://www.ncbi.nlm.nih.gov/gene/9842):

> The protein encoded by this gene is essential for bone resorption, and may play a critical role in vesicular transport in the osteoclast. Mutations in this gene are associated with autosomal recessive osteopetrosis type 6 (OPTB6). Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Sep 2009]

**Accessions** — [HGNC:29017](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29017) · Entrez [9842](https://www.ncbi.nlm.nih.gov/gene/9842) · UniProt [Q9Y4G2](https://www.uniprot.org/uniprotkb/Q9Y4G2) · Ensembl [ENSG00000225190](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000225190)

## Data

Gene col 13440: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13440); `tables/drug_effects.parquet` (66 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13440, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13440]; `tensor/DDL_lfc|DDL_z.npy` [13440]; `embed/gene_vectors.npy` [13440]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13440 or target_col == 13440). Every well: [[PLEKHM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLEKHM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
