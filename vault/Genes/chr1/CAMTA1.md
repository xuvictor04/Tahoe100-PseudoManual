---
symbol: "CAMTA1"
type: "gene"
col: 10155
ensembl_id: "ENSG00000171735"
name: "calmodulin binding transcription activator 1"
location: "1p36.31-p36.23"
module: 51
arm: "-"
pooled_cpm: 249.19
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 15
n_dd_up_clean: 21
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# CAMTA1

*calmodulin binding transcription activator 1* — 1p36.31-p36.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.69× (z +16.9, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.466× (z -12.6, q 2e-33, down in 41 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.633× (z -7.8, q 7e-13, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[METRN]] (+0.63, fdr 2e-05), [[HABP4]] (+0.58, fdr 4e-05), [[KAZN]] (+0.57, fdr 2e-05); moves opposite to [[TRMO]] (-0.63, fdr 1e-05), [[FASTKD2]] (-0.62, fdr 1e-05), [[ZNF268]] (-0.58, fdr 2e-05).
> It sits in the **-** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[KAZN]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10155.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.69×** | +16.9 | 0e+00 | 46/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.50×** | +15.7 | 0e+00 | 47/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.46×** | +15.4 | 0e+00 | 47/48 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.44×** | +15.3 | 0e+00 | 44/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.12×** | +12.9 | 5e-36 | 46/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.11×** | +12.8 | 1e-35 | 45/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.99×** | +11.8 | 2e-30 | 45/48 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.57×** | +10.5 | 1e-23 | 33/48 (A549, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.87×** | +10.3 | 3e-23 | 44/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.78×** | +9.5 | 1e-19 | 40/48 (PANC-1, A549, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.32×** | +6.5 | 3e-09 | 33/48 (Panc 03.27, CFPAC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.46×** | +6.4 | 6e-09 | 33/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.44×** | +6.2 | 2e-08 | 34/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +6.0 | 1e-07 | 30/49 (AsPC-1, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.37×** | +5.4 | 3e-06 | 35/48 (LS 180, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.73×** | +4.9 | 3e-05 | 34/49 (C-33 A, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +4.7 | 8e-05 | 31/48 (RKO, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10155.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.466×** | -12.6 | 2e-33 | 41/44 (SNU-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.534×** | -10.8 | 2e-24 | 43/49 (SNU-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.538×** | -10.2 | 3e-22 | 42/47 (SNU-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.633×** | -7.8 | 7e-13 | 46/48 (HS-578T, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.723×** | -7.3 | 2e-11 | 41/48 (HS-578T, SNU-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.697×** | -5.7 | 1e-06 | 32/45 (HS-578T, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.753×** | -4.9 | 1e-04 | 38/48 (NCI-H661, SW 1088, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Darinaparsin (drug)]] 5 µM |  | **0.822×** | -4.5 | 5e-04 | 25/48 (PANC-1, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Apalutamide (drug)]] 0.5 µM |  | **0.811×** | -3.6 | 0.022 | 25/48 (AsPC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.814×** | -3.5 | 0.024 | 27/48 (KATO III, SNU-1, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **0.815×** | -3.5 | 0.024 | 23/48 (NCI-H1792, A-172, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.679×** | -3.5 | 0.025 | 28/47 (CHP-212, SW48, …) | top dose only | noisy plate (z scaled) |
| [[Mifepristone (drug)]] 0.5 µM |  | **0.826×** | -3.3 | 0.048 | 22/48 (NCI-H1573, COLO 205, …) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **0.828×** | -3.2 | 0.052 | 25/48 (SW1417, NCI-H1792, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.702×** | -3.2 | 0.058 | 21/48 (KATO III, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 0.835× | -3.1 | 0.072 | 19/48 (A-172, HS-578T, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.838× | -3.0 | 0.080 | 22/47 (A498, NCI-H2030, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10155. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 265 | 14 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 8.53× (z +23.2) | — |
| [[PANC-1 (line)]] | alt | 194 | 13 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +24.3) | [[Dinaciclib (drug)]] 5 µM 0.523× (z -8.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 218 | 12 (3 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.09× (z +22.7) | [[Dinaciclib (drug)]] 0.5 µM 0.511× (z -10.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 190 | 11 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.79× (z +16.2) | — |
| [[NCI-H23 (line)]] | alt | 425 | 8 (2 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.71× (z +18.0) | [[Dinaciclib (drug)]] 5 µM 0.313× (z -12.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 119 | 10 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.32× (z +19.6) | — |
| [[HOP62 (line)]] | alt | 406 | 7 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.98× (z +15.2) | [[Dinaciclib (drug)]] 5 µM 0.342× (z -11.4) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 571 | 4 | 6 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.51× (z +10.1) | [[Dinaciclib (drug)]] 0.05 µM 0.272× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.426× (z -12.3) |
| [[MIA PaCa-2 (line)]] | alt | 343 | 7 (2 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.08× (z +11.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.303× (z -12.1) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 156 | 9 (2 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 4.80× (z +16.8) | [[Selinexor (drug)]] 5 µM 0.495× (z -10.0) |
| [[SHP-77 (line)]] | alt | 403 | 8 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.62× (z +15.8) | [[Dinaciclib (drug)]] 5 µM 0.397× (z -10.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 786 | 5 (1 ⚠) | 5 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.83× (z +15.8) | [[Dinaciclib (drug)]] 5 µM 0.201× (z -18.2) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.518× (z -10.2) |
| [[SNU-423 (line)]] | alt | 187 | 10 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +18.7) | — |
| [[SW 900 (line)]] | alt | 199 | 9 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.49× (z +15.6) | [[Dinaciclib (drug)]] 5 µM 0.438× (z -9.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 229 | 9 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.22× (z +15.7) | — |
| [[A549 (line)]] | wt | 216 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.47× (z +26.2) | — |
| [[C32 (line)]] | wt | 223 | 8 (2 ⚠) | 1 | [[Panobinostat (drug)]] 0.5 µM 3.15× (z +12.0) | [[Selinexor (drug)]] 5 µM 0.545× (z -8.5) |
| [[Hs 766T (line)]] | wt | 177 | 8 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.91× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.366× (z -10.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 177 | 8 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +17.9) | [[Dinaciclib (drug)]] 5 µM 0.285× (z -12.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 254 | 6 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +14.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.317× (z -11.1) ⚠ toxic · without an alert: [[Selinexor (drug)]] 5 µM 0.493× (z -9.4) |
| [[SW48 (line)]] | wt | 261 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +18.1) | — |
| [[COLO 205 (line)]] | alt | 197 | 8 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 4.13× (z +13.2) | — |
| [[HepG2_C3A (line)]] | wt | 440 | 4 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -12.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 276 | 4 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.48× (z +12.7) | [[Dinaciclib (drug)]] 0.5 µM 0.373× (z -13.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 248 | 6 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +13.6) | [[Dinaciclib (drug)]] 0.5 µM 0.358× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 160 | 8 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.35× (z +14.6) | — |
| [[HEC-1-A (line)]] | alt | 301 | 3 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.48× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.370× (z -14.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 154 | 7 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.74× (z +12.9) | — |
| [[Panc 03.27 (line)]] | alt | 143 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.18× (z +14.7) | [[Dinaciclib (drug)]] 5 µM 0.329× (z -13.7) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 311 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.18× (z +13.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.446× (z -8.8) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 104 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +16.3) | — |
| [[H4 (line)]] | wt | 242 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.16× (z +10.9) | — |
| [[NCI-H1573 (line)]] | alt | 495 | 1 | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.04× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.198× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.298× (z -9.9) |
| [[RPMI-7951 (line)]] | alt | 250 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 3.46× (z +13.5) | — |
| [[SW1417 (line)]] | alt | 183 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.40× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.446× (z -10.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 202 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.373× (z -9.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 326 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.300× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.365× (z -9.2) |
| [[LS 180 (line)]] | wt | 202 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.55× (z +16.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.439× (z -8.7) ⚠ toxic |
| [[A-172 (line)]] | wt | 209 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.336× (z -10.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 195 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.18× (z +11.1) | — |
| [[HT-29 (line)]] | alt | 203 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.55× (z +11.5) | — |
| [[KATO III (line)]] | alt | 152 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.18× (z +15.8) | — |
| [[NCI-H661 (line)]] | alt | 370 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.199× (z -9.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 329 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.275× (z -9.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 266 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +10.5) | — |
| [[SW 1088 (line)]] | alt | 226 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.192× (z -8.9) |
| [[CHP-212 (line)]] | wt | 131 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 284 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 298 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 207 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10155), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METRN]] | +0.63 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[HABP4]] | +0.58 | +0.40 / +0.61 | both halves | 4e-05 |  |
| [[KAZN]] | +0.57 | +0.46 / +0.60 | both halves | 2e-05 |  |
| [[ULK1]] | +0.56 | +0.63 / +0.38 | both halves | 7e-05 |  |
| [[MAP3K3]] | +0.55 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[GPX4]] | +0.54 | +0.33 / +0.53 | both halves | 1e-04 |  |
| [[STK32C]] | +0.53 | +0.52 / +0.39 | both halves | 6e-05 |  |
| [[CBFA2T2]] | +0.53 | +0.63 / +0.27 | both halves | 3e-04 |  |
| [[TMEM256]] | +0.53 | +0.42 / +0.39 | both halves | 5e-05 |  |
| [[WIPI1]] | +0.52 | +0.58 / +0.34 | both halves | 1e-04 |  |
| [[LINC01881]] | +0.51 | +0.57 / +0.38 | both halves | 7e-05 |  |
| [[ELF2]] | +0.51 | +0.56 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*54 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRMO]] | -0.63 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[FASTKD2]] | -0.62 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[ZNF268]] | -0.58 | -0.65 / -0.46 | both halves | 2e-05 |  |
| [[ZNF195]] | -0.58 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[NOL11]] | -0.58 | -0.65 / -0.50 | both halves | 1e-05 |  |
| [[CUL5]] | -0.55 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[MRPS7]] | -0.55 | -0.66 / -0.39 | both halves | 6e-05 |  |
| [[FUNDC1]] | -0.55 | -0.58 / -0.39 | both halves | 5e-05 |  |
| [[ZNF614]] | -0.55 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[TOR1AIP1]] | -0.54 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[GATB]] | -0.54 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[AAR2]] | -0.54 | -0.54 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KAZN]] | B | KAZN activity raises CAMTA1's level | lines that do not express KAZN (5) vs lines expressing it (45) | 1.74× lower at baseline in the lines without KAZN | 0.013 | ⚠ within organs, on part of the lines; also absent: DNAH6, SLC1A4, ENSG00000197332; maybe low, not absent |
| [[C19orf33]] | B | C19orf33 activity lowers CAMTA1's level | lines that do not express C19orf33 (19) vs lines expressing it (31) | 1.44× higher at baseline in the lines without C19orf33 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: KRT80, MISP, AREG |
| [[LINC02885]] | B | LINC02885 activity raises CAMTA1's level | lines that do not express LINC02885 (15) vs lines expressing it (35) | 1.33× lower at baseline in the lines without LINC02885 | 0.068 | ⚠ within organs, on part of the lines; also absent: LINC01399, PCDHB2, ENSG00000258168; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **-** arm (projection on the module's main direction -0.390). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-20.4, 11.4); signed map (-22.1, 13.2). **Vector** length 115, 47.5% of its response variance represented; |z| ≥ 3 in 1,619 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +9.7 | +10.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +8.2 | +6.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.9 | +15.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.6 | +15.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.5 | +3.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.1 | -0.1 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +2.8 | +0.7 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +2.7 | +0.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.6 | -1.3 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -10.3 | -7.8 |
|  | [[Selinexor (drug)]] 5 µM |  | -9.5 | -7.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -8.8 | -10.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.4 | +0.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -6.2 | +2.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -5.2 | -0.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.0 | +3.4 |
|  | [[EX229 (drug)]] 5 µM |  | -4.7 | -2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.0 | -2.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.7 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | calmodulin binding transcription activator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.31-p36.23 — chr1:6,785,454-7,769,706 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0833 |
| Gene groups (HGNC) | IPT domain containing; Calmodulin binding transcription activators |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6Y1](https://www.uniprot.org/uniprotkb/Q9Y6Y1) (Calmodulin-binding transcription activator 1):

> Transcriptional activator.

**Summary**, from NCBI Gene [23261](https://www.ncbi.nlm.nih.gov/gene/23261):

> The protein encoded by this gene contains a CG1 DNA-binding domain, a transcription factor immunoglobulin domain, ankyrin repeats, and calmodulin-binding IQ motifs. The encoded protein is thought to be a transcription factor and may be a tumor suppressor. However, a translocation event is sometimes observed between this gene and the WWTR1 gene, with the resulting WWTR1-CAMTA1 oncoprotein leading to epithelioid hemangioendothelioma, a malignant vascular cancer. [provided by RefSeq, Mar 2017]

**Accessions** — [HGNC:18806](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18806) · Entrez [23261](https://www.ncbi.nlm.nih.gov/gene/23261) · UniProt [Q9Y6Y1](https://www.uniprot.org/uniprotkb/Q9Y6Y1) · Ensembl [ENSG00000171735](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171735)

## Data

Gene col 10155: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10155); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10155, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10155]; `tensor/DDL_lfc|DDL_z.npy` [10155]; `embed/gene_vectors.npy` [10155]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10155 or target_col == 10155). Every well: [[CAMTA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CAMTA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
