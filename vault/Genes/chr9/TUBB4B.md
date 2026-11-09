---
symbol: "TUBB4B"
type: "gene"
col: 11992
ensembl_id: "ENSG00000188229"
name: "tubulin beta 4B class IVb"
location: "9q34.3"
module: 171
arm: "-"
pooled_cpm: 129.95
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 10
n_dd_up_clean: 5
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 4
tags: ["gene", "module/171"]
generated_by: "tahoemap"
---

# TUBB4B

*tubulin beta 4B class IVb* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.40× (z +13.5, q 7e-39, up in 42 of 48 measured lines) ⚠ cell-cycle shift, explains ~63% of this change. The strongest without an alert is [[Docetaxel (drug)]] 5 µM: 1.96× (z +7.4, q 1e-11, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.283× (z -5.1, q 2e-04, down in 42 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TUBA1C]] (+0.70, fdr 7e-06), [[DYNLL1]] (+0.59, fdr 1e-05), [[MIDN]] (+0.59, fdr 1e-05); moves opposite to [[TMEM183A]] (-0.65, fdr 7e-06), [[MRPS35]] (-0.61, fdr 7e-06), [[CIZ1]] (-0.61, fdr 2e-05).
> It sits in the **-** arm of [[Module 171]] (Sealing of the nuclear envelope (NE) by ESCRT-III).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 4 go from it, the strongest it → [[SGSH]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 15 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11992.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **3.40×** | +13.5 | 7e-39 | 42/48 (AsPC-1, C32, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~50% of this change | **2.92×** | +8.4 | 2e-14 | 48/48 (CFPAC-1, SW1417, …) | all doses, flat | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **2.83×** | +8.1 | 8e-14 | 48/48 (AsPC-1, NCI-H460, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **2.92×** | +8.0 | 1e-13 | 41/48 (NCI-H1573, AsPC-1, …) | rises with dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.67×** | +7.7 | 2e-12 | 37/48 (C32, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 5 µM |  | **1.96×** | +7.4 | 1e-11 | 47/48 (NCI-H2347, C32, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **2.18×** | +6.1 | 9e-08 | 41/48 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **2.17×** | +6.1 | 1e-07 | 41/48 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **2.05×** | +5.6 | 1e-06 | 38/48 (AsPC-1, NCI-H460, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **2.02×** | +5.5 | 2e-06 | 42/48 (AsPC-1, RKO, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.99×** | +5.4 | 4e-06 | 41/48 (SK-MEL-2, C-33 A, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.96×** | +5.2 | 7e-06 | 45/49 (C32, NCI-H2347, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.95×** | +5.2 | 7e-06 | 37/48 (NCI-H460, AsPC-1, …) | rises with dose | position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.95×** | +5.2 | 7e-06 | 46/48 (NCI-H1792, LoVo, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.75×** | +4.2 | 9e-04 | 31/47 (CFPAC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Docetaxel (Trihydrate) (drug)]] 5 µM |  | **1.59×** | +3.5 | 0.017 | 37/48 (NCI-H2347, A549, …) | all doses, flat |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.51×** | +3.2 | 0.042 | 28/49 (NCI-H2030, LOX-IMVI, …) | top dose only | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.46×** | +3.0 | 0.087 | 27/48 (AsPC-1, SW48, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11992.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.283×** | -5.1 | 2e-04 | 42/49 (BT-474, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.645×** | -4.8 | 4e-04 | 38/48 (A-427, CFPAC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.548×** | -4.7 | 5e-04 | 39/48 (HCT15, A-427, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.341×** | -4.4 | 0.002 | 37/48 (BT-474, NCI-H2347, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.626×** | -3.6 | 0.030 | 36/48 (HEC-1-A, A-427, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.641×** | -3.5 | 0.048 | 33/48 (A-427, KATO III, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.598×** | -3.4 | 0.048 | 34/50 (LoVo, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.629×** | -3.3 | 0.056 | 34/48 (LoVo, SW480, …) | inconsistent across doses | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.654×** | -3.3 | 0.056 | 31/48 (HEC-1-A, HCT15, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.737×** | -3.3 | 0.056 | 28/48 (SW480, Hs 766T, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | 0.670× | -3.0 | 0.14 | 27/49 (SNU-423, J82, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.53 per unit of S-phase module lfc, +0.96 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11992. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 107 | 9 (9 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +23.9) ⚠ cell-cycle shift, explains ~63% of this change | — |
| [[NCI-H460 (line)]] | wt | 100 | 7 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.57× (z +15.9) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 4.43× (z +8.9) | — |
| [[C32 (line)]] | wt | 59.4 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 19.2× (z +23.0) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Docetaxel (drug)]] 5 µM 3.21× (z +9.1) | — |
| [[NCI-H1573 (line)]] | alt | 86.2 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.65× (z +19.0) ⚠ cell-cycle shift, explains ~63% of this change | — |
| [[A549 (line)]] | wt | 82.5 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +10.3) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Docetaxel (drug)]] 5 µM 2.68× (z +8.5) | — |
| [[NCI-H1792 (line)]] | alt | 42.1 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.8× (z +20.4) ⚠ cell-cycle shift, explains ~63% of this change | — |
| [[PANC-1 (line)]] | alt | 59.4 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +14.0) ⚠ cell-cycle shift, explains ~63% of this change | — |
| [[SW1417 (line)]] | alt | 152 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +13.8) ⚠ cell-cycle shift, explains ~63% of this change | — |
| [[SW48 (line)]] | wt | 155 | 4 (4 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.49× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | — |
| [[CFPAC-1 (line)]] | alt | 79.7 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.73× (z +14.5) ⚠ cell-cycle shift, explains ~63% of this change | — |
| [[COLO 205 (line)]] | alt | 86.6 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.6× (z +17.9) ⚠ cell-cycle shift, explains ~63% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 68.0 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.98× (z +17.5) ⚠ cell-cycle shift, explains ~63% of this change | — |
| [[LOX-IMVI (line)]] | wt | 84.0 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.77× (z +14.6) ⚠ cell-cycle shift, explains ~63% of this change | — |
| [[A498 (line)]] | wt | 113 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +14.4) ⚠ cell-cycle shift, explains ~63% of this change | — |
| [[RPMI-7951 (line)]] | alt | 74.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.37× (z +15.0) ⚠ cell-cycle shift, explains ~63% of this change | — |
| [[A-172 (line)]] | wt | 253 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.283× (z -8.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 79.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.62× (z +11.2) ⚠ cell-cycle shift, explains ~63% of this change | — |
| [[BT-474 (line)]] | alt | 157 | 0 | 1 | — | [[Neratinib (drug)]] 0.5 µM 0.225× (z -10.5) |
| [[H4 (line)]] | wt | 119 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 60.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +10.1) ⚠ cell-cycle shift, explains ~63% of this change | — |
| [[HOP62 (line)]] | alt | 125 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +10.7) ⚠ cell-cycle shift, explains ~63% of this change | — |
| [[Hs 766T (line)]] | wt | 99.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +11.1) ⚠ cell-cycle shift, explains ~63% of this change | — |
| [[HS-578T (line)]] | alt | 69.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +11.3) ⚠ cell-cycle shift, explains ~63% of this change | — |
| [[KATO III (line)]] | alt | 213 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +8.8) ⚠ cell-cycle shift, explains ~63% of this change | — |
| [[LoVo (line)]] | wt | 137 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +11.4) ⚠ cell-cycle shift, explains ~63% of this change | — |
| [[LS 180 (line)]] | wt | 198 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.153× (z -9.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 137 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +8.9) ⚠ cell-cycle shift, explains ~63% of this change | — |
| [[NCI-H2030 (line)]] | alt | 97.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.48× (z +12.1) ⚠ cell-cycle shift, explains ~63% of this change | — |
| [[NCI-H2347 (line)]] | alt | 173 | 1 | 0 | [[Docetaxel (drug)]] 5 µM 2.72× (z +9.6) | — |
| [[Panc 03.27 (line)]] | alt | 99.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +10.8) ⚠ cell-cycle shift, explains ~63% of this change | — |
| [[RKO (line)]] | wt | 195 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 128 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +8.5) ⚠ cell-cycle shift, explains ~63% of this change | — |
| [[SNU-423 (line)]] | alt | 81.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.79× (z +15.7) ⚠ cell-cycle shift, explains ~63% of this change | — |
| [[SW 1271 (line)]] | alt | 202 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +9.0) ⚠ cell-cycle shift, explains ~63% of this change | — |
| [[SW 900 (line)]] | alt | 95.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.58× (z +12.5) ⚠ cell-cycle shift, explains ~63% of this change | — |
| [[SW480 (line)]] | alt | 196 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.89× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | — |
| [[A-427 (line)]] | wt | 136 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 136 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 46.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 253 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 246 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 236 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 79.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 88.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 57.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 145 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 89.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11992), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*48 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TUBA1C]] | +0.70 | +0.77 / +0.65 | both halves | 7e-06 | pathway: Activation of AMPK downstream of NMDARs; STRING 990 |
| [[DYNLL1]] | +0.59 | +0.56 / +0.61 | both halves | 1e-05 | pathway: AURKA Activation by TPX2; STRING 549 |
| [[MIDN]] | +0.59 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[KIF20B]] | +0.57 | +0.50 / +0.59 | both halves | 1e-05 | pathway: COPI-dependent Golgi-to-ER retrograde traffic |
| [[JPT1]] | +0.57 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[TUBB2A]] | +0.57 | +0.57 / +0.56 | both halves | 1e-05 | same gene group; pathway: Activation of AMPK downstream of NMDARs; STRING 889 |
| [[SGO2]] | +0.57 | +0.49 / +0.61 | both halves | 1e-05 | pathway: EML4 and NUDC in mitotic spindle formation |
| [[PKNOX1]] | +0.57 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[PFN1]] | +0.56 | +0.62 / +0.50 | both halves | 1e-05 | pathway: RHO GTPase Effectors |
| [[SNRPB]] | +0.56 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[HJURP]] | +0.55 | +0.44 / +0.58 | both halves | 3e-05 | pathway: G2/M Transition |
| [[TEDC1]] | +0.54 | +0.49 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*52 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM183A]] | -0.65 | -0.73 / -0.59 | both halves | 7e-06 |  |
| [[MRPS35]] | -0.61 | -0.64 / -0.60 | both halves | 7e-06 |  |
| [[CIZ1]] | -0.61 | -0.47 / -0.65 | both halves | 2e-05 |  |
| [[RPIA]] | -0.59 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[VTI1B]] | -0.59 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[RPS3A]] | -0.58 | -0.51 / -0.59 | both halves | 1e-05 | pathway: Antimicrobial mechanism of IFN-stimulated genes |
| [[SUMO1]] | -0.58 | -0.62 / -0.55 | both halves | 1e-05 | pathway: Antimicrobial mechanism of IFN-stimulated genes |
| [[SCP2]] | -0.58 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[RPL6]] | -0.57 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[SELENOF]] | -0.57 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[STT3A]] | -0.56 | -0.52 / -0.57 | both halves | 1e-05 | pathway: Asparagine N-linked glycosylation |
| [[RPL14]] | -0.56 | -0.54 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SGSH]] | B | TUBB1, [[TUBB2A]], [[TUBB3]], TUBB4A, TUBB4B activity raises SGSH's level | compounds that target TUBB1, TUBB2A, TUBB3, TUBB4A, TUBB4B: 2 of 2 lower it (Docetaxel, Mebendazole) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; shared targets |
| [[MZT1]] | B | TUBB1, [[TUBB2A]], [[TUBB3]], TUBB4A, TUBB4B activity lowers MZT1's level | compounds that target TUBB1, TUBB2A, TUBB3, TUBB4A, TUBB4B: 2 of 2 raise it (Docetaxel, Mebendazole) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[ENSG00000287352]] | B | TUBB1, [[TUBB2A]], [[TUBB3]], TUBB4A, TUBB4B activity lowers ENSG00000287352's level | compounds that target TUBB1, TUBB2A, TUBB3, TUBB4A, TUBB4B: 2 of 2 raise it (Docetaxel, Mebendazole) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[RAB28]] | B | TUBB1, [[TUBB2A]], [[TUBB3]], TUBB4A, TUBB4B activity raises RAB28's level | compounds that target TUBB1, TUBB2A, TUBB3, TUBB4A, TUBB4B: 2 of 2 lower it (Docetaxel, Mebendazole) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

## Where it sits

- **Module**: [[Module 171]] — Sealing of the nuclear envelope (NE) by ESCRT-III; 24 genes; this gene is in the **-** arm (projection on the module's main direction -0.738). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.41).
- **Nodal map** (x, y) = (-9.5, -13.4); signed map (1.1, 24.9). **Vector** length 136, 53.8% of its response variance represented; |z| ≥ 3 in 1,353 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | +6.8 | +13.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | +5.6 | +6.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | +5.5 | +5.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | +5.3 | +8.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | +5.3 | +6.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.2 | +1.5 |
|  | [[Docetaxel (drug)]] 5 µM |  | +2.9 | +7.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.8 | +2.6 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | +2.8 | +1.6 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +2.8 | +1.7 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -11.8 | -1.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -11.6 | -1.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -11.2 | -1.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | -8.5 | -5.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -7.0 | -4.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.3 | -4.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.4 | -3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.0 | -0.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.1 | -0.7 |
|  | [[EX229 (drug)]] 5 µM |  | -2.7 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | tubulin beta 4B class IVb |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.3 — chr9:137,241,287-137,243,707 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Beta2; previously TUBB2C |
| Gene groups (HGNC) | Tubulin beta family |
| Reactome | 94 pathways, smallest: Microtubule-dependent trafficking of connexons from Golgi to the plasma membrane; Transport of connexons to the plasma membrane; Gap junction assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [P68371](https://www.uniprot.org/uniprotkb/P68371) (Tubulin beta-4B chain):

> Tubulin is the major constituent of microtubules, a cylinder consisting of laterally associated linear protofilaments composed of alpha- and beta-tubulin heterodimers. Microtubules grow by the addition of GTP-tubulin dimers to the microtubule end, where a stabilizing cap forms. Below the cap, tubulin dimers are in GDP-bound state, owing to GTPase activity of alpha-tubulin.

**Summary**, from NCBI Gene [10383](https://www.ncbi.nlm.nih.gov/gene/10383):

> Enables double-stranded RNA binding activity. Predicted to be involved in microtubule cytoskeleton organization and mitotic cell cycle. Located in axonemal microtubule. Implicated in Leber congenital amaurosis with early-onset deafness. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20771](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20771) · Entrez [10383](https://www.ncbi.nlm.nih.gov/gene/10383) · UniProt [P68371](https://www.uniprot.org/uniprotkb/P68371) · Ensembl [ENSG00000188229](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188229)

## Data

Gene col 11992: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11992); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11992, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11992]; `tensor/DDL_lfc|DDL_z.npy` [11992]; `embed/gene_vectors.npy` [11992]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11992 or target_col == 11992). Every well: [[TUBB4B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TUBB4B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
