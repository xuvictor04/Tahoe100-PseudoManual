---
symbol: "EIF4G3"
type: "gene"
col: 1102
ensembl_id: "ENSG00000075151"
name: "eukaryotic translation initiation factor 4 gamma 3"
location: "1p36.12"
module: 4
arm: "+"
pooled_cpm: 326.82
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 12
n_dd_up_clean: 4
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# EIF4G3

*eukaryotic translation initiation factor 4 gamma 3* — 1p36.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.28× (z +7.6, q 1e-11, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.746× (z -9.2, q 3e-17, down in 36 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HLCS]] (+0.63, fdr 1e-05), [[CDC42BPA]] (+0.61, fdr 1e-05), [[DDX10]] (+0.60, fdr 7e-06); moves opposite to [[LINC00674]] (-0.62, fdr 7e-06), [[IL17RC]] (-0.60, fdr 7e-06), [[FRG1DP]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[LOX]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1102.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +7.6 | 1e-11 | 32/48 (LoVo, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.32×** | +6.1 | 3e-07 | 31/49 (LoVo, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.29×** | +5.7 | 2e-06 | 29/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +5.5 | 5e-06 | 24/48 (CFPAC-1, HS-578T, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.27×** | +5.2 | 3e-05 | 28/48 (COLO 205, NCI-H2347, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.19× | +3.9 | 0.010 | 23/48 (SW480, CFPAC-1, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.18× | +3.6 | 0.022 | 18/49 (H4, MIA PaCa-2, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.36×** | +3.6 | 0.022 | 25/48 (MIA PaCa-2, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Brimonidine (drug)]] 5 µM |  | 1.16× | +3.4 | 0.051 | 13/48 (SW1417, J82, …) | top dose only |  |
| [[Apalutamide (drug)]] 0.5 µM |  | 1.15× | +3.0 | 0.15 | 13/48 (SW48, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 14 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1102.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.746×** | -9.2 | 3e-17 | 36/49 (LOX-IMVI, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **0.750×** | -6.4 | 4e-08 | 34/48 (PANC-1, RKO, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **0.578×** | -6.4 | 4e-08 | 39/49 (RKO, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.739×** | -6.2 | 7e-08 | 28/45 (NCI-H23, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.759×** | -6.1 | 1e-07 | 29/48 (HepG2/C3A, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.760×** | -5.9 | 3e-07 | 27/49 (A-427, LoVo, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.783×** | -5.4 | 4e-06 | 26/48 (KATO III, NCI-H1573, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.784×** | -5.4 | 5e-06 | 25/48 (KATO III, BT-474, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.778×** | -5.4 | 5e-06 | 27/47 (RKO, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.655×** | -4.9 | 5e-05 | 31/47 (SW48, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.862× | -4.7 | 2e-04 | 13/48 (RKO, PANC-1, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.832×** | -3.9 | 0.004 | 25/48 (SW480, HS-578T, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 0.844× | -3.8 | 0.007 | 23/48 (A-427, NCI-H23, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.890× | -3.6 | 0.012 | 19/48 (AsPC-1, NCI-H1573, …) | top dose only | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | 0.847× | -3.5 | 0.015 | 22/47 (LoVo, NCI-H23, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 0.858× | -3.3 | 0.035 | 11/49 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 0.869× | -3.0 | 0.074 | 13/48 (A-427, HEC-1-A, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1102. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 812 | 0 | 15 (14 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.274× (z -21.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.417× (z -14.4) |
| [[KATO III (line)]] | alt | 365 | 0 | 12 (10 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.162× (z -25.7) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.386× (z -13.4) |
| [[LoVo (line)]] | wt | 352 | 2 | 10 (8 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.70× (z +13.7) | [[Homoharringtonine (drug)]] 5 µM 0.571× (z -14.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.635× (z -11.7) |
| [[RKO (line)]] | wt | 617 | 0 | 12 (9 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.313× (z -16.2) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.431× (z -12.3) |
| [[HT-29 (line)]] | alt | 551 | 0 | 10 (10 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.354× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[NCI-H1573 (line)]] | alt | 361 | 0 | 10 (9 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.230× (z -23.5) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.261× (z -11.2) |
| [[PANC-1 (line)]] | alt | 561 | 1 (1 ⚠) | 8 (7 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 1.68× (z +10.2) ⚠ unreliable plate only | [[Digitoxin (drug)]] 5 µM 0.401× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.598× (z -14.3) |
| [[HepG2_C3A (line)]] | wt | 541 | 0 | 6 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.175× (z -25.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.485× (z -10.6) |
| [[NCI-H460 (line)]] | wt | 299 | 0 | 6 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.425× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[BT-474 (line)]] | alt | 273 | 0 | 5 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.229× (z -18.9) ⚠ cell-cycle shift, explains ~38% of this change |
| [[C-33 A (line)]] | alt | 811 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.253× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.409× (z -13.4) |
| [[CFPAC-1 (line)]] | alt | 100 | 5 (3 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 2.11× (z +10.4) | — |
| [[LS 180 (line)]] | wt | 310 | 0 | 5 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.295× (z -13.9) ⚠ cell-cycle shift, explains ~38% of this change |
| [[MIA PaCa-2 (line)]] | alt | 407 | 1 (1 ⚠) | 4 (4 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 1.85× (z +9.9) ⚠ unreliable plate only | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.443× (z -12.6) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 378 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -12.7) |
| [[SW480 (line)]] | alt | 324 | 0 | 5 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.417× (z -16.5) ⚠ cell-cycle shift, explains ~38% of this change |
| [[A-427 (line)]] | wt | 496 | 0 | 4 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.383× (z -17.3) |
| [[LOX-IMVI (line)]] | wt | 473 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.490× (z -14.6) |
| [[SW1417 (line)]] | alt | 204 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -20.9) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 201 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -25.0) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 290 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.636× (z -11.1) |
| [[SK-MEL-2 (line)]] | alt | 288 | 0 | 3 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -12.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.548× (z -8.7) |
| [[SNU-1 (line)]] | wt | 333 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.371× (z -11.5) |
| [[SW48 (line)]] | wt | 309 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.343× (z -9.7) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.361× (z -9.2) |
| [[COLO 205 (line)]] | alt | 350 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -17.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.278× (z -10.1) |
| [[J82 (line)]] | alt | 439 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.595× (z -10.4) |
| [[NCI-H1792 (line)]] | alt | 271 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.06× (z +9.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A-172 (line)]] | wt | 143 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.60× (z +8.9) | — |
| [[HCT15 (line)]] | alt | 423 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.456× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[HS-578T (line)]] | alt | 322 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +9.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H596 (line)]] | alt | 309 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 0.05 µM 0.346× (z -10.5) |
| [[SHP-77 (line)]] | alt | 355 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.459× (z -12.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 221 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +10.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A498 (line)]] | wt | 162 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 185 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 290 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 161 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 207 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 227 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 200 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 261 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 257 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 234 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 316 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 298 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 238 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 311 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 212 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1102), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HLCS]] | +0.63 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[CDC42BPA]] | +0.61 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[DDX10]] | +0.60 | +0.61 / +0.61 | both halves | 7e-06 | STRING 416 |
| [[PKP4]] | +0.60 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[MTAP]] | +0.59 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[ENOX2]] | +0.59 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[TXNRD1]] | +0.59 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[SMARCA4]] | +0.58 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[BICD1]] | +0.58 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[NUTM2B-AS1]] | +0.58 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[SERBP1]] | +0.57 | +0.58 / +0.62 | both halves | 8e-06 |  |
| [[GNL3L]] | +0.57 | +0.61 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00674]] | -0.62 | -0.58 / -0.62 | both halves | 7e-06 |  |
| [[IL17RC]] | -0.60 | -0.60 / -0.58 | both halves | 7e-06 |  |
| [[FRG1DP]] | -0.59 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[MBIP]] | -0.58 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[FRG1JP]] | -0.58 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[MMUT]] | -0.58 | -0.60 / -0.57 | both halves | 9e-06 |  |
| [[ANG]] | -0.57 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[C12orf76]] | -0.55 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[HSPB11]] | -0.55 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[ZNF836]] | -0.55 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[COPS4]] | -0.55 | -0.62 / -0.45 | both halves | 3e-05 |  |
| [[TCTN2]] | -0.54 | -0.46 / -0.59 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LOX]] | B | LOX activity weakens EIF4G3's drug response | lines that do not express LOX (31) vs lines expressing it (18) | the lines without LOX respond 1.94× as strongly (z diff -2.09); strongest at Dinaciclib 0.05 µM: 0.62x vs 1.02x (z diff -6.3) | 0.039 | ⚠ within organs, on part of the lines; also absent: C5orf46, RRAD, LINC01411; target measured in part of the lines; artifact flags |
| [[PCED1B]] | B | PCED1B activity lowers EIF4G3's level | lines that do not express PCED1B (11) vs lines expressing it (39) | 1.59× higher at baseline in the lines without PCED1B | 0.057 | ⚠ within organs, on part of the lines; also absent: AMIGO2, CXCL3, PRDM1 |
| [[CEP83]] | C | CEP83's natural level strengthens EIF4G3's drug response | CEP83's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.62, reverse -0.01; direction not clear | 0.082 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[MTHFD1L]] | C | MTHFD1L activity raises EIF4G3's level | lines that do not express MTHFD1L (3) vs lines expressing it (47) | 1.95× lower at baseline in the lines without MTHFD1L | 0.083 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent |
| [[CTSV]] | C | CTSV's natural level weakens EIF4G3's drug response | CTSV's natural level across 43 lines (lineage-adjusted; a glimpse) | r -0.66, reverse -0.14; direction not clear | 0.089 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.471). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-1.3, -32.6); signed map (5.3, -50.3). **Vector** length 143, 53.0% of its response variance represented; |z| ≥ 3 in 1,329 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +9.5 | +5.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +5.9 | +3.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.9 | +5.2 |
|  | [[EX229 (drug)]] 5 µM |  | +4.7 | +3.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.6 | +2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +7.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.0 | -9.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | -5.9 | -6.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -5.7 | -4.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.7 | -6.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.7 | -5.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.4 | -0.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -3.3 | -1.8 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -3.2 | -0.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -3.1 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation initiation factor 4 gamma 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.12 — chr1:20,806,292-21,177,285 (-) |
| Ensembl biotype | protein_coding |
| Also known as | eIF4GII |
| Gene groups (HGNC) | MicroRNA protein coding host genes; MIF4G domain containing proteins |
| Hallmark sets | ALLOGRAFT_REJECTION |
| Reactome | 7 pathways, smallest: ISG15 antiviral mechanism; Dengue Virus Genome Translation and Replication; Antimicrobial mechanism of IFN-stimulated genes |
| Matched by | ensembl_id |

**Function**, from UniProt [O43432](https://www.uniprot.org/uniprotkb/O43432) (Eukaryotic translation initiation factor 4 gamma 3):

> Component of the protein complex eIF4F, which is involved in the recognition of the mRNA cap, ATP-dependent unwinding of 5'-terminal secondary structure and recruitment of mRNA to the ribosome. Functional homolog of EIF4G1.

**Summary**, from NCBI Gene [8672](https://www.ncbi.nlm.nih.gov/gene/8672):

> The protein encoded by this gene is thought to be part of the eIF4F protein complex, which is involved in mRNA cap recognition and transport of mRNAs to the ribosome. Interestingly, a microRNA (miR-520c-3p) has been found that negatively regulates synthesis of the encoded protein, and this leads to a global decrease in protein translation and cell proliferation. Therefore, this protein is a key component of the anti-tumor activity of miR-520c-3p. [provided by RefSeq, May 2016]

**Accessions** — [HGNC:3298](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3298) · Entrez [8672](https://www.ncbi.nlm.nih.gov/gene/8672) · UniProt [O43432](https://www.uniprot.org/uniprotkb/O43432) · Ensembl [ENSG00000075151](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000075151)

## Data

Gene col 1102: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1102); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1102, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1102]; `tensor/DDL_lfc|DDL_z.npy` [1102]; `embed/gene_vectors.npy` [1102]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1102 or target_col == 1102). Every well: [[EIF4G3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF4G3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
