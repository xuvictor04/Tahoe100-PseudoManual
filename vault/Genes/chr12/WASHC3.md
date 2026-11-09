---
symbol: "WASHC3"
type: "gene"
col: 4228
ensembl_id: "ENSG00000120860"
name: "WASH complex subunit 3"
location: "12q23.2"
module: 28
arm: "+"
pooled_cpm: 27.5
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 31
n_dd_up_clean: 15
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# WASHC3

*WASH complex subunit 3* — 12q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.48× (z +5.2, q 1e-04, up in 29 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (14 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.210× (z -21.5, q 0e+00, down in 43 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.215× (z -21.2, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLK]] (+0.64, fdr 1e-05), [[ZNF429]] (+0.63, fdr 1e-05), [[TRMT1L]] (+0.61, fdr 1e-05); moves opposite to [[LRP8]] (-0.58, fdr 1e-05), [[PRR5-ARHGAP8]] (-0.57, fdr 1e-05), [[PIP5KL1]] (-0.54, fdr 4e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 1 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4228.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.48×** | +5.2 | 1e-04 | 29/47 (SW480, SK-MEL-2, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.42×** | +4.8 | 4e-04 | 26/48 (LoVo, KATO III, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.37×** | +4.4 | 0.002 | 22/48 (A-427, KATO III, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.39×** | +4.4 | 0.002 | 19/47 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.35×** | +4.2 | 0.003 | 22/48 (SW480, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.30×** | +4.2 | 0.003 | 21/48 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.23×** | +3.9 | 0.006 | 17/48 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.32×** | +3.8 | 0.010 | 18/47 (SW480, C-33 A, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.22×** | +3.7 | 0.011 | 13/48 (SW480, Hs 766T, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.28×** | +3.6 | 0.019 | 12/48 (SW480, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.29×** | +3.6 | 0.019 | 17/47 (SW480, SK-MEL-2, …) | two highest doses | low cells (technical?) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.61×** | +3.4 | 0.028 | 9/47 (SW480, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.28×** | +3.4 | 0.028 | 12/48 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.20×** | +3.3 | 0.042 | 13/48 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.28×** | +3.2 | 0.054 | 4/48 (SW480, SK-MEL-2, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.25×** | +3.1 | 0.069 | 13/48 (NCI-H2347, A-427, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 14 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4228.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.210×** | -21.5 | 0e+00 | 43/47 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.215×** | -21.2 | 0e+00 | 47/48 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.271×** | -18.0 | 0e+00 | 45/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.298×** | -16.7 | 0e+00 | 45/48 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.432×** | -11.5 | 9e-29 | 44/48 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.563×** | -11.2 | 5e-27 | 36/47 (NCI-H460, COLO 205, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.505×** | -9.0 | 1e-17 | 31/44 (LOX-IMVI, NCI-H1792, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.523×** | -8.9 | 3e-17 | 34/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.353×** | -7.5 | 4e-12 | 38/48 (SK-MEL-2, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.604×** | -6.9 | 2e-10 | 35/48 (J82, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.630×** | -6.4 | 1e-08 | 29/48 (NCI-H1792, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.415×** | -6.3 | 1e-08 | 30/41 (Hs 766T, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.632×** | -6.3 | 1e-08 | 32/48 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.636×** | -6.2 | 2e-08 | 27/48 (SNU-423, LOX-IMVI, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.627×** | -6.2 | 2e-08 | 25/47 (NCI-H460, NCI-H1792, …) | top dose only | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.424×** | -6.2 | 2e-08 | 36/47 (MIA PaCa-2, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.626×** | -6.1 | 4e-08 | 31/48 (SW480, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.758×** | -3.7 | 0.006 | 16/48 (SW480, NCI-H460, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.699×** | -3.5 | 0.009 | 14/48 (Hs 766T, SNU-423, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.717×** | -3.3 | 0.023 | 12/48 (NCI-H460, LS 180, …) | rises with dose | noisy plate (z scaled) |
| [[Piroxicam (drug)]] 0.05 µM |  | **0.793×** | -3.2 | 0.029 | 13/48 (RKO, SNU-423, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.646×** | -3.1 | 0.033 | 13/48 (Hs 766T, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4228. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 33.8 | 0 | 12 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.147× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.168× (z -15.3) |
| [[SW480 (line)]] | alt | 40.9 | 0 | 10 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0673× (z -23.9) |
| [[Hs 766T (line)]] | wt | 43.8 | 0 | 7 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.121× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.188× (z -12.5) |
| [[J82 (line)]] | alt | 28.4 | 0 | 7 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.107× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.145× (z -14.9) |
| [[SNU-423 (line)]] | alt | 43.1 | 0 | 7 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.124× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.182× (z -12.9) |
| [[HOP62 (line)]] | alt | 37.7 | 0 | 6 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.146× (z -15.7) |
| [[MIA PaCa-2 (line)]] | alt | 38.4 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.116× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.167× (z -12.8) |
| [[NCI-H1792 (line)]] | alt | 45.0 | 0 | 6 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.155× (z -13.3) |
| [[PANC-1 (line)]] | alt | 28.4 | 0 | 6 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0929× (z -20.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.123× (z -18.2) |
| [[LOX-IMVI (line)]] | wt | 30.2 | 0 | 5 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.125× (z -13.9) ⚠ toxic; cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.214× (z -10.8) |
| [[NCI-H1573 (line)]] | alt | 47.7 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0953× (z -20.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.166× (z -15.8) |
| [[NCI-H23 (line)]] | alt | 36.3 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.102× (z -17.1) |
| [[AsPC-1 (line)]] | alt | 21.4 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0355× (z -19.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.203× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 30.1 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.375× (z -11.3) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.260× (z -11.0) |
| [[A-172 (line)]] | wt | 40.4 | 0 | 3 | — | [[Digitoxin (drug)]] 0.5 µM 0.267× (z -10.2) |
| [[A-427 (line)]] | wt | 21.3 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.132× (z -12.7) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.209× (z -9.8) |
| [[A549 (line)]] | wt | 26.5 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0889× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.251× (z -9.2) |
| [[COLO 205 (line)]] | alt | 27.4 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0460× (z -18.2) |
| [[HS-578T (line)]] | alt | 23.4 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.155× (z -11.4) |
| [[LoVo (line)]] | wt | 19.6 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.249× (z -9.7) |
| [[RPMI-7951 (line)]] | alt | 31.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.115× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.209× (z -9.3) |
| [[SNU-1 (line)]] | wt | 25.8 | 0 | 3 (1 ⚠) | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.125× (z -10.0) |
| [[C-33 A (line)]] | alt | 18.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0892× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Decitabine (drug)]] 0.05 µM 0.0990× (z -10.1) |
| [[C32 (line)]] | wt | 18.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0378× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.138× (z -9.9) |
| [[CFPAC-1 (line)]] | alt | 23.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -11.7) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.221× (z -10.5) |
| [[HT-29 (line)]] | alt | 16.1 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.173× (z -10.8) |
| [[KATO III (line)]] | alt | 26.7 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.188× (z -12.0) |
| [[NCI-H2347 (line)]] | alt | 19.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.253× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.282× (z -9.3) |
| [[Panc 03.27 (line)]] | alt | 22.8 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.172× (z -12.0) |
| [[SK-MEL-2 (line)]] | alt | 34.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -8.9) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.319× (z -8.7) |
| [[H4 (line)]] | wt | 26.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.158× (z -8.8) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 25.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0474× (z -15.3) |
| [[HepG2_C3A (line)]] | wt | 20.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0459× (z -14.4) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 20.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.100× (z -11.9) |
| [[LS 180 (line)]] | wt | 27.7 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.226× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 14.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.166× (z -9.6) |
| [[SW1417 (line)]] | alt | 17.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.195× (z -9.6) |
| [[A498 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.76 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4228), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLK]] | +0.64 | +0.69 / +0.49 | both halves | 1e-05 |  |
| [[ZNF429]] | +0.63 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[TRMT1L]] | +0.61 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[RAD52]] | +0.60 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[C15orf40]] | +0.59 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[LMLN]] | +0.59 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[KCTD18]] | +0.58 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[KMT2A]] | +0.57 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[CCDC90B]] | +0.57 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[RRAGC]] | +0.57 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[EBAG9]] | +0.57 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[MRPS31]] | +0.56 | +0.56 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRP8]] | -0.58 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[PRR5-ARHGAP8]] | -0.57 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[PIP5KL1]] | -0.54 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[ATP11A]] | -0.53 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[PMPCA]] | -0.52 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[MCOLN2]] | -0.52 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[BRI3BP]] | -0.51 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[LRP5]] | -0.50 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[GNB1L]] | -0.50 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[SNRPA]] | -0.50 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[CCDC138]] | -0.50 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[ATP2A2]] | -0.49 | -0.57 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers WASHC3's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.2% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds |
| [[TMEM9B-AS1]] | B | TMEM9B-AS1 activity raises WASHC3's level | lines that do not express TMEM9B-AS1 (5) vs lines expressing it (45) | 1.30× lower at baseline in the lines without TMEM9B-AS1 | 0.086 | ⚠ within organs, on part of the lines; also absent: TSEN2, SCML2, CAP2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.631). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-25.9, 8.0); signed map (10.7, -23.7). **Vector** length 69.6, 16.5% of its response variance represented; |z| ≥ 3 in 1,235 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.2 | -0.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.0 | +3.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +4.2 | -6.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +3.0 | -4.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.8 | +2.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.6 | +1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.4 | +3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +4.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -0.7 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -3.3 | -6.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.1 | -11.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.9 | -18.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | -2.7 | -6.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.9 | -3.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.7 | -1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.6 | -6.3 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.3 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | WASH complex subunit 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.2 — chr12:102,012,840-102,062,149 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-116; previously CCDC53 |
| Gene groups (HGNC) | WASH complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y3C0](https://www.uniprot.org/uniprotkb/Q9Y3C0) (WASH complex subunit 3):

> Acts as a component of the WASH core complex that functions as a nucleation-promoting factor (NPF) at the surface of endosomes, where it recruits and activates the Arp2/3 complex to induce actin polymerization, playing a key role in the fission of tubules that serve as transport intermediates during endosome sorting.

**Summary**, from NCBI Gene [51019](https://www.ncbi.nlm.nih.gov/gene/51019):

> Predicted to be involved in actin filament polymerization and exocytosis. Part of WASH complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24256](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24256) · Entrez [51019](https://www.ncbi.nlm.nih.gov/gene/51019) · UniProt [Q9Y3C0](https://www.uniprot.org/uniprotkb/Q9Y3C0) · Ensembl [ENSG00000120860](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120860)

## Data

Gene col 4228: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4228); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4228, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4228]; `tensor/DDL_lfc|DDL_z.npy` [4228]; `embed/gene_vectors.npy` [4228]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4228 or target_col == 4228). Every well: [[WASHC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WASHC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
