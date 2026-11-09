---
symbol: "ASXL1"
type: "gene"
col: 10112
ensembl_id: "ENSG00000171456"
name: "ASXL transcriptional regulator 1"
location: "20q11.21"
module: 51
arm: "+"
pooled_cpm: 211.92
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 18
n_dd_up_clean: 5
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# ASXL1

*ASXL transcriptional regulator 1* — 20q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.72× (z +18.1, q 0e+00, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.427× (z -20.2, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POGZ]] (+0.58, fdr 2e-05), [[ZNF644]] (+0.57, fdr 2e-05), [[PTBP2]] (+0.56, fdr 3e-05); moves opposite to [[DCUN1D2]] (-0.57, fdr 1e-05), [[NIPA1]] (-0.52, fdr 3e-05), [[PPP1R32]] (-0.51, fdr 4e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10112.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.72×** | +18.1 | 0e+00 | 37/48 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.65×** | +11.2 | 1e-26 | 46/49 (PANC-1, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.57×** | +10.3 | 9e-23 | 32/48 (A498, PANC-1, …) | top dose only | cell-cycle shift (explains ~8% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.44×** | +10.2 | 2e-22 | 47/48 (SW480, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.30×** | +5.9 | 4e-07 | 30/47 (LoVo, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.21×** | +4.6 | 5e-04 | 25/48 (PANC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | 1.17× | +3.4 | 0.040 | 17/48 (A498, NCI-H460, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.20× | +3.4 | 0.040 | 21/47 (SW48, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.15× | +3.3 | 0.066 | 19/48 (SNU-1, SHP-77, …) | top dose only |  |
| [[crizotinib (drug)]] 5 µM |  | 1.15× | +3.2 | 0.066 | 12/48 (NCI-H1573, HOP62, …) | top dose only |  |
| [[Pentagastrin (drug)]] 5 µM |  | 1.10× | +3.2 | 0.074 | 0/48 | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10112.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.427×** | -20.2 | 0e+00 | 48/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.454×** | -18.7 | 0e+00 | 48/48 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.588×** | -17.9 | 0e+00 | 47/49 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.462×** | -17.6 | 0e+00 | 40/44 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.476×** | -17.6 | 0e+00 | 48/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.548×** | -14.3 | 4e-44 | 43/49 (SNU-1, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.639×** | -10.2 | 1e-22 | 41/50 (SK-MEL-2, LOX-IMVI, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.660×** | -9.9 | 4e-21 | 44/48 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.666×** | -9.7 | 3e-20 | 42/48 (SNU-423, SK-MEL-2, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.677×** | -8.9 | 3e-17 | 42/48 (NCI-H23, HOP62, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.735×** | -7.3 | 1e-11 | 39/48 (J82, SNU-423, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | **0.743×** | -6.8 | 5e-10 | 36/47 (MIA PaCa-2, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.758×** | -6.2 | 3e-08 | 33/48 (A549, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **0.783×** | -5.4 | 3e-06 | 26/45 (RPMI-7951, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.818×** | -4.8 | 7e-05 | 27/48 (RKO, C-33 A, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.677×** | -4.5 | 3e-04 | 30/49 (SW480, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | 0.905× | -3.4 | 0.022 | 12/48 (A549, SNU-423, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.811×** | -3.2 | 0.041 | 19/47 (Hs 766T, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.763×** | -3.1 | 0.050 | 20/49 (NCI-H23, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 0.917× | -2.9 | 0.086 | 1/49 (NCI-H1573) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 0.876× | -2.9 | 0.090 | 10/47 (LS 180, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.887× | -2.9 | 0.097 | 16/49 (SW1417, NCI-H2347, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10112. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 139 | 6 (2 ⚠) | 8 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +23.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.513× (z -14.3) |
| [[SNU-423 (line)]] | alt | 359 | 3 | 11 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +22.0) | [[Dinaciclib (drug)]] 5 µM 0.260× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.298× (z -16.8) |
| [[NCI-H2347 (line)]] | alt | 160 | 5 | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +24.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -16.2) |
| [[RPMI-7951 (line)]] | alt | 294 | 2 | 10 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +17.1) | [[Dinaciclib (drug)]] 0.5 µM 0.279× (z -18.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.371× (z -14.3) |
| [[SK-MEL-2 (line)]] | alt | 279 | 4 | 8 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +17.8) | [[Dinaciclib (drug)]] 5 µM 0.290× (z -17.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.396× (z -13.8) |
| [[J82 (line)]] | alt | 413 | 4 (1 ⚠) | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +22.8) | [[Panobinostat (drug)]] 5 µM 0.443× (z -13.6) |
| [[PANC-1 (line)]] | alt | 360 | 6 (1 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +28.3) | [[Panobinostat (drug)]] 5 µM 0.405× (z -17.2) |
| [[A549 (line)]] | wt | 154 | 5 (2 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +31.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.394× (z -19.2) |
| [[HOP62 (line)]] | alt | 242 | 1 | 9 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -20.0) |
| [[LOX-IMVI (line)]] | wt | 287 | 0 | 10 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.284× (z -17.9) |
| [[NCI-H23 (line)]] | alt | 219 | 1 | 9 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +14.3) | [[Panobinostat (drug)]] 5 µM 0.313× (z -18.2) |
| [[SW 900 (line)]] | alt | 219 | 2 | 8 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +11.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -13.3) |
| [[HEC-1-A (line)]] | alt | 169 | 2 | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.59× (z +10.4) | [[Panobinostat (drug)]] 5 µM 0.359× (z -16.2) |
| [[NCI-H2030 (line)]] | alt | 317 | 2 | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +11.6) | [[Panobinostat (drug)]] 5 µM 0.350× (z -12.9) |
| [[SW480 (line)]] | alt | 215 | 2 | 7 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 3.30× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.307× (z -22.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.346× (z -21.2) |
| [[A-172 (line)]] | wt | 137 | 3 (1 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +26.1) | [[Dinaciclib (drug)]] 5 µM 0.400× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.545× (z -12.7) |
| [[CFPAC-1 (line)]] | alt | 260 | 1 | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +16.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -20.0) |
| [[MIA PaCa-2 (line)]] | alt | 193 | 2 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +12.7) | [[Panobinostat (drug)]] 5 µM 0.325× (z -16.7) |
| [[A498 (line)]] | wt | 150 | 4 (2 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.30× (z +38.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -13.0) |
| [[C32 (line)]] | wt | 143 | 2 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -12.4) |
| [[HepG2_C3A (line)]] | wt | 372 | 2 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +10.2) | [[Panobinostat (drug)]] 5 µM 0.328× (z -14.8) |
| [[RKO (line)]] | wt | 271 | 1 | 6 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 4.74× (z +10.9) | [[Panobinostat (drug)]] 0.5 µM 0.407× (z -13.0) |
| [[H4 (line)]] | wt | 151 | 1 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -14.6) |
| [[NCI-H1792 (line)]] | alt | 200 | 1 | 5 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.54× (z +12.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.414× (z -17.1) |
| [[Panc 03.27 (line)]] | alt | 170 | 2 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +18.7) | [[Panobinostat (drug)]] 5 µM 0.445× (z -11.9) |
| [[SNU-1 (line)]] | wt | 357 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.178× (z -19.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.357× (z -11.5) |
| [[SW1417 (line)]] | alt | 228 | 1 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.50× (z +9.5) | [[Panobinostat (drug)]] 5 µM 0.451× (z -13.5) |
| [[BT-474 (line)]] | alt | 180 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.429× (z -14.5) |
| [[Hs 766T (line)]] | wt | 301 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.387× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.509× (z -9.7) |
| [[hTERT-HPNE (line)]] | wt | 140 | 2 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +12.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -11.6) |
| [[A-427 (line)]] | wt | 226 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.397× (z -12.0) |
| [[AsPC-1 (line)]] | alt | 155 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.345× (z -12.6) |
| [[HS-578T (line)]] | alt | 147 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +22.1) | [[Dinaciclib (drug)]] 5 µM 0.345× (z -12.3) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 178 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.471× (z -10.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 178 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.247× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.394× (z -11.0) |
| [[CHP-212 (line)]] | wt | 191 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.229× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -9.9) |
| [[COLO 205 (line)]] | alt | 162 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.456× (z -9.3) |
| [[KATO III (line)]] | alt | 137 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.462× (z -10.7) |
| [[LoVo (line)]] | wt | 110 | 1 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 1.97× (z +9.9) ⚠ toxic | [[Dinaciclib (drug)]] 0.5 µM 0.573× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[NCI-H1573 (line)]] | alt | 140 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +18.3) | — |
| [[SW48 (line)]] | wt | 173 | 1 | 1 | [[TAK-901 (drug)]] 0.05 µM 4.44× (z +11.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.455× (z -10.3) |
| [[LS 180 (line)]] | wt | 60.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -12.3) |
| [[SW 1271 (line)]] | alt | 393 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.178× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[AN3 CA (line)]] | alt | 194 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 200 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 181 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 194 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 283 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 172 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10112), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POGZ]] | +0.58 | +0.46 / +0.63 | both halves | 2e-05 |  |
| [[ZNF644]] | +0.57 | +0.46 / +0.63 | both halves | 2e-05 |  |
| [[PTBP2]] | +0.56 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[ZMYM4]] | +0.55 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[SCAF8]] | +0.55 | +0.39 / +0.64 | both halves | 5e-05 |  |
| [[FNBP1P1]] | +0.54 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[PUM1]] | +0.54 | +0.40 / +0.56 | both halves | 5e-05 |  |
| [[EPC2]] | +0.53 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[CYB5RL]] | +0.53 | +0.42 / +0.40 | both halves | 5e-05 |  |
| [[THRAP3]] | +0.53 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[ATF1]] | +0.51 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[SRSF3]] | +0.51 | +0.54 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCUN1D2]] | -0.57 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[NIPA1]] | -0.52 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[PPP1R32]] | -0.51 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[TMEM87B]] | -0.51 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[FAHD2A]] | -0.51 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[GAN]] | -0.51 | -0.46 / -0.58 | both halves | 3e-05 |  |
| [[KXD1]] | -0.49 | -0.54 / -0.34 | both halves | 1e-04 |  |
| [[TIMM10B]] | -0.49 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[BVES]] | -0.48 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[PIGF]] | -0.48 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[MFN1]] | -0.48 | -0.36 / -0.44 | both halves | 9e-05 |  |
| [[TMED7-TICAM2]] | -0.47 | -0.45 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ASXL1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.602). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-26.5, 12.4); signed map (12.8, -33.6). **Vector** length 108, 37.7% of its response variance represented; |z| ≥ 3 in 1,362 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +10.9 | +18.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.7 | +10.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.8 | +11.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | +5.0 | +3.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.7 | +10.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.8 | +0.7 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.3 | -0.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.2 | -0.8 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +2.1 | +1.3 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.9 | +0.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.6 | +0.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.6 | -1.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.4 | +4.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -4.1 | +3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.7 | -9.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.4 | -1.5 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -2.4 | -0.4 |
|  | [[Pemetrexed (drug)]] 0.5 µM |  | -2.0 | -0.8 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -1.9 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | ASXL transcriptional regulator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.21 — chr20:32,358,330-32,439,319 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0978 |
| Reactome | 2 pathways, smallest: UCH proteinases; Deubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IXJ9](https://www.uniprot.org/uniprotkb/Q8IXJ9) (Polycomb group protein ASXL1):

> Probable Polycomb group (PcG) protein involved in transcriptional regulation mediated by ligand-bound nuclear hormone receptors, such as retinoic acid receptors (RARs) and peroxisome proliferator-activated receptor gamma (PPARG). Acts as a coactivator of RARA and RXRA through association with NCOA1. Acts as a corepressor for PPARG and suppresses its adipocyte differentiation-inducing activity (By similarity). Non-catalytic component of the PR-DUB complex, a complex that specifically mediates …

**Summary**, from NCBI Gene [171023](https://www.ncbi.nlm.nih.gov/gene/171023):

> This gene is similar to the Drosophila additional sex combs gene, which encodes a chromatin-binding protein required for normal determination of segment identity in the developing embryo. The protein is a member of the Polycomb group of proteins, which are necessary for the maintenance of stable repression of homeotic and other loci. The protein is thought to disrupt chromatin in localized areas, enhancing transcription of certain genes while repressing the transcription of other genes. The …

**Accessions** — [HGNC:18318](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18318) · Entrez [171023](https://www.ncbi.nlm.nih.gov/gene/171023) · UniProt [Q8IXJ9](https://www.uniprot.org/uniprotkb/Q8IXJ9) · Ensembl [ENSG00000171456](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171456)

## Data

Gene col 10112: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10112); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10112, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10112]; `tensor/DDL_lfc|DDL_z.npy` [10112]; `embed/gene_vectors.npy` [10112]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10112 or target_col == 10112). Every well: [[ASXL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ASXL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
