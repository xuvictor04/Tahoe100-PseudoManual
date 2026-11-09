---
symbol: "USP42"
type: "gene"
col: 2747
ensembl_id: "ENSG00000106346"
name: "ubiquitin specific peptidase 42"
location: "7p22.1"
module: 54
arm: "+"
pooled_cpm: 63.01
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 12
n_dd_up_clean: 9
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# USP42

*ubiquitin specific peptidase 42* — 7p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.78× (z +13.1, q 1e-36, up in 40 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.312× (z -27.5, q 0e+00, down in 38 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 0.717× (z -11.4, q 5e-28, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LIN7B]] (+0.70, fdr 7e-06), [[LSM2]] (+0.65, fdr 1e-05), [[SSNA1]] (+0.64, fdr 4e-05); moves opposite to [[PRKAR1A]] (-0.68, fdr 1e-05), [[EDEM1]] (-0.65, fdr 1e-04), [[EIF4G2]] (-0.61, fdr 2e-05).
> It sits in the **+** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2747.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.78×** | +13.1 | 1e-36 | 40/49 (LoVo, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.61×** | +11.7 | 3e-29 | 41/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.34×** | +10.9 | 2e-25 | 36/48 (MIA PaCa-2, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +10.3 | 1e-22 | 33/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.50×** | +9.9 | 3e-21 | 39/48 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.43×** | +8.9 | 7e-17 | 44/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.43×** | +8.2 | 1e-14 | 38/48 (PANC-1, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.37×** | +7.8 | 5e-13 | 34/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +7.6 | 2e-12 | 30/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +6.6 | 3e-09 | 29/48 (PANC-1, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.22×** | +6.5 | 4e-09 | 25/48 (PANC-1, KATO III, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.26×** | +5.7 | 5e-07 | 24/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.25×** | +5.3 | 4e-06 | 25/48 (BT-474, CFPAC-1, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~2% of this change | **1.20×** | +4.6 | 2e-04 | 22/48 (CFPAC-1, SNU-423, …) | two highest doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.37×** | +4.0 | 0.002 | 20/45 (SNU-423, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.25×** | +4.0 | 0.002 | 21/49 (PANC-1, SNU-423, …) | all doses, flat | noisy plate (z scaled) |
| [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.056 | 4/49 (A-172, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2747.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.312×** | -27.5 | 0e+00 | 38/43 (KATO III, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.361×** | -20.4 | 0e+00 | 44/48 (NCI-H1792, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.520×** | -14.9 | 0e+00 | 31/45 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.717×** | -11.4 | 5e-28 | 38/48 (A-172, NCI-H2347, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.722×** | -10.4 | 3e-23 | 38/48 (AsPC-1, J82, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.646×** | -10.3 | 5e-23 | 38/50 (MIA PaCa-2, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.680×** | -9.1 | 6e-18 | 31/48 (HS-578T, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.787×** | -7.5 | 6e-12 | 29/49 (A-172, A498, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.741×** | -7.4 | 1e-11 | 31/48 (H4, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.809×** | -5.2 | 1e-05 | 24/49 (AsPC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.828×** | -4.6 | 2e-04 | 21/48 (NCI-H1573, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.876× | -4.5 | 4e-04 | 13/48 (AsPC-1, A498, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.794×** | -4.0 | 0.002 | 18/47 (NCI-H23, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 0.864× | -3.6 | 0.013 | 16/48 (A-172, SHP-77, …) | rises with dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.874× | -3.3 | 0.035 | 12/48 (CFPAC-1, SW 1271, …) | inconsistent across doses |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.874× | -3.3 | 0.035 | 15/48 (H4, NCI-H2347, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.877× | -3.2 | 0.043 | 17/48 (AN3 CA, MIA PaCa-2, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.881× | -3.1 | 0.058 | 6/48 (HS-578T, A498, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.883× | -3.0 | 0.071 | 11/48 (SW 1088, CHP-212, …) | rises with dose |  |
| [[Omeprazole (drug)]] 0.05 µM |  | 0.885× | -3.0 | 0.074 | 7/48 (NCI-H2347, HEC-1-A, …) | inconsistent across doses |  |
| [[Simotinib (drug)]] 0.05 µM |  | 0.879× | -2.9 | 0.091 | 16/48 (SW1417, NCI-H23, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2747. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 79.1 | 8 (3 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.40× (z +17.1) | [[Dinaciclib (drug)]] 5 µM 0.165× (z -24.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 61.3 | 3 | 5 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.03× (z +11.0) | [[Dinaciclib (drug)]] 0.05 µM 0.302× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.479× (z -10.7) |
| [[MIA PaCa-2 (line)]] | alt | 78.2 | 1 | 6 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 6.09× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.217× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -11.8) |
| [[A-172 (line)]] | wt | 75.1 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.171× (z -18.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -15.3) |
| [[HS-578T (line)]] | alt | 74.7 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.284× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -12.3) |
| [[LoVo (line)]] | wt | 72.8 | 4 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.55× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.344× (z -14.3) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 54.3 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.195× (z -18.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -13.9) |
| [[BT-474 (line)]] | alt | 84.3 | 2 (1 ⚠) | 3 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.42× (z +9.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.26× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.324× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.527× (z -10.2) |
| [[A498 (line)]] | wt | 79.5 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.197× (z -21.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.467× (z -14.0) |
| [[HEC-1-A (line)]] | alt | 47.4 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.194× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -8.5) |
| [[J82 (line)]] | alt | 40.8 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.279× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.490× (z -9.5) |
| [[KATO III (line)]] | alt | 67.6 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +10.7) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.49× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.0540× (z -30.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 64.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.299× (z -13.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 89.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.235× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.487× (z -11.6) |
| [[C-33 A (line)]] | alt | 80.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.160× (z -16.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 49.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.228× (z -15.9) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 56.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.342× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 94.1 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.94× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.149× (z -19.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 73.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.221× (z -13.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 63.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.247× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -8.5) |
| [[A-427 (line)]] | wt | 76.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.128× (z -25.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 75.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -19.4) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 56.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -14.7) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 77.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -14.3) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 87.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.119× (z -14.9) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 103 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.151× (z -10.3) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 123 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.188× (z -14.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 38.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -11.5) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 46.2 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.446× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 43.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0590× (z -21.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 62.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.345× (z -10.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 43.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.282× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 53.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.471× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H596 (line)]] | alt | 63.8 | 0 | 1 | — | [[Citalopram (hydrobromide) (drug)]] 0.05 µM 0.220× (z -13.0) |
| [[SHP-77 (line)]] | alt | 86.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.312× (z -13.2) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 64.7 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.346× (z -11.2) |
| [[SW 1088 (line)]] | alt | 78.6 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 5 µM 0.0811× (z -8.6) |
| [[SW 1271 (line)]] | alt | 91.1 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.0904× (z -9.9) |
| [[C32 (line)]] | wt | 36.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 58.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 48.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 66.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 59.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 43.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2747), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 9 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIN7B]] | +0.70 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[LSM2]] | +0.65 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[SSNA1]] | +0.64 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[C15orf61]] ⚠ | +0.64 | +0.49 / +0.54 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[PUS3]] | +0.63 | +0.38 / +0.56 | both halves | 7e-05 |  |
| [[MPHOSPH10]] | +0.62 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[TECPR1]] | +0.62 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[POP7]] | +0.61 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[DHX57]] | +0.60 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[MRPL36]] | +0.60 | +0.39 / +0.52 | both halves | 6e-05 |  |
| [[ENKD1]] | +0.60 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[C4orf48]] | +0.60 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[MRPL14]] | +0.60 | +0.42 / +0.50 | both halves | 4e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKAR1A]] | -0.68 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[EDEM1]] | -0.65 | -0.33 / -0.65 | both halves | 1e-04 |  |
| [[EIF4G2]] | -0.61 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[MOB1A]] | -0.59 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[MIR30DHG]] | -0.58 | -0.29 / -0.58 | both halves | 2e-04 |  |
| [[FLNA]] | -0.57 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[LIN7C]] | -0.57 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[DHFR]] | -0.57 | -0.26 / -0.51 | both halves | 3e-04 |  |
| [[M6PR]] | -0.56 | -0.36 / -0.59 | both halves | 9e-05 |  |
| [[SDCBP]] | -0.56 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[HNRNPK]] | -0.56 | -0.52 / -0.39 | both halves | 5e-05 |  |
| [[DDX39B]] | -0.56 | -0.49 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises USP42's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.2% of all compounds | 0.007 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **+** arm (projection on the module's main direction 0.682). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-43.5, -14.6); signed map (-33.5, 4.6). **Vector** length 96.9, 26.4% of its response variance represented; |z| ≥ 3 in 1,109 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~2% of this change | +4.8 | +4.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.1 | +1.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | +2.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | +0.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.1 | +0.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | +0.6 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +2.1 | +2.3 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.0 | -0.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.0 | +0.3 |
|  | [[Bendamustine (drug)]] 5 µM |  | +2.0 | +0.1 |
| fall | [[Selinexor (drug)]] 5 µM |  | -8.6 | -10.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.9 | -10.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -5.6 | -7.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.2 | -11.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.0 | -9.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -2.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.3 | -3.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.0 | -0.9 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -2.0 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin specific peptidase 42 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p22.1 — chr7:6,104,949-6,161,564 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12697 |
| Gene groups (HGNC) | Ubiquitin specific peptidases |
| Reactome | 2 pathways, smallest: Ub-specific processing proteases; Deubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H9J4](https://www.uniprot.org/uniprotkb/Q9H9J4) (Ubiquitin carboxyl-terminal hydrolase 42):

> Deubiquitinating enzyme which may play an important role during spermatogenesis.

**Summary**, from NCBI Gene [84132](https://www.ncbi.nlm.nih.gov/gene/84132):

> Enables cysteine-type deubiquitinase activity. Predicted to be involved in protein deubiquitination; regulation of apoptotic process; and regulation of protein stability. Predicted to be located in nucleoplasm. Predicted to be active in cytosol and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20068](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20068) · Entrez [84132](https://www.ncbi.nlm.nih.gov/gene/84132) · UniProt [Q9H9J4](https://www.uniprot.org/uniprotkb/Q9H9J4) · Ensembl [ENSG00000106346](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106346)

## Data

Gene col 2747: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2747); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2747, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2747]; `tensor/DDL_lfc|DDL_z.npy` [2747]; `embed/gene_vectors.npy` [2747]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2747 or target_col == 2747). Every well: [[USP42 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USP42.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
