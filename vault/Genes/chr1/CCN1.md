---
symbol: "CCN1"
type: "gene"
col: 6661
ensembl_id: "ENSG00000142871"
name: "cellular communication network factor 1"
location: "1p22.3"
module: 120
arm: "+"
pooled_cpm: 135.78
n_lines_expressing: 43
n_dd_up: 27
n_dd_down: 32
n_dd_up_clean: 14
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 7
direction_downstream: 9
tags: ["gene", "module/120"]
generated_by: "tahoemap"
---

# CCN1

*cellular communication network factor 1* — 1p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (13 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 8.91× (z +12.6, q 1e-33, up in 40 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.367× (z -15.7, q 0e+00, down in 38 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCN2]] (+0.78, fdr 7e-06), [[DDAH1]] (+0.72, fdr 7e-06, ⚠ same locus), [[SRGAP1]] (+0.65, fdr 7e-06), [[CRIM1]] (+0.65, fdr 7e-06); moves opposite to [[ZUP1]] (-0.47, fdr 7e-05), [[TMEM68]] (-0.46, fdr 5e-05), [[CIAO2A]] (-0.46, fdr 5e-05).
> It is in [[Module 120]], a single-armed module (RHOA GTPase cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[CLCN4]] → it (grade B ⚠); 9 go from it, the strongest it → [[LATS2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 14 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6661.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **8.91×** | +12.6 | 1e-33 | 40/42 (MIA PaCa-2, SNU-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **2.24×** | +12.5 | 1e-33 | 31/41 (C32, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **2.62×** | +10.6 | 5e-24 | 34/41 (SNU-1, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **2.10×** | +8.2 | 4e-14 | 31/41 (SNU-1, LOX-IMVI, …) | rises with dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **3.74×** | +7.6 | 3e-12 | 30/41 (MIA PaCa-2, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.94×** | +7.3 | 3e-11 | 32/41 (SNU-1, BT-474, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.81×** | +6.5 | 6e-09 | 30/41 (SNU-1, BT-474, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.78×** | +5.9 | 3e-07 | 23/39 (A549, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~24% here); composition shift |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.66×** | +5.6 | 2e-06 | 31/41 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.64×** | +5.5 | 3e-06 | 22/41 (HS-578T, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.64×** | +5.4 | 3e-06 | 26/41 (MIA PaCa-2, SNU-1, …) | top dose only | position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.64×** | +5.4 | 3e-06 | 28/40 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **1.65×** | +5.3 | 6e-06 | 25/41 (C32, CFPAC-1, …) | rises with dose | composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.40×** | +5.2 | 9e-06 | 24/42 (SW 900, HT-29, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.58×** | +5.0 | 2e-05 | 29/41 (MIA PaCa-2, C32, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.60×** | +5.0 | 2e-05 | 29/40 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.54×** | +4.7 | 7e-05 | 27/40 (A-172, HS-578T, …) | all doses, stronger at high dose | position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **1.77×** | +4.5 | 2e-04 | 28/41 (A-172, NCI-H23, …) | all doses, flat | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.39×** | +3.6 | 0.007 | 22/41 (CFPAC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +3.6 | 0.009 | 22/41 (NCI-H460, HEC-1-A, …) | rises with dose |  |
| [[vincristine (drug)]] 5 µM |  | **1.86×** | +3.6 | 0.009 | 21/39 (NCI-H23, HS-578T, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **1.36×** | +3.4 | 0.018 | 16/41 (NCI-H2347, A498, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.31×** | +3.0 | 0.067 | 19/41 (A-172, SW 900, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.34×** | +3.0 | 0.069 | 14/41 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6661.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.367×** | -15.7 | 0e+00 | 38/42 (LOX-IMVI, SNU-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.408×** | -9.5 | 4e-19 | 36/40 (NCI-H23, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.412×** | -9.4 | 7e-19 | 33/43 (LOX-IMVI, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.431×** | -9.3 | 2e-18 | 31/41 (J82, NCI-H23, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.419×** | -9.3 | 2e-18 | 32/41 (LOX-IMVI, NCI-H23, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.443×** | -9.0 | 2e-17 | 36/40 (RKO, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.446×** | -8.9 | 3e-17 | 28/41 (RKO, J82, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.562×** | -6.4 | 1e-08 | 26/41 (HepG2/C3A, NCI-H23, …) | rises with dose | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.551×** | -6.4 | 1e-08 | 31/42 (J82, PANC-1, …) | top dose only | position effect removed |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.600×** | -5.7 | 8e-07 | 27/41 (J82, H4, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.05 µM |  | **0.593×** | -5.4 | 5e-06 | 28/40 (SK-MEL-2, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.577×** | -4.4 | 6e-04 | 23/41 (RKO, SW48, …) | rises with dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.691×** | -4.1 | 0.002 | 20/41 (J82, H4, …) | rises with dose |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.771×** | -4.1 | 0.002 | 19/41 (A498, HOP62, …) | rises with dose | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.498×** | -4.0 | 0.002 | 22/41 (RKO, SW48, …) | rises with dose | noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **0.703×** | -3.9 | 0.003 | 24/41 (SW 1088, RKO, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.704×** | -3.9 | 0.003 | 22/41 (HepG2/C3A, NCI-H23, …) | rises with dose | position effect removed |
| [[EX229 (drug)]] 0.05 µM |  | **0.702×** | -3.7 | 0.006 | 24/41 (RKO, SW48, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.81 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6661. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 123 | 11 (6 ⚠) | 11 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.29× (z +18.1) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 111× (z +17.1) | [[Adagrasib (drug)]] 0.05 µM 0.527× (z -15.4) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.225× (z -14.6) |
| [[LOX-IMVI (line)]] | wt | 654 | 3 (3 ⚠) | 13 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.27× (z +12.0) ⚠ cell-cycle shift, explains ~37% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0933× (z -27.6) |
| [[SNU-1 (line)]] | wt | 667 | 8 (5 ⚠) | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 8.50× (z +17.9) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 35.5× (z +15.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.187× (z -19.7) |
| [[NCI-H2030 (line)]] | alt | 645 | 0 | 10 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0997× (z -19.5) |
| [[NCI-H23 (line)]] | alt | 208 | 1 | 9 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 26.2× (z +12.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.158× (z -18.6) |
| [[A549 (line)]] | wt | 66.4 | 8 (6 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 5.30× (z +15.8) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 70.2× (z +14.9) | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.263× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 89.0 | 7 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +23.8) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 24.7× (z +11.5) | — |
| [[J82 (line)]] | alt | 317 | 0 | 7 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.206× (z -17.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -15.7) |
| [[RKO (line)]] | wt | 259 | 1 (1 ⚠) | 6 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.62× (z +8.5) ⚠ cell-cycle shift, explains ~37% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.113× (z -19.3) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -16.5) |
| [[Hs 766T (line)]] | wt | 181 | 2 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +11.1) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 18.6× (z +9.9) | [[Ponatinib (drug)]] 5 µM 0.230× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 121 | 2 (1 ⚠) | 4 | [[TAK-901 (drug)]] 5 µM 41.5× (z +13.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -12.5) |
| [[A-427 (line)]] | wt | 90.8 | 2 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 16.8× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.143× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.185× (z -10.7) |
| [[HepG2_C3A (line)]] | wt | 219 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.177× (z -15.7) |
| [[Panc 03.27 (line)]] | alt | 186 | 4 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +13.5) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 13.5× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.247× (z -8.7) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 36.1 | 4 (4 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 7.78× (z +10.9) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[C32 (line)]] | wt | 35.2 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 35.1× (z +24.2) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[A-172 (line)]] | wt | 38.2 | 3 (2 ⚠) | 0 | [[Daptomycin (drug)]] 0.5 µM 6.51× (z +9.0) ⚠ unreliable plate only · without an alert: [[Peretinoin (drug)]] 0.5 µM 6.12× (z +8.7) | — |
| [[AsPC-1 (line)]] | alt | 127 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -13.5) |
| [[C-33 A (line)]] | alt | 107 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -10.4) |
| [[NCI-H661 (line)]] | alt | 352 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0530× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.198× (z -11.4) |
| [[PANC-1 (line)]] | alt | 284 | 2 (1 ⚠) | 1 | [[TAK-901 (drug)]] 5 µM 41.7× (z +14.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -11.7) |
| [[RPMI-7951 (line)]] | alt | 72.7 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 7.29× (z +15.3) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 22.4× (z +8.8) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.195× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 62.5 | 2 (1 ⚠) | 1 | [[TAK-901 (drug)]] 5 µM 104× (z +11.0) | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0776× (z -11.1) |
| [[A498 (line)]] | wt | 88.8 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +10.9) ⚠ cell-cycle shift, explains ~68% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -10.5) |
| [[HOP62 (line)]] | alt | 62.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +8.5) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 15.1× (z +8.5) | — |
| [[HS-578T (line)]] | alt | 143 | 1 | 1 | [[Peretinoin (drug)]] 0.5 µM 5.74× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -9.2) |
| [[HT-29 (line)]] | alt | 35.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.91× (z +14.4) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[SW1417 (line)]] | alt | 65.7 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.55× (z +14.5) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[HEC-1-A (line)]] | alt | 119 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.440× (z -9.0) |
| [[hTERT-HPNE (line)]] | wt | 127 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 76.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -9.6) |
| [[NCI-H596 (line)]] | alt | 109 | 1 | 0 | [[Fulvestrant (drug)]] 5 µM 7.08× (z +9.9) | — |
| [[SNU-423 (line)]] | alt | 68.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +8.7) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[SW 900 (line)]] | alt | 71.8 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 4.35× (z +8.6) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[SW48 (line)]] | wt | 109 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.166× (z -13.3) |
| [[AN3 CA (line)]] | alt | 76.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.4 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 10.2 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 81.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 20.4 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 22.3 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 12.5 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 79.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 73.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.95 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 20.2 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6661), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCN2]] | +0.78 | +0.76 / +0.80 | both halves | 7e-06 | same gene group; pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 816 |
| [[DDAH1]] | +0.72 | +0.72 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_UV_RESPONSE_DN; ⚠ same locus (2.4 kb: neighbours can correlate without regulation) |
| [[SRGAP1]] | +0.65 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[CRIM1]] | +0.65 | +0.62 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[DLC1]] | +0.64 | +0.55 / +0.62 | both halves | 1e-05 | pathway: HALLMARK_UV_RESPONSE_DN |
| [[ANKRD1]] | +0.64 | +0.53 / +0.61 | both halves | 1e-05 | STRING 772 |
| [[AMOTL2]] | +0.64 | +0.66 / +0.69 | both halves | 7e-06 | STRING 759 |
| [[STARD13]] | +0.63 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[CYTOR]] | +0.61 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[SFTA1P]] | +0.60 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[SMURF2]] | +0.60 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[LATS2]] | +0.58 | +0.59 / +0.64 | both halves | 7e-06 | STRING 651 |
| [[EXT1]] | +0.58 | +0.59 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZUP1]] | -0.47 | -0.47 / -0.37 | both halves | 7e-05 |  |
| [[TMEM68]] | -0.46 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[CIAO2A]] | -0.46 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[TIAL1]] | -0.45 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[BCL2L2-PABPN1]] | -0.45 | -0.45 / -0.38 | both halves | 6e-05 |  |
| [[NAPB]] | -0.44 | -0.47 / -0.40 | both halves | 4e-05 |  |
| [[RTCA]] | -0.44 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[SOS1]] | -0.44 | -0.43 / -0.37 | both halves | 8e-05 |  |
| [[NADSYN1]] | -0.43 | -0.37 / -0.42 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLCN4]] | B | CLCN4 activity lowers CCN1's level | lines that do not express CLCN4 (7) vs lines expressing it (43) | 3.16× higher at baseline in the lines without CLCN4 | 0.006 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises CCN1's level | compounds that target TOP2A: 5 of 5 lower it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 6.7% of all compounds | 0.008 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[SFTA1P]] | B | SFTA1P activity raises CCN1's level | lines that do not express SFTA1P (32) vs lines expressing it (18) | 2.48× lower at baseline in the lines without SFTA1P | 0.021 | ⚠ within organs, on part of the lines; also absent: SUN3, SIM1, MMRN1 |
| [[CLCN4]] | B | CLCN4 activity weakens CCN1's drug response | lines that do not express CLCN4 (7) vs lines expressing it (36) | the lines without CLCN4 respond 1.28× as strongly (z diff -0.95); strongest at c-Kit-IN-1 0.05 µM: 0.22x vs 0.54x (z diff -4.4) | 0.058 | ⚠ within organs, on part of the lines; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[FRMD6]] | B | FRMD6 activity raises CCN1's level | lines that do not express FRMD6 (13) vs lines expressing it (37) | 2.72× lower at baseline in the lines without FRMD6 | 0.062 | ⚠ within organs, on part of the lines; also absent: CTSL, OSMR-DT, EVC; maybe low, not absent |
| [[CCN2]] | B | CCN2 activity raises CCN1's level | lines that do not express CCN2 (17) vs lines expressing it (33) | 2.36× lower at baseline in the lines without CCN2 | 0.068 | ⚠ within organs, on part of the lines; also absent: GDNF-AS1, CPEB1, TRIML2 |
| [[AMOTL2]] | C | AMOTL2 activity raises CCN1's level | lines that do not express AMOTL2 (4) vs lines expressing it (46) | 3.97× lower at baseline in the lines without AMOTL2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: BCL2L1, RASSF7, FCHO1; its own permutation p |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LATS2]] | B | CCN1 activity raises LATS2's level | lines that do not express CCN1 (7) vs lines expressing it (43) | 2.08× lower at baseline in the lines without CCN1 | 0.004 | ⚠ within organs, on part of the lines; also absent: CTSL, ENSG00000232295, EBI3 |
| [[TNFRSF12A]] | B | CCN1 activity raises TNFRSF12A's level | lines that do not express CCN1 (7) vs lines expressing it (43) | 1.99× lower at baseline in the lines without CCN1 | 0.007 | ⚠ within organs, on part of the lines; also absent: CTSL, ENSG00000232295, EBI3 |
| [[PTPN14]] | B | CCN1 activity raises PTPN14's level | lines that do not express CCN1 (7) vs lines expressing it (43) | 1.98× lower at baseline in the lines without CCN1 | 0.017 | ⚠ within organs, on part of the lines; also absent: CTSL, ENSG00000232295, EBI3 |
| [[DDAH1]] | B | CCN1 activity raises DDAH1's level | lines that do not express CCN1 (7) vs lines expressing it (43) | 2.05× lower at baseline in the lines without CCN1 | 0.019 | ⚠ within organs, on part of the lines; also absent: CTSL, ENSG00000232295, EBI3 |
| [[AMOTL2]] | B | CCN1 activity raises AMOTL2's level | lines that do not express CCN1 (7) vs lines expressing it (43) | 1.72× lower at baseline in the lines without CCN1 | 0.023 | ⚠ within organs, on part of the lines; also absent: CTSL, ENSG00000232295, EBI3 |
| [[CRIM1]] | B | CCN1 activity raises CRIM1's level | lines that do not express CCN1 (7) vs lines expressing it (43) | 2.14× lower at baseline in the lines without CCN1 | 0.054 | ⚠ within organs, on part of the lines; also absent: CTSL, ENSG00000232295, EBI3 |
| [[ABL2]] | B | CCN1 activity raises ABL2's level | lines that do not express CCN1 (7) vs lines expressing it (43) | 2.52× lower at baseline in the lines without CCN1 | 0.060 | ⚠ within organs, on part of the lines; also absent: CTSL, ENSG00000232295, EBI3 |
| [[MIR222HG]] | B | CCN1 activity raises MIR222HG's level | lines that do not express CCN1 (7) vs lines expressing it (43) | 1.40× lower at baseline in the lines without CCN1 | 0.070 | ⚠ within organs, on part of the lines; also absent: CTSL, ENSG00000232295, EBI3 |
| [[MAPK8]] | B | CCN1 activity raises MAPK8's level | lines that do not express CCN1 (7) vs lines expressing it (43) | 1.28× lower at baseline in the lines without CCN1 | 0.095 | ⚠ within organs, on part of the lines; also absent: CTSL, ENSG00000232295, EBI3 |

## Where it sits

- **Module**: [[Module 120]] — RHOA GTPase cycle; 41 genes; every member is in the + arm (projection on the module's main direction 0.827). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (39.5, 12.5); signed map (13.9, 41.0). **Vector** length 151, 51.4% of its response variance represented; |z| ≥ 3 in 1,607 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.9 | +12.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | +6.3 | +12.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | +6.2 | +5.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.0 | +3.6 |
|  | [[vincristine (drug)]] 0.5 µM |  | +5.8 | +4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +3.6 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +5.2 | +4.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.0 | +5.2 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -7.7 | -6.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -6.9 | -9.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.8 | -3.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.7 | -9.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~85% of this change | -6.6 | -3.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -5.7 | -9.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.3 | -4.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.0 | -9.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -4.9 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | cellular communication network factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p22.3 — chr1:85,580,761-85,584,589 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GIG1; previously IGFBP10, CYR61 |
| Gene groups (HGNC) | Cellular communication network factors |
| Hallmark sets | UV_RESPONSE_DN, HYPOXIA, EPITHELIAL_MESENCHYMAL_TRANSITION, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 2 pathways, smallest: Post-translational protein phosphorylation; Regulation of Insulin-like Growth Factor (IGF) transport and uptake by Insulin-like Growth Factor Binding Proteins (IGFBPs) |
| Matched by | ensembl_id |

**Function**, from UniProt [O00622](https://www.uniprot.org/uniprotkb/O00622) (CCN family member 1):

> Promotes cell proliferation, chemotaxis, angiogenesis and cell adhesion. Appears to play a role in wound healing by up-regulating, in skin fibroblasts, the expression of a number of genes involved in angiogenesis, inflammation and matrix remodeling including VEGA-A, VEGA-C, MMP1, MMP3, TIMP1, uPA, PAI-1 and integrins alpha-3 and alpha-5. CCN1-mediated gene regulation is dependent on heparin-binding. Down-regulates the expression of alpha-1 and alpha-2 subunits of collagen type-1. Promotes cell …

**Summary**, from NCBI Gene [3491](https://www.ncbi.nlm.nih.gov/gene/3491):

> The secreted protein encoded by this gene is growth factor-inducible and promotes the adhesion of endothelial cells. The encoded protein interacts with several integrins and with heparan sulfate proteoglycan. This protein also plays a role in cell proliferation, differentiation, angiogenesis, apoptosis, and extracellular matrix formation. [provided by RefSeq, Sep 2011]

**Accessions** — [HGNC:2654](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2654) · Entrez [3491](https://www.ncbi.nlm.nih.gov/gene/3491) · UniProt [O00622](https://www.uniprot.org/uniprotkb/O00622) · Ensembl [ENSG00000142871](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142871)

## Data

Gene col 6661: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6661); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6661, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6661]; `tensor/DDL_lfc|DDL_z.npy` [6661]; `embed/gene_vectors.npy` [6661]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6661 or target_col == 6661). Every well: [[CCN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
