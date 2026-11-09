---
symbol: "PIAS1"
type: "gene"
col: 417
ensembl_id: "ENSG00000033800"
name: "protein inhibitor of activated STAT 1"
location: "15q23"
module: 24
arm: "+"
pooled_cpm: 218.94
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 12
n_dd_up_clean: 14
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# PIAS1

*protein inhibitor of activated STAT 1* — 15q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.50× (z +14.2, q 6e-43, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.300× (z -34.4, q 0e+00, down in 44 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.697× (z -10.7, q 1e-24, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NPEPPS]] (+0.72, fdr 7e-06), [[PAN3]] (+0.72, fdr 7e-06), [[AMBRA1]] (+0.71, fdr 7e-06); moves opposite to [[THOC6]] (-0.66, fdr 7e-06), [[TXLNA]] (-0.66, fdr 1e-05), [[ZNF121]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 417.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.50×** | +14.2 | 6e-43 | 47/49 (PANC-1, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.54×** | +12.9 | 1e-35 | 45/48 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.53×** | +12.7 | 1e-34 | 44/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.49×** | +11.8 | 4e-30 | 41/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.05×** | +11.1 | 1e-26 | 42/48 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +10.8 | 2e-25 | 32/49 (MIA PaCa-2, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.44×** | +10.7 | 5e-25 | 38/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.37×** | +9.3 | 7e-19 | 32/48 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.35×** | +8.9 | 3e-17 | 37/48 (RPMI-7951, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +8.8 | 1e-16 | 35/48 (NCI-H23, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.32×** | +7.9 | 1e-13 | 28/48 (PANC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.29×** | +7.6 | 2e-12 | 35/48 (PANC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.22×** | +5.9 | 2e-07 | 24/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.23×** | +5.8 | 2e-07 | 26/47 (PANC-1, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~8% of this change | **1.20×** | +5.2 | 8e-06 | 25/48 (RPMI-7951, HS-578T, …) | all doses, flat |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.18× | +4.7 | 7e-05 | 21/49 (C-33 A, SHP-77, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.22×** | +4.3 | 6e-04 | 22/49 (PANC-1, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.15× | +4.1 | 0.001 | 20/48 (SK-MEL-2, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 8 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 417.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.300×** | -34.4 | 0e+00 | 44/44 (KATO III, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.322×** | -33.6 | 0e+00 | 49/49 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.389×** | -25.9 | 0e+00 | 41/45 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.697×** | -10.7 | 1e-24 | 41/48 (HOP62, SW480, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.742×** | -8.9 | 8e-17 | 39/48 (KATO III, HT-29, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.780×** | -7.4 | 2e-11 | 32/48 (CFPAC-1, SW480, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.792×** | -6.7 | 2e-09 | 27/47 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.690×** | -5.8 | 6e-07 | 37/48 (CFPAC-1, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.746×** | -4.6 | 3e-04 | 27/48 (CFPAC-1, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.762×** | -4.2 | 0.001 | 26/48 (SW480, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 0.906× | -4.2 | 0.002 | 1/48 (HCT15) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 0.876× | -3.9 | 0.004 | 12/48 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.776×** | -3.9 | 0.004 | 24/48 (CFPAC-1, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.881× | -3.6 | 0.012 | 14/48 (NCI-H2347, NCI-H1573, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.808×** | -3.3 | 0.035 | 18/49 (NCI-H2347, COLO 205, …) | top dose only | noisy plate (z scaled) |
| [[Apalutamide (drug)]] 0.5 µM |  | 0.900× | -3.1 | 0.061 | 10/48 (HOP62, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Mifepristone (drug)]] 0.5 µM |  | 0.901× | -3.1 | 0.067 | 9/48 (A-172, LS 180, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.903× | -3.0 | 0.073 | 11/48 (HOP62, A-172, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.05 µM |  | 0.896× | -3.0 | 0.073 | 4/48 (SW 1088, HOP62, …) | inconsistent across doses |  |
| [[(S)-Crizotinib (drug)]] 0.5 µM |  | 0.904× | -3.0 | 0.075 | 6/48 (A-172, SNU-423, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.904× | -3.0 | 0.075 | 5/48 (C32, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 417. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 179 | 14 (4 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +29.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.44× (z +26.2) | [[Dinaciclib (drug)]] 5 µM 0.355× (z -21.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 167 | 9 (3 ⚠) | 2 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +13.4) | [[Dinaciclib (drug)]] 0.5 µM 0.374× (z -17.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 244 | 7 (1 ⚠) | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.38× (z +14.3) | [[Dinaciclib (drug)]] 0.5 µM 0.248× (z -31.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.564× (z -13.0) |
| [[LoVo (line)]] | wt | 316 | 6 (2 ⚠) | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.27× (z +16.0) | [[Dinaciclib (drug)]] 5 µM 0.230× (z -27.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.611× (z -9.6) |
| [[A549 (line)]] | wt | 250 | 5 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +15.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 1.76× (z +10.9) | [[Dinaciclib (drug)]] 0.05 µM 0.314× (z -21.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.663× (z -11.7) |
| [[MIA PaCa-2 (line)]] | alt | 160 | 5 | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +17.7) | [[Dinaciclib (drug)]] 0.5 µM 0.267× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.480× (z -11.2) |
| [[NCI-H460 (line)]] | wt | 159 | 4 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 1.82× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.324× (z -20.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.639× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 169 | 4 (2 ⚠) | 4 (3 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +10.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.482× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.561× (z -8.5) |
| [[C-33 A (line)]] | alt | 174 | 5 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.40× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.313× (z -15.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 221 | 4 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 1.76× (z +9.6) | [[Dinaciclib (drug)]] 0.05 µM 0.306× (z -18.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 241 | 4 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.08× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.155× (z -29.3) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 211 | 4 (1 ⚠) | 3 (3 ⚠) | [[Digitoxin (drug)]] 5 µM 2.32× (z +12.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.25× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.238× (z -19.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 189 | 3 | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.78× (z +11.3) | [[Dinaciclib (drug)]] 0.05 µM 0.244× (z -18.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.478× (z -10.3) |
| [[A-172 (line)]] | wt | 180 | 3 (2 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +16.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.11× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.322× (z -16.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 158 | 2 | 4 (4 ⚠) | [[Panobinostat (drug)]] 0.5 µM 1.86× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.394× (z -12.2) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 186 | 3 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.72× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.342× (z -12.8) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 121 | 4 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.71× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.401× (z -11.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 181 | 2 (1 ⚠) | 4 (4 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 1.84× (z +9.8) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 2.82× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.290× (z -20.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 226 | 3 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.75× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.181× (z -23.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 170 | 2 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +14.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.07× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.340× (z -14.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 291 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.247× (z -23.7) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 361 | 4 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.88× (z +16.5) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 4.01× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.118× (z -34.6) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 414 | 1 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 4.18× (z +12.6) | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -25.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 359 | 1 | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.61× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.100× (z -40.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 230 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.61× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.205× (z -22.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 298 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.240× (z -26.9) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 187 | 2 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.09× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.223× (z -21.0) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 293 | 2 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.12× (z +10.2) | [[Dinaciclib (drug)]] 0.05 µM 0.195× (z -20.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 266 | 2 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.60× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.203× (z -27.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 120 | 3 (1 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.0815× (z -36.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 282 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.163× (z -18.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 195 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.262× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.478× (z -9.4) |
| [[HOP62 (line)]] | alt | 206 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.286× (z -18.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.398× (z -13.9) |
| [[Hs 766T (line)]] | wt | 184 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.57× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.392× (z -13.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 131 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.57× (z +13.4) | [[Dinaciclib (drug)]] 0.5 µM 0.415× (z -12.4) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 248 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 2.73× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.211× (z -25.3) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 274 | 3 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.92× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -18.1) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 251 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.59× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.311× (z -17.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 257 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.65× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.141× (z -27.5) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 198 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -19.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 193 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.254× (z -20.1) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 237 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.133× (z -14.9) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 226 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.228× (z -20.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 182 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.75× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -13.5) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 241 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.222× (z -10.7) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 206 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.08× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.301× (z -14.0) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 313 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.129× (z -15.0) ⚠ toxic; transcription drop |
| [[NCI-H2122 (line)]] | alt | 285 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 243 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 197 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 417), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 6 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPEPPS]] | +0.72 | +0.77 / +0.64 | both halves | 7e-06 |  |
| [[PAN3]] | +0.72 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[AMBRA1]] | +0.71 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[ELF2]] | +0.69 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[SEC24B]] | +0.68 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[TMEM59]] | +0.67 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[NDUFA2]] | +0.66 | +0.42 / +0.64 | both halves | 4e-05 |  |
| [[LAMTOR2]] | +0.66 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[FBXL20]] | +0.66 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[ATP5PD]] | +0.63 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[RELCH]] | +0.63 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[SMIM27]] | +0.63 | +0.39 / +0.61 | both halves | 6e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THOC6]] | -0.66 | -0.64 / -0.58 | both halves | 7e-06 |  |
| [[TXLNA]] | -0.66 | -0.53 / -0.69 | both halves | 1e-05 |  |
| [[ZNF121]] | -0.63 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[ZNF460]] | -0.62 | -0.45 / -0.66 | both halves | 3e-05 |  |
| [[ZNF587B]] | -0.62 | -0.32 / -0.68 | both halves | 1e-04 |  |
| [[PNO1]] | -0.60 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[RNASEH1]] | -0.58 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[GTF2H3]] | -0.58 | -0.44 / -0.59 | both halves | 3e-05 | pathway: Formation of Incision Complex in GG-NER; STRING 405 |
| [[NOLC1]] | -0.56 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[ELK4]] | -0.56 | -0.57 / -0.46 | both halves | 2e-05 | pathway: HALLMARK_ANDROGEN_RESPONSE |
| [[SNHG26]] | -0.56 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[ZNF202]] | -0.56 | -0.52 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.576). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (0.1, -41.1); signed map (-15.2, 12.4). **Vector** length 118, 43.0% of its response variance represented; |z| ≥ 3 in 1,409 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.6 | +8.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.7 | +5.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +10.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.5 | +14.2 |
|  | [[Sunitinib (drug)]] 5 µM | ⚠ toxic | +3.4 | +2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.2 | +2.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.2 | +1.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.8 | +0.2 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +2.7 | +2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.7 | +1.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -9.9 | -7.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -9.9 | -10.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -8.8 | -2.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.4 | +5.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.2 | -6.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.8 | -4.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.8 | -5.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.7 | -4.2 |
|  | [[EX229 (drug)]] 5 µM |  | -4.3 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | protein inhibitor of activated STAT 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q23 — chr15:68,054,309-68,198,603 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GBP, GU/RH-II, ZMIZ3; previously DDXBP1 |
| Gene groups (HGNC) | Zinc fingers MIZ-type |
| Hallmark sets | ANDROGEN_RESPONSE |
| Reactome | 16 pathways, smallest: Regulation of IFNG signaling; SUMOylation of transcription factors; SUMOylation of intracellular receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [O75925](https://www.uniprot.org/uniprotkb/O75925) (E3 SUMO-protein ligase PIAS1):

> Functions as an E3-type small ubiquitin-like modifier (SUMO) ligase, stabilizing the interaction between UBE2I and the substrate, and as a SUMO-tethering factor. Catalyzes sumoylation of various proteins, such as CEBPB, MRE11, MTA1, PTK2, PML and ZNF76. Plays a crucial role as a transcriptional coregulation in various cellular pathways, including the STAT pathway, the p53 pathway and the steroid hormone signaling pathway. In vitro, binds A/T-rich DNA. The effects of this transcriptional …

**Summary**, from NCBI Gene [8554](https://www.ncbi.nlm.nih.gov/gene/8554):

> This gene encodes a member of the protein inhibitor of activated STAT (PIAS) family. PIAS proteins function as SUMO E3 ligases and play important roles in many cellular processes by mediating the sumoylation of target proteins. This protein plays a central role as a transcriptional coregulator of numerous cellular pathways includign the STAT1 and nuclear factor kappaB pathways. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Mar 2016]

**Accessions** — [HGNC:2752](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2752) · Entrez [8554](https://www.ncbi.nlm.nih.gov/gene/8554) · UniProt [O75925](https://www.uniprot.org/uniprotkb/O75925) · Ensembl [ENSG00000033800](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000033800)

## Data

Gene col 417: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 417); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 417, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 417]; `tensor/DDL_lfc|DDL_z.npy` [417]; `embed/gene_vectors.npy` [417]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 417 or target_col == 417). Every well: [[PIAS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIAS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
