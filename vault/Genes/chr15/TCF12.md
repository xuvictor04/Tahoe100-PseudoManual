---
symbol: "TCF12"
type: "gene"
col: 6379
ensembl_id: "ENSG00000140262"
name: "transcription factor 12"
location: "15q21.3"
module: 143
arm: "+"
pooled_cpm: 305.25
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 12
n_dd_up_clean: 8
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/143"]
generated_by: "tahoemap"
---

# TCF12

*transcription factor 12* — 15q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.24× (z +5.6, q 2e-05, up in 24 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.420× (z -15.9, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARID1B]] (+0.72, fdr 7e-06), [[FBXL17]] (+0.72, fdr 7e-06), [[ZMYND11]] (+0.69, fdr 7e-06); moves opposite to [[NPRL2]] (-0.67, fdr 1e-05), [[HSPB11]] (-0.67, fdr 1e-05), [[LCMT1]] (-0.64, fdr 1e-05).
> It is in [[Module 143]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6379.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.24×** | +5.6 | 2e-05 | 24/48 (A549, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.31×** | +5.0 | 2e-04 | 32/48 (HT-29, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.29×** | +4.7 | 4e-04 | 30/48 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.27×** | +4.1 | 0.005 | 27/48 (LoVo, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.52×** | +4.0 | 0.008 | 26/49 (LoVo, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.25×** | +3.9 | 0.011 | 30/47 (LOX-IMVI, C32, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.48×** | +3.8 | 0.014 | 30/48 (LoVo, LS 180, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.22×** | +3.6 | 0.021 | 27/48 (H4, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Demeclocycline (drug)]] 5 µM |  | 1.13× | +3.2 | 0.089 | 1/48 (CFPAC-1) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6379.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.420×** | -15.9 | 0e+00 | 48/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.452×** | -14.6 | 1e-45 | 48/48 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.503×** | -12.6 | 2e-34 | 47/48 (SW480, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.652×** | -7.6 | 6e-12 | 32/44 (LoVo, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.622×** | -6.7 | 2e-09 | 39/49 (SNU-1, LoVo, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.721×** | -6.0 | 2e-07 | 42/48 (RPMI-7951, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.731×** | -5.5 | 2e-06 | 34/47 (SW1417, RKO, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.757×** | -5.1 | 2e-05 | 31/48 (NCI-H23, SK-MEL-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.758×** | -4.7 | 1e-04 | 31/45 (C-33 A, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.638×** | -4.3 | 9e-04 | 38/48 (HOP62, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.821×** | -3.6 | 0.015 | 26/48 (SW480, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.826×** | -3.5 | 0.019 | 25/48 (HepG2/C3A, SW480, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.846× | -3.1 | 0.088 | 20/48 (AN3 CA, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6379. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 658 | 4 | 7 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.89× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.381× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.401× (z -16.4) |
| [[SW480 (line)]] | alt | 428 | 2 | 6 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 1.95× (z +9.6) | [[Panobinostat (drug)]] 5 µM 0.204× (z -24.0) |
| [[HT-29 (line)]] | alt | 388 | 3 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +18.2) | [[Panobinostat (drug)]] 0.5 µM 0.293× (z -16.7) |
| [[KATO III (line)]] | alt | 421 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.393× (z -13.5) |
| [[A549 (line)]] | wt | 398 | 2 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +18.6) | [[Panobinostat (drug)]] 0.5 µM 0.407× (z -12.6) |
| [[AN3 CA (line)]] | alt | 573 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.298× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.328× (z -12.1) |
| [[AsPC-1 (line)]] | alt | 202 | 3 | 3 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +13.1) | [[Panobinostat (drug)]] 5 µM 0.300× (z -16.7) |
| [[C-33 A (line)]] | alt | 491 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.366× (z -15.2) |
| [[LOX-IMVI (line)]] | wt | 337 | 1 | 5 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.02× (z +10.4) | [[Panobinostat (drug)]] 0.5 µM 0.362× (z -16.1) |
| [[MIA PaCa-2 (line)]] | alt | 212 | 2 (1 ⚠) | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.65× (z +9.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.57× (z +8.7) | [[Panobinostat (drug)]] 0.5 µM 0.351× (z -14.4) |
| [[NCI-H23 (line)]] | alt | 225 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.437× (z -12.8) |
| [[A498 (line)]] | wt | 242 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +12.4) | [[Panobinostat (drug)]] 5 µM 0.469× (z -12.0) |
| [[NCI-H1792 (line)]] | alt | 359 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.317× (z -17.2) |
| [[PANC-1 (line)]] | alt | 336 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +10.6) | [[Panobinostat (drug)]] 0.5 µM 0.449× (z -12.3) |
| [[RKO (line)]] | wt | 576 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +10.8) | [[Panobinostat (drug)]] 0.5 µM 0.295× (z -16.8) |
| [[SNU-1 (line)]] | wt | 518 | 1 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.534× (z -9.4) |
| [[A-427 (line)]] | wt | 204 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.478× (z -11.6) |
| [[HEC-1-A (line)]] | alt | 325 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.509× (z -11.9) |
| [[HepG2_C3A (line)]] | wt | 370 | 1 | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.24× (z +9.9) | [[Panobinostat (drug)]] 0.5 µM 0.295× (z -15.0) |
| [[NCI-H2030 (line)]] | alt | 313 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.370× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.526× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 164 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +11.7) | [[Panobinostat (drug)]] 0.5 µM 0.438× (z -11.5) |
| [[SK-MEL-2 (line)]] | alt | 261 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.346× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.416× (z -11.4) |
| [[SW1417 (line)]] | alt | 349 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.304× (z -18.3) |
| [[A-172 (line)]] | wt | 211 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.402× (z -11.9) |
| [[HOP62 (line)]] | alt | 206 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.310× (z -14.4) |
| [[J82 (line)]] | alt | 203 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.434× (z -10.6) |
| [[LS 180 (line)]] | wt | 312 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.407× (z -14.7) |
| [[NCI-H460 (line)]] | wt | 299 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.405× (z -13.3) |
| [[Panc 03.27 (line)]] | alt | 335 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.360× (z -13.2) |
| [[RPMI-7951 (line)]] | alt | 358 | 1 (1 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.55× (z +8.5) ⚠ cell-cycle shift, would explain all of this change | [[Docetaxel (drug)]] 0.05 µM 0.457× (z -10.8) ⚠ transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.498× (z -9.6) |
| [[SHP-77 (line)]] | alt | 379 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.410× (z -14.0) |
| [[SNU-423 (line)]] | alt | 192 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.325× (z -14.0) |
| [[SW48 (line)]] | wt | 351 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.359× (z -12.0) |
| [[BT-474 (line)]] | alt | 260 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +11.2) | [[Panobinostat (drug)]] 0.5 µM 0.340× (z -13.2) |
| [[CHP-212 (line)]] | wt | 472 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.297× (z -11.0) |
| [[H4 (line)]] | wt | 257 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.28× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.438× (z -8.5) |
| [[Hs 766T (line)]] | wt | 154 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.345× (z -12.3) |
| [[SW 900 (line)]] | alt | 158 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +9.6) | [[Panobinostat (drug)]] 0.5 µM 0.458× (z -10.1) |
| [[C32 (line)]] | wt | 313 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.543× (z -9.5) |
| [[CFPAC-1 (line)]] | alt | 180 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.94× (z +9.0) | — |
| [[hTERT-HPNE (line)]] | wt | 236 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.490× (z -8.7) |
| [[COLO 205 (line)]] | alt | 295 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 311 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 133 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 219 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 305 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 323 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 361 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 198 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 341 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6379), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARID1B]] | +0.72 | +0.63 / +0.65 | both halves | 7e-06 | pathway: ATP-dependent chromatin remodelers |
| [[FBXL17]] | +0.72 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[ZMYND11]] | +0.69 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[STAG1]] | +0.69 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[GTF3C6]] | +0.68 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[CACNA2D1]] | +0.67 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[ZFX]] | +0.67 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[ZFP91]] | +0.67 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[ATE1]] | +0.66 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[CNTLN]] | +0.66 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[CUX1]] | +0.66 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[ATF7IP]] | +0.65 | +0.68 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPRL2]] | -0.67 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[HSPB11]] | -0.67 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[LCMT1]] | -0.64 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[SDHAP1]] | -0.63 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[NBPF3]] | -0.63 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[INSIG2]] | -0.63 | -0.57 / -0.46 | both halves | 2e-05 |  |
| [[AHDC1]] | -0.63 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[ZNF526]] | -0.62 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[ANKRD37]] | -0.62 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[BET1L]] | -0.62 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[MPG]] | -0.61 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[PPP2R5B]] | -0.61 | -0.44 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises TCF12's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 143]]; 32 genes; every member is in the + arm (projection on the module's main direction 0.818). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-4.0, 7.3); signed map (23.6, -31.9). **Vector** length 134, 51.1% of its response variance represented; |z| ≥ 3 in 1,088 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +8.4 | +4.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +7.3 | -0.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.0 | +2.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +5.8 | -6.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +5.7 | +5.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.1 | +2.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.5 | +3.9 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +4.3 | +1.9 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +3.8 | +2.0 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -7.8 | -15.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -7.6 | -14.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -7.1 | -12.6 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -3.6 | -1.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.6 | -2.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -3.5 | -1.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.0 | -2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | transcription factor 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.3 — chr15:56,918,623-57,299,281 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HEB, HTF4, HsT17266, bHLHb20, p64 |
| Gene groups (HGNC) | Basic helix-loop-helix proteins |
| Reactome | 24 pathways, smallest: TGFBR3 expression; Myogenesis; NGF-stimulated transcription |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99081](https://www.uniprot.org/uniprotkb/Q99081) (Transcription factor 12):

> Transcriptional regulator. Involved in the initiation of neuronal differentiation. Activates transcription by binding to the E box (5'-CANNTG-3') (By similarity). May be involved in the functional network that regulates the development of the GnRH axis.

**Summary**, from NCBI Gene [6938](https://www.ncbi.nlm.nih.gov/gene/6938):

> The protein encoded by this gene is a member of the basic helix-loop-helix (bHLH) E-protein family that recognizes the consensus binding site (E-box) CANNTG. This encoded protein is expressed in many tissues, among them skeletal muscle, thymus, B- and T-cells, and may participate in regulating lineage-specific gene expression through the formation of heterodimers with other bHLH E-proteins. Several alternatively spliced transcript variants of this gene have been described, but the full-length …

**Accessions** — [HGNC:11623](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11623) · Entrez [6938](https://www.ncbi.nlm.nih.gov/gene/6938) · UniProt [Q99081](https://www.uniprot.org/uniprotkb/Q99081) · Ensembl [ENSG00000140262](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140262)

## Data

Gene col 6379: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6379); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6379, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6379]; `tensor/DDL_lfc|DDL_z.npy` [6379]; `embed/gene_vectors.npy` [6379]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6379 or target_col == 6379). Every well: [[TCF12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TCF12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
