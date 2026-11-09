---
symbol: "SSBP3"
type: "gene"
col: 8053
ensembl_id: "ENSG00000157216"
name: "single stranded DNA binding protein 3"
location: "1p32.3"
module: 59
arm: "+"
pooled_cpm: 86.97
n_lines_expressing: 48
n_dd_up: 15
n_dd_down: 27
n_dd_up_clean: 13
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# SSBP3

*single stranded DNA binding protein 3* — 1p32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.37× (z +27.3, q 0e+00, up in 39 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.456× (z -16.9, q 0e+00, down in 33 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Vinblastine (sulfate) (drug)]] 5 µM: 0.775× (z -8.0, q 1e-13, down in 26 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TSPAN15]] (+0.59, fdr 1e-05), [[IFFO2]] (+0.58, fdr 1e-05), [[CDC42EP4]] (+0.57, fdr 1e-05); moves opposite to [[SLC38A1]] (-0.56, fdr 2e-05), [[SDHC]] (-0.52, fdr 3e-05), [[EMG1]] (-0.52, fdr 3e-05).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[EPHB3]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Clofarabine (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8053.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.37×** | +27.3 | 0e+00 | 39/46 (HEC-1-A, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.12×** | +16.8 | 0e+00 | 39/46 (LOX-IMVI, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.05×** | +16.1 | 0e+00 | 39/46 (LOX-IMVI, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.95×** | +14.9 | 0e+00 | 39/46 (NCI-H1792, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.81×** | +13.3 | 1e-38 | 36/46 (SNU-423, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.67×** | +11.0 | 4e-26 | 33/46 (J82, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +8.1 | 3e-14 | 30/46 (HT-29, CFPAC-1, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.95×** | +7.8 | 5e-13 | 35/47 (CFPAC-1, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.39×** | +7.4 | 7e-12 | 27/46 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.35×** | +6.7 | 1e-09 | 31/46 (J82, SNU-423, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.30×** | +5.8 | 3e-07 | 24/46 (BT-474, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.49×** | +4.6 | 2e-04 | 20/46 (LOX-IMVI, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.22×** | +4.5 | 3e-04 | 22/47 (HT-29, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | **1.21×** | +4.3 | 6e-04 | 20/46 (BT-474, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 1.19× | +3.8 | 0.005 | 16/46 (BT-474, NCI-H460, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.37×** | +3.7 | 0.008 | 17/46 (NCI-H1792, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 1.16× | +3.3 | 0.031 | 13/47 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |
| [[Fumaric acid (drug)]] 5 µM |  | 1.16× | +3.2 | 0.043 | 8/47 (C32, SK-MEL-2, …) | rises with dose | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 55 in all, 16 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8053.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.456×** | -16.9 | 0e+00 | 33/40 (SK-MEL-2, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.487×** | -14.9 | 0e+00 | 32/43 (C32, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.533×** | -14.1 | 1e-42 | 37/46 (C32, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.597×** | -11.5 | 1e-28 | 36/46 (LoVo, AsPC-1, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.775×** | -8.0 | 1e-13 | 26/47 (A-172, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.529×** | -7.4 | 9e-12 | 34/46 (LoVo, Panc 03.27, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.545×** | -7.1 | 1e-10 | 35/46 (LoVo, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.559×** | -6.8 | 8e-10 | 30/46 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.571×** | -6.6 | 4e-09 | 35/46 (LoVo, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.773×** | -5.8 | 5e-07 | 22/45 (A-172, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.786×** | -5.4 | 4e-06 | 25/46 (Hs 766T, NCI-H2347, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.787×** | -5.3 | 4e-06 | 24/46 (CFPAC-1, NCI-H2347, …) | all doses, flat |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.642×** | -5.2 | 1e-05 | 18/35 (BT-474, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.796×** | -5.1 | 1e-05 | 25/46 (A-172, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.809×** | -4.5 | 2e-04 | 21/45 (CHP-212, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.813×** | -4.4 | 3e-04 | 21/45 (A-172, A-427, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.820×** | -4.4 | 3e-04 | 23/46 (Hs 766T, HS-578T, …) | all doses, flat |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.760×** | -4.4 | 4e-04 | 20/46 (A-172, A-427, …) | all doses, stronger at high dose | low cells (technical?); noisy plate (z scaled) |
| [[Sulfatinib (drug)]] 5 µM |  | **0.818×** | -4.3 | 5e-04 | 17/47 (HOP62, NCI-H2347, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **0.698×** | -4.2 | 7e-04 | 18/46 (LoVo, CHP-212, …) | top dose only | noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.05 µM |  | 0.835× | -4.0 | 0.001 | 20/46 (NCI-H2347, Hs 766T, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8053. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 319 | 0 | 15 (11 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0431× (z -23.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.156× (z -14.8) |
| [[LoVo (line)]] | wt | 195 | 0 | 11 (7 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.466× (z -10.6) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.490× (z -9.9) |
| [[J82 (line)]] | alt | 37.9 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.45× (z +22.6) | [[Dinaciclib (drug)]] 0.5 µM 0.369× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 56.2 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +17.1) | — |
| [[BT-474 (line)]] | alt | 106 | 5 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +17.6) | [[Lonafarnib (drug)]] 5 µM 0.128× (z -10.8) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 80.9 | 4 | 2 (1 ⚠) | [[Cobimetinib (drug)]] 0.5 µM 2.84× (z +9.9) | [[Dinaciclib (drug)]] 0.05 µM 0.328× (z -9.7) ⚠ toxic; transcription drop · without an alert: [[Betamethasone dipropionate (drug)]] 0.5 µM 0.381× (z -9.1) |
| [[HT-29 (line)]] | alt | 93.2 | 5 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +14.5) | [[Auranofin (drug)]] 5 µM 0.452× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 103 | 5 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.73× (z +13.1) | [[Dinaciclib (drug)]] 0.05 µM 0.451× (z -9.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 42.7 | 6 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.96× (z +17.1) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.56× (z +13.1) | — |
| [[NCI-H2347 (line)]] | alt | 108 | 1 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.339× (z -11.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 193 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +19.9) | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -16.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 90.4 | 3 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +15.0) | [[Dinaciclib (drug)]] 5 µM 0.425× (z -11.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 110 | 0 | 5 (2 ⚠) | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.336× (z -11.5) |
| [[CFPAC-1 (line)]] | alt | 94.9 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +16.8) | [[Dinaciclib (drug)]] 5 µM 0.262× (z -14.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 102 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.116× (z -18.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 39.7 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +14.4) | — |
| [[AsPC-1 (line)]] | alt | 71.6 | 1 (1 ⚠) | 3 (2 ⚠) | [[Trametinib (drug)]] 5 µM 2.47× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.345× (z -10.4) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.400× (z -9.0) |
| [[CHP-212 (line)]] | wt | 281 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.100× (z -16.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 55.4 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.96× (z +22.7) | — |
| [[NCI-H1573 (line)]] | alt | 27.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +11.6) | — |
| [[NCI-H460 (line)]] | wt | 40.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +15.8) | — |
| [[Panc 03.27 (line)]] | alt | 106 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +14.8) | [[Dinaciclib (drug)]] 5 µM 0.152× (z -16.3) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 121 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +13.7) | [[Dinaciclib (drug)]] 0.05 µM 0.289× (z -9.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 64.7 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +16.4) | [[Dinaciclib (drug)]] 5 µM 0.414× (z -8.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 187 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.377× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 58.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +15.7) | — |
| [[RPMI-7951 (line)]] | alt | 123 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.323× (z -11.1) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 88.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +10.7) | — |
| [[HCT15 (line)]] | alt | 49.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +9.5) | — |
| [[KATO III (line)]] | alt | 113 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.339× (z -11.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 104 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +18.3) | — |
| [[NCI-H2030 (line)]] | alt | 43.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +9.2) | — |
| [[NCI-H23 (line)]] | alt | 36.6 | 2 | 0 | [[Belinostat (drug)]] 5 µM 3.97× (z +11.3) | — |
| [[SW48 (line)]] | wt | 53.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +10.7) | — |
| [[A498 (line)]] | wt | 92.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +9.4) | — |
| [[AN3 CA (line)]] | alt | 216 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.226× (z -10.3) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 88.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +10.5) | — |
| [[HOP62 (line)]] | alt | 95.6 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.638× (z -13.9) ⚠ position not correctable |
| [[RKO (line)]] | wt | 111 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +10.0) | — |
| [[SHP-77 (line)]] | alt | 132 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.354× (z -9.3) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 69.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +11.4) | — |
| [[A549 (line)]] | wt | 18.7 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 84.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 87.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 17.8 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 68.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8053), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSPAN15]] | +0.59 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[IFFO2]] | +0.58 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[CDC42EP4]] | +0.57 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[ATP8B1]] | +0.57 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[ZMIZ1]] | +0.56 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[CRACR2B]] | +0.55 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[NOS1AP]] | +0.54 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[HES4]] | +0.54 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[DBP]] | +0.53 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[ELF3]] | +0.53 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[MAN1C1]] | +0.53 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[MYLIP]] | +0.52 | +0.49 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC38A1]] | -0.56 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[SDHC]] | -0.52 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[EMG1]] | -0.52 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[RBM19]] | -0.52 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[DDX21]] | -0.52 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[DHX34]] | -0.52 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[CARS2]] | -0.52 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[UQCC1]] | -0.51 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[TRMT6]] | -0.51 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[MAPKAPK5]] | -0.50 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[TSR1]] | -0.50 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[ZNF202]] | -0.50 | -0.44 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 1, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPHB3]] | B | EPHB3 activity raises SSBP3's level | lines that do not express EPHB3 (15) vs lines expressing it (35) | 1.75× lower at baseline in the lines without EPHB3 | 0.085 | ⚠ within organs, on part of the lines; also absent: SLC7A8, MCF2L, ENPP5; maybe low, not absent |
| [[HES4]] | C | HES4 activity strengthens SSBP3's drug response | lines that do not express HES4 (4) vs lines expressing it (43) | the lines without HES4 respond 0.51× as strongly (z diff +1.80); strongest at Belinostat 5 µM: 0.90x vs 2.09x (z diff +5.8) | 0.010 | ⚠ few lines (4 vs 46); across organs; also absent: SLC26A4, ADAMTSL5; target measured in part of the lines; artifact flags |
| [[HES4]] | C | HES4 activity lowers SSBP3's level | lines that do not express HES4 (4) vs lines expressing it (46) | 2.23× higher at baseline in the lines without HES4 | 0.054 | ⚠ few lines (4 vs 46); across organs; also absent: SLC26A4, ADAMTSL5 |
| [[BMF]] | C | BMF activity raises SSBP3's level | lines that do not express BMF (4) vs lines expressing it (46) | 1.86× lower at baseline in the lines without BMF | 0.096 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000285868; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Clofarabine (drug)]] 0.5 µM | C | SSBP3's natural level raises the cells' numbers under Clofarabine 0.5 µM (protects the cells) | SSBP3's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.60 | 0.491 over the table, 0.083 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.444). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-4.9, 32.6); signed map (-4.4, 27.2). **Vector** length 130, 41.7% of its response variance represented; |z| ≥ 3 in 1,824 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +8.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.2 | +13.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.3 | +6.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +5.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.9 | +11.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.4 | +7.8 |
|  | [[Arbutin (drug)]] 5 µM |  | +2.6 | +0.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.5 | +3.0 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.5 | -0.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -10.1 | -11.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -6.4 | -8.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -6.1 | -7.4 |
|  | [[EX229 (drug)]] 5 µM |  | -6.1 | -6.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -6.0 | -6.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.8 | -7.1 |

## What is on record

|  |  |
|---|---|
| Name | single stranded DNA binding protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p32.3 — chr1:54,225,432-54,413,479 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CSDP, SSDP, FLJ10355, SSDP1 |
| Gene groups (HGNC) | Wnt enhanceosome complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BWW4](https://www.uniprot.org/uniprotkb/Q9BWW4) (Single-stranded DNA-binding protein 3):

> May be involved in transcription regulation of the alpha 2(I) collagen gene where it binds to the single-stranded polypyrimidine sequences in the promoter region.

**Summary**, from NCBI Gene [23648](https://www.ncbi.nlm.nih.gov/gene/23648):

> Predicted to enable transcription coactivator activity. Predicted to be involved in positive regulation of transcription by RNA polymerase II. Predicted to act upstream of or within hematopoietic progenitor cell differentiation. Predicted to be part of transcription regulator complex. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:15674](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15674) · Entrez [23648](https://www.ncbi.nlm.nih.gov/gene/23648) · UniProt [Q9BWW4](https://www.uniprot.org/uniprotkb/Q9BWW4) · Ensembl [ENSG00000157216](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157216)

## Data

Gene col 8053: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8053); `tables/drug_effects.parquet` (76 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8053, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8053]; `tensor/DDL_lfc|DDL_z.npy` [8053]; `embed/gene_vectors.npy` [8053]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8053 or target_col == 8053). Every well: [[SSBP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SSBP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
