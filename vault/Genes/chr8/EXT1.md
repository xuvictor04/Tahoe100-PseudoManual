---
symbol: "EXT1"
type: "gene"
col: 11258
ensembl_id: "ENSG00000182197"
name: "exostosin glycosyltransferase 1"
location: "8q24.11"
module: 224
arm: "+"
pooled_cpm: 824.29
n_lines_expressing: 47
n_dd_up: 14
n_dd_down: 23
n_dd_up_clean: 12
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 18
direction_downstream: 2
tags: ["gene", "module/224"]
generated_by: "tahoemap"
---

# EXT1

*exostosin glycosyltransferase 1* — 8q24.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.56× (z +17.5, q 0e+00, up in 42 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.466× (z -13.7, q 8e-40, down in 39 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.630× (z -12.2, q 7e-32, down in 28 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FHL2]] (+0.64, fdr 1e-05), [[CMIP]] (+0.63, fdr 1e-05), [[INHBA]] (+0.62, fdr 1e-05); moves opposite to [[CHPT1]] (-0.54, fdr 1e-05), [[PTPDC1]] (-0.52, fdr 5e-05), [[MED24]] (-0.48, fdr 8e-05).
> It is in [[Module 224]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 18 arrows point to it, the strongest [[PTGS2]] → it (grade B ⚠); 2 go from it, the strongest it → [[KLF7]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠; shown: the 15 strongest. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11258.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.56×** | +17.5 | 0e+00 | 42/45 (AsPC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.29×** | +15.4 | 0e+00 | 41/45 (AsPC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.12×** | +14.0 | 4e-42 | 41/45 (SK-MEL-2, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.63×** | +12.8 | 3e-35 | 30/45 (Panc 03.27, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +9.3 | 2e-18 | 34/45 (SK-MEL-2, RKO, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.58×** | +9.2 | 2e-18 | 40/46 (LoVo, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.57×** | +8.4 | 4e-15 | 35/45 (SK-MEL-2, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.39×** | +6.2 | 5e-08 | 29/45 (NCI-H1573, SK-MEL-2, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.38×** | +5.8 | 5e-07 | 24/44 (NCI-H1573, C32, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.68×** | +5.1 | 2e-05 | 30/45 (C32, HS-578T, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.61×** | +4.7 | 2e-04 | 32/46 (A-172, SW1417, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.27×** | +4.5 | 3e-04 | 25/44 (NCI-H1573, C32, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.27×** | +4.0 | 0.002 | 21/44 (SK-MEL-2, C32, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +3.9 | 0.004 | 16/46 (NCI-H1573, C32, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.20×** | +3.4 | 0.022 | 22/46 (RKO, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11258.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.466×** | -13.7 | 8e-40 | 39/41 (A498, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.478×** | -12.6 | 1e-33 | 40/46 (A498, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.630×** | -12.2 | 7e-32 | 28/46 (J82, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.499×** | -12.0 | 6e-31 | 42/42 (C32, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.574×** | -10.0 | 3e-21 | 35/44 (NCI-H2030, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.631×** | -8.6 | 9e-16 | 42/45 (HT-29, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.737×** | -5.7 | 1e-06 | 29/45 (H4, SW 900, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **0.577×** | -5.4 | 6e-06 | 36/44 (RKO, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.759×** | -4.9 | 4e-05 | 28/46 (H4, HOP62, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.767×** | -4.9 | 4e-05 | 27/45 (HepG2/C3A, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.832×** | -4.9 | 6e-05 | 24/45 (H4, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.785×** | -4.5 | 3e-04 | 26/45 (H4, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.786×** | -4.5 | 3e-04 | 23/45 (H4, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.789×** | -4.2 | 9e-04 | 32/44 (HepG2/C3A, RKO, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.786×** | -4.1 | 0.002 | 27/45 (H4, HOP62, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.816×** | -3.8 | 0.005 | 25/45 (H4, HOP62, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **0.686×** | -3.7 | 0.008 | 31/45 (J82, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.803×** | -3.6 | 0.011 | 23/45 (AsPC-1, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.832×** | -3.4 | 0.016 | 23/45 (H4, HOP62, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | 0.839× | -3.3 | 0.027 | 22/45 (H4, HOP62, …) | all doses, stronger at high dose |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.884× | -3.2 | 0.029 | 4/46 (SHP-77, HS-578T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11258. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 1,101 | 2 | 22 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.75× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.237× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Dexamethasone (drug)]] 5 µM 0.277× (z -14.2) |
| [[HOP62 (line)]] | alt | 1,633 | 3 | 20 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 2.99× (z +12.3) | [[Dinaciclib (drug)]] 0.05 µM 0.285× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -12.0) |
| [[Hs 766T (line)]] | wt | 668 | 1 | 14 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.19× (z +9.8) | [[Dexamethasone (drug)]] 5 µM 0.410× (z -11.2) |
| [[NCI-H23 (line)]] | alt | 581 | 5 | 9 (6 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.59× (z +11.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.289× (z -22.0) |
| [[C32 (line)]] | wt | 584 | 10 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +23.2) | [[Dinaciclib (drug)]] 0.05 µM 0.301× (z -15.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 810 | 0 | 12 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -17.3) |
| [[HepG2_C3A (line)]] | wt | 925 | 2 | 9 (6 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.86× (z +11.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.291× (z -15.0) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.508× (z -12.1) |
| [[NCI-H1573 (line)]] | alt | 555 | 8 (2 ⚠) | 3 (2 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 2.13× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.419× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.609× (z -9.3) |
| [[HT-29 (line)]] | alt | 1,766 | 5 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +18.8) | [[Dinaciclib (drug)]] 5 µM 0.241× (z -17.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 1,125 | 7 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.60× (z +13.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.293× (z -12.8) ⚠ toxic |
| [[HS-578T (line)]] | alt | 2,108 | 3 | 6 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.79× (z +15.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.328× (z -18.0) |
| [[LoVo (line)]] | wt | 775 | 8 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +18.8) | [[Auranofin (drug)]] 5 µM 0.445× (z -10.6) |
| [[LOX-IMVI (line)]] | wt | 1,944 | 1 | 8 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 2.23× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.241× (z -21.7) |
| [[SK-MEL-2 (line)]] | alt | 427 | 8 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 7.65× (z +23.8) | [[Dinaciclib (drug)]] 5 µM 0.407× (z -10.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 390 | 7 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +22.9) | [[Dinaciclib (drug)]] 0.05 µM 0.383× (z -13.6) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 808 | 6 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 6.36× (z +26.3) | [[Dinaciclib (drug)]] 0.05 µM 0.481× (z -9.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 544 | 4 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 3.39× (z +13.7) | [[Dinaciclib (drug)]] 5 µM 0.255× (z -14.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 421 | 7 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +23.3) | [[Dinaciclib (drug)]] 5 µM 0.322× (z -14.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 534 | 4 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 7.65× (z +13.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.533× (z -11.0) |
| [[RPMI-7951 (line)]] | alt | 952 | 4 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.67× (z +12.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.541× (z -10.9) |
| [[CFPAC-1 (line)]] | alt | 546 | 5 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.55× (z +11.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.385× (z -11.0) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 605 | 3 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.47× (z +16.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -17.4) |
| [[SW 900 (line)]] | alt | 1,546 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.242× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.347× (z -10.8) |
| [[A498 (line)]] | wt | 1,617 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -22.2) |
| [[BT-474 (line)]] | alt | 588 | 6 | 0 | [[Tucidinostat (drug)]] 5 µM 2.43× (z +13.1) | — |
| [[J82 (line)]] | alt | 2,339 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.226× (z -23.2) |
| [[NCI-H460 (line)]] | wt | 522 | 5 | 1 | [[Panobinostat (drug)]] 5 µM 2.87× (z +13.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -14.6) |
| [[SNU-1 (line)]] | wt | 543 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +16.6) | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -11.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 423 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.87× (z +15.4) | — |
| [[CHP-212 (line)]] | wt | 1,354 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.178× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -13.2) |
| [[HEC-1-A (line)]] | alt | 340 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +19.9) | — |
| [[SHP-77 (line)]] | alt | 553 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.355× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~2% of this change |
| [[C-33 A (line)]] | alt | 386 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.24× (z +14.4) | — |
| [[COLO 205 (line)]] | alt | 1,328 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.230× (z -14.8) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -10.1) |
| [[HCT15 (line)]] | alt | 324 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.53× (z +16.5) | — |
| [[SW48 (line)]] | wt | 432 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.29× (z +13.8) | — |
| [[hTERT-HPNE (line)]] | wt | 1,104 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -11.9) |
| [[LS 180 (line)]] | wt | 770 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +13.8) | [[Dinaciclib (drug)]] 5 µM 0.380× (z -11.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 875 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -19.1) |
| [[SNU-423 (line)]] | alt | 1,036 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -12.3) |
| [[A549 (line)]] | wt | 983 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.218× (z -18.4) |
| [[AN3 CA (line)]] | alt | 361 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +16.2) | — |
| [[NCI-H596 (line)]] | alt | 804 | 1 | 0 | [[Methylthiouracil (drug)]] 0.05 µM 2.83× (z +12.2) | — |
| [[SW 1088 (line)]] | alt | 1,012 | 0 | 1 | — | [[Dexamethasone (drug)]] 5 µM 0.230× (z -9.4) |
| [[A-427 (line)]] | wt | 190 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 177 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 805 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 279 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 295 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 192 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11258), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FHL2]] | +0.64 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[CMIP]] | +0.63 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[INHBA]] | +0.62 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[TM4SF1]] | +0.62 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[STK17A]] | +0.62 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[SYTL2]] | +0.61 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[ADAMTS16]] | +0.59 | +0.56 / +0.55 | both halves | 1e-05 | pathway: Diseases of glycosylation |
| [[CD44]] | +0.58 | +0.50 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_GLYCOLYSIS |
| [[CCN1]] | +0.58 | +0.59 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA |
| [[LIMA1]] | +0.58 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[CREB5]] | +0.57 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[MYO10]] | +0.57 | +0.52 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHPT1]] | -0.54 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[PTPDC1]] | -0.52 | -0.59 / -0.40 | both halves | 5e-05 |  |
| [[MED24]] | -0.48 | -0.40 / -0.37 | both halves | 8e-05 | pathway: HALLMARK_GLYCOLYSIS |
| [[ABCB10]] | -0.48 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[RAVER2]] | -0.47 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[DRAM2]] | -0.47 | -0.40 / -0.42 | both halves | 4e-05 |  |
| [[SLC43A1]] | -0.47 | -0.39 / -0.41 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 16, C 2. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTGS2]] | B | PTGS2 activity raises EXT1's level | lines that do not express PTGS2 (27) vs lines expressing it (23) | 2.08× lower at baseline in the lines without PTGS2 | 0.001 | ⚠ within organs, on part of the lines; also absent: ADAMTS9-AS2, CFH, ITGA4 |
| [[FAM107B]] | B | FAM107B activity raises EXT1's level | lines that do not express FAM107B (11) vs lines expressing it (39) | 2.22× lower at baseline in the lines without FAM107B | 0.003 | ⚠ within organs, on part of the lines; also absent: KIAA1217, ETS2, NRP1 |
| [[GLIS3]] | B | GLIS3 activity raises EXT1's level | lines that do not express GLIS3 (21) vs lines expressing it (29) | 1.76× lower at baseline in the lines without GLIS3 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, SYNPO |
| [[TRIB1]] | B | TRIB1 activity raises EXT1's level | lines that do not express TRIB1 (6) vs lines expressing it (44) | 2.54× lower at baseline in the lines without TRIB1 | 0.016 | ⚠ within organs, on part of the lines; also absent: TGFBR2, VDR, PLSCR2; maybe low, not absent |
| [[PLOD2]] | B | PLOD2 activity raises EXT1's level | lines that do not express PLOD2 (15) vs lines expressing it (35) | 1.97× lower at baseline in the lines without PLOD2 | 0.025 | ⚠ within organs, on part of the lines; also absent: ITGA1, TMEM92-AS1, RGS17 |
| [[CD44]] | B | CD44 activity raises EXT1's level | lines that do not express CD44 (15) vs lines expressing it (35) | 1.67× lower at baseline in the lines without CD44 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: GBP3, CLEC2B, ADAMTS16 |
| [[IL6]] | B | IL6 activity raises EXT1's level | lines that do not express IL6 (32) vs lines expressing it (18) | 1.80× lower at baseline in the lines without IL6 | 0.038 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, G0S2 |
| [[IL1RAP]] | B | IL1RAP activity raises EXT1's level | lines that do not express IL1RAP (8) vs lines expressing it (42) | 2.29× lower at baseline in the lines without IL1RAP | 0.039 | ⚠ within organs, on part of the lines; also absent: LACC1, GSDMD, TGFBR2 |
| [[ADAMTS16]] | B | ADAMTS16 activity raises EXT1's level | lines that do not express ADAMTS16 (25) vs lines expressing it (25) | 1.54× lower at baseline in the lines without ADAMTS16 | 0.039 | ⚠ within organs, on part of the lines; also absent: PLAU, ADAMTS12, GBP5 |
| [[NR3C1]] | B | NR3C1 activity lowers EXT1's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 4.8% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[C12orf75-AS1]] | B | C12orf75-AS1 activity raises EXT1's level | lines that do not express C12orf75-AS1 (22) vs lines expressing it (28) | 1.61× lower at baseline in the lines without C12orf75-AS1 | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, FOXC2, GLIPR1 |
| [[CD274]] | B | CD274 activity raises EXT1's level | lines that do not express CD274 (18) vs lines expressing it (32) | 1.61× lower at baseline in the lines without CD274 | 0.075 | ⚠ within organs, on part of the lines; also absent: GBP5, IL1B, PDCD1LG2 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLF7]] | C | EXT1 activity raises KLF7's level | lines that do not express EXT1 (3) vs lines expressing it (47) | 4.56× lower at baseline in the lines without EXT1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GNA14, B4GALT1, RIGI; maybe low, not absent; its own permutation p |
| cells under [[Vinblastine (sulfate) (drug)]] 5 µM | C | EXT1's natural level lowers the cells' numbers under Vinblastine (sulfate) 5 µM (makes them more sensitive) | EXT1's natural level across 45 lines (lineage-adjusted; a glimpse) | r -0.72 | 0.268 over the table, 0.036 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 224]] — hypoxia; 9 genes; every member is in the + arm (projection on the module's main direction 0.752). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (48.6, 4.1); signed map (3.5, 45.8). **Vector** length 143, 53.2% of its response variance represented; |z| ≥ 3 in 2,048 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.0 | +9.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.8 | +15.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.8 | +17.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +6.6 | +14.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +6.4 | +5.8 |
|  | [[vincristine (drug)]] 0.5 µM |  | +4.9 | +1.1 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +4.8 | +4.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.6 | +3.9 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -7.7 | -4.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -6.8 | -4.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -6.7 | -3.4 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -6.3 | -4.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -6.2 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | exostosin glycosyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.11 — chr8:117,794,490-118,111,826 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ttv; previously LGCR, LGS |
| Gene groups (HGNC) | Exostosin glycosyltransferase family |
| Hallmark sets | GLYCOLYSIS, HYPOXIA |
| Reactome | 9 pathways, smallest: Defective EXT1 causes exostoses 1, TRPS2 and CHDS; Defective EXT2 causes exostoses 2; HS-GAG biosynthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16394](https://www.uniprot.org/uniprotkb/Q16394) (Exostosin-1):

> Glycosyltransferase forming with EXT2 the heterodimeric heparan sulfate polymerase which catalyzes the elongation of the heparan sulfate glycan backbone. Glycan backbone extension consists in the alternating transfer of (1->4)-beta-D-GlcA and (1->4)-alpha-D-GlcNAc residues from their respective UDP-sugar donors. Both EXT1 and EXT2 are required for the full activity of the polymerase since EXT1 bears the N-acetylglucosaminyl-proteoglycan 4-beta-glucuronosyltransferase activity within the complex …

**Summary**, from NCBI Gene [2131](https://www.ncbi.nlm.nih.gov/gene/2131):

> This gene encodes an endoplasmic reticulum-resident type II transmembrane glycosyltransferase involved in the chain elongation step of heparan sulfate biosynthesis. Mutations in this gene cause the type I form of multiple exostoses. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:3512](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3512) · Entrez [2131](https://www.ncbi.nlm.nih.gov/gene/2131) · UniProt [Q16394](https://www.uniprot.org/uniprotkb/Q16394) · Ensembl [ENSG00000182197](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182197)

## Data

Gene col 11258: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11258); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11258, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11258]; `tensor/DDL_lfc|DDL_z.npy` [11258]; `embed/gene_vectors.npy` [11258]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11258 or target_col == 11258). Every well: [[EXT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EXT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
