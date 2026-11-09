---
symbol: "CLK4"
type: "gene"
col: 3439
ensembl_id: "ENSG00000113240"
name: "CDC like kinase 4"
location: "5q35.3"
module: 28
arm: "+"
pooled_cpm: 33.7
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 16
n_dd_up_clean: 14
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# CLK4

*CDC like kinase 4* — 5q35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.23× (z +43.4, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.417× (z -16.2, q 0e+00, down in 43 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.605× (z -13.2, q 2e-37, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PEX12]] (+0.78, fdr 7e-06), [[COIL]] (+0.76, fdr 7e-06), [[EPC1]] (+0.74, fdr 7e-06); moves opposite to [[TPST2]] (-0.72, fdr 7e-06), [[NIPA2]] (-0.69, fdr 1e-05), [[FAM20B]] (-0.67, fdr 7e-06).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3439.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.23×** | +43.4 | 0e+00 | 48/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.64×** | +23.9 | 0e+00 | 47/48 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.28×** | +21.2 | 0e+00 | 47/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.47×** | +12.1 | 2e-31 | 45/49 (HEC-1-A, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.63×** | +9.1 | 1e-17 | 37/48 (LoVo, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.55×** | +8.1 | 5e-14 | 32/48 (LoVo, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.50×** | +7.6 | 3e-12 | 29/48 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.86×** | +6.0 | 1e-07 | 27/48 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.37×** | +5.8 | 3e-07 | 25/48 (BT-474, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.23×** | +5.4 | 3e-06 | 22/48 (Panc 03.27, SNU-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.32×** | +5.2 | 1e-05 | 21/48 (LoVo, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.25×** | +4.1 | 0.002 | 20/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **1.24×** | +3.8 | 0.006 | 8/48 (HEC-1-A, PANC-1, …) | rises with dose | plate-row cell shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.012 | 11/48 (KATO III, MIA PaCa-2, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 1.14× | +3.5 | 0.015 | 13/48 (A498, SHP-77, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.38×** | +3.1 | 0.062 | 5/48 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.18× | +3.0 | 0.087 | 12/48 (PANC-1, HEC-1-A, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3439.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.417×** | -16.2 | 0e+00 | 43/47 (HOP62, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.423×** | -15.9 | 0e+00 | 47/48 (HEC-1-A, A498, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.461×** | -13.8 | 4e-41 | 32/37 (NCI-H2347, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.605×** | -13.2 | 2e-37 | 41/48 (HS-578T, AsPC-1, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.497×** | -13.0 | 2e-36 | 42/48 (LoVo, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.491×** | -12.2 | 4e-32 | 37/41 (H4, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.531×** | -11.7 | 8e-30 | 43/48 (HEC-1-A, SW 900, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.646×** | -8.1 | 4e-14 | 31/48 (SW 900, SW480, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.654×** | -7.6 | 2e-12 | 34/48 (AN3 CA, SK-MEL-2, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.674×** | -7.0 | 1e-10 | 31/48 (SW 900, AN3 CA, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.688×** | -6.4 | 8e-09 | 30/48 (SW 900, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.727×** | -5.9 | 2e-07 | 28/48 (LoVo, A549, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~65% of this change | **0.789×** | -4.2 | 0.001 | 23/47 (RKO, CFPAC-1, …) | top dose only |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.806×** | -4.0 | 0.003 | 19/48 (SW48, RKO, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **0.813×** | -3.7 | 0.008 | 19/47 (HEC-1-A, COLO 205, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.730×** | -3.1 | 0.075 | 10/48 (A498, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.849× | -3.0 | 0.075 | 11/48 (C32, NCI-H1792, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.893× | -3.0 | 0.089 | 11/48 (LOX-IMVI, A-427, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.848× | -2.9 | 0.094 | 11/47 (H4, HOP62, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3439. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 44.4 | 6 (1 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.55× (z +27.1) | [[Panobinostat (drug)]] 5 µM 0.336× (z -12.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.514× (z -10.6) |
| [[SW 900 (line)]] | alt | 83.0 | 2 | 7 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +17.2) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.254× (z -12.6) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.321× (z -10.9) |
| [[HEC-1-A (line)]] | alt | 43.2 | 5 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.38× (z +26.2) | [[Panobinostat (drug)]] 5 µM 0.251× (z -12.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H2347 (line)]] | alt | 55.4 | 3 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +20.3) | [[Dinaciclib (drug)]] 5 µM 0.215× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.547× (z -8.5) |
| [[A-172 (line)]] | wt | 31.3 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.14× (z +23.2) | [[Belinostat (drug)]] 5 µM 0.291× (z -9.7) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A-427 (line)]] | wt | 36.7 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +18.5) | [[Dinaciclib (drug)]] 5 µM 0.205× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HS-578T (line)]] | alt | 54.9 | 3 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.40× (z +19.3) | [[Dinaciclib (drug)]] 5 µM 0.180× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.323× (z -13.0) |
| [[RKO (line)]] | wt | 39.3 | 3 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.75× (z +19.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.128× (z -14.7) ⚠ toxic; cell-cycle shift, explains ~65% of this change · without an alert: [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.313× (z -8.6) |
| [[A498 (line)]] | wt | 31.4 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.43× (z +28.5) | [[Panobinostat (drug)]] 5 µM 0.267× (z -12.5) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HOP62 (line)]] | alt | 35.9 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.08× (z +22.2) | [[Dinaciclib (drug)]] 0.5 µM 0.190× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[MIA PaCa-2 (line)]] | alt | 31.8 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +14.9) | [[Dinaciclib (drug)]] 0.05 µM 0.260× (z -9.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 60.8 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.31× (z +26.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -8.9) |
| [[SW480 (line)]] | alt | 29.1 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +23.8) | [[Lonafarnib (drug)]] 5 µM 0.103× (z -13.1) ⚠ toxic |
| [[A549 (line)]] | wt | 28.2 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.75× (z +26.1) | [[Dinaciclib (drug)]] 0.05 µM 0.197× (z -12.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 68.4 | 0 | 4 (4 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.109× (z -10.9) ⚠ cell-cycle shift, explains ~33% of this change |
| [[AsPC-1 (line)]] | alt | 24.8 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.34× (z +16.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -11.1) |
| [[CFPAC-1 (line)]] | alt | 30.2 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.54× (z +20.4) | [[Dinaciclib (drug)]] 0.5 µM 0.214× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[hTERT-HPNE (line)]] | wt | 29.7 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.36× (z +17.0) | [[Dinaciclib (drug)]] 5 µM 0.241× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H1573 (line)]] | alt | 27.6 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.78× (z +24.3) | [[Dinaciclib (drug)]] 0.5 µM 0.357× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[NCI-H460 (line)]] | wt | 22.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.50× (z +24.2) | — |
| [[PANC-1 (line)]] | alt | 27.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +36.1) | — |
| [[SK-MEL-2 (line)]] | alt | 30.3 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.70× (z +20.1) | [[Dinaciclib (drug)]] 0.5 µM 0.151× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[H4 (line)]] | wt | 40.5 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.86× (z +15.6) | [[Dinaciclib (drug)]] 0.05 µM 0.0932× (z -13.8) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 42.4 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +13.9) | [[Dinaciclib (drug)]] 5 µM 0.182× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[SBI-0640756 (drug)]] 5 µM 0.0603× (z -11.2) |
| [[KATO III (line)]] | alt | 26.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.88× (z +20.9) | — |
| [[LOX-IMVI (line)]] | wt | 27.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +14.7) | — |
| [[LS 180 (line)]] | wt | 41.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +14.4) | [[Belinostat (drug)]] 5 µM 0.345× (z -8.6) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H1792 (line)]] | alt | 29.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +12.6) | [[Panobinostat (drug)]] 5 µM 0.275× (z -9.0) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SNU-423 (line)]] | alt | 35.4 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.87× (z +23.3) | [[Dinaciclib (drug)]] 5 µM 0.323× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SW1417 (line)]] | alt | 29.1 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.79× (z +19.4) | [[Dinaciclib (drug)]] 0.05 µM 0.282× (z -9.1) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 39.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.09× (z +18.2) | — |
| [[C-33 A (line)]] | alt | 26.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +11.7) | — |
| [[C32 (line)]] | wt | 23.8 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.97× (z +12.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -9.3) |
| [[COLO 205 (line)]] | alt | 33.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.181× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[HepG2_C3A (line)]] | wt | 37.9 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.70× (z +13.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -8.5) |
| [[HT-29 (line)]] | alt | 20.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.17× (z +16.5) | [[Dinaciclib (drug)]] 5 µM 0.209× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H2030 (line)]] | alt | 26.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.10× (z +17.0) | — |
| [[RPMI-7951 (line)]] | alt | 25.4 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +12.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -8.9) |
| [[SNU-1 (line)]] | wt | 46.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +12.4) | [[Dinaciclib (drug)]] 0.05 µM 0.209× (z -10.1) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 21.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.41× (z +15.7) | — |
| [[CHP-212 (line)]] | wt | 34.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.66× (z +9.1) | — |
| [[HCT15 (line)]] | alt | 38.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +12.1) | — |
| [[J82 (line)]] | alt | 20.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.93× (z +19.9) | — |
| [[NCI-H23 (line)]] | alt | 23.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.06× (z +19.0) | — |
| [[SHP-77 (line)]] | alt | 18.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.174× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H2122 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 71.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3439), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PEX12]] | +0.78 | +0.75 / +0.72 | both halves | 7e-06 |  |
| [[COIL]] | +0.76 | +0.78 / +0.66 | both halves | 7e-06 |  |
| [[EPC1]] | +0.74 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[RAD52]] | +0.74 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[C1orf131]] | +0.74 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[NDUFA5]] | +0.73 | +0.83 / +0.69 | both halves | 7e-06 |  |
| [[ZNF226]] | +0.72 | +0.77 / +0.54 | both halves | 1e-05 |  |
| [[SEPSECS]] | +0.72 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[MRFAP1L1]] | +0.72 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[ZNF44]] | +0.72 | +0.78 / +0.66 | both halves | 7e-06 |  |
| [[REPIN1]] | +0.72 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[GORAB]] | +0.71 | +0.71 / +0.74 | both halves | 7e-06 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPST2]] | -0.72 | -0.65 / -0.67 | both halves | 7e-06 |  |
| [[NIPA2]] | -0.69 | -0.68 / -0.55 | both halves | 1e-05 |  |
| [[FAM20B]] | -0.67 | -0.67 / -0.62 | both halves | 7e-06 |  |
| [[BCAP31]] | -0.67 | -0.64 / -0.57 | both halves | 9e-06 |  |
| [[SMG1P2]] | -0.66 | -0.66 / -0.55 | both halves | 1e-05 |  |
| [[NUTF2]] | -0.66 | -0.67 / -0.55 | both halves | 1e-05 |  |
| [[ZNF731P]] | -0.64 | -0.71 / -0.52 | both halves | 1e-05 |  |
| [[CORO7]] | -0.64 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[BUD23]] | -0.62 | -0.43 / -0.65 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises CLK4's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.810). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-29.1, 6.6); signed map (5.5, -19.5). **Vector** length 102, 28.0% of its response variance represented; |z| ≥ 3 in 1,211 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +12.1 | +43.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +10.9 | +21.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +10.8 | +23.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.2 | +7.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +6.6 | +5.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.0 | +3.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.9 | +4.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.2 | +1.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.1 | +2.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.7 | +2.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.2 | -8.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -3.3 | -15.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -2.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -3.2 | -13.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.0 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | -1.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.6 | -2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.2 | -1.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.2 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | CDC like kinase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.3 — chr5:178,602,664-178,630,615 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | CDC like kinases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HAZ1](https://www.uniprot.org/uniprotkb/Q9HAZ1) (Dual specificity protein kinase CLK4):

> Dual specificity kinase acting on both serine/threonine and tyrosine-containing substrates. Phosphorylates serine- and arginine-rich (SR) proteins of the spliceosomal complex and may be a constituent of a network of regulatory mechanisms that enable SR proteins to control RNA splicing. Phosphorylates SRSF1 and SRSF3. Required for the regulation of alternative splicing of MAPT/TAU. Regulates the alternative splicing of tissue factor (F3) pre-mRNA in endothelial cells.

**Summary**, from NCBI Gene [57396](https://www.ncbi.nlm.nih.gov/gene/57396):

> The protein encoded by this gene belongs to the CDC2-like protein kinase (CLK) family. This protein kinase can interact with and phosphorylate the serine- and arginine-rich (SR) proteins, which are known to play an important role in the formation of spliceosomes, and thus may be involved in the regulation of alternative splicing. Studies in the Israeli sand rat Psammomys obesus suggested that the ubiquitin-like 5 (UBL5/BEACON), a highly conserved ubiquitin-like protein, may interact with and …

**Accessions** — [HGNC:13659](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13659) · Entrez [57396](https://www.ncbi.nlm.nih.gov/gene/57396) · UniProt [Q9HAZ1](https://www.uniprot.org/uniprotkb/Q9HAZ1) · Ensembl [ENSG00000113240](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113240)

## Data

Gene col 3439: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3439); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3439, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3439]; `tensor/DDL_lfc|DDL_z.npy` [3439]; `embed/gene_vectors.npy` [3439]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3439 or target_col == 3439). Every well: [[CLK4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLK4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
