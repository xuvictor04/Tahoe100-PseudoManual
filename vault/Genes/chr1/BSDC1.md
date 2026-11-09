---
symbol: "BSDC1"
type: "gene"
col: 8294
ensembl_id: "ENSG00000160058"
name: "BSD domain containing 1"
location: "1p35.1"
module: 187
arm: "+"
pooled_cpm: 88.49
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 15
n_dd_up_clean: 9
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/187"]
generated_by: "tahoemap"
---

# BSDC1

*BSD domain containing 1* — 1p35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 2.16× (z +14.2, q 9e-43, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.421× (z -16.0, q 0e+00, down in 47 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Abemaciclib (drug)]] 5 µM: 0.412× (z -8.5, q 2e-15, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EAPP]] (+0.76, fdr 7e-06), [[ULK1]] (+0.75, fdr 7e-06), [[RNF181]] (+0.73, fdr 7e-06); moves opposite to [[ATIC]] (-0.71, fdr 7e-06), [[VARS1]] (-0.69, fdr 7e-06), [[EIF4G1]] (-0.66, fdr 7e-06).
> It is in [[Module 187]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8294.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.16×** | +14.2 | 9e-43 | 47/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.00×** | +12.8 | 8e-35 | 47/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.08×** | +12.7 | 8e-35 | 47/48 (PANC-1, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.49×** | +7.3 | 3e-11 | 33/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +5.9 | 3e-07 | 26/49 (SW48, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.72×** | +5.5 | 5e-06 | 40/49 (LOX-IMVI, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.29×** | +4.7 | 2e-04 | 25/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.20× | +4.7 | 2e-04 | 23/49 (KATO III, SHP-77, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.26×** | +4.2 | 0.002 | 25/48 (HT-29, COLO 205, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.48×** | +3.9 | 0.005 | 28/48 (RPMI-7951, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.25×** | +3.9 | 0.005 | 26/47 (NCI-H2030, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.22×** | +3.7 | 0.011 | 24/48 (SNU-423, KATO III, …) | top dose only | position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.42×** | +3.4 | 0.029 | 20/45 (SNU-1, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.19× | +3.2 | 0.048 | 18/48 (HepG2/C3A, HEC-1-A, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 1.19× | +3.2 | 0.048 | 21/48 (A-427, C32, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.18× | +3.0 | 0.091 | 15/47 (COLO 205, HT-29, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8294.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.421×** | -16.0 | 0e+00 | 47/48 (MIA PaCa-2, NCI-H460, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.530×** | -11.3 | 6e-27 | 34/44 (SNU-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.573×** | -10.3 | 2e-22 | 42/49 (COLO 205, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **0.412×** | -8.5 | 2e-15 | 45/48 (MIA PaCa-2, A-427, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.644×** | -7.5 | 7e-12 | 38/45 (HS-578T, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.468×** | -7.3 | 2e-11 | 44/48 (NCI-H460, A-427, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.492×** | -6.8 | 6e-10 | 41/48 (NCI-H460, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.508×** | -6.5 | 5e-09 | 38/48 (MIA PaCa-2, Panc 03.27, …) | all doses, flat | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.531×** | -6.1 | 7e-08 | 38/48 (NCI-H1792, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.757×** | -4.9 | 5e-05 | 30/48 (SNU-423, LS 180, …) | top dose only |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.760×** | -4.8 | 9e-05 | 32/48 (NCI-H460, LoVo, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.680×** | -3.9 | 0.005 | 28/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.862× | -3.8 | 0.005 | 15/48 (NCI-H460, NCI-H2347, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.822×** | -3.6 | 0.012 | 22/48 (MIA PaCa-2, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.833× | -3.4 | 0.029 | 18/48 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 0.835× | -3.3 | 0.032 | 19/48 (SW 1088, NCI-H1573, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.5 µM |  | **0.739×** | -3.0 | 0.077 | 13/48 (MIA PaCa-2, KATO III, …) | all doses, flat | noisy plate (z scaled) |
| [[Volasertib (drug)]] 0.5 µM |  | **0.747×** | -2.9 | 0.094 | 11/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 5 µM |  | 0.854× | -2.9 | 0.094 | 17/48 (SW 900, NCI-H460, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8294. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 80.6 | 3 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.49× (z +10.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.409× (z -10.0) ⚠ unreliable plate only |
| [[COLO 205 (line)]] | alt | 130 | 3 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.68× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.307× (z -12.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 115 | 1 | 4 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.21× (z +8.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.198× (z -18.1) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.143× (z -11.4) |
| [[NCI-H460 (line)]] | wt | 77.0 | 3 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.22× (z +10.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.261× (z -17.0) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.270× (z -8.7) |
| [[PANC-1 (line)]] | alt | 85.8 | 4 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.62× (z +11.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.479× (z -9.0) ⚠ unreliable plate only |
| [[SNU-423 (line)]] | alt | 110 | 0 | 5 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.376× (z -12.3) ⚠ unreliable plate only |
| [[SW480 (line)]] | alt | 88.7 | 3 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.48× (z +10.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.420× (z -10.1) ⚠ unreliable plate only |
| [[HEC-1-A (line)]] | alt | 71.1 | 3 | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.55× (z +10.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.384× (z -11.6) ⚠ unreliable plate only |
| [[HS-578T (line)]] | alt | 130 | 0 | 4 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.379× (z -12.8) ⚠ unreliable plate only |
| [[HT-29 (line)]] | alt | 96.5 | 2 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.44× (z +9.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.383× (z -9.7) ⚠ unreliable plate only |
| [[KATO III (line)]] | alt | 96.1 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.74× (z +9.4) | — |
| [[LoVo (line)]] | wt | 78.7 | 3 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.71× (z +10.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.429× (z -9.1) ⚠ unreliable plate only |
| [[LS 180 (line)]] | wt | 109 | 3 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.54× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.453× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 90.7 | 2 | 2 (2 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.57× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.284× (z -12.9) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 58.6 | 0 | 3 (2 ⚠) | — | [[Lidocaine (hydrochloride) (drug)]] 5 µM 0.248× (z -10.4) |
| [[HOP62 (line)]] | alt | 99.4 | 2 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.37× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.411× (z -9.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 104 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.212× (z -14.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 73.0 | 2 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.65× (z +10.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.313× (z -12.2) ⚠ unreliable plate only |
| [[NCI-H2347 (line)]] | alt | 76.5 | 0 | 3 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.382× (z -12.2) ⚠ unreliable plate only |
| [[SNU-1 (line)]] | wt | 108 | 2 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.28× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.134× (z -15.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 64.1 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.98× (z +10.1) | [[Dinaciclib (drug)]] 0.05 µM 0.268× (z -11.3) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 98.0 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.282× (z -14.6) ⚠ unreliable plate only |
| [[H4 (line)]] | wt | 130 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.294× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 110 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.356× (z -11.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 86.8 | 2 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.52× (z +9.2) | — |
| [[A498 (line)]] | wt | 72.6 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.454× (z -8.6) ⚠ unreliable plate only |
| [[A549 (line)]] | wt | 70.5 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.320× (z -11.7) ⚠ unreliable plate only |
| [[AN3 CA (line)]] | alt | 93.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -10.9) ⚠ cell-cycle shift, explains ~58% of this change |
| [[AsPC-1 (line)]] | alt | 80.0 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.382× (z -10.1) ⚠ unreliable plate only |
| [[C-33 A (line)]] | alt | 87.9 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.353× (z -9.4) ⚠ unreliable plate only |
| [[HCT15 (line)]] | alt | 124 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.367× (z -9.3) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 89.9 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.65× (z +8.7) | — |
| [[NCI-H1573 (line)]] | alt | 93.2 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.78× (z +9.2) | — |
| [[NCI-H2030 (line)]] | alt | 86.6 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.27× (z +8.5) | — |
| [[NCI-H596 (line)]] | alt | 95.7 | 0 | 1 | — | [[Methylthiouracil (drug)]] 5 µM 0.110× (z -11.8) |
| [[NCI-H661 (line)]] | alt | 81.3 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.165× (z -8.8) |
| [[RKO (line)]] | wt | 83.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.332× (z -10.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 81.6 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.47× (z +9.2) | — |
| [[SW 900 (line)]] | alt | 81.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.406× (z -8.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 69.7 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.346× (z -10.6) ⚠ unreliable plate only |
| [[SW48 (line)]] | wt | 105 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +9.5) | — |
| [[A-172 (line)]] | wt | 74.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 86.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 98.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 80.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 91.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 61.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 98.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 80.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8294), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EAPP]] | +0.76 | +0.59 / +0.81 | both halves | 7e-06 |  |
| [[ULK1]] | +0.75 | +0.65 / +0.83 | both halves | 7e-06 |  |
| [[RNF181]] | +0.73 | +0.63 / +0.75 | both halves | 7e-06 |  |
| [[RB1CC1]] | +0.71 | +0.62 / +0.74 | both halves | 7e-06 |  |
| [[SYF2]] | +0.69 | +0.40 / +0.80 | both halves | 5e-05 |  |
| [[ATXN3]] | +0.69 | +0.56 / +0.75 | both halves | 1e-05 |  |
| [[FBXL20]] | +0.69 | +0.58 / +0.72 | both halves | 8e-06 |  |
| [[MED31]] | +0.68 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[SELENOK]] | +0.67 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[WDR83OS]] ⚠ | +0.67 | +0.51 / +0.68 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MXD4]] | +0.66 | +0.54 / +0.72 | both halves | 1e-05 |  |
| [[EGFL8]] | +0.66 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[ATG14]] | +0.66 | +0.65 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATIC]] | -0.71 | -0.64 / -0.73 | both halves | 7e-06 |  |
| [[VARS1]] | -0.69 | -0.63 / -0.70 | both halves | 7e-06 |  |
| [[EIF4G1]] | -0.66 | -0.64 / -0.68 | both halves | 7e-06 |  |
| [[VMA21]] | -0.66 | -0.57 / -0.71 | both halves | 1e-05 |  |
| [[MTHFD1]] | -0.65 | -0.52 / -0.71 | both halves | 1e-05 |  |
| [[FARSB]] | -0.65 | -0.54 / -0.70 | both halves | 1e-05 |  |
| [[PRKDC]] | -0.63 | -0.54 / -0.69 | both halves | 1e-05 |  |
| [[C1QBP]] | -0.63 | -0.62 / -0.60 | both halves | 7e-06 |  |
| [[AKAP11]] | -0.63 | -0.62 / -0.61 | both halves | 7e-06 |  |
| [[SYNCRIP]] | -0.63 | -0.60 / -0.58 | both halves | 7e-06 |  |
| [[TFDP1]] | -0.62 | -0.51 / -0.66 | both halves | 1e-05 |  |
| [[BTBD1]] | -0.62 | -0.54 / -0.63 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 187]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.829). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (2.4, -43.0); signed map (-23.2, 9.0). **Vector** length 151, 51.3% of its response variance represented; |z| ≥ 3 in 1,127 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +11.7 | +14.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +11.4 | +12.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +10.8 | +12.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.3 | +5.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +6.0 | +5.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +5.6 | +3.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +5.3 | +2.7 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +4.4 | +2.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -14.3 | -16.0 |
|  | [[EX229 (drug)]] 5 µM |  | -8.2 | -6.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -7.9 | -8.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -7.5 | -7.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -7.5 | -6.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -6.1 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | BSD domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.1 — chr1:32,364,633-32,394,731 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10276, RP4-811H24.7 |
| Matched by | ensembl_id |

UniProt [Q9NW68](https://www.uniprot.org/uniprotkb/Q9NW68) carries no function annotation.

**Summary**, from NCBI Gene [55108](https://www.ncbi.nlm.nih.gov/gene/55108):

> Located in Golgi apparatus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25501](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25501) · Entrez [55108](https://www.ncbi.nlm.nih.gov/gene/55108) · UniProt [Q9NW68](https://www.uniprot.org/uniprotkb/Q9NW68) · Ensembl [ENSG00000160058](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160058)

## Data

Gene col 8294: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8294); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8294, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8294]; `tensor/DDL_lfc|DDL_z.npy` [8294]; `embed/gene_vectors.npy` [8294]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8294 or target_col == 8294). Every well: [[BSDC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BSDC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
