---
symbol: "TSC1"
type: "gene"
col: 9172
ensembl_id: "ENSG00000165699"
name: "TSC complex subunit 1"
location: "9q34.13"
module: 122
arm: "+"
pooled_cpm: 62.8
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 6
n_dd_up_clean: 17
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/122"]
generated_by: "tahoemap"
---

# TSC1

*TSC complex subunit 1* — 9q34.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.71× (z +23.6, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.487× (z -17.0, q 0e+00, down in 43 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.813× (z -6.9, q 6e-10, down in 30 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (NCI-H460 0.0959×, AsPC-1 0.197×, SW48 0.136×, A-427 0.231×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (HOP62 0.292×, SNU-423 0.317×, NCI-H460 0.380×, CHP-212 0.130×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (NCI-H23 0.131×, NCI-H460 0.343×, NCI-H1792 0.316×, H4 0.147×; ⚠ toxic; transcription drop); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (SW 1271 0.0754×); [[Decitabine (drug)]] 0.05 µM in 1 line (AN3 CA 0.136×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FLCN]] (+0.71, fdr 1e-05), [[N4BP2L2]] (+0.69, fdr 7e-06), [[ATP6V1G1]] (+0.67, fdr 7e-06); moves opposite to [[MACROH2A1]] (-0.57, fdr 2e-05), [[SRPK1]] (-0.57, fdr 1e-05), [[NUP93]] (-0.56, fdr 3e-05).
> It is in [[Module 122]], a single-armed module (Transferrin endocytosis and recycling).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9172.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.71×** | +23.6 | 0e+00 | 47/48 (NCI-H460, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.92×** | +21.7 | 0e+00 | 44/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.10×** | +17.6 | 0e+00 | 45/48 (NCI-H460, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.88×** | +14.9 | 0e+00 | 41/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.84×** | +14.4 | 1e-44 | 43/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.36×** | +10.6 | 4e-24 | 40/49 (NCI-H460, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.53×** | +10.1 | 5e-22 | 33/48 (LoVo, NCI-H23, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +7.8 | 4e-13 | 32/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.34×** | +6.6 | 3e-09 | 33/48 (PANC-1, A-172, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.70×** | +6.6 | 3e-09 | 29/48 (RKO, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.31×** | +6.4 | 1e-08 | 29/48 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.31×** | +6.1 | 5e-08 | 26/48 (NCI-H460, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +5.5 | 2e-06 | 26/48 (HEC-1-A, C32, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.26×** | +5.4 | 2e-06 | 29/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.50×** | +5.0 | 2e-05 | 23/49 (A498, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.22×** | +4.6 | 2e-04 | 25/47 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 9 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9172.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (NCI-H460 0.0959×, AsPC-1 0.197×, SW48 0.136×, A-427 0.231×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (HOP62 0.292×, SNU-423 0.317×, NCI-H460 0.380×, CHP-212 0.130×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (NCI-H23 0.131×, NCI-H460 0.343×, NCI-H1792 0.316×, H4 0.147×; ⚠ toxic; transcription drop); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (SW 1271 0.0754×); [[Decitabine (drug)]] 0.05 µM in 1 line (AN3 CA 0.136×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.487×** | -17.0 | 0e+00 | 43/49 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.594×** | -11.9 | 6e-30 | 31/42 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.617×** | -10.6 | 8e-24 | 35/45 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.813×** | -6.9 | 6e-10 | 30/48 (A498, LOX-IMVI, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.807×** | -5.1 | 4e-05 | 25/48 (CFPAC-1, AN3 CA, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.814×** | -4.9 | 1e-04 | 23/48 (HOP62, SNU-423, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | 0.843× | -4.0 | 0.004 | 20/48 (SNU-423, CFPAC-1, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.857× | -3.7 | 0.016 | 14/49 (A498, LOX-IMVI, …) | rises with dose |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | 0.857× | -3.7 | 0.016 | 8/48 (SW 1088, HT-29, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | 0.853× | -3.6 | 0.016 | 23/50 (RPMI-7951, SNU-423, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | 0.860× | -3.4 | 0.031 | 15/48 (RPMI-7951, H4, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9172. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 76.2 | 12 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.82× (z +26.9) | [[Dinaciclib (drug)]] 5 µM 0.0959× (z -31.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H1792 (line)]] | alt | 78.2 | 4 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.26× (z +15.2) | [[Dinaciclib (drug)]] 0.05 µM 0.316× (z -13.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 56.7 | 4 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.20× (z +14.2) | [[Dinaciclib (drug)]] 0.5 µM 0.292× (z -15.2) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 73.5 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.352× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[RKO (line)]] | wt | 120 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +17.1) | — |
| [[SW480 (line)]] | alt | 68.5 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.08× (z +16.6) | [[Dinaciclib (drug)]] 5 µM 0.445× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[BT-474 (line)]] | alt | 87.0 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.71× (z +14.0) | — |
| [[COLO 205 (line)]] | alt | 88.9 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.80× (z +19.3) | [[Dinaciclib (drug)]] 0.5 µM 0.289× (z -12.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 53.0 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.31× (z +17.8) | — |
| [[NCI-H1573 (line)]] | alt | 34.4 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +14.7) | [[Dinaciclib (drug)]] 5 µM 0.197× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H23 (line)]] | alt | 55.9 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +10.9) | [[Dinaciclib (drug)]] 0.05 µM 0.131× (z -21.3) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 47.9 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.13× (z +18.7) | — |
| [[SNU-1 (line)]] | wt | 80.8 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.97× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -9.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 96.7 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +14.3) | [[Dinaciclib (drug)]] 0.5 µM 0.317× (z -13.9) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 65.4 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.50× (z +13.4) | [[Dinaciclib (drug)]] 0.05 µM 0.293× (z -12.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 67.1 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +15.7) | — |
| [[LOX-IMVI (line)]] | wt | 62.3 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.409× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[H4 (line)]] | wt | 86.5 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +10.1) | [[Dinaciclib (drug)]] 0.05 µM 0.147× (z -13.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 64.0 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.06× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.429× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[LS 180 (line)]] | wt | 52.8 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.80× (z +14.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 74.6 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.287× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H2347 (line)]] | alt | 57.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.377× (z -10.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 57.3 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.06× (z +11.4) | — |
| [[A-172 (line)]] | wt | 66.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +14.0) | — |
| [[A-427 (line)]] | wt | 35.6 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.58× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.231× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A498 (line)]] | wt | 56.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +19.5) | — |
| [[AsPC-1 (line)]] | alt | 62.7 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.91× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.197× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HEC-1-A (line)]] | alt | 82.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +11.8) | — |
| [[HS-578T (line)]] | alt | 49.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +14.2) | — |
| [[hTERT-HPNE (line)]] | wt | 83.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.290× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[RPMI-7951 (line)]] | alt | 65.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.332× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SW1417 (line)]] | alt | 61.4 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.92× (z +12.6) | — |
| [[SW48 (line)]] | wt | 59.5 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.66× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.136× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A549 (line)]] | wt | 70.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.416× (z -9.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 76.4 | 0 | 1 | — | [[Decitabine (drug)]] 0.05 µM 0.136× (z -10.7) |
| [[C-33 A (line)]] | alt | 51.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.34× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[CHP-212 (line)]] | wt | 101 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.130× (z -13.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 63.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.327× (z -10.4) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 33.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +14.5) | — |
| [[SHP-77 (line)]] | alt | 66.9 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.37× (z +9.2) | — |
| [[SK-MEL-2 (line)]] | alt | 40.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +12.0) | — |
| [[SW 1271 (line)]] | alt | 102 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0754× (z -11.5) |
| [[C32 (line)]] | wt | 48.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 95.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 73.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 72.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9172), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FLCN]] | +0.71 | +0.75 / +0.57 | both halves | 1e-05 | STRING 498 |
| [[N4BP2L2]] | +0.69 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[ATP6V1G1]] | +0.67 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[GPRASP3]] | +0.65 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[FNIP1]] | +0.64 | +0.69 / +0.57 | both halves | 1e-05 | STRING 610 |
| [[MCCC1]] | +0.64 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[VPS11]] | +0.63 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[HEXA]] | +0.63 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[UFC1]] | +0.62 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[UAP1L1]] | +0.62 | +0.57 / +0.62 | both halves | 9e-06 |  |
| [[RRAGC]] | +0.62 | +0.67 / +0.52 | both halves | 1e-05 | pathway: Autophagy; STRING 881 |
| [[LRRC37B]] | +0.61 | +0.60 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MACROH2A1]] | -0.57 | -0.64 / -0.47 | both halves | 2e-05 |  |
| [[SRPK1]] | -0.57 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[NUP93]] | -0.56 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[TRAP1]] | -0.54 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[TFDP1]] | -0.53 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[IPO7]] | -0.52 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[TEX2]] | -0.52 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[FAR1]] | -0.52 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[SSX2IP]] | -0.52 | -0.44 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises TSC1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises TSC1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 122]] — Transferrin endocytosis and recycling; 40 genes; every member is in the + arm (projection on the module's main direction 0.713). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-18.5, 15.4); signed map (-1.3, -5.8). **Vector** length 91.4, 23.9% of its response variance represented; |z| ≥ 3 in 1,210 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.2 | +10.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +6.1 | +3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.2 | +2.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +17.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +4.0 | +23.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +3.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.2 | -0.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | +3.0 | -0.1 |
| fall | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | -4.1 | -4.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -3.8 | -5.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -6.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | -2.8 | -4.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.7 | -3.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.2 | -2.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.5 | +0.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.5 | +0.8 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -1.5 | +0.8 |

## What is on record

|  |  |
|---|---|
| Name | TSC complex subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.13 — chr9:132,891,348-132,946,874 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0243, LAM, hamartin; previously TSC |
| Gene groups (HGNC) | Armadillo like helical domain containing; TSC complex |
| Hallmark sets | APICAL_JUNCTION, MITOTIC_SPINDLE |
| Reactome | 11 pathways, smallest: Inhibition of TSC complex formation by AKT (PKB); Energy dependent regulation of mTOR by LKB1-AMPK; TBC/RABGAPs |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92574](https://www.uniprot.org/uniprotkb/Q92574) (Hamartin):

> Non-catalytic component of the TSC-TBC complex, a multiprotein complex that acts as a negative regulator of the canonical mTORC1 complex, an evolutionarily conserved central nutrient sensor that stimulates anabolic reactions and macromolecule biosynthesis to promote cellular biomass generation and growth. The TSC-TBC complex acts as a GTPase-activating protein (GAP) for the small GTPase RHEB, a direct activator of the protein kinase activity of mTORC1. In absence of nutrients, the TSC-TBC …

**Summary**, from NCBI Gene [7248](https://www.ncbi.nlm.nih.gov/gene/7248):

> This gene is a tumor suppressor gene that encodes the growth inhibitory protein hamartin. The encoded protein interacts with and stabilizes the GTPase activating protein tuberin. This hamartin-tuberin complex negatively regulates mammalian target of rapamycin complex 1 (mTORC1) signaling which is a major regulator of anabolic cell growth. This protein also functions as a co-chaperone for Hsp90 that inhibits its ATPase activity. This protein functions as a facilitator of Hsp90-mediated folding …

**Accessions** — [HGNC:12362](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12362) · Entrez [7248](https://www.ncbi.nlm.nih.gov/gene/7248) · UniProt [Q92574](https://www.uniprot.org/uniprotkb/Q92574) · Ensembl [ENSG00000165699](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165699)

## Data

Gene col 9172: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9172); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9172, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9172]; `tensor/DDL_lfc|DDL_z.npy` [9172]; `embed/gene_vectors.npy` [9172]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9172 or target_col == 9172). Every well: [[TSC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TSC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
