---
symbol: "RALY"
type: "gene"
col: 4701
ensembl_id: "ENSG00000125970"
name: "RALY heterogeneous nuclear ribonucleoprotein"
location: "20q11.22"
module: 109
arm: "+"
pooled_cpm: 231.92
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 9
n_dd_up_clean: 7
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/109"]
generated_by: "tahoemap"
---

# RALY

*RALY heterogeneous nuclear ribonucleoprotein* — 20q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.25× (z +18.3, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 0.712× (z -7.7, q 1e-11, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EGR3]] (+0.68, fdr 7e-06), [[MAPKAPK2]] (+0.65, fdr 8e-06), [[NCKAP5L]] (+0.63, fdr 2e-05); moves opposite to [[RAB11FIP2]] (-0.67, fdr 3e-05), [[RWDD3]] (-0.66, fdr 8e-06), [[MYLK-AS1]] (-0.58, fdr 3e-05).
> It is in [[Module 109]], a single-armed module (immediate early).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TGM2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4701.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.25×** | +18.3 | 0e+00 | 48/48 (NCI-H2030, KATO III, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.01×** | +14.1 | 2e-42 | 47/48 (NCI-H2030, KATO III, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.54×** | +13.7 | 2e-40 | 38/48 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~7% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.79×** | +13.1 | 5e-37 | 47/48 (NCI-H2030, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.99×** | +8.1 | 6e-14 | 39/49 (C32, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.30×** | +5.5 | 3e-06 | 26/45 (LoVo, NCI-H460, …) | inconsistent across doses | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~20% of this change | **1.28×** | +5.3 | 1e-05 | 26/47 (LoVo, NCI-H1573, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.23×** | +4.5 | 6e-04 | 24/48 (NCI-H460, A498, …) | top dose only | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.21×** | +4.3 | 0.001 | 25/48 (C32, SK-MEL-2, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.36×** | +3.6 | 0.019 | 20/48 (MIA PaCa-2, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 1.18× | +3.3 | 0.039 | 22/48 (NCI-H460, NCI-H2030, …) | two highest doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +3.3 | 0.039 | 0/50 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4701.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **0.712×** | -7.7 | 1e-11 | 40/48 (NCI-H23, SW1417, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.735×** | -6.9 | 1e-09 | 35/48 (A-427, HS-578T, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.749×** | -6.3 | 7e-08 | 28/47 (HEC-1-A, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.767×** | -5.8 | 1e-06 | 33/47 (SW480, H4, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.855× | -5.0 | 7e-05 | 20/49 (HEC-1-A, SW1417, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.866× | -4.6 | 4e-04 | 17/48 (NCI-H1573, A-427, …) | rises with dose | low cells (technical?) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.871× | -4.3 | 0.001 | 14/48 (MIA PaCa-2, NCI-H23, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.838× | -4.3 | 0.001 | 23/50 (NCI-H23, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.697×** | -4.3 | 0.001 | 29/47 (MIA PaCa-2, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | 0.876× | -4.2 | 0.001 | 13/48 (A549, A498, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.818×** | -4.2 | 0.001 | 28/48 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.845× | -4.2 | 0.001 | 20/48 (NCI-H23, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.877× | -4.2 | 0.001 | 15/48 (C32, A-427, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.826×** | -4.2 | 0.001 | 26/48 (NCI-H23, A-427, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.832×** | -4.1 | 0.001 | 24/49 (NCI-H23, SW480, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.852× | -3.9 | 0.004 | 21/49 (NCI-H23, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.845× | -3.8 | 0.005 | 22/48 (KATO III, A-427, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.849× | -3.7 | 0.007 | 16/47 (SW480, C32, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.896× | -3.5 | 0.013 | 1/49 (hTERT-HPNE) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4701. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 165 | 15 (10 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +25.3) | — |
| [[SK-MEL-2 (line)]] | alt | 251 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +19.1) | [[Dinaciclib (drug)]] 5 µM 0.527× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 176 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +19.9) | — |
| [[A-427 (line)]] | wt | 207 | 3 | 2 | [[Panobinostat (drug)]] 5 µM 3.36× (z +16.0) | [[Homoharringtonine (drug)]] 0.05 µM 0.452× (z -10.6) |
| [[LoVo (line)]] | wt | 140 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +21.7) | — |
| [[LS 180 (line)]] | wt | 141 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.63× (z +14.6) | — |
| [[NCI-H1573 (line)]] | alt | 201 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +16.4) | — |
| [[NCI-H23 (line)]] | alt | 201 | 2 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.08× (z +10.7) | [[Trametinib (drug)]] 5 µM 0.541× (z -9.3) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.539× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 229 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +17.8) | — |
| [[C32 (line)]] | wt | 173 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +21.1) | — |
| [[HEC-1-A (line)]] | alt | 202 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.25× (z +13.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.591× (z -8.6) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 243 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.69× (z +14.2) | — |
| [[NCI-H2030 (line)]] | alt | 173 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.10× (z +20.5) | — |
| [[Panc 03.27 (line)]] | alt | 303 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +14.2) | — |
| [[A549 (line)]] | wt | 184 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.97× (z +14.0) | — |
| [[AsPC-1 (line)]] | alt | 414 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.24× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.507× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 148 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.21× (z +13.3) | — |
| [[HepG2_C3A (line)]] | wt | 340 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.14× (z +10.7) | — |
| [[KATO III (line)]] | alt | 284 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.27× (z +19.2) | — |
| [[PANC-1 (line)]] | alt | 153 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.68× (z +15.6) | — |
| [[RKO (line)]] | wt | 231 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.58× (z +12.3) | — |
| [[SW 900 (line)]] | alt | 197 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +16.9) | [[Dinaciclib (drug)]] 5 µM 0.437× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 579 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.43× (z +14.0) | — |
| [[SW48 (line)]] | wt | 150 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.86× (z +10.3) | — |
| [[SW480 (line)]] | alt | 290 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.09× (z +18.1) | — |
| [[CFPAC-1 (line)]] | alt | 285 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +15.2) | — |
| [[Hs 766T (line)]] | wt | 401 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.19× (z +8.9) | — |
| [[HS-578T (line)]] | alt | 218 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.39× (z +12.1) | — |
| [[NCI-H1792 (line)]] | alt | 250 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +11.9) | — |
| [[RPMI-7951 (line)]] | alt | 343 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +10.9) | — |
| [[SHP-77 (line)]] | alt | 144 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.28× (z +10.9) | — |
| [[SNU-1 (line)]] | wt | 195 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 4.60× (z +9.2) | — |
| [[A498 (line)]] | wt | 181 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.58× (z +11.0) | — |
| [[COLO 205 (line)]] | alt | 277 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.418× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 176 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +13.1) | — |
| [[hTERT-HPNE (line)]] | wt | 168 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +10.9) | — |
| [[SNU-423 (line)]] | alt | 299 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.20× (z +9.8) | — |
| [[SW 1271 (line)]] | alt | 438 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.82× (z +8.5) | — |
| [[A-172 (line)]] | wt | 178 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 241 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 142 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 188 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 183 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 378 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 358 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 227 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 220 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 229 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 271 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4701), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EGR3]] | +0.68 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[MAPKAPK2]] | +0.65 | +0.64 / +0.58 | both halves | 8e-06 |  |
| [[NCKAP5L]] | +0.63 | +0.66 / +0.48 | both halves | 2e-05 |  |
| [[EGR1]] | +0.63 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[SYAP1]] | +0.61 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[EGR2]] | +0.60 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[TGFB1]] | +0.60 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[ACTN1]] | +0.59 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[VCL]] | +0.58 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[STAU1]] | +0.58 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[IER2]] | +0.58 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[KHDRBS1]] | +0.57 | +0.48 / +0.49 | both halves | 2e-05 | STRING 754 |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB11FIP2]] | -0.67 | -0.72 / -0.46 | both halves | 3e-05 |  |
| [[RWDD3]] | -0.66 | -0.64 / -0.58 | both halves | 8e-06 |  |
| [[MYLK-AS1]] | -0.58 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[RNF146]] | -0.58 | -0.54 / -0.36 | both halves | 1e-04 |  |
| [[MIX23]] | -0.57 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[MACROH2A2]] | -0.57 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[FBXW4]] | -0.56 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[TMEM68]] | -0.56 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[LINC02100]] | -0.56 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[COA6]] | -0.56 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[IWS1]] | -0.55 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[PHC3]] | -0.55 | -0.51 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TGM2]] | B | TGM2 activity raises RALY's level | lines that do not express TGM2 (16) vs lines expressing it (34) | 1.38× lower at baseline in the lines without TGM2 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: CCL20, SAA2, ALDH1A3 |
| [[SLC16A14]] | B | SLC16A14 activity lowers RALY's level | lines that do not express SLC16A14 (16) vs lines expressing it (34) | 1.18× higher at baseline in the lines without SLC16A14 | 0.040 | ⚠ within organs, on part of the lines; also absent: ENSG00000288656, ARHGEF16, NEBL |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 109]] — immediate early; 43 genes; every member is in the + arm (projection on the module's main direction 0.681). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.7, 0.7); signed map (3.3, 28.1). **Vector** length 149, 53.3% of its response variance represented; |z| ≥ 3 in 1,341 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *immediate early* (control, mean cos +0.55 to 9); *NGF-stimulated transcription* (reactome, mean cos +0.53 to 9); *Nuclear Events (kinase and transcription factor activation)* (reactome, mean cos +0.53 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +8.7 | +18.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +8.0 | +14.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +6.7 | +13.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.8 | +3.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +3.4 | +3.3 |
|  | [[Larotrectinib (drug)]] 0.05 µM |  | +2.7 | +2.0 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | +2.7 | +1.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.6 | +2.0 |
|  | [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | +2.6 | +1.4 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -8.3 | -6.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -7.8 | -7.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.2 | -3.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.1 | -6.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -7.0 | -4.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -6.1 | -5.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.0 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -5.7 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | RALY heterogeneous nuclear ribonucleoprotein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.22 — chr20:33,993,646-34,108,308 (+) |
| Ensembl biotype | protein_coding |
| Also known as | P542, HNRPCL2 |
| Gene groups (HGNC) | RNA binding motif containing; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UKM9](https://www.uniprot.org/uniprotkb/Q9UKM9) (RNA-binding protein Raly):

> RNA-binding protein that acts as a transcriptional cofactor for cholesterol biosynthetic genes in the liver. Binds the lipid-responsive non-coding RNA LeXis and is required for LeXis-mediated effect on cholesterogenesis (By similarity). May be a heterogeneous nuclear ribonucleoprotein (hnRNP).

**Summary**, from NCBI Gene [22913](https://www.ncbi.nlm.nih.gov/gene/22913):

> This gene encodes a member of the heterogeneous nuclear ribonucleoprotein (hnRNP) gene family. This protein may play a role in pre-mRNA splicing and in embryonic development. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Sep 2011]

**Accessions** — [HGNC:15921](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15921) · Entrez [22913](https://www.ncbi.nlm.nih.gov/gene/22913) · UniProt [Q9UKM9](https://www.uniprot.org/uniprotkb/Q9UKM9) · Ensembl [ENSG00000125970](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125970)

## Data

Gene col 4701: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4701); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4701, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4701]; `tensor/DDL_lfc|DDL_z.npy` [4701]; `embed/gene_vectors.npy` [4701]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4701 or target_col == 4701). Every well: [[RALY — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RALY.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
