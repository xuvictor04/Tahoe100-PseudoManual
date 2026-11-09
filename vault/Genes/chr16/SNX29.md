---
symbol: "SNX29"
type: "gene"
col: 535
ensembl_id: "ENSG00000048471"
name: "sorting nexin 29"
location: "16p13.13-p13.12"
module: 72
arm: "+"
pooled_cpm: 73.7
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 17
n_dd_up_clean: 16
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# SNX29

*sorting nexin 29* — 16p13.13-p13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.55× (z +29.1, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (13 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.492× (z -13.6, q 2e-39, down in 42 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.405× (z -7.9, q 2e-13, down in 37 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TANGO2]] (+0.70, fdr 1e-05), [[DYNC1I1]] (+0.68, fdr 7e-06), [[EXOC6B]] (+0.67, fdr 7e-06); moves opposite to [[KBTBD2]] (-0.55, fdr 2e-05), [[CFH]] (-0.52, fdr 1e-04), [[SLC39A1]] (-0.51, fdr 3e-05).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 535.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.55×** | +29.1 | 0e+00 | 48/48 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.68×** | +25.0 | 0e+00 | 48/48 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.28×** | +22.8 | 0e+00 | 47/48 (KATO III, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **3.06×** | +21.5 | 0e+00 | 47/48 (HOP62, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **3.17×** | +20.4 | 0e+00 | 46/48 (NCI-H1792, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.86×** | +20.1 | 0e+00 | 45/48 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.00×** | +13.3 | 1e-38 | 47/48 (SK-MEL-2, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.38×** | +8.8 | 9e-17 | 28/49 (MIA PaCa-2, RKO, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.50×** | +7.8 | 4e-13 | 38/48 (SK-MEL-2, SNU-423, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +7.1 | 8e-11 | 31/48 (KATO III, SW1417, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.22×** | +7.0 | 1e-10 | 39/49 (SK-MEL-2, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.40×** | +6.4 | 6e-09 | 34/48 (RKO, LOX-IMVI, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.40×** | +6.2 | 2e-08 | 32/48 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.34×** | +5.4 | 3e-06 | 25/47 (HEC-1-A, A498, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.48×** | +5.3 | 4e-06 | 28/49 (NCI-H1792, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.26×** | +4.4 | 3e-04 | 25/49 (RKO, MIA PaCa-2, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.22×** | +3.8 | 0.004 | 19/48 (A-172, LOX-IMVI, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +3.7 | 0.006 | 14/48 (MIA PaCa-2, SW48, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 14 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 535.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.492×** | -13.6 | 2e-39 | 42/48 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.510×** | -12.4 | 6e-33 | 32/43 (hTERT-HPNE, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.532×** | -12.1 | 2e-31 | 38/49 (A-427, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.565×** | -10.1 | 6e-22 | 36/44 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.600×** | -9.8 | 1e-20 | 36/48 (PANC-1, H4, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.620×** | -8.8 | 1e-16 | 27/48 (HS-578T, A-172, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.405×** | -7.9 | 2e-13 | 37/49 (HS-578T, RPMI-7951, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~58% of this change | **0.672×** | -7.6 | 2e-12 | 31/47 (hTERT-HPNE, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.709×** | -6.3 | 2e-08 | 29/47 (NCI-H2030, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.725×** | -6.2 | 4e-08 | 28/48 (PANC-1, hTERT-HPNE, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.532×** | -5.5 | 2e-06 | 24/48 (A-172, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **0.746×** | -5.4 | 3e-06 | 27/47 (LoVo, J82, …) | top dose only |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.842× | -4.6 | 2e-04 | 18/49 (Panc 03.27, NCI-H2347, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.792×** | -4.5 | 3e-04 | 23/48 (PANC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.801×** | -4.3 | 8e-04 | 22/48 (HS-578T, A-172, …) | inconsistent across doses |  |
| [[Sulfatinib (drug)]] 5 µM |  | **0.824×** | -3.6 | 0.013 | 21/49 (J82, A-172, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.668×** | -3.5 | 0.013 | 17/48 (HS-578T, A-172, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.840× | -3.1 | 0.056 | 17/47 (RKO, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, -0.61 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 535. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 125 | 5 | 12 (11 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.64× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -20.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.144× (z -9.9) |
| [[A-172 (line)]] | wt | 127 | 6 | 9 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 3.42× (z +13.7) | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.442× (z -9.1) |
| [[hTERT-HPNE (line)]] | wt | 148 | 3 | 12 (12 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 3.79× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.0630× (z -23.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 60.7 | 6 | 9 (9 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 6.20× (z +19.4) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.298× (z -12.9) ⚠ cell-cycle shift, explains ~35% of this change |
| [[HEC-1-A (line)]] | alt | 56.5 | 12 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.63× (z +15.5) | [[Lonafarnib (drug)]] 5 µM 0.0794× (z -11.7) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 49.5 | 7 | 6 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 5.56× (z +19.8) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.220× (z -17.5) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.180× (z -9.1) |
| [[A498 (line)]] | wt | 58.9 | 9 (1 ⚠) | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 6.16× (z +17.7) | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -14.1) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 63.2 | 7 | 5 (5 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 6.70× (z +20.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.261× (z -14.2) ⚠ cell-cycle shift, explains ~35% of this change |
| [[Hs 766T (line)]] | wt | 75.6 | 10 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 6.10× (z +17.0) | [[Dinaciclib (drug)]] 5 µM 0.131× (z -18.4) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 110 | 3 | 9 (9 ⚠) | [[Panobinostat (drug)]] 5 µM 4.03× (z +14.1) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.256× (z -13.8) ⚠ cell-cycle shift, explains ~35% of this change |
| [[LOX-IMVI (line)]] | wt | 65.1 | 7 | 5 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 5.90× (z +17.6) | [[Digitoxin (drug)]] 5 µM 0.246× (z -13.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 58.4 | 6 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 6.01× (z +17.3) | [[Dinaciclib (drug)]] 0.05 µM 0.233× (z -13.0) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 93.7 | 4 | 6 (6 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 6.86× (z +14.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.154× (z -14.4) ⚠ cell-cycle shift, explains ~35% of this change |
| [[KATO III (line)]] | alt | 61.5 | 8 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 10.1× (z +24.0) | [[Dinaciclib (drug)]] 0.5 µM 0.328× (z -11.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 50.9 | 8 (3 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.09× (z +20.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.332× (z -12.0) ⚠ toxic; cell-cycle shift, explains ~25% of this change |
| [[SK-MEL-2 (line)]] | alt | 80.2 | 7 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 5.85× (z +17.0) | [[Homoharringtonine (drug)]] 5 µM 0.493× (z -9.7) ⚠ cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 78.2 | 8 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.08× (z +18.8) | [[Dinaciclib (drug)]] 0.5 µM 0.427× (z -9.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 42.4 | 7 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 8.40× (z +18.7) | [[Dinaciclib (drug)]] 0.05 µM 0.333× (z -9.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 141 | 1 | 7 (6 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.83× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.157× (z -18.1) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.129× (z -9.2) |
| [[SW 900 (line)]] | alt | 45.0 | 7 | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 6.12× (z +12.9) | [[Docetaxel (drug)]] 0.05 µM 0.288× (z -9.6) ⚠ transcription drop; cell-cycle shift, explains ~58% of this change |
| [[HepG2_C3A (line)]] | wt | 71.1 | 6 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 8.15× (z +15.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.237× (z -10.1) ⚠ toxic |
| [[HT-29 (line)]] | alt | 79.9 | 6 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.74× (z +16.5) | [[Dinaciclib (drug)]] 0.5 µM 0.403× (z -9.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 55.0 | 7 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.46× (z +16.5) | — |
| [[NCI-H1573 (line)]] | alt | 84.0 | 6 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 4.58× (z +15.4) | [[Dinaciclib (drug)]] 5 µM 0.117× (z -21.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 78.7 | 6 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 7.78× (z +19.9) | [[Digitoxin (drug)]] 5 µM 0.363× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 66.6 | 4 (1 ⚠) | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.94× (z +13.3) | [[Dinaciclib (drug)]] 0.5 µM 0.137× (z -19.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 43.0 | 7 | 0 | [[Panobinostat (drug)]] 5 µM 5.97× (z +14.7) | — |
| [[SW480 (line)]] | alt | 141 | 5 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.40× (z +16.4) | [[Dinaciclib (drug)]] 5 µM 0.197× (z -17.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 57.0 | 4 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 10.4× (z +19.5) | [[Digitoxin (drug)]] 5 µM 0.319× (z -9.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 88.2 | 6 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.52× (z +12.3) | — |
| [[C32 (line)]] | wt | 65.7 | 6 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.62× (z +16.0) | — |
| [[COLO 205 (line)]] | alt | 180 | 4 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 4.77× (z +14.7) | [[Dinaciclib (drug)]] 0.5 µM 0.150× (z -17.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 64.8 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.26× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.136× (z -16.9) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 69.4 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.87× (z +13.8) | [[Dinaciclib (drug)]] 0.5 µM 0.322× (z -11.6) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 74.7 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.23× (z +13.4) | [[Dinaciclib (drug)]] 0.05 µM 0.207× (z -11.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 81.3 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.81× (z +9.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.117× (z -19.8) ⚠ toxic |
| [[RKO (line)]] | wt | 41.2 | 4 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.59× (z +13.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.174× (z -11.8) ⚠ toxic |
| [[SW48 (line)]] | wt | 46.9 | 4 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 5.57× (z +10.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.212× (z -8.9) ⚠ toxic |
| [[A-427 (line)]] | wt | 69.6 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.00× (z +15.1) | [[Dinaciclib (drug)]] 0.5 µM 0.0853× (z -26.8) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 54.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.69× (z +11.4) | — |
| [[NCI-H2347 (line)]] | alt | 33.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.11× (z +12.5) | — |
| [[SNU-1 (line)]] | wt | 44.4 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.81× (z +9.2) | — |
| [[SW 1088 (line)]] | alt | 118 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.103× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Bestatin (drug)]] 0.05 µM 0.103× (z -9.6) |
| [[NCI-H596 (line)]] | alt | 78.7 | 0 | 2 | — | [[Atazanavir (sulfate) (drug)]] 0.05 µM 0.165× (z -14.7) |
| [[Panc 03.27 (line)]] | alt | 60.7 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.93× (z +14.0) | — |
| [[AN3 CA (line)]] | alt | 59.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.46× (z +8.5) | — |
| [[CHP-212 (line)]] | wt | 48.8 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.122× (z -8.8) ⚠ toxic |
| [[SW 1271 (line)]] | alt | 57.6 | 0 | 1 | — | [[Cepharanthine (drug)]] 0.5 µM 0.0817× (z -9.0) |
| [[NCI-H2122 (line)]] | alt | 80.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 47.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 535), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TANGO2]] | +0.70 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[DYNC1I1]] | +0.68 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[EXOC6B]] | +0.67 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[PCYT1A]] | +0.66 | +0.69 / +0.57 | both halves | 1e-05 |  |
| [[ANKRD39]] | +0.65 | +0.66 / +0.47 | both halves | 2e-05 |  |
| [[EPS15L1]] | +0.64 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[KIF1B]] | +0.63 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[PSMB4]] | +0.63 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[PWWP3A]] | +0.61 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[PSMD13]] | +0.60 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[HSP90AA2P]] | +0.58 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[TM2D2]] | +0.58 | +0.67 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KBTBD2]] | -0.55 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[CFH]] | -0.52 | -0.36 / -0.49 | both halves | 1e-04 |  |
| [[SLC39A1]] | -0.51 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[ZNF608]] | -0.51 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[TIFA]] | -0.50 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[CYB5RL]] | -0.50 | -0.46 / -0.28 | both halves | 3e-04 |  |
| [[PAXIP1-DT]] | -0.50 | -0.48 / -0.29 | both halves | 2e-04 |  |
| [[PAXIP1]] | -0.49 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[TEF]] | -0.49 | -0.43 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.714). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.5, -8.3); signed map (-28.3, -26.0). **Vector** length 109, 35.0% of its response variance represented; |z| ≥ 3 in 1,679 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +14.0 | +21.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +14.0 | +20.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +14.0 | +20.4 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | +6.3 | +4.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +6.0 | +5.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.8 | +2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +0.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.4 | +0.1 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.8 | -6.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -7.2 | -2.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | -6.7 | -7.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | -6.0 | -8.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.0 | -10.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.0 | -5.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.3 | +2.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.8 | -2.9 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -1.5 | -3.6 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.4 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | sorting nexin 29 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.13-p13.12 — chr16:11,976,734-12,574,287 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12363; previously RUNDC2A |
| Gene groups (HGNC) | Sorting nexins; RUN domain containing |
| Matched by | ensembl_id |

UniProt [Q8TEQ0](https://www.uniprot.org/uniprotkb/Q8TEQ0) carries no function annotation.

**Summary**, from NCBI Gene [92017](https://www.ncbi.nlm.nih.gov/gene/92017):

> Predicted to enable phosphatidylinositol binding activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30542](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30542) · Entrez [92017](https://www.ncbi.nlm.nih.gov/gene/92017) · UniProt [Q8TEQ0](https://www.uniprot.org/uniprotkb/Q8TEQ0) · Ensembl [ENSG00000048471](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000048471)

## Data

Gene col 535: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 535); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 535, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 535]; `tensor/DDL_lfc|DDL_z.npy` [535]; `embed/gene_vectors.npy` [535]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 535 or target_col == 535). Every well: [[SNX29 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNX29.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
