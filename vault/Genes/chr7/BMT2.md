---
symbol: "BMT2"
type: "gene"
col: 8968
ensembl_id: "ENSG00000164603"
name: "S-adenosylmethionine sensor upstream of mTORC1"
location: "7q31.1"
module: 99
arm: "+"
pooled_cpm: 64.35
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 17
n_dd_up_clean: 11
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/099"]
generated_by: "tahoemap"
---

# BMT2

*S-adenosylmethionine sensor upstream of mTORC1* — 7q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.89× (z +16.1, q 0e+00, up in 45 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.302× (z -25.0, q 0e+00, down in 47 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.478× (z -14.8, q 0e+00, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ASB7]] (+0.72, fdr 7e-06), [[ALKBH5]] (+0.68, fdr 7e-06), [[PLEKHA8]] (+0.67, fdr 1e-05); moves opposite to [[FKRP]] (-0.62, fdr 1e-05), [[YTHDC2]] (-0.61, fdr 7e-06), [[ZC3H7B]] (-0.61, fdr 1e-05).
> It is in [[Module 099]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8968.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.89×** | +16.1 | 0e+00 | 45/49 (NCI-H23, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +13.4 | 1e-38 | 35/49 (MIA PaCa-2, SW1417, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.79×** | +12.1 | 2e-31 | 42/48 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.92×** | +10.9 | 2e-25 | 40/48 (HEC-1-A, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.67×** | +10.7 | 1e-24 | 40/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +10.3 | 8e-23 | 33/48 (MIA PaCa-2, SW1417, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.61×** | +9.9 | 4e-21 | 34/48 (A-172, HEC-1-A, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +9.2 | 4e-18 | 30/50 (SW1417, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.48×** | +8.2 | 2e-14 | 35/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.39×** | +6.0 | 1e-07 | 31/48 (A498, LoVo, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **1.70×** | +5.4 | 4e-06 | 30/49 (HT-29, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.25×** | +4.6 | 2e-04 | 22/48 (LOX-IMVI, LoVo, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.53×** | +4.4 | 6e-04 | 22/44 (RKO, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.20×** | +3.9 | 0.005 | 20/48 (SW1417, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 1.13× | +3.6 | 0.012 | 6/48 (SHP-77, RPMI-7951, …) | rises with dose |  |
| [[Roxadustat (drug)]] 5 µM |  | 1.19× | +3.5 | 0.018 | 17/48 (NCI-H460, AN3 CA, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.18× | +3.4 | 0.025 | 15/47 (A549, LOX-IMVI, …) | rises with dose |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.17× | +3.2 | 0.036 | 7/48 (A549, SK-MEL-2, …) | inconsistent across doses | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.17× | +3.0 | 0.078 | 7/48 (HEC-1-A, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8968.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.302×** | -25.0 | 0e+00 | 47/49 (RKO, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.291×** | -24.7 | 0e+00 | 40/42 (SK-MEL-2, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.489×** | -20.6 | 0e+00 | 39/48 (C32, AsPC-1, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.478×** | -14.8 | 0e+00 | 42/48 (AsPC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.481×** | -14.1 | 5e-43 | 35/45 (HEC-1-A, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.554×** | -12.3 | 9e-33 | 41/48 (C32, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.659×** | -8.4 | 5e-15 | 31/47 (NCI-H460, HCT15, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.718×** | -6.9 | 4e-10 | 29/48 (A498, SW1417, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.585×** | -5.4 | 3e-06 | 35/48 (A498, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~59% of this change | **0.802×** | -4.6 | 2e-04 | 23/48 (MIA PaCa-2, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[EX229 (drug)]] 5 µM |  | **0.646×** | -4.4 | 5e-04 | 21/48 (A498, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | 0.863× | -4.2 | 0.001 | 14/48 (J82, C-33 A, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.671×** | -4.0 | 0.002 | 21/48 (A498, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 0.840× | -3.6 | 0.011 | 18/48 (NCI-H460, A498, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | 0.852× | -3.3 | 0.033 | 22/48 (BT-474, AsPC-1, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **0.723×** | -3.3 | 0.035 | 12/48 (A498, COLO 205, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.855× | -3.3 | 0.036 | 16/47 (SNU-423, A498, …) | all doses, flat |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.752×** | -3.2 | 0.036 | 9/48 (RKO, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.764×** | -3.1 | 0.059 | 9/49 (A498, NCI-H1792, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Mifepristone (drug)]] 0.5 µM |  | 0.863× | -3.1 | 0.060 | 12/48 (LoVo, NCI-H1792, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.900× | -3.0 | 0.064 | 10/48 (NCI-H1573, HCT15, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.752×** | -2.9 | 0.094 | 9/48 (A498, Panc 03.27, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8968. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 63.7 | 4 (1 ⚠) | 5 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.78× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.225× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.426× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 65.3 | 3 | 6 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 7.62× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.228× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.362× (z -10.8) |
| [[C32 (line)]] | wt | 351 | 1 | 7 (5 ⚠) | [[Auranofin (drug)]] 5 µM 2.23× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -25.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.229× (z -18.7) |
| [[MIA PaCa-2 (line)]] | alt | 81.7 | 3 | 5 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +15.5) | [[Dinaciclib (drug)]] 5 µM 0.232× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.422× (z -8.9) |
| [[HT-29 (line)]] | alt | 72.8 | 2 | 5 (4 ⚠) | [[Auranofin (drug)]] 5 µM 2.40× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.0947× (z -23.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.377× (z -10.1) |
| [[NCI-H1573 (line)]] | alt | 65.0 | 1 | 6 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.0914× (z -24.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.297× (z -13.2) |
| [[NCI-H460 (line)]] | wt | 54.6 | 1 | 6 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 5.24× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.177× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.247× (z -15.1) |
| [[PANC-1 (line)]] | alt | 36.4 | 3 | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +12.2) | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -15.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.371× (z -11.7) |
| [[SW1417 (line)]] | alt | 71.6 | 2 | 5 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +15.3) | [[Dinaciclib (drug)]] 5 µM 0.161× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.351× (z -10.9) |
| [[A-172 (line)]] | wt | 60.8 | 2 | 4 (3 ⚠) | [[Auranofin (drug)]] 5 µM 2.91× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.203× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.381× (z -9.9) |
| [[AsPC-1 (line)]] | alt | 33.5 | 1 | 5 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.51× (z +14.2) | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -17.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.136× (z -15.8) |
| [[HOP62 (line)]] | alt | 59.7 | 3 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 8.28× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.302× (z -12.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 59.4 | 3 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.274× (z -13.1) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 50.3 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.156× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.334× (z -9.5) |
| [[NCI-H1792 (line)]] | alt | 71.0 | 1 | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 7.26× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.176× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.368× (z -10.2) |
| [[SNU-423 (line)]] | alt | 96.5 | 1 | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 4.98× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -17.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.450× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 75.7 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 9.77× (z +11.3) | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -17.8) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SW 900 (line)]] | alt | 74.4 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.309× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.312× (z -9.9) |
| [[SW480 (line)]] | alt | 56.3 | 3 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.76× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.366× (z -12.1) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 124 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0343× (z -21.3) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 78.0 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 8.54× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.142× (z -16.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 67.3 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -15.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 85.7 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0641× (z -20.5) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 59.3 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -12.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 50.2 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -12.8) ⚠ cell-cycle shift, explains ~28% of this change |
| [[LoVo (line)]] | wt | 48.6 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +11.7) | [[Niclosamide (olamine) (drug)]] 5 µM 0.350× (z -10.3) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 64.7 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.29× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.172× (z -18.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 50.9 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -16.7) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 45.8 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.88× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.290× (z -9.9) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 62.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0579× (z -13.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 62.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0421× (z -24.5) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 61.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.232× (z -14.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 45.9 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.18× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.354× (z -9.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 36.6 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.190× (z -10.6) |
| [[NCI-H2030 (line)]] | alt | 41.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.455× (z -9.5) ⚠ cell-cycle shift, explains ~28% of this change |
| [[RKO (line)]] | wt | 92.1 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 10.9× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.0853× (z -21.7) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 63.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.329× (z -9.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 127 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0771× (z -27.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 34.1 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.296× (z -9.5) |
| [[H4 (line)]] | wt | 48.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.188× (z -11.4) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 64.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -10.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 57.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -10.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 53.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.141× (z -13.6) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 93.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0896× (z -8.9) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 73.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.271× (z -8.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 74.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 63.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8968), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASB7]] | +0.72 | +0.78 / +0.62 | both halves | 7e-06 |  |
| [[ALKBH5]] | +0.68 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[PLEKHA8]] | +0.67 | +0.74 / +0.54 | both halves | 1e-05 |  |
| [[CTDP1]] | +0.67 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[RELCH]] | +0.67 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[RNF4]] | +0.67 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[GAPVD1]] | +0.66 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[WDR45B]] | +0.65 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[CNOT8]] | +0.65 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[SNHG30]] | +0.64 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[INSIG2]] | +0.63 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[MOSPD3]] | +0.62 | +0.60 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FKRP]] | -0.62 | -0.69 / -0.53 | both halves | 1e-05 |  |
| [[YTHDC2]] | -0.61 | -0.58 / -0.58 | both halves | 7e-06 |  |
| [[ZC3H7B]] | -0.61 | -0.59 / -0.57 | both halves | 1e-05 |  |
| [[POGLUT1]] | -0.60 | -0.58 / -0.66 | both halves | 7e-06 |  |
| [[SRSF6]] | -0.59 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[CELSR3]] | -0.59 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[COA7]] | -0.59 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[THOC6]] | -0.58 | -0.61 / -0.42 | both halves | 4e-05 |  |
| [[SMARCB1]] | -0.57 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[CEP83]] | -0.57 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[TFE3]] | -0.56 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[ST7L]] | -0.56 | -0.61 / -0.58 | both halves | 8e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers BMT2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 099]] — hypoxia; 48 genes; every member is in the + arm (projection on the module's main direction 0.595). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (8.8, -18.0); signed map (-40.3, 23.6). **Vector** length 122, 38.5% of its response variance represented; |z| ≥ 3 in 1,152 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +8.4 | +16.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.9 | +9.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.7 | +10.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +13.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +10.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | +1.8 |
|  | [[Sulfatinib (drug)]] 5 µM |  | +2.1 | +0.2 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | +2.1 | +0.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -14.6 | -20.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -11.2 | -14.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -10.6 | -12.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.3 | -24.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.1 | -25.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.6 | -3.0 |
|  | [[EX229 (drug)]] 5 µM |  | -3.7 | -4.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.2 | -5.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.0 | -4.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.8 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | S-adenosylmethionine sensor upstream of mTORC1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q31.1 — chr7:112,819,147-112,939,875 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp762M126, FLJ31818; previously BMT2, C7orf60 |
| Gene groups (HGNC) | 7BS non-methyltransferases |
| Reactome | 4 pathways, smallest: Amino acids regulate mTORC1; Cellular response to starvation; Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [Q1RMZ1](https://www.uniprot.org/uniprotkb/Q1RMZ1) (S-adenosylmethionine sensor upstream of mTORC1):

> S-adenosyl-L-methionine-binding protein that acts as an inhibitor of mTORC1 signaling via interaction with the GATOR1 and KICSTOR complexes. Acts as a sensor of S-adenosyl-L-methionine to signal methionine sufficiency to mTORC1: in presence of methionine, binds S-adenosyl-L-methionine, leading to disrupt interaction with the GATOR1 and KICSTOR complexes and promote mTORC1 signaling. Upon methionine starvation, S-adenosyl-L-methionine levels are reduced, thereby promoting the association with …

**Summary**, from NCBI Gene [154743](https://www.ncbi.nlm.nih.gov/gene/154743):

> Enables S-adenosyl-L-methionine binding activity. Involved in cellular response to amino acid starvation; cellular response to methionine; and positive regulation of TORC1 signaling. Predicted to be located in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26475](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26475) · Entrez [154743](https://www.ncbi.nlm.nih.gov/gene/154743) · UniProt [Q1RMZ1](https://www.uniprot.org/uniprotkb/Q1RMZ1) · Ensembl [ENSG00000164603](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164603)

## Data

Gene col 8968: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8968); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8968, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8968]; `tensor/DDL_lfc|DDL_z.npy` [8968]; `embed/gene_vectors.npy` [8968]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8968 or target_col == 8968). Every well: [[BMT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BMT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
