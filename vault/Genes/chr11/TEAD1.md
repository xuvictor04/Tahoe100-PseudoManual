---
symbol: "TEAD1"
type: "gene"
col: 11882
ensembl_id: "ENSG00000187079"
name: "TEA domain transcription factor 1"
location: "11p15.3"
module: 151
arm: "+"
pooled_cpm: 382.33
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 6
n_dd_up_clean: 7
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/151"]
generated_by: "tahoemap"
---

# TEAD1

*TEA domain transcription factor 1* — 11p15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.28× (z +22.7, q 0e+00, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.647× (z -8.2, q 2e-13, down in 39 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 0.772× (z -5.0, q 9e-05, down in 27 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 18 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (SNU-1 0.196×, LoVo 0.320×, SW480 0.465×; ⚠ toxic; transcription drop); [[Trametinib (drug)]] 5 µM in 1 line (C32 0.208×; ⚠ cell-cycle shift, explains ~43% of this change); [[Binimetinib (drug)]] 0.5 µM in 1 line (C32 0.237×); [[Binimetinib (drug)]] 5 µM in 1 line (C32 0.260×); [[Cobimetinib (drug)]] 0.5 µM in 1 line (C32 0.219×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CTNNAL1]] (+0.68, fdr 7e-06), [[MIR4435-2HG]] (+0.63, fdr 7e-06), [[SCHIP1]] (+0.62, fdr 7e-06); moves opposite to [[KCTD7]] (-0.60, fdr 1e-05), [[MAPKAPK5-AS1]] (-0.55, fdr 2e-05), [[USP30]] (-0.53, fdr 2e-05).
> It is in [[Module 151]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[CCN2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11882.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.28×** | +22.7 | 0e+00 | 41/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.62×** | +9.0 | 1e-16 | 39/48 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.57×** | +8.7 | 4e-16 | 37/48 (NCI-H460, SNU-1, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.45×** | +7.2 | 9e-11 | 34/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.40×** | +6.5 | 7e-09 | 33/48 (BT-474, NCI-H460, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +5.7 | 1e-06 | 28/48 (MIA PaCa-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.31×** | +5.3 | 1e-05 | 34/48 (NCI-H1573, HT-29, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.67×** | +5.2 | 1e-05 | 32/49 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.31×** | +5.2 | 1e-05 | 34/48 (BT-474, SNU-1, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +5.0 | 3e-05 | 27/50 (AsPC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.28×** | +4.9 | 6e-05 | 30/47 (NCI-H1573, HT-29, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.26×** | +4.5 | 3e-04 | 30/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.25×** | +4.4 | 5e-04 | 27/48 (BT-474, SNU-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.24×** | +4.1 | 0.002 | 23/48 (NCI-H460, J82, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.015 | 23/47 (NCI-H1573, HT-29, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.35×** | +3.0 | 0.079 | 23/49 (A549, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.12× | +3.0 | 0.086 | 10/48 (MIA PaCa-2, Hs 766T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11882.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 18 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (SNU-1 0.196×, LoVo 0.320×, SW480 0.465×; ⚠ toxic; transcription drop); [[Trametinib (drug)]] 5 µM in 1 line (C32 0.208×; ⚠ cell-cycle shift, explains ~43% of this change); [[Binimetinib (drug)]] 0.5 µM in 1 line (C32 0.237×); [[Binimetinib (drug)]] 5 µM in 1 line (C32 0.260×); [[Cobimetinib (drug)]] 0.5 µM in 1 line (C32 0.219×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.647×** | -8.2 | 2e-13 | 39/47 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.745×** | -5.5 | 1e-05 | 27/44 (SNU-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.772×** | -5.0 | 9e-05 | 27/48 (C32, H4, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.784×** | -4.8 | 3e-04 | 29/49 (SW480, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.774×** | -4.6 | 4e-04 | 26/45 (AN3 CA, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.791×** | -4.6 | 5e-04 | 31/48 (J82, C32, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.858× | -3.6 | 0.028 | 20/48 (C32, SK-MEL-2, …) | two highest doses | noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | 0.882× | -3.5 | 0.035 | 12/48 (NCI-H2030, AN3 CA, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.840× | -3.3 | 0.057 | 21/48 (C32, SK-MEL-2, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.846× | -3.3 | 0.057 | 21/48 (H4, LoVo, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.846× | -3.3 | 0.057 | 21/48 (SW48, C32, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~54% of this change | 0.841× | -3.2 | 0.064 | 20/48 (C32, SW480, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.856× | -3.0 | 0.10 | 23/49 (C32, SK-MEL-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11882. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 298 | 2 (1 ⚠) | 16 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +12.4) | [[Trametinib (drug)]] 5 µM 0.208× (z -19.7) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Binimetinib (drug)]] 0.5 µM 0.237× (z -19.6) |
| [[NCI-H460 (line)]] | wt | 305 | 16 (9 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +35.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 185 | 13 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.34× (z +38.0) | — |
| [[SK-MEL-2 (line)]] | alt | 392 | 3 (1 ⚠) | 10 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.54× (z +10.3) | [[Trametinib (drug)]] 5 µM 0.436× (z -9.9) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.391× (z -9.9) |
| [[HT-29 (line)]] | alt | 354 | 10 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +27.1) | — |
| [[PANC-1 (line)]] | alt | 319 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +27.9) | — |
| [[SNU-1 (line)]] | wt | 477 | 7 (5 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.39× (z +29.1) | [[Dinaciclib (drug)]] 5 µM 0.196× (z -16.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 187 | 8 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +21.0) | — |
| [[NCI-H23 (line)]] | alt | 336 | 4 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +28.7) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.457× (z -11.1) |
| [[RKO (line)]] | wt | 578 | 6 (4 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +15.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.382× (z -11.4) ⚠ toxic |
| [[A549 (line)]] | wt | 307 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +25.5) | — |
| [[AsPC-1 (line)]] | alt | 352 | 6 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +27.5) | [[Dinaciclib (drug)]] 0.05 µM 0.498× (z -9.5) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 401 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +20.9) | — |
| [[SW480 (line)]] | alt | 675 | 2 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.58× (z +10.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.448× (z -12.6) ⚠ toxic |
| [[SW48 (line)]] | wt | 528 | 0 | 6 (4 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.336× (z -12.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.394× (z -10.2) |
| [[hTERT-HPNE (line)]] | wt | 339 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +16.3) | — |
| [[J82 (line)]] | alt | 631 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +16.2) | — |
| [[LOX-IMVI (line)]] | wt | 810 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +12.2) | [[Dinaciclib (drug)]] 0.05 µM 0.354× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 217 | 4 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +10.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.324× (z -10.3) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 240 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +19.1) | — |
| [[HEC-1-A (line)]] | alt | 423 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.403× (z -11.2) ⚠ cell-cycle shift, explains ~80% of this change |
| [[KATO III (line)]] | alt | 220 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +15.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.469× (z -9.2) ⚠ toxic |
| [[LS 180 (line)]] | wt | 413 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.391× (z -11.5) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 419 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +20.4) | — |
| [[A498 (line)]] | wt | 363 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +23.7) | — |
| [[AN3 CA (line)]] | alt | 813 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.257× (z -10.9) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 477 | 1 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.43× (z +10.5) ⚠ cell-cycle shift, explains ~28% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.459× (z -9.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 565 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +10.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.492× (z -9.3) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 166 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +17.4) | — |
| [[NCI-H2030 (line)]] | alt | 285 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +10.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.417× (z -11.9) ⚠ toxic |
| [[A-172 (line)]] | wt | 479 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +13.7) | — |
| [[A-427 (line)]] | wt | 468 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +18.4) | — |
| [[LoVo (line)]] | wt | 371 | 1 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.13× (z +10.0) ⚠ cell-cycle shift, explains ~28% of this change | [[Dinaciclib (drug)]] 5 µM 0.320× (z -14.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 297 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +17.2) | — |
| [[SW 1271 (line)]] | alt | 254 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +9.0) | — |
| [[CFPAC-1 (line)]] | alt | 246 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +15.9) | — |
| [[CHP-212 (line)]] | wt | 405 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.264× (z -11.5) ⚠ toxic |
| [[H4 (line)]] | wt | 558 | 0 | 1 | — | [[Ponatinib (drug)]] 5 µM 0.388× (z -9.9) |
| [[HS-578T (line)]] | alt | 281 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +11.7) | — |
| [[NCI-H1792 (line)]] | alt | 367 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.595× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H661 (line)]] | alt | 276 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +8.7) | — |
| [[RPMI-7951 (line)]] | alt | 240 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +14.2) | — |
| [[SW 900 (line)]] | alt | 208 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +13.3) | — |
| [[SW1417 (line)]] | alt | 487 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +11.6) | — |
| [[HepG2_C3A (line)]] | wt | 250 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 370 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 377 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 377 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 196 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 314 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11882), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTNNAL1]] | +0.68 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[MIR4435-2HG]] | +0.63 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[SCHIP1]] | +0.62 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[WWC2]] | +0.60 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[CYTOR]] | +0.59 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[DCBLD2]] | +0.59 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[PTPN14]] | +0.58 | +0.47 / +0.59 | both halves | 2e-05 | STRING 445 |
| [[MYL12A]] | +0.58 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[CCND1]] | +0.57 | +0.54 / +0.58 | both halves | 1e-05 | pathway: Co-inhibition by PD-1; STRING 418 |
| [[TNFRSF12A]] | +0.57 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[SVIL]] | +0.57 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[MACF1]] | +0.57 | +0.41 / +0.66 | both halves | 4e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCTD7]] | -0.60 | -0.49 / -0.67 | both halves | 1e-05 |  |
| [[MAPKAPK5-AS1]] | -0.55 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[USP30]] | -0.53 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[MORN4]] | -0.53 | -0.46 / -0.54 | both halves | 2e-05 |  |
| [[NDUFAF7]] | -0.50 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[NUPR1]] | -0.50 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[FRG1GP]] | -0.50 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[IQSEC2]] | -0.50 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[TMEM143]] | -0.50 | -0.37 / -0.52 | both halves | 8e-05 |  |
| [[ZNF836]] | -0.49 | -0.40 / -0.53 | both halves | 4e-05 |  |
| [[CRYZL1]] | -0.49 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[C20orf96]] | -0.49 | -0.37 / -0.58 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCN2]] | B | CCN2 activity strengthens TEAD1's drug response | lines that do not express CCN2 (17) vs lines expressing it (32) | the lines without CCN2 respond 0.77× as strongly (z diff +1.32); strongest at Homoharringtonine 0.5 µM: 1.23x vs 1.73x (z diff +3.9) | 0.033 | ⚠ within organs, on part of the lines; also absent: GDNF-AS1, CPEB1, TRIML2; target measured in part of the lines; artifact flags |
| [[MAMLD1]] | B | MAMLD1 activity raises TEAD1's level | lines that do not express MAMLD1 (11) vs lines expressing it (39) | 1.34× lower at baseline in the lines without MAMLD1 | 0.041 | ⚠ within organs, on part of the lines; also absent: FHOD3, PGM5P2-1, CAV1 |
| [[NUPR1]] | B | NUPR1 activity lowers TEAD1's level | lines that do not express NUPR1 (24) vs lines expressing it (26) | 1.33× higher at baseline in the lines without NUPR1 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TTTY14, SPARC, PCDH18 |
| [[EPB41L2]] | B | EPB41L2 activity raises TEAD1's level | lines that do not express EPB41L2 (6) vs lines expressing it (44) | 1.46× lower at baseline in the lines without EPB41L2 | 0.071 | ⚠ within organs, on part of the lines; also absent: SLC26A2, CRTAP, FAM216A; maybe low, not absent |
| [[SCHIP1]] | B | SCHIP1 activity raises TEAD1's level | lines that do not express SCHIP1 (7) vs lines expressing it (43) | 1.25× lower at baseline in the lines without SCHIP1 | 0.087 | ⚠ within organs, on part of the lines; also absent: DYRK3, IQCJ-SCHIP1, ROBO3 |
| [[DDAH1]] | C | DDAH1 activity strengthens TEAD1's drug response | lines that do not express DDAH1 (3) vs lines expressing it (46) | the lines without DDAH1 respond 0.14× as strongly (z diff +3.31); strongest at Homoharringtonine 5 µM: 0.89x vs 2.35x (z diff +8.8) | 0.058 | ⚠ few lines (3 vs 47); across organs; also absent: MMP25, KDELR3, BCL2L1; maybe low, not absent; target measured in part of the lines; the reference differs; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 151]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.677). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (39.9, 10.4); signed map (11.5, 41.2). **Vector** length 142, 49.4% of its response variance represented; |z| ≥ 3 in 1,626 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.0 | -4.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +8.1 | +5.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.6 | -5.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.6 | +2.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +6.5 | +3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.3 | +3.0 |
|  | [[vincristine (drug)]] 0.5 µM |  | +5.2 | +1.0 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +4.4 | +1.6 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -7.4 | -3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -6.2 | -5.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.1 | -8.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~54% of this change | -6.0 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.4 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.7 | -1.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.1 | -3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.9 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | TEA domain transcription factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.3 — chr11:12,674,421-12,944,737 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TEF-1; previously TCF13, AA |
| Gene groups (HGNC) | TEA domain transcription factors |
| Reactome | 10 pathways, smallest: RUNX3 regulates YAP1-mediated transcription; YAP1- and WWTR1 (TAZ)-stimulated gene expression; EGR2 and SOX10-mediated initiation of Schwann cell myelination |
| Matched by | ensembl_id |

**Function**, from UniProt [P28347](https://www.uniprot.org/uniprotkb/P28347) (Transcriptional enhancer factor TEF-1):

> Transcription factor which plays a key role in the Hippo signaling pathway, a pathway involved in organ size control and tumor suppression by restricting proliferation and promoting apoptosis. The core of this pathway is composed of a kinase cascade wherein MST1/MST2, in complex with its regulatory protein SAV1, phosphorylates and activates LATS1/2 in complex with its regulatory protein MOB1, which in turn phosphorylates and inactivates YAP1 oncoprotein and WWTR1/TAZ. Acts by mediating gene …

**Summary**, from NCBI Gene [7003](https://www.ncbi.nlm.nih.gov/gene/7003):

> This gene encodes a ubiquitous transcriptional enhancer factor that is a member of the TEA/ATTS domain family. This protein directs the transactivation of a wide variety of genes and, in placental cells, also acts as a transcriptional repressor. Mutations in this gene cause Sveinsson's chorioretinal atrophy. Additional transcript variants have been described but their full-length natures have not been experimentally verified. [provided by RefSeq, May 2010]

**Accessions** — [HGNC:11714](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11714) · Entrez [7003](https://www.ncbi.nlm.nih.gov/gene/7003) · UniProt [P28347](https://www.uniprot.org/uniprotkb/P28347) · Ensembl [ENSG00000187079](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187079)

## Data

Gene col 11882: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11882); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11882, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11882]; `tensor/DDL_lfc|DDL_z.npy` [11882]; `embed/gene_vectors.npy` [11882]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11882 or target_col == 11882). Every well: [[TEAD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TEAD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
