---
symbol: "UBA2"
type: "gene"
col: 4728
ensembl_id: "ENSG00000126261"
name: "ubiquitin like modifier activating enzyme 2"
location: "19q13.11"
module: 33
arm: "+"
pooled_cpm: 162.9
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 10
n_dd_up_clean: 10
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# UBA2

*ubiquitin like modifier activating enzyme 2* — 19q13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.12× (z +14.3, q 1e-43, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.819× (z -5.4, q 4e-05, down in 27 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MCMBP]] (+0.60, fdr 1e-05), [[CSE1L]] (+0.60, fdr 1e-05), [[TMEM209]] (+0.59, fdr 1e-05); moves opposite to [[TP53INP2]] (-0.53, fdr 2e-05), [[DAAM1]] (-0.53, fdr 2e-05), [[YPEL5]] (-0.52, fdr 3e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4728.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.12×** | +14.3 | 1e-43 | 44/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.04×** | +13.5 | 3e-39 | 46/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.67×** | +12.9 | 6e-36 | 47/49 (HEC-1-A, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.39×** | +12.1 | 9e-32 | 47/48 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.52×** | +11.3 | 2e-27 | 36/48 (A549, NCI-H460, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.71×** | +10.2 | 1e-22 | 43/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.49×** | +7.3 | 2e-11 | 32/48 (NCI-H460, HOP62, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.46×** | +7.2 | 4e-11 | 40/48 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.95×** | +6.7 | 2e-09 | 33/38 (SW480, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.41×** | +6.6 | 3e-09 | 32/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.37×** | +5.9 | 2e-07 | 36/48 (HT-29, CFPAC-1, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **1.33×** | +5.3 | 7e-06 | 33/47 (LoVo, NCI-H23, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.26×** | +4.4 | 6e-04 | 26/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.25×** | +4.3 | 8e-04 | 28/48 (RPMI-7951, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.32×** | +3.7 | 0.007 | 24/48 (A498, LOX-IMVI, …) | two highest doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **1.23×** | +3.7 | 0.009 | 26/48 (PANC-1, LoVo, …) | all doses, flat |  |
| [[Tomivosertib (drug)]] 5 µM |  | **1.39×** | +3.2 | 0.038 | 18/48 (MIA PaCa-2, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.054 | 17/49 (J82, HOP62, …) | inconsistent across doses |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 1.18× | +3.0 | 0.076 | 13/48 (PANC-1, SW480, …) | top dose only | plate-row cell shift |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.34×** | +2.9 | 0.091 | 16/48 (HT-29, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4728.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.819×** | -5.4 | 4e-05 | 27/49 (RKO, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.771×** | -4.8 | 4e-04 | 30/47 (NCI-H23, A-427, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.783×** | -4.7 | 6e-04 | 26/48 (A-427, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **0.796×** | -4.4 | 0.002 | 28/49 (A-427, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.861× | -3.9 | 0.008 | 13/49 (SW480, HOP62, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.865× | -3.9 | 0.008 | 13/48 (LS 180, HT-29, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.813×** | -3.8 | 0.012 | 24/47 (A-427, HOP62, …) | two highest doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.819×** | -3.7 | 0.017 | 23/48 (A-427, NCI-H23, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.843× | -3.6 | 0.017 | 20/48 (SW480, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.824×** | -3.6 | 0.018 | 24/47 (LoVo, J82, …) | two highest doses | low cells (technical?) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.777×** | -3.4 | 0.028 | 28/48 (LOX-IMVI, CHP-212, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.866× | -3.4 | 0.028 | 13/48 (SW480, SW48, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.839× | -3.4 | 0.030 | 22/50 (NCI-H23, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.781×** | -3.4 | 0.030 | 26/47 (SW48, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 0.843× | -3.3 | 0.040 | 18/48 (A549, CFPAC-1, …) | top dose only |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.726×** | -3.2 | 0.046 | 15/50 (CHP-212, A-427, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4728. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 113 | 12 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +17.5) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.28× (z +13.9) | — |
| [[PANC-1 (line)]] | alt | 235 | 8 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.87× (z +18.5) | — |
| [[SW480 (line)]] | alt | 223 | 7 (3 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.98× (z +17.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.603× (z -11.6) |
| [[HOP62 (line)]] | alt | 241 | 6 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.12× (z +12.1) | — |
| [[RKO (line)]] | wt | 173 | 4 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +11.8) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 4.95× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -16.7) |
| [[BT-474 (line)]] | alt | 133 | 5 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.98× (z +12.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.52× (z +10.5) | — |
| [[H4 (line)]] | wt | 209 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.04× (z +11.0) | — |
| [[HEC-1-A (line)]] | alt | 233 | 3 | 2 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 4.26× (z +12.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.644× (z -10.7) |
| [[LoVo (line)]] | wt | 101 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.52× (z +11.7) | — |
| [[COLO 205 (line)]] | alt | 84.6 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.61× (z +13.3) | — |
| [[KATO III (line)]] | alt | 143 | 4 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.10× (z +10.2) | — |
| [[LS 180 (line)]] | wt | 125 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.69× (z +11.5) | — |
| [[NCI-H1792 (line)]] | alt | 138 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.84× (z +13.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.74× (z +13.6) | — |
| [[Hs 766T (line)]] | wt | 105 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +9.4) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.88× (z +8.9) | — |
| [[HT-29 (line)]] | alt | 185 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.37× (z +10.3) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 4.93× (z +9.9) | — |
| [[NCI-H1573 (line)]] | alt | 91.3 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.26× (z +12.6) | — |
| [[NCI-H23 (line)]] | alt | 161 | 2 (2 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 2.03× (z +9.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.592× (z -10.2) |
| [[SW 900 (line)]] | alt | 153 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +10.9) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.29× (z +8.5) | — |
| [[A549 (line)]] | wt | 281 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +18.0) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.85× (z +10.4) | — |
| [[AsPC-1 (line)]] | alt | 111 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.84× (z +11.6) | — |
| [[J82 (line)]] | alt | 168 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.32× (z +10.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 212 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 5.37× (z +9.9) | — |
| [[NCI-H2030 (line)]] | alt | 175 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +16.2) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +9.5) | — |
| [[A-172 (line)]] | wt | 124 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 4.62× (z +8.8) | — |
| [[A-427 (line)]] | wt | 195 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.418× (z -13.5) |
| [[A498 (line)]] | wt | 167 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.55× (z +8.6) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[C-33 A (line)]] | alt | 207 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.424× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 155 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.379× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 87.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +15.5) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[HCT15 (line)]] | alt | 218 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.558× (z -9.4) |
| [[hTERT-HPNE (line)]] | wt | 88.3 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.74× (z +9.6) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 142 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 2.42× (z +8.8) | — |
| [[Panc 03.27 (line)]] | alt | 130 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +9.8) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[RPMI-7951 (line)]] | alt | 185 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.23× (z +9.1) | — |
| [[SNU-1 (line)]] | wt | 169 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.27× (z +8.9) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 99.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +10.1) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[SW48 (line)]] | wt | 196 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 2.64× (z +8.5) | — |
| [[AN3 CA (line)]] | alt | 183 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 200 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 146 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 131 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 302 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 226 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 85.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 150 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4728), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCMBP]] | +0.60 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[CSE1L]] | +0.60 | +0.49 / +0.71 | both halves | 1e-05 |  |
| [[TMEM209]] | +0.59 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[DHX15]] | +0.59 | +0.59 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 417 |
| [[AHCTF1]] | +0.56 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[TARBP1]] | +0.56 | +0.46 / +0.47 | both halves | 3e-05 |  |
| [[NUP35]] | +0.56 | +0.53 / +0.57 | both halves | 1e-05 | pathway: SUMOylation |
| [[SF3B3]] | +0.55 | +0.48 / +0.62 | both halves | 2e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[USP10]] | +0.55 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[PMS1]] | +0.54 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[ALG6]] | +0.54 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[STX18-AS1]] | +0.54 | +0.36 / +0.49 | both halves | 1e-04 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TP53INP2]] | -0.53 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[DAAM1]] | -0.53 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[YPEL5]] | -0.52 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[MYL6]] | -0.52 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[MIR22HG]] | -0.51 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[CENPT]] | -0.50 | -0.48 / -0.40 | both halves | 4e-05 |  |
| [[SWT1]] | -0.50 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[ATP6V0C]] | -0.49 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[TUBA1A]] | -0.47 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[JUN]] | -0.46 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[GABARAPL1]] | -0.46 | -0.44 / -0.42 | both halves | 4e-05 | STRING 486 |
| [[CLU]] | -0.46 | -0.44 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises UBA2's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.2% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.469). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-23.5, -42.4); signed map (-11.3, -59.6). **Vector** length 82.2, 28.0% of its response variance represented; |z| ≥ 3 in 1,236 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.6 | -1.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.3 | +1.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.2 | +2.5 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +2.6 | +6.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +2.4 | +11.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.0 | +12.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.0 | -1.5 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.8 | -1.6 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +1.8 | +1.9 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.5 | +2.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.5 | +4.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.3 | +0.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -4.1 | +7.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.9 | +14.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.7 | -3.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.4 | -3.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.4 | -0.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.1 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin like modifier activating enzyme 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.11 — chr19:34,428,352-34,471,251 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13058, HRIHFB2115; previously SAE2 |
| Gene groups (HGNC) | Ubiquitin like modifier activating enzymes |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 4 pathways, smallest: SUMO is conjugated to E1 (UBA2:SAE1); SUMO is transferred from E1 to E2 (UBE2I, UBC9); Processing and activation of SUMO |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBT2](https://www.uniprot.org/uniprotkb/Q9UBT2) (SUMO-activating enzyme subunit 2):

> The heterodimer acts as an E1 ligase for SUMO1, SUMO2, SUMO3, and probably SUMO4. It mediates ATP-dependent activation of SUMO proteins followed by formation of a thioester bond between a SUMO protein and a conserved active site cysteine residue on UBA2/SAE2.

**Summary**, from NCBI Gene [10054](https://www.ncbi.nlm.nih.gov/gene/10054):

> Posttranslational modification of proteins by the addition of the small protein SUMO (see SUMO1; MIM 601912), or sumoylation, regulates protein structure and intracellular localization. SAE1 (MIM 613294) and UBA2 form a heterodimer that functions as a SUMO-activating enzyme for the sumoylation of proteins (Okuma et al., 1999 [PubMed 9920803]).[supplied by OMIM, Mar 2010]

**Accessions** — [HGNC:30661](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30661) · Entrez [10054](https://www.ncbi.nlm.nih.gov/gene/10054) · UniProt [Q9UBT2](https://www.uniprot.org/uniprotkb/Q9UBT2) · Ensembl [ENSG00000126261](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126261)

## Data

Gene col 4728: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4728); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4728, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4728]; `tensor/DDL_lfc|DDL_z.npy` [4728]; `embed/gene_vectors.npy` [4728]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4728 or target_col == 4728). Every well: [[UBA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
