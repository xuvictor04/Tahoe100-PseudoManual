---
symbol: "ATR"
type: "gene"
col: 10554
ensembl_id: "ENSG00000175054"
name: "ATR checkpoint kinase"
location: "3q23"
module: 5
arm: "+"
pooled_cpm: 95.45
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 7
n_dd_up_clean: 15
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# ATR

*ATR checkpoint kinase* — 3q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.18× (z +13.6, q 1e-39, up in 43 of 48 measured lines) ⚠ cell-cycle shift, explains ~41% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.54× (z +10.7, q 7e-25, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.757× (z -4.5, q 0.003, down in 24 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.863× (z -3.7, q 0.027, down in 17 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRMT3]] (+0.76, fdr 7e-06), [[LARS2]] (+0.76, fdr 7e-06), [[ALG8]] (+0.71, fdr 7e-06); moves opposite to [[AHDC1]] (-0.67, fdr 1e-05), [[LRP1]] (-0.63, fdr 1e-05), [[CCDC88B]] (-0.60, fdr 3e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[CDA]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 16 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10554.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **2.18×** | +13.6 | 1e-39 | 43/48 (NCI-H2347, A-172, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.12×** | +12.7 | 2e-34 | 45/48 (HOP62, SW480, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.63×** | +12.1 | 3e-31 | 38/49 (CFPAC-1, SNU-423, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.90×** | +11.3 | 2e-27 | 42/48 (NCI-H2347, A-172, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.54×** | +10.7 | 7e-25 | 41/48 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.82×** | +10.5 | 1e-23 | 39/48 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.64×** | +8.7 | 4e-16 | 36/48 (COLO 205, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.66×** | +8.5 | 1e-15 | 36/50 (Panc 03.27, CFPAC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.59×** | +8.1 | 3e-14 | 34/48 (COLO 205, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | **1.60×** | +7.9 | 2e-13 | 39/47 (LOX-IMVI, AsPC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.54×** | +7.6 | 2e-12 | 40/48 (COLO 205, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.54×** | +7.6 | 2e-12 | 31/48 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.52×** | +7.4 | 8e-12 | 40/48 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.41×** | +6.0 | 1e-07 | 29/48 (COLO 205, A549, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.42×** | +5.8 | 2e-07 | 33/48 (NCI-H2347, NCI-H23, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.40×** | +5.4 | 3e-06 | 33/47 (A-427, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.36×** | +5.2 | 6e-06 | 24/48 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.22×** | +4.9 | 3e-05 | 23/48 (NCI-H2347, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.29×** | +4.5 | 2e-04 | 23/48 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.27×** | +4.2 | 8e-04 | 25/48 (LOX-IMVI, NCI-H1573, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.29×** | +4.0 | 0.002 | 26/48 (Hs 766T, NCI-H1573, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.23×** | +3.4 | 0.015 | 21/47 (HEC-1-A, NCI-H2347, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.44×** | +3.3 | 0.019 | 20/49 (NCI-H2347, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | **1.20×** | +2.9 | 0.076 | 9/48 (NCI-H1573, LOX-IMVI, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10554.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.757×** | -4.5 | 0.003 | 24/45 (RKO, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.795×** | -4.0 | 0.010 | 25/49 (A-427, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.795×** | -4.0 | 0.010 | 25/49 (KATO III, CHP-212, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 0.862× | -3.7 | 0.027 | 15/48 (KATO III, LS 180, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.863× | -3.7 | 0.027 | 17/48 (SNU-1, LS 180, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.827×** | -3.4 | 0.071 | 17/48 (NCI-H2030, KATO III, …) | inconsistent across doses |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.828×** | -3.3 | 0.071 | 17/48 (H4, CHP-212, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.830×** | -3.3 | 0.071 | 19/48 (RKO, HEC-1-A, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | **0.833×** | -3.2 | 0.081 | 13/48 (A-427, KATO III, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | 0.716× | -3.1 | 0.12 | 12/48 (SNU-1, SHP-77, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.56 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10554. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 38.4 | 11 (7 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.12× (z +12.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.66× (z +11.1) | — |
| [[COLO 205 (line)]] | alt | 86.5 | 9 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.55× (z +14.0) | — |
| [[NCI-H2347 (line)]] | alt | 50.6 | 8 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +16.8) | — |
| [[Panc 03.27 (line)]] | alt | 107 | 6 (3 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.30× (z +12.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.77× (z +10.7) | — |
| [[HOP62 (line)]] | alt | 61.0 | 5 (5 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.57× (z +13.7) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[A-172 (line)]] | wt | 67.2 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.15× (z +10.6) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[A549 (line)]] | wt | 83.7 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.42× (z +9.2) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.28× (z +8.6) | — |
| [[HEC-1-A (line)]] | alt | 109 | 3 (2 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +9.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 1.99× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.469× (z -10.0) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 120 | 1 (1 ⚠) | 3 (3 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +11.2) ⚠ cell-cycle shift, explains ~29% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.305× (z -13.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 173 | 1 (1 ⚠) | 3 (3 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +10.0) ⚠ cell-cycle shift, explains ~29% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.444× (z -11.5) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 53.4 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +12.6) | — |
| [[Hs 766T (line)]] | wt | 49.7 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +10.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.09× (z +8.6) | — |
| [[HT-29 (line)]] | alt | 90.3 | 3 (2 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +10.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.71× (z +8.8) | — |
| [[LoVo (line)]] | wt | 115 | 2 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.01× (z +8.7) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.05× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.408× (z -10.4) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 102 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +11.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 1.91× (z +8.9) | — |
| [[NCI-H460 (line)]] | wt | 72.8 | 3 (3 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +11.8) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 133 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -13.4) |
| [[SNU-423 (line)]] | alt | 45.5 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.33× (z +12.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 2.23× (z +8.6) | — |
| [[A-427 (line)]] | wt | 182 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.268× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 42.6 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.94× (z +8.9) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[NCI-H1573 (line)]] | alt | 93.4 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 2.40× (z +9.3) | — |
| [[RPMI-7951 (line)]] | alt | 79.6 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.10× (z +9.9) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[SW 900 (line)]] | alt | 51.2 | 2 (2 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.01× (z +10.5) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[SW480 (line)]] | alt | 141 | 2 (2 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +13.6) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[A498 (line)]] | wt | 77.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.521× (z -9.0) |
| [[AN3 CA (line)]] | alt | 109 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.232× (z -9.4) ⚠ transcription drop |
| [[H4 (line)]] | wt | 71.0 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.74× (z +8.9) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[HS-578T (line)]] | alt | 97.5 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.73× (z +11.9) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[LOX-IMVI (line)]] | wt | 69.9 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +8.6) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H1792 (line)]] | alt | 42.6 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.11× (z +12.3) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H23 (line)]] | alt | 176 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.241× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 159 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0932× (z -24.0) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 81.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 153 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 71.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 72.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 55.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 123 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 73.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 62.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 64.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 85.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 83.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 87.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 109 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10554), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRMT3]] | +0.76 | +0.79 / +0.68 | both halves | 7e-06 |  |
| [[LARS2]] | +0.76 | +0.75 / +0.70 | both halves | 7e-06 |  |
| [[ALG8]] | +0.71 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[METTL8]] | +0.70 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[WDR4]] | +0.69 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[TASOR2]] | +0.69 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[LYRM4]] | +0.69 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[ANAPC7]] | +0.69 | +0.78 / +0.63 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[ANAPC1]] | +0.68 | +0.72 / +0.59 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[ENOX2]] | +0.68 | +0.72 / +0.58 | both halves | 7e-06 |  |
| [[TIMM23B-AGAP6]] | +0.68 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[LETM1]] | +0.67 | +0.66 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AHDC1]] | -0.67 | -0.71 / -0.57 | both halves | 1e-05 |  |
| [[LRP1]] | -0.63 | -0.65 / -0.57 | both halves | 1e-05 |  |
| [[CCDC88B]] | -0.60 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[DBP]] | -0.60 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[LINC00674]] | -0.60 | -0.68 / -0.50 | both halves | 1e-05 |  |
| [[PLCD1]] | -0.60 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[FHIP1A]] | -0.60 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[NRTN]] | -0.59 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[ANG]] | -0.59 | -0.66 / -0.49 | both halves | 1e-05 |  |
| [[RAP1GAP]] | -0.59 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[MAST1]] | -0.59 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[RYBP]] | -0.58 | -0.59 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDA]] | B | CDA activity strengthens ATR's drug response | lines that do not express CDA (16) vs lines expressing it (34) | the lines without CDA respond 0.61× as strongly (z diff +1.87); strongest at Belinostat 5 µM: 1.42x vs 2.14x (z diff +3.1) | 0.004 | ⚠ within organs, on part of the lines; also absent: TMEM92, LASTR, KITLG; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers ATR's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SRRM3]] | B | SRRM3 activity weakens ATR's drug response | lines that do not express SRRM3 (17) vs lines expressing it (33) | the lines without SRRM3 respond 1.62× as strongly (z diff -1.71); strongest at Epirubicin (hydrochloride) 5 µM: 2.14x vs 1.45x (z diff -2.6) | 0.046 | ⚠ within organs, on part of the lines; also absent: B4GALNT4, KIF26A, SEPTIN3; maybe low, not absent; artifact flags |
| [[FAR2]] | B | FAR2 activity lowers ATR's level | lines that do not express FAR2 (19) vs lines expressing it (31) | 1.27× higher at baseline in the lines without FAR2 | 0.092 | ⚠ within organs, on part of the lines; also absent: CCN3, MIR155HG, LINC02605; maybe low, not absent |
| [[POLR3E]] | C | POLR3E's natural level weakens ATR's drug response | POLR3E's natural level across 50 lines (lineage-adjusted; a glimpse) | r -0.62, reverse +0.36; direction not clear | 0.063 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.766). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-12.2, -33.2); signed map (-0.1, -50.0). **Vector** length 127, 44.6% of its response variance represented; |z| ≥ 3 in 1,283 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.55 to 13); *ribosome biogenesis* (control, mean cos +0.52 to 6); *tRNA modification in the nucleus and cytosol* (reactome, mean cos +0.51 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +7.5 | +7.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +6.5 | +12.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +6.5 | +8.1 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | +6.3 | +5.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +6.1 | +5.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.1 | +10.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.5 | +4.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.4 | +4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +2.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -8.0 | -3.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -8.0 | -4.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.6 | +4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.1 | -3.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | -4.1 | +2.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -3.8 | -2.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.9 | -3.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.7 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | ATR checkpoint kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q23 — chr3:142,449,007-142,578,733 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FRP1, SCKL, SCKL1, MEC1 |
| Gene groups (HGNC) | Armadillo like helical domain containing; Phosphatidylinositol 3-kinase-related kinase family |
| Reactome | 34 pathways, smallest: Impaired BRCA2 binding to RAD51; Activation of ATR in response to replication stress; Fanconi Anemia Pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13535](https://www.uniprot.org/uniprotkb/Q13535) (Serine/threonine-protein kinase ATR):

> Serine/threonine protein kinase which activates checkpoint signaling upon genotoxic stresses such as ionizing radiation (IR), ultraviolet light (UV), or DNA replication stalling, thereby acting as a DNA damage sensor. Recognizes the substrate consensus sequence [ST]-Q. Phosphorylates BRCA1, CHEK1, MCM2, RAD17, RBBP8, RPA2, SMC1 and p53/TP53, which collectively inhibit DNA replication and mitosis and promote DNA repair, recombination and apoptosis. Phosphorylates 'Ser-139' of histone variant …

**Summary**, from NCBI Gene [545](https://www.ncbi.nlm.nih.gov/gene/545):

> The protein encoded by this gene is a serine/threonine kinase and DNA damage sensor, activating cell cycle checkpoint signaling upon DNA stress. The encoded protein can phosphorylate and activate several proteins involved in the inhibition of DNA replication and mitosis, and can promote DNA repair, recombination, and apoptosis. This protein is also important for fragile site stability and centrosome duplication. Defects in this gene are a cause of Seckel syndrome 1. [provided by RefSeq, Aug …

**Accessions** — [HGNC:882](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:882) · Entrez [545](https://www.ncbi.nlm.nih.gov/gene/545) · UniProt [Q13535](https://www.uniprot.org/uniprotkb/Q13535) · Ensembl [ENSG00000175054](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175054)

## Data

Gene col 10554: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10554); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10554, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10554]; `tensor/DDL_lfc|DDL_z.npy` [10554]; `embed/gene_vectors.npy` [10554]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10554 or target_col == 10554). Every well: [[ATR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
