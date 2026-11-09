---
symbol: "SBNO1"
type: "gene"
col: 6336
ensembl_id: "ENSG00000139697"
name: "strawberry notch homolog 1"
location: "12q24.31"
module: 11
arm: "-"
pooled_cpm: 206.59
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 5
n_dd_up_clean: 13
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# SBNO1

*strawberry notch homolog 1* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.97× (z +19.7, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.714× (z -9.4, q 3e-18, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GLG1]] (+0.69, fdr 7e-06), [[ADIPOR1]] (+0.68, fdr 7e-06), [[GMCL1]] (+0.68, fdr 7e-06); moves opposite to [[ZNF620]] (-0.66, fdr 7e-06), [[YTHDC2]] (-0.65, fdr 7e-06), [[ZNF641]] (-0.63, fdr 1e-05).
> It sits in the **-** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[IL15]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6336.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.97×** | +19.7 | 0e+00 | 48/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.86×** | +18.1 | 0e+00 | 47/48 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.83×** | +17.5 | 0e+00 | 46/48 (SHP-77, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.73×** | +16.0 | 0e+00 | 47/48 (SHP-77, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.72×** | +15.8 | 0e+00 | 47/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.62×** | +13.9 | 3e-42 | 46/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.58×** | +13.2 | 4e-38 | 45/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.45×** | +10.8 | 2e-25 | 40/48 (HT-29, C-33 A, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.01×** | +10.6 | 1e-24 | 37/48 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.94×** | +10.1 | 3e-22 | 42/49 (COLO 205, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.24×** | +8.8 | 7e-17 | 24/49 (AsPC-1, NCI-H460, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.34×** | +8.4 | 2e-15 | 37/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.32×** | +8.0 | 7e-14 | 35/48 (HEC-1-A, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.31×** | +7.9 | 1e-13 | 35/48 (A549, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **1.24×** | +6.0 | 8e-08 | 25/47 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.36×** | +4.7 | 8e-05 | 29/49 (SHP-77, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.29×** | +3.8 | 0.004 | 22/48 (NCI-H23, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.13× | +3.4 | 0.015 | 9/48 (PANC-1, Hs 766T, …) | rises with dose |  |
| [[Fluvoxamine (maleate) (drug)]] 5 µM |  | 1.08× | +3.1 | 0.040 | 0/48 | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6336.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.714×** | -9.4 | 3e-18 | 33/48 (HCT15, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.707×** | -9.2 | 1e-17 | 40/48 (A-427, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.789×** | -6.6 | 7e-09 | 32/48 (NCI-H2347, NCI-H1573, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.800×** | -6.5 | 1e-08 | 28/48 (C32, A-427, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.821×** | -5.7 | 1e-06 | 25/48 (A-427, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.848× | -4.6 | 4e-04 | 16/48 (NCI-H23, SW 1088, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.851× | -4.5 | 5e-04 | 20/47 (NCI-H23, NCI-H460, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.899× | -4.3 | 0.001 | 4/48 (NCI-H23, AsPC-1, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.851× | -4.3 | 0.001 | 14/47 (NCI-H23, SNU-423, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.875× | -3.7 | 0.011 | 20/44 (AsPC-1, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.888× | -3.5 | 0.027 | 11/49 (Panc 03.27, SK-MEL-2, …) | inconsistent across doses |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | 0.894× | -3.2 | 0.055 | 6/48 (hTERT-HPNE, KATO III, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.888× | -3.2 | 0.060 | 14/47 (AN3 CA, C32, …) | all doses, stronger at high dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6336. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 194 | 14 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.33× (z +25.2) | — |
| [[SW480 (line)]] | alt | 202 | 12 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.31× (z +17.3) | — |
| [[LS 180 (line)]] | wt | 145 | 9 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.98× (z +20.0) | [[Harringtonine (drug)]] 0.5 µM 0.497× (z -9.3) |
| [[NCI-H1792 (line)]] | alt | 186 | 10 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.76× (z +15.2) | — |
| [[LoVo (line)]] | wt | 190 | 9 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.13× (z +18.8) | — |
| [[PANC-1 (line)]] | alt | 313 | 9 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.13× (z +21.2) | — |
| [[COLO 205 (line)]] | alt | 205 | 8 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.96× (z +17.7) | — |
| [[AsPC-1 (line)]] | alt | 241 | 5 (2 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.32× (z +19.0) | [[Dinaciclib (drug)]] 5 µM 0.428× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.527× (z -9.2) |
| [[KATO III (line)]] | alt | 180 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.04× (z +17.2) | — |
| [[A-172 (line)]] | wt | 108 | 5 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 2.28× (z +11.1) | [[Harringtonine (drug)]] 0.5 µM 0.488× (z -8.8) |
| [[A-427 (line)]] | wt | 353 | 1 | 5 (2 ⚠) | [[Auranofin (drug)]] 5 µM 1.59× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.452× (z -20.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.517× (z -12.2) |
| [[HOP62 (line)]] | alt | 166 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.31× (z +14.6) | — |
| [[HT-29 (line)]] | alt | 196 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.28× (z +14.8) | — |
| [[C-33 A (line)]] | alt | 279 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.18× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.487× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 220 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.14× (z +11.0) | — |
| [[SHP-77 (line)]] | alt | 258 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.69× (z +16.6) | — |
| [[HepG2_C3A (line)]] | wt | 214 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.55× (z +12.4) | — |
| [[Hs 766T (line)]] | wt | 139 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +11.4) | — |
| [[HS-578T (line)]] | alt | 142 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.91× (z +9.5) | — |
| [[NCI-H23 (line)]] | alt | 401 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.81× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.537× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 207 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.42× (z +10.0) | — |
| [[A549 (line)]] | wt | 190 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 1.98× (z +10.3) | — |
| [[CFPAC-1 (line)]] | alt | 166 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.78× (z +9.5) | — |
| [[HCT15 (line)]] | alt | 301 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 1.86× (z +9.5) | [[Harringtonine (drug)]] 5 µM 0.459× (z -11.6) |
| [[HEC-1-A (line)]] | alt | 184 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.29× (z +14.7) | — |
| [[J82 (line)]] | alt | 159 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.45× (z +13.4) | — |
| [[NCI-H1573 (line)]] | alt | 186 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +15.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.77× (z +14.0) | — |
| [[Panc 03.27 (line)]] | alt | 109 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.34× (z +12.6) | — |
| [[SNU-423 (line)]] | alt | 165 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.36× (z +12.6) | — |
| [[SW 900 (line)]] | alt | 223 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.30× (z +13.0) | — |
| [[SW1417 (line)]] | alt | 207 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.44× (z +14.5) | — |
| [[A498 (line)]] | wt | 176 | 2 | 0 | [[Belinostat (drug)]] 5 µM 1.69× (z +8.7) | — |
| [[BT-474 (line)]] | alt | 189 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.13× (z +10.3) | — |
| [[NCI-H2347 (line)]] | alt | 200 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.97× (z +12.1) | — |
| [[SW48 (line)]] | wt | 216 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 2.28× (z +9.2) | [[Harringtonine (drug)]] 0.5 µM 0.424× (z -8.8) |
| [[CHP-212 (line)]] | wt | 259 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.293× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 165 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.46× (z +9.8) | — |
| [[hTERT-HPNE (line)]] | wt | 182 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 1.85× (z +8.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 285 | 1 | 0 | [[Belinostat (drug)]] 5 µM 2.09× (z +9.6) | — |
| [[NCI-H2030 (line)]] | alt | 253 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.72× (z +8.7) | — |
| [[SK-MEL-2 (line)]] | alt | 143 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +11.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[AN3 CA (line)]] | alt | 245 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 178 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 256 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 198 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 201 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 256 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 242 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6336), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLG1]] | +0.69 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[ADIPOR1]] | +0.68 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[GMCL1]] | +0.68 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[MOSPD3]] | +0.66 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[MARK4]] | +0.65 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[AP1S1]] | +0.65 | +0.69 / +0.50 | both halves | 1e-05 | same gene group |
| [[TMED4]] | +0.64 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[KIAA1958]] | +0.62 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[PIBF1]] | +0.62 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[GNB2]] | +0.62 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[IGSF8]] | +0.61 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[SLC35E1]] | +0.61 | +0.62 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF620]] | -0.66 | -0.63 / -0.61 | both halves | 7e-06 |  |
| [[YTHDC2]] | -0.65 | -0.60 / -0.66 | both halves | 7e-06 |  |
| [[ZNF641]] | -0.63 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[SDSL]] | -0.63 | -0.71 / -0.43 | both halves | 3e-05 |  |
| [[FAM169A]] | -0.62 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[ELAC1]] | -0.61 | -0.66 / -0.43 | both halves | 3e-05 |  |
| [[ZXDA]] | -0.61 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[LACC1]] | -0.61 | -0.61 / -0.46 | both halves | 3e-05 |  |
| [[THOC7]] | -0.60 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[GDAP1]] | -0.60 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[ZXDB]] | -0.60 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[LIG4]] | -0.59 | -0.52 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL15]] | B | IL15 activity lowers SBNO1's level | lines that do not express IL15 (10) vs lines expressing it (40) | 1.42× higher at baseline in the lines without IL15 | 0.008 | ⚠ within organs, on part of the lines; also absent: TGFBR2, ITGA3, PSORS1C1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **-** arm (projection on the module's main direction -0.448). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (3.8, -14.4); signed map (-35.2, 14.1). **Vector** length 124, 44.2% of its response variance represented; |z| ≥ 3 in 1,372 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +6.0 | +7.9 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.9 | +16.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.9 | +17.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.7 | +18.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.2 | +8.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +10.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.0 | +4.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.5 | +2.2 |
|  | [[Vilanterol (drug)]] 5 µM |  | +2.4 | +3.0 |
|  | [[Arbutin (drug)]] 5 µM |  | +2.2 | +2.6 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -17.6 | -9.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -15.6 | -9.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -11.1 | -5.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -9.0 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -8.5 | -6.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.6 | -6.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.9 | -3.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.3 | -2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.3 | +3.4 |

## What is on record

|  |  |
|---|---|
| Name | strawberry notch homolog 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:123,289,109-123,364,847 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MOP3, FLJ10701, FLJ10833, Sno |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [A3KN83](https://www.uniprot.org/uniprotkb/A3KN83) (Protein strawberry notch homolog 1):

> Plays a crucial role in the regulation of neural stem cells (NSCs) proliferation. Enhances the phosphorylation of GSK3B through the PI3K-Akt signaling pathway, thereby up-regulating the Wnt/beta-catenin signaling pathway and promoting the proliferation of NSCs. Improves ischemic stroke recovery while inhibiting neuroinflammation through small extracellular vesicles (sEVs)-mediated mechanism. Enhances the secretion of sEVs from NSCs, which in turn inhibit both the MAPK and NF-kappaB pathways in …

**Summary**, from NCBI Gene [55206](https://www.ncbi.nlm.nih.gov/gene/55206):

> Predicted to enable chromatin DNA binding activity and histone binding activity. Predicted to be involved in several processes, including negative regulation of neuroinflammatory response; positive regulation of neural precursor cell proliferation; and regulation of signal transduction. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:22973](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22973) · Entrez [55206](https://www.ncbi.nlm.nih.gov/gene/55206) · UniProt [A3KN83](https://www.uniprot.org/uniprotkb/A3KN83) · Ensembl [ENSG00000139697](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139697)

## Data

Gene col 6336: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6336); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6336, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6336]; `tensor/DDL_lfc|DDL_z.npy` [6336]; `embed/gene_vectors.npy` [6336]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6336 or target_col == 6336). Every well: [[SBNO1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SBNO1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
