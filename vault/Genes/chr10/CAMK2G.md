---
symbol: "CAMK2G"
type: "gene"
col: 7301
ensembl_id: "ENSG00000148660"
name: "calcium/calmodulin dependent protein kinase II gamma"
location: "10q22.2"
module: 159
arm: "+"
pooled_cpm: 60.09
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 23
n_dd_up_clean: 24
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/159"]
generated_by: "tahoemap"
---

# CAMK2G

*calcium/calmodulin dependent protein kinase II gamma* — 10q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (1 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 3.68× (z +33.2, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.374× (z -35.4, q 0e+00, down in 47 of 49 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDRG3]] (+0.73, fdr 1e-05), [[PACC1]] (+0.70, fdr 7e-06), [[REPS1]] (+0.70, fdr 1e-05); moves opposite to [[LINC01004]] (-0.71, fdr 3e-05), [[ANKRD17-DT]] (-0.70, fdr 2e-04), [[ZNF337-AS1]] (-0.70, fdr 2e-04).
> It is in [[Module 159]], a single-armed module (High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7301.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **3.68×** | +33.2 | 0e+00 | 48/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **3.38×** | +27.9 | 0e+00 | 48/48 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.98×** | +27.9 | 0e+00 | 48/48 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **2.64×** | +24.7 | 0e+00 | 46/48 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.56×** | +23.9 | 0e+00 | 46/48 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.50×** | +23.4 | 0e+00 | 47/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.94×** | +16.9 | 0e+00 | 46/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.27×** | +14.9 | 0e+00 | 45/49 (SW480, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.47×** | +14.0 | 2e-42 | 38/48 (LOX-IMVI, HS-578T, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.56×** | +12.5 | 3e-34 | 42/44 (LS 180, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.61×** | +12.1 | 6e-32 | 41/48 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.47×** | +12.0 | 1e-31 | 42/49 (PANC-1, CFPAC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.29×** | +9.1 | 3e-18 | 36/48 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.35×** | +7.6 | 1e-12 | 33/48 (SW480, C32, …) | all doses, stronger at high dose |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **1.25×** | +5.5 | 1e-06 | 21/48 (NCI-H460, A-172, …) | rises with dose |  |
| [[Brivudine (drug)]] 0.5 µM |  | **1.32×** | +5.0 | 2e-05 | 22/49 (A549, HS-578T, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7301.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.374×** | -35.4 | 0e+00 | 47/49 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.520×** | -23.5 | 0e+00 | 40/48 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.441×** | -20.9 | 0e+00 | 45/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.508×** | -16.6 | 0e+00 | 42/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.531×** | -15.5 | 0e+00 | 36/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.592×** | -13.3 | 1e-38 | 38/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.595×** | -12.7 | 3e-35 | 39/49 (SW48, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.637×** | -11.5 | 1e-28 | 32/47 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.652×** | -10.9 | 7e-26 | 36/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.748×** | -10.5 | 8e-24 | 34/48 (A-427, SNU-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.668×** | -10.3 | 4e-23 | 35/48 (PANC-1, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.670×** | -10.2 | 8e-23 | 32/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.754×** | -10.2 | 1e-22 | 34/48 (SW1417, Panc 03.27, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.744×** | -7.5 | 2e-12 | 28/48 (A-427, HT-29, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.583×** | -7.2 | 2e-11 | 27/49 (NCI-H460, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.773×** | -6.5 | 2e-09 | 23/48 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.788×** | -6.1 | 4e-08 | 27/48 (J82, RKO, …) | rises with dose | cell-cycle shift (explains ~2% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7301. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 65.9 | 9 | 13 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 4.16× (z +20.8) | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -26.7) |
| [[SW480 (line)]] | alt | 51.9 | 8 | 12 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 5.29× (z +24.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -22.6) |
| [[NCI-H460 (line)]] | wt | 50.7 | 8 | 8 | [[Ixazomib citrate (drug)]] 0.5 µM 4.20× (z +18.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -21.5) |
| [[HOP62 (line)]] | alt | 48.7 | 12 (3 ⚠) | 3 | [[Ixazomib citrate (drug)]] 5 µM 7.29× (z +18.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -17.5) |
| [[A-427 (line)]] | wt | 70.6 | 3 (1 ⚠) | 11 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.76× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.27× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -29.9) |
| [[A-172 (line)]] | wt | 81.2 | 7 | 6 | [[Ixazomib citrate (drug)]] 5 µM 3.43× (z +14.9) | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -21.4) |
| [[NCI-H1573 (line)]] | alt | 61.1 | 4 | 9 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 5.04× (z +15.6) | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -20.0) |
| [[HT-29 (line)]] | alt | 90.2 | 6 | 6 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.28× (z +14.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -19.8) |
| [[HS-578T (line)]] | alt | 54.2 | 5 | 6 | [[Ixazomib citrate (drug)]] 5 µM 3.72× (z +12.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.275× (z -17.7) |
| [[LoVo (line)]] | wt | 69.1 | 5 | 6 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.67× (z +17.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -25.8) |
| [[LOX-IMVI (line)]] | wt | 52.3 | 9 | 2 | [[Ixazomib citrate (drug)]] 5 µM 4.79× (z +16.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -14.1) |
| [[SW 900 (line)]] | alt | 53.6 | 6 | 5 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.69× (z +11.6) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.225× (z -12.6) |
| [[C32 (line)]] | wt | 27.4 | 7 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 7.11× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 6.19× (z +13.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -11.7) |
| [[HEC-1-A (line)]] | alt | 121 | 3 | 7 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.21× (z +18.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.284× (z -28.8) |
| [[Hs 766T (line)]] | wt | 45.4 | 6 | 4 | [[Ixazomib citrate (drug)]] 5 µM 4.39× (z +13.2) | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -20.8) |
| [[Panc 03.27 (line)]] | alt | 73.6 | 6 | 4 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.24× (z +12.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.199× (z -25.0) |
| [[SW1417 (line)]] | alt | 92.4 | 6 | 4 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.83× (z +10.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.249× (z -22.9) |
| [[A549 (line)]] | wt | 57.3 | 6 | 3 | [[Ixazomib citrate (drug)]] 5 µM 3.87× (z +13.6) | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -14.2) |
| [[SNU-1 (line)]] | wt | 64.3 | 1 | 8 (2 ⚠) | [[Bortezomib (drug)]] 0.05 µM 4.04× (z +9.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.171× (z -12.7) |
| [[CFPAC-1 (line)]] | alt | 48.6 | 7 | 1 | [[Panobinostat (drug)]] 5 µM 3.90× (z +14.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.460× (z -11.6) |
| [[KATO III (line)]] | alt | 46.8 | 6 | 2 | [[Ixazomib citrate (drug)]] 0.5 µM 4.17× (z +13.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -17.6) |
| [[MIA PaCa-2 (line)]] | alt | 47.7 | 5 | 3 | [[Belinostat (drug)]] 5 µM 3.60× (z +10.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.288× (z -15.0) |
| [[SNU-423 (line)]] | alt | 59.1 | 6 | 2 | [[Ixazomib citrate (drug)]] 5 µM 3.80× (z +12.6) | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -12.5) |
| [[A498 (line)]] | wt | 71.7 | 2 | 5 | [[Bortezomib (drug)]] 0.05 µM 2.70× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -12.3) |
| [[HepG2_C3A (line)]] | wt | 50.0 | 5 | 2 | [[Ixazomib citrate (drug)]] 5 µM 5.60× (z +12.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -11.2) |
| [[hTERT-HPNE (line)]] | wt | 34.8 | 6 | 1 | [[Ixazomib citrate (drug)]] 5 µM 6.17× (z +12.0) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -8.7) |
| [[J82 (line)]] | alt | 48.1 | 4 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.97× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 2.73× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.288× (z -19.0) |
| [[NCI-H1792 (line)]] | alt | 33.0 | 6 | 1 | [[Ixazomib citrate (drug)]] 5 µM 5.42× (z +13.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 45.1 | 3 | 4 | [[Belinostat (drug)]] 5 µM 2.80× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -17.9) |
| [[NCI-H2347 (line)]] | alt | 67.3 | 5 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.01× (z +13.2) | [[Homoharringtonine (drug)]] 5 µM 0.551× (z -10.0) |
| [[RKO (line)]] | wt | 54.5 | 4 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.13× (z +10.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.115× (z -19.3) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -11.6) |
| [[SK-MEL-2 (line)]] | alt | 44.3 | 2 | 5 | [[Ixazomib citrate (drug)]] 0.5 µM 3.21× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.176× (z -19.6) |
| [[SW48 (line)]] | wt | 145 | 3 | 4 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 4.26× (z +15.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.253× (z -20.4) |
| [[H4 (line)]] | wt | 57.4 | 5 | 1 | [[Ixazomib citrate (drug)]] 5 µM 5.83× (z +12.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -8.5) |
| [[LS 180 (line)]] | wt | 119 | 3 | 3 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.97× (z +19.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -22.3) |
| [[NCI-H23 (line)]] | alt | 34.8 | 2 | 4 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 4.57× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -15.2) |
| [[AN3 CA (line)]] | alt | 104 | 1 | 4 | [[Ixazomib citrate (drug)]] 0.5 µM 3.55× (z +8.8) | [[Homoharringtonine (drug)]] 0.5 µM 0.110× (z -15.4) |
| [[AsPC-1 (line)]] | alt | 29.8 | 5 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.79× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 4.12× (z +10.2) | — |
| [[COLO 205 (line)]] | alt | 45.1 | 4 | 1 | [[Ixazomib citrate (drug)]] 5 µM 7.99× (z +15.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.239× (z -14.7) |
| [[HCT15 (line)]] | alt | 60.9 | 2 | 2 | [[Ixazomib citrate (drug)]] 5 µM 3.40× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -10.5) |
| [[RPMI-7951 (line)]] | alt | 46.6 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.09× (z +11.2) | — |
| [[C-33 A (line)]] | alt | 56.6 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -8.7) |
| [[BT-474 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 55.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 57.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7301), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*47 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDRG3]] | +0.73 | +0.79 / +0.53 | both halves | 1e-05 |  |
| [[PACC1]] | +0.70 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[REPS1]] | +0.70 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[ANKRD27]] | +0.69 | +0.62 / +0.43 | both halves | 3e-05 |  |
| [[SLC27A1]] | +0.69 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[WASF3]] | +0.68 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[ARHGAP44]] | +0.68 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[CCDC134]] | +0.67 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[NXPE3]] | +0.67 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[ANKRD39]] | +0.67 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[TSPAN33]] | +0.66 | +0.39 / +0.54 | both halves | 6e-05 |  |
| [[PIK3CB]] | +0.66 | +0.62 / +0.55 | both halves | 1e-05 | pathway: Intracellular signaling by second messengers |

## Genes that move opposite

*53 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01004]] | -0.71 | -0.63 / -0.46 | both halves | 3e-05 |  |
| [[ANKRD17-DT]] | -0.70 | -0.68 / -0.32 | both halves | 2e-04 |  |
| [[ZNF337-AS1]] | -0.70 | -0.64 / -0.30 | both halves | 2e-04 |  |
| [[KRBOX5]] | -0.69 | -0.63 / -0.35 | both halves | 1e-04 |  |
| [[ERCC6L2-AS1]] | -0.68 | -0.59 / -0.30 | both halves | 2e-04 |  |
| [[BCDIN3D]] | -0.68 | -0.60 / -0.40 | both halves | 5e-05 |  |
| [[UBE3B]] | -0.67 | -0.62 / -0.41 | both halves | 4e-05 |  |
| [[MAD2L1-DT]] | -0.67 | -0.56 / -0.31 | both halves | 2e-04 |  |
| [[SENP8]] | -0.67 | -0.60 / -0.33 | both halves | 1e-04 |  |
| [[PBLD]] | -0.67 | -0.52 / -0.32 | both halves | 1e-04 |  |
| [[ARRDC3-AS1]] | -0.67 | -0.60 / -0.28 | both halves | 3e-04 |  |
| [[RFX3-DT]] | -0.66 | -0.60 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises CAMK2G's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ABL1]] | B | ABL1 activity lowers CAMK2G's level | compounds that target ABL1: 4 of 6 raise it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 3.9% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LRRC20]] | B | LRRC20 activity raises CAMK2G's level | lines that do not express LRRC20 (5) vs lines expressing it (45) | 1.56× lower at baseline in the lines without LRRC20 | 0.099 | ⚠ within organs, on part of the lines; also absent: MCM2, MCM10, SEMA4D; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 159]] — High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells; 27 genes; every member is in the + arm (projection on the module's main direction 0.765). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.43; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (2.0, 6.4); signed map (-38.0, -6.1). **Vector** length 156, 54.1% of its response variance represented; |z| ≥ 3 in 1,716 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +16.6 | +33.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +15.2 | +27.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +13.8 | +27.9 |
|  | [[Belinostat (drug)]] 5 µM |  | +10.8 | +24.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +10.2 | +16.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +8.6 | +14.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +8.2 | +12.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +7.9 | +9.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.7 | +14.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -15.6 | -35.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -12.7 | -16.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -12.0 | -10.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -11.8 | -20.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -11.1 | -12.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.4 | -6.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.6 | -7.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.2 | -4.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.6 | -4.9 |

## What is on record

|  |  |
|---|---|
| Name | calcium/calmodulin dependent protein kinase II gamma |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.2 — chr10:73,812,501-73,874,591 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CAMKG |
| Gene groups (HGNC) | CAMK2 family |
| Reactome | 57 pathways, smallest: CREB1 phosphorylation through the activation of CaMKII/CaMKK/CaMKIV cascasde; CaMK IV-mediated phosphorylation of CREB; Ras activation upon Ca2+ influx through NMDA receptor |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13555](https://www.uniprot.org/uniprotkb/Q13555) (Calcium/calmodulin-dependent protein kinase type II subunit gamma):

> Calcium/calmodulin-dependent protein kinase that functions autonomously after Ca(2+)/calmodulin-binding and autophosphorylation, and is involved in sarcoplasmic reticulum Ca(2+) transport in skeletal muscle and may function in dendritic spine and synapse formation and neuronal plasticity. In slow-twitch muscles, is involved in regulation of sarcoplasmic reticulum (SR) Ca(2+) transport and in fast-twitch muscle participates in the control of Ca(2+) release from the SR through phosphorylation of …

**Summary**, from NCBI Gene [818](https://www.ncbi.nlm.nih.gov/gene/818):

> The product of this gene is one of the four subunits of an enzyme which belongs to the serine/threonine protein kinase family, and to the Ca(2+)/calmodulin-dependent protein kinase subfamily. Calcium signaling is crucial for several aspects of plasticity at glutamatergic synapses. In mammalian cells the enzyme is composed of four different chains: alpha, beta, gamma, and delta. The product of this gene is a gamma chain. Many alternatively spliced transcripts encoding different isoforms have …

**Accessions** — [HGNC:1463](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1463) · Entrez [818](https://www.ncbi.nlm.nih.gov/gene/818) · UniProt [Q13555](https://www.uniprot.org/uniprotkb/Q13555) · Ensembl [ENSG00000148660](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148660)

## Data

Gene col 7301: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7301); `tables/drug_effects.parquet` (68 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7301, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7301]; `tensor/DDL_lfc|DDL_z.npy` [7301]; `embed/gene_vectors.npy` [7301]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7301 or target_col == 7301). Every well: [[CAMK2G — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CAMK2G.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
