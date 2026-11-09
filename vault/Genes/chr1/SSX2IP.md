---
symbol: "SSX2IP"
type: "gene"
col: 3882
ensembl_id: "ENSG00000117155"
name: "SSX family member 2 interacting protein"
location: "1p22.3"
module: 25
arm: "+"
pooled_cpm: 35.91
n_lines_expressing: 49
n_dd_up: 19
n_dd_down: 16
n_dd_up_clean: 8
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# SSX2IP

*SSX family member 2 interacting protein* — 1p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.62× (z +19.4, q 0e+00, up in 39 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.53× (z +12.1, q 7e-32, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.747× (z -8.3, q 7e-14, down in 30 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HLTF]] (+0.71, fdr 7e-06), [[PHF6]] (+0.70, fdr 7e-06), [[ZDHHC21]] (+0.70, fdr 7e-06); moves opposite to [[NOXRED1]] (-0.69, fdr 9e-06), [[PCF11-AS1]] (-0.68, fdr 7e-06), [[EIF3J-DT]] (-0.67, fdr 2e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ADAMTS9-AS2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 14 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3882.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.62×** | +19.4 | 0e+00 | 39/43 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **2.29×** | +16.0 | 0e+00 | 32/38 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.98×** | +13.7 | 1e-40 | 40/47 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.92×** | +13.1 | 4e-37 | 40/47 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.98×** | +12.7 | 9e-35 | 33/41 (HEC-1-A, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.53×** | +12.1 | 7e-32 | 41/47 (NCI-H2347, LOX-IMVI, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.78×** | +11.6 | 2e-29 | 39/47 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.72×** | +10.9 | 1e-25 | 34/47 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.09×** | +7.6 | 3e-12 | 33/47 (AsPC-1, CFPAC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.45×** | +6.4 | 7e-09 | 27/47 (LOX-IMVI, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.36×** | +6.1 | 5e-08 | 25/47 (NCI-H1792, A498, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.33×** | +5.8 | 3e-07 | 21/47 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.31×** | +5.5 | 2e-06 | 21/47 (PANC-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.31×** | +5.2 | 8e-06 | 18/47 (SW480, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.29×** | +5.1 | 1e-05 | 18/46 (LoVo, SW480, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.17× | +4.5 | 3e-04 | 13/47 (PANC-1, RKO, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.23×** | +4.1 | 0.001 | 15/47 (SW48, A-427, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.19× | +3.2 | 0.036 | 10/45 (AsPC-1, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Bentamapimod (drug)]] 5 µM |  | **1.37×** | +3.2 | 0.036 | 2/47 (PANC-1, LoVo) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 1.17× | +3.1 | 0.052 | 3/46 (RKO, SNU-423, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 1.15× | +2.8 | 0.096 | 6/47 (NCI-H1573, Hs 766T, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.16× | +2.8 | 0.096 | 12/47 (NCI-H1573, PANC-1, …) | top dose only |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 1.15× | +2.8 | 0.096 | 4/47 (NCI-H1573, HCT15, …) | all doses, flat |  |
| [[Bentamapimod (drug)]] 0.05 µM |  | 1.16× | +2.8 | 0.096 | 6/46 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 7 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3882.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.747×** | -8.3 | 7e-14 | 30/46 (NCI-H460, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.697×** | -7.3 | 1e-10 | 28/46 (HS-578T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.674×** | -5.7 | 2e-06 | 22/44 (HS-578T, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.755×** | -5.7 | 2e-06 | 21/47 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.757×** | -5.6 | 3e-06 | 23/47 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.762×** | -5.2 | 2e-05 | 16/47 (A498, Hs 766T, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.780×** | -4.7 | 2e-04 | 20/47 (PANC-1, SNU-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.665×** | -4.2 | 0.002 | 17/47 (LoVo, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | 0.863× | -4.2 | 0.002 | 20/47 (CFPAC-1, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.812×** | -3.6 | 0.018 | 14/47 (CHP-212, HS-578T, …) | all doses, flat |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.816×** | -3.5 | 0.023 | 12/44 (SNU-423, SK-MEL-2, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~51% of this change | 0.844× | -3.4 | 0.030 | 12/47 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.718×** | -3.4 | 0.030 | 8/47 (LOX-IMVI, LS 180, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 0.888× | -3.4 | 0.030 | 9/47 (hTERT-HPNE, A498, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.846× | -3.4 | 0.030 | 17/47 (NCI-H1573, SNU-1, …) | rises with dose |  |
| [[Thymol (drug)]] 0.5 µM |  | **0.830×** | -3.2 | 0.046 | 19/44 (HS-578T, Panc 03.27, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 5 µM |  | **0.732×** | -3.2 | 0.046 | 3/47 (SW480, RKO, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | 0.836× | -3.1 | 0.059 | 6/45 (HS-578T, SW 900, …) | rises with dose |  |
| [[Daidzin (drug)]] 5 µM |  | 0.852× | -3.1 | 0.059 | 7/47 (HOP62, LS 180, …) | rises with dose | plate-row cell shift; position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 0.862× | -3.0 | 0.077 | 14/44 (SK-MEL-2, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.812×** | -3.0 | 0.077 | 6/47 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.52 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3882. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 12.6 | 2 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.70× (z +9.2) ⚠ cell-cycle shift, explains ~49% of this change | [[Selinexor (drug)]] 5 µM 0.342× (z -9.0) ⚠ cell-cycle shift, explains ~54% of this change |
| [[NCI-H23 (line)]] | alt | 59.2 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.07× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.498× (z -9.4) |
| [[SW480 (line)]] | alt | 33.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.68× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[A549 (line)]] | wt | 19.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[HOP62 (line)]] | alt | 12.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.40× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[HS-578T (line)]] | alt | 42.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -13.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 38.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 38.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.99× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[NCI-H1573 (line)]] | alt | 19.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 7.77× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | [[Digitoxin (drug)]] 0.5 µM 0.220× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 29.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -10.5) |
| [[PANC-1 (line)]] | alt | 88.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 40.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.32× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | [[Bortezomib (drug)]] 5 µM 0.0867× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 10.8 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.34× (z +8.8) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[C-33 A (line)]] | alt | 93.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.410× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[HEC-1-A (line)]] | alt | 50.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.78× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[HepG2_C3A (line)]] | wt | 10.9 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.103× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 26.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.27× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[Panc 03.27 (line)]] | alt | 29.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.83× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[SHP-77 (line)]] | alt | 59.4 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.159× (z -8.5) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 14.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.56× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[A-172 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 65.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 38.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.77 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 39.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 48.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 58.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 77.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 36.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 77.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 52.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3882), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HLTF]] | +0.71 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[PHF6]] | +0.70 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[ZDHHC21]] | +0.70 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[ICMT]] | +0.68 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[LRRCC1]] | +0.67 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[CDCA7L]] | +0.67 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[PPP5C]] | +0.67 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[DNAJC10]] | +0.66 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[AGPS]] | +0.66 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[HNRNPR]] | +0.66 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[TUBGCP3]] | +0.65 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[NIN]] | +0.64 | +0.65 / +0.55 | both halves | 1e-05 | same gene group; STRING 505 |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOXRED1]] | -0.69 | -0.57 / -0.70 | both halves | 9e-06 |  |
| [[PCF11-AS1]] | -0.68 | -0.59 / -0.61 | both halves | 7e-06 |  |
| [[EIF3J-DT]] | -0.67 | -0.48 / -0.64 | both halves | 2e-05 |  |
| [[UBE2CP5]] | -0.65 | -0.59 / -0.63 | both halves | 7e-06 |  |
| [[UXT]] | -0.63 | -0.58 / -0.66 | both halves | 8e-06 |  |
| [[URM1]] | -0.63 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[SYNRG]] | -0.62 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[SPATC1]] | -0.62 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[DENND6A-AS1]] | -0.62 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[ZNF394]] | -0.62 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[LRRC41]] | -0.62 | -0.46 / -0.63 | both halves | 2e-05 |  |
| [[NGDN]] | -0.62 | -0.43 / -0.57 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAMTS9-AS2]] | B | ADAMTS9-AS2 activity lowers SSX2IP's level | lines that do not express ADAMTS9-AS2 (30) vs lines expressing it (20) | 1.68× higher at baseline in the lines without ADAMTS9-AS2 | 0.044 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ENSG00000233539, NID2 |
| [[ANKRD44]] | B | ANKRD44 activity raises SSX2IP's level | lines that do not express ANKRD44 (6) vs lines expressing it (44) | 1.89× lower at baseline in the lines without ANKRD44 | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000236230, TBC1D19, SSBP2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.598). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-27.1, -35.8); signed map (-17.6, -43.9). **Vector** length 116, 31.5% of its response variance represented; |z| ≥ 3 in 1,135 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.8 | +12.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | +5.3 | +19.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.9 | +7.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.9 | +10.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.8 | +6.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.0 | +4.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | +5.5 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +2.9 | +2.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.2 | -8.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.2 | -0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.9 | -2.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -4.5 | -4.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.2 | -5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.0 | -0.1 |
|  | [[Thymol (drug)]] 0.5 µM |  | -3.6 | -3.2 |
|  | [[Temsirolimus (drug)]] 5 µM |  | -3.3 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | SSX family member 2 interacting protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p22.3 — chr1:84,643,706-84,690,803 (-) |
| Ensembl biotype | protein_coding |
| Also known as | hMsd1 |
| Gene groups (HGNC) | Centriolar satellite proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2D8](https://www.uniprot.org/uniprotkb/Q9Y2D8) (Afadin- and alpha-actinin-binding protein):

> Belongs to an adhesion system, which plays a role in the organization of homotypic, interneuronal and heterotypic cell-cell adherens junctions (AJs). May connect the nectin-afadin and E-cadherin-catenin system through alpha-actinin and may be involved in organization of the actin cytoskeleton at AJs through afadin and alpha-actinin (By similarity). Involved in cell movement: localizes at the leading edge of moving cells in response to PDGF and is required for the formation of the leading edge …

**Summary**, from NCBI Gene [117178](https://www.ncbi.nlm.nih.gov/gene/117178):

> This gene encodes a protein that binds the cancer-testis antigen Synovial Sarcoma X breakpoint 2 protein. The encoded protein may regulate the activity of Synovial Sarcoma X breakpoint 2 protein in malignant cells. Alternate splicing results in multiple transcript variants. A pseudogene of this gene is found on chromosome 3. [provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:16509](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16509) · Entrez [117178](https://www.ncbi.nlm.nih.gov/gene/117178) · UniProt [Q9Y2D8](https://www.uniprot.org/uniprotkb/Q9Y2D8) · Ensembl [ENSG00000117155](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117155)

## Data

Gene col 3882: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3882); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3882, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3882]; `tensor/DDL_lfc|DDL_z.npy` [3882]; `embed/gene_vectors.npy` [3882]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3882 or target_col == 3882). Every well: [[SSX2IP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SSX2IP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
