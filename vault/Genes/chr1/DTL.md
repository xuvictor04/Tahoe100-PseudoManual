---
symbol: "DTL"
type: "gene"
col: 6752
ensembl_id: "ENSG00000143476"
name: "denticleless E3 ubiquitin protein ligase adapter"
location: "1q32.3"
module: 6
arm: "+"
pooled_cpm: 48.07
n_lines_expressing: 50
n_dd_up: 49
n_dd_down: 36
n_dd_up_clean: 19
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 11
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# DTL

*denticleless E3 ubiquitin protein ligase adapter* — 1q32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 49 drug-doses (30 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.94× (z +15.3, q 0e+00, up in 44 of 48 measured lines) ⚠ cell-cycle shift, explains ~48% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.59× (z +6.5, q 2e-09, up in 27 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (12 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.649× (z -8.6, q 7e-15, down in 30 of 48 measured lines) ⚠ cell-cycle shift, explains ~56% of this change. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 0.711× (z -4.9, q 2e-04, down in 21 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EXO1]] (+0.96, fdr 7e-06), [[CDC45]] (+0.94, fdr 7e-06), [[WDR76]] (+0.92, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[E2F2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 49 in all, 30 with an alert ⚠; shown: the 15 strongest and the 14 next strongest without an alert. 49 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 30 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6752.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **2.94×** | +15.3 | 0e+00 | 44/48 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~98% of this change | **2.66×** | +13.8 | 5e-41 | 43/48 (LOX-IMVI, A549, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **2.42×** | +12.5 | 2e-33 | 42/48 (A549, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | **2.36×** | +12.2 | 7e-32 | 41/47 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **2.22×** | +11.3 | 2e-27 | 41/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **2.14×** | +10.8 | 4e-25 | 39/48 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **2.00×** | +9.8 | 8e-21 | 38/48 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~98% of this change | **1.86×** | +8.5 | 2e-15 | 33/48 (HOP62, SW480, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.83×** | +8.2 | 1e-14 | 33/47 (HOP62, SNU-423, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **3.77×** | +7.9 | 1e-13 | 38/48 (LOX-IMVI, J82, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.70×** | +7.5 | 4e-12 | 32/48 (HT-29, SW1417, …) | rises with dose |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.45×** | +7.2 | 3e-11 | 39/48 (HT-29, RKO, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.66×** | +7.2 | 3e-11 | 30/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.67×** | +6.9 | 2e-10 | 30/48 (J82, A549, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.59×** | +6.5 | 2e-09 | 27/48 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.45×** | +5.3 | 3e-06 | 22/48 (LOX-IMVI, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +4.5 | 1e-04 | 22/48 (J82, SW480, …) | rises with dose |  |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +4.5 | 2e-04 | 19/48 (A-427, HOP62, …) | rises with dose | plate-row cell shift |
| [[Gemcitabine (drug)]] 0.05 µM |  | **1.25×** | +4.2 | 4e-04 | 15/48 (SW480, C-33 A, …) | all doses, flat |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.31×** | +3.6 | 0.006 | 17/48 (MIA PaCa-2, A498, …) | inconsistent across doses |  |
| [[Irinotecan (drug)]] 0.5 µM |  | **1.42×** | +3.5 | 0.008 | 11/48 (SW480, HOP62, …) | two highest doses | noisy plate (z scaled) |
| [[Gemcitabine (drug)]] 0.5 µM |  | **1.27×** | +3.4 | 0.011 | 12/48 (SW480, J82, …) | all doses, flat | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.27×** | +3.4 | 0.011 | 13/48 (A-427, HOP62, …) | rises with dose |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | **1.29×** | +3.3 | 0.018 | 16/48 (HT-29, C-33 A, …) | rises with dose |  |
| [[Oxaliplatin (drug)]] 0.5 µM |  | **1.36×** | +3.1 | 0.028 | 9/48 (MIA PaCa-2, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **1.27×** | +3.1 | 0.030 | 15/48 (A-427, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **1.26×** | +3.0 | 0.032 | 12/48 (NCI-H460, RPMI-7951, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **1.25×** | +2.9 | 0.042 | 11/48 (Panc 03.27, A498, …) | inconsistent across doses |  |
| [[Methotrexate (drug)]] 5 µM |  | **1.22×** | +2.8 | 0.062 | 7/48 (SW480, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6752.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.649×** | -8.6 | 7e-15 | 30/48 (A498, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.572×** | -7.3 | 6e-11 | 28/48 (A498, A-172, …) | all doses, stronger at high dose |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.661×** | -5.6 | 5e-06 | 25/48 (RKO, COLO 205, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.711×** | -4.9 | 2e-04 | 21/47 (SK-MEL-2, NCI-H2030, …) | two highest doses | low cells (technical?) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.783×** | -4.8 | 2e-04 | 26/48 (COLO 205, KATO III, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **0.651×** | -4.8 | 2e-04 | 23/48 (A-427, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.735×** | -4.7 | 2e-04 | 24/48 (A-427, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~79% of this change | **0.709×** | -4.6 | 3e-04 | 22/48 (A498, NCI-H460, …) | all doses, stronger at high dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.642×** | -4.5 | 4e-04 | 18/48 (NCI-H460, A-172, …) | rises with dose | noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | **0.799×** | -4.4 | 6e-04 | 20/48 (Panc 03.27, NCI-H23, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.700×** | -4.4 | 6e-04 | 20/48 (A-427, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.732×** | -4.3 | 9e-04 | 22/47 (HEC-1-A, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.810×** | -4.2 | 0.001 | 23/48 (MIA PaCa-2, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Temsirolimus (drug)]] 5 µM |  | **0.807×** | -4.2 | 0.001 | 22/48 (HOP62, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.728×** | -4.2 | 0.001 | 24/47 (AN3 CA, H4, …) | all doses, stronger at high dose |  |
| [[palbociclib (drug)]] 5 µM |  | **0.503×** | -4.1 | 0.001 | 18/47 (MIA PaCa-2, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.505×** | -4.1 | 0.001 | 19/48 (A-427, HEC-1-A, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | **0.754×** | -4.0 | 0.002 | 15/48 (NCI-H23, RKO, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.752×** | -3.9 | 0.003 | 18/47 (HEC-1-A, HOP62, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.824×** | -3.8 | 0.004 | 19/48 (HCT15, RKO, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | **0.828×** | -3.7 | 0.006 | 16/48 (MIA PaCa-2, NCI-H23, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.827×** | -3.7 | 0.006 | 17/48 (HOP62, SHP-77, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.65 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6752. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 69.5 | 0 | 6 (5 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.178× (z -17.1) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.370× (z -9.7) |
| [[J82 (line)]] | alt | 120 | 5 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.413× (z -9.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 64.9 | 4 (4 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.70× (z +13.8) ⚠ cell-cycle shift, explains ~48% of this change | [[Dinaciclib (drug)]] 5 µM 0.299× (z -10.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 70.1 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.135× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.278× (z -13.2) |
| [[HEC-1-A (line)]] | alt | 125 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -13.3) |
| [[A549 (line)]] | wt | 28.8 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.32× (z +12.1) | — |
| [[H4 (line)]] | wt | 38.8 | 1 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.44× (z +9.3) ⚠ cell-cycle shift, explains ~48% of this change | [[Selinexor (drug)]] 5 µM 0.222× (z -9.7) ⚠ cell-cycle shift, explains ~56% of this change |
| [[HOP62 (line)]] | alt | 54.8 | 3 (3 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.11× (z +9.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H23 (line)]] | alt | 65.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -18.0) |
| [[NCI-H460 (line)]] | wt | 59.4 | 1 (1 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.76× (z +9.5) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.279× (z -12.7) ⚠ cell-cycle shift, explains ~56% of this change |
| [[SW480 (line)]] | alt | 63.5 | 3 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.81× (z +11.9) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[A-172 (line)]] | wt | 63.2 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.285× (z -9.9) ⚠ cell-cycle shift, explains ~56% of this change |
| [[C-33 A (line)]] | alt | 80.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.151× (z -13.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 40.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -9.5) |
| [[LOX-IMVI (line)]] | wt | 28.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 4.90× (z +9.3) ⚠ cell-cycle shift, explains ~98% of this change | [[Selinexor (drug)]] 5 µM 0.264× (z -10.9) ⚠ cell-cycle shift, explains ~56% of this change |
| [[MIA PaCa-2 (line)]] | alt | 56.2 | 1 (1 ⚠) | 1 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.36× (z +9.0) ⚠ cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.0937× (z -20.6) |
| [[NCI-H2347 (line)]] | alt | 21.8 | 2 (2 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.84× (z +9.0) ⚠ cell-cycle shift, explains ~98% of this change | — |
| [[AN3 CA (line)]] | alt | 75.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.109× (z -10.0) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 39.8 | 0 | 1 | — | [[Artesunate (drug)]] 0.5 µM 0.0412× (z -9.2) |
| [[LS 180 (line)]] | wt | 21.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.145× (z -12.0) ⚠ cell-cycle shift, explains ~56% of this change |
| [[NCI-H2030 (line)]] | alt | 44.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H661 (line)]] | alt | 59.8 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0820× (z -8.7) |
| [[SHP-77 (line)]] | alt | 152 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.254× (z -12.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 31.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.134× (z -11.4) ⚠ cell-cycle shift, explains ~56% of this change |
| [[SNU-423 (line)]] | alt | 29.6 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 5.78× (z +9.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW 900 (line)]] | alt | 56.5 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.13× (z +8.5) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[SW1417 (line)]] | alt | 31.5 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.33× (z +9.1) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[AsPC-1 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 35.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 70.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 35.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6752), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EXO1]] | +0.96 | +0.95 / +0.94 | both halves | 7e-06 | STRING 901 |
| [[CDC45]] | +0.94 | +0.94 / +0.93 | both halves | 7e-06 | STRING 938 |
| [[WDR76]] | +0.92 | +0.94 / +0.91 | both halves | 7e-06 | same gene group |
| [[MCM10]] | +0.92 | +0.90 / +0.91 | both halves | 7e-06 | STRING 915 |
| [[BLM]] | +0.92 | +0.92 / +0.92 | both halves | 7e-06 | STRING 431 |
| [[RAD54L]] | +0.91 | +0.90 / +0.90 | both halves | 7e-06 | STRING 516 |
| [[WDHD1]] | +0.90 | +0.86 / +0.92 | both halves | 7e-06 | same gene group; STRING 947 |
| [[MELK]] | +0.90 | +0.90 / +0.89 | both halves | 7e-06 | STRING 842 |
| [[POLQ]] | +0.90 | +0.88 / +0.90 | both halves | 7e-06 | STRING 527 |
| [[FANCA]] | +0.90 | +0.90 / +0.88 | both halves | 7e-06 | **novel candidate** |
| [[GINS1]] | +0.90 | +0.88 / +0.90 | both halves | 7e-06 | STRING 513 |
| [[FANCI]] | +0.89 | +0.90 / +0.88 | both halves | 7e-06 | STRING 689 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 6, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F2]] | B | E2F2 activity raises DTL's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 2.07× lower at baseline in the lines without E2F2 | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[MTOR]] | B | MTOR activity raises DTL's level | compounds that target MTOR: 6 of 8 lower it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 6.2% of all compounds | 0.008 | ⚠ off-target possible; 6 compounds; artifact flags |
| [[TCF19]] | B | TCF19 activity raises DTL's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.18× lower at baseline in the lines without TCF19 | 0.020 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[CDC25A]] | B | CDC25A activity raises DTL's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.49× lower at baseline in the lines without CDC25A | 0.026 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers DTL's level | compounds that target TOP2A: 4 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Mitoxantrone) | 80% of the class's compounds vs 8.4% of all compounds | 0.084 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CDCA7]] | B | CDCA7 activity raises DTL's level | lines that do not express CDCA7 (6) vs lines expressing it (44) | 2.02× lower at baseline in the lines without CDCA7 | 0.096 | ⚠ within organs, on part of the lines; also absent: PKMYT1, CHD7, CYP2R1; maybe low, not absent |
| [[DSCC1]] | C | DSCC1 activity raises DTL's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.42× lower at baseline in the lines without DSCC1 | 0.045 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |
| [[CENPP]] | C | CENPP activity raises DTL's level | lines that do not express CENPP (4) vs lines expressing it (46) | 2.34× lower at baseline in the lines without CENPP | 0.050 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ALDH1B1, EID2, ENSG00000284691; maybe low, not absent |
| [[MCM10]] | C | MCM10 activity raises DTL's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 2.50× lower at baseline in the lines without MCM10 | 0.062 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |
| [[PKMYT1]] | C | PKMYT1 activity raises DTL's level | lines that do not express PKMYT1 (3) vs lines expressing it (47) | 2.66× lower at baseline in the lines without PKMYT1 | 0.069 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: AURKB, TCF19, SMARCD3; maybe low, not absent |
| [[ZNF367]] | C | ZNF367 activity raises DTL's level | lines that do not express ZNF367 (4) vs lines expressing it (46) | 2.45× lower at baseline in the lines without ZNF367 | 0.073 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CDC25A; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.937). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-34.9, -45.7); signed map (-38.7, -44.4). **Vector** length 150, 56.3% of its response variance represented; |z| ≥ 3 in 1,702 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.70 to 65); *DNA strand elongation* (reactome, mean cos +0.76 to 28); *DNA Replication* (reactome, mean cos +0.75 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.7 | +5.1 |
|  | [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | +5.3 | +5.9 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.0 | +4.1 |
|  | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | +4.8 | +5.0 |
|  | [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.7 | +4.5 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +3.8 | +3.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.5 | +3.6 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +3.4 | +3.0 |
|  | [[Raltitrexed (drug)]] 0.5 µM |  | +3.2 | +3.3 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +3.2 | +2.4 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~95% of this change | -8.8 | -1.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -8.5 | -4.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | -7.5 | -8.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | -6.5 | -7.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -5.1 | -1.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -4.4 | -2.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -4.2 | -3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.1 | -1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -4.1 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | denticleless E3 ubiquitin protein ligase adapter |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.3 — chr1:212,035,553-212,107,400 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RAMP, L2DTL, DCAF2, CDT2 |
| Gene groups (HGNC) | WD repeat domain containing; DDB1 and CUL4 associated factors; MicroRNA protein coding host genes |
| Reactome | 4 pathways, smallest: Recognition of DNA damage by PCNA-containing replication complex; DNA Damage Bypass; Neddylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZJ0](https://www.uniprot.org/uniprotkb/Q9NZJ0) (Denticleless protein homolog):

> Substrate-specific adapter of a DCX (DDB1-CUL4-X-box) E3 ubiquitin-protein ligase complex required for cell cycle control, DNA damage response and translesion DNA synthesis. The DCX(DTL) complex, also named CRL4(CDT2) complex, mediates the polyubiquitination and subsequent degradation of CDT1, CDKN1A/p21(CIP1), FBH1, KMT5A and SDE2. CDT1 degradation in response to DNA damage is necessary to ensure proper cell cycle regulation of DNA replication. CDKN1A/p21(CIP1) degradation during S phase or …

**Summary**, from NCBI Gene [51514](https://www.ncbi.nlm.nih.gov/gene/51514):

> Contributes to ubiquitin-protein transferase activity. Involved in several processes, including protein ubiquitination; regulation of G2/M transition of mitotic cell cycle; and translesion synthesis. Located in centrosome and nucleoplasm. Part of Cul4A-RING E3 ubiquitin ligase complex and Cul4B-RING E3 ubiquitin ligase complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30288](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30288) · Entrez [51514](https://www.ncbi.nlm.nih.gov/gene/51514) · UniProt [Q9NZJ0](https://www.uniprot.org/uniprotkb/Q9NZJ0) · Ensembl [ENSG00000143476](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143476)

## Data

Gene col 6752: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6752); `tables/drug_effects.parquet` (89 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6752, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6752]; `tensor/DDL_lfc|DDL_z.npy` [6752]; `embed/gene_vectors.npy` [6752]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6752 or target_col == 6752). Every well: [[DTL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DTL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
