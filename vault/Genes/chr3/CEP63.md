---
symbol: "CEP63"
type: "gene"
col: 11343
ensembl_id: "ENSG00000182923"
name: "centrosomal protein 63"
location: "3q22.2"
module: 28
arm: "+"
pooled_cpm: 59.22
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 15
n_dd_up_clean: 4
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# CEP63

*centrosomal protein 63* — 3q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.54× (z +15.6, q 0e+00, up in 35 of 48 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.75× (z +14.5, q 1e-45, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.442× (z -21.2, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EBAG9]] (+0.71, fdr 1e-05), [[SUPT20H]] (+0.68, fdr 1e-05), [[FAM114A2]] (+0.68, fdr 1e-05); moves opposite to [[C1orf216]] (-0.67, fdr 7e-06), [[RAD9A]] (-0.61, fdr 1e-05), [[TXN]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ANKRD20A8P]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11343.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.54×** | +15.6 | 0e+00 | 35/48 (A-172, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.75×** | +14.5 | 1e-45 | 42/47 (A-427, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.50×** | +10.2 | 3e-22 | 31/48 (A-172, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.33×** | +7.5 | 8e-12 | 24/47 (HEC-1-A, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~15% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.72×** | +7.4 | 2e-11 | 28/49 (LoVo, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.28×** | +6.3 | 3e-08 | 23/43 (LOX-IMVI, LoVo, …) | two highest doses | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.25×** | +5.8 | 5e-07 | 25/48 (A-172, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.23×** | +5.5 | 3e-06 | 26/48 (A-427, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +5.3 | 7e-06 | 14/48 (Panc 03.27, NCI-H2347, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.16× | +3.8 | 0.008 | 12/48 (AN3 CA, NCI-H23, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.05 µM |  | 1.15× | +3.8 | 0.009 | 6/48 (KATO III, A549, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **1.31×** | +3.7 | 0.010 | 14/48 (PANC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.14× | +3.5 | 0.017 | 9/48 (NCI-H1792, KATO III, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.13× | +3.3 | 0.045 | 11/48 (C32, HepG2/C3A, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.14× | +3.1 | 0.074 | 11/47 (NCI-H1573, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Radotinib (drug)]] 5 µM |  | 1.09× | +3.0 | 0.085 | 4/48 (HT-29, LoVo, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.17× | +3.0 | 0.085 | 7/47 (MIA PaCa-2, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11343.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.442×** | -21.2 | 0e+00 | 45/48 (HS-578T, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.462×** | -20.1 | 0e+00 | 43/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.472×** | -19.5 | 0e+00 | 44/48 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.531×** | -16.4 | 0e+00 | 44/48 (HS-578T, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.544×** | -15.8 | 0e+00 | 43/48 (SW480, SK-MEL-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.554×** | -15.4 | 0e+00 | 44/48 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.692×** | -9.5 | 1e-19 | 34/48 (PANC-1, LoVo, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.686×** | -9.2 | 2e-18 | 33/48 (PANC-1, J82, …) | all doses, flat | cell-cycle shift (explains ~21% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~21% of this change | **0.733×** | -7.8 | 6e-13 | 31/47 (HepG2/C3A, J82, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.792×** | -6.0 | 9e-08 | 25/47 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.793×** | -6.0 | 9e-08 | 23/48 (J82, SW480, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.647×** | -5.9 | 2e-07 | 26/45 (BT-474, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | 0.849× | -5.8 | 2e-07 | 18/48 (HOP62, MIA PaCa-2, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.797×** | -5.7 | 6e-07 | 26/47 (HS-578T, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.823×** | -5.0 | 2e-05 | 21/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.895× | -3.9 | 0.003 | 12/48 (HOP62, SW 1271, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.823×** | -3.6 | 0.009 | 12/48 (Hs 766T, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.919× | -3.0 | 0.066 | 3/48 (KATO III, SNU-1, …) | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | 0.884× | -2.9 | 0.077 | 11/47 (HCT15, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11343. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 36.9 | 3 (2 ⚠) | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +15.6) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.42× (z +10.2) | [[Digitoxin (drug)]] 5 µM 0.226× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.342× (z -12.4) |
| [[J82 (line)]] | alt | 71.7 | 0 | 8 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.281× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.361× (z -12.6) |
| [[NCI-H460 (line)]] | wt | 42.2 | 1 (1 ⚠) | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +9.3) ⚠ cell-cycle shift, explains ~35% of this change | [[Digitoxin (drug)]] 0.05 µM 0.381× (z -13.3) |
| [[PANC-1 (line)]] | alt | 106 | 1 | 6 | [[Homoharringtonine (drug)]] 0.5 µM 1.74× (z +10.0) | [[Ixazomib citrate (drug)]] 5 µM 0.444× (z -14.7) |
| [[SW1417 (line)]] | alt | 82.0 | 0 | 7 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.287× (z -16.7) |
| [[A-172 (line)]] | wt | 84.0 | 4 (3 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +16.4) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.49× (z +11.9) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.405× (z -11.9) |
| [[HOP62 (line)]] | alt | 59.3 | 0 | 6 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.240× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.294× (z -14.5) |
| [[HS-578T (line)]] | alt | 91.7 | 0 | 6 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.206× (z -19.8) |
| [[KATO III (line)]] | alt | 76.5 | 2 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +9.5) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.07× (z +8.7) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.360× (z -12.2) |
| [[SW480 (line)]] | alt | 54.1 | 1 (1 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.00× (z +9.7) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.193× (z -22.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.259× (z -18.7) |
| [[LS 180 (line)]] | wt | 40.1 | 2 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +11.6) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.91× (z +10.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.393× (z -9.5) |
| [[SHP-77 (line)]] | alt | 66.8 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.310× (z -11.6) |
| [[HEC-1-A (line)]] | alt | 59.6 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.54× (z +12.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.35× (z +11.1) | [[Ixazomib citrate (drug)]] 5 µM 0.467× (z -9.8) |
| [[HT-29 (line)]] | alt | 35.6 | 0 | 4 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.307× (z -10.6) |
| [[A-427 (line)]] | wt | 142 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.5 µM 3.17× (z +17.0) | [[Auranofin (drug)]] 5 µM 0.473× (z -10.9) |
| [[H4 (line)]] | wt | 79.5 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.251× (z -12.1) |
| [[HepG2_C3A (line)]] | wt | 61.1 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0703× (z -21.3) ⚠ toxic; cell-cycle shift, explains ~21% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.312× (z -9.7) |
| [[NCI-H2347 (line)]] | alt | 42.4 | 1 | 2 | [[Homoharringtonine (drug)]] 0.5 µM 2.28× (z +9.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.435× (z -9.0) |
| [[Panc 03.27 (line)]] | alt | 79.6 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +9.7) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.11× (z +8.6) | [[Auranofin (drug)]] 5 µM 0.378× (z -11.1) |
| [[SW 900 (line)]] | alt | 38.2 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.246× (z -11.5) |
| [[C-33 A (line)]] | alt | 60.7 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.220× (z -13.2) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 56.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.301× (z -10.2) |
| [[LOX-IMVI (line)]] | wt | 56.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +9.6) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.39× (z +9.6) | — |
| [[NCI-H23 (line)]] | alt | 81.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.26× (z +10.3) ⚠ toxic; transcription drop | [[Auranofin (drug)]] 5 µM 0.416× (z -11.0) |
| [[RKO (line)]] | wt | 30.9 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.197× (z -11.4) ⚠ toxic; cell-cycle shift, explains ~21% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.298× (z -8.9) |
| [[A498 (line)]] | wt | 55.5 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.490× (z -9.4) |
| [[C32 (line)]] | wt | 53.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.335× (z -9.9) ⚠ toxic; cell-cycle shift, explains ~21% of this change |
| [[CFPAC-1 (line)]] | alt | 28.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +8.5) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[HCT15 (line)]] | alt | 45.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.252× (z -9.5) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 53.6 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.345× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 47.6 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.37× (z +11.9) | — |
| [[SK-MEL-2 (line)]] | alt | 103 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.352× (z -12.8) |
| [[SNU-1 (line)]] | wt | 69.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.263× (z -10.3) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 67.2 | 0 | 1 (1 ⚠) | — | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.0643× (z -9.2) ⚠ unreliable plate only |
| [[A549 (line)]] | wt | 51.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 48.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 62.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 76.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11343), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EBAG9]] | +0.71 | +0.83 / +0.51 | both halves | 1e-05 |  |
| [[SUPT20H]] | +0.68 | +0.77 / +0.53 | both halves | 1e-05 |  |
| [[FAM114A2]] | +0.68 | +0.80 / +0.49 | both halves | 1e-05 |  |
| [[CCDC25]] | +0.67 | +0.70 / +0.57 | both halves | 1e-05 |  |
| [[COQ5]] | +0.65 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[CETN3]] | +0.65 | +0.75 / +0.55 | both halves | 1e-05 | same gene group; STRING 624 |
| [[NSMCE1]] | +0.65 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[RAD50]] | +0.64 | +0.74 / +0.51 | both halves | 1e-05 |  |
| [[MRPS33]] | +0.61 | +0.71 / +0.44 | both halves | 3e-05 |  |
| [[DARS1]] | +0.61 | +0.71 / +0.39 | both halves | 5e-05 |  |
| [[SUCLG1]] | +0.60 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[RNF214]] | +0.60 | +0.62 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C1orf216]] | -0.67 | -0.66 / -0.60 | both halves | 7e-06 |  |
| [[RAD9A]] | -0.61 | -0.68 / -0.50 | both halves | 1e-05 |  |
| [[TXN]] | -0.56 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[MBOAT7]] | -0.56 | -0.65 / -0.50 | both halves | 1e-05 |  |
| [[UBE2M]] | -0.55 | -0.62 / -0.40 | both halves | 5e-05 |  |
| [[SNHG30]] | -0.54 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[SPINDOC]] | -0.54 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[RAB5IF]] | -0.53 | -0.57 / -0.39 | both halves | 6e-05 |  |
| [[HSPE1]] | -0.53 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[MED31]] | -0.53 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[AHSA1]] | -0.53 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[ILRUN]] | -0.53 | -0.63 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANKRD20A8P]] | B | ANKRD20A8P activity raises CEP63's level | lines that do not express ANKRD20A8P (38) vs lines expressing it (12) | 1.51× lower at baseline in the lines without ANKRD20A8P | 0.032 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ENSG00000291025, ENSG00000249174, TPTE |
| [[FAR2P1]], [[POTEF]] | B | FAR2P1, POTEF activity raises CEP63's level | lines that do not express FAR2P1, POTEF (29) vs lines expressing them (21) | 1.21× lower at baseline in the lines without FAR2P1, POTEF | 0.062 | ⚠ within organs, on part of the lines; also absent: POTEE, ENSG00000264660, ENSG00000286329; co-absent genes |
| [[PSMB5]] | B | PSMB5 activity raises CEP63's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.667). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-27.8, 3.7); signed map (6.5, -24.9). **Vector** length 120, 33.0% of its response variance represented; |z| ≥ 3 in 1,154 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +10.7 | +14.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +10.5 | +15.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +8.2 | +10.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +7.7 | +7.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | +6.3 | +5.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.1 | +5.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.9 | +1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +5.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.5 | +2.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +3.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -9.5 | -15.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -8.9 | -20.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -8.7 | -15.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -8.2 | -19.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -7.9 | -16.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.8 | -9.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.5 | -3.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.9 | -3.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | -2.4 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | centrosomal protein 63 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q22.2 — chr3:134,485,699-134,587,789 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13386 |
| Gene groups (HGNC) | Centriolar satellite proteins |
| Reactome | 17 pathways, smallest: Loss of Nlp from mitotic centrosomes; Loss of proteins required for interphase microtubule organization from the centrosome; AURKA Activation by TPX2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96MT8](https://www.uniprot.org/uniprotkb/Q96MT8) (Centrosomal protein of 63 kDa):

> Required for normal spindle assembly. Plays a key role in mother-centriole-dependent centriole duplication; the function seems also to involve CEP152, CDK5RAP2 and WDR62 through a stepwise assembled complex at the centrosome that recruits CDK2 required for centriole duplication. Reported to be required for centrosomal recruitment of CEP152; however, this function has been questioned. Also recruits CDK1 to centrosomes. Plays a role in DNA damage response. Following DNA damage, such as …

**Summary**, from NCBI Gene [80254](https://www.ncbi.nlm.nih.gov/gene/80254):

> This gene encodes a protein with six coiled-coil domains. The protein is localized to the centrosome, a non-membraneous organelle that functions as the major microtubule-organizing center in animal cells. Several alternatively spliced transcript variants have been found, but their biological validity has not been determined. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:25815](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25815) · Entrez [80254](https://www.ncbi.nlm.nih.gov/gene/80254) · UniProt [Q96MT8](https://www.uniprot.org/uniprotkb/Q96MT8) · Ensembl [ENSG00000182923](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182923)

## Data

Gene col 11343: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11343); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11343, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11343]; `tensor/DDL_lfc|DDL_z.npy` [11343]; `embed/gene_vectors.npy` [11343]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11343 or target_col == 11343). Every well: [[CEP63 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CEP63.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
