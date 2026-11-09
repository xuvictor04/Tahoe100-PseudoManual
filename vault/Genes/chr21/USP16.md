---
symbol: "USP16"
type: "gene"
col: 7963
ensembl_id: "ENSG00000156256"
name: "ubiquitin specific peptidase 16"
location: "21q21.3"
module: 51
arm: "+"
pooled_cpm: 87.69
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 8
n_dd_up_clean: 11
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# USP16

*ubiquitin specific peptidase 16* — 21q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.25× (z +24.7, q 0e+00, up in 47 of 48 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.19× (z +16.9, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.617× (z -10.4, q 1e-22, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RABL3]] (+0.78, fdr 7e-06), [[LARP7]] (+0.73, fdr 7e-06), [[RBM23]] (+0.73, fdr 7e-06); moves opposite to [[MFSD14CP]] (-0.68, fdr 7e-06), [[RNF4]] (-0.66, fdr 1e-05), [[PIGF]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7963.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.25×** | +24.7 | 0e+00 | 47/48 (LoVo, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.19×** | +16.9 | 0e+00 | 47/48 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.84×** | +13.1 | 5e-37 | 46/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.79×** | +12.5 | 1e-33 | 42/49 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.77×** | +12.3 | 1e-32 | 46/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.79×** | +12.0 | 2e-31 | 43/48 (NCI-H1573, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.67×** | +11.1 | 1e-26 | 43/48 (SW480, C32, …) | rises with dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.39×** | +9.8 | 7e-21 | 43/49 (LoVo, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.56×** | +9.5 | 9e-20 | 43/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.56×** | +9.3 | 1e-18 | 32/44 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.47×** | +8.4 | 3e-15 | 41/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.44×** | +7.9 | 1e-13 | 37/48 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.38×** | +6.9 | 2e-10 | 32/48 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.37×** | +6.8 | 3e-10 | 39/48 (LS 180, LOX-IMVI, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.35×** | +6.2 | 3e-08 | 36/48 (LS 180, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.27×** | +5.2 | 8e-06 | 27/48 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.56×** | +5.0 | 2e-05 | 27/48 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 1.17× | +3.3 | 0.027 | 15/48 (HS-578T, NCI-H1792, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.031 | 16/48 (NCI-H2347, HS-578T, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.21×** | +3.0 | 0.074 | 15/49 (HOP62, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7963.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.617×** | -10.4 | 1e-22 | 44/48 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.733×** | -9.5 | 6e-19 | 34/49 (SHP-77, NCI-H460, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.684×** | -8.2 | 5e-14 | 46/48 (NCI-H1573, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.700×** | -7.7 | 2e-12 | 40/48 (NCI-H1573, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.702×** | -7.6 | 3e-12 | 39/48 (NCI-H1573, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.738×** | -6.5 | 6e-09 | 38/48 (NCI-H1573, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.740×** | -6.3 | 3e-08 | 33/48 (C32, SW480, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.608×** | -5.6 | 1e-06 | 35/49 (LoVo, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.853× | -4.9 | 7e-05 | 19/48 (CHP-212, HS-578T, …) | top dose only | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.880× | -3.9 | 0.005 | 15/48 (H4, A498, …) | rises with dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.844× | -3.7 | 0.013 | 17/48 (SHP-77, NCI-H1573, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.850× | -3.5 | 0.021 | 15/48 (J82, LoVo, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.853× | -3.4 | 0.026 | 13/48 (LoVo, J82, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.857× | -3.2 | 0.055 | 19/47 (SNU-423, SW 900, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7963. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 72.1 | 12 (9 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +17.8) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.81× (z +14.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.600× (z -9.8) |
| [[NCI-H1573 (line)]] | alt | 129 | 6 (4 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +17.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.65× (z +14.0) | [[Belinostat (drug)]] 5 µM 0.415× (z -12.6) |
| [[SW480 (line)]] | alt | 113 | 10 (7 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.71× (z +14.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.22× (z +11.9) | — |
| [[LoVo (line)]] | wt | 96.9 | 7 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +19.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.33× (z +13.0) | [[Belinostat (drug)]] 5 µM 0.576× (z -8.6) |
| [[PANC-1 (line)]] | alt | 63.9 | 6 (5 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +18.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.59× (z +13.2) | [[Belinostat (drug)]] 5 µM 0.514× (z -9.3) |
| [[HOP62 (line)]] | alt | 83.7 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +15.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.35× (z +10.1) | — |
| [[LS 180 (line)]] | wt | 86.0 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +13.3) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.52× (z +10.9) | — |
| [[RKO (line)]] | wt | 95.0 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.60× (z +9.5) | — |
| [[A-172 (line)]] | wt | 72.8 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +19.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.22× (z +13.2) | — |
| [[A-427 (line)]] | wt | 69.1 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +12.6) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.51× (z +9.1) | — |
| [[A498 (line)]] | wt | 92.4 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +17.3) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.00× (z +13.2) | — |
| [[C32 (line)]] | wt | 82.6 | 3 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +15.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.26× (z +12.6) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.349× (z -10.8) |
| [[HEC-1-A (line)]] | alt | 97.4 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +17.3) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.64× (z +14.3) | — |
| [[HS-578T (line)]] | alt | 87.4 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +13.6) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.42× (z +10.2) | — |
| [[LOX-IMVI (line)]] | wt | 103 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +16.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.82× (z +13.4) | — |
| [[NCI-H23 (line)]] | alt | 75.0 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +14.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.46× (z +9.7) | — |
| [[BT-474 (line)]] | alt | 73.5 | 3 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.43× (z +9.8) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 75.9 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +9.4) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[HT-29 (line)]] | alt | 69.4 | 3 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.23× (z +10.3) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 108 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +14.6) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.39× (z +10.6) | — |
| [[NCI-H1792 (line)]] | alt | 85.4 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +15.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.82× (z +10.5) | — |
| [[NCI-H2347 (line)]] | alt | 92.1 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +16.4) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.25× (z +11.9) | — |
| [[SHP-77 (line)]] | alt | 95.2 | 2 (1 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 2.28× (z +9.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.14× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.541× (z -10.2) |
| [[SW48 (line)]] | wt | 91.4 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +12.5) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[A549 (line)]] | wt | 78.2 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +14.3) ⚠ cell-cycle shift, explains ~30% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.562× (z -9.5) |
| [[AsPC-1 (line)]] | alt | 76.7 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +16.3) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[CFPAC-1 (line)]] | alt | 96.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +18.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.14× (z +9.9) | — |
| [[H4 (line)]] | wt | 122 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.30× (z +11.3) | — |
| [[HCT15 (line)]] | alt | 137 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +11.0) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H2030 (line)]] | alt | 64.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +16.4) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.72× (z +10.5) | — |
| [[RPMI-7951 (line)]] | alt | 113 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.63× (z +10.7) | — |
| [[SK-MEL-2 (line)]] | alt | 119 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +10.7) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[SW1417 (line)]] | alt | 114 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +9.8) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[C-33 A (line)]] | alt | 85.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +9.2) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[CHP-212 (line)]] | wt | 88.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.245× (z -12.3) ⚠ cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 103 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +12.2) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[Hs 766T (line)]] | wt | 63.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +11.1) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[J82 (line)]] | alt | 52.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +13.7) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[KATO III (line)]] | alt | 63.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +10.9) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[Panc 03.27 (line)]] | alt | 89.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +8.9) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[SNU-1 (line)]] | wt | 153 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +10.8) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[SNU-423 (line)]] | alt | 91.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +15.9) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[SW 900 (line)]] | alt | 59.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +11.2) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[AN3 CA (line)]] | alt | 117 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 70.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 76.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 92.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 86.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 91.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 62.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7963), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RABL3]] | +0.78 | +0.74 / +0.72 | both halves | 7e-06 |  |
| [[LARP7]] | +0.73 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[RBM23]] | +0.73 | +0.72 / +0.67 | both halves | 7e-06 |  |
| [[ACIN1]] | +0.71 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[COQ7]] | +0.69 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[TRMO]] | +0.68 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[TRMT10A]] | +0.68 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[EPC2]] | +0.67 | +0.75 / +0.53 | both halves | 1e-05 |  |
| [[LZIC]] | +0.66 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[TAF2]] | +0.66 | +0.70 / +0.57 | both halves | 1e-05 |  |
| [[SRRM2]] | +0.66 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[ATRX]] | +0.66 | +0.66 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MFSD14CP]] | -0.68 | -0.68 / -0.59 | both halves | 7e-06 |  |
| [[RNF4]] | -0.66 | -0.65 / -0.56 | both halves | 1e-05 | pathway: HALLMARK_COMPLEMENT |
| [[PIGF]] | -0.65 | -0.65 / -0.52 | both halves | 1e-05 |  |
| [[PRELID1]] | -0.62 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[FBXO31]] | -0.61 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[METAP1]] | -0.61 | -0.66 / -0.45 | both halves | 3e-05 |  |
| [[ZNF250]] | -0.61 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[GLRX5]] | -0.60 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[SLC15A4]] | -0.60 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[LPCAT4]] | -0.59 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[MMS19]] | -0.59 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[DHRS1]] | -0.59 | -0.54 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises USP16's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.701). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-23.9, 10.1); signed map (12.1, -28.5). **Vector** length 100, 31.3% of its response variance represented; |z| ≥ 3 in 1,290 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.9 | +12.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.8 | +16.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +7.6 | +24.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.5 | +9.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.0 | +11.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.4 | +5.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.1 | +0.5 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.9 | -0.6 |
|  | [[Apalutamide (drug)]] 0.5 µM |  | +2.5 | +0.7 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -6.4 | -6.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.6 | +0.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.3 | -10.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.8 | -6.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.7 | +1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.1 | -0.8 |
|  | [[Lopinavir (drug)]] 5 µM |  | -2.3 | -2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.3 | -5.6 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.9 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin specific peptidase 16 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q21.3 — chr21:29,024,629-29,054,488 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Ubp-M |
| Gene groups (HGNC) | Ubiquitin specific peptidases |
| Hallmark sets | COMPLEMENT |
| Reactome | 2 pathways, smallest: Ub-specific processing proteases; Deubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5T5](https://www.uniprot.org/uniprotkb/Q9Y5T5) (Ubiquitin carboxyl-terminal hydrolase 16):

> Specifically deubiquitinates 'Lys-120' of histone H2A (H2AK119Ub), a specific tag for epigenetic transcriptional repression, thereby acting as a coactivator. Deubiquitination of histone H2A is a prerequisite for subsequent phosphorylation at 'Ser-11' of histone H3 (H3S10ph), and is required for chromosome segregation when cells enter into mitosis. In resting B- and T-lymphocytes, phosphorylation by AURKB leads to enhance its activity, thereby maintaining transcription in resting lymphocytes. …

**Summary**, from NCBI Gene [10600](https://www.ncbi.nlm.nih.gov/gene/10600):

> This gene encodes a deubiquitinating enzyme that is phosphorylated at the onset of mitosis and then dephosphorylated at the metaphase/anaphase transition. It can deubiquitinate H2A, one of two major ubiquitinated proteins of chromatin, in vitro and a mutant form of the protein was shown to block cell division. Alternate transcriptional splice variants, encoding different isoforms, have been characterized. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:12614](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12614) · Entrez [10600](https://www.ncbi.nlm.nih.gov/gene/10600) · UniProt [Q9Y5T5](https://www.uniprot.org/uniprotkb/Q9Y5T5) · Ensembl [ENSG00000156256](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156256)

## Data

Gene col 7963: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7963); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7963, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7963]; `tensor/DDL_lfc|DDL_z.npy` [7963]; `embed/gene_vectors.npy` [7963]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7963 or target_col == 7963). Every well: [[USP16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USP16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
