---
symbol: "CKS2"
type: "gene"
col: 4466
ensembl_id: "ENSG00000123975"
name: "CDC28 protein kinase regulatory subunit 2"
location: "9q22.2"
module: 22
arm: "+"
pooled_cpm: 38.91
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 4
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# CKS2

*CDC28 protein kinase regulatory subunit 2* — 9q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (18 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.36× (z +16.3, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.610× (z -4.6, q 0.003, down in 24 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 0.5 µM: 0.692× (z -3.5, q 0.056, down in 28 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 2 lines (H4 0.214×, A-427 0.351×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A-427 0.219×, C-33 A 0.207×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.542×; ⚠ position not correctable); [[Clofarabine (drug)]] 5 µM in 1 line (SW 1271 0.0514×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM83D]] (+0.72, fdr 7e-06), [[SGO2]] (+0.67, fdr 7e-06), [[PIMREG]] (+0.67, fdr 7e-06); moves opposite to [[ATAD1]] (-0.55, fdr 7e-05), [[TYW5]] (-0.53, fdr 6e-05), [[NBDY]] (-0.52, fdr 1e-04).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 18 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4466.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.36×** | +16.3 | 0e+00 | 47/48 (AsPC-1, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **3.54×** | +12.0 | 6e-31 | 47/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.76×** | +9.7 | 8e-20 | 45/48 (SK-MEL-2, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **2.70×** | +9.4 | 5e-19 | 47/47 (KATO III, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **2.78×** | +9.4 | 8e-19 | 42/47 (NCI-H460, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **2.01×** | +9.4 | 8e-19 | 34/48 (PANC-1, A549, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **2.09×** | +7.0 | 2e-10 | 41/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **2.05×** | +6.8 | 6e-10 | 43/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.11×** | +6.8 | 6e-10 | 38/48 (HEC-1-A, A-172, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.78×** | +5.5 | 2e-06 | 36/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.77×** | +5.4 | 3e-06 | 35/48 (RKO, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **2.77×** | +5.1 | 2e-05 | 37/48 (KATO III, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.69×** | +5.0 | 3e-05 | 34/48 (SW480, RKO, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.63×** | +4.6 | 1e-04 | 32/48 (KATO III, A498, …) | two highest doses | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.65×** | +4.6 | 2e-04 | 29/48 (PANC-1, A549, …) | top dose only | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.06×** | +3.6 | 0.009 | 24/48 (HEC-1-A, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **1.45×** | +3.4 | 0.021 | 22/48 (A549, NCI-H460, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +2.9 | 0.082 | 23/48 (HOP62, BT-474, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.37×** | +2.9 | 0.094 | 24/47 (NCI-H460, A549, …) | rises with dose | position effect removed |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **1.24×** | +2.8 | 0.094 | 18/48 (SNU-423, NCI-H2030, …) | rises with dose | position effect removed |
| [[Gefitinib (drug)]] 5 µM |  | **1.35×** | +2.8 | 0.099 | 17/48 (NCI-H460, hTERT-HPNE, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4466.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 2 lines (H4 0.214×, A-427 0.351×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A-427 0.219×, C-33 A 0.207×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.542×; ⚠ position not correctable); [[Clofarabine (drug)]] 5 µM in 1 line (SW 1271 0.0514×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.610×** | -4.6 | 0.003 | 24/38 (HEC-1-A, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.650×** | -4.1 | 0.010 | 32/48 (HCT15, A-427, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.746×** | -4.0 | 0.012 | 26/48 (H4, A-427, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.692×** | -3.5 | 0.056 | 28/48 (KATO III, SK-MEL-2, …) | two highest doses | position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | 0.778× | -3.3 | 0.10 | 26/48 (SK-MEL-2, SW480, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | 0.675× | -3.2 | 0.11 | 22/48 (A-427, HCT15, …) | all doses, flat | noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 0.717× | -3.2 | 0.11 | 22/48 (SK-MEL-2, SNU-1, …) | inconsistent across doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 0.708× | -3.1 | 0.13 | 21/48 (A549, A-172, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.733× | -3.0 | 0.17 | 21/48 (HCT15, LS 180, …) | two highest doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, +0.77 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4466. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 32.8 | 11 (8 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 11.8× (z +15.6) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.32× (z +13.0) | — |
| [[LoVo (line)]] | wt | 31.2 | 7 (5 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.04× (z +14.4) | — |
| [[PANC-1 (line)]] | alt | 32.5 | 6 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.90× (z +14.9) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +10.0) | — |
| [[HOP62 (line)]] | alt | 37.9 | 5 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.71× (z +13.8) | — |
| [[KATO III (line)]] | alt | 44.8 | 5 (4 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 9.84× (z +15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +10.8) | — |
| [[AsPC-1 (line)]] | alt | 23.6 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.3× (z +21.9) | — |
| [[HEC-1-A (line)]] | alt | 44.6 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.89× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.301× (z -9.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 32.6 | 4 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 9.09× (z +13.3) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.03× (z +9.4) | — |
| [[SW480 (line)]] | alt | 49.1 | 4 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.79× (z +10.1) | — |
| [[A-172 (line)]] | wt | 30.8 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.56× (z +10.0) | — |
| [[LOX-IMVI (line)]] | wt | 49.3 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.82× (z +10.7) | — |
| [[SW1417 (line)]] | alt | 46.8 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.12× (z +14.4) | — |
| [[A-427 (line)]] | wt | 38.6 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.351× (z -9.9) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 51.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +11.2) ⚠ cell-cycle shift, explains ~88% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +9.2) | — |
| [[A549 (line)]] | wt | 33.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +12.3) ⚠ cell-cycle shift, explains ~88% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.15× (z +10.3) | — |
| [[HS-578T (line)]] | alt | 26.6 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.22× (z +11.6) | — |
| [[HT-29 (line)]] | alt | 43.1 | 2 | 0 | [[Auranofin (drug)]] 5 µM 5.86× (z +11.1) | — |
| [[J82 (line)]] | alt | 57.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.48× (z +11.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 69.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.59× (z +12.1) | [[Adagrasib (drug)]] 0.05 µM 0.542× (z -11.8) ⚠ position not correctable |
| [[Panc 03.27 (line)]] | alt | 29.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.65× (z +15.8) | — |
| [[RKO (line)]] | wt | 62.4 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.42× (z +11.6) | — |
| [[SNU-423 (line)]] | alt | 45.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.07× (z +11.3) | — |
| [[SW 900 (line)]] | alt | 41.0 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.44× (z +9.1) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +8.9) | — |
| [[BT-474 (line)]] | alt | 23.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.76× (z +11.8) | — |
| [[C-33 A (line)]] | alt | 39.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.207× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 51.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +8.9) ⚠ cell-cycle shift, explains ~88% of this change | — |
| [[CFPAC-1 (line)]] | alt | 20.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.24× (z +13.2) | — |
| [[COLO 205 (line)]] | alt | 18.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.02× (z +10.5) | — |
| [[H4 (line)]] | wt | 38.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.214× (z -10.0) ⚠ cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 60.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.244× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 18.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.28× (z +10.6) | — |
| [[Hs 766T (line)]] | wt | 34.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.08× (z +12.7) | — |
| [[hTERT-HPNE (line)]] | wt | 46.9 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.50× (z +9.0) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H1792 (line)]] | alt | 19.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.60× (z +11.0) | — |
| [[NCI-H2030 (line)]] | alt | 29.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.86× (z +12.3) | — |
| [[NCI-H23 (line)]] | alt | 35.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.90× (z +9.1) | — |
| [[NCI-H2347 (line)]] | alt | 43.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.25× (z +11.1) | — |
| [[RPMI-7951 (line)]] | alt | 46.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.04× (z +10.4) | — |
| [[SK-MEL-2 (line)]] | alt | 41.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.09× (z +13.3) | — |
| [[SW 1271 (line)]] | alt | 71.9 | 0 | 1 | — | [[Clofarabine (drug)]] 5 µM 0.0514× (z -9.9) |
| [[SW48 (line)]] | wt | 40.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.86× (z +10.0) | — |
| [[AN3 CA (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4466), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM83D]] | +0.72 | +0.66 / +0.77 | both halves | 7e-06 |  |
| [[SGO2]] | +0.67 | +0.61 / +0.73 | both halves | 7e-06 |  |
| [[PIMREG]] | +0.67 | +0.64 / +0.70 | both halves | 7e-06 | STRING 447 |
| [[FAM72A]] | +0.67 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[CDC25C]] | +0.65 | +0.63 / +0.68 | both halves | 7e-06 | STRING 588 |
| [[TACC3]] | +0.65 | +0.64 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[FAM72D]] | +0.64 | +0.55 / +0.73 | both halves | 1e-05 |  |
| [[PTTG1]] | +0.63 | +0.65 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 888 |
| [[AURKA]] | +0.63 | +0.60 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 804 |
| [[CDCA3]] | +0.62 | +0.63 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 548 |
| [[KPNA2]] | +0.62 | +0.70 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 789 |
| [[HJURP]] | +0.61 | +0.59 / +0.68 | both halves | 7e-06 | STRING 513 |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATAD1]] | -0.55 | -0.38 / -0.54 | both halves | 7e-05 |  |
| [[TYW5]] | -0.53 | -0.38 / -0.57 | both halves | 6e-05 |  |
| [[NBDY]] | -0.52 | -0.33 / -0.59 | both halves | 1e-04 |  |
| [[VPS72]] | -0.51 | -0.38 / -0.52 | both halves | 6e-05 |  |
| [[ZNF502]] | -0.50 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[CHURC1]] | -0.50 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[RRP15]] | -0.50 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[ZSCAN21]] | -0.49 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[PGGT1B]] | -0.49 | -0.38 / -0.55 | both halves | 6e-05 |  |
| [[ZNHIT6]] | -0.49 | -0.39 / -0.51 | both halves | 6e-05 |  |
| [[VPS16]] | -0.49 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[SLC25A46]] | -0.48 | -0.35 / -0.54 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises CKS2's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 1.67× lower at baseline in the lines without PIMREG | 0.018 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers CKS2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NDC80]] | C | NDC80 activity raises CKS2's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 1.83× lower at baseline in the lines without NDC80 | 0.033 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises CKS2's level | lines that do not express AURKB (4) vs lines expressing it (46) | 1.87× lower at baseline in the lines without AURKB | 0.043 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[FAM72D]] | C | FAM72D activity raises CKS2's level | lines that do not express FAM72D (3) vs lines expressing it (47) | 1.82× lower at baseline in the lines without FAM72D | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.564). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-36.5, -58.5); signed map (-52.1, -41.5). **Vector** length 104, 36.0% of its response variance represented; |z| ≥ 3 in 1,217 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cyclin A/B1/B2 associated events during G2/M transition* (reactome, mean cos +0.50 to 12); *spermatogenesis* (hallmark, mean cos +0.50 to 12); *Polo-like kinase mediated events* (reactome, mean cos +0.51 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.1 | +16.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.2 | +9.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +6.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +3.8 | +4.2 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +2.3 |
|  | [[Gefitinib (drug)]] 5 µM |  | +2.7 | +2.8 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | +2.3 | +2.4 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +2.3 | +2.8 |
|  | [[Infigratinib (drug)]] 5 µM |  | +2.1 | +1.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.8 | +2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.2 | -1.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.8 | +0.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.7 | -4.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | +2.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.4 | -1.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | -3.0 | -2.4 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | -2.6 | -1.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -2.3 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | CDC28 protein kinase regulatory subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q22.2 — chr9:89,311,195-89,316,703 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Hallmark sets | G2M_CHECKPOINT, E2F_TARGETS |
| Matched by | ensembl_id |

**Function**, from UniProt [P33552](https://www.uniprot.org/uniprotkb/P33552) (Cyclin-dependent kinases regulatory subunit 2):

> Binds to the catalytic subunit of the cyclin dependent kinases and is essential for their biological function.

**Summary**, from NCBI Gene [1164](https://www.ncbi.nlm.nih.gov/gene/1164):

> CKS2 protein binds to the catalytic subunit of the cyclin dependent kinases and is essential for their biological function. The CKS2 mRNA is found to be expressed in different patterns through the cell cycle in HeLa cells, which reflects specialized role for the encoded protein. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:2000](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2000) · Entrez [1164](https://www.ncbi.nlm.nih.gov/gene/1164) · UniProt [P33552](https://www.uniprot.org/uniprotkb/P33552) · Ensembl [ENSG00000123975](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123975)

## Data

Gene col 4466: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4466); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4466, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4466]; `tensor/DDL_lfc|DDL_z.npy` [4466]; `embed/gene_vectors.npy` [4466]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4466 or target_col == 4466). Every well: [[CKS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CKS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
