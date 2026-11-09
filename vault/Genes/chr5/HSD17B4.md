---
symbol: "HSD17B4"
type: "gene"
col: 5480
ensembl_id: "ENSG00000133835"
name: "hydroxysteroid 17-beta dehydrogenase 4"
location: "5q23.1"
module: 57
arm: "+"
pooled_cpm: 48.91
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 15
n_dd_up_clean: 18
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# HSD17B4

*hydroxysteroid 17-beta dehydrogenase 4* — 5q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.58× (z +13.3, q 1e-37, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.402× (z -18.8, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GNPDA2]] (+0.77, fdr 7e-06), [[BLMH]] (+0.74, fdr 7e-06), [[NDRG3]] (+0.74, fdr 7e-06); moves opposite to [[PPP1R14B-AS1]] (-0.62, fdr 1e-05), [[TOB2]] (-0.60, fdr 1e-05), [[TNRC6C]] (-0.59, fdr 4e-05).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MAP2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5480.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.58×** | +13.3 | 1e-37 | 46/48 (SW480, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.79×** | +12.0 | 1e-30 | 40/48 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.77×** | +11.7 | 1e-29 | 43/48 (LOX-IMVI, HOP62, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.82×** | +11.7 | 2e-29 | 46/48 (LOX-IMVI, A498, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.76×** | +11.7 | 2e-29 | 44/48 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.75×** | +11.5 | 1e-28 | 43/48 (LOX-IMVI, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.73×** | +11.3 | 9e-28 | 43/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.75×** | +11.1 | 1e-26 | 33/42 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.59×** | +9.5 | 1e-19 | 40/48 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.56×** | +9.2 | 2e-18 | 41/48 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.52×** | +8.7 | 2e-16 | 41/48 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.49×** | +7.7 | 9e-13 | 31/44 (J82, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.87×** | +6.7 | 7e-10 | 38/48 (PANC-1, AsPC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.32×** | +5.7 | 4e-07 | 27/48 (J82, RKO, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.33×** | +5.6 | 9e-07 | 26/47 (A498, SW48, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.20×** | +4.4 | 4e-04 | 21/48 (SW480, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.33×** | +4.2 | 0.001 | 14/48 (LOX-IMVI, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.23×** | +4.1 | 0.001 | 18/48 (SK-MEL-2, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5480.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.402×** | -18.8 | 0e+00 | 45/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.406×** | -18.6 | 0e+00 | 43/47 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.468×** | -15.7 | 0e+00 | 44/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.508×** | -14.0 | 3e-42 | 43/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.676×** | -11.5 | 2e-28 | 39/48 (NCI-H23, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.718×** | -9.7 | 3e-20 | 29/48 (NCI-H1573, AN3 CA, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.720×** | -6.8 | 9e-10 | 31/48 (MIA PaCa-2, HCT15, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.801×** | -6.5 | 7e-09 | 29/48 (MIA PaCa-2, KATO III, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.768×** | -5.5 | 3e-06 | 27/47 (hTERT-HPNE, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.791×** | -4.8 | 7e-05 | 24/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.802×** | -4.4 | 6e-04 | 20/48 (RKO, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.940× | -4.2 | 0.001 | 1/49 (SW 1271) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.826×** | -4.0 | 0.003 | 19/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.828×** | -3.9 | 0.004 | 22/48 (SW480, SNU-1, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.699×** | -3.9 | 0.004 | 17/48 (BT-474, SW480, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.724×** | -3.5 | 0.017 | 17/49 (SNU-1, NCI-H1573, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 0.891× | -3.4 | 0.024 | 13/48 (NCI-H460, Hs 766T, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.904× | -3.0 | 0.088 | 15/48 (SW 1088, Panc 03.27, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.862× | -3.0 | 0.088 | 11/47 (Panc 03.27, MIA PaCa-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5480. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 32.0 | 11 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.58× (z +10.6) | — |
| [[NCI-H460 (line)]] | wt | 51.9 | 3 (2 ⚠) | 8 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.40× (z +11.2) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 1.95× (z +8.8) | [[Digitoxin (drug)]] 5 µM 0.204× (z -21.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.316× (z -15.5) |
| [[PANC-1 (line)]] | alt | 32.0 | 5 (2 ⚠) | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.96× (z +10.4) | [[Digitoxin (drug)]] 5 µM 0.321× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.322× (z -11.1) |
| [[SW480 (line)]] | alt | 38.2 | 2 (1 ⚠) | 6 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.65× (z +10.9) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 1.89× (z +10.4) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.204× (z -18.5) |
| [[NCI-H1792 (line)]] | alt | 65.2 | 5 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.82× (z +10.1) ⚠ toxic; transcription drop · without an alert: [[Clobetasol propionate (drug)]] 5 µM 2.48× (z +9.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.408× (z -9.1) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 64.4 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -20.2) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.159× (z -17.8) |
| [[J82 (line)]] | alt | 33.5 | 4 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.30× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.54× (z +8.5) | [[Digitoxin (drug)]] 5 µM 0.351× (z -9.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 81.5 | 1 (1 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.99× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -16.1) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.411× (z -12.1) |
| [[LOX-IMVI (line)]] | wt | 34.9 | 3 | 2 | [[Ixazomib citrate (drug)]] 5 µM 3.76× (z +12.1) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.368× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 53.1 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -12.7) |
| [[A498 (line)]] | wt | 47.5 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.32× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.591× (z -8.6) ⚠ cell-cycle shift, explains ~56% of this change |
| [[HT-29 (line)]] | alt | 68.8 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.304× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.389× (z -8.8) |
| [[SNU-1 (line)]] | wt | 51.6 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.134× (z -14.3) |
| [[SNU-423 (line)]] | alt | 37.2 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.32× (z +9.8) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.332× (z -9.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.348× (z -8.6) |
| [[HS-578T (line)]] | alt | 55.1 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.349× (z -10.1) |
| [[LS 180 (line)]] | wt | 105 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.367× (z -12.5) |
| [[MIA PaCa-2 (line)]] | alt | 38.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0790× (z -20.9) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.467× (z -8.9) |
| [[RKO (line)]] | wt | 40.9 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.175× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.326× (z -9.4) |
| [[HCT15 (line)]] | alt | 52.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.149× (z -14.0) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.312× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 84.3 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +14.3) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[Hs 766T (line)]] | wt | 52.7 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.212× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.278× (z -10.4) |
| [[NCI-H2030 (line)]] | alt | 62.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.195× (z -19.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.334× (z -12.8) |
| [[NCI-H2347 (line)]] | alt | 40.8 | 2 | 0 | [[Budesonide (drug)]] 5 µM 2.37× (z +8.6) | — |
| [[Panc 03.27 (line)]] | alt | 42.7 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.309× (z -10.0) |
| [[SW1417 (line)]] | alt | 23.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.187× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.282× (z -9.5) |
| [[A-427 (line)]] | wt | 66.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.417× (z -9.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 94.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -19.9) ⚠ cell-cycle shift, explains ~56% of this change |
| [[BT-474 (line)]] | alt | 36.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.308× (z -8.8) |
| [[C32 (line)]] | wt | 40.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.285× (z -9.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 34.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +9.5) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 40.7 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.0988× (z -9.5) ⚠ transcription drop |
| [[H4 (line)]] | wt | 44.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.223× (z -9.2) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 28.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.128× (z -12.7) ⚠ cell-cycle shift, explains ~18% of this change |
| [[KATO III (line)]] | alt | 62.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.503× (z -9.9) ⚠ cell-cycle shift, explains ~56% of this change |
| [[SHP-77 (line)]] | alt | 65.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.265× (z -12.8) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 49.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -9.9) ⚠ cell-cycle shift, explains ~56% of this change |
| [[SW 900 (line)]] | alt | 45.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -8.9) ⚠ cell-cycle shift, explains ~56% of this change |
| [[A-172 (line)]] | wt | 32.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 49.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 78.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 70.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5480), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNPDA2]] | +0.77 | +0.76 / +0.77 | both halves | 7e-06 |  |
| [[BLMH]] | +0.74 | +0.72 / +0.69 | both halves | 7e-06 |  |
| [[NDRG3]] | +0.74 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[NXPE3]] | +0.73 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[PHKB]] | +0.71 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[RAD23B]] | +0.69 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[GSR]] | +0.69 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[DLD]] | +0.67 | +0.61 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_FATTY_ACID_METABOLISM |
| [[SKIC3]] | +0.65 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[PPP5C]] | +0.64 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[ADH5]] | +0.64 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[MPP1]] | +0.63 | +0.61 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R14B-AS1]] | -0.62 | -0.52 / -0.68 | both halves | 1e-05 |  |
| [[TOB2]] | -0.60 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[TNRC6C]] | -0.59 | -0.66 / -0.40 | both halves | 4e-05 |  |
| [[CD63]] | -0.58 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[CATSPERG]] | -0.58 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[EP300]] | -0.56 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[ANKRD17-DT]] | -0.56 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[TPRN]] | -0.56 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[CLCF1]] | -0.56 | -0.40 / -0.65 | both halves | 4e-05 |  |
| [[LINC01004]] | -0.56 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[LINS1]] | -0.55 | -0.38 / -0.46 | both halves | 6e-05 |  |
| [[PDCD7]] | -0.55 | -0.37 / -0.51 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2]] | B | MAP2 activity raises HSD17B4's level | lines that do not express MAP2 (15) vs lines expressing it (35) | 1.09× lower at baseline in the lines without MAP2 | 0.033 | ⚠ within organs, on part of the lines; also absent: LRRC7, ANKRD6, DSEL; maybe low, not absent |
| [[PIR]] | B | PIR activity raises HSD17B4's level | lines that do not express PIR (10) vs lines expressing it (40) | 1.44× lower at baseline in the lines without PIR | 0.042 | ⚠ within organs, on part of the lines; also absent: VEGFD, ELMO1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises HSD17B4's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MAP2K1]] | B | MAP2K1 activity lowers HSD17B4's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.4% of all compounds | 0.067 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.679). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-20.2, -7.4); signed map (-27.9, -21.5). **Vector** length 129, 40.7% of its response variance represented; |z| ≥ 3 in 1,565 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +11.2 | +11.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +10.9 | +11.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +10.5 | +11.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +8.3 | +13.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.2 | +8.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.6 | +4.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +4.2 | +3.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +4.2 | +3.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -12.5 | -11.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -7.2 | -4.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -6.8 | -15.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.4 | -6.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.0 | -18.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.0 | -3.9 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -3.0 | -1.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -4.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.6 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | hydroxysteroid 17-beta dehydrogenase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q23.1 — chr5:119,452,465-119,637,199 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MFE-2, DBP, SDR8C1 |
| Gene groups (HGNC) | Short chain dehydrogenase/reductase superfamily; SCP2 domain containing; Carbon-oxygen lyases |
| Hallmark sets | BILE_ACID_METABOLISM, PEROXISOME, FATTY_ACID_METABOLISM |
| Reactome | 14 pathways, smallest: TYSND1 cleaves peroxisomal proteins; Beta-oxidation of pristanoyl-CoA; Beta-oxidation of very long chain fatty acids |
| Matched by | ensembl_id |

**Function**, from UniProt [P51659](https://www.uniprot.org/uniprotkb/P51659) (Peroxisomal multifunctional enzyme type 2):

> Bifunctional enzyme acting on the peroxisomal fatty acid beta-oxidation pathway. Catalyzes two of the four reactions in fatty acid degradation: hydration of 2-enoyl-CoA (trans-2-enoyl-CoA) to produce (3R)-3-hydroxyacyl-CoA, and dehydrogenation of (3R)-3-hydroxyacyl-CoA to produce 3-ketoacyl-CoA (3-oxoacyl-CoA), which is further metabolized by SCPx. Can use straight-chain and branched-chain fatty acids, as well as bile acid intermediates as substrates. May play a role in peroxisomal …

**Summary**, from NCBI Gene [3295](https://www.ncbi.nlm.nih.gov/gene/3295):

> The protein encoded by this gene is a bifunctional enzyme that is involved in the peroxisomal beta-oxidation pathway for fatty acids. It also acts as a catalyst for the formation of 3-ketoacyl-CoA intermediates from both straight-chain and 2-methyl-branched-chain fatty acids. Defects in this gene that affect the peroxisomal fatty acid beta-oxidation activity are a cause of D-bifunctional protein deficiency (DBPD). An apparent pseudogene of this gene is present on chromosome 8. Multiple …

**Accessions** — [HGNC:5213](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5213) · Entrez [3295](https://www.ncbi.nlm.nih.gov/gene/3295) · UniProt [P51659](https://www.uniprot.org/uniprotkb/P51659) · Ensembl [ENSG00000133835](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133835)

## Data

Gene col 5480: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5480); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5480, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5480]; `tensor/DDL_lfc|DDL_z.npy` [5480]; `embed/gene_vectors.npy` [5480]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5480 or target_col == 5480). Every well: [[HSD17B4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HSD17B4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
