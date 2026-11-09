---
symbol: "TYW1B"
type: "gene"
col: 15886
ensembl_id: "ENSG00000277149"
name: "tRNA-yW synthesizing protein 1 homolog B"
location: "7q11.22-q11.23"
module: 215
arm: "+"
pooled_cpm: 56.71
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 5
n_dd_up_clean: 21
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/215"]
generated_by: "tahoemap"
---

# TYW1B

*tRNA-yW synthesizing protein 1 homolog B* — 7q11.22-q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 10.4× (z +41.4, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.567× (z -10.1, q 4e-21, down in 33 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[vincristine (drug)]] 0.5 µM: 0.735× (z -3.9, q 0.010, down in 20 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (SW480 0.156×, SW1417 0.209×, PANC-1 0.251×, NCI-H23 0.163×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (SW480 0.222×, KATO III 0.159×, NCI-H2030 0.159×, C32 0.175×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SW480 0.322×, PANC-1 0.344×; ⚠ toxic; transcription drop); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (SNU-1 0.0477×); [[Filgotinib (drug)]] 5 µM in 1 line (SW 1088 0.0416×); [[Tofacitinib (drug)]] 5 µM in 1 line (C32 0.533×).
> Its strongest partners by |cos| (77 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 28 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARIH1]] (+0.49, fdr 9e-05), [[SLC25A5]] (+0.48, fdr 3e-04), [[RPS6KA5]] (+0.48, fdr 2e-04); moves opposite to [[ZSCAN20]] (-0.50, fdr 1e-04), [[ZNF304]] (-0.50, fdr 1e-04), [[RNF6]] (-0.48, fdr 0.001, ⚠ one half only (not replicated)), [[ZSCAN22]] (-0.48, fdr 2e-04).
> It is in [[Module 215]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15886.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **10.4×** | +41.4 | 0e+00 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **8.48×** | +37.8 | 0e+00 | 48/48 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **7.10×** | +34.6 | 0e+00 | 48/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.48×** | +22.7 | 0e+00 | 41/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.68×** | +17.4 | 0e+00 | 48/48 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.91×** | +11.4 | 3e-28 | 44/48 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.58×** | +11.4 | 3e-28 | 33/49 (AsPC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.53×** | +10.6 | 2e-24 | 41/48 (A498, SK-MEL-2, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.95×** | +10.0 | 1e-21 | 46/49 (SW480, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.69×** | +9.2 | 1e-18 | 41/49 (MIA PaCa-2, RKO, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.72×** | +9.2 | 3e-18 | 40/48 (HS-578T, A-172, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.71×** | +9.1 | 3e-18 | 36/50 (HS-578T, A-172, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.69×** | +8.9 | 3e-17 | 32/48 (MIA PaCa-2, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.55×** | +7.7 | 5e-13 | 32/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.52×** | +7.3 | 8e-12 | 35/48 (J82, RKO, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.42×** | +6.1 | 3e-08 | 33/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.92×** | +6.0 | 5e-08 | 36/48 (MIA PaCa-2, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.40×** | +5.9 | 1e-07 | 29/48 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.38×** | +5.7 | 3e-07 | 30/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15886.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (SW480 0.156×, SW1417 0.209×, PANC-1 0.251×, NCI-H23 0.163×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (SW480 0.222×, KATO III 0.159×, NCI-H2030 0.159×, C32 0.175×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SW480 0.322×, PANC-1 0.344×; ⚠ toxic; transcription drop); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (SNU-1 0.0477×); [[Filgotinib (drug)]] 5 µM in 1 line (SW 1088 0.0416×); [[Tofacitinib (drug)]] 5 µM in 1 line (C32 0.533×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.567×** | -10.1 | 4e-21 | 33/49 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.573×** | -9.5 | 6e-19 | 28/42 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.693×** | -6.0 | 3e-07 | 24/44 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~18% of this change | **0.766×** | -4.7 | 3e-04 | 26/48 (AsPC-1, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[vincristine (drug)]] 0.5 µM |  | **0.735×** | -3.9 | 0.010 | 20/48 (PANC-1, C32, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.823× | -3.2 | 0.12 | 19/47 (A549, SNU-423, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.52 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15886. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 109 | 15 (3 ⚠) | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 11.5× (z +35.4) | [[Dinaciclib (drug)]] 0.5 µM 0.156× (z -27.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 24.3 | 9 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 26.0× (z +25.3) | — |
| [[BT-474 (line)]] | alt | 69.7 | 9 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 9.35× (z +21.7) | — |
| [[NCI-H460 (line)]] | wt | 35.3 | 9 | 0 | [[Panobinostat (drug)]] 5 µM 18.0× (z +28.8) | — |
| [[PANC-1 (line)]] | alt | 65.2 | 5 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 6.84× (z +26.7) | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -19.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 113 | 5 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 8.30× (z +27.2) | [[Dinaciclib (drug)]] 0.5 µM 0.209× (z -20.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 57.3 | 6 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 11.7× (z +28.5) | [[Dinaciclib (drug)]] 0.5 µM 0.347× (z -12.3) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 27.2 | 7 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 33.7× (z +23.1) | [[Docetaxel (drug)]] 0.05 µM 0.225× (z -9.8) ⚠ transcription drop; cell-cycle shift, explains ~18% of this change |
| [[C32 (line)]] | wt | 102 | 4 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 5.13× (z +15.6) | [[Dinaciclib (drug)]] 5 µM 0.175× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Tofacitinib (drug)]] 5 µM 0.533× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 71.5 | 7 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 13.3× (z +25.6) | [[Dinaciclib (drug)]] 0.5 µM 0.294× (z -12.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 50.5 | 5 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 8.22× (z +20.6) | [[Dinaciclib (drug)]] 5 µM 0.378× (z -9.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 34.8 | 7 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 15.9× (z +24.8) | — |
| [[HS-578T (line)]] | alt | 32.5 | 7 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 18.3× (z +22.2) | — |
| [[LoVo (line)]] | wt | 57.6 | 7 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 13.5× (z +28.2) | — |
| [[LS 180 (line)]] | wt | 55.4 | 6 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 8.63× (z +18.9) | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -16.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 58.0 | 6 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 14.1× (z +22.5) | [[Dinaciclib (drug)]] 5 µM 0.334× (z -9.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 54.6 | 6 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 11.5× (z +21.2) | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -11.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 58.3 | 6 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 12.5× (z +21.9) | [[Dinaciclib (drug)]] 5 µM 0.237× (z -12.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 33.4 | 7 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 17.6× (z +21.5) | — |
| [[LOX-IMVI (line)]] | wt | 52.1 | 4 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 10.3× (z +20.0) | [[Dinaciclib (drug)]] 5 µM 0.247× (z -11.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 38.7 | 5 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 10.3× (z +20.4) | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -12.3) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 89.9 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 11.0× (z +19.0) | [[Dinaciclib (drug)]] 0.5 µM 0.151× (z -15.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 40.4 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 9.39× (z +19.6) | — |
| [[HEC-1-A (line)]] | alt | 84.4 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 9.35× (z +20.8) | [[Dinaciclib (drug)]] 5 µM 0.204× (z -14.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 72.3 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 8.10× (z +18.8) | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -12.3) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 23.9 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 23.7× (z +15.8) | — |
| [[J82 (line)]] | alt | 30.2 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 15.3× (z +23.3) | — |
| [[KATO III (line)]] | alt | 87.6 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 10.5× (z +27.5) | [[Dinaciclib (drug)]] 5 µM 0.159× (z -20.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 62.5 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 8.10× (z +20.9) | [[Dinaciclib (drug)]] 5 µM 0.159× (z -17.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 50.2 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 12.0× (z +20.4) | — |
| [[RPMI-7951 (line)]] | alt | 35.2 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 14.4× (z +17.6) | [[Dinaciclib (drug)]] 0.05 µM 0.124× (z -12.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 33.0 | 4 | 1 | [[Panobinostat (drug)]] 5 µM 12.3× (z +13.2) | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0477× (z -14.9) |
| [[SW 900 (line)]] | alt | 60.5 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 8.78× (z +19.0) | — |
| [[A-427 (line)]] | wt | 63.4 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.19× (z +17.8) | [[Dinaciclib (drug)]] 0.5 µM 0.282× (z -12.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 32.3 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 17.6× (z +23.5) | — |
| [[COLO 205 (line)]] | alt | 45.5 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 9.49× (z +15.7) | — |
| [[H4 (line)]] | wt | 33.0 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 20.1× (z +16.0) | — |
| [[Hs 766T (line)]] | wt | 26.2 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 25.8× (z +20.4) | — |
| [[NCI-H23 (line)]] | alt | 54.8 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.14× (z +19.2) | [[Dinaciclib (drug)]] 0.5 µM 0.163× (z -19.1) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 58.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 10.0× (z +11.5) | — |
| [[C-33 A (line)]] | alt | 59.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.90× (z +16.8) | — |
| [[CHP-212 (line)]] | wt | 66.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 9.34× (z +11.2) | — |
| [[HCT15 (line)]] | alt | 54.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 8.71× (z +14.2) | — |
| [[HepG2_C3A (line)]] | wt | 48.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 9.41× (z +15.9) | — |
| [[SHP-77 (line)]] | alt | 74.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.57× (z +15.3) | — |
| [[NCI-H661 (line)]] | alt | 54.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0708× (z -9.3) ⚠ toxic; cell-cycle shift, explains ~70% of this change |
| [[SW 1088 (line)]] | alt | 47.4 | 0 | 1 | — | [[Filgotinib (drug)]] 5 µM 0.0416× (z -8.8) |
| [[NCI-H2122 (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 69.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15886), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 13 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARIH1]] | +0.49 | +0.41 / +0.37 | both halves | 9e-05 |  |
| [[SLC25A5]] | +0.48 | +0.27 / +0.47 | both halves | 3e-04 |  |
| [[RPS6KA5]] | +0.48 | +0.31 / +0.44 | both halves | 2e-04 |  |
| [[SLC25A3]] | +0.48 | +0.32 / +0.39 | both halves | 2e-04 |  |
| [[SNHG25]] | +0.48 | +0.28 / +0.44 | both halves | 3e-04 |  |
| [[CUL3]] | +0.48 | +0.27 / +0.31 | both halves | 3e-04 |  |
| [[RBM6]] | +0.47 | +0.19 / +0.49 | ⚠ not reproduced | 8e-04 |  |
| [[UBAP2]] | +0.46 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[TUBD1]] | +0.45 | +0.25 / +0.47 | both halves | 4e-04 |  |
| [[SRGAP2B]] | +0.45 | +0.38 / +0.39 | both halves | 7e-05 |  |
| [[CASTOR3P]] | +0.45 | +0.39 / +0.41 | both halves | 5e-05 |  |
| [[COX5A]] ⚠ | +0.45 | +0.36 / +0.34 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[ACVR2A]] | +0.44 | +0.35 / +0.51 | both halves | 1e-04 |  |
| [[RPL36A]] | +0.44 | +0.24 / +0.39 | both halves | 5e-04 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 15 of them with an alert (⚠; 15 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZSCAN20]] | -0.50 | -0.46 / -0.34 | both halves | 1e-04 |  |
| [[ZNF304]] | -0.50 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[RNF6]] | -0.48 | -0.15 / -0.52 | ⚠ one half (not replicated) | 0.001 |  |
| [[ZSCAN22]] | -0.48 | -0.46 / -0.30 | both halves | 2e-04 |  |
| [[MANBAL]] | -0.48 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[PDAP1]] | -0.48 | -0.31 / -0.41 | both halves | 2e-04 |  |
| [[ZKSCAN8]] | -0.48 | -0.30 / -0.36 | both halves | 2e-04 |  |
| [[STX16]] | -0.47 | -0.26 / -0.47 | both halves | 4e-04 |  |
| [[SCRN1]] | -0.47 | -0.24 / -0.61 | both halves | 5e-04 |  |
| [[RIMOC1]] | -0.47 | -0.15 / -0.50 | ⚠ not reproduced | 0.001 |  |
| [[ZNF267]] | -0.47 | -0.38 / -0.44 | both halves | 7e-05 |  |
| [[ACTR8]] | -0.46 | -0.28 / -0.36 | both halves | 3e-04 |  |
| [[NRAS]] | -0.46 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[ZNF770]] | -0.45 | -0.29 / -0.36 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 215]]; 13 genes; every member is in the + arm (projection on the module's main direction -0.535). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-55.6, -12.0); signed map (-60.7, -1.1). **Vector** length 77.6, 20.3% of its response variance represented; |z| ≥ 3 in 1,454 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +10.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.7 | +5.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | +2.6 | +6.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +2.3 | +7.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +2.3 | +6.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.9 | +9.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.8 | +6.0 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.6 | +0.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.5 | +2.1 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.8 | -6.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.1 | -2.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.0 | -9.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.8 | -2.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.8 | -10.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.9 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | +0.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.2 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | tRNA-yW synthesizing protein 1 homolog B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.22-q11.23 — chr7:72,558,744-72,828,200 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RSAFD2, MGC87315, NCRNA00069, LINC00069 |
| Gene groups (HGNC) | Radical S-adenosylmethionine domain containing; tRNA-yW synthesizing protein 1 homologs |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6NUM6](https://www.uniprot.org/uniprotkb/Q6NUM6) (S-adenosyl-L-methionine-dependent tRNA 4-demethylwyosine synthase TYW1B):

> Involved in the biosynthesis of wybutosine, a hyper modified guanosine with a tricyclic base located at position 37 of eukaryotic phenylalanine tRNA (tRNA(Phe)) that contributes to maintenance of the translational reading frame (By similarity). Catalyzes the condensation of N-methylguanine with 2 carbon atoms from pyruvate to form the tricyclic 4-demethylwyosine, an intermediate in wybutosine biosynthesis (By similarity).

**Summary**, from NCBI Gene [441250](https://www.ncbi.nlm.nih.gov/gene/441250):

> Wybutosine is a hypermodified guanosine found in phenylalanine tRNA. Wybutosine functions to stabilize codon-anticodon interactions during ribosome decoding and therefore supports the maintenance of the reading frame. In yeast, the homolog of this gene is essential for the synthesis of wybutosine. The human genome contains two closely related genes that putatively function in wybutosine synthesis. The open reading frame of this locus is disrupted in some individuals. Thus, this locus appears to …

**Accessions** — [HGNC:33908](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33908) · Entrez [441250](https://www.ncbi.nlm.nih.gov/gene/441250) · UniProt [Q6NUM6](https://www.uniprot.org/uniprotkb/Q6NUM6) · Ensembl [ENSG00000277149](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000277149)

## Data

Gene col 15886: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15886); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15886, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15886]; `tensor/DDL_lfc|DDL_z.npy` [15886]; `embed/gene_vectors.npy` [15886]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15886 or target_col == 15886). Every well: [[TYW1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TYW1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
