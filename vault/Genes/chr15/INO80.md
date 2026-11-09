---
symbol: "INO80"
type: "gene"
col: 4930
ensembl_id: "ENSG00000128908"
name: "INO80 complex ATPase subunit"
location: "15q15.1"
module: 51
arm: "+"
pooled_cpm: 139.02
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 20
n_dd_up_clean: 17
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# INO80

*INO80 complex ATPase subunit* — 15q15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.31× (z +17.8, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.363× (z -21.6, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WARS2]] (+0.82, fdr 7e-06), [[EPC2]] (+0.77, fdr 7e-06), [[TTC27]] (+0.76, fdr 7e-06); moves opposite to [[PMS2P3-1]] (-0.64, fdr 1e-05), [[GMCL1]] (-0.63, fdr 1e-05), [[INSIG2]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4930.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.31×** | +17.8 | 0e+00 | 48/48 (LS 180, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.74×** | +16.7 | 0e+00 | 46/48 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.87×** | +13.3 | 2e-38 | 46/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.86×** | +13.2 | 2e-37 | 47/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.79×** | +12.3 | 1e-32 | 43/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.80×** | +12.0 | 4e-31 | 45/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.71×** | +11.4 | 3e-28 | 44/48 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.71×** | +11.1 | 1e-26 | 44/49 (LoVo, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.66×** | +10.7 | 4e-25 | 46/48 (MIA PaCa-2, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.57×** | +10.5 | 5e-24 | 46/48 (PANC-1, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.53×** | +9.1 | 7e-18 | 46/48 (HT-29, NCI-H460, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +7.2 | 3e-11 | 38/47 (LoVo, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.40×** | +7.2 | 3e-11 | 38/48 (HT-29, NCI-H2030, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.30×** | +5.2 | 8e-06 | 31/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.40×** | +5.2 | 8e-06 | 33/48 (SHP-77, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.26×** | +4.9 | 3e-05 | 25/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.31×** | +4.1 | 0.002 | 28/49 (MIA PaCa-2, SNU-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.20×** | +3.9 | 0.003 | 21/48 (LOX-IMVI, SNU-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4930.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.363×** | -21.6 | 0e+00 | 48/48 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.391×** | -20.0 | 0e+00 | 48/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.418×** | -18.5 | 0e+00 | 48/48 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.547×** | -18.2 | 0e+00 | 46/49 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.509×** | -13.8 | 2e-41 | 40/44 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.510×** | -13.2 | 1e-37 | 48/48 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.564×** | -12.2 | 3e-32 | 44/48 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.578×** | -11.7 | 9e-30 | 41/49 (A-427, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.644×** | -9.4 | 5e-19 | 37/48 (NCI-H23, SK-MEL-2, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.637×** | -9.2 | 1e-18 | 37/50 (SW48, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.751×** | -8.6 | 3e-16 | 42/48 (PANC-1, HT-29, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.659×** | -8.2 | 1e-14 | 36/45 (AN3 CA, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.675×** | -8.1 | 3e-14 | 38/48 (NCI-H23, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.505×** | -7.6 | 1e-12 | 48/49 (PANC-1, AsPC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.739×** | -6.5 | 4e-09 | 42/49 (A498, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.789×** | -5.1 | 1e-05 | 27/48 (LoVo, NCI-H23, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.802×** | -4.7 | 7e-05 | 28/49 (RKO, HT-29, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 0.876× | -4.0 | 0.002 | 13/48 (AsPC-1, RPMI-7951, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4930. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 137 | 14 (2 ⚠) | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +19.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -15.3) |
| [[PANC-1 (line)]] | alt | 158 | 9 (1 ⚠) | 10 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +19.2) | [[Belinostat (drug)]] 5 µM 0.304× (z -19.5) |
| [[LoVo (line)]] | wt | 274 | 9 (2 ⚠) | 7 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.61× (z +18.6) | [[Dinaciclib (drug)]] 5 µM 0.301× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.406× (z -13.1) |
| [[SW480 (line)]] | alt | 128 | 5 | 9 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +12.5) | [[Belinostat (drug)]] 5 µM 0.346× (z -15.7) |
| [[LS 180 (line)]] | wt | 141 | 6 (1 ⚠) | 7 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.95× (z +19.7) | [[Belinostat (drug)]] 5 µM 0.378× (z -12.1) |
| [[NCI-H1573 (line)]] | alt | 187 | 9 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +15.9) | [[Belinostat (drug)]] 5 µM 0.278× (z -14.4) |
| [[NCI-H23 (line)]] | alt | 157 | 5 (1 ⚠) | 8 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +11.6) | [[Auranofin (drug)]] 5 µM 0.321× (z -15.3) |
| [[LOX-IMVI (line)]] | wt | 133 | 5 | 7 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.43× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -14.6) |
| [[MIA PaCa-2 (line)]] | alt | 149 | 4 | 8 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 5.08× (z +9.5) | [[Panobinostat (drug)]] 5 µM 0.257× (z -15.2) |
| [[SNU-1 (line)]] | wt | 199 | 6 (1 ⚠) | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.219× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.346× (z -11.2) |
| [[HEC-1-A (line)]] | alt | 147 | 2 | 9 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.283× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.313× (z -16.5) |
| [[HT-29 (line)]] | alt | 176 | 7 (1 ⚠) | 4 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.55× (z +14.5) | [[Belinostat (drug)]] 5 µM 0.311× (z -13.4) |
| [[NCI-H2030 (line)]] | alt | 293 | 2 | 9 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -17.8) |
| [[SW48 (line)]] | wt | 184 | 3 | 8 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.92× (z +12.6) | [[Belinostat (drug)]] 5 µM 0.218× (z -14.0) |
| [[A498 (line)]] | wt | 102 | 3 | 7 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +21.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -15.4) |
| [[KATO III (line)]] | alt | 148 | 6 | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.79× (z +13.7) | [[Belinostat (drug)]] 5 µM 0.332× (z -14.8) |
| [[SNU-423 (line)]] | alt | 94.8 | 2 | 8 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.21× (z +9.5) | [[Panobinostat (drug)]] 5 µM 0.330× (z -13.5) |
| [[RKO (line)]] | wt | 143 | 4 (1 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +12.3) | [[Belinostat (drug)]] 5 µM 0.348× (z -11.9) |
| [[SW1417 (line)]] | alt | 158 | 2 | 7 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.26× (z +10.3) | [[Panobinostat (drug)]] 0.5 µM 0.391× (z -11.9) |
| [[AsPC-1 (line)]] | alt | 91.3 | 4 (1 ⚠) | 4 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.55× (z +15.0) | [[Belinostat (drug)]] 5 µM 0.363× (z -12.0) |
| [[CFPAC-1 (line)]] | alt | 144 | 1 | 7 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.79× (z +9.6) | [[Belinostat (drug)]] 5 µM 0.361× (z -14.1) |
| [[HOP62 (line)]] | alt | 100 | 2 | 6 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.18× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -12.5) |
| [[NCI-H1792 (line)]] | alt | 147 | 3 | 5 | [[Harringtonine (drug)]] 5 µM 2.91× (z +10.9) | [[Belinostat (drug)]] 5 µM 0.236× (z -15.5) |
| [[A-427 (line)]] | wt | 111 | 2 | 5 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 4.57× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.418× (z -10.9) |
| [[C-33 A (line)]] | alt | 204 | 1 | 6 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.45× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -14.1) |
| [[COLO 205 (line)]] | alt | 174 | 4 (1 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.48× (z +11.5) | [[Belinostat (drug)]] 5 µM 0.271× (z -12.1) |
| [[HepG2_C3A (line)]] | wt | 96.1 | 1 | 6 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.62× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.254× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.277× (z -12.2) |
| [[NCI-H2347 (line)]] | alt | 79.5 | 3 | 4 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +14.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.500× (z -12.5) |
| [[SHP-77 (line)]] | alt | 122 | 4 (1 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.16× (z +14.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -13.2) |
| [[Panc 03.27 (line)]] | alt | 127 | 2 | 4 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.37× (z +9.7) | [[Belinostat (drug)]] 5 µM 0.416× (z -9.9) |
| [[SK-MEL-2 (line)]] | alt | 118 | 1 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +10.0) | [[Auranofin (drug)]] 5 µM 0.336× (z -13.1) |
| [[SW 900 (line)]] | alt | 107 | 3 | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.10× (z +11.8) | [[Belinostat (drug)]] 5 µM 0.354× (z -10.9) |
| [[A-172 (line)]] | wt | 88.1 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +17.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.450× (z -13.5) |
| [[HS-578T (line)]] | alt | 84.4 | 1 | 4 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +10.1) | [[Belinostat (drug)]] 5 µM 0.329× (z -13.1) |
| [[RPMI-7951 (line)]] | alt | 177 | 1 | 4 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.31× (z +9.3) | [[Belinostat (drug)]] 5 µM 0.321× (z -13.2) |
| [[A549 (line)]] | wt | 100 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +18.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -16.1) |
| [[C32 (line)]] | wt | 81.0 | 2 | 2 | [[Harringtonine (drug)]] 5 µM 2.67× (z +9.6) | [[Belinostat (drug)]] 5 µM 0.349× (z -10.8) |
| [[J82 (line)]] | alt | 133 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.518× (z -11.9) |
| [[H4 (line)]] | wt | 131 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.335× (z -10.3) |
| [[AN3 CA (line)]] | alt | 177 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0623× (z -19.6) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.224× (z -11.0) |
| [[BT-474 (line)]] | alt | 128 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.386× (z -10.5) |
| [[CHP-212 (line)]] | wt | 136 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -9.9) |
| [[HCT15 (line)]] | alt | 185 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.26× (z +9.2) | [[Belinostat (drug)]] 5 µM 0.423× (z -9.8) |
| [[Hs 766T (line)]] | wt | 66.0 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.05× (z +10.5) | — |
| [[SW 1088 (line)]] | alt | 105 | 0 | 1 | — | [[Monocrotaline (drug)]] 5 µM 0.106× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 81.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 98.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4930), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WARS2]] | +0.82 | +0.71 / +0.79 | both halves | 7e-06 |  |
| [[EPC2]] | +0.77 | +0.70 / +0.77 | both halves | 7e-06 | STRING 563 |
| [[TTC27]] | +0.76 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[THADA]] | +0.73 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[ZNF644]] | +0.72 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[STAG1]] | +0.72 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[LANCL2]] | +0.71 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[COMMD10]] | +0.70 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[UTP20]] | +0.68 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[CDK12]] | +0.68 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[BPTF]] | +0.66 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[AP5S1]] | +0.65 | +0.58 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PMS2P3-1]] | -0.64 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[GMCL1]] | -0.63 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[INSIG2]] | -0.61 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[HDAC3]] | -0.61 | -0.46 / -0.61 | both halves | 3e-05 |  |
| [[SDHAP4]] | -0.60 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[HERC3]] | -0.60 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[IFI27L1]] | -0.60 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[SRP54-AS1]] | -0.60 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[HSPB11]] | -0.59 | -0.41 / -0.61 | both halves | 4e-05 |  |
| [[OSTF1]] | -0.58 | -0.46 / -0.54 | both halves | 2e-05 |  |
| [[PJA2]] | -0.57 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[SRD5A1]] | -0.57 | -0.49 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.764). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-23.3, 12.7); signed map (12.5, -31.7). **Vector** length 110, 44.6% of its response variance represented; |z| ≥ 3 in 1,644 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.5 | +16.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.1 | +12.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.7 | +11.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | -13.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.4 | -11.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.7 | +0.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.4 | +9.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | -1.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.9 | -0.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.9 | +0.9 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -7.1 | -12.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -6.0 | -13.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.3 | -9.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -5.2 | -7.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.6 | -21.6 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -3.5 | -0.4 |
|  | [[Balsalazide (sodium hydrate) (drug)]] 0.05 µM |  | -3.2 | -0.9 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -3.0 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | INO80 complex ATPase subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.1 — chr15:40,978,880-41,116,280 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1259, hINO80, INO80A; previously INOC1 |
| Gene groups (HGNC) | INO80 complex subunits; SNF2 related family; DexD/H helicases |
| Reactome | 6 pathways, smallest: DNA Damage Recognition in GG-NER; UCH proteinases; Global Genome Nucleotide Excision Repair (GG-NER) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULG1](https://www.uniprot.org/uniprotkb/Q9ULG1) (Chromatin-remodeling ATPase INO80):

> ATPase component of the chromatin remodeling INO80 complex which is involved in transcriptional regulation, DNA replication and DNA repair. Binds DNA. As part of the INO80 complex, remodels chromatin by shifting nucleosomes. Regulates transcription upon recruitment by YY1 to YY1-activated genes, where it acts as an essential coactivator. Involved in UV-damage excision DNA repair. The contribution to DNA double-strand break repair appears to be largely indirect through transcriptional …

**Summary**, from NCBI Gene [54617](https://www.ncbi.nlm.nih.gov/gene/54617):

> This gene encodes a subunit of the chromatin remodeling complex, which is classified into subfamilies depending on sequence features apart from the conserved ATPase domain. This protein is the catalytic ATPase subunit of the INO80 chromatin remodeling complex, which is characterized by a DNA-binding domain. This protein is proposed to bind DNA and be recruited by the YY1 transcription factor to activate certain genes. Alternative splicing results in multiple transcript variants. [provided by …

**Accessions** — [HGNC:26956](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26956) · Entrez [54617](https://www.ncbi.nlm.nih.gov/gene/54617) · UniProt [Q9ULG1](https://www.uniprot.org/uniprotkb/Q9ULG1) · Ensembl [ENSG00000128908](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128908)

## Data

Gene col 4930: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4930); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4930, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4930]; `tensor/DDL_lfc|DDL_z.npy` [4930]; `embed/gene_vectors.npy` [4930]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4930 or target_col == 4930). Every well: [[INO80 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/INO80.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
