---
symbol: "WAPL"
type: "gene"
col: 714
ensembl_id: "ENSG00000062650"
name: "WAPL cohesin release factor"
location: "10q23.2"
module: 7
arm: "+"
pooled_cpm: 163.15
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 6
n_dd_up_clean: 17
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# WAPL

*WAPL cohesin release factor* — 10q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.49× (z +21.4, q 0e+00, up in 46 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.477× (z -23.4, q 0e+00, down in 40 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.850× (z -7.6, q 6e-12, down in 16 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNTTIP2]] (+0.72, fdr 7e-06), [[CCDC137]] (+0.72, fdr 7e-06), [[PSMD7]] (+0.69, fdr 7e-06); moves opposite to [[CREG1]] (-0.59, fdr 3e-05), [[NUP62CL]] (-0.58, fdr 1e-05), [[TWSG1]] (-0.57, fdr 2e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 714.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.49×** | +21.4 | 0e+00 | 46/49 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.55×** | +20.4 | 0e+00 | 44/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.74×** | +18.1 | 0e+00 | 47/48 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.79×** | +17.6 | 0e+00 | 44/48 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.73×** | +17.0 | 0e+00 | 48/48 (HT-29, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.53×** | +14.0 | 1e-42 | 45/48 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.52×** | +13.8 | 3e-41 | 43/48 (HT-29, NCI-H1573, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.52×** | +13.7 | 4e-41 | 38/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.38×** | +10.7 | 1e-24 | 40/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.38×** | +10.2 | 2e-22 | 37/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.33×** | +9.4 | 2e-19 | 39/48 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.33×** | +9.4 | 4e-19 | 38/48 (LoVo, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.33×** | +9.3 | 7e-19 | 38/48 (LoVo, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.30×** | +8.6 | 3e-16 | 31/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.59×** | +8.0 | 7e-14 | 37/45 (SW480, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.37×** | +7.3 | 1e-11 | 38/49 (MIA PaCa-2, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.20×** | +6.1 | 4e-08 | 23/48 (LoVo, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 714.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.477×** | -23.4 | 0e+00 | 40/44 (A-427, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.519×** | -21.5 | 0e+00 | 46/49 (NCI-H460, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.552×** | -18.1 | 0e+00 | 40/45 (A498, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.850× | -7.6 | 6e-12 | 16/48 (A498, NCI-H2347, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.829×** | -6.2 | 8e-08 | 26/49 (CFPAC-1, A498, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.813×** | -4.8 | 1e-04 | 25/47 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[OTS514 (drug)]] 5 µM |  | **0.756×** | -4.8 | 1e-04 | 28/46 (SNU-1, SNU-423, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.867× | -4.7 | 2e-04 | 18/48 (Hs 766T, RKO, …) | inconsistent across doses | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | 0.880× | -4.2 | 0.002 | 11/48 (AN3 CA, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.883× | -4.1 | 0.003 | 10/48 (A498, PANC-1, …) | inconsistent across doses |  |
| [[Posaconazole (drug)]] 5 µM |  | 0.897× | -3.4 | 0.033 | 2/48 (HEC-1-A, C32) | top dose only | plate-row cell shift |
| [[Entrectinib (drug)]] 5 µM |  | 0.904× | -3.3 | 0.046 | 2/48 (SW 1271, Panc 03.27) | top dose only |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | 0.899× | -3.2 | 0.054 | 6/47 (RKO, COLO 205, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 714. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 203 | 13 (1 ⚠) | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.05× (z +19.2) | [[Dinaciclib (drug)]] 0.5 µM 0.539× (z -12.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 228 | 12 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +22.8) | [[Dinaciclib (drug)]] 0.5 µM 0.373× (z -19.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 151 | 13 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.48× (z +18.5) | [[Dinaciclib (drug)]] 0.5 µM 0.647× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 158 | 10 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.414× (z -13.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 188 | 7 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.55× (z +13.6) | [[Dinaciclib (drug)]] 0.5 µM 0.370× (z -17.0) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 186 | 6 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 6.16× (z +14.8) | [[Dinaciclib (drug)]] 5 µM 0.399× (z -13.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 174 | 7 (1 ⚠) | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.79× (z +16.1) | [[Dinaciclib (drug)]] 5 µM 0.290× (z -23.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 156 | 8 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +13.9) | [[Dinaciclib (drug)]] 0.5 µM 0.475× (z -12.1) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 147 | 6 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.65× (z +14.1) | [[Dinaciclib (drug)]] 5 µM 0.230× (z -22.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 159 | 5 | 3 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.91× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.477× (z -12.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 148 | 5 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.76× (z +14.6) | [[Dinaciclib (drug)]] 0.5 µM 0.415× (z -15.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 104 | 6 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.517× (z -8.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 135 | 5 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.35× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.0729× (z -44.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 153 | 5 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.39× (z +14.3) | [[Dinaciclib (drug)]] 0.05 µM 0.415× (z -13.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 143 | 4 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.45× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.327× (z -16.3) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 149 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.92× (z +10.2) | — |
| [[SNU-423 (line)]] | alt | 193 | 4 | 3 (3 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.00× (z +10.9) | [[Dinaciclib (drug)]] 0.05 µM 0.421× (z -13.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 124 | 5 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.93× (z +15.0) | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -19.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 170 | 5 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.96× (z +12.9) | [[Dinaciclib (drug)]] 0.5 µM 0.560× (z -9.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 196 | 1 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 2.61× (z +9.6) | [[Dinaciclib (drug)]] 0.05 µM 0.386× (z -16.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 117 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.273× (z -15.5) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 160 | 4 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.06× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.424× (z -12.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 109 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +11.5) | [[Dinaciclib (drug)]] 0.05 µM 0.393× (z -12.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 160 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +16.5) | [[Dinaciclib (drug)]] 0.05 µM 0.403× (z -12.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 175 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.80× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -15.6) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 213 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.457× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 182 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +12.5) | [[Dinaciclib (drug)]] 0.05 µM 0.344× (z -15.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 176 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.58× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.469× (z -11.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 134 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +11.9) | [[Dinaciclib (drug)]] 0.05 µM 0.316× (z -15.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 170 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.77× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.271× (z -14.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 228 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.327× (z -17.8) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 171 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.28× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.362× (z -12.4) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 161 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.348× (z -16.4) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 227 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.444× (z -11.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 135 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.285× (z -13.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 179 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 2.71× (z +9.4) | — |
| [[SW48 (line)]] | wt | 153 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -12.0) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 128 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 2.00× (z +9.5) | — |
| [[CHP-212 (line)]] | wt | 148 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0654× (z -20.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 126 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.566× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 143 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.592× (z -9.3) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 137 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0689× (z -12.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 79.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.296× (z -13.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 226 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 64.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 138 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 714), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNTTIP2]] | +0.72 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[CCDC137]] | +0.72 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[PSMD7]] | +0.69 | +0.64 / +0.61 | both halves | 7e-06 | pathway: Mitotic Anaphase |
| [[SART3]] | +0.68 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[SNW1]] | +0.67 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[TSSC4]] | +0.67 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[PHF5A]] | +0.65 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[SLC4A1AP]] | +0.65 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[PRR14L]] | +0.64 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[CHD8]] | +0.64 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[CDK12]] | +0.63 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[FAM32A]] | +0.62 | +0.64 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CREG1]] | -0.59 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[NUP62CL]] | -0.58 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[TWSG1]] | -0.57 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[NPTN]] | -0.54 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[CLSTN1]] | -0.54 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[CXADR]] | -0.53 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[CD83]] | -0.53 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[TMSB4X]] | -0.53 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[SNX30]] | -0.52 | -0.52 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.598). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-38.6, 8.6); signed map (-4.6, -22.6). **Vector** length 86.9, 25.5% of its response variance represented; |z| ≥ 3 in 1,435 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +6.3 | +17.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.5 | +18.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.3 | +13.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.0 | +9.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +5.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +6.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.4 | +5.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | -0.4 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.2 | -18.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.1 | -7.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.5 | -6.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.9 | -21.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.4 | -23.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | -0.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.9 | -1.3 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.6 | -0.7 |
|  | [[Clonidine (hydrochloride) (drug)]] 5 µM |  | -1.6 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | WAPL cohesin release factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q23.2 — chr10:86,435,256-86,521,792 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FOE; previously KIAA0261, WAPAL |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Reactome | 12 pathways, smallest: Cohesin Loading onto Chromatin; Establishment of Sister Chromatid Cohesion; Mitotic Telophase/Cytokinesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z5K2](https://www.uniprot.org/uniprotkb/Q7Z5K2) (Wings apart-like protein homolog):

> Regulator of sister chromatid cohesion in mitosis which negatively regulates cohesin association with chromatin. Involved in both sister chromatid cohesion during interphase and sister-chromatid resolution during early stages of mitosis. Couples DNA replication to sister chromatid cohesion. Cohesion ensures that chromosome partitioning is accurate in both meiotic and mitotic cells and plays an important role in DNA repair.

**Summary**, from NCBI Gene [23063](https://www.ncbi.nlm.nih.gov/gene/23063):

> Enables ATP-dependent protein-DNA unloader activity. Involved in several processes, including mitotic sister chromatid segregation; negative regulation of DNA replication; and negative regulation of sister chromatid cohesion. Located in chromatin; cytoplasm; and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23293](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23293) · Entrez [23063](https://www.ncbi.nlm.nih.gov/gene/23063) · UniProt [Q7Z5K2](https://www.uniprot.org/uniprotkb/Q7Z5K2) · Ensembl [ENSG00000062650](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000062650)

## Data

Gene col 714: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 714); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 714, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 714]; `tensor/DDL_lfc|DDL_z.npy` [714]; `embed/gene_vectors.npy` [714]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 714 or target_col == 714). Every well: [[WAPL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WAPL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
