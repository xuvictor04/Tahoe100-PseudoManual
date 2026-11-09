---
symbol: "NFATC3"
type: "gene"
col: 1027
ensembl_id: "ENSG00000072736"
name: "nuclear factor of activated T cells 3"
location: "16q22.1"
module: 186
arm: "+"
pooled_cpm: 107.12
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 8
n_dd_up_clean: 14
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/186"]
generated_by: "tahoemap"
---

# NFATC3

*nuclear factor of activated T cells 3* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.08× (z +22.2, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.584× (z -16.3, q 0e+00, down in 41 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.05 µM: 0.802× (z -6.2, q 6e-08, down in 24 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (A-427 0.195×, SW480 0.327×, MIA PaCa-2 0.324×, A498 0.343×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (SW480 0.165×, NCI-H2030 0.307×, MIA PaCa-2 0.339×, A498 0.355×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (SW480 0.299×, SW 900 0.199×, NCI-H2030 0.295×, MIA PaCa-2 0.362×; ⚠ toxic; transcription drop); [[Vortioxetine (drug)]] 0.05 µM in 1 line (SW 1088 0.0797×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.570×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TNPO3]] (+0.73, fdr 1e-05), [[NR2F6]] (+0.71, fdr 7e-06), [[ANKRD13D]] (+0.70, fdr 7e-06); moves opposite to [[NOTCH2NLC]] (-0.67, fdr 1e-05), [[HIVEP2]] (-0.66, fdr 1e-05), [[RIPK2-DT]] (-0.66, fdr 7e-06).
> It is in [[Module 186]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[EGFR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1027.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.08×** | +22.2 | 0e+00 | 47/48 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.06×** | +21.9 | 0e+00 | 47/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.84×** | +18.5 | 0e+00 | 47/48 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +16.0 | 0e+00 | 42/49 (NCI-H460, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.56×** | +13.4 | 1e-38 | 45/48 (HOP62, J82, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.48×** | +11.2 | 4e-27 | 35/48 (HOP62, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.43×** | +10.9 | 9e-26 | 40/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.41×** | +10.4 | 1e-23 | 36/48 (HOP62, C32, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.39×** | +10.0 | 7e-22 | 38/48 (HOP62, J82, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.53×** | +6.7 | 1e-09 | 35/49 (CFPAC-1, J82, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.30×** | +5.6 | 8e-07 | 31/49 (HOP62, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.21×** | +5.5 | 2e-06 | 22/48 (LoVo, NCI-H460, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~72% of this change | 1.20× | +5.5 | 2e-06 | 20/48 (LoVo, NCI-H460, …) | two highest doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.40×** | +5.3 | 5e-06 | 26/45 (J82, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.37×** | +5.0 | 2e-05 | 24/48 (PANC-1, A498, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.33×** | +4.5 | 3e-04 | 20/49 (KATO III, C32, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.15× | +4.3 | 6e-04 | 16/49 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.12× | +3.3 | 0.028 | 10/48 (HepG2/C3A, C32, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1027.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (A-427 0.195×, SW480 0.327×, MIA PaCa-2 0.324×, A498 0.343×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (SW480 0.165×, NCI-H2030 0.307×, MIA PaCa-2 0.339×, A498 0.355×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (SW480 0.299×, SW 900 0.199×, NCI-H2030 0.295×, MIA PaCa-2 0.362×; ⚠ toxic; transcription drop); [[Vortioxetine (drug)]] 0.05 µM in 1 line (SW 1088 0.0797×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.570×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.584×** | -16.3 | 0e+00 | 41/49 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.602×** | -14.8 | 0e+00 | 33/44 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.627×** | -13.1 | 5e-37 | 30/45 (SW480, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.799×** | -9.6 | 8e-20 | 27/48 (HOP62, J82, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.793×** | -7.1 | 2e-10 | 31/48 (A-427, HOP62, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.802×** | -6.2 | 6e-08 | 24/47 (HOP62, RKO, …) | all doses, flat | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.827×** | -5.8 | 5e-07 | 24/48 (MIA PaCa-2, A498, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.829×** | -5.7 | 8e-07 | 24/48 (NCI-H1573, HOP62, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | 0.843× | -5.0 | 4e-05 | 21/48 (HOP62, A-172, …) | all doses, flat | composition shift |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.866× | -4.4 | 7e-04 | 20/48 (HT-29, COLO 205, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.913× | -3.9 | 0.005 | 12/49 (SW480, HT-29, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.877× | -3.9 | 0.005 | 12/47 (HT-29, COLO 205, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.883× | -3.8 | 0.006 | 12/47 (BT-474, NCI-H1573, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.890× | -3.6 | 0.015 | 13/47 (HT-29, SW 900, …) | rises with dose |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.893× | -3.5 | 0.021 | 6/47 (HEC-1-A, LS 180, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | 0.859× | -3.3 | 0.036 | 10/48 (NCI-H460, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 0.906× | -3.0 | 0.078 | 7/47 (NCI-H2030, SW 1271, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1027. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 102 | 8 | 5 (5 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.20× (z +12.2) | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -17.2) ⚠ cell-cycle shift, explains ~58% of this change |
| [[NCI-H460 (line)]] | wt | 137 | 7 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +15.3) | [[Dinaciclib (drug)]] 0.5 µM 0.487× (z -12.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 77.5 | 5 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.41× (z +11.5) | [[Lonafarnib (drug)]] 5 µM 0.157× (z -12.8) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 159 | 3 | 5 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.27× (z +13.2) | [[Dinaciclib (drug)]] 0.5 µM 0.324× (z -18.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.570× (z -9.0) |
| [[LS 180 (line)]] | wt | 84.6 | 4 (2 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.32× (z +15.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.39× (z +11.4) | [[Dinaciclib (drug)]] 0.05 µM 0.305× (z -14.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 288 | 4 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.03× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.165× (z -32.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 135 | 2 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 1.91× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -25.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 82.1 | 5 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.75× (z +13.4) | [[Dinaciclib (drug)]] 0.5 µM 0.511× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 151 | 3 | 3 (3 ⚠) | [[Belinostat (drug)]] 5 µM 2.24× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.307× (z -17.3) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 79.7 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.58× (z +12.5) | [[Dinaciclib (drug)]] 0.5 µM 0.471× (z -9.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 80.2 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.37× (z +12.0) | [[Homoharringtonine (drug)]] 5 µM 0.513× (z -13.2) ⚠ cell-cycle shift, explains ~58% of this change |
| [[NCI-H1792 (line)]] | alt | 107 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.52× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.453× (z -10.1) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 119 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.38× (z +9.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.447× (z -8.9) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 123 | 2 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 1.97× (z +9.4) | [[Dinaciclib (drug)]] 0.05 µM 0.400× (z -11.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 135 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.343× (z -16.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 66.2 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.59× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.424× (z -9.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 103 | 3 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.59× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.450× (z -8.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 38.1 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.03× (z +14.0) | — |
| [[LoVo (line)]] | wt | 80.7 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.07× (z +11.2) | [[Dinaciclib (drug)]] 0.05 µM 0.520× (z -9.3) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 72.2 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.34× (z +10.9) | — |
| [[NCI-H1573 (line)]] | alt | 73.2 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.77× (z +13.9) | [[Harringtonine (drug)]] 0.5 µM 0.411× (z -12.1) ⚠ cell-cycle shift, explains ~13% of this change |
| [[PANC-1 (line)]] | alt | 84.5 | 2 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.79× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.408× (z -16.1) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 107 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.199× (z -17.8) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 78.9 | 3 | 0 | [[Belinostat (drug)]] 5 µM 2.81× (z +10.6) | — |
| [[NCI-H23 (line)]] | alt | 102 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.09× (z +9.8) | — |
| [[NCI-H2347 (line)]] | alt | 49.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.36× (z +10.0) | — |
| [[SNU-423 (line)]] | alt | 65.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.34× (z +9.6) | — |
| [[A-172 (line)]] | wt | 56.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.485× (z -12.7) ⚠ cell-cycle shift, explains ~58% of this change |
| [[A549 (line)]] | wt | 97.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.36× (z +11.9) | — |
| [[HepG2_C3A (line)]] | wt | 224 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.313× (z -12.9) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 91.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.15× (z +8.9) | — |
| [[AN3 CA (line)]] | alt | 181 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.249× (z -11.1) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 148 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.436× (z -10.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 90.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +9.1) | — |
| [[HCT15 (line)]] | alt | 86.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.57× (z +9.0) | — |
| [[HS-578T (line)]] | alt | 73.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.370× (z -9.6) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 69.7 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.362× (z -9.1) ⚠ cell-cycle shift, explains ~51% of this change |
| [[Panc 03.27 (line)]] | alt | 53.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.58× (z +9.7) | — |
| [[RPMI-7951 (line)]] | alt | 81.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +12.7) | — |
| [[SHP-77 (line)]] | alt | 126 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 1.99× (z +8.8) | — |
| [[SNU-1 (line)]] | wt | 113 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.395× (z -8.6) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 85.3 | 0 | 1 | — | [[Vortioxetine (drug)]] 0.05 µM 0.0797× (z -9.4) |
| [[SW48 (line)]] | wt | 98.9 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 2.92× (z +9.6) | — |
| [[BT-474 (line)]] | alt | 84.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 164 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 88.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 90.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 122 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1027), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNPO3]] | +0.73 | +0.76 / +0.57 | both halves | 1e-05 |  |
| [[NR2F6]] | +0.71 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[ANKRD13D]] | +0.70 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[SAP130]] | +0.70 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[UBE2G1]] | +0.70 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[SRPK2]] | +0.69 | +0.74 / +0.56 | both halves | 1e-05 |  |
| [[PPP2R5E]] | +0.68 | +0.73 / +0.55 | both halves | 1e-05 |  |
| [[GRB2]] | +0.68 | +0.73 / +0.52 | both halves | 1e-05 | pathway: FCERI mediated Ca+2 mobilization |
| [[MRPL34]] | +0.67 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[ARMH3]] | +0.66 | +0.70 / +0.50 | both halves | 1e-05 |  |
| [[TAF5L]] | +0.66 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[TYW1]] | +0.66 | +0.66 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOTCH2NLC]] | -0.67 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[HIVEP2]] | -0.66 | -0.57 / -0.66 | both halves | 1e-05 |  |
| [[RIPK2-DT]] | -0.66 | -0.59 / -0.63 | both halves | 7e-06 |  |
| [[LIG4]] | -0.66 | -0.61 / -0.57 | both halves | 1e-05 |  |
| [[ZNF655]] | -0.64 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[NOTCH2NLB]] | -0.64 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[CGGBP1]] | -0.63 | -0.66 / -0.47 | both halves | 2e-05 |  |
| [[APLF]] | -0.61 | -0.64 / -0.43 | both halves | 3e-05 |  |
| [[ZNF776]] | -0.61 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[TRMT13]] | -0.61 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[ZC3H11A]] | -0.61 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[ETS1]] | -0.60 | -0.48 / -0.65 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EGFR]] | B | EGFR activity lowers NFATC3's level | lines that do not express EGFR (7) vs lines expressing it (43) | 1.68× higher at baseline in the lines without EGFR | 0.044 | ⚠ within organs, on part of the lines; also absent: C1RL-AS1, PSD4, RNASEL |
| [[CHGB]] | B | CHGB activity raises NFATC3's level | lines that do not express CHGB (33) vs lines expressing it (17) | 1.42× lower at baseline in the lines without CHGB | 0.089 | ⚠ within organs, on part of the lines; also absent: MAGEA4, SLC6A11, CTNNA2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 186]]; 20 genes; every member is in the + arm (projection on the module's main direction 0.667). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-11.5, -7.2); signed map (-42.6, 2.6). **Vector** length 115, 33.8% of its response variance represented; |z| ≥ 3 in 1,204 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +6.9 | +13.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.8 | +11.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.1 | +10.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.6 | +10.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.1 | +5.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +3.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +2.5 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +2.1 | +2.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | -13.4 | -9.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -11.2 | -7.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -9.2 | -13.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -8.6 | -14.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -8.5 | -16.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.7 | -5.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.6 | -0.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.4 | -6.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.0 | -3.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.9 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | nuclear factor of activated T cells 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:68,084,751-68,229,259 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NFAT4, NFATX, n339260 |
| Gene groups (HGNC) | Nuclear factors of activated T-cells; IPT domain containing |
| Reactome | 10 pathways, smallest: Calcineurin activates NFAT; CLEC7A (Dectin-1) induces NFAT activation; FCERI mediated Ca+2 mobilization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12968](https://www.uniprot.org/uniprotkb/Q12968) (Nuclear factor of activated T-cells, cytoplasmic 3):

> Acts as a regulator of transcriptional activation. Binds to the TNFSF11/RANKL promoter region and promotes TNFSF11 transcription (By similarity). Binding to the TNFSF11 promoter region is increased by high levels of Ca(2+) which induce NFATC3 expression and may lead to regulation of TNFSF11 expression in osteoblasts (By similarity). Plays a role in promoting mesenteric arterial wall remodeling in response to the intermittent hypoxia-induced increase in EDN1 and ROCK signaling (By similarity). …

**Summary**, from NCBI Gene [4775](https://www.ncbi.nlm.nih.gov/gene/4775):

> The product of this gene is a member of the nuclear factors of activated T cells DNA-binding transcription complex. This complex consists of at least two components: a preexisting cytosolic component that translocates to the nucleus upon T cell receptor (TCR) stimulation and an inducible nuclear component. Other members of this family participate to form this complex also. The product of this gene plays a role in the regulation of gene expression in T cells and immature thymocytes. Several …

**Accessions** — [HGNC:7777](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7777) · Entrez [4775](https://www.ncbi.nlm.nih.gov/gene/4775) · UniProt [Q12968](https://www.uniprot.org/uniprotkb/Q12968) · Ensembl [ENSG00000072736](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000072736)

## Data

Gene col 1027: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1027); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1027, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1027]; `tensor/DDL_lfc|DDL_z.npy` [1027]; `embed/gene_vectors.npy` [1027]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1027 or target_col == 1027). Every well: [[NFATC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NFATC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
