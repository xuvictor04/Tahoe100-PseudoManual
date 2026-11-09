---
symbol: "TNFRSF12A"
type: "gene"
col: 108
ensembl_id: "ENSG00000006327"
name: "TNF receptor superfamily member 12A"
location: "16p13.3"
module: 151
arm: "+"
pooled_cpm: 36.19
n_lines_expressing: 49
n_dd_up: 35
n_dd_down: 31
n_dd_up_clean: 20
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/151"]
generated_by: "tahoemap"
---

# TNFRSF12A

*TNF receptor superfamily member 12A* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.63× (z +22.9, q 0e+00, up in 45 of 46 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 6.17× (z +18.5, q 0e+00, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.597× (z -7.7, q 7e-12, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AGO2]] (+0.66, fdr 7e-06), [[CYTOR]] (+0.65, fdr 7e-06), [[BACH1]] (+0.65, fdr 7e-06); moves opposite to [[ASB7]] (-0.65, fdr 7e-06), [[TENT2]] (-0.63, fdr 1e-05), [[COPS4]] (-0.62, fdr 7e-06).
> It is in [[Module 151]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[CCN1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 15 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 108.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **4.63×** | +22.9 | 0e+00 | 45/46 (AsPC-1, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **6.17×** | +18.5 | 0e+00 | 46/47 (NCI-H1573, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **5.65×** | +18.3 | 0e+00 | 45/46 (A-172, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **3.82×** | +14.2 | 1e-43 | 46/47 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **3.37×** | +12.9 | 8e-36 | 44/45 (SW480, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **3.13×** | +12.1 | 1e-31 | 45/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.71×** | +10.5 | 4e-24 | 42/47 (LoVo, SW480, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.49×** | +9.6 | 4e-20 | 43/47 (SW480, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.46×** | +9.5 | 1e-19 | 43/47 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.25×** | +8.2 | 1e-14 | 42/47 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **1.93×** | +7.0 | 2e-10 | 37/43 (A498, NCI-H1792, …) | all doses, flat | composition shift; position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **1.94×** | +6.8 | 6e-10 | 39/46 (HT-29, A-172, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.79×** | +6.2 | 3e-08 | 40/46 (HT-29, SW 900, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.79×** | +6.1 | 3e-08 | 41/47 (HT-29, SW 900, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.74×** | +5.9 | 1e-07 | 35/46 (HS-578T, SW 900, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.58×** | +4.8 | 4e-05 | 33/47 (HT-29, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.59×** | +4.5 | 2e-04 | 27/46 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.35×** | +4.5 | 2e-04 | 31/47 (LS 180, HT-29, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.51×** | +4.4 | 3e-04 | 30/46 (SW480, KATO III, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.71×** | +4.0 | 0.001 | 27/47 (HT-29, LS 180, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **1.48×** | +4.0 | 0.002 | 25/47 (SHP-77, HEC-1-A, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.99×** | +3.8 | 0.003 | 25/47 (NCI-H460, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **1.84×** | +3.4 | 0.015 | 19/43 (LS 180, SW 900, …) | two highest doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 108.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.597×** | -7.7 | 7e-12 | 36/47 (HT-29, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.572×** | -5.9 | 1e-06 | 37/47 (KATO III, HOP62, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.591×** | -5.7 | 2e-06 | 33/47 (SW48, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.583×** | -5.5 | 6e-06 | 28/46 (SW480, NCI-H23, …) | rises with dose | position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.674×** | -5.2 | 2e-05 | 30/47 (SW480, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.643×** | -5.1 | 2e-05 | 29/47 (AsPC-1, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.706×** | -5.0 | 4e-05 | 36/47 (SW480, LoVo, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.714×** | -4.8 | 1e-04 | 33/47 (SW480, NCI-H2347, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.692×** | -4.8 | 1e-04 | 31/47 (SW480, SW48, …) | all doses, flat | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.642×** | -4.7 | 2e-04 | 30/47 (KATO III, LoVo, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.445×** | -4.4 | 5e-04 | 30/46 (RKO, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.453×** | -4.3 | 7e-04 | 26/47 (SW48, AsPC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.752×** | -4.3 | 9e-04 | 20/47 (HEC-1-A, LoVo, …) | rises with dose | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.649×** | -4.2 | 9e-04 | 29/47 (SW480, LoVo, …) | all doses, flat |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.483×** | -4.0 | 0.002 | 26/47 (PANC-1, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.656×** | -4.0 | 0.003 | 27/47 (NCI-H23, SW480, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.693×** | -3.7 | 0.006 | 27/46 (HOP62, HepG2/C3A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.70 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 108. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 32.5 | 9 (5 ⚠) | 7 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.87× (z +14.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 5.80× (z +13.5) | [[Binimetinib (drug)]] 0.5 µM 0.323× (z -10.7) |
| [[KATO III (line)]] | alt | 42.2 | 4 (1 ⚠) | 9 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.11× (z +17.3) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 7.49× (z +13.6) | [[Ponatinib (drug)]] 0.5 µM 0.148× (z -12.9) |
| [[NCI-H460 (line)]] | wt | 28.4 | 10 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.62× (z +17.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 11.9× (z +16.5) | — |
| [[SNU-1 (line)]] | wt | 56.2 | 8 (4 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 8.71× (z +14.5) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.191× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 20.4 | 8 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.60× (z +16.2) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 12.7× (z +12.8) | — |
| [[NCI-H1573 (line)]] | alt | 42.0 | 8 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.51× (z +20.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 15.0× (z +17.6) | — |
| [[AsPC-1 (line)]] | alt | 86.6 | 6 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +23.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 9.14× (z +15.0) | [[Binimetinib (drug)]] 5 µM 0.272× (z -8.7) |
| [[HT-29 (line)]] | alt | 40.9 | 6 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 6.73× (z +18.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.55× (z +13.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.197× (z -16.0) |
| [[LOX-IMVI (line)]] | wt | 36.8 | 6 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +14.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 6.17× (z +12.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -10.3) |
| [[MIA PaCa-2 (line)]] | alt | 24.0 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.70× (z +15.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 12.9× (z +13.7) | [[Adagrasib (drug)]] 0.05 µM 0.549× (z -11.3) ⚠ position not correctable |
| [[A-172 (line)]] | wt | 48.9 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.89× (z +21.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 10.8× (z +17.0) | — |
| [[A-427 (line)]] | wt | 55.5 | 4 (1 ⚠) | 2 | [[Harringtonine (drug)]] 0.5 µM 3.99× (z +10.3) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.354× (z -11.0) |
| [[A498 (line)]] | wt | 43.2 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.78× (z +17.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 7.86× (z +14.1) | — |
| [[HEC-1-A (line)]] | alt | 57.4 | 5 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +10.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.40× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -12.6) |
| [[HOP62 (line)]] | alt | 47.7 | 4 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +13.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 6.54× (z +12.3) | [[Adagrasib (drug)]] 0.05 µM 0.510× (z -15.9) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -9.6) |
| [[PANC-1 (line)]] | alt | 26.7 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.65× (z +19.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 7.05× (z +15.0) | — |
| [[A549 (line)]] | wt | 34.1 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.03× (z +17.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 10.9× (z +14.5) | — |
| [[C32 (line)]] | wt | 27.1 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.87× (z +14.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 11.8× (z +13.1) | — |
| [[CFPAC-1 (line)]] | alt | 34.8 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.77× (z +20.3) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 7.52× (z +12.7) | — |
| [[Hs 766T (line)]] | wt | 24.5 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.68× (z +17.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 8.64× (z +11.4) | — |
| [[NCI-H2030 (line)]] | alt | 34.3 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.92× (z +15.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.66× (z +11.9) | — |
| [[NCI-H23 (line)]] | alt | 36.3 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +11.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.83× (z +9.4) | [[Adagrasib (drug)]] 0.05 µM 0.527× (z -15.5) ⚠ position not correctable |
| [[SW48 (line)]] | wt | 42.1 | 3 (1 ⚠) | 2 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 6.36× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.177× (z -12.4) |
| [[COLO 205 (line)]] | alt | 9.41 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 35.5× (z +16.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 46.7× (z +12.2) | — |
| [[LoVo (line)]] | wt | 22.2 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.29× (z +16.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.80× (z +11.3) | — |
| [[NCI-H1792 (line)]] | alt | 18.9 | 4 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 12.3× (z +13.0) | — |
| [[NCI-H2347 (line)]] | alt | 21.4 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.46× (z +11.1) | — |
| [[RKO (line)]] | wt | 77.4 | 3 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 4.51× (z +11.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -13.6) |
| [[SW 900 (line)]] | alt | 24.5 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.00× (z +13.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 10.7× (z +12.2) | — |
| [[SW1417 (line)]] | alt | 53.5 | 3 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +16.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.40× (z +12.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -10.5) |
| [[BT-474 (line)]] | alt | 46.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.00× (z +12.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.84× (z +10.1) | — |
| [[HCT15 (line)]] | alt | 30.0 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +9.2) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 7.85× (z +8.7) | — |
| [[HS-578T (line)]] | alt | 34.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +10.3) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 5.14× (z +9.4) | — |
| [[hTERT-HPNE (line)]] | wt | 26.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.37× (z +12.2) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 8.48× (z +9.6) | — |
| [[Panc 03.27 (line)]] | alt | 22.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.70× (z +13.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 6.84× (z +10.4) | — |
| [[RPMI-7951 (line)]] | alt | 27.4 | 3 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 8.90× (z +11.2) | — |
| [[SNU-423 (line)]] | alt | 20.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.89× (z +15.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 8.84× (z +10.7) | — |
| [[J82 (line)]] | alt | 48.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +12.2) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.68× (z +11.4) | — |
| [[SK-MEL-2 (line)]] | alt | 53.9 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 5.37× (z +10.6) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.158× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 33.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -9.6) |
| [[HepG2_C3A (line)]] | wt | 54.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +9.7) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H661 (line)]] | alt | 28.6 | 0 | 1 | — | [[Clobetasol propionate (drug)]] 0.5 µM 0.0581× (z -8.7) |
| [[AN3 CA (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.65 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.65 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 108), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGO2]] | +0.66 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[CYTOR]] | +0.65 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[BACH1]] | +0.65 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[PTPN21]] | +0.64 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[PHLDA1]] | +0.64 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[THOC6]] | +0.63 | +0.69 / +0.58 | both halves | 7e-06 | ⚠ same locus (1.6 kb, same strand: neighbours can correlate without regulation) |
| [[TOMM34]] | +0.63 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[FAM83G]] | +0.63 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[MYL12A]] | +0.62 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[TMEM185B]] | +0.62 | +0.58 / +0.64 | both halves | 8e-06 |  |
| [[FOSL1]] | +0.62 | +0.58 / +0.63 | both halves | 8e-06 | STRING 401 |
| [[ZNF674]] | +0.61 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[LINC01204]] | +0.61 | +0.58 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASB7]] | -0.65 | -0.70 / -0.61 | both halves | 7e-06 |  |
| [[TENT2]] | -0.63 | -0.70 / -0.57 | both halves | 1e-05 |  |
| [[COPS4]] | -0.62 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[SNX1]] | -0.61 | -0.65 / -0.67 | both halves | 7e-06 |  |
| [[LAPTM4A]] | -0.60 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[MARCHF6]] | -0.60 | -0.62 / -0.47 | both halves | 2e-05 |  |
| [[NDUFAF7]] | -0.60 | -0.62 / -0.58 | both halves | 7e-06 |  |
| [[TFG]] | -0.60 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[KDELR1]] | -0.59 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[TMEM94]] | -0.59 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[DNASE2]] | -0.59 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[UBE4B]] | -0.59 | -0.63 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCN1]] | B | CCN1 activity raises TNFRSF12A's level | lines that do not express CCN1 (7) vs lines expressing it (43) | 1.99× lower at baseline in the lines without CCN1 | 0.007 | ⚠ within organs, on part of the lines; also absent: CTSL, ENSG00000232295, EBI3 |
| [[CCND1]] | B | CCND1 activity raises TNFRSF12A's level | lines that do not express CCND1 (7) vs lines expressing it (43) | 1.60× lower at baseline in the lines without CCND1 | 0.026 | ⚠ within organs, on part of the lines; also absent: FSTL3, ADAMTSL5; maybe low, not absent |
| [[ITGB1-DT]] | B | ITGB1-DT activity raises TNFRSF12A's level | lines that do not express ITGB1-DT (21) vs lines expressing it (29) | 1.36× lower at baseline in the lines without ITGB1-DT | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000282849, LTBP2, ADTRP; maybe low, not absent |
| [[HOMER3]] | C | HOMER3 activity raises TNFRSF12A's level | lines that do not express HOMER3 (3) vs lines expressing it (47) | 2.07× lower at baseline in the lines without HOMER3 | 0.064 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CHST3, RGS10, ENSG00000290876; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 151]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.697). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (39.7, 9.5); signed map (10.6, 40.9). **Vector** length 123, 45.7% of its response variance represented; |z| ≥ 3 in 1,767 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.9 | +18.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +9.2 | +14.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +8.8 | +22.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.5 | +18.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.1 | +10.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +7.4 | +8.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +5.0 | +6.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.6 | +4.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.0 | +4.5 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -6.9 | -0.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.6 | -1.4 |
|  | [[NG25 (drug)]] 5 µM |  | -5.6 | -4.4 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -4.3 | -5.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | +1.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.0 | -4.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.7 | -2.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.5 | -5.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.3 | -5.2 |

## What is on record

|  |  |
|---|---|
| Name | TNF receptor superfamily member 12A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:3,018,445-3,022,383 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FN14, TweakR, CD266 |
| Gene groups (HGNC) | CD molecules; Tumor necrosis factor receptor superfamily |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING, CHOLESTEROL_HOMEOSTASIS, APOPTOSIS, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 3 pathways, smallest: TNF receptor superfamily (TNFSF) members mediating non-canonical NF-kB pathway; TNFR2 non-canonical NF-kB pathway; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NP84](https://www.uniprot.org/uniprotkb/Q9NP84) (Tumor necrosis factor receptor superfamily member 12A):

> Receptor for TNFSF12/TWEAK. Weak inducer of apoptosis in some cell types. Promotes angiogenesis and the proliferation of endothelial cells. May modulate cellular adhesion to matrix proteins.

**Summary**, from NCBI Gene [51330](https://www.ncbi.nlm.nih.gov/gene/51330):

> Involved in positive regulation of extrinsic apoptotic signaling pathway and regulation of wound healing. Predicted to be located in cell surface; membrane; and ruffle. Predicted to be active in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18152](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18152) · Entrez [51330](https://www.ncbi.nlm.nih.gov/gene/51330) · UniProt [Q9NP84](https://www.uniprot.org/uniprotkb/Q9NP84) · Ensembl [ENSG00000006327](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000006327)

## Data

Gene col 108: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 108); `tables/drug_effects.parquet` (66 rows, flagged included); `relations/gene_relations.parquet` (col_a == 108, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 108]; `tensor/DDL_lfc|DDL_z.npy` [108]; `embed/gene_vectors.npy` [108]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 108 or target_col == 108). Every well: [[TNFRSF12A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TNFRSF12A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
