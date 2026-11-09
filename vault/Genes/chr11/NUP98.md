---
symbol: "NUP98"
type: "gene"
col: 3159
ensembl_id: "ENSG00000110713"
name: "nucleoporin 98 and 96 precursor"
location: "11p15.4"
module: 22
arm: "+"
pooled_cpm: 220.48
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 10
n_dd_up_clean: 12
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# NUP98

*nucleoporin 98 and 96 precursor* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.83× (z +17.9, q 0e+00, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.497× (z -14.1, q 1e-42, down in 42 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.689× (z -7.8, q 7e-13, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PILRB]] (+0.65, fdr 1e-05), [[STIL]] (+0.62, fdr 1e-05), [[VCL]] (+0.57, fdr 1e-05); moves opposite to [[RAB21]] (-0.58, fdr 8e-05), [[ZNF790]] (-0.57, fdr 5e-05), [[ZNF343]] (-0.55, fdr 4e-05).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3159.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.83×** | +17.9 | 0e+00 | 43/48 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.00×** | +14.6 | 1e-45 | 47/48 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.96×** | +14.1 | 4e-43 | 47/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.95×** | +14.0 | 1e-42 | 48/48 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.75×** | +11.8 | 8e-30 | 45/48 (SW480, A-172, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.68×** | +10.8 | 2e-25 | 46/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.66×** | +10.2 | 1e-22 | 43/48 (NCI-H460, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~2% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.61×** | +10.0 | 9e-22 | 44/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.58×** | +9.6 | 5e-20 | 41/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.78×** | +6.3 | 1e-08 | 36/49 (SW480, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.29×** | +5.4 | 3e-06 | 38/48 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.27×** | +5.1 | 2e-05 | 28/47 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.56×** | +4.9 | 5e-05 | 35/48 (SW480, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.26×** | +4.8 | 6e-05 | 30/48 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~20% of this change | **1.26×** | +4.6 | 1e-04 | 25/47 (NCI-H460, COLO 205, …) | top dose only |  |
| [[Pentagastrin (drug)]] 5 µM |  | 1.11× | +3.0 | 0.077 | 1/48 (SNU-1) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3159.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.497×** | -14.1 | 1e-42 | 42/44 (HepG2/C3A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.586×** | -11.2 | 8e-27 | 41/49 (HEC-1-A, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.631×** | -9.0 | 6e-17 | 36/45 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.689×** | -7.8 | 7e-13 | 41/48 (A-427, NCI-H23, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.784×** | -7.2 | 5e-11 | 33/48 (AsPC-1, COLO 205, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.805×** | -6.5 | 1e-08 | 34/48 (AsPC-1, COLO 205, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.742×** | -6.3 | 3e-08 | 38/48 (AN3 CA, COLO 205, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.774×** | -5.4 | 5e-06 | 34/48 (H4, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.863× | -4.4 | 7e-04 | 21/49 (A498, A549, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **0.830×** | -3.9 | 0.005 | 23/48 (A-172, HEC-1-A, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.707×** | -3.8 | 0.007 | 23/49 (PANC-1, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.837× | -3.7 | 0.009 | 19/48 (COLO 205, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.840× | -3.7 | 0.011 | 19/48 (H4, NCI-H23, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.845× | -3.5 | 0.016 | 21/48 (A-172, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.856× | -3.3 | 0.038 | 14/48 (A498, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 0.5 µM |  | 0.860× | -3.2 | 0.052 | 15/48 (Panc 03.27, BT-474, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.861× | -3.1 | 0.055 | 19/48 (RKO, NCI-H1573, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.902× | -3.1 | 0.064 | 16/48 (HOP62, SW1417, …) | top dose only |  |
| [[Neratinib (drug)]] 5 µM |  | 0.868× | -3.0 | 0.084 | 11/48 (C-33 A, SW1417, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.864× | -3.0 | 0.086 | 18/48 (A498, hTERT-HPNE, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3159. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 138 | 16 (4 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +26.2) | [[Dinaciclib (drug)]] 0.05 µM 0.428× (z -12.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 241 | 8 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.68× (z +17.8) | [[Dinaciclib (drug)]] 0.05 µM 0.410× (z -14.9) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 211 | 7 | 3 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.70× (z +12.2) | [[Dinaciclib (drug)]] 0.05 µM 0.428× (z -9.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.480× (z -9.0) |
| [[HOP62 (line)]] | alt | 221 | 5 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +17.6) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.596× (z -10.6) |
| [[LoVo (line)]] | wt | 202 | 6 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.51× (z +13.8) | [[Dinaciclib (drug)]] 5 µM 0.377× (z -14.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 225 | 3 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.535× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.627× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 309 | 5 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +17.3) | [[Dinaciclib (drug)]] 5 µM 0.316× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.603× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 210 | 3 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.360× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.572× (z -9.1) |
| [[Hs 766T (line)]] | wt | 182 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +15.6) | — |
| [[A-172 (line)]] | wt | 151 | 6 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.09× (z +16.4) | [[Dinaciclib (drug)]] 5 µM 0.339× (z -15.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 119 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +15.8) | — |
| [[A498 (line)]] | wt | 386 | 1 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -13.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.661× (z -8.9) |
| [[COLO 205 (line)]] | alt | 210 | 5 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +12.7) | [[Selinexor (drug)]] 5 µM 0.545× (z -9.1) |
| [[LS 180 (line)]] | wt | 176 | 4 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +12.9) | [[Dinaciclib (drug)]] 0.5 µM 0.487× (z -9.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 479 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +13.9) | [[Dinaciclib (drug)]] 0.5 µM 0.429× (z -12.2) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 166 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.27× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.292× (z -12.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 342 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.414× (z -13.0) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 103 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.68× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.455× (z -9.3) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 229 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +14.0) | — |
| [[SW1417 (line)]] | alt | 285 | 3 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.00× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.462× (z -11.6) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 187 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.291× (z -14.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 127 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +15.0) | — |
| [[HS-578T (line)]] | alt | 142 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +12.9) | — |
| [[NCI-H2347 (line)]] | alt | 208 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +12.0) | — |
| [[RPMI-7951 (line)]] | alt | 145 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +13.2) | — |
| [[SK-MEL-2 (line)]] | alt | 157 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +16.5) | — |
| [[BT-474 (line)]] | alt | 124 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.18× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.250× (z -15.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 80.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +15.4) | — |
| [[HT-29 (line)]] | alt | 329 | 2 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.40× (z +11.4) | [[Auranofin (drug)]] 5 µM 0.420× (z -11.4) |
| [[hTERT-HPNE (line)]] | wt | 185 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.261× (z -13.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 213 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.458× (z -9.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 151 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.417× (z -9.4) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 139 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +16.5) | — |
| [[RKO (line)]] | wt | 200 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.389× (z -11.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 273 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.193× (z -18.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.273× (z -15.8) |
| [[C-33 A (line)]] | alt | 232 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.292× (z -13.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 160 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.190× (z -17.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 282 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.413× (z -10.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 192 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.358× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.425× (z -12.0) |
| [[SHP-77 (line)]] | alt | 165 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 2.14× (z +9.3) | [[Auranofin (drug)]] 5 µM 0.434× (z -10.3) |
| [[H4 (line)]] | wt | 228 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.50× (z +9.2) | — |
| [[HCT15 (line)]] | alt | 184 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.414× (z -8.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 215 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 95.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 182 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 267 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 107 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3159), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PILRB]] | +0.65 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[STIL]] | +0.62 | +0.54 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[VCL]] | +0.57 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[CCNF]] | +0.56 | +0.40 / +0.51 | both halves | 4e-05 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[KNL1]] | +0.55 | +0.40 / +0.62 | both halves | 5e-05 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[KIF18B]] | +0.54 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[LINC01572]] | +0.54 | +0.40 / +0.52 | both halves | 5e-05 |  |
| [[KIF2C]] | +0.54 | +0.45 / +0.59 | both halves | 3e-05 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[EML4]] | +0.54 | +0.46 / +0.45 | both halves | 3e-05 | pathway: EML4 and NUDC in mitotic spindle formation; STRING 547 |
| [[SCLT1]] | +0.54 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[NECTIN2]] | +0.53 | +0.59 / +0.32 | both halves | 2e-04 |  |
| [[SAPCD2]] | +0.53 | +0.45 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB21]] | -0.58 | -0.54 / -0.37 | both halves | 8e-05 |  |
| [[ZNF790]] | -0.57 | -0.39 / -0.56 | both halves | 5e-05 |  |
| [[ZNF343]] | -0.55 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[EAF1]] | -0.55 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[ZNF596]] | -0.54 | -0.28 / -0.57 | both halves | 3e-04 |  |
| [[UBE2Q2P1]] | -0.53 | -0.37 / -0.58 | both halves | 9e-05 |  |
| [[THBS4]] | -0.53 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[MIX23]] | -0.53 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[ATP6V1H]] | -0.53 | -0.49 / -0.45 | both halves | 3e-05 | pathway: HIV Infection |
| [[TDP2]] | -0.52 | -0.45 / -0.38 | both halves | 6e-05 |  |
| [[TSTD3]] | -0.52 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[VPS13B-DT]] | -0.52 | -0.27 / -0.56 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.453). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-45.8, -53.2); signed map (-50.6, -36.0). **Vector** length 105, 38.5% of its response variance represented; |z| ≥ 3 in 1,321 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +6.0 | +14.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.0 | +14.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.4 | +11.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.5 | +1.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +3.1 | +10.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.3 | -0.7 |
|  | [[Thymol (drug)]] 5 µM |  | +2.0 | -0.1 |
|  | [[HI-TOPK-032 (drug)]] 0.5 µM |  | +2.0 | -0.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.9 | +1.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -11.0 | -7.8 |
|  | [[Selinexor (drug)]] 5 µM |  | -10.2 | -7.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -6.7 | -6.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.5 | -4.4 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -6.3 | -5.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.5 | -3.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.5 | -6.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.2 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | nucleoporin 98 and 96 precursor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:3,671,083-3,797,792 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NUP96, Nup98-Nup96, Nup98-96, NUP196 |
| Gene groups (HGNC) | Nucleoporins |
| Hallmark sets | G2M_CHECKPOINT |
| Reactome | 85 pathways, smallest: Postmitotic nuclear pore complex (NPC) reformation; IP3 and IP4 transport between cytosol and nucleus; IP6 and IP7 transport between cytosol and nucleus |
| Matched by | ensembl_id |

**Function**, from UniProt [P52948](https://www.uniprot.org/uniprotkb/P52948) (Nuclear pore complex protein Nup98-Nup96):

> Plays a role in the nuclear pore complex (NPC) assembly and/or maintenance. NUP98 and NUP96 are involved in the bidirectional transport across the NPC. May anchor NUP153 and TPR to the NPC. In cooperation with DHX9, plays a role in transcription and alternative splicing activation of a subset of genes. Involved in the localization of DHX9 in discrete intranuclear foci (GLFG-body).; (Microbial infection) Interacts with HIV-1 capsid protein P24 and nucleocapsid protein P7 and may thereby promote …

**Summary**, from NCBI Gene [4928](https://www.ncbi.nlm.nih.gov/gene/4928):

> Nuclear pore complexes (NPCs) regulate the transport of macromolecules between the nucleus and cytoplasm, and are composed of many polypeptide subunits, many of which belong to the nucleoporin family. This gene belongs to the nucleoporin gene family and encodes a 186 kDa precursor protein that undergoes autoproteolytic cleavage to generate a 98 kDa nucleoporin and 96 kDa nucleoporin. The 98 kDa nucleoporin contains a Gly-Leu-Phe-Gly (GLGF) repeat domain and participates in many cellular …

**Accessions** — [HGNC:8068](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8068) · Entrez [4928](https://www.ncbi.nlm.nih.gov/gene/4928) · UniProt [P52948](https://www.uniprot.org/uniprotkb/P52948) · Ensembl [ENSG00000110713](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110713)

## Data

Gene col 3159: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3159); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3159, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3159]; `tensor/DDL_lfc|DDL_z.npy` [3159]; `embed/gene_vectors.npy` [3159]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3159 or target_col == 3159). Every well: [[NUP98 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUP98.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
